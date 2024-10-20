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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e63a3cad-94ba-3d61-8514-97fbc0a2d880 | -4.1775 | -46.626202 | 2024-10-20 00:14:14 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40e8a21d-7e04-336b-a857-f6df4247dfc5 | -4.1804 | -46.639099 | 2024-10-20 00:14:14 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b183fdf7-eedb-3786-9a3a-25bb90c504c4 | -4.1648 | -46.615398 | 2024-10-20 00:14:14 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0abae270-8c8b-315e-a21e-b4dc5ee18cbf | -4.1677 | -46.6283 | 2024-10-20 00:14:14 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 03221285-f3b7-3624-892a-e29822633731 | -4.1706 | -46.641201 | 2024-10-20 00:14:14 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 39c423a4-c80f-3afb-aaa5-0909eafe71e1 | -3.8897 | -45.748001 | 2024-10-20 00:14:15 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a0b3b51-bdf6-3af5-b2b8-48dee35f1e59 | -4.1068 | -46.861 | 2024-10-20 00:14:16 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25e1dfe3-d73e-37a1-b918-a4159c5eb020 | -3.8411 | -45.8055 | 2024-10-20 00:14:16 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 47efc180-d37b-3c55-9723-e23806327d80 | -3.8436 | -45.816799 | 2024-10-20 00:14:16 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff381c3d-af14-3c4b-a074-adebd5fadc8f | -3.8461 | -45.827999 | 2024-10-20 00:14:16 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4466f5fa-b319-3124-badc-542571f58c88 | -3.8338 | -45.818901 | 2024-10-20 00:14:16 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d14f808-6bc5-3030-a74e-67dde030d07c | -3.8363 | -45.830101 | 2024-10-20 00:14:16 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1f594015-2967-3c52-9ec8-e23ef72e58f6 | -3.8023 | -45.861198 | 2024-10-20 00:14:17 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5bec0a3-9d7b-3458-9fa6-4d8a2764a2f0 | -3.8048 | -45.872501 | 2024-10-20 00:14:17 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb73a7a-a43a-3a4f-896a-759d68028964 | -4.0211 | -46.935501 | 2024-10-20 00:14:17 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 779c2a4b-2f69-3a88-86ad-b0a005eb2cce | -4.3182 | -48.557098 | 2024-10-20 00:14:18 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed22354-c93d-3ac1-b2f9-3c0e962a0b70 | -4.3221 | -48.574799 | 2024-10-20 00:14:18 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10c5de8b-f250-3646-b614-8bb339447ee7 | -3.4078 | -44.2416 | 2024-10-20 00:14:18 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2abca19f-7da5-3140-8cf9-1d799f8f7899 | -3.4098 | -44.2505 | 2024-10-20 00:14:18 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c4db2e4-c9dc-3d3c-8cd2-cbf2f3b69a42 | -3.4119 | -44.259399 | 2024-10-20 00:14:18 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f805df0f-82cd-3cce-8a92-61f2d7403461 | -4.0113 | -46.937599 | 2024-10-20 00:14:18 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15eb3ba6-578c-3383-b4b2-8cb24e230239 | -4.0143 | -46.951099 | 2024-10-20 00:14:18 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1eea43-6eb0-3889-8408-421381fbe27c | -3.7584 | -45.894402 | 2024-10-20 00:14:18 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2fc48f8-2099-3ce5-87b0-79dd11ee07c4 | -3.761 | -45.9058 | 2024-10-20 00:14:18 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca8e1155-0645-343c-8fae-b8a72d401b08 | -3.7487 | -45.8965 | 2024-10-20 00:14:18 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa640f6e-93af-397c-8b83-bcd216c23d48 | -3.7512 | -45.907902 | 2024-10-20 00:14:18 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d957d6b8-49a6-3893-8f1e-aebfe8727882 | -3.7537 | -45.919201 | 2024-10-20 00:14:18 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c18ca40d-809b-39a5-b0db-bde3b079826d | -4.3085 | -48.5592 | 2024-10-20 00:14:19 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40183d07-bb28-3f48-a729-82fa4b1bcf79 | -4.3065 | -48.5966 | 2024-10-20 00:14:19 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a982bf3-6b35-3542-8776-d5a0aeaa7abf | -4.3104 | -48.614399 | 2024-10-20 00:14:19 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d03769d-a53e-39c9-ba4d-8603732d1c5e | -4.3007 | -48.616501 | 2024-10-20 00:14:19 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1cfc7a8-2ec4-3b0a-83cc-60bd5d62be0c | -3.5255 | -45.815399 | 2024-10-20 00:14:21 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8187a81b-5728-370c-9cef-8c45fc033be2 | -3.528 | -45.826599 | 2024-10-20 00:14:21 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c0fbdc6-69ff-3fb8-a346-b0170ae75838 | -3.5305 | -45.8377 | 2024-10-20 00:14:21 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b63903bb-eedc-31a2-9fde-69c8ff710ffd | -3.5157 | -45.8176 | 2024-10-20 00:14:22 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb8f09a-5db6-3be2-9ef0-e8e23fd2ed04 | -3.5182 | -45.8288 | 2024-10-20 00:14:22 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1603d65e-3557-313b-830c-f8732baf9225 | -3.9379 | -47.942101 | 2024-10-20 00:14:22 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3accab07-9836-3477-91db-469fb68742a8 | -4.4546 | -50.4324 | 2024-10-20 00:14:23 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| febda8b1-a2c7-3dbe-a3d1-4ec81cd1dd5a | -4.4449 | -50.434502 | 2024-10-20 00:14:23 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba142596-ecc6-3339-9b04-0cdf46e586f0 | -3.5871 | -47.5116 | 2024-10-20 00:14:27 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05b94fda-43b9-3785-b803-e37617539f8a | -3.8074 | -48.872299 | 2024-10-20 00:14:28 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7463afb-0b63-35dc-9075-739736ef969b | -3.7937 | -48.8563 | 2024-10-20 00:14:28 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e77965a3-c9e8-3fd7-967a-2d0b7008117f | -3.7977 | -48.874401 | 2024-10-20 00:14:28 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaa474bb-27a2-3e2e-aa40-95a578abd141 | -3.8139 | -48.947601 | 2024-10-20 00:14:28 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f127071a-331e-3a47-b620-75fd6e27c519 | -3.818 | -48.966 | 2024-10-20 00:14:28 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91aee068-6105-3a7a-8977-3d83f64da27d | -3.784 | -48.858398 | 2024-10-20 00:14:28 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e50c6a88-3fb3-3a1b-9b63-403831fb0d02 | -3.8042 | -48.949699 | 2024-10-20 00:14:28 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3907c9e5-77ef-31f4-a968-509c3fe75f23 | -3.8082 | -48.968102 | 2024-10-20 00:14:28 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bcd8152-453d-3343-ae31-b9dd1efc9922 | -4.2289 | -50.974701 | 2024-10-20 00:14:29 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 038068df-fbe0-3f35-bc5c-9baed69cdc74 | -4.2192 | -50.976799 | 2024-10-20 00:14:29 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95bdc402-2b78-3144-8620-e652225bc5b8 | -3.8745 | -49.959202 | 2024-10-20 00:14:31 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26ed4dd1-aece-3d50-95ad-e08f6a4babd1 | -3.8793 | -49.9809 | 2024-10-20 00:14:31 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04e0da80-c3c3-37c6-a79d-2823d2935b4b | -3.8648 | -49.9613 | 2024-10-20 00:14:31 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88dba5f2-1781-3af9-92af-fd8d424a532d | -3.8696 | -49.983002 | 2024-10-20 00:14:31 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e131fcad-3d7f-3c70-94a7-16e31eb3760d | -2.7365 | -45.3643 | 2024-10-20 00:14:33 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 471acfb6-3bab-3a1a-9e1b-846730df74dc | -2.625 | -45.506802 | 2024-10-20 00:14:35 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| faac79a9-2144-3640-8e1e-172fe5a1f7c4 | -3.5213 | -50.2897 | 2024-10-20 00:14:38 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85a1446f-64e2-30af-b268-f06e86a092d5 | -2.6109 | -46.898899 | 2024-10-20 00:14:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edf15ba3-cfce-3121-af9a-4a2c1d8b512c | -2.6012 | -46.9011 | 2024-10-20 00:14:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 387a6c82-7b63-34cd-beb2-fc3cb7cfcb22 | -2.604 | -46.913799 | 2024-10-20 00:14:40 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee0a293-eea1-3fc4-8d07-7bc62943c5e9 | -3.3654 | -50.638802 | 2024-10-20 00:14:42 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1c537f7-7c0e-3ff9-aca2-9c5d216f145b | -3.3706 | -50.662601 | 2024-10-20 00:14:42 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e54f3b99-06d0-38d1-a44f-b60fa79f91f4 | -3.3557 | -50.6409 | 2024-10-20 00:14:42 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d21854-cec6-3a62-96f3-db7b4cc839ad | -3.3609 | -50.6647 | 2024-10-20 00:14:42 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a876523-9b70-3686-86b5-aff0d8b4d20a | -2.5276 | -47.1203 | 2024-10-20 00:14:42 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 784fdeef-e850-3e7b-b58f-19c493136407 | -2.7705 | -48.655102 | 2024-10-20 00:14:44 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bff8ab37-82ee-33c5-8446-f432a04e0626 | -2.7743 | -48.672001 | 2024-10-20 00:14:44 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fda39211-e970-36da-9919-eccc83b46ba7 | -2.7781 | -48.688999 | 2024-10-20 00:14:44 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7a726cd-539c-320f-9934-c4a8989272a2 | -2.7646 | -48.674099 | 2024-10-20 00:14:44 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bec255e1-8bb4-3ed8-8325-e1df2d6d5c29 | -2.4866 | -47.483002 | 2024-10-20 00:14:44 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc82c179-29e2-357b-b960-0498fa83bc7c | -1.9457 | -45.5914 | 2024-10-20 00:14:52 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 663eed10-43dd-3f47-bbd8-2922390d92c4 | -2.7461 | -49.274502 | 2024-10-20 00:14:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f966d1b6-ac6c-37e0-9196-24f6ac62aeec | -1.9336 | -45.583302 | 2024-10-20 00:14:53 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8481d3e-0d1b-3edc-97e2-468b5fa587bc | -1.9359 | -45.593601 | 2024-10-20 00:14:53 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2bd73b3a-f900-33fe-b1bd-b59538fa1912 | -2.7697 | -49.289001 | 2024-10-20 00:14:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05fefe41-23d5-3d00-8dc1-4988520e9577 | -1.9238 | -45.585499 | 2024-10-20 00:14:53 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef889b5e-cf5f-3300-96d7-97fd4475c112 | -2.7558 | -49.2724 | 2024-10-20 00:14:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7f0157d-6135-376b-a158-ab2825d9b81e | -2.76 | -49.2911 | 2024-10-20 00:14:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 382449dd-1bad-3d58-b178-878532367276 | -2.7642 | -49.309799 | 2024-10-20 00:14:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e23767b-2e9b-3cf5-ab35-07297ee37182 | -2.7503 | -49.293201 | 2024-10-20 00:14:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b01a7894-ac39-34fa-baed-641ba18a42c8 | -2.7545 | -49.311901 | 2024-10-20 00:14:53 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c93b25b-3b6f-3f27-a22a-bc96cac38d56 | -3.0087 | -50.995499 | 2024-10-20 00:14:55 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90262ce1-d7da-3218-8f42-ebc3496e8fe8 | -3.0142 | -51.020401 | 2024-10-20 00:14:55 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6ba58ed-a44f-3934-a1f5-dbf259c122de | -2.2613 | -47.845299 | 2024-10-20 00:14:56 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da101961-475a-3601-945d-ad3af8ae02f0 | -2.3407 | -48.287701 | 2024-10-20 00:14:56 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6de2f6b1-11ad-31a0-a3de-bea083567494 | -2.2817 | -48.5695 | 2024-10-20 00:14:58 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c1bc0b9-7a2f-3dc1-9957-d3fe66dac90f | -2.2854 | -48.585899 | 2024-10-20 00:14:58 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03630ec9-30d7-3775-bacc-6098a094ef69 | -2.2682 | -48.555302 | 2024-10-20 00:14:58 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 470759dd-6a18-3642-a4ed-0bba075a1453 | -2.2719 | -48.571701 | 2024-10-20 00:14:58 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16fe1438-1787-35a6-8b71-25c5a48c74d9 | -2.2756 | -48.5881 | 2024-10-20 00:14:58 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 181ffb83-45eb-3da8-96d2-1b970cfb7bc8 | -2.2793 | -48.6045 | 2024-10-20 00:14:58 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f087944e-f119-3ce7-ae56-fa034bc2cfa0 | -2.2622 | -48.573799 | 2024-10-20 00:14:58 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98d09469-e31a-3c73-95d4-43ff53de5a51 | -2.2659 | -48.590199 | 2024-10-20 00:14:58 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b5bab9f-258a-3f27-8d56-180c3aa96421 | -2.1884 | -50.460098 | 2024-10-20 00:15:06 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cd05d70-1b37-30ca-bb46-22d60b3f5617 | -2.1835 | -50.438 | 2024-10-20 00:15:06 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eed35b62-76fc-3399-9c72-8a4060ae7d17 | -2.1738 | -50.440102 | 2024-10-20 00:15:07 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e85f6af1-4526-3c02-b81e-65ed4e86f76e | -2.1787 | -50.4622 | 2024-10-20 00:15:07 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72bf59da-29de-305f-91b0-9a58e5c94b12 | -1.3251 | -47.509201 | 2024-10-20 00:15:10 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c22513d-d20e-368d-b1df-2289a2ed6a2f | -1.3282 | -47.522598 | 2024-10-20 00:15:10 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 163106b3-86a4-3a6b-bffc-ca293590ae78 | -1.4416 | -48.963299 | 2024-10-20 00:15:13 | METOP-C | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
