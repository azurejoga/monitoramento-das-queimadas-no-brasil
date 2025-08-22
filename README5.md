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
| ce516a05-7d6c-3414-9a7e-ad4488b7ea85 | -13.0114 | -45.222 | 2025-08-22 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| d2896474-bb18-3244-a478-e2cdfab123e9 | -18.9008 | -45.0044 | 2025-08-22 01:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 71fe4c59-e143-3bc7-9764-f33127f42e5b | -8.8736 | -62.4115 | 2025-08-22 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 0a01116e-8238-31c7-930d-505a78473d1b | -18.8805 | -45.0093 | 2025-08-22 01:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 27bfe756-7636-3809-9417-8ebc0e76dc60 | -8.5943 | -62.6315 | 2025-08-22 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.6 |
| d515fc4b-5761-394d-96cb-d56efec9c895 | -12.9921 | -45.2252 | 2025-08-22 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| ce850f73-dc08-3892-a761-ffb23ba5cca8 | -13.6587 | -45.693 | 2025-08-22 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| f8d7cb01-c74a-3686-9759-7f5e4208a137 | -18.8798 | -45.0334 | 2025-08-22 01:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 8eabdb7e-7f26-3797-adc7-7d845e1a9e00 | -13.0114 | -45.222 | 2025-08-22 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 72dc1b7e-a680-3f82-8da8-aeadfac5d7be | -8.613 | -62.6118 | 2025-08-22 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b08af9db-da28-380d-bd53-13c5755eaa02 | -12.9921 | -45.2252 | 2025-08-22 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 60217991-824b-3b50-9ad6-9344c26ebab9 | -8.5944 | -62.6126 | 2025-08-22 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.2 |
| c0aaf76d-7082-3c15-8cea-0b3fa8c7d7bc | -14.968 | -47.1409 | 2025-08-22 02:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 74a41a2f-cf31-3301-848c-987ff1475b47 | -8.8736 | -62.4115 | 2025-08-22 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 93c5db35-99e2-336b-be04-7091e2346b8e | -18.8798 | -45.0334 | 2025-08-22 02:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 16051a4c-f4b8-3d47-bc46-9abe14275ca0 | -18.8805 | -45.0093 | 2025-08-22 02:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 5d3225aa-baed-3e09-9720-553b9e3f2577 | -14.9875 | -47.1375 | 2025-08-22 02:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 842400c0-d222-378f-a9e1-491afc282734 | -2.4685 | -47.7697 | 2025-08-22 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| bb788ddf-aa8a-375f-9ae2-c52e812cab94 | -9.5179 | -60.5461 | 2025-08-22 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 4c936791-0db2-3d31-b009-fb9353daf681 | -8.613 | -62.6118 | 2025-08-22 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 7ef912df-6520-3fad-a732-844f767f89d2 | -12.9921 | -45.2252 | 2025-08-22 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 14204150-f95b-3ac3-bac5-62b357bed25a | -13.0288 | -46.3213 | 2025-08-22 02:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f20548ba-2948-346f-9511-f24ae3cb8996 | -18.8798 | -45.0334 | 2025-08-22 02:10:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 97.0 |
| e5512890-0740-3b3e-98be-b5227a96f2fe | -18.8805 | -45.0093 | 2025-08-22 02:10:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 139.3 |
| f3a753ea-e928-35af-9c22-c03457853372 | -8.8736 | -62.4115 | 2025-08-22 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 2a283b59-358d-3625-94af-5004b3cdc792 | -12.9921 | -45.2252 | 2025-08-22 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 0eabac1c-7469-3975-bdbf-2e8a617893c1 | -14.968 | -47.1409 | 2025-08-22 02:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 6f2f3e2d-dd1f-34b3-b4d8-8ec728819e7e | -13.0288 | -46.3213 | 2025-08-22 02:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 954c8263-1a36-3eb2-86b3-45759d652848 | -12.0027 | -44.6618 | 2025-08-22 02:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 085c7e19-0a51-3adc-8feb-9ca9c3529926 | -18.8798 | -45.0334 | 2025-08-22 02:20:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0c394e9a-28a4-3570-9a95-e6787af5c729 | -14.9875 | -47.1375 | 2025-08-22 02:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 21f78bfc-f181-3e6d-a814-d9e9c60ff7d5 | -18.8805 | -45.0093 | 2025-08-22 02:20:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 39edc6e4-6e14-39dd-901c-7f80bbca05c2 | -8.613 | -62.6118 | 2025-08-22 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 311d73ae-1d08-3a15-91e6-7165b13867af | -14.9209 | -49.451 | 2025-08-22 02:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ea0f6a43-7a84-35e5-b121-b1a71e22446e | -12.0023 | -44.6851 | 2025-08-22 02:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 22440f19-122e-38eb-9291-0674b61b22a7 | -2.4685 | -47.7697 | 2025-08-22 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b2691a9b-ec94-3d55-8932-bf195a361e50 | -12.9921 | -45.2252 | 2025-08-22 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 6e3a0f3d-c508-372e-b195-3602a548e962 | -14.9675 | -47.1637 | 2025-08-22 02:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 68cf285b-c78f-3be9-8824-a309c3bd11ef | -14.9685 | -47.1181 | 2025-08-22 02:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| aa359032-5df9-3dce-9edf-dc8f6c9c057f | -14.9015 | -49.454 | 2025-08-22 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 82ba8681-1109-318f-8c9d-3f8e1beb7729 | -2.4685 | -47.7697 | 2025-08-22 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2a49da1b-ad3c-3fc7-a18b-34392f28edf9 | -14.9205 | -49.473 | 2025-08-22 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 49df58c7-6290-3c09-8869-946e119057fe | -14.988 | -47.1147 | 2025-08-22 02:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 71b95635-94ae-3d49-b844-97a17e962969 | -12.0027 | -44.6618 | 2025-08-22 02:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c020a586-2be1-3835-93ea-b4027f8f48b5 | -14.9875 | -47.1375 | 2025-08-22 02:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 709.1 |
| bde32600-6258-3e2f-b940-720d7a1d6263 | -18.8798 | -45.0334 | 2025-08-22 02:30:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 94.6 |
| cc485635-7b59-3d66-baec-eae9bb9aa50a | -14.9209 | -49.451 | 2025-08-22 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 610.1 |
| 90aadee1-ae98-3f00-8ebd-e5194289bbaa | -14.9871 | -47.1603 | 2025-08-22 02:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 187.3 |
| c7512e81-de66-3722-96aa-57155c1fe3cd | -14.968 | -47.1409 | 2025-08-22 02:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 342.1 |
| bb26def3-b187-31f0-a0e1-7a21ca677879 | -18.8805 | -45.0093 | 2025-08-22 02:30:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 3f2b528c-fa83-3299-a2a1-cc92c4da154d | -13.0288 | -46.3213 | 2025-08-22 02:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d1bbe95a-3c95-3bc5-84e9-4222d97b1aaf | -14.9404 | -49.448 | 2025-08-22 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 1d10e8bf-14e0-339a-bfb6-d6a1c5bf05d8 | -14.9214 | -49.4289 | 2025-08-22 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 54.5 |
| a59b8816-d89c-3ff2-9ce6-7c2fe7bb47fd | -14.9875 | -47.1375 | 2025-08-22 02:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 147.0 |
| c326ce4a-9ed3-36be-a1b8-39efd554cacb | -19.9466 | -44.5497 | 2025-08-22 02:40:00 | GOES-19 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| 98dc7ed0-247f-34d5-a6d5-52ec74d99b6e | -14.988 | -47.1147 | 2025-08-22 02:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 37195742-da45-3ee2-b428-fb74b06ed1ef | -19.9254 | -44.5795 | 2025-08-22 02:40:00 | GOES-19 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.0 |
| 831946b3-411b-30e5-a28e-aeb0fd52f48d | -13.0288 | -46.3213 | 2025-08-22 02:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e547e821-ddb6-3804-a697-b979da75cb5b | -19.9459 | -44.5742 | 2025-08-22 02:40:00 | GOES-19 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 151.5 |
| ca83818d-f6a6-3540-9d7a-997a07410000 | -18.8805 | -45.0093 | 2025-08-22 02:40:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 5643d534-2868-3c39-9a85-48fca537d06e | -14.968 | -47.1409 | 2025-08-22 02:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 988b3fda-0731-32eb-9102-b9ae7bb923be | -18.8798 | -45.0334 | 2025-08-22 02:40:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 74.5 |
| f1e61f31-d713-3e03-b7ae-dc1bd96f5c6e | -2.4685 | -47.7697 | 2025-08-22 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a9655bb2-85d5-36ba-a75a-a78bc1944f06 | -12.9921 | -45.2252 | 2025-08-22 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 1471cf59-c9ce-3c39-b18b-0d9607987a2d | -18.8798 | -45.0334 | 2025-08-22 02:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 54b9cd5f-459d-3333-8f93-b00b00768613 | -14.6716 | -54.8521 | 2025-08-22 02:50:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 196f1858-a67b-3423-8347-4afa22fd9711 | -14.9875 | -47.1375 | 2025-08-22 02:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 1eeedf3e-edb9-3f4f-a3c8-0e0e9eae63b2 | -2.4685 | -47.7697 | 2025-08-22 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b6bbd381-db0b-3664-8cc5-268fe6e4ec8e | -12.0027 | -44.6618 | 2025-08-22 02:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| b27dcb5c-5316-3a6a-8f98-cdc141c7b865 | -19.9459 | -44.5742 | 2025-08-22 02:50:00 | GOES-19 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.4 |
| 874797eb-a54e-3296-86fb-fa2aebc147f1 | -19.9466 | -44.5497 | 2025-08-22 02:50:00 | GOES-19 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.9 |
| 14d347bc-5c08-3767-a93a-2451300537f6 | -14.968 | -47.1409 | 2025-08-22 02:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 997e30c3-6cb5-37e1-bac5-9ec7b8f7b7a5 | -18.8805 | -45.0093 | 2025-08-22 02:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 126.8 |
| fd2d9012-c4b5-3f82-b979-d8defff5bce2 | -12.9921 | -45.2252 | 2025-08-22 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 5f2afc1e-dd7f-3d06-b9cd-9de8659cbb60 | -12.0027 | -44.6618 | 2025-08-22 03:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 10fed4bb-ab38-3a8b-b620-82aa633fb2e4 | -19.9459 | -44.5742 | 2025-08-22 03:00:00 | GOES-19 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.0 |
| 33a2936e-213c-3892-ae61-8258c4b11535 | -18.8798 | -45.0334 | 2025-08-22 03:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| ec7efe4f-ea49-3507-b350-4dd075d0ef06 | -18.8805 | -45.0093 | 2025-08-22 03:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| a036461c-b93c-3c56-81c3-051297e2bdc6 | -2.4685 | -47.7697 | 2025-08-22 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2a7ad2ac-8128-386b-9c7d-bc3f7ea75da7 | -18.8805 | -45.0093 | 2025-08-22 03:10:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 2c1fec8d-9054-3b78-86de-be3ed26ee63f | -22.6964 | -43.7457 | 2025-08-22 03:10:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| e128e140-ee31-34ce-b39c-b5ebe3b7aa1b | -15.8955 | -43.4523 | 2025-08-22 03:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 59.7 |
| b0ae2160-0a05-37dd-a2d4-299b5eb3027a | -18.8805 | -45.0093 | 2025-08-22 03:20:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 74.5 |
| af33b218-988a-3428-a5d4-4beeb951be0f | -3.45578 | -39.59731 | 2025-08-22 03:28:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e3038c78-4953-304c-a310-4bbbb323b272 | -2.87476 | -40.09326 | 2025-08-22 03:28:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2eb700d9-b793-33e3-90f1-2ba3bc897c98 | -3.45508 | -39.59548 | 2025-08-22 03:28:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be30274a-40be-3a63-bfeb-41ce5e774753 | -18.8805 | -45.0093 | 2025-08-22 03:30:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 9afdaedd-e9e0-3983-a1df-f4dddb11ffe8 | -12.0027 | -44.6618 | 2025-08-22 03:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 88ce1848-aac3-3725-8bec-a1e1058b531e | -3.98542 | -43.24929 | 2025-08-22 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2d044e9-0f3b-3753-a8d2-d138b71a5a27 | -7.02999 | -44.63174 | 2025-08-22 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd699f68-8129-3884-8f01-2c0688c68363 | -5.16599 | -35.80453 | 2025-08-22 03:30:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 248824b5-75c3-3189-9c1f-c8cbfc9ff224 | -4.40337 | -44.09293 | 2025-08-22 03:30:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b4566a41-298c-3e70-a336-8e7d746d2bf2 | -4.40438 | -44.08727 | 2025-08-22 03:30:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7cd3fac3-7b73-3d56-8472-efac5807c793 | -5.696 | -43.53541 | 2025-08-22 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d789e762-9b6b-3d4e-a333-eb5829a7d476 | -7.15756 | -44.66582 | 2025-08-22 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ee98255-a32c-3864-88c3-9f4cd675d225 | -4.93905 | -38.00099 | 2025-08-22 03:30:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f1391e6-1296-3cca-ac1d-3f780a4b3a46 | -3.63125 | -43.54351 | 2025-08-22 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a66ad9db-e543-3b71-8da6-4dc93e92b652 | -8.21651 | -44.42934 | 2025-08-22 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe69a706-7097-3d5e-9e96-b72f77562309 | -4.64062 | -41.40247 | 2025-08-22 03:30:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f1589339-11b4-3e78-8d49-5038b5556ecd | -7.229 | -45.1762 | 2025-08-22 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README6.md)
