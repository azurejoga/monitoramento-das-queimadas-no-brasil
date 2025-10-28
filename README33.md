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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 261e4246-0b37-3801-adc1-8defa3873f15 | -11.28537 | -45.5085 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b9abefcf-3796-3f2a-a5f6-61b24e72ab9c | -7.15989 | -47.00145 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4087296-9d9c-347c-883e-46875756f328 | -7.33016 | -42.45399 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42803b69-84f8-3743-8621-31046f3936ad | -6.82284 | -41.20527 | 2025-10-28 04:14:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f5ffd228-1896-3437-9ae3-db5fe90ca464 | -8.14757 | -47.02278 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df800360-fc2b-3296-8c08-ff0209c60941 | -7.88552 | -45.70192 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27200464-4019-3ac8-a251-492de090b09c | -11.19454 | -44.63156 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ebb25d2-4ffd-377a-814f-9394276d46e0 | -6.67386 | -45.42026 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cba7e0e-beef-3a04-aa6a-50bf4e2f6d8d | -7.07763 | -44.9409 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c5597ee-5fe8-3647-9923-72dd9c660ade | -6.88752 | -45.03226 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c83df64-8db8-35c2-a01e-49f4fd80055b | -6.42371 | -42.02581 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f32591ac-11f5-38b7-b25a-bd3cf6e045cd | -7.44834 | -47.16137 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36c54ce4-59b1-3f47-a9ca-918595b25320 | -11.37978 | -48.18605 | 2025-10-28 04:14:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a732bad1-e26a-341c-8419-093b962b8361 | -7.13989 | -47.35821 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bcdbbf41-1859-3a36-bd8c-d95e5861c5aa | -8.69049 | -47.0557 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ea031f9-2f30-3c18-8f78-17d323c14526 | -7.97165 | -46.74648 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 84427708-e19b-3ef2-bf8c-b68b87e49832 | -6.47032 | -43.18991 | 2025-10-28 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54fe6e07-c963-3985-8996-da85c0e92502 | -8.64282 | -45.28191 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e5731462-d0bc-334d-9b17-f6f64ad6e65c | -8.68332 | -47.12189 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80c6f8d4-cc56-33c7-8329-da75dde02cbc | -9.2931 | -45.21761 | 2025-10-28 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4f91a5a-4a3c-36ca-af93-37f3f4602acc | -6.13145 | -42.7016 | 2025-10-28 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c813e860-293b-3821-9b16-94866f8e0df1 | -11.27866 | -45.50739 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 914be3c0-c22f-37c8-8a49-f11dae5a6dd9 | -11.82563 | -44.51479 | 2025-10-28 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63fb1ed5-1c95-3e8a-808a-0cd097f024e6 | -12.62267 | -44.24955 | 2025-10-28 04:14:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25596860-30f2-3320-8f19-ee4a12f8e73b | -8.71131 | -47.97499 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc53a302-51f2-3e71-ac72-99664d191180 | -12.32091 | -46.56585 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce8ef219-a7ca-3f87-9af7-331b1ef400f3 | -9.6267 | -47.71795 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7e64078-7aeb-32e3-818d-5c6b0cf8a7ab | -10.92131 | -50.2757 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a132d08-0d68-3792-bb53-20ecbbca909e | -6.59183 | -42.65088 | 2025-10-28 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0faafd2e-17de-3165-9add-ae83f56e1a30 | -7.9775 | -46.75636 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d65dbbf-b2f2-31c3-8480-62e026296d2f | -5.64752 | -47.64088 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d97e61ee-4bfc-3ba2-8779-0a98e4ddbef7 | -8.16001 | -42.82728 | 2025-10-28 04:14:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 813a30c0-ad44-383f-957a-46576086668c | -10.28736 | -47.23322 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a2e4f284-68e8-3bc8-bccd-fa79c72b8f83 | -10.07083 | -48.20068 | 2025-10-28 04:14:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a04e8ef0-87c5-3b96-9989-371ad04aad7b | -9.46535 | -47.72724 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c506b19-74c0-33b9-8495-b49260dfd0b3 | -7.89499 | -45.68761 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26af9260-a8a3-3e52-8ee7-ae5c73533aed | -8.31823 | -46.83055 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 156b0452-3fd3-31de-89c4-3fcfc1c1a21d | -6.437 | -42.02805 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d92852a3-b96a-37e7-a73d-efe1c4ee9dbc | -11.21716 | -49.76915 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66c53147-0aeb-3ba0-bec0-ec7b6f356fcd | -7.50985 | -46.28809 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21cebeb2-9f73-3d02-b6a9-50e9a9e3b552 | -11.84814 | -47.91973 | 2025-10-28 04:14:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb5fa4e1-0589-3a30-8036-b9e88794f5d5 | -6.99701 | -39.12025 | 2025-10-28 04:14:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 53ea9b3f-6413-3fbf-ae9f-fcb121655ed1 | -6.64462 | -43.70311 | 2025-10-28 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4b70aa7-3465-37d2-b5b4-299e64e8a570 | -8.15788 | -47.00622 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98ddf9ad-0553-33e4-8cb2-c21b0b5952d0 | -6.69048 | -42.03892 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b3d87b1f-51c7-3568-8a15-032748698142 | -10.6808 | -47.26471 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6337d3b5-4360-357f-a3a5-badf363e3901 | -10.65583 | -47.91534 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a4351be-0116-377b-ac36-21d442bbd256 | -8.53928 | -47.3567 | 2025-10-28 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9312ca2-a482-31ce-be20-550a4ac43647 | -7.27052 | -45.00994 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6251c32e-d97c-3e6e-b74f-87b89f77cfe0 | -11.03185 | -47.85322 | 2025-10-28 04:14:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d875e989-5984-3f6e-acee-ca265df296c9 | -6.16618 | -43.08866 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a1cd9da-4b7e-3db4-bd6c-c99e3146f156 | -8.18318 | -45.71425 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6318f34e-4af5-3815-91e8-231f9227187b | -7.82101 | -45.38739 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c22af18-4a79-3124-a7bf-7982fe4592eb | -6.5892 | -42.68938 | 2025-10-28 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 40bd258c-d79b-336f-8e06-34efbc0a8bce | -8.32119 | -46.8353 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3449f90-eefd-36f0-a5f6-97447fce7112 | -10.58137 | -49.79105 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2815c75a-fc3b-323d-8852-e231432a39ea | -6.60906 | -42.05868 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eb3c291d-3807-380c-9120-7d583a12f7b6 | -5.85049 | -46.44909 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 044c1255-9e04-3f97-91dc-cddbf4ceb46d | -7.07586 | -44.95199 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fb91b019-d4f3-3a08-ade1-8d68fbc0288b | -6.27845 | -43.75889 | 2025-10-28 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17281820-ad38-312b-8bb1-084534d66341 | -7.16886 | -47.25249 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22327a65-462a-378f-b2b8-ad3cc262762e | -6.78443 | -46.45512 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34d0191c-8954-3c39-9cd0-b2c439ce31c6 | -6.96255 | -46.23736 | 2025-10-28 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf21c557-1fa8-3f2c-a0ad-f8c7eabb7095 | -7.29627 | -45.0671 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 19bff285-c861-33ac-94f5-22cd9826c177 | -10.57716 | -49.79031 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0101e4c5-8120-31d7-b773-f934bce09c69 | -7.64868 | -45.23681 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fed56f2d-1600-3c39-948e-aa0368c02faa | -12.64742 | -46.71935 | 2025-10-28 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99466640-6b0c-33ce-a4a6-d72d9d6a7589 | -8.48772 | -45.56744 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d94dbb9-0b0f-3cbc-a48f-1f955683b9d0 | -8.63328 | -44.79219 | 2025-10-28 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39ef3df4-0663-3b2f-9d9f-899c9736bd59 | -7.95576 | -45.46666 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b28560cf-5c0a-3385-8173-9ea8ace85740 | -9.21002 | -46.37136 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71ddfa5b-5962-3bec-833b-2615dab869c4 | -7.95435 | -45.54078 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 248ad44b-498b-3ebf-9ab2-91fc5bc99aeb | -9.51752 | -40.31398 | 2025-10-28 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 089b51d4-f7c6-3301-91a0-02c52c284778 | -7.81654 | -46.43249 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 60c1497c-06cf-3b76-b0ac-ae883e962fc6 | -10.57996 | -49.79899 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09a585f0-6949-3a35-b0d9-281772d0a60f | -7.41977 | -41.87124 | 2025-10-28 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7c6bad27-a4ac-3527-a877-d8ac9af3f705 | -7.90194 | -45.68866 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12f5497c-f091-3f66-870d-fdac3fb41656 | -7.9673 | -46.75016 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 8742b62b-c271-33d7-b2c7-e6bedc44fc61 | -12.19174 | -43.58419 | 2025-10-28 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1622710c-9849-3eb5-9765-4e626b503061 | -6.26275 | -41.81324 | 2025-10-28 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fbe4f424-d46e-3000-bafd-de5f6c8c8177 | -6.4466 | -42.36185 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 01f23a62-e574-3dc0-8dbb-a2bf2b9fcc2b | -7.89099 | -42.03869 | 2025-10-28 04:14:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 093b7b7e-28fe-3198-b370-cfcc8e6f5031 | -6.23818 | -42.56347 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3a782c51-552d-355a-9a9d-8b071f256365 | -7.94205 | -45.50762 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1fea5430-4698-3add-8d7c-2d6f329cccd4 | -9.87735 | -49.78625 | 2025-10-28 04:14:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4578ce94-c8c4-3918-b22c-528dd5bb650c | -6.24217 | -44.65119 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 292b1114-87f8-3fcb-9574-0eea12bc1bf8 | -13.5445 | -43.74075 | 2025-10-28 04:14:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15efa7c7-4282-339d-a31f-b1107e1390ac | -6.22321 | -42.52938 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b6d59a0-c7f0-30db-82ed-63437ca3825c | -6.11851 | -42.45927 | 2025-10-28 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bb877519-f86b-3007-ae12-72cde46e8ee1 | -10.84529 | -47.89434 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 46febde7-a4cb-3149-aafc-62ac5f7e0618 | -9.2248 | -46.36953 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a74badf5-84c8-34cb-97ad-857c2766a5d4 | -10.59957 | -48.03676 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9185703a-b29d-330f-8fb1-ca1921014b05 | -10.52717 | -47.72943 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1eaee75f-6da0-3e89-b428-eec33aba8661 | -6.96545 | -46.24215 | 2025-10-28 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3f7cd6ce-ba8a-39b9-9879-1725fd579d21 | -10.31032 | -47.16245 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d49b1411-8389-353d-a881-ab8742f5fd6b | -12.52831 | -47.54039 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a39d21af-5587-33bb-9482-c7d35eec1342 | -12.87617 | -44.58633 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f3cc2b8-c6ec-33e9-85bd-9f8a2d9fa28d | -10.73446 | -49.78593 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0dfeda99-c2b4-3831-aca5-769db5a7bef2 | -9.58856 | -47.85009 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1e52961-be72-3727-8bef-d47166c71720 | -5.78442 | -47.71816 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README34.md)
