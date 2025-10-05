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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74d5e05d-7f29-30f9-b22d-5faaddbe27dd | -17.94068 | -57.60392 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| ea465261-8839-3585-9ae4-fc70e67e3b00 | -18.14732 | -53.34867 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c78ba311-4437-3dd5-97e6-09dddce9e91c | -19.95297 | -44.63703 | 2025-10-05 04:49:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1033c3cb-f6bc-3040-a89d-166546017a69 | -17.712 | -56.74868 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8b36969d-cb99-3d0d-b462-2ed32fc063a5 | -17.95418 | -57.59226 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7b4617de-f430-32d7-a470-0e65925993c4 | -18.19386 | -53.35603 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48c70c8a-9259-334b-b428-4611ffc71231 | -15.3227 | -46.36646 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a89c8678-17bc-34db-b6a4-65c82f1ca35a | -16.0721 | -50.92036 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 907bce58-37fb-38a6-b942-77421b04da4c | -14.92348 | -46.85442 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 258e4ac8-a211-3aa8-bca8-13d7e1f7769a | -14.66258 | -48.3599 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b508adb4-5d77-3ce5-bc0a-1bca660fe149 | -15.61376 | -52.46965 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4ed7980-2eb5-3980-a6d5-a1feb271514b | -14.32611 | -47.67036 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 260df605-f337-30a1-ab6e-faa719d09329 | -19.51762 | -50.37757 | 2025-10-05 04:49:00 | NOAA-21 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b2d3815-c7b8-36d3-8425-3e0369998d26 | -15.37824 | -47.93652 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c37f4493-29b3-3535-89cb-bc9d31c9622b | -13.73889 | -47.96679 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f757bb95-2f74-39f6-afc4-d11929219079 | -16.12701 | -53.97364 | 2025-10-05 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6d67d280-3520-33da-9bae-6f14275dc3ab | -14.01063 | -48.20324 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| aa23fbbd-29ce-3756-86a8-f6e6f2a8af62 | -18.25118 | -53.35838 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cc01acd-8669-3bab-b45a-a538feed40ea | -14.75313 | -54.65828 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 391e0585-df3a-383d-a2d5-d8c958a3947c | -15.39339 | -47.94641 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2c8c0db2-139f-3366-8d23-37a011bf2205 | -19.94316 | -44.38594 | 2025-10-05 04:49:00 | NOAA-21 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 126dec1b-8a96-30e5-81cb-22789904d5f5 | -17.99171 | -51.63344 | 2025-10-05 04:49:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 811a0ef9-6c98-30d0-bf71-6eae07bd0074 | -14.66485 | -48.28315 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c94dd27e-28ac-3c34-8128-3d8ec18d2a67 | -15.45909 | -51.56162 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cdb10ab-c475-32b3-b506-f719a1382901 | -15.69097 | -46.27276 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc813140-0a2d-3950-9c63-7ff64c7d2293 | -13.73031 | -51.26397 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cf32edd-ffc9-3b91-86b4-67411050340c | -13.74051 | -51.31077 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c77e404-7feb-3bc3-a21e-57d41626cf77 | -15.42203 | -50.21153 | 2025-10-05 04:49:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df932a13-7d08-3a49-96b0-e22837949495 | -14.95452 | -46.8517 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44135f8e-def3-3ae3-8989-15ca445ff2f6 | -11.76182 | -64.9296 | 2025-10-05 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e6e8020e-0999-35f1-86e3-5562c231d879 | -19.01437 | -50.59474 | 2025-10-05 04:49:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 46bd9e04-950d-365e-9885-c732c766f4ad | -15.94114 | -48.98842 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2377f667-d7b5-3859-9983-465e2e6f5d3c | -15.301 | -47.95237 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab3a03d7-2570-37b6-974c-10614d920804 | -13.68764 | -51.23831 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad5de55f-72b5-3429-a676-7808c2268f23 | -11.84811 | -63.71703 | 2025-10-05 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a5d56fd-5207-38ee-9097-a724b191aca6 | -14.32516 | -47.6776 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c52b8fd3-46a8-3c6e-8986-d262903743da | -16.1237 | -53.97309 | 2025-10-05 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c88afa6a-614f-3296-b9fa-5c9218d76a16 | -14.32118 | -47.67648 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8f0633c3-3c64-39a3-81d1-9cf0f34e7746 | -14.8304 | -54.76754 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37bfd08a-399f-3c14-ac9e-5b979c1a4717 | -14.66935 | -48.3091 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 13726479-85ce-328c-a3b1-06e4292e17b3 | -15.21609 | -56.80657 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd862830-86af-350d-bf31-318c7094fac4 | -16.05357 | -48.09847 | 2025-10-05 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a1366da-dea6-3bed-abde-de05effc2ab2 | -17.88674 | -57.63837 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| ff1a3311-6117-3d8e-affb-21e34c7f698c | -16.29083 | -45.24249 | 2025-10-05 04:49:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9dccf571-bb03-39e9-96ca-8c77f5d37b02 | -14.95232 | -46.85361 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04a38ede-619a-347d-a934-781aa4cf61fd | -16.08714 | -50.91444 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b609e425-c2f7-3b11-8d4e-d7ca6180fe37 | -18.24788 | -53.3578 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5d44bd16-3537-3020-9d47-801982adfb47 | -13.73234 | -47.95563 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d004f95d-df9e-3c82-ba8b-792585831d97 | -15.39502 | -47.96515 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79070093-ef62-3b36-8f09-a44b3705e968 | -14.99501 | -49.98618 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e956d19e-43f5-3bef-91ff-61644908d0f9 | -15.24234 | -49.28989 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a882934c-d4df-3107-ba39-416c225f91db | -14.60614 | -52.50014 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1649f2a1-d1cd-3487-b854-c74d99adce31 | -14.93404 | -46.84071 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3907a125-2d1e-3803-8e40-36fe993a73b5 | -15.979 | -50.86252 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72221664-ae45-3ff7-a654-ac77cc5bca9e | -14.66008 | -48.34885 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f24e8ac1-29f2-3b02-ab5a-9e9b996a2b5f | -15.59496 | -52.45922 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c4fdbb1-bd92-30f7-92ec-b0530eabca7a | -15.99043 | -55.98875 | 2025-10-05 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 466de524-f893-3ffc-9289-4efcd87c1512 | -16.0288 | -50.9505 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b2e70c08-92e7-36a6-8235-34f26b717ae6 | -16.00501 | -50.85458 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 75b4064c-f572-38e8-a457-1266b43fd4c0 | -15.58616 | -52.49461 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd11f895-fbbf-308f-8c4f-0f38acbd6933 | -14.64744 | -48.31849 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3e6fea5-3d02-38b5-a5cd-edcb704c4a5f | -14.3173 | -45.85884 | 2025-10-05 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b1138c4-8eb2-3f99-81f5-95e0a2ba4e92 | -13.68343 | -48.05173 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd1d774b-adf9-36d0-a440-c9c0c3fd408c | -14.64427 | -48.31267 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03da1012-3a85-3fad-8674-4de9a14335c9 | -13.69128 | -48.05272 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d387b584-e3cf-31ed-9b7e-3e403a43e49d | -17.57507 | -46.07753 | 2025-10-05 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83b104f1-ac93-3a2e-91b2-f9af04a68ace | -15.7796 | -49.09494 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b1ba7be-1bb7-3420-8c33-382596bfd97d | -17.8847 | -57.59666 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9fdf6b7c-d97e-33c1-b17e-eaf7602060a6 | -13.72457 | -51.46183 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f06549c-5508-3f3e-8dd1-5fae19fbb3cc | -16.01954 | -50.82816 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 343751c8-8f51-3f48-8048-e1683b5825b9 | -18.24513 | -53.35361 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f996a04-5c20-34cf-8d2a-2f8b251af4a6 | -14.92921 | -46.8441 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 73837ac8-66b4-3f7b-af56-b64f9c1fc105 | -16.07615 | -50.91689 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d4179fb-6365-3065-86e6-0da1e1f36fd4 | -14.87796 | -48.15745 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e174d09c-fa2a-3f34-8521-1effd5b06c27 | -18.32416 | -49.15332 | 2025-10-05 04:49:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2504150a-f4a5-3595-98e6-331e42a3d81b | -15.98537 | -50.91622 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 972b866d-275e-32d4-b3d5-f6f8f2f8d91e | -17.84316 | -57.62498 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| bc230ad8-7074-3481-8a0f-64a173852a3e | -14.99615 | -49.97816 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f34784a8-c39e-3b13-825f-75efabe44091 | -18.14071 | -53.34758 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4299481-858e-3eed-bbfe-a993537bea7e | -14.67878 | -48.3575 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e36d87f6-565e-398d-a772-13fa71ca8dc8 | -14.88372 | -48.26139 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5fa6c83-e135-3ca3-9ea8-080f8425d696 | -17.96033 | -57.57898 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f1478147-a36f-3984-87f0-d70e8b4f88b4 | -15.75089 | -46.27213 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c96d40f-e4db-32fc-bbb6-d8f55f8507ee | -15.30857 | -47.9571 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a694e643-c482-3027-af13-c59d43b2f5f8 | -15.58225 | -52.45346 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb03c542-f134-3cbc-a034-bbb7eb1c32f7 | -18.14182 | -53.34033 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de23a23f-0fe6-394f-9b2f-887d972c3480 | -17.32231 | -46.55499 | 2025-10-05 04:49:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 197517a8-aa03-3d30-8290-d4ee66cf20e1 | -18.26423 | -53.36388 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af44f30a-1519-38fd-b3b8-05d100557fc2 | -15.17386 | -43.63631 | 2025-10-05 04:49:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4ea19590-0d24-3262-8ae8-d9d8e17404dc | -15.60328 | -52.49378 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc4d981b-c323-32f9-8559-1747b0ae3a20 | -15.76611 | -46.26107 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb1b1b2d-e066-3fe4-818a-1b771d797e0a | -15.70001 | -46.2741 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b42b931c-670c-3bb2-8e76-46a312ddcd37 | -16.38774 | -52.15825 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f1f02a3-ef09-3a30-b7c9-dd753a7decbb | -16.43897 | -52.15949 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad9cf64c-d808-3a37-b7fb-84dfb121e9c6 | -17.8527 | -57.63605 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 7bf065bc-e08e-37e5-80e6-2e636d01265a | -15.94047 | -48.99324 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9de194ad-946b-30f2-9892-a2dd37f37e27 | -14.61862 | -48.11954 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a258d0c1-3724-3e95-a8ca-67fd38d2e5a8 | -18.16026 | -53.3319 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78e7811d-b405-38a4-b616-ede915a7b575 | -14.32915 | -47.67866 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0a30a839-ed49-335a-9227-b42006012cfe | -15.72558 | -46.25331 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README112.md)
