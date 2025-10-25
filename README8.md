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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c63ddb27-0e6f-371b-9498-cd500ad5a4f8 | -2.8149 | -49.1354 | 2025-10-25 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 61dc2965-3799-31a5-920d-2d4b95d98f21 | -2.7964 | -49.136 | 2025-10-25 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 6b45c05c-ee0f-3ae5-a5b2-357b38c04849 | -19.7587 | -48.2824 | 2025-10-25 01:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 382bc886-bd8c-3056-b4a2-200239a132b3 | -19.7791 | -48.278 | 2025-10-25 01:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 267833a3-fb7b-364a-9bcd-6542ad94addd | -6.9171 | -45.1515 | 2025-10-25 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 94d2e368-6f3a-32b1-9653-953c84b50ace | -18.1714 | -51.7466 | 2025-10-25 01:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 111.6 |
| e835c987-6d48-3064-b0ef-b20a759d962b | -2.7964 | -49.136 | 2025-10-25 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 2e48b30f-df31-3af9-bcf5-8de6f9aba47d | -18.1709 | -51.7685 | 2025-10-25 01:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 78528547-81f6-3071-a0f2-08565df42532 | -6.9169 | -45.1743 | 2025-10-25 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| f435db5d-bf41-338a-b434-c8df4d144f39 | -19.7581 | -48.3056 | 2025-10-25 01:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 55.1 |
| a6df53a7-0b29-36d0-a985-b31b7ebe9eae | -2.8149 | -49.1354 | 2025-10-25 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| cd0dfc62-baff-3500-a437-9f358ae3936f | -19.7587 | -48.2824 | 2025-10-25 01:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 90ffeb7d-1d6c-3af6-b23b-c5a52c097a81 | -4.8399 | -50.9345 | 2025-10-25 01:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 1d7ed19c-dd9b-34f2-a749-7ed6adbda3a6 | -14.8706 | -48.0822 | 2025-10-25 01:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 62392fa0-5c79-37b2-8332-fe25fe11bd09 | -19.7784 | -48.3011 | 2025-10-25 01:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 6e281851-1983-3ecb-9814-9f1851037cdf | -19.7791 | -48.278 | 2025-10-25 01:40:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 9b4f9783-8f8e-37a4-a89c-9fcc1ca7aab3 | -18.1714 | -51.7466 | 2025-10-25 01:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 803a1241-92cc-3faf-a94d-da3adadeced7 | -19.7587 | -48.2824 | 2025-10-25 01:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 7b7fa0e9-2f91-316f-a5f5-e77ac8af78bf | -14.8706 | -48.0822 | 2025-10-25 01:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| d01e8e31-cdcc-3165-ba73-f1494ef7d3d6 | -18.1709 | -51.7685 | 2025-10-25 01:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| df35437c-3162-395b-9c03-5ae4a2133595 | -19.7791 | -48.278 | 2025-10-25 01:50:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 80c7b35e-cb23-3bea-8fde-9a5e38961cde | -18.1714 | -51.7466 | 2025-10-25 02:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| e1e0805a-b53a-3ec9-8d61-6dc64a64cac1 | -19.7587 | -48.2824 | 2025-10-25 02:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 3708da65-b985-38fd-b5e5-ee500e9c502c | -18.1709 | -51.7685 | 2025-10-25 02:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 34166c7b-29cb-353b-978f-9f6da9ef3034 | -12.0674 | -46.3962 | 2025-10-25 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 647dcbbb-4e0a-39a4-8e49-26a9aa403005 | -19.7791 | -48.278 | 2025-10-25 02:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 72f0970d-8ef9-3e38-94cc-f2a5b19fe444 | -14.8706 | -48.0822 | 2025-10-25 02:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 02e3812a-7dca-3478-b171-fe66f7fe2554 | -9.5562 | -66.7442 | 2025-10-25 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 0ea22bb8-f193-355b-863c-8b560da2c32b | -18.1714 | -51.7466 | 2025-10-25 02:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| cff44312-7a67-32be-96b9-d390f306824b | -14.8706 | -48.0822 | 2025-10-25 02:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 5b05e3dd-e999-32a0-a08a-6d441f77d201 | -2.7964 | -49.136 | 2025-10-25 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| d70500b1-8dca-3d3e-9b6d-1b0294955887 | -19.7587 | -48.2824 | 2025-10-25 02:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 6f8a7a35-ba1f-3d15-bedd-0341ebf72276 | -19.7791 | -48.278 | 2025-10-25 02:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 69e7171a-6dab-358c-90b9-5c164e5abef2 | -2.8149 | -49.1354 | 2025-10-25 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| c026bb46-c442-395a-8c0e-8316356f57d0 | -9.6295 | -40.3392 | 2025-10-25 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 9ad77eab-5bb2-3b00-a749-3792bbd30f3f | -19.7587 | -48.2824 | 2025-10-25 02:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b5cf333a-1007-3c5e-94b1-75dc0874cf79 | -2.7964 | -49.136 | 2025-10-25 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 2574d3b1-3745-393f-8c1d-81abb3777ba9 | -18.1709 | -51.7685 | 2025-10-25 02:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 3e17050c-378d-30d8-b210-2bd6a1d4a2ef | -19.7791 | -48.278 | 2025-10-25 02:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 06793456-63e0-3771-a8c8-acdd4a269f3b | -18.1714 | -51.7466 | 2025-10-25 02:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a89bb780-4e61-37e6-af2a-16b257f729f3 | -18.1714 | -51.7466 | 2025-10-25 02:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| a1d7c657-fdff-3a5b-80ed-e0101e2d7a7d | -23.7228 | -51.6495 | 2025-10-25 02:30:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 99.9 |
| 73bad226-23bd-3535-a6e8-3f2cb7013fbb | -23.744 | -51.6447 | 2025-10-25 02:30:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 91.7 |
| 84e155bb-1412-3005-a460-9006459a76c2 | -19.7587 | -48.2824 | 2025-10-25 02:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 78d6e805-f325-3c49-8dfe-0a1e44b8640a | -18.1709 | -51.7685 | 2025-10-25 02:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| c2720dff-3683-348a-913b-f3ffdc52a148 | -13.3204 | -42.4207 | 2025-10-25 02:40:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 099fcaac-1e51-339b-8d67-3114990392a6 | -2.8148 | -49.1567 | 2025-10-25 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 81a50af1-7b99-3330-82f4-2c92d22942ec | -18.1714 | -51.7466 | 2025-10-25 02:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5763b3fb-43f4-3ec2-b479-f5463f840fc0 | -2.7964 | -49.136 | 2025-10-25 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a3f1f19d-bf3e-3ea1-9978-c8b4b3a0f9a2 | -2.8149 | -49.1354 | 2025-10-25 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 25a66993-8d45-3fe4-bedf-5efb3ac23fd7 | -14.8706 | -48.0822 | 2025-10-25 02:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 0a86c0be-e2e6-3147-b7c7-232afcf7f875 | -2.8149 | -49.1354 | 2025-10-25 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d4a86f20-d5cb-385d-a030-fdc5312a0ff2 | -18.1714 | -51.7466 | 2025-10-25 02:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 5b304270-9e0c-3835-af09-6bb208094cf2 | -2.7964 | -49.136 | 2025-10-25 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 1f791311-6172-37e4-b79d-5799368b0ae7 | -14.8706 | -48.0822 | 2025-10-25 02:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 8bc46a4a-6231-38eb-8b40-a58946f40d04 | -2.7964 | -49.136 | 2025-10-25 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 91d488d5-4a19-3006-95c0-bb54c228dd0c | -14.8706 | -48.0822 | 2025-10-25 03:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4c938653-8138-3e6d-b6fe-88c2bfc2ceef | -2.8149 | -49.1354 | 2025-10-25 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 1feb3f3f-6286-3572-b183-28ebe2440ce4 | -18.1714 | -51.7466 | 2025-10-25 03:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 2822c6b2-28a2-38e0-b9db-4e35cb85307d | -16.3745 | -49.9445 | 2025-10-25 03:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 17233e01-2755-3b78-836b-c92b4b493d88 | -16.3552 | -49.9256 | 2025-10-25 03:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 679c89fc-1c5a-3b43-b33c-5b0bc9690e78 | -4.8933 | -43.2349 | 2025-10-25 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| e7b01570-728c-3ef2-8e13-58f5a5114329 | -14.8706 | -48.0822 | 2025-10-25 03:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 81.5 |
| ff002478-bcd9-36c4-bb29-bc2c9dd3e612 | -2.7964 | -49.136 | 2025-10-25 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 939d1576-48f0-3d17-aa1c-fbd717919671 | -18.1714 | -51.7466 | 2025-10-25 03:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 4b5efd24-91d3-31f9-9b74-dd7a4f8b9f21 | -16.3749 | -49.9223 | 2025-10-25 03:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1df5e07b-6ec9-39a2-be7e-ec7b1ad8f810 | -2.8149 | -49.1354 | 2025-10-25 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4f4f5edc-c04d-3273-bdb5-ba31dca57b94 | -22.8323 | -51.349 | 2025-10-25 03:20:00 | GOES-19 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 61.6 |
| ea526cbc-a284-36d9-b516-c72edaed673e | -2.7964 | -49.136 | 2025-10-25 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 2fb21d3f-4839-39fc-866f-b9204139783a | -18.1714 | -51.7466 | 2025-10-25 03:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| d137ad0c-cc5b-3510-ac88-a88f7389b61b | -18.1709 | -51.7685 | 2025-10-25 03:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 0a6465b8-659b-32f0-8b71-a41a490a6976 | -14.8706 | -48.0822 | 2025-10-25 03:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c13ecf0e-abe3-3ef1-a698-a74c88767ac0 | -9.6295 | -40.3392 | 2025-10-25 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 86542583-d81f-3877-acee-10050d30699a | -2.8149 | -49.1354 | 2025-10-25 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| dc986209-930c-3b2a-aa4e-78a37a8dcb89 | -14.8701 | -48.1047 | 2025-10-25 03:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 56.7 |
| c702972f-ca40-3680-9f38-9108b5348de1 | -12.0862 | -46.4162 | 2025-10-25 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 44159890-aaa0-33e1-aa03-d064d31da527 | -6.3155 | -40.92177 | 2025-10-25 03:28:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1558eb95-dfc8-3571-89df-e5db97d62720 | -6.31023 | -40.92091 | 2025-10-25 03:28:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6b063d0f-48dc-30f5-8ba9-3b8bb3d90c25 | -6.10403 | -40.58857 | 2025-10-25 03:28:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a123b482-215a-3d32-a9b9-59b008cc6f18 | -6.32036 | -41.86129 | 2025-10-25 03:28:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7209abe4-27c2-3c4f-99ea-fdf3b4a2cd9d | -5.03491 | -41.19942 | 2025-10-25 03:28:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b8765285-aba9-3456-bdb5-2a5fa3efffdc | -5.5978 | -45.18804 | 2025-10-25 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f89ad888-8ce2-3684-9d6e-14349f7a1ca7 | -5.8223 | -40.80654 | 2025-10-25 03:28:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ae6b3d66-4874-3300-a4a2-6f535bd08c91 | -6.01995 | -38.43463 | 2025-10-25 03:28:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| a023f499-cefc-3b13-ab4c-ef6149c0bd40 | -5.91446 | -39.19671 | 2025-10-25 03:28:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 257d8987-520c-30b3-90f7-e1fd23bacf8e | -6.31613 | -41.85278 | 2025-10-25 03:28:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f2f73569-e7a5-3cc1-8042-b02958bf7a93 | -5.84056 | -40.79476 | 2025-10-25 03:28:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 09229221-8166-3817-844f-8008d0cd8beb | -5.67987 | -42.76898 | 2025-10-25 03:28:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f4cc7f6-5b25-3a3e-b459-63efee1019d7 | -5.86567 | -39.50633 | 2025-10-25 03:28:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 54afa678-68bf-3a87-afbd-de9bbf76eb36 | -5.45809 | -45.41224 | 2025-10-25 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99dc8f62-ab4b-3d06-9e61-3e18eb273c3c | -4.18427 | -42.9788 | 2025-10-25 03:28:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6a8430b3-b96c-3113-8442-1047503492a3 | -5.24975 | -44.13498 | 2025-10-25 03:28:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ac052aaf-0199-3726-85c7-093635458b80 | -5.6807 | -42.76426 | 2025-10-25 03:28:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| de9308ed-d54d-39e9-ad8c-6cb8c14218fb | -4.17912 | -42.98078 | 2025-10-25 03:28:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 83a49f28-a15e-328b-b409-cca2e81117a8 | -5.80381 | -35.57954 | 2025-10-25 03:28:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 39036e46-8dd4-389b-bfa4-a1f2dab92398 | -5.45112 | -45.41058 | 2025-10-25 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4885ce58-1bbb-356c-8eda-af1be6befef7 | -5.25672 | -44.1404 | 2025-10-25 03:28:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 731ce9c2-a4d3-3079-b038-2771106b5fa8 | -6.89196 | -38.2751 | 2025-10-25 03:28:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1d462263-7974-3038-a823-1cd02994c70d | -5.03556 | -41.19572 | 2025-10-25 03:28:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6d14708e-5598-32bd-8976-2847570b40be | -3.70163 | -40.42443 | 2025-10-25 03:28:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |


[Clique aqui para ver as próximas entradas](README9.md)
