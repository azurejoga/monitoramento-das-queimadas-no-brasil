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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43e3f79d-ac82-3976-b2fe-5974f5913db8 | -12.7272 | -54.1988 | 2026-06-05 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 8315db47-d8ac-3288-8c97-59f36e337368 | -14.3983 | -45.5657 | 2026-06-05 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 5ff2c416-8379-39aa-8f77-9c3f95260d66 | -14.2118 | -57.4299 | 2026-06-05 14:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| cd1b920b-1b2b-3e23-b47f-57010b4d3a85 | -12.4464 | -58.4825 | 2026-06-05 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| e4a4ca4f-f223-3872-ada1-dd299fee434a | -10.8573 | -53.7425 | 2026-06-05 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| cb0abf45-03ae-359b-a02f-93bb0f168169 | -8.9985 | -45.7418 | 2026-06-05 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| b134a784-abf3-3bbb-bc7b-defdf75bfc26 | -12.7269 | -54.2195 | 2026-06-05 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d9e62d2d-eb3a-3dae-8c1b-c0d07c4bd01b | -14.2121 | -57.4098 | 2026-06-05 14:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 2108252e-d7f8-33c2-9757-d690a4d62131 | -12.4473 | -58.4033 | 2026-06-05 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| a747e030-414c-3e7b-a0fa-1670989d243a | -10.8573 | -53.7425 | 2026-06-05 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 94481d9a-9666-31b1-8982-7bb5f3acf917 | -14.2118 | -57.4299 | 2026-06-05 14:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 3411a6a0-a224-30e4-90c4-d0b74403bd69 | -11.6329 | -55.1844 | 2026-06-05 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| b6f12bb3-69ea-3257-a7d7-0907f4206e91 | -12.7272 | -54.1988 | 2026-06-05 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 7cfc8ee0-eec4-3ebf-90fc-212c4236879c | -12.5103 | -46.2863 | 2026-06-05 14:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e3182e4a-b6be-30c2-a516-7b6dff117802 | -12.4473 | -58.4033 | 2026-06-05 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| fa19ee91-08ed-3de6-a238-bc02fdf724ab | -12.0097 | -45.3315 | 2026-06-05 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| b3cdef4e-570f-33af-9527-b05e50398f75 | -8.9985 | -45.7418 | 2026-06-05 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 7f49dfef-ef36-3819-8d3c-25a0c5a3102e | -14.3983 | -45.5657 | 2026-06-05 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 68234ba0-9e76-3a4f-a882-80a356b91040 | -12.4464 | -58.4825 | 2026-06-05 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 28dc1873-c6ff-35a4-adb5-e9490689e122 | -10.9882 | -47.0362 | 2026-06-05 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 90b0f9c6-4790-3732-aa7d-ce8b52a1266e | -12.0093 | -45.3546 | 2026-06-05 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c10d1085-1600-3294-af0e-334624e04fa9 | -12.7463 | -54.1969 | 2026-06-05 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 226d6bf9-5a12-3d2d-9c6e-e872ff813647 | -10.9882 | -47.0362 | 2026-06-05 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 605f29cf-391d-3920-9906-7d5b58fe15fc | -8.9985 | -45.7418 | 2026-06-05 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| afe31847-2ba1-3de1-98a4-b3e689a307c6 | -12.0097 | -45.3315 | 2026-06-05 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 7ef9bcb3-aa3c-30a2-ac09-fbb4e95ae572 | -14.3983 | -45.5657 | 2026-06-05 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 21391219-0a0b-30fc-97d5-539308e1f255 | -10.6802 | -49.9187 | 2026-06-05 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ecdb7d60-31f9-377c-acdc-340cff287e3a | -14.2118 | -57.4299 | 2026-06-05 14:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 3171fd56-22d5-3db3-9017-15f400028195 | -12.4464 | -58.4825 | 2026-06-05 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 156.3 |
| e6ccc97f-55fd-3be5-ba79-e9583283321a | -10.8573 | -53.7425 | 2026-06-05 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| cdfe5dc9-53c9-38f5-bbc2-53c1b9b7c366 | -12.7272 | -54.1988 | 2026-06-05 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| ca10b73d-42f3-339f-9205-f16b694cfa14 | -12.4274 | -58.484 | 2026-06-05 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 4dff1ebd-e75b-392c-a1c1-117c83d270e1 | -11.6329 | -55.1844 | 2026-06-05 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 3c6cf53d-ae52-3c83-adb0-2642e1bb7b72 | -12.4473 | -58.4033 | 2026-06-05 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 402fab26-6346-3777-8106-61ddf382b41d | -10.9882 | -47.0362 | 2026-06-05 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 58ef0914-72ad-3835-8e8d-31d9cf22436a | -12.4462 | -58.5023 | 2026-06-05 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 5eeb4abd-682b-391a-b35f-ad50a6e7e45e | -12.7272 | -54.1988 | 2026-06-05 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 9c7c3163-92a5-3531-811a-01679758ee9a | -11.0073 | -47.0338 | 2026-06-05 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 785001aa-3e05-3ce4-9042-0772e4613803 | -10.6802 | -49.9187 | 2026-06-05 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 3fc6eb73-748e-3618-b6e7-02096325197a | -14.2118 | -57.4299 | 2026-06-05 14:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| b62a0611-1578-30ee-95c7-e28bdaf3568f | -12.5103 | -46.2863 | 2026-06-05 14:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 2b0e9575-79af-3f6e-891c-9fcf219b0568 | -10.8573 | -53.7425 | 2026-06-05 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| fa42136b-d9ab-346f-8f8a-e2f7702b21ee | -8.9985 | -45.7418 | 2026-06-05 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 72bd408f-763d-3045-807a-919ab643acd8 | -11.6329 | -55.1844 | 2026-06-05 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e5249b1c-779f-346c-b726-7db60e9d04ee | -12.0097 | -45.3315 | 2026-06-05 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1d33752d-995a-39ee-b58d-eb7e1fb1576b | -12.7463 | -54.1969 | 2026-06-05 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 9b73718f-16b7-3667-8c98-bd72b5376cbd | -10.9695 | -47.0163 | 2026-06-05 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 34475a67-07d6-3dfb-a000-aa6367521a81 | -12.0097 | -45.3315 | 2026-06-05 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b6951d00-996f-33f5-a878-8d35eb2d10a4 | -12.4274 | -58.484 | 2026-06-05 14:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 60e16b6f-31ea-3e67-9eaf-8730ccc6e76c | -10.8573 | -53.7425 | 2026-06-05 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| e5388c78-4095-3aba-9a30-7f20ffcaedb3 | -8.9985 | -45.7418 | 2026-06-05 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 7466fee8-0317-3fb0-8ede-08c4661796d4 | -13.5523 | -55.2428 | 2026-06-05 14:50:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 07676bdd-5413-3bbe-aa5f-a2e4f06f1e44 | -11.6329 | -55.1844 | 2026-06-05 14:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 61711e83-0701-3aeb-9075-7ea81738388c | -12.7272 | -54.1988 | 2026-06-05 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| fe60bed4-2504-3b26-be2f-4bfe86f5f6a4 | -10.9695 | -47.0163 | 2026-06-05 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| f898745f-0a3c-3878-bbc8-4bb15d02e981 | -12.7272 | -54.1988 | 2026-06-05 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 6a0e8195-5a16-3bf7-9a5d-6a9e82ae982d | -10.9695 | -47.0163 | 2026-06-05 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| c8fe91e1-3c59-330c-80b3-29122c928a66 | -14.2118 | -57.4299 | 2026-06-05 15:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| df6cfdfe-54eb-3369-82d2-0db1fce06234 | -11.6329 | -55.1844 | 2026-06-05 15:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 38e8d1a3-f358-39e9-98f9-4c93205af577 | -12.4274 | -58.484 | 2026-06-05 15:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| aa479109-ed7f-38e7-ba3e-bf7bf2573c1d | -14.1106 | -59.4157 | 2026-06-05 15:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| a602ac83-cceb-34cf-84ac-678c2e6dd94a | -8.9985 | -45.7418 | 2026-06-05 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 2ba75c42-c127-379b-a838-c4e52e694add | -10.8573 | -53.7425 | 2026-06-05 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 2bd1f6f7-73bc-35fd-9847-c56c3fce7e9e | -11.6329 | -55.1844 | 2026-06-05 15:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 26cc624d-1b0d-3bf1-a3bc-b57b05312711 | -12.7272 | -54.1988 | 2026-06-05 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.2 |
| f1506de9-91f4-362c-8b5f-9e0fe01327e7 | -14.1106 | -59.4157 | 2026-06-05 15:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a16b4af4-2919-3ff6-99a9-eced50e17807 | -10.9882 | -47.0362 | 2026-06-05 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 64ac02ca-68e1-3bd0-a133-6eb6795ad2bd | -12.7269 | -54.2195 | 2026-06-05 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| bd9532ef-5647-3715-80f7-55ae890fcb8f | -12.0923 | -51.9966 | 2026-06-05 15:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 30b0eb5d-5323-3845-8b46-277a1d3a2906 | -10.8573 | -53.7425 | 2026-06-05 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| fa640f19-9233-3771-af54-77358394c4aa | -8.9985 | -45.7418 | 2026-06-05 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.8 |
| bff03ce0-11e0-3c03-be1f-edacf18f6d85 | -8.9985 | -45.7418 | 2026-06-05 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 2e6755eb-ec78-38ff-9ef1-cd0ca840547c | -12.7272 | -54.1988 | 2026-06-05 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| f4a71c3b-af22-33ea-a3dd-91d44a0afe09 | -14.1106 | -59.4157 | 2026-06-05 15:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1787858c-df1e-38c4-a90f-4304d3d9059c | -10.9882 | -47.0362 | 2026-06-05 15:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 06a4a584-f713-304d-91bf-265817fad749 | -10.8573 | -53.7425 | 2026-06-05 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 6738c25d-5a93-3b40-8e8c-92558113998f | -12.0923 | -51.9966 | 2026-06-05 15:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| a7db158b-e62a-3f43-a61f-217b1bb9dd24 | -12.0097 | -45.3315 | 2026-06-05 15:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| f62daff1-1dc7-3375-b3b3-5a55eb0a6c4f | -12.5103 | -46.2863 | 2026-06-05 15:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 14536f98-a82b-3b14-b782-d20de4dd6abb | -16.5973 | -58.2365 | 2026-06-05 15:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 53d3b40e-3534-3e61-9ecc-81318553eeed | -12.7463 | -54.1969 | 2026-06-05 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| a7b104c2-755c-3835-8cda-edda8d782cef | -12.0097 | -45.3315 | 2026-06-05 15:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 63db408a-802b-3542-83a2-bdd09b16c27c | -10.8573 | -53.7425 | 2026-06-05 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 49c33660-e325-30ab-b6a9-e36d07a36495 | -12.0923 | -51.9966 | 2026-06-05 15:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 948ec737-22bf-329b-aa2c-cb4aadf295f3 | -16.5973 | -58.2365 | 2026-06-05 15:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| f0f12d39-f8ff-3817-976b-876a6fe732fd | -10.9882 | -47.0362 | 2026-06-05 15:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 4cea876c-67e2-3962-bf4b-0ee820187f9a | -12.7272 | -54.1988 | 2026-06-05 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 99c83638-1c44-3e77-81b2-56e1432fb405 | -8.9985 | -45.7418 | 2026-06-05 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| ea024fef-7daf-3be7-9efd-f6934e802f4e | -16.5973 | -58.2365 | 2026-06-05 15:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| cf77c715-e817-393e-a588-3e48c4ea5c22 | -12.0923 | -51.9966 | 2026-06-05 15:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| c7055b90-6124-34a3-b313-3747923120b3 | -12.0097 | -45.3315 | 2026-06-05 15:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 49990246-cce6-3d15-adb6-840ea5d3f655 | -8.9985 | -45.7418 | 2026-06-05 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 6e4cfd39-2540-3bf0-83c3-b94125cef4b8 | -10.8573 | -53.7425 | 2026-06-05 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| e4f83948-b719-3ace-aae2-c4d79d878823 | -12.7272 | -54.1988 | 2026-06-05 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 1fd0c2c6-0e76-3742-9b73-565807e80a9b | -11.0073 | -47.0338 | 2026-06-05 15:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 46e86f9d-8dda-3281-8cf9-8f957e1af514 | -10.9882 | -47.0362 | 2026-06-05 15:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 9372ca13-690f-3535-9723-cd3a900e708f | -12.7272 | -54.1988 | 2026-06-05 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 660a1fb4-4fa6-3a77-ae23-4949e92583bc | -12.0923 | -51.9966 | 2026-06-05 15:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 5e28d595-ba27-326d-9353-e178a30b9328 | -11.0073 | -47.0338 | 2026-06-05 15:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d32ae7ff-33f0-35db-89de-cc4d77bb8a68 | -16.5973 | -58.2365 | 2026-06-05 15:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |


[Clique aqui para ver as próximas entradas](README18.md)
