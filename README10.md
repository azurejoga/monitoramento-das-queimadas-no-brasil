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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63ba0aed-15e3-3e3b-8894-aa7302e8a4e8 | -11.65832 | -57.3805 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 8152ab2e-7861-3014-8c6b-1a01a8c31454 | -9.4424 | -68.94961 | 2025-09-02 01:49:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ebb761be-7cbb-32d2-8654-735f9477d554 | -8.66131 | -62.92945 | 2025-09-02 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bab8a6fd-1c88-3c08-856b-8d6e5b03579f | -7.67208 | -61.09487 | 2025-09-02 01:49:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 66cbd05a-e963-3b86-a326-1f0605e8513d | -7.7004 | -61.10497 | 2025-09-02 01:49:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 214af2ad-5d4b-3df7-9059-6bb034188150 | -7.60917 | -61.61745 | 2025-09-02 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 20c2465d-b7fc-34b0-965c-c183ab56964c | -12.62386 | -56.99928 | 2025-09-02 01:49:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| a4fd54e1-6550-3ec1-bc4a-5e7afbc7d408 | -9.85759 | -65.05319 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fa7692c7-acc8-34cb-8fed-c1c68be6378c | -12.42232 | -63.91116 | 2025-09-02 01:49:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e08a4f6d-91ab-32f2-b864-0a0baf0348b3 | -8.76611 | -61.4437 | 2025-09-02 01:49:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8d3cc4cb-a642-3340-be2c-ea7123a3aac5 | -12.9311 | -56.97956 | 2025-09-02 01:49:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ac24c701-bdda-37ad-bd1a-7e6437a16bad | -8.75869 | -62.42955 | 2025-09-02 01:49:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5389edc0-7c17-3e5f-b516-392029248c76 | -10.64089 | -69.03595 | 2025-09-02 01:49:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4f9adf26-aade-383f-a35b-fd1388a939de | -9.21085 | -67.5843 | 2025-09-02 01:49:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 811a2f70-b56c-32e6-b362-818c57556c7d | -9.87969 | -65.00918 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e2ffd0f9-885c-3ff8-9e47-f75d495d2d29 | -8.64167 | -63.26996 | 2025-09-02 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 077feaae-ad71-365e-8431-9a1b24e1f63b | -11.66518 | -57.38458 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| fdafeb6a-0e08-35ec-b0c6-5e04aa57ed72 | -8.64991 | -62.61996 | 2025-09-02 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| dea1a66b-65cd-3e64-ad51-ed126a4d32b6 | -7.48382 | -63.82827 | 2025-09-02 01:49:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fbea61c6-51ff-3ae5-8c3b-2660793596a3 | -7.55029 | -61.32102 | 2025-09-02 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 082ea587-7767-378a-ad16-ec9e3a625bad | -17.8815 | -47.161 | 2025-09-02 01:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 0a86b04c-6ed9-3866-ac8a-d357e2675591 | -5.6079 | -45.0265 | 2025-09-02 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 3696763b-4088-34c5-a99e-0ca37ff6b406 | -6.403 | -58.1979 | 2025-09-02 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b70b807e-ff7c-3824-80b4-727f9924f9a2 | -7.5476 | -61.3437 | 2025-09-02 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 167.6 |
| c161b1c4-90b0-368f-9ec3-3ea261c9e90c | -12.9197 | -56.9471 | 2025-09-02 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 8d05176b-2e6e-3dd0-94fc-17baf51fb9e3 | -8.5134 | -63.9175 | 2025-09-02 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 31d3ad7f-ca3e-3d0b-b6bf-c9b09b3a95fc | -9.1207 | -61.4864 | 2025-09-02 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| fae5acec-b4b9-386f-8edf-213b18f54bae | -3.2305 | -47.135 | 2025-09-02 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0bc84d5e-8a46-31fe-8744-8e1e0c3f659a | -15.5666 | -48.3469 | 2025-09-02 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e348d45a-6673-370a-abbb-5c703c9dbbee | -6.7909 | -52.8165 | 2025-09-02 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| d7e46bdf-3ffc-361b-9d80-b5f59ac76a54 | -10.062 | -48.1197 | 2025-09-02 01:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| a658dfd2-a677-3e16-a278-d2f71b4b5a05 | -7.5477 | -61.3247 | 2025-09-02 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 149.3 |
| aa49ce86-2ce1-3be2-8530-18fdccad1c75 | -17.7091 | -46.8962 | 2025-09-02 01:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e94fd3dc-ff7d-397d-9b6a-0c5589e5cce8 | -15.5661 | -48.3694 | 2025-09-02 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 12e71f98-c90a-30f0-8a6c-610aec3adf74 | -12.9382 | -56.9856 | 2025-09-02 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 98274cc1-d95e-3dce-8884-dc58f28a3042 | -6.4029 | -58.2173 | 2025-09-02 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| fa1d830f-40e2-3046-a4e7-ab2d49c42427 | -11.6647 | -57.3533 | 2025-09-02 01:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 74580f77-f735-3e79-be2d-1d9aed8d1739 | -10.0617 | -48.1417 | 2025-09-02 01:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 833ecbd1-05be-3041-b8f1-0e815b527f37 | -17.7096 | -46.873 | 2025-09-02 01:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 63812fc8-f4b6-33d2-88ae-59a229cfcd2f | -6.8095 | -52.8154 | 2025-09-02 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 3892cfb6-474c-3bb2-9e8c-da9c8a9edd43 | -6.8466 | -52.8132 | 2025-09-02 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| cf4ecb94-8c28-3661-8959-3e9d810fb4f7 | -8.9664 | -65.9796 | 2025-09-02 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 433995a7-f3a4-3bdc-adcb-76dab4fd469d | -6.8281 | -52.8143 | 2025-09-02 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a3fd3292-bbf3-325c-828d-44728885f3fc | -7.6783 | -61.0908 | 2025-09-02 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8315e466-617f-30e6-a4b0-caf79cdbba68 | -11.1033 | -44.6548 | 2025-09-02 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 707484fb-4d61-3bae-8fb5-f796ba646087 | -8.6673 | -62.8369 | 2025-09-02 01:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 80.2 |
| ea2b690d-9465-34f5-a80a-1de973463259 | -15.5852 | -48.3885 | 2025-09-02 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 38bf269e-8fa7-3bda-b981-49b30e906061 | -6.8279 | -52.8348 | 2025-09-02 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 36a48f44-9e0a-3ab4-9d63-e0933a443ee3 | -11.1037 | -44.6315 | 2025-09-02 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| af1381ef-4543-3f4a-b2c1-add63bc80616 | -15.5857 | -48.366 | 2025-09-02 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 763c1e2d-4ad0-3d4b-8cce-3072a453ab58 | -9.5913 | -40.3448 | 2025-09-02 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.9 |
| c1f5c428-192f-35d3-898c-3f9e58fbc4b1 | -5.6081 | -45.0038 | 2025-09-02 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 6f6aae6f-2a8e-385a-9924-6fae6dae78f8 | -17.9016 | -47.1569 | 2025-09-02 01:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 7b24eb92-7ee5-38cc-87a8-f320345a00ea | -15.5656 | -48.3918 | 2025-09-02 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| dc2af7c2-544d-34f7-974e-559922f57b3e | -5.6268 | -45.0025 | 2025-09-02 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 0a4e2d16-aab4-3cad-bff7-0f2bcb501baa | -6.8279 | -52.8348 | 2025-09-02 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7bbd71e7-f9d0-3c92-8326-6762f335209d | -15.5656 | -48.3918 | 2025-09-02 02:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f28ada77-6163-3601-b856-d6eba903ad3b | -12.9385 | -56.9655 | 2025-09-02 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 145bbfb0-94f1-33f2-aa31-4701e105fcb1 | -9.5908 | -40.3696 | 2025-09-02 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 5d9fc5a7-4949-380b-bd19-7cbc498b880b | -11.6647 | -57.3533 | 2025-09-02 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 5a38ddbc-8d6d-3e68-8f93-023ae6bd22d5 | -15.5666 | -48.3469 | 2025-09-02 02:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| aeecc00c-ea05-34fb-a770-6d07dc51f1ba | -7.5477 | -61.3247 | 2025-09-02 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 143.7 |
| ece262d0-64a6-3110-b826-c83994f70b29 | -6.1672 | -47.2858 | 2025-09-02 02:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 97284c03-5acf-324c-8e5f-b8eb5ae33360 | -10.0617 | -48.1417 | 2025-09-02 02:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 58b9b667-53cb-3e2f-99a2-7d8c817d23d9 | -11.6644 | -57.3733 | 2025-09-02 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e31fd346-82e4-3bf8-9797-673a14913fc4 | -5.6081 | -45.0038 | 2025-09-02 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 5749ca9d-e1ab-3463-94cb-72205ba6a6f1 | -9.5913 | -40.3448 | 2025-09-02 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 473.7 |
| 23e85015-92ca-3426-b41d-ad18779277c3 | -5.6079 | -45.0265 | 2025-09-02 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 1c80bde8-162b-3794-9f61-02cb7484d71c | -6.8281 | -52.8143 | 2025-09-02 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b77b1f4d-13f1-31e8-a13c-b932b85181fb | -6.8095 | -52.8154 | 2025-09-02 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 0bd82a83-e5e5-3442-8865-eae20a916d78 | -9.6104 | -40.342 | 2025-09-02 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 211.4 |
| cb0d56e7-f514-3517-a8c6-84acba522d60 | -9.5917 | -40.3199 | 2025-09-02 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.7 |
| ef868545-1948-372c-9cb5-31326df58f93 | -7.5476 | -61.3437 | 2025-09-02 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 131.2 |
| c4031095-2f92-3f87-8de3-4f385361bb7b | -11.1037 | -44.6315 | 2025-09-02 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| f31d9be3-8b5d-3d01-aa7a-c6b547a79e06 | -6.1859 | -47.2845 | 2025-09-02 02:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| eef5e3d9-5e15-3cc2-bde9-adc50d0d78ff | -12.9197 | -56.9471 | 2025-09-02 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0cacdaac-ba48-3f1d-89a4-e61cb35f3ec0 | -9.1207 | -61.4864 | 2025-09-02 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d0a2e7a0-c4f9-358d-a0a8-293b6a11137d | -17.7091 | -46.8962 | 2025-09-02 02:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 50406694-73e2-363f-9241-47e716c04cc9 | -7.6783 | -61.0908 | 2025-09-02 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 9f716a93-6cf2-362d-b0b7-ac07d78e237e | -12.9382 | -56.9856 | 2025-09-02 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 56e00ac5-6b31-326e-a9b1-3626c8bf37e6 | -6.4029 | -58.2173 | 2025-09-02 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9d103cc9-af8d-3ab9-90e7-ccfefc1ce7ed | -6.7909 | -52.8165 | 2025-09-02 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| ac860087-4c0d-3155-ac46-cf401b8042da | -17.9016 | -47.1569 | 2025-09-02 02:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 845684d2-4d52-39bb-b84a-821b376f7a74 | -17.7096 | -46.873 | 2025-09-02 02:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| c3268be1-6440-3950-9371-0e971abd47e1 | -6.403 | -58.1979 | 2025-09-02 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 9c452001-f022-334b-8d4e-aa240f304f4f | -15.5852 | -48.3885 | 2025-09-02 02:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 9f5bfe95-9548-31fe-bd35-46d28264ad40 | -8.6673 | -62.8369 | 2025-09-02 02:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d0f305cf-4921-3748-a287-3661e3e06251 | -15.5661 | -48.3694 | 2025-09-02 02:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 9cf462c8-209e-32a0-ab6a-7f16859416bf | -5.6268 | -45.0025 | 2025-09-02 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 12d4f27f-badb-3ead-8f1f-b74a44772f04 | -15.5857 | -48.366 | 2025-09-02 02:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 184.0 |
| aef4467c-617a-36c6-8143-3ae8f796303f | -11.1033 | -44.6548 | 2025-09-02 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| aa464c56-b848-35fd-83b7-bafc3f4f0479 | -3.2305 | -47.135 | 2025-09-02 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| d132b6a6-712d-3aaa-9619-c204be785680 | -6.8466 | -52.8132 | 2025-09-02 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 266781d6-ab37-3dbb-8e93-f17d05a0d0e1 | -6.7909 | -52.8165 | 2025-09-02 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| a7d19512-cacd-3144-b295-cd1efb34e51a | -3.2305 | -47.135 | 2025-09-02 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a95d81e0-1fc7-336c-a5ec-cf3f860d7de8 | -10.062 | -48.1197 | 2025-09-02 02:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| bf62fef3-6c87-323c-98f0-a24b62e34f9b | -15.5857 | -48.366 | 2025-09-02 02:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 51167def-5de1-353b-8a2a-258559e26729 | -15.5661 | -48.3694 | 2025-09-02 02:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 48332b37-eb7b-36f7-98e8-5cd4883f2f47 | -6.8095 | -52.8154 | 2025-09-02 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 0ed15c8b-21c1-3372-93c4-97988c72f94b | -11.6647 | -57.3533 | 2025-09-02 02:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |


[Clique aqui para ver as próximas entradas](README11.md)
