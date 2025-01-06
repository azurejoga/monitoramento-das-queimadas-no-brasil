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
| 527a2d90-dd48-354e-a665-dca1ea1f97aa | -29.85232 | -54.93174 | 2025-01-06 04:53:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| a8ad3fb6-ae55-3ec9-8d72-f4fdad40c323 | -29.84832 | -54.9353 | 2025-01-06 04:53:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 112409af-00ba-34a9-a411-53619e41f57c | -29.85172 | -54.93594 | 2025-01-06 04:53:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 5794dd15-0e20-30c2-9016-c7aa74ae1269 | 4.31559 | -60.82905 | 2025-01-06 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b12b4681-3604-3909-b7cb-6a2c549b11ce | 3.89595 | -60.11472 | 2025-01-06 05:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7185055e-61e7-33ea-a3ea-ce474874408b | 3.49859 | -60.80346 | 2025-01-06 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36f8d1a8-2adb-34a7-8ac6-1f3bb114a776 | 4.31927 | -60.82458 | 2025-01-06 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09ff1a52-1a3e-371c-ba02-c88d6f50000e | 4.31128 | -60.82924 | 2025-01-06 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edc0ea1a-c2d7-3bcf-8d45-fe1fe0acf5e1 | 2.02772 | -60.8803 | 2025-01-06 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3bc3cbd-79b6-381f-87bd-bbdfd0ad3492 | 3.50277 | -60.8028 | 2025-01-06 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d66db3dc-04f6-39d1-8fe8-a726489ce921 | 1.10842 | -59.5556 | 2025-01-06 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46b31f99-571b-3982-aa5b-638d5f600500 | 1.35168 | -60.02972 | 2025-01-06 05:10:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d1760a9-af56-3981-a188-a1c5329ea644 | 1.10706 | -59.55379 | 2025-01-06 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18d41774-049d-388f-9953-726a2329db51 | 1.35555 | -60.02915 | 2025-01-06 05:10:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b13d74c-79bd-3aaf-beff-456a5b30a9e2 | 1.34931 | -60.03979 | 2025-01-06 05:10:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d94f6b7f-aa25-3612-9dfb-e349a37a2133 | 1.35317 | -60.03922 | 2025-01-06 05:10:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7118efcf-c4c9-3bcb-b71f-7c4bf6253cd8 | 1.34782 | -60.03028 | 2025-01-06 05:10:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 62b2e371-378b-3454-ae93-871a4978da5a | 1.35243 | -60.03447 | 2025-01-06 05:10:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 388f2efb-5688-3625-b465-b7958407f2bb | 1.34856 | -60.03503 | 2025-01-06 05:10:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c6da2cc-75df-3b7a-a484-a013c9dbd38e | -18.51107 | -53.40022 | 2025-01-06 05:14:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9798f43-22c6-385b-a395-e12f7b534292 | -18.51563 | -53.40065 | 2025-01-06 05:14:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f89c4a8e-bcf5-30f9-b92e-2a614d9b90a0 | -18.59005 | -53.16269 | 2025-01-06 05:14:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42fb956a-06f4-32e3-bebd-faa700d70e3d | -23.102 | -55.17322 | 2025-01-06 05:16:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 748ea977-88c3-3332-adfe-aeabe19a54b0 | -21.56417 | -54.20697 | 2025-01-06 05:16:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf031644-d56a-3276-a63f-7c50d64d0fdd | -21.55441 | -54.19923 | 2025-01-06 05:16:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5576ce92-8e56-3286-8773-8e6bbd7fc0c1 | -21.55834 | -54.20454 | 2025-01-06 05:16:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26e04285-5b00-3fec-934f-ca4292764e2b | -21.56281 | -54.20519 | 2025-01-06 05:16:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3ad8929-661d-35e8-982d-47cfd1a14827 | -23.77441 | -53.39264 | 2025-01-06 05:16:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f3a04c63-6e43-3c5e-9582-6674ce53183f | -21.56021 | -54.2017 | 2025-01-06 05:16:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c557254-2946-34a9-820d-3bde2828b046 | -30.31817 | -53.41584 | 2025-01-06 05:18:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 4ed17837-39ea-3928-9d74-3de66cec1261 | -29.85054 | -54.9372 | 2025-01-06 05:18:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 0ff9a42e-bf73-3ea2-83d3-7dcedfc5c128 | -30.32229 | -53.41833 | 2025-01-06 05:18:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 454043ef-dcbb-3cda-a467-0edc4a2746d7 | -29.85639 | -54.9263 | 2025-01-06 05:18:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| f5212fda-fb10-3917-b1e9-b84f8780ed40 | -29.85585 | -54.93205 | 2025-01-06 05:18:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| e4a4af57-8e60-382c-a9df-c9bc09adef71 | -29.84578 | -54.93661 | 2025-01-06 05:18:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 08948aac-697d-3d72-9517-ebb5720bf3a9 | -30.32256 | -53.41477 | 2025-01-06 05:18:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| c6e24e36-2b27-36d4-a8ec-129203b56a67 | -29.85109 | -54.93145 | 2025-01-06 05:18:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| e91ef8cf-56a1-3b10-aea4-15700616a1e3 | -30.32342 | -53.41628 | 2025-01-06 05:18:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 03929a6d-3ab9-30de-9b0d-b74f9697594a | -5.8523 | -35.4882 | 2025-01-06 05:20:00 | GOES-16 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 77da42c1-7d56-33a0-bebe-8e2b86aeb66d | -5.8526 | -35.461 | 2025-01-06 05:20:00 | GOES-16 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 2661cc8d-cc1f-3f2c-b7f4-05b21831dfa1 | 1.35576 | -60.02917 | 2025-01-06 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b615686-acce-39d2-8c23-ca494ece69c9 | 4.30907 | -60.82772 | 2025-01-06 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a17b66f4-197d-308e-80bd-a4ae38bdcfb5 | 4.31845 | -60.82269 | 2025-01-06 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 66ef2a30-56ed-3870-85f5-6bfc2fb9bbef | 3.49153 | -60.81466 | 2025-01-06 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cda7bfc6-927d-3999-ac0c-14bc795d63b2 | 4.31238 | -60.82721 | 2025-01-06 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d77ef9e-2a70-3a10-a813-5f1e4558c368 | 3.49707 | -60.80669 | 2025-01-06 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82776a67-cb3f-39c1-9d57-2353244b7e3a | 1.10643 | -59.55669 | 2025-01-06 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cad440a-001f-3924-bee3-50c05494e22e | 2.02766 | -60.88332 | 2025-01-06 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93a07cd9-a260-3d7a-aae8-39d6d25228cc | 3.49984 | -60.8027 | 2025-01-06 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfa46ecb-e9e8-3891-9d28-a9ca42923895 | 3.30697 | -60.52893 | 2025-01-06 05:31:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a503e78c-ac7e-36e7-8280-d7ef3fd82835 | 3.49653 | -60.80322 | 2025-01-06 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a71c1bab-3a47-3f6e-8917-d3ff9f85f1d2 | 3.89394 | -60.11622 | 2025-01-06 05:31:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d238c49-2a93-3924-b5cd-8ff27586e77d | 1.3501 | -60.03768 | 2025-01-06 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 605fcc23-ad25-3d3d-b923-057a9c0d4f75 | 1.34892 | -60.03027 | 2025-01-06 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9328a552-618f-36ca-a5e9-0bf9ff1b6123 | 3.51961 | -60.77822 | 2025-01-06 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6f1f735-088c-3a9f-8cf3-15f65a1d825c | 1.68659 | -60.37369 | 2025-01-06 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2754c9e9-c2af-3ed3-96dc-38166d100835 | 3.49539 | -60.8176 | 2025-01-06 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09baf72d-14b9-3860-8f81-91ab3ced1646 | 1.35234 | -60.02972 | 2025-01-06 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82941e85-e348-3378-835e-7caf6bb42ae7 | 4.31569 | -60.82666 | 2025-01-06 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61f7a149-047a-3f97-ac91-c5ad1f15c383 | 3.4943 | -60.81067 | 2025-01-06 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0d10237-ae0f-3387-b858-15cff3302c4f | 3.49262 | -60.82159 | 2025-01-06 05:31:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad641a20-f5d5-3251-b2ad-a50281a31cc3 | 1.34951 | -60.03397 | 2025-01-06 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 291f52fd-615a-3feb-b221-b8889ac5afea | 1.35293 | -60.03343 | 2025-01-06 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78ac96a3-6482-33bb-9b8b-77f6e1eb2c48 | 3.89729 | -60.11568 | 2025-01-06 05:31:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93504568-e44a-3f70-a75f-8a6ea27275ec | 1.10583 | -59.55282 | 2025-01-06 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c12189f-09e3-3c74-8273-b35db1d7ed97 | 2.02711 | -60.87983 | 2025-01-06 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c65b3888-0d6e-316b-aa9d-58fc49017f31 | -18.51353 | -53.40734 | 2025-01-06 05:37:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db65949f-7613-34a0-a459-32eae348d527 | -18.51017 | -53.40673 | 2025-01-06 05:37:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a56a2ad3-f8ae-3aa8-9be4-e56f380f7f46 | -18.51401 | -53.40174 | 2025-01-06 05:37:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 907743ae-f042-31fd-9475-3e269c0871cf | 1.35234 | -60.03013 | 2025-01-06 06:14:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 56761301-7105-3990-a01f-f40b263ffbe0 | 3.49522 | -60.80451 | 2025-01-06 06:24:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 14302c60-1b8e-36be-a652-1d6cf0fd911e | 3.49636 | -60.81115 | 2025-01-06 06:24:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 843053ad-dda8-3e3e-baf4-1293f06b76c9 | -3.61925 | -42.30042 | 2025-01-06 12:14:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| bbf82eac-0f8b-3711-a2b8-55308a3f1ecb | -3.70826 | -42.13373 | 2025-01-06 12:14:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 72b2adbd-d1e0-3377-86e9-6bb31e9e1a09 | -3.70693 | -42.1429 | 2025-01-06 12:14:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 29900ff0-8187-34e4-9917-563972706b75 | -3.00208 | -41.78886 | 2025-01-06 12:14:00 | TERRA_M-T | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 37f02826-741a-34fc-991d-063dddba7418 | -4.14358 | -43.71365 | 2025-01-06 12:14:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 52bd624b-20d6-3353-9d8f-d06b6382e126 | -6.1025 | -39.53134 | 2025-01-06 12:14:00 | TERRA_M-T | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 9181cc4d-016c-3113-9001-c521995b5e05 | -3.69791 | -42.14163 | 2025-01-06 12:14:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0a4aeaf2-4de5-3176-a025-ab2c5e4fe47f | -3.69924 | -42.13244 | 2025-01-06 12:14:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c89b7969-006c-3075-84d6-024e05c20eff | -7.18106 | -40.89309 | 2025-01-06 12:16:00 | TERRA_M-T | VILA NOVA DO PIAUÍ | PIAUÍ | Brasil | 2211605 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| baa860c5-5900-3458-a8e8-11a4725b238c | -9.97197 | -38.06815 | 2025-01-06 12:16:00 | TERRA_M-T | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 37038e33-a06f-3f7f-8e14-1658ee78200b | -7.31927 | -39.98281 | 2025-01-06 12:16:00 | TERRA_M-T | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d5b7f0cf-001e-30ea-b03e-0183a1cd7bbc | -9.97373 | -38.05481 | 2025-01-06 12:16:00 | TERRA_M-T | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 5e6b7916-7d25-3e0c-95ca-165debe329ff | -9.59365 | -38.23282 | 2025-01-06 12:16:00 | TERRA_M-T | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e4daedf0-81ec-3df4-8859-ad9e1a119339 | -7.7562 | -37.55756 | 2025-01-06 12:16:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 14.8 |
| b99b8739-ff36-33bb-9e4e-eaea1a0e9ac0 | -14.31492 | -39.31782 | 2025-01-06 12:16:00 | TERRA_M-T | UBAITABA | BAHIA | Brasil | 2932200 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| c166de91-f210-39d1-b55d-a6be193302e8 | -7.60999 | -37.79987 | 2025-01-06 12:16:00 | TERRA_M-T | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 2a67e59c-8c7c-3fe2-a737-2bd181bcaada | -7.68576 | -37.84081 | 2025-01-06 12:16:00 | TERRA_M-T | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 13.4 |
| effda21c-f249-33e6-8a29-e04fde8dcbcb | -20.86177 | -40.93589 | 2025-01-06 12:18:00 | TERRA_M-T | RIO NOVO DO SUL | ESPÍRITO SANTO | Brasil | 3204401 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 8b5287e7-4ee0-3837-84f3-c84ab4efffbe | -20.2452 | -48.31196 | 2025-01-06 12:21:00 | TERRA_M-T | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 13.0 |
| dc8cca64-3ff8-3bab-a1d9-5b619a610020 | -22.89395 | -43.48783 | 2025-01-06 12:21:00 | TERRA_M-T | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 37c00c8d-2dbe-369c-9351-f70026871def | -20.19634 | -48.49823 | 2025-01-06 12:21:00 | TERRA_M-T | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b6cf3c66-8b78-3b68-9f6c-e9075b50e554 | -22.813 | -43.34816 | 2025-01-06 12:21:00 | TERRA_M-T | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |


