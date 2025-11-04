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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b35cceb-a521-372a-94fa-3edaf6bfd120 | -6.41516 | -43.06636 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 81288ec2-4e0c-3cd9-ac14-ca52e90b14dd | -7.3314 | -46.29503 | 2025-11-04 04:31:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd11756e-ff44-3d67-b96d-a319f746e9dd | -4.91101 | -45.09187 | 2025-11-04 04:31:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f6a207d-d048-38b3-9b22-b94d3d5e3795 | -1.58794 | -53.23282 | 2025-11-04 04:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36ffb6f0-fe5f-35a0-8e57-ddecb748fe3a | -3.61954 | -50.48591 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 860ecb00-880f-3faf-9f47-6a8fa785e4db | -3.00682 | -49.47342 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d57c8dd-ed34-30ef-8f2d-8b560c794da9 | -6.40256 | -43.06955 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5748dfda-28b8-387c-aa0f-1da1c9f05903 | -4.47629 | -43.22694 | 2025-11-04 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8d83235b-cc2e-3d3c-bb7d-96bc9ca7cd6a | -1.76671 | -53.55804 | 2025-11-04 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00999247-f5bd-3744-bc89-a83545ea173a | -9.92826 | -44.81752 | 2025-11-04 04:31:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc4db71a-8166-393d-8d98-949bd4cdb2c4 | -3.43438 | -50.24011 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 350d0adb-aeff-30e5-8e72-f44501bce1e9 | -3.77274 | -52.32381 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 354799fb-2450-3dbc-bb54-2392803fd0e2 | -4.3128 | -41.45237 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d69ef118-ebc8-394b-b256-dd3bf56ed7d7 | -3.34247 | -45.37764 | 2025-11-04 04:31:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 805c99d4-6714-326f-9948-5f2f2e970486 | -3.5203 | -50.31191 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24239491-1146-35de-af9d-00f47dca22ef | -7.0991 | -49.96058 | 2025-11-04 04:31:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a102c8d-7589-3a23-afa3-1efac859ef05 | -7.55056 | -45.85076 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 156be865-265a-306c-8788-5dbd4a1f2c60 | -4.25158 | -46.38243 | 2025-11-04 04:31:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2a152ea-5d40-381f-b087-8e9c359d562f | -3.44573 | -53.26019 | 2025-11-04 04:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e6f7625-1fb6-3f94-a13a-26d0c4885983 | -3.02172 | -51.09188 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5ee928d-e2df-3584-a627-12c450e218e3 | -7.55459 | -45.84752 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0697847-c940-3bbd-9203-a375f3f89b6d | -6.64008 | -43.14427 | 2025-11-04 04:31:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24f0f6e3-a2f4-3bb7-86b4-f99be71bf771 | -3.43731 | -50.24482 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 9f188e96-d87f-3d04-ad33-a56372352a95 | -5.83582 | -44.06136 | 2025-11-04 04:31:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8a4f784-3804-391c-b561-5e09a0f1fbb5 | -3.02116 | -51.09386 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e211978-a20f-34aa-80e9-f8033c3dce4b | -5.61811 | -45.97952 | 2025-11-04 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95bec43d-bbd4-3773-b13b-59ef164756b5 | -4.8737 | -47.54591 | 2025-11-04 04:31:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a538b438-74d2-350e-bfcd-8abf4bc13360 | -2.34613 | -48.11979 | 2025-11-04 04:31:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f56a8d0-744b-3988-b7ae-1fe5ecccb7b7 | -5.52094 | -41.08719 | 2025-11-04 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ae416177-dc5c-3756-8b87-8e9eb20948be | -4.61549 | -46.5963 | 2025-11-04 04:31:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09c978d1-972c-3f4a-85af-4a376433be94 | -3.44555 | -50.21647 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52b3b3ff-cd8c-3bda-9433-4bc81f807786 | -3.0458 | -50.27742 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63ef7af1-2014-3e62-9442-bc270b5c5459 | -4.02648 | -45.46203 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f49ac681-a294-36d9-b224-705e12b6565a | -6.35382 | -46.47178 | 2025-11-04 04:31:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba59c57f-9a10-3a10-9c22-e208ecbe4493 | -6.43412 | -43.07458 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9663b5a-143b-3ca6-8bf0-8eed16a9f9c7 | -3.44622 | -50.2123 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0df60c3-822b-3bbd-a222-144ffc1156c7 | -3.92573 | -47.69625 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87a93dc7-60fa-3677-a4b6-8d1b7fff5b6f | -3.50022 | -50.45902 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d17351c-f5f9-3adb-9907-26773cc37bea | -6.47969 | -39.42183 | 2025-11-04 04:31:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 467d0d9b-2be4-31fb-b09b-3dcac0c17cd4 | -2.9824 | -48.04993 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb01bffc-84da-3bdd-87df-e4d501b4a868 | -3.89453 | -52.31754 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a35b35f-de7b-3bbf-b4d8-9ab261b18fe7 | -3.53731 | -49.44447 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ae25513-7149-3d95-826c-90de7fd51cfd | -3.43079 | -50.2395 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ad76325-f913-3dce-aabf-022e89e61af9 | -2.61201 | -46.91514 | 2025-11-04 04:31:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1164fc9-92e5-39fe-a2ba-ebed8e4487b5 | -4.96081 | -44.90885 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 305759b3-7462-37fc-ad68-69b30a2f7940 | -4.94417 | -48.56081 | 2025-11-04 04:31:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88285c59-05e2-3f49-9bd9-b9ba00451be0 | -7.61645 | -46.46866 | 2025-11-04 04:31:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1862c135-cf5e-3f9c-99f4-581ce35c7d0a | -2.02333 | -50.86297 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f1ddfcc-2525-3301-9def-01ce170102c2 | -5.61529 | -45.97536 | 2025-11-04 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ff44e801-d2a6-3d9d-a4e3-3fc84cf0d260 | -3.07056 | -47.7742 | 2025-11-04 04:31:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 03794036-e26b-32c0-b5c8-d69f207097f7 | -9.04029 | -47.00584 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 806f0f9e-99e1-3aa8-89cb-2baf89f9fb4c | -3.01353 | -48.04762 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61fe593a-8c69-3cbb-813b-bdf911af8606 | -4.40446 | -46.12066 | 2025-11-04 04:31:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 443ae413-318f-3fd9-a407-b1f6bf9b3dce | -3.34529 | -45.38181 | 2025-11-04 04:31:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c66d44f0-d678-37a9-866f-8282b46d4325 | -3.44129 | -50.22008 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a97d541-711e-3c51-8185-c897995dbb1c | -5.36254 | -44.74359 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9a2e71c-88ed-39b0-b923-8b0906a7a2b2 | -5.23115 | -44.20301 | 2025-11-04 04:31:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cf03b66-ec50-38c6-b95a-b1e4a1c6bad1 | -3.02305 | -51.39409 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1edf02f9-dd45-347c-b182-63a45a73dab5 | -2.97296 | -44.59454 | 2025-11-04 04:31:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb623aaf-939a-37ac-851b-b08d6f7bf48f | -7.23667 | -45.06598 | 2025-11-04 04:31:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef8757ba-2351-31dc-9f0e-19120c131c5a | -3.27943 | -50.76289 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a58b9dc-9822-3832-b4af-9560309d604d | -2.21188 | -51.0892 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b47adbf-b2e6-313d-b806-dd94a6774139 | -3.3867 | -50.28345 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1a3a80b-5767-3c21-a646-304776dbfc55 | -2.55867 | -48.94341 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 082d95ae-4739-39a3-b329-e7907fd82901 | -2.87602 | -45.292 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07c54d71-6155-39dc-af98-e64b4f0f3ae5 | -2.86867 | -45.29459 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88b04389-bfc8-351f-999b-d579a2760282 | -2.87263 | -45.29147 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdc9d4ae-de16-3b1f-82f3-adf67ab615b2 | -5.036 | -43.61969 | 2025-11-04 04:31:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6d35d236-ec1b-3f67-b2d7-1bd78af9db37 | -3.02384 | -51.38917 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3807c4c7-1912-3aef-8d3a-af748be81408 | -4.62783 | -49.46974 | 2025-11-04 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f130b043-013a-3e04-979f-01e182320a4b | -5.68134 | -46.36089 | 2025-11-04 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f15b9e9-0a41-3b37-bf62-ed0ba5ebfdf2 | -5.92204 | -41.32309 | 2025-11-04 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 07b9f0f4-cdef-343a-bd38-efdc1b578a26 | -6.84423 | -46.30009 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4d9c77e1-acf1-36ec-b2bb-1d991567a384 | -5.54129 | -47.23476 | 2025-11-04 04:31:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32b0d28e-a339-3602-96fe-58f34bf76989 | -4.2861 | -47.17797 | 2025-11-04 04:31:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 023eafac-0928-38e6-a432-a258007f29bd | -6.18565 | -46.74355 | 2025-11-04 04:31:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83301691-574b-3c84-b4ba-d3d3662c01e4 | -1.96419 | -52.11251 | 2025-11-04 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b03cf95-f24a-3274-9390-4be3364da462 | -3.54955 | -49.43468 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a623c545-982f-32e3-bcfd-ca4f214e563b | -1.76743 | -53.55346 | 2025-11-04 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 651d35ca-213e-359f-8173-67424f205ad7 | -7.07059 | -46.7535 | 2025-11-04 04:31:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00adb916-b949-3026-a38a-00f68c446745 | -4.02406 | -51.01299 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de7a3027-cecd-3d80-a1b6-172777eb9457 | -3.92628 | -47.6928 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a585fcd7-7ffb-3741-b682-2dcda1ed8ae8 | -4.47667 | -43.22906 | 2025-11-04 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2819855b-d3be-3b94-8170-50dd9bf4ff70 | -9.04646 | -47.01051 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7467d5da-9df8-336a-b3ee-48f136906a0e | -3.04247 | -50.34573 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3affd51f-c8e8-30d9-a999-36701d0facd9 | -7.55655 | -45.8514 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3811364-5611-3b9b-bf38-7dd79f5f8298 | -3.43504 | -50.23599 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4793d76-e82b-3599-a08a-86e0465ea02c | -2.73993 | -49.39417 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eeb41201-e70d-32f7-b9f4-b0d1d4a8d7ef | -2.8715 | -45.29875 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 896582e9-ec34-3cb7-b145-d360bf0a076c | -3.57141 | -50.64452 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| af38ab63-4141-30b5-be95-604a0edaf076 | -2.78968 | -48.61826 | 2025-11-04 04:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0754289-8d66-395e-8996-746a278195cd | -5.04684 | -45.93718 | 2025-11-04 04:31:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d93715c8-00ae-3fe0-a44a-549601991fa9 | -5.50775 | -45.3083 | 2025-11-04 04:31:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89b6ac3b-e8dd-3348-90eb-4bac1cc8dbc5 | -2.97772 | -49.15325 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b51f7ed6-38ab-379f-8642-bd63f6e1c380 | -1.76289 | -53.55267 | 2025-11-04 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ee8cf1f-6dbe-3125-a29c-71d5c553d13f | -4.94361 | -48.56435 | 2025-11-04 04:31:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c72ee9e7-e983-379d-acd5-e6be0c95ac27 | -4.69323 | -45.68309 | 2025-11-04 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ff1344c-80d2-36da-ae3a-750ac976c44b | -3.01533 | -51.3928 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e543d4cd-6fd3-38e5-8395-a1afe4a93c6f | -3.43292 | -51.51925 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26d067ab-4563-3d8d-bb27-38fc09fd38aa | -1.75835 | -53.55191 | 2025-11-04 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README21.md)
