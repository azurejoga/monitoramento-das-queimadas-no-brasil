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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ebca4ff-e260-36de-9d8a-aa9cdb9fe35c | -9.74821 | -67.56578 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88e43820-ffcb-3ed4-a724-19f1489824d1 | -9.71158 | -67.47385 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7d7b1cb-cbf2-3f0a-9b12-1fbcfea43a35 | -9.71103 | -67.47734 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96e052b0-5423-3e69-a7e6-f9bc93c8497e | -9.68343 | -67.58769 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71baee9c-5a02-3cb8-a9ca-8ac6485b317c | -9.59844 | -67.52775 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85ec1685-9790-3e96-9641-9d1cbcdf49b7 | -9.59506 | -67.46268 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd84b60f-6d8f-3c31-b668-e00668b38bfa | -9.59173 | -67.46215 | 2024-10-16 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9bacc9d-d623-39f9-ba71-e60d63d28f0f | -10.63225 | -67.83672 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0df7e8c6-1848-3100-85f5-43b403a4b779 | -10.62893 | -67.83617 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82cdc51b-583f-3b6f-ab8e-09d0dc4ac430 | -10.62782 | -67.84319 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5237c0ac-190a-361d-9ce6-0d488c759b61 | -10.62505 | -67.83915 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f76a453d-84a1-3a2e-8a6a-149d248f201f | -10.57579 | -67.76658 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61b9d100-fa76-32f8-b486-5aedbb36b5b0 | -10.57523 | -67.7701 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a245d93-eb60-3887-a32d-741f12809a6f | -10.57357 | -67.75903 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c57f0a8-f47c-30e0-9e2f-ba741ffc6c41 | -10.55751 | -67.77444 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bef8d13-ee93-3893-b084-5a2e2321a5fa | -10.55419 | -67.7739 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e3938ca-90ae-3460-aca2-510183a56d98 | -10.54366 | -67.7758 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40611c45-4fde-301d-b88a-562aed0e3b79 | -10.54034 | -67.77526 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e9f5058-aa6d-3af9-bf0d-450f456f29c7 | -10.53868 | -67.80738 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80962ac4-b83a-3d52-a2d7-74df4422a7bc | -10.53813 | -67.81089 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e7f3261-0fd2-305f-b82b-5def497da555 | -10.46152 | -67.74129 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b08e096-245d-3f5b-ad85-58161c2ee946 | -10.41943 | -67.89998 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56a8e27b-4a70-3f0f-b3e0-81b98744a014 | -10.40282 | -67.91882 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7630dc6e-2195-343a-859c-52d2a87c1723 | -10.39227 | -67.96391 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96eedf8a-e007-3d6e-bb17-ff865f95ed6b | -10.38895 | -67.96336 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32a86529-b7aa-39bf-a20f-d8f8c8dfc364 | -10.38508 | -67.90163 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a82ba003-ec71-3712-a27a-3339bef7aec9 | -10.38454 | -67.90508 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c3d37e4-12cd-3a33-9d0e-c6a14bb7cb85 | -10.35791 | -67.96555 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9f02f35-26c7-3311-be8d-3f60c6ffac51 | -10.35504 | -68.06957 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6223dde5-a579-3fa0-8485-3865acbb50e3 | -10.35458 | -67.96501 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8317584-9753-3563-bb53-feba56adc23f | -10.35171 | -68.06903 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 902499b9-1b18-3e2e-9e42-66bf88e49237 | -10.34752 | -67.92801 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2458ad24-0545-3671-9dd2-579f36d5f8e4 | -10.34475 | -67.92396 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c990fad-31a4-36e7-bdbd-4505b148bdd1 | -10.34419 | -67.92747 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0150ef6c-eb1e-32ed-9915-5c0f2955b7a5 | -10.33643 | -67.95502 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee159bda-e6e3-3550-bffc-8d4c747f6b57 | -10.3331 | -67.95448 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0e64e98-d30d-36f4-b42b-ea8271b82126 | -10.32811 | -67.96447 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a33a4a1f-a043-3505-9f8b-2b2f4265c0b5 | -10.32756 | -67.96799 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83eebce1-0972-391f-a94c-ed10a1d17e4e | -10.28263 | -68.01473 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69a03b0c-4a9f-3ece-aa75-f9adb3626990 | -10.19716 | -68.31528 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 604b40ea-63c6-3dee-b1ee-0e2b75b13f49 | -10.19326 | -68.31828 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71727de9-7b0e-34f4-8982-0706b02c4a45 | -10.18567 | -67.92316 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0348e6f-b054-387b-8a88-4498578bda4f | -10.13409 | -68.31202 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6af0cfe3-fa0d-35ea-8078-aeeeade3c4fa | -10.11497 | -68.38882 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39b25160-f93a-3db6-91a1-2e8fa570e65d | -10.11351 | -68.31229 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef39adb7-7c68-3c6b-ae47-461189eb7bca | -10.0904 | -67.90432 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab54aa9b-7da8-3131-89c6-ce5bfe6a5e54 | -10.08283 | -68.2966 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f71bae1-3008-31ea-aafd-065587e8bb17 | -10.07949 | -68.29605 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9593ad5-2631-3dc1-8163-14e56ce5ebc3 | -10.07496 | -68.3605 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eab6798-bf36-3285-913a-6b378943a51a | -10.07439 | -68.36404 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bf156ef-58ff-3090-a60f-9265a0d03897 | -10.07271 | -68.36029 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32e00f3e-191c-31e7-ac9f-32c323023bb2 | -10.07256 | -68.05988 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 632199bb-1f0e-3834-8633-df7147d6910d | -10.072 | -68.0634 | 2024-10-16 05:48:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 688eb784-1014-31e9-9b9f-8cfcfe9b401d | -10.6317 | -67.84023 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61880f71-155c-3377-b5d1-c3828ed572e6 | -10.62837 | -67.83968 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bb3e798-9dbe-3412-878a-c3149627b6b4 | -10.62173 | -67.83862 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 652c24a1-bfa1-3a1a-888c-57aa1baf3b15 | -10.6184 | -67.83808 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7ce7077-2549-3a3c-a658-64be94e6bd6b | -10.61785 | -67.84158 | 2024-10-16 05:48:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b811be6-3307-33bf-857e-4b1bb7dd55b8 | -6.28659 | -58.26517 | 2024-10-16 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f30f3f83-edef-334d-9653-9773c1822122 | -6.28572 | -58.27121 | 2024-10-16 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31868f38-f85e-3fc7-95ee-b6c30f6d093f | -6.2819 | -58.26143 | 2024-10-16 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c216103-f15d-3a55-b227-59c7afa5fbe8 | -6.28146 | -58.26444 | 2024-10-16 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38d87ea4-6129-3299-8a5d-2f188c3f849d | -6.2806 | -58.27047 | 2024-10-16 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f399a0fb-6ac6-39c3-a0c8-19e774a13107 | -5.5689 | -61.49913 | 2024-10-16 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29ae4523-d83e-30eb-905b-63dd5941be3e | -8.98503 | -61.42858 | 2024-10-16 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8ea2102-1644-3c9c-b9c5-b33a7930a765 | -8.98447 | -61.43262 | 2024-10-16 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e589332a-d412-3485-ad80-1c0cd21c0b24 | -7.6018 | -63.48818 | 2024-10-16 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 058daf57-e70f-345c-8447-1350c33b62fe | -8.80786 | -63.18346 | 2024-10-16 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 238274bd-1330-37b7-94f7-51faa231135a | -9.29744 | -63.23569 | 2024-10-16 05:48:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68532633-967c-394c-9ddb-25f869b674d4 | -7.81667 | -65.12924 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e2559a5-54a6-36ca-9ac6-8fa1403c3c82 | -9.17775 | -65.3923 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e218f37-2727-34b5-9051-76bef0cb736e | -9.17717 | -65.39606 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 831b599c-066a-3f7a-b7a5-d73e98ef041b | -9.1766 | -65.39983 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b845995-4249-32a7-94a3-4c97436c1076 | -9.17603 | -65.40359 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c5d2831-cef2-3ece-bd1b-0f0b0279afb2 | -9.17546 | -65.40736 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8bf23b0-8347-3dc9-93d7-aec3ccd23f2e | -9.17489 | -65.41113 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41e9e0da-f4c1-379e-aa8c-72f7ae110ddc | -9.1743 | -65.39176 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f343578-1a0c-3424-ac3d-2c49c0d79af0 | -9.17373 | -65.39553 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5bc9caa-4684-3b48-8193-480d04ba3577 | -9.17316 | -65.39929 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4608ec91-23da-3f6f-a35e-d19992b4e402 | -9.17259 | -65.40305 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bdbbad9-95dc-3c77-a706-39bf47b37825 | -9.17202 | -65.40682 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 671788d8-dd17-3803-afc2-dd1bea038962 | -9.17028 | -65.395 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7665c534-89e5-3f82-a25d-52f0f4e5d54e | -9.16971 | -65.39876 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bba9b934-deab-3829-ad95-bd4304569de6 | -9.16914 | -65.40253 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81ec7540-fc8b-320a-a8cf-97db96109026 | -9.16627 | -65.39823 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 797e386b-b5f6-3505-80de-963ccf15cbbf | -8.93289 | -64.31873 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9a02192-5ca6-34a9-af93-555d4d33c86c | -9.4416 | -64.57468 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae2db920-c218-3ba0-a7f6-187182b42d36 | -9.30361 | -65.36909 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b382e69-b975-399b-a20a-9128dc1a6ad8 | -9.30074 | -65.36477 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ee8b794-3f9c-36a4-9623-9199bfef3eb5 | -9.30016 | -65.36857 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a667b3e7-0f15-3efc-9061-025e20450bbc | -9.29728 | -65.36424 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 99641c67-4905-3cb9-9be8-7d5ba71dc777 | -9.29671 | -65.36805 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2656d0cd-24b4-37be-a46d-3ef373c1eb09 | -9.29497 | -65.37949 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73c590e6-135f-3b03-a922-9076de59b6c9 | -9.28864 | -65.37466 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5a40ecc-4416-3117-a60d-db596d46e916 | -9.28577 | -65.3703 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 596528f9-3652-3d9f-8a38-e95043588e0f | -9.26987 | -65.56784 | 2024-10-16 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5745845-5ef3-3855-b183-96094f845ea8 | -9.92679 | -65.20423 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30abd652-5bd8-3ec4-bfb8-78493110fdb7 | -9.92621 | -65.20812 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21bad60b-d8d8-3bca-b726-34ac2708bbd9 | -9.56962 | -64.62466 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ae0877b-eb2a-352c-8962-1e6d7e369a2d | -9.56786 | -64.62158 | 2024-10-16 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README68.md)
