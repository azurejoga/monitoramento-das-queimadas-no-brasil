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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81444ae8-19d1-33df-8d78-ba2babe51e58 | -15.25956 | -53.79342 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 454dd7a0-e98e-3cc1-a87f-c6eebfa2030f | -15.25129 | -48.81552 | 2025-09-09 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 783a90cb-0571-3317-9c6b-b169762dcb6f | -16.06723 | -50.491 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a217fb4-4011-34f4-ae03-ddeb52eece6d | -16.53691 | -51.76413 | 2025-09-09 04:36:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50fd7f15-3520-3221-90be-ecc4a6668f2e | -16.34904 | -52.93847 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d782c555-65c1-396f-a141-65b0353481f4 | -15.54138 | -48.39861 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ddd520a-372c-3cec-bc98-2b9cbfbce20d | -17.68102 | -52.26746 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10907110-169e-36ae-ad1e-d86d1613ee81 | -18.555 | -44.04716 | 2025-09-09 04:36:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bef67a7-2ec4-3dee-922f-978cfb2d3d76 | -15.56569 | -42.717 | 2025-09-09 04:36:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d7448999-5960-354b-8717-4cca749eb05c | -16.43857 | -49.29644 | 2025-09-09 04:36:00 | NOAA-21 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 434b2fe9-0b21-382e-8853-9e56017bf54a | -15.52834 | -48.3696 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47f7fcd9-d2bf-3d99-84fc-f8d70afee569 | -16.29049 | -45.68599 | 2025-09-09 04:36:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d7bcd38-7cdc-3985-8916-65a7f25c81cc | -15.76772 | -53.54998 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e15a303-a1be-3ebc-8b3d-e5c3481d2f5e | -15.14865 | -48.07061 | 2025-09-09 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d72ea5d-5598-35c1-8e9e-f5a469d1a121 | -15.70401 | -49.89993 | 2025-09-09 04:36:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| db09a273-def0-3111-a822-868a66ecdb93 | -15.21683 | -44.04068 | 2025-09-09 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 082cdb30-2e03-3ed6-aabf-9db82adfe2af | -15.87076 | -52.20081 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2f54e002-5fef-3ccf-a2a1-48aad631a76d | -16.0711 | -50.48798 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7eff2578-bae4-32a2-87b5-4fc0802a844e | -15.25587 | -53.79275 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9175e49-de3d-3884-955f-8abdff0f0800 | -14.54548 | -48.76783 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d72b7bb-7062-3c41-bbc1-853aa05b13fd | -18.77571 | -48.19522 | 2025-09-09 04:36:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4546e38-f781-36f1-a3ab-ef35bcb6c6bf | -14.36967 | -60.30705 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0444485a-6e08-3b0f-b930-b4d8f6a876a0 | -19.99669 | -46.95671 | 2025-09-09 04:36:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1661fb4d-2b56-33f2-bcec-87709a1a5863 | -16.29438 | -45.68657 | 2025-09-09 04:36:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b66197e4-5d3e-3ef6-ae1b-2e99af20e00e | -17.26638 | -46.68461 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a1a583ca-68ef-3897-b442-b3260300c70b | -17.94999 | -46.92852 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9894846f-2215-35aa-97ad-4dc8ee9edfdf | -16.07771 | -50.48909 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06edddd6-faad-3a29-9052-d33792891ce4 | -15.74178 | -53.52757 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c09f9d43-14d2-3720-83a1-fa5cce1009a0 | -19.73468 | -43.91257 | 2025-09-09 04:36:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 086f85a3-1179-3b37-8412-30ae04ab5a7e | -15.81718 | -52.27018 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c70dab27-3bb8-3155-a10f-b6170aa6df11 | -17.2997 | -46.71801 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4c1ae23f-c017-3ab1-8bde-edcfe29c86f2 | -19.83363 | -48.16922 | 2025-09-09 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 993fc80b-907e-34b8-8507-4233f7b7d673 | -15.81981 | -52.25433 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2840652c-aba2-325d-b45e-73ce33437d8c | -15.52728 | -48.40014 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 15852841-e3b2-3b01-8095-b2d485d4e276 | -16.33225 | -52.93124 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 490cb010-d34c-37b1-8b83-358f66ce5d15 | -12.8734 | -62.09674 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a8c5326-bc89-3979-94cf-d623af6c2fe3 | -16.43578 | -49.29227 | 2025-09-09 04:36:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c9b7d85-ae72-39cc-b3a7-e8cbaffcb183 | -17.72562 | -44.49268 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b453d91b-b8b7-3209-89a7-7b7abbdcad34 | -15.27701 | -53.79551 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a025fc3f-197f-349f-95fa-73b52923d19a | -17.28059 | -46.6916 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0dcac4c-a702-30b5-aa7a-fca1768aca81 | -15.11956 | -48.05456 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12dbbe9b-fc88-3ca4-b6ba-fe2fe8c53ae0 | -17.08418 | -49.23095 | 2025-09-09 04:36:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f899f72c-412a-3afe-8050-b622488b675c | -19.82652 | -48.16814 | 2025-09-09 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c29d9d9e-ce66-3c43-bc2d-30cd357dbdbc | -15.0488 | -50.13071 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3805e00-ed4f-3e94-84af-7752e7cf6a46 | -15.52673 | -48.40384 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35ac5e32-5159-3e70-bef0-57a9d1854493 | -17.73421 | -44.49347 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fb91449e-9b73-3907-8c06-8f3c5f68c9f9 | -15.53851 | -48.37125 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9266ac5-f38f-344b-816a-25e849fe3719 | -19.99734 | -46.95181 | 2025-09-09 04:36:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80a3391a-531c-378f-87dd-2ce7606fa5cf | -20.07284 | -47.36152 | 2025-09-09 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ad4a732-2f94-3cb7-aa21-e534ebb296a5 | -15.27622 | -53.80003 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17734ea7-0b27-3b3d-80c1-d7e2a540b611 | -18.4649 | -49.5494 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d25df72-50c4-3757-9b50-ddb4c39893f2 | -14.52122 | -53.96942 | 2025-09-09 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e016d050-2524-3e68-a87a-5c9e094c2121 | -15.26368 | -52.36363 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5329b502-c9ea-39b4-8099-b19f1db2e58b | -14.53008 | -56.22607 | 2025-09-09 04:36:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 43b2d55c-cd54-360e-a1b7-e21792dfc994 | -15.26517 | -53.79792 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a1164ed-97a3-32f7-a0fa-df1ec4a25e4c | -16.95384 | -45.81612 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f21914d6-bbf9-3d84-b32a-24d858a5488e | -15.25184 | -48.81187 | 2025-09-09 04:36:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8abdb6f-6fe7-36de-a52f-0adc79ce139b | -16.43912 | -49.29278 | 2025-09-09 04:36:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 172aa636-377a-3d8f-8915-a55e936624ab | -16.34273 | -52.93312 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 605746d8-cf0e-3cac-a4fe-5631b98cb2ad | -15.73462 | -53.58581 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95da5383-65a4-3347-b615-af7a09d32be5 | -17.28493 | -46.6875 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c0a24cd-2d87-3f4f-a676-ab96d022fc63 | -15.78575 | -53.57527 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f095ccf4-e0b7-3434-adf0-74161287bd90 | -15.54194 | -48.39489 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62b50c4f-d656-35a4-b11e-4cc54a0c65d8 | -20.17444 | -44.79435 | 2025-09-09 04:36:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 545c7785-5e7a-39ef-ab3b-bd7274a21bd2 | -14.79619 | -48.22691 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84c84939-8d0d-305d-9e7b-9d607fa0ac5a | -14.5293 | -48.73925 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 29cb78e5-692e-32ca-9d58-ddbf38bc024c | -16.07054 | -50.49155 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e1748c3-6f7d-3fe3-b44f-d70f10a3ba1a | -20.7062 | -46.61687 | 2025-09-09 04:36:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2064084d-e6f3-3591-8520-2ec1f1ba4f19 | -12.87639 | -62.11477 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f54c836-7e43-3547-9ffd-6134dc426517 | -14.62568 | -52.15969 | 2025-09-09 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e83bfaf2-97ff-3d27-934a-9f15cace71ea | -17.5637 | -44.54652 | 2025-09-09 04:36:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2de35077-e71d-375c-b92c-7f109c439581 | -18.73847 | -49.63206 | 2025-09-09 04:36:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d17f987b-b453-34b4-bbbc-0c0693b20d38 | -14.76727 | -47.78352 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e6133ce-54e3-3b1c-987a-3c3b5d307634 | -15.27093 | -53.80842 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbedf828-91ab-3023-9ab5-7aecc132d0a2 | -15.87492 | -52.34452 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e205e95-d809-3862-80a2-a1066d63a357 | -15.11671 | -48.05018 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61615263-28c8-39fd-accd-1af9cbd1a788 | -18.34093 | -49.38489 | 2025-09-09 04:36:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| be907be8-0cb0-352e-a120-d658ff259980 | -15.78027 | -56.42044 | 2025-09-09 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f25517e4-cf74-3e3a-a53f-fe7d47cad30c | -14.52918 | -53.27098 | 2025-09-09 04:36:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e09fc4c-123f-3931-8dfa-ed8a0ddfe13e | -15.53067 | -48.40068 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2d2cf2a5-8f96-350e-be1c-787b7f234812 | -15.78885 | -53.53569 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a96d81e-de3e-37ca-b4ad-d5157006e208 | -17.72327 | -44.47694 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7073fea1-7cc6-3ba5-ad94-8af4d0b7f577 | -19.49357 | -55.0104 | 2025-09-09 04:36:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6983dfce-7ac7-3174-99e6-ddd23c50738f | -15.26461 | -53.80844 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cabdf6b-12bc-396b-9e1a-2cbbd6084eeb | -15.81573 | -52.25767 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33898b7e-21e3-370c-bcf6-f921889c2933 | -17.30033 | -46.71343 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 33ac029f-bc5e-38d5-ae21-33ba8321013e | -18.66712 | -47.54648 | 2025-09-09 04:36:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5b262c54-f714-3f0a-acfa-65230319da60 | -16.28342 | -45.6798 | 2025-09-09 04:36:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 297ce17e-f673-332e-a4ec-eef74cf5bf6f | -15.10765 | -48.06438 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5084f3a3-2611-33b5-8a57-3e0b018833aa | -14.52205 | -53.96466 | 2025-09-09 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 61445b84-96ad-3877-ad29-b89f73b6d9cb | -16.2018 | -44.21825 | 2025-09-09 04:36:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7148f035-06d2-3f76-94f7-f65fd7e946e1 | -16.07166 | -50.48441 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8237d84f-78c0-3a02-9cfe-24e5a3ca7130 | -20.07536 | -47.35923 | 2025-09-09 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25f0f1b4-fca9-3658-a8a9-9424137eada7 | -14.53988 | -48.73723 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf0b2658-eb2b-3ea4-8693-a7d15f435309 | -15.29237 | -46.97839 | 2025-09-09 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4686187c-9aef-3089-8fab-7f9298912b58 | -15.77947 | -56.41158 | 2025-09-09 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e2e9b293-dfe9-300c-9084-0de17d043c77 | -15.17637 | -47.9539 | 2025-09-09 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 639ddbd6-ef2b-35e1-a5e9-2205b3e627ca | -17.0853 | -49.2235 | 2025-09-09 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 256eb1eb-29c9-3c5d-98c2-8ecb15b43d8e | -15.2586 | -53.79204 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c83ba33e-68e8-33fc-9ae6-cd9a8b67f2c8 | -14.54159 | -48.7709 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README50.md)
