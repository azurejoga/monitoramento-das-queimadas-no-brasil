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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca952225-d8c3-3860-8ead-e4532413a1ff | -6.66492 | -58.87737 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c4a10aeb-9e3b-35a2-8940-4b63d3e25e84 | -2.90357 | -54.1413 | 2026-10-01 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 88a0684f-76d7-308b-b40b-dea759571c7a | -2.03526 | -54.05742 | 2026-10-01 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e716fe4d-2780-377c-a0b2-deef19357f66 | -5.97388 | -55.37593 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 937bfe15-2398-39d2-a5c0-b4dc6cb18c1d | -7.55006 | -55.02813 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d563e1fe-db41-346b-a192-5791b50aac6b | -3.37516 | -50.9403 | 2026-10-01 05:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53fb87b2-b491-3fd3-aa5b-b24babf2c6b7 | -6.43878 | -55.8063 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f18682a4-2672-3c3c-abfc-6d0d65ef280f | 2.086 | -50.74431 | 2026-10-01 05:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83512744-8510-3499-b639-6bd2156b8378 | -2.98823 | -51.03317 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3df3a423-7e81-3e71-868c-d6d34afd6fdf | -7.71751 | -54.79514 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b23c7d3-eea1-356c-80fe-2eefc37b616a | -7.35203 | -55.59116 | 2026-10-01 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 125f3ff5-7532-3183-a5e8-22a700ebe381 | -6.84535 | -59.35736 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a536388-09b7-3fe0-a01f-d2f6a2f358b2 | -2.98019 | -51.0388 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 386b00cb-8910-3472-9d33-c2f765600f7f | -2.03418 | -54.05958 | 2026-10-01 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01b2b0ef-89e9-302f-a2af-effa06fbb5e2 | -8.26018 | -54.73677 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a452178a-0600-305e-82bc-d350bf764a27 | -2.99526 | -51.03424 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3d5a187f-0f2d-3f80-a00e-4d5021cf2d67 | -7.54979 | -55.04332 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35db00e3-b399-3d4b-b004-228b124cbda0 | -5.86619 | -57.7571 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e109ef0-0344-36a8-8c58-dc99d3cebd8e | -6.67449 | -58.87427 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14f5fc63-84c4-3a74-ae21-1566b7e2edb4 | -7.49001 | -55.00037 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9621b306-a2d5-3cb5-aaad-bf1363e4ad99 | -6.4869 | -58.53614 | 2026-10-01 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 743fd3dc-6ae0-382e-af5a-f04f495cea5a | -7.70501 | -54.79774 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bffcbdd1-a10f-37fb-b2ae-f5fefb9e792a | -6.69886 | -55.05036 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87d79718-e46c-3a99-8894-d49e170bac7e | -1.44937 | -54.46058 | 2026-10-01 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb13af3c-2edd-3a56-b98f-dd04931d88ab | -6.66806 | -58.87561 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b8a86ca-df2a-3219-92ea-c0103df44d35 | 3.28247 | -60.6176 | 2026-10-01 05:53:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 64d889f4-db91-3ebd-b5c6-6b81ec9b424d | -7.34588 | -55.59426 | 2026-10-01 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93e09cc7-c20f-36ee-b7dd-53f21d26f524 | -2.4992 | -56.9106 | 2026-10-01 05:53:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 188c05bd-d45a-37af-81cd-ebe8a73e1759 | -5.86188 | -57.7526 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84adb4eb-be01-3614-af1d-9d621a86f577 | -6.49144 | -58.53683 | 2026-10-01 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e122abe5-5f4e-39c6-925d-ec54ef6bb4af | -5.29536 | -56.00475 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f32933f-c55a-3ee8-9c5a-c307969b5f43 | 2.89565 | -60.29557 | 2026-10-01 05:53:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98ad087a-e723-3fb8-a529-ab644272ea66 | -5.12498 | -56.00783 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0395ed9-7a02-32b8-bb1b-d75193b4dee3 | 1.87754 | -55.64034 | 2026-10-01 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5fbbf077-abb5-36ae-b48d-5215e18b3d15 | -6.53222 | -60.03502 | 2026-10-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b5d1bdb-01ea-37d1-9ede-4ed7694c988f | -2.89977 | -54.08647 | 2026-10-01 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b7c21a2-4a69-3850-917b-011ce15f950b | -2.96009 | -51.02879 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71c36c78-ac6c-3be0-a060-07389e7929de | -3.18616 | -51.24633 | 2026-10-01 05:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f5e293e-2ce3-3f23-a39f-c8efea350e2a | -7.4965 | -54.99663 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9924ad61-6f57-3497-aa41-31d53b73a40f | -7.50835 | -55.04105 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f734be5f-eb0c-3f5a-826c-fb0bbe5725b6 | -2.91102 | -51.31476 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 885ceac9-0eff-3a41-b116-a25442f1cb11 | -6.69831 | -55.05438 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abb62331-9a84-32f0-963f-b88a26c9c835 | -6.11241 | -55.69979 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26b728a4-7b01-3ac3-8b1c-c6f3a9ef1bcf | -3.17917 | -51.24541 | 2026-10-01 05:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a93079d-b620-364c-92b4-88f70afdd8e4 | -2.905 | -54.09141 | 2026-10-01 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1860c03d-ddb1-3992-83af-6852e4a40ba5 | -6.11141 | -55.70691 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c4c6ba1-2eeb-3263-b61c-4a5db2d89dfc | -2.96792 | -60.07775 | 2026-10-01 05:55:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 216dc0f5-3999-396b-8c15-6a6e4049c740 | -4.30339 | -50.76146 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 7a218f78-8f49-39b4-a98e-15c564734eb6 | -3.06816 | -54.37937 | 2026-10-01 05:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 386f7043-0c2b-3b89-b72c-7338baadf900 | -12.69789 | -54.06721 | 2026-10-01 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 679532b4-f31c-3e68-92ac-09a3de45d478 | -4.30651 | -50.73979 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5755eba9-b90e-369c-96b6-bb2df98dcff9 | -3.83177 | -55.79654 | 2026-10-01 05:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd625473-e565-3c57-bd55-457be1eb8221 | -3.0119 | -53.87929 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cfe07ba-ee14-3e85-9849-548fbaa57c2c | -13.65763 | -53.94012 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 110852b5-3774-39f3-bf97-eafb8a52024c | -4.28047 | -50.76596 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d44ad8b9-4df8-37b4-b909-b32722b62a1b | -3.17691 | -54.09511 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5b204721-fae7-372e-8e57-7e35508bd7be | -4.29713 | -50.75334 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9ca2d884-3733-3687-a872-6c9d152e06fa | -3.18089 | -60.06897 | 2026-10-01 05:55:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b52c307d-e40e-3133-b101-4e0498fe7fd7 | -11.26173 | -54.81547 | 2026-10-01 05:55:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 763d5d34-c7fe-3693-9a39-df20eaa49a48 | -3.59287 | -54.55476 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe6054b1-7098-3f08-8faf-5b51b9a9635d | -9.37412 | -65.47015 | 2026-10-01 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5984e95a-d90d-3a8e-ae72-463f6fb8df2f | -3.82647 | -55.79589 | 2026-10-01 05:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e585ecfb-9b48-34b7-b8c1-02362f522402 | -2.55005 | -57.40502 | 2026-10-01 05:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 657eb5eb-24f8-3b96-aa80-411283e99716 | -10.50986 | -57.78044 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 085699e0-e8d3-35ea-bda3-da5d4f72f902 | -3.14666 | -53.75031 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73a1c190-ce18-3fbc-937a-3c4ec924eca7 | -3.16979 | -54.10264 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ae65c6ab-f346-3c28-ac77-ec7fdd1b419c | -9.00547 | -65.70563 | 2026-10-01 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32c40d51-3b2c-3359-bf42-eea171ba7ea7 | -4.25044 | -50.75814 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 1892a770-30b3-3a5e-a227-ca2c7a49aeac | -3.00834 | -54.22969 | 2026-10-01 05:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6e772db-d6ec-3d63-99c2-351f75f82715 | -10.2457 | -59.02574 | 2026-10-01 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60ea9ad8-5d1f-345e-9e9f-fc42ab56eba5 | -3.29443 | -53.85629 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3baaa474-e4ff-3bdf-b1c8-61364c930d65 | -3.0204 | -53.8831 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6404f899-824f-3e89-bfc2-05d26de91deb | -3.18216 | -54.09991 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a7451125-640a-32a6-aca8-951962eebd62 | -4.04244 | -54.23712 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4518e76e-b0b5-3bdb-8fc0-8565d2adbdf8 | -4.29189 | -50.78979 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c08d1058-cbf7-31dc-ac42-a5caccca5351 | -10.06975 | -63.0805 | 2026-10-01 05:55:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25d628bd-10f8-32ac-b3a7-151ae9c6251d | -2.88392 | -54.87514 | 2026-10-01 05:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de15740a-01c7-3a0a-ab9f-ffbc99473e87 | -4.2721 | -50.77267 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 8f6f9f50-35fe-3a52-b20d-96f5319adb18 | -4.29677 | -50.75809 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5634faf0-5bb2-312d-a16b-fd85492686bc | -10.53021 | -57.78315 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56172b20-0f7d-3ef3-b850-2a6297ad5361 | -10.25034 | -59.02645 | 2026-10-01 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3bdec72-70c7-3564-ac45-36f1895cf22c | -4.29814 | -50.74632 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a31414d2-5503-3544-93b8-8ff215f8af0b | -3.17104 | -54.0943 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f281be12-43ba-3ec2-b9a8-eb59af7f3bdb | -9.70215 | -58.12494 | 2026-10-01 05:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3747f001-5f41-342d-ab11-28361a2791c0 | -10.5255 | -57.77961 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a27f37f6-18a9-3268-8a5d-b76dc2f6c1b8 | -11.172 | -54.11794 | 2026-10-01 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9d41cb4-4677-3709-a262-c757d0fc0c78 | -10.41175 | -53.78126 | 2026-10-01 05:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d89f4085-a229-33a5-b374-2027b9188e3c | -3.0033 | -53.87614 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a53ff88d-14c5-35e1-8520-24fef30b78d7 | -13.6532 | -53.93913 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fdd92853-ea2a-352a-a673-c122690e999c | -3.14733 | -53.74594 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73b4d68b-cc8b-37cc-b395-754087f38bb2 | -4.25663 | -50.76646 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| c184ce1b-c2a9-39c8-8c6c-abce5ade2193 | -3.30037 | -53.85723 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8306407-41ff-3b43-96b9-babcad2f6909 | -3.28848 | -53.85534 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4cbbb11f-b0c5-3c16-b86d-fb12f25eab0d | -9.33824 | -57.1767 | 2026-10-01 05:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2ce24e4-abfa-3e8d-aa0c-cfedd7c29d17 | -3.14135 | -53.74506 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2b25945-6d93-38b9-ae6a-755a146bfebc | -12.7768 | -54.02389 | 2026-10-01 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c2b2d76-58a1-30b9-9fc3-e2523a0c1c22 | -3.17628 | -54.09928 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 902fe5d9-3710-36c4-83c2-ecd44fc106c4 | -4.30403 | -50.75924 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 043c3947-e485-3ea4-8b4a-969797a3c4cf | -3.98185 | -56.08506 | 2026-10-01 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0afdaa09-0c53-30be-89a4-1676cedcc047 | -12.77811 | -54.01218 | 2026-10-01 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README88.md)
