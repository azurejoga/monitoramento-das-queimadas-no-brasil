# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ebea91c-03e6-3ba8-ad30-5804893dffb2 | -9.13372 | -40.92102 | 2024-10-30 04:21:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c1a412b5-6314-3e73-9f4a-a9c9626f2803 | -8.74347 | -39.68242 | 2024-10-30 04:21:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0e0387e2-a1cf-37ee-88f5-265439f29faf | -8.53711 | -40.44837 | 2024-10-30 04:21:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd2466fe-1690-31de-9922-5fbfd0da0100 | -8.53637 | -40.45343 | 2024-10-30 04:21:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 19296ebd-3039-325f-80de-c49760387c35 | -14.44523 | -42.13756 | 2024-10-30 04:21:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dee1b4cb-3ff0-322e-a33a-41f64ed07d55 | -12.18277 | -43.09385 | 2024-10-30 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 09192702-ef01-335b-af50-bac8e88faa48 | -11.56433 | -42.18818 | 2024-10-30 04:21:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 71253560-9e21-39a7-8026-bbf7f5a8c50b | -11.56389 | -42.18565 | 2024-10-30 04:21:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1014259f-de7b-3a3a-a0bb-9b67c5bd3b9f | -11.292 | -41.86255 | 2024-10-30 04:21:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4d536001-b79f-34fc-846d-b071ed598585 | -11.29112 | -41.86024 | 2024-10-30 04:21:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6e34fb23-bd7a-3e2a-aba7-93764f8d357e | -11.29046 | -41.86478 | 2024-10-30 04:21:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1a78c7ba-ea6b-319e-b31a-bdd1e504d1ef | -11.28826 | -41.86196 | 2024-10-30 04:21:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eb25625d-4002-38a0-97c0-568ad66114fa | -10.86755 | -42.93612 | 2024-10-30 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1f73b4f0-55cd-30ab-9029-18fba4dd6d2e | -10.86403 | -42.93557 | 2024-10-30 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4c88539a-26d3-38cf-9e66-7e27777f3fb7 | -10.86231 | -42.89834 | 2024-10-30 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eeeed53c-7d1a-3c09-a934-c069603103ad | -13.47794 | -43.25692 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 458300e2-af03-39b3-835e-40f3f26d3fb4 | -13.47735 | -43.26107 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a3b24553-9707-3a2c-9b9c-52318344ebc2 | -13.47518 | -43.25808 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d61fb471-4e83-39eb-ab14-06ebf0887796 | -13.47456 | -43.26223 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f0ac5092-1f31-380e-b9d0-a70a2596e4a1 | -13.57306 | -43.42658 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01b4894b-d024-38e3-abbc-8e0a04b2f138 | -13.56951 | -43.42604 | 2024-10-30 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d7e8036-79cb-38f5-99f9-45b52797668b | -12.20214 | -43.15788 | 2024-10-30 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 08488d1c-2911-3795-9bc3-25f3010cad54 | -13.90114 | -43.35453 | 2024-10-30 04:21:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| becef27c-9094-35d3-83f6-42a373acc278 | -13.89757 | -43.35397 | 2024-10-30 04:21:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7d9d04c6-0cfb-32a8-ba70-96e9b7f543e3 | -13.89553 | -43.35037 | 2024-10-30 04:21:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 477c5e11-d45b-366f-a667-ce7e48ef3727 | -13.89492 | -43.35452 | 2024-10-30 04:21:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cc6fc811-a3dd-3fc7-a6fe-7b9665ca9af9 | -13.89401 | -43.35342 | 2024-10-30 04:21:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 948fff2c-9cb2-3a8c-a76a-8014f7511a91 | -13.89196 | -43.34982 | 2024-10-30 04:21:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ca2d3f9-d02c-3a5b-8970-16cd27f19937 | -13.89103 | -43.34871 | 2024-10-30 04:21:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe2cc2ef-f9d5-36c6-8c75-9fc17326c25d | -13.89044 | -43.35288 | 2024-10-30 04:21:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7713fd15-5d57-31e4-8aaa-4f7f0bd82f3e | -13.87123 | -43.06178 | 2024-10-30 04:21:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fddb89c9-a057-3b13-a818-ebd546022ea3 | -13.86761 | -43.06123 | 2024-10-30 04:21:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| da5ff94b-57f0-32a9-9dd3-a5549350f48e | -13.8485 | -43.37289 | 2024-10-30 04:21:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 502e7f41-4a99-34b5-8da5-6f234d41767c | -13.82401 | -42.35101 | 2024-10-30 04:21:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a5ecd5e8-72e9-3a4e-b75b-960d01e58dcd | -15.30107 | -43.19719 | 2024-10-30 04:21:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 142c121d-92d2-3f22-b4bd-bb292963afa2 | -9.27466 | -43.25563 | 2024-10-30 04:21:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e41afd02-b0f4-3848-833a-9e3c3db83b18 | -9.11067 | -43.18136 | 2024-10-30 04:21:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6cb0282c-6076-3278-942a-1bea222e4ba5 | -8.95475 | -42.97989 | 2024-10-30 04:21:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d60a731f-f1ac-3b24-814a-332190b121ab | -8.95219 | -42.97966 | 2024-10-30 04:21:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8615391c-4965-37d5-8981-2daad5d38d6c | -8.95166 | -42.96001 | 2024-10-30 04:21:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 595c46ba-2288-3a8b-ac0e-e3eab0a537fc | -8.16274 | -42.84261 | 2024-10-30 04:21:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 944d1c03-3682-3a93-a01b-a071addb79ee | -8.31249 | -43.68476 | 2024-10-30 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e655c56-5f5a-3a8b-9cf3-d0fb7346aa39 | -8.27835 | -43.66869 | 2024-10-30 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e40c6b1c-6c12-3973-8949-dcf95a46dd9e | -7.97606 | -43.88519 | 2024-10-30 04:21:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63ac1ee9-44c7-30a3-941f-fcf1445f76b2 | -10.78449 | -44.07549 | 2024-10-30 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1880f55-ce73-3dbe-a18a-b1330c10fdc8 | -10.77779 | -44.09694 | 2024-10-30 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1794ff3a-c6a5-3312-9278-9665f8afe7d0 | -10.4292 | -44.38003 | 2024-10-30 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab53e37c-ef14-3eca-9474-c11bba8ec92b | -10.33172 | -44.0803 | 2024-10-30 04:21:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3197f7f0-344e-3962-aae6-8370535b3c31 | -10.14771 | -44.01902 | 2024-10-30 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35eb1a00-40f0-38e9-bcea-82d366f89a5f | -10.14716 | -44.02264 | 2024-10-30 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d7af036-19da-3cec-a787-b8576f890c95 | -10.14434 | -44.0185 | 2024-10-30 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 966daaf4-8d20-39dd-a2d4-2e2e0e705edd | -10.14042 | -44.02159 | 2024-10-30 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55d14174-1f7b-3487-b95c-e0eedb083e6b | -10.06395 | -43.9236 | 2024-10-30 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4da8e3d8-2680-311d-b3de-3c32158aa5f3 | -9.366 | -43.64561 | 2024-10-30 04:21:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 773131dc-e674-3549-8963-4f690386d577 | -11.51544 | -43.24898 | 2024-10-30 04:21:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b5504aa9-29b0-3183-9cc5-b02b220783eb | -11.51135 | -43.2524 | 2024-10-30 04:21:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a3443d25-83f8-3434-9730-7e431b904436 | -12.34113 | -43.66907 | 2024-10-30 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91d1c80a-c706-3325-bc3a-26d5c4ee9a25 | -12.33766 | -43.66854 | 2024-10-30 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4948792f-4453-3823-a858-5ef42f354bf5 | -12.25383 | -43.54873 | 2024-10-30 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10473938-3acc-3743-b1f4-c388a6f3d9d9 | -12.11536 | -43.91854 | 2024-10-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 131663e7-9fa2-3a27-94f8-1c32c0c2b929 | -11.99165 | -44.43279 | 2024-10-30 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1cea6fc-5946-3854-a52f-57a21fe2d464 | -11.98828 | -44.43225 | 2024-10-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9279cb71-d700-37ff-9310-e444cae00747 | -11.98038 | -44.39353 | 2024-10-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80ae843f-e1c2-3ada-b91d-7a098ef9d2c0 | -11.91074 | -43.81028 | 2024-10-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef5bd8b9-f385-38fe-859c-97926797cbf4 | -11.91018 | -43.81409 | 2024-10-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4837ef0c-7a57-37c7-985d-a0f1f92c89f5 | -11.88389 | -43.82555 | 2024-10-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65d29c14-ad38-31f4-b82b-7449b83c5d5e | -11.88333 | -43.82935 | 2024-10-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 587fd15a-44c0-335e-87b1-ce3c53d22de5 | -11.88046 | -43.82501 | 2024-10-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dfc6d832-cab6-3719-bd0b-4ae722ba5e3c | -11.74264 | -44.32283 | 2024-10-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42df4722-f3c0-3911-93bc-d8c24fc6efa7 | -11.74208 | -44.3265 | 2024-10-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7d9df1f-1f62-327c-a306-67ab2abc3d2c | -11.61901 | -43.90989 | 2024-10-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfa95488-b0f8-3675-9131-3c86f63f2748 | -11.61559 | -43.90935 | 2024-10-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04cd1094-59df-3e70-bf99-affcb1e36c0e | -11.25788 | -43.20783 | 2024-10-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c37d106-d144-37ca-b077-57e19fac3407 | -10.91935 | -43.99454 | 2024-10-30 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3296afb-fe04-3286-9eda-0356d825d5f6 | -10.89085 | -44.40752 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 500a1d44-e4b1-3878-a2b9-816fa3526279 | -10.8875 | -44.40699 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a76f7108-9ffc-375b-a9a2-52593b7ccd9d | -10.86966 | -44.41154 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b504462-6229-3a3d-9f2c-a1310e1f3284 | -10.86686 | -44.40742 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5e4bfe5-1e65-3e97-817a-70a0be3adca9 | -10.8663 | -44.41102 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0dcad35-553b-352d-8065-63b391d73435 | -10.84976 | -44.2716 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a9f3118-62ef-3a86-ac06-1f1598522ea2 | -10.84805 | -44.26023 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52de01eb-1d41-33df-a511-7ea5175f4240 | -10.84468 | -44.2597 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e6bd79d-9d54-33ba-aae3-b6474aaf32a0 | -10.84414 | -44.26332 | 2024-10-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beb6e9d4-d4c3-3584-b8c3-b8c80c874261 | -12.66874 | -43.82439 | 2024-10-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1651fa6-b317-3211-b65d-03f415ba196b | -12.66297 | -43.81557 | 2024-10-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71439e33-7df4-382d-a03f-877da8fe27af | -12.65952 | -43.81504 | 2024-10-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77efd9c4-54ac-3b3f-9e6e-cd50935f1b93 | -12.65895 | -43.81891 | 2024-10-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1346f32-956c-3454-931e-6c9faabbb5b4 | -12.65838 | -43.82278 | 2024-10-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c5b4a82-f95f-391d-976e-d9e1ed824f92 | -12.65663 | -43.81063 | 2024-10-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50c70cc4-24f3-36af-a6c6-877f714a1050 | -12.65606 | -43.8145 | 2024-10-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a192da6e-9fb7-3db0-be95-5621c37ca40b | -12.65549 | -43.81837 | 2024-10-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5ec4749-6844-3786-b74a-7c523f719431 | -12.65492 | -43.82224 | 2024-10-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0391068c-e097-3dcd-a727-7aee6d90ecfe | -12.65204 | -43.81783 | 2024-10-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f770130c-ce50-3cb0-b74d-a7e638818a4e | -12.65147 | -43.8217 | 2024-10-30 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ed4ee79-59c8-30bc-a0dc-75cb33cf0530 | -12.59033 | -44.76114 | 2024-10-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f963255-8ff5-3451-ba13-e56a8badd14c | -12.28509 | -44.25947 | 2024-10-30 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eac0a3e4-06aa-3168-bbbd-c2f57012f794 | -12.28453 | -44.26318 | 2024-10-30 04:21:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bb4db20a-c57a-33ec-a20c-ed14b0a250d0 | -12.2817 | -44.25895 | 2024-10-30 04:21:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5f1d8c31-a80a-33c5-ac1c-618fa063a03b | -13.61094 | -43.98768 | 2024-10-30 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4c24670-6675-33c5-9f9b-566ae2d9becd | -13.46773 | -44.4354 | 2024-10-30 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README49.md)
