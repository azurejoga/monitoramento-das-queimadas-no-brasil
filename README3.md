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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3137247-db90-376d-a415-7c226e28887f | -16.4906 | -55.1276 | 2025-09-13 00:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 9acf0dbe-1b4e-36b0-bca6-63061baf85db | -9.5139 | -54.6089 | 2025-09-13 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9641dc48-e44f-3aee-842d-9ba743c236aa | -16.3935 | -49.0542 | 2025-09-13 00:20:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ebcf7da5-137c-3d6c-b1c7-b2a8db20374d | -3.2507 | -46.7829 | 2025-09-13 00:20:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 95f4076f-4dd4-3ed0-9002-a387b9c94309 | -16.0252 | -47.952 | 2025-09-13 00:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 5049d6ca-5f14-3e49-976e-1454444abacd | -15.2229 | -56.6782 | 2025-09-13 00:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c783ba7f-1929-3f50-bac4-40fc925082d2 | -14.1898 | -46.2472 | 2025-09-13 00:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 032b4a18-d317-3d8e-beed-74a57f1c2a96 | -12.9292 | -54.7538 | 2025-09-13 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| cc8109dc-2a96-3bf2-be0e-62d003a51461 | -9.5135 | -54.6494 | 2025-09-13 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 2d7959f1-514d-3cc6-9302-149cb6cbf575 | -9.5004 | -55.9788 | 2025-09-13 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b9ee0a09-b3db-33d9-8fae-6d0747b71a02 | -16.393 | -49.0766 | 2025-09-13 00:20:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c9e9c308-c7d7-3f5e-9cf0-fd40dec321a6 | -22.2473 | -48.5869 | 2025-09-13 00:20:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 142.7 |
| 96df4ba6-f4ad-3bc0-822a-6eeb3ea023ff | -17.824 | -50.4014 | 2025-09-13 00:20:00 | GOES-19 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 90d717ef-aef7-327f-a196-3645473745ab | -9.4996 | -46.4075 | 2025-09-13 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 41c90db1-88e0-377d-bbde-c1052c618aeb | -9.7108 | -47.5418 | 2025-09-13 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4cc6a2e9-cd81-3035-828f-8993c546b151 | -22.248 | -48.5633 | 2025-09-13 00:20:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.9 |
| a0756308-3b9c-3620-b702-208c3281a672 | -16.534 | -51.7299 | 2025-09-13 00:20:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 781fbf26-deaf-3f74-b878-342ba56d7496 | -9.5324 | -54.6277 | 2025-09-13 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| e884104a-16aa-3bcd-85a8-d4f1d002720e | -9.2503 | -51.2472 | 2025-09-13 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 41f5d69f-cbbd-3949-81ac-f691908a2314 | -17.8439 | -50.3979 | 2025-09-13 00:20:00 | GOES-19 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 2d3ad579-ae44-3da4-82ec-154c0d9b7d49 | -14.2088 | -46.2669 | 2025-09-13 00:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 229.1 |
| b7c1cc9e-94db-3e16-b6ec-22562f9f42e6 | -12.006 | -47.7505 | 2025-09-13 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| e22e832a-8972-3313-914f-0a2cfec4164d | -10.0885 | -59.1575 | 2025-09-13 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 2488b231-91d6-3e28-b47f-0902bda34388 | -9.0344 | -67.4641 | 2025-09-13 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| aa228da5-c093-3e91-9947-07b798d40f45 | -17.8235 | -50.4236 | 2025-09-13 00:20:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 128.9 |
| b7767217-90dd-39cb-8f83-e5835fcec508 | -15.7161 | -50.5763 | 2025-09-13 00:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 46.1 |
| deafed33-9751-3f64-9ff8-a1d9232503a8 | -9.247 | -59.4201 | 2025-09-13 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e8555301-3858-3ed0-be49-147a1ccd6a5f | -16.5469 | -49.2282 | 2025-09-13 00:20:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| c53d11a5-e027-3764-8e87-ecd2044f6aa8 | -13.8983 | -48.2581 | 2025-09-13 00:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 45.7 |
| c188ffec-f5c2-38c4-b095-a68df9d08cff | -16.0454 | -47.9258 | 2025-09-13 00:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c7093169-451a-3a30-996c-5600df024eb7 | -9.5006 | -55.9588 | 2025-09-13 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 749c3fe2-a560-3d86-b01a-9e7195c75062 | -9.4807 | -46.4096 | 2025-09-13 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 6db5872e-1720-33f1-822c-68dbd4826185 | -11.9869 | -47.7531 | 2025-09-13 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| b4fcda6b-c964-348b-ba44-c4a99cbceba7 | -11.7196 | -46.6031 | 2025-09-13 00:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| e65e9c5e-2ba2-301b-95fb-eba0408a3807 | -12.006 | -47.7505 | 2025-09-13 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 8ae7a504-4e11-3701-b42c-e1980b06cf26 | -16.3935 | -49.0542 | 2025-09-13 00:30:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 31b106a5-5cd9-3de2-8de7-bcf0231f68d6 | -9.2844 | -59.3986 | 2025-09-13 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 9afad377-a743-3fa5-af2d-8414d3ebd753 | -22.2473 | -48.5869 | 2025-09-13 00:30:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 162.1 |
| ef5685f1-5ef1-332c-ab4d-ece44547cd74 | -10.0885 | -59.1575 | 2025-09-13 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| ac673d62-fe51-3263-9391-1e9d51c588b7 | -16.08 | -49.9709 | 2025-09-13 00:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 567f6945-fc23-369f-8241-8741a08547b9 | -21.6187 | -46.8115 | 2025-09-13 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| f1e2dd9c-ae2d-3b6c-b86b-a0f4abf52135 | -16.0449 | -47.9485 | 2025-09-13 00:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 50.7 |
| c7d61d89-4604-3f48-8b34-b272ea1c3f78 | -9.5191 | -55.9775 | 2025-09-13 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9381aa82-158c-322e-a400-e7e4b71d95a1 | -9.5137 | -54.6292 | 2025-09-13 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 184.3 |
| a800bf5a-9ff1-32c8-b68d-ccabb44cb4d5 | -14.1888 | -46.2932 | 2025-09-13 00:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| fcaf54e4-6ca4-3406-853d-e07f167c9df9 | -3.2305 | -47.135 | 2025-09-13 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| c8fa634b-5883-3c23-94ba-e2ce98be4356 | -14.4394 | -47.3206 | 2025-09-13 00:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| dd37359a-67f5-3607-94b7-6410c2905040 | -14.1893 | -46.2702 | 2025-09-13 00:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 235.7 |
| 41df8b80-9d46-33a6-85cd-57df1c7897fc | -17.3036 | -47.2324 | 2025-09-13 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f17f9b19-7c5d-3924-8f23-891401550b42 | -9.2656 | -59.4191 | 2025-09-13 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 5b14a84a-2e22-3832-9610-4dade30fb0aa | -16.0061 | -47.9329 | 2025-09-13 00:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 62f4e82b-9312-3f15-86e4-273636265484 | -11.1703 | -51.4421 | 2025-09-13 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 078b4cd8-ad59-3d08-a7fb-69844f80048f | -9.247 | -59.4201 | 2025-09-13 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 38795f14-eef0-3a72-827d-769197742d54 | -9.5135 | -54.6494 | 2025-09-13 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 3626b616-d799-3d24-bb77-36a8542475b2 | -9.4804 | -46.4321 | 2025-09-13 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 784952d2-b715-38ff-a281-fcce31e90d87 | -16.4906 | -55.1276 | 2025-09-13 00:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 123.3 |
| 489d3d00-bd90-3e84-9f16-67b8b9a59296 | -16.0262 | -47.9067 | 2025-09-13 00:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 29.9 |
| b3828ad7-bf3b-34cb-a0ff-c4495968c8ed | -10.7667 | -50.5086 | 2025-09-13 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 8ddc6ea7-ae8e-31c8-8324-a8874c5e643a | -15.6966 | -50.5793 | 2025-09-13 00:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b0932397-1ff5-3f6b-ab0b-1006ea96cd01 | -10.7661 | -50.5513 | 2025-09-13 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 02643ac0-4b8e-3dc7-9b1c-717ac603a73b | -10.7474 | -50.5319 | 2025-09-13 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| bc672cee-1194-3474-97c8-bdf692a2fcc9 | -3.2306 | -47.1131 | 2025-09-13 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 51faa2cb-bfcc-3bdf-9746-b4bec3cd250b | -9.5324 | -54.6277 | 2025-09-13 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| f0b2f401-c419-373f-bb49-b410fe6294fe | -22.248 | -48.5633 | 2025-09-13 00:30:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 134.8 |
| e56d66af-04b0-3d28-a8ae-194800928528 | -17.2836 | -47.2364 | 2025-09-13 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e4bb5401-a558-38e6-86b1-96607499b2d2 | -22.2264 | -48.592 | 2025-09-13 00:30:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.6 |
| c69c3dbe-43a1-3eb5-957f-1de93e678aea | -16.5469 | -49.2282 | 2025-09-13 00:30:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 147fe94c-6010-371a-a0a8-798a638ab567 | -16.0252 | -47.952 | 2025-09-13 00:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5ad710fe-b7c7-36d3-90a2-913d76ad6bf7 | -9.2503 | -51.2472 | 2025-09-13 00:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| f581aaf6-7358-36c7-a96d-a544e3747ef8 | -9.2472 | -59.4007 | 2025-09-13 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 138df65b-cf7a-31c0-be9c-6cc7218a6844 | -3.2283 | -47.6154 | 2025-09-13 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 7da08af8-e7d2-3f38-b656-8f255efae608 | -7.9488 | -46.8996 | 2025-09-13 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d2dea847-12a4-3fb7-b220-c067d40e01a4 | -17.303 | -47.2555 | 2025-09-13 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9ac10be9-368c-3d95-bb8e-dafb6d418bbe | -11.4285 | -43.5544 | 2025-09-13 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 67d11599-8e55-3b83-86a9-fca3a4b58cd0 | -16.4903 | -55.1484 | 2025-09-13 00:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| e84ec140-d0a5-3a18-bcb2-a18743f01936 | -10.8972 | -45.58 | 2025-09-13 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a7ba45ad-4f42-3b5c-ba4f-42416cbc0d03 | -16.5666 | -49.2247 | 2025-09-13 00:30:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 6e04c987-72b4-3a3c-80e7-fea53e75c1b6 | -14.1898 | -46.2472 | 2025-09-13 00:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8840c326-cba0-323a-b535-c379bbcbde29 | -3.2321 | -46.7836 | 2025-09-13 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1a18818a-88a5-3610-916f-d02e55e74686 | -9.5006 | -55.9588 | 2025-09-13 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 5f19cce1-e6a9-347b-9248-ca3c7ce03bd0 | -9.4807 | -46.4096 | 2025-09-13 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 08bc35f9-702f-3f72-a290-b347054b2ce3 | -9.5004 | -55.9788 | 2025-09-13 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 124.0 |
| b91e5ca2-d1f2-32e4-b385-3a3af955d201 | -9.2505 | -51.2261 | 2025-09-13 00:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 374d8945-2543-3c4f-8a99-fd052f926f79 | -3.2507 | -46.7829 | 2025-09-13 00:30:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| d068e138-d320-3c40-a400-1ae01bf7bd10 | -16.0257 | -47.9294 | 2025-09-13 00:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 8e75b5a9-21d5-36fe-a009-a3f79769e17e | -15.7161 | -50.5763 | 2025-09-13 00:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 0ef5a720-b837-3c8d-b935-8562110204cb | -18.482 | -41.4402 | 2025-09-13 00:30:00 | GOES-19 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 4588d4ec-ac2a-34c4-b7c7-10a43e7f0174 | -9.4996 | -46.4075 | 2025-09-13 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| ceab297d-7a0e-3592-8fe4-69304bd14d95 | -10.7477 | -50.5106 | 2025-09-13 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 805af63c-eb2e-359e-97c8-cb6c316f388e | -14.2088 | -46.2669 | 2025-09-13 00:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 370.9 |
| b00cd8a1-eb2b-3de2-8599-8855bc57243a | -10.7664 | -50.5299 | 2025-09-13 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 275.9 |
| 9ddb92fe-322d-385c-b79d-87c18a7a592a | -17.2831 | -47.2594 | 2025-09-13 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 6510bf38-37e3-3d56-9bcd-e5cc07df1d6c | -17.3643 | -42.6284 | 2025-09-13 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 35821499-d6b3-3fcb-b435-6e84a15949ec | -12.9292 | -54.7538 | 2025-09-13 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| dfe47999-6691-33c3-9931-9e27ccf2c8d1 | -16.0454 | -47.9258 | 2025-09-13 00:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8526c210-2aa0-38c7-87e1-61f31166d766 | -16.5099 | -55.1459 | 2025-09-13 00:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 2314a3e6-7912-3203-b0b3-4de27fb352ba | -14.2092 | -46.2439 | 2025-09-13 00:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 240.1 |
| 94bc2153-0cd6-388f-83ed-d0321aaf7e92 | -9.4817 | -55.9801 | 2025-09-13 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 24104ee3-681b-3711-af42-27ed0143c4af | -16.5102 | -55.125 | 2025-09-13 00:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 145.5 |
| 0963ad4c-1328-37cc-9840-d552f5f4bff5 | -9.4993 | -46.4299 | 2025-09-13 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |


[Clique aqui para ver as próximas entradas](README4.md)
