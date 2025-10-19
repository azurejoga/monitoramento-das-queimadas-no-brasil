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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33c74403-db06-3b3b-b90d-db1fda26e012 | -3.52559 | -51.66526 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ab62e11-6176-376d-99a1-ffaedf99262f | -8.67241 | -66.87181 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a9e3e65-a56a-3003-a6ee-419808f4abfb | -9.96795 | -63.73205 | 2025-10-19 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a8f1609-fbf2-3d8b-8b4b-b23e0fd875b3 | -10.17342 | -63.06031 | 2025-10-19 05:23:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9a1c1f5-6bd2-3248-be8f-5eae25603395 | -9.90818 | -63.58401 | 2025-10-19 05:23:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7095d95-be95-3801-a774-c36cc6efb6bd | -4.29981 | -49.66245 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c94a6965-bf7d-3532-a275-4ed5dcf6183c | -2.86269 | -50.74321 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9204849e-0f22-30af-add3-390989577afc | -2.30542 | -56.96413 | 2025-10-19 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8791fcc-4c0e-3637-8d49-e514b5af8439 | -6.91222 | -59.26567 | 2025-10-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a88fbbab-c243-364b-a6ee-b19b82d5d6be | -3.82158 | -48.65294 | 2025-10-19 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 546ab1a4-6000-3d3a-bc0d-c8c249b92e78 | -3.15041 | -50.24683 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c20f1667-0402-3222-9e1a-4dfd939a05be | -9.72584 | -61.9294 | 2025-10-19 05:23:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1485b4b2-829a-3b2d-b4c1-1c516b916ba1 | -4.24764 | -48.56697 | 2025-10-19 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7e6a2f4-e7b2-34bc-8086-86a88583fa0c | -9.31103 | -61.84016 | 2025-10-19 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fc0198d-659e-3595-aec2-d3f10f46d5c8 | -2.92006 | -52.72227 | 2025-10-19 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7929af8e-d482-3f41-a884-8c1647808532 | -2.79031 | -49.66122 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88250f3c-db55-3847-b6ce-6659218da059 | -2.69363 | -49.54918 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 87f13240-718d-3769-8557-1f09124edd05 | -4.15944 | -51.09435 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44cedcbe-ffd0-366a-9b0e-6c94675eff1c | -2.81331 | -54.38518 | 2025-10-19 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 475aa21c-639e-34ba-9568-4212d848c0c0 | -9.90473 | -63.58345 | 2025-10-19 05:23:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d48ec58e-c429-38ca-ab51-80ce4e6b6ae2 | -3.13897 | -50.2486 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16b459b0-5a06-3ded-93c1-42c743182fbe | -3.04004 | -51.21027 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5ddc1f5-c5fe-3d55-bab5-332542c6160b | -11.6029 | -44.05109 | 2025-10-19 05:23:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5a3caae9-6cbd-33c7-93fc-26b4651f6485 | -9.85247 | -68.10968 | 2025-10-19 05:23:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9783255-8bb3-3e26-8995-3f02c2c0e352 | -4.96847 | -56.27271 | 2025-10-19 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1b1f240-16f9-33a0-92a0-8f9a21f96388 | -9.92294 | -64.08987 | 2025-10-19 05:23:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b7f0735-0618-3e00-97a8-550c721b78ba | -2.68793 | -49.54831 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5bfdf50b-e1fa-3b43-96e0-f5b400c0ef9f | -2.8694 | -50.73424 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 591a9f0a-e6b5-387e-b93e-d78028a925a2 | -2.69875 | -49.55395 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4e88f345-c6b8-31a6-926e-263a728661db | -9.11305 | -65.36609 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d849fb22-75d1-3e11-87db-222146b96053 | -9.82349 | -59.45452 | 2025-10-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f67cf0f-9f74-377a-b1ac-434725ef8346 | -10.04449 | -59.36133 | 2025-10-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfc8cbb8-e493-3bd8-8f8e-bdfc5b3d7405 | -10.92667 | -60.93116 | 2025-10-19 05:23:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51116c0d-25b9-36b3-a1fa-6f565533ea00 | -9.22884 | -65.73625 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1f6d952-e0a9-3fb1-b309-5e85aa02d8ed | -9.5547 | -66.64587 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1e56051-5934-363b-952e-36dfc1dad835 | -10.71994 | -44.53935 | 2025-10-19 05:23:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 840f150e-4302-3ea5-bd1f-6b617086cb8d | -3.10353 | -51.29562 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ff30021-257b-3c15-85c8-1f6c190266e6 | -7.19711 | -42.19514 | 2025-10-19 05:23:00 | AQUA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 05aaa861-557f-3b4e-a2d5-0bc30463622f | -9.29424 | -64.22483 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78825902-3317-3192-af76-48f020c023eb | -2.87086 | -50.72442 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b5f916a-9e3b-3333-ab60-93d90f6f3eb0 | -2.69818 | -49.55782 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 210181c9-9ee4-392e-82a8-28428bcb7969 | -6.52801 | -60.03592 | 2025-10-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 419b90c9-c3bc-3548-ac4f-e932d39295bd | -2.81833 | -58.29135 | 2025-10-19 05:23:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1823f233-3092-38d5-b66f-0ef8c4d567d1 | -2.66312 | -54.07555 | 2025-10-19 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40bdc1d9-d736-336c-bbf2-7fb7d2f7607b | -9.82009 | -59.45399 | 2025-10-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4d8a05f-df0f-3705-9368-4cad3a34ca40 | -5.09399 | -60.21931 | 2025-10-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 048a61f9-5c06-3550-8105-ee9078c6b931 | -4.22513 | -50.62688 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| efbf277e-17f0-34cb-93a0-264e8ff1f72c | -5.59904 | -50.05465 | 2025-10-19 05:23:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8621377e-1c4b-3180-a6b1-ea5765309429 | -5.10501 | -47.79987 | 2025-10-19 05:23:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f6892b37-6ecc-3e19-9582-c6a74c321c50 | -4.76265 | -50.69452 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a0f3242-9166-3a35-93a8-daf9266fdf1f | -6.67582 | -58.74756 | 2025-10-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 267744b0-6836-35a3-9606-44493d951295 | -4.22899 | -50.62514 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fee2c7f-a1ab-3cc5-bcb8-68ffa674e01f | -4.14311 | -47.65769 | 2025-10-19 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f56089cc-98fe-3162-aea3-71f6f01242fa | -1.9513 | -56.60819 | 2025-10-19 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6fd00aa-a768-33d0-99e5-e40ab2c9712c | -9.22747 | -61.83044 | 2025-10-19 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abbda9b9-c6e9-32be-aa11-02b2e1efcfba | -2.30677 | -56.96317 | 2025-10-19 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aae2c13-a500-3591-b3de-7bdbee852d0a | -7.0399 | -43.93781 | 2025-10-19 05:23:00 | AQUA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 206c402f-bfda-35bc-826f-9bcc0e165e04 | -2.85838 | -50.73584 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddec0462-5583-338d-aea8-8f9c31f8bef7 | -2.69306 | -49.55307 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a277a104-77af-3be1-a356-d9b52b3af8d9 | -8.67311 | -66.86783 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfb84a6c-a18a-3aee-95d8-2c2726e6ffbe | -3.80475 | -51.65085 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c61cd0c2-5cd6-3b62-b780-d16761c87a22 | -9.52153 | -62.03652 | 2025-10-19 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 012d26c5-debe-3542-8868-cd1bc703b7a0 | -3.71946 | -57.27275 | 2025-10-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dbe6bcc-af4a-338f-9262-5ce593e15810 | -8.42692 | -44.14069 | 2025-10-19 05:23:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8444293c-7d76-34c7-b9df-a06818ca748f | -9.58786 | -63.50072 | 2025-10-19 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d979573-886a-37bf-b2ce-975b010b0d64 | -10.45406 | -45.01183 | 2025-10-19 05:23:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0306cc44-8919-39dd-9fe6-affdf09ad7a1 | -3.86144 | -49.81817 | 2025-10-19 05:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c084388-96c4-390a-a5f1-c8046b36dde7 | -5.23804 | -50.95016 | 2025-10-19 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05d55579-aa1b-3822-8d38-7ddba570cd1d | -9.11158 | -64.42382 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b01a643f-af83-3ee5-8867-2048918867da | -4.22848 | -50.6286 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 338e1038-7f91-3680-8d0e-6b4b43a7b9ed | -3.14495 | -50.24596 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6052f7c6-c85a-3df5-b1d8-3c746487fdbc | -2.87182 | -50.71792 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23de606c-2972-311a-a547-336d2bfee759 | -6.91277 | -59.2621 | 2025-10-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 809151f6-603c-3d49-a195-f8741e3438e7 | -9.91875 | -64.09328 | 2025-10-19 05:23:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78caf27d-ca27-3500-a1a5-cfa0266ce6e6 | -3.14443 | -50.24948 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a626af7-ad37-301d-9299-add46e5ad741 | -9.18123 | -62.4586 | 2025-10-19 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c397c60e-4b58-3cd2-b2c8-aab1c286ea32 | -2.70415 | -49.86725 | 2025-10-19 05:23:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2338a020-1cf0-3ed3-b325-550413cd7291 | -2.32384 | -57.10899 | 2025-10-19 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e141c9a2-f81d-35ed-95fb-42d0eebf0dd9 | -3.39628 | -54.06406 | 2025-10-19 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f64ac146-2989-3d60-8284-d08b9218e359 | -9.17896 | -62.45843 | 2025-10-19 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa2023e4-28a9-3819-a28b-86c4c3527888 | -9.2656 | -62.46848 | 2025-10-19 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8387454-b074-3f25-a475-576ed0f4beff | -10.87852 | -46.08035 | 2025-10-19 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 86047e12-272e-35f3-9974-7eac00574746 | -10.04393 | -59.36507 | 2025-10-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71d2334e-f7fa-3123-8c3b-8f3f5ab95ace | -3.82261 | -51.70374 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e17330f3-86bc-3105-a0c1-6c4d3ac93452 | -6.24773 | -57.77761 | 2025-10-19 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f8b12e0-37db-3bad-9e93-8ae0d7754bf0 | -2.70616 | -49.54311 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75c57d47-96c7-3f14-a306-63b1b5a7578d | -6.53185 | -60.03296 | 2025-10-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4b9529a-b066-3a5b-bffb-755eef792e6e | -4.30583 | -48.06134 | 2025-10-19 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 29e83c3d-8f3d-35ab-b77b-bb8ad7944219 | -8.42862 | -44.14627 | 2025-10-19 05:23:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ae8c22d5-29a7-3694-946e-28d746b22e6e | -10.21975 | -44.0513 | 2025-10-19 05:23:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d6ebe842-15c4-3200-aa6c-b546ce9ce79f | -8.60696 | -40.18549 | 2025-10-19 05:23:00 | AQUA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 45.9 |
| 1c26b4b3-7168-3895-b6d0-f4dc63c4c65f | -6.52855 | -60.03244 | 2025-10-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae08f79f-c48e-3023-9f9c-efcd85ddfcf7 | -9.64133 | -65.25331 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d67092d9-d1cb-3bc9-9e6d-c0055ab4af28 | -3.1273 | -50.21331 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 433c96df-ec78-3285-8e9f-b912ecdd68fe | -9.38313 | -68.32732 | 2025-10-19 05:23:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d965d4a5-c996-35b8-9d1a-4579f9b66bf0 | -5.14558 | -56.07505 | 2025-10-19 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afac4e89-e088-3b46-940e-d1959223db9b | -5.36151 | -47.20971 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ceb08689-f123-34a4-8123-98475b72f9e5 | -9.59476 | -63.50188 | 2025-10-19 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 135529e4-1d34-38ef-971c-87e4bda902a1 | -4.96982 | -56.2637 | 2025-10-19 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e33e5790-2851-3928-919e-4af2eab77400 | -4.96232 | -56.26256 | 2025-10-19 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README57.md)
