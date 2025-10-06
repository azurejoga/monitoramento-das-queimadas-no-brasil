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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35fd27ac-f304-3531-a874-4f651f562508 | -8.1055 | -44.7891 | 2025-10-06 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 947e9ca6-8ed7-35e7-87d7-e0750b8b2dda | -7.2094 | -45.8942 | 2025-10-06 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 3bdeda83-2bce-37bf-87d2-ba528b3597b5 | -7.4669 | -43.0674 | 2025-10-06 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 131.8 |
| b3a5a44e-ef77-36b2-843a-8e801a878ba1 | -15.2351 | -49.2914 | 2025-10-06 13:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 8511bdc8-3e65-3ecc-b451-6fb83000d445 | -17.842 | -57.6048 | 2025-10-06 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 5fa13af4-62f5-3b3f-939b-4535b741dc70 | -21.4063 | -45.0368 | 2025-10-06 13:20:00 | GOES-19 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.5 |
| 0795b1b4-95b0-3d4f-86a3-c61a7977b186 | -9.3165 | -45.9779 | 2025-10-06 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.4 |
| b714fa50-f99c-3548-b92e-de78855465b4 | -8.5004 | -46.3566 | 2025-10-06 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 7ec091be-eb8b-369a-bf21-bc2a73147f60 | -8.0866 | -44.791 | 2025-10-06 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 365.1 |
| 80dd4b24-7920-3509-9600-7ca747a5a32c | -9.6804 | -48.4014 | 2025-10-06 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 0bd4c389-0eff-3727-b32d-8306d2c894fd | -18.018 | -44.9965 | 2025-10-06 13:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 00ebaa7e-0332-3068-8094-d1b44969742d | -14.863 | -51.5019 | 2025-10-06 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 152.0 |
| f9d6858b-dc69-3ae0-83d7-682b97b702d9 | -9.9779 | -48.7405 | 2025-10-06 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b562095f-d72b-3425-a56b-44e5a2515475 | -14.5433 | -46.9861 | 2025-10-06 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 498.9 |
| e7b1a2e7-5404-3c5c-bb3b-3d083507e68b | -7.4089 | -46.5255 | 2025-10-06 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 4a321806-b433-3464-aae7-baac0d7c3de1 | -17.7045 | -46.2927 | 2025-10-06 13:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 124.3 |
| e67365b5-7ec4-31b0-9a9e-0fe886535be4 | -16.0038 | -50.8365 | 2025-10-06 13:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 619e2de0-bb2d-335f-8dbd-91726018ef8a | -14.6893 | -48.4021 | 2025-10-06 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 1b355254-2431-319f-8bdf-22038d25f3b9 | -14.882 | -51.5207 | 2025-10-06 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 464.6 |
| 7f6b7c03-0121-3b8b-b8b5-c2862f2a7220 | -8.8794 | -47.6722 | 2025-10-06 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 2372f55e-11a8-30c1-91f4-afddba2a8f24 | -17.9807 | -57.5674 | 2025-10-06 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 59ea1a2a-4b2e-3854-923f-468e838b135d | -9.9207 | -50.2323 | 2025-10-06 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| d4dff762-07f8-3334-9cd7-c6192243ceb0 | -10.3643 | -48.1519 | 2025-10-06 13:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f047aec8-bbd1-3923-8e3c-65613e68b086 | -7.4276 | -46.5239 | 2025-10-06 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| a7e3a537-e768-3349-86b9-ef7b35a38ad1 | -13.2515 | -47.7979 | 2025-10-06 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b70d0706-2d9c-3880-913f-55d02ca25d4a | -7.7206 | -42.3784 | 2025-10-06 13:20:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 9ca63c31-f5a1-37c5-9283-945d85858379 | -18.393 | -45.1962 | 2025-10-06 13:20:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e06d7405-af96-3b2f-9269-04df2f7be346 | -18.0008 | -57.5444 | 2025-10-06 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| d0beab2f-6a72-3a8f-9cb8-6677611f6738 | -9.9018 | -50.2341 | 2025-10-06 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 656aa5d2-0f21-30ed-bbf5-fcdd55729504 | -13.3044 | -48.0575 | 2025-10-06 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 0f84ac28-0174-382e-a00e-34371af5c31e | -11.9331 | -46.4153 | 2025-10-06 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| b932452a-69cc-3aa9-8c7a-ba8014fe6ac1 | -13.3237 | -48.0547 | 2025-10-06 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 130.8 |
| add7138a-dae4-3b36-a8c9-1182b0b15a4a | -14.9161 | -46.8312 | 2025-10-06 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8ae17137-f0d3-3bba-9443-7e66dc2e2ad3 | -14.5623 | -47.0056 | 2025-10-06 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| ad94001c-7b8a-3b43-9d81-9679f2ed338e | -14.6897 | -48.3797 | 2025-10-06 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 6adb12dc-d418-3c5c-888f-dae6b9802819 | -8.6139 | -46.3227 | 2025-10-06 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 6c7e6198-d34f-34a8-8592-5969c6e96054 | -8.8803 | -47.6061 | 2025-10-06 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f6024076-9796-3fe2-8160-3f8a2a27f4e0 | -7.7203 | -42.4023 | 2025-10-06 13:20:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 109.9 |
| 4482b7a4-d112-3c16-be36-75389e0a945b | -8.519 | -46.3771 | 2025-10-06 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 108e3be7-fc8e-32b2-b96d-98ae37679665 | -14.5504 | -46.6433 | 2025-10-06 13:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 9986157d-716b-300a-aa41-deab0706b9e0 | -12.5929 | -48.1144 | 2025-10-06 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| df802cc4-da39-35a1-b836-fa49f58a4db0 | -9.9024 | -50.1914 | 2025-10-06 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 38bd7dcd-ee8d-3a7d-8c98-f48882b2ca31 | -11.655 | -47.039 | 2025-10-06 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 93df95d5-be5b-3c20-896a-bfe383f4c21f | -8.1876 | -44.2514 | 2025-10-06 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 41a9fcb4-93e7-32fd-a2f2-cc6ac5e5d07f | -10.386 | -45.4184 | 2025-10-06 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| cb4136cc-217a-309b-9f2f-e781f2ac5b70 | -15.5896 | -47.2819 | 2025-10-06 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| c0d56d27-d6a8-3c3b-92f9-cee4cdafa7e7 | -8.88 | -47.6282 | 2025-10-06 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| eb3d3651-1270-31b5-bd1b-1bd8254999b4 | -7.4672 | -43.0438 | 2025-10-06 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 90dc7eac-0f4d-3491-b28e-b2985cfe716e | -12.1267 | -50.9545 | 2025-10-06 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| baee1d89-60fc-3241-8919-b32d6ee33174 | -9.9215 | -50.1682 | 2025-10-06 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 3099670b-31d4-31f5-ae2a-2e46e509b59e | -10.6184 | -46.3646 | 2025-10-06 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 44b8ed72-8982-34ec-a48b-1c0d5af3050e | -18.2869 | -45.4109 | 2025-10-06 13:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b90b0b9a-b705-34e8-b868-93779ba2bcd0 | -11.9327 | -46.438 | 2025-10-06 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ca86a91c-b6a9-3ed2-8648-cfc02313e37b | -13.7738 | -45.7429 | 2025-10-06 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 65ec1335-34c7-3287-9f7f-f42241607f2f | -15.5637 | -52.4516 | 2025-10-06 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| c9c44597-e67d-314d-af24-4ad781d739e1 | -7.7935 | -42.5845 | 2025-10-06 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 4fe28f86-b459-38a3-9d33-da9fa73899e9 | -12.9812 | -46.8051 | 2025-10-06 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 320a9cdd-f227-303e-b01d-661584dd4bc3 | -8.6144 | -46.2778 | 2025-10-06 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 287c6bc5-f7a5-350c-8bfe-0560257f83c5 | -8.1879 | -44.2283 | 2025-10-06 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 51a953f2-a0ca-3cec-873b-b08f18773934 | -18.0011 | -57.5238 | 2025-10-06 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 77d784ae-329c-378c-8898-ffd00138e0ab | -13.343 | -48.0519 | 2025-10-06 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| edc88f01-0c50-341c-aa1e-5abf6dbdfb58 | -9.3162 | -46.0005 | 2025-10-06 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 190.8 |
| fe8fb522-9852-30af-96dc-e6a7a6eccd66 | -10.9681 | -47.1058 | 2025-10-06 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| eacde88f-3b07-38dc-9089-a2421f025dd9 | -15.3546 | -47.3007 | 2025-10-06 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 2a86e14f-a45e-30f5-846a-1e2cd2187ebb | -16.0083 | -56.0155 | 2025-10-06 13:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 171.0 |
| 66a80832-114a-3b2b-90a1-27e4f336862d | -7.2091 | -45.9167 | 2025-10-06 13:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 9581ab1a-1f59-38f6-b018-faa2893b8455 | -8.5387 | -46.3079 | 2025-10-06 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 658381d1-4e93-3984-aa25-17e1f0938b90 | -11.8033 | -45.0856 | 2025-10-06 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 305.2 |
| e45b0c92-83ae-3fee-982a-89822957f746 | -17.9998 | -57.6062 | 2025-10-06 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 7bb72e9f-90f8-36e5-89b5-3a0c78b6cd53 | -8.5584 | -46.2387 | 2025-10-06 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 4f66356e-a747-31a0-b114-f4186705d629 | -14.8626 | -51.5234 | 2025-10-06 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 451.2 |
| 23d19109-60fa-3a79-9a39-52b782613ff8 | -8.1684 | -44.2766 | 2025-10-06 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a3e56984-01fa-392a-b8f2-df9ff758fb4b | -21.1171 | -49.9537 | 2025-10-06 13:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.1 |
| 1ad32904-3b73-3d7f-9770-d184cf858efb | -11.8038 | -45.0624 | 2025-10-06 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 2e7b7a94-2040-3815-8efc-060764b8413b | -11.1907 | -49.9915 | 2025-10-06 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0ec74f57-40ab-3f19-a7ff-fb80d6e0de14 | -8.1687 | -44.2534 | 2025-10-06 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.3 |
| b4942cee-a3fc-37d9-a532-4c5db103ab78 | -8.8991 | -47.6042 | 2025-10-06 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 961b3ae0-414c-3e52-b0c6-1cc842081b2c | -12.9844 | -51.0433 | 2025-10-06 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| f7134942-eb97-3609-aafd-a82a772ade9f | -14.8824 | -51.4992 | 2025-10-06 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 60382375-52cd-3845-bfff-df7e76842c03 | -12.9841 | -51.0648 | 2025-10-06 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ddd318c5-437d-32f6-a049-70d66eb11645 | -7.6801 | -42.5966 | 2025-10-06 13:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| c0b160b3-b021-3fa6-b399-157f5efb695b | -8.0678 | -44.7929 | 2025-10-06 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| fb1966f3-6627-3eb2-aa46-44622e0c035f | -9.9776 | -48.7622 | 2025-10-06 13:20:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| ad051e5f-a7bd-3dae-9b05-e19eb79fffb0 | -8.5004 | -46.3566 | 2025-10-06 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| d2bccd7a-6b92-349e-a797-265de1734a5f | -15.6206 | -52.5288 | 2025-10-06 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 45b06836-dac3-3ddf-9695-ba8578c76db6 | -17.842 | -57.6048 | 2025-10-06 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.8 |
| b4d0fcd8-7e0f-3dee-b173-7e2c62e340fa | -8.8803 | -47.6061 | 2025-10-06 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 6c9fe6c4-4a1d-3ba2-9b2d-9df8461047ae | -17.3816 | -53.5947 | 2025-10-06 13:30:00 | GOES-19 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| e7dff1db-09bc-31a0-9068-20715cc73c01 | -11.6554 | -47.0166 | 2025-10-06 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 2c92d4da-61d8-3a58-8b40-d899089399e9 | -12.9816 | -46.7824 | 2025-10-06 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 54390b6d-ef12-3c33-b1b2-7202d6cc8473 | -18.0008 | -57.5444 | 2025-10-06 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 1b9f6880-40bc-3c3b-af96-285a913c406e | -13.3237 | -48.0547 | 2025-10-06 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d79eebdf-5cf2-3d56-91bf-408f8c6633eb | -18.0011 | -57.5238 | 2025-10-06 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.9 |
| de489b62-3939-354d-b2c0-2d65fca4e091 | -10.9684 | -47.0834 | 2025-10-06 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 258.4 |
| 842dd0fb-118a-3f8f-a53a-f887b5e79cff | -8.6141 | -46.3003 | 2025-10-06 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| ac4f4369-96f9-363a-a3dd-76418edbcaf1 | -14.5438 | -46.9633 | 2025-10-06 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 146.1 |
| e4a74b78-0883-39f1-be19-6d39430f0e10 | -10.0028 | -48.3015 | 2025-10-06 13:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| bee9a248-8195-32c7-a922-3bbf91b20f9d | -16.0083 | -56.0155 | 2025-10-06 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 156.8 |
| a30b112c-515f-3530-a0c8-ea0c2095be85 | -17.9813 | -57.5262 | 2025-10-06 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| fb18d477-5d15-3f98-bd09-a2366d487771 | -7.4669 | -43.0674 | 2025-10-06 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 136.7 |


[Clique aqui para ver as próximas entradas](README89.md)
