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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56a7f0d1-6181-3c7d-bc7f-c7a37c74f01c | -11.20696 | -41.62224 | 2024-10-25 16:50:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 6175831d-a019-3bc5-b3bd-ce66339fd9ec | -11.20598 | -41.61691 | 2024-10-25 16:50:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 044169c3-c0ce-36c9-ab94-1e64d816afb9 | -13.77898 | -42.47432 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 86aaaf43-9b59-33ba-988b-ee0678a970c2 | -13.77465 | -42.47509 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 41fdd5dd-f52a-3e25-8d20-8fe849d0f64c | -13.7711 | -42.48021 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3a69a2dc-6fe9-34c7-bdcd-773d086f2f9a | -13.70407 | -42.514 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 26bd34d5-d183-3c23-98a9-4a29253e1600 | -13.68436 | -42.86634 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 41b5672a-7301-321d-9706-65bb516169ba | -13.68412 | -42.86678 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| cadafb2f-4025-3acc-8167-a116d69e9e5a | -13.68013 | -42.86705 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 56dde271-3d88-3b8a-96d8-04d040018c3f | -13.67727 | -42.87557 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 2fd3b2cc-ccf8-3139-a6d0-3ca4cf625995 | -13.65994 | -42.94972 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| eb04e2d8-74d1-3cd4-88e3-198441445b12 | -13.63478 | -43.00294 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 83c172c4-7055-3754-936a-dd06096071b1 | -13.61656 | -42.70693 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 07ec18a5-df84-3a97-b594-71d13980f92a | -13.64163 | -42.26766 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b3ff2a72-5812-3d39-b8b0-27b0954d7c68 | -13.63191 | -42.11302 | 2024-10-25 16:50:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2da555ef-aa28-3fa8-8a20-8e9ef714cce3 | -13.00723 | -42.19098 | 2024-10-25 16:50:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 9193569b-ab8f-3629-80d2-f77e43200182 | -13.0027 | -42.1915 | 2024-10-25 16:50:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 1e029dad-a5db-3ded-9402-7f7f33746795 | -12.95956 | -42.33403 | 2024-10-25 16:50:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 2211b5c8-c64c-30b1-a7a4-1344c3fabec5 | -12.72263 | -42.02559 | 2024-10-25 16:50:00 | NOAA-21 | NOVO HORIZONTE | BAHIA | Brasil | 2923035 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 73c708f6-f702-3e70-aa5d-73a78ebcb087 | -12.64714 | -42.36053 | 2024-10-25 16:50:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| bb1b5a33-9cfb-372b-8dc2-ffb84f4c322c | -12.59241 | -42.06175 | 2024-10-25 16:50:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5f562091-61cf-3840-8ed4-aa2cbaeeefa9 | -12.5737 | -42.03678 | 2024-10-25 16:50:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f8e9975c-55ad-363a-ae2c-f49920677e28 | -12.55489 | -42.01389 | 2024-10-25 16:50:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 7b525362-9c48-38d7-b419-ebc45aeef922 | -12.55476 | -42.0108 | 2024-10-25 16:50:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| f65d45e2-355a-3d38-a406-5c747d15b03b | -12.47512 | -42.09249 | 2024-10-25 16:50:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 28683bed-4105-35ef-9f92-55670a569fc8 | -12.39893 | -41.93459 | 2024-10-25 16:50:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 5af7c8a9-a6d2-310f-a552-b5f8ea87e0be | -12.38666 | -42.10082 | 2024-10-25 16:50:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 21986dcb-9ac4-3e99-9bab-676e76998a3c | -12.38213 | -42.10172 | 2024-10-25 16:50:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 91c0a9af-9ded-364e-8503-e81a4f9e4cd9 | -12.22774 | -42.92709 | 2024-10-25 16:50:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2face176-424c-3d2e-8afa-bc52e692c237 | -13.5725 | -42.92379 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| a381e42c-316f-3ab3-8a91-17b476f7c194 | -13.53414 | -43.30069 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| fb59539b-7cde-34ff-b7e9-edc6a981a2bb | -13.53348 | -43.29688 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ed4ca61f-fd19-3a9a-a87a-cccbd7324faa | -13.53326 | -42.9964 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 113c8696-bd00-3dff-8f32-4695a087c32c | -13.52451 | -42.72726 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7ab6d0d5-663e-3dc3-a1f0-65819e58fdb9 | -13.51546 | -42.92167 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 27971441-fce0-3556-81e1-71a2af864848 | -13.51378 | -43.03262 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 9c313f66-ed6e-35a9-bcb1-395a2f11759f | -13.50399 | -43.02641 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f85f7d49-34ec-36f5-bed2-29be9ca744b8 | -13.49304 | -42.62558 | 2024-10-25 16:50:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 104.8 |
| 764b2e3a-127c-3459-965a-97d4107acfa7 | -13.49228 | -42.62136 | 2024-10-25 16:50:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 104.8 |
| 0f1d75b8-c9db-3e04-8896-09e373149359 | -13.45608 | -42.59369 | 2024-10-25 16:50:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| d194af17-ca21-3006-a840-aadd8d6e0e9f | -13.44526 | -42.94261 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 3631c469-a98a-368e-92d3-03026cc9efde | -13.40348 | -42.48217 | 2024-10-25 16:50:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 40159609-acd0-3fe2-a2af-e7ed705c5e02 | -13.40051 | -42.61688 | 2024-10-25 16:50:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 39444148-ed4e-33a6-af71-aef063bc8f73 | -13.39929 | -42.47949 | 2024-10-25 16:50:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| cf533b8c-37ea-3b83-8903-3604db8d0ba4 | -13.31977 | -43.34385 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ed5f38e0-25a8-3df4-b16b-2f054b9057b6 | -13.31847 | -43.13372 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 27a4a4d8-24be-3583-a144-19d9fd059b8c | -13.3054 | -43.3347 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e5262250-4400-3092-8848-f05a976ff623 | -13.30473 | -43.33089 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| cb6d901b-a6e0-3e85-a441-940128dd4a35 | -13.29672 | -42.94084 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d38c27c4-2f8e-3af5-86d1-556139d9e970 | -13.27731 | -43.29636 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a2e4739c-f613-3fa0-b16d-87cb61fcdbad | -13.57282 | -43.42592 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5d40337c-e183-3a03-a8cd-86c5c35d114a | -13.57218 | -43.42219 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3e9c3a43-92c6-34dd-9798-066f56faa633 | -13.57205 | -43.42596 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 667cbd0e-811b-36d7-a10f-f53971ab20ad | -13.57138 | -43.42224 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a68b5d23-749b-3ae0-9316-47ec1da47aa6 | -13.53951 | -43.52421 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c991a384-27ee-3f43-bc24-97d9c17a634a | -13.52249 | -43.42751 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7a217ad7-681e-3794-a368-2b65bfebd4dd | -13.51474 | -43.47902 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bf06beab-e654-381e-998c-3ec004570ab2 | -13.50857 | -43.49168 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f015d2f9-abb4-39c6-a874-a4a128383bdd | -13.50681 | -43.43429 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 16cc4d2d-4641-35a1-b15c-6b9f2b1a15ef | -13.50615 | -43.43055 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d6ee72c9-eb9c-3162-8534-63337411707f | -14.6517 | -42.33539 | 2024-10-25 16:50:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ba8a189c-d589-3cd0-bb61-4848275a13e1 | -13.50273 | -43.43505 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 44321a2c-d6d6-3444-a803-6f05ce3b2e80 | -13.48349 | -43.49249 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1dd8222d-6193-3949-a91c-80486fa96eaf | -13.46635 | -43.48836 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 14a251d8-a1d4-3433-8da3-abdc6d2a29a1 | -13.43245 | -43.48699 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d941d0e5-6602-357e-a684-0a2db4904d5d | -13.20236 | -42.94846 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 489e0f2f-519d-3f65-9149-0176bee0b607 | -13.19874 | -43.09769 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bd39907b-4b80-3b39-8d83-adfce0d3897d | -13.16469 | -42.98001 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| daf27c72-aa2b-3886-9b0d-a3ec8f91d71c | -13.14503 | -43.16446 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 34.3 |
| a650b367-85b9-32bd-82ea-dafecdbf9026 | -13.1162 | -43.05124 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 3709bb30-66a9-3e75-a3f2-b90b0f7ef491 | -13.03331 | -43.09898 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d5a70e4b-61e5-3a74-8e15-1a7ec1881a94 | -13.03121 | -43.1117 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 545ef193-4f52-3b3f-a09f-4af0f2146614 | -13.02698 | -43.08784 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 43.4 |
| 48d857b1-628b-366a-92d0-4c4489eaf933 | -13.02278 | -43.08865 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 43.4 |
| 1e71b17b-0ea3-3f9c-af19-329a8f05a729 | -13.01578 | -43.09819 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5384229b-6a5a-3d72-9b86-b19981c9cbb8 | -12.99977 | -42.91002 | 2024-10-25 16:50:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 87e5b932-2440-3d0a-90c9-72ec7de5baf8 | -12.96528 | -42.59075 | 2024-10-25 16:50:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| aff8d76f-446c-32ff-af0e-82e60b6b6aff | -12.90548 | -42.58381 | 2024-10-25 16:50:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0f8f25a7-b1bf-32b9-bd81-cd3a2d426a3f | -12.9019 | -42.58891 | 2024-10-25 16:50:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 19.7 |
| e1842663-5f2a-3833-bdc2-0bed754f2707 | -12.90111 | -42.58458 | 2024-10-25 16:50:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 56bcdbbb-b2be-3897-bb27-8af8610bb708 | -12.89353 | -43.19367 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 78437931-5c5c-3ac9-9a52-b28d8dfbe70f | -12.87215 | -43.09913 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 60.2 |
| a771fa26-a428-36eb-b9d6-c562e2065799 | -12.78768 | -42.7909 | 2024-10-25 16:50:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a4bf4eac-07c9-3ea8-a6ef-59529dc2b8cb | -12.78696 | -42.78688 | 2024-10-25 16:50:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 163c6343-bdce-3532-bd35-125fc929d008 | -12.75751 | -42.96954 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 13cc4d47-3a2c-31cb-baf0-6e69a24951dd | -12.75497 | -43.14935 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 003b331e-b828-3ade-a4e1-ae654a34c42b | -12.75481 | -43.14909 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 9ce4d72d-df46-3902-a9fe-8d28907fd5c9 | -12.71828 | -43.13938 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 77474222-06b0-3295-8dea-b661bdfd948a | -12.71406 | -43.14015 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 8125f078-3a20-30a9-94d8-3830e425feba | -12.68969 | -42.97757 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| fd4964b8-f737-361b-85d7-3afd48163edf | -12.68898 | -42.97353 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| c9ba926f-7187-3845-974f-36c0b785d4e6 | -12.68599 | -42.69768 | 2024-10-25 16:50:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 26dca09c-914b-3a9b-a4d1-ecefcaef970e | -12.66924 | -43.01112 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| d9c481f6-3bd2-3eac-842d-ca4135f7eff9 | -12.66387 | -42.83203 | 2024-10-25 16:50:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| ed660549-e6b7-3660-abc3-3769607538aa | -12.66368 | -42.78064 | 2024-10-25 16:50:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 3209492e-b556-3ce7-abc4-357dafc7832d | -12.59146 | -42.82576 | 2024-10-25 16:50:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b2fc6eb1-9733-39b0-b173-5bd6cddf9ebe | -12.58942 | -42.82432 | 2024-10-25 16:50:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5f6f03c3-f603-374d-bb71-8d5903cc42cd | -12.57824 | -42.93747 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 18b7fe10-c804-3151-9f03-f27f2ac9798d | -12.57716 | -42.88124 | 2024-10-25 16:50:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| f83907f5-b9de-3b99-8a27-4e90e1ba2a23 | -12.57685 | -42.92964 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |


[Clique aqui para ver as próximas entradas](README142.md)
