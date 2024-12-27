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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 604d9722-fb0d-30c6-b257-5f8299059b68 | -5.21083 | -44.90655 | 2024-12-27 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0f3f912-726f-3096-915b-0ee9f026eb8d | -6.42452 | -39.75398 | 2024-12-27 03:40:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a9bd4828-6630-348a-a72e-a20d0ed4dc86 | -4.42017 | -46.56342 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 547da642-7f86-341d-b1d2-2efc9b1720bf | -4.0332 | -46.1762 | 2024-12-27 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22a683ef-c072-3dc4-afaf-f6849c3e5c38 | -5.22161 | -41.2401 | 2024-12-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6af2dcef-ca8a-3923-bc11-5f2053869556 | -3.19 | -45.99297 | 2024-12-27 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89f3b9e3-e049-3bb9-9cc6-d8c69c31218c | -4.42737 | -46.57109 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9d6b4a00-f6e5-32b6-b75b-1e3dfbfd170a | -4.43285 | -46.56585 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c87cd7d3-344b-34c7-9508-c2560be10711 | -4.55811 | -44.12889 | 2024-12-27 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d181b494-1bbf-3942-ad7c-e716404210ab | -7.90386 | -35.20355 | 2024-12-27 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| ae2ce65e-bf75-3f9a-960d-11cfe9d61a47 | -7.42883 | -35.05035 | 2024-12-27 03:40:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b1b1ffb1-4237-3381-b8c6-dc8f28cc380d | -6.90537 | -39.59048 | 2024-12-27 03:40:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f69c5621-1eb1-30bc-ade7-423e3b1a4c6c | -3.41569 | -44.90411 | 2024-12-27 03:40:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4f9133bd-0790-3d10-875f-fe98681d0404 | -5.37292 | -44.84478 | 2024-12-27 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9e61712-266a-32f2-afc8-4f5fabdad7f2 | -5.2248 | -44.72604 | 2024-12-27 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2cb64436-39fa-338f-820d-8ce913ea7580 | -9.8126 | -35.93607 | 2024-12-27 03:40:00 | NOAA-20 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b38e2243-6243-3e6f-8505-8bef8cbd5a75 | -4.52629 | -42.06998 | 2024-12-27 03:40:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 32996da5-630f-3663-9bb9-43f4ffbca1fb | -3.06326 | -40.08225 | 2024-12-27 03:40:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 5ef2a19c-67bb-388b-bbcc-3a1e75665516 | -10.1277 | -36.4561 | 2024-12-27 03:40:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba81017d-0f98-3572-9fa8-6925eb9dbb88 | -7.75467 | -35.13791 | 2024-12-27 03:40:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ceb341ef-a755-3be9-bf1f-58fb3511e6a5 | -10.38784 | -36.9145 | 2024-12-27 03:40:00 | NOAA-20 | SÃO FRANCISCO | SERGIPE | Brasil | 2806909 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2dd68ac7-80fd-37ef-be40-89e8a1ad1c2e | -3.69855 | -43.42297 | 2024-12-27 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d588b35b-82fc-3b9f-ab83-809e1b7320e8 | -4.55087 | -44.13841 | 2024-12-27 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f0117ac-72cf-32b9-9967-d60ca5a44748 | -3.03564 | -40.11803 | 2024-12-27 03:40:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 6093e717-3c70-324b-94af-1bcefea00791 | -4.36893 | -44.00924 | 2024-12-27 03:40:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2da215a-6c1e-3244-b179-ee26143207d3 | -6.58842 | -34.99613 | 2024-12-27 03:40:00 | NOAA-20 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 380d8c8a-9319-3afd-98d8-87dbf6965e15 | -5.64096 | -43.72358 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 46df533a-6480-3c12-bf60-b11f268e6310 | -4.51516 | -42.07848 | 2024-12-27 03:40:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 30f0617d-187d-3e1e-be45-0c7edc3485d3 | -3.06339 | -47.76984 | 2024-12-27 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| baf4d0ea-0aca-370a-97a1-3dbb1fb44c11 | -2.25492 | -46.39551 | 2024-12-27 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7bd8efa-37a5-377f-af1e-13780687656f | -3.03584 | -40.11857 | 2024-12-27 03:40:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| aa77e754-caa4-373d-b3ea-7971a58be31f | -7.37655 | -34.88546 | 2024-12-27 03:40:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a0c2d380-89d2-3cd9-8e2e-98167195e5cd | -3.18593 | -46.13152 | 2024-12-27 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3792f77b-1f62-3c7b-b6a7-9215a65eae85 | -8.66534 | -35.71658 | 2024-12-27 03:40:00 | NOAA-20 | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0646d0e1-bc80-3cd7-80cb-0d1ecebb7b0f | -5.3696 | -44.84525 | 2024-12-27 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9307a7e-f8ec-3ead-90fe-36ab030186e6 | -9.08872 | -37.1072 | 2024-12-27 03:40:00 | NOAA-20 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e477d8c7-f738-392d-87d5-90e7252162cd | -5.22241 | -41.23814 | 2024-12-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 443d13b8-0010-3560-a25f-82b498ca59c2 | -4.30201 | -42.33087 | 2024-12-27 03:40:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 249cc6e0-4712-33cc-a3c2-9a78ff875929 | -3.55482 | -40.85028 | 2024-12-27 03:40:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72d0d709-eeb6-3e80-8271-de4b1662f509 | -6.90153 | -39.58973 | 2024-12-27 03:40:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb7b66be-0863-33c4-8e4a-d10591c8fd38 | -4.39491 | -37.84632 | 2024-12-27 03:40:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3ab1247f-a12e-3a72-ac58-078d7ad43d32 | -9.30585 | -36.02623 | 2024-12-27 03:40:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0d3f2e36-93c3-3035-bd8b-ed44dd1ec75e | -5.13693 | -43.24185 | 2024-12-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ee3faf3-cefb-33fd-b3e8-4457196aaac5 | -7.90717 | -35.20407 | 2024-12-27 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| af0f05ac-f52c-35ea-b1a8-3f15a36a22d3 | -4.71477 | -44.46764 | 2024-12-27 03:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e2c744d-3dfe-396e-a12f-0217ac5f23dc | -4.51433 | -42.08352 | 2024-12-27 03:40:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 16b9e0fc-982f-3616-8d05-966ba6de3ed4 | -3.99002 | -43.25816 | 2024-12-27 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 725eda9d-16b2-3668-a5e9-24c897417c00 | -9.41914 | -35.99765 | 2024-12-27 03:40:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 8bc7a55e-e084-36c7-9fd9-bb45cb889f53 | -2.27886 | -45.57721 | 2024-12-27 03:40:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09cad5b9-dec4-3d01-9ec8-5d4922045ff4 | -2.254 | -46.401 | 2024-12-27 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce4fb6fe-70bf-30fe-a15a-bcca562954a5 | -5.3619 | -39.34887 | 2024-12-27 03:40:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0208335a-0b9d-376d-b3a8-750adb386b2e | -5.35802 | -39.34822 | 2024-12-27 03:40:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 579c1188-4b19-37cf-b88a-23b08746d1b5 | -5.60683 | -38.99269 | 2024-12-27 03:40:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 421f276d-a13e-3fda-b0a8-71be74b64ed7 | -7.90331 | -35.20702 | 2024-12-27 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 71368bb3-5669-3ca7-bdff-cfd2b942e1f5 | -4.42191 | -46.56493 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c209cf3e-7fd8-3fd1-8460-cd4b0cb26073 | -2.27807 | -45.58199 | 2024-12-27 03:40:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71412fd4-9ea0-34ba-85e2-c6984e1ab204 | -4.4265 | -46.56472 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 271565aa-c6f7-345a-bd1c-2630ffa6c5bc | -10.52681 | -36.95562 | 2024-12-27 03:40:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5acf7231-8c10-37ae-8ebc-5dd5ce038c29 | -7.0291 | -35.3246 | 2024-12-27 03:40:00 | NOAA-20 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 34b1a224-2ec9-3ec2-8fa5-9958157f6c6d | -5.63685 | -43.71638 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc0dba1b-a8a6-322e-9930-51bf0b69e471 | -3.55896 | -40.84964 | 2024-12-27 03:40:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 47db1a9c-211c-3c9b-9b04-cd035448cff2 | -5.92876 | -43.77636 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0547abaa-5c97-37ac-a954-adbc9f328d80 | -5.38807 | -40.67538 | 2024-12-27 03:40:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 30a9b04c-1869-3c60-b0a1-1f39a316e667 | -4.1645 | -42.0327 | 2024-12-27 03:40:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e0170290-c8c8-391e-be44-43848e011df9 | -4.30137 | -42.32677 | 2024-12-27 03:40:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a3ee0b68-101a-35b3-8aed-3b32113e0980 | -4.37373 | -44.01372 | 2024-12-27 03:40:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58eff2af-2186-3c5c-b133-616b549eafc5 | -4.52073 | -42.07424 | 2024-12-27 03:40:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2d49dc3f-be04-3326-b333-a87cf340ff28 | -7.90336 | -35.22838 | 2024-12-27 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6906eb85-03d2-31d5-b07c-c33a793543e9 | -4.24587 | -41.92196 | 2024-12-27 03:40:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 01ad7f40-d3b8-31d2-971b-50ba377ef42f | -5.39231 | -40.67609 | 2024-12-27 03:40:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a6717f26-81e0-37af-99ad-f13ae25b420c | -3.22698 | -45.96421 | 2024-12-27 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78ef7fcb-d3a7-3450-a9f0-ba9795fe6d55 | -8.77593 | -41.26429 | 2024-12-27 03:40:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b193fd1-0545-348f-8ddc-d93f84a78a66 | -5.21728 | -41.24176 | 2024-12-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 946586ff-1d1b-3b1c-94d9-51415ebb576d | -5.1319 | -43.2408 | 2024-12-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a289257b-7a94-3c1f-b80b-0e725df0ce30 | -3.22896 | -45.97622 | 2024-12-27 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b38e8147-182c-3529-96b3-0f4eb6fbb3cc | -3.4106 | -44.89899 | 2024-12-27 03:40:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2034f3e1-05bd-3bb9-8a83-5f0fdd0a9ecf | -5.21001 | -41.25834 | 2024-12-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4190d66c-a6bb-31f0-9122-c51ca0295325 | -9.41306 | -35.9931 | 2024-12-27 03:40:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a9c498a0-516e-3410-b4bd-384f338bcd5b | -8.63461 | -35.95409 | 2024-12-27 03:40:00 | NOAA-20 | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dd6a41ae-e78e-3121-be31-e68e9abf2bde | -8.06983 | -35.14098 | 2024-12-27 03:40:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| beea2df4-36f0-3fe6-b8aa-06ee10fb92a3 | -5.12631 | -43.24289 | 2024-12-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c7755b5a-fbad-38ae-96ba-c97be4421cc6 | -7.35108 | -39.83942 | 2024-12-27 03:40:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6c111d59-7bdd-3222-b73f-45119f717230 | -4.4193 | -46.5685 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 290db246-40c6-36da-b339-f42decc6c0bd | -6.02742 | -39.76925 | 2024-12-27 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 84022dd9-5f9a-3be4-aacf-242d462946d5 | -10.53014 | -36.95617 | 2024-12-27 03:40:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d141925f-9a32-3b23-bfc1-208276071659 | -5.24428 | -41.40173 | 2024-12-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bc279faa-1f3e-3ae4-a210-7e0fd5eeb00f | -5.23987 | -41.40068 | 2024-12-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0a19423a-14a9-3a3b-9e14-c7932328e93c | -9.33343 | -35.98061 | 2024-12-27 03:40:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8ff27626-070b-3629-a0a3-aabb0bac3fd9 | -10.14963 | -42.44284 | 2024-12-27 03:40:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d89b59c-13bd-3e3d-932d-ab8fa4bdd8f9 | -5.65353 | -43.71256 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ddde9e0-7f41-3e15-aad8-8a2f4f4d2be5 | -4.42736 | -46.5597 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 503fd9c5-453a-3df7-9435-386035e8236f | -3.23242 | -45.97003 | 2024-12-27 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc438d79-2fe6-3310-9b30-2f6f7238c0f6 | -3.00205 | -48.05592 | 2024-12-27 03:40:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 69d95b54-4afe-3ae4-9d98-82da1d2310a8 | -5.21216 | -41.24533 | 2024-12-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fd9b0c58-b469-3d94-9b62-a034e11885be | -3.41088 | -44.90068 | 2024-12-27 03:40:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3813a9b2-6dd2-36f1-bf4b-c9b328a9bce4 | -3.55925 | -40.85091 | 2024-12-27 03:40:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ce2ad20-a908-3457-a6ff-206c174fa80d | -3.17961 | -46.13048 | 2024-12-27 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84da53af-013a-3377-b42a-9aebc2aee06a | -2.28424 | -45.58308 | 2024-12-27 03:40:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbea19f9-1317-39ca-b481-3a63b9671a07 | -2.99869 | -48.05698 | 2024-12-27 03:40:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8dfe375d-99c6-357a-9fc7-658b9e08bdef | -3.06748 | -40.08293 | 2024-12-27 03:40:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README6.md)
