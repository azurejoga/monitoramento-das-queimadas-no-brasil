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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b45556be-ba61-37fc-abde-5a0de3d70467 | -4.38511 | -43.15433 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 716a4426-1995-39ca-91d2-88c1c5a36906 | -3.211 | -50.13677 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f23a709e-ba76-3685-8307-4390bb41ba79 | -4.37718 | -43.15853 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1b5afb38-53c7-3310-ad6c-db34801c7c19 | -6.31322 | -43.81214 | 2025-12-01 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6eda0d31-83aa-304b-ab91-b530da72f612 | -2.60102 | -49.2599 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbadf3ee-b154-354d-9949-8b27f6ccb0d3 | -3.71431 | -45.90493 | 2025-12-01 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db6620fb-49c9-322c-9857-cd1bce92a8cc | -4.14709 | -43.73226 | 2025-12-01 04:25:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71f21e0d-92b7-3eee-a6ab-0d4df96dd71e | -2.42579 | -45.73722 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c77993b-b870-3b26-bf15-7977ad9d2f53 | -2.24703 | -45.62078 | 2025-12-01 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75a86a11-ab79-3c90-b0fc-bc32467cd103 | -3.39335 | -50.25103 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7db8437-3942-3613-910c-a7128683cccb | -2.93439 | -53.28542 | 2025-12-01 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c180bb56-0564-33a1-ac0d-be21bbfcf24f | -3.44608 | -50.14863 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d71d2c7-30aa-3b68-904c-156fddb06785 | -4.39388 | -43.33326 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b5652105-4cde-3cfc-ac85-debc24511c9b | -2.74847 | -49.32737 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 466bfcfc-1aae-386d-939b-9986d2ce9877 | -2.24925 | -45.62816 | 2025-12-01 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcc62b0e-0c56-38ad-9f16-2e746dccaf49 | -3.60317 | -47.27212 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f08f7248-1977-30a5-b850-89bdc4aee7d2 | -6.08537 | -42.07754 | 2025-12-01 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 65ad42c4-a890-3be6-aa19-c75f8338a036 | -7.7364 | -44.18168 | 2025-12-01 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0c9a119-7f18-3223-83f8-ee6b4e4cf275 | -0.99037 | -53.20743 | 2025-12-01 04:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d999f4c3-1fc6-3332-bf73-4608545b65e6 | -3.89053 | -46.50943 | 2025-12-01 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f745626-d136-31f8-bfd1-633ee7aadc50 | -2.24392 | -46.5193 | 2025-12-01 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6b6eb4c-9871-39e0-8057-a30ff2643db1 | -2.35832 | -49.29918 | 2025-12-01 04:25:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32d18cf2-0d3f-3ceb-8ae3-c203a6646b68 | -5.87631 | -40.84019 | 2025-12-01 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 16447273-8f55-38c4-a93f-858b45693134 | -4.38337 | -43.33159 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 066f2ccd-5794-348c-a68f-d6328fc3f5cb | -3.57431 | -45.69628 | 2025-12-01 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8f7d887-3a3e-3e3e-a1e6-29f33ad3f489 | -3.38944 | -50.25037 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e6fc1aa-e864-3aec-a09c-266f0d394941 | -4.0909 | -44.85196 | 2025-12-01 04:25:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ff6702e-bf3b-3662-951a-948150696735 | -5.52086 | -42.5877 | 2025-12-01 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd696682-5d89-3c64-b56f-8d117e3ebfcd | -3.03752 | -50.23899 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f009046d-d9ad-37d4-8ded-79a533afa427 | -3.39676 | -50.20595 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03f9aef9-903d-38a5-9646-d2a76547a585 | -4.70061 | -44.40718 | 2025-12-01 04:25:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8cf3239f-88ac-3027-80de-4acfd1e8a8b4 | -1.68649 | -45.83598 | 2025-12-01 04:25:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 659ed30f-7625-3fc2-9018-5ec21c76cae6 | -3.10581 | -54.17637 | 2025-12-01 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d80d6f8f-0b97-3df4-9e7e-8357ac48d5cd | -4.36596 | -43.16087 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7107f79c-2054-33e2-ae44-646cd4b19aaa | -3.57423 | -50.30023 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b07d317-1b64-3ae0-89f1-20839e8e8dcd | -4.14306 | -43.73548 | 2025-12-01 04:25:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7a8fad8-7e88-3203-a150-068930fba5e9 | -3.14361 | -40.18182 | 2025-12-01 04:25:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 71400ba0-4e9e-3fdd-96e2-1aba868a4480 | -4.39328 | -43.33716 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16c6bcbe-60d3-3850-9bf7-f0365cadbdfc | -1.73898 | -46.87041 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b2a6d41-92b4-35ab-bb4c-06ae2a7c9fa9 | -4.37011 | -43.15746 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47d49e74-fe63-33f4-84ff-b3a02ec62d55 | -6.08155 | -42.07694 | 2025-12-01 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7efe7a47-5f65-3ac5-af9e-2175aeae5732 | -3.21409 | -50.14233 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e57f7a3-c240-399f-9385-42bcdfbaba02 | -3.21526 | -41.56616 | 2025-12-01 04:25:00 | NOAA-20 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 576f0885-9fe5-346c-9f51-2f235077d1f3 | -3.1957 | -45.23152 | 2025-12-01 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 876752b4-a259-3b76-bb98-04cf71ac63fb | -3.44528 | -50.15361 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79f5a1c2-3081-3ef0-821f-ee9ed62b03e5 | -2.24811 | -45.61391 | 2025-12-01 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68624e7b-6908-3e60-a8e1-b9f602c9267a | -2.84815 | -45.62421 | 2025-12-01 04:25:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0de4f605-5e20-3183-9d96-29e7a63dd9ee | -2.31305 | -53.85094 | 2025-12-01 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aad71cdf-3f2e-36fe-b702-ec342f92da32 | -4.40133 | -48.9208 | 2025-12-01 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52dc0d4c-23e6-37d4-b99b-340cd9382f62 | -3.03668 | -50.24404 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d32fbf4a-e87c-30d5-a4ca-8b3e074bb661 | -3.56631 | -47.17784 | 2025-12-01 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c849b950-0d88-32d6-81c0-6525df2e38ac | -4.36366 | -43.15239 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43efddf8-db98-347e-9a10-b046705c8dcc | -2.24757 | -45.61734 | 2025-12-01 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 251f8c89-7075-3e45-b386-2db0f996e10b | -3.47978 | -44.91453 | 2025-12-01 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 009a127d-ac5b-334f-8dfa-2e630cedb663 | -3.75335 | -42.9589 | 2025-12-01 04:25:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9191151e-c34b-30f5-852a-8034d51650c6 | -3.23718 | -50.24781 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a41309b1-d12a-320e-9d56-4cbcf7b31d37 | -4.38488 | -43.15563 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48688eae-5d80-32f3-93e8-3ee9df162097 | -3.57856 | -50.27359 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ba5d259-5ca7-3f25-846a-50a7e6668080 | -3.57461 | -50.29835 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95d5e2b2-32e2-3669-a779-66d3a8d8c6cf | -2.49008 | -47.82991 | 2025-12-01 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aed4acbe-be67-3bdf-8063-1533ff5c5639 | -2.63995 | -49.11226 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1abc1548-b0df-34fb-a4e6-b773ee3f9706 | -3.39127 | -50.11266 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a85ae77f-4161-3e16-ae4e-76f2d7161b3c | -3.57504 | -50.29535 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6d81411d-23c7-3e15-a269-d34bba045eac | -5.33128 | -43.56541 | 2025-12-01 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| c2d3b1c4-906d-33b1-a6ae-65b13d0afe9d | -7.73989 | -44.18221 | 2025-12-01 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d664a321-f04e-3b9c-b265-c4d4a6e8a10c | -3.79188 | -44.93776 | 2025-12-01 04:25:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b8c6011-10f6-3cfe-aff3-86d86e1ece33 | -3.71036 | -50.65241 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6456f602-8cd4-347b-99c8-dd2bc770be9f | -2.73527 | -45.21896 | 2025-12-01 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 43be5560-7e18-33c9-bf21-cf862302fd69 | -5.33479 | -43.5659 | 2025-12-01 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8a101e7-f75a-341d-b894-71adcd6b9df5 | -3.47749 | -51.36905 | 2025-12-01 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6ee435b-e07d-3a66-87fe-e8d32e1c3767 | -4.37135 | -43.14951 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9bc31106-faca-3cbf-b9bd-1cddd13f2abd | -3.59585 | -47.27462 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da3f7a45-c4b6-3540-a3ed-51fe391afffa | -2.74331 | -49.33572 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84ea7691-733e-3e34-b1b4-30b61fc691f5 | -5.5182 | -42.60513 | 2025-12-01 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 62b5ba7d-481d-3207-950d-e379a90a4a05 | -2.64385 | -48.54586 | 2025-12-01 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ac5b3b4-b85f-3a60-8a4d-d9facd0a7e9d | -5.48843 | -40.93116 | 2025-12-01 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 093b662e-8eab-3789-8e66-61d3b665bd2a | -3.70385 | -45.90681 | 2025-12-01 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87534d8f-2358-34f3-9cc7-49babde68cee | -1.24916 | -46.30248 | 2025-12-01 04:25:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ca70fd1-81dd-3c9e-a0d9-55d29dceb442 | -3.70824 | -45.90046 | 2025-12-01 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fb395401-7d5f-3e46-9452-d253d8339f95 | -3.60037 | -47.26794 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f5c6f86d-fc81-3a56-b896-3115d4cf3246 | -4.5975 | -45.21719 | 2025-12-01 04:25:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 254fa691-e76b-3729-b184-75fc9fcf8f75 | -4.38807 | -43.32435 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8790039-3429-3e4a-bd67-02badd89ba7e | -4.38747 | -43.32825 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 96bad724-2c14-3441-a138-425763f4541a | -4.3778 | -43.15457 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9d4dc8cd-50fa-3ed6-8bbb-9918ac5f6fa1 | -2.98626 | -52.62915 | 2025-12-01 04:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08969d7f-ced1-3a52-9307-318406555576 | -3.35667 | -50.49878 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e06f3666-fcfb-3a81-bafa-56bf0c1a6afd | -3.57777 | -50.27853 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e341fd7-2a69-3696-aa5e-fce0b68dfc89 | -3.3527 | -50.49812 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d97a8b52-0187-3083-b997-b8bd60e3b609 | -3.26587 | -48.57141 | 2025-12-01 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a4c68e9-d208-394f-a4ce-308bf1c30b00 | -3.597 | -47.26739 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ebbf6cd4-bb10-3856-9a0e-f36d04e316e4 | -4.1339 | -43.72639 | 2025-12-01 04:25:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0de7fbee-42fc-3c34-8827-559f50a3cb41 | -3.93725 | -45.84875 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1ed5f15d-3866-3336-80a4-ee06b2dec97c | -4.36304 | -43.15636 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5553b572-1f3f-3f74-948b-0e9e7354f853 | -2.39153 | -48.62722 | 2025-12-01 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75fe338d-6cdd-38dc-a813-c2dca9b23c8e | -4.3073 | -45.37755 | 2025-12-01 04:25:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e4dba1f-a67d-31e6-bd96-2c256b873d74 | -5.88047 | -40.84058 | 2025-12-01 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 72f397cd-2486-32c8-9560-9cd20afcf19c | -2.75612 | -45.26137 | 2025-12-01 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 822aa6ff-d2d2-328b-8fd7-8cdd9674fb10 | -5.33539 | -43.56198 | 2025-12-01 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af0bd257-beb1-3ea3-9ac0-56fba7f5f5d6 | -5.3603 | -43.02483 | 2025-12-01 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d603014e-4b26-3eb2-967b-1193fce65c1d | -6.99435 | -38.69556 | 2025-12-01 04:25:00 | NOAA-20 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README16.md)
