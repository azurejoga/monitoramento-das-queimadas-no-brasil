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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 435f6c23-9cc2-3b0c-96c8-cb463c84d42a | -3.26364 | -54.18221 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 05bb64f7-c9a3-3952-b67a-5a37aba315a4 | -3.01459 | -51.00874 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7988cce-7697-317d-82e0-bf4cb62018ea | -5.74443 | -45.1344 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c3055985-fdcc-321a-bb56-344dcc59b75a | -7.11294 | -52.65328 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 794e8adb-cf4f-38df-8433-b365a8e899c2 | -4.40193 | -49.78275 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bcc1d6d4-afe5-3436-96a6-dc4eb4bbbc03 | -3.76341 | -45.95382 | 2026-10-10 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac58a1a1-9979-3ae7-a202-1f1013531338 | -7.1942 | -42.00301 | 2026-10-10 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0e4d9dea-5598-3319-8444-4c567c93e56e | -6.81799 | -39.55507 | 2026-10-10 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 61cfd7dd-0939-3bea-b83d-6aaca27803d8 | -3.23044 | -49.4311 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2a6f05a9-fbfd-3435-af67-dda5543cd5c5 | -2.99836 | -53.91126 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ac42706-6d4d-3215-a135-c74f5638fa65 | -5.12958 | -42.87972 | 2026-10-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54c215f9-3117-30f1-be2b-26478740e16d | -7.52539 | -45.309 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 45435271-78b7-315a-9089-1e32836236f8 | -8.52225 | -46.89542 | 2026-10-10 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a439cba-d3a3-3734-919b-dfb648115f06 | -9.3308 | -46.46233 | 2026-10-10 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cf79172-d76c-3727-a4ce-9dd3b734d3e0 | -5.75978 | -41.6701 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e0701875-12fa-3000-9f0c-8dcf1fc101ed | -5.88043 | -43.4099 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5bac6520-4ed6-3b51-82bf-189336fe0364 | -3.49081 | -50.49201 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca84df24-53a8-3bb4-8773-dda792aed004 | -3.28008 | -50.39673 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9f34c7d-2fa9-3ada-8d9b-4b87cf5ff42c | -3.48396 | -50.33504 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5733d030-edb9-326a-ac63-32da14e774c2 | -3.1857 | -50.58568 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9906d4c3-0d32-3fe7-8c6e-e60ae6b903b5 | -4.41262 | -49.78141 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4e836fcb-9cca-3888-bba2-69038146b959 | -3.22746 | -49.4491 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b33501f-eecd-3fe4-bd29-bc7a19495e7c | -3.58164 | -54.72262 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24735fc6-6573-32fb-9de3-a3b03b436e44 | -9.11138 | -45.82729 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da0899b9-f10d-3261-9fd3-2d7531e6e7fa | -2.19329 | -46.83507 | 2026-10-10 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61cfbcb8-f21e-3fbe-87b0-06e568f35804 | -7.03681 | -47.67164 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac0a465c-59b3-30e2-8181-305bf92fccbe | -3.85619 | -51.93458 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aa480be-4ea9-395d-ae54-f91469cea7ab | -1.9534 | -54.39265 | 2026-10-10 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93e126bd-4c32-3aa0-b803-3a2fe3333224 | -7.05489 | -40.95192 | 2026-10-10 04:08:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 41ba4c0b-b9ca-3060-92fd-d1bdd140fb42 | -7.5247 | -45.31324 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d1a77eef-35f8-39f2-8498-2a21737384f5 | -3.50681 | -49.94251 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a95d021-47f2-3885-a956-c9366c7843b2 | -3.22439 | -49.43622 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 03fcc292-5255-3f97-b856-738d455cc7ae | -7.18868 | -41.99508 | 2026-10-10 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8aaa239c-f957-3428-9291-67e521186f68 | -7.50433 | -54.99864 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 9aece9d5-e9de-3384-9a1b-8da14f06771b | -9.9399 | -44.88754 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5dfcdf51-475d-3489-ab0c-43db1ef4a14c | -4.45554 | -47.91628 | 2026-10-10 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1f5e1c55-de11-3ab4-932d-46794eda5a4a | -2.22152 | -50.49004 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92af3118-226e-34ba-a186-06aed5950766 | -7.04166 | -47.66861 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 473103a6-1de9-379e-8c23-1de8ebb4ff70 | -10.8905 | -44.8232 | 2026-10-10 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| f66f6729-4ece-3668-9b29-7c8a3a6e7c28 | 2.727 | -60.2586 | 2026-10-10 04:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 6aa62acc-b55b-35fa-86cf-2de5998f90b5 | -7.535 | -45.3006 | 2026-10-10 04:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| debd439a-7935-3704-9c82-a1a8946a8364 | -4.4025 | -49.7774 | 2026-10-10 04:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 745a16e9-88b4-3e08-bc88-b529f2cf54d6 | -7.5347 | -45.3233 | 2026-10-10 04:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 2027efd5-4e41-37dc-a0a9-a34beb24da7e | -10.8909 | -44.8001 | 2026-10-10 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| bb95c457-a771-38b8-b229-8a5233116b19 | -14.3418 | -55.0135 | 2026-10-10 04:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 1092cfea-bed9-3807-874c-a39beeedb26d | -6.4566 | -55.5008 | 2026-10-10 04:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| f71f39b0-5512-3440-92e6-debb2d7b79b5 | -10.9097 | -44.8206 | 2026-10-10 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 3fab2672-fb79-33ef-933d-c4cfa76f32c8 | -3.9912 | -59.356 | 2026-10-10 04:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 8270a326-4eb8-3d55-9b95-56ea4af3c485 | -11.2658 | -46.3485 | 2026-10-10 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| f9465836-6a27-3ee4-81c7-8849b6978ee3 | -11.2467 | -46.3511 | 2026-10-10 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 6b7e3082-ad19-3500-a98a-eec0d045e7d5 | -11.90654 | -46.56998 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 204eada4-53cd-357e-a3f7-3cab22c3299f | -12.0026 | -43.43739 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 933aab0b-0722-3d67-be10-7ebecb5fff16 | -12.22532 | -44.68779 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e195c341-0ffd-3c88-a3a5-ae2ef7e16854 | -13.26502 | -43.99696 | 2026-10-10 04:10:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0fde8e6-1d60-33f4-abf3-96e069f689c1 | -12.96333 | -44.58434 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d658c9a1-4362-3524-a562-97ee23c1197d | -11.84308 | -46.81252 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80a59723-4bcc-3966-a76d-7b5299491b31 | -13.53043 | -48.42984 | 2026-10-10 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8791f09-ca93-34a0-8d95-ae54a2219061 | -13.15042 | -54.36018 | 2026-10-10 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07707496-2fe6-329e-a373-467d5497d77f | -12.04166 | -43.44743 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fea79a7-6666-38a8-80e2-cb4f81bad782 | -11.56512 | -43.70523 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6e57540-140f-35ab-bfee-a71cab3c6cb9 | -11.03222 | -45.44631 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ee3f3e9-3b05-30fe-ae84-3a4e2bc474ad | -11.94536 | -43.47451 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17d4a920-f07e-3f83-834d-81672d3a922e | -15.10486 | -43.63603 | 2026-10-10 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9bdfc284-0ee9-34eb-b190-2c1b31d943a8 | -12.02452 | -43.49155 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3ead73b-ef24-36d4-afeb-3b9a456477df | -10.93123 | -45.3761 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d73a142e-d037-399e-904d-409b79745064 | -13.14448 | -46.33361 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4a1b532-6c94-3495-96e7-71b0680771db | -10.88761 | -44.79009 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8bbf4f9-1df5-31c4-bf5d-dc44a58a1a1a | -14.55544 | -48.02023 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98ec0f78-cddf-30c5-9e1b-b49dcf95e291 | -9.62936 | -48.88073 | 2026-10-10 04:10:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a3ffac84-bfa6-3fc6-aa37-c052796a9dc3 | -11.76688 | -43.52867 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6dc2d3da-2c1e-35c1-b45e-326a47e6a97f | -10.35242 | -46.56215 | 2026-10-10 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3db61567-bdcc-3ac9-b12b-ccf1b0a4f852 | -16.12977 | -46.88507 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 88627690-7299-3be2-adcb-c8f9886d72f3 | -14.51727 | -49.33538 | 2026-10-10 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1d47ac1-f509-3b50-830a-0b70c87aa8f6 | -11.97786 | -43.46183 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63136aa1-b0ed-32ae-9b10-b3ff0a0a903b | -15.56652 | -48.49414 | 2026-10-10 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d277fcb6-d4f4-386b-bfc5-fd6d3d2370a7 | -14.75586 | -48.23407 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45891208-cda7-3bf5-bbc0-ad90ba8ed59e | -13.3538 | -43.90958 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e998861a-9b69-3fa7-a91b-dee92b5bcf23 | -16.71589 | -41.8868 | 2026-10-10 04:10:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c1fd471d-ec12-3b21-badd-1390a64aa2ae | -11.67063 | -43.70488 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 59938db5-5f37-3d6d-b666-4e25ea3ab297 | -15.10155 | -43.63549 | 2026-10-10 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ff8c3d27-8670-3a28-9faf-2dffa0cfaa4c | -17.3457 | -42.68542 | 2026-10-10 04:10:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae81bf89-118f-39f8-8fe8-17784a69262e | -11.75513 | -46.77914 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91d0d342-2694-3d3d-822d-5028f17b2603 | -13.91045 | -48.91468 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a5f8f6ee-8383-31e0-8f3e-508db4da5cf8 | -11.57373 | -45.40336 | 2026-10-10 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 208a1134-ac18-31cb-bc2f-4cc003b1bc74 | -14.34375 | -55.01002 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e42a784f-0d78-355b-b3b0-63808b1095a0 | -14.45189 | -43.93887 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20acd0cb-dd49-36bb-8ed4-d2f75522fcc0 | -11.05505 | -49.55848 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd624d69-87f6-36c5-afed-e9feaaefddbc | -11.20572 | -45.25137 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16447a97-7025-3a28-be89-026ace7016db | -14.73603 | -48.21076 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 598be588-852e-30e7-bcb2-6f41d3e78856 | -11.20508 | -45.25525 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76c3b669-0d62-3ae9-8990-ea81d900f131 | -11.77768 | -45.50943 | 2026-10-10 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d26399cb-e241-3287-9d16-c12973aa3db9 | -12.02122 | -43.49099 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a70b4ae-7919-31f3-8ed5-437b691c5242 | -10.90051 | -44.81887 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 7bd084dc-709a-358b-948a-9767d415fdce | -15.5656 | -48.4993 | 2026-10-10 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abfddc1d-25eb-3570-966d-dc01e1033a2c | -12.0571 | -43.41396 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 518402bb-9914-301f-8e89-779f994a47ac | -10.25198 | -49.66575 | 2026-10-10 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12c295b7-bab7-371f-8767-7383ec19dabf | -11.75292 | -46.79225 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ebcdecc2-a2d0-3ad8-ae0b-969447e22cc8 | -11.85182 | -43.52791 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed2474bb-07f4-3d16-9ae2-6f667877dee8 | -11.46058 | -43.37772 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8886c207-3fcf-39f8-9502-1d66f6454ef0 | -12.95998 | -44.58377 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README44.md)
