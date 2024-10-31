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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e64f3c0-e4b7-3204-8280-d3141df0d93b | -16.56357 | -56.24994 | 2024-10-31 04:27:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 86ac46b1-fcaa-39bd-93cd-0edc04bf274b | -16.55885 | -56.24891 | 2024-10-31 04:27:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 03db3250-9d79-3e8c-ba70-6fe9c5952bdd | -18.26451 | -55.96333 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 20e95956-2d79-3766-b176-7364c61bb6ca | -18.26002 | -55.96236 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 66131dc1-3cf4-3880-9df1-7f73b6458c42 | -18.25904 | -55.99171 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cf0af2da-d188-3ce6-8a51-6e924d459317 | -18.25553 | -55.96137 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5674496a-9320-3841-bd21-a5bc44cd45cb | -18.25461 | -55.9661 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 901f9fda-5e87-3e11-ac37-4496fc8d6f3d | -18.25453 | -55.99075 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ebd33cee-39c2-3bb3-898e-04985adc91b2 | -18.25012 | -55.96512 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c22af039-cd86-3687-8887-54edff631b7f | -18.2492 | -55.96985 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 846fc5ae-b3b5-36c2-a6de-4bc257d5f1db | -15.46404 | -57.51654 | 2024-10-31 04:27:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5169ed0e-1f2e-37d7-9b33-1a1cec6986a6 | -15.45815 | -57.51868 | 2024-10-31 04:27:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95920919-3d36-3033-9c0d-4c18f132fbce | -16.16988 | -56.78707 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42dbaa48-5dec-3192-a9a5-b3b807ee7e29 | -15.79117 | -56.61539 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cff728f0-157c-331b-a1ee-6683d26926d3 | -15.79024 | -56.61388 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d16c7a7-480e-3743-b435-be2bf47e768c | -18.08011 | -57.37576 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 86063045-82ac-3f0d-b5f7-4b0e4da3a11c | -18.05429 | -57.22472 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4071200b-057d-31be-a53d-0931ef709686 | -18.05323 | -57.22308 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 80dff467-8fbf-3529-8c01-97b51162e329 | -18.0494 | -57.22363 | 2024-10-31 04:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ff433ca5-22a8-3a00-858f-f10529fc580f | -17.81412 | -57.38808 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| a22c8ddb-ae7e-3152-b830-ac3a06718c7b | -17.81279 | -57.36922 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5f576b02-d8a4-3266-b5b5-34b8c4651bcc | -17.81158 | -57.37513 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 500d8890-8d02-37cc-ae85-eafb4acb4533 | -17.80783 | -57.3681 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3668fac3-a0bd-3a96-8982-4d339d947b9f | -17.80726 | -57.37168 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0fcff20e-f149-3a83-8327-6c461270e69b | -17.78247 | -57.36608 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 145798c9-3399-3661-9dd5-00ea6ca8743b | -17.74301 | -57.53736 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 27efe98b-61ce-332e-9536-09196e7c6f56 | -17.7424 | -57.5404 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9f60370e-22f7-3db8-876a-6df8a423be29 | -17.73224 | -57.51274 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ad36b431-d341-3e10-9d6d-4b8f21ffaafa | -17.73176 | -57.54116 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5e536a70-b6fe-3008-aae0-503472413d7e | -17.73115 | -57.54421 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0061c1c0-46bf-3587-bae9-48b1bf288edf | -17.73053 | -57.54725 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 250da58b-6440-3764-b96d-d984cf9a17e1 | -17.72723 | -57.5116 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bab8d4fa-4c1b-33a1-88c4-a079c52adc57 | -17.72674 | -57.54003 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ed952f1b-17ba-3474-b635-afd39adbf5ac | -17.72428 | -57.55222 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 3b3e750b-c13c-3ffc-8429-9f4968fadac8 | -17.72367 | -57.55526 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 332cb0b6-662d-32ac-a000-4cd9928a32da | -17.71926 | -57.55106 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 022ecab9-f03c-30f7-b109-732caedf331a | -17.71865 | -57.55412 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 72e5629e-240f-3df3-9144-13d68b7e23b7 | -17.67838 | -57.4943 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d4589503-719c-3170-bc8f-0f10e0fa0b37 | -17.67776 | -57.49733 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7a8ccd45-0550-35ab-b84c-3e2f8aa123a4 | -17.67275 | -57.49619 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6c7a1184-79fb-3429-a0b3-0eb8e838150e | -17.65959 | -57.4928 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 542655fa-f507-3912-b066-79be0f78bedf | -17.65772 | -57.49281 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5175f2bc-dcbf-3368-9a05-29af070ba4e7 | -17.65459 | -57.49166 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b7584f29-9c4c-34c7-8eb5-161b3ba6e88e | -17.65398 | -57.49468 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 03dac93e-859f-3cc8-bb97-c9c9c80b43bb | -17.65271 | -57.49168 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6b59c242-3007-3d18-8717-eaae8fd91d99 | -17.6526 | -57.47538 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b5cdcacf-ea98-31c1-a1fa-b5bb3ce30d72 | -17.65199 | -57.4784 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0fa77030-e62c-3949-b222-a06415503fab | -17.64699 | -57.47728 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 627e5c20-5f2d-342d-9e69-6e9feb0c6d4c | -17.27563 | -57.49724 | 2024-10-31 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0f552caa-6503-38fd-b576-81c8324d0ee8 | -17.27501 | -57.50032 | 2024-10-31 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| f44bae1b-f9fc-31c1-88df-cab98b3c6eb2 | -17.27438 | -57.5034 | 2024-10-31 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| e2c297dc-5583-3c9c-8cce-7d52cee517ef | -17.26996 | -57.49919 | 2024-10-31 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| fee0aa1b-9b40-36f0-bc6b-cb8712d73ae8 | -17.26933 | -57.50228 | 2024-10-31 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| da0834d4-97c6-3837-8daf-302b0828dd52 | -16.92334 | -57.65851 | 2024-10-31 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a7d1dc2e-28ce-3644-a90c-81c2361efe95 | -16.92269 | -57.66171 | 2024-10-31 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 35187027-6920-3fb3-a3da-96adedcbc60b | -16.9182 | -57.65736 | 2024-10-31 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f9b37983-debc-3391-ab97-b46e205e7871 | -16.91755 | -57.66056 | 2024-10-31 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 63b078f0-d05d-3cd0-89dc-5e95e51b7ecd | -16.83035 | -56.70072 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8bfe276e-9038-391f-a82f-f9769c94a882 | -16.82659 | -56.69411 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 99f8b85f-94b8-307d-8880-e82c51131704 | -16.82175 | -56.69307 | 2024-10-31 04:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7f02e8a4-6909-34c5-ba9c-e94084dd6ec3 | -16.21576 | -59.33211 | 2024-10-31 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cffbb7a-83bb-331d-aa18-d4e24e32d158 | -16.21487 | -59.33628 | 2024-10-31 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 710365b9-7886-349b-8cd2-b29b11a3d227 | -16.21072 | -59.33348 | 2024-10-31 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5cf1bbf-67d4-3815-93cb-63aaf580cdc9 | -16.20911 | -59.3349 | 2024-10-31 04:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7626e0e-ac8a-3df1-809d-7cc8b722bb32 | -15.12346 | -59.02278 | 2024-10-31 04:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c79a5c7f-eb7b-3333-b161-0893d90b3955 | -15.12251 | -59.02737 | 2024-10-31 04:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a95c7b7-373a-3185-8b7d-ba0c1862c758 | -9.74074 | -36.08567 | 2024-10-31 04:29:00 | AQUA_M-M | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 52.5 |
| 937d06c1-8bb9-3f4f-978f-08d5615ba999 | -9.73915 | -36.09583 | 2024-10-31 04:29:00 | AQUA_M-M | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 4126fb13-8083-3380-8412-c09119e6ef24 | -9.73133 | -36.08419 | 2024-10-31 04:29:00 | AQUA_M-M | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 37.9 |
| 03b68e7e-e2a8-3df4-ba36-f666c30076a8 | -9.72973 | -36.09435 | 2024-10-31 04:29:00 | AQUA_M-M | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| bfc48236-8141-3fc1-812d-c3327f10e890 | -9.72191 | -36.0827 | 2024-10-31 04:29:00 | AQUA_M-M | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| ad0d4f1e-5b7c-3492-969b-0bf6ee40fde9 | -6.68375 | -37.46326 | 2024-10-31 04:29:00 | AQUA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 10.4 |
| deda01c6-0426-3836-8dc5-84f5bfafe6d2 | -6.04042 | -35.28078 | 2024-10-31 04:29:00 | AQUA_M-M | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 2eb070a1-81e6-3ad7-8723-f8666c101e58 | -6.03884 | -35.29088 | 2024-10-31 04:29:00 | AQUA_M-M | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 7eeb403e-6edc-3d24-88ab-d72c4dc6a029 | -3.39174 | -41.63269 | 2024-10-31 04:29:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 9a0e42f9-cdc3-3ff4-b56d-30a2740ba44c | -3.40083 | -41.62614 | 2024-10-31 04:29:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 76bccb74-0fe5-3ad2-822c-1f0278b5ff6d | -22.89917 | -43.75258 | 2024-10-31 04:29:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 80d81fc1-0b88-30ce-8482-fd0c0543cb46 | -22.69816 | -43.34799 | 2024-10-31 04:29:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2c798a59-4325-30fc-86cb-233c8b390415 | -21.19347 | -44.93564 | 2024-10-31 04:29:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c302285b-fa96-3678-b3ed-894ac4a8e215 | -22.53243 | -44.43052 | 2024-10-31 04:29:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6ea17811-f084-3bdc-b869-a5bf6a473c75 | -22.53195 | -44.43456 | 2024-10-31 04:29:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a1ad8d9e-a8d0-328a-bca2-b86857a893d1 | -23.75716 | -45.7286 | 2024-10-31 04:29:00 | NPP-375D | SÃO SEBASTIÃO | SÃO PAULO | Brasil | 3550704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 495e2413-854e-3e02-8e1e-80b7c58aa5ce | -23.75674 | -45.72715 | 2024-10-31 04:29:00 | NPP-375D | SÃO SEBASTIÃO | SÃO PAULO | Brasil | 3550704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0593db7f-6633-3d72-aecd-a53d8364b88c | -20.47392 | -46.57745 | 2024-10-31 04:29:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d473d3a-2efb-332a-a8d0-f7ba24483f27 | -20.47333 | -46.58166 | 2024-10-31 04:29:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d03dc00-a8a4-36b5-8bb9-0fadb6149a27 | -23.70362 | -46.47607 | 2024-10-31 04:29:00 | NPP-375D | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5356b5b-a8f5-3151-a31f-b4aac05c2b3e | -23.40486 | -46.55651 | 2024-10-31 04:29:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a2048119-cb73-3e89-b81c-4e347ab190cf | -20.95686 | -47.17208 | 2024-10-31 04:29:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ab15e1b-c7d3-3c16-b998-f2776ffea413 | -20.95338 | -47.17145 | 2024-10-31 04:29:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 79f8586b-d0c1-348d-b40a-818b3319d91e | -20.71032 | -47.28743 | 2024-10-31 04:29:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9afb1f9-c2ad-3682-aef7-dc75a2c4b108 | -20.64842 | -47.22387 | 2024-10-31 04:29:00 | NPP-375D | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11fdafae-5da3-3fd8-b6ae-9895f9bef19f | -20.76287 | -46.76954 | 2024-10-31 04:29:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f62f3530-b771-3f07-8f59-58bdca0828e5 | -22.42335 | -48.58492 | 2024-10-31 04:29:00 | NPP-375D | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 23c96668-cff5-3f61-be63-abced2509000 | -22.36278 | -48.75965 | 2024-10-31 04:29:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2d09f039-1424-3f25-9da8-7094ade8aae6 | -21.63449 | -49.84046 | 2024-10-31 04:29:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 034ed4a5-52bb-3719-9c4e-9220ff234709 | -22.88615 | -49.22149 | 2024-10-31 04:29:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 762b9207-27db-3430-924d-494a2d36698b | -22.53887 | -48.81261 | 2024-10-31 04:29:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 528a7065-22d5-32cb-bd57-c3215245aa2d | -22.79522 | -50.19796 | 2024-10-31 04:29:00 | NPP-375D | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5b5fa837-7711-3fed-af3c-1db1199f0835 | -24.65852 | -50.17476 | 2024-10-31 04:29:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74ca6561-93c7-38b4-8868-dae2c8e10d04 | -20.31808 | -50.01208 | 2024-10-31 04:29:00 | NPP-375D | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README27.md)
