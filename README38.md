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
| 7990fff0-3101-3dc1-a4cf-5535ab5c0644 | -6.11396 | -55.70567 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| b705ff02-2dd1-3ba3-b70a-7939645f7e0f | -13.17896 | -54.36866 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 312f171e-5ec7-3f5e-bed5-21572bd39999 | -11.9763 | -57.62051 | 2026-10-09 00:35:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 2d05a689-808d-3396-a380-bbfc6bf880fd | -11.1533 | -54.80612 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 28536845-2b24-3a28-a3a0-1a2175053eaa | -7.20691 | -55.19333 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0feace86-5d70-3005-b635-a29e3ec8dd47 | -10.02811 | -48.04803 | 2026-10-09 00:35:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| bc68d725-efcf-3346-9e3b-e3fdf2ab193b | -7.22199 | -55.15512 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| db8a86df-44eb-3300-bf3f-602db5f699ca | -13.20659 | -54.35289 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 616bb483-3816-32a5-b77d-f63a3dc8857d | -7.03121 | -55.67948 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a0454847-3e83-33c1-b75d-3c48ec895e95 | -4.0825 | -59.84156 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 61c206ab-5c59-346d-88a6-6c9d5756e2c0 | -3.74355 | -60.59893 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 10ddc67e-4cc1-3734-bb98-4ad524c23a47 | -3.2526 | -54.03569 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| c6080639-8983-3801-926f-480ed93bde4e | -3.16627 | -61.09162 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d4b2642c-7877-3317-8bc5-11daf9bc975c | -3.97715 | -59.33517 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9c28ad4c-470d-32df-b042-fd27b8371586 | -4.79535 | -56.14956 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 154a5927-c35c-3a52-b91e-e820c62e09cd | -2.88205 | -54.18038 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 5772518c-4ff5-3e39-8bf7-2ad68cb1a5fe | -3.72289 | -57.10968 | 2026-10-09 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d83472cf-9371-3fc1-a304-817ee387d655 | -2.89125 | -54.07907 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 9e946c00-f4ae-3b0b-a16b-ed2b955e571a | -3.07339 | -59.1375 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7e58aa13-de25-3abe-997a-f80a7a4a4086 | -3.48528 | -59.38678 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3e395994-14bb-3980-8242-5e88ef7dd6cd | -3.73564 | -59.45898 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| f403114e-ca45-3c65-886e-979d01162488 | -3.30686 | -53.6944 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 9c25af22-092f-3bba-9311-2fade37ff045 | -1.30899 | -54.1923 | 2026-10-09 00:37:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| da413887-62ab-3643-b171-444ee5289992 | -3.94555 | -55.85104 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9c773dd6-3c19-33d3-943e-20c00f10ec3a | -2.85199 | -59.27659 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7bc50d8c-87e4-311d-9fb5-307a622c9b8d | -4.74648 | -55.65642 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d43dceb3-1fc9-35bb-9b42-3cb3da39cad4 | -3.28299 | -61.00558 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1e54b1e0-13e2-3752-bbbb-89879274190f | -3.40978 | -59.5736 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 124c5949-f8bd-3495-9da6-02210876370e | 1.75687 | -55.56064 | 2026-10-09 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 3cd92877-cde3-3886-beab-ad6e61b87a55 | -3.18014 | -58.64107 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 18cf49c2-35b2-3bf7-8705-f5650720afd3 | -3.39521 | -58.00003 | 2026-10-09 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3d7e37a4-fd70-33ea-921d-2543eb763d22 | -2.06729 | -56.88968 | 2026-10-09 00:37:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7360ed7f-7b19-3f87-b6eb-0c8d656c8221 | -1.1293 | -57.28348 | 2026-10-09 00:37:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7c58836b-8cd7-302c-9f0e-dd58486d55a2 | -2.76029 | -54.11036 | 2026-10-09 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7cbf64ce-7faa-3b37-a161-07611f0f796f | -1.13076 | -57.29392 | 2026-10-09 00:37:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 21265c37-4b45-3698-9260-073e11d0e27b | -4.28184 | -49.10067 | 2026-10-09 00:37:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 8b232049-6adc-3fcf-8f89-9fc45651337c | -1.54873 | -54.55308 | 2026-10-09 00:37:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 702c6f2d-3937-3daa-932a-fd9f99265436 | -3.864 | -56.00023 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 9ba53fdd-b4df-3c05-817c-4eae88914214 | -5.08867 | -56.19928 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f1b15d98-f07d-3819-bb7a-dfbaafb2b18f | -2.49684 | -56.16896 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ddb93551-a0ec-3b96-bf3a-659f88198d95 | -3.29506 | -53.99589 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 6ade9efc-edb5-3eb2-b890-65595041c1c5 | -3.55684 | -59.43348 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| cb492411-4665-3bde-8dc5-551334331f81 | -1.8324 | -56.17272 | 2026-10-09 00:37:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| ca2ce6e3-9913-3a55-909a-5368768dedbb | -4.12526 | -59.88993 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 61dc7776-30e3-3001-a2ab-5ef0a3976f59 | -3.50746 | -59.2704 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6d4b1bce-f3f3-36ab-8857-d20b1f40caea | -2.5919 | -59.98407 | 2026-10-09 00:37:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fa9d07c3-be1f-3718-baf9-f4238ba983f9 | -3.54551 | -54.62707 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 67b5fc21-8b05-361f-8122-5ede5c0a9613 | -3.5069 | -59.34798 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 17bc6fa7-ef03-3885-8327-003dff61a7f9 | -3.00873 | -53.91983 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 22bf45c9-ba79-3d21-8586-7968bafa6a2f | -3.28509 | -57.86956 | 2026-10-09 00:37:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 352c7d75-3042-355b-95cf-de1454678ab1 | -3.45059 | -60.27814 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2360aeff-6af3-3e4d-9e71-ad240f292932 | -2.74848 | -54.11212 | 2026-10-09 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 71de12d0-66a7-3e9b-889a-7b932337d6e4 | -4.29552 | -54.80316 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9f64b726-5db4-36ff-ba30-6f49accee7a8 | -3.19543 | -60.43287 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d28ecf3a-7462-37c2-93fd-6f6792f9b235 | -3.17178 | -58.8417 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0a47ba23-653f-3868-a5aa-93dbf936c7b5 | -3.1789 | -58.63214 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| e30b1201-00d4-3889-9298-3045b63f89a6 | -4.69411 | -56.2255 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 917ab4f4-6cf2-3b43-bf76-a7dab70069c3 | -3.67077 | -60.60552 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2731052a-2008-3ed6-a18b-7daa1579e605 | -3.87315 | -55.99242 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 55b4378e-fe63-3e9f-b515-3ade7d1545e6 | -3.71391 | -58.84353 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ac437429-dea3-3b9a-80a4-1c14b5fcbf97 | -4.03978 | -54.22849 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| c0067fc3-5c86-373a-b55f-bf84bd94eb12 | 0.44774 | -60.53334 | 2026-10-09 00:37:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| b5b364d9-fc96-36b4-9e0f-77b38266fc68 | -2.03222 | -56.9441 | 2026-10-09 00:37:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d18219e6-d7d4-370b-ad4c-56e53a340b5e | -3.55042 | -55.52948 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7b762a57-b8a4-3044-a1fd-19d70d33c69e | -2.52471 | -58.10194 | 2026-10-09 00:37:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4c5e21a2-8667-3c9f-88fe-e1e2cdf6243b | -2.07545 | -56.87753 | 2026-10-09 00:37:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| fbb65d15-ca95-3960-aa16-c17e5bdeeb44 | -3.40458 | -59.60119 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ec31f8a6-4fab-3099-8951-fac9cc658acb | -3.12364 | -54.16598 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 29a8f709-876a-3d80-b384-d5ceb6c8089c | -4.74807 | -55.67338 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 06739881-e658-31aa-a2e6-b042a1ed8d74 | -3.77274 | -58.52426 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cd5c1b44-8f92-3e8f-921f-dca0bccf7365 | -3.6928 | -58.28481 | 2026-10-09 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5939c88f-37dc-306b-a106-1ceabc2af97c | -6.086 | -62.50658 | 2026-10-09 00:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3c990b28-e8d3-3b05-9237-0782295f736d | -3.64625 | -60.62763 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c67ae278-4b69-3c07-91ce-58556b36b9cb | -3.20541 | -50.84155 | 2026-10-09 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| cbe56b8b-97b2-36d7-8113-18bb763fe903 | -3.54277 | -54.68711 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 593baa02-d230-3db9-afcd-e12c9875e8cd | -3.11199 | -54.16787 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 78008ddb-af30-3d84-ab9a-33daf8f4a7b9 | -3.43696 | -57.96892 | 2026-10-09 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3fd54941-3fed-3e6e-bc97-564a8bce9463 | -3.89958 | -59.44174 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 46123b1d-4050-31e4-8d33-b0210abb0265 | -3.77057 | -58.58509 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 011a27b6-23c8-38bd-8809-10c4e62c8782 | -3.44384 | -59.5599 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 74dff38f-d5cd-3738-91d8-7183baea621e | -4.66329 | -56.21904 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| c3a6882a-0183-3afa-b7da-3a184c06a693 | -3.10492 | -54.20154 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4b67d772-b1a3-3378-a395-0d425e6efe2d | -3.65798 | -54.5303 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d1f7f2fd-6515-38d7-9991-435ce2c0dc1d | -3.10752 | -53.79435 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 67251139-ceef-3f6a-be88-a6ad34bdf025 | -3.74972 | -59.62729 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a4191bca-1e23-3df9-ba67-0665ec177c5b | -3.00213 | -57.75475 | 2026-10-09 00:37:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 593b6fc5-2607-3303-b2c2-72d7e5a8c860 | -3.82925 | -59.40382 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1c0945e7-16f5-3531-8cbd-ddd5bb3ffe00 | -3.68981 | -60.54089 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9f0cc456-ee6f-3bc0-bfb0-79de0b2f24a6 | -3.09034 | -59.26053 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 00b8096f-1de9-3fed-a1f8-398d3f6b243f | -3.58705 | -61.61628 | 2026-10-09 00:37:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6009499e-06ea-3afc-bc78-ddb23cf3d202 | -2.987 | -53.85302 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a987c561-db2b-3402-a577-a09a686a79fd | -2.57092 | -56.18824 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6e1e68be-a2ef-3678-a55d-f207c592af63 | -2.83284 | -54.14432 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 0bbdd887-2cb7-34c0-8ce7-35247cdc2893 | -4.58201 | -54.95082 | 2026-10-09 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c0d4f030-481a-31b5-a4b6-3b80d8420d8a | -3.74204 | -59.44019 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d6bfa5b9-2f73-3b75-a815-a748b0ad1b06 | -2.80809 | -60.08588 | 2026-10-09 00:37:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9be850e0-8e5d-3669-84ea-e08fda27a6c8 | -3.56293 | -54.66922 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| fc027771-08c4-38eb-a01b-aa6b2b108e53 | -3.71068 | -60.15996 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2269f177-04dc-3652-9d1b-bf8ec40e347c | -3.58966 | -54.68919 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 8735e8d8-d40e-31b2-a954-7ed57617d21a | -3.30392 | -54.00575 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |


[Clique aqui para ver as próximas entradas](README39.md)
