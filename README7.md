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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40f3c2c8-ffd4-3641-b06c-0dc6a745a53f | -7.42434 | -39.89586 | 2024-12-05 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 53ba7ccb-687b-3125-96c1-af1d33d416ef | -6.93026 | -43.54593 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0761840b-94e7-3d38-888c-fc20ae14b8a3 | -2.25131 | -45.48363 | 2024-12-05 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc2839ab-24b6-3008-a5bf-e3ccb236fa58 | -9.82651 | -36.64098 | 2024-12-05 03:53:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 46792eaf-6a4a-36f9-8fa1-8ed059cebb62 | -13.61783 | -44.09228 | 2024-12-05 03:53:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4630f395-e243-3191-a0f8-4d1e3caedbdc | -2.75303 | -45.71295 | 2024-12-05 03:53:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55de5ee9-9764-3547-a324-b8e89564ad88 | -1.71399 | -45.78452 | 2024-12-05 03:53:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8adeada7-2c2e-3401-9301-376817f8204f | -1.71349 | -45.78757 | 2024-12-05 03:53:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e3e1d78-c77e-3ea9-bb77-e77f477bc247 | -8.07226 | -34.97771 | 2024-12-05 03:53:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 45908838-e60c-336c-83f0-c306918ab7bb | -2.31582 | -45.5288 | 2024-12-05 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34f237a7-8691-3df5-9cd7-1410ffc5d8e7 | -5.68022 | -46.50365 | 2024-12-05 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1bdb08e-fff8-3052-a35c-7501bd83edd3 | -5.17053 | -46.15226 | 2024-12-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91fb0a28-5a9d-3787-87bf-848d793615a6 | -6.99254 | -42.77785 | 2024-12-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c4e110e6-087d-3772-9d58-479a8f4adbd9 | -6.92332 | -43.53732 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5dd8e234-1ed6-3be8-bf4a-9e03b45f4ede | -6.92798 | -43.53441 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e57e49f-715a-32a3-a3a9-b088c5190132 | -13.361 | -41.33475 | 2024-12-05 03:53:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f0884c2f-77a6-3df4-8d24-bf6d215d9fad | -6.92272 | -43.54092 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29b73d7a-6f83-329f-a78f-3fd7976ac35c | -2.74846 | -45.70919 | 2024-12-05 03:53:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5415545d-308c-36f4-8e78-df570fec919f | -1.49757 | -46.15604 | 2024-12-05 03:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d7ab64c-f091-3f1a-8084-df68ef458fa8 | -7.4283 | -39.89279 | 2024-12-05 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9408390a-8396-3e7a-8fce-8cac4d643a5b | -1.4981 | -46.15274 | 2024-12-05 03:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f5c7c8c9-3a44-3efc-bb7b-f23d30195e12 | -6.98261 | -40.30368 | 2024-12-05 03:53:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 495a3143-5c5e-3649-b464-cfca602edf2a | -6.29758 | -46.44721 | 2024-12-05 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa92ed1b-c2ae-3282-bf13-b0437c35df18 | -5.58126 | -45.16131 | 2024-12-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a9e9a5f-4c4d-3a39-b083-184209f97294 | -8.0749 | -34.97655 | 2024-12-05 03:53:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a056c750-3954-3579-a27a-6364a1792224 | -6.93601 | -43.53607 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d5c60871-9993-35c0-8bd9-eddaefd30b04 | -13.35642 | -41.34156 | 2024-12-05 03:53:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 30f11241-5d8b-33b6-a9ed-aaca52dfc2e4 | -5.58498 | -45.21468 | 2024-12-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 180fe44b-da51-3568-b84d-f066f9caa783 | -2.15342 | -46.15664 | 2024-12-05 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0049dc42-9fcf-37a9-b09e-3b887bf46ffd | -6.9355 | -43.53946 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fe743090-e19c-301b-97fa-a26db2b37e9e | -6.93884 | -43.54392 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91bc3a44-a18a-3dd1-adc7-843be46d0b61 | -6.92619 | -43.54523 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2de8af1f-d4cf-3a1f-8565-067ab49f0659 | -2.24631 | -45.48278 | 2024-12-05 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7da1a734-2623-3798-a446-8d60428cfa09 | -9.98619 | -35.99971 | 2024-12-05 03:53:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 581eea97-192d-3cdb-b936-215669421658 | -5.17004 | -46.15516 | 2024-12-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e7e1dd7-24a4-38ce-a8be-fc9e33713683 | -2.1529 | -46.15987 | 2024-12-05 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 12285e7a-88e2-3015-82fd-202ac427fad4 | -6.93609 | -43.53587 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ff2db01b-c470-32cd-925b-04c99b90308c | -4.62594 | -38.48618 | 2024-12-05 03:53:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 90dcdef2-6255-3fa6-a3ce-595640beb390 | -6.93478 | -43.54321 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c58e902b-89a1-3efd-af8d-926774577475 | -6.05224 | -40.39378 | 2024-12-05 03:53:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9da58da-7b0e-3351-b867-055d7a7d9ca1 | -5.17774 | -37.59299 | 2024-12-05 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5881e01a-d6a6-3634-bc33-c3cd453b8e82 | -5.58026 | -45.15895 | 2024-12-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 989da16c-e8a1-3d41-84c7-ee2fd812223e | -5.39211 | -40.66209 | 2024-12-05 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc20032f-36ae-3cd0-9f76-9bf02ff26ff5 | -6.14858 | -46.68554 | 2024-12-05 03:53:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b460ad3d-ef6c-328e-b605-b67b6a7cdfc0 | -17.79409 | -40.4365 | 2024-12-05 03:55:00 | NOAA-20 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 78135178-295c-356a-90f3-2edee490447d | -19.1659 | -40.13904 | 2024-12-05 03:55:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| f9d0fa1e-9d93-31ba-9966-958a924d3626 | -10.82046 | -44.36937 | 2024-12-05 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b59a27fd-3dc4-3b16-9dc1-7ba3f9e2b958 | -21.65687 | -41.32558 | 2024-12-05 03:55:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 333f7455-6448-380c-8abc-8902185ffc92 | -16.68107 | -43.88272 | 2024-12-05 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b56d934-f73c-387d-b848-c605049befbb | -9.34133 | -41.2673 | 2024-12-05 03:55:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c0416e9-d9d4-32aa-9a96-9830dbb9379c | -9.34418 | -41.27178 | 2024-12-05 03:55:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bcb6de1d-f955-3f92-b76d-1d8f59cd6ed5 | -16.85246 | -40.66413 | 2024-12-05 03:55:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 59e0c865-f78c-33ba-8eec-91bba8ea7f9a | -10.50347 | -36.70242 | 2024-12-05 03:55:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2567863b-d610-3bdc-ab96-48c36c07faaf | -11.61298 | -42.09019 | 2024-12-05 03:55:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cea9605a-eec1-3738-97f8-122904e19b0a | -9.10325 | -43.19548 | 2024-12-05 03:55:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dab91682-f764-352b-a3c3-8c328af9621a | -18.50671 | -39.92133 | 2024-12-05 03:55:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 285a6302-7620-386b-a9f3-2d62b9fc686d | -10.49833 | -36.98564 | 2024-12-05 03:55:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 194b19b7-24b1-36d8-80c5-06a9ce622784 | -17.75396 | -42.89614 | 2024-12-05 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d70a827-0c24-394b-bee5-04b242d84d12 | -9.34481 | -41.26789 | 2024-12-05 03:55:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 91d0482f-7542-382b-8ea3-bcbfceda6b71 | -11.29356 | -40.97811 | 2024-12-05 03:55:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d4554c43-99fa-32d9-9b4a-090a17a1b740 | -9.89598 | -44.34977 | 2024-12-05 03:55:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c14ffacc-3b19-316d-abf8-e7808dcb5c58 | -11.3879 | -38.98497 | 2024-12-05 03:55:00 | NOAA-20 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9ab00741-0931-3eee-a488-8ae073fab77a | -9.87688 | -44.33852 | 2024-12-05 03:55:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38d29f84-eac5-35a7-992a-773e578eba76 | -10.56641 | -36.7908 | 2024-12-05 03:55:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 639c90d9-2eb5-304d-ac5c-a96523caf8da | -9.98771 | -38.1642 | 2024-12-05 03:55:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 44741600-824c-3779-a1aa-9afc8ef7ced7 | -19.16255 | -40.13848 | 2024-12-05 03:55:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 96ed33b1-abc0-3b07-8eac-bcd394202310 | -10.49997 | -36.7019 | 2024-12-05 03:55:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 68cf4003-1a56-3513-a221-7477f40b2449 | -11.29416 | -40.97444 | 2024-12-05 03:55:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 458c2d47-543d-3baa-8231-3103910d70d9 | -17.52746 | -40.81827 | 2024-12-05 03:55:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4998ebc5-4e25-37fe-9808-ae7cd4be24e6 | -11.19562 | -37.39946 | 2024-12-05 03:55:00 | NOAA-20 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f4b3c521-2e28-3969-9798-3b81d00b5a2e | -11.7672 | -38.68312 | 2024-12-05 03:55:00 | NOAA-20 | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 271c1c74-140b-310c-a876-d83d30c3d0fa | -10.49776 | -36.98948 | 2024-12-05 03:55:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 96f1fd81-45a4-3b1a-b4f5-182ba82a9f98 | -10.49706 | -36.69746 | 2024-12-05 03:55:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d0951886-440e-3e5b-8627-5bb8b1704b18 | -9.16587 | -43.16485 | 2024-12-05 03:55:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce967cb5-b26d-3986-a4e0-f2d8c737d953 | -17.386 | -42.66107 | 2024-12-05 03:55:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c19ceb81-7254-3c63-ba9f-9de6fc3cbe90 | -19.59085 | -40.86432 | 2024-12-05 03:55:00 | NOAA-20 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e62be4c9-fcc7-396e-8b66-e0885c9242f7 | -11.87232 | -38.35551 | 2024-12-05 03:55:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bbad570b-cc1f-37e0-b20e-08c836616fbe | -11.11166 | -37.32898 | 2024-12-05 03:55:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 803e7557-75c6-30f0-a48d-b7ba44146188 | -11.86841 | -38.35859 | 2024-12-05 03:55:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 503ff125-668d-3c00-9765-edf72e9f8f35 | -18.03921 | -39.92584 | 2024-12-05 03:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aef4499a-bb54-3ff8-876b-52e6d242e968 | -9.29154 | -43.27322 | 2024-12-05 03:55:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a0d5b583-dfce-34e6-b4e1-050f9cf17f43 | -10.49648 | -36.70139 | 2024-12-05 03:55:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eb24bef2-6dd0-3f77-a2d9-f4f446cc32c4 | -17.80698 | -41.49788 | 2024-12-05 03:55:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c11d8d87-da69-39ed-98a2-c3dc2f90b857 | -11.50078 | -40.4783 | 2024-12-05 03:55:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f113d59e-cddf-3fa3-a45e-65a6dd40105e | -11.01615 | -38.16358 | 2024-12-05 03:55:00 | NOAA-20 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aea2af14-3276-3401-9837-8376fc9158f3 | -10.68812 | -40.48592 | 2024-12-05 03:55:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1a0f1145-9730-38ff-9a0a-0e38b47b8d48 | -11.12072 | -37.26838 | 2024-12-05 03:55:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 232a7eb5-0940-3ef7-97c9-beec6ccb24d5 | -11.12015 | -37.27217 | 2024-12-05 03:55:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3187df50-d8fa-3f41-9b05-97cc454fdeeb | -28.58401 | -49.44384 | 2024-12-05 03:57:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ee88da63-258a-379b-af49-6aff55907a24 | -28.70502 | -49.30238 | 2024-12-05 03:57:00 | NOAA-20 | IÇARA | SANTA CATARINA | Brasil | 4207007 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0a3ac4a3-43f0-3342-8c19-d585b2848862 | -30.53239 | -50.4617 | 2024-12-05 03:59:00 | NOAA-20 | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 0fb2e81a-d86b-325f-97e0-318852048c1b | -30.52831 | -50.46056 | 2024-12-05 03:59:00 | NOAA-20 | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 8c0c40ae-1b17-3bd5-8c94-4c6ba7b3522f | -29.87158 | -51.15907 | 2024-12-05 03:59:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 246fef7d-1870-30e7-9fee-b501eb03ee92 | -31.25988 | -53.10437 | 2024-12-05 03:59:00 | NOAA-20 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 8019f151-cb72-373b-a743-e2ffe9b77ffa | -6.9346 | -43.5168 | 2024-12-05 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 59f5296c-175a-374d-925d-72195dfa85c9 | -6.9344 | -43.5401 | 2024-12-05 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 6155ace4-3f9c-365c-983e-27af4057cf01 | -6.9346 | -43.5168 | 2024-12-05 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 17f0aa28-1446-306c-a46a-c23733f2d381 | -6.9344 | -43.5401 | 2024-12-05 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 155.6 |
| f019e145-b1c6-3928-849f-c0b1bfbcba3c | -6.9344 | -43.5401 | 2024-12-05 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 77a9fb1b-4e8e-3a9f-a40c-b6d940ba2720 | -6.9344 | -43.5401 | 2024-12-05 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |


[Clique aqui para ver as próximas entradas](README8.md)
