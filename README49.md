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
| f46d4d46-c538-3ee4-89cd-868b145499e6 | -3.49275 | -54.04929 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56ac799c-406c-3e48-b837-a603f99100f6 | -2.68792 | -49.16703 | 2025-11-18 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 311422bd-b97c-3c7d-afa5-95500505825a | -4.18701 | -44.23977 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46cdf969-5223-37f4-a03a-1c267fab8de4 | -2.60683 | -49.21622 | 2025-11-18 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8c0d1b3-0e49-3f77-bc31-3ea4ebc672b5 | -7.14377 | -44.92191 | 2025-11-18 05:10:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f2b494d-01c7-3763-ba4f-c3cdc3de972a | -3.59979 | -43.61153 | 2025-11-18 05:10:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bd5bf71-9883-304f-8cec-c33ef0200bb0 | -3.5474 | -51.53785 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63c9c48b-162e-3ce7-89a8-85f0c5c8980f | -3.08604 | -51.26343 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 509c8f4a-5180-3b4a-9ae7-ef147b4d9955 | -6.4433 | -43.81533 | 2025-11-18 05:10:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 52752446-45a5-309c-a1e3-fb20f965b1d1 | -9.39667 | -48.45445 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6b34f69b-af71-374a-98d5-10c527c0be60 | -3.41839 | -50.36036 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea612329-d555-3f5e-92ce-92f3bc468391 | -3.24705 | -43.03923 | 2025-11-18 05:10:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fe8de841-387e-3f6a-a646-b33bbf2afc13 | -4.13723 | -52.11931 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 429e2160-d816-3117-aa75-b8fb908c4cdd | -3.26195 | -50.08892 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edb7b5aa-d2bc-38e2-83c5-a8942f84f37a | -5.95836 | -52.9356 | 2025-11-18 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97b4d745-d59c-3225-8230-35ce912e3d55 | -1.41072 | -55.74712 | 2025-11-18 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6bcc413-0c14-37fb-bea2-fa2a6420b136 | -3.0487 | -51.14676 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18848e15-658e-3582-9257-5e654e2eb51d | -3.1331 | -50.25587 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35b02903-f75a-36ec-821c-3f191e085489 | -2.49794 | -49.34879 | 2025-11-18 05:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56746ee0-2619-3f94-acd0-fb22e45246a5 | -3.04797 | -59.18942 | 2025-11-18 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcee358a-9931-376c-89c9-6e1db65c402a | -2.51485 | -47.82692 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7fb3f779-29c9-38b4-b1ce-7e1686ebeb82 | -3.23533 | -50.50366 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ef4f7af-af41-3d2d-98cc-9716c64cee90 | -2.51672 | -47.81461 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e753f0-8366-3e06-801f-80d396f8a0a0 | -2.34073 | -55.79676 | 2025-11-18 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b1a4a24-0507-3bc3-a067-18f6757614c9 | -3.35164 | -53.21838 | 2025-11-18 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d05edf0f-a506-319f-b285-482d8be9fc30 | -3.18933 | -50.64984 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50ec58db-4d80-31ce-9eb8-abb6fba5c223 | -3.58336 | -51.43884 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4962451e-afa3-3158-a378-68a9fc7d5430 | -2.33355 | -55.79918 | 2025-11-18 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3260dc9c-ba2f-37fb-a0f0-b8f2fd431419 | -3.47863 | -51.57897 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d281fc5-0a71-37ab-a049-9958e4157616 | -4.18847 | -53.44024 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91c2d559-a5f5-3240-8e2e-45246855e8ea | -2.90493 | -57.32518 | 2025-11-18 05:10:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b80a1f82-3ada-3e83-b0b3-578127837e80 | -1.61482 | -55.85346 | 2025-11-18 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e772b50-9332-3038-b23b-6c25be4f3ddc | -3.14798 | -51.31831 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1e06312-7f8e-3a4c-b374-8cea9ebed60c | -3.17836 | -48.028 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6134c729-6ba4-309c-938e-d1d7883f4c55 | -8.86445 | -47.3238 | 2025-11-18 05:10:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21cea548-d6a0-3db7-99b0-9813587a1002 | -3.75724 | -50.94778 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba295c9f-cded-3a05-bb87-8c06e56f5b7b | -3.78093 | -45.59163 | 2025-11-18 05:10:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f928d3a7-d872-3ed5-aa7b-610f43084478 | -3.26946 | -52.47425 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad079347-6f21-38e6-91af-b4a912b83ef9 | -2.57899 | -54.24834 | 2025-11-18 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1bc077df-21e1-3e9b-8a8e-ccabf7812eda | -7.06924 | -46.05158 | 2025-11-18 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 248b1999-bbf2-3b4b-9aad-3dad1d62796a | -5.0929 | -56.1613 | 2025-11-18 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9719d398-f9f9-3899-b5d7-7f00810ca545 | -8.47044 | -47.98316 | 2025-11-18 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9cf7b44-06c7-3a2d-a587-cf2e0ac7b820 | -4.18912 | -53.43593 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7234a4b6-5b28-3793-9d0d-89d10ad35714 | -3.17421 | -46.60762 | 2025-11-18 05:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc160f6d-fc96-3934-b0e7-e482733a1c8e | -5.2137 | -50.17559 | 2025-11-18 05:10:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0190f81f-b0c9-3dcb-9610-5fa31b3b103d | -3.08375 | -52.92302 | 2025-11-18 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53fd6d6a-51ec-3fbb-8669-a431eaa5292e | -6.72018 | -46.31771 | 2025-11-18 05:10:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9458a5dc-a721-37a8-8529-6670ce869300 | -6.30243 | -43.79401 | 2025-11-18 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f5a3e928-3fa6-304a-b7f9-3c218de07b4b | -4.04832 | -47.50532 | 2025-11-18 05:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b63e2a47-b59d-3dfd-a9b1-3a83bcb15efe | -3.23907 | -50.50077 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91a924fe-0021-381f-858e-789c612f76be | -3.08217 | -52.92116 | 2025-11-18 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d38a70c-af58-3778-98bf-5051bf432f2f | -6.92305 | -59.27693 | 2025-11-18 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6abd7f85-a71d-35a1-a874-4b4f7af2bce4 | -2.51767 | -47.80834 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c0a72822-d307-326a-af51-856a4c4b5f08 | -9.3907 | -48.45727 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 98b827b3-707c-3202-9d55-3344b3ee2616 | -3.3038 | -50.07086 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a0e31b8-c2c4-3bd5-9871-24f305eeae44 | -4.27415 | -44.25133 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 747e44be-fbeb-3642-bab2-d2ca3f290db5 | -8.35381 | -55.15992 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfcad78b-b8f8-39cb-b6ed-d564527f986d | -2.45612 | -53.80265 | 2025-11-18 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa843794-38d6-3fba-a20b-ec6f13028f0c | -6.70986 | -47.7943 | 2025-11-18 05:10:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03fa6ece-a94c-354a-9b1d-893d5d92ed0a | -1.62996 | -55.71456 | 2025-11-18 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1077bff6-4312-3250-a69d-9357601fdfbe | -3.21522 | -50.18605 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef6d2df4-7606-3e76-82ec-03f3c5b16284 | -4.18205 | -44.24828 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9acc0724-2754-392f-b076-cc4bbb41810b | -1.83593 | -55.35452 | 2025-11-18 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd566411-855e-357a-b0c4-e88473106300 | -3.35097 | -44.39044 | 2025-11-18 05:10:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| caa26120-0118-381c-8a17-8f4daf97d534 | -4.27215 | -44.23994 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9de3f4d7-3756-3689-906f-1c13fff4e09d | -2.75625 | -48.42868 | 2025-11-18 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1742acc3-fdb1-33f3-baf3-caf8aefd73ee | -3.51997 | -50.34344 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48e18a9b-d6b6-3a4a-9a9a-d4a26b94c7f9 | -3.33204 | -50.27836 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a8829ae-29ac-3b5b-a3f3-665c1707453f | -2.85922 | -53.01195 | 2025-11-18 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b6914ef-257c-3a9e-b617-4695691a3ddd | -9.39165 | -48.45004 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| de8a668f-95fc-3107-97f4-5131e7c087dc | -3.3058 | -50.07259 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58499068-0699-307e-9b6e-1941cf6ec3e0 | -2.79921 | -54.65746 | 2025-11-18 05:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c48363fc-ed2b-3ace-aaa9-646e2e16a020 | -1.64491 | -54.39633 | 2025-11-18 05:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f394f4f4-2cec-3643-95df-33af12046e75 | -3.28538 | -51.42861 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fc3389d-352c-3af4-a996-a9951d2acd5e | -3.51516 | -50.28479 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5417ccf6-fd0c-314c-bc6e-d57c02c607fa | -4.1893 | -53.43766 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 509ec67f-9411-3b09-9fa6-08d515947514 | -3.2908 | -53.83322 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3a1fc35-090e-36ad-bb95-5f0297423903 | -2.45405 | -50.28181 | 2025-11-18 05:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb9d4e2d-6a23-39db-bf94-7c02b97ef8a5 | -4.48334 | -46.59642 | 2025-11-18 05:10:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 111bf7c1-c0c1-39a1-96b4-50fd0a640797 | -2.50543 | -47.81901 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2069451-9e19-37a6-8a33-ef01353ae78a | -2.83365 | -45.42502 | 2025-11-18 05:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0a8c3c7-9272-393f-a2df-49b13712c134 | -4.65116 | -46.54225 | 2025-11-18 05:10:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc2d8696-4cff-37e2-9dbb-39673bbae02a | -6.30561 | -43.78712 | 2025-11-18 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9844cc6b-3d68-31a2-9b4c-04b310362585 | -3.23774 | -50.50923 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb02c169-0a43-3f90-9956-80b721b54b97 | -6.14554 | -57.84861 | 2025-11-18 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 178923d5-26f7-3372-92eb-0f30e885764c | -3.29961 | -53.8469 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8677fa28-8f72-3c0c-bb05-df24926f61fb | -3.08307 | -51.2553 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dbbfa68-b33e-3712-9118-4afe5fed4290 | -2.82755 | -45.42411 | 2025-11-18 05:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e49e10e-95f1-3cc1-9625-8521a4a55928 | -8.93468 | -49.84441 | 2025-11-18 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ad5736a-c15b-3524-afbc-2a811bd41e46 | -1.45748 | -53.43028 | 2025-11-18 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ef7efe9-5388-3e0e-b502-fffe50fae33a | -4.13327 | -52.1187 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3cb929a-e6af-3a57-853f-d399489f70f4 | -4.13646 | -52.12436 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 504bf965-69ee-34f0-96be-4cfac7144ed9 | -4.52701 | -46.41612 | 2025-11-18 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb661749-f32a-3bf5-b0c7-cb2ba68d2a99 | -2.49719 | -49.35369 | 2025-11-18 05:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cefc8d0c-37fe-30f4-a458-02716c0e2216 | -4.64853 | -47.94747 | 2025-11-18 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5c57d1d6-e3ac-32a9-8037-f31a5ee93c6b | -3.27691 | -54.85387 | 2025-11-18 05:10:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b45ce351-1f37-3797-988a-8ab7f079d431 | -5.96222 | -52.93617 | 2025-11-18 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8db1b4e4-779f-3050-9a29-867ce83cda1f | -2.45198 | -53.80603 | 2025-11-18 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8883e40d-c245-3e39-9adc-46c463fadcb9 | -2.82754 | -45.42636 | 2025-11-18 05:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b976acc-6b4c-3c24-9bf9-9c8677ccf8a0 | -7.43616 | -45.19318 | 2025-11-18 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README50.md)
