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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d0e82ca-cbea-365f-8fee-05041e595f40 | -3.4974 | -53.8339 | 2024-12-01 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 81dc6613-7e74-3416-9e68-e0d17074b070 | -3.2591 | -53.6186 | 2024-12-01 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| c65515db-81a2-3282-9483-198b7a961e96 | -6.9156 | -43.5418 | 2024-12-01 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ae7be7d7-ccbf-3041-8940-3205eeee7fdf | -4.5562 | -43.3028 | 2024-12-01 04:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 0149307e-d66b-3f06-9496-b4e97beee8ac | -4.5375 | -43.304 | 2024-12-01 04:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f942c4f0-205e-3990-bb2c-1eac6b30c8b2 | -3.1273 | -54.5264 | 2024-12-01 04:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c0ae30fa-8e39-3ecc-ade0-7614cdb454aa | -4.5562 | -43.3028 | 2024-12-01 04:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 275fbb70-832c-35f2-8503-2ccb3b3e01f2 | -3.1273 | -54.5264 | 2024-12-01 04:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 31addaf8-d8c0-32e4-bb95-342b7a466255 | -10.6674 | -44.4835 | 2024-12-01 04:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d818abab-9c84-3522-8daf-02a3d8edaaa2 | -3.4974 | -53.8339 | 2024-12-01 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 13e7fcea-098d-3c2a-bfec-7cf9c2dc229a | -4.5578 | -45.7232 | 2024-12-01 04:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 4ef37575-ebc0-36ea-8eb8-bd5c8b550c97 | -4.5375 | -43.304 | 2024-12-01 04:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 486c3495-d956-37d4-aeed-e34f055825fa | -2.9963 | -45.5706 | 2024-12-01 04:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7d3dc1d2-d655-3001-bd04-76748121b873 | -3.259 | -53.6388 | 2024-12-01 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 4f905c5a-7537-3369-981a-5eeb3e061062 | -3.2591 | -53.6186 | 2024-12-01 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4769e48e-e456-3a0d-9a62-f793aa47662a | -4.0052 | -44.7596 | 2024-12-01 04:20:00 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 07c9c410-ed73-3130-bf73-080809fbcb97 | -2.8013 | -53.043 | 2024-12-01 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c970f4eb-527f-3dd1-81d9-cbe04cb3f2f0 | -2.9778 | -45.5713 | 2024-12-01 04:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a8557b48-85e5-35b0-b109-09e90835e4fa | -2.8197 | -53.0425 | 2024-12-01 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 04703d64-e97e-36e7-9f46-1332b67f0df6 | 0.93713 | -50.74545 | 2024-12-01 04:21:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b68d9e70-5744-346c-adfc-7ca8239c2763 | -1.95898 | -46.44136 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fe98392-694a-34e0-90af-be29ebf88902 | -3.41254 | -51.97678 | 2024-12-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 660eef4f-8d10-35fe-9519-72677b93b99d | -3.21312 | -53.1271 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 12a925a4-b4eb-3366-abed-241083008b42 | -1.2666 | -54.5555 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f3955b41-04ff-351d-ac5c-756c95c58c77 | -2.96394 | -53.72406 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3ce1ad0-96ca-3bfa-acfc-1d47b0241f34 | -4.00297 | -44.75336 | 2024-12-01 04:21:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc4d8034-20c2-3aad-8e55-5035de4110cf | -3.45567 | -44.92612 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eb4efc7-066c-3f42-aec1-0f16a7b41d4d | -2.99924 | -51.06738 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8bbb32f3-ab01-302d-ade2-a2f79517c5cd | -1.70356 | -46.1476 | 2024-12-01 04:21:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 68709ffb-a993-3f1e-90c6-cf9898a54c03 | -2.99659 | -46.94251 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8aaedb8d-f77e-380d-b5d6-b2882267b4fe | -0.20127 | -51.40364 | 2024-12-01 04:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffb9266a-feb3-3962-923f-e25cfd685e09 | -3.12422 | -51.78941 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2abe665e-9d50-3edb-b88f-3f7d0d63af2e | -3.58825 | -51.20789 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aad3de4-f442-3503-9133-4da13647f3fb | -1.43788 | -53.39858 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d18e64ef-3252-3f3f-899c-4b01f30ba569 | -2.70182 | -45.41827 | 2024-12-01 04:21:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94fb4c77-d541-3829-aaab-a22dae1821f0 | -1.32496 | -51.67855 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| dbdc2dae-6dee-3024-9980-906cf143b628 | -2.88068 | -46.80392 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89f6b44e-6f60-377e-8539-fed207e50e3b | -2.76211 | -49.22525 | 2024-12-01 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94e7dbf2-3152-3686-bba3-11f5293477e2 | -3.7003 | -47.14583 | 2024-12-01 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2c5f217-601a-3ab2-b4d0-03ec6448170e | -3.04019 | -50.24082 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5396ba6-d0eb-3d13-bea3-e7a85fa37f2c | -3.40226 | -50.66128 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0dfdd69-1d0b-3e89-b6f1-711af571a00c | -2.6357 | -46.19998 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b542f821-a18c-3fe5-bc58-8d5c5cb8838c | -3.69701 | -50.16637 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ca5342f-2be2-3720-a4a4-572643c0d931 | -3.06848 | -53.81051 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 40707b67-756c-3334-b11e-01f15356396e | -2.80629 | -45.94129 | 2024-12-01 04:21:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca6fb9c5-0a06-30a7-8c9a-138a527c7021 | -1.725 | -45.76397 | 2024-12-01 04:21:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 433f88ba-56c6-33a8-bad4-465d8d0bbe57 | -2.92821 | -51.45198 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fa028cc4-7f64-3924-8226-e4cffe14c46e | -1.733 | -49.81426 | 2024-12-01 04:21:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32bf1870-85fc-320b-89a7-005218dbac37 | -3.75268 | -49.93537 | 2024-12-01 04:21:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 996f2073-0bf8-3363-a059-c76131a47eac | -2.74989 | -46.09887 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 567c9b5a-cbce-3db5-a286-0367deefcd77 | -3.59792 | -50.3749 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eed3c6c-ffa3-3583-8d52-5699391dc8ed | -2.12618 | -45.98067 | 2024-12-01 04:21:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cb54bae-ee22-30ec-8087-81cc3598f59e | -2.61428 | -51.81387 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01a966b1-9bd4-3cd5-8bf8-deae5deca9d4 | -4.89543 | -41.32101 | 2024-12-01 04:21:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1cd7bd0f-3a71-3b61-b17d-97c68f282f48 | -3.88927 | -46.68598 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7168dbda-e257-3280-bf62-fc15f2fc05b0 | -3.98374 | -46.64186 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8855e229-a2c2-3696-a00d-3934fe1861ff | -4.0082 | -46.31179 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d724c4b4-080f-30e4-9f60-4dacb965b257 | -1.32005 | -51.67781 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5c86d1b9-9795-3878-ba9f-1074c4482d00 | -3.26912 | -50.20796 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ee695066-ee65-3b99-9dc5-1c4aed709b76 | -2.65768 | -51.87358 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| bd0c2ef7-0cf9-3118-9b9d-e9d15ea9deed | -2.30902 | -47.90921 | 2024-12-01 04:21:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af30fe61-56d0-3ddb-8953-4aabc285cb79 | -2.6544 | -46.12628 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e079a13-d829-3f90-adcd-1ae97b0268ae | -3.23785 | -50.24903 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c63d0d5-0b4e-33a5-99f8-787d742f7dac | -1.82619 | -50.90365 | 2024-12-01 04:21:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1b565d59-957f-3512-b96d-38246d428a9d | -1.2732 | -54.55225 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe99e59d-43d3-32b4-8163-da39137b91d2 | -2.12258 | -46.41052 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f3bfe5-b53c-32e7-aadc-217e07c5e6c0 | -2.63571 | -54.19772 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f27752ad-ae00-31d1-b525-ad60f956b370 | -3.2126 | -53.13031 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7c662949-5afb-3b83-a2e5-b76f4ffe9020 | -2.61596 | -46.23538 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6514ed2b-5198-3b73-8360-38d10d6a3985 | -2.6709 | -46.59583 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91f42dae-4437-36e2-97c4-798fa6bea65a | -3.33014 | -50.18446 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dbf71de-35ba-35e7-9cee-432df1f84add | -1.70306 | -52.64082 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16dbb525-ba97-3e97-b626-a5299e5c6254 | -2.13066 | -46.41494 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b47dbca-bc00-3a9e-9953-e92800b604f6 | -3.03141 | -51.5423 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3fb46bc8-e224-38f9-bde0-3b132e7a7a93 | -3.2245 | -46.44814 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8c7e210-c1f9-39e8-93cd-31bd0fb26e43 | -1.00877 | -51.72501 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d104dcae-1ad3-3c0c-8b1f-b144b34f19d3 | -3.17622 | -53.64098 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 426f671d-c72d-3ebc-9173-227afbef2b5e | -2.62782 | -46.2721 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e414984-2b11-3246-a47f-60d422410072 | -4.04562 | -44.72129 | 2024-12-01 04:21:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 099c5c67-3695-3f5b-b53b-5e264fc39cbe | -2.12628 | -46.5774 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d809fb39-2235-370a-b2c9-02c7bbb45976 | -3.30185 | -50.80291 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05643ec8-e717-3a9b-aa7d-792289ef2ecd | -1.18631 | -51.7743 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 824749be-4737-3397-adc0-3e3e5052b944 | -1.94512 | -53.3406 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd0fd327-fbc4-339c-a77b-a32dcecb4ea1 | -2.81055 | -53.05177 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d18ed7cb-6267-3cf1-bc50-5a133bd13ea3 | -3.53853 | -50.18257 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f0c42d4-9c57-30c0-9257-5860d0312338 | -2.9641 | -48.04147 | 2024-12-01 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 298876bc-7c6e-3ed4-8d7d-690882dcf172 | -2.46359 | -46.57634 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9c345af-be3b-32e5-9ebf-c485ab3ae417 | -4.03508 | -46.54124 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad2fdcb1-7f70-3034-8354-b6f4cdd1ec8e | -2.69001 | -48.66114 | 2024-12-01 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b9631e6-fa54-3980-abdb-2f343b9f68f6 | -1.13948 | -53.67035 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3102062a-b886-38b0-aa2a-92dbe407c3c6 | -4.51892 | -42.93455 | 2024-12-01 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73bed789-5b29-365a-8893-a214d12791db | -1.62472 | -45.6879 | 2024-12-01 04:21:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd9945a9-4aca-3152-b91a-a6a500b15e8c | -2.74977 | -46.12172 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 667678ff-0ef2-37ab-a759-5e90c89597f4 | -3.26848 | -50.56648 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5c0c96d-5526-36d8-bb07-c062513c26f5 | -4.44205 | -45.35925 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceb8df01-90ab-3514-aa8b-3fbcf64d4301 | -4.03896 | -46.93347 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b293b787-2e66-35b3-90e5-b71dc3f4d8f6 | -2.87426 | -46.79889 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bf1cab1-91a7-377d-85d5-e895efbd783f | -2.65783 | -46.1268 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d52542df-1b6b-3272-8ebe-9eec6788c3ab | -3.93631 | -46.71628 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34c0098a-79df-3ad6-991b-7a26a5f47b64 | -1.09282 | -53.63818 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README23.md)
