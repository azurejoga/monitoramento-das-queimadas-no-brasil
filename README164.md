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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3782fdfc-06a4-375c-9c71-117db17e84db | -16.59563 | -57.19165 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 5413de71-6d99-37d6-9e92-76d5d79c5d94 | -16.59522 | -57.17297 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cf2e7cb7-0412-399e-8bed-2ce66bbbb564 | -16.59348 | -57.18383 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8ffa9a39-ac7c-3fb6-9c9c-2c08bf0bf20c | -16.59294 | -57.25077 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e638e17c-26d9-3e2e-b7d5-5d656d4df302 | -16.59289 | -57.18745 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 9b92b308-cfa2-3a21-8fc7-37992a9effb1 | -16.59235 | -57.25441 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d92d1c17-ce49-31dc-9212-d68a7388e93d | -16.58903 | -57.25383 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 52e3018e-9f5b-3184-9bb9-adcef4994119 | -16.5857 | -57.25325 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2987345c-aad2-3cdf-80b7-e45a20af39c7 | -16.58511 | -57.25688 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7c87c7a3-2a8b-3ade-9c48-74c833027e36 | -16.58179 | -57.25631 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 85092b0b-cb16-3673-985b-51538042ce02 | -16.57904 | -57.2521 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 20319b70-4c30-3243-8b03-1f690645b967 | -16.57591 | -57.2292 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f458c359-2990-355f-abe8-a5c4f6c9fffc | -16.57532 | -57.23282 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 98e2bfba-f0ef-3137-b616-37eefd449ad5 | -16.42866 | -57.3877 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 45b1732c-356f-392a-a37c-2ac351ac4411 | -16.42533 | -57.38712 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 98c8f0c4-cbe9-3ce8-b113-7c832d032a3a | -16.42239 | -57.40536 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b911ef63-6a40-3ba0-8a7f-c59ad326de94 | -16.41905 | -57.40478 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 687260d2-610f-390c-9052-400f17bd3b76 | -16.41807 | -57.38961 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e7c0c329-92de-3a7c-ac17-0d92a7a260dc | -16.41748 | -57.39325 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 7ec8a676-9b71-37df-834f-3d32ba67295f | -16.41414 | -57.39267 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 3d2b289a-a0e8-33e3-b5e7-038675014200 | -16.4114 | -57.38844 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| fd0487bc-1b6b-3e0a-b89d-88280fde4462 | -16.41081 | -57.39209 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9d7b7cfd-1443-3ea0-8788-81a72b33dd13 | -16.40747 | -57.39151 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6785b094-465b-3f96-b85b-caed5d883874 | -16.40689 | -57.39516 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 95b65dd9-f637-3a7c-be29-d7dee4b1ab86 | -16.40414 | -57.39093 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 94b13a5b-d012-3d60-a14d-a215ccc23662 | -16.40022 | -57.394 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ead79acc-252b-3fb4-ac1b-24c49697d7cd | -16.39963 | -57.39764 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 51f63a01-87ba-3d7c-af52-dbc9987cbb92 | -15.7966 | -57.3396 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69f1059d-100f-31fc-b8af-44325852de52 | -15.79483 | -57.33564 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cdfd59a5-4011-3a6d-bfd4-019446ee4d03 | -15.79149 | -57.33503 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ffe5b14-f971-3e2e-bfb2-05af83f3f5d7 | -15.79091 | -57.3386 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd63d196-3053-33a4-bf2a-646af85687b7 | -15.78975 | -57.34573 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9188bb2-5bef-3f75-8580-c42493513af8 | -15.78798 | -57.35677 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 103e227c-0983-3f20-8aad-7f4cbb1fe25f | -15.78679 | -57.36422 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec86f9bf-d1e4-33f4-8cad-4440cd9f88a8 | -15.78344 | -57.36369 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1800bd63-5f21-36af-9ca0-fe71bda2a2ac | -15.77794 | -57.35518 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 786b211b-a668-3d4e-a369-7d3b904ae4d1 | -15.77735 | -57.35889 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 892c58e7-2b8a-31a4-913a-5fc6b6bcf2ce | -15.77519 | -57.35091 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73650bf1-c915-384e-9ca5-f8145959fccb | -15.77185 | -57.35037 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa7f259d-7cf4-3b47-87bb-c835502e5a41 | -15.77125 | -57.3541 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a385a805-9edc-3244-8289-570bdda6bf64 | -15.7691 | -57.34611 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ef38879-3c85-3f77-aeff-3d798690fae2 | -15.7685 | -57.34982 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21f59b47-123d-3406-a040-d2f1181b1f7c | -15.76575 | -57.34558 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cb6b09e-26d6-3228-9245-7dde79fe2f5d | -15.7624 | -57.34506 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88f5c5c7-ed1c-30cd-b2a9-a6c1e382194a | -15.69373 | -57.40812 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1313c383-6571-3944-afac-7865ff7e7dfb | -15.69098 | -57.40389 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef95d75f-9122-30a1-a1e5-c2145050329e | -15.66885 | -57.40033 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abca2693-540e-33d7-bf0d-790621220c1c | -15.65605 | -57.39438 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27dcaa23-8657-3a75-a668-f68ecfdcb74d | -15.65365 | -57.4093 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07ddf559-703f-383f-bbdd-2f967998f9d4 | -15.6521 | -57.39758 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38bb26a8-2fed-3de0-8e4a-d9c2a7fc7476 | -15.6503 | -57.40873 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68544d93-a476-3f5f-bc22-fe540f874699 | -15.64695 | -57.40816 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e18e204-f50a-32d3-b805-8e8f1ddde701 | -16.80901 | -57.82301 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6f6909c5-1c31-346d-b887-2b28df7a95ac | -16.8084 | -57.82671 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0cf1f526-b3de-37b1-8b0d-9c85751c718b | -16.80565 | -57.82241 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ae25915a-4e74-3ef6-9769-28b4f715ab0c | -16.79929 | -57.82906 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f52d92e5-b815-3430-a359-2e762a6301b8 | -16.79593 | -57.82846 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3ea02733-656a-352b-b1e7-3eba5d2ae96f | -16.79533 | -57.83218 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 94d071b0-c151-314a-a571-9f240b84a2ad | -16.79318 | -57.82417 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b70d7d4b-5981-3f6e-adc8-3bc2705dc7f9 | -16.79258 | -57.82788 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3a41aeab-9745-39b0-a0b8-9f128795cfd2 | -16.79197 | -57.83158 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 13e6cf33-3c69-324c-a9df-344e4f1e7e9d | -16.78922 | -57.82728 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3c4f0f19-6a36-3a77-94da-f5771966202b | -16.78861 | -57.83099 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 05b382f4-bafe-3528-828e-50f60aedccb1 | -16.78663 | -57.54641 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9e614e60-54cd-39b3-b76c-6e3c6eb376f3 | -16.78586 | -57.82668 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 01c296d3-bb5e-3683-9dde-d625efa0ba65 | -16.78526 | -57.83039 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 29930da8-83b0-3903-972f-0293289a1be2 | -16.78465 | -57.8341 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0ac78a0a-7e27-3a5d-82ed-6fd809793a03 | -16.78389 | -57.54216 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 034ed426-0200-3233-b34c-3c05176bc282 | -16.7816 | -57.49285 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7e3979ea-be8a-30e8-b612-7e91c631850b | -16.7813 | -57.83351 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 18d67913-0a62-3a13-a8d4-17d5ddd2807e | -16.781 | -57.49651 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 08eed9ca-15e7-32fd-b5fc-7feb968bd14e | -16.78041 | -57.50017 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 94e20d4e-bc85-322a-80f2-312aa2d4ac74 | -16.77854 | -57.8292 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 261bbc5f-4f25-375c-9ff9-907768406743 | -16.77826 | -57.49227 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b19e4f40-66c6-3dae-a75a-9f9e269471e5 | -16.77767 | -57.49593 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a4b0e6ea-8e9b-3817-9cbc-8a290e13518f | -16.77518 | -57.82861 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d235d468-dd99-3d7b-ba7e-61f3c9564f6d | -16.77492 | -57.49169 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 7bff2152-adab-3006-a476-5b0647b15a7b | -16.77433 | -57.49534 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 14a4edd8-6754-32a0-81a3-3aa3bd5ea949 | -16.76678 | -57.73195 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bdc2dd88-88ab-3e50-9db1-bc6f299a5772 | -16.76437 | -57.74673 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 64ebb22f-a601-3ceb-bd80-8a3b92c2c301 | -16.76377 | -57.75043 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7dd765a2-9455-3ae6-8d8b-e5c01013895c | -16.76316 | -57.75413 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 64570d5f-0ed7-3f12-83c0-d85b05ab260e | -16.76102 | -57.74615 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6ad71f3e-50b9-3f09-811a-00bf0f8b76bb | -16.75585 | -57.75665 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d7c709cc-8cc8-3321-b7ce-240281c437da | -16.75525 | -57.76034 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d94c6105-dfbf-3dc3-9530-42e76fea21dc | -16.75443 | -57.82876 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ae6262a6-c257-3215-bd0f-9a32a67c56a1 | -16.75431 | -57.49185 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0d2070da-1cda-33ab-8f5e-7947130bbaa4 | -16.7525 | -57.75605 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2b1ddc37-a534-3c1e-8b6a-253373ce5c27 | -16.75156 | -57.74068 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d5c71edf-eaa3-30f1-b00f-82dbe784fa2f | -16.75096 | -57.74438 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| eb28960d-6ef4-387c-9a89-063b6dfe0ca2 | -17.02025 | -56.74583 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bbb1c3ec-020f-3f5c-b93f-ab81844cb390 | -17.01968 | -56.74942 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 31f41c6f-e4c3-3592-a0c8-b07299138f07 | -17.01911 | -56.75302 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 202fd8fa-fe9c-39a3-85b6-3af6d3a004ba | -17.01855 | -56.75662 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a5febd8e-e95c-39ae-a9a5-6a796a3ba327 | -17.01844 | -56.77877 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e2d78f88-daaa-3748-8f12-22f532fb2285 | -17.01808 | -56.73806 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 36dcac03-2787-371a-a53a-163b37a1fb51 | -17.01787 | -56.78237 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4be7432e-1f88-3661-8c77-9fd450372590 | -17.01751 | -56.74166 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2b3fb1c0-bdab-3af9-9110-e748ef4c3b3a | -17.01694 | -56.74526 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b4f9c0c3-6412-390f-b8b3-d90579bbd511 | -17.01637 | -56.74886 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |


[Clique aqui para ver as próximas entradas](README165.md)
