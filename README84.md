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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 262731a9-b3f8-3a37-a77f-acf1d2477880 | -6.68339 | -55.05841 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cd8861b5-0f6c-3f50-8eb5-67cfa350dc9c | -5.93034 | -59.91544 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff48b1cc-3671-3001-b199-8c44ae8cb8f0 | -8.80954 | -44.264 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 844131f0-3f32-3d71-b9dc-abfb691851ed | -8.25415 | -50.87124 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdbe4dd0-950f-3a74-8ed4-ab393367dc4b | -6.77512 | -58.60871 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ece372d6-fd60-3a99-9946-dce013d3c458 | -11.46288 | -47.74887 | 2026-09-23 05:04:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e43bcbd5-c8cd-3899-ae0d-636798bbf19a | -4.06538 | -56.2258 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eda5afea-701f-3396-9841-0a37f063df72 | -6.78339 | -48.6846 | 2026-09-23 05:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5988f9c-3fbb-3edc-9db1-682fe206a41b | -6.10595 | -44.15126 | 2026-09-23 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19706a30-cbd2-346f-b8df-74cbfad97d06 | -7.42439 | -49.85838 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b3705c1-a15f-371a-a37e-96a2d40a16c9 | -8.18027 | -54.82521 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1b7ec77-46d4-35c7-9e9a-dfc3cb2bb56d | -6.88751 | -43.75271 | 2026-09-23 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 731d88e3-e5b0-30f9-b73d-946848feff44 | -6.89966 | -43.62986 | 2026-09-23 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d21537a9-3b8b-3911-bd74-9898bc1ea916 | -5.88949 | -52.10326 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e39ec7a-7ee2-36a8-baed-9e7e212fee29 | -3.10558 | -60.72264 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d7b2697-d1ab-3e8d-a26f-71570424c27b | -6.04899 | -57.8247 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cf192d6-f099-3aca-863e-9b53c79a171b | -7.13819 | -48.42528 | 2026-09-23 05:04:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2014d1bf-b84d-312d-a4f0-3581e4de393e | -9.16439 | -61.36105 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8268cfb9-3ccf-3dd5-b835-b77ea224a6e4 | -5.80907 | -52.07642 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a08a2221-dee8-3028-b6b0-955843a6e083 | -6.14257 | -59.93495 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d00d3aff-63d4-31e2-a3b6-321f25a53f04 | -10.69523 | -48.72235 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 030a3dfc-d273-3e22-aabb-7562e748f0ea | -6.52952 | -55.35681 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0cf1703-1ab1-3548-a824-8beb1c856590 | -11.11602 | -51.05452 | 2026-09-23 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 860db9c8-9559-3868-943f-b2f8422df49a | -8.45542 | -51.48957 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e7d0b90-a2e3-3188-a43d-c61d4b6cb847 | -5.88498 | -53.61953 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7429c2cb-3d97-367b-bba4-513d7c275a7d | -8.49295 | -57.61258 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 81cc0273-5991-3c66-957a-178e096e350e | -8.30497 | -54.76899 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 307f28a0-4681-3ddb-82bc-4435431786d1 | -9.94621 | -48.47234 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9774963f-db23-35c7-a7ac-c66bc90212c2 | -8.61869 | -54.62268 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a332536f-dd21-35eb-8856-e89b7bb4fcfc | -10.45605 | -46.28251 | 2026-09-23 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ca4020d-efa3-3db8-91ca-7ba37e11f392 | -6.35845 | -58.29314 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1223ecf-fa77-3e3a-a521-e7495f33d1de | -10.96907 | -54.1567 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10fe795f-4b84-3daf-b2d9-bbe3a1283318 | -5.69812 | -47.3894 | 2026-09-23 05:04:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76c53dad-b42c-3ac1-b512-50fbfb05e80c | -6.43339 | -55.61745 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 006e09f8-c12c-3986-adc7-ef8f319ba504 | -11.43632 | -47.39193 | 2026-09-23 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| afc00b53-77cf-33f6-98ae-6cf1e7aa06a0 | -5.89391 | -52.09687 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 41f71641-2abd-36bc-9c1f-57d7c885611d | -8.44857 | -55.0212 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74c8e0fe-e131-36a3-811c-1fbc07c87174 | -10.24578 | -45.50394 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1eb3ab18-3592-3bc6-ab23-47a2c0efa175 | -7.42452 | -49.83299 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 30dc96d9-9fbb-3508-b619-e49a9b6cca97 | -3.14764 | -60.63181 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdb72fc3-a260-3f56-b40e-6594dba62a00 | -6.13778 | -55.66545 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7de438a6-a080-3eda-b420-ee2ca8b01258 | -6.67515 | -55.06493 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21044737-e0c9-38e6-9889-0016c5c62a31 | -8.36131 | -45.60925 | 2026-09-23 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf2a47be-9048-348f-8e15-f0d6546d2da0 | -7.09853 | -52.7581 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 432ad8e2-d46f-3768-8337-853928348719 | -6.72379 | -44.15134 | 2026-09-23 05:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5a94bba8-ed19-3ae0-b1de-0bd8f722ea30 | -9.25577 | -65.44051 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f34b89f-bc28-3425-94e0-bdeba3377857 | -10.24943 | -49.97014 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3052aeb5-837f-3a5f-8922-9e598fe4746f | -5.92948 | -59.92042 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fedfa054-4077-3919-af80-304e9798df78 | -4.50929 | -54.98603 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b3eabec-1f4f-3905-9253-884c0e9dcc16 | -10.70737 | -48.70533 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c635ed44-7e05-35ff-b975-c8a73b7d4934 | -7.12197 | -56.54887 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28ff4d3f-120c-3f87-9080-3ee89f39a0e5 | -11.40825 | -44.03219 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 12266570-ab6c-36f9-891e-d21592cacb8a | -3.60853 | -60.56982 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30d932ed-af16-3ff8-8c0c-d0df2457fae4 | -3.64575 | -60.60854 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 008f76d4-a5bf-3042-af79-6cdc8d0d9cef | -6.9288 | -46.56004 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e73745d-abb8-3143-8636-0aa1fb0227c4 | -5.61062 | -43.35313 | 2026-09-23 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f3d2d0f-8d0a-3271-8c3d-3d16bc671db0 | -8.81387 | -44.2716 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 700d013a-8587-3d50-9afb-9dcf526ad6f8 | -8.16999 | -54.82352 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 214d7537-75bd-337a-bc8c-3feaf5d236db | -10.8731 | -50.15172 | 2026-09-23 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7b7e3f4-bc4e-3434-90d8-15248cdf4a92 | -6.66471 | -58.57029 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6852d31-b4d7-3628-baca-01030d18da67 | -6.44439 | -57.77532 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b937119-c59c-308d-b1bf-e3f5c5933d42 | -8.25531 | -54.7722 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb878803-aeb4-3067-bdb0-6978aed4d500 | -4.33713 | -55.65377 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a8da249-27bc-32c7-a12f-d41c9c969cc0 | -5.17666 | -56.18199 | 2026-09-23 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ea8bcca-468f-374f-b88a-0bfc45a88829 | -10.25856 | -49.98498 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a474b38-0a64-313e-90e0-da9b5079161c | -7.98547 | -47.46636 | 2026-09-23 05:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f49d24bf-d06d-3400-b8c6-cf23b42121d4 | -6.09274 | -55.55585 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c48c1afd-8fa6-30a7-8425-408e6c08453e | -7.15267 | -59.59442 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5fe9742-844b-3d11-b23f-dc6b1c400a02 | -8.80435 | -44.26274 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a9bca5a-ca53-367f-b528-536d3ac14612 | -9.57379 | -46.53733 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b1b3e520-fa1c-38eb-b06c-5ea12baba794 | -3.11725 | -60.68516 | 2026-09-23 05:04:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b813a473-1b53-3905-9a47-d200dbcd79ad | -4.53748 | -54.96985 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92b2a525-bb19-3b2e-acfa-71f66cbf3676 | -8.92095 | -61.48942 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38517826-0eeb-3136-98a0-e95897ac2b0a | -8.25901 | -45.42903 | 2026-09-23 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a6a4801-7d1d-39a5-8f92-a6f63e71ef5f | -11.29843 | -51.35215 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 882f6649-862b-3aa0-9bbf-ead9640a7f57 | -3.68965 | -60.56867 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39132249-8e86-3f6b-8b17-4a820a5613d1 | -9.01161 | -49.81927 | 2026-09-23 05:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fd124c1-a72e-34dc-ad50-6348766a4dce | -11.11727 | -48.31393 | 2026-09-23 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d681d229-a9f2-3b04-b7a8-e3f7a7a6026b | -5.13817 | -50.05219 | 2026-09-23 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f90efe38-1adc-3e54-82da-476647833528 | -6.68089 | -55.07388 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98fc831f-bda3-3322-ad0f-49c31685050b | -5.94894 | -52.18033 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e491abd0-6045-3086-8d2a-1a88d7832850 | -6.46157 | -59.98651 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9a6af122-add3-3a7e-a6c3-43bdcaa13582 | -9.93816 | -48.47122 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db6a6456-82d6-3de2-9202-debf7b61adaa | -8.48627 | -46.86353 | 2026-09-23 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16a12c4e-3ec4-34f7-88a4-8d36f7636de7 | -9.08952 | -61.43432 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3f312e6d-b6ca-3519-a1d4-80b90fbff2bc | -8.75776 | -45.83811 | 2026-09-23 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a804b1d3-e081-35e1-8fed-6273d41bf5aa | -3.08831 | -61.16794 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 539504c5-bc64-3229-9d48-f82b3e02207b | -3.39202 | -61.06755 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f44d9afc-899f-3a4d-a5c1-e91368ab28f7 | -8.31283 | -54.78538 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 624aaef4-d587-3b35-9bc5-bf2de6ca61e0 | -8.44513 | -55.02061 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86983530-ec90-3903-8790-29e5e262c02f | -7.31433 | -44.16779 | 2026-09-23 05:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0c78220-aec4-3735-97e9-8388bf7711f6 | -9.18664 | -65.85445 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a038bd15-6f12-36a7-a7cb-2a64d6fc3d5a | -3.11191 | -60.71712 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c30a9419-2595-3c6b-a43f-bc20d53540aa | -5.76654 | -56.52098 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 452abf38-f490-321e-8152-8d4424391abf | -3.82117 | -59.33458 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59bc2b76-3fdd-346e-bc11-bc47029869bb | -6.67058 | -50.94513 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d330147-73b4-3d9f-b99b-ad26cc516815 | -6.81495 | -59.45816 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 269e1495-8297-3b3f-976d-1753af627af9 | -4.8343 | -55.76821 | 2026-09-23 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ce92f2f-2190-3e43-b422-341e7d985951 | -9.01529 | -49.81982 | 2026-09-23 05:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbb13c58-8e97-3179-b2f8-c4c0f337be0e | -6.93899 | -46.55501 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README85.md)
