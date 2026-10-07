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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddaee952-41d7-3c5e-8ff6-84fabe394a95 | -7.3747 | -46.2161 | 2026-10-07 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a30291b1-248b-3773-b74a-de4dc13634e9 | -11.0642 | -45.854 | 2026-10-07 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 50919c54-aa23-3d9e-97cf-557faead8c79 | -11.1988 | -49.4297 | 2026-10-07 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 735ebb77-608d-3780-9bde-2b3d038cb252 | -9.158 | -45.1328 | 2026-10-07 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 162.1 |
| ba2a5873-5680-3214-a068-fe9d73172489 | -6.9331 | -43.6566 | 2026-10-07 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 172.5 |
| acc0c7f8-e1d8-364d-bdaf-552ff17c2be8 | 3.1281 | -60.575 | 2026-10-07 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 8ad743e2-43d6-3547-9428-a51f89a8e9eb | -11.7947 | -46.683 | 2026-10-07 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7d2bc52b-9e5b-35da-8ec8-f73454b861e9 | -11.3742 | -46.7173 | 2026-10-07 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 7545809e-5764-3373-bfbd-81f8cecb21b9 | -11.0459 | -45.8109 | 2026-10-07 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 247.0 |
| 8af2b064-ba6b-3cc6-aa03-ba3bb6c81cff | -11.8311 | -43.5628 | 2026-10-07 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 256.4 |
| aaae219c-a88b-31ae-aa93-74056c5791f9 | -11.2295 | -46.2403 | 2026-10-07 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 530.5 |
| b85806bf-28fb-34c7-b6f9-6b1d35ad398f | -9.1363 | -65.2835 | 2026-10-07 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 30358954-5f27-3770-bcad-484be7633952 | -9.158 | -45.1328 | 2026-10-07 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| e7150e50-99ef-3d27-9d82-db21a8085f37 | -10.8591 | -50.6692 | 2026-10-07 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 14017d7a-7631-39b2-9d7a-1f30c75c342a | -6.935 | -45.2408 | 2026-10-07 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| fd6bdac9-8a65-3fb2-b6d7-556c487ecec6 | -11.8315 | -43.5391 | 2026-10-07 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 48e6df4f-2b57-3643-9b57-d360c7b7fc5a | -7.721 | -45.4645 | 2026-10-07 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c063fe16-020c-39ad-8f37-3f7bcaf967d6 | -7.7213 | -45.4418 | 2026-10-07 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 87f2f9d2-b084-3714-bd5b-78072820dec3 | -7.7399 | -45.4627 | 2026-10-07 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 57bdc146-9118-31a4-bb29-be88b6b285bf | -7.3935 | -46.2144 | 2026-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 524e1f1a-45eb-32a5-b605-49686ed9429b | -7.7592 | -43.8325 | 2026-10-07 14:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 424ed83a-1dc9-3617-85f7-151a703990d7 | -16.0295 | -39.8601 | 2026-10-07 14:00:00 | GOES-19 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 99.7 |
| a2bc3714-1766-3879-85b3-9b200cfb04e3 | -11.8503 | -43.5598 | 2026-10-07 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 453.3 |
| f18fba86-397b-3e1a-9533-8bf29a8b71cd | -10.6199 | -60.4852 | 2026-10-07 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 26bbd15b-3668-35de-8441-902e6163fec3 | -11.0642 | -45.854 | 2026-10-07 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 228.9 |
| e2ca87f5-b0ab-3290-9cbd-d2b54585657b | -7.5568 | -46.7128 | 2026-10-07 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| beceba42-55d0-39e8-914a-e3dd779f3bab | -6.4413 | -55.0224 | 2026-10-07 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| c13659ff-f8b8-3501-92d8-1e595dbff37b | -7.8789 | -72.3492 | 2026-10-07 14:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 110.4 |
| a6f0c4c7-68c0-3adf-ac10-a3da24b67fc8 | -7.2 | -55.1026 | 2026-10-07 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| d565d903-dc39-35c3-8ee5-46b866b0b2e7 | -7.5286 | -45.8659 | 2026-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 785ff40b-1d52-3ff0-abf8-45abc5bd0b40 | -11.1556 | -46.0916 | 2026-10-07 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| cd8f8425-8919-3230-970c-22ce0cc79d0e | -11.7943 | -46.7056 | 2026-10-07 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c1b1f062-1e75-3c04-b03b-ebb0ff4577c8 | -11.0935 | -47.6019 | 2026-10-07 14:00:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c18dcd45-f8ed-34dd-931f-e9ca4d40d3b8 | -15.4011 | -46.0781 | 2026-10-07 14:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 862d873c-00e0-30f8-85f6-f697fb85499c | -11.7751 | -46.7082 | 2026-10-07 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e2ea8f15-e99b-3c04-9285-ca601f43b968 | -7.349 | -55.014 | 2026-10-07 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 61ad7f1b-0024-3d4d-acb4-e85bda61da1e | -11.2104 | -46.2428 | 2026-10-07 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.0 |
| a6906bc4-1fe9-3eaf-967e-5f65ae98b52e | 3.1463 | -60.5937 | 2026-10-07 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1ca48e3d-e9ce-32ec-bbc0-24f98987cd2a | -7.7579 | -54.9499 | 2026-10-07 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| d24a574c-03bc-36e4-8ff0-593f531ca025 | -11.8508 | -43.5361 | 2026-10-07 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 292.3 |
| f7251198-381a-34ac-aa7b-749da11b1594 | -8.3022 | -44.1467 | 2026-10-07 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c609dc16-131c-3f47-a920-e81f5beea917 | -7.5756 | -46.7112 | 2026-10-07 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 3fe5aa5e-22d7-34a3-9e6c-1f0c0dfa0aeb | -12.2132 | -44.6991 | 2026-10-07 14:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 89182d9e-13f2-385a-8564-7596d406adff | -7.2816 | -46.1571 | 2026-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 702cff4f-34e2-3d33-afdc-393eebb9a348 | -8.2184 | -46.3396 | 2026-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 8132d448-1995-3871-9bb9-30e4878a01f6 | -7.5571 | -46.6906 | 2026-10-07 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 4a08cb77-8893-3c6e-b095-f571102aaab1 | -7.5847 | -55.7205 | 2026-10-07 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 04a6f4f2-f583-34ab-8b3b-d0bb379aa30d | -6.9143 | -43.6583 | 2026-10-07 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 1afbc8bb-0c2b-39a4-ad80-4e14aef1a450 | -11.7143 | -43.652 | 2026-10-07 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| a8c6ee8d-cab9-3711-81f2-981ba3af5edb | -7.7595 | -43.8092 | 2026-10-07 14:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| 09c4e879-ac03-3395-bf06-bcffda01ae1d | 2.1267 | -50.8371 | 2026-10-07 14:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ade7b856-2798-3418-b371-7b5eba0a9f4a | -11.3745 | -46.6948 | 2026-10-07 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 5a8244be-85e8-38e3-bc35-473831621ad4 | -7.5284 | -45.8885 | 2026-10-07 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 85067a2d-5578-3c5b-91bf-d37ab963b174 | -8.5844 | -45.6729 | 2026-10-07 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 2ef3ca75-66e4-34dc-b861-b8be45647ce1 | -8.6033 | -45.6709 | 2026-10-07 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 946fad67-16b3-3f5a-93e5-dfb133047822 | -7.8146 | -45.5009 | 2026-10-07 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 2bc66ded-c51b-35bb-8345-5d8455db9b89 | -7.3475 | -45.2725 | 2026-10-07 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 2ec7acab-90f4-30db-901a-d133cab89dd4 | -6.9925 | -45.1223 | 2026-10-07 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 4d7442ee-43c4-30db-9b8b-0c8ad2921bf9 | -11.8216 | -47.3521 | 2026-10-07 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 3ab034a0-63f6-3e81-9b95-f533efa9304f | -9.4492 | -44.6167 | 2026-10-07 14:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 12564e41-ff8b-3bee-877e-41128f22b000 | -11.0935 | -47.6019 | 2026-10-07 14:10:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c2c499c3-a0db-37c5-b010-a686892069df | -9.432 | -45.8293 | 2026-10-07 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| bbbc3f20-5e34-317c-88aa-b82ed200259c | -11.1051 | -45.689 | 2026-10-07 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 6d3fc80b-2df9-30a2-8728-6026a31076c9 | -6.6943 | -44.9431 | 2026-10-07 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f0f2ba30-f1f1-3bbb-8dbd-a079c17e40e5 | 3.1281 | -60.575 | 2026-10-07 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 0e307e29-9070-334b-86e3-47fb56384688 | -7.3935 | -46.2144 | 2026-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| f47fae1f-940a-3a96-be71-6232522b9d02 | -7.7579 | -54.9499 | 2026-10-07 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e9471ac3-0072-3b28-b164-625c4d74f947 | -10.5287 | -47.2711 | 2026-10-07 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| d990fbe8-deae-3f2e-84eb-aad7f7ec2966 | -6.694 | -44.9658 | 2026-10-07 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 9356415e-ab6b-3d05-9162-a16ea6429199 | -6.4756 | -52.8142 | 2026-10-07 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 70efcbb3-97a4-318d-a91b-a9e288c8864a | -7.8973 | -72.349 | 2026-10-07 14:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 7b15d8ce-6115-321d-92b8-311dbb93a2ef | -11.2295 | -46.2403 | 2026-10-07 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 5c90da80-0a05-3f51-8ffd-627ee87ce0cc | 3.0733 | -60.576 | 2026-10-07 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1dee3e52-3fd1-3e20-ae07-64a44d43ecac | 1.5283 | -56.0227 | 2026-10-07 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 7ffe8e87-a3f0-3eb2-8620-7c8dbe3caed9 | -8.8364 | -62.4321 | 2026-10-07 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 3400ff8b-2c62-3f37-b8df-a5a2fc4fda14 | -6.9328 | -43.6799 | 2026-10-07 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 238.2 |
| 249ac002-ee9b-3937-9af0-a258779521c2 | -6.935 | -45.2408 | 2026-10-07 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 1b48c11f-730d-3011-bb82-d63accde67c1 | -15.9672 | -40.6923 | 2026-10-07 14:10:00 | GOES-19 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| f7ce9e58-3aeb-3586-80c8-668128fdad7e | -7.8146 | -45.5009 | 2026-10-07 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 6556dbab-1b12-342e-a25e-ed73f32a93d9 | -7.5847 | -55.7205 | 2026-10-07 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 3f7e7b48-5640-30b6-99b0-572278cff1ca | -11.7139 | -43.6757 | 2026-10-07 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| aff9aa42-1c3f-3995-a139-fcde3b482c66 | -7.5756 | -46.7112 | 2026-10-07 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| cc56108f-8931-365d-8942-98f650586ca1 | -7.2 | -55.1026 | 2026-10-07 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| a99034ec-22cf-30f0-8eca-493d7e8e85ca | -8.5844 | -45.6729 | 2026-10-07 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| f987412c-cd66-3180-a52e-db164e1ab942 | 3.1463 | -60.5937 | 2026-10-07 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 58c4b724-7ead-3d4a-ba45-1640456ec214 | -11.7943 | -46.7056 | 2026-10-07 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| fc44fecf-4f63-3f5b-ae58-d59f86a3eda9 | -11.8315 | -43.5391 | 2026-10-07 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 9ef74de5-7240-38d8-bd18-d3d2306db8a9 | -12.2136 | -44.6758 | 2026-10-07 14:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| bcc905d1-7243-366a-8beb-9e98daea3415 | -7.5568 | -46.7128 | 2026-10-07 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 7c90a7e5-d3c5-3249-8645-9137685975bb | -7.3677 | -54.9929 | 2026-10-07 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| c27aa887-76f0-38f5-bdc2-076eed84ceee | -11.3745 | -46.6948 | 2026-10-07 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 805ca851-36b7-335c-8c48-73c497c0c1d1 | -11.8311 | -43.5628 | 2026-10-07 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.6 |
| ab633dd5-9364-32fe-ba3c-e75ad0e32e73 | -7.8789 | -72.3674 | 2026-10-07 14:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f0ff5b84-fa84-36ca-a476-cda59a2255fc | -7.5284 | -45.8885 | 2026-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 88a76d48-2315-33bf-a84f-f8dd558bffe3 | -12.2132 | -44.6991 | 2026-10-07 14:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 0166f194-3566-3c1c-a6dc-2506bda4c0ee | -7.5571 | -46.6906 | 2026-10-07 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7508b8f6-a92d-30f3-87dc-5a1ce637b68e | -7.8789 | -72.3492 | 2026-10-07 14:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 115.4 |
| df3bd866-4c6e-3b89-8eb1-d01d42362d38 | -7.3676 | -55.013 | 2026-10-07 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 291c473e-cd1c-3119-9741-b3ab7915a3f6 | -7.8676 | -44.2153 | 2026-10-07 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| ccfc763c-2c5e-3a01-a018-feec5c23ade7 | -7.349 | -55.014 | 2026-10-07 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |


[Clique aqui para ver as próximas entradas](README132.md)
