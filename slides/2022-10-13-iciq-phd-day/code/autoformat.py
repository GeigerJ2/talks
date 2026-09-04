def plotly_to_image2(plotly_fig, save_directory, filename, svg=True, png=True, pdf=False, html=True, paper=True):
    if plotly_fig is not None:
        if png is True:
            plotly_fig.write_image(os.path.join(save_directory, filename) + '.png', engine='kaleido')
            print(os.path.join(save_directory, filename))



def plot_energies2(result_dict, error_dict, n_features, show_train=True, show_test=True, set_range=None,
                  reference='metal', metal=None, cv_id=0, which_error='mean', showticklabels=True, y_title='E<sub>ML</sub> / eV', ):
    # Include threshold for deviation somewhere
    # Todo: When doing LOOCV, the excluded metal (group) is not added to the legend.
    try:
        if cv_id is None:
            cv_id = np.argmin(error_dict['rmse_tests'])
        # Todo: Legacy code from trying multivariate regression and/or both different references. `reference` no effect when model previously fit with only one reference. Order is 1) metal, 2) global, 3) 2O
        if reference == 'metal':
            target_id = 0
        else:  # reference == 'global'
            target_id = 1

        # print(len(result_dict['m_train']),
        #       len(result_dict['l_train']),
        #       len(result_dict['y_train']),
        #       len(result_dict['y_train_pred']),)

        train_df = pd.DataFrame({
            'metal': result_dict['m_trains'][cv_id],
            'plot_label': result_dict['l_trains'][cv_id],
            'y_calc': result_dict['y_trains'][cv_id][:, target_id],
            'y_pred': result_dict['y_train_preds'][cv_id][:, target_id],
        })

        test_df = pd.DataFrame({
            'metal': result_dict['m_tests'][cv_id],
            'plot_label': result_dict['l_tests'][cv_id],
            'y_calc': result_dict['y_tests'][cv_id][:, target_id],
            'y_pred': result_dict['y_test_preds'][cv_id][:, target_id],
        })

    except IndexError:
        # Tried to create df with metal and label before and then add y_calc and y_pred with if, but assignment of new
        # columns gives ValueError due to supposed different length (1) of passed array to new df-column
        train_df = pd.DataFrame({
            'metal': result_dict['m_trains'][cv_id],
            'plot_label': result_dict['l_trains'][cv_id],
            'y_calc': result_dict['y_trains'][cv_id],
            'y_pred': result_dict['y_train_preds'][cv_id],
        })

        test_df = pd.DataFrame({
            'metal': result_dict['m_tests'][cv_id],
            'plot_label': result_dict['l_tests'][cv_id],
            'y_calc': result_dict['y_tests'][cv_id],
            'y_pred': result_dict['y_test_preds'][cv_id],
        })

    if metal is not None:
        train_df = train_df.loc[train_df['metal'] == metal]
        test_df = test_df.loc[test_df['metal'] == metal]

    # Plot energies
    ener_fig = go.Figure()

    # Add annotation with R^2 and RMSEs
    if which_error == 'mean':
        _ = ener_fig.add_annotation(
            xanchor='left', yanchor='top',
            xref='paper', yref='paper',
            x=0, y=1,
            align="left",
            text="R<sup>2</sup> = {:.3f} &#177; {:.3f}<br>RMSE = {:.3f} &#177; {:.3f}<br>MAE = {:.3f} &#177; {:.3f}".format(
                np.mean(error_dict['rsquared_tests']), np.std(error_dict['rsquared_tests']),
                np.mean(error_dict['rmse_tests']), np.std(error_dict['rmse_tests']),
                np.mean(error_dict['mae_tests']), np.std(error_dict['mae_tests'])),
            font_size=26, font_family="Arial", showarrow=False,
            bgcolor='rgba(0,0,0,0.1)'
        )
    else:  # elif == 'best'
        _ = ener_fig.add_annotation(
            xanchor='left', yanchor='top',
            xref='paper', yref='paper',
            x=0, y=1,
            align="left",
            text="R<sup>2</sup> = {:.3f} &#177; {:.3f}<br>RMSE = {:.3f} &#177; {:.3f}<br>MAE = {:.3f} &#177; {:.3f}".format(
                np.max(error_dict['rsquared_tests']), np.std(error_dict['rsquared_tests']),
                np.min(error_dict['rmse_tests']), np.std(error_dict['rmse_tests']),
                np.min(error_dict['mae_tests']), np.std(error_dict['mae_tests'])),
            font_size=26, font_family="Arial", showarrow=False,
            bgcolor='rgba(0,0,0,0.1)'
        )

    # Plot energy data points
    test_legend = True
    if show_train is True:
        test_legend = False
        for metal in METALS:
            # Add trace for training data
            metal_train_df = train_df.loc[train_df['metal'] == metal]

            train_plot_text = [
                i + j for i, j in zip(
                    metal_train_df['plot_label'].to_list(),
                    ['<br>Deviation: {}eV'.format(round(dev, 3)) for dev in
                     np.abs(metal_train_df['y_calc'] - metal_train_df['y_pred'])])
            ]
            _ = ener_fig.add_trace(
                go.Scatter(
                    x=metal_train_df['y_calc'],
                    y=metal_train_df['y_pred'],
                    mode='markers', marker=dict(size=8, symbol=0, color=color_dict[metal], opacity=1),
                    hoverinfo='text+x+y',
                    name=metal.title(), text=train_plot_text, legendgroup=metal, showlegend=True,
                ),
            )

    if show_test is True:

        # Add testing data in second loop so that it is on top
        for metal in METALS:
            # Add trace for testing data
            metal_test_df = test_df.loc[test_df['metal'] == metal]

            test_plot_text = [
                i + j for i, j in zip(
                    metal_test_df['plot_label'].to_list(),
                    ['<br>Deviation: {}eV'.format(round(dev, 3)) for dev in
                     np.abs(metal_test_df['y_calc'] - metal_test_df['y_pred'])])
            ]

            _ = ener_fig.add_trace(
                go.Scatter(
                    x=metal_test_df['y_calc'],
                    y=metal_test_df['y_pred'],
                    mode='markers', marker=dict(size=11, symbol='x', color=color_dict[metal], opacity=1,
                                                line=dict(width=0.5, color='rgba(255, 255, 255, 0.5)', ), ),
                    hoverinfo='text+x+y',
                    name=metal.title(), text=test_plot_text, legendgroup=metal, showlegend=test_legend,
                ),
            )

    all_values = train_df['y_calc'].tolist() + train_df['y_pred'].tolist() + \
                 test_df['y_calc'].tolist() + test_df['y_pred'].tolist()
    full_range = [min(all_values), max(all_values)]
    range_ext = (full_range[0] - 0.075*np.ptp(full_range), full_range[1] + 0.075*np.ptp(full_range))

    if set_range is not None:
        range_ext = set_range

    # Update global layout
    ener_layout = go.Layout(
        width=597, height=597,
        font=dict(family='Arial', color='black'),
        margin=dict(l=0, r=0, b=0, t=0, ),
        hoverlabel={'namelength': -1},
        # title=dict(text=plot_title, x=0.5, ),
        paper_bgcolor='white', plot_bgcolor='white',
        legend=dict(xanchor="right", x=1, yanchor="bottom", y=0,
                    bgcolor='rgba(0,0,0,0.1)',  # bordercolor='rgba(0,0,0,0.4)',
                    font_size=26, tracegroupgap=2, ),
        xaxis=dict(
            title_font_size=30, range=range_ext, showticklabels=showticklabels, title='E<sub>DFT</sub> / eV',
            showline=True, linewidth=3, linecolor='black', mirror=True,
            showgrid=False, zeroline=False, gridcolor='rgba(0,0,0,0.3)',
            ticks='outside', tickfont_size=26, tickformat=".1f", tickwidth=3, ticklen=6),
        yaxis=dict(
            title_font_size=30, range=range_ext, showticklabels=showticklabels, title=y_title,
            showline=True, linewidth=3, linecolor='black', mirror=True,
            showgrid=False, zeroline=False, gridcolor='rgba(0,0,0,0.3)',
            ticks='outside', tickfont_size=26, tickformat=".1f", tickwidth=3, ticklen=6),
    )

    _ = ener_fig.update_layout(ener_layout)

    # Add ideal fit line to plot
    _ = ener_fig.add_trace(
        go.Scatter(
            x=range_ext,
            y=range_ext,
            mode='lines', line=dict(color='black', width=2, dash='dash'), hoverinfo='skip', showlegend=False,
        ),
    )

    return ener_fig



for i in range(1):
    # model_evaluation_dfs['rf_forward_kfold'].head(8)
    rf_kfold_features = literal_eval(model_evaluation_dfs['rf_forward_kfold'].iloc[i]['eval_sets'])

    rf_kfold = run_regr(
        df_in=prep_calc_df, ml_model=RandomForestRegressor(**rf_dict),
        ml_features=rf_kfold_features, ml_target=['E_rel_global'],
        cv_type='kfold', n_splits=N_SPLITS,
    )

    rf_kfold_energy_fig = plot_energies2(
        result_dict=rf_kfold['result_dict'], error_dict=rf_kfold['error_dict'],
        reference='global', showticklabels=True, set_range=fig3_range, # show_train=False,
        y_title='E<sub>RF</sub> / eV', n_features=len(rf_kfold_features),
    )

    rf_kfold_energy_fig.show()

    # plotly_to_image2(
    #     plotly_fig=rf_kfold_energy_fig,
    #     save_directory='/media/jgeiger/WAREHOUSE/projects/1_ceria_sac/figs/phd_day',
    #     filename='rf_desc_{:02d}'.format(i)
    #     )
