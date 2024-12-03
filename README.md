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
| c35f9948-3cd0-38b0-bfa5-ed33fdff97b2 | -5.1365 | -43.2419 | 2024-12-03 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 0db4cf71-a289-3416-a40b-a4a9db8ead77 | -3.0945 | -53.3601 | 2024-12-03 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 2d70585e-8263-38cb-b0e3-d8b4b4745d6e | -4.5589 | -42.9289 | 2024-12-03 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 160.8 |
| a7ca868c-b0f8-3b15-a921-8b4fb42b7ac3 | -1.0736 | -53.436 | 2024-12-03 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| ea1faea9-7be7-357c-909a-bcca8c9a76c3 | -1.0919 | -53.4561 | 2024-12-03 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 179.8 |
| be1095e1-6867-3eba-a865-6f7ad9b70ea7 | -3.0761 | -53.3606 | 2024-12-03 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 6b831486-1e70-3730-b7a5-35e804efeb8f | -3.2774 | -53.6383 | 2024-12-03 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a4210a59-9ff7-3c60-a40e-bd2730410999 | -3.2591 | -53.6186 | 2024-12-03 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| f33659f8-aebe-38c0-83df-84425c317ebf | -2.3644 | -45.7254 | 2024-12-03 00:00:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d4efb301-7a45-35da-a173-240b5c8062d4 | -3.5497 | -50.1699 | 2024-12-03 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 31051e5d-02e7-35a0-b403-29fcdcbea529 | -3.5018 | -41.5427 | 2024-12-03 00:00:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| 28d6ad0e-1b41-3783-a69a-e5627393e2c0 | -3.259 | -53.659 | 2024-12-03 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 4e811e10-2ac8-3f91-9137-23afdf5061bb | -2.6644 | -44.9743 | 2024-12-03 00:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 012b13a3-5868-3879-a580-3be9ee383d09 | -2.3396 | -53.8214 | 2024-12-03 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2ccf2023-f110-3461-9633-050bb1b5f7b4 | -9.374 | -57.5553 | 2024-12-03 00:00:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 026053a6-b053-39fc-aee1-84ec4a69c64f | -3.2775 | -53.6181 | 2024-12-03 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 3f0e2dbd-2db1-3245-8620-1e0098762120 | -4.5403 | -42.9066 | 2024-12-03 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 49eca2c5-adeb-3d4a-b57e-3f291ad5e4ba | -3.0944 | -53.3804 | 2024-12-03 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| aa91db05-cc92-3d55-8f1c-7c737996b33f | -5.1552 | -43.2406 | 2024-12-03 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 8b492afd-fc77-311b-8356-fce3c1315f60 | -2.3459 | -45.7036 | 2024-12-03 00:00:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 3d6368cc-86f9-3afc-874f-60506a11411a | -4.5591 | -42.9054 | 2024-12-03 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c46f0294-8af6-325d-bafc-59c2709b5378 | -2.6061 | -45.6063 | 2024-12-03 00:00:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ffa0f582-519b-35d8-a594-593bae031f6c | -6.1229 | -43.9578 | 2024-12-03 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| fe4c89f6-1e33-3eff-94d4-f6bc59275de7 | -2.8295 | -45.4868 | 2024-12-03 00:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c757f65f-7885-3950-b1fe-3cf7ee971870 | -5.118 | -43.2198 | 2024-12-03 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| a96ab3f2-de1b-3dab-a2e7-c1c565768cbe | -3.3606 | -51.2209 | 2024-12-03 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b143089f-2e40-3e54-8470-9151fa0d2c5c | -1.0919 | -53.4359 | 2024-12-03 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| d0f7b1b3-6938-3663-b192-0e7b941b3733 | -5.1367 | -43.2185 | 2024-12-03 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 09149f7d-e911-3044-b380-5fdbfd1b0f63 | -2.8396 | -52.5941 | 2024-12-03 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 682b0699-b1f8-3d60-9eda-3fbc2a2dcc2b | -1.736 | -52.657 | 2024-12-03 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| c484a71d-3399-3286-a880-b664d53a703c | -3.6096 | -45.5908 | 2024-12-03 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0bfe7faa-fab3-3447-9cd9-0a9c0e506494 | -3.3606 | -51.2001 | 2024-12-03 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 168c6176-f4ad-3362-a412-79788412e4d9 | -2.6643 | -44.9969 | 2024-12-03 00:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 9e8fd637-4aa4-3507-8fe7-1c2368482ddd | -1.0735 | -53.4562 | 2024-12-03 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 247.8 |
| c1f0de48-227e-368e-ab02-d1edbd92e693 | -3.2021 | -45.2932 | 2024-12-03 00:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a23de113-62c6-3279-ab29-6faaab8424d6 | -3.183 | -54.3448 | 2024-12-03 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 735f6339-c95a-3abe-b575-732d25357ef4 | -1.0735 | -53.4764 | 2024-12-03 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ae7c8d66-13d8-3bbf-94cb-829faa0c3023 | -2.8196 | -53.0629 | 2024-12-03 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| a16c7675-8436-334c-9924-b0bfd221e46e | -1.7541 | -52.7789 | 2024-12-03 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| cc2c07b0-7caf-3c04-ae54-979f7166bfce | -1.7361 | -52.6366 | 2024-12-03 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| abb6e4b4-58b2-3c42-a8f7-6c29c037a7fd | -2.8212 | -52.5741 | 2024-12-03 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d971165d-5d37-3f6a-8f53-9fcd7a1b4bcb | -1.0919 | -53.4762 | 2024-12-03 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 131b7a82-a704-3a89-a370-8c53046367b9 | -2.8013 | -53.043 | 2024-12-03 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a9865b61-7b84-3980-b68f-b0e58f5f289c | -4.4025 | -49.7774 | 2024-12-03 00:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 21801535-419c-3e5b-a3a3-db5a6e00f550 | -2.8212 | -52.5945 | 2024-12-03 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| f81f2b45-61e9-3f0f-b165-3f0c4923e823 | -5.1181 | -43.1964 | 2024-12-03 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 1e2ef446-891e-3fa9-a6b8-0b83013dc7cb | -2.3645 | -45.7031 | 2024-12-03 00:00:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 7c18989c-5673-3db3-b038-ed5362a167bb | -5.1554 | -43.2172 | 2024-12-03 00:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 1ac01c69-435b-30d2-bb35-58ef9e0aff74 | -2.0271 | -53.9477 | 2024-12-03 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| ffccae94-ca51-3491-9e7b-5d09bb8d12fd | -3.3421 | -51.2215 | 2024-12-03 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 02a8a06d-4eaf-3ba2-97f2-753826a84f01 | -4.1915 | -51.1706 | 2024-12-03 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 64b79af3-8666-3fac-9092-029477963d2b | -3.259 | -53.6388 | 2024-12-03 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 02c6b96a-3e44-3387-a069-d76371350008 | -3.4617 | -41.9983 | 2024-12-03 00:00:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| ef900c00-29e4-3f33-9814-68ea9231c55e | -3.3422 | -51.2007 | 2024-12-03 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| f4a612c4-6ea3-3bcb-8b9c-0293186a1264 | -3.1831 | -54.3247 | 2024-12-03 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c7812682-1890-3d5f-999d-9dea3ccfea9c | -3.076 | -53.3808 | 2024-12-03 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 635f4caa-4290-3365-9d2c-1c562ebb14f7 | -1.7361 | -52.6162 | 2024-12-03 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| f4a2a2fe-f87c-3110-9735-fa886311e1d8 | -2.3396 | -53.8013 | 2024-12-03 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0d9df1f6-4c3b-3617-a368-6b2a59b1ff81 | -4.5402 | -42.93 | 2024-12-03 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 75c9ab3d-0558-3ee3-976f-6b3f31398502 | -4.1914 | -51.1914 | 2024-12-03 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bd045ccb-e538-386f-aac6-111a6c542850 | -2.9609 | -45.1898 | 2024-12-03 00:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 30f2ad9a-df72-3d9e-8e62-a0881a0f8ca1 | -2.8197 | -53.0425 | 2024-12-03 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 334e02ca-7465-356c-99bc-ea37b662f6ec | -2.8012 | -53.0633 | 2024-12-03 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5d505a20-70ea-36b7-b67c-47228012fc49 | -1.7541 | -52.7993 | 2024-12-03 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| b1ba13f8-3507-3dbf-9c47-a49223078590 | -5.13 | -43.25 | 2024-12-03 00:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad4a9d17-2d1e-3bee-b441-68401f7db43c | -5.13 | -43.2 | 2024-12-03 00:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9628707-bb8e-396f-8de8-f8a3474e86fd | -3.183 | -54.3448 | 2024-12-03 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 93d7de28-6670-3c02-ba88-d6799546629f | -3.259 | -53.659 | 2024-12-03 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| b8c11615-7f3f-39f4-bce7-fd5e0f67401f | -2.8197 | -53.0425 | 2024-12-03 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 440b321d-2241-3954-895e-e812e0630ac5 | -4.5591 | -42.9054 | 2024-12-03 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 91491f95-ce50-3efe-a76b-a55d710352af | -3.0945 | -53.3601 | 2024-12-03 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 99e79c65-08b0-3a25-b087-2bd13aeeccee | -3.2021 | -45.2932 | 2024-12-03 00:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| e71595ad-522e-3d3d-bc89-44825713da97 | -2.3645 | -45.6807 | 2024-12-03 00:10:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 0a7ee14f-b0d8-3ee2-bca2-929c2fc9a469 | -3.3421 | -51.2215 | 2024-12-03 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 003ca969-c2ca-3a19-90df-f0013820602f | -4.4025 | -49.7774 | 2024-12-03 00:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5326f1b7-1bd3-34cd-a066-69c8953e03b4 | -2.6643 | -44.9969 | 2024-12-03 00:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 0e2ece9f-ca60-3e2f-8604-06e893bfd17a | -3.6096 | -45.5908 | 2024-12-03 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 395ba7f4-aeb1-3972-a446-801e4fcd708a | -2.3396 | -53.8214 | 2024-12-03 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7b8a4ff9-606b-3375-bc00-6aa077cc8cbe | -1.736 | -52.657 | 2024-12-03 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 3e6f7483-3707-36ec-9bb0-60a4d6bab9f1 | -3.3422 | -51.2007 | 2024-12-03 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| d7e61fdc-4b0f-370e-8f58-863cff32ee2b | -1.0919 | -53.4561 | 2024-12-03 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 174.8 |
| 596f0aa5-4f61-3540-b467-6c082001cdc5 | -3.0761 | -53.3606 | 2024-12-03 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b7ef4019-7cc1-3410-beaa-f7a5fb9ab363 | -3.5018 | -41.5427 | 2024-12-03 00:10:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 54.0 |
| d8154fa9-358c-31d5-b42a-53950cc56b35 | -2.3396 | -53.8013 | 2024-12-03 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| fc19755d-a115-34d1-9514-d51a5b019055 | -5.118 | -43.2198 | 2024-12-03 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 2a0fe21f-2f04-3ad1-b44a-08bca9be81c1 | -3.1134 | -53.2178 | 2024-12-03 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 2bb8f0a9-adef-3772-ac9a-188edc5e1004 | -1.7541 | -52.7789 | 2024-12-03 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1d9215d3-145c-35ba-abfb-d1ea44ae8748 | -4.5403 | -42.9066 | 2024-12-03 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 7c932790-5a4b-33c2-bf3e-754580e78705 | -1.0735 | -53.4764 | 2024-12-03 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| aa51eea3-df5a-3989-9816-eb4b5a088cf5 | -2.8212 | -52.5945 | 2024-12-03 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d680a8b7-58e6-3f9d-bba5-091d338aa50c | -3.0944 | -53.3804 | 2024-12-03 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| b8c735be-1445-3084-a543-fa6ca161b627 | -1.7361 | -52.6162 | 2024-12-03 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a5ae3a3e-4c95-31aa-b2a3-2160ab197f88 | -2.3458 | -45.7259 | 2024-12-03 00:10:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| e525118a-f26a-3b6a-b8f0-2ce926fc252c | -4.5589 | -42.9289 | 2024-12-03 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 153.0 |
| f44ecd22-1500-3d68-82cc-49d7f903baf4 | -2.3644 | -45.7254 | 2024-12-03 00:10:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 959a367f-06a1-3021-802d-52181372d284 | -2.3645 | -45.7031 | 2024-12-03 00:10:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 339.2 |
| 6cca82a5-71fc-31a1-a6bd-d3d43fcc2b59 | -3.1133 | -53.2381 | 2024-12-03 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ca369f73-40e3-3127-9d67-910bc71a74b2 | -3.4617 | -41.9983 | 2024-12-03 00:10:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 97fe3d0d-753a-3c3d-b02e-bd4bf9ea2ca7 | -3.1831 | -54.3247 | 2024-12-03 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 61df2e59-c1d0-336b-b41c-e0957ecfe1cb | -1.0919 | -53.4359 | 2024-12-03 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |


[Clique aqui para ver as próximas entradas](README2.md)
