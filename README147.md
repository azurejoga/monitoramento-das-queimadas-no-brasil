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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c380c1d-6c08-36fa-8719-568373946677 | -2.99625 | -54.07493 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cfd20cb-37e1-33f1-b82f-65fb81c27914 | -3.52972 | -54.66262 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2654aa13-c5fe-32a9-9aa8-64017956d32e | -9.56822 | -46.83407 | 2026-10-09 05:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e770f6ca-f5e0-3ad3-b171-48be73f2feb2 | -11.05226 | -44.0499 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3c0673b-8b3d-3a6d-91f9-79ede6769ccc | -5.38266 | -45.94386 | 2026-10-09 05:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 874c25b9-bd79-385e-a626-12173d155b29 | -6.35745 | -55.15169 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bca0ce28-a142-35d5-8f2f-723cc7a0d802 | -11.11 | -45.68348 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7062f59-3660-3bdb-8b07-63c95c231443 | -8.97176 | -47.53117 | 2026-10-09 05:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2c30a70-e309-387b-a0ff-ee0ee179dccc | -6.22511 | -55.61869 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43df40c3-0b5f-3e5f-bc06-a326dc13c4d0 | -7.06866 | -47.39564 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cef4bc7-ef92-31c8-a833-92f25299f4c2 | -11.30253 | -46.67808 | 2026-10-09 05:04:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 606b4cd0-75bb-3a6a-b54e-dd5253a2ebac | -6.24371 | -52.85582 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c3852d8-687c-31a7-8fbb-cbde2ba0a26b | -3.03549 | -54.23496 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ab6cac3-1ade-3700-a565-65439d502287 | -6.47372 | -55.47092 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e0a4fe5-6b21-3b71-b7c4-706fe1170436 | -3.86585 | -56.00322 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b4bec5b-7cc3-3ba4-8f24-9f7ac24c2860 | -8.13776 | -49.43834 | 2026-10-09 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9b5402c-6e2b-3d96-976d-9b1bf875a678 | -6.04652 | -44.03535 | 2026-10-09 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 138edd7d-63f0-3f43-9df7-127293277d8c | -5.96616 | -55.37959 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a49aa7e4-eed6-3a75-8993-d34703e93281 | -11.65516 | -43.68089 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f1b6617-6b21-309e-bd04-442d1016178a | -5.99987 | -53.49746 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 350b02fe-da31-3520-b3ab-b5fea705e0f7 | -3.31874 | -54.04141 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93a14ccc-5a8d-3338-9bf6-29db6064c2af | -12.00729 | -43.44461 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bba8e277-a563-311e-8dab-5ff0debceaa8 | -4.5727 | -56.00023 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28d4789f-7ded-35d4-b622-f7870f65a485 | -3.05494 | -54.22609 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9a09ebd-ca14-3837-8a9b-40377dacf6ee | -4.69418 | -56.22633 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c81ffc54-2d75-376c-8adb-e70385d48f64 | -3.08307 | -53.93911 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba3e8b73-27c5-3853-b51f-9450d2446f6a | -6.45468 | -53.69414 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9030a950-a945-31f5-979c-d523e6b9b150 | -5.89301 | -57.72541 | 2026-10-09 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 118d29b5-68a0-3222-a97a-f86cae3b63de | -6.17327 | -52.85555 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd8c535b-00d4-3952-8400-65a3e6e01be6 | -2.88173 | -54.18358 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e47e7253-abf7-35b9-b01b-adb97bde2312 | -5.94644 | -55.34291 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 54f4b0ee-ebb1-375e-87be-17760166c477 | -9.78426 | -44.77907 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2e7a066-9917-36b6-bfba-ea095250a117 | -9.09908 | -59.38641 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f45e3be-8852-3764-9c70-15bbd452f1c8 | -4.27242 | -55.71241 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53fcc16b-43fa-327f-ae94-50b5a84e94ed | -2.98289 | -54.06886 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 599882f2-9d72-319a-98b8-d45489ca3451 | -3.25776 | -57.0429 | 2026-10-09 05:04:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4589f97-cca5-32d4-9b3b-47ddbe306d3d | -4.11552 | -55.03377 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9b73294-deec-3150-9064-2b15837b4da6 | -3.22937 | -53.96956 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e27a41c-7f74-365c-8954-1cdb953435f8 | -11.64061 | -43.70617 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7720e92-2081-3293-8b79-71411eb68727 | -8.16474 | -46.80663 | 2026-10-09 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0097f993-5f2f-3b5b-97c1-cbbe4f9beb81 | -2.99214 | -54.07822 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2377ff4e-21da-347b-93fb-9bbab4dd3fab | -5.70215 | -49.08512 | 2026-10-09 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f974ea20-d960-360f-9b17-bc971a86952b | -2.57638 | -56.18362 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 337a6449-5039-3b12-91a9-61c90844e45a | -4.31076 | -60.87278 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0538cbad-867e-386a-a419-d1904d59634d | -3.01355 | -54.14801 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd8df4ac-0f36-361c-9f6c-a8e76ad08b21 | -3.08057 | -54.24615 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c11f71e-756d-3ea4-8a51-31ebebed8bc4 | -3.62424 | -54.22996 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 978e8232-0456-3604-8082-30a5eedb6f99 | -3.00219 | -54.0601 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81420194-bba7-390c-9fdd-39285379a1a3 | -3.84957 | -58.89816 | 2026-10-09 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cb79f6d-5c43-37bb-a3c8-3f4c98bfc85b | -6.14053 | -52.86816 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 453efb6d-ccc0-3b3d-8ab5-46955c7ef8a8 | -3.11375 | -53.77016 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e31ecb8-ea91-3107-8983-c7abbefd1473 | -11.19388 | -45.31739 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 387e4157-e868-35f4-b3e7-b2c5e447e63e | -3.11692 | -54.17948 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 32673efb-8e5e-34a0-a751-f98bf518328a | -11.41063 | -47.58728 | 2026-10-09 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34c79934-54d0-35f5-ab09-e2cd24aa48bc | -3.11943 | -54.16405 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7638b785-3b27-3828-9f4d-f65c180de99e | -6.13089 | -53.50747 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3574214-b3df-300d-97c2-1a1bdc23ddca | -9.25938 | -60.88352 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d96f11e3-aea7-30cc-8778-9bba2050c76c | -3.27146 | -54.0691 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 976a47ae-36f5-333c-a661-0bc19f2a6532 | -6.39029 | -55.26348 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86fe1940-5489-3ad3-9135-8b6bfa9cda2b | -2.9952 | -54.05899 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bfc6421-c4cb-30ec-950b-686564178449 | -9.93783 | -43.55365 | 2026-10-09 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 034383d9-db10-3e5d-aa56-885e7193cbff | -4.12031 | -59.88154 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0977fc20-ed7e-3ec2-beb3-8fa1f1adf927 | -5.36169 | -42.88071 | 2026-10-09 05:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 30643724-6b77-3f5a-84d0-85c83508c574 | -8.65226 | -54.53166 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0058742a-d401-3ca1-bb4f-0798ed210e3e | -6.4958 | -55.31625 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| feaca7ee-d03d-3f74-a31e-24e6bd8c9b94 | -2.50209 | -58.07413 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62c45623-5d51-3dd5-97fa-cec905a2e4a0 | -2.98251 | -54.11622 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60791358-8306-32e5-a2e6-d1e66cb2218b | -3.99257 | -56.26232 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2a96542-3a56-3113-b2fd-c969c7d0b210 | -3.00096 | -54.06779 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02b1f76a-d2e8-3dd4-9e5f-ea8d20539ab9 | -11.76118 | -45.47707 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc50d388-7f21-3318-aa78-04cf50baf231 | -3.26572 | -54.06033 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f501aa55-1043-3fb0-9189-eef137fc2faf | -5.09703 | -46.21503 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f6d51bd-6bac-3664-b7b6-7ca01c8c3fce | -3.28355 | -54.08281 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0daf0073-4acb-379e-ba16-5151fb7381fc | -3.16288 | -61.08257 | 2026-10-09 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a04c54f-77ce-385f-9c2b-ac268fec75a5 | -10.5069 | -47.34023 | 2026-10-09 05:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0a3dcce-6ac9-334f-99c0-c92379c28de2 | -6.22948 | -60.03824 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c24f523d-6ff6-3b21-b0d8-5b21dae2e7f6 | -8.32631 | -45.44768 | 2026-10-09 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8921af9-61c1-32d6-8eb8-fcebee0678ba | -3.17692 | -54.60909 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90ffa58d-7e7d-3bf1-a0ed-f2fd434e161b | -3.00772 | -54.09557 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22fb8ef6-f977-3685-b8f2-2e73eeb5c6e9 | -3.01299 | -54.04128 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ceb7c262-d8fe-32c8-9ac9-babc7551c404 | -3.4659 | -60.25242 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8930f4cd-4157-3520-8141-973dfe64aea1 | -3.49302 | -54.73114 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2346275-f589-3612-98d8-31d8f03b5101 | -4.93248 | -45.72794 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b891f4cc-1807-3080-81db-535d1fee675d | -8.24343 | -54.72615 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b881f9d7-4a51-337e-baa5-9abaf8195b17 | -2.49691 | -58.07777 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4442fd34-3c0c-3464-9f28-c1f72e9a3fd8 | -3.40264 | -60.84561 | 2026-10-09 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7312520b-8db0-3969-830b-e78f8862dfe7 | -12.01933 | -43.49059 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| defd0ca6-3e12-3619-9173-85c1e6008293 | -5.99328 | -55.3716 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5974e120-dcea-31de-9786-7dace56ebe37 | -10.2887 | -46.61057 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c747c304-85c3-3f33-beff-e1e53ba286cd | -5.95294 | -55.34811 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83991308-8aae-38ad-adad-fda6a7cd4296 | -9.86803 | -44.86796 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2592dca-e0ed-39bc-a517-79c88b176979 | -6.23149 | -52.88955 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e02d93b3-8e48-321d-9ae8-d9042a9d918b | -2.50281 | -58.06977 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afdbab1a-8a89-3513-ba0f-7e69932b9a3f | -4.57992 | -55.72476 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 69c33502-6b99-3cd0-8ae2-4f29fb24e34c | -7.51295 | -47.33183 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ec2a30a-184e-3888-a4a0-01463813188d | -6.93388 | -46.5939 | 2026-10-09 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 422bf41e-54b2-3aff-a37e-450d82ade92b | -3.7242 | -59.69143 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b35e4e7-5cf0-3f4a-b64a-735e14f281f9 | -3.01648 | -54.04184 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 537e62f2-18ac-3663-8175-8513e6525a35 | -3.10512 | -53.93483 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d32108f4-2de2-3efc-aa44-012e744f40d1 | -3.98037 | -56.21608 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README148.md)
