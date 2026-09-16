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
| 9f8a73dd-0fc4-36d5-a9c4-7edb4d9445d2 | -5.123 | -55.93887 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4afe08d3-8cec-3e9c-8705-499fd678475c | -7.17762 | -43.51853 | 2026-09-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 444fd38c-be8d-3189-9543-8a4422ead02e | -1.85018 | -55.80745 | 2026-09-16 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a1cca55f-49dd-309e-abb6-13573a902fc3 | -6.13934 | -57.69669 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d1f23d9-02b0-3c9b-b4db-7c6f8511ecf1 | -6.74857 | -59.43067 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c55173f-646c-35e9-b60f-de817b06466b | -8.79623 | -46.89791 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 817218c2-7551-32fc-8831-5a939b117b10 | -8.57339 | -48.51614 | 2026-09-16 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7534172a-d325-3621-bf62-ee6bb13373c6 | -6.77951 | -58.79874 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab5c0ce9-1d0c-330c-b918-be20af68aaab | -2.95135 | -50.40682 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d9291b0-1d3d-3e6f-be5f-83fdeaa07244 | -5.77584 | -45.0904 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fa40cc99-94af-36a4-93e8-11e6f1424e7f | -2.90143 | -50.39488 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c67dac72-e902-3378-b2e2-3682b48f2389 | -6.01679 | -51.79434 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f736b34f-abba-3bde-88fa-26a807b7579b | -2.86467 | -49.63169 | 2026-09-16 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 114304fb-60cb-376a-bcde-7fe6ec8a6066 | -6.33402 | -60.01817 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be082963-7723-3586-ab4c-3b0462a099e3 | -3.31229 | -47.14053 | 2026-09-16 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1c07a47b-c6ba-3ee4-87e6-f9e9d48c5107 | -8.80115 | -46.89867 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19f486de-b4b6-39f2-8fa0-b8c4d5160e32 | -9.23273 | -46.698 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a95d5a2-7a07-3d23-b5c4-f1cdc1908f1d | -2.10577 | -52.04762 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 863b2a97-3cdd-39a3-baee-085470162fed | -2.90911 | -50.41735 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60d5cd62-f9f1-3654-a200-1dea20f37bf5 | -5.69487 | -52.29391 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29440e88-46cc-3801-a127-3ddeed22e7d9 | -9.09986 | -45.72321 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1b22fee8-5197-3512-957c-9cceb846117e | -5.0737 | -56.24853 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60cd148e-7bab-3ad5-b6a1-5bec6aeaf181 | -5.91006 | -52.10004 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94dcf545-30d6-3c80-aac7-cd040a2d0cd9 | -6.3298 | -60.01762 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7945c7a4-425d-3763-a1ee-cdb80c5a938c | -2.89406 | -50.41928 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a059aa8-59c3-3c34-829c-683a1c785af4 | -6.76868 | -58.81679 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b285931-b6a9-3c09-9511-1dad61079c16 | -6.76482 | -58.81616 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 418035ae-2f96-3c5b-9df2-ab6400ec4452 | -3.01638 | -51.21108 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7cbe4d7-a914-3fbb-946c-313b7b8d46f5 | -6.03027 | -57.76773 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2d9a6de-ce9c-3c57-aa88-a4473eb19b96 | -6.43786 | -55.60498 | 2026-09-16 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f2edf4c-6a9d-3763-9383-3c8b42a444a1 | -4.57462 | -54.91182 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 943ff271-0216-3eaf-9d9a-44c113e60e55 | -3.73588 | -55.94122 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e380c76-df5b-33f4-a414-d797a3771210 | -5.14122 | -55.93408 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76131929-683e-3984-8e3d-fb0533456324 | -2.10076 | -52.05779 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8f8bc98a-dd3f-3ea5-bd5f-ad437f68c7f1 | -2.78606 | -51.36443 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ce1f6a8-48c3-3578-8526-cb63ac4ef2eb | -6.1135 | -46.10573 | 2026-09-16 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ca5eb06-852c-3b6f-8f4a-c58e44715f1d | -3.39697 | -50.75802 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53bce106-0983-3df4-8b1e-755ca1ad5c38 | -2.87831 | -51.74352 | 2026-09-16 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a2bfa34a-f5b5-380d-a311-88a185988473 | -4.60566 | -55.70372 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a7bdfc8-4271-3680-bdfe-52763550651a | -5.12399 | -47.61221 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 38ee1561-def7-3bca-b953-f1f56845aca5 | -3.84768 | -51.76017 | 2026-09-16 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce3e1541-bcd4-32c4-ac90-92ce0e0fbee3 | -3.10427 | -57.68041 | 2026-09-16 04:57:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 955cfdef-321a-3b3e-a25a-38030f23ce5f | -2.91021 | -50.43447 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0892e941-26d6-3471-9bf7-f7ad3fbcc960 | -3.73874 | -55.94548 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 297906dc-fa25-3a8e-b43e-914edd91d0ef | -7.60912 | -57.60863 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03f06b32-bd27-3f08-9a5c-b1226ebd22ad | -8.85109 | -44.89891 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88b22bf0-ae18-363c-af10-f32f6a02458b | -6.40002 | -44.05415 | 2026-09-16 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 241615f6-a28d-3b8d-98b7-1d5164cea288 | -2.89343 | -50.42343 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba6453c3-3168-3a15-ae12-a12e772758f3 | -7.05557 | -59.22838 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c14e5f4-9d96-3aa9-9139-836d8f09489b | -2.90865 | -50.396 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 104e447d-fcd8-3772-96a7-4fc471ab35c9 | -2.10632 | -52.04406 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b5751658-2359-34c5-8779-d800c8d57d93 | -2.91398 | -50.4096 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2af3fa5-ced7-3112-bd75-4da238b1fff2 | -6.10831 | -57.63533 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0aad0272-8ffa-3aa7-88fc-7cbfb56b83c5 | -6.07451 | -57.86283 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 859b369b-48d2-3dc7-b645-8d64f56e6ece | -6.30083 | -59.98507 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be0f50e2-e8da-3e2d-bb8f-34c139d3e6f2 | -6.29252 | -56.02801 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2797c3c-6e45-3411-922c-6020f887e0fb | -4.49782 | -55.50069 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78d8ed48-8568-30ca-bc19-cb17e989840a | -6.02957 | -57.77203 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 401f1710-0aac-34d5-af79-d9b1d665ea4b | -3.29517 | -59.46421 | 2026-09-16 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3190484a-ce66-3c8a-bf10-321a16a86002 | -2.91931 | -50.42316 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78ce30a2-5ffc-3e83-bc6c-a0defc5857a2 | -2.78142 | -57.02487 | 2026-09-16 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3bead72-ac21-3a1c-bdff-6971cd1f469a | -6.16092 | -55.70362 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 151c6511-9ee0-331d-9ffc-0e46a8e25a0b | -6.08629 | -57.86015 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c4545f7-40ae-39b1-9a38-808e8e37b65a | -2.10803 | -52.05526 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 03f43880-64b2-3261-ac13-9dd71f0de29f | -6.02088 | -51.79097 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e587b819-86c2-3c07-9e04-5d64d566a85a | -6.78187 | -58.79673 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47d0e4d9-a12c-36e5-a92d-8ee1e0bb351b | -6.34632 | -55.56088 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f55d82de-b7f6-3ae9-b6bc-9eb432004ef0 | -5.75413 | -57.59544 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 33f8af31-1e93-3e82-9714-0602106c2b38 | -6.16035 | -55.70723 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a65671d-48cd-3495-94bc-b34291729ff0 | -6.34098 | -49.3976 | 2026-09-16 04:57:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c78e813-8bd9-3da6-92f4-5cf4ca9e6724 | -6.75791 | -58.81007 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9c736fc-fc96-3db3-84c7-3d76ddc4d736 | -2.94647 | -50.41459 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43bf698f-3c1a-3edb-92cc-5c70f793b79c | -2.89218 | -50.43173 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0103ec0-0490-30e5-952e-02db9c8aa0b2 | -5.11955 | -47.61154 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c65de3a2-5712-3044-9474-048d70714298 | -3.10806 | -57.681 | 2026-09-16 04:57:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da309a68-de8a-3790-bdeb-cd6c6fcbc314 | -6.62755 | -58.37291 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e38ff5cc-190d-3d80-a835-2b6e922dec4c | -2.10913 | -52.04814 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7df31f53-34f0-3ba4-912b-4f5cde151b2d | -5.14699 | -47.60386 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8746d211-6102-310a-ad96-52bd2468de19 | -9.09451 | -45.72237 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| dec1a417-02eb-39c3-9816-a0279e8c42ec | -1.61079 | -55.57141 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 04c68581-79b2-3eb9-828d-46b7d9c7c423 | -5.90316 | -52.09904 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e95a56c7-55fe-394c-b304-8fdeb7c4ac7f | -3.16749 | -58.64118 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 625389fe-4190-3a9e-8d85-055e859967dc | -7.51836 | -47.56521 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c505424f-535c-3144-8060-fd75fb754fbc | -8.80685 | -46.89378 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15f6a114-3dbe-37f9-a309-bbb0b8432dc9 | -7.17886 | -43.50922 | 2026-09-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| badd8007-3fdd-3734-aac3-5786be58e14d | -5.81818 | -52.08282 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f07164a-4b89-37d9-988d-201d82ab1c53 | -5.77051 | -45.08953 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 61bf14cf-a561-368b-80d7-8951c120efef | -2.0996 | -52.04302 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ccef5c1-3f73-3bb0-b05f-695640aa2161 | -6.3143 | -59.95591 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d20a5c06-4d25-35e3-84d6-9c0e3fc51709 | -5.88418 | -52.08455 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b2eb743-6afb-3a07-a643-49bf2ae5f3d6 | -5.13266 | -55.94403 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52422b16-40c7-33e1-9841-f61d474ac109 | -4.53476 | -54.97015 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6aac9450-a506-3eab-8bbb-e108c01cc20b | -8.11945 | -54.80212 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 546d1abe-5f3d-3d43-bdf5-215cf47be305 | -3.80308 | -51.70735 | 2026-09-16 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1c7b33d-b017-3200-bb7c-fd1b0ff2e3a0 | -6.76096 | -56.32792 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8fc5e25-f5cc-3a63-9dca-efc8744a56eb | -6.75406 | -58.80943 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc7b3b9b-ea5e-3fff-adff-970bb3a490a0 | -4.89308 | -55.88374 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8e17535-96a6-37a9-b0b7-eb659352c9b3 | -8.79654 | -46.9091 | 2026-09-16 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4e6b306-5e84-3671-812b-8a0c8b4b5617 | -4.53142 | -54.96965 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c163629f-ce31-3783-9ac0-2e7b1e170f93 | -3.10806 | -51.82675 | 2026-09-16 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README39.md)
