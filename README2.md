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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac4ebc0a-59da-36ab-a296-9bdb2f96cffa | -14.199 | -51.9122 | 2026-07-29 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 60238dee-be3b-3312-8a85-ad37d126faaf | -13.1523 | -51.3214 | 2026-07-29 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| edb191d2-b1e0-360c-b149-3c4d031e3f0e | -10.3612 | -49.7378 | 2026-07-29 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 3b2f2b26-9ec2-3553-ba4b-98533ba4f2d4 | -10.9397 | -43.0593 | 2026-07-29 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 97a09646-ae2c-32b2-bf86-15a09ef3cfe5 | -6.8708 | -46.0126 | 2026-07-29 01:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e0e9ade8-a8b8-3d7f-9025-84e4e548ae50 | -18.8004 | -51.2417 | 2026-07-29 01:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 3d5a9fcb-5c35-398f-ab25-b08d6c1385d2 | -7.36 | -45.8361 | 2026-07-29 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 387c340b-067e-3e28-aac1-70308b5ef1fb | -10.9401 | -43.0355 | 2026-07-29 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 223395f5-db90-3abd-9e08-f55bc2292e34 | -7.3598 | -45.8586 | 2026-07-29 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| a4db5bb4-aaac-3fbe-b33f-b04fddcc281d | -21.9726 | -56.031 | 2026-07-29 01:00:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 73.6 |
| f9b50d8f-0622-36dd-b760-3fb603870137 | -7.3413 | -45.8377 | 2026-07-29 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 0cbc360c-6590-3d1c-8469-60d419cd0ab3 | -10.3234 | -49.7418 | 2026-07-29 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 6cf7dd7a-62cc-36a6-859a-becbe32543ed | -10.3236 | -49.7202 | 2026-07-29 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| aaf07c31-579f-3cf7-83a9-91633a16764a | -4.3774 | -47.7627 | 2026-07-29 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 880f5eab-997d-3056-a9e1-6f601c2c7a5b | -21.77068 | -56.30036 | 2026-07-29 01:09:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1d28af60-ca11-3e62-a3ee-1f46617468f8 | -6.8708 | -46.0126 | 2026-07-29 01:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 5ad87c42-58d1-3a54-a197-1f5187966b53 | -7.341 | -45.8602 | 2026-07-29 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 2b19342b-f700-347b-9262-f829dffa1097 | -10.3239 | -49.6987 | 2026-07-29 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 2338640c-ce60-35f8-9eea-4c0ba93775dc | -4.3774 | -47.7627 | 2026-07-29 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a7b7ee21-87fb-34a8-ae49-1768a41f19cb | -10.3426 | -49.7183 | 2026-07-29 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| da1b7db2-6bc2-3460-86c5-ffbc0a5f7b6d | -14.1797 | -51.9147 | 2026-07-29 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 3cbb1365-fc1d-3f96-86cc-49f5de33c6ea | -4.3588 | -47.7636 | 2026-07-29 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 69774989-490e-3466-b8c6-d4dd1de0bbed | -3.6916 | -47.6411 | 2026-07-29 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6ad87fa8-db74-36ba-9f9a-a73ee0001bb0 | -10.9397 | -43.0593 | 2026-07-29 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7e10b86e-0668-3300-bf49-1c7c2ccc4caa | -10.3423 | -49.7398 | 2026-07-29 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 4c9f3209-e4c6-3a09-9aa8-463f5082c195 | -14.199 | -51.9122 | 2026-07-29 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 133.8 |
| c1ff31b3-7a23-3853-a72e-6c085d7eb30a | -10.9205 | -43.0622 | 2026-07-29 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| b514371d-3d96-3a10-808f-de5e55d2a72e | -10.3236 | -49.7202 | 2026-07-29 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| cfa0df7b-5fdd-3115-b76d-5b9fb0d9c720 | -14.1994 | -51.8908 | 2026-07-29 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 490d19ed-9fc2-3636-817c-44aaf2de2c01 | -7.3413 | -45.8377 | 2026-07-29 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 249.2 |
| 7ae399c9-a5f3-3387-af1e-bce2641d06a9 | -7.36 | -45.8361 | 2026-07-29 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 1ad5c4b4-f6a8-3595-b35a-ff2fba5ec70d | -20.91259 | -57.4887 | 2026-07-29 01:11:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 80557fbe-7d7c-3697-8cd0-4b9b651125e0 | -20.60952 | -57.24909 | 2026-07-29 01:11:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7122a1c7-0265-37e3-a6c1-28e1d3acbddc | -14.34823 | -58.95135 | 2026-07-29 01:11:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 26a85637-fb47-3571-84b8-96b968a7d6aa | -14.34274 | -58.93981 | 2026-07-29 01:11:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 998a6c9c-3215-34ae-9aeb-fab01fdc765b | -20.6078 | -57.2552 | 2026-07-29 01:11:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 3ce6b8f9-fd1e-34c5-901d-fe1c564e42e1 | -20.90056 | -57.49127 | 2026-07-29 01:11:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 22.4 |
| f56379ab-fa6a-3cba-994d-3f8f7ae9259a | -14.34571 | -58.95814 | 2026-07-29 01:11:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 37.4 |
| b36cc9b9-35f7-3d4c-b5b4-575b60db2ffd | -14.33595 | -58.95361 | 2026-07-29 01:11:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 9ddd0d0b-c20d-3999-bf3a-c136daa82bd4 | -14.33345 | -58.9605 | 2026-07-29 01:11:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f73d3144-fc99-3be5-a6ef-9c6ac0e30dff | -18.53948 | -56.82679 | 2026-07-29 01:11:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.9 |
| f71bbbbd-71cc-3a58-8d02-26ae63773174 | -9.48478 | -57.31492 | 2026-07-29 01:13:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| dad36d11-e2de-3885-a774-a52496a52feb | -8.93739 | -65.00359 | 2026-07-29 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4554afbf-4c52-3a8c-95bd-e01c5391d580 | -11.64555 | -60.44765 | 2026-07-29 01:13:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9f83406c-e6b5-37af-b62c-f0fea1f666dc | -8.821 | -66.75495 | 2026-07-29 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 37115090-7c3a-3545-98aa-b4671be51e26 | -9.49205 | -63.30307 | 2026-07-29 01:13:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| aa00a0ed-0771-3599-a27b-ea083efa5a72 | -12.3717 | -63.43818 | 2026-07-29 01:13:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 33cab506-2fda-3199-b169-8d1ce57c87cd | -8.82222 | -66.76389 | 2026-07-29 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ce97b66a-46ca-317b-93ba-5012b650a4e9 | -12.36609 | -63.44496 | 2026-07-29 01:13:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 22af90de-ad1a-3055-a217-bcbdf5407284 | -9.50175 | -63.30161 | 2026-07-29 01:13:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 865daf18-47b6-32cc-9480-7db41bdd3069 | -9.07068 | -68.69453 | 2026-07-29 01:13:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| be2ffd57-bc4f-3f51-909e-b902cf764f0d | -12.3568 | -63.44641 | 2026-07-29 01:13:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7c6a80aa-ab42-3e34-a95c-6fc415d430bc | -9.47839 | -63.36691 | 2026-07-29 01:13:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2d6a2c8e-2fdc-34e1-8bd5-d5e26a2ed3e0 | -9.48597 | -57.33902 | 2026-07-29 01:13:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 5a43b900-861f-3ca9-8356-eed911b58317 | -11.64493 | -60.45734 | 2026-07-29 01:13:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9fee1d63-70e6-3219-a3b6-576d95d1f394 | -7.34 | -45.85 | 2026-07-29 01:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca0b9650-29a5-3928-934e-b678108317f7 | -3.6916 | -47.6411 | 2026-07-29 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 3fd85df9-63ec-3f23-ae52-e58b9dfb2a94 | -7.36 | -45.8361 | 2026-07-29 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 198.8 |
| d971f708-d0a8-3fd1-99bb-7c075fe441aa | -13.1526 | -51.3 | 2026-07-29 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 840e1f08-c300-3245-89e6-6b517239c767 | -14.199 | -51.9122 | 2026-07-29 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 04200b38-0ca5-3fac-b279-a579c3b623ff | -3.6731 | -47.6418 | 2026-07-29 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 52dc194a-0d36-310b-918a-1de2fc17105f | -10.9205 | -43.0622 | 2026-07-29 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| b4b89ae5-9c4d-354c-897b-bb8cd750c7ce | -10.9397 | -43.0593 | 2026-07-29 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 2e7eca3b-d2f5-3440-9da0-eca2883306ae | -4.3588 | -47.7636 | 2026-07-29 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 24af26c0-ef03-31f2-92bc-7e833bfef685 | -13.1331 | -51.3238 | 2026-07-29 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| fbac2380-350d-366a-a3b8-e234750949d0 | -4.3774 | -47.7627 | 2026-07-29 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| c1142601-c8f5-3a19-8960-99240336d215 | -13.1334 | -51.3024 | 2026-07-29 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 4109a596-aaa5-3bb6-a994-56cf63e79ee8 | -7.3413 | -45.8377 | 2026-07-29 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 234.3 |
| 50bf7c4d-716c-383b-9acd-d88f8bc86c7b | -6.8708 | -46.0126 | 2026-07-29 01:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e64f34ca-5ea2-3a99-9b41-424c3b948943 | -7.341 | -45.8602 | 2026-07-29 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 41beae01-77fb-3bda-a7bf-9b766ee575a6 | -7.3598 | -45.8586 | 2026-07-29 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| beeba508-e930-3946-a79c-7522d6e8cf95 | -10.9401 | -43.0355 | 2026-07-29 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 889d4b03-952c-32e2-a7b3-153a40cc92bb | -7.341 | -45.8602 | 2026-07-29 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| fa4b12cf-4590-3040-9068-87c147606219 | -13.1526 | -51.3 | 2026-07-29 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 12759b61-bc7f-376e-a1cd-c2999c69d6d7 | -4.3774 | -47.7627 | 2026-07-29 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| bcb82c26-72f3-36d9-8042-a3009e11666e | -10.9397 | -43.0593 | 2026-07-29 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 803cdafe-a939-3801-a214-648edf03fed9 | -10.9205 | -43.0622 | 2026-07-29 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8ccb629b-1cf5-39fd-86fe-b9d08cf14506 | -7.36 | -45.8361 | 2026-07-29 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 227.0 |
| 6e200920-f7f4-3bf8-8934-04928ac2693d | -10.3423 | -49.7398 | 2026-07-29 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 6b4770a5-80d5-3885-8f64-870bd414c65b | -13.1523 | -51.3214 | 2026-07-29 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 68721716-b8b1-3420-9fcf-ead5e1f1947c | -13.1334 | -51.3024 | 2026-07-29 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| b9eece72-e3ba-305b-b8d1-a55658807855 | -7.3415 | -45.8152 | 2026-07-29 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 4bcf06c9-c4fb-3c0e-a781-bee7fb3cbe5f | -6.8708 | -46.0126 | 2026-07-29 01:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ee146e91-a863-3f31-a8af-0de96c09be12 | -7.3598 | -45.8586 | 2026-07-29 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a4138bfe-f768-3824-9140-eb3c37cfbddd | -7.3603 | -45.8136 | 2026-07-29 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 467a20c7-3e54-3cb9-8cb6-87b1af39e8f4 | -7.3413 | -45.8377 | 2026-07-29 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 269.2 |
| 78f58c2c-bb09-3fb6-9be2-ad988c522318 | -14.199 | -51.9122 | 2026-07-29 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 16427ace-199f-3db3-8534-2995f3c0f490 | -7.3413 | -45.8377 | 2026-07-29 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 269.1 |
| 1e8905e6-1b09-35e3-b256-235377db3484 | -7.36 | -45.8361 | 2026-07-29 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 300.6 |
| 18561b08-5add-3497-86c6-9c1abb1e3ba8 | -10.9397 | -43.0593 | 2026-07-29 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| d26cbfa8-3f44-343f-a351-7406260f8997 | -7.341 | -45.8602 | 2026-07-29 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 76acdad8-6690-38e6-b9e7-13aa90c7135f | -4.3774 | -47.7627 | 2026-07-29 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 22edee7d-a352-36f7-820b-863b2ef657f2 | -7.3603 | -45.8136 | 2026-07-29 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| cf591662-d071-3ac2-b314-a02dc234fde4 | -7.3598 | -45.8586 | 2026-07-29 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 9f4a917a-6501-3a8b-90cb-9972fb9e5419 | -7.3415 | -45.8152 | 2026-07-29 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 4523ecfa-e094-36df-b315-8e008d09b3d7 | -6.8708 | -46.0126 | 2026-07-29 01:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 126988d1-f260-3d92-90b3-218c2eb0e4d8 | -10.9205 | -43.0622 | 2026-07-29 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 0e17cea6-bb3d-3660-bfa1-8659e842ec6a | -7.3413 | -45.8377 | 2026-07-29 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 326.4 |
| 3b92860b-ff88-38de-b2bb-29d018633eb7 | -7.3415 | -45.8152 | 2026-07-29 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c3ea276d-bd64-33da-a69e-ed593dc0bf10 | -7.341 | -45.8602 | 2026-07-29 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |


[Clique aqui para ver as próximas entradas](README3.md)
