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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95b38c98-16f9-3d38-a438-c314ba03ff6b | -10.64011 | -49.98419 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc83e4a7-4cc8-3f26-ba61-b32ad88a8c06 | -16.33312 | -43.33847 | 2026-08-03 04:40:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 798e25ee-1cc5-3454-af38-f1f91c773ef8 | -10.62953 | -49.9861 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53360c09-865f-36a6-ae26-cc652211f429 | -17.96861 | -47.14155 | 2026-08-03 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65197380-5c71-37b3-b421-9199148c93bc | -11.91409 | -55.89622 | 2026-08-03 04:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 955f62b4-2389-3688-9e1a-4e4580433d97 | -11.5827 | -50.23095 | 2026-08-03 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9015faa-7cf0-3775-807c-1e1211d15b69 | -11.25538 | -54.83624 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1719ef97-73c3-38c5-a70b-1d7f826f44a0 | -15.23629 | -52.90207 | 2026-08-03 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a2ac17e6-de6e-3c9e-94a7-f1b2bd59a132 | -11.27254 | -54.84173 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fd71871-39a6-3b27-bb3d-1afe65c48184 | -15.23489 | -52.91027 | 2026-08-03 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82b23864-2a86-33b2-b226-af3ad89d3ea0 | -12.27247 | -51.54705 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67fa2478-e1f1-3ae3-97ab-cc7a7701be4b | -18.25582 | -49.40795 | 2026-08-03 04:40:00 | NOAA-20 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0b7d1d5-3e0b-3194-aa6f-d704fd6da2e1 | -12.27183 | -51.55089 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47cbc799-573c-3b3c-8066-8909be43b51f | -14.35238 | -48.0569 | 2026-08-03 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8de1cf05-1b8a-3746-ae20-7aaf8d38182a | -10.59373 | -50.01678 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 231222a2-6ba3-3185-a297-9192fec391f8 | -11.23393 | -54.86023 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50ffe818-9105-3b24-8111-471827e6b5b9 | -16.3594 | -52.41451 | 2026-08-03 04:40:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8934ed6a-4db7-30a5-a30e-0c3cdc2a6506 | -11.23672 | -54.86892 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f2f2d11-1199-3085-8db3-384fe040add3 | -11.25122 | -54.83543 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3723a3ae-fe83-3a4e-8eb1-6d35e049dea7 | -18.25639 | -49.40421 | 2026-08-03 04:40:00 | NOAA-20 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 51a26feb-1857-34e3-b090-b7234189a359 | -12.24394 | -51.55484 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bff0e52-3af5-3239-9269-bd70f5289e0c | -12.26997 | -51.54738 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7ed0a76-6f86-3125-a641-ff8a31599e3f | -11.45047 | -50.72563 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2962866d-20cb-3935-884d-3158016fbb64 | -16.22157 | -45.49419 | 2026-08-03 04:40:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57c7913d-16d2-3fca-bbfc-2591f3a60442 | -11.2767 | -54.84257 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcf1f2f9-9a9c-38a7-a619-1dd619eb4f28 | -12.1982 | -46.98159 | 2026-08-03 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a665e43-6632-3e51-93a2-687c0c4e090b | -11.22837 | -54.86728 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 893bafcc-33b1-33e3-9baa-857444f7ede3 | -11.2381 | -54.86106 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de8e8f52-226f-3da6-9d25-9c01ba4562bc | -16.66321 | -49.13113 | 2026-08-03 04:40:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6651e3df-3790-355a-8123-87997c2e7bc1 | -11.24907 | -54.82307 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cc6b0328-32c9-3087-9b3f-4ca222e86901 | -11.25257 | -54.82771 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 555470eb-757e-35aa-a1e3-eaebaf5a5eb5 | -18.63782 | -43.26556 | 2026-08-03 04:40:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 06336b82-07ac-3188-aa4c-3b1f5666e811 | -11.26235 | -54.84573 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ded86d58-e00b-311c-b4e8-6ae392e415c7 | -11.52854 | -46.89577 | 2026-08-03 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04e03883-553b-32ee-8d95-74674343ba42 | -12.51279 | -50.3632 | 2026-08-03 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27565895-8b84-327f-8ea5-2f1ce12b8eeb | -11.13732 | -50.40131 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d5e0c57-ff5d-3600-8069-0371ca7449ad | -15.23559 | -52.90618 | 2026-08-03 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6b70e132-87d5-3da4-85c6-94ba9a0f56be | -17.9665 | -51.61375 | 2026-08-03 04:40:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| accbd42b-2c37-3082-ba78-f65d4ab29ae2 | -17.96493 | -47.1411 | 2026-08-03 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a83b90fb-c77f-3863-8440-de493fa2351b | -13.68457 | -51.99 | 2026-08-03 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 501c88d3-ee77-396f-bb20-7102d595d9b6 | -11.27324 | -54.83784 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fa3a152-819c-3da5-b463-9ebb51b68972 | -11.45237 | -50.173 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5154ec28-b444-349f-ba16-4a6177633e5c | -10.60214 | -50.00719 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b46d9b42-fdda-382c-b207-91865d1d2a9c | -11.25818 | -54.84491 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd76a36b-283c-3806-91c0-f73883b31247 | -11.25955 | -54.83705 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4787df0-41c7-303c-b5d7-b5e50f63db87 | -11.26303 | -54.8418 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c3ad38a-17d5-35cb-94b3-22f043a27b15 | -11.24159 | -54.86581 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b931f368-5111-3885-8f93-babffa98542c | -11.82621 | -49.60245 | 2026-08-03 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5421f8c4-1d06-3547-96f4-cb25a4324f14 | -11.52796 | -46.8996 | 2026-08-03 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96074863-dd64-354a-98c2-5ac62921ff47 | -16.33824 | -43.33438 | 2026-08-03 04:40:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9d31456-3c05-3e03-a6d3-60c37e61ef3a | -14.34735 | -48.0672 | 2026-08-03 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfe2a0c6-d233-3249-a893-f14a60bf812f | -11.91851 | -55.89709 | 2026-08-03 04:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5d12339-eeae-334e-b5a8-300babdafb4d | -16.35876 | -52.4183 | 2026-08-03 04:40:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3fb81136-922e-37fd-a344-6a3a5a0bc2e0 | -11.27135 | -54.84348 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a0a8535-1131-33d7-b3cb-83f38f435676 | -12.26652 | -51.54678 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fd345d4-c8f0-3caf-b2e6-7b4dc5d7f10f | -10.60272 | -50.00362 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 712d22aa-8bba-33a5-bda3-02db1a0b142c | -11.23598 | -54.8486 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3194628e-2957-37f3-9caf-f1f971065166 | -12.26903 | -51.54644 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bef96ae9-2fb8-3fa1-bd1b-49ac8d07dc0d | -11.26767 | -54.84481 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfcc7102-14d0-335e-b047-8d2b64ce07ba | -11.25606 | -54.83237 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e319aaf4-4222-3c81-910e-ee6e9f9fa6f3 | -11.45295 | -50.16943 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f38dd13-bd3c-317f-9c7f-802f217a82b0 | -11.26422 | -54.84006 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ed2a9d0-64bd-3afd-ab97-a0577c916c97 | -12.26934 | -51.55124 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 845ea55e-c373-35c7-8b38-3dab6dfd3829 | -11.27183 | -54.84563 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67ec6a3c-1403-359f-b1fe-6861249b997e | -11.25189 | -54.83156 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dad1afc-e6e2-3f69-9f8e-d4c899aab72f | -17.96316 | -47.12664 | 2026-08-03 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a1f26123-7120-35a2-9f0a-407d4ce14320 | -14.54599 | -53.1158 | 2026-08-03 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85f46913-ffe9-3d41-98a6-6fdff91dc9c2 | -11.27068 | -54.84738 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5188152a-9cf0-3ea2-af29-0c32558d1dfe | -14.03263 | -46.29592 | 2026-08-03 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9bed2d8-6c2c-31fe-89de-029cead9ab21 | -11.2774 | -54.83869 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4c4cf88-ea48-35ce-8b42-89fbba1aa01a | -11.276 | -54.84644 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9af0330-5b1a-3116-a1e7-019499dc606a | -17.86617 | -40.05177 | 2026-08-03 04:40:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a8d18ab9-aec0-3689-8799-42d13603689f | -11.22907 | -54.86332 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15afa60e-9392-334e-b5c7-3046fad37872 | -12.26589 | -51.55064 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fb89f60-d1ab-3b40-9d2f-861aec23672f | -11.1379 | -50.3977 | 2026-08-03 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8e4c2e8-39c1-3051-bcc4-26cd877285a1 | -11.25053 | -54.83933 | 2026-08-03 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 913b0294-e36c-3a0d-b455-8fbcb80716da | -12.24647 | -51.53948 | 2026-08-03 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e9eda1e-435b-3909-ab7b-6e3842ee1b63 | -13.06048 | -52.71696 | 2026-08-03 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 627a3ac7-8d8e-3fbd-aa4e-79006cad73d2 | -14.41484 | -49.68718 | 2026-08-03 04:40:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f1b3fa5-c838-348c-8fe9-a79e61ce83bb | -19.04552 | -45.95933 | 2026-08-03 04:42:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 876c0167-e98b-3308-bac8-28bf532cde17 | -19.31187 | -48.92033 | 2026-08-03 04:42:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b33834b9-12c6-3cb6-9f5c-ce3a5cbdcbf5 | -18.58515 | -48.70592 | 2026-08-03 04:42:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee1f1a5e-0508-3059-9bf2-6f75af072f8e | -23.19356 | -49.1547 | 2026-08-03 04:42:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ce34a34-3cee-3597-a8e4-909057baca35 | -20.38706 | -50.01379 | 2026-08-03 04:42:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9fc7c064-4194-318a-a537-4b962f093eda | -21.64107 | -43.05285 | 2026-08-03 04:42:00 | NOAA-20 | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0055dbd6-e131-3635-98aa-06454641ff7c | -23.27746 | -46.09805 | 2026-08-03 04:42:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9e6e6833-bd14-316c-b833-61c6bf856d5d | -23.3141 | -47.23261 | 2026-08-03 04:42:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6bd8b424-fdc6-3b23-b9f0-f7e5e5b64a48 | -20.88041 | -45.54574 | 2026-08-03 04:42:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1472cbbc-dea3-36cd-8455-b65bfdc7ab9b | -23.38588 | -46.23156 | 2026-08-03 04:42:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bcb7365f-a3cb-3780-a6f6-252bffb35d4e | -23.31411 | -47.23417 | 2026-08-03 04:42:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4eab190c-e682-3483-8cdd-481add700891 | -22.15673 | -47.36746 | 2026-08-03 04:42:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0ce2f015-a41e-3e1d-b4ef-366861eab775 | -23.42913 | -46.75831 | 2026-08-03 04:42:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 04d14800-58f7-360c-aaa2-e45974cbb79c | -19.77238 | -42.08192 | 2026-08-03 04:42:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8c37b335-7bd3-3122-a089-9e64059039ca | -18.58425 | -48.70478 | 2026-08-03 04:42:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 285a3ee1-e169-3223-bae4-c9bf5f91ebfb | -20.97702 | -48.99567 | 2026-08-03 04:42:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2cd3adc4-f77c-3f6a-b02b-a7077ec1cf71 | -23.31799 | -47.23326 | 2026-08-03 04:42:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 405c313f-72db-3edd-9a65-692389116917 | -18.26963 | -52.09341 | 2026-08-03 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43d25894-234d-319e-a9ce-37841d520b33 | -19.23331 | -46.99583 | 2026-08-03 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9c279bc-5207-3646-8c2e-c5f0ed8a7936 | -19.22955 | -46.99535 | 2026-08-03 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e0b7a61-fdf2-334b-a361-c6a83785eec8 | -21.50705 | -48.8196 | 2026-08-03 04:42:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README8.md)
