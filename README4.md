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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e3b82b7-d08b-3add-a270-2de03ecde88a | -9.40905 | -35.93991 | 2025-12-20 04:21:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 97d162b7-5119-3353-a281-6649a95d414e | -5.92569 | -42.27457 | 2025-12-20 04:21:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4bb4e0fe-a1f4-3b61-a14a-1bcfefb16f11 | -3.86436 | -40.64409 | 2025-12-20 04:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 47852c63-547d-336c-aaa7-a0eaa88e9e9b | -9.5729 | -44.60855 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0ec6e21a-fa38-3af8-b368-14540d8ca4df | -9.56346 | -44.60344 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c65aad0e-4915-3258-8c28-564c35ed99dc | -13.39195 | -44.3729 | 2025-12-20 04:23:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23522753-143c-38fa-b167-9ca66d725cfb | -13.39138 | -44.37672 | 2025-12-20 04:23:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 951de1a8-4d9d-3697-a869-86defea3f857 | -13.61721 | -43.01307 | 2025-12-20 04:23:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 733c3f04-7d81-3a10-a174-01a13b3ac578 | -10.49569 | -44.92756 | 2025-12-20 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f16c1ea-096b-382c-b6e1-f0e6c307f90f | -13.54168 | -44.4967 | 2025-12-20 04:23:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35a4b7ff-140e-3f1c-8045-9755ab44bb90 | -13.9648 | -43.27444 | 2025-12-20 04:23:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e54b731e-606e-3c26-b7b1-0dc8179bb20f | -9.58453 | -44.59954 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5036fd23-cf50-3d74-8b44-ea20503fe05d | -13.94852 | -44.35123 | 2025-12-20 04:23:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3f568b7-9362-3c35-bfaf-94e4a28fd8f9 | -9.48107 | -40.98 | 2025-12-20 04:23:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 955815a2-b815-3e09-905b-254976c06074 | -13.94507 | -44.35071 | 2025-12-20 04:23:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d08084d-2d68-38dc-a56b-d3ff513bc9a5 | -10.0164 | -42.3307 | 2025-12-20 04:23:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 46e6ef10-11c0-3b0d-9822-a6fc56bbe63a | -9.11445 | -40.20816 | 2025-12-20 04:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6b6f3e2a-b68f-387a-8a80-186b084be6e3 | -9.51789 | -43.20143 | 2025-12-20 04:23:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1bfa2b9b-e229-386b-968b-d3877c9ca6ff | -9.79757 | -43.71817 | 2025-12-20 04:23:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aaad404d-0186-3cf6-9c6c-4affb56c8cb8 | -10.67392 | -40.40501 | 2025-12-20 04:23:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d6c360e2-5eb2-3cca-a6e3-fdb99b7071b8 | -11.16174 | -43.31265 | 2025-12-20 04:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 42602383-549c-3a11-bba3-69ffa807374c | -11.15824 | -43.31211 | 2025-12-20 04:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 503e7c5a-2b6f-3f22-a4dc-1c4c1ae4a146 | -13.38795 | -44.37619 | 2025-12-20 04:23:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fe3dffe-7c32-3db9-8737-eb857d772a89 | -20.45645 | -56.55118 | 2025-12-20 04:23:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5fd0b724-1e62-3ee5-a583-a38ff5aaec18 | -11.16233 | -43.30869 | 2025-12-20 04:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a1fba81f-41ea-3eaf-be4b-43ba247d8e10 | -13.9445 | -44.35456 | 2025-12-20 04:23:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8265bb6b-0ea2-3006-8557-cde1b91f6f0a | -9.57176 | -44.59391 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99f2a4a3-382b-3ba1-a8d2-086c7fb729a2 | -20.31168 | -57.27935 | 2025-12-20 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b0bbb176-b536-3fda-b894-03253bc3e29c | -10.49901 | -44.92809 | 2025-12-20 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1552f535-a5ab-368d-bd50-f137d711ef3f | -11.7571 | -43.32436 | 2025-12-20 04:23:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a56a8b3-0558-3578-a351-68f5ac7273fe | -9.57678 | -44.60555 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9e0e0f0e-2b96-3704-a710-c3daa5d8aef0 | -13.13643 | -40.23834 | 2025-12-20 04:23:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cbdaa4fd-9b17-3502-8412-382282288b52 | -13.13415 | -40.23571 | 2025-12-20 04:23:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0be1634b-d9b8-320e-aca7-fc5155034cb6 | -9.5812 | -44.59902 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 379d7977-b485-3af6-aea8-7f563876897a | -10.77194 | -37.13921 | 2025-12-20 04:23:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b13164ab-e175-3ccb-b3c1-8d612115428d | -10.02003 | -42.33126 | 2025-12-20 04:23:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 698cf148-48e4-3552-93d8-157b5671b84a | -11.16115 | -43.3166 | 2025-12-20 04:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 88393b39-5a85-3cde-be0f-a1907b33d1ba | -12.24507 | -44.38501 | 2025-12-20 04:23:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52732b88-31be-3fa7-9e1b-335e8fe0bb29 | -20.30658 | -57.27813 | 2025-12-20 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2ad9d70d-1f46-3397-8e05-9bf919e4b6be | -12.88851 | -43.8204 | 2025-12-20 04:23:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d99d9d06-1729-3271-8a15-fe0b3dd392b8 | -15.45217 | -39.29416 | 2025-12-20 04:23:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 61fda791-ad1e-36a0-b3c0-2060332c331f | -11.15765 | -43.31606 | 2025-12-20 04:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6961c74a-1567-33f4-afb0-35ca9df70b2f | -19.20962 | -40.12173 | 2025-12-20 04:23:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6c7e2dbd-1fe2-3155-893a-e07462ca7e79 | -9.57399 | -44.6015 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| dd4a7e1f-9040-376b-8be0-3f38ec715f18 | -10.14246 | -39.84293 | 2025-12-20 04:23:00 | NOAA-21 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2ee0fd8-f9a1-31e8-b17e-8fc5229c0b88 | -13.85677 | -43.97279 | 2025-12-20 04:23:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2d6f9e9-0363-361b-a1a6-3c36cacd4e59 | -10.49956 | -44.92455 | 2025-12-20 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4f0a250-e4e7-376b-9771-4bbe6c520f07 | -9.58065 | -44.60255 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b8c641fa-1572-3d79-abd0-41569b2103cf | -13.61229 | -44.32788 | 2025-12-20 04:23:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57a78962-cc59-3bd3-b0b8-27c13ca361e0 | -9.57345 | -44.60503 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c0425251-828a-3cec-b328-f4305c508393 | -9.3968 | -40.35821 | 2025-12-20 04:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2cc69367-8ae1-3105-9ee7-9ce3bb66b7c6 | -13.3574 | -44.11298 | 2025-12-20 04:23:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fc05fa9-29e5-3b30-821f-6e90915e10e3 | -9.57732 | -44.60203 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 427d4e71-fe91-3ab1-baf5-74faa12f6d5c | -11.76062 | -43.32489 | 2025-12-20 04:23:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c22177b-b694-30f9-9238-fc6fd7233fb1 | -10.49623 | -44.92403 | 2025-12-20 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 068a916b-11a8-3096-9bd2-7fedff53170c | -9.56679 | -44.60397 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad0d9f53-b346-3702-876c-f0e75dbd5723 | -15.26404 | -39.31455 | 2025-12-20 04:23:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 727dab9b-9360-3b81-bdc2-601d38a877ac | -12.51688 | -48.37965 | 2025-12-20 04:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28c8fee1-0c2c-3fbe-a77e-befdb8651997 | -10.49846 | -44.93162 | 2025-12-20 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3c5c049-091a-3aed-bfb8-628f517fd3c2 | -11.75768 | -43.32035 | 2025-12-20 04:23:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e6b84c3-336c-375f-b6ed-05b21e35d585 | -11.7612 | -43.32088 | 2025-12-20 04:23:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 028789b5-4901-39ad-875c-7a548fea16e0 | -8.66893 | -44.2751 | 2025-12-20 04:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3112a8b1-fd20-3154-8898-5ff0eadd919d | -10.14191 | -39.8469 | 2025-12-20 04:23:00 | NOAA-21 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99c41912-d772-39e5-83f2-1859c43cda62 | -20.31235 | -57.27612 | 2025-12-20 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5c45502f-d0b5-38dd-a186-da4d56bffb0c | -9.56957 | -44.60802 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7565788f-2386-3bcb-a5b6-db7cad4e9a6b | -9.47948 | -40.98333 | 2025-12-20 04:23:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 724e667c-1c1b-3e17-bbe1-c13931547cdb | -13.54509 | -44.49725 | 2025-12-20 04:23:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0098ebb8-3b18-33e5-8cba-d0534e76e711 | -9.57787 | -44.5985 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a4fc3571-34bf-3d2d-ab84-bef23e74cc1b | -13.96119 | -43.2739 | 2025-12-20 04:23:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67a6662c-5098-3a66-872b-f8786394bbd3 | -10.67441 | -40.40149 | 2025-12-20 04:23:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dda7282f-c70a-3e54-94aa-645aa86bb394 | -9.56624 | -44.6075 | 2025-12-20 04:23:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f799ea06-eb76-3e15-9ac4-aa0105f46e49 | -20.309 | -57.27627 | 2025-12-20 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| fe664f19-8e05-3844-a3dd-1e208676a7d3 | -28.26302 | -48.86791 | 2025-12-20 04:25:00 | NOAA-21 | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 04d9cd7a-0e60-3608-8bda-f006471ca388 | -27.90031 | -48.95464 | 2025-12-20 04:25:00 | NOAA-21 | SÃO BONIFÁCIO | SANTA CATARINA | Brasil | 4215901 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 52baa6d5-2741-38a4-8bad-28ffb2a355c9 | -29.05613 | -52.34582 | 2025-12-20 04:25:00 | NOAA-21 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9ebe4f1c-b0d6-3795-b840-c07be1d2c45b | -20.3083 | -57.2795 | 2025-12-20 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7aafcde9-d877-3c36-b8cd-7673d5a84c05 | -26.74327 | -52.08829 | 2025-12-20 04:25:00 | NOAA-21 | VARGEÃO | SANTA CATARINA | Brasil | 4219101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fde1d919-3347-31f6-a1db-309c26b1d0bf | -25.51093 | -49.46758 | 2025-12-20 04:25:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7d217022-721b-31a2-a542-43d338f54196 | -20.45821 | -56.55314 | 2025-12-20 04:25:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 435985d6-d7f0-3b74-bc2c-0572188623e5 | -25.19619 | -49.52277 | 2025-12-20 04:25:00 | NOAA-21 | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 923f305b-509b-30fc-82c1-9acf53ef1169 | -20.45334 | -56.55206 | 2025-12-20 04:25:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7fbe6ab-67b7-31da-ae54-8c54e1424e0a | -23.47452 | -47.29386 | 2025-12-20 04:25:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9eb9ce4b-9d87-3932-a800-5c9f683aa1f6 | -17.67776 | -42.44505 | 2025-12-20 04:25:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 185cb406-12be-31ae-b9de-bb4a73b97f42 | -28.88017 | -49.34421 | 2025-12-20 04:25:00 | NOAA-21 | ARARANGUÁ | SANTA CATARINA | Brasil | 4201406 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 673afc23-d1c1-3fb7-bcb4-cf57ea939c95 | -27.90365 | -48.95526 | 2025-12-20 04:25:00 | NOAA-21 | SÃO BONIFÁCIO | SANTA CATARINA | Brasil | 4215901 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fdeea8c5-daa3-3354-b137-cf5df372e957 | -22.98088 | -48.64612 | 2025-12-20 04:25:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8aafcef9-4c80-30cf-b4c7-e6312352a41d | -31.60878 | -52.35488 | 2025-12-20 04:27:00 | NOAA-21 | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 345914b4-c0e2-3f4c-bac5-822e67dea8fd | -29.54716 | -50.4927 | 2025-12-20 04:27:00 | NOAA-21 | ROLANTE | RIO GRANDE DO SUL | Brasil | 4316006 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a2bb9f0a-4017-3a1d-bc35-4487d8b1537b | -1.03673 | -46.83132 | 2025-12-20 04:48:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b83b2867-b413-3dbb-9b5f-4010d78eb946 | -1.8884 | -46.27026 | 2025-12-20 04:48:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee792aaa-b641-3bf7-aada-ccbe8c83397f | -1.50295 | -45.6906 | 2025-12-20 04:48:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b9d603b-3a1d-374c-a274-766569ffe3f6 | -1.89287 | -46.26632 | 2025-12-20 04:48:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1023f0fc-4582-3ae4-a393-19d2868bb140 | -9.56799 | -44.60775 | 2025-12-20 04:50:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 168e64b6-45b7-396c-825e-ed1b40712057 | -4.17136 | -40.71782 | 2025-12-20 04:50:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a862225b-28d5-3781-837d-c09d99f7161e | -3.85994 | -40.64576 | 2025-12-20 04:50:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 32e88f71-f791-3174-a99a-2374eae2328c | -4.1719 | -40.71401 | 2025-12-20 04:50:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 38e6d3a1-69ea-39bc-9055-ae8dbd79771a | -3.89876 | -41.70044 | 2025-12-20 04:50:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d2e83fae-5d52-3a1e-99ab-97d145f7edab | -9.57 | -44.59314 | 2025-12-20 04:50:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc21fda5-7942-367e-9b59-16d5522ff8c4 | -3.86264 | -40.64046 | 2025-12-20 04:50:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c085136a-916c-356b-bb8b-7985744a3b92 | -4.1745 | -40.7158 | 2025-12-20 04:50:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README5.md)
