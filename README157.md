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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 958a4485-623e-32f5-b9de-2d313c52b2f5 | -7.8134 | -54.73793 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a779604e-6863-3ad8-ae6c-91d753fb07f6 | -7.809 | -54.72789 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58e6eaf9-26bf-3f96-acc4-4c557591b241 | -7.80793 | -54.72857 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf5080dc-861e-370d-b3e2-3420f3da52b3 | -7.8078 | -54.73694 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 496ff9fd-38e6-3311-a75a-bdd408c7ab9f | -7.80716 | -54.74177 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce3ac386-9554-3343-a45a-3dd3c5873585 | -7.8065 | -54.74673 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7999826-5fe1-3f78-9a6c-f2bc741bb65a | -7.80254 | -54.72643 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f34797fa-b317-3fa2-ba60-a309aad3717b | -7.80207 | -54.7222 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a937ffd8-4a91-3cce-8374-a136e480b8e9 | -7.8019 | -54.73122 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c19235f-2bbd-35a0-847c-a6282aaa7411 | -7.80087 | -54.73178 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb181b49-06f4-31fb-bee4-a6f8aa271f55 | -7.80062 | -54.74091 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51bfd157-1dc0-3579-bed9-9922524c6532 | -7.79964 | -54.74158 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 343e4188-6b10-30b3-8e0b-41b1e0288136 | -7.73245 | -55.7189 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd8098d8-7ddc-31c2-a3de-59fde07e0b6b | -7.72686 | -55.71385 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0b72f63-b520-34c1-84d1-3cfca7f354ae | -7.61285 | -55.35476 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c97bade-be97-3414-bec9-75d97fd21eb8 | -7.61217 | -55.35978 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef812244-2175-3670-b363-c9853af5475a | -7.61144 | -55.29546 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e89ce85-875d-39ae-bd41-a50fd2b1aa50 | -7.61004 | -55.3572 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88bb9ef1-e0e9-3b74-bc58-83747cd2490a | -7.6094 | -55.36225 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| feea371c-c378-3694-a78e-c08df048e7bc | -7.60903 | -55.28737 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39e35d52-f32a-36bd-b69d-e1c11e802cde | -7.60589 | -55.35901 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ec2b2df-d84d-31ed-a72e-f1e46e1b1688 | -7.60311 | -55.36148 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea8d9dcf-abbb-3a31-997a-54a1f124b627 | -7.59641 | -55.18792 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e57237f0-9168-3d7e-8e66-480ff9a44b38 | -7.59573 | -55.19312 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75bac240-5857-3bf7-b38d-ec186e04fc81 | -7.57235 | -55.17435 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73251cf7-1454-30b0-8f53-4e147d410d33 | -7.56723 | -55.16398 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e78bfb52-c68e-309e-8578-b6932df2f3f8 | -7.5603 | -55.16755 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ac08559b-e1ce-3ad9-927a-1c4b8f25d890 | -7.55521 | -55.1569 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b3e6a20d-50f0-3279-8ee3-ede80116a783 | -7.37434 | -55.50304 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 879d9ae3-6350-35a0-ba70-fff5a7670ad0 | -7.37302 | -55.51279 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 2e49c591-0ebb-3d01-8af3-2f1827949bfe | -7.37225 | -55.51077 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| dfd1fa3e-e9c9-38f9-9563-b8bf377a3e9e | -7.3704 | -55.52524 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cbb2b0b7-6216-30e3-a7a9-a4e2f49ffba6 | -7.36879 | -55.4973 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ebe2955d-e378-385e-8304-75e2c14e0ea2 | -7.36813 | -55.50219 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8bcb79d3-d711-3c18-97bb-8370cf1d12d5 | -7.56601 | -55.17338 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d616f34e-5f95-34b1-8b16-c998640f3d43 | -7.56386 | -55.17139 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 193d1a39-ec71-3a5d-a29c-0d13e0d17e3d | -7.55246 | -55.16011 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98153455-b81a-3d46-85e5-6e5d06c71351 | -7.37288 | -55.50584 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 2cccafcf-804f-3f3f-a9eb-c6e2b06ae80d | -7.37163 | -55.51566 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 3b39eb0b-a35f-3c96-a59e-401c659a460c | -7.36191 | -55.50155 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2aa67a03-2c6f-3c52-8d8f-37fc0a7828af | -8.52284 | -55.19179 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 597fcf73-9b1d-3485-94bd-bf725e3b050f | -8.52219 | -55.19695 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99c16426-8e5c-389e-812f-03acd9368371 | -8.5164 | -55.19109 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4e9ea51-0fee-3109-a099-78044055e1ef | -8.5145 | -55.19347 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54ff17d9-92be-3357-8eaf-bd575f82a7fb | -8.51382 | -55.19861 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42559612-740f-39e7-a556-075fabf5a61b | -8.40539 | -55.02142 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c33d1be1-0eaa-33af-a66a-b1c5f8cef163 | -8.31573 | -55.00002 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6bfaae82-052a-37c7-ba9d-0b21788f2c35 | -8.31439 | -55.01076 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 06d6b3c7-e1e6-3ad9-b310-829ef786c730 | -8.11569 | -54.80315 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e31e7f9e-d019-3aae-96be-b407e381b2c5 | -8.11071 | -54.79423 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a3bf53a-19b5-379b-94a1-8b63b3a023fa | -8.6935 | -55.04057 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cc3629f-6a95-3681-b9d2-982c246a545e | -8.68707 | -55.03926 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 037c1030-e661-3e7c-a524-4c27ad759560 | -8.51705 | -55.18586 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b101562c-d5c7-379d-bd2d-682c749a1058 | -8.51575 | -55.19628 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aee4f89d-aa60-3952-8812-1aa5d0982609 | -8.51519 | -55.18825 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d342b28-27df-3a52-b6c9-8c32c00937e2 | -8.51511 | -55.20138 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6a7a128-a2e4-382b-bc87-ea3a0aa93baa | -8.41122 | -55.02756 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b833f4b6-8a44-3e16-901d-75f623acc790 | -8.39891 | -55.02064 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da9ca318-480b-3f9b-a8ae-b6c166cdc94f | -8.31505 | -55.00544 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 32078d96-f51a-3096-8ead-1ad0b78609b8 | -8.31482 | -55.00266 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 035c48ff-135c-3730-bf29-621f2778659f | -8.31411 | -55.008 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 1fb33aaf-ac93-3fee-b661-5df43b282642 | -8.11578 | -54.80632 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f610a052-1d0c-3338-9ae1-ad5e16ed7933 | -8.10997 | -54.79991 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 530631a9-4e2e-371a-920e-c7fc9b6c1b8f | -8.10986 | -54.79659 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80c1fb93-fac1-3409-a162-a89d11bcde78 | -2.46116 | -55.6217 | 2024-09-26 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8893b55f-34a8-361d-bbf0-f98ef814dba3 | -2.45602 | -55.61681 | 2024-09-26 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcfbea64-0d10-372f-b52d-62c633f8197d | -2.45541 | -55.62086 | 2024-09-26 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bb71c3a-e815-3037-8a11-ae4388361409 | -2.4548 | -55.62484 | 2024-09-26 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c33ae922-7c95-3c98-ac8e-10a486b2e3df | -8.34236 | -56.51329 | 2024-09-26 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e0fd7fd-05da-368a-b4d7-357b2cb26c13 | -8.34183 | -56.51746 | 2024-09-26 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5b5bac9-0e16-33ec-9bb2-6bd0df3b4e23 | -8.33698 | -56.5085 | 2024-09-26 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3c3970b-d0ce-3d7c-8b46-3d5c01be660f | -9.40097 | -56.87355 | 2024-09-26 05:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed96fc09-1977-3896-9cc9-509031474f26 | -9.37878 | -56.86124 | 2024-09-26 05:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca9efb59-8260-35eb-91dd-dbdba880e0e0 | -9.37291 | -56.86062 | 2024-09-26 05:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29aa553e-c967-3643-b789-c526113f185b | -9.30168 | -57.14654 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b15e1c0-bb19-380f-a06f-296362bfbf47 | -9.30051 | -57.14271 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc1a5797-a7bc-3767-92ce-b8fd260e21cd | -8.93482 | -57.14126 | 2024-09-26 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0079335-3aaa-30af-b22c-0b8e9db40f08 | -8.92859 | -57.14451 | 2024-09-26 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ea0e30e-6455-3908-9ef9-6b775f18ca5f | -9.40203 | -56.86529 | 2024-09-26 05:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7444717f-8fd1-3ade-a91d-fadc6107ed71 | -9.40151 | -56.86938 | 2024-09-26 05:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b6c9d97-d311-3d56-91c0-9c5d74b07acd | -9.3957 | -56.86829 | 2024-09-26 05:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49fbd422-2f42-36ff-a1a1-5d9a9ec18605 | -9.37823 | -56.86557 | 2024-09-26 05:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4b433ff-a805-38da-acfe-6391a7c94261 | -9.37236 | -56.86503 | 2024-09-26 05:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e180234-cd0f-3edb-a51f-04ff50a8cf92 | -9.30691 | -57.15137 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7eb1472-ebfc-3f56-8aa0-26da75eef0fe | -9.3057 | -57.14755 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e4c40ac-5093-3634-b5ff-24a1eac4245d | -9.30516 | -57.15161 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2acc9a8-8283-3b67-a1b5-f4d6e4b30131 | -9.30361 | -57.16338 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a49a5e57-d364-3608-b428-e05f020f5420 | -9.30219 | -57.14253 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 335845ce-0ba3-3498-a3de-6a95799942b7 | -9.29999 | -57.14666 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff1ef87e-cc11-37fb-a9b5-c8c28ff78709 | -9.29843 | -57.15846 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4296ad8-a311-338f-944c-906a98c4adf6 | -9.29599 | -57.14544 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bc8d2f8-6432-34a6-8f41-f2b9e8d06266 | -8.34345 | -56.50485 | 2024-09-26 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0377e2ca-7aa5-377e-891c-b8141f0fde36 | -8.3429 | -56.50909 | 2024-09-26 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1d6c8da-9e70-3873-8b6a-9e8de196b29a | -8.3383 | -56.50942 | 2024-09-26 05:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebaff0d6-198e-38dd-896c-ef7c840b3057 | -9.69466 | -57.20684 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad1f6f3d-0da2-3c65-8792-a66659511b9d | -9.69307 | -57.21915 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7a60ee5-a3b1-3ada-a0aa-64d742fc987b | -9.61644 | -57.76458 | 2024-09-26 05:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed04795e-a48b-3258-a8a2-c261045b19cb | -9.61139 | -57.76014 | 2024-09-26 05:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39d0d126-d2ab-3a39-ad93-b76fcc38cef9 | -9.61091 | -57.76387 | 2024-09-26 05:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff942ec7-7ccd-3cb9-9055-5f0f7c0f61fb | -9.55946 | -57.54555 | 2024-09-26 05:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README158.md)
