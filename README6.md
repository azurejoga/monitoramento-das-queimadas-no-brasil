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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed368570-5980-398f-85dd-a7bca7cf886e | -3.1792 | -48.612999 | 2025-11-19 00:35:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9bf01c5-6492-37b2-bed0-576f78d196d4 | -13.4288 | -48.231899 | 2025-11-19 00:35:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f89baf69-1b44-3163-bb11-c13643c83032 | -11.7888 | -44.636902 | 2025-11-19 00:35:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3738e380-e476-30ae-aefc-fbaebe748b77 | -12.404 | -43.149899 | 2025-11-19 00:35:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0dd5b9eb-b366-32fa-abc0-17dc4849d992 | -11.6703 | -47.9753 | 2025-11-19 00:35:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04715a99-c9c9-3ac6-b2cc-4c721a545f76 | 3.65008 | -51.30052 | 2025-11-19 00:37:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 41.4 |
| eb8b0f99-017e-39d9-9b01-7454240a19de | 3.64112 | -51.29927 | 2025-11-19 00:37:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 83303ab4-717e-35cc-94dd-a99431785b16 | 3.64237 | -51.29018 | 2025-11-19 00:37:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ea660bb5-7708-3f8a-9def-b5a2c04f0c40 | 2.79124 | -51.38281 | 2025-11-19 00:37:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 70287820-cf39-374a-910f-d5b46109cb92 | 3.6603 | -51.29268 | 2025-11-19 00:37:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 235b70c5-efa6-3f19-9794-abb8aa83bb11 | 3.65134 | -51.29144 | 2025-11-19 00:37:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d881d9ca-cc7e-3e17-9ecd-2468abb21c8d | -10.3538 | -48.8957 | 2025-11-19 01:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f1feff79-138c-34d8-99f0-52e1f82fd881 | -21.4275 | -47.6869 | 2025-11-19 01:20:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d2421513-9627-3cce-bad9-56682e3f9869 | -4.6878 | -43.2015 | 2025-11-19 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b8a9685d-c280-32d1-97eb-83d67cc14637 | -4.6876 | -43.2248 | 2025-11-19 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| de8a2ee1-cc22-34b7-bcdf-46b7f6683f65 | -3.5654 | -43.4727 | 2025-11-19 01:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 6c4a9c3c-fd3e-3de6-876a-861f2374bc82 | -6.1138 | -42.9569 | 2025-11-19 01:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 1f1010ae-c211-3f01-bfbf-8ee93166b397 | -6.114 | -42.9334 | 2025-11-19 01:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 7457a753-5f65-3975-8d90-4a3ec91d43bd | -3.2024 | -45.2256 | 2025-11-19 01:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 6b6b2bc4-ef91-3a16-94d6-9a8da8fef604 | -4.6689 | -43.226 | 2025-11-19 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 180.9 |
| fcb32db0-6d6b-3a4d-ac9c-c6615b7b729f | -5.0399 | -43.6205 | 2025-11-19 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 996b7fd3-85c8-315a-b16c-5d3d596594b3 | -11.8117 | -44.621 | 2025-11-19 01:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 4e1e6a63-1725-3a78-a7c6-855bf5b8a8de | -6.1326 | -42.9554 | 2025-11-19 01:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 6fdfc734-3fa2-388f-9454-a87c35836228 | -5.0401 | -43.5973 | 2025-11-19 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| ae73936b-9421-3d06-9b83-a1d2c75a42ee | -2.8474 | -45.6431 | 2025-11-19 01:20:00 | GOES-19 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 46a2cfcb-eb07-320b-94fa-f01e3884ef8c | -3.2211 | -45.2024 | 2025-11-19 01:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ee3c3df7-3dfa-3553-a1aa-f91925e87397 | -4.9937 | -44.7491 | 2025-11-19 01:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6d499f43-4e68-306f-812a-ea11f2f7076d | -11.7925 | -44.6239 | 2025-11-19 01:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 6fbcc7b6-25b5-34d5-a033-eb5f48ef7e28 | -3.2025 | -45.2031 | 2025-11-19 01:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ec6751d3-ac03-3add-b9e1-884637cc9eb0 | -2.8476 | -45.5983 | 2025-11-19 01:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 1e3630a1-fc91-3d4f-a2f9-13117d5b7cdb | -2.8475 | -45.6207 | 2025-11-19 01:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 265.4 |
| a4a28ad8-dc41-35bf-986b-5defbe5f0fe2 | -4.6691 | -43.2026 | 2025-11-19 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 04f5f591-352d-3822-864d-515d16f73358 | -6.1136 | -42.9804 | 2025-11-19 01:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 991fffc0-b430-3582-81da-a6b2a68629eb | -2.8661 | -45.6201 | 2025-11-19 01:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 615638d7-a4f2-379c-bf4c-1c53a4bb8253 | -3.221 | -45.2249 | 2025-11-19 01:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 729cac29-f50a-334a-924e-4eeaba67b8b9 | -5.0588 | -43.5961 | 2025-11-19 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 0aaa62e8-1c4f-3a2d-835e-40bfc645785a | -5.0214 | -43.5986 | 2025-11-19 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| bf46c681-3de1-3430-ac0a-ad6b88dd7209 | -6.2039 | -39.41034 | 2025-11-19 03:10:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 54e03107-5038-3f52-87a2-a17887754c3d | -7.85561 | -39.8165 | 2025-11-19 03:10:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5c549ab4-e961-3def-9b31-ed3b3ff7401f | -6.69043 | -38.06748 | 2025-11-19 03:10:00 | NOAA-20 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0640e4cd-7244-3c86-9034-12b162ac9ce7 | -6.21447 | -39.60868 | 2025-11-19 03:10:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 39883132-01bd-3e24-bf30-c7b06faa255f | -6.20566 | -39.40507 | 2025-11-19 03:10:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2a7227f2-d2cc-3148-af2f-6c7efc34517b | -6.2209 | -39.61027 | 2025-11-19 03:10:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fffac427-1c2b-3eed-8a5e-06a5cf666953 | -5.42219 | -40.6605 | 2025-11-19 03:10:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| de3b6bba-afcb-31ea-9f17-25ba36221385 | -6.1985 | -39.4034 | 2025-11-19 03:10:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| cc470ba3-42a5-36f8-b679-ad1d4538525a | -5.42096 | -40.66723 | 2025-11-19 03:10:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4f226dc8-95da-3b77-b1f0-679b0b88276a | -7.85602 | -39.81939 | 2025-11-19 03:10:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 390de91d-80fd-3a19-954b-bb7c452e2f17 | -6.52517 | -35.26705 | 2025-11-19 03:10:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8fe15535-3774-316e-b713-6270be3d967c | -5.13993 | -35.70307 | 2025-11-19 03:10:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0b74e55b-beb2-30e5-972d-f9cce44879ea | -6.2049 | -39.40479 | 2025-11-19 03:10:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9a4fc146-15b1-3acc-bc7a-55578d1ad32f | -6.21498 | -39.60915 | 2025-11-19 03:10:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 07142215-ac44-3b68-97b2-41bd363c5e2a | -9.91557 | -36.25592 | 2025-11-19 03:12:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| df5577a3-34a2-33ae-be66-9aa62983a33f | -9.92443 | -36.26348 | 2025-11-19 03:12:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d9ddc321-9efb-3aa5-9514-a7faed6880bd | -9.91949 | -36.26253 | 2025-11-19 03:12:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 12867123-17c5-32de-be11-afe29b1089c2 | -9.76038 | -36.05514 | 2025-11-19 03:12:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 35a1a02c-a1ef-3c9a-8193-8f52f3f3a2f5 | -9.91655 | -36.25574 | 2025-11-19 03:12:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| a423b50a-3168-3105-892c-7958e58de369 | -9.9205 | -36.25687 | 2025-11-19 03:12:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 85c245a8-0d49-3d49-9dfd-aa32487d8ead | -10.80092 | -36.934 | 2025-11-19 03:12:00 | NOAA-20 | BARRA DOS COQUEIROS | SERGIPE | Brasil | 2800605 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8c7de020-a584-35ba-86e4-a9162d65376d | -9.46191 | -42.22844 | 2025-11-19 03:12:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 00857b25-ef16-3be2-80a6-a63e9bf0bc0b | -9.75731 | -36.05579 | 2025-11-19 03:12:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 047376cd-0db1-3953-856c-6d0515664e49 | -11.35156 | -37.42862 | 2025-11-19 03:12:00 | NOAA-20 | SANTA LUZIA DO ITANHY | SERGIPE | Brasil | 2806305 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 03a70d4f-87ce-3181-aed0-b027f86e4826 | -9.92148 | -36.25668 | 2025-11-19 03:12:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 1b4cf9e3-d8fa-3ce8-9aea-cd968e583645 | -11.34637 | -37.42751 | 2025-11-19 03:12:00 | NOAA-20 | SANTA LUZIA DO ITANHY | SERGIPE | Brasil | 2806305 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9a9bf2cc-9ba3-3732-a203-bf333d51a77c | -9.92043 | -36.26232 | 2025-11-19 03:12:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8113c8aa-061e-3d36-8d08-15f6073e1ae5 | -15.94634 | -38.90958 | 2025-11-19 03:14:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5695fe61-120e-37ba-89fb-331aac2f3f86 | -15.94565 | -38.91296 | 2025-11-19 03:14:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 77c02ca5-23f3-3629-a3be-2c5b0ecef8d9 | -6.1878 | -42.02836 | 2025-11-19 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 817ba248-1341-39fe-8bd3-8b9832ca0642 | -6.95409 | -38.61452 | 2025-11-19 03:59:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 37af02d7-e440-318f-be1a-dda1855b958c | -5.35245 | -43.03251 | 2025-11-19 03:59:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 452b9f00-aa2e-3347-b0ee-689f458d2490 | -5.09312 | -37.87253 | 2025-11-19 03:59:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e884c56d-b935-38f1-bd41-042965225e46 | -3.00878 | -44.38583 | 2025-11-19 03:59:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32c88e84-baae-3061-a122-2a437a2e2c5d | -7.1696 | -40.65863 | 2025-11-19 03:59:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 429f9346-4034-334e-82db-efdffd988562 | -7.02581 | -39.36193 | 2025-11-19 03:59:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f23aa36f-e880-3ba7-9d6e-7cd8f5e6e19e | -6.11964 | -42.95735 | 2025-11-19 03:59:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| aed30bb5-3534-3018-9fbf-b2a45e55d8b8 | -3.74505 | -40.83421 | 2025-11-19 03:59:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4e8cc871-1458-3404-856a-3bb465bf487e | -2.96417 | -40.83612 | 2025-11-19 03:59:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d43d19b-73f4-39b5-a4e1-7e8887c15611 | -4.99017 | -44.75908 | 2025-11-19 03:59:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 812bc020-2739-3fa2-b5f2-9a09b527bf40 | -2.22293 | -44.81756 | 2025-11-19 03:59:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 8dc1b765-5b60-3122-9def-fdfe87e1eef3 | -6.93986 | -39.62915 | 2025-11-19 03:59:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c9ed2e64-a2bc-345a-9b71-006ca6f26e79 | -6.93818 | -39.61824 | 2025-11-19 03:59:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e8f3ae00-c6d6-365d-80e6-9f72ef27fb5e | -3.00819 | -44.3895 | 2025-11-19 03:59:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c432e26-b4a8-3b24-ade5-d581cc843863 | -6.09326 | -41.76587 | 2025-11-19 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 56e79a70-2506-306e-a14e-37994144b259 | -6.08845 | -41.68497 | 2025-11-19 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2d8ed512-874f-38d5-9488-f3765f1a021b | -3.02224 | -44.45975 | 2025-11-19 03:59:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8201a730-6d5a-3da0-ab40-634daa6b37ef | -6.11895 | -42.96155 | 2025-11-19 03:59:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b7be58b4-107d-398d-9768-d7ee787e4a10 | -3.59607 | -40.97027 | 2025-11-19 03:59:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a71fee7-77e5-3a54-b82c-985ea5951de1 | -3.35243 | -43.50104 | 2025-11-19 03:59:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5eb154fa-f727-3630-8670-b8858a2ef32d | -6.18027 | -42.03105 | 2025-11-19 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 94b57df3-f464-3121-bc1f-d1968b51e1ad | -4.76071 | -45.75625 | 2025-11-19 03:59:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25c15b27-08ac-3809-8b57-9371a6910021 | -3.73499 | -45.59351 | 2025-11-19 03:59:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0dad09e-33b1-3ddf-ba7b-baffc92783c1 | -6.89023 | -39.20506 | 2025-11-19 03:59:00 | NOAA-21 | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bf080a6d-8aba-3452-bc9f-436edf9f5e26 | -4.87737 | -45.89764 | 2025-11-19 03:59:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 283f63ee-e311-35a1-9274-1e025da0ede1 | -6.19125 | -42.02893 | 2025-11-19 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fd2af8fb-c38a-342c-8587-687083c8ddd4 | -6.04058 | -39.65994 | 2025-11-19 03:59:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 69051251-d085-359f-ac9d-3d3e9af8a591 | -5.90257 | -38.15468 | 2025-11-19 03:59:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 24dc6dbd-e7af-353c-b8bc-386e5a380f85 | -4.86138 | -43.99769 | 2025-11-19 03:59:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f85ba8e-c2a4-379f-9710-7d35aec81779 | -4.76003 | -45.76043 | 2025-11-19 03:59:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bdc2942-daaa-3bf1-a11f-fb39cfa82a84 | -8.17221 | -34.9797 | 2025-11-19 03:59:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eac68734-2a80-3757-a2e1-3f9805c3c648 | -3.46203 | -40.51775 | 2025-11-19 03:59:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ccd8d0e1-62cc-33cd-a14a-bcbcab69d2de | -5.61853 | -37.80547 | 2025-11-19 03:59:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |


[Clique aqui para ver as próximas entradas](README7.md)
