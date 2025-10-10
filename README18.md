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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe36a5bc-bcd2-38fe-92b0-b33f527a85d5 | -13.36139 | -47.59881 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d65a229-883c-3434-9bb1-d26dca8559b8 | -14.72842 | -48.36325 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5393ee31-912b-3728-b2f0-60f5cac9def6 | -13.35009 | -47.75083 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7207bf1-2ec6-3ed1-9d0f-2592051df04b | -15.46315 | -48.53823 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e259afae-f7fa-32e4-b83b-06f475abe693 | -14.67888 | -48.06551 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4930ed89-bc59-3fe6-b6fc-b8fc9d483e2f | -17.21102 | -47.65335 | 2025-10-10 03:42:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5fcab14a-d419-375a-8857-8b8d40e0b97c | -15.08921 | -46.60785 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa12ae81-c382-3d7f-9afe-649e0f80ee72 | -15.42608 | -47.99541 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ec8a2bfe-ccf5-3f08-9613-73edb70f007d | -18.74402 | -48.08613 | 2025-10-10 03:42:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 93d9e195-6fce-32ac-9e1c-ec4bd3e6ec37 | -17.08862 | -45.48194 | 2025-10-10 03:42:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2de2297b-e558-38f2-9d7c-ab8265d2613e | -14.6788 | -48.06541 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 803fc6e1-c5a6-3ae4-98d8-8269b7e19631 | -16.25412 | -47.10949 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c247400-3217-3296-b749-ceab106d3d98 | -16.27125 | -47.16043 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2626e301-02f7-3050-b516-f6f7fe58d97b | -14.93076 | -46.7781 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1ff15a3f-03e2-3556-b9fa-391ed194599e | -13.84566 | -45.83518 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d6e15ac7-0a1a-3fd4-aecc-5d47d1da2212 | -17.92831 | -45.03383 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 79428f8b-c92e-392b-95c4-7f99db1761b7 | -14.26775 | -45.91086 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49f43c08-c3e2-3bad-a2b3-c68d36dabc8e | -14.2629 | -45.90564 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c747fa4c-2bfd-333f-b9a0-6b56b25bf4a9 | -14.87545 | -48.24358 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb831acf-80ed-3ab6-9d64-6760c786de41 | -15.73804 | -43.94527 | 2025-10-10 03:42:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1ae575a-2ffb-3af8-8775-73dc3d5b9d9d | -14.92673 | -46.78556 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50818cc9-4a6c-3a6b-8a29-9d523078c061 | -16.32485 | -47.05473 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8946a64-d397-3690-a9a5-e30718a0d039 | -15.57486 | -44.42936 | 2025-10-10 03:42:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7dbe90c3-340d-3ba6-9f73-93d2d4d70feb | -15.28541 | -46.15314 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06832003-a4ff-386d-8785-22b9f1d9eebd | -14.99306 | -47.1992 | 2025-10-10 03:42:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 86261f13-21e6-3823-bd7a-a74236643969 | -17.93677 | -45.01818 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| f20bc1d1-b33c-3cea-80c8-89dd9b503b1e | -17.9306 | -45.02268 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 57050c3d-221a-30b8-b2b3-95866b8ee210 | -14.93684 | -46.7664 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4f581d90-4f8b-3d5c-af02-7c5770494f1d | -13.88088 | -44.24723 | 2025-10-10 03:42:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2764933a-3630-3bcb-b83c-491e69c85fd9 | -15.09378 | -46.60738 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 587413fc-37f0-36bb-a158-ae7a9b4b23e6 | -15.40509 | -48.00089 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fda4412-1e66-3a10-959b-54408fea3772 | -16.29579 | -47.1614 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86e8dc1a-c18e-3409-b53d-42474193fdc2 | -15.42834 | -47.98482 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c7156c3-baa1-32d8-9b8e-868a7de7e082 | -13.35672 | -47.75133 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd239f7b-d656-3cf7-aac0-c4b7eacdeeec | -17.64247 | -44.4323 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 109b4c29-8d67-31de-9b3b-4bfcf5808f4c | -13.35641 | -47.75249 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84b3ed2e-cb63-39f8-9319-a8f71dc0b220 | -14.6839 | -48.07282 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| fb717a08-1ba6-3a2d-9125-0dfd5d46d57e | -15.089 | -46.60113 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d7dedbb-5f1d-327a-af2b-498f05b9c999 | -14.67262 | -48.06293 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00142de4-fe43-343a-be77-7a3f28513180 | -14.42372 | -48.00198 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1cf71412-118b-36c8-9dc4-9d9fb84ac899 | -13.84072 | -45.86011 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0d85b6dd-60f4-31ea-9c93-99c47c57a183 | -13.82524 | -45.78897 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f12e8c7-8b2c-3118-afeb-955ab6a2e10b | -14.44825 | -47.98107 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5007bff7-712d-3a86-ab5b-196487268f40 | -15.37866 | -47.29375 | 2025-10-10 03:42:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1ad91ed-b1c1-3681-8b57-732a38ead2d3 | -15.82101 | -43.78048 | 2025-10-10 03:42:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c8cc6374-f5a0-30ec-8c81-4f9c817a146c | -14.26847 | -45.87876 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2677e3c5-17c9-393e-80cb-361e7781ed57 | -13.35454 | -47.5997 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f223d0a-69ad-3b3b-8c3e-3c0dba095655 | -13.84503 | -45.84098 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f64d87c9-a779-3538-8ade-69ecf535ed86 | -13.29121 | -48.48926 | 2025-10-10 03:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86a7a95f-807c-38f4-b850-07bd3b72568e | -17.93301 | -45.01096 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 70e75070-c4e8-3687-a7ac-23f3153ad256 | -13.31825 | -47.7419 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac1b44cb-7a8d-3307-b3ed-e24494d8e3bc | -15.74415 | -48.99033 | 2025-10-10 03:42:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9d00799-d8c6-30c8-b18d-816d7f0b0177 | -19.83767 | -41.80859 | 2025-10-10 03:42:00 | NPP-375D | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7edba9c6-8bef-33a5-8adb-93a1c80fa869 | -18.09062 | -44.69763 | 2025-10-10 03:42:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e03d0554-5516-37cc-99b5-d3fbd8dda2a3 | -14.87669 | -48.23793 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f1804a45-004b-328c-8eed-6a70336708a2 | -14.84688 | -48.46849 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9caebbe0-94e3-340a-a44e-c789276ae6e7 | -15.41254 | -47.99696 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63051371-4bad-349e-91ca-e8fdda6fce72 | -15.39697 | -48.03868 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b3a9727-a345-3592-a1dc-34376d3de6eb | -14.93468 | -46.75974 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1b72d836-cc5c-3a24-8feb-bb37a863b228 | -14.26576 | -45.91706 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8fd86d60-58e0-3946-91d6-0137d77fc1a6 | -15.57042 | -44.42524 | 2025-10-10 03:42:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 084b2c00-d90a-3521-b09c-38445783813b | -14.68402 | -48.07296 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ec75a352-b9ec-3e21-b26a-b10857ec1db8 | -17.96418 | -44.96071 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23e56cf3-3e2f-366d-afa7-ddd0fe4c6020 | -15.37797 | -47.29575 | 2025-10-10 03:42:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53e3dc18-688c-3d2a-92b6-a1b79ee5d785 | -14.69023 | -48.07465 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b5002602-11b5-370f-89cc-197b17502033 | -13.84163 | -45.85748 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| f836db62-29c6-3268-93a2-cd6931cbf3bb | -13.34864 | -47.75737 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75a3764c-2489-3ab5-baf1-d0a07289d6aa | -14.884 | -48.23541 | 2025-10-10 03:42:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 42b48ba7-75e3-332f-914e-99dbd13ba342 | -14.43378 | -48.01641 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a819a674-9a75-34e1-8df4-d6110fa06ebd | -13.35539 | -47.75728 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebc97030-b847-3f0a-9577-dbd83eef0077 | -18.02009 | -45.01992 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 0462b834-ea25-3ae6-99b0-489d8a43112d | -17.66223 | -44.46023 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e51a4a37-0dad-307b-8dff-5f322239b41f | -17.94377 | -45.03512 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 483cd921-cf03-3077-853a-cd9f84784478 | -14.44113 | -48.01355 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bae6cfb3-3681-307c-badc-8a22c663b5a6 | -15.42419 | -47.98497 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bf34ae6-8a46-3433-a634-a355c2b3a301 | -16.10383 | -40.60342 | 2025-10-10 03:42:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d3c55b1a-f21e-39e9-96c6-750353842ee4 | -13.32223 | -48.47601 | 2025-10-10 03:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddbefede-98a8-323a-a33f-a2a17174e9aa | -14.94435 | -46.77237 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba2a959d-c4d8-3418-a293-d8fcdf8a307d | -14.71245 | -45.17859 | 2025-10-10 03:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fb5f11b-fcf1-349a-9423-a6b90da94d82 | -14.27122 | -45.88971 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3ce793a-9c41-3bb8-950f-6a443a087567 | -14.26711 | -45.88068 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f462e93-f05e-305f-a3ba-ecc5d9b3456d | -14.26857 | -45.90688 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edbe65c0-d699-3515-8e2a-8904902f96c2 | -16.3239 | -47.05915 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12958c25-5d2d-39e4-b574-7fda0cedc534 | -14.97506 | -41.6808 | 2025-10-10 03:42:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b7d96d1a-1718-3a94-bdb3-e0aa56a78fc9 | -14.26692 | -45.91484 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 631a435c-1755-3fbb-a176-e64eca7eb21e | -13.84332 | -45.84929 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| fd920141-2dee-318b-bf23-595bed780af9 | -17.94536 | -45.02733 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 257ed2cb-1f1e-3b84-94e8-f4db41e40951 | -13.26639 | -48.02326 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59574093-5f4f-375d-90e1-0126b6a8e880 | -13.84074 | -45.83008 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c727e9fb-302d-3a6f-94ab-13a74af178d6 | -15.08717 | -46.60978 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31e3baa6-a5ba-39c2-bfcc-6f6596f89239 | -15.73575 | -43.94952 | 2025-10-10 03:42:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56d5a577-ce82-3eb6-abd7-ffaa26dbaaa3 | -16.74251 | -43.97713 | 2025-10-10 03:42:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbf4973f-bebb-3441-ab88-97d4515df430 | -13.84154 | -45.85596 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 37731147-8e9e-37d1-b911-5c73cc06fd74 | -15.39858 | -48.04089 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fac93491-ebb9-3f5e-8a9c-877695b116c4 | -18.53498 | -45.0733 | 2025-10-10 03:42:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bafefb77-deff-3501-9d8d-606bf373232f | -14.87251 | -48.2261 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c535d2d6-a550-35e9-ad4d-75624cd0bd86 | -14.44258 | -47.97645 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd059540-f3b2-3cb7-a7c0-8771006ec77c | -13.3757 | -47.75686 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b334b868-54e0-3504-b5f1-33906e74f69c | -18.63729 | -43.93958 | 2025-10-10 03:42:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94ac23ea-ae22-37b8-877a-b117342515a6 | -13.29675 | -48.49093 | 2025-10-10 03:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README19.md)
