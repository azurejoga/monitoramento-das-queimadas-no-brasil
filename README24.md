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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f25f9e46-1bc2-32f4-b6ea-be954f798934 | -11.66829 | -43.59619 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| b8afe2d4-5fde-3900-87bb-307dabf01a5f | -14.32822 | -44.74609 | 2026-10-02 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a367cc8-e25d-3792-ba47-07be363eb08e | -11.44137 | -43.40724 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 21595b30-fdcf-3361-bfcf-d68a1f6b1cb8 | -13.34538 | -43.85215 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 75c1bc1a-265b-35cc-843d-b567c0f05a12 | -11.7996 | -43.57489 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2edd75fa-7e5e-3e27-b9e0-bf67c929c5f9 | -13.48009 | -42.48697 | 2026-10-02 03:19:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 89453482-2eaa-3283-b92a-311af210e79b | -11.66572 | -43.60101 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 342.6 |
| 9522845b-5b7d-3e63-8c65-567aabebab89 | -14.91202 | -39.27325 | 2026-10-02 03:19:00 | NOAA-21 | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c0a0ba2f-38e4-33b5-a953-fc1c58978213 | -11.42561 | -43.40347 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 846962f2-4040-3c68-a237-a4e2b0ddc2b6 | -14.87497 | -40.6971 | 2026-10-02 03:19:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5d17ac31-efab-3935-9444-3a4c2243347b | -11.7623 | -43.55116 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed0169f7-e838-30e4-a8ea-2b2c3a36bd37 | -11.7981 | -43.58221 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c09c5b86-20a5-32ae-94de-15be2009b2ed | -14.33474 | -44.74758 | 2026-10-02 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24d70506-0181-3d28-a6bd-f687c08a8474 | -11.43233 | -43.40486 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e11c9098-c36c-33bf-b7f9-c6bf57c0d9ad | -11.78881 | -43.56942 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 44e3c35c-cc21-3013-a866-57b5a4464010 | -11.78755 | -43.57535 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cbad2be5-d0c2-34e1-9b0f-e20a7097915f | -11.7334 | -43.44173 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9d3288e-3b8d-36b1-80f6-50ece023dbcf | -11.69534 | -43.59417 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 50fe9fd6-68d3-3905-95f8-4045ddf47d10 | -11.65051 | -43.57219 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8765e272-2e1f-3b52-8054-05ad8e871633 | -11.46864 | -43.44501 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 00d90dde-e9fc-3fea-a5d0-b3a89cfa71fa | -13.54964 | -40.07779 | 2026-10-02 03:19:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a993d6fa-797b-3321-85e0-863748fe9ed0 | -15.25421 | -40.22314 | 2026-10-02 03:19:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 83b9b6d5-c731-38e1-88b9-5078197ac94d | -11.75353 | -43.44578 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd6756b7-8050-3406-ba54-63469d56e9e5 | -14.33632 | -44.74055 | 2026-10-02 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6aa2dd5a-ee5f-37e2-95ee-13f605e58342 | -11.69433 | -43.60662 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b9b3f7d1-9e5e-3f31-b1f2-fa2280b4e295 | -14.87424 | -40.70064 | 2026-10-02 03:19:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b54106b0-7923-3e71-a0cb-92acf51fb840 | -11.77949 | -43.58014 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 81e1030e-3b61-3d7c-af50-3792eb0efab8 | -11.73886 | -43.44926 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0e944066-ad66-38c2-9fa8-208e83fe9745 | -11.76319 | -43.58082 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| a91d1485-e16e-35c6-be5c-71ae16d5b2fa | -13.34746 | -43.86102 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a9d90f80-84c1-3665-96a4-7e828b2f0479 | -13.86125 | -43.63188 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84932537-5f4c-3fb0-95e2-f8ae5d7f529f | -11.78496 | -43.57765 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2599dbb6-fa43-3adb-bde1-e323c184ee02 | -12.53066 | -43.09147 | 2026-10-02 03:19:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 51eaf45c-c1ab-3805-876c-44d2e64c2396 | -12.53829 | -43.088 | 2026-10-02 03:19:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3a08c170-53a0-3b64-b19e-a4f4a7964353 | -11.67823 | -43.60883 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 49336ba5-0188-375f-9e9a-6c862d52e40a | -11.68751 | -43.60551 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fe153229-33f6-37f9-89f8-575eee14981e | -11.2587 | -43.52394 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d85d1b6b-55bd-393e-b6dd-341987b6aeb0 | -13.34614 | -43.86732 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a1212c9c-319b-3f15-9f4c-199c35b0e6df | -14.34518 | -44.73455 | 2026-10-02 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3d1c0a6-4792-37f9-aa5b-3e2e2bd986b0 | -11.43906 | -43.40623 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 843384fe-7a7a-3ad3-b537-3eb375866875 | -11.45356 | -43.4161 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c302a9b2-4307-3099-adf8-6b61f8eccb09 | -13.86607 | -43.63434 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2a9e2dd4-608d-3ef9-9935-757520007b75 | -14.87284 | -40.69653 | 2026-10-02 03:19:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c169f6e5-f7f2-360d-be81-edc2e6162e14 | -11.41449 | -43.4017 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e8de8296-f12c-348f-a7b2-d1f4b5555e29 | -11.67382 | -43.60339 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 3846f5ee-8b1e-38cc-b68c-8c56c7e340f6 | -11.78066 | -43.57463 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 18695e1b-b72e-3d7a-a193-046968b38a51 | -11.41219 | -43.40057 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 49b46ddf-b4fa-3960-b904-f6144c66fea9 | -11.66146 | -43.58743 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 41e6cb56-65ff-38da-9af7-1298eae5034d | -11.75622 | -43.58047 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| f5a0f9ad-bfa2-3f60-884b-bb92214ffbc2 | -17.43972 | -41.91409 | 2026-10-02 03:19:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 59d37852-f99e-35cc-a329-dd18d1b5b596 | -11.26549 | -43.56511 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b315981-1f85-3d86-b1e7-b3f869448e78 | -13.33413 | -43.85808 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ab3ad926-a7ef-3769-9707-24ac3cc1175c | -17.70854 | -39.75782 | 2026-10-02 03:19:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 789ef48a-8249-3a35-b047-16fe92c1a1c5 | -11.2642 | -43.57122 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31f4e019-f841-387e-a1ad-8bb3e37f908e | -13.3493 | -43.86619 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3e3da3dd-08a4-3f1a-8fd8-0bb50c8bab5c | -11.72794 | -43.43424 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fb644edd-3052-3067-b2d5-f83ebbb419fd | -17.71333 | -39.75884 | 2026-10-02 03:19:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c33f8191-ed5e-3ecf-ad20-f55aaa9832ec | -3.1483 | -53.7426 | 2026-10-02 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 50cf2298-2b12-3740-b604-55272e135b30 | -11.6771 | -43.587 | 2026-10-02 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.3 |
| a4b27a5a-ce2c-3e6a-b635-ad3c332979b3 | -11.6575 | -43.6136 | 2026-10-02 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 447.2 |
| ec1ac853-10ad-3006-9f2f-f1ba5906f4e0 | -12.9807 | -51.2786 | 2026-10-02 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.7 |
| ea67171b-057c-3edc-857d-9184908f3602 | -12.9998 | -51.2763 | 2026-10-02 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 255.8 |
| 5e41df93-496d-383c-8896-a0b94021f19e | -3.1655 | -54.0844 | 2026-10-02 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 7d780433-7812-307a-a6a8-a33a90058af2 | -3.1299 | -53.7633 | 2026-10-02 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a336c297-f1f1-3e16-bac2-0b508439ac16 | -11.1615 | -44.6002 | 2026-10-02 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 75228702-f00e-374c-8ae6-9cb4a937dd15 | -5.7355 | -43.2916 | 2026-10-02 03:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2c379797-11f4-3735-a65e-9c08cef2ea67 | -5.7563 | -45.152 | 2026-10-02 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 1453399c-bd9e-356f-8c4e-4f1c91dadecd | -3.1838 | -54.104 | 2026-10-02 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 5ee51438-4251-37de-b43b-f04965202ec4 | -2.0394 | -56.8593 | 2026-10-02 03:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 36a0d460-91a9-3db7-9f42-a9d56058958c | -7.4031 | -55.2114 | 2026-10-02 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 8a1325f0-3bf8-3307-a84b-02c562e9b2d0 | -11.1424 | -44.6029 | 2026-10-02 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 4d2c7008-ed49-31c5-a2c2-7c0df1dbd463 | -2.0393 | -56.8789 | 2026-10-02 03:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 54cb5565-7574-34db-8326-a582db7c5808 | -6.914 | -43.6816 | 2026-10-02 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 2eff5a5b-55c3-36fb-9985-97cf686a08cb | -2.0577 | -56.8591 | 2026-10-02 03:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 53d46d77-e031-3444-835e-30d7f854a15a | -3.1839 | -54.0839 | 2026-10-02 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| a7ea0422-133e-3225-87d2-ff920d128dfa | -6.209 | -60.0378 | 2026-10-02 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b49b45da-53e2-3a59-96d4-fad2da6f89cf | -13.019 | -51.2739 | 2026-10-02 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 132.2 |
| da108b6c-5cdf-3401-99d2-c6281579db3d | -7.4188 | -55.5902 | 2026-10-02 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 97fdcfa7-ca99-3ecb-8cbb-7f6efd74eafa | -13.1348 | -51.2169 | 2026-10-02 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 95777f03-c1ac-33cd-a637-a42fce5bcbf8 | -3.2951 | -53.8395 | 2026-10-02 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 9ec25f96-5a2f-30f5-ac3d-f3aca4d180b5 | -4.2676 | -50.7506 | 2026-10-02 03:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 3fbc560b-b9e0-3686-8668-b50441438876 | -3.295 | -53.8597 | 2026-10-02 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 58483225-014a-32f3-8ab6-269769b23d97 | -4.4507 | -47.9112 | 2026-10-02 03:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e259fcbb-fa33-3189-a824-6297bf505bdf | -11.6583 | -43.5662 | 2026-10-02 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 25ab9204-5482-3996-8ce4-f963337a395f | -3.1299 | -53.7431 | 2026-10-02 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 8328796c-9217-3d72-a9b6-d4a9d963944a | -7.7364 | -49.2082 | 2026-10-02 03:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 2ab59fd8-1992-35d6-9adc-30d90e0769a4 | -2.0576 | -56.8786 | 2026-10-02 03:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| aea7fff9-768f-330d-8324-8a9bd02a08b3 | -11.6767 | -43.6106 | 2026-10-02 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 8f08c424-5bff-3b2e-80c6-1629f7ef12b3 | -6.3952 | -56.4158 | 2026-10-02 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b647198e-34f8-3c0c-ba53-09f3eb722243 | -12.9803 | -51.3 | 2026-10-02 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 79c0b17d-7998-3688-8f50-d485e4b5d691 | -13.0187 | -51.2953 | 2026-10-02 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 164.1 |
| cc41ea30-4eca-3eb7-a672-97db20e9c760 | -11.6579 | -43.5899 | 2026-10-02 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 790.8 |
| aa826435-31b5-39da-8795-7b612a7355c3 | -12.9995 | -51.2976 | 2026-10-02 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 244.2 |
| b25aa94a-0902-3d9c-9a95-420744388875 | -11.142 | -44.6261 | 2026-10-02 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 48302383-565f-3680-aac5-c0394ff972ee | -7.3846 | -55.2124 | 2026-10-02 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ae26bc87-14cb-3fe7-9f64-dd0829f6c9b1 | -4.4506 | -47.9329 | 2026-10-02 03:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a2aef846-ab4b-306b-8525-bdb24c90e3a8 | -3.2767 | -53.84 | 2026-10-02 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 57fc13f0-522f-3aad-9255-9d73d61f562f | -11.1611 | -44.6234 | 2026-10-02 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 9f7ffc82-8d54-3a64-898d-e416704c5383 | -18.95004 | -41.0115 | 2026-10-02 03:21:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5b8fc9eb-a59a-36f8-944b-60b626e55ab9 | -18.95071 | -41.00822 | 2026-10-02 03:21:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
