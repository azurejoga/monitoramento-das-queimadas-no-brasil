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

## Dados Diários - Página 311

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b49ad005-a1e1-39f7-a216-4d36cf46f635 | -6.3634 | -42.56939 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| a893ef1f-a5cc-385e-a006-da7d1120ec4e | -5.99242 | -40.93986 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 39.6 |
| 0a48c133-da2e-3445-9023-63dbfea5b0d0 | -9.95242 | -45.96841 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a84a9c24-d6aa-332e-ae2c-59ba2ba57e02 | -8.96177 | -47.54771 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c22cf77f-488c-3c15-ad58-2a08e6537009 | -18.674 | -43.62615 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7329c81c-a4c4-3447-b9ef-971a4d121a30 | -6.79738 | -45.05842 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 483f85ec-a5dc-3838-8c7a-312bcb7e4e70 | -10.07668 | -45.68926 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 1853c0a5-5778-3f44-8b3c-c80c0397e913 | -19.41392 | -48.62165 | 2026-10-08 16:37:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9274b538-6f3a-3973-8c83-f761e7fabc20 | -11.73798 | -43.64416 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| e7a14cd0-1cb7-3ed5-a43f-297edb2f0536 | -6.37656 | -45.78783 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 647c31a0-20cb-3118-b10f-976ccd921adf | -12.83276 | -44.62536 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 58126518-7d9e-31c5-bcd1-d31d8f29872c | -10.43671 | -47.28367 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5aeb1c75-943c-3236-b844-d4ba6990a468 | -6.42944 | -44.83174 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 14d30f88-7912-3cb9-9114-741abafd20da | -6.69205 | -45.30025 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 148552cc-2f75-3827-9625-11d39affae98 | -8.0769 | -45.61142 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d40382c5-4813-3701-b540-890a206127a6 | -6.55121 | -39.488 | 2026-10-08 16:37:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 9e44a150-cd63-3c5e-944a-63f7c863b795 | -11.97961 | -39.0476 | 2026-10-08 16:37:00 | NOAA-20 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 9ed7472d-be20-392c-b4d4-35aa3bc97356 | -10.7722 | -38.49876 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| cf508cc9-e0f9-3ea9-bafc-237ee8bb7c75 | -8.30942 | -45.73454 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 493ad795-9b92-3ffb-94f7-b25fed041814 | -18.28181 | -41.22863 | 2026-10-08 16:37:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 98773a54-563f-3d84-9690-753169e83cdc | -7.76689 | -44.17422 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 958f91e4-b6c4-34b7-b1a7-44d4ccd7c938 | -9.33474 | -48.34671 | 2026-10-08 16:37:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 087b6e47-b68f-35be-9e67-b2c378af0a22 | -10.40099 | -46.26658 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2beaa5ec-2b7e-3b35-9cfc-4e50befbd243 | -8.9578 | -45.15735 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9c3b7fda-7d6b-37d5-93f3-98ccd12a2ca6 | -9.77424 | -47.81531 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a7bd0257-db3b-3087-8e88-f2a52af52264 | -11.62441 | -43.69994 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 8799cff8-f068-3e5f-876c-1c95b982764c | -6.32525 | -37.74673 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 12.6 |
| f61bc248-fdf7-332e-8391-44408a619e44 | -10.47688 | -47.8555 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fd828b66-a5c7-317e-8e14-6e0129c1e971 | -7.69538 | -45.44534 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d9956f32-e8ff-3088-8d34-17ccff431901 | -11.21521 | -41.57658 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 3051cb89-20fa-3245-a58a-5ed90e3ac02c | -7.491 | -42.79687 | 2026-10-08 16:37:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 0c5b9629-7449-3f6f-9475-dd76fcf3c296 | -10.89861 | -45.54003 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b48a6088-b290-3f23-bc46-729a5e8caae3 | -8.74954 | -47.13148 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bab44dc3-1751-3ce2-822d-9ecc24acbeb3 | -7.69869 | -45.44483 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| b72431bc-5ef3-3c83-a9eb-36bffdf7d91e | -6.68278 | -44.32174 | 2026-10-08 16:37:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 423ec2d5-a873-3cfe-9c63-72f084441e66 | -10.76727 | -46.60973 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5637e23d-7beb-329b-acf1-4365a84ffe5b | -6.53168 | -45.38301 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e68fe4c8-2094-3143-a2ee-5d3d1b677af8 | -10.47005 | -47.23096 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| c2b09cd5-947c-35eb-9ae9-89cff590f7ef | -6.84719 | -41.75902 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7ce447cb-f833-34ed-bde2-e94877f96bb1 | -6.91226 | -43.93095 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1d4431e4-3a50-3d07-87bc-34e003998748 | -6.94001 | -41.94687 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 0bbb6d2e-0e73-302b-b7b4-aa7af3194cce | -10.77195 | -46.57122 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 70668593-e520-355d-9de4-37202940ecee | -5.59978 | -36.17524 | 2026-10-08 16:37:00 | NOAA-20 | LAJES | RIO GRANDE DO NORTE | Brasil | 2406700 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 165c894b-5910-3905-bf4e-f1d0267b51b2 | -14.50433 | -49.33139 | 2026-10-08 16:37:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b6e6933-6f75-33dd-9391-0ec7bbbfae25 | -7.89955 | -54.72138 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0decad9c-dd22-37f9-bac5-7c145e4bbbc8 | -11.82406 | -40.4902 | 2026-10-08 16:37:00 | NOAA-20 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| efb92d31-4f62-312d-a55f-58bec8219333 | -11.84579 | -47.38839 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4f7dbd70-755e-3ef6-8941-474a36e8364e | -8.26904 | -46.90978 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a2a47a44-8a28-3fb3-af02-e24b6f7c013a | -10.21995 | -48.04864 | 2026-10-08 16:37:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ef4a53a7-0fbf-3f3a-b394-75d577d1003e | -18.98214 | -44.45317 | 2026-10-08 16:37:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36d3664d-b241-3a46-aa4b-d593a74459e5 | -5.99654 | -43.61775 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| abb7c264-92d3-37e2-92dd-62828cec282d | -8.62237 | -44.87522 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe23a67b-89d2-34e6-8d1f-c458b03701a7 | -9.26753 | -45.63152 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| bef39457-d6e3-3d5a-84f0-9144e701ed67 | -7.48812 | -42.79661 | 2026-10-08 16:37:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 42430502-04bd-3b41-b764-22db52a44e8f | -7.88837 | -55.00805 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d5a43554-2e76-362f-b3a6-265e804a4f68 | -11.07306 | -44.04255 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 239.5 |
| 87aec395-eebe-3015-b285-8cb146373577 | -11.27878 | -45.20498 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 608b7d34-0980-3eef-93be-52999d7d8216 | -11.59039 | -43.67955 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| c68b6de1-4326-3efb-8592-c5de95394549 | -6.93032 | -43.66673 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 854e7f4f-5c92-3ee5-8842-773d3bd0f78c | -11.65171 | -43.68391 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ef7befbe-6a8b-39f1-aeb8-9bca0625f8ca | -12.31876 | -45.26314 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 47dc39c1-ea06-38b4-9234-e6efe91fbe33 | -13.70723 | -49.10424 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5971541b-8da6-3063-ad9f-e0b14f6618c2 | -11.79029 | -46.78873 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6b09c85-776f-3bcc-b5fb-ade60d6b2c13 | -6.81627 | -38.53061 | 2026-10-08 16:37:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 404fe9e5-aa95-31b3-8252-fb0014a9ad9d | -8.06578 | -45.62734 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03122bb0-614d-3990-8e0a-6bc0eb32f31a | -11.84529 | -47.33519 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6aaa7545-3596-30a2-9422-af9322fd946e | -9.52472 | -45.60527 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6d6acacc-e52c-3db5-9dd1-230b1dbd2d8d | -8.17457 | -44.41363 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ded8a6f5-c2c2-3cd7-9083-d43eb972aae2 | -12.61649 | -44.54201 | 2026-10-08 16:37:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| e6f4d87d-4085-36c8-8ec6-0a9ab761482f | -11.75289 | -44.93058 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6225e40f-590e-313e-b3bc-38e1acc5166b | -11.63601 | -43.59841 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 09b62b00-0ed5-34ff-8d86-a90c1142cbd3 | -12.3193 | -45.26669 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2730eb6a-5926-3cdb-b6e3-6bcfb2b0fdd2 | -11.27441 | -45.19849 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c3d6fe6b-d2fe-3bbd-9949-f0158ebaae6f | -12.03838 | -43.43604 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e39c2225-3f8b-3d14-bcb4-9f885748d85a | -9.41543 | -46.54879 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b452d2c8-b157-363f-86a3-c9f92584177f | -11.75974 | -45.49372 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 9a10d0a7-749f-33a5-8807-aada80b3c998 | -9.97701 | -43.49818 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 39841a0a-0022-3590-ab1c-3ee84ca2d8a3 | -7.26338 | -43.50893 | 2026-10-08 16:37:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 0da8e711-f4bc-3ab9-9669-55a1a0930007 | -8.03517 | -47.99869 | 2026-10-08 16:37:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3c8fdf9-7267-335e-83c0-8700ded410eb | -10.07239 | -46.00028 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 05f143e5-09a8-3da2-ae25-c46a757907cc | -9.10551 | -45.12596 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ca7c5cdb-8f96-3470-9d61-9263dada4d31 | -12.18928 | -44.65514 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f3d0878d-a056-31f1-9590-7cb388c39e9c | -11.78684 | -46.78919 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 46bb2676-d188-3b04-9ccc-96562c28c8e3 | -17.12328 | -39.51406 | 2026-10-08 16:37:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 3f37563d-0883-32b2-9b87-55b08fe45379 | -8.75107 | -46.83989 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bcae08c2-60f0-3fc0-87db-54d53ff068bb | -13.19849 | -47.87468 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 236c33f5-2a37-332f-b6ce-31a46242dcbf | -9.91668 | -44.79477 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 54d09aa2-63c5-3a58-97bd-446694ff01d2 | -11.07917 | -44.01611 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 060fd43c-c66f-37ac-87d6-5190ea89eb75 | -7.33815 | -45.28573 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 06ddcb2e-585f-307d-9b6b-bee2397d8bcc | -11.15312 | -47.28922 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9234e86a-674f-3a2e-b177-b334bfcd3d74 | -11.63219 | -43.70596 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| fbdea5cb-6a5e-3aae-96ec-67043000d2ce | -5.53154 | -39.84013 | 2026-10-08 16:37:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a33ac630-9cd9-3e0e-99b4-9c7a6ee3bcfa | -9.69212 | -58.09639 | 2026-10-08 16:37:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7db5d322-3485-334c-88e4-96e7ab87c30e | -10.81073 | -47.33991 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 14ee1b5b-12f6-37f1-95bd-c0dd06b2a914 | -10.42115 | -47.27416 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| eafaed98-7c4a-38c9-b470-8ed61c03cfba | -8.17684 | -54.72174 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 29652718-6b27-357a-b1bc-09c9bef1b2b5 | -5.97851 | -41.35814 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 10cee263-7314-377e-b78d-ac5751ce9cb8 | -8.20388 | -46.3374 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 57bb0aa5-eba7-345b-86bd-90fbd6501ab4 | -9.36651 | -45.94941 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| b5d3fc5e-0976-365a-ba97-ce70a9e9706a | -10.41769 | -47.27469 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |


[Clique aqui para ver as próximas entradas](README312.md)
