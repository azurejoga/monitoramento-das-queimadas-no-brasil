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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 265e268e-bf68-3047-8349-dfffc286854a | -6.1229 | -43.9578 | 2024-12-03 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 1ffab195-0ac6-3b1b-9205-61227824ba0c | -3.272 | -50.3263 | 2024-12-03 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 17e20d44-ed3c-31ca-a11e-9c6275b7c4d0 | -1.0919 | -53.4359 | 2024-12-03 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 626f19ae-5a14-3405-9744-ff4aea40cba0 | -3.5681 | -50.1903 | 2024-12-03 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 90244ec8-86e6-337c-8538-b651eaeb21ed | -2.8012 | -53.0633 | 2024-12-03 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| fd9a5512-f7cd-32b8-b765-fe0e3fa15a37 | -5.1554 | -43.2172 | 2024-12-03 00:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 582a0454-16f1-3f47-b6c9-5429264b6d08 | -5.8009 | -46.4941 | 2024-12-03 00:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 3e65bbe0-a336-3684-8cde-8ae16f19495c | -1.7361 | -52.6162 | 2024-12-03 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| cf060336-5958-33c9-b105-a3e18a96a8fc | -3.259 | -53.659 | 2024-12-03 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 91097082-f935-3315-8805-37da82546c61 | -9.7553 | -36.3983 | 2024-12-03 00:50:00 | GOES-16 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| 0848e4df-26c5-366c-90ac-d4d218e6c731 | -5.1181 | -43.1964 | 2024-12-03 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 68e4d4c2-794f-37e4-b182-a324a461e0d6 | -4.5591 | -42.9054 | 2024-12-03 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| eec11cd6-866d-38c6-885e-25e3b2bcf79c | -5.8197 | -46.4706 | 2024-12-03 00:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 07b3e438-de59-3e18-9b51-ef362e3554b0 | -3.1133 | -53.2381 | 2024-12-03 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 31380950-b60e-336e-85d3-01a55e430999 | -5.8195 | -46.4929 | 2024-12-03 00:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2ec31e35-07bc-312a-afd1-3a223cb96541 | -3.2406 | -53.6595 | 2024-12-03 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| f3b3bf98-d171-3f86-847f-42653c03d89b | -1.0736 | -53.436 | 2024-12-03 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 3c5aefcd-a06d-3867-b3b4-3536a29abfa1 | -3.259 | -53.6388 | 2024-12-03 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| b69450f0-3b27-3d7f-96aa-0b09754e1c3c | -3.076 | -53.3808 | 2024-12-03 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 199.2 |
| 799e8307-e70f-3ee3-bce5-768e3c6630fa | -3.0945 | -53.3601 | 2024-12-03 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 7abcc5db-1a27-39ef-a10a-33441d21a1b3 | -9.374 | -57.5553 | 2024-12-03 00:50:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 37bce31f-3ae6-326e-a22b-7e7e22d2a3c0 | -1.0919 | -53.4561 | 2024-12-03 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 203.4 |
| e89d5f65-179c-35a3-aecf-01f437d83b01 | -9.736 | -36.4017 | 2024-12-03 00:50:00 | GOES-16 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 156.7 |
| f7c773c9-4740-32a9-a4f6-69ff58a67544 | -5.118 | -43.2198 | 2024-12-03 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 97c4f9a9-486b-3976-9617-d7962a01c3a3 | -3.1831 | -54.3247 | 2024-12-03 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| cd7ebbb5-fe8c-33c9-82cd-0ff2d5c15f7e | -4.5589 | -42.9289 | 2024-12-03 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 2c7fbf04-6cd3-3895-8ee7-a26101b9a0f2 | -3.5496 | -50.191 | 2024-12-03 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 61fdcdb6-fcdd-3e39-a704-aa5507c6fcc1 | -1.7541 | -52.7993 | 2024-12-03 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 897f3ecf-8676-3a28-9875-43c40764f7d9 | -4.0477 | -54.2394 | 2024-12-03 00:50:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ddaa496e-7500-3ad4-8a02-9ee83deb05d0 | -5.1367 | -43.2185 | 2024-12-03 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0074b9a7-0726-30be-a109-256078cb877c | -2.3459 | -45.7036 | 2024-12-03 00:50:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 722b34de-c503-3dca-8aa3-a9fbef67a1ad | -1.3283 | -54.9964 | 2024-12-03 00:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c3a90711-d8b3-3e17-9877-cde88f9d1fcf | -1.7361 | -52.6366 | 2024-12-03 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 3227c619-3567-33dd-938a-ab9aadc75155 | -3.0949 | -53.2385 | 2024-12-03 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 101feca5-8770-30d3-8475-4cd24344d85f | -3.0192 | -53.8668 | 2024-12-03 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 3ee3da39-b27a-3441-9f66-33f3f885c9cb | -1.0919 | -53.4762 | 2024-12-03 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| df8c36c2-d433-3bd4-9427-0662fb7f94c4 | -1.0736 | -53.436 | 2024-12-03 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| dc7bc0b2-02f4-33bb-b4b3-7e1e6d424ea0 | -1.0735 | -53.4562 | 2024-12-03 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 242.4 |
| 5f604117-4961-3a38-b509-f6b9595bd7d0 | -3.5496 | -50.191 | 2024-12-03 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| ee889663-f7b0-33dd-946e-0d3b31c68b2e | -2.8013 | -53.043 | 2024-12-03 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e51b633b-a64c-33ae-b7b4-b63c49b69b60 | -3.0376 | -53.8664 | 2024-12-03 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 974e0754-a10b-3e3d-b15f-abd70fbf48e4 | -2.3645 | -45.7031 | 2024-12-03 01:00:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 3523a01b-504b-364b-a812-bd237d10773f | -4.5589 | -42.9289 | 2024-12-03 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 552c818b-bef7-300c-b9df-c671ff6233f4 | -3.259 | -53.6388 | 2024-12-03 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 851a4015-0f05-353d-9641-abe7e7ff4df0 | -1.7541 | -52.7789 | 2024-12-03 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 3e866db6-c174-3c1b-b535-7d6344d33dc2 | -3.2774 | -53.6383 | 2024-12-03 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a80b860a-57f2-33da-9b5c-657436536222 | -5.8009 | -46.4941 | 2024-12-03 01:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| f2d7ec19-8eb4-3971-a6d0-4a01cee49f9b | -1.7361 | -52.6162 | 2024-12-03 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 65696bad-9f91-3cfe-b8e2-063757e995d8 | -3.5681 | -50.1903 | 2024-12-03 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 8c45827e-6fc0-3244-a169-78cbff5ea69b | -4.5591 | -42.9054 | 2024-12-03 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 84be8b0a-7afb-301b-ac92-460863eb4c97 | -1.0919 | -53.4561 | 2024-12-03 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 180.7 |
| e04e82cb-eeb4-3da0-b78e-e6a07aa4b899 | -5.8197 | -46.4706 | 2024-12-03 01:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 8ab0fc0c-61db-3b01-b2b9-67ee469583e1 | -3.1133 | -53.2381 | 2024-12-03 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6ce25934-9b04-3147-911c-f839e4264368 | -1.736 | -52.657 | 2024-12-03 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7e1b9bfc-fc91-3083-b803-4281cbea5f0c | -3.1831 | -54.3247 | 2024-12-03 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c9697f10-2b4c-3a56-88db-0a4a2eb38fae | -3.0945 | -53.3601 | 2024-12-03 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 73544834-103b-3fb3-b70a-1b140af8ef2a | -5.801 | -46.4719 | 2024-12-03 01:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| c20553cb-68fd-3ef6-8846-17c2bf72d68f | -3.0761 | -53.3606 | 2024-12-03 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a0973cc2-2711-3763-bbbf-abfa52c95ce1 | -2.8212 | -52.5945 | 2024-12-03 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0846809a-d9f5-3401-8fea-80fa139f3fd3 | -3.0944 | -53.3804 | 2024-12-03 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 200.0 |
| 14affb0b-9f69-3b1b-b40f-7d2a66a45679 | -1.0735 | -53.4764 | 2024-12-03 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e909000a-ab9c-3fc7-8467-1a4222cec408 | -3.0949 | -53.2385 | 2024-12-03 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 59916ea4-e6e8-3219-ab57-5f1c666477be | -5.8195 | -46.4929 | 2024-12-03 01:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 1014d250-fb10-3c80-8f89-2c833d1b025c | -1.7361 | -52.6366 | 2024-12-03 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| eae33953-2501-3ec4-9ead-9899308a7007 | -2.8012 | -53.0633 | 2024-12-03 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 8939b372-067a-30d9-b3ba-068b84cbf095 | -3.3422 | -51.2007 | 2024-12-03 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 8a635768-edbe-3315-a49c-423dbc740aca | -4.5402 | -42.93 | 2024-12-03 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 3f0795f5-894b-3e11-ab98-321e8c6e91ef | -3.2591 | -53.6186 | 2024-12-03 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 201ffad8-c4d3-3ce0-9d38-009c98b37b7f | -2.3459 | -45.7036 | 2024-12-03 01:00:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c0b3f852-4f18-3bc8-8764-d638d6d3867b | -2.8196 | -53.0629 | 2024-12-03 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 92e34506-7121-31d1-843b-449300b665b2 | -1.0919 | -53.4359 | 2024-12-03 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 57a27286-1e06-3490-9c7f-28437f908764 | -15.0865 | -59.6487 | 2024-12-03 01:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| cb8bb641-fea6-301c-8861-829b2a888da2 | -3.076 | -53.3808 | 2024-12-03 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 5fd69040-4571-3765-9b60-a68712917da7 | -3.259 | -53.659 | 2024-12-03 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 11bb360f-9d30-312e-bad2-07d15edc4332 | -3.5497 | -50.1699 | 2024-12-03 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 59045fc4-75d0-3f8a-a628-17db622cdadd | -2.8212 | -52.5741 | 2024-12-03 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 24edd815-9080-3fac-8cd2-455819f86d7c | -3.272 | -50.3263 | 2024-12-03 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d8bee4e0-64eb-3557-bdad-8a4e0e3be3f4 | -2.8197 | -53.0425 | 2024-12-03 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| dc17f1f8-355d-35a0-9cab-1d3642e72b0b | -1.7541 | -52.7993 | 2024-12-03 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 92ea260c-43b8-37e5-97fc-252c24f445da | -3.5682 | -50.1693 | 2024-12-03 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 3a6dfed4-657b-3521-ba04-807cd9433ded | -6.1229 | -43.9578 | 2024-12-03 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7bfd4548-4303-3eb2-a8af-6c66afd1f3e1 | -3.183 | -54.3448 | 2024-12-03 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 36e6bdec-8a28-3d6a-b149-973cf234cc0d | -2.3396 | -53.8013 | 2024-12-03 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f89c8bcb-740a-3f9d-b0e8-cf94aad0948c | -3.183 | -54.3448 | 2024-12-03 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0462d6db-5118-3f48-8ec0-9e26c3ceffba | -2.2111 | -53.7835 | 2024-12-03 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 58cbd9d9-f160-3c70-9117-d8a8964bf943 | -3.2406 | -53.6595 | 2024-12-03 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| cfbab413-7443-3962-a891-1d29ec1d4fa8 | -4.5589 | -42.9289 | 2024-12-03 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a9b04087-23db-3102-95e0-dc9a0ff3093c | -3.259 | -53.6388 | 2024-12-03 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| f21ee367-4e56-396c-b898-9e0c90aa46e5 | -2.8012 | -53.0633 | 2024-12-03 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2f479ce6-5641-320b-b6ca-85d37fa98075 | -5.8197 | -46.4706 | 2024-12-03 01:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 798c66e3-618a-3b2f-8bb9-0914e8f7822a | -3.5681 | -50.1903 | 2024-12-03 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a9e940c3-8615-3a27-9821-9015e3e93037 | -1.7361 | -52.6162 | 2024-12-03 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ee6e7073-c07f-34d7-ba3e-4ef3611f77cf | -3.0945 | -53.3601 | 2024-12-03 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5ad935c7-7f45-35c2-b253-0fff9c136936 | -5.8195 | -46.4929 | 2024-12-03 01:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| c1c24cdc-efad-30e8-ad8e-4e1a893a1b34 | -5.801 | -46.4719 | 2024-12-03 01:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| ff7bbcc6-4dd2-3436-a9ce-3fac80a94e12 | -3.0949 | -53.2385 | 2024-12-03 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2af78635-12fa-3126-95ae-60df678f9e65 | -2.8197 | -53.0425 | 2024-12-03 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 851179c3-9af2-3d4b-a97c-085ef2e3bc6c | -3.1134 | -53.2178 | 2024-12-03 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 0da8b254-efea-3a5a-aa01-9350572bbfa4 | -1.7541 | -52.7789 | 2024-12-03 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| ecb615f4-a66e-3055-9c6e-de05b30e6ef2 | -6.1229 | -43.9578 | 2024-12-03 01:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |


[Clique aqui para ver as próximas entradas](README14.md)
