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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1074d6ab-71f5-3663-a263-a42d7bc81b31 | -4.82545 | -48.09865 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03c911eb-c5c7-3dd0-a5b1-44093bc963e3 | -3.2523 | -50.01924 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf366401-68e4-34b1-be7d-adeaba743ba0 | -3.67333 | -46.50747 | 2025-11-28 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c102062e-d92f-3f00-9339-2b5599e68c1e | -2.93804 | -49.44458 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cfcf30c-a787-338e-9df9-bf9bb3eefd83 | -3.76545 | -46.96381 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eba65571-c94c-3141-9984-fbf22e2d1a9a | -2.27107 | -47.09824 | 2025-11-28 04:31:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3e3b50d-cc60-3d85-9b81-f5ce44558048 | -4.30057 | -48.60136 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3c6295ec-9e10-3aff-834d-2ad5dd63e1ac | -5.3628 | -44.80459 | 2025-11-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| caa26c5b-2a3b-3d78-be8e-8b280052e878 | -5.4527 | -44.69065 | 2025-11-28 04:31:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6fcac2b1-f339-3650-943b-2f356f78bc04 | -2.92362 | -48.22858 | 2025-11-28 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb7f3fe3-67b7-3a61-9997-d6243cc457c2 | -2.70494 | -45.67421 | 2025-11-28 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 64d1380f-6e34-3cd1-abec-fb14efb2aa1d | -4.01798 | -50.5972 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b848136d-dff1-34ea-9ff9-f636bb9d976b | -4.35534 | -43.73056 | 2025-11-28 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 091fc1b9-b345-36fd-b3f8-548be0114fce | -3.79017 | -50.98473 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca61a29c-2294-3ee3-80cb-75d4fe93b925 | -3.89557 | -47.23823 | 2025-11-28 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6fe11df-ba17-3bce-b390-7d55baee83fa | -3.89503 | -47.24166 | 2025-11-28 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d077412d-894a-30e4-9a6a-2d80b8172a8e | -4.76557 | -43.37024 | 2025-11-28 04:31:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da4a41a8-15ff-3fc7-9fb0-21665014679e | -3.92901 | -50.16641 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e45ac8fb-7bad-334e-a14a-10c4a5f9fe80 | -2.71748 | -45.21471 | 2025-11-28 04:31:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6414d7f6-4227-317e-8183-2d4abf46a7be | -3.84035 | -50.31618 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbb0ff94-da79-3b25-875d-ba1490d5d9d2 | -3.7467 | -46.95386 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a8a2adf-f980-3d93-928e-a25860f4ffff | -5.53818 | -46.97975 | 2025-11-28 04:31:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d060ee9d-db86-378d-af3a-0bb081feb17b | -5.57217 | -44.97733 | 2025-11-28 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7965d8d-f533-3819-b840-a095e90a7013 | -3.03457 | -50.97425 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc489dcf-ee80-3491-944e-9ce9d78f6d29 | -3.75331 | -46.95488 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d8fc8b8-d10d-34c2-ba23-50ac64b6c9cc | -2.71464 | -45.21053 | 2025-11-28 04:31:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ee8f045-714b-366c-bd2f-35ed23ca54f4 | -2.7151 | -53.17953 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13432be8-d4aa-3976-afda-b83063e0ef4f | -4.93845 | -41.14151 | 2025-11-28 04:31:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4bf5ca3b-310b-340e-b8c6-cefd49abe75f | -1.47044 | -46.3254 | 2025-11-28 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1562a4db-285f-373d-ac71-69c01f54ecfa | -3.06222 | -50.35444 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c573b768-83b8-34d9-9041-89ae03acb156 | -3.2366 | -50.69906 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddebb23d-7375-3d01-9e78-a6d7775f56c9 | -2.3331 | -45.94173 | 2025-11-28 04:31:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2669107e-c799-3880-91eb-4f822ccc8648 | -2.35942 | -46.09985 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2fa971f-f650-30c5-95d2-aa75af915b4a | -2.71635 | -45.22203 | 2025-11-28 04:31:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab67c987-3a59-3d16-8512-3922348b34e2 | -4.91069 | -48.59194 | 2025-11-28 04:31:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11e1a4a2-54e3-3534-9476-a92e389fab45 | -3.38524 | -50.25713 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3b94190-3ed9-354e-a176-e9322167998f | -4.73723 | -42.46817 | 2025-11-28 04:31:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ee860466-cecd-36d5-a3eb-b8130df76799 | -3.10686 | -53.13537 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32655d25-c72b-3c93-a26b-72f04543c8fa | -3.32178 | -52.72039 | 2025-11-28 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15f68aff-71cc-3a5d-9b24-924df64586a3 | -2.89479 | -45.54249 | 2025-11-28 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e0c9b7a-e393-3ed7-8e6c-4f91913c3968 | -3.49182 | -53.27106 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e83ecd5-3473-3796-9361-752ef4a2f9c8 | -3.58855 | -52.05442 | 2025-11-28 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9617cdb-7527-3a5d-b529-fd03b17850d1 | -5.4661 | -45.90742 | 2025-11-28 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 354c355e-49d0-3206-b513-ffa3725d4b5c | -3.79064 | -45.80092 | 2025-11-28 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 276c9d86-fc22-3012-bace-312aba2b0e3e | -2.89702 | -49.47769 | 2025-11-28 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5370434-f1e3-3260-888a-2ba4579f49c5 | -3.93627 | -50.44466 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e1c2619-6702-33bf-9e2d-8dd11546c85e | -5.44617 | -44.68562 | 2025-11-28 04:31:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d5abd422-cfb7-350b-826e-4537181c5ea3 | -4.56116 | -40.65645 | 2025-11-28 04:31:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 494fb7a2-29f0-33ea-a851-5c49579e7bb6 | -3.28246 | -52.62052 | 2025-11-28 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3eca1742-81e1-3bc8-8c45-453534c762f6 | -5.43376 | -49.29903 | 2025-11-28 04:31:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b89f672-2581-3cde-a621-cfbbf0c7c6dd | -2.42722 | -50.29222 | 2025-11-28 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ad6c268-2ab7-3a6a-ab74-c26fab505874 | -3.95377 | -44.76278 | 2025-11-28 04:31:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c7c1703-4756-3ea8-8737-a1926efcbcd1 | -2.16327 | -50.62561 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ce1043d-f08e-3486-a052-8e943bcd9983 | -2.39246 | -49.3853 | 2025-11-28 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9e74ba8-5d46-35eb-9d55-c3828e6ae042 | -5.11374 | -43.29547 | 2025-11-28 04:31:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8022cd57-2cfb-3135-a28f-4e34e0af8156 | -3.85641 | -47.05613 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a53307d1-1939-3ac0-8e7b-0532156aef93 | -4.20503 | -41.64425 | 2025-11-28 04:31:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b650f694-4611-3462-ab16-156e0a8927e5 | -3.22622 | -50.31756 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ac2cab2b-c6d0-36cd-b6e4-e434aea1fca9 | -4.03726 | -50.80132 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a3bf80c-5dbd-3747-aa95-4320d20a9b79 | -3.30956 | -51.53935 | 2025-11-28 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acbd0988-e7d1-3fd0-a9bc-f9586ac6afae | -3.50659 | -51.07834 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1f689d4-19c2-3f86-b5dc-0a8d8fbdd451 | -8.3841 | -41.75668 | 2025-11-28 04:31:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1e130548-4ac5-360d-99ea-f54c21895577 | -5.54478 | -47.76318 | 2025-11-28 04:31:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1e74b04-e439-3c32-8017-c07e50eb4ffc | -4.24766 | -43.67504 | 2025-11-28 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44f3f8f6-37cc-3077-be8f-5ae2b3595dd6 | -3.82883 | -50.18069 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da027387-1df6-33ec-945e-dab341b1fade | -3.38948 | -50.1152 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa6c7ded-80f0-3c4d-aad9-0cbdb9852537 | -5.29122 | -44.96551 | 2025-11-28 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f826f3e4-8458-32c7-8f87-02355b09ef12 | -6.91926 | -38.62772 | 2025-11-28 04:31:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c681ef7e-30fd-3239-bb24-e17a6e4faa1c | -2.27438 | -47.09875 | 2025-11-28 04:31:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85708213-da14-39c7-96d6-f6c6889bd0c8 | -6.39373 | -46.55124 | 2025-11-28 04:31:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1566eb8d-9df0-3d48-923c-deb2e04f17bd | -4.73867 | -42.46784 | 2025-11-28 04:31:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0e5fec02-a914-3ea0-b214-e19b1d6f815a | -1.37948 | -55.87096 | 2025-11-28 04:31:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57f9b4f8-3b2a-3232-bc0c-b330d8c2aad8 | -1.50121 | -54.7081 | 2025-11-28 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf4f894b-58e4-3a6d-a799-b32e25af7dbf | -5.06769 | -40.81716 | 2025-11-28 04:31:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 0768e3d7-0ff4-3b22-8ce7-6c3c3a5f3dae | -2.3943 | -48.51561 | 2025-11-28 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b129c5b3-d8c3-3292-bece-349a6e4839f2 | -3.09688 | -51.54296 | 2025-11-28 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd5f6c5e-c7cf-3d35-b6d2-f0e70f353fcf | -3.35013 | -54.09313 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 151d9dc7-5b8f-3c8e-9dae-57548f6469ec | -2.93231 | -51.00673 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb192190-2f68-3bb1-887a-7808298f29b4 | -2.82243 | -52.39885 | 2025-11-28 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47926742-347a-32d7-9f0a-96e5037fd1ef | -3.78759 | -42.33929 | 2025-11-28 04:31:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9f8d2e4-1e36-3eaa-b10f-32620779d6e2 | -4.1561 | -47.98562 | 2025-11-28 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69ca7100-d9ea-367f-86e1-92f29788add1 | -5.10481 | -46.11209 | 2025-11-28 04:31:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eab696c1-b622-36d4-b2e7-6e474b206b0b | -4.01504 | -50.59241 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a214e6dc-28db-3141-b35b-ef0432e594b4 | -3.63887 | -44.87851 | 2025-11-28 04:31:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 298247a7-1ff0-322a-b9be-9e10b19f6595 | -3.92837 | -50.17042 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a119cb8-6bf4-3dbb-b89b-5cf6828ecbb2 | -3.75992 | -46.95591 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea9c9474-73a6-3a70-b999-a3528afdf85e | -5.36327 | -44.80196 | 2025-11-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9183ed86-ec88-3bc4-8e9d-ca811367aa05 | -3.5016 | -53.9469 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cca8f42c-3edc-3b2b-99a3-982dd898a477 | -4.64443 | -46.4299 | 2025-11-28 04:31:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67d0b7d4-fbdf-33f2-9c93-4cff560de1c9 | -1.72372 | -46.20639 | 2025-11-28 04:31:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bf828ac-0e0f-33f7-a441-108794f074ce | -2.99133 | -52.51316 | 2025-11-28 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bc76fd5-f19b-38d8-abe6-63b698fd3951 | -3.85195 | -47.04135 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5c49f22-ebd8-387b-8534-1deea6fa2a03 | -2.69225 | -49.18116 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33f4d2a0-c879-3494-bf20-bffdef10d03a | -2.38835 | -49.38862 | 2025-11-28 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f61dc597-1d3e-3820-89f4-891172641e36 | -4.01832 | -50.58997 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24369a76-9d91-3c6c-b32c-75a05d2d3e93 | -4.01365 | -50.60086 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 170b7d8d-6d1e-3318-9001-c93051a43c04 | -2.72384 | -53.18071 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f11bf220-8cf2-38b4-a026-4993cfc9630f | -3.75607 | -46.95884 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6257b167-e96d-3ceb-89bc-c277725e9835 | -3.43939 | -50.23065 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7124e004-db59-383f-bb8d-e20069fe56ce | -2.69855 | -49.55873 | 2025-11-28 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
