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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27ef36ea-ecfc-352b-ae8e-ac84c09b936c | -17.82724 | -54.54474 | 2024-11-16 05:22:00 | AQUA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2b548048-b6d0-39f6-9fa4-bdedc250ea79 | -17.23528 | -57.45499 | 2024-11-16 05:22:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 59862c63-a817-374f-afa6-bc67da6cc09c | -17.59971 | -57.56172 | 2024-11-16 05:22:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 178.4 |
| 55f7b6ba-09ff-3ec4-8e00-950c18bfb377 | -2.78 | -48.5806 | 2024-11-16 05:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 16a5f6cb-a2c6-3ae9-b6b7-1e871bfd1447 | -4.4725 | -44.5752 | 2024-11-16 05:30:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 4f3b388d-ccf4-3525-a190-a1a3e0261e0b | -6.1363 | -42.578 | 2024-11-16 05:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 2ba21f10-2050-3331-a430-39405202650b | -2.2299 | -53.6018 | 2024-11-16 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3292add8-600c-3483-833b-75ff81f44c71 | -3.2753 | -45.5151 | 2024-11-16 05:30:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 897e1016-b2f1-38b8-84f2-a57d200473fe | -3.2939 | -45.5144 | 2024-11-16 05:30:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b5336064-9c79-3e16-ab06-ff83cc36301c | -2.2299 | -53.6219 | 2024-11-16 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 38dc4c1a-8347-3240-843b-034a39ec829b | -4.4726 | -44.5524 | 2024-11-16 05:40:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 47ca65c0-1666-3b9b-ac44-4699cb8e81b0 | -4.4725 | -44.5752 | 2024-11-16 05:40:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 02ecf6cf-711c-3c33-ba38-7cf9ee9ceee4 | -3.2753 | -45.5151 | 2024-11-16 05:40:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3ccfa553-def8-31b4-8443-bdb81071b046 | -3.2939 | -45.5144 | 2024-11-16 05:40:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| e671566e-a3ca-3b0e-98b0-2dcade683c2a | -6.1363 | -42.578 | 2024-11-16 05:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| eef318d4-7130-3eb3-ab62-7f20e04b899f | -2.78 | -48.5806 | 2024-11-16 05:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9eeb15ae-fdba-3261-9b54-315fc26b0218 | -2.2299 | -53.6018 | 2024-11-16 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 2c1b2b55-1ca5-3f3b-ba4d-3fa53e1ab1c6 | -3.2754 | -45.4927 | 2024-11-16 05:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 3512ee7b-4370-320b-9ca7-07498797a711 | -2.14959 | -53.71365 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e0151ee-80ee-3de6-9f0c-802a5f15fcd7 | -1.63832 | -53.27762 | 2024-11-16 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eb22ba5-9bce-3fb6-80ac-0e2de76ffc7b | -2.15245 | -53.71493 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7add229e-38b7-394e-a89f-de3c7e9fddf6 | -1.64517 | -53.27362 | 2024-11-16 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6eee973-ebf7-37eb-aabd-cbc279d19be8 | 2.62184 | -60.41315 | 2024-11-16 05:42:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27e4e4f4-db2f-34a6-bd6a-4c30a39281aa | -1.23424 | -53.70693 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29f09b17-cd42-3c6d-9ebf-eadd6e8198e6 | 2.61825 | -60.4137 | 2024-11-16 05:42:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bf0951c-9d7f-3fe9-872b-cafe2c54093c | 2.6189 | -60.41781 | 2024-11-16 05:42:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30857f80-a6bd-3342-96e8-8ea049ac8c5d | -1.63217 | -53.27703 | 2024-11-16 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80037703-0cb3-316f-a8ab-866d36d08196 | -2.15623 | -53.71022 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 147f3d70-666c-3c20-b61b-0da331fe77c1 | -2.15309 | -53.71053 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ecd46b0-5b35-336b-9468-0e3470f2d4a5 | 0.79298 | -50.73887 | 2024-11-16 05:42:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a612ad96-0be4-31e8-9121-774eea02a87c | 2.62543 | -60.41257 | 2024-11-16 05:42:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef8e0ef4-0ee2-33a2-8f8f-0c2e727b93e0 | -2.15026 | -53.70925 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1f3bf22-6a76-38ff-95ee-67274791c3f1 | -2.22864 | -53.61398 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 151b540f-2d7c-3733-9244-95ee9a7292ec | -3.54429 | -51.49154 | 2024-11-16 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8c814b2-4744-389e-b824-abd11f869674 | 1.59204 | -55.85849 | 2024-11-16 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96453976-9ce8-300c-9036-99c54bbecfd8 | -2.22999 | -53.60489 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a94765dc-1abc-3fc6-9d59-bb59c89990c3 | 0.79411 | -50.74129 | 2024-11-16 05:42:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aeb2f53f-e2c7-32d3-8b79-262a53fa1116 | -2.22931 | -53.60943 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f97c9b53-a4e0-3096-a036-abecea9aeec5 | 0.42559 | -50.91762 | 2024-11-16 05:42:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 02a8a6fd-b854-35c8-8baf-7c729f3132c4 | -2.14712 | -53.70951 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68a71895-b105-3d88-8ba5-f41c5877effb | -1.22829 | -53.70636 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e7428e7-ae63-3706-98fb-9d7730baccbb | -2.15372 | -53.70616 | 2024-11-16 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80642f34-dcea-36c8-ad54-184d559c0091 | 0.72514 | -60.36938 | 2024-11-16 05:42:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa778551-fb4c-3c1b-a4db-72ca59614a62 | -9.13449 | -62.48809 | 2024-11-16 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 51eb2214-4041-3940-b1af-0d70ac888f45 | -9.53542 | -66.61309 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd9be3e6-d885-3554-b7b8-8290961cace1 | -9.70377 | -66.9706 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b0e0364-5c28-3c23-ae18-c97bb573d26c | -9.71222 | -64.19175 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38d39f29-2107-30bb-8d92-a636132b4460 | -9.55229 | -66.20184 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a4c5e2f-a49e-3337-9b07-b1cb02fa3143 | -9.07901 | -65.85596 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa978482-bcac-3f02-99cb-4777dc8f6efb | -9.70822 | -64.195 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 188d4476-76a3-3a9e-bc89-be1877485577 | -9.07571 | -65.85544 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f841cbd3-8f28-3160-ab26-0f25d654da7d | -9.90079 | -65.12992 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41c5a6fb-e3fa-3d73-8205-8444a5d7e119 | -8.9934 | -65.4202 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e0df8d6-9ba0-3367-8629-92c08b9e2584 | -9.82322 | -63.36088 | 2024-11-16 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa2bbd8-668e-3d21-a58e-f4c3e0c6e03b | -9.42377 | -66.58813 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ded6c544-1624-3da2-909d-5f247cc734e9 | -9.81724 | -63.23459 | 2024-11-16 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 122b04ca-b29e-338d-99e3-949f1d4ce295 | -9.22904 | -64.23583 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91347e64-f969-3af3-bf5a-c67d292c0ec9 | -9.70534 | -64.19069 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12902c16-dba4-3163-aad4-aef56dfe9311 | -9.07517 | -65.85892 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 645bdbe2-2cff-32fc-a606-4ced22d25fa9 | -9.66296 | -67.33389 | 2024-11-16 05:44:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43c82726-a18b-385a-8a40-c4cd59081e2e | -9.62118 | -64.89182 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0c238c8-b890-37e1-8cdb-6a1cce132831 | -9.6348 | -67.23469 | 2024-11-16 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45fa272e-41ce-312d-8d3f-b470e1ed4c25 | -8.99672 | -65.42072 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e7111f1-38c4-3acd-9a79-ed4de3e351a0 | -9.86554 | -64.89554 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c97c4264-a91d-3e78-b2f8-9d3c9c8392ea | -10.11998 | -65.02711 | 2024-11-16 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e882b048-dcef-3131-8ce8-d20cf45f2e85 | -8.99286 | -65.42371 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b45d5543-f443-3f1f-81d4-e551430868ef | -10.03025 | -64.21925 | 2024-11-16 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad80a89a-2887-3088-9bed-25d9a7de473f | -9.07625 | -65.85197 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 497a2b81-7959-3ead-8189-4e5dbb35c4f2 | -9.8888 | -63.94761 | 2024-11-16 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1499a810-48c5-37b1-a7ff-b0f5c7d102ce | -9.60615 | -66.18532 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a270674-8eab-394a-8159-15b512405ec2 | -9.07847 | -65.85944 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8667b175-a514-3f3b-9f86-73de04cac233 | -9.58291 | -66.3992 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 572516b1-30c7-35cb-9340-c8bc9e4f4294 | -7.93067 | -61.55642 | 2024-11-16 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c9a899c-e5f0-3b9e-836d-29d935258198 | -9.63757 | -67.23877 | 2024-11-16 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe819612-d98a-3020-9c98-c5e978d229a1 | -9.70321 | -66.97412 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2838e01a-ee05-3025-a648-c3ec1d079263 | -9.52995 | -66.64798 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b90f477-6c96-3e39-979d-2cf62acf8bb5 | -9.56062 | -66.64921 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a00af3b-eb21-3640-9ac1-bd397cafc760 | -9.64117 | -66.32993 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9537e903-5730-382c-aef7-c880ba7f44e7 | -10.12334 | -65.02764 | 2024-11-16 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5f43af39-d4d1-37cd-ac96-89ff13631f66 | -9.07294 | -65.85146 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be050cb2-a42b-388c-a9f5-c00d3861eb1d | -9.56338 | -66.65323 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4ba998d-8b3c-30b8-9ba2-a4da98e1d0ef | -9.81966 | -63.36031 | 2024-11-16 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4e7e9d5-b853-3c4e-8358-f1096ec475a1 | -10.12389 | -65.02403 | 2024-11-16 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 936f2742-3311-35d2-8e5f-b4545efd1690 | -9.45659 | -68.58504 | 2024-11-16 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 413c2ac0-1c56-3d25-b84f-2df363b911d2 | -9.63423 | -67.23824 | 2024-11-16 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86d98509-b7c4-3201-b297-c4a7a8ad28e1 | -9.0724 | -65.85492 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 634004a0-52e9-3e82-a0c6-22bea56a7aaa | -9.65076 | -65.74239 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c98b893a-5bf1-3cbd-9cb2-7947cbe2889a | -10.02969 | -64.22305 | 2024-11-16 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6377fce-6e7d-3e78-b0a3-a219d01f539c | -9.25318 | -63.62433 | 2024-11-16 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 808a1f57-63d6-3b6a-a901-b39a463e8bf2 | -9.06963 | -65.85093 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4855d990-f277-33af-82be-fbfa0a815d7a | -9.91021 | -64.04176 | 2024-11-16 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2d29c23-4d79-3aae-b684-a892d8017202 | -8.99618 | -65.42422 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 947cfbe7-aa28-3cea-ac16-dce0515f4ade | -9.90133 | -65.12634 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f58e5c7f-ee66-3627-9433-81858a7fe7fa | -9.92922 | -65.12335 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfe8d185-1710-3c5f-8294-6d8d556e438d | -9.08178 | -65.85996 | 2024-11-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d641b1f-6c51-3c5c-85d8-f6e29879afd8 | -9.5871 | -64.58086 | 2024-11-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 827a9de3-2bb6-3978-9e05-a0874afdd102 | -15.90115 | -59.25837 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 68a66ac5-2391-3fca-8a4d-5f13491d70f8 | -17.65955 | -57.54678 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 83f1ed17-9bae-37be-b92a-7a6c5e85221c | -17.25585 | -57.46212 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 838ae0b3-7248-3085-8f22-1a1c8066ae74 | -15.89584 | -59.26033 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README58.md)
