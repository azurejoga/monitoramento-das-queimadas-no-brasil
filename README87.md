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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88d2c20f-7659-3a89-aa34-48144f5936fb | -17.18308 | -56.21264 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| b86bc462-6e72-380c-a650-57e22b861ced | -17.18291 | -56.22093 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| dbae684e-8815-32c5-b90b-d28008c9d77e | -17.18255 | -56.19514 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 928d01da-0eee-33f9-bd33-bbd750888992 | -17.18222 | -56.21673 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 2d3fb4d7-2a0a-3cc0-bbfb-a5a9d89d3b1c | -17.18167 | -56.19921 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2a0d7fa1-ee19-3e4e-994f-db0c2f8327ac | -17.18084 | -56.19497 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b5e65361-d808-32a4-b363-bb531119d6e3 | -17.18079 | -56.20327 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8f6ca1d4-d57c-375d-8ac0-41c4decd09ff | -17.17999 | -56.19905 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ea09c7eb-bced-309d-a462-76a7ddca5d6d | -17.1799 | -56.20733 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d5032805-f229-3920-a7a1-cb871f5111d2 | -17.17902 | -56.2114 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| d9bef3ee-9888-3448-bc83-1c048ff6d013 | -17.17827 | -56.2072 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 5b53e1d0-ffbc-37cb-9e1e-eb0b2ca0ff3d | -17.17813 | -56.21548 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 42846410-5692-34e4-8075-cef956b6831e | -17.17742 | -56.21128 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4c2e94c4-f799-3f1d-8cd2-a288123efb71 | -17.17724 | -56.21959 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 43b764cb-272d-3d46-842c-f66ede938607 | -17.17656 | -56.21537 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 3818da32-a46e-335e-b242-dbcfe95cf923 | -17.17634 | -56.22371 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7c2c3096-c1e4-371e-a111-161fb806302d | -17.17569 | -56.21949 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5ff5b4cf-2cf7-3cd0-8b39-32a5db636965 | -17.17544 | -56.22786 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2b789546-32d9-37c1-984f-3ca6e695548d | -17.17482 | -56.22363 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 86be3de7-8a42-3863-8080-876ad8e0324a | -17.17366 | -56.23606 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5bf00f20-2549-3a91-95e9-3561951dff8f | -17.17347 | -56.20179 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4e8c7db4-1223-3bf8-a03c-c4ba69842eeb | -17.17261 | -56.20586 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dd9a12bb-2054-3ebd-a696-c94d6f9e887e | -17.17175 | -56.20993 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f3979cf4-ee57-311c-a3cd-6357e21a4189 | -17.17089 | -56.21401 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8a886b11-53b1-38d7-9435-1d1c65c5dd14 | -17.17002 | -56.21815 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e931ad44-1532-3ad5-9350-f88ef380768e | -17.16953 | -56.19228 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e3c80307-3a74-31e8-b452-dcb38847333f | -17.16915 | -56.22229 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a3d5216a-c6ea-3a9d-85e1-ef589d701d7f | -17.16867 | -56.19635 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9f445c88-5532-3ccb-92cd-d5f9a1b6628b | -17.16829 | -56.22642 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 90bb2c09-0e43-3cb7-a58f-1f4c0585a46d | -17.16781 | -56.20043 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 15bd2648-08cc-3659-b2d3-898244679b27 | -17.16695 | -56.2045 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1ae3aa3c-e2d3-3607-8299-70000f911a42 | -17.16609 | -56.20859 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1c020ebf-2e5a-3dfc-9fac-acf5f11edb90 | -17.16522 | -56.21269 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1d07bb79-4544-3ee7-9a13-6b5f1da52a43 | -17.16435 | -56.21682 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e86c12d0-cfed-392b-bda8-3ccecdc9af5d | -17.16387 | -56.19093 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8be0f1cb-e412-3215-beb4-debbabbf6911 | -17.16348 | -56.22096 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 28212896-2e80-319b-901e-d77ded8044a9 | -17.16301 | -56.19503 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d44d3082-7929-375e-8016-5bd3f72f053a | -17.16215 | -56.19908 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a20a5937-c85b-331b-89e0-ebb7f7c2dba1 | -17.1613 | -56.20313 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4c54663f-1798-3921-a14b-a63a9b5bdb11 | -17.16043 | -56.20724 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 28853eb5-a7bc-3187-90e6-e4d7a05c00c3 | -17.15956 | -56.21136 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 51788c80-81fe-3935-8033-624204171536 | -17.15869 | -56.21549 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 34aaac9a-3172-3d6d-bf10-b5aa4ca117d5 | -17.15781 | -56.21961 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b64ba2b0-c44c-35d6-87b9-5fae48ff73ab | -17.15736 | -56.19364 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e20ca6f1-b2b5-32e5-a0a3-1d1d6c163db4 | -17.15695 | -56.22371 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 688f921b-6945-372f-8ed0-e3b610546db8 | -17.1565 | -56.19772 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1ab6e766-1186-3fef-ad7a-20f6d33b5fc4 | -17.15608 | -56.22781 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| de31055f-0046-344b-a218-99abe708875c | -17.15564 | -56.20178 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d0158945-dd6b-3553-b2bb-f2c77ed1211e | -17.15477 | -56.20589 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| f3b92fbe-3aca-358c-a2f4-786efe1765e7 | -17.15389 | -56.21002 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 29c66cd7-c6d2-3e35-98e8-7ab42625e528 | -17.15302 | -56.21415 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0ad6b554-6048-3b40-a39d-b169260f01a1 | -17.15215 | -56.21827 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9ae0858f-eae6-30ac-b1fa-9034c45928e7 | -17.1517 | -56.19227 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 00b482c4-5137-3ee0-8c80-038a8233ba42 | -17.15128 | -56.22237 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 00c2d673-1008-37ea-93e3-d9582cc17888 | -17.15083 | -56.19638 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 56b9406c-de1c-389f-ab6e-c4babda95a38 | -17.15041 | -56.22646 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 81f02199-eab9-3a22-81a8-1f7f188a65b2 | -17.14997 | -56.20047 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b1830631-52f3-37a7-b287-7cfee55495e3 | -17.1491 | -56.20458 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| efe3e7e3-403f-3568-920b-db3fae227d16 | -17.14822 | -56.20869 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3508aaa6-33c8-3185-9671-e33b76db4216 | -17.14735 | -56.21281 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4ce3b21d-3bf7-3210-b6b2-2df302806951 | -17.14648 | -56.21692 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9db3612d-5570-31e8-a07c-92cef3164d3b | -17.14605 | -56.19093 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 38eae1e9-8af8-365e-b9ab-5ecf88f09556 | -17.14517 | -56.19505 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 623440f5-bf21-38b0-9954-6d1f7bc754cc | -17.1443 | -56.19915 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 25e01e14-8588-3531-8207-6c10520c516c | -17.14343 | -56.20325 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f51e72e1-cd90-3d48-94f9-86282f17069a | -17.14256 | -56.20735 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 2970d85d-0c0a-3a38-8a88-74f96fd8927b | -17.14169 | -56.21146 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 65b78a67-df61-3235-a503-5a3c64ede59a | -17.14081 | -56.21556 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d60cf436-0285-3be0-b2c4-23d981f21010 | -17.13952 | -56.19366 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 97496089-2e35-3e7f-b026-aa4e968ac7d6 | -17.13865 | -56.19776 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f67bc349-0006-3580-9ad1-97b5d9fe0f76 | -17.13515 | -56.2142 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ceacddc4-732f-3f1e-8f73-c8da12cdbd04 | -17.13386 | -56.1923 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7f2c3187-9702-357d-8f25-df2c9a67b2b0 | -17.10669 | -56.40411 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d4ffdef4-e534-3d8c-a6c7-1fcfa48d9590 | -17.08173 | -56.20752 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cfdc07ac-38fb-3455-ab52-32028f9dc735 | -16.84111 | -55.89875 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b80a9cf1-d46e-3e21-9c59-3ac041e5e64a | -16.8386 | -55.89623 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a8017aad-a070-3adf-9b50-3d8f13cbfabc | -16.83779 | -55.90017 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ac1ddde9-6724-3bad-ad8f-5d27008ac1a7 | -16.83553 | -55.89742 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 42759c59-7f81-3a37-8c9b-98f437ff6cf1 | -16.8322 | -55.89882 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9c9cdd65-d335-3505-a002-1bc8a4efcc93 | -16.83139 | -55.90276 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 016a6577-3075-3a8f-b70e-02d492b23eef | -16.81148 | -55.88563 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 219f3c52-1b4a-3619-9237-fd777d1ab22d | -16.80506 | -55.88828 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 76dd9230-e9e2-3e70-9c03-e6f0ada99dd0 | -16.80193 | -55.87514 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ef9af0b0-37f8-3bae-9a7e-f277a88c38b9 | -16.80063 | -55.82529 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 403d4a21-f0a3-3d6c-9ef4-69a71449819f | -16.77545 | -55.77841 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 74f0c1c5-495c-3630-afdb-fb1bfd69299f | -16.77298 | -55.79012 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b6361799-6072-38a8-b23b-35214df62e2f | -16.77133 | -55.79793 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7b8118df-a0b5-3f52-967d-8d347f989b17 | -16.76968 | -55.80574 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ad31c169-d35b-3c29-9eb8-465e65655b3f | -16.76907 | -55.78101 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 5cd90799-aea3-30c9-bfa6-325be7cd5af9 | -16.76742 | -55.78881 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 81c34a27-d0ad-3a0c-b6ec-73ad72fc333f | -16.76659 | -55.79271 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| ca4f0369-89ff-3ea3-be60-3215981a123e | -16.76412 | -55.80441 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| b584f28a-0cdd-32ed-8b48-03b41f4db35e | -16.76329 | -55.80833 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 634d788e-9f16-3ca2-bbf5-914798ce58d2 | -16.76186 | -55.7875 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 7a7c08af-18f0-3a48-99a1-a66a8af4058a | -16.75938 | -55.7992 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| f616cf40-f504-3e21-9dea-79c529406110 | -16.75855 | -55.8031 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 6aad2635-846d-3d9d-8ecb-2995347dbf12 | -16.75713 | -55.78227 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 160b070c-6fba-3cd1-85db-ab580b6f434c | -16.75689 | -55.81094 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9c5d8462-da52-3e43-8eea-4bb63c33411b | -16.75298 | -55.80181 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ca6ac5e4-a022-35d3-b276-143db0e9fea9 | -16.75277 | -55.7868 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README88.md)
