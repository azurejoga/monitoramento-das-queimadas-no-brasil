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

## Dados Diários - Página 282

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 505e46df-460e-3dbe-8d27-dc2a72fe5506 | -3.21829 | -42.96468 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| f016af85-064e-3f43-a9f0-bd5c9fbf7df0 | -3.20292 | -42.96138 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6c9ef462-c7aa-38d1-b3eb-94fdd69b024f | -1.45688 | -48.9829 | 2026-10-09 16:03:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 928c4286-372f-359e-a0bc-80deba18233b | -4.86299 | -45.65599 | 2026-10-09 16:03:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c74138b-1742-38e0-b738-35bcfc125d4f | -3.82119 | -44.60435 | 2026-10-09 16:03:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1d6e70f2-9bb1-391c-9b1b-60bfc18f6aaf | -1.45791 | -48.98944 | 2026-10-09 16:03:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 355da714-8f35-3ff3-8f0d-97690e34bea9 | -4.32281 | -40.17159 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| ce2f6145-dd87-356f-ad81-f1697d1c9c7e | -4.37965 | -41.8134 | 2026-10-09 16:03:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| c9862573-504c-3bec-8345-95c231802092 | -4.50444 | -43.65059 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 41565b2a-396e-316f-ba48-3edf1c348ad8 | -4.60535 | -43.46476 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7506603-b64f-394a-9c0f-89948ea3ffe9 | -4.36312 | -44.35073 | 2026-10-09 16:03:00 | NPP-375 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0ab53759-6d6d-33e4-9e54-45689930ecc0 | -1.78172 | -47.80697 | 2026-10-09 16:03:00 | NPP-375 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 513a5071-16c1-37d1-9b4d-28a43cb0e56d | -4.15321 | -44.33467 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| ea47e6a9-5b4b-3fd1-805a-a59d6a734295 | -4.02695 | -40.6459 | 2026-10-09 16:03:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 99df2573-ff0c-3729-9c95-8df9697a0ac6 | -3.207 | -42.95533 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2f8cafbf-e952-3dd7-99aa-0b0011849781 | -1.72501 | -48.23893 | 2026-10-09 16:03:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ad0ebe62-3f68-38bc-b392-23b5977c5ee1 | -4.6474 | -44.84291 | 2026-10-09 16:03:00 | NPP-375 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1e8661c4-a013-30ef-813b-ba16569f9cca | -3.66485 | -44.76954 | 2026-10-09 16:03:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a005283-415a-37ad-b8dd-c1c5a7e0f6cc | -4.37052 | -41.81475 | 2026-10-09 16:03:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e5721bf3-53f1-3657-a388-243519c0131d | -4.50087 | -43.62553 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4a085084-f32b-3040-9008-b8f9c9533708 | -4.16147 | -42.96059 | 2026-10-09 16:03:00 | NPP-375 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d123953c-0277-3012-982f-3fbe7151de77 | -3.50373 | -42.58205 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f2741a38-773f-36f7-97cb-f5c0f33255a0 | -4.24113 | -44.25605 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3f1a6253-b31a-3006-8e8a-53d76d5bc8d7 | -4.43412 | -45.24229 | 2026-10-09 16:03:00 | NPP-375 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 281ac2e5-a958-343d-9346-f9fbb6ce20d9 | -0.75168 | -49.39719 | 2026-10-09 16:03:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 72491b54-43f6-3072-940b-c1128c2a59b7 | -3.90176 | -42.11314 | 2026-10-09 16:03:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 00209f02-e67c-31ef-bca1-946358f81664 | -3.21263 | -42.95996 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 082c5c4c-d6de-3a50-9aa0-bb6c1bb18a99 | -4.01744 | -41.75836 | 2026-10-09 16:03:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 5036ee48-fcd2-3c54-9030-401c154e37e6 | -3.5644 | -38.96848 | 2026-10-09 16:03:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ab897c3a-1de7-352c-913b-e0a5640fc27a | -1.77973 | -47.80426 | 2026-10-09 16:03:00 | NPP-375 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 38611768-325e-3027-a6c3-e5a7e14f62eb | -4.65153 | -44.84993 | 2026-10-09 16:03:00 | NPP-375 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 95368325-93d7-350b-99b5-2ba666d0ca61 | -4.08127 | -44.12143 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 038c5289-4832-3e4d-a070-c6010d78dd12 | -4.37508 | -41.81408 | 2026-10-09 16:03:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3879d6cb-c273-3ea4-82ea-0cc7f8198562 | -4.15912 | -44.33735 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 8605512f-796b-3a0b-aea1-be7d52c067e0 | -3.82669 | -44.60361 | 2026-10-09 16:03:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4ee3976b-351e-3106-abde-49fd9b2dbd26 | -4.35724 | -44.35923 | 2026-10-09 16:03:00 | NPP-375 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 845196bb-1582-30d6-82a9-6e5e069c40c4 | -4.65098 | -44.84603 | 2026-10-09 16:03:00 | NPP-375 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7af8bd57-1b90-3628-b9b2-a145e96c065c | -1.19486 | -49.06798 | 2026-10-09 16:03:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 08c23238-d3c0-3cd0-93b5-ff8610f4914e | -3.60854 | -44.57102 | 2026-10-09 16:03:00 | NPP-375 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 738c0711-1e77-3a42-8a4e-328e3583dc09 | -2.89605 | -44.76898 | 2026-10-09 16:03:00 | NPP-375 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7a2464f7-eced-359c-92a4-0a127fc939d8 | -4.03166 | -40.64888 | 2026-10-09 16:03:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f7cffcad-f82a-3489-895a-675599170d9a | -4.36595 | -41.81542 | 2026-10-09 16:03:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 6a888ea0-46d9-3aa7-893a-c95b608c4992 | -4.57426 | -44.73404 | 2026-10-09 16:03:00 | NPP-375 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff1efd1a-5e21-3471-a364-8617ee7875e5 | -4.49226 | -43.63947 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5fb187a9-6263-379e-bfe1-1156c6489cb4 | -4.15863 | -44.3339 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 6c309005-9c99-3ea1-bd3b-d4d45e706160 | -3.2977 | -44.52502 | 2026-10-09 16:03:00 | NPP-375 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4d37e417-7469-34ca-9781-6ca6d7922b04 | -4.64852 | -44.85053 | 2026-10-09 16:03:00 | NPP-375 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1a5828cd-f197-3aad-a6f9-a3db459e1ab3 | -2.27375 | -48.76742 | 2026-10-09 16:03:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f385d4bf-f570-3af5-94a7-88499737be7c | -4.08079 | -44.11814 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83e861b6-ad3f-3de8-b7f9-214487cd547b | -5.29178 | -46.72168 | 2026-10-09 16:03:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9fb69aa5-91a8-3a22-97b1-39a270bda6ee | -4.09258 | -44.16134 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e66a1233-fd91-38e9-832b-2078516ed4c6 | -4.10116 | -42.50515 | 2026-10-09 16:03:00 | NPP-375 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 197f8ca5-e325-35e7-9dca-ac1921c2875d | -5.1108 | -46.22706 | 2026-10-09 16:03:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2c13c33f-9518-308d-ae75-1bf48ed59048 | -5.2431 | -48.41354 | 2026-10-09 16:03:00 | NPP-375 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9e172c95-e35a-30c6-a284-d103f05ad74a | -2.52448 | -48.18562 | 2026-10-09 16:03:00 | NPP-375 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3ec51aa6-b14c-3c88-a549-0bcd0c565b95 | -2.33094 | -45.42151 | 2026-10-09 16:03:00 | NPP-375 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f5a1c70a-663d-3989-86f3-9316511d89a8 | -1.76666 | -47.80628 | 2026-10-09 16:03:00 | NPP-375 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4296b648-fd0e-32fa-b608-b6cbf85ae074 | -4.08663 | -44.12086 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b17f4a52-88de-39b9-a2f9-550e15464c0d | -2.06927 | -46.00326 | 2026-10-09 16:03:00 | NPP-375 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f7d2323f-94d7-34a7-86cf-92da6d7b5780 | -4.14852 | -44.35375 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 04c0cfea-e4e4-38f3-8067-63cf9b596a98 | -0.83557 | -49.23999 | 2026-10-09 16:03:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b6c72b2-6b33-33dd-b622-8d85ab9d7e33 | -4.36166 | -44.35157 | 2026-10-09 16:03:00 | NPP-375 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b2e62bfe-ea0f-3519-be98-9787ddc8f7d8 | -3.71026 | -40.83372 | 2026-10-09 16:03:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ab6b61ff-3a88-3af5-9103-531458e43f19 | -2.17928 | -45.58569 | 2026-10-09 16:03:00 | NPP-375 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4edfa63a-6fd9-34d0-8369-79dce535e77d | -4.31794 | -41.24319 | 2026-10-09 16:03:00 | NPP-375 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4ef7b21d-8ba1-3bee-9c16-8425706b2565 | -4.24281 | -44.25603 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3e7a64c7-d2e3-3251-8d59-751285ea9e7a | -3.48521 | -40.5723 | 2026-10-09 16:03:00 | NPP-375 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 15939013-aaa5-321f-a1ae-a5f963133607 | -0.83397 | -49.24215 | 2026-10-09 16:03:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| f7d076f7-7de5-378b-a9a4-7038fb0d9eb9 | -4.83222 | -45.84189 | 2026-10-09 16:03:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 981af9ff-e29b-3d5b-9833-7931c999a21b | -1.66831 | -48.11293 | 2026-10-09 16:03:00 | NPP-375 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7d4c43e1-6435-3fa1-8227-57c9b6c7030e | -4.60722 | -43.22733 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fef01d41-e742-3c57-9b21-86623a645a6d | -4.3532 | -44.3592 | 2026-10-09 16:03:00 | NPP-375 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ee307ed-f697-3184-9f02-41598dc4c9c7 | -2.33038 | -45.41772 | 2026-10-09 16:03:00 | NPP-375 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4ed57d7f-d6ea-3fa5-b517-3f57ff03ebac | -1.45645 | -48.98759 | 2026-10-09 16:03:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 07e9f479-a22f-30c4-b9c5-b220cd40ec1b | -2.27389 | -48.76225 | 2026-10-09 16:03:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 48c6598c-9b10-363a-b239-5516c4347be7 | -4.15566 | -44.35196 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cdcb0b51-1695-38a1-9a47-d9c3b456174a | -4.83023 | -45.8278 | 2026-10-09 16:03:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 5590c02a-28bd-3472-b3cb-be0158614f16 | -4.84833 | -46.09007 | 2026-10-09 16:03:00 | NPP-375 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| baf625cc-e7cc-327d-a3d6-75da7bd725f3 | -3.69123 | -39.12687 | 2026-10-09 16:03:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 727ec8c6-4315-34c2-9e5d-7662518b0e00 | -3.54909 | -38.81216 | 2026-10-09 16:03:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1cc52e18-eab6-36d2-8ade-13b8b8815c3e | -2.18388 | -45.589 | 2026-10-09 16:03:00 | NPP-375 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9ecf490a-857b-37eb-af09-c2ab56ad169c | -4.14731 | -44.33198 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7e3eaa62-4ec1-31d1-8a31-da9689ad86a4 | -4.08674 | -44.15873 | 2026-10-09 16:03:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f0d21b09-80fb-36fe-be24-fcc09ba606ba | -4.89653 | -45.67816 | 2026-10-09 16:03:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6d9bb8ed-d238-3a19-ae6b-69fa62c9a87b | -4.15273 | -44.33121 | 2026-10-09 16:03:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 8bbfcdc3-4c7b-3a1d-84dd-bcac5d1e6506 | -4.0181 | -41.76292 | 2026-10-09 16:03:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| aebd1dcf-385b-35ac-ad9e-f17af3c48daa | -4.23795 | -40.55845 | 2026-10-09 16:03:00 | NPP-375 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3707c739-31b8-3ec1-b000-eab57033f3c9 | -0.74864 | -49.39973 | 2026-10-09 16:03:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c0c52c12-da16-38b8-a844-a11fb4f839d6 | -4.04539 | -44.52571 | 2026-10-09 16:03:00 | NPP-375 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c988fc2b-9fd4-32ca-a47a-1064df284627 | -1.89839 | -48.14548 | 2026-10-09 16:03:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b03c404a-6376-39e8-94dd-6355caa62273 | -4.44049 | -45.2456 | 2026-10-09 16:03:00 | NPP-375 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 30.5 |
| fb736b64-8e2d-382e-b3ed-1e39a5f73cc0 | -3.20049 | -42.96292 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| ac8a7483-35ff-3697-8bf4-2f37a3ca83e3 | -3.53462 | -44.32994 | 2026-10-09 16:03:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5afa6dc4-cb78-34aa-ad3b-12c501d89bbc | -5.24014 | -48.41541 | 2026-10-09 16:03:00 | NPP-375 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fc3bc923-cdb4-369c-987f-4a348ac14e8c | -3.63062 | -43.10332 | 2026-10-09 16:03:00 | NPP-375 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 02525198-c028-36e5-bea3-97f1efef51bf | -3.78062 | -44.36503 | 2026-10-09 16:03:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 799a837c-cf7b-3139-993e-d1ab79bd8960 | -4.32231 | -41.24247 | 2026-10-09 16:03:00 | NPP-375 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f150247e-2756-3dca-b45a-03b1aff50962 | -4.60491 | -43.46171 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d311880-2028-3e90-a115-a1417f45fd4a | -4.50562 | -43.62175 | 2026-10-09 16:03:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 07f8a592-c902-39b7-974e-4d779c58cd8e | -3.17941 | -42.97044 | 2026-10-09 16:03:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README283.md)
