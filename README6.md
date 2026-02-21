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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79635a86-41d5-3363-9b4c-aabad3fbc039 | 4.07654 | -61.15519 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9026477-7e00-3e4a-b64f-febe39179ac9 | 2.55038 | -60.56717 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddd2c9af-c7ff-3f96-9da9-07d07f4a7495 | 3.09714 | -60.37221 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a245da9-ede4-390f-a538-e41389eb579d | 2.6874 | -60.24995 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 485067a0-4a8a-3aa9-a7fc-651d2c8decb9 | 2.70611 | -60.23999 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5550f68a-4ae0-3733-9329-f344f34f1f56 | 1.93698 | -60.36524 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a5c7c7d-1353-3d38-a3d0-b5d2f83927a6 | 3.08179 | -60.10388 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91c66f1d-6ab5-31eb-8190-aa8164644b4a | 4.07057 | -60.14475 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d75f630-e939-375a-83b3-097dec846177 | 3.77671 | -60.02533 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cc78bf6-5b5a-3a06-a028-d3e4037071f9 | 4.16078 | -60.93286 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27cbeb80-ac06-37a1-8e14-084abd7d9f89 | 3.08125 | -60.10045 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb6a2bdf-59df-377d-9629-d1b23b2d4490 | 1.94137 | -60.37158 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f3d5bb4-86f5-3604-818a-746e5232f191 | 3.07465 | -60.10149 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98af39fb-efd0-3bac-a32a-38be3ae0d116 | 2.5625 | -60.55823 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13c4a9b2-548e-36d8-9f0c-f71bae3acb80 | 1.94028 | -60.36472 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ebc03b26-0e07-3ab0-91c9-33dd5a7fc46c | 1.93752 | -60.36867 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d8e461b-48a5-35d5-9de5-a05a832e173a | 2.55324 | -60.73588 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 73796382-5a0f-3897-b1ff-324de4060b10 | 2.56304 | -60.56167 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04df33b0-3496-3ae9-a8e6-89879026141f | 2.55601 | -60.73192 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3d270c9e-2816-3afe-ae3e-6d1db62a0d1b | 4.05935 | -61.08909 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a76d685-e1c7-38ff-bbcb-b1323ef4a682 | 4.02664 | -60.12346 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77230c83-3de8-31e9-8f2f-876f61600397 | 2.69129 | -60.23177 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3302d91-2885-3e9f-8e23-c02b331cf7a7 | 4.06379 | -61.09562 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e4945ee-2318-3447-af4a-9b6235cd7aef | 3.47736 | -60.75702 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4571458d-7762-3d25-9518-994f1f7117fc | 4.27131 | -59.77845 | 2026-02-21 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1c55e48-82f0-388b-be3d-5afbc23fa8ed | 3.60678 | -61.42796 | 2026-02-21 05:29:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61a91540-d109-37d0-867b-9ddcf6aa9045 | 2.69405 | -60.22783 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a13816bd-5585-309c-b1ad-49483f25c193 | 3.47627 | -60.75008 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5aaa92ca-6854-3378-8fd6-182c9a7c55ad | 4.82611 | -60.19446 | 2026-02-21 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b4d0e9c-e111-39e2-8cf2-6cdcf895954a | 2.70557 | -60.23656 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9e9c4697-3d25-3629-9688-decc5f4df979 | 2.5658 | -60.55771 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f30308d-d938-39a9-b267-75b665aac201 | 2.5559 | -60.55927 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f1c8606-600a-3222-bfc4-5820115a757e | 4.0671 | -61.11674 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bbd8459-c235-3bfa-a4aa-3df014a745f6 | 3.92297 | -59.96363 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8240b210-5c85-3942-bedf-44a8c1d79b77 | 4.14601 | -60.29855 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d91d3d62-4dfd-3001-8745-43a8cab485a6 | 3.19319 | -60.65646 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e91f59b-2d59-3697-ac69-b0e8f8a51c90 | 2.70281 | -60.24051 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fbec8a1a-6e37-3ba5-9007-7d9b58028745 | 2.6902 | -60.22492 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| db335d2b-25af-3a31-81f7-d6a4f7d6e01e | 3.48009 | -60.77437 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e260093-ddbc-328a-810a-552b6eece3ba | 4.16476 | -60.87132 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55271069-a4b7-36bc-9d3f-fd031cfe1e63 | 2.99544 | -61.12843 | 2026-02-21 05:29:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56ed7256-59c4-359f-8064-6a903d5d1888 | 3.97446 | -60.56923 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a8b0a96-8644-3107-b282-b7e9190f4be2 | 3.08455 | -60.09994 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 426a565c-a77d-3f7f-b06c-faf8e4286f65 | 2.54885 | -60.7295 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43fe62a5-f400-3939-83a9-bbfd60f093c9 | 2.65686 | -60.12513 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aa0ddcb-1bcb-3baf-99ab-ed77f4b1951e | 4.1499 | -60.28024 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bdcd7e1-6ffe-3029-a25d-8e855531c7b1 | 2.70227 | -60.23708 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63069152-af5c-3544-b8d6-9e14a59c577a | 3.45747 | -60.76011 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85009174-e2a6-329f-ae61-78473a4dde9b | 3.68946 | -61.15415 | 2026-02-21 05:29:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc1da5f0-2c96-3eab-8249-cf3e842ce13f | 4.26801 | -59.77897 | 2026-02-21 05:29:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a6308cd-6404-34ba-bec1-13a475421a71 | 4.0699 | -61.11274 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a566b82-0dfa-3a3c-82be-bcd89a3e0843 | 1.97966 | -60.69939 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2b4d3d1-192a-3758-9672-1762431bbc8e | 3.0714 | -60.08091 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4b8b2a7-7ff6-33ab-96d4-dc5c8fd4a68e | 3.084 | -60.0965 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ef39df3-bc50-3c7d-a9f8-df64caff4368 | 2.68745 | -60.22886 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a84f5a17-0ca1-390c-b1c4-13d4faac54c1 | 4.16421 | -60.86781 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94e42e96-0d17-32bb-9553-3e62cbc1f283 | 2.55314 | -60.56321 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ec5d9f0b-f4bf-3757-8ce3-eb3b21e11661 | 2.70833 | -60.23262 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d314416b-0571-3a7f-85c1-257351f6924f | 2.67875 | -60.41338 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d20c7ce8-9f35-311f-975d-292f3d855ac7 | 2.69296 | -60.22097 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a48683af-f28d-3610-bd33-4420c0ecc9af | 2.68966 | -60.22149 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 747cf064-82c4-331d-8fac-b9fda9377b16 | 3.09384 | -60.37273 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d3c4d11-a156-3798-aade-6197d2b9c1b6 | 1.94509 | -60.37087 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4399c35-4f0a-3b39-b518-50899976b18b | 3.47572 | -60.74661 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35d25eb3-f4d1-3af4-af5a-ccc5039c74e4 | 2.55986 | -60.73484 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78f5782b-b961-3257-8fa7-1296dcce7fca | 2.6935 | -60.2244 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 207dff66-aa2d-3aa9-9e19-c0ff5e5c30d9 | 1.94455 | -60.36745 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72c14606-b011-3cfb-a126-ba8289f15dcc | 2.76758 | -60.28661 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bb4a1ae-23c0-31e5-a762-7e8c0abfe20f | 4.16753 | -60.86726 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac2e0d57-1272-31bb-be62-3f47fe11af04 | 2.70503 | -60.23313 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 046997f5-ee78-3c5b-ab3b-bf7aceca414c | 2.89377 | -60.59048 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29909412-8a13-3351-8697-9f5a2fad41d0 | 2.87725 | -60.59307 | 2026-02-21 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91bf718b-d44b-33db-8160-597caf7de1d1 | 4.06765 | -61.12024 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be6d6691-644f-32cc-8b92-f8b5e1c912b9 | 2.68151 | -60.40944 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b47ee27-234c-374f-a558-050740be47a2 | 4.15536 | -60.85489 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6657a94-89f2-3c07-a0c3-a610e01fdeff | 2.65631 | -60.12172 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e65175a7-89e5-3c21-91c2-ba46c574b583 | 2.28716 | -60.51716 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6494ca2-d0bc-345d-8b41-01e513ef7f07 | 4.16588 | -60.85674 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 171d5e6c-64c8-3bf3-8566-d62bb3f46297 | 2.68794 | -60.25338 | 2026-02-21 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2165283-5eb5-3abe-8d7f-fd50a37960e6 | 3.92681 | -59.96655 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b12e4ae7-3278-3b04-a3c0-d4f593593609 | 2.67821 | -60.40995 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aeadb11f-83b1-30b5-b593-f8173d4a66ee | 4.07044 | -61.11624 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 151e34d4-809a-3435-abad-181321e3343b | 2.55974 | -60.56218 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81c6677e-8778-3369-ba6d-2eacf30e19af | 1.94082 | -60.36815 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fdb78ce8-aee8-3e3b-89a3-d8722e2d21ce | 4.16643 | -60.86026 | 2026-02-21 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c93d252b-840c-3584-bcfb-f65ba68b3d4d | 2.54983 | -60.56373 | 2026-02-21 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3d8ce22-ed0b-3279-91e2-6c029f1e3464 | 3.78001 | -60.02481 | 2026-02-21 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c857bc1-1d0a-3441-8a0e-aed3b46c4a76 | 2.5149 | -60.99 | 2026-02-21 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90c4d6e9-bb5a-3dfa-b176-867963abcc8f | 2.7088 | -60.2398 | 2026-02-21 05:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.5 |
| cf1d1f91-27e1-3afa-a6c2-4a1b470ee54c | 1.0547 | -59.49393 | 2026-02-21 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0a8e67a-ddcc-35cf-acd9-fc70acbb8d17 | 0.45054 | -60.39879 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23372765-e359-3ddd-926f-771138ecd7bc | 1.83239 | -60.84194 | 2026-02-21 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5709715-bcc7-3052-b68d-eed16c056768 | 0.45715 | -60.39776 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46f6112d-367a-3c5b-9a31-4e8bd31b4f0b | 1.44496 | -59.96035 | 2026-02-21 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48601e58-deee-383c-94af-c86e3d63c6e3 | 0.0691 | -60.65205 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5de2c756-0fe2-3258-ba53-89223988d114 | 1.4415 | -59.96098 | 2026-02-21 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4168ab8d-3f9e-3499-9879-dd326bc616bd | 1.44827 | -59.95984 | 2026-02-21 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 389adc4d-f246-3715-9d3a-f94b9f80078c | 0.45661 | -60.39432 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9bf4e57-eaf1-3dd8-800d-cb86ca30f639 | 0.45385 | -60.39827 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a800033b-1c00-30a2-bd61-37ad34fbcaef | 0.4533 | -60.39483 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
