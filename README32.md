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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc831c91-50cd-3b04-a9ea-966c406c22e8 | -3.04988 | -54.40108 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ed9c9b2-184d-3908-9efc-f5aaa614b288 | -8.07079 | -44.4536 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f45ca9a6-0aa6-3321-a898-72aa84a15fec | -4.10185 | -44.85601 | 2024-11-20 04:27:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7c205e3-a054-3086-98fb-62986e5b1511 | -4.08392 | -44.8171 | 2024-11-20 04:27:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2ecbabc-7f63-3a2d-9eab-6f25e879c36a | -2.91702 | -53.06648 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e648867b-1600-3235-8342-eca80984e501 | -3.51463 | -53.80271 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb0b0efd-5689-3dea-92d6-7725397456ab | -3.07297 | -49.20177 | 2024-11-20 04:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb01fc07-7586-3da4-ae3d-c2f19f094641 | -9.85801 | -44.35729 | 2024-11-20 04:27:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1b9b72d-e6c8-320d-bcc9-2b37a74987d3 | -11.24555 | -44.44365 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffc29653-e14f-3fad-a739-880ad39ddbb8 | -3.24779 | -48.44252 | 2024-11-20 04:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f2acf90-73bf-30b8-b481-8e0ea4b998b6 | -3.77837 | -46.66934 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b4900c34-6546-34bb-9e62-9fd8a26025b8 | -2.8579 | -49.13974 | 2024-11-20 04:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8eed0f6d-6cdd-3738-b5db-888239f9dabd | -10.03153 | -44.10982 | 2024-11-20 04:27:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e17a8b5-ca5c-34e9-992a-6b399c2c1b82 | -7.99948 | -44.37273 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1702f37f-e7e1-3019-b85c-7feb33be215c | -5.58199 | -46.31724 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bf707c4-9c7a-313a-9c0a-f5bae6d9fcca | -3.05405 | -54.40779 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e053e4c4-2e0b-3b2d-a519-248c0fe8dfdd | -5.60858 | -46.3637 | 2024-11-20 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30ecfc25-efce-323d-8a81-1ed45ba0daa4 | -6.80749 | -43.29718 | 2024-11-20 04:27:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e51dd91f-b065-3279-a17b-8d07a052fe40 | -3.09117 | -54.6693 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 984fc988-59b5-32d0-81f9-249f696190f3 | -6.63793 | -47.35006 | 2024-11-20 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| b66ae381-8477-32ac-bb24-03f2223b7777 | -6.24522 | -47.27348 | 2024-11-20 04:27:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7fb27818-95fa-3582-b5cd-e3a27f892965 | -3.79387 | -46.94015 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe4a5111-6e68-31c0-bcd4-4eeee6722ab6 | -3.00656 | -51.00907 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88c73738-6bcf-36b3-9e71-85a9df858b88 | -7.20512 | -45.87205 | 2024-11-20 04:27:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7c92491-7884-3bd1-88a1-60ef9908d050 | -4.18253 | -45.62795 | 2024-11-20 04:27:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab6fe916-2f61-3cc6-b708-a2f7976754b1 | -2.91276 | -53.07297 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d6fccc6b-c1d1-374a-a411-8f27af1ddb20 | -6.24577 | -47.26999 | 2024-11-20 04:27:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32f6b1c0-e568-3292-93bc-5ed099542567 | -2.93503 | -48.33501 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bf50dd36-7a89-3f87-aaee-df3ce1263b6c | -6.90734 | -39.5531 | 2024-11-20 04:27:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4539bcd6-c345-3509-a580-4635f14ad43e | -3.1068 | -53.74634 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 520dfef5-c698-3cbd-8d36-0aa4f94beac6 | -2.92214 | -53.0748 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 182185db-9cad-3735-8377-6f93d6513299 | -7.99919 | -44.38361 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c9ad4bb-b759-345c-a41b-0561846cfeb8 | -6.22362 | -47.28088 | 2024-11-20 04:27:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7da1655-5dff-30c9-8676-f6340355f6b7 | -3.80722 | -47.79945 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 35d855f4-cc0c-3410-af1a-b4fd4e562988 | -3.20193 | -54.32592 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 24adaf60-6b21-39a2-afcb-7a5dff71e554 | -2.92477 | -48.32622 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfd57981-35e5-3a77-b8eb-841d8e75be61 | -10.92729 | -44.88328 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 55b89ab5-8e1e-35af-be6f-e2834316f403 | -4.53914 | -43.29186 | 2024-11-20 04:27:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dda10dd7-89a7-30f2-8c25-80e1e1986930 | -5.72966 | -46.19896 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69971f99-4b5c-3b69-87ea-e92dd185ff08 | -4.70139 | -47.9608 | 2024-11-20 04:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98f8229d-fdac-30a7-8004-cbb849a637fe | -3.76369 | -45.08422 | 2024-11-20 04:27:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9488aa86-eac7-304e-b714-7043d9a5d61e | -3.95799 | -43.70116 | 2024-11-20 04:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebe0808b-03e4-3add-a849-b3e2b348fc32 | -2.91546 | -53.07628 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e891fe6-ac70-3293-ad4b-480806dbbfeb | -3.45944 | -53.30335 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f4d8d64-d177-3f29-aa31-b405c78f45be | -3.73075 | -47.37795 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb8c9dda-ac2b-3f1a-a461-db9ffc981a72 | -2.7453 | -51.82554 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 14aee9d0-ff39-3093-a98f-0d69c9883cbe | -10.42749 | -44.89191 | 2024-11-20 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bfabc9e-b862-32f1-8c04-54000579ad5a | -4.38324 | -47.77603 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9bce7583-e88f-3ef6-bcc2-04a70a2c714b | -2.92131 | -53.07974 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a199316-4c62-35fd-8083-b0d6553ca178 | -2.95911 | -51.41394 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74fe3530-4ff2-3ad0-b2b8-1a4610b65afb | -3.05922 | -54.40857 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ae34c78-8371-3797-98f2-6334f5499efc | -4.11472 | -43.5865 | 2024-11-20 04:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15fccbc6-883d-3019-a754-0b11b8b3d1d0 | -3.08694 | -54.66214 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3211d260-6893-3699-9459-ff14d63cd9a3 | -4.61197 | -46.66945 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfa37f09-434a-3e0d-986b-292846bb112e | -10.95258 | -44.41093 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11d3c40d-24e9-353b-b261-cebad06e579e | -3.24086 | -48.78174 | 2024-11-20 04:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba878e45-757e-31a1-938c-9bbfd08ab354 | -11.06272 | -41.62074 | 2024-11-20 04:27:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 2a6c05ba-1be2-3611-aaa7-5279192ef8ae | -9.17435 | -44.72841 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0ae8223-494c-3698-887f-95f117675ef8 | -2.97307 | -49.28877 | 2024-11-20 04:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0bda542-03b7-3579-8fd2-60c1fb3359b8 | -4.22226 | -47.2206 | 2024-11-20 04:27:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff207b1e-653e-3f66-ba6b-4148f5a8ff9d | -4.08251 | -49.28798 | 2024-11-20 04:27:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 502e774d-2e2d-3f7d-804c-321d88294e15 | -3.70469 | -43.4718 | 2024-11-20 04:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 913738b5-bb39-3a45-b511-5e817bace490 | -3.50271 | -51.67453 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf82af00-de17-3313-a930-06b40b4fcaf1 | -3.04937 | -54.40412 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c996c54e-eb11-3ce7-ba21-bcbf68244c89 | -3.18844 | -46.54877 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a87647d-5747-325d-95f7-3d42fc7d489a | -2.9037 | -53.05908 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ff014c1-ecca-32a6-a2b6-a074f3305e82 | -9.79423 | -44.71411 | 2024-11-20 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61f1d4a3-897f-3c33-9cc3-067ba59355c5 | -7.55272 | -45.26287 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebe467b2-5bae-38e5-96f9-db0ee8f7401f | -3.10277 | -53.74001 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f646fb0a-667f-33ff-bd83-6898883b9851 | -4.10971 | -51.05268 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7df372c4-34f7-3a76-b3a1-990e6f4580f1 | -4.99419 | -42.8116 | 2024-11-20 04:27:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0556733d-d0f2-3035-9465-5a73a7051603 | -8.0021 | -44.38805 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8d3c223-91ff-3785-ae24-83dc09465877 | -5.49372 | -46.20756 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a1d99e4-ec76-3529-b4a1-ce130ecff116 | -3.428 | -53.28726 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c32b2e09-008c-326c-92a3-1d9009f9404e | -3.88127 | -46.66449 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e8f9e81-34c3-3c49-9e47-fb3344322b9a | -4.66055 | -49.02288 | 2024-11-20 04:27:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bab66f1-a76e-3bac-82dc-8af5eaba7583 | -5.15124 | -44.12727 | 2024-11-20 04:27:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 548a6548-ea63-3a3b-9c5f-eef6187634fd | -2.59651 | -54.00643 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14c2c0ed-8b99-31e5-a6c3-7e136a57f7cc | -2.92767 | -48.33068 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 920ba2d1-665f-3cce-8a16-4b100d01db64 | -9.43546 | -39.02724 | 2024-11-20 04:27:00 | NOAA-21 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aff6cae4-32f0-3147-9dbf-c3100aa66088 | -3.0567 | -48.50277 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb71ba9a-a3cd-3be7-b8d9-b0afe2dff43e | -3.95098 | -46.69677 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0db3d9fc-7a58-3189-801f-592830573aaa | -4.15058 | -43.9755 | 2024-11-20 04:27:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c2b8793-4742-370b-bc70-17f0d37b73b0 | -4.35078 | -45.88026 | 2024-11-20 04:27:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3319b6f-d124-368e-9f87-feaa6befa920 | -6.93212 | -41.19834 | 2024-11-20 04:27:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| e0596e5e-0ef2-3887-a5f4-28608f22387e | -9.1929 | -44.72335 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 039e1200-3947-3ea1-b987-71a1ab506720 | -4.44409 | -46.5895 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3d0ee03d-1156-3114-8657-181d825b78a7 | -2.60181 | -51.79539 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3de9735-796a-3dc5-a5fa-122060f23183 | -2.46827 | -54.75166 | 2024-11-20 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee8a0632-ae1b-3fb8-96a4-52a0c5d0958f | -3.18512 | -46.54826 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ff68979-8fc9-3ba4-8afb-6d6c00fa5429 | -2.58601 | -51.71675 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a689e40-f1e9-3047-86fc-207810657566 | -4.41522 | -42.13998 | 2024-11-20 04:27:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e88f4e1-87a4-3582-82db-44e29724aa08 | -3.66844 | -54.27336 | 2024-11-20 04:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9d3d7d5-421f-35cb-961d-a597dd9caa73 | -10.42151 | -44.48568 | 2024-11-20 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e525207-b966-3008-9e7d-4b0c411042a7 | -3.31849 | -54.08768 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a22d389a-624c-375d-822d-8babf2045258 | -3.81515 | -51.35323 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| eee1eb3e-d6b2-34ab-b757-4b0803e77547 | -3.43655 | -44.98007 | 2024-11-20 04:27:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f111b72c-7512-3980-afed-7ad3760390ce | -2.94546 | -54.80244 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d9ce185-284f-37f4-ba4c-ea28acd499e5 | -8.00268 | -44.38415 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcbc5b12-1748-37c5-b13d-9f539ac110b7 | -1.83604 | -55.04528 | 2024-11-20 04:27:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README33.md)
