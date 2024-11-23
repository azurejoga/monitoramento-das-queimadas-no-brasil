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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 053ef0c6-9488-3996-ad81-ac4b74618eed | -3.94314 | -47.9679 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6b844adc-11c0-31d5-b631-e640313f4a74 | -6.25194 | -43.55624 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 584676a7-cc21-3fe7-be3f-2fadfc83a2e2 | -3.77169 | -48.95948 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8ca0c8d-453a-315d-9a2e-e96cba0892a8 | -3.23834 | -54.25233 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e9c127c-2091-32bf-b2d7-dcdfe9cd508d | -9.72938 | -37.0298 | 2024-11-23 04:18:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 7cac8892-1543-3893-93ed-5c888a1c1f22 | -8.71238 | -44.00096 | 2024-11-23 04:18:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4215229d-e08a-3786-9f04-4c353ca6c549 | -4.47332 | -45.65848 | 2024-11-23 04:18:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f67d967b-a583-337c-a29b-b06edd0472fb | -5.74275 | -46.27046 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2211d470-9b56-34d5-87eb-d2a692c95c7d | -3.7957 | -51.76079 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d10af409-6daa-33cd-bfc5-a40daea94851 | -3.22892 | -54.23773 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a93eb31d-2aaa-3b99-b20e-fcb69f51bc97 | -6.13369 | -44.72618 | 2024-11-23 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6010f492-2056-348c-bb40-c6e4e2648cbc | -2.79713 | -52.46624 | 2024-11-23 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bdd51ff-6c44-3801-96ca-d07efdb971c5 | -4.60457 | -46.50341 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 6ad5db5e-fd21-3613-8ad8-7f6e17c162e2 | -3.12722 | -49.40884 | 2024-11-23 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b56d3da-3c1d-346f-89eb-20932569600e | -4.72697 | -45.49683 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75936c57-e62f-30e0-a476-de5431417512 | -5.42666 | -49.08376 | 2024-11-23 04:18:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7efc8863-489f-3fa1-bdb3-0b742c015348 | -3.12271 | -53.10141 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6ee790a0-5059-34dc-a14f-92a67de5cdea | -4.70805 | -45.85389 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffd3e27f-5bd9-389d-a3f3-51615157622e | -4.69171 | -45.84766 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7deff63d-2f3f-3373-8096-0b089a67f6b3 | -3.1842 | -54.32718 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f7cc3b1-d565-3be2-8454-10dd4c282a3d | -3.11907 | -53.10789 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2dfde597-f9d0-3c0c-9b38-1c90e5d70612 | -6.35133 | -39.79674 | 2024-11-23 04:18:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4c5665e4-44d7-358e-93bb-dac472ab94fe | -10.28857 | -36.66212 | 2024-11-23 04:18:00 | NOAA-20 | SANTANA DO SÃO FRANCISCO | SERGIPE | Brasil | 2806404 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b6717dcc-023d-3d09-983c-d30804adfd55 | -3.96646 | -46.64594 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5e134d7e-89a2-35c0-867a-4a532afc527c | -3.20315 | -54.2501 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8a299cc-0940-3917-949a-ce9901a70e04 | -4.55661 | -45.75203 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a9e9d17-c86c-3da9-a43a-7242b3aa2df8 | -3.78493 | -49.36467 | 2024-11-23 04:18:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c27839a-1695-3f0c-96dc-212ae4b77364 | -5.53978 | -45.78963 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30132c22-b6c1-3c55-8bee-443036193540 | -2.76768 | -54.07016 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6de3f2b2-4bac-3ce9-93ad-c15f04aa3b31 | -4.47669 | -45.65901 | 2024-11-23 04:18:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d1c9c04-d930-3adb-beba-d535e5ed3b4e | -4.54637 | -45.88056 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aaa5d135-f3ef-326a-ae75-09ab9abdfbe1 | -4.68972 | -44.40287 | 2024-11-23 04:18:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7a14f0c-dd39-35fc-b763-36a0a8a698f3 | -6.63526 | -47.34939 | 2024-11-23 04:18:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1b89d13-ee98-344a-814b-4e28c94111c8 | -3.91886 | -46.40159 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d942475c-756f-3bab-afa5-1ad82e6708be | -4.11473 | -49.31277 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f4f930e-51c3-3422-b5cd-3d1af643143d | -5.12958 | -41.56176 | 2024-11-23 04:18:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 88d308de-c341-3986-b4bb-a2dc2389480a | -3.4698 | -47.68828 | 2024-11-23 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb87cd07-3a91-3808-bf0f-a60426c8c7d7 | -5.37089 | -50.85251 | 2024-11-23 04:18:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4869794-02a3-3764-8d0b-5fe4cb03d88a | -3.2418 | -54.2315 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c051a2ef-99f9-3e0f-bed3-0208486326b6 | -4.5288 | -42.7599 | 2024-11-23 04:18:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d846457-e3cf-3379-9dcc-d2e9098ece12 | -6.14207 | -46.68696 | 2024-11-23 04:18:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb5484c3-b199-3078-965b-b015f8a0658c | -3.24418 | -54.25714 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19b0b3be-33b5-3756-a3c0-9d9a2b77412b | -4.27371 | -46.28919 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b405d7f5-9024-36c3-957b-4760acb7efae | -4.34239 | -46.01397 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccc12378-860a-341e-9688-9bbd008d52fd | -3.22316 | -54.23678 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdd096ef-fef6-3776-8e23-03b4e36b8970 | -2.94672 | -53.7218 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a1df039-d5d7-3c9a-af31-a3c9b431d78a | -6.62021 | -47.90459 | 2024-11-23 04:18:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6aa491d-22b9-3deb-a5fd-8085c5c862e2 | -4.07043 | -46.83128 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36a0549f-d31d-3b50-9966-76d0f1708fe5 | -3.70695 | -47.61399 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5381500-9a7b-366d-9a15-d0f604d034c6 | -4.33898 | -46.01343 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afc6c6da-77c5-3931-9439-e3f3971d03a9 | -2.94736 | -53.71806 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fffed58-c330-3fae-89b0-6ad596d6ed2b | -3.23469 | -54.23868 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3cce7fb-2b45-3d34-b52c-e2b4348a1fec | -3.80163 | -46.60959 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85c1872b-dfbb-3d78-88a6-cecf95e1dd19 | -3.24756 | -54.23244 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f02b3c0a-6af8-30ef-9510-eeca6656164b | -6.61729 | -47.89981 | 2024-11-23 04:18:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8dd9e5f9-9240-32cb-bc7e-a97747e0e02a | -5.94644 | -38.3301 | 2024-11-23 04:18:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ea47733b-2314-30e2-87b6-e5c9ed85daf0 | -3.89808 | -47.93722 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c904b024-7fa0-326e-bd77-f99e0a764b60 | -4.74995 | -45.78624 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f134bce5-bf19-367c-a95f-954f8965149a | -3.84349 | -52.39079 | 2024-11-23 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf7146f7-d066-3899-8eed-85b0d21542c6 | -6.26732 | -44.54566 | 2024-11-23 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d78f84cb-ff17-346d-8aea-748a18839631 | -4.4187 | -49.1089 | 2024-11-23 04:18:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c29d2f52-b4a4-3fec-8411-4872bfc55574 | -4.5403 | -42.9066 | 2024-11-23 04:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| bf0ac5a4-d3eb-3839-ac0a-ae0de37e02dd | -1.7359 | -52.7181 | 2024-11-23 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 12e9a48a-0b6c-32b9-8f24-4ea5635dd54b | -4.5216 | -42.9078 | 2024-11-23 04:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 07a02ff9-984a-340a-b5bc-fff6afb0c004 | -1.6075 | -52.5977 | 2024-11-23 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 41e62e13-2034-3b1a-abda-594ac94eec6d | -4.6085 | -46.5002 | 2024-11-23 04:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 28be59c7-fed2-3641-9c2c-c3c63c91fd5a | -1.7359 | -52.7385 | 2024-11-23 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 39ca13e5-0f54-30af-a030-182b99aa7ca8 | -3.2768 | -53.8199 | 2024-11-23 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| bc3de700-eee6-38f6-b060-e5ffdde3d8c4 | -11.78122 | -44.63295 | 2024-11-23 04:21:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37990a56-6f33-3140-833b-09bb05248ea6 | -11.77787 | -44.63242 | 2024-11-23 04:21:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f3d20fb-3302-31b3-b906-369099f362d8 | -12.05052 | -40.47521 | 2024-11-23 04:21:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07a42c50-1e10-36a6-a9fe-83a121daaa47 | -13.24392 | -43.70022 | 2024-11-23 04:21:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 336cfd1f-ca05-3c6e-9b6c-8fdce4362e6d | -12.87679 | -49.26816 | 2024-11-23 04:21:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d4738da2-990e-3fff-81e0-1f8fd2f335b8 | -11.77731 | -44.63603 | 2024-11-23 04:21:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a162b470-dff9-3abf-9ae5-feae15e98e05 | -11.78067 | -44.63656 | 2024-11-23 04:21:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f00c3ab-e341-3c7d-959c-60cbf9b1c085 | -10.9408 | -45.17191 | 2024-11-23 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ebee1ee-d03d-337b-a794-17f03fa94c3b | -11.97914 | -44.21388 | 2024-11-23 04:21:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b0ea4da-4185-32c3-99ef-a7b78d9272ce | -10.84924 | -48.96798 | 2024-11-23 04:21:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 760ed750-c64a-3c67-a114-8aa93284f2a8 | -13.39361 | -48.45399 | 2024-11-23 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1e3f73d-84cb-3dec-8e0d-28b7557282a0 | -11.02976 | -44.6819 | 2024-11-23 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 354ff3dd-4903-3dca-985f-e54a7bce9a56 | -11.03031 | -44.67833 | 2024-11-23 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5dec781e-c90d-35ff-ae57-dee122f8d668 | -23.59288 | -47.43806 | 2024-11-23 04:23:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| df887f15-b2b3-3b00-9a57-a11803fe5ad2 | -21.38697 | -48.5998 | 2024-11-23 04:23:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9ee1c5aa-ed0d-33e9-8229-b28998724e77 | -22.53894 | -48.81406 | 2024-11-23 04:23:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1baf1297-884c-3c5f-b4f6-f40705f6ab3f | -22.06539 | -46.91302 | 2024-11-23 04:23:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 44be5d3c-8e7a-3b7c-9cf8-57aeea9831a2 | -21.38192 | -52.94372 | 2024-11-23 04:23:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3defa842-4428-312e-a16a-7393c1854ddf | -23.63253 | -46.42556 | 2024-11-23 04:23:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c6c940c7-1397-3523-9b99-4824c9fd6983 | -24.2422 | -50.7406 | 2024-11-23 04:23:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 41b84ae7-b0f9-34ee-8718-3db2ed07ea28 | -23.96173 | -48.70736 | 2024-11-23 04:23:00 | NOAA-20 | TAQUARIVAÍ | SÃO PAULO | Brasil | 3553856 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b95a3ad4-710d-36a8-b292-7874c1de29dc | -20.63247 | -50.73617 | 2024-11-23 04:23:00 | NOAA-20 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6cf8851b-a50c-30ef-9b50-10db226429f5 | -24.1181 | -51.05872 | 2024-11-23 04:23:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a7025b22-8eaa-31cd-b91b-bf29ab8b8987 | -23.98246 | -48.92022 | 2024-11-23 04:23:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8629d63b-e74f-3647-a674-b127bbebafae | -22.6424 | -49.78506 | 2024-11-23 04:23:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47d37123-eaae-3868-a67d-c57b1b4a82b7 | -23.98306 | -48.91645 | 2024-11-23 04:23:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9b9ab6c-4e19-37e3-8183-c4471cf490a8 | -21.38297 | -52.9402 | 2024-11-23 04:23:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be9a788e-a8a6-367c-9ade-ffe30d8c8357 | -20.6332 | -50.732 | 2024-11-23 04:23:00 | NOAA-20 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9b584d62-21f3-3258-b116-6e4ca05575b8 | -25.11379 | -48.71975 | 2024-11-23 04:25:00 | NOAA-20 | ANTONINA | PARANÁ | Brasil | 4101200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7b40021d-7d6d-3c87-890a-35fcf1ec6494 | -25.10989 | -48.72295 | 2024-11-23 04:25:00 | NOAA-20 | ANTONINA | PARANÁ | Brasil | 4101200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 937d74ba-91e7-3dde-928d-ed7b132bd1b7 | -4.5403 | -42.9066 | 2024-11-23 04:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| e1f70790-82cd-3599-92df-ad8a7872d5aa | -4.2605 | -48.697 | 2024-11-23 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |


[Clique aqui para ver as próximas entradas](README45.md)
