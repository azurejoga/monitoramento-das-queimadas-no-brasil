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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9baee7ce-c63e-315d-b5db-c1160b1e59a6 | -19.23989 | -43.36995 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 49820bf1-924b-3f0f-ac40-f9ae8c428fe3 | -19.23932 | -43.37371 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68fbd03f-3346-3673-81ad-b5329913aa3b | -19.23875 | -43.37748 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7633b50-e4c9-3ff5-b0c4-31850da17258 | -19.23819 | -43.38117 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a123c2c8-c9cf-3446-8716-4a819783e3ec | -19.23764 | -43.38482 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d6e58aa-aa97-3a5d-be66-511c68f4dbd8 | -19.23599 | -43.3731 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21887321-380e-3094-96f8-f01a0ce047ae | -19.23542 | -43.37685 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3f672e5-2758-3ef0-a593-f4b86804c3df | -19.23486 | -43.38057 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08942a75-8221-3b45-9446-21eba3309002 | -19.2343 | -43.38425 | 2024-10-04 04:12:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5070c791-8e0f-344b-827a-594bca9807de | -19.17675 | -43.51597 | 2024-10-04 04:12:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db064828-1cf5-32b8-b708-d863c59748d0 | -18.59167 | -43.96167 | 2024-10-04 04:12:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bd35330-9c62-39d2-a100-033e5254ddc6 | -18.58892 | -43.95751 | 2024-10-04 04:12:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a52efe47-62f3-34d4-994e-a8327da45fc9 | -18.58836 | -43.96112 | 2024-10-04 04:12:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cc6519f-9b12-33de-956c-1e3d755f464f | -18.58561 | -43.95695 | 2024-10-04 04:12:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bff28a62-ff65-3727-82a9-db2c7066b8d5 | -18.58231 | -43.9564 | 2024-10-04 04:12:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db63b368-1a8e-3a19-a201-6061e90dc689 | -18.58393 | -43.96777 | 2024-10-04 04:12:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 442e9a64-4980-31b3-9495-05e03f9122df | -18.72218 | -43.28464 | 2024-10-04 04:12:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 851d7b9b-bab6-3c30-b979-7735802132c6 | -18.86607 | -43.59274 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| df45220a-b577-3fc0-9020-8c99b4750979 | -18.86282 | -43.5694 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1447c1af-42bc-331d-8b1a-5de1241152dd | -18.86274 | -43.59225 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 9d7d4f53-d231-369f-a2ed-ce870712a348 | -18.86225 | -43.57315 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| bc4e2f24-aecc-34f1-8951-3e50a7c4ddd2 | -18.86217 | -43.59592 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| ca7938a0-101f-3a76-8354-07cf0430db01 | -18.8595 | -43.5688 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3a7a5187-bf4b-3522-a4af-5e650316feaf | -18.85942 | -43.5917 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7e77a0a6-131d-3157-acf2-8d0b340aa68f | -18.85885 | -43.59538 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5e2461d5-f025-3a18-8188-bcf7c643a988 | -18.85829 | -43.59903 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| d6c788e7-c3bb-35c1-976b-06ba3931e3bf | -18.85774 | -43.60268 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 346ac545-215d-3da2-bdda-b13ac6e673c6 | -18.85718 | -43.6063 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a9bb6a66-67b0-31e4-a7bf-f64d6529efa2 | -18.85666 | -43.58744 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8e17ef9e-2c83-379c-b72a-b8df401df22b | -18.85562 | -43.57191 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bcfb51d7-dad4-39c2-8eb1-f8045b8d1ed1 | -18.85553 | -43.59483 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 704065ac-2fd8-3716-9390-6b609af07eb6 | -18.85505 | -43.57565 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fca44265-33f4-3469-bf4c-e98e5ef23733 | -18.85497 | -43.5985 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 779fff3c-317b-39bc-957e-7b88a8865f30 | -18.85448 | -43.57939 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 04d8e05a-c6c9-3108-90e4-3b7477cec129 | -18.85441 | -43.60215 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 3338246f-84e9-328e-8036-74fd38140e29 | -18.85391 | -43.58311 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 92be0415-d0ec-30a4-85e6-2c12485f949b | -18.85386 | -43.60577 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 891023d8-2617-3e84-90a7-46958a6651cb | -18.85335 | -43.58685 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6b7e1a78-3798-3ed6-b32e-c01121382e40 | -18.85287 | -43.56758 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3f09e218-d0ac-387f-9cd7-f2ec2d00dc8d | -18.85278 | -43.59055 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 67522869-4c4b-35fb-8aec-ce81c479184d | -18.85231 | -43.57129 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 80e29def-b5e9-3947-8272-c5ef298e6974 | -18.85221 | -43.59425 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0ecdf135-e8f9-348c-9e9e-3460a1c49df7 | -18.85174 | -43.57502 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 78351c05-bcbc-3539-8691-6f08ee8c0b76 | -18.85117 | -43.57876 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9c993076-e94d-37a8-9a2b-c9f084d30b4c | -18.8506 | -43.58249 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fe31d0b9-450d-3c44-b4de-f4a0d082a0ec | -18.849 | -43.57067 | 2024-10-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ea5b4b0f-a87c-37ae-8e77-beb52be03ad6 | -18.845 | -43.61917 | 2024-10-04 04:12:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e348704e-6fe3-30d7-925c-e7a3669822c8 | -18.84167 | -43.61868 | 2024-10-04 04:12:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 96473c19-d4b2-3692-b351-7733deaed2f5 | -18.84111 | -43.62235 | 2024-10-04 04:12:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0ab2e18d-7501-34b9-a4ce-39dd457685e8 | -18.83834 | -43.61819 | 2024-10-04 04:12:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4e759c9a-0e4e-3f61-ab7e-a61a086a21f5 | -18.83778 | -43.62185 | 2024-10-04 04:12:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 52df65ba-45fd-3d96-95e2-8605c3643d02 | -20.52406 | -44.89541 | 2024-10-04 04:12:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ea16fc50-169a-3be3-a4d7-ebcccf7a8076 | -20.52349 | -44.89907 | 2024-10-04 04:12:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b5c18c6a-c96d-37b2-b396-0fc9054006af | -20.52076 | -44.89482 | 2024-10-04 04:12:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| aa8ea322-baca-3966-8514-8dbfb7cb4ae2 | -20.52019 | -44.89849 | 2024-10-04 04:12:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9de3552c-fb6a-34c0-b8f7-c0f147cf9024 | -20.51961 | -44.90215 | 2024-10-04 04:12:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bcc5b801-1464-38b8-acae-9b8b48a8f7c8 | -20.51903 | -44.90581 | 2024-10-04 04:12:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 32ad2a30-dd80-3141-984a-8f5a8863354b | -20.51631 | -44.90157 | 2024-10-04 04:12:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7c63ce06-5d56-36cf-9981-61806fa66cf9 | -20.42824 | -43.77545 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 164a8fb8-1e1c-3935-bdce-f9463f1c9c19 | -20.42715 | -43.76002 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 430879b8-82c3-3d15-a0a9-30a23c016b1d | -20.42491 | -43.77485 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5704b0b5-2883-34a7-83a5-598fdd3ffd52 | -20.4227 | -43.76688 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a0eee55-763d-3b99-98bf-ecd35c5e6fa0 | -20.42159 | -43.77426 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6ff92a14-bc22-3b60-9f83-1c8cb25e90e7 | -20.41769 | -43.7774 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| be617cdf-ab01-34be-a389-f8d7b901395b | -20.34792 | -43.88073 | 2024-10-04 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0e6676d0-2a8d-386d-b244-d676a4f80026 | -20.29151 | -43.60391 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fc24d398-7a21-35b0-9da7-3e9fb2c5c8af | -20.28704 | -43.61081 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e05ec3ce-f9b1-325c-b056-3ee27ee3ebb9 | -20.28428 | -43.60649 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1eb35ad5-0969-312d-b1a4-fa651ef8cbda | -20.28371 | -43.61023 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b7d41ea6-0918-39d1-8486-16ac98871e7a | -20.27922 | -44.10754 | 2024-10-04 04:12:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f87a4b99-410b-3e50-a77e-bf9a36ec83cb | -20.27591 | -44.10697 | 2024-10-04 04:12:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 82aa5cc1-b5af-3b35-bc84-ab4a609aa35a | -20.35401 | -43.88554 | 2024-10-04 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 14c6fc7d-d288-3af3-b921-738bbbe14cbb | -20.34849 | -43.87701 | 2024-10-04 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 34015e0a-ba1a-338d-a74d-a8ea525d8d3e | -19.87331 | -44.4033 | 2024-10-04 04:12:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 469dd386-2f70-3aec-9df2-c38ceff0ab6f | -19.83783 | -44.23628 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad380a89-2ecb-310d-b94c-8a96d873506c | -19.83235 | -44.22781 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4267c3f7-fedc-33b9-b545-88105c157604 | -19.6256 | -44.11369 | 2024-10-04 04:12:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0deac112-6cf1-3545-9a00-ea43d5514a16 | -19.56448 | -44.24566 | 2024-10-04 04:12:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9ca7635-3534-33da-930f-85ba42e5bb67 | -19.54066 | -43.89262 | 2024-10-04 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cd0a040-c7b2-3775-bc44-297a78786257 | -19.87662 | -44.40388 | 2024-10-04 04:12:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fc54cb3-9e93-3007-b290-43c5701a717d | -19.87275 | -44.40694 | 2024-10-04 04:12:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c35969b9-adc1-3b26-acf5-b3d9ee095dee | -19.83896 | -44.22897 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dcd4c29e-94a8-3546-ac9e-50da0a4c95df | -19.8145 | -43.76889 | 2024-10-04 04:12:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea1772ee-5b49-3d72-9f56-584e04857818 | -19.80363 | -43.6382 | 2024-10-04 04:12:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9fe6e66-d58e-3afc-81e7-3a8cf6196764 | -19.80306 | -43.64193 | 2024-10-04 04:12:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f31e8ac-5e78-3f9c-b4af-a5d87848c2e4 | -19.76141 | -43.69157 | 2024-10-04 04:12:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ed9aaa9-67bb-30cd-a716-8a06e616a1e3 | -19.75813 | -44.26793 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0040a441-6a42-3a78-b614-d39f4ce9fcfb | -19.75038 | -44.27409 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74fe08f5-ca98-3a5d-903a-f2708961d302 | -19.74708 | -44.27351 | 2024-10-04 04:12:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdb8dd17-b8eb-3141-88a0-b1a17bc3d585 | -20.14644 | -43.84283 | 2024-10-04 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| aac2a6bf-d2fc-30fa-acee-63d93ee53209 | -20.14304 | -43.86511 | 2024-10-04 04:12:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 67cdef70-746b-331c-8dca-74fa4ce24307 | -20.13704 | -43.83743 | 2024-10-04 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3a4efa46-3e91-3f23-b3e0-443ad164fee5 | -20.13315 | -43.84054 | 2024-10-04 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b63b9596-340d-3d56-b298-e3b42611bd2c | -20.02019 | -44.50725 | 2024-10-04 04:12:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 85eb9048-26d8-3dfa-a22b-f93970d8ca9e | -19.9622 | -44.09171 | 2024-10-04 04:12:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 00163ec5-cb22-315d-9e9b-7a6dd65dd6d4 | -19.95889 | -44.09114 | 2024-10-04 04:12:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3401f4f-e283-35df-a620-0d47e1a6bbbc | -20.58113 | -44.57413 | 2024-10-04 04:12:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| faa20d8e-30d9-3c6b-8979-9adba2b17c84 | -20.57783 | -44.57355 | 2024-10-04 04:12:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1113f06f-5c6d-3e36-a8b8-906378c95cd8 | -20.42659 | -43.76374 | 2024-10-04 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 37c33deb-6442-3824-9a24-5b01dad7307f | -20.35181 | -43.8776 | 2024-10-04 04:12:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README88.md)
