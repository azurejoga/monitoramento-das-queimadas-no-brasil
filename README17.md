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
| 4c706ba4-8e3b-3462-abf5-21ba79daac25 | -9.73011 | -43.41222 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 61b7396c-cc1b-3e50-9e33-f37c88fddd41 | -11.52688 | -49.61848 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a2e8126-9039-3ccd-b3ee-12847c4eca3d | -9.74517 | -43.38666 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b8149c72-d562-3fb4-9e06-fc862f21c744 | -9.96935 | -47.9838 | 2026-09-07 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0acf6fce-90d8-31bc-bd2d-3909052e8f57 | -9.75313 | -43.41082 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b26177b0-0882-32fe-b0be-858bd6f4050f | -11.27789 | -45.10254 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3bcef4af-9a32-326e-93e3-9f04d6865ca5 | -11.31955 | -45.07176 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1be70a1-7db2-3be0-8f18-be2d460b1d21 | -9.33014 | -48.45077 | 2026-09-07 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0748539b-5645-3f80-84ad-f88b7491907a | -9.75005 | -43.40579 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 3ba7f273-bf85-3b37-9b6a-7de69afc2269 | -7.16778 | -46.45817 | 2026-09-07 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cb3f3fe-85d1-3362-8c9e-63d23338966c | -5.30054 | -60.14888 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dc88bdd-057e-3f47-8338-f8554cbd7a04 | -6.05519 | -57.80545 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03f7f02c-f3cb-3daa-bb35-22eb9e1d321d | -6.0614 | -57.80626 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eae92df3-34fe-380c-8b0a-d2a5010feed4 | -11.29179 | -45.12877 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da699751-0656-34d7-87d4-755d4666b59f | -6.00454 | -57.69847 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4894afb-efdd-3815-a8e2-8bec1c680e93 | -13.23511 | -61.73249 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3b2f6120-249d-389a-b99b-ea71793ba427 | -15.93738 | -41.97564 | 2026-09-07 04:29:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8edd23f1-dd49-3900-9af6-e46d68f79dbe | -13.24026 | -61.77496 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4679108-47d3-304b-be8b-c27f64f44d10 | -13.24889 | -61.77011 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 25380e50-f29f-3543-bf7b-8dcd493c4026 | -13.28055 | -61.7218 | 2026-09-07 04:29:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b1fa735-ab22-3ece-97af-54b04027cf46 | -13.23375 | -61.77365 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e873b140-4df7-3994-8686-069001476cba | -13.25169 | -61.72236 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ec747d6-cb31-347a-a221-1c4529844be6 | -15.47164 | -43.87425 | 2026-09-07 04:29:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e22368e1-aa55-3a20-85a6-3b72b1e9a0f4 | -13.24198 | -61.73399 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a7937cd3-a557-3935-b645-621da75e4e45 | -13.27348 | -61.7546 | 2026-09-07 04:29:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9816c167-ab08-3bc2-bd52-f5ac5c7ae9bb | -13.22698 | -61.73761 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eba9ad5d-cbc3-39d9-8176-8236b699141e | -13.21851 | -61.7426 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 15f5b0a6-040f-31ad-8356-849d3087e13d | -13.24071 | -61.74067 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cac2d824-bc48-3990-9be7-70e06b96447c | -13.21165 | -61.74108 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d8f2298c-a783-3c84-a900-ed48ee3a2550 | -13.29003 | -61.74448 | 2026-09-07 04:29:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd0bccd9-1e3f-36f8-9a2c-e608350a2101 | -13.23524 | -61.73258 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b5ad37ff-82a4-3ab9-b653-f4b25f14f3fc | -13.26542 | -61.72536 | 2026-09-07 04:29:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d4cf57aa-b643-3257-9bf5-b6af7aed0ecf | -13.22682 | -61.73754 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 93ba35fd-4b28-3398-b3cc-691001024fba | -13.25034 | -61.72905 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e9d2965a-609a-349a-badd-ff8b4753b7d0 | -14.62467 | -48.8759 | 2026-09-07 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8036e6e-dd1d-3935-81dc-18dc8857f331 | -15.93624 | -41.98458 | 2026-09-07 04:29:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 6b5b2eaa-781f-3a77-b9c8-a82a266b17c9 | -13.25858 | -61.724 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a633ebd1-f5d8-3901-bb8f-3d250139edba | -13.24341 | -61.72744 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e1cbca8-ea61-3aa5-be8f-e6d743baa2e2 | -13.21186 | -61.7411 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 965f0784-f0ea-3f45-8ef7-81b0a95f9d48 | -13.23195 | -61.78005 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca9e1aa3-5933-3013-b90e-69ef9ab14f12 | -13.21872 | -61.74266 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 31427af5-f62b-3eff-9dc8-eae3d827c206 | -14.62798 | -48.87645 | 2026-09-07 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a688e7c-7f7a-33ae-856e-2637039b4303 | -14.6313 | -48.877 | 2026-09-07 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f040cc6-0951-31f9-8e91-470dfb3ad39f | -13.21995 | -61.73605 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f985a80-21ee-3332-9a27-2da622c4ed68 | -13.24055 | -61.74054 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28cf6924-63e5-31f8-918c-8b4c4765f937 | -13.28863 | -61.75102 | 2026-09-07 04:29:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65059444-0b3a-3339-bc63-7003d8f47c38 | -13.23338 | -61.77345 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44730966-af44-3bef-86cc-14df2d4ccd9d | -14.64512 | -48.87566 | 2026-09-07 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1015f20-118d-3806-907e-75ce25f97ec5 | -13.24348 | -61.72754 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 27c30eb2-8936-33e7-8c81-849d775d009c | -15.94181 | -41.97625 | 2026-09-07 04:29:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d548ed05-a83b-375e-b648-d6ad6d434c18 | -13.24202 | -61.76857 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bccb6405-176d-3c06-a530-2c4b55ed64b8 | -17.39403 | -44.54339 | 2026-09-07 04:29:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 791ce6f0-1b6f-3a10-9d7d-76a07769026d | -13.27206 | -61.76116 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eef0d95d-9862-30f4-bed9-b49ad3b1c756 | -13.25173 | -61.72247 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3d53d272-dc81-3179-8749-26057dcef344 | -13.25688 | -61.76477 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c60253ac-8318-3a6b-97e0-66223aa8727e | -13.2417 | -61.76835 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00eeef72-6a3b-3e92-8492-64aa5c02f2f2 | -13.24858 | -61.76986 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2b97cf92-2396-3ccf-8ea9-b84adeafe1ef | -13.25856 | -61.72386 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 317c44fd-cebb-367f-87c8-aed9c6166f3c | -13.25027 | -61.72892 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7ef08e90-8014-3845-9f17-99a18814c147 | -13.27369 | -61.72031 | 2026-09-07 04:29:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60014527-d04b-3e89-9416-50916a330507 | -15.9368 | -41.98015 | 2026-09-07 04:29:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 35b512c4-1a7f-3aab-ba76-b40c439eb448 | -13.22012 | -61.73608 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eb932e5e-3ec8-3e72-9a1c-35c47a2bd79e | -13.24063 | -61.7752 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3b203dfb-ac09-385f-950b-7d0954361bca | -13.26376 | -61.76627 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f568bff-ed6d-303d-a1b4-64988de1fa08 | -13.26519 | -61.75968 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3912a031-0e61-36f0-8e2e-76526c526d99 | -13.2421 | -61.7341 | 2026-09-07 04:29:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 71d49804-8c4e-3f82-8977-af05deca75f1 | -13.28034 | -61.75611 | 2026-09-07 04:29:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 597d77a1-de9f-347f-88a1-7800bb4b097c | -15.47233 | -43.86913 | 2026-09-07 04:29:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2a44a99-f9fa-30bc-9a0c-0803dd696409 | -3.1462 | -60.6506 | 2026-09-07 04:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6bc45b26-bec8-3ed5-9ba1-6d2fa18490d5 | -2.8839 | -50.4428 | 2026-09-07 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f4f4a3a5-a2c1-379b-b8a2-6d3d7bd9b84c | -27.7479 | -50.2844 | 2026-09-07 04:32:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6c2c9592-de16-3907-8ae5-56239f4fc107 | -20.42768 | -57.41729 | 2026-09-07 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4a2b6ca0-b5bc-31a7-8628-fdef9243d83d | -28.6769 | -49.04712 | 2026-09-07 04:34:00 | NOAA-21 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c814500e-a8c0-3740-b3ab-28c70bb7123c | -28.67631 | -49.05153 | 2026-09-07 04:34:00 | NOAA-21 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0f5706f8-f20c-3972-878d-750ef6d0ed54 | -28.18303 | -49.86281 | 2026-09-07 04:34:00 | NOAA-21 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 51afe36f-af5b-3076-98e4-ed3b1725c039 | -28.67281 | -49.05092 | 2026-09-07 04:34:00 | NOAA-21 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f2be13f7-9369-34f4-99de-2a7989579326 | -3.1462 | -60.6506 | 2026-09-07 04:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 424e20fa-7943-33c2-93e5-c528494ea70b | -3.1461 | -60.6696 | 2026-09-07 04:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 0ba053ef-c8ae-3c5c-b27c-245339f2d1c0 | -3.1462 | -60.6506 | 2026-09-07 04:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 209ebc2c-20ca-3ee8-8639-bc599f45d432 | -3.1461 | -60.6696 | 2026-09-07 04:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d305ee42-2b3a-3151-934e-d60ff0dc377c | -3.1461 | -60.6696 | 2026-09-07 05:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| f540c1c6-f2aa-35bc-ac9d-66626059deb8 | -3.1462 | -60.6506 | 2026-09-07 05:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 3c58cdae-6a8e-3016-98cf-17564653e592 | -2.95958 | -48.706 | 2026-09-07 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 09164806-edb2-392a-84ee-565367955319 | -3.55176 | -48.18388 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ff5730d-f86b-3b6b-9c65-5147a6b7f313 | -3.20885 | -42.97644 | 2026-09-07 05:01:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6bd7462-2d5f-3493-8636-7ca1f9620a6b | -2.82449 | -49.23082 | 2026-09-07 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 586e9631-9643-3c59-96c6-8d2eb8adf9d3 | -2.86207 | -50.45223 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61e0a327-5735-3c83-897e-a7298c1da1c6 | -4.12519 | -54.40959 | 2026-09-07 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 121ec02d-c949-3cf1-9aa4-e6c0a625009f | -3.37242 | -59.41588 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c32f2259-af36-30ad-9dea-e23db4f47e18 | -3.12096 | -57.68725 | 2026-09-07 05:01:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85551602-bd93-3f1e-839b-3c5f0900cb77 | -3.27181 | -50.59659 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6bb6602-1a63-3d7b-ba71-be2c4be326a9 | -4.21453 | -48.56443 | 2026-09-07 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cde10740-1c59-311d-ac6e-dd0cc2848251 | -3.59436 | -50.67912 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 944c9c89-78eb-3211-8871-65b2bfd0de35 | -3.09427 | -61.07081 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51176c34-e856-3c69-a807-776d4eda6707 | -4.59743 | -50.98363 | 2026-09-07 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec22b874-80d3-3799-9079-0a6b82fade47 | -2.95595 | -48.70543 | 2026-09-07 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c90ca882-0189-373b-a28b-278246020204 | -3.62466 | -54.60708 | 2026-09-07 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f76234ef-5a37-31e2-acb9-8bfc342701cd | -2.62932 | -46.76823 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 609a287f-ec5f-3170-96dd-e03aa5550abc | -3.7933 | -55.87821 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39624d6f-ec5a-3bf1-842a-1a9daf6a4e96 | -1.48945 | -54.83042 | 2026-09-07 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README18.md)
