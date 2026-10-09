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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a46969c-2b81-3653-be22-bdb660c134f6 | -5.99331 | -40.98391 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 991d7270-8e93-35cd-aab2-87b3fad09739 | -6.8213 | -39.31946 | 2026-10-09 03:42:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 02e1096b-07b3-3b64-9ca6-5c4aa1bbbff4 | -4.93441 | -45.72648 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 544e8ce7-d1c4-382e-ac67-d16352eb0e56 | -2.08478 | -46.57777 | 2026-10-09 03:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4029e6a2-822a-3628-99e7-b0c0deff79e7 | -5.99452 | -40.94792 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e873e188-55c4-3a3d-8713-ee1880de902b | -6.60033 | -37.90425 | 2026-10-09 03:42:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 50decc25-36f8-3381-abff-33ee37c34c45 | -6.00219 | -40.9597 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 36.3 |
| 82df2d80-af5e-31a1-9147-0993905be27d | -5.43934 | -43.44852 | 2026-10-09 03:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d80c930a-2169-3a4e-8669-d9e5b733dd55 | -6.00268 | -40.9856 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 72eb61ce-bf17-3b89-8b87-5f9b81c68600 | -6.21746 | -44.15665 | 2026-10-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ac22b09-21ef-3042-88a5-f2e4dd58d51b | -5.99883 | -40.97973 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| c8ea31db-9521-3496-9c6b-aee07c99a2aa | -4.08781 | -45.90527 | 2026-10-09 03:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23d441a4-1922-3e48-811f-0e2c02ced594 | -7.06615 | -40.95209 | 2026-10-09 03:42:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2f1e35ca-ab8d-33ab-99a3-f9c287460dd0 | -4.07578 | -44.11699 | 2026-10-09 03:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b43ad15f-6b18-3ca1-9927-e7d879fd31d1 | -6.8066 | -41.24233 | 2026-10-09 03:42:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 42d72446-780a-3007-b30f-24d0282e6790 | -5.87484 | -43.41861 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 40ba69f5-64cd-39ae-b549-8090a91ea492 | -6.04201 | -44.03542 | 2026-10-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a86158b-bf09-387d-b0e1-6d9433b6361e | -6.00135 | -40.9647 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 43c0d699-37f2-3c08-a827-59c43c60bd43 | -5.99456 | -40.96093 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| d2b4aade-4878-3a19-9854-b0e6fe2371fe | -3.02867 | -42.11282 | 2026-10-09 03:42:00 | NOAA-20 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36701da0-1a59-39d9-9c0a-5df1c982ce4b | -7.11645 | -42.54186 | 2026-10-09 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3f74884d-443c-326d-9633-6b112ee6b370 | -4.01747 | -41.76968 | 2026-10-09 03:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| fd383d5f-b0be-3aca-abc7-71017156ec5f | -4.01486 | -41.7683 | 2026-10-09 03:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 123bb697-e9b9-3880-89bd-233bf77344fb | -6.16359 | -39.44257 | 2026-10-09 03:42:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 5a66843b-e464-3f96-9ea0-60fda93ff092 | -4.75702 | -44.00881 | 2026-10-09 03:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08ffc148-0720-32e6-923b-1b94a2258506 | -6.00129 | -40.97759 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 926e9c6c-4583-378b-a60e-57683171695e | -5.41731 | -44.62932 | 2026-10-09 03:42:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 627eccea-fcf7-3dcc-b172-1f7c671a4a65 | -5.48768 | -44.30092 | 2026-10-09 03:42:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffad324f-ace5-3ab9-aa5b-be0e152fbfb6 | -4.93306 | -45.73223 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a045ce5-fa40-3af6-baae-10c858c4575c | -5.43867 | -43.45236 | 2026-10-09 03:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7649d73d-14ea-3b35-b19d-a36e6d04be31 | -4.01997 | -41.76921 | 2026-10-09 03:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2ea76eb6-4155-3f36-9cf0-5a21da0f31a9 | -5.61759 | -44.38006 | 2026-10-09 03:42:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| abc8fbcb-fbc9-3cf2-8785-7a174e077c6f | -5.99967 | -40.97472 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 8f354c02-1593-3455-a2b8-b321d6af8a34 | -4.02571 | -40.65121 | 2026-10-09 03:42:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f5c82f13-246f-3c71-bd46-6d35fba81354 | -6.16224 | -39.45041 | 2026-10-09 03:42:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 487a1fa4-9b45-3f0b-bc77-d614cdd95688 | -5.3444 | -45.18411 | 2026-10-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97b3e1e2-087d-3d61-81ca-67212a75129c | -5.09477 | -46.22174 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ff1de00-b838-3e1d-8677-d016a4620c31 | -7.40674 | -35.19383 | 2026-10-09 03:42:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2e155c04-4edb-3107-a564-ff66d4ef68d4 | -3.02922 | -42.10955 | 2026-10-09 03:42:00 | NOAA-20 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99122bf2-d7b3-338b-a3e1-e42f72ea8f4b | -5.33902 | -45.17813 | 2026-10-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c843bd4b-f7c3-3ddb-aece-ce62fcc06717 | -6.16492 | -35.29466 | 2026-10-09 03:42:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7df63a49-5031-3d23-a206-ecfeb892671e | -6.81539 | -38.54984 | 2026-10-09 03:42:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a73af1e-bfd7-3ef2-8c65-dbc067533f90 | -5.9972 | -40.9459 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 38642342-e0c5-358e-867e-4159f0db8739 | -6.00602 | -40.96561 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 3b97120f-d420-37a2-bbce-38df0ea2a08b | -5.99537 | -40.94291 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 67c8cbb0-22a6-3747-8853-494c91e8112f | -6.00216 | -40.97259 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| a77e5268-be0a-3461-b05d-5398c4437528 | -6.79745 | -39.33495 | 2026-10-09 03:42:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d65b327e-1e9e-3189-8b38-85809354bf93 | -7.40339 | -35.19327 | 2026-10-09 03:42:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5bb1d9d4-35a8-3365-a834-eb45ed95ef63 | -5.08806 | -46.22073 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa6f7c73-d303-390e-84b1-4aecb180de0b | -5.99583 | -40.96887 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dd87cdce-a684-3785-9028-f147ed94e8d5 | -5.08909 | -46.21486 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fe3ed96-ec1c-3302-a18b-d2645169f84b | -5.61458 | -44.38334 | 2026-10-09 03:42:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9f2a855-0f89-3a49-9b64-73c3824ff614 | -4.97559 | -46.04512 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1569f04-44ef-3486-b09b-48aeb94f6eb7 | -6.79682 | -39.33867 | 2026-10-09 03:42:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d2c93102-7db5-3dc1-93cc-8f0ca04ea076 | -5.67127 | -46.36615 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f56a0f50-0158-3849-8795-c239076f34ca | -4.98337 | -46.04 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d77d163c-8f44-36d3-a0be-986fded62e62 | -6.82818 | -39.5663 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| da011360-499c-397c-bae6-1191c16a6356 | -4.88534 | -43.34184 | 2026-10-09 03:42:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb7513ed-e389-38cb-9cd2-f3d80bcd99e0 | -6.11601 | -44.81744 | 2026-10-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acddb7f9-453f-3788-8458-ed1e29af3c14 | -5.88054 | -43.41338 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e9420aa4-7154-3dd3-8402-e64e13c2a6fd | -5.88165 | -43.41228 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d4f88b46-b3cd-3e5f-baab-eb64d4c50154 | -6.81935 | -38.55039 | 2026-10-09 03:42:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ee5326f6-d79a-3cef-a71a-7c101fe05532 | -6.00011 | -40.95676 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 491813f8-32e8-31bb-9439-c2715aeda51c | -7.38304 | -39.97321 | 2026-10-09 03:42:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cbd6fc17-a45b-33bf-8552-5c07df741c99 | -6.49866 | -43.95462 | 2026-10-09 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c0a0228-6aa4-3df0-9b8b-56deda8f316b | -6.88008 | -43.69389 | 2026-10-09 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6fc8ad92-82f2-3ddc-b6fc-d28b1b9deaa9 | -5.61207 | -44.84626 | 2026-10-09 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 919f43e2-d39b-336e-9796-759d798220a9 | -5.37965 | -36.82204 | 2026-10-09 03:42:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| df69d0e2-8e95-3e15-9a44-0c49b0cebd1e | -5.99367 | -40.96597 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 23b97272-4bee-3ff2-a6b4-6e7a7618ab5c | -5.1044 | -46.22572 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd15a8d6-fa79-3a4c-8e85-fc735ca34356 | -5.99836 | -40.96675 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 77fe604e-4494-3041-8b2b-aeb5485b7795 | -5.75582 | -41.64219 | 2026-10-09 03:42:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7ee01ea4-6a42-3e46-b21b-6ebb35e4d3d1 | -5.99341 | -40.94006 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 907e0908-8850-3ac4-a410-e52941e735d4 | -5.99104 | -40.98095 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| d66c1f5f-27da-31f6-8380-e142cf7748f0 | -6.83187 | -39.39387 | 2026-10-09 03:42:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ec7e63a2-379c-3df1-8da3-33b541fa1236 | -5.34247 | -45.18028 | 2026-10-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 48d890fc-0305-3522-9468-160c4c5dda5e | -5.99835 | -40.95382 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| dedc818f-5baa-323d-965c-d1f2f2350d70 | -6.15574 | -47.27752 | 2026-10-09 03:42:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 22141f3a-8c34-353d-a564-091ca4cb2905 | -4.97826 | -46.04499 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61147d24-fd14-3cab-b033-4850ba4cb942 | -5.23936 | -43.98082 | 2026-10-09 03:42:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d8ce53a-3b2a-3d11-bd68-4b78fc0f0632 | -6.24388 | -45.32914 | 2026-10-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b35d3777-8e5b-3549-9d82-b7228fe24b5d | -5.09312 | -46.21199 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32ac137f-88eb-344b-b517-27f14d2c3e97 | -5.88522 | -43.42461 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5a090e52-c277-3962-b12e-9a29fdeb8866 | -5.99799 | -40.98475 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 486d38f2-d000-39ad-9e5a-4872ec9feb16 | -6.15451 | -39.44492 | 2026-10-09 03:42:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1be0389a-98af-3eeb-ba2c-02e253e05738 | -6.00976 | -40.98439 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 20295690-98c6-3c37-99b0-2200bd625f3f | -4.08321 | -44.10962 | 2026-10-09 03:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1acbbf8-ac16-3581-a5a6-ba7da2890496 | -5.95323 | -40.93578 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 00b2e2fd-841d-342d-8e87-99b65aaecd3e | -6.59502 | -37.88914 | 2026-10-09 03:42:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8c0cc5f3-f375-30be-a65a-39a1b2aa1a04 | -3.20793 | -42.95872 | 2026-10-09 03:42:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d813e6c4-7517-30bf-842d-97735989c010 | -5.74605 | -43.27879 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| be8a19c9-d440-3c0b-a9db-ab07faecda4a | -6.00099 | -40.95178 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| e102da0a-fee9-383a-83ba-79b6336c6266 | -6.83722 | -39.564 | 2026-10-09 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 15e9dff3-b4d1-3195-bfdb-bd03392c6628 | -5.87547 | -43.41496 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ebc1dbf-6866-3435-8958-ef508ab4f2c4 | -6.01148 | -40.97449 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| cd048aa0-4b4f-3962-81f6-23424464b9db | -4.93337 | -45.73236 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 075efe8b-0467-31f0-bdbd-3578e0e1c9a3 | -6.18621 | -39.38623 | 2026-10-09 03:42:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c900662a-ec9c-35d9-9e18-f03015eb2e40 | -7.05609 | -40.95554 | 2026-10-09 03:42:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6c1c2455-76d4-34b0-b527-0127e2dcab50 | -5.99632 | -40.95088 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| a2e6a352-137f-371e-9b3d-4aca7c806783 | -5.88025 | -38.9802 | 2026-10-09 03:42:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README60.md)
