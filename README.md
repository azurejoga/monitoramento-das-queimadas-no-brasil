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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73645c69-6297-31f9-80ef-58e0f464bc97 | -2.1929 | -53.7234 | 2024-10-26 00:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 89f2f0ab-89e4-332f-8af4-9e1034232250 | -2.8739 | -53.3252 | 2024-10-26 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 54f56a09-9b58-3ed7-b50c-6a0b8aa21a34 | -2.874 | -53.3049 | 2024-10-26 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 2e835d81-ef85-3350-bf9c-8479f875950e | -2.8923 | -53.3247 | 2024-10-26 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 1cd58d70-7802-3a46-b471-57d58c6f6523 | -2.9501 | -52.5708 | 2024-10-26 00:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| e220dd1e-9b5b-31a7-a74c-f803ca7e0504 | -2.9578 | -50.4198 | 2024-10-26 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| b0cb2e7b-5dda-3e61-965c-d41800055236 | -3.0932 | -53.7239 | 2024-10-26 00:05:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| b7d28951-0aed-3568-9796-937cc395734b | -3.1116 | -53.7234 | 2024-10-26 00:05:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| f14ac0fa-a03e-3402-8e1d-a5f1cc4cee1d | -3.2368 | -45.8077 | 2024-10-26 00:05:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 0a501446-12af-357d-9bb9-d02d270b9c89 | -3.2553 | -45.807 | 2024-10-26 00:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 842c8513-44fe-3ebf-8a14-3f6b277fc22b | -3.4729 | -43.3377 | 2024-10-26 00:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 45a0a288-08f9-32ae-827b-53cc35a1fc3d | -3.473 | -43.3144 | 2024-10-26 00:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| a8999193-c9fd-3033-ae05-60049993848c | -3.4915 | -43.3368 | 2024-10-26 00:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 907b752d-6727-3c55-b610-407ea3c42fa7 | -3.4917 | -43.3136 | 2024-10-26 00:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c1824674-557b-3a87-b92a-afeda2101a56 | -3.5943 | -44.9833 | 2024-10-26 00:05:25 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 206.3 |
| e655c3b9-b0f1-388f-afec-49d5243ac623 | -3.5944 | -44.9606 | 2024-10-26 00:05:25 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 221.5 |
| e43d2151-9875-36aa-92ff-d9817798bee8 | -3.6129 | -44.9824 | 2024-10-26 00:05:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 150.5 |
| fa7b3727-043f-35ac-bf9d-fe208e72ce4c | -3.613 | -44.9598 | 2024-10-26 00:05:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 8c51dc99-bf66-330f-a681-e140f2ca20cd | -3.8981 | -41.0396 | 2024-10-26 00:05:27 | GOES-16 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 57.6 |
| 267a9b43-e102-31f0-b5bb-1b92364b9ee8 | -4.4842 | -42.91 | 2024-10-26 00:05:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 2f22e654-b308-3315-9a59-0ef9c5c53f11 | -4.4844 | -42.8866 | 2024-10-26 00:05:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0f2e4d23-acfc-3a03-8f40-3519fdc6122d | -4.2979 | -48.6523 | 2024-10-26 00:05:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 08fba7ed-41bb-3eb5-8047-a000a141f125 | -4.5613 | -48.0358 | 2024-10-26 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 355e5147-d73f-3e29-845c-2174b6079a8e | -4.5614 | -48.0141 | 2024-10-26 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 146.6 |
| c94569fc-4c49-3e3e-a62c-621c8fee819b | -4.5799 | -48.0349 | 2024-10-26 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 161.3 |
| c7752eae-59d0-36d9-aba8-5c1d429036b0 | -4.58 | -48.0132 | 2024-10-26 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 201.2 |
| 6755d017-edd4-35c9-822d-9a8fc3b1f7d1 | -4.9108 | -45.8598 | 2024-10-26 00:05:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 8a647a1b-05e3-3624-9012-3d43634a5c9b | -4.9295 | -45.8587 | 2024-10-26 00:05:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 10c051ea-b50d-31a8-b254-594566240893 | -5.7201 | -45.0186 | 2024-10-26 00:05:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 96f28ddd-820f-37e9-9dec-36ba150e26fa | -7.629 | -63.459 | 2024-10-26 00:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 6c18a87d-bad3-396e-b26c-c0cd3c45f610 | -7.6474 | -63.4584 | 2024-10-26 00:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| f045ddfa-94fb-38e2-b53a-49f5ec2cc7bb | -7.6475 | -63.4396 | 2024-10-26 00:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1805925c-f24a-36c0-98b7-6027bab708f6 | -7.6659 | -63.4578 | 2024-10-26 00:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| dc06d20e-79eb-3fde-ac70-5d29c0f2aad5 | -9.6072 | -42.9371 | 2024-10-26 00:05:59 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 8e27e4b9-f126-32d6-aef2-2a598c002ddf | -9.6075 | -42.9134 | 2024-10-26 00:05:59 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 09e1790f-851a-38f9-8375-46fbe1e637da | -9.4996 | -47.8068 | 2024-10-26 00:05:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 087c37c4-e2c0-3dd0-b26c-d49db8d20449 | -9.6346 | -47.5942 | 2024-10-26 00:06:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 5d1830d5-ca24-3f59-b2f6-33930d23783e | -10.3124 | -47.8057 | 2024-10-26 00:06:03 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| eff4d2db-61f7-324b-b1fc-556d011752ba | -10.3127 | -47.7836 | 2024-10-26 00:06:03 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 20b187de-268d-3c4b-b152-ad5c2fbd242c | -10.5806 | -45.1413 | 2024-10-26 00:06:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8c289573-820a-3ead-a093-5c93406daddf | -11.1671 | -56.2939 | 2024-10-26 00:06:09 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| e8b04daa-2699-33b9-86fe-6e25073475cd | -11.9471 | -44.5539 | 2024-10-26 00:06:12 | GOES-16 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 0c778001-2c57-3438-b28c-0ffc1400da6e | -12.0012 | -63.9013 | 2024-10-26 00:06:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| cf18901b-2ff6-3486-8eb0-39a689a2e337 | -12.4589 | -63.1895 | 2024-10-26 00:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 55026635-8bda-3de3-b536-1668f26ee177 | -12.4591 | -63.1704 | 2024-10-26 00:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1887ed33-de01-35d6-b4ce-67608eeec854 | -15.78 | -55.7129 | 2024-10-26 00:06:34 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 80f57eb5-cbac-342c-a933-d2f10dc606d5 | -16.9012 | -57.5108 | 2024-10-26 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.1 |
| c8ccf31d-b9fe-37e4-9d2f-64685ec4e171 | -17.0499 | -53.452 | 2024-10-26 00:06:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a8818152-cdaf-3170-8ef3-69fc94531a3c | -17.0593 | -57.4107 | 2024-10-26 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.3 |
| bd2363cf-4f00-314b-b4bd-6cdeb87f95d2 | -17.0596 | -57.3902 | 2024-10-26 00:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.4 |
| cb5723c0-7883-3175-8d31-22255f4dea06 | -17.0789 | -57.4085 | 2024-10-26 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.4 |
| ff4c1e21-0fbb-390c-941f-7612abec01d6 | -17.1987 | -57.2714 | 2024-10-26 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 14e6bd50-904c-3fc7-a4b0-69a80caf0ffa | -17.199 | -57.2509 | 2024-10-26 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| ee2f8844-1b33-3b55-ba78-98ef352d9b56 | -17.2183 | -57.2691 | 2024-10-26 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.8 |
| 2ee6042f-2f00-3020-b0e7-bffc02392dc6 | -17.2186 | -57.2485 | 2024-10-26 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 38838220-70a3-3f63-b4dd-2ad17310b8af | -17.219 | -57.228 | 2024-10-26 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.5 |
| 5d81613b-e6db-3f19-8a67-962bf5e86dc8 | -17.2344 | -57.4926 | 2024-10-26 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.3 |
| 189a1182-cae7-328c-93a6-b0ca5fb05825 | -17.2537 | -57.5108 | 2024-10-26 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| bf23378a-a730-3aa9-877b-23247aab410f | -17.254 | -57.4903 | 2024-10-26 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 7bb901a5-ac43-352f-8b13-bc48ec243068 | -17.2733 | -57.5085 | 2024-10-26 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.5 |
| b87dbda3-4384-388a-9396-086b4d4b5a86 | -17.6667 | -57.4822 | 2024-10-26 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| d9e4491f-fec2-3877-8f5c-45f5f3f281e8 | -17.6861 | -57.5004 | 2024-10-26 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| ca6bcd3c-a107-3ca1-9b1a-42f54ec522c0 | -17.6865 | -57.4798 | 2024-10-26 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 155.0 |
| 5292d51b-50ea-3024-9c4d-1773363a113e | -17.7062 | -57.4774 | 2024-10-26 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 44a98375-ded9-397e-b84e-671afa7fda48 | -17.7671 | -57.3673 | 2024-10-26 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 2632c4ef-e588-3f4c-be6e-51b3470e23a8 | -17.7674 | -57.3467 | 2024-10-26 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 4e42ef38-83ef-3879-8d7f-0a0a07453162 | -17.7868 | -57.3649 | 2024-10-26 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 292.1 |
| 631e15a6-8cc6-3788-91f4-5bda11d00e26 | -17.7872 | -57.3443 | 2024-10-26 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 175.5 |
| 2561b98c-7890-332e-9643-d020319618a6 | -17.8066 | -57.3625 | 2024-10-26 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 155.0 |
| 10804f91-db51-3259-967f-fddb1c6fa70b | -17.8069 | -57.3419 | 2024-10-26 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 399431ec-5063-3312-86e7-5776aac64796 | -18.065 | -57.2481 | 2024-10-26 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| b35d5352-e9e2-307c-b16e-3004e65a3a05 | -18.0653 | -57.2274 | 2024-10-26 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 38371a68-1db8-376e-bb2c-b8b28e7b077d | -18.1039 | -57.2845 | 2024-10-26 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.9 |
| d3daefcf-2196-3dcf-af14-635abbd43b6d | -18.1042 | -57.2638 | 2024-10-26 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 5b67f263-2dfa-3614-9139-9383f48f6652 | -19.6434 | -56.873 | 2024-10-26 00:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 9938beb6-e889-3760-8b53-2706384051f6 | -2.1929 | -53.7436 | 2024-10-26 00:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 3612414f-2f83-3d4b-8665-f4273e83b4a1 | -2.1929 | -53.7234 | 2024-10-26 00:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 0b587dc9-1b38-3552-96ed-58dc0c8cf797 | -2.8739 | -53.3252 | 2024-10-26 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 62d7acd3-fc42-3c89-9820-92f2ba530e67 | -2.874 | -53.3049 | 2024-10-26 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 80558bd3-745b-38dd-860d-57f8e5e366b7 | -2.8923 | -53.3247 | 2024-10-26 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 6defe47d-3d86-309a-ac0e-3cb0aca6b4b1 | -2.8924 | -53.3045 | 2024-10-26 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b50a1332-fb69-3cda-855a-9f44260fc7e1 | -2.9501 | -52.5708 | 2024-10-26 00:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c8069caa-785b-37a9-952d-cabf2b12dc73 | -2.9578 | -50.4198 | 2024-10-26 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 6f9d72b4-1f48-3b2e-b1be-275477005e15 | -2.9944 | -50.5025 | 2024-10-26 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| fa2fa7fd-cff0-3737-8a2f-1c0f8faed392 | -2.9945 | -50.4816 | 2024-10-26 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 242.4 |
| d716ad06-245e-32e9-be7c-09be79f77785 | -3.0129 | -50.502 | 2024-10-26 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 336e68c4-1a0e-31d3-bcb0-c76e66317332 | -3.013 | -50.481 | 2024-10-26 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 346.7 |
| fba8f49f-c6f7-3f22-a19b-b3ff634d6463 | -3.013 | -50.4601 | 2024-10-26 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 24f5cfb5-5594-3567-b6ec-608536af0f21 | -3.0314 | -50.4805 | 2024-10-26 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4a06307f-860a-3daf-9d63-61639a6cdefd | -3.0932 | -53.7239 | 2024-10-26 00:15:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 50875b14-af79-332a-a291-d19962843e7d | -3.1116 | -53.7234 | 2024-10-26 00:15:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 1ab1219e-e76b-3afb-885d-ea2f2efd42dd | -3.2368 | -45.8077 | 2024-10-26 00:15:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 86.8 |
| c40f74f9-4a1d-3681-8fef-8192423150ab | -3.2553 | -45.807 | 2024-10-26 00:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 3aa4ca78-40e7-303f-b12c-8c1708dad150 | -3.4729 | -43.3377 | 2024-10-26 00:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 9e620997-46c6-377f-8abe-9d9d870d7a1a | -3.473 | -43.3144 | 2024-10-26 00:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 00cafb71-4318-3de9-bc7f-e665ea8647f6 | -3.4915 | -43.3368 | 2024-10-26 00:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| b237f753-cc26-36d1-aac5-1c7ea5dfc7d4 | -3.4917 | -43.3136 | 2024-10-26 00:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 60a723f0-ea97-3f2f-abcb-5a46597024ce | -3.5943 | -44.9833 | 2024-10-26 00:15:25 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 3b273612-8d75-3da3-9ee8-60c7e61d3fd1 | -3.5944 | -44.9606 | 2024-10-26 00:15:25 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 6faf2979-6dc7-31f2-84ff-31fc43839afb | -3.6129 | -44.9824 | 2024-10-26 00:15:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 283.1 |


[Clique aqui para ver as próximas entradas](README2.md)
