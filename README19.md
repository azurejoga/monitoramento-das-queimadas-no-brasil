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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ceedc48-83e3-3f93-aa19-e9279ab92863 | -4.01036 | -48.04811 | 2025-11-08 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d782170a-d8b2-37c0-808e-ec967a4710a8 | -5.50027 | -47.07967 | 2025-11-08 04:36:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0643c5d4-c713-3744-80d9-a1cd49d6ffdb | -6.12288 | -57.70879 | 2025-11-08 04:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5cc1803-fd79-32e9-bf8c-d7c03bb05edf | -3.52921 | -47.53893 | 2025-11-08 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 49103f7f-ad3c-37cd-a6f5-a07dd7087083 | -3.44365 | -43.16631 | 2025-11-08 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c39ee3b-16f5-3fdf-a9b0-8ca0bd5e2a0e | -4.20701 | -46.40111 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66278fa3-0d68-3b62-b6a5-d71102b80538 | -2.43171 | -48.04114 | 2025-11-08 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31ab5d3c-d1cd-3204-854d-eabfac489cf1 | -3.8339 | -49.82974 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1ee2fba-0e00-3a3e-b540-dac510fb8c57 | -7.55687 | -45.85848 | 2025-11-08 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11bf036e-16f8-38dc-b27b-ad865d86ff34 | -4.87036 | -43.74511 | 2025-11-08 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9314eb44-112e-357b-9c23-c455686fff2b | -4.64494 | -47.9495 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7d89c8e3-8b86-3d80-8722-49d5ec245bd5 | -4.49979 | -45.1356 | 2025-11-08 04:36:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46b20bd6-d7bc-38bc-8b5e-b413c1194914 | -3.25126 | -52.91594 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f00e4691-ec3e-3cfa-9162-7b83855b5c31 | -5.8635 | -44.70695 | 2025-11-08 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ba140a9-bc89-3294-bece-57296f1b6899 | -5.61447 | -41.07978 | 2025-11-08 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9bc6621a-baf6-33f4-8770-75d8f6e433aa | -5.97728 | -44.17737 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0e3d4d1-f666-3906-b284-8ef14c0919a8 | -3.26082 | -45.97972 | 2025-11-08 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57732b26-0dae-37c4-a4d4-8a79da34c3e6 | -7.38137 | -43.53529 | 2025-11-08 04:36:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d5ab8a9-d550-3909-b78d-a5d33f8e975b | -4.81409 | -45.57668 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ff52c51-2edb-33ef-b48e-7f6e82a46919 | -2.21433 | -51.3791 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a1cf87a-929a-3cf4-8e7f-8b999e7dfafd | -4.58817 | -45.99684 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6bbbbbe-5560-3527-bd19-ad0cb2b43621 | -6.26226 | -44.17303 | 2025-11-08 04:36:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ece8657f-859c-3474-9041-72a6e8d2e796 | -4.15422 | -46.81521 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21b107fa-01d7-383b-9d8a-7ebd98b3c807 | -6.67215 | -38.5587 | 2025-11-08 04:36:00 | NPP-375D | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 39a8dd00-ac4f-3ba9-94ec-ac2631f0f57a | -4.98405 | -48.41017 | 2025-11-08 04:36:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 356b4f3a-0568-3940-9ac5-65852aa34570 | -3.09598 | -49.25032 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9958c055-92f1-31c0-9984-7154828b9ad7 | -5.77706 | -40.79528 | 2025-11-08 04:36:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| be979837-14e5-3211-af2a-a65e0ef29cac | -3.39905 | -45.43183 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17fd46cc-41eb-3630-9b96-2c934ab97ad1 | -4.59213 | -45.99372 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 0f242d93-6d41-3d45-a5ad-c53c42f99b57 | -5.01072 | -44.60718 | 2025-11-08 04:36:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce446817-8c9f-37f0-b8b2-bf81a27d7f1d | -8.205 | -46.97791 | 2025-11-08 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a48de2d-2075-3b6c-88de-e4bebcf8a189 | -3.15866 | -45.49642 | 2025-11-08 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6ec49ef-3186-3c59-8f5d-f0742241f77a | -7.55319 | -47.24878 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 132201ef-1b8f-3125-9da3-cb8df19a1f3a | -2.71458 | -47.40669 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 018bcd85-c60f-35be-8a29-179ec33c9998 | -3.58126 | -51.24933 | 2025-11-08 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ab75f349-aeb4-3225-b3f9-a61b4a3b8d45 | -3.14759 | -50.28923 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0d955d2-80ea-3aef-8d4a-b1debcfe9acf | -7.78807 | -48.53038 | 2025-11-08 04:36:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73dcffef-9d08-3c6e-9077-80d1a1559b06 | -4.3572 | -45.84617 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a5d41a7-5a6e-3aca-8664-f52955d7fe50 | -4.05537 | -46.43536 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e98107ba-a4b2-3cdb-90c8-572e2c1891f7 | -4.68855 | -46.40694 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3584a0ab-7555-32e3-bc56-f09d1acccb13 | -3.33719 | -50.20284 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a56934dd-909b-36ba-bc61-a1d8181c3f89 | -3.67403 | -50.03639 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f2e9ece-590e-3749-addf-d184eca913b2 | -4.11502 | -48.00736 | 2025-11-08 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de47cc70-6fc5-3a33-8a5c-92e48ce35837 | -3.85965 | -45.22724 | 2025-11-08 04:36:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06a196df-f5aa-31ce-9267-3a765d9e804c | -3.83742 | -49.83028 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 355a8f23-f675-3f77-8797-6bdfd4cd1de5 | -3.09824 | -49.25844 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0fe9642-891d-3fa9-945c-d1640b464ef4 | -7.31965 | -47.38188 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 267b22b8-2634-3aab-9b2b-44bb67ebe017 | -4.48868 | -55.80404 | 2025-11-08 04:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9460bfa-54b2-3061-8394-c4b9b67ad6e5 | -4.46887 | -45.33335 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdf72d51-cbd1-39dc-a952-2a9cc837eb2e | -6.12725 | -44.09834 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2c0815c-c377-3b27-8446-123ed5ba73c3 | -3.68049 | -50.04154 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab313e86-094a-3521-962f-52092076eb2b | -4.22051 | -48.34725 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c85d6f2f-f224-3e32-ada4-e15c6db4ad91 | -3.25392 | -50.13944 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea1fd23d-23d5-35f6-be47-4169f56b6b7e | -7.53184 | -47.3862 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38a1116a-fcff-3f8d-8b5b-0bc43cfec297 | -3.65821 | -50.27068 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4bbdc4a7-99f0-3a55-b2b7-0d5842201d43 | -3.40589 | -45.43289 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 95713a95-b858-39c5-a766-3dff3152d948 | -2.55161 | -48.39083 | 2025-11-08 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10734353-6e41-327f-932d-ccecaf80ad10 | -4.03696 | -50.44516 | 2025-11-08 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 742234c0-ed9e-30fe-88cc-b0e659774373 | -5.63457 | -43.91525 | 2025-11-08 04:36:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94948888-1f33-3ac6-b46a-bc111565459e | -9.09292 | -44.32278 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2023532-1c9a-3227-b3e8-6e83fb14c785 | -6.18117 | -43.44382 | 2025-11-08 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba0f3309-735b-332e-a165-1e991cea044b | -3.85525 | -47.40268 | 2025-11-08 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fbdff34a-7676-3693-a3c2-6cd7fcc4b74a | -2.19228 | -49.131 | 2025-11-08 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64ef0bda-6a6e-3cb8-a54a-54274a0d3b1e | -6.69818 | -40.77138 | 2025-11-08 04:36:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 856d2c75-416a-3ca0-be21-5a7ccef44031 | -3.32702 | -53.36452 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c96ad83b-1cb2-321a-9467-e2c9f4e9e087 | -3.64138 | -45.88897 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23371f9a-2cc9-3420-b8db-8cfad9b12c5e | -4.29492 | -45.68774 | 2025-11-08 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c396163-22c2-3570-b7bf-91b10bcf0941 | -4.53662 | -45.61486 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63b06b58-3536-3458-a4a3-5543c1ff732a | -4.45 | -46.43888 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e52fe10-8c45-3d90-89fd-0a67c2886b89 | -6.64001 | -44.55111 | 2025-11-08 04:36:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31dc6bdc-1d70-3c2a-affe-476b9afcbf19 | -3.55976 | -50.81055 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5115c71f-5f04-35b4-b25f-09fc82125ee1 | -4.39391 | -45.36031 | 2025-11-08 04:36:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2fc22a46-9d16-32b8-9295-ac9986e9c145 | -4.64881 | -46.87843 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91895762-af55-39fc-af5a-a42885b448ce | -4.79803 | -49.6046 | 2025-11-08 04:36:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06a56efb-d6d2-34aa-8fda-bd1e70df80ae | -4.26808 | -48.55764 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fc11930-73d4-3f9d-b17a-d37e757d0034 | -4.27674 | -46.4045 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5265072-2438-3b6e-a9d7-054fc890a9e2 | -6.11569 | -41.56649 | 2025-11-08 04:36:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0304fa24-e94e-37a9-86a9-1f4c06b770e7 | -3.3132 | -50.12353 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9440921f-0cdc-3804-a245-3f126b671e3d | -2.93429 | -48.7728 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0f3913f-245a-3739-85ca-82df9e1169f1 | -3.09673 | -50.32819 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0dae6444-4fa7-318d-871b-58bab1948548 | -6.32273 | -39.70329 | 2025-11-08 04:36:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ee506592-501d-3a65-bbab-ee9f55bf97fe | -5.37691 | -44.72579 | 2025-11-08 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afe863b0-7bc1-3b0a-b872-0856866fc403 | -2.94705 | -45.17502 | 2025-11-08 04:36:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04c2188b-d6c6-32d7-b40d-266066961bf3 | -4.59053 | -46.475 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0358549c-adaf-3365-acea-81f9014630f7 | -3.41272 | -45.43395 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3de01352-f2de-3e8e-9868-3698cbd98e1e | -3.36493 | -49.51273 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e044fa0f-4c22-34e5-a977-8a4cf8efd2d9 | -2.97387 | -44.58833 | 2025-11-08 04:36:00 | NPP-375D | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51d7a46b-4119-34c9-9e70-5d1e30a849b9 | -4.05871 | -46.43589 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8dcc01e0-3930-3c02-948c-9fdcfd2b9781 | -4.11391 | -48.01432 | 2025-11-08 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4f51c78-594c-3c85-9d57-48de1a067ced | -3.44125 | -43.15646 | 2025-11-08 04:36:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18170202-4623-36dd-ab2f-0a39ad5e7000 | -3.85139 | -47.40561 | 2025-11-08 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f11ae4e0-87d9-3b51-b9af-8815fe70e783 | -4.15809 | -46.81226 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c95daa70-bf9d-32bf-b854-e619fd980c48 | -6.6776 | -38.55945 | 2025-11-08 04:36:00 | NPP-375D | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1658e3ed-d5af-3c87-a484-3a3bf8924487 | -2.69989 | -48.97439 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b160c00d-fe13-339f-8021-bc9db2d99f78 | -3.84311 | -47.41492 | 2025-11-08 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed35e8c2-6d70-3d93-aeb7-8f35b9eabf81 | -3.31678 | -50.1241 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdd9da5e-8ae9-3f48-94c0-4ce96a3fc0ea | -4.47005 | -45.32579 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b1dcc555-4b0f-39ca-8f02-4968f61737b2 | -3.35001 | -53.22678 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3713850-1608-365a-aeb8-d8b8f934cc0b | -3.44054 | -43.16111 | 2025-11-08 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a32c72a-0139-3c4b-b868-708b41e00f41 | -3.06979 | -49.37056 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README20.md)
