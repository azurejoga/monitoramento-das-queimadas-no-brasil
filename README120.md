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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cc4d777-facd-34a1-acbc-d4d6b39c6a01 | -12.5994 | -55.2162 | 2024-10-11 13:36:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 6baa223d-69f6-32f8-8fab-630d988e13c4 | -13.0353 | -42.1577 | 2024-10-11 13:36:19 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 87.1 |
| fe1afc4c-8089-3301-90a9-b5445aa39882 | -12.9658 | -53.511 | 2024-10-11 13:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 241.6 |
| b8f82af5-5ad7-3bc2-b7f8-b774ad61f7a9 | -13.9548 | -44.5011 | 2024-10-11 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 4bd7a54d-b057-3476-95a6-091e5e4835b1 | -13.9348 | -44.5282 | 2024-10-11 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 92918c36-48b9-3bd1-9859-61bebc1f6440 | -13.9543 | -44.5247 | 2024-10-11 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 0f1c1d60-727b-3947-b0ac-7ebceb6051bb | -13.9353 | -44.5046 | 2024-10-11 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 3741fd1c-9ba0-3069-97fc-d3787eb061b9 | -13.8734 | -44.6799 | 2024-10-11 13:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| fe1fb2de-3b70-387a-a149-ce9739d0cae2 | -14.1392 | -44.9603 | 2024-10-11 13:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| c075936c-ee61-353f-8cca-cb17e6326557 | -14.1197 | -44.9637 | 2024-10-11 13:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 08cb93f7-7b3c-3557-bab6-a5cafce83bcf | -14.1202 | -44.9403 | 2024-10-11 13:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| c3502bef-fc96-313f-ad44-70d8ed5f5f2f | -14.1192 | -44.9872 | 2024-10-11 13:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| f40ddcf9-8ef6-3768-bcb2-a2eb093db271 | -14.1002 | -44.9672 | 2024-10-11 13:36:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| dbad423b-7fa4-3d43-aef9-46ac219b00c3 | -1.0244 | -48.8087 | 2024-10-11 13:45:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 83fe85bb-c7e4-3fd2-8a4b-4858f450985f | -6.747 | -59.3259 | 2024-10-11 13:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 0c9a1799-605c-30da-bf2d-01db872fc01d | -7.0417 | -59.4103 | 2024-10-11 13:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 7925565a-0306-3ff9-b62a-dbdd3aab374f | -7.0416 | -59.4296 | 2024-10-11 13:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| c328d750-1f48-3287-88ab-ca498e37aa0b | -7.0601 | -59.4095 | 2024-10-11 13:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e9a77e8f-13a3-38a7-b0dc-f9f6cb167044 | -7.964 | -54.7562 | 2024-10-11 13:45:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a025747c-01e3-3687-a8de-d34d77964190 | -8.4233 | -55.4503 | 2024-10-11 13:45:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| f52e1998-769e-32ae-9905-f1fa4b22974f | -8.4417 | -55.4692 | 2024-10-11 13:45:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| ebb1aa7a-1dc3-331c-a5dd-3b6036fc15e4 | -8.4231 | -55.4704 | 2024-10-11 13:45:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| a6ebda55-3595-3dbc-bd24-e62cead62a98 | -9.5852 | -44.3923 | 2024-10-11 13:46:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| e0784604-8387-35b5-b2a2-1650d05a8636 | -9.5662 | -44.3946 | 2024-10-11 13:46:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d0c1237f-fa6e-354c-901a-543ac4e64fce | -9.8367 | -60.2783 | 2024-10-11 13:46:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 0a40d3bc-357d-345e-94d3-f1faa0ecadfa | -9.8552 | -60.2966 | 2024-10-11 13:46:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| db660bea-b70e-3dd6-8a80-a9ceb2158fc3 | -10.7151 | -53.0337 | 2024-10-11 13:46:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| fed09c33-1f7c-34cd-ac5f-8684081d8897 | -11.2597 | -53.272 | 2024-10-11 13:46:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 094f34e4-1dd7-3cc3-a7f0-cc505d0b5444 | -12.2978 | -45.3112 | 2024-10-11 13:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 60faece2-1afd-3aef-bbe5-256d54d0ca0b | -12.2974 | -45.3343 | 2024-10-11 13:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| ee8bc5d8-eeef-30c5-94fe-3df407db2ec9 | -12.3167 | -45.3314 | 2024-10-11 13:46:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| bef2073b-a492-37ee-9147-a36585f41390 | -12.3171 | -45.3083 | 2024-10-11 13:46:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 5caccfa9-2cda-318c-96fa-66b7600cd057 | -12.4754 | -53.1482 | 2024-10-11 13:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 40411fd4-b97d-3916-8387-799e4587a8fc | -12.3989 | -53.1772 | 2024-10-11 13:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 293.4 |
| 706a6d44-de1a-38a0-b28e-8c582088bd51 | -12.4563 | -53.1503 | 2024-10-11 13:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 164.6 |
| 34c20811-1c75-30eb-a17d-f9f43930d3e5 | -12.6909 | -45.8712 | 2024-10-11 13:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| c792a69e-f764-340a-a253-7b02377d306e | -12.5996 | -55.1958 | 2024-10-11 13:46:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 127.4 |
| cb9f8c0a-3864-33b9-8baf-82b4638c1764 | -12.5994 | -55.2162 | 2024-10-11 13:46:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| d5fc0c62-65f3-3cf0-b184-daf6517265a0 | -12.9923 | -46.213 | 2024-10-11 13:46:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 6db3c6c2-6060-3b5c-84c1-993378e38a95 | -12.9919 | -46.2359 | 2024-10-11 13:46:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 032b4588-7b75-3bb1-bb04-980f316db3ad | -12.9658 | -53.511 | 2024-10-11 13:46:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 188.6 |
| 1ee051e6-4b21-3c2c-9eab-a4a28d1806f2 | -13.9548 | -44.5011 | 2024-10-11 13:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a66e5cae-d5e6-35b9-8941-fc797ed3dd27 | -13.9543 | -44.5247 | 2024-10-11 13:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8106ed7b-4de1-3abe-ace2-e603fe0de3ce | -13.9353 | -44.5046 | 2024-10-11 13:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 479cc8c4-c7b4-38d9-b010-23abc7c274fd | -13.9158 | -44.5081 | 2024-10-11 13:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 502636ed-58c9-3769-a999-5856f1181146 | -13.797 | -44.6231 | 2024-10-11 13:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| ab607d7a-c28f-366e-8b68-2c6ca25a61a4 | -13.9348 | -44.5282 | 2024-10-11 13:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 75259d70-a709-37bb-a76b-d42cbdfcd9d7 | -13.7965 | -44.6466 | 2024-10-11 13:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 6a4a4cb6-0769-3a72-8002-7e67d08fd47e | -14.1397 | -44.9368 | 2024-10-11 13:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| ed2fde4f-06f6-3fd2-b647-b0300471343e | -14.1392 | -44.9603 | 2024-10-11 13:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 44748c0f-bdc2-3914-81ed-fd594bc90850 | -14.0997 | -44.9907 | 2024-10-11 13:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 4de167b3-7e6a-3a55-8202-0fb7bbe6cb07 | -14.1197 | -44.9637 | 2024-10-11 13:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 8afa7562-5814-33ea-90e4-6bf09ce2dbcb | -14.1202 | -44.9403 | 2024-10-11 13:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b485a68b-a3c1-3b3e-84b2-9c8f41b455d2 | -14.1192 | -44.9872 | 2024-10-11 13:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |


