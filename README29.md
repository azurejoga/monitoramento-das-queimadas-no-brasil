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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28696efb-96e4-34c5-8453-3fa25f62e87c | -6.86403 | -38.56784 | 2024-11-29 04:04:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 16ea8f77-5d9b-396b-821a-d510aad55ddf | -2.83275 | -49.88839 | 2024-11-29 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f091dbd0-df23-36c9-8c6d-db26a1a7ab6d | -3.27884 | -50.04061 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2662cf0-770a-37cc-a33d-c62cdc8a51c3 | -3.99587 | -46.32044 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb211b4a-a5fe-3af4-bcfb-19afc4795945 | -3.79083 | -46.69415 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3faeefb2-94e9-3d68-810f-97f9d9ede4ad | -5.62856 | -46.96148 | 2024-11-29 04:04:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f9b5b85-1bd7-33c9-9fa3-cebcc9e58097 | -1.52692 | -51.62406 | 2024-11-29 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cea5a08f-b167-30fd-9a56-944eddea2ce4 | -1.33223 | -51.92632 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1fe2c537-a4c9-3349-a0e7-6c4cecc5ad63 | -1.67491 | -52.42712 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54eba89a-a2b8-3695-bd59-ef89b146ec69 | -4.41326 | -50.82701 | 2024-11-29 04:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b05fa900-c9b4-3521-b7af-cfda321a9759 | -3.85392 | -50.15048 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cd307b1-ace3-314d-a4d2-3b5762216eaa | -1.53305 | -51.62515 | 2024-11-29 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9b42d9ec-a9c5-3486-96fc-a34c669012fc | -3.40914 | -50.17206 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f2f9ee7-40ab-3845-8086-acd824dd5a04 | -2.61163 | -46.56398 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57e3f891-0c8e-3f3c-8221-daf90f634dde | -3.34817 | -46.30398 | 2024-11-29 04:04:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5c010d0-336f-3e11-84d9-076401430ca1 | -3.96516 | -47.24312 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34c5d181-2641-39f7-8d5e-9aef7a4d07bd | -4.39022 | -41.7179 | 2024-11-29 04:04:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d62c853c-2dbf-3251-acba-0cae55a1d11e | -5.37591 | -40.3747 | 2024-11-29 04:04:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e7c0c6fa-a013-3d2e-a3d8-7a93c41f5391 | -2.57237 | -51.84303 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 517f474c-6419-3905-b363-7ad25810b70b | -4.17922 | -46.84151 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05fd5ed5-a2eb-3b0f-a787-03f72934d563 | -3.09916 | -50.36988 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9986496-81e6-32ad-bcfc-1ad711b8ab8c | -4.86499 | -41.27166 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4c2fd5dd-b3ad-3593-8490-c34bd0a92ca1 | -4.44986 | -44.00285 | 2024-11-29 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 652dce29-dcc4-3f86-a3c8-1f8a2afee570 | -5.20927 | -41.28772 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 11ae0fbd-2979-3155-8b0b-7b98d40d4130 | -1.93891 | -52.96622 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1eee5ee-151e-3e81-b494-30149b998d11 | -4.42958 | -46.58018 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| a3d8bafc-903e-3dad-a277-159e816038d9 | -2.41997 | -47.60682 | 2024-11-29 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff108458-3646-32b3-bdd7-175a03d391f3 | -4.43314 | -46.58468 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 0af481da-bbfd-3bce-bf5a-8fe8c7432e3b | -5.92958 | -39.96112 | 2024-11-29 04:04:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 60e8b887-4483-39f3-81c8-e85d8e65226e | -4.43252 | -46.58854 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 28.7 |
| e677f7a0-8f99-3294-93b6-694123cef2ae | -2.60906 | -46.56421 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a6a322e-60f1-3607-8bdb-bf38a884c68f | -1.65553 | -52.50661 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d422105e-7406-30e5-9716-dd66d83b3f4a | -3.47696 | -49.92702 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5473d51c-1591-3c09-9bfd-e81fad498a7c | -3.33102 | -46.70405 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40cca87d-ab50-335b-be0d-adfa3cfae3ec | -2.77735 | -48.58054 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c931f07-6c9e-3189-8adb-77bef849b92e | 0.98595 | -50.1301 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f44cd583-97ce-3b69-8f5e-6810e3693655 | -1.14124 | -48.34743 | 2024-11-29 04:04:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef3e01ed-6afd-3527-8826-d28f3a3931ce | -3.33167 | -46.69997 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 10618509-f1bb-3287-8e4a-cbdef53782ce | -2.51973 | -48.51675 | 2024-11-29 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52bfd893-5efd-32de-8551-695233ae897a | -4.06099 | -46.68755 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 320a1655-a25c-3060-bf52-ecb5ac2c0293 | -5.76653 | -43.39468 | 2024-11-29 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 884eb0e1-4fc9-3444-9d22-f8cc74c56bb4 | -4.01693 | -45.96559 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f7ab4e69-02c8-3c2b-bb3c-f9a3f113af8e | -3.81255 | -44.04791 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca3d27b3-9ce6-3938-99d5-f9c7d4240d53 | -5.04129 | -43.61559 | 2024-11-29 04:04:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 51f93b28-c958-3c1a-9a10-812564539c0f | -2.6807 | -46.27799 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9c86d16-d8ea-3e07-90a8-410d1e0dd1c0 | -2.87219 | -46.86642 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15bba04c-aaae-311a-af42-e6289ab3349a | -3.36878 | -50.17971 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c6f9374-267f-3257-b942-8e78fe75cf45 | -4.22595 | -45.77909 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f986ea88-0cb8-357d-8f09-a3e65fdc0df4 | -5.4792 | -42.07237 | 2024-11-29 04:04:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 95115ae7-9e9d-3bc6-9120-fdc2d80c9525 | -2.85142 | -46.82858 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e57e2d4-54d9-3f69-b16d-3f7ab7ab2760 | -1.61644 | -52.46106 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21592594-4815-35c9-bb7b-43e200eed324 | -2.65901 | -48.8011 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a709a26b-e8c4-37ba-b8eb-545549e679d6 | -1.14213 | -48.34176 | 2024-11-29 04:04:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 879457a0-c374-3cb8-9352-34294755f925 | -3.86745 | -48.36802 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| adacf42f-2b66-3a6f-a55f-0205372c127d | -2.85637 | -46.88115 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf77f729-13cd-33c4-b32f-4e3ecef5f256 | -4.95488 | -44.15928 | 2024-11-29 04:04:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4749816c-fca5-353f-b433-dc3d43ffcf6c | -5.12163 | -45.155 | 2024-11-29 04:04:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0d0e1cb-1428-3dcc-9fa6-5e264ab4f296 | -3.38704 | -54.28602 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a61f4eb0-796c-30a4-a448-238c7bf30021 | -4.01669 | -45.96252 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 52df193e-bb27-382a-b6bf-2b5ee5417399 | -4.04902 | -48.33633 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8de8b547-355d-35cf-ba14-b1f648f85996 | -5.23076 | -44.91292 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4f264014-b407-323f-a2e4-b4fbe3f9a7dc | -2.53542 | -47.32928 | 2024-11-29 04:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60e4936c-cf3c-3bc6-bb96-1d7311667145 | -2.52353 | -47.07494 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72965e3c-b6b0-37cd-994d-f6d9812e13a6 | -4.8804 | -44.64487 | 2024-11-29 04:04:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b633b2e9-3629-3808-af92-99daf6dd85fe | -0.04657 | -50.82264 | 2024-11-29 04:04:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c632fbf-8b75-3fe4-a98e-a1346f94d0bf | -1.87891 | -48.5466 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94fcb16b-9e2b-3804-b934-2b9a751a1df6 | -2.58411 | -51.92153 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 078cb747-ca30-38bc-9ebd-540ddca21c8f | -3.19665 | -46.56691 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.4 |
| b3f0d0c1-8e39-3263-87b5-e20d79cc29eb | -3.47113 | -50.54401 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50d324d1-9fcd-3b2d-9dbd-90f17683a909 | -3.2439 | -50.59153 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 117b8e20-bace-3596-8eda-d2ab2287d460 | -3.34552 | -50.52275 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7c89d03-f2b6-33ee-aad7-accd4250ee94 | -3.83576 | -46.52893 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fddad14-7e53-39f8-bb26-c0d70e17e6b2 | -2.64836 | -46.12708 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2249961-cdc3-34ab-a772-b5cd24558ff3 | -2.66635 | -48.78754 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa3d6cf4-6410-364e-b0b4-0a8feda97de9 | -5.04417 | -43.62003 | 2024-11-29 04:04:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d2a7ae4c-5b63-3824-93b0-a24d5b656c41 | -3.24951 | -50.62759 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db889df8-d81d-32f3-b38f-39ec3d6bc4d8 | -3.68956 | -50.22383 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf92100c-3afe-36b3-95ae-1efe94832bef | -3.62781 | -51.43089 | 2024-11-29 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8da21532-f7b3-3d8c-bcbb-91578067b00b | -3.21912 | -46.29864 | 2024-11-29 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66200434-b447-319d-b3c4-6e46f03522c4 | -2.83861 | -46.8523 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae842c9b-e656-326d-a7fa-381687ec9e03 | -3.52177 | -50.48125 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9fba9db7-eed1-3400-b85e-b0126ef3b030 | -4.10089 | -46.11447 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb85609a-86ae-3703-902c-62ba8dd1ae96 | -3.14879 | -49.43462 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6903c620-0ed5-3944-b6ce-9c1090f62b7c | -3.17415 | -48.43794 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56111c47-2187-31c9-9be8-96e2573bdcc9 | -2.52714 | -47.40871 | 2024-11-29 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbb5763a-81d0-3521-9c7d-517f25033519 | -3.24846 | -50.6217 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34f746e0-259a-3223-89a4-41aea142e051 | -1.69839 | -52.45043 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 46cd3cd5-2c71-3e23-89df-db5519864f25 | -3.70238 | -50.51941 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e407326-3b1f-34d6-b4a7-e73622e8b60a | -4.16918 | -44.27407 | 2024-11-29 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5062b43-e22f-3a10-8ffd-78544cc28860 | -3.29025 | -50.61319 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e4119dc-1914-35f4-85ae-ef97592ec8f1 | -2.69164 | -51.99175 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79a3a9a6-8a28-358a-a443-2e1bf687ee05 | 0.98369 | -50.26753 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 698a472e-99b9-3e7a-a4b2-c3bc8b06f70b | -3.27904 | -50.61132 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f1fca96-041b-371e-94d6-623568166d68 | -5.89449 | -35.41421 | 2024-11-29 04:04:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f5c0f7ea-0231-39dc-a939-595ec77021dd | -3.47642 | -49.93034 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fec713b-d860-369f-a229-32cb9b468cb3 | -2.64994 | -48.79362 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 624b957f-2090-3a43-9e6f-1b9d51b57456 | -2.83107 | -49.84783 | 2024-11-29 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12fd4a2c-0cee-3319-b2f5-48cc21016147 | -1.16153 | -53.68 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b44cd7c4-e345-3adc-9554-7edca00d5dd2 | -1.94455 | -52.97326 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ef9390b-b658-3f88-95d6-036612435ec8 | 0.98953 | -50.26661 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README30.md)
