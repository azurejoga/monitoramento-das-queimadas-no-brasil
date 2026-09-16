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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04913510-38b8-349c-ba1c-92a46d7dba92 | -6.77 | -48.67 | 2026-09-16 14:15:00 | MSG-03 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d6da46cc-e377-3947-90dc-5a58a2e8f72c | -11.4167 | -51.4371 | 2026-09-16 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| bbe0f746-9710-3bf3-99c7-602be64c8764 | -9.3892 | -60.3215 | 2026-09-16 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 57f3603e-a219-3f97-8fab-983094efb589 | -8.5428 | -44.5132 | 2026-09-16 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 648.0 |
| 0cd1d521-2e74-3dce-abfd-42c2cd49d2b3 | -5.6311 | -51.6858 | 2026-09-16 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| feadf337-851b-3079-96ca-d9041474e8cb | -9.1337 | -65.844 | 2026-09-16 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 7eb3906f-344a-37b5-8a06-b91e0d59e8db | -6.75 | -58.8043 | 2026-09-16 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d6bbca04-8714-3427-b6d9-3290a301bc17 | -10.5975 | -47.7505 | 2026-09-16 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 85da9c56-a1b3-3979-a9e8-15665a036884 | -13.287 | -51.2832 | 2026-09-16 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| bfb8c16a-6b7c-3071-af27-720afbc68000 | -13.2239 | -51.6318 | 2026-09-16 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 656bb00a-a2bc-3021-a4e5-afe54126ed92 | -7.3561 | -44.4956 | 2026-09-16 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 881e3e86-c625-3874-ac9a-8b8ea0b08bc9 | -11.417 | -51.416 | 2026-09-16 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| e6cb1f12-9a84-3ae9-b346-200ae5a2d4b0 | -5.7429 | -57.6009 | 2026-09-16 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4e505762-b1fc-30dd-973d-aced3e796a00 | -2.6784 | -57.5504 | 2026-09-16 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 38d20bc0-40d3-336e-892f-e6238d7f02a8 | -6.8032 | -59.1693 | 2026-09-16 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 586.2 |
| 2eaa682b-608c-3c15-ab94-63bdc4bb125c | -8.6188 | -44.4819 | 2026-09-16 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 345.6 |
| 53410887-08f4-3b0b-9287-8bdfcc40c8d3 | -2.6783 | -57.6087 | 2026-09-16 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 858b24e4-892b-3109-865d-dd632af1a901 | -12.3277 | -47.9513 | 2026-09-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 305.8 |
| a6b5be34-e2e0-31fc-9e89-b4c786012f1c | -9.762 | -46.5796 | 2026-09-16 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| a571ffbe-488a-37cb-9dc6-bc8f5b3b0716 | -10.0293 | -52.12 | 2026-09-16 14:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| b8c43e12-700c-3751-af69-83311b200ff3 | -11.6315 | -47.3105 | 2026-09-16 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 8444a3a3-14af-3e45-b10d-77e960e6ee1d | -10.9107 | -54.0045 | 2026-09-16 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| c28ebbea-78f4-30e3-96bc-91e07aba70bc | -13.2235 | -51.6531 | 2026-09-16 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 08599892-be3d-3fe2-b52b-68a25d56c84c | -6.7703 | -48.6792 | 2026-09-16 14:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 58.3 |
| cf34e8a2-5754-3451-a54b-0f601230a9bf | -10.8916 | -54.0267 | 2026-09-16 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 794fc3ac-1d6d-3d14-bbfa-834ffdcbde91 | -12.1453 | -44.2195 | 2026-09-16 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 7c17b342-4f40-37f8-93c9-61248e2c6003 | -9.7793 | -60.4744 | 2026-09-16 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 7862a324-8db3-37b6-9d31-ce2984351b01 | -12.3273 | -47.9735 | 2026-09-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 6a514632-d329-3440-a8ce-76da0c49e297 | -13.2047 | -51.6342 | 2026-09-16 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| ada4036d-1888-3538-b6f4-57d70dd0ad30 | -11.8941 | -47.5876 | 2026-09-16 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 06125bc7-362d-3755-a37b-52443757531f | -13.2678 | -51.2856 | 2026-09-16 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 24d7b6dc-b112-3353-9b0d-cdc39aaeb337 | -13.2874 | -51.2618 | 2026-09-16 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| df17d5c2-02af-3811-9bd4-38ea498623c8 | -8.6184 | -44.5049 | 2026-09-16 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 27b7549a-ad5a-38cc-a48f-eecf74aaa8a7 | -11.9033 | -43.8112 | 2026-09-16 14:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 78d5d219-b295-3d8a-899c-8174d610a427 | -10.6827 | -54.1679 | 2026-09-16 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 30b6282f-2a06-336e-b554-0e5ab8bef561 | -9.3893 | -60.3022 | 2026-09-16 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fce4ea02-43e9-38e2-9a66-61cc345f0178 | -10.3955 | -58.2962 | 2026-09-16 14:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 194.7 |
| 529d1c34-f750-390f-a507-09bab8972f1f | -10.8571 | -50.8183 | 2026-09-16 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 178.1 |
| e99babbf-d9f5-3eff-8c82-6e055ad46c8d | -14.4479 | -40.8379 | 2026-09-16 14:20:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 144.3 |
| 39e62ef4-268f-3f41-923a-b18a076dbb92 | -10.6641 | -54.1491 | 2026-09-16 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 73abca78-03e6-35f5-83a7-23e1adae14e8 | -10.0988 | -45.5685 | 2026-09-16 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| d2094dba-4f91-3952-9ba5-d5aff72d5e3d | -6.7705 | -48.6577 | 2026-09-16 14:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 143.9 |
| d17c307e-5c5e-3703-8ec0-ca7cfc5c671d | -12.3081 | -47.9761 | 2026-09-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 543f3ade-e4a8-3848-b78b-02fe51d1c726 | -15.6557 | -52.7366 | 2026-09-16 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 9cf8f51a-8e81-3200-be23-806e30af4728 | -10.3766 | -58.3171 | 2026-09-16 14:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| a778bb64-d19d-3d61-9ac7-82574d57876f | -1.6206 | -55.5679 | 2026-09-16 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 2d3acfd8-9fd8-3908-92d5-905837003ea2 | -5.144 | -55.9345 | 2026-09-16 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 6eaa2db0-edad-37c7-8e85-6e78cf75bf67 | -9.0962 | -65.9384 | 2026-09-16 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 11884bf6-086b-30f3-be0a-eda81b88e4eb | -12.126 | -44.2225 | 2026-09-16 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 204.7 |
| e385f8ff-09cb-3b0f-847c-188cb8700196 | -12.4145 | -48.4701 | 2026-09-16 14:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b5e5c59a-bcd4-39f1-85aa-05d70838c40c | -12.0488 | -47.4777 | 2026-09-16 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 83779420-e2d9-32f2-9e0b-d66fdf8fc947 | -3.7128 | -60.6211 | 2026-09-16 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 3844e2cd-09bf-3725-9d6a-aeb6d75ee0d1 | -13.5127 | -51.5532 | 2026-09-16 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 7f208bf9-e75d-389a-a34b-c95bac85b4db | -3.4461 | -58.0005 | 2026-09-16 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 57983bec-3219-3456-8495-38a42ab2234e | -13.3059 | -51.3022 | 2026-09-16 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| cd48db6c-dbf1-3a3b-8738-a41ca59964e4 | -10.3953 | -58.3159 | 2026-09-16 14:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 258.7 |
| 77672bad-2ca3-3904-a9ce-00389dba0884 | -10.1179 | -45.5662 | 2026-09-16 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 431.1 |
| de255508-b803-3ff6-8288-c1a1135f43f2 | -6.3147 | -41.6807 | 2026-09-16 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 1d7c06e8-37cb-3058-af07-9f62aaf91afd | -8.6191 | -44.4588 | 2026-09-16 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 177.7 |
| dc629eb9-f076-34c5-9952-2a15fd785275 | -9.2311 | -46.7055 | 2026-09-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 7c6eb74f-7b3c-3482-9187-e335c91927a9 | -9.0866 | -61.0287 | 2026-09-16 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9a005a8d-3398-3ca3-9d7b-9f5874c3bdc2 | -6.7684 | -58.8035 | 2026-09-16 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a6e06209-427c-3573-b7af-f41af60ff2cf | -9.7322 | -64.9067 | 2026-09-16 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 85af8f9a-49e7-33be-bf4d-b4d8c1042c9d | -6.8216 | -59.1686 | 2026-09-16 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 262.1 |
| b960b23e-8907-3eb1-b6bf-008937192dd4 | -10.6829 | -54.1475 | 2026-09-16 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d571bd5a-86c6-3ce2-b23f-0be8d1e0a09d | -9.7608 | -60.4561 | 2026-09-16 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 2d6d8ffe-f744-3d2b-adbf-b1b76dabdacf | -7.9831 | -44.0183 | 2026-09-16 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 158.8 |
| c672f655-c50e-383b-be27-791e3858eb64 | -10.876 | -50.8163 | 2026-09-16 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| b347f678-a7bc-3c39-808b-daf8a40e9150 | -11.5432 | -46.8745 | 2026-09-16 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 37312f5b-c76c-373a-ae8e-5a531cac2dc3 | -6.174 | -53.524 | 2026-09-16 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 10e385f7-7a83-394d-9594-dd0c46d9075a | -11.5436 | -46.852 | 2026-09-16 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 77a764e8-e454-3ea3-b6c8-26b3e16247d4 | -2.6783 | -57.5893 | 2026-09-16 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ba89121d-5567-3537-b993-7688a02406d2 | -12.1265 | -44.199 | 2026-09-16 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 9f557d9b-aeb1-3b54-8e2f-cc92b173a4f9 | -8.5617 | -44.5112 | 2026-09-16 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 337.9 |
| 4a6346d8-c3f9-3bf9-a323-273a8a5761d1 | -3.1174 | -57.6779 | 2026-09-16 14:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| af03fdb0-dae0-3504-940e-ce234b43145c | -10.8919 | -54.0062 | 2026-09-16 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 0e63f96d-b79f-355b-8178-10cd4c88d58a | -13.1855 | -51.6365 | 2026-09-16 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 71124299-e884-3129-b165-d1bd8c47edf0 | -6.6021 | -58.849 | 2026-09-16 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 552f8e3e-1995-3c61-b919-9689242f67e1 | -8.5431 | -44.4902 | 2026-09-16 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 7a0b5a2d-d16b-3846-b86e-393e61dcd416 | -6.1159 | -44.6932 | 2026-09-16 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a25f0d60-c4a7-3d49-94f9-e5bb4c8573a4 | -6.7703 | -48.6792 | 2026-09-16 14:30:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 5f5ea8e5-9405-3e9d-b732-32b38eb9650b | -10.6641 | -54.1491 | 2026-09-16 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 602c3cc2-f10e-3b25-9d7b-5bec8fe31edf | -9.7322 | -64.9067 | 2026-09-16 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| a8891343-0c44-309d-b978-07e1aa12cf02 | -15.6557 | -52.7366 | 2026-09-16 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| cdf0dd1d-70e4-374f-9c59-dd1da883ac82 | -9.3707 | -60.3032 | 2026-09-16 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c02a2586-4d97-3523-a511-89e42d80a36a | 3.823 | -60.4479 | 2026-09-16 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 582222dd-3dfb-38a1-a924-6aed48ce0f74 | -9.0962 | -65.9384 | 2026-09-16 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9c31ad93-32be-332d-b5df-643da9680c00 | 4.0606 | -60.5188 | 2026-09-16 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 16f36ca5-1a5d-34e0-b40a-4f57fc6ebea5 | -5.7429 | -57.6009 | 2026-09-16 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 3b1da85e-0999-3e9c-b920-f7e664f0e2c6 | -9.1337 | -65.844 | 2026-09-16 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 9a25870f-ff65-3410-ae1c-904d4df46cef | -6.3147 | -41.6807 | 2026-09-16 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 118.6 |
| e8960273-1bf4-3bcd-9bb2-b81a6b3b8a60 | -9.5912 | -46.6213 | 2026-09-16 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 4f34d01a-5415-3ffa-a767-49136358b560 | -9.0866 | -61.0287 | 2026-09-16 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| e70462e6-450c-3a1f-a0d8-07434e5d9663 | -10.6827 | -54.1679 | 2026-09-16 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b8fa248e-2906-3be7-8db1-b6463c1ba9e4 | -9.7687 | -46.1067 | 2026-09-16 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| f8ef42dd-4379-3b8a-ace9-85386d5a88a2 | -13.3387 | -51.6389 | 2026-09-16 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| b29d01df-7da9-3bde-a273-c36824f7d0f1 | -12.3273 | -47.9735 | 2026-09-16 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| b69431cb-e9bc-3e27-9011-1797fa194c1c | -8.8459 | -45.8713 | 2026-09-16 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 3382942c-3ea7-3f46-954f-16618322474a | -7.3564 | -44.4726 | 2026-09-16 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 857264f6-73be-394a-9011-612e15b7f63a | -5.1255 | -55.955 | 2026-09-16 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |


[Clique aqui para ver as próximas entradas](README76.md)
