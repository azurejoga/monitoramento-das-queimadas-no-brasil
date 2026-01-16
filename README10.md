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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df07f581-d93c-3aa8-b07b-22ff7efea0b9 | -1.80081 | -53.80039 | 2026-01-16 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 392df4c6-18a1-374a-b3e8-bdb56e488db3 | 2.76219 | -60.32358 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84df1d27-8ff3-3f8c-90b5-cc69cdc6c4d7 | 3.00042 | -60.23963 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0001f88-a3b5-3457-b433-a69708b6260c | 3.0608 | -60.10242 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57ad8a1f-e2aa-39ca-82ba-3ff7bf7c53e7 | 2.76692 | -60.33381 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e1a06c59-df72-3a42-92f2-4e6e52c0702c | -1.94003 | -53.47614 | 2026-01-16 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6426ebd1-240b-324b-8add-09ecf655b791 | 3.06103 | -60.10358 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f247887b-87f4-3d63-9a4b-246bb1099eb1 | 3.2001 | -60.4516 | 2026-01-16 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6af85143-906b-384d-a1b5-7be80b7708fb | -1.82986 | -53.44118 | 2026-01-16 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48e7bd56-87be-3e46-82b2-9a2d9780c3a9 | 2.69599 | -60.07063 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65600b31-6448-3a40-aada-3bf4a110ebee | -5.38243 | -43.19873 | 2026-01-16 05:03:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2619b04-cb37-3ab5-b7b8-9da4602e06ad | 2.75173 | -60.22739 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f47e9860-e570-394f-b881-438e960268e8 | 2.70278 | -60.05678 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 397c027c-1243-32c0-a88f-701bc876a0bd | 2.20948 | -60.15171 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94269ef2-6134-3bd3-a578-7ddb88442d0a | 3.06454 | -60.09752 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4888bf8-f6fe-3980-87c9-49ec97b5331a | 2.76082 | -60.3148 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13616d41-1902-3411-b259-2f56b0b01a98 | -0.08781 | -51.27782 | 2026-01-16 05:03:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7241cbfd-d009-3d3a-9a83-0128549ca6f1 | -1.80084 | -53.86522 | 2026-01-16 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22d3d213-5b59-3305-9bb1-bbbab8cc2599 | 2.75774 | -60.32425 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 136122f0-d785-3e35-a612-74640355d9b7 | -4.21662 | -48.4673 | 2026-01-16 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9e440fa-a83a-3eb0-b1e3-1d1498256f4f | 3.0652 | -60.10176 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd352f6c-9c3c-3565-9f0c-387e1537527c | 2.7524 | -60.23166 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 033f15dd-6db6-31ce-b55b-5ed146666d8a | -1.16701 | -53.72741 | 2026-01-16 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e7a01715-24a4-3547-a1d6-cca981697c9e | -5.37417 | -43.19451 | 2026-01-16 05:03:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a74759d-adcd-366a-a7e7-3dda4e184ee9 | 2.7615 | -60.3192 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7038b52-5c3b-3b82-ac71-11a47a5451a4 | -3.91221 | -54.21683 | 2026-01-16 05:03:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf6947a2-d96d-370a-a401-018a64b30db0 | -1.92435 | -53.90201 | 2026-01-16 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be274fbe-79b0-3706-85fd-8dab1bc55f7d | -5.38081 | -43.19538 | 2026-01-16 05:03:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7915dfd-2797-382c-9c00-c857a23244ac | 2.76052 | -60.32132 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3b265f4a-e47f-347d-ae81-42918ae5dd9d | -4.21593 | -48.47191 | 2026-01-16 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3ef3520-8aeb-34fe-93ed-db4ff301bdc3 | -5.38005 | -43.20092 | 2026-01-16 05:03:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b60f709-5519-3f51-b3bf-bb32f11edcfa | 2.76627 | -60.32941 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 23fe70c3-2f0d-3bc2-9471-e0f40a039ee8 | 3.0648 | -60.09867 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a39e360-a479-338b-be28-2a16ed6c557c | -2.96158 | -54.34268 | 2026-01-16 05:03:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29348f2d-d7e2-3547-8fdf-6c89f99f013e | -1.80418 | -53.86573 | 2026-01-16 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d077195-1679-3bc8-b464-9275e16ebe01 | 2.75987 | -60.31692 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 98d11d49-eee9-3e96-b792-434e1c572935 | 2.69842 | -60.05746 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd0fe5cb-c323-389a-9e95-3ae7d5951cfd | -5.37577 | -43.19799 | 2026-01-16 05:03:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61639cee-61b1-3010-8479-eb35b3a07cd8 | -2.96212 | -54.33921 | 2026-01-16 05:03:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 983fbbb3-5f31-381d-8317-14ae73d7d92f | 2.75144 | -60.22924 | 2026-01-16 05:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9039f20-8c85-3f98-8cd8-f970acce82a8 | -11.95503 | -44.20953 | 2026-01-16 05:05:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5c99293-124a-39d0-bb2b-0ba9bf5552b5 | -12.65193 | -46.75712 | 2026-01-16 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ba52dd00-49a3-3291-a5dd-b7103e0d5a4e | -7.22174 | -43.05981 | 2026-01-16 05:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d272948a-06af-3d8e-b1da-fb21aafd4b8a | -12.6626 | -46.76712 | 2026-01-16 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a10063d-c635-3c44-899b-31a3514a1a0f | -12.65143 | -46.76138 | 2026-01-16 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3308c9b1-82df-375c-b709-b2dd6abe363d | -12.64651 | -46.7582 | 2026-01-16 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7b3d77ad-04b3-3d1c-ba56-80600f43cbcd | -9.54698 | -63.53179 | 2026-01-16 05:05:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5ea0373-0e09-3c83-a757-85b39340fc09 | -12.65678 | -46.76632 | 2026-01-16 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a091ffaf-4677-319f-b2fd-5a90d1123d6e | -7.23541 | -43.06175 | 2026-01-16 05:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 4e0936d9-ef74-3920-bf4e-9b4acb03744a | -12.65288 | -46.7546 | 2026-01-16 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4c3cd3a3-3733-3366-b905-9f330d02b515 | -7.2294 | -43.05444 | 2026-01-16 05:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| bb0aa984-c308-3e5f-bc6f-aa1941d97f24 | -12.65242 | -46.75283 | 2026-01-16 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 90c33b83-7b93-3450-b53a-7443a38066a9 | -12.08262 | -45.29454 | 2026-01-16 05:05:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b01ab1d4-d76d-391e-b144-5f48ae9a29c3 | -12.65235 | -46.75888 | 2026-01-16 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2bf5a697-5fa4-3be4-8c87-56a1873111ee | -12.08564 | -45.29232 | 2026-01-16 05:05:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d3ca1d7-58bf-3c92-a8e5-1d15f538f6ab | -12.64608 | -46.75644 | 2026-01-16 05:05:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7dc78831-3d95-3cc0-a76a-9766a1fd425c | -12.08656 | -43.76985 | 2026-01-16 05:05:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 98fdc65e-d59a-3fdd-970f-6432302e0a91 | -7.22856 | -43.06085 | 2026-01-16 05:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ce9abc8f-1063-3df6-affe-0c3ca8ec1afd | -12.08622 | -45.28721 | 2026-01-16 05:05:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be05b88b-f84e-352d-8d7e-8fadf7db21a7 | -12.08324 | -45.2894 | 2026-01-16 05:05:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d5283ba5-c11d-3b1b-9e73-e07aa73c6172 | -13.69206 | -55.67602 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| da7595fc-e64e-3afc-999c-dfc9f28fd52a | -13.69639 | -52.60208 | 2026-01-16 05:08:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfb31626-d809-32ab-865b-03aecb0ef3d0 | -15.11341 | -52.94748 | 2026-01-16 05:08:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 690da6a0-bb30-38ae-b555-ed855070794b | -15.1174 | -52.94811 | 2026-01-16 05:08:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78cda8f8-8e3e-355f-9db7-832b0c5be40f | -13.69264 | -55.67221 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0f541978-5ed0-395d-af92-14f904e91d4c | -15.11281 | -52.95191 | 2026-01-16 05:08:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b870dc9-817d-3d13-a1e5-bec1add19a12 | -15.62077 | -56.1539 | 2026-01-16 05:08:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 892d0cfd-f14b-3629-a744-7448c8588c7e | -18.81386 | -51.60433 | 2026-01-16 05:08:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90cd5e10-60a0-30cb-a50f-9bdad94f03be | -12.29267 | -57.39153 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f1acce9-1573-358b-8984-4b32d60763f6 | -16.24013 | -58.92034 | 2026-01-16 05:08:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 69e5b591-3b76-3968-9b31-5d70b59c9893 | -16.10414 | -56.75319 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b918f50-84b2-3ffd-b3e8-5b4871224fa4 | -12.9201 | -49.48881 | 2026-01-16 05:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f72d4975-e616-38a1-8c3a-d9135fce8758 | -15.96945 | -56.2772 | 2026-01-16 05:08:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ad502abd-5412-30e3-91f3-f5b87485c137 | -15.43947 | -56.33585 | 2026-01-16 05:08:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e7ab225-4801-3afc-9e69-76403b7511d5 | -16.25983 | -56.88414 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3880aa37-d86d-3336-838e-0233a4757041 | -17.60959 | -46.66042 | 2026-01-16 05:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1356820c-0a17-302a-b895-43c1f46e4b06 | -13.68806 | -55.67928 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b746b81-4fb2-38aa-ad28-f836ce68a92b | -13.69091 | -55.68362 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 43a90974-f7fe-3655-bd5c-c33577dca646 | -17.61731 | -46.66122 | 2026-01-16 05:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96c3d141-72e8-3325-ac10-f0c2435974db | -13.69948 | -55.6733 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a02b4339-62f4-30b4-b5ae-e4ea1ee492b6 | -16.11089 | -56.75426 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| df7d917b-f13b-3b2a-a614-2f9e2bf1fda1 | -15.11608 | -52.95786 | 2026-01-16 05:08:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2621e207-69d1-3235-9e8f-94fb4ff08a48 | -16.2632 | -56.88469 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| caa40798-0532-3c25-a0df-f6097617e67e | -16.11146 | -56.75055 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7ec5ac8a-a6b0-3869-9cc9-55f36db65a2d | -13.69238 | -52.60152 | 2026-01-16 05:08:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5061400-1089-3881-ade4-6f189d233bd1 | -15.43664 | -56.33154 | 2026-01-16 05:08:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b50ce6c8-b4b5-321b-9b2a-be0d9fa46b42 | -15.43041 | -56.32669 | 2026-01-16 05:08:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b3c1722-7bd7-3058-9190-5035be8153ad | -15.11209 | -52.95726 | 2026-01-16 05:08:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3c8375d-2ffa-3b64-b501-d99bc46bd9e3 | -18.81844 | -51.60506 | 2026-01-16 05:08:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b1cd3f1-6451-38be-9149-6fc0d296dd31 | -15.43324 | -56.33101 | 2026-01-16 05:08:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 277b4bf0-f9ae-3e8f-83d2-7cf86e583d76 | -15.59002 | -57.34214 | 2026-01-16 05:08:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd94c7e5-9644-3155-9ad8-9c075d015fb5 | -18.82586 | -51.62119 | 2026-01-16 05:08:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fcee02f7-23fb-39fc-ad0a-d2557f5b3a30 | -16.10695 | -56.75744 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44ca818b-6565-3136-8128-9ef0f56727fe | -16.10302 | -56.76061 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efd100e5-5690-33bb-9672-309f8292ba6b | -13.69548 | -55.67656 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d5b0bb5b-f352-352e-9b02-2dbe4c538269 | -13.68864 | -55.67548 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fa6c871-8e86-38a9-9501-43d6588c7670 | -16.10077 | -56.75265 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 234c69d2-6486-38dd-a77d-45e0a1fac4a4 | -16.09964 | -56.76007 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00ff6f4d-1516-344f-a697-4125e281f48f | -16.1002 | -56.75636 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44dff328-e14d-35bc-8fa1-84e79eb48119 | -19.34231 | -54.17856 | 2026-01-16 05:08:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README11.md)
