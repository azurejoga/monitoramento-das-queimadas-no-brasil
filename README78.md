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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d076ba74-210e-36bc-b66f-91e70c9a1e7a | -15.28243 | -47.90556 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76b105a9-e7ed-3c72-86b1-8638d3991777 | -15.99453 | -50.90098 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e71f8d47-f7d2-3c7d-99dc-d8decad84d2b | -15.21931 | -48.73331 | 2025-10-03 04:14:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ece0864-75a0-3b99-8168-501221cad3c3 | -16.87487 | -52.80006 | 2025-10-03 04:14:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 006d1115-3466-3e5b-a72c-3f499b9bc032 | -21.58707 | -45.2805 | 2025-10-03 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f208ff04-1429-3c0e-a99b-1d618c4eb3c3 | -14.97498 | -46.85469 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd2a3eb0-482b-3a35-ad7c-efa2fdd197d2 | -15.32027 | -46.38605 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7405e6de-ab9c-3661-b9ae-1345ff5f32bd | -15.92232 | -43.33549 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54b4bb27-441a-328d-82c6-e412829dbfc7 | -15.28938 | -49.30269 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 144a021a-49d3-3ff1-a24c-c522d1271f56 | -17.96651 | -45.01147 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fe3610f-3b89-3ad6-87fa-3bce6a0f12f1 | -18.23269 | -53.34653 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1ce5cc7-5924-3f53-9871-0811c66b7968 | -16.93084 | -54.1498 | 2025-10-03 04:14:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8d1d02b-6b10-3884-99f8-101f199e4c36 | -19.69916 | -43.99433 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31251b25-a4eb-35f9-ac79-a6746ef9eb0e | -15.22974 | -48.06892 | 2025-10-03 04:14:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9c64682-cf26-3ac5-83ed-da48de613e65 | -14.74337 | -48.11697 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0bf88b02-ffef-3b08-90f7-6e84acd0363b | -15.94782 | -46.22178 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8aad7026-0ec3-36db-86aa-77baae8d11f2 | -16.76328 | -43.96263 | 2025-10-03 04:14:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 399eb3ee-c8fc-3b2b-91f0-5f945cd79e9e | -19.13995 | -41.50293 | 2025-10-03 04:14:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 19802dab-c8d6-3372-a082-6a2819c671dc | -15.7841 | -43.7 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ff97929-3fa8-3b14-b267-85fb60c76868 | -19.56265 | -43.17227 | 2025-10-03 04:14:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 288a19e9-c943-3a0f-b945-92c91e73a27f | -19.94124 | -45.72327 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c86ce5c8-b2a8-39b2-bc7a-36eca78ba091 | -14.93934 | -46.91379 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 780537c8-f142-3b54-a1a3-9a887e861b1a | -21.58981 | -45.28483 | 2025-10-03 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c74d73a3-2308-3dd2-bd9d-a402b2eaf6c0 | -19.5973 | -43.84031 | 2025-10-03 04:14:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0787aebc-3fdd-350a-9b9e-cce2024acdc7 | -15.8075 | -46.26027 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfa04c17-cfe4-398c-b520-f2f92c6fd270 | -14.71946 | -48.20424 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0b575fa-fe9a-32da-8270-8ae89fcf0729 | -15.70278 | -43.22516 | 2025-10-03 04:14:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8594d849-6d0b-32a4-9a31-85696cd118ec | -14.64741 | -48.25248 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 590097e2-c132-3cd3-b8ef-c095f8bfe00d | -15.52481 | -46.81129 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 93bb8ad0-ba0f-339a-a14c-932d82328212 | -14.95158 | -47.51763 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d9eeb7c-f122-3440-a434-31974a1def1f | -20.08845 | -45.80365 | 2025-10-03 04:14:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ca78e9f-15a1-3d13-a78c-639a9024ee39 | -19.14583 | -41.49758 | 2025-10-03 04:14:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 422c9f81-0d88-3843-98a3-d29c82eb846a | -21.27186 | -45.61887 | 2025-10-03 04:14:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ad7f29c4-8684-3403-96c1-908c92a98340 | -15.24146 | -49.30075 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fca1efb-77d5-3510-9e93-b95415b53259 | -19.97223 | -41.65606 | 2025-10-03 04:14:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c4504fed-ac86-3ad6-ae28-49f29dd97ef2 | -20.42131 | -48.85789 | 2025-10-03 04:14:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2284d9a0-6a99-3905-ae6a-dee115b09d14 | -15.27771 | -47.90992 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67d8966a-8606-3d5a-9a4c-e40507ecb376 | -14.97661 | -49.95803 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bc7acb2-d620-3f4a-9860-d23e8fce73c4 | -14.90543 | -48.34047 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 91870d6d-603c-3238-a4c7-2320f7f662d4 | -19.97587 | -43.71185 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f6682d26-7799-380b-a1fe-b18037682f0d | -17.86206 | -57.61226 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| faaab70f-3eab-3ffa-8777-846cabce6e46 | -14.98222 | -46.85617 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7bf1a30-2c38-38c8-9607-cddf113e45d7 | -14.91505 | -48.33214 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c3f0ad88-0065-3713-b18f-8523c9624dd6 | -14.74428 | -48.11195 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 023a395e-cfaf-3fd7-961b-049a47748755 | -17.216 | -46.98403 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cccc94a-4587-3f5a-a625-7ffe291a3233 | -14.93644 | -46.88665 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 586f6f03-3152-3126-a0a9-b1b62c283d50 | -15.30343 | -46.18584 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9dd9fd49-eec7-3411-8971-fe156800f41b | -19.454 | -44.28994 | 2025-10-03 04:14:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb15d465-b2d2-3ee4-97cd-f09d9b3f79f7 | -15.95405 | -43.30754 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09dd7b41-ab2a-308c-9966-f6a99e53f7ac | -14.90421 | -47.82667 | 2025-10-03 04:14:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 687e3002-3c6d-3cb8-b935-86f859287eeb | -14.73149 | -48.09774 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c336c8ae-ac39-39a8-bae5-3122697399ea | -14.94102 | -46.89853 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 09a0db7e-3c11-3cea-a642-1ce8288f39f3 | -16.29471 | -45.2397 | 2025-10-03 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c35bca04-188b-33b8-9095-1a7f74fa6491 | -20.11754 | -44.39502 | 2025-10-03 04:14:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 64b06732-f202-3837-a318-db48f4adeed6 | -17.98448 | -45.01797 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8162eb5-6cf7-393a-8aa3-57110d110ca0 | -14.93788 | -46.90027 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bab3ee38-d0a3-310b-a8ba-8361209cab43 | -19.36479 | -44.25544 | 2025-10-03 04:14:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ec7522e-d943-3f1f-8805-f7837b58f4df | -14.91482 | -48.34478 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bf75b33-5817-399e-89a1-159c537da745 | -15.28154 | -47.91063 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b70fc7f8-16ae-35c3-b6a1-dde44e06b81b | -15.32732 | -46.38757 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d056d0cd-9b19-31bf-85cd-3517070f5892 | -14.94013 | -46.887 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e42e7d21-b986-3425-93da-f3538a2ef2c8 | -15.75809 | -43.66981 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bce3e1d-a96f-355a-b9e1-e87e37046ad5 | -20.49311 | -43.92849 | 2025-10-03 04:14:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 69f3e4cf-93d4-3570-a8d8-13e40d7add90 | -18.16591 | -53.33317 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3890bad-38f2-3c6f-b306-c296d61b4a12 | -18.51259 | -44.04065 | 2025-10-03 04:14:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64b00549-e0a8-394b-abf2-f25326abc4d2 | -18.79523 | -43.74579 | 2025-10-03 04:14:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85ecc8aa-bd46-3bd5-b576-143ff276a6ac | -15.25857 | -49.32549 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d6a238d-5aab-37ee-be89-f6fa7f554dc6 | -20.76216 | -44.56491 | 2025-10-03 04:14:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eb878e7f-c3b8-3ecd-9396-13cc2e367a69 | -17.18305 | -47.014 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 848aeed4-528f-3853-9c64-4748a410ace1 | -20.14656 | -42.02034 | 2025-10-03 04:14:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8f6e833a-1a9d-3270-b2f9-2c4b833d9987 | -18.16856 | -53.34602 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b062c2df-6206-38f6-b255-f5f2bec2c6b7 | -14.62469 | -48.24279 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac1c077e-8e4d-3052-8a3e-9a641b7ba06a | -14.74128 | -48.10618 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45046f6e-fea1-3383-a959-47691743cf9a | -15.32306 | -46.89645 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3904f9c2-3a0f-31ff-9436-46efe10042f9 | -15.24296 | -49.29251 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 410c8b78-f406-3d57-97c6-8f46d319a7fb | -18.45426 | -43.80949 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6312d9a4-7055-3989-94ce-9dc1d6e06652 | -20.27152 | -44.79198 | 2025-10-03 04:14:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 088ab283-ed1a-3ad2-a502-80867eddff85 | -15.23099 | -47.97231 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8553013-42b8-33b3-b3bb-bdbb3027be10 | -17.85881 | -57.6264 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2aeff941-d5ce-39a6-a3ae-1e8767da813e | -15.71002 | -46.25931 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a2348aa-b1b3-3c22-938f-609ae3d44036 | -15.28066 | -47.91568 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6268f02-1c70-3f55-8856-729e004c6601 | -14.9785 | -49.97211 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e5783f2-3b43-3171-9749-fa0cfe078f2c | -18.16392 | -53.3351 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb846c22-85ca-3a02-9c21-aa827bb71b38 | -14.65197 | -48.29549 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4f5a2138-e0c0-350c-89ea-5ae57a213532 | -15.28456 | -49.30542 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 336a20a8-85c3-3c70-9a25-3089ddea7881 | -18.18141 | -53.28493 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9577f20c-ff35-3633-8c62-9364dad76d54 | -14.90301 | -48.34235 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7d7235fb-4894-3abf-af93-5b9474c38b50 | -19.58792 | -45.89596 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 018a0eba-8540-3f1a-a777-d65e2ac1bb97 | -19.71715 | -45.91565 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a94194f7-695e-322d-9503-760bd82e3f74 | -15.92566 | -43.33606 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 411dfa0c-0abe-3b2f-9f71-32361fe08581 | -14.90869 | -48.29876 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2f8f4240-59fa-30a8-b30d-673a26054e72 | -15.22169 | -47.18389 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7483a9c-f5eb-30ab-940c-9d52f2bcefa4 | -15.94712 | -46.22585 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4870603-1243-375c-bd8f-2982e76bfd91 | -19.46188 | -43.65023 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 251049db-c579-37cf-b4d9-ebe4c6a332a8 | -15.94366 | -46.22501 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| baee8e75-382c-3b90-aaa4-6374f14dbf5d | -15.33549 | -46.29619 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 854f7166-3778-3a90-b3ef-9299280099a0 | -16.3255 | -42.36757 | 2025-10-03 04:14:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4f17d4ff-b8a0-3dfb-8aef-d22eeafc7965 | -19.8346 | -42.28949 | 2025-10-03 04:14:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0ab1450e-e5f7-3594-bade-91bce1e3f944 | -17.35079 | -49.05427 | 2025-10-03 04:14:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e252764-3720-3b3f-8bc0-b1e903e7f5cb | -15.61181 | -47.86017 | 2025-10-03 04:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README79.md)
