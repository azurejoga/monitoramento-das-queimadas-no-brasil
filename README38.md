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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dc79f68-10ad-3fdf-9c62-c483bef5074c | -6.98882 | -44.77366 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60c1a774-cdff-3868-91fa-7d8ef9d0ab3d | -5.77674 | -43.91382 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c940f7b-5506-3ed6-9574-918bad400468 | -6.63471 | -44.74262 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f740c5c-4b5d-3f40-83b1-03a8204d71f8 | -3.82371 | -44.10775 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5d789da-c8ea-3fa8-a402-12acd0448808 | -5.6704 | -45.06182 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40598551-833d-30a6-83bb-171b622a44cc | -5.67262 | -45.04766 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32ddb862-fb7b-3f39-8c01-c77b333e6f2a | -4.1756 | -48.57433 | 2025-09-16 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8712765-3715-3066-8e15-c6a15f1cadd2 | -4.06156 | -46.93814 | 2025-09-16 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5cbbcfcf-8791-3737-9c62-20c558e13ee6 | -6.77633 | -44.72714 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0f375a8-e0b7-3741-92d7-cb84c5d281f9 | -5.05297 | -45.20066 | 2025-09-16 04:27:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0dbf8fd-3711-3b02-a94a-1442bfc67b1a | -6.18907 | -41.19133 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20078caf-6d9b-3bee-9055-6513d562b0f8 | -5.78719 | -43.94574 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ec6e1c6a-564f-3479-9205-6ab4a84e2d61 | -6.12904 | -42.94189 | 2025-09-16 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0bacaa7f-ac28-3341-a471-d59f5fe36849 | -5.88046 | -45.66265 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecf6e370-1d7b-34dc-956c-a1e2688e5441 | -7.14775 | -44.32875 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f9f2266-64a3-35ca-b1d1-5a5a95e057f9 | -6.54504 | -44.0068 | 2025-09-16 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36e0eb5d-47a0-3caf-893e-9fd641d1a936 | -6.09333 | -46.5003 | 2025-09-16 04:27:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 722f2522-97d7-3cd1-8c1c-cbd1287ee091 | -6.55377 | -43.99634 | 2025-09-16 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6e45b9e-760d-3a29-ba02-6d609e4d8a21 | -5.99718 | -43.70191 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20b530c0-595b-3176-b794-0e29780f1f71 | -3.95423 | -49.43751 | 2025-09-16 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c43c440-a549-3c80-9f67-ad817963b927 | -6.07875 | -50.1697 | 2025-09-16 04:27:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ff0d3d9-2f3a-30cb-9b7e-b2185babfa67 | -5.56824 | -46.46378 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2709168a-bb1b-3594-bb2f-8af9fd54cba1 | -6.76118 | -48.11409 | 2025-09-16 04:27:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e404a205-864a-3732-a554-1a6fe760df32 | -6.26307 | -43.47338 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5e72c3f-9f76-3b2d-a74f-528861f3f6e4 | -6.66358 | -45.54166 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1910472-f9d7-360b-91e6-aa8a4e54959e | -5.98175 | -45.79234 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e51c8ea-e43c-36ed-ae7f-9d63cceb2de0 | -5.25196 | -44.14305 | 2025-09-16 04:27:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 921312f3-8597-336e-b634-4136ed6b9a06 | -3.87927 | -52.29864 | 2025-09-16 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4e75aab-3b25-3d9f-9b7c-4f25bb370654 | -5.97464 | -45.83754 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b88c539d-a0e9-3366-b2d8-395b08c73062 | -5.51375 | -42.70589 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1ebec609-7c6d-3b9f-a742-dc91a1b06946 | -5.93995 | -45.71093 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce330793-4702-3b69-afa0-d5111e226e62 | -6.97693 | -44.53852 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2c2b4f3-bc25-3a2f-b667-3559a9f43b92 | -5.79587 | -43.93541 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 689caa90-5823-3f9f-9ac3-a5b8a20df3ac | -4.06437 | -46.94223 | 2025-09-16 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdbd60eb-99cc-3aa5-9fa4-97378a6eb773 | -6.17723 | -41.21487 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 48567d88-9176-3dcc-9138-9f350c4ca045 | -6.44218 | -43.30809 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1fa9a95-ed2c-3e19-9f68-ed2b4d413de3 | -2.74648 | -48.60554 | 2025-09-16 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3df4e8e5-8e18-35c3-bb33-ce9f8a48d9d8 | -7.26664 | -46.59004 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b3469b67-7acc-3920-a899-8d8e5ca71f71 | -3.81117 | -41.56907 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c6aefe8d-9975-3e3a-912d-09c20cfcd3ce | -7.00745 | -44.53851 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6cd913c-b5d6-38db-8ea3-eeecdd703c7b | -5.75686 | -46.61829 | 2025-09-16 04:27:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f7ce389-f441-358c-bf03-003579a3738f | -6.40594 | -42.65161 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4fe00181-2e26-34db-9b44-64ea0fd840c0 | -5.79513 | -45.92345 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9404c4f1-1b11-365f-a177-d42f925e8310 | -6.41031 | -42.64779 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d7d162d-9815-36d8-8c8f-ca2606dc0729 | -5.79568 | -45.91998 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d96d6f48-88f3-34a8-94a2-e66b9e67bf6d | -5.78907 | -45.94023 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbb8f875-fb6b-3761-b981-cae962680dd8 | -5.98408 | -45.84258 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1dcf050-8890-3fa1-9042-893a0b1cd272 | -5.34261 | -44.81887 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a091d0d4-658b-301f-95ee-5d2630907846 | -5.77495 | -43.92527 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 473b41e0-aa2b-381a-9fce-29cadd37bcf2 | -2.9458 | -49.34669 | 2025-09-16 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c80a82e8-64a9-3574-ba1e-c7c0d2f2d44c | -6.18501 | -41.1908 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0b778a99-b062-34f9-8870-596238c1288b | -7.27552 | -46.59859 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba9c4183-7174-3ea8-a2ac-7096972d77d9 | -7.06038 | -44.16822 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adb01eab-8784-3b7b-b109-a5ce88344210 | -6.29321 | -42.3978 | 2025-09-16 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2091fcd0-f253-3fcd-a606-957873d1fa37 | -6.18652 | -43.47416 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f3b0a7a-47a9-3941-9e26-e91d7115e5b4 | -5.08575 | -42.05508 | 2025-09-16 04:27:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e098c037-f711-3ad1-8b45-e41c3548de2c | -5.77731 | -45.88869 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f85818f2-0816-34a3-8435-27abb72c2f76 | -5.79905 | -45.9418 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61dbc930-cd2f-37f7-a70d-3f8d41356c31 | -7.27439 | -46.58415 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce68c50c-b6f4-3d58-af33-66f78fdcaae0 | -6.12665 | -43.3713 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78eb4ff7-1aa7-33f1-b092-63e2de00b397 | -7.30579 | -43.9264 | 2025-09-16 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34a5ed5f-1e82-3720-a196-c2c14cbc47e8 | -7.6862 | -44.47836 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25364d34-db49-3c01-8955-e6503becc848 | -4.45209 | -38.44414 | 2025-09-16 04:27:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 570b3261-b43a-34a1-81f5-58632dc7dab6 | -5.97683 | -45.82362 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81cbea6a-c3b6-3340-97e8-41e2a175b464 | -6.18519 | -45.42754 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 15b6d5e1-fa16-358c-9ace-c1c9e051f2b7 | -7.3099 | -43.92304 | 2025-09-16 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 071b59f3-3dd0-3f36-89c4-ec9fcbbf1e96 | -5.34206 | -44.82244 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 918a0b11-6d0c-39cf-bc5a-a2e8bf92a54c | -7.84947 | -46.12875 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c50660d-8c5e-360d-9ea5-df5f9341eaf6 | -7.44842 | -46.16571 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b8e3206-a105-33f2-86ea-985260db3f75 | -7.54513 | -50.48328 | 2025-09-16 04:29:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cae178a1-6aea-3208-ad68-8f33c32f7a0d | -7.67734 | -46.29863 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f880c485-212f-33c7-a5ad-1364adc05f38 | -8.97841 | -45.75925 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3dc8fd95-7fbf-34b3-b19f-b2ba1804a4c8 | -13.02453 | -47.97125 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 910c1125-57cf-3517-9c6e-c90d54fe4e5a | -12.84274 | -47.13017 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddda4d64-8507-3be9-a3e8-825f19d4711f | -11.08079 | -49.75064 | 2025-09-16 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b1e2692-d3dd-3d17-916b-c24b1e59dfee | -12.62856 | -47.52175 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8879fb2-4bf2-395f-8306-6df9673e06fa | -10.6417 | -46.45667 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a75d723c-a212-31e5-89a3-0cd6197dee5b | -10.71413 | -46.48967 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a47f904a-8ecb-3ceb-9a11-8b79877cabea | -12.9713 | -47.9625 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd37cf3c-5344-3a28-a6bc-1344350f83dc | -12.85622 | -47.14306 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9c8f4c0-06ab-3027-8ff9-ccf2261ee1a5 | -8.96049 | -45.76378 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31670776-04e9-3f06-a5e8-b38c32548aeb | -12.68813 | -48.00353 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82ed0a28-7788-384d-bd4f-a59d8f197996 | -12.11293 | -44.81614 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7b4b0bf-88ae-3e25-804a-1c8462f4163a | -9.06851 | -44.83432 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fda5433-9123-3832-852c-77750a073d00 | -10.23558 | -46.74031 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eebb2d70-aba0-3ea0-93d6-2f3c299bf522 | -12.10402 | -44.8271 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c55be359-7812-3f70-a8cc-a1a347653bfc | -11.11968 | -45.34391 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c680a88-8f1e-3564-a174-ac3ca79f4bfa | -12.62012 | -45.74693 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 07790dfe-09d3-395c-a180-4a8e6e0688ba | -12.65755 | -47.72233 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fdc16f2f-8fed-394f-b35e-0b629b697da6 | -8.39759 | -47.26131 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b3d3db0-465f-3a4f-9ad5-0bd61968c392 | -12.11114 | -44.82813 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9db36ec-6701-34f9-85a6-00af0afac340 | -12.62069 | -45.74314 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1a30233e-f5e0-3ed8-aa93-aaab678c21e4 | -8.97688 | -45.04244 | 2025-09-16 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a28806ed-4563-39bb-99de-b7736f75d258 | -10.71724 | -44.76347 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9bb5656-3544-3dc3-9602-40ee608ae7e5 | -8.1814 | -47.13647 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb8d28a6-ccb9-36e5-bc97-a42588a4dbb9 | -12.76857 | -47.96183 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0802c532-c1f6-3136-9cb2-6b8d24b8cbdf | -11.11509 | -45.3509 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e0f64c7-6c87-3a7e-889c-c8adbed2cb40 | -8.93276 | -45.51258 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a72740f1-2d8b-3550-a6d0-b8663dde9e4c | -8.21923 | -45.58673 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d323beb-1d81-3191-b9e2-ba4b65b47189 | -8.09799 | -45.51709 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README39.md)
