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
| 6b2dfcae-c326-3fa7-9df4-53c81b384dc1 | -8.7317 | -36.59282 | 2024-12-05 03:53:00 | NOAA-20 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| da26ddba-3f1f-3afb-8d84-44d558406e0a | -4.449 | -46.04113 | 2024-12-05 03:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9f44b99-eb3e-3864-8f0f-5a46391337cf | -6.93195 | -43.53534 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0b9f964f-9e91-34de-a6a5-905aa6a247fc | -4.44972 | -46.04026 | 2024-12-05 03:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| acf58046-8756-3c75-aa0b-6842ea4a7d84 | -5.69827 | -45.04769 | 2024-12-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7420a11c-3700-3a10-90ec-038f71f886c2 | -6.93257 | -43.53176 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4d4696f-341b-3bbc-9704-a113e6125dde | -6.93502 | -42.83118 | 2024-12-05 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b22e92b-7f99-3523-9ac8-933df811ceb1 | -6.66439 | -34.97324 | 2024-12-05 03:53:00 | NOAA-20 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4643d00c-e0e6-3f2c-bd71-c17005bd1ee0 | -8.67355 | -37.00022 | 2024-12-05 03:53:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 14f4d0ed-3f6e-3163-8d58-174ed11770fc | -6.15419 | -46.68339 | 2024-12-05 03:53:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b20a89a-3804-33e0-b12d-5189c833ab7a | -2.25085 | -45.48651 | 2024-12-05 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b8e63a5-51dc-3806-af9a-4eb8950e1421 | -6.98201 | -40.30742 | 2024-12-05 03:53:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9bab21a2-c505-3e49-8c75-3ac44f591e22 | -7.42771 | -39.8964 | 2024-12-05 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a37182ca-4f23-3cee-93d9-3657f0b7c1f5 | -7.43328 | -39.76516 | 2024-12-05 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 61b24bde-c1e5-370d-b578-bb4b1ef02c1b | -6.29258 | -46.44635 | 2024-12-05 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d04845c-34d8-3309-9717-4d54ccfd5d22 | -6.93492 | -43.54303 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 38e3af58-efd0-3e07-8192-f886276805b5 | -6.93433 | -43.54663 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a7a0ef48-3e4a-3da0-a087-4bded8eb743c | -4.40118 | -45.93092 | 2024-12-05 03:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34b36031-6df9-3041-a273-bd4945941233 | -14.50665 | -40.71958 | 2024-12-05 03:53:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd110891-8372-3884-982f-ac6f4155ce13 | -5.20313 | -37.58289 | 2024-12-05 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f002c600-d058-3c04-8f17-5f977b2836e7 | -5.58046 | -45.16616 | 2024-12-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98f90602-68da-3b9e-ac06-cd70a352d75b | -13.41392 | -41.11497 | 2024-12-05 03:53:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8bbbae47-af12-32e2-90fc-7f7df6e2bd46 | -7.43108 | -39.89694 | 2024-12-05 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd91841f-c71c-3d3e-b6fc-f2f3cbfa7e5f | -6.92725 | -42.82984 | 2024-12-05 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0749439b-a6c1-30c2-8825-b5628ef609ff | -5.4739 | -38.58084 | 2024-12-05 03:53:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d0c47fd-05a7-3bd8-948a-240a118e1cf4 | -2.74799 | -45.7121 | 2024-12-05 03:53:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 54a99c72-80ef-36e7-8d40-3c4153740f0b | -6.93263 | -43.53154 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e40d8e0c-f0b6-399f-9ca8-588109050a06 | -6.93144 | -43.53873 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3db5febf-048e-3915-b53b-1f48f85cdaa8 | -6.27311 | -41.03734 | 2024-12-05 03:53:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5367f6ae-ef8d-3d6d-b351-b3186791dff0 | -6.93072 | -43.54251 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d5a665f1-4f47-3c95-8e9d-fb9fb509e6bb | -6.04878 | -40.39323 | 2024-12-05 03:53:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b4a78f49-bb8e-3b74-b728-dc55d0ea23e9 | -5.74846 | -46.50152 | 2024-12-05 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a44a8b42-93a8-3e2b-bf0d-8f48f9050226 | -13.36317 | -41.34272 | 2024-12-05 03:53:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0f0df631-f47a-359c-8192-56c172a7bf2d | -6.93823 | -43.54751 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61ec1b9a-94a4-3b75-892c-9c3f2c048da4 | -4.70436 | -38.72038 | 2024-12-05 03:53:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4c16f123-1d0a-38ab-ae3b-eaebefa0b4e7 | -8.23532 | -39.03453 | 2024-12-05 03:53:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 90a6acfa-0654-3247-a179-546bf1dcad74 | -6.93663 | -43.53248 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8574d8f-f8be-3f6e-9bf8-4927991c9e81 | -6.92738 | -43.53801 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61a4705d-d126-3639-bcf9-aeb52cee0bf1 | -11.87144 | -43.72287 | 2024-12-05 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 510a9f13-dcc5-3d65-a4ea-d1e2b707f63b | -5.38782 | -42.956 | 2024-12-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| be10703f-76d5-3e64-a67a-a8cea04b5841 | -7.33562 | -39.81526 | 2024-12-05 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0f63088a-5cf1-3148-a46e-b2a9e784658a | -6.49164 | -35.19786 | 2024-12-05 03:53:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 87b4d1b3-67a6-37f1-b228-01c816eed8ce | -8.58755 | -39.53207 | 2024-12-05 03:53:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eaae3281-b85d-3c83-a3d4-56af73c05df2 | -5.24788 | -40.88214 | 2024-12-05 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fdd0282b-c7e6-3d90-a922-8179a44466e9 | -13.3604 | -41.33843 | 2024-12-05 03:53:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 56723abd-66ad-3a09-ba86-b13f612f0ab5 | -5.49629 | -40.78016 | 2024-12-05 03:53:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0736fd98-efef-320e-a312-301a40423467 | -2.74894 | -45.70628 | 2024-12-05 03:53:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 469bc2be-a182-3a42-9af5-d83ef8d13d7f | -12.71657 | -40.20734 | 2024-12-05 03:53:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0694fb15-7547-3aba-9be0-c080cbd4d121 | -12.45475 | -43.55923 | 2024-12-05 03:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2bceefc-fb71-3568-bb69-e49b37a05805 | -1.55979 | -45.76688 | 2024-12-05 03:53:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b208e06-bc2e-33ad-84e9-339c33d7eb2f | -6.93204 | -43.53513 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 61854e5d-6f7e-3a92-9c96-4425f8445f22 | -6.94007 | -43.53678 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd39261f-5dc7-342b-8126-3aa4b74530a3 | -2.31535 | -45.53168 | 2024-12-05 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 804215c9-d215-3c0b-83e1-e5311c78579d | -6.93322 | -43.52795 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8a0e9e4-6102-348b-9f03-0ea8061b80bc | -5.25571 | -40.40463 | 2024-12-05 03:53:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a8b02ff-6240-3748-9bc8-27ef52040dd6 | -6.93668 | -43.53227 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de1cd305-b131-3796-a629-ffff1afd0373 | -2.15764 | -46.16397 | 2024-12-05 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b66045af-74b4-3213-91e7-04a5a8e09b63 | -12.33493 | -44.48735 | 2024-12-05 03:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09273c98-589a-3ff7-9f1a-4f2fef7a25f5 | -5.09758 | -40.14437 | 2024-12-05 03:53:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d6ef81bc-8d9d-3d1e-aeb7-d12dabb055ec | -6.15471 | -46.6804 | 2024-12-05 03:53:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7df9ef8e-9634-3058-ad4f-a622f21398d4 | -5.69596 | -46.59367 | 2024-12-05 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7329131d-8c2a-38fd-992f-14f44febdb68 | -4.50372 | -44.33858 | 2024-12-05 03:53:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95ef3180-9a24-362f-90fe-8b4e8a9f3148 | -4.50444 | -44.33418 | 2024-12-05 03:53:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f743add4-c066-388f-a2d8-f6a6a672b151 | -1.23299 | -46.03179 | 2024-12-05 03:53:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08050514-0701-375a-b7cb-074b4ca09c9a | -7.42888 | -39.88919 | 2024-12-05 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a2bf04da-9c3a-36f4-bcea-94a43989df9b | -6.93539 | -43.53965 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 02cb452e-ebc4-3a95-9dcd-5327940e1356 | -5.19982 | -37.58237 | 2024-12-05 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ff9b2afb-1f99-3f93-950c-2c804bd4d1f7 | -4.9077 | -38.74486 | 2024-12-05 03:53:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e1313090-1da2-315a-9195-e3465bf310b4 | -6.29209 | -46.44918 | 2024-12-05 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d991fd9f-61cb-38d7-a59a-75567c59350c | -5.1772 | -37.59645 | 2024-12-05 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42883e4c-daf3-36db-b6e0-885cf75fa307 | -6.9301 | -43.54611 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4939283b-2585-3315-9c55-ff8d1db943e5 | -9.47398 | -36.60892 | 2024-12-05 03:53:00 | NOAA-20 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e9689831-a5d3-340b-96f4-661e79af50d9 | -4.44924 | -46.04314 | 2024-12-05 03:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb81b88c-07ed-3c57-9f0d-cdc2bb25f484 | -6.14911 | -46.68246 | 2024-12-05 03:53:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12c9abba-a015-30fd-ab37-0e19ecb34c12 | -6.92857 | -43.53082 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71218e9c-b4c1-3f72-b56e-7eeeab486452 | -1.56029 | -45.76375 | 2024-12-05 03:53:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40936333-ac87-373a-9893-3733a28ccefb | -6.93085 | -43.54232 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 73b010b1-c7a0-3de0-a8cb-b313d8a69af6 | -5.69544 | -46.59667 | 2024-12-05 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75d6c2f5-d15d-3abd-9390-a41330079859 | -6.93945 | -43.54036 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dcf4872-8d35-3c20-bcbb-e4c250801819 | -6.93417 | -43.5468 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bc704cec-bd78-3cc6-934d-2fc22a224017 | -6.2396 | -46.18424 | 2024-12-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a264fd7-5d2d-30e1-89f9-1751cb7545d2 | -13.09715 | -43.37311 | 2024-12-05 03:53:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53705656-aea9-3581-8bd4-61fc7ea0888f | -8.50071 | -35.72646 | 2024-12-05 03:53:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b89e13f5-d6d4-302e-a0f8-19f2b38c0ada | -8.18111 | -35.27139 | 2024-12-05 03:53:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2ce39f40-fcd9-31b1-9d51-98b73f3d8992 | -1.2277 | -46.03094 | 2024-12-05 03:53:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36e77948-0cbd-30ff-b253-902bb2705a5a | -6.19625 | -46.73064 | 2024-12-05 03:53:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05d3b91c-6d86-38a5-ad07-0701f01092cb | -7.42493 | -39.89226 | 2024-12-05 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9f1575bd-4e18-310c-9e7d-a9ef37593552 | -6.92679 | -43.54161 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2353386-1689-3072-b785-15c20bd2f7a9 | -5.38839 | -42.95253 | 2024-12-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6caf0061-c4e7-3f32-8666-7e7ac5584268 | -2.17065 | -45.34786 | 2024-12-05 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c249fc8-be54-3edf-8e86-9662c352e509 | -4.61606 | -40.35034 | 2024-12-05 03:53:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 51d81aa6-cfb7-3c36-bc32-e6a91405e860 | -4.92508 | -40.14473 | 2024-12-05 03:53:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| af197f2c-2edd-3131-a6da-48aa1683409a | -2.15816 | -46.16073 | 2024-12-05 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 44fd4d28-509d-3fda-92ce-26ec0ad73f65 | -5.57943 | -45.16377 | 2024-12-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90dfa763-4868-329d-b131-dae21eafda3f | -2.75351 | -45.71002 | 2024-12-05 03:53:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c404096-1464-32bf-b4de-26246f057d80 | -2.15238 | -46.16311 | 2024-12-05 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ec9d7c67-83c2-3523-9ccb-903ba45937f5 | -6.93134 | -43.53893 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 21ef4404-0fac-3388-b3a6-c5c5606b36d3 | -7.43166 | -39.89333 | 2024-12-05 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7bd3b569-c33a-3450-8fcd-1daf8f78b137 | -5.75303 | -46.50529 | 2024-12-05 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04d9b226-4b8f-3fcf-98c3-9c26bb1bec38 | -7.55906 | -35.23388 | 2024-12-05 03:53:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README7.md)
