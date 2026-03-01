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
| 68617d83-ab14-329d-bd9f-30e252c7f0c1 | 3.1662 | -59.9276 | 2026-03-01 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 588aaa6e-e290-3892-a3c5-8907babd1fb3 | 3.148 | -59.9279 | 2026-03-01 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 48.7 |
| a25468b9-4dc0-3089-bd83-9bb9cdd7ea94 | 2.8354 | -60.7694 | 2026-03-01 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 91cd290d-d015-3712-8285-4c357aa0d3a7 | 1.5046 | -59.9306 | 2026-03-01 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 0c5643c4-425e-37fe-a9e7-032b307cf407 | 1.4681 | -59.9309 | 2026-03-01 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 86a58377-4df0-362c-a06b-366eedea0de1 | 2.8354 | -60.7883 | 2026-03-01 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f4a32348-c687-3734-bc12-35a82e8f288e | 1.4864 | -59.9117 | 2026-03-01 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 194.3 |
| 3429d5ee-fff1-3a76-afad-5fe9e8f9317d | 3.1663 | -59.9085 | 2026-03-01 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 38220244-862e-3b4f-a8f0-a1c18ea3a7f9 | 1.5047 | -59.9116 | 2026-03-01 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 38ed839b-1068-323e-8675-d84230cd371e | 1.4864 | -59.9308 | 2026-03-01 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 63895165-6a94-39f4-a414-e96ee2f9fdf2 | 0.1914 | -60.4499 | 2026-03-01 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 776dd243-5817-3f9b-97fd-4d795642cf96 | 1.4682 | -59.9119 | 2026-03-01 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| e8224a6f-aa94-35ce-80c9-27208582d83f | -24.3514 | -49.43859 | 2026-03-01 00:02:00 | TERRA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 33.2 |
| 61e27bc2-16ea-3a46-b3d4-e993071cecd3 | -24.35369 | -49.46316 | 2026-03-01 00:02:00 | TERRA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| 8c62df14-819b-3cb4-8f2f-0c19c34d2a3e | -24.36156 | -49.45694 | 2026-03-01 00:02:00 | TERRA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 34.6 |
| 373168f0-f814-3823-8c72-41f1c66896c3 | 3.1663 | -59.9085 | 2026-03-01 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| eca7274c-66f9-389d-a292-a6f90c4c9345 | 1.5047 | -59.9116 | 2026-03-01 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 187.0 |
| f7469177-dfde-3ff2-8ded-c46fdda098f2 | 0.1914 | -60.4499 | 2026-03-01 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 97f4772c-1b83-31c1-92bb-f44f89940943 | 1.4682 | -59.9119 | 2026-03-01 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9c15786d-a6e4-33c2-bcb0-b8f43ff67a7a | 3.1662 | -59.9276 | 2026-03-01 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 637cfe7d-8992-30be-85aa-2a141214ca52 | 1.4864 | -59.9308 | 2026-03-01 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 153.5 |
| c3599b13-e1e1-3f3d-8c02-d4bc0eabdfe9 | 1.5046 | -59.9306 | 2026-03-01 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 129ea549-98d1-323a-b3c5-6d8e29cd3647 | 1.4681 | -59.9309 | 2026-03-01 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 310ae218-1be1-3bef-a33e-44d17d73fe5f | 1.4864 | -59.9117 | 2026-03-01 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 185.7 |
| faeb4bb4-0719-3d40-b805-9ee030341e99 | 1.4864 | -59.9308 | 2026-03-01 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 16a2dd8b-2a27-3439-9fd2-9cd5ce844e37 | 1.4864 | -59.9117 | 2026-03-01 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 186.9 |
| 2c4082d7-682e-322e-9afd-3c8a829ac31d | 1.4681 | -59.9309 | 2026-03-01 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 126425e5-5a7a-32b2-b564-4163b6a328d9 | 1.5047 | -59.9116 | 2026-03-01 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 7bdd8c4f-e4a4-3047-b6de-478bd5cf5a76 | 2.3251 | -60.3782 | 2026-03-01 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| ea30dd89-fac7-3bb4-b48c-bde951971a32 | 3.1663 | -59.9085 | 2026-03-01 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| dc1bc3a0-2b69-39e3-84ba-2d897783ba03 | 1.4682 | -59.9119 | 2026-03-01 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 64bca1cf-0f3a-3454-b416-6f3a4a89984f | 1.5046 | -59.9306 | 2026-03-01 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 612ed4ee-dabe-3eff-a2b8-cc8e33535b85 | 1.5046 | -59.9306 | 2026-03-01 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 91ec8c55-b090-3bcf-a81d-e74feb52eb8c | 1.5047 | -59.9116 | 2026-03-01 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 160.4 |
| ab69ad50-4684-3255-aedc-1b4e524e5a4e | 1.4682 | -59.9119 | 2026-03-01 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 79c75b69-9fad-3e77-9c25-f721a8387fd6 | 1.4864 | -59.9117 | 2026-03-01 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 192.7 |
| 5d827468-f55c-3a52-9313-ff3b30d29b77 | 1.4681 | -59.9309 | 2026-03-01 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 72d629c1-df00-34ac-b1c6-a993a1e5fede | 1.4864 | -59.9308 | 2026-03-01 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 164.9 |
| aa4378b0-7c92-3bbb-8de3-d55bc5a8b4ed | 3.1663 | -59.9085 | 2026-03-01 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d2b63530-ff38-3e47-82dd-e7e5e085eeeb | 3.4564 | -60.7968 | 2026-03-01 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 47e9618b-ad4d-3e6f-96c9-663006d66af3 | 3.4381 | -60.7972 | 2026-03-01 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e7ca3869-c2ee-3f0a-b096-9038368d3404 | 1.4682 | -59.9119 | 2026-03-01 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 5de38d0c-3712-3530-bc6b-5525a396fad8 | 1.4864 | -59.9308 | 2026-03-01 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 1608a5b6-f9bc-3fd3-a9dd-52d24acb0ab8 | 1.4681 | -59.9309 | 2026-03-01 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 452b0375-7a3c-3ab5-8fa6-af12b1afd53e | 1.4864 | -59.9117 | 2026-03-01 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 206.2 |
| 8725c1db-fd2d-3857-8445-cebb53e1cd71 | 1.5046 | -59.9306 | 2026-03-01 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 4694c4ea-3953-3c5f-8b87-fcbe2a4cb30b | 1.5047 | -59.9116 | 2026-03-01 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 191.7 |
| 84a8ff7b-2798-38b2-a24b-38d99ad2b09d | 2.8354 | -60.7694 | 2026-03-01 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 84af74a5-9e1a-363b-9b54-48642f2709b5 | 1.5046 | -59.9306 | 2026-03-01 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 2afc07d9-6385-31b0-86ee-3db51cef5e2b | 1.5047 | -59.9116 | 2026-03-01 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 534f9e2a-faa1-3023-a853-63f295d5c4d0 | 3.1663 | -59.9085 | 2026-03-01 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f1a5cf0e-efeb-3f76-90c8-b943b172e0ef | 1.4864 | -59.9308 | 2026-03-01 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 4e41b5fb-bae6-3f39-8118-7d0f41a8b3cb | 3.4564 | -60.7968 | 2026-03-01 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ded70a38-3685-31bf-9e8b-1f3092a36b4f | 1.4681 | -59.9309 | 2026-03-01 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 96fb2777-78bb-3e90-994f-ead8c22e6a32 | 2.3251 | -60.3782 | 2026-03-01 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 51476c2a-37ee-3fb4-b3a6-84ff0464eec4 | 2.8354 | -60.7883 | 2026-03-01 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f4018dc0-8cf7-3d05-a220-57c5ab506a51 | 1.4682 | -59.9119 | 2026-03-01 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 75a0490a-63cc-329d-b175-465ae2c85810 | 1.4864 | -59.9117 | 2026-03-01 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 190.1 |
| 10e79c42-4eee-3896-a8f0-33d1540e233b | 3.4564 | -60.7968 | 2026-03-01 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 399dc256-a87a-372d-9ea1-6bce2a64b4de | 1.4682 | -59.9119 | 2026-03-01 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8d0d0a9a-36ca-3214-9737-a5e08bb4c504 | 1.4681 | -59.9309 | 2026-03-01 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.3 |
| aef559c7-4fb6-3b85-8461-d00b4692a711 | 1.5047 | -59.9116 | 2026-03-01 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 181.8 |
| 5ce3488f-15f7-3d28-a4ac-637858a09a9d | 1.4864 | -59.9117 | 2026-03-01 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 217.9 |
| 49270b90-b3fb-3014-bc91-fac41323b4d1 | 1.4864 | -59.9308 | 2026-03-01 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 5c123ac1-25bb-3052-bc35-528d4f00ac6f | 1.5046 | -59.9306 | 2026-03-01 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 389d6060-0b62-3b85-9f24-608704da9529 | 3.4381 | -60.8161 | 2026-03-01 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 9705b042-1e86-3ddf-9506-56905b77452f | 3.4381 | -60.7972 | 2026-03-01 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 7c45c72f-1baa-38be-9c6d-2919fb80a1e6 | 3.4564 | -60.8158 | 2026-03-01 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| fa6cf084-c0fc-362c-8ff7-263e10196c27 | 1.4864 | -59.9117 | 2026-03-01 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 190.0 |
| 0de0c383-7be1-347c-890e-cb0d16ab0f72 | 1.5047 | -59.9116 | 2026-03-01 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 178.7 |
| f0ad5137-e702-3e3e-841d-4d24f0dd4eb5 | 3.4381 | -60.8161 | 2026-03-01 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 5f44b9d8-dc67-35c8-95e2-2d15dd351fcf | 1.4864 | -59.9308 | 2026-03-01 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 170.1 |
| 365da1ea-b748-3d65-9409-0217046ac5b2 | 3.4564 | -60.8158 | 2026-03-01 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| f34fc208-15a2-32c1-9d6a-a7fc502a3eda | 1.4682 | -59.9119 | 2026-03-01 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b6af1f61-c1a4-38a3-a15f-8f574a2d71a5 | 1.5046 | -59.9306 | 2026-03-01 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 8e0b616b-5608-37f4-87e7-26878d8b9c4f | 1.4681 | -59.9309 | 2026-03-01 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 6cf365d9-45ae-3cb6-9276-ebe105c48b1c | 3.4381 | -60.7972 | 2026-03-01 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| a53e9ec5-6170-3543-944b-f9563894ac95 | 1.4864 | -59.9117 | 2026-03-01 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 177.0 |
| c5d5c250-8b09-3781-b067-cc5d6fa57297 | 1.4864 | -59.9308 | 2026-03-01 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 163.3 |
| e8ada548-772c-32cf-8bae-2fcf2eac2846 | 3.4381 | -60.7972 | 2026-03-01 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 0c9188bf-e370-3362-a350-d971c8e8cbdb | 1.5047 | -59.9116 | 2026-03-01 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 181.8 |
| ec4f9352-12ff-3ba6-a326-fc9bb289f4ca | 1.4682 | -59.9119 | 2026-03-01 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 91e8af7b-fe42-3d1b-ba91-306c862c76b2 | 1.5046 | -59.9306 | 2026-03-01 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 147.1 |
| c10182fa-a6a2-3542-9b53-29dd18949e1b | 3.4564 | -60.7968 | 2026-03-01 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 42297851-27eb-355d-87bf-3595e8b5f6dd | 3.4564 | -60.8158 | 2026-03-01 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 3d76ffaf-5c4d-3515-898e-6a0f86f1043e | 1.4681 | -59.9309 | 2026-03-01 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 68dc42f0-4d0a-3bc8-aae1-04876450e836 | 3.4381 | -60.8161 | 2026-03-01 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 1deacb5f-ddef-3f40-9770-6a4e87a3d232 | 3.4564 | -60.7968 | 2026-03-01 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 69aef60d-3863-363d-a7fe-3bdf40724519 | 1.4864 | -59.9117 | 2026-03-01 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 208.8 |
| 72ce27b4-4f94-3be3-ae98-991ff80c25a5 | 1.5046 | -59.9306 | 2026-03-01 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 1cf50651-3003-3fbf-8e86-c6fa0e69bad1 | 1.4682 | -59.9119 | 2026-03-01 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f2d736a6-477a-3ae0-8ad2-e406231c9813 | 1.4681 | -59.9309 | 2026-03-01 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 60ab0459-f6a3-3e73-9a9d-aed048a57277 | 3.4381 | -60.7972 | 2026-03-01 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 383f0daf-4d0c-3e02-a5b5-a5f7750b7b9b | 3.4564 | -60.8158 | 2026-03-01 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 3d2d708b-733c-363c-997f-d320c6888e81 | 1.5047 | -59.9116 | 2026-03-01 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 182.4 |
| 354e65fe-a96d-325f-abd2-6770b0dc766d | 1.4864 | -59.9308 | 2026-03-01 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 5d6a2542-94ca-3227-aae1-bbbf4183c29a | 3.4381 | -60.8161 | 2026-03-01 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 109.2 |
| f70df34a-3940-3eb5-99ed-802fa2a73048 | -21.70574 | -56.32047 | 2026-03-01 01:38:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 2aea3fe6-ce33-34ee-8075-a22f37d6ecb6 | -21.70288 | -56.32581 | 2026-03-01 01:38:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 29.2 |
| c8622659-162c-39b4-a344-3528f436af51 | 1.4681 | -59.9309 | 2026-03-01 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |


[Clique aqui para ver as próximas entradas](README2.md)
