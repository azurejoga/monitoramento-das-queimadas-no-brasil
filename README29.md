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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca873acb-99fb-30f0-8994-423b21006f25 | -11.3949 | -44.20737 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ceb5401a-839c-350c-ab2b-4b14ac679b81 | -15.15571 | -41.81735 | 2025-10-17 03:30:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5cf00f89-deab-3d13-8e17-0c9556e22e40 | -10.65136 | -45.2481 | 2025-10-17 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 095d601e-3faa-37bb-8810-799d8c1fb537 | -9.16088 | -46.61262 | 2025-10-17 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76f31bc9-ecb5-30af-bc0e-1dbe9d53a222 | -10.11747 | -44.56513 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d501d1c-a503-3f13-a68b-c1f2048992bf | -11.39486 | -44.14591 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58bde01b-eb43-32da-b4c4-a461b354f44d | -11.38687 | -44.20692 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac8e026f-978f-39f2-b83b-8aabed2540a3 | -10.8073 | -43.93922 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46ef8908-6cd2-3ac5-8df6-179d6bbc71d9 | -10.66078 | -44.86671 | 2025-10-17 03:30:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8001d26b-8199-387e-a9ab-81c3b04671ac | -10.28545 | -44.04119 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| f95c16c3-1adc-3fa2-af6a-ed1730c5847a | -9.71467 | -44.5572 | 2025-10-17 03:30:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67757d41-e729-300b-9a35-86b7b2931d5f | -9.26231 | -44.35657 | 2025-10-17 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 54bd73d1-99f4-376e-ac6d-5e5a0bba7c9c | -10.65461 | -45.29838 | 2025-10-17 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ccda374-9fc9-3e7b-9e35-43cf5cd24393 | -9.27011 | -45.27557 | 2025-10-17 03:30:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0980e88-c553-3979-b1c4-2c93e7105a4a | -11.40504 | -44.21905 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| edc7aad9-217b-3d27-9a0a-d50d4167388e | -13.12847 | -43.68525 | 2025-10-17 03:30:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ef539b7-60e1-3624-be09-c4bdac881bcc | -11.39464 | -44.19905 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2b75122-5406-3a57-898f-0e52db5fc409 | -10.64879 | -45.29717 | 2025-10-17 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cb2ab04-4100-30fc-a916-05f397d98725 | -11.48856 | -44.17505 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12a1d6c2-2d67-3b6c-bdc3-c3839210758e | -9.71144 | -44.56078 | 2025-10-17 03:30:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e1d34a8-e4d9-3068-bf14-7e4534c102b9 | -10.28827 | -44.05901 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e54233d8-bc6a-3e19-a031-2380c1ed466b | -11.37999 | -44.21021 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12a32c59-a77a-329e-be4c-a0893687543e | -13.36904 | -43.59596 | 2025-10-17 03:30:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 501fe83b-38e4-319d-99a3-9882a4b83741 | -11.52413 | -43.49871 | 2025-10-17 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb2c2697-493d-3f43-86ee-ce9ca9b0c2dd | -11.40218 | -44.22451 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49ef8f72-e7c9-3b16-ba3f-30cda1fa374d | -10.28642 | -44.03621 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 67b4906a-0b6a-315e-9b9f-86f98c82cae1 | -11.40484 | -44.21078 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 61fdace6-5349-38b3-a5ea-7d1a30ba8873 | -10.26047 | -44.04026 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb20ae1f-3695-328c-8caf-8b416e2f86a7 | -11.48503 | -44.20243 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6b2f4b8b-b4e5-33f3-9003-29456bf73f9e | -15.29403 | -39.6643 | 2025-10-17 03:30:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f32f8616-6903-3dca-9639-bc6a8c3d452e | -10.61832 | -42.31392 | 2025-10-17 03:30:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 03df35c3-5c41-3347-8c40-7d78f7c3dc1f | -11.38891 | -44.20612 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 96e08749-16cb-324c-a15e-fd66ba326ba8 | -9.12528 | -46.64145 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86bdb300-0021-3806-930f-2ce64e3713b5 | -9.1397 | -46.64395 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 51b5d700-58f5-3998-914f-239571162ec7 | -12.14037 | -43.2722 | 2025-10-17 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0618438f-5665-3e10-a81f-8e8483a1e120 | -11.47992 | -44.18737 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f8ce27f7-4fc5-32eb-a548-7afccfaade55 | -11.46045 | -44.25464 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a2720db-3686-3dcf-be3c-482b586deb8b | -14.15352 | -44.32025 | 2025-10-17 03:30:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e2ac668-1de9-3cfd-831c-bc7fa04b448a | -11.4978 | -44.06481 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c016d5b9-439b-367d-b379-49f985a150d1 | -10.25842 | -44.04765 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d8df4cb-bde6-3f0c-9258-33cda9a126aa | -10.29146 | -44.04262 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| f0bc47d4-23fc-3ebc-bcf9-8b396d820276 | -11.58521 | -44.07407 | 2025-10-17 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2ec2fb7-d507-3fd5-af14-3bbddda60593 | -12.90919 | -41.82594 | 2025-10-17 03:30:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fbabf600-7591-36d1-94a3-0146d1b736d6 | -11.46012 | -44.28806 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdd2c48d-1b20-36fd-9f2a-d6b8d2dc8049 | -11.47126 | -44.19977 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 416f810d-e8f4-3b94-9647-701823b7722c | -10.50441 | -43.43987 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95781126-baef-307b-83e8-fa42f1bd8dc6 | -11.45744 | -44.01938 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05cff4fd-7b20-3a3c-89b5-c00a19151be8 | -10.28733 | -44.06383 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdc66f90-73da-3d39-ae41-fce97bf51f40 | -10.26135 | -44.03579 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c4dc158-09a6-3357-b94e-dbd4ccef160e | -11.39721 | -44.22692 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e1f241a1-4b48-329b-b1b4-ac3957a2555d | -10.25861 | -44.04967 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5673a93f-b574-3e45-8f19-7ca45ab38ac1 | -11.39582 | -44.20281 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 024997a5-71bf-315d-964a-7bb23bd09822 | -11.46555 | -44.26049 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ceaee76-e8d2-390a-a705-8b84238c783a | -13.37461 | -43.59715 | 2025-10-17 03:30:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 786078a3-ad03-37e8-93e1-a66e2e6d6556 | -9.24679 | -44.36932 | 2025-10-17 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 062c1c6e-c539-3779-9dcc-0d68f9462281 | -11.47145 | -45.08427 | 2025-10-17 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4fe36f2-8fc6-36de-9dbd-71359c08178d | -11.40089 | -44.20863 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f62e4b21-e927-3c5a-9573-b01ad5439cc2 | -10.29528 | -44.05532 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b0a02e9-c6a6-3d8c-8a01-7f4f04e136ae | -11.40729 | -44.23035 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1a02e6c3-bb2d-3f3b-a75f-aa4a97f37975 | -10.08146 | -45.34113 | 2025-10-17 03:30:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2d0aedf-04f2-37d2-a55d-878e973964ef | -10.05341 | -43.83848 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 129f7eea-d34a-301c-b9e5-5852f9edc283 | -10.29038 | -44.04819 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6f5b5e17-44fc-3ca6-bf8c-7c7b52a776e5 | -11.40779 | -44.20536 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| d8a664eb-61a1-3259-845d-cb6f0529ee9f | -13.5075 | -41.00591 | 2025-10-17 03:30:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b13e928f-5564-3288-ab1c-2e8fd35fd153 | -9.02853 | -46.62959 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1abd9b1-9bac-3ad8-8752-a8ae7e8d180b | -11.40306 | -44.21993 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a10f50f2-4149-3e74-8c28-66decf7d991e | -11.4551 | -44.18696 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f8b4d78-ce62-332c-8cb8-06d8e0510b66 | -11.3791 | -44.21479 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2db0ef1-4ae3-3f1b-a8e4-eeff84945fee | -11.40906 | -44.22121 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1d41d43-b67b-35fa-a92a-2094d7dffa22 | -10.61225 | -42.31639 | 2025-10-17 03:30:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d16b732e-f811-3692-ae9a-c07755148675 | -11.39375 | -44.20362 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f608387-8cb6-3748-adc6-913685c82e72 | -11.40871 | -44.20081 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| baa0c522-3d66-3198-9490-8bfba2972c28 | -11.38776 | -44.20235 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e2cb71e-8119-3c7f-98ac-fd58d6d592e1 | -11.45717 | -44.05167 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1e07c3bf-01c4-3a99-ba9d-1aa681448735 | -11.41794 | -44.21703 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 06cb73f4-7310-3b3b-a421-d80af8f1592b | -11.45895 | -44.04276 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 81c4daed-a405-3708-b241-fd57bb2bce22 | -10.16185 | -44.53849 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 49446299-ddb9-3811-be69-ba211b467d79 | -10.28127 | -44.03046 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d2d4f8f-8c3f-3201-b3dd-3bfd9c4081f9 | -12.65574 | -41.25752 | 2025-10-17 03:30:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e2c0a026-1d44-3c4b-a312-f768ccfc7e76 | -10.15178 | -44.53896 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85ce9aea-70ca-3c1d-a873-c296cc549c4b | -15.16801 | -43.53246 | 2025-10-17 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d5ff3fd2-87d2-393a-96ee-091eec1ace8e | -11.40129 | -44.22907 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 98a356b7-021a-3b98-bb0c-95c992727e9a | -12.92462 | -41.82699 | 2025-10-17 03:30:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8bcebfeb-4139-3e23-ab0a-469f95e97b77 | -11.39553 | -44.1945 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e883512-e468-3d79-a1a6-233ceeb5c5e4 | -11.47813 | -44.19648 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c8dc90b0-ebfa-38db-b568-3f1d27113573 | -10.65078 | -45.25277 | 2025-10-17 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4b3bcdb-7910-3dc9-992b-53d20f716104 | -12.91911 | -41.82858 | 2025-10-17 03:30:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| faa5ab70-0f0c-337d-bf77-10688e7d4154 | -10.49252 | -43.40802 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b88e1725-f9a5-3189-a865-f77f3458a39f | -10.25932 | -44.04293 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 730786e4-247d-3065-8b49-6ee946076356 | -13.39149 | -47.21103 | 2025-10-17 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6eb46cb-23fc-356b-841d-d6e3c99d7199 | -11.48688 | -44.19337 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ee51d08-ee69-3795-8f06-e0b0558ec827 | -10.43433 | -45.02377 | 2025-10-17 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b4e11bbb-db03-3fd8-be80-6df26dce6799 | -11.48596 | -44.1979 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ffd9086-0cb1-31fd-9dee-748ad8b8b37c | -10.49943 | -43.43443 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2536aedc-d746-3730-8ab9-ef113872b04b | -10.26019 | -44.03832 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f243e4a-ff69-3f1a-9101-b3ce23168ade | -11.38614 | -44.21983 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b8ef4f42-99ce-3708-b020-da23b3ce610d | -11.38983 | -44.20156 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62bb5f53-e449-36e3-a66f-523dac0d2176 | -11.39529 | -44.22781 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f46e2286-393e-3294-a577-bd61b164e0f5 | -10.13642 | -44.585 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 47899f1a-f5fa-34c3-917f-49135f0ab9c8 | -10.50412 | -43.41029 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README30.md)
