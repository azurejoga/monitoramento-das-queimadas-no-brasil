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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a729aba7-4d6c-32f0-8edf-71ca8e312013 | -9.83264 | -47.63344 | 2026-10-05 17:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e2c15edd-4d81-3b70-856f-52aa6ea0dcea | -11.20729 | -47.13161 | 2026-10-05 17:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| eca77015-766a-3a86-865a-c95cbbfbaea0 | -3.24513 | -58.49879 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c4923d93-f675-399b-a493-f2a4c8ce98bd | -3.48846 | -59.38659 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07de49a6-460b-3657-95de-c6cc1f50ccf9 | -11.21047 | -47.14735 | 2026-10-05 17:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 02007f03-8b1d-35ad-8faa-50a9c37470e9 | -6.82669 | -58.58813 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8f76b42a-df22-3aa8-af3b-5afdb11a35a9 | -3.72804 | -60.56902 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 844fd1d5-8ae7-3d60-8336-8953b577e39c | -3.96619 | -59.10004 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 6144fcf8-42bd-3851-954b-84fe026423ca | -3.75291 | -59.10338 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 240dbd7e-f027-344f-9bde-7aa26464d16c | -10.95467 | -60.9131 | 2026-10-05 17:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 90f10d6c-b3f6-3a20-957f-25a061a46ead | -5.96108 | -55.35092 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ed336af4-c757-3539-b143-e28f2873afb7 | -8.24087 | -73.38521 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3e46a946-e94b-3863-92d3-60040fefc491 | -3.64688 | -58.62135 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d2eb17bc-d627-396d-a3ad-f0dd865ed211 | -3.07 | -54.15823 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 8e13820a-c6a8-369c-ac99-12b1039a9689 | -3.16877 | -58.63647 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2a876cfd-3bd3-31cb-82af-829ba5e86499 | -10.30764 | -63.39093 | 2026-10-05 17:34:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3042ee13-ea58-3394-acae-c6724eeb54d2 | -3.19178 | -54.0944 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d5497ea0-15ae-398b-8ea7-95a91ecb7983 | -3.12372 | -53.70799 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| eb921961-5f3f-3677-ba67-aa180683b065 | -4.06414 | -54.05279 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f34c8928-681b-364c-915a-5b89f5c6a846 | -4.3937 | -59.55398 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9d32f5c1-d50c-3840-9af9-50bfdeed921a | -3.396 | -60.83923 | 2026-10-05 17:34:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 567750d0-e3df-3804-94fc-eb2d353a2b0a | -3.28936 | -57.0083 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c46f928d-d326-33d9-bebb-16bd4b0665b8 | -3.07794 | -54.17308 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 6e766250-aecb-3b6b-a525-70eb2adca13b | -5.99555 | -61.60545 | 2026-10-05 17:34:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c150b896-d7f3-3467-bbb1-0ff37b15b085 | -4.07624 | -55.32703 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 158a35f4-7e11-3e21-b76d-70da3c2b9116 | -3.07872 | -54.17777 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c3361ba6-1340-3567-a710-2619e5b00780 | -7.77399 | -69.9257 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a07552bb-1a77-36a4-891b-927fc66a4ec8 | -3.4943 | -59.57981 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b0b170e-6a25-30e5-b8ea-c8c2f1d51be7 | -3.4765 | -54.62313 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8ba33fd3-2f9b-395e-9cda-e8720be3fb18 | -3.37149 | -58.19545 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 269ca18a-98cb-3228-addf-5a0f339db75e | -3.64634 | -60.92332 | 2026-10-05 17:34:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a2888e34-caac-3e5d-a8ba-bc28242044e8 | -3.0192 | -57.4865 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 55c5893e-71d4-3317-88e0-332767a614b7 | -3.28823 | -60.11315 | 2026-10-05 17:34:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c9bd6201-853c-36f6-92a0-c589089418bc | -3.87778 | -59.20697 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bfdaf1d-d33d-3af3-8ce5-e695039d2647 | -11.10659 | -46.09225 | 2026-10-05 17:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b5f346ee-745e-3bc9-8797-e1e05425fb6f | -3.89009 | -55.80228 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9d0d0402-c6ce-3898-8928-f2e9f1d4d0ef | -6.39913 | -67.94454 | 2026-10-05 17:34:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 8380ffb9-fa3f-34de-86a8-9d927ba814e5 | -3.67429 | -60.61592 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 0a62a055-b746-357b-955c-88e03045d9fb | -6.91836 | -59.26321 | 2026-10-05 17:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5f576a14-0ae2-321b-b20e-e275b4f38ab8 | -3.51089 | -54.61364 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c782c015-39ce-3221-a990-d770967d24a5 | -5.8139 | -53.83878 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| e8ab6fdc-f820-3b78-a6c9-ee7630159874 | -12.4122 | -54.68536 | 2026-10-05 17:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 5a401b91-99ef-3e7b-b068-4385c75a64b9 | -2.99281 | -51.04699 | 2026-10-05 17:34:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0eeb13fd-b04b-3e91-8905-58b3ebd348ec | -3.24388 | -57.86772 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ca23338c-4ddd-3b54-a017-90210780c75f | -6.54411 | -69.72389 | 2026-10-05 17:34:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d6a74ae6-024c-3558-b0d8-2b9fe96f8036 | -6.17477 | -55.71666 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 5a21f312-5a9c-39b2-8e68-a25ddbf0004d | -3.21314 | -57.8716 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f48eeb7c-1124-3644-8ba4-e0e8c445b1a1 | -3.70289 | -59.62742 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e8231807-708f-3995-9b11-11a14057403d | -3.87864 | -55.80787 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 520ffe6e-6719-3b5d-9607-e4283e1b99a2 | -8.35656 | -70.07684 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 995b8650-4b20-3c64-8b17-35ddf2d14a19 | -3.98167 | -59.34232 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 894a3277-f92c-35d1-bb30-3bf45e8d8f5c | -13.50766 | -61.12291 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8e960eed-7ccc-3b92-b89a-1fe5b7a2efb6 | -3.41796 | -59.72243 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e371336a-bafc-35be-8292-a61e406ce0cf | -4.27178 | -59.20044 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bb458f49-9a95-3c40-ac1c-7cf1af97b273 | -3.25249 | -57.18906 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 91983ab1-33c3-3e98-99eb-90ddb5b01e35 | -3.28926 | -59.41398 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5395c2dc-077f-37ad-a051-3eb88eb3dc2c | -2.95308 | -54.15736 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b1a46bee-15b6-3b50-bc77-a714cc31c396 | -3.5883 | -54.31004 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 47518877-4d67-3a56-b9f0-0619b08aaf0b | -3.28455 | -54.17867 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 87ab214a-1d8f-3e59-bd4d-616a08958398 | -11.34462 | -46.68171 | 2026-10-05 17:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 00451069-967f-37e1-9bb4-28054d55b69f | -10.86711 | -61.41257 | 2026-10-05 17:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d93da043-b3f0-3ee1-b2c4-e6e3d2e3dad4 | -13.50178 | -61.13192 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4917ad18-103f-3a81-9de1-7315cd219881 | -3.24922 | -58.50211 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5ccd6d8a-8feb-342e-b8ef-2010862e62ec | -10.34852 | -64.21524 | 2026-10-05 17:34:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 305e9d10-c0f6-37d4-84b4-d38558c5e261 | -8.02535 | -70.07963 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 093542cf-4b8f-3b0e-804a-799e95b76058 | -7.58578 | -69.94134 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 72c8bde6-ee94-34a4-a2a9-7e6bb7e31e42 | -3.01266 | -57.91873 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| f0edb529-3e6e-3f04-a991-844cd7c661d8 | -2.99042 | -54.09924 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f555f1d2-2dcb-349a-80bb-1ea411629575 | -5.12956 | -48.09609 | 2026-10-05 17:34:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 5a446f44-6f93-3eb0-85c4-b2214ee0991a | -2.70643 | -56.53395 | 2026-10-05 17:34:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c4d7c1e1-fced-383f-804b-9ab4cc3ffa2d | -3.88683 | -58.95152 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 018328e0-4809-3f64-a926-d4f1229758dd | -3.86432 | -55.8291 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b41ce3a1-3b84-30cc-a4de-e0e8eefe19b6 | -9.5206 | -46.82072 | 2026-10-05 17:34:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 07f768d3-620d-3d42-a0a9-bc456e2d4aec | -9.74657 | -48.17252 | 2026-10-05 17:34:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1c24dd8f-b550-33e9-b25a-ca81e5bc5464 | -3.64702 | -58.22193 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29dfb9e0-dead-3614-b9ea-2300cf1682a7 | -7.79178 | -70.0147 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 13d4598f-2a8a-3461-b68c-29418d580910 | -10.958 | -60.90865 | 2026-10-05 17:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ddb9dd1d-8fef-3895-8057-1db35b576bdc | -8.19724 | -72.98457 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8cd1d62d-3b7f-3e18-ae2f-a2dd4956a96b | -2.94694 | -54.12023 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 449f0ca2-c1a7-3f15-b5f3-b5c65325cdc0 | -3.42746 | -59.71736 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9a298cf2-1862-3a58-ae11-2605d8260e99 | -3.9627 | -55.47794 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 57530d04-04c9-3fbc-a3e1-45a856f0e079 | -8.23374 | -73.1105 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 7d147458-eda5-3522-93ef-b1707baea6bf | -5.13054 | -48.10167 | 2026-10-05 17:34:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 9757c1d5-f577-3447-8821-92a05f6032e5 | -2.94922 | -54.10559 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ae70a669-b9fc-3535-a3e1-c2afff837078 | -7.82006 | -71.91992 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5b635f70-5786-3669-8612-596713b9ef61 | -7.52918 | -70.39401 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a194783f-1253-3fac-a03a-d23dd2b01a22 | -3.51561 | -59.562 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 35463a1d-13eb-3256-a3ce-d734075305ce | -3.5219 | -58.69903 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 46a4ea46-dbe5-35d3-8530-71c9f4838dd8 | -3.55561 | -59.48651 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ff2206af-53f3-37e5-921c-1bb34c40cfc1 | -8.34255 | -70.10358 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 01d5aff8-c8bc-312e-b54b-49e718c282e2 | -3.85313 | -61.38927 | 2026-10-05 17:34:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e87fd31e-3656-3094-bea4-e301bcf1ddca | -10.95751 | -60.90886 | 2026-10-05 17:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f7e6c893-561e-3b84-b6c2-e7dc1ab0e698 | -3.25587 | -57.92047 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 41d5afc6-fefb-3702-983c-ec0d5d429275 | -3.22153 | -54.30479 | 2026-10-05 17:34:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e797b269-1bd7-343e-b9a7-e209968bffb2 | -3.61235 | -54.59906 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 167b852a-f0e9-3725-9d5a-0f568bdd73e4 | -6.82612 | -58.58451 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e4ea33bb-2e80-3b11-87b6-2d24b4465c82 | -10.23256 | -46.65754 | 2026-10-05 17:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54df1f3a-8961-37de-a74b-e5eb092ee646 | -3.82381 | -55.78139 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 07f2914a-225f-3819-a19d-5570d363955d | -2.98953 | -57.90035 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c7a9d55e-306b-3fad-9018-917d27863a6f | -2.94043 | -54.13924 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |


[Clique aqui para ver as próximas entradas](README137.md)
