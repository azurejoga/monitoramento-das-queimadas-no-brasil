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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dabb749-e591-3ff8-a729-f3afbf997ce3 | -13.95529 | -47.83102 | 2026-08-01 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8637e59c-a8e1-3ad4-a47b-3907cd29b92e | -14.07922 | -46.23198 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d8e280d-d653-322f-8f89-74517b9b6799 | -14.06901 | -46.25483 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77712b83-2e0a-3b2b-ae0f-8406dc64b05f | -13.06673 | -52.71929 | 2026-08-01 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb23348e-cf5d-3b2a-897a-aca10576094e | -14.0718 | -46.269 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b4f33e5e-0389-3f68-97a8-2dc1b408713a | -14.0769 | -46.24929 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbba5181-9d6c-3820-b242-1a4dca7771ba | -13.95322 | -49.14701 | 2026-08-01 04:57:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4be2b3d4-1498-3c30-b647-6b0b8402ed14 | -11.21614 | -54.0475 | 2026-08-01 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf30d068-656d-3afb-acf2-d5e83fa23a5b | -11.24507 | -54.86793 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| afebb605-c113-34d6-8a40-a678fcd9c05b | -9.71763 | -47.31686 | 2026-08-01 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8593bd09-d88d-3330-8e23-1d351c7f24f2 | -14.08283 | -46.27331 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3710ad9d-8b52-39ae-9745-b1b94e1ed40c | -10.95467 | -49.80572 | 2026-08-01 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e156541e-f630-3844-9564-b9f741562544 | -14.08977 | -46.23559 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 841beac3-1afc-301e-987f-ea3bb06e57b6 | -14.87673 | -52.76413 | 2026-08-01 04:57:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dcf9a48-8cdb-3b27-8e7f-dd625ab120b1 | -14.0757 | -46.27435 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de3ed3db-cd27-3bbd-a2f7-7cf836fa9c86 | -14.34393 | -48.03881 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2450116f-37fa-3281-9765-3d1d80a87402 | -14.0835 | -46.2849 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58805ff3-e672-3b60-87d3-c06e01fba2f2 | -14.07834 | -46.27266 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7503daf8-465e-326b-ad5d-bdaa231b18bb | -14.07959 | -46.27969 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 978db477-75f4-3282-b0e5-79301b43c19a | -14.07201 | -46.28579 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 78fbe3f1-6982-3f42-8ee9-407a58012cc5 | -11.22383 | -54.84378 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d37a7378-ba7d-3cf1-9d1a-23eaa196eb8c | -11.22449 | -54.83981 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26bd2d85-129c-3723-9bc7-d4cd1beb4519 | -11.24792 | -54.87252 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 075efe82-9d38-3b1f-93ef-b8782d946f66 | -11.24288 | -54.85937 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1200a46a-3fbc-330f-ae57-28da0fae5748 | -14.08584 | -46.23042 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 289f04b6-a375-3dd0-b234-e51e265a3715 | -11.2534 | -54.86124 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 01a6b85a-c6a0-384b-95d6-78c1f0ad68fe | -12.30686 | -43.72871 | 2026-08-01 04:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39e5ab73-f591-3e01-a0a1-669c6277359f | -14.08158 | -46.28257 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cfd2a469-1e2d-3b7a-928f-16ea2e054576 | -14.07408 | -46.25091 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 096a162d-847f-36d5-bf3e-193553ef855b | -11.24552 | -54.84353 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d3b2eb6-3383-3074-8047-64309f8369d8 | -14.06939 | -46.27125 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b5a44b99-3848-356c-bfff-0182557c59e3 | -14.08741 | -46.29002 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7a99ea1-e83e-320f-8fe0-55498bd240e4 | -11.24441 | -54.87191 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e148c07a-8761-3d67-9dff-0e7f3da02ef9 | -11.24836 | -54.84812 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed7b30e8-449f-348a-afa9-b59bacc4f1c2 | -14.08371 | -46.23266 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6798158-ffbf-31e3-9478-b3f0940074bb | -14.77383 | -48.30172 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e1c0473-887c-32fb-85e4-c36f4fc2065a | -13.95579 | -47.82743 | 2026-08-01 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1978c97a-9b3f-3754-a7eb-bf8e0f5b5139 | -14.07974 | -46.29627 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60bba9c6-ccfb-381d-b6d1-17435655acc1 | -14.40993 | -48.07027 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e12ab358-e1a7-345c-aee1-98d52aabc3e2 | -11.24771 | -54.85207 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0dc32c1f-042d-3015-a4c9-aa26285a6715 | -14.41321 | -48.07619 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 885b6950-268f-3a0e-a416-8424ec9c7112 | -14.07386 | -46.27196 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f0b9ccf6-eb9e-3367-b3e0-68949b54b9eb | -9.2675 | -50.69022 | 2026-08-01 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af16a9d8-f9cf-3a7b-b942-f83ab90c2732 | -13.25967 | -54.3562 | 2026-08-01 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71489b82-c690-3768-bd6e-4b50d3083e43 | -14.0757 | -46.2583 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44fe828f-8be9-3539-9dec-be2aa3e6a979 | -11.24223 | -54.86333 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6775c4ec-9f43-3f7b-afb8-48d431526b97 | -14.0822 | -46.27797 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 276d4787-01a3-3dc6-856f-4957be2bb4be | -8.1905 | -55.43918 | 2026-08-01 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 910090e0-bcd2-359d-95bb-3e7e40d37394 | -11.23038 | -54.86944 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d400e679-d570-3017-8763-53c1dcd8607a | -14.41011 | -48.03885 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85593160-3d8d-3a46-b40e-c84bf5e8129e | -15.58106 | -46.80767 | 2026-08-01 04:57:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4492d4a4-fb0c-3914-a47b-5409a2a3977a | -14.81581 | -48.50853 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2cf7b88-bdc3-322b-9872-23800c096573 | -14.08138 | -46.25008 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2243ca6-03b8-39e7-a5bc-834fb2a34825 | -14.83139 | -48.51157 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5b76785-ef41-39ad-ab4a-42cadc6ac4ba | -14.07295 | -46.25989 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 51d803c1-24d8-3e5a-b388-bae9422faa08 | -14.33205 | -48.0359 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b51d6ae6-6437-3e4d-a7a2-20f935777901 | -14.06877 | -46.27586 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 60809446-1fd1-32fb-8ffa-bdf2837524b2 | -11.28932 | -47.03838 | 2026-08-01 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74069a94-2a92-3f3f-b552-06be876f8ad1 | -14.3526 | -48.03528 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaa3c6d5-2231-3955-aad8-e160f61763fc | -13.94181 | -49.27982 | 2026-08-01 04:57:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f2b0a7e-251b-38c2-9135-f31b2a7a14e7 | -11.25406 | -54.85727 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ac1833c-a80b-31b7-b72f-1581858c443a | -14.08077 | -46.25461 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c700dc7c-08fc-302a-91c6-095df8738c30 | -11.22515 | -54.83586 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6318ddd3-447e-3663-a0d9-b15f5532e19a | -14.07352 | -46.2554 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0eccb9e-5083-36c5-8835-2da7d8b6f4e7 | -14.07262 | -46.28121 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 42aa7f98-ec99-343c-9d48-1ed4e4f72446 | -8.45039 | -51.50668 | 2026-08-01 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1c5b456-87be-3a4f-8c04-141267acbf16 | -8.19799 | -55.44045 | 2026-08-01 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28e2bb10-7d6d-3ad7-8384-4d376cdfaf3c | -14.22076 | -51.92028 | 2026-08-01 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 827de453-cc87-333c-bee4-530f9b385bbf | -14.41365 | -48.04296 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ea7110c-037c-3e76-952f-1f5d799edf72 | -14.81511 | -48.51359 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02208180-6675-3b65-a642-aa00f627cda2 | -11.2442 | -54.85145 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8933d0a4-f108-393f-93d3-f2e448b264a0 | -9.4827 | -57.32542 | 2026-08-01 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8458a886-cbc1-3937-8720-1885003fdbc5 | -14.07509 | -46.26279 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 39dd48a0-a584-3cee-9379-86264e826635 | -11.2499 | -54.86061 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a64fb879-21c7-364d-962b-fcfa7d0d8360 | -15.92012 | -48.3239 | 2026-08-01 04:57:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2de56bc1-cf55-364f-9f57-2b2eaef47aac | -11.24069 | -54.85083 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22274f76-74ec-3f9f-a082-0b938574c968 | -14.83994 | -48.505 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b9d0192-d95e-3cf8-9432-b4c87f1db6db | -11.24858 | -54.86855 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 98fc2547-d533-3b2e-a204-d36f0f8e7f0d | -15.45043 | -41.3793 | 2026-08-01 04:57:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d44763d6-fdf0-3d23-b426-a9cdc72e74e4 | -14.34112 | -48.02953 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 509c5de2-619c-3904-9d59-81bfaf9a8dc7 | -15.44357 | -41.38382 | 2026-08-01 04:57:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ffae5a53-b85d-3c13-8f63-5d79cc1f92c2 | -11.5491 | -46.912 | 2026-08-01 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0017ff9-162e-31b8-9100-0f818260197f | -14.41412 | -48.03944 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4595846a-52d9-3f40-9a79-c30f82a88eca | -14.07324 | -46.2766 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c3eec99-8934-3b0a-adb5-ce9d1dc0e606 | -14.06845 | -46.25929 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 752cd91e-0c55-3fe9-a364-2926a0be5474 | -11.24354 | -54.8554 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 711bb3ce-9bb3-3f2e-b4c9-3a3d8fd1a318 | -14.06692 | -46.28964 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 724191ec-7d16-3e12-9752-c014649908ed | -11.77553 | -50.16518 | 2026-08-01 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b32a382-3700-37b9-b074-f85b7e4a1bed | -15.44408 | -41.37896 | 2026-08-01 04:57:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 03ba6f3c-438a-3e1c-ade0-9417ef2a6a2d | -14.06889 | -46.29204 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 541cfcc5-d08a-3abf-828a-aa9ab1a1dfdb | -15.82056 | -48.17696 | 2026-08-01 04:57:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71bf3af4-44a6-3317-9334-a996e6b691e1 | -14.83982 | -48.50853 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95083966-09e6-30a2-bd31-6f3bd47a7ca9 | -14.07915 | -46.24707 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28666bde-1c95-303d-a6ad-823a3ef3b6cb | -13.95175 | -47.82685 | 2026-08-01 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bcbad81-d0de-3c05-845a-96b33e023191 | -14.07122 | -46.27362 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 38f7c55b-2c41-37bf-942a-f604b02f57a5 | -11.22799 | -54.84042 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddffb400-7bae-34d8-b8db-c294c8e6483f | -14.08077 | -46.2704 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b823255-4f9f-3ea3-a1c3-bdcc11e532a6 | -14.08363 | -46.24789 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2055be47-7752-3897-8cb6-edd1ab652082 | -14.07181 | -46.25314 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36dfff49-8e7b-3473-a6a1-b5ff9a258070 | -12.6113 | -44.61368 | 2026-08-01 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README20.md)
