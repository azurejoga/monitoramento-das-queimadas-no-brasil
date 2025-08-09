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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25cac84c-a708-3f0b-8d9a-c778b0eed32a | -11.9283 | -44.5335 | 2025-08-09 00:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 41dd10db-c8e8-38a2-b1fd-6aef787c864a | -6.5668 | -44.5655 | 2025-08-09 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| e1956d13-0aad-3736-9564-d1c0ab167c66 | -17.5291 | -50.2988 | 2025-08-09 00:30:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 259f65dd-e846-34a3-8d72-83070ec33b7a | -13.0778 | -43.83 | 2025-08-09 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| a36d7df9-dc9e-3b0e-82b1-298f82e14323 | -8.9215 | -60.7297 | 2025-08-09 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 99f65de7-7495-3f25-b963-144395e4d7f0 | -18.4334 | -50.7122 | 2025-08-09 00:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| cd925652-5e69-3429-b8d5-4fb587cb656c | -8.9213 | -60.7489 | 2025-08-09 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 162.6 |
| 19c62529-f10a-3be3-a445-c8fdf8cf03d8 | -11.1077 | -50.4934 | 2025-08-09 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 38c2c4ae-6996-322b-b03f-edb010730bd0 | -5.2262 | -46.0642 | 2025-08-09 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 3dee8cd9-4031-38bd-9ebc-e75343d6d906 | -13.058 | -43.8571 | 2025-08-09 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 68498aba-217e-34c1-a178-29d93f3598b6 | -8.9399 | -60.7481 | 2025-08-09 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 64cbd541-8a42-3db0-943b-5add3a2674f9 | -17.5296 | -50.2766 | 2025-08-09 00:30:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 878e64ab-1144-354f-a441-c43a1cf7bce5 | -17.5098 | -50.2801 | 2025-08-09 00:30:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| cc70bff9-c897-3f98-be98-275660f735f5 | -19.813 | -47.0398 | 2025-08-09 00:30:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 6094ed71-c37f-35aa-9494-90428c391647 | -11.9279 | -44.5569 | 2025-08-09 00:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 62e97f80-9963-3694-8bfb-6a5fdb22ea49 | -13.0584 | -43.8333 | 2025-08-09 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 6a703116-7709-3c1b-ba18-e3cdef729a41 | -5.2075 | -46.0653 | 2025-08-09 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 151.4 |
| 0f8990e2-c4f9-315d-8813-70f49679ee2c | -12.0481 | -47.5224 | 2025-08-09 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 304cd74b-78d9-317c-bf6f-2e0ec780d9cc | -6.5856 | -44.564 | 2025-08-09 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| ad758385-3df3-3bca-ae5f-e00aa36f9d55 | -19.8124 | -47.0634 | 2025-08-09 00:30:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 47b9fc14-8b4f-3e11-a4bc-5b589c8e4612 | -5.2073 | -46.0876 | 2025-08-09 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 06faeaf9-3d65-303a-95ef-64fe9589a1a1 | -19.8328 | -47.0586 | 2025-08-09 00:30:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 39a75293-da6e-36ae-91f3-fccb4d2c8540 | -13.0386 | -43.8604 | 2025-08-09 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e447e909-714e-34fc-aadd-1986d4cbc447 | -5.2075 | -46.0653 | 2025-08-09 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 85b477f4-c914-36b6-bb36-306686168924 | -17.5098 | -50.2801 | 2025-08-09 00:40:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| e223b1a0-0218-3f46-8fa4-ba3d8ae072e2 | -17.5296 | -50.2766 | 2025-08-09 00:40:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| e9b97eae-fe35-3ac0-81ff-b206a9933a8f | -6.1326 | -42.9554 | 2025-08-09 00:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 52.9 |
| 2a500b39-14d3-3c44-a50a-34429606866a | -11.9279 | -44.5569 | 2025-08-09 00:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f46a7c6d-9b1d-3d34-8a63-1e4c1a07561c | -8.9215 | -60.7297 | 2025-08-09 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 28a2cfe7-abd9-366f-8b1a-14cd7a460463 | -3.4254 | -49.0517 | 2025-08-09 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 320707ed-db96-3981-b12f-4aa9609e149b | -8.9399 | -60.7481 | 2025-08-09 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 81597b6e-59b1-380e-98d9-bd2c1e5f4d60 | -5.2073 | -46.0876 | 2025-08-09 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| aefcb30f-e7b3-3576-bbb5-5f0b06ac9e14 | -17.5291 | -50.2988 | 2025-08-09 00:40:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2a70cd9b-d415-3048-a0a3-7d0a831d62aa | -5.2262 | -46.0642 | 2025-08-09 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 74ee0cff-c139-35d6-80eb-a029c4600f71 | -3.4439 | -49.051 | 2025-08-09 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8477f00f-d5e8-36a5-8d4c-b3f9efb74ed3 | -6.5856 | -44.564 | 2025-08-09 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 85f69fa2-a90e-3327-9163-395f4ca5e3d6 | -5.226 | -46.0865 | 2025-08-09 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 5cc88918-3ffa-35dd-a8c5-dfa7ac592edb | -19.8328 | -47.0586 | 2025-08-09 00:40:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| df56694a-ef3d-3503-8457-bc66849a914c | -19.8124 | -47.0634 | 2025-08-09 00:40:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 98892428-6b2a-3f40-a11f-ff8f5217bff0 | -13.0584 | -43.8333 | 2025-08-09 00:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 151fa552-fa19-32d0-8319-ca38a99b66b8 | -8.9401 | -60.7288 | 2025-08-09 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 60e4fbfa-5d40-3a16-8d77-75a39876a8cd | -9.5589 | -62.7238 | 2025-08-09 00:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b0d8c256-2b1c-35b9-a5e2-b11b9504a9f2 | -8.9213 | -60.7489 | 2025-08-09 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 139.5 |
| f01a3698-3102-30d8-8c59-4498a42406a7 | -3.4255 | -49.0303 | 2025-08-09 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2bdb5d49-204b-3b90-acd2-ab5ca2ca228a | -17.5093 | -50.3023 | 2025-08-09 00:40:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c7fa93b5-0fa4-3943-a809-dcb181422188 | -11.9283 | -44.5335 | 2025-08-09 00:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6a40c104-0352-3b77-9c91-cc415bfffdf9 | -11.1077 | -50.4934 | 2025-08-09 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 2d866f75-017d-33ef-9e02-5e1b4d4de792 | -13.058 | -43.8571 | 2025-08-09 00:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 7e2e020b-3434-3f0c-8bb9-3e0af1468404 | -21.50531 | -49.14028 | 2025-08-09 00:43:00 | TERRA_M-M | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 22abf19d-5271-358f-abca-2d1cc81daecd | -22.14371 | -49.44636 | 2025-08-09 00:43:00 | TERRA_M-M | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 40497828-9a10-3698-a70f-7612e66f792d | -22.14501 | -49.45611 | 2025-08-09 00:43:00 | TERRA_M-M | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 26fab27c-c648-3cd0-8b58-54d524e4d5f1 | -3.9638 | -47.888 | 2025-08-09 00:44:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fecfba42-3c92-304e-b97e-a7ce9144bee4 | -4.8728 | -47.758598 | 2025-08-09 00:44:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae553f5f-3f1f-3256-859b-51eec5f9a660 | -7.0496 | -59.165798 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 590a9ede-1b70-3b97-9622-ff2e76ecea14 | -17.7885 | -50.116798 | 2025-08-09 00:44:00 | METOP-C | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| af325cb4-9ad5-3f6a-a5b9-d515da4baf49 | -7.0834 | -59.182899 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f55b827-6267-3c73-8d96-8cde6083f610 | -11.1012 | -50.4939 | 2025-08-09 00:44:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea2c27d1-714c-3dfd-a9fc-3c83e8b33d82 | -5.2131 | -46.078999 | 2025-08-09 00:44:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4eb32328-ae2b-3951-86ed-84a5ef5b0538 | -6.129 | -42.9622 | 2025-08-09 00:44:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1a7c0566-2746-30aa-99b3-f611709c097a | -12.0413 | -47.514801 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8323ac1e-1a1b-34b3-971d-e6a4335b7abf | -19.594801 | -42.688999 | 2025-08-09 00:44:00 | METOP-C | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 90740ad2-8265-32ac-a123-1b6bf07de30e | -5.211 | -46.0704 | 2025-08-09 00:44:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7df55030-16f6-3bd9-9874-ec31a6183b6f | -5.2228 | -46.076698 | 2025-08-09 00:44:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d931d7bb-e81e-3729-afd6-22d88669c926 | -4.4693 | -48.110298 | 2025-08-09 00:44:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f987369-6942-3440-bdf3-31d895bf8831 | -6.1387 | -42.959801 | 2025-08-09 00:44:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bf4c99ba-6cf5-3a75-ac19-5c3cd3e5d17e | -7.0592 | -59.212002 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f91d2aea-9667-393d-b6f1-7904f731ab62 | -16.055201 | -49.037701 | 2025-08-09 00:44:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 85992335-76ca-3056-83ed-2cdb4b655028 | -13.5536 | -55.258801 | 2025-08-09 00:44:00 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50a60001-33aa-3336-92f0-5fcdfd54e5bf | -16.257 | -48.450001 | 2025-08-09 00:44:00 | METOP-C | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 54ad4a03-a66e-3a81-a0b0-6ee84ee7d23c | -9.6576 | -43.848598 | 2025-08-09 00:44:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fde678ad-5a72-3b89-868e-c2af4774c66f | -11.1029 | -50.501598 | 2025-08-09 00:44:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7d6c7e4-79fa-3863-bb3c-0d6e4d0bd6e0 | -7.0737 | -59.184898 | 2025-08-09 00:44:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23d2a7ad-62c5-3731-9353-719cc310a0d1 | -17.526501 | -50.284801 | 2025-08-09 00:44:00 | METOP-C | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b34db5fc-f53d-3c2e-98e9-291dc7ac066d | -11.7461 | -47.487701 | 2025-08-09 00:44:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9d47f6e-89cd-3ce7-b639-26389eb868e5 | -6.1673 | -46.142601 | 2025-08-09 00:44:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1766bc93-77fa-38df-80a1-154b85753f97 | -11.0847 | -50.465599 | 2025-08-09 00:44:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 437c625c-9a31-35b2-9a6e-3ad7a67560bf | -9.0538 | -45.075401 | 2025-08-09 00:44:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b887a551-5839-30da-977f-2752f9d8190a | -3.9851 | -47.8909 | 2025-08-09 00:44:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2adf16da-cf6a-3d1e-a1c9-c917fa35fac5 | -12.7227 | -47.790298 | 2025-08-09 00:44:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9eb4caf6-b357-34d1-877b-4b4fefedd806 | -8.9107 | -60.691299 | 2025-08-09 00:44:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b029ca3-5894-3d22-a138-f56e22148e77 | -3.8377 | -47.7449 | 2025-08-09 00:44:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7e8cf78-4bb2-32b1-983b-a3cb6c924b27 | -14.1656 | -43.6698 | 2025-08-09 00:44:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0e0a82c-89a7-3ddb-a8fb-42b619dd355e | -8.0764 | -46.842499 | 2025-08-09 00:44:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83814ef7-3bb7-3e15-a803-afb9b8e04edc | -9.068 | -40.474701 | 2025-08-09 00:44:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 0c89652e-1140-3d13-af08-5d239382dd96 | -11.9326 | -44.535599 | 2025-08-09 00:44:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a192022f-4e44-3ff1-ad4c-d3534d61f904 | -5.209 | -46.061798 | 2025-08-09 00:44:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78d37d4b-61db-37de-996e-c3c37bf1e681 | -6.0521 | -43.7528 | 2025-08-09 00:44:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e719490-ea6c-34fd-860a-f4a4497f1440 | -19.812901 | -47.065498 | 2025-08-09 00:44:00 | METOP-C | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 62c0d927-f97d-3d8b-88bf-89a3532780ae | -13.066 | -43.830002 | 2025-08-09 00:44:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2dff1fa-ad5d-3661-8efb-b7912e54b956 | -5.0844 | -48.315601 | 2025-08-09 00:44:00 | METOP-C | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0c8902c-2e26-344b-9318-bd04694274e4 | -7.1064 | -46.097698 | 2025-08-09 00:44:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 670a8788-1ec3-33a8-8029-8febd5e6b479 | -10.5775 | -44.792 | 2025-08-09 00:44:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 64210182-eaee-3953-b329-432bec6ff109 | -3.6523 | -48.3256 | 2025-08-09 00:44:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c15e474-d57b-3998-b2c3-e29d8dd237cf | -13.0682 | -43.8391 | 2025-08-09 00:44:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b6a0bd6-1d9b-339f-be71-d68c0f1365bc | -6.0591 | -43.738998 | 2025-08-09 00:44:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0035e142-01dc-357e-8492-ec558c7f54f7 | -11.7759 | -47.392101 | 2025-08-09 00:44:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3662a313-570d-3a27-8f82-9052d592ebf9 | -13.6365 | -49.022999 | 2025-08-09 00:44:00 | METOP-C | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a7de6292-dc71-3bd1-ae68-376838cc1fd8 | -4.2924 | -48.0592 | 2025-08-09 00:44:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aafe75f-00ba-341d-9b1e-f1f94f603136 | -22.1474 | -49.443501 | 2025-08-09 00:44:00 | METOP-C | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 323db4fb-4c67-3503-9a9e-2bf0a6e2a94a | -17.518499 | -50.295898 | 2025-08-09 00:44:00 | METOP-C | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
