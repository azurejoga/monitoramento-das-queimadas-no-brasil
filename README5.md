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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c70e0c1-029d-3d52-a875-35f1c7945ccc | -2.8196 | -53.0629 | 2024-12-03 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| e96511c0-d262-3db0-923c-6ee91da81055 | -4.5589 | -42.9289 | 2024-12-03 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 83d1a9ad-0c47-3a36-8572-c8da73a85deb | -1.7361 | -52.6162 | 2024-12-03 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 95e56db7-51e6-30e5-97c2-a35be607480c | -5.8009 | -46.4941 | 2024-12-03 00:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| ef840cd5-c6ee-3fb2-9be5-ba5cbfb915eb | -4.5403 | -42.9066 | 2024-12-03 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4e4ae6e4-6c0e-34f2-a2e5-4fdd60ce26ba | -3.3421 | -51.2215 | 2024-12-03 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 915db7c0-2c3b-349f-a09b-26f9d0fa6f8b | -1.736 | -52.657 | 2024-12-03 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 328bd5cd-8742-3dba-85ee-993ddd3c253b | -4.5591 | -42.9054 | 2024-12-03 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| bbbf0d67-872d-3c00-a177-6378cec374d0 | -6.1229 | -43.9578 | 2024-12-03 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f829ec8b-3338-3360-8e98-8fd100a77944 | -3.0761 | -53.3606 | 2024-12-03 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 0fc5b632-3201-3fda-8765-12afe0e61bbd | -3.2775 | -53.6181 | 2024-12-03 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| eb6c456e-bdca-3970-942d-7970748b2615 | -3.259 | -53.659 | 2024-12-03 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 22e50ed6-2f2e-369d-b68a-441f5acd624f | -3.1133 | -53.2381 | 2024-12-03 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c4d4fc77-2d02-3df7-981c-4ba8fa6287f7 | -3.3422 | -51.2007 | 2024-12-03 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| ee8c8ad2-6364-3320-a08f-48cb18bf1b56 | -2.3645 | -45.7031 | 2024-12-03 00:30:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 186.7 |
| b118764f-4424-3d9c-9c1e-6914ac277da2 | -1.7541 | -52.7993 | 2024-12-03 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 6292c1ef-225f-3bf3-ac1a-41ea22c3e8ce | -4.7484 | -45.1271 | 2024-12-03 00:30:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 7d8e6bf9-d7de-3c96-9975-56bbaea111c7 | -5.118 | -43.2198 | 2024-12-03 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| f4f4b913-822e-3637-8bf1-aa68710a931b | -2.6644 | -44.9743 | 2024-12-03 00:30:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 7c6b0ff4-b6fd-338d-be8b-0247379d490a | -2.8012 | -53.0633 | 2024-12-03 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 4a1b373e-ed21-3bf0-869c-6b88b6c1efc5 | -2.3644 | -45.7254 | 2024-12-03 00:30:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 31d646ee-77d5-3d68-be54-2ba4ceeab2d2 | -2.8212 | -52.5741 | 2024-12-03 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 21a00b7c-fb75-3cff-8e77-ba23f4f0f1ff | -3.6096 | -45.5908 | 2024-12-03 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 81dc6ad9-bb3b-3e2c-b816-9fd4dd4b67b1 | -3.0945 | -53.3601 | 2024-12-03 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2f42227a-aa97-3ccc-81cd-954cb1901eeb | -1.7541 | -52.7789 | 2024-12-03 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| f3c883a1-0a5d-3bc3-9169-1cf512ed6d8c | -5.8195 | -46.4929 | 2024-12-03 00:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 4919351d-48ac-3dc9-abf6-38de2622573c | -4.7485 | -45.1044 | 2024-12-03 00:30:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| b701b03f-5492-370a-a113-17938938b9f6 | -4.1684 | -48.5937 | 2024-12-03 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 357ffe6a-1915-36cf-b9fb-8333673f1569 | -5.8197 | -46.4706 | 2024-12-03 00:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| cf400033-4b90-3d2e-b49f-e48ee894f5cf | -3.0949 | -53.2385 | 2024-12-03 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 815c47dc-3adb-3202-81dc-16d9dc322f37 | -4.4025 | -49.7774 | 2024-12-03 00:30:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 48d043b2-0b23-330c-b81f-7ac596b8c10f | -2.0271 | -53.9477 | 2024-12-03 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 523951d0-39c2-326f-b0a6-89c5f4540863 | -1.7361 | -52.6366 | 2024-12-03 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 96391e33-2db6-35dc-9376-059519cd7f2b | -1.0736 | -53.436 | 2024-12-03 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 4996f8fe-447a-3bbb-8055-59a500d08e97 | -9.6723 | -62.4335 | 2024-12-03 00:30:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 59bd8597-6282-31a7-a468-d08045d974d2 | -2.3459 | -45.7036 | 2024-12-03 00:30:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 742cb2d7-7b74-3573-a275-944dc53f3a6c | -3.2406 | -53.6595 | 2024-12-03 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ab61e3fc-03ac-35d4-b3ca-73fde9ade38d | -3.1092 | -54.036098 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bf2882d-75b2-3f74-b354-3c50dcc57624 | -3.2494 | -53.650398 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16ef4e0d-d549-3490-a329-8ad03649076d | -3.8553 | -52.264999 | 2024-12-03 00:37:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 971ba55e-7d51-31db-97d6-b0d0b5e6395a | -3.1052 | -53.742001 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b6a6529-8371-31fd-8bae-1211c1d9b64a | -3.9474 | -47.654099 | 2024-12-03 00:37:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1edcae3a-fbb2-3cd1-9056-872d0e4cdda7 | -3.2501 | -54.205399 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e362afe-0aa5-329f-9265-f5bbc7c9eb31 | -3.2919 | -53.655899 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3228f66a-a490-3e19-bddc-bfc97db6518d | -4.4672 | -46.349098 | 2024-12-03 00:37:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fdc63891-13c8-3b4b-9fef-82da52783191 | -2.7659 | -54.111599 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 801c514e-d6db-33b5-9a1a-e3e060b5b1f2 | -2.4668 | -53.696301 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c80e3b-c1f1-30b0-8846-c969f651860e | -1.7858 | -52.2733 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 424673b5-417f-315b-a4e6-bf158caadebc | -2.5786 | -47.4762 | 2024-12-03 00:37:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42bfe567-ca44-3a47-b4c7-6a9fe232763b | -3.4036 | -52.868301 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0212858-d04c-305f-a1fb-2dd8e31450ac | -6.0253 | -42.511501 | 2024-12-03 00:37:00 | METOP-B | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2e256637-0499-3694-86de-c46055617530 | -3.5397 | -49.375198 | 2024-12-03 00:37:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c17687df-c12d-33dd-af93-9d6daae8cd59 | -5.8075 | -46.4888 | 2024-12-03 00:37:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1693680a-bc8d-3d75-9453-41253361aca2 | -2.8803 | -54.1171 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 023dfad9-f802-3d0a-b8cf-c1cbd7db1ff3 | -3.7372 | -52.427399 | 2024-12-03 00:37:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 699b2d29-6ae1-369e-9b66-6a2f819664a0 | -2.8558 | -54.053799 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 909eef07-143f-3f9f-a87a-19331cc16b2d | -3.101 | -53.218201 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c56ffb96-182c-38aa-a2ed-88dd7167117c | -2.3804 | -53.6782 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 520eaa76-7c87-336b-b9a5-e3a03b090580 | -3.5466 | -50.173 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73030d7d-d3a8-3ede-8f22-1944ced2e8a1 | -0.351 | -51.578602 | 2024-12-03 00:37:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3785900c-6b9c-3ce2-8b3e-490bd89b3e2b | -2.7915 | -53.032501 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c550394-a4f1-3bd7-a89b-4704ee1613f1 | -2.846 | -54.1017 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec3e79c-9c4e-3a04-8734-136d57cd72f5 | -3.0717 | -51.259602 | 2024-12-03 00:37:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39ca856b-136b-3620-bf71-7bc74e0ac239 | -2.6362 | -53.349998 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85967e58-875d-374d-a658-60bb0d7ddd78 | -2.8142 | -53.041801 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bff38379-d68e-3258-bc02-8fc9294156be | -2.6919 | -52.910198 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f19727a1-e1c6-3968-bf8a-3090de96a901 | -5.7928 | -46.4697 | 2024-12-03 00:37:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f622570-c1e6-3cf2-a457-b0b3dc376bf5 | -3.5894 | -45.587002 | 2024-12-03 00:37:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86003e81-d942-3fa2-a82a-d61ab8d38387 | -3.8547 | -52.308201 | 2024-12-03 00:37:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63c28ea8-980c-3777-882e-3c9716083220 | -3.2449 | -50.614101 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7f52823-1400-3ef2-b9aa-238a948e70f9 | -2.4211 | -53.997799 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 501afb96-1ec3-3508-95bc-836d2cb79b0c | -1.0733 | -53.455399 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2cdc83b-bd04-3db1-a4c0-cc6d340aa20e | -3.5991 | -45.584801 | 2024-12-03 00:37:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3ab9efa-197c-3f61-a568-f1fef6462777 | -2.5443 | -53.399502 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec2ebaef-1142-3002-ab2d-1345f3aeed62 | -4.5648 | -45.103901 | 2024-12-03 00:37:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 22043595-1127-3e9d-9af6-ab89317dc7cf | -2.3438 | -45.706001 | 2024-12-03 00:37:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 61a0220c-ede3-360c-afcd-0b7eeaf9adbc | -3.1022 | -53.269199 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f22e5202-6697-3f62-b50f-80cf2db0eb72 | -2.869 | -54.020302 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e533850f-1e3b-39c6-914f-bae46405ba34 | -2.8221 | -52.572701 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 591e0588-4c5e-39bd-9ca5-458c735f92b1 | -3.7617 | -52.078201 | 2024-12-03 00:37:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79bc07ca-bec4-3f7a-8f77-8d8132c4315f | -2.4408 | -53.993401 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 408adbfd-bf1f-33a9-97b0-ca52a1529202 | -1.1767 | -53.410801 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bdc4374-4fd4-33b6-845c-9366e3d54284 | -3.2804 | -53.237099 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 215482ad-07da-3542-811d-8dbac0c3a26e | -2.4607 | -53.6236 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f828cf6-7acf-33de-bfd9-4d62e1ff6ff5 | -2.781 | -55.3307 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 583ee0c0-ac9f-3d30-b537-85066d1f6cff | -1.326 | -54.990299 | 2024-12-03 00:37:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 519030f7-94a0-39a2-bf80-351ad4fde2e9 | -3.2642 | -53.624699 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c90274d-ea57-343f-8788-7d6dd251c95d | -3.1216 | -50.252899 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77482f67-856f-35fa-acc6-c84f0e78f48b | -2.4586 | -53.705502 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62ec9b0e-99d6-368b-abc5-6f4bf8751a19 | -1.4426 | -54.821701 | 2024-12-03 00:37:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8bea903-8560-3305-9609-53655187dd09 | -3.5 | -50.0592 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a326ab2d-9ea2-39ae-bff2-e265803ace6f | -6.1021 | -43.967201 | 2024-12-03 00:37:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ea3e72f-6e6c-3cd8-81f0-eb1e0c9d4c0b | -2.8941 | -51.5676 | 2024-12-03 00:37:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 392f91f0-ab5b-368f-a522-871fb969d419 | -4.7951 | -44.991402 | 2024-12-03 00:37:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8d7fef4-94af-30f0-b9ca-036e927940df | -3.0357 | -54.075298 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff1ae172-3c72-3588-b443-49d35115a0b9 | -4.0395 | -46.809601 | 2024-12-03 00:37:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb2968c-879e-30fd-8ed5-3d7ec7994072 | -4.04 | -46.988701 | 2024-12-03 00:37:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4da73413-67f8-3396-b5e1-44d0cb8e8bea | -3.9379 | -49.945 | 2024-12-03 00:37:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dcd893e-0373-328b-a4de-4f17cd275c27 | -3.2544 | -53.6269 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae010915-2dcc-3926-b2c8-a26f20fa7f21 | -3.6465 | -52.6199 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
