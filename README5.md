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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dca3b8f-1930-34e3-b125-dfe18d0a463f | 0.45254 | -60.39464 | 2026-02-21 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfa6e46a-5cd8-39d9-a4aa-beff08935ec3 | 2.6906 | -60.23289 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 426fb11d-6291-3ac2-a94d-cd2567c4ada7 | 2.70531 | -60.23954 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 95e60288-c4b1-32e9-82f8-fbec6d42a7d3 | 2.67547 | -60.40783 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b785a892-0ede-3ada-b633-a65488984cbb | 1.93611 | -60.3677 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a5b4217f-155e-396c-b517-97bfda007041 | 3.48088 | -60.77741 | 2026-02-21 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c0b2c6f-176a-37ce-b8b5-4af798fb587f | 2.5468 | -60.73446 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c424c34d-4d92-3122-96bc-75ca7acb5509 | 2.56708 | -60.5601 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 004b62f1-9b68-34ec-b2fd-05a4cb4aec67 | 3.0862 | -60.09503 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e31454a-364f-388f-a8b3-4b645c10f5ec | 3.08175 | -60.09571 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27e39fb5-1958-3a86-af41-921428fb0f41 | 0.45448 | -60.40712 | 2026-02-21 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49c093ec-f18d-3108-87b6-2f032e60cc47 | 2.67919 | -60.40904 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ad65255b-3865-3c59-8c98-b746e965c8e0 | 2.89401 | -60.58753 | 2026-02-21 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01c1fdb9-0706-39cc-b2c6-705ae0498da1 | 2.6844 | -60.41284 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01a3f79f-856d-3ff7-ba3e-604588e7f034 | 2.67989 | -60.41352 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90c18a67-d584-3d05-b0f3-a998dd8ec815 | 2.68565 | -60.26063 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2bf29256-4b37-30ed-908b-892f46fc41e6 | 2.69885 | -60.2271 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e5a6be4-d95c-3fdb-a316-02bb6d7c510e | 4.16518 | -60.86074 | 2026-02-21 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bde32fb-6c55-3650-8677-025946c0bf4a | 2.67998 | -60.40714 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab94c0f9-707f-3875-8309-100f0c932b89 | 2.87569 | -60.59044 | 2026-02-21 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35856ba2-2576-3c72-946e-39e5636e5dea | 2.68879 | -60.25113 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 998b605b-779a-35ad-a385-92e0627aafb7 | 2.55601 | -60.73302 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 494109a7-ff6e-3fdc-95c1-03d3ce80a68e | 3.47872 | -60.77606 | 2026-02-21 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4da9791-cea6-3c0f-9605-c32193c2b193 | 1.83084 | -60.84559 | 2026-02-21 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9865d646-cc9b-30c0-b4c6-ccda620c95d3 | 0.45754 | -60.39811 | 2026-02-21 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66776800-ea83-300c-a3a0-8267ee3f4b83 | 2.88627 | -60.59826 | 2026-02-21 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4e3139d-e43c-3da0-ba46-023488d1c5e2 | 2.76776 | -60.28842 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e700b80-718b-3c57-aae2-a2c7b783c60b | 2.55412 | -60.56673 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d24cf85e-5e40-3519-96b3-f26255e82eda | 2.7091 | -60.23447 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 602d459b-4372-322d-873a-60b229b9efb3 | 0.45383 | -60.40295 | 2026-02-21 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d449b1da-b448-32a7-b587-6e83b21da2a7 | 2.68862 | -60.21975 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6d2ae51-44e5-391b-8349-bf9522ecc8ff | 3.77994 | -60.02666 | 2026-02-21 05:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13233c9f-f824-36ba-ae85-d0a57197d15c | 2.55141 | -60.73373 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d1b7668e-74e5-3644-a027-54dc0ffc9895 | 2.70151 | -60.24463 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0d12dda-f2cf-3857-a983-e9716e5bd278 | 2.68131 | -60.41612 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c45564e-24c2-364a-a547-fcde0a7126ff | 3.4834 | -60.77534 | 2026-02-21 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97533b1a-8711-37e2-b43e-1f86028e1f22 | 2.67613 | -60.41233 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1054f24a-e00c-3961-918b-4292de873dbf | 1.945 | -60.36633 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a4da725-f5ce-33ff-979f-14394cd85761 | 1.94567 | -60.37072 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e21214d-89b7-357a-a65f-e43c869e728a | 1.94056 | -60.36702 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b088f15a-b0bb-311f-9d8b-664ec564085d | 0.45319 | -60.39879 | 2026-02-21 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59284bb7-38ae-39eb-adb5-62cf2d9c5288 | 4.16593 | -60.86589 | 2026-02-21 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbf58e67-8172-37cf-ae36-c8dec70ff1fd | 1.97695 | -60.70033 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3703b36a-8b36-3fcf-9f36-cd2a95521051 | 2.70843 | -60.23009 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3c4ceb93-01bc-3086-9dd8-05b72fa2cd4a | 2.56252 | -60.56075 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a5f0cd7-f8f7-38bd-b583-ef294b1d5a27 | 3.0824 | -60.10005 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c729a7e9-dcf0-3908-8dd2-065cbe28f872 | 4.06604 | -61.12104 | 2026-02-21 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22a462bf-1cb9-3b7d-8fd6-f965d7a170ce | 2.54886 | -60.56281 | 2026-02-21 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b0c2fc76-4019-3372-969a-a56aa613954d | 1.82697 | -60.85098 | 2026-02-21 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0c116e7-13a3-3f07-88d5-a3d3de94ae6e | 3.08305 | -60.10439 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa8ade8b-8756-3182-94a5-ca36b3328dec | 2.69952 | -60.23148 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6bb98efd-04d0-3496-81a3-f205f93cca3f | 2.70397 | -60.23078 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8fbb902a-0a90-3acd-a0d7-ce828893949c | 2.88027 | -60.58973 | 2026-02-21 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ccc8026-d320-3009-aa8d-7345fd027c0c | 4.16668 | -60.87106 | 2026-02-21 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a24e021d-04bd-30fa-8e37-cf17e3ca653d | 2.70085 | -60.24024 | 2026-02-21 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31e2973d-ff68-33a3-b724-ab8d3ff96f6d | 2.7088 | -60.2208 | 2026-02-21 05:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 70219c3b-894f-3215-a499-93f2545b7d2f | -11.8402 | -58.04274 | 2026-02-21 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 771738f8-62ef-33c0-aec4-4eb44367bf26 | -11.83627 | -58.04578 | 2026-02-21 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52ae2ac3-b879-33cd-b59b-4e95f105164a | -11.95414 | -58.742 | 2026-02-21 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b522ea2-4826-3a80-84d3-3e1715adeccd | -9.92328 | -59.92404 | 2026-02-21 05:12:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6e63a1eb-b457-35f7-9b7b-a18d5b211068 | -11.83685 | -58.04219 | 2026-02-21 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4c4e022-e648-3ffd-8f0d-09637e546dd8 | -11.83742 | -58.03861 | 2026-02-21 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7242acff-8b8f-395d-8550-6ac1347459ac | -11.95474 | -58.7383 | 2026-02-21 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d51000bc-0235-3839-840a-a6abedca0ab7 | -18.97413 | -52.92997 | 2026-02-21 05:14:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 05baf135-964f-3afc-bbbb-e7b853981c3e | -15.60005 | -59.29447 | 2026-02-21 05:14:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30b84af5-847d-3d90-8ff3-d25bd09d4f2b | -18.97463 | -52.92586 | 2026-02-21 05:14:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f3c40ddb-ce75-3140-be50-238ae1f25c7d | 3.92627 | -59.96312 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62d23cf1-d38d-3b5b-922a-62a2342beb25 | 3.07903 | -60.10783 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c705df6a-994f-3ba7-89f0-c4a4ccaf2230 | 2.68205 | -60.41287 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbbc413d-c53b-3381-8e60-784bad80a4e3 | 2.6846 | -60.25784 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2a0b49d-0f10-3c31-b8e7-195349cf4cc2 | 2.88001 | -60.58911 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 635fb6f9-4add-3f84-9e85-e1f94dc07f17 | 2.8767 | -60.58963 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b1cea56-9082-3a8d-9b18-96b5fd69b4a3 | 4.14655 | -60.30198 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52b0b59e-f9b0-3729-89ef-878a3d1a69f9 | 2.8844 | -60.59547 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f8acee0-4888-3148-9035-35b10ee6c78e | 2.67766 | -60.40651 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b720729-23d3-3995-8bba-d40437bcd8f0 | 2.54939 | -60.73295 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8d412edc-e071-34d0-b336-a2ec3d8d2dae | 4.08768 | -61.16068 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc66c538-9243-3622-99d7-1e30927853bd | 4.27733 | -59.79511 | 2026-02-21 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d47328c3-8c09-34df-a8fe-e4d27b9406d8 | 3.07958 | -60.11126 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a4c0251-a001-3e12-8b22-4c771e7dc640 | 4.59267 | -60.39434 | 2026-02-21 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26e89f37-111d-360b-b590-d55eeaa30b9b | 2.70449 | -60.22971 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0a7a66fa-602d-3165-acdc-42451465f476 | 2.70779 | -60.22919 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e83b9729-2399-3a12-a7e8-aaedc413e35c | 2.5527 | -60.73243 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8dfedf67-a7fd-33df-8d4b-1ca592f9f606 | 4.08379 | -61.15768 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 484d2a9a-6a05-3355-b880-40ffb8d301f4 | 3.48063 | -60.77784 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2173d04d-295d-3610-9c68-09064b6178d1 | 4.16355 | -60.92876 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2a83bd1-ff65-329f-9084-c764c0687579 | 4.0599 | -61.09261 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80ca7bb4-4a60-3623-b916-67ebcad9a69c | 4.07387 | -60.14423 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bac4dd0-2461-3320-ad69-2628ebebedfe | 4.16698 | -60.86375 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18806caf-5e4c-329d-bc2e-6244a5a8bec7 | 2.55644 | -60.5627 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 277e668c-a87f-3aad-97ed-ee545b7fe8b4 | 2.55655 | -60.73536 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| da57499f-df0a-3b47-96e0-6e92461bb458 | 2.68799 | -60.23228 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90d7487c-cc28-3177-a2bb-28566e111d1c | 2.55368 | -60.56665 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 18028530-504d-3916-932f-d5cda702345d | 2.56635 | -60.56115 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 80812907-7396-3bc6-81ac-df79ecad0599 | 2.68096 | -60.406 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4d24af0-c141-39a6-951a-b6e629d65f09 | 4.18233 | -60.05283 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb63f93e-55bc-3d93-945e-c88bf7dafece | 2.69789 | -60.23074 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d337e0c2-ca9b-36e7-9d3b-328fdf531859 | 3.4492 | -60.75074 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17570b59-10ad-3fd0-841a-f7b78d26796d | 2.70119 | -60.23022 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 102385e1-894f-3cf0-a0ca-34706aeb7b5b | 2.68514 | -60.26126 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README6.md)
