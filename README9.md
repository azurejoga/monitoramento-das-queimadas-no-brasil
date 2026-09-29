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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b37e1d3f-5f28-3cbd-bb10-f6e5f3fd76b4 | -11.4302 | -43.4596 | 2026-09-29 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 77f7477e-8a4f-31bf-8df1-71779884f1dc | -3.8202 | -55.899 | 2026-09-29 03:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| dd82f2d2-6861-3b64-ae39-adf1c73e108e | -9.177 | -61.4073 | 2026-09-29 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 97befd1c-1c2b-3695-bd91-915d3490b9c5 | -11.1775 | -44.7832 | 2026-09-29 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| a6b8f87a-c6d4-33c9-8cae-857daa207d0c | -12.7606 | -50.6857 | 2026-09-29 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 91f5006b-4e4d-3aa8-aa3f-6e145a7c0a92 | -9.76426 | -36.98862 | 2026-09-29 03:13:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4fc69c40-aac5-3c29-bc96-074fd20208c5 | -9.76546 | -36.98251 | 2026-09-29 03:13:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 901e6dac-f37f-3e3b-8676-1bd96ccd170a | -9.77179 | -36.98416 | 2026-09-29 03:13:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3cae6bcb-3188-35c0-ad60-96383bec768a | -9.76667 | -36.9764 | 2026-09-29 03:13:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 05176061-2a2f-3658-a714-146d2f6c6f2e | -11.42 | -43.48 | 2026-09-29 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bcb335c8-97b2-3b1a-8961-b1409e811c7a | -15.25 | -43.28 | 2026-09-29 03:15:00 | MSG-03 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| ef64dee8-3d05-37b5-be59-47cd87552823 | -11.42 | -43.43 | 2026-09-29 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c1a4a249-9833-3292-bc7a-f69acbf8ead0 | -18.84774 | -41.99643 | 2026-09-29 03:15:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| af9a13cd-fea0-3483-8f34-4a843f67cf5f | -3.8202 | -55.9187 | 2026-09-29 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| b2dd7574-dc39-39e5-837c-4c5ca9bd13f0 | 1.6567 | -55.8833 | 2026-09-29 03:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bd95d993-4765-3cb6-943f-22bbcc49af52 | -11.4298 | -43.4833 | 2026-09-29 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 86d454b4-605a-331e-81c0-e0d02d39cf0b | -7.8297 | -45.8156 | 2026-09-29 03:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 3096812c-c259-3727-90ed-3427a45f12c4 | -15.2517 | -43.2501 | 2026-09-29 03:20:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 04acb490-3dac-3d78-9044-374cf5ab00d4 | -11.4302 | -43.4596 | 2026-09-29 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 80ffc779-9c18-3f08-ab4f-2acc9ceab283 | -5.6081 | -45.0038 | 2026-09-29 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 3ec168ba-56a4-3cd8-abc7-444535d209d2 | -11.4307 | -43.4358 | 2026-09-29 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| ac5c495b-8387-3168-bb24-92f2f3ed9b7e | -11.1775 | -44.7832 | 2026-09-29 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d0efae7b-3ae1-35f3-8777-62f41c0625ac | -7.4074 | -40.2299 | 2026-09-29 03:20:00 | GOES-19 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 57.1 |
| 3d073727-b8ba-3bec-89cb-a0a8e507d460 | -15.2511 | -43.2743 | 2026-09-29 03:20:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 197.1 |
| 3f9f7591-a3d2-3f71-b167-7460fa8238c5 | -3.8202 | -55.899 | 2026-09-29 03:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 8184c070-e77f-3f3b-9f52-2a419c75ed85 | -9.177 | -61.4073 | 2026-09-29 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| d0df7f9c-ec17-3092-a18c-96fdf8721f29 | -7.8486 | -45.8138 | 2026-09-29 03:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 7c07772c-bed2-35e1-8fe1-3077f32d4edf | -11.411 | -43.4625 | 2026-09-29 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| a048d3cf-f6eb-3578-bd7f-ce20aa84e181 | -11.4495 | -43.4566 | 2026-09-29 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 7a9bacc5-7a72-3564-964a-816853e89a0e | -11.4115 | -43.4388 | 2026-09-29 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 99e94bbb-c9a9-3069-b7d4-c1aee128894f | -3.69325 | -39.58178 | 2026-09-29 03:28:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 04b767c0-5d3d-35cb-acb5-f0dc05593f1c | -3.69382 | -39.57845 | 2026-09-29 03:28:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 43eb7f15-df15-3b19-aa47-187f68a8edd8 | -3.68773 | -39.58102 | 2026-09-29 03:28:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 20d0217d-0894-319a-82d8-81d085c9afe6 | -3.99878 | -38.98428 | 2026-09-29 03:28:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cb3f5702-2aa3-368a-b7de-ce74453a7ac4 | -3.68837 | -39.57723 | 2026-09-29 03:28:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b336084f-2582-3ba6-8bdd-7275513a57d5 | -3.8202 | -55.9187 | 2026-09-29 03:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8b763404-1fc5-3d25-972d-483edf326dd8 | -12.0658 | -46.487 | 2026-09-29 03:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 8c6acb7d-0a15-370c-83d9-0354f0c46d36 | -7.8486 | -45.8138 | 2026-09-29 03:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 27eede7d-6320-38a4-9c4a-e801078cedaa | -11.411 | -43.4625 | 2026-09-29 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 6c4cc712-ab56-31c9-8658-2038564e9c57 | -9.177 | -61.4073 | 2026-09-29 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 1e04f952-44ee-327e-9d1a-719aa75b7915 | -3.8202 | -55.899 | 2026-09-29 03:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f8d75a18-1e17-33d8-9c08-c8cd0629f3f7 | -11.4307 | -43.4358 | 2026-09-29 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 5636a8d6-1ddf-3e1e-a759-268d36f990f6 | 1.6567 | -55.8833 | 2026-09-29 03:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e934fc1a-4297-3141-8279-4edc2f4695d0 | -9.1584 | -61.4082 | 2026-09-29 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 33bbfd24-ed38-3b17-ac78-cb66102956e2 | 1.675 | -55.8831 | 2026-09-29 03:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 5d97f59f-12e5-3aed-96c4-1cb457a3bf9b | -11.4302 | -43.4596 | 2026-09-29 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| daf8e719-0237-313d-91e3-44f4e24d3e16 | -11.4115 | -43.4388 | 2026-09-29 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 140b789c-7d8a-35e0-953f-124cd1ce21a9 | -15.2511 | -43.2743 | 2026-09-29 03:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 128.8 |
| 8ea586be-b497-3d82-8374-d772c16c1afe | -15.2314 | -43.2784 | 2026-09-29 03:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 8ca8bc2f-7148-342a-9101-8b0946cfdc0a | -5.6081 | -45.0038 | 2026-09-29 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 2964e490-64fd-326f-a8de-d9677ae31284 | -7.8297 | -45.8156 | 2026-09-29 03:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| cba40511-1795-31da-b2c9-9551e9728157 | -9.76226 | -36.98153 | 2026-09-29 03:30:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ff0b6d26-28f7-35d5-b071-1700ddbddc96 | -5.0296 | -43.576 | 2026-09-29 03:30:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0201554f-ebc8-36d8-b4f2-4c36380c711e | -7.40274 | -40.22505 | 2026-09-29 03:30:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 18.8 |
| b4394ca7-3f10-318b-8026-837693e69a75 | -7.40601 | -40.2248 | 2026-09-29 03:30:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 78fef53f-88f3-3ded-8fed-40159ca67143 | -5.4217 | -43.45509 | 2026-09-29 03:30:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 63690f34-1e2a-3bec-855c-a24b4cecf7e2 | -4.36923 | -40.6205 | 2026-09-29 03:30:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f04cf067-1cb7-3662-ad68-f74352e640a1 | -7.40211 | -40.22849 | 2026-09-29 03:30:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 36fb2f5d-0463-387c-9747-7751883407e7 | -9.7664 | -36.9824 | 2026-09-29 03:30:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ef1b429e-0e92-347d-b1db-41b4c236d349 | -4.49911 | -42.55628 | 2026-09-29 03:30:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d8f3a9c5-b0ac-322b-8105-08a8429eb839 | -7.99237 | -43.26559 | 2026-09-29 03:30:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c6c7afdf-0c10-3f34-9c67-1809c21a8b14 | -7.40003 | -40.22724 | 2026-09-29 03:30:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 45.4 |
| 940f8db5-e4a3-3594-a655-094876100326 | -6.88864 | -43.63219 | 2026-09-29 03:30:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68272c80-93c2-33c9-a27e-534ad37ceb7c | -7.39736 | -40.22405 | 2026-09-29 03:30:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 18.8 |
| aa04427d-8ba1-3867-a524-03a39a43209e | -6.2889 | -43.64825 | 2026-09-29 03:30:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5491b2c6-11ef-34ea-a5f0-634232a41c5f | -4.49829 | -42.55415 | 2026-09-29 03:30:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 379b0f21-e907-3e78-978b-39e3c042d525 | -5.13835 | -35.70485 | 2026-09-29 03:30:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8abe4e15-cf6d-37f8-97f4-d703c02caffb | -9.76155 | -36.98558 | 2026-09-29 03:30:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 7.5 |
| bf1f067e-5e3e-3f11-98ea-215214421803 | -7.40337 | -40.22162 | 2026-09-29 03:30:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 59801003-720c-351c-8395-0196dc7e027c | -7.67127 | -44.89023 | 2026-09-29 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9ddfa095-2cfb-3987-b487-18c20bafe414 | -7.40875 | -40.22261 | 2026-09-29 03:30:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3f0114c-eab2-31ae-910f-6682e3ece531 | -4.07727 | -40.51471 | 2026-09-29 03:30:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ede5b5c-0327-37e7-8574-c3952b6ea88e | -7.40662 | -40.22135 | 2026-09-29 03:30:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| c673ea64-2fec-307a-be29-088fe4e8c1a7 | -7.99879 | -43.267 | 2026-09-29 03:30:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 586f7b2d-105d-3117-bfd8-a51e39fd749e | -5.42288 | -43.44872 | 2026-09-29 03:30:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 456321d1-45ec-368c-8b12-d3be641f6234 | -5.42905 | -43.44642 | 2026-09-29 03:30:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 89138e52-0b01-39f5-a3fb-4b370764b38b | -4.37504 | -40.62152 | 2026-09-29 03:30:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| afc7f87e-b2a5-3937-ac2b-0a2fe41c0890 | -6.28211 | -43.64708 | 2026-09-29 03:30:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d63e31a8-ca41-3fa5-a801-733e5628bb94 | -7.99919 | -43.26553 | 2026-09-29 03:30:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f36b7728-0535-3cef-a44b-2567922a708a | -7.06901 | -41.74374 | 2026-09-29 03:30:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 99db7446-9114-3a73-b786-3e33e9687f24 | -6.19238 | -35.25372 | 2026-09-29 03:30:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5b02d2e5-227f-3c85-ac05-6e230190e9f0 | -6.89537 | -43.63339 | 2026-09-29 03:30:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d2f7377-e7c0-3b8c-8f5e-9a8970ae2e00 | -9.7671 | -36.97836 | 2026-09-29 03:30:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ac19a9d4-616e-3f7c-87a4-8bbd6012a315 | -7.40812 | -40.22605 | 2026-09-29 03:30:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4314e870-0f2f-3e0b-9041-aacfd59432ab | -4.07656 | -40.51884 | 2026-09-29 03:30:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| db6f2810-384b-30bf-9e2b-36b44ce4243c | -4.85203 | -42.9377 | 2026-09-29 03:30:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50335e32-03a5-395f-8306-bc913b892df0 | -7.0682 | -41.74812 | 2026-09-29 03:30:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a041a2cd-332d-3040-8220-8466e032e09f | -5.03078 | -43.5695 | 2026-09-29 03:30:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c267f73b-3453-3a8e-8176-f815c43f033f | -4.31484 | -38.73525 | 2026-09-29 03:30:00 | NOAA-20 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f91f19b2-a9f3-3de7-bf45-a7f3280a8947 | -5.42112 | -43.45156 | 2026-09-29 03:30:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a746c94f-3af7-3a33-b190-9bf3968ac2a5 | -7.99977 | -43.26176 | 2026-09-29 03:30:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6470b945-b826-3d3e-bd77-0aa718e2046d | -5.42967 | -43.44995 | 2026-09-29 03:30:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e5e29e76-5279-30e3-8f2f-21f0bf395146 | -9.77054 | -36.98323 | 2026-09-29 03:30:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6941d78d-e70e-325a-a876-bbedcd670302 | -7.07496 | -41.74494 | 2026-09-29 03:30:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01ee5ac7-545a-370b-9f22-38c9b013b340 | -7.40063 | -40.22379 | 2026-09-29 03:30:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 35d07e5d-dcdb-353d-b40a-6859e9022af3 | -4.49812 | -42.56194 | 2026-09-29 03:30:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 575853b4-be38-3d83-b70f-c83fbc7381b9 | -4.49727 | -42.55976 | 2026-09-29 03:30:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 515cc9b8-83a0-34c7-853b-7bf2186233fc | -7.39673 | -40.22748 | 2026-09-29 03:30:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 16.4 |
| c6ff6d5a-a680-3f34-a56e-71eb2cc8b8ae | -5.02272 | -43.57473 | 2026-09-29 03:30:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a37ca507-7dde-3476-97c2-a3c18ec6b192 | -7.66988 | -44.89718 | 2026-09-29 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README10.md)
