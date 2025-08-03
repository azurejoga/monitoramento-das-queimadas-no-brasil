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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79c940f2-ba7b-3b67-a04e-c03993faa8bf | -9.462 | -57.8302 | 2025-08-03 01:08:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2da7ffc1-47ca-307e-940b-75deca37a6c0 | -6.6516 | -59.103802 | 2025-08-03 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 699ac139-3823-323b-a757-fd51d3a68aaa | -23.7143 | -51.648499 | 2025-08-03 01:08:00 | METOP-C | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79ba6838-7476-3a2b-8981-5c6289c90130 | -4.3256 | -48.116299 | 2025-08-03 01:08:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa02010f-060a-3bd6-8205-185a743fca89 | -8.0148 | -43.178902 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e04e4d3e-eb05-3285-9f7e-9a742aa89cfa | -21.313299 | -48.563 | 2025-08-03 01:08:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bd79fbd4-ba74-396b-8659-f77aab1dffcb | -10.4717 | -50.2784 | 2025-08-03 01:08:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0759ce7-1045-3a91-b67b-6bb75f217d73 | -24.2246 | -51.868801 | 2025-08-03 01:08:00 | METOP-C | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11dd8439-13fe-3320-b93b-2e795f31dd39 | -6.6535 | -59.112598 | 2025-08-03 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fae80f29-d2ed-36fc-85da-94c32f74e083 | -8.0355 | -43.1409 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72e5a553-51df-371c-a101-d6ff464abc9c | -27.1689 | -51.2043 | 2025-08-03 01:08:00 | METOP-C | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2e1c5b0f-bd0f-31b7-ac8d-e6bea6f3ed55 | -21.4569 | -55.097801 | 2025-08-03 01:08:00 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8a953ff0-b1f8-36e6-a4e1-eb6354e4205f | -10.4619 | -50.2808 | 2025-08-03 01:08:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79038fa2-bc63-3d04-9d75-863bd19229fa | -21.712999 | -47.690701 | 2025-08-03 01:08:00 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b2f50045-d3fd-3c5d-bea8-1949a97fa0f0 | -6.7379 | -59.168999 | 2025-08-03 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b96867b9-846d-3fcb-b27a-985290dd1918 | -8.9438 | -46.734402 | 2025-08-03 01:08:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 403acaa8-18df-3c33-b3cf-1672768fd24c | -6.6751 | -59.163898 | 2025-08-03 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45167299-7d4f-3e0c-a765-4b5a1dfd7927 | -8.0067 | -43.148499 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f86be58b-358d-3eec-a431-82ccf7de90cd | -8.0323 | -43.206699 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1e7ec03e-270d-3294-988c-daa3e61570c0 | -4.5836 | -44.2216 | 2025-08-03 01:08:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4530f069-e6e7-32d7-aabe-c5ee349cbb9d | -4.3217 | -48.1003 | 2025-08-03 01:08:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5930d491-8666-3a77-ab0f-525a1166eb3a | -12.6402 | -44.4913 | 2025-08-03 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| d606c2cd-ee91-35dd-a6fd-4ce03ef998bd | -6.6376 | -59.0988 | 2025-08-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 90af2c97-efe3-3474-9e48-dcc968c97667 | -6.6375 | -59.1181 | 2025-08-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 15ec6ba9-f3dc-3eeb-b6da-4e2aa71e5e34 | -6.656 | -59.0981 | 2025-08-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.7 |
| e195eb90-28aa-30c3-998a-f405971a6d00 | -6.6741 | -59.1746 | 2025-08-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 15a0a926-4e02-3d76-914f-ec7ef7b7c780 | -12.6398 | -44.5148 | 2025-08-03 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| cf82c155-cf6d-3d0d-99a3-05a1c8a87d3f | -12.6209 | -44.4945 | 2025-08-03 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 00c915b5-11e6-3b18-8a1e-d8a3fd41110d | -6.6559 | -59.1174 | 2025-08-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 7b5e0edc-454d-30ac-83a2-3b6644303360 | -18.8407 | -46.4417 | 2025-08-03 01:10:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 93.3 |
| b365a9ef-8cd5-3702-b309-a1be604ada2f | -12.6591 | -44.5117 | 2025-08-03 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| f4fbbed1-7e57-306e-a7d0-22294b5742f6 | -6.6742 | -59.1553 | 2025-08-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b5322ddb-d50b-3e85-b9c2-11a119148f26 | -4.5684 | -44.2036 | 2025-08-03 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 2c479488-c2d6-39e6-900a-7bcaa56a0c5d | -12.6595 | -44.4882 | 2025-08-03 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 0c32cefb-6c68-3d56-b64b-35a681b2828c | -4.3196 | -48.1125 | 2025-08-03 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| aa734b22-8b45-3701-bc97-b79e9e9adbf8 | -12.6789 | -44.4851 | 2025-08-03 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 093c718d-df2d-3629-9d18-52b9e3cb4b9f | -6.6559 | -59.1174 | 2025-08-03 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| fbbce82c-4bbd-37e7-88f9-5e15346b8cc1 | -12.6789 | -44.4851 | 2025-08-03 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ebebcb85-ecde-3ac0-a326-63b4825721ba | -4.5497 | -44.2047 | 2025-08-03 01:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 7257da8e-331e-38d0-89b2-b0f067626900 | -12.6595 | -44.4882 | 2025-08-03 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| f9dc0402-c71e-3b2d-9c04-3e681862ac8b | -6.6375 | -59.1181 | 2025-08-03 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f507c9e2-5479-316e-9463-1229540be395 | -12.6402 | -44.4913 | 2025-08-03 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| fbe86ede-ca27-3ae9-9ab0-1aa90aa8b6c4 | -6.6329 | -59.9649 | 2025-08-03 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 4603b9cd-a3a3-3830-8091-0b2495788152 | -12.6591 | -44.5117 | 2025-08-03 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1320d8c0-828c-38b4-8c5d-36a8542f5195 | -18.8407 | -46.4417 | 2025-08-03 01:20:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 54d18df3-e9de-379f-b568-9be562a4f7f1 | -4.5684 | -44.2036 | 2025-08-03 01:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 6b591125-c2cb-39e9-96de-ad6b064f7e98 | -6.656 | -59.0981 | 2025-08-03 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| a7c008c0-34de-3618-aefb-4b3c2d1fff31 | -6.6741 | -59.1746 | 2025-08-03 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 85085d01-b8b5-3506-8b5c-67a83f1271aa | -6.6144 | -59.9656 | 2025-08-03 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9f0bc838-9a5f-3d26-afc8-fc983999a127 | -12.6209 | -44.4945 | 2025-08-03 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| e21a0a26-5b7d-3ada-8b1d-778b9bbb4c7f | -6.6376 | -59.0988 | 2025-08-03 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 305404cf-6153-3c61-909a-2e1769fc8c90 | -12.6398 | -44.5148 | 2025-08-03 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ca8feae8-6c69-39af-b1dd-51e53fa9d5e4 | -12.6595 | -44.4882 | 2025-08-03 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 69135ddf-7c56-37c0-8dc0-88264d5ff376 | -21.7152 | -47.7101 | 2025-08-03 01:30:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 5190f4e0-4e9e-311d-bef3-ddb9cf8abe27 | -21.7159 | -47.6864 | 2025-08-03 01:30:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 773653dc-7496-33e1-aa91-54acea7fd21f | -15.5513 | -54.2674 | 2025-08-03 01:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e5c3ecd9-59cd-3c0b-b9b8-6d80ef3d6f5f | -6.6559 | -59.1174 | 2025-08-03 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 9635688b-5004-3b10-8288-4ac466814e23 | -15.551 | -54.2883 | 2025-08-03 01:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 477b8a12-8955-3339-9156-b2aceccdc06d | -4.5684 | -44.2036 | 2025-08-03 01:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 64178b5f-34b4-3f9c-aaab-a852bda87107 | -12.6402 | -44.4913 | 2025-08-03 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 0ddcace6-261d-3323-8ea7-b164404e2f4a | -6.6145 | -59.9464 | 2025-08-03 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 37d11f0f-c48c-3c7f-803c-1b3ccd562776 | -6.6741 | -59.1746 | 2025-08-03 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 78c5543d-a0e4-379c-af6b-693c5a624210 | -12.6591 | -44.5117 | 2025-08-03 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 35c99650-6665-3a95-be5a-87f45e1acd87 | -6.6144 | -59.9656 | 2025-08-03 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7c3a7666-6942-3504-973d-69cdd2592367 | -18.8407 | -46.4417 | 2025-08-03 01:30:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 882b3e92-f87b-39c4-b181-4ed7e5ebdd3a | -6.6376 | -59.0988 | 2025-08-03 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 66bc7f16-8f16-336b-9e44-30f6920c6530 | -6.6742 | -59.1553 | 2025-08-03 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 2502b63f-e626-3beb-bbe0-4c0ff6a717fa | -6.656 | -59.0981 | 2025-08-03 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 1815af05-517f-3efa-8ff1-12f43fcae833 | -6.6375 | -59.1181 | 2025-08-03 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 27f9c2de-b6df-3810-81cb-3384934a5d54 | -12.6789 | -44.4851 | 2025-08-03 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| d0f5c927-80b9-3d07-8f60-089db0f6073c | -12.6209 | -44.4945 | 2025-08-03 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| bd1dddc6-d3e9-3e72-977d-3807ac500d54 | -6.633 | -59.9457 | 2025-08-03 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cc5b0b5e-f683-30b2-b3e4-cdeb1956a682 | -12.6398 | -44.5148 | 2025-08-03 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ee9fc8ef-ae97-3a00-bd1a-d0001ac08b58 | -4.5497 | -44.2047 | 2025-08-03 01:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| fcd963d9-e316-37d9-82b8-4936509bd0c5 | -6.6329 | -59.9649 | 2025-08-03 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 73b5dbd9-68b0-35a4-80a5-cf795598a1f4 | -6.6741 | -59.1746 | 2025-08-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 310dc806-f270-3b74-9b6c-00377473ce25 | -6.6144 | -59.9656 | 2025-08-03 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 98f91903-b97a-3f9b-9a15-9e32e37dd80e | -6.6375 | -59.1181 | 2025-08-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 343db4aa-5100-3efe-8946-e1c6af57ef24 | -6.6376 | -59.0988 | 2025-08-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b53cdfa5-59a4-387a-bc9f-7c1f3d6752e8 | -6.6329 | -59.9649 | 2025-08-03 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 88242dae-2141-3992-98e7-cefd43323e64 | -6.6559 | -59.1174 | 2025-08-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| a8869252-f9a4-3c0b-9e44-2dfb0b67c48d | -6.656 | -59.0981 | 2025-08-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| f0e081fe-0e0e-397a-8e48-0439573de9d1 | -12.6398 | -44.5148 | 2025-08-03 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| faf1f1fe-ecc1-323c-95a4-44bacc81db65 | -12.6591 | -44.5117 | 2025-08-03 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 82089891-15fd-3ea0-b395-3cff5f9822d7 | -7.0208 | -59.8346 | 2025-08-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 38c79670-9071-3515-8114-5123e932b8dc | -18.8407 | -46.4417 | 2025-08-03 01:40:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 14b860fe-948b-3692-95e8-7fed9ddd5535 | -6.6145 | -59.9464 | 2025-08-03 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c855ac49-c5c9-33c9-81bb-9bb76684b36b | -6.633 | -59.9457 | 2025-08-03 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 082d3b5e-1c56-370c-86ea-07e1e983af4e | -12.6402 | -44.4913 | 2025-08-03 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 6ba1ad08-3b64-3234-89d2-64855b7cdf67 | -12.6789 | -44.4851 | 2025-08-03 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8cd1b565-84e2-3b80-ab4c-e4ce8a37b9fa | -7.0391 | -59.8531 | 2025-08-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 1ec192dd-e93a-3a21-9fe3-0b14de2686ed | -12.6595 | -44.4882 | 2025-08-03 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| c956c0e6-efe2-3edc-9342-935ab7bcdcc2 | -4.5684 | -44.2036 | 2025-08-03 01:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 9c07ffdf-abc9-358f-9d1d-5fb72f24ec65 | -6.64389 | -59.10067 | 2025-08-03 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 9444157c-edf4-3ada-a5ac-254061c3503e | -6.65109 | -59.10615 | 2025-08-03 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| e96c0006-279d-30ab-ab41-37f5889c395a | -7.02226 | -59.83453 | 2025-08-03 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ca37b426-623d-3ab5-abf0-3a8eb8f91cd8 | -6.64759 | -59.12395 | 2025-08-03 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| eeac799b-e3ae-3116-946e-be120a7c312a | -6.6328 | -59.9462 | 2025-08-03 01:47:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 81e91d51-0a93-3643-bd09-8855a954e0c1 | -6.61999 | -59.9482 | 2025-08-03 01:47:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 1e9fa241-a711-31f4-9ddd-6a779cd84304 | -6.62304 | -59.96798 | 2025-08-03 01:47:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |


[Clique aqui para ver as próximas entradas](README7.md)
