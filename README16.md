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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2881cc0-1352-3e8d-85e7-b5f7c9f056b4 | -3.8538 | -44.53569 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0255b683-1cf8-3ec3-ae78-f1359e0bdeda | -5.07103 | -45.45054 | 2024-11-05 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01f81cf4-e21a-33b7-bb1e-4333a7274948 | -3.00574 | -45.84607 | 2024-11-05 04:08:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05b28f4f-a620-3866-ae2b-d95e93ea1136 | -4.77485 | -43.64506 | 2024-11-05 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bde44100-de4a-3bf1-9253-7a30a471deab | -3.52484 | -40.66401 | 2024-11-05 04:08:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3e2f45da-ae75-330d-bcc2-6141e0ee7517 | -3.939 | -45.00705 | 2024-11-05 04:08:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ae8ae89-025b-38ec-af40-cba376f6269a | -6.48463 | -39.97085 | 2024-11-05 04:08:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6320c66d-d22f-390e-9b13-17ffe290e4a5 | -4.89166 | -46.70505 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e8afb7b-3a3f-3c45-8965-bbe60d0a1058 | -2.80091 | -51.48714 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b90224e6-005b-316a-ac6a-f08efa3b5b8d | -3.08451 | -54.49922 | 2024-11-05 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec481b56-1225-30f8-a956-6efd124b03fe | -5.69542 | -45.84197 | 2024-11-05 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04a874be-0685-3f4f-b198-2d5adeaac14f | -4.89107 | -46.70872 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 945fd24e-93ce-3884-bff8-94f61f068a18 | -5.30433 | -46.24612 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b548da7-7540-3ae8-b9b6-af18b1b041fb | -4.06013 | -46.93456 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ca361b13-da53-3694-ad81-8a0e3428cdfe | -6.10974 | -43.95747 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9481109f-def3-379a-aa7b-c8a5bd457421 | -6.67573 | -37.45897 | 2024-11-05 04:08:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bbb90694-2f57-3bf4-a102-d7f91c9de4ea | -2.26081 | -46.30717 | 2024-11-05 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f9e348a-89c5-39a0-863f-e04a66dfb21a | -2.65584 | -48.56956 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| d2cdd8f6-ed16-3ac2-94ab-c50f918e8bc1 | -5.85593 | -39.42464 | 2024-11-05 04:08:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 06e8481c-f36d-3caa-a178-14a0afb4e6c0 | -5.61539 | -41.76485 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7f21a30e-a2ef-3c4b-ac2c-8239b3edfe26 | -3.76224 | -45.89725 | 2024-11-05 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a5c54b5-3e6e-3531-ad5f-4d7ed9b9bf9a | -7.25509 | -38.94798 | 2024-11-05 04:08:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 270dfed4-65bc-3373-abe6-d0515ab2927f | -4.65937 | -43.81927 | 2024-11-05 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5c6f1a8-e574-350b-b1b9-88fc3b13e6e1 | -6.01497 | -43.9904 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33dfe791-3fbd-3adc-b49c-0d67f0ffbcc2 | -8.37143 | -40.78516 | 2024-11-05 04:08:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9ae9e57-f6de-368c-a0a8-16a031774bee | -5.30688 | -43.19811 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6aa5da36-985f-3411-9505-e026b5032d52 | -3.54462 | -47.3775 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 90ceb580-be28-30b8-ab5f-f29f6941c575 | -3.12188 | -51.10323 | 2024-11-05 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 84ba96a0-f2c6-3ed0-a862-8aca5402c567 | -4.63913 | -45.06955 | 2024-11-05 04:08:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 699fe258-64f9-3fb8-8bd6-2e1013bf202e | -4.88279 | -46.70732 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a225cc9a-8470-300b-b3bd-5902b4be400a | -5.62343 | -47.78499 | 2024-11-05 04:08:00 | NOAA-21 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c0a545d-e4e8-3489-8cdf-7f3fd2db8bc9 | -3.49616 | -51.07491 | 2024-11-05 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f81e4fa-46a0-3a73-b00c-d78dec659c00 | -5.48532 | -41.65901 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7e9f567-c4fb-3b57-826d-966d3ed701b4 | -7.13498 | -46.01002 | 2024-11-05 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f378575c-9920-33d6-8611-b1f11f8b74b7 | -2.77291 | -42.85622 | 2024-11-05 04:08:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ca9270c-0712-36b6-864c-f3ae316e04a3 | -4.88752 | -46.70436 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e43e4ae-ee80-360b-9cf3-1eb56d99863b | -5.98206 | -45.36435 | 2024-11-05 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eebddbe9-d2e6-3b44-b3b3-ca9ecb804589 | -5.94474 | -43.6928 | 2024-11-05 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 578aab90-664c-34b3-bffd-491033b1c885 | -5.51005 | -41.65224 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 76e7477c-5e65-3dc2-87f4-13e3e6dca624 | -6.11835 | -43.97078 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 69566d70-df90-3193-a2ea-567d896fc55b | -3.56023 | -47.39324 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb8aff18-3914-3d51-bb5c-f94e1abff2ab | -4.22736 | -44.23477 | 2024-11-05 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8a16710-e2a8-3107-92c8-5dcc29e2ed2e | -6.10277 | -43.95638 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 810fe440-eabc-321b-9972-16517a687522 | -5.98599 | -42.47954 | 2024-11-05 04:08:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63dbd438-7975-37df-89d8-c584179c9e5a | -3.90305 | -46.43851 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a53fd20-07a2-3d25-925d-f0328ba26519 | -4.38509 | -43.11955 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f80ae85f-7440-3e11-bf85-b3be672dce14 | -3.55504 | -47.39717 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 9cc98a83-158e-376c-99d6-f21743409d35 | -4.72083 | -46.44557 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcbfaeea-af8f-31b1-91ec-c4b7ab1948d2 | -5.29167 | -43.07518 | 2024-11-05 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9936d967-bdca-382d-b7ff-8a1d1c104de1 | -8.307 | -44.93756 | 2024-11-05 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b488b70-3053-30b2-b29e-4bc5fb5adeb9 | -5.3845 | -46.44718 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a267bb19-5da2-342b-bcea-34ca6f7d9928 | -5.9341 | -43.64833 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4c89b86-8896-367d-a21c-248df44a6bc9 | -5.86533 | -42.6632 | 2024-11-05 04:08:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c1e0950f-7db5-3e08-b9d6-1666ed39f3e6 | -5.41701 | -43.32158 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10d8a1bd-8513-3540-901c-4c478443f274 | -3.75824 | -45.89664 | 2024-11-05 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 410e6595-eca5-3ec4-aca7-b48c3e048fb7 | -5.71744 | -43.92075 | 2024-11-05 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ce7e0a0-bfb2-3708-8c92-f8ae0684bd68 | -5.2975 | -46.26303 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7000ffa-1ace-3108-9d38-d34fb68e6f41 | -4.37192 | -47.23376 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b2ffa360-1ef2-36dc-b735-83bb5b56a556 | -1.04117 | -47.78897 | 2024-11-05 04:08:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a347f8cb-dc96-3631-ab67-6bda60f52319 | -4.02592 | -43.23695 | 2024-11-05 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c112f52-31e7-3f08-a769-da1086982579 | -4.90229 | -46.71817 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87cbb3f7-2a1a-374b-a7cf-dc99fb031798 | -6.28248 | -44.96647 | 2024-11-05 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 989a4ef6-f781-354b-b80c-17cd46760b02 | -5.83582 | -43.64825 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1fefd3b8-3602-3c61-a703-0e8db39f5970 | -3.69772 | -44.61957 | 2024-11-05 04:08:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 934d91d1-35f9-3370-97ce-d035aded58fa | -5.29637 | -46.24464 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53b8e059-30f2-34c9-ae74-2a53b8cf2504 | -4.01512 | -43.629 | 2024-11-05 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 325fdead-1ad1-3007-a6e1-f3c9bd6100f9 | -5.90938 | -42.98565 | 2024-11-05 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 59f99960-e180-3ac7-a85d-b58d67a7b7a4 | -3.08426 | -54.51693 | 2024-11-05 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 571d0535-7da1-3971-aff7-cf13ac8a99a5 | -2.4692 | -50.23372 | 2024-11-05 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 697fe81c-85a1-3d29-9ec4-0dc09eb4c0f2 | -2.78732 | -48.71908 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb8471f2-2e73-3b12-9538-33f4a97d4645 | -4.60395 | -46.8745 | 2024-11-05 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f86d732c-b5ef-3999-8ad9-b84494cae131 | -5.29618 | -40.53677 | 2024-11-05 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13499808-dc36-3026-bfa1-3917ec173a48 | -5.85942 | -39.42503 | 2024-11-05 04:08:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 1dbf5ee1-fb24-3ced-aa94-b0de9cfb64d7 | -4.31657 | -44.73557 | 2024-11-05 04:08:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46ee05c8-743c-34ed-966b-d306a09a8450 | -5.51572 | -48.07854 | 2024-11-05 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a53b05cb-e553-3391-8e2a-5dde80204b96 | -4.83413 | -42.79103 | 2024-11-05 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 813eefdf-d9d8-365e-8680-ee714aeacf86 | -3.97073 | -48.16312 | 2024-11-05 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f685785-9828-39de-9da1-e2373c6e7ab5 | -2.21577 | -46.42817 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13b4f596-5be8-3d9c-9b24-207eaf50f1f0 | -3.09363 | -48.14214 | 2024-11-05 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33d0102d-bb32-3794-b13f-4b70061556f6 | -8.49357 | -42.09066 | 2024-11-05 04:08:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 583f7a29-c065-3388-9dd5-6461daa9d592 | -3.95679 | -46.36821 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8abcb797-8fd7-3463-be64-3390191110bf | -6.11773 | -43.97467 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43c069b6-b73a-3a02-bb9e-09323c10d2a2 | -4.60881 | -46.87123 | 2024-11-05 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 454739b9-1f77-38b7-8862-ec20734f5f06 | -6.25248 | -43.56638 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5818ade1-2bda-3c34-b32d-6eb51dcde5ec | -4.59975 | -46.87374 | 2024-11-05 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 91f6998f-45bd-3b77-a6aa-d03594d1ff7d | -5.87273 | -40.16859 | 2024-11-05 04:08:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4b905778-4a12-35d0-888c-121c9773150b | -4.91693 | -44.36184 | 2024-11-05 04:08:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b80a8f05-201f-3361-82ee-8235078376df | -3.96855 | -46.37372 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ea927d3-f171-374a-8b6a-3940f0c2c749 | -7.60203 | -38.85198 | 2024-11-05 04:08:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 118d3721-3666-34be-97e8-4ea2ecf2c4af | -3.91815 | -46.47582 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88148045-52b5-3479-b1c4-711a49cb82ea | -6.13474 | -44.70142 | 2024-11-05 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15a6abfa-edd1-34b2-a51f-cf45a20c0f0d | 0.04883 | -49.55859 | 2024-11-05 04:08:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51bdb9a5-d4d9-3e3d-a2d4-ed462a6e0e0f | -2.53099 | -47.52571 | 2024-11-05 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35aca4bd-0cb1-3fec-aace-20853f78de8e | -7.54363 | -35.12801 | 2024-11-05 04:08:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7260551f-344d-348b-aec7-816938903f95 | -1.92939 | -46.45319 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ce185de-d2a1-36a8-9646-ff5f099e8390 | -4.38793 | -43.12381 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0c98415-252b-3c4b-9708-58b058421f19 | -5.51506 | -41.66777 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a424e0d0-e895-33a0-a853-6e5e8ad53b4b | -3.5469 | -47.39129 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cbc860a-1835-316d-b581-ea86976fc996 | -2.6502 | -46.76981 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b58fb821-4611-3d0e-a5ee-5a075871a1dc | -6.24669 | -41.64201 | 2024-11-05 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README17.md)
