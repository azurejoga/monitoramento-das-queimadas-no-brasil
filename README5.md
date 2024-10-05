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
| 94a7b2ec-9810-38d0-9e5d-ed5e5a97ef59 | -19.4811 | -42.8969 | 2024-10-05 00:20:02 | METOP-C | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c58dc90a-809d-316e-bf6f-acc4460991e1 | -19.236 | -43.353901 | 2024-10-05 00:20:08 | METOP-C | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 86f94cba-a17a-3451-a895-92e977234d11 | -19.2379 | -43.3633 | 2024-10-05 00:20:08 | METOP-C | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 43a2a7e9-3f6a-307f-bac9-7d88a37b4ca3 | -20.5714 | -51.343201 | 2024-10-05 00:20:09 | METOP-C | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2c1ea2a-44ac-3d14-b240-46cbaf25674f | -20.5763 | -51.375198 | 2024-10-05 00:20:09 | METOP-C | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 295fcf32-0cdc-30d9-b82b-36fff36b9507 | -20.5618 | -51.344799 | 2024-10-05 00:20:09 | METOP-C | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47666174-1fb4-3024-8711-8bdf9b789dc0 | -20.5667 | -51.376801 | 2024-10-05 00:20:09 | METOP-C | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1862577e-b771-301e-b119-d12bbfdc26d1 | -19.7439 | -46.663502 | 2024-10-05 00:20:10 | METOP-C | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c739f2d7-4df9-33d4-9045-d52a64609c1f | -19.026899 | -43.176399 | 2024-10-05 00:20:11 | METOP-C | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2c6235d-0f2b-38ab-a540-6c8d3ee94dcd | -19.015301 | -43.169399 | 2024-10-05 00:20:11 | METOP-C | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| addb6d03-7983-3ed9-b837-8cb4294f012a | -19.017099 | -43.178501 | 2024-10-05 00:20:11 | METOP-C | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 44b11589-03a0-3578-9d20-d7d46084df1b | -18.8734 | -43.580601 | 2024-10-05 00:20:15 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 81a0b395-b303-3c7d-9d08-d2c4d321c211 | -18.875299 | -43.590199 | 2024-10-05 00:20:15 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2db0623-d10f-3563-bc1e-7b1a2ad5b344 | -18.877199 | -43.599701 | 2024-10-05 00:20:15 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ba4969d-683b-34d0-b139-1f17b507aee9 | -18.8636 | -43.582699 | 2024-10-05 00:20:15 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e948f74-dbca-3ab8-a7c2-9f4a57a3e4c3 | -18.865499 | -43.5923 | 2024-10-05 00:20:15 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5c4f676c-6a51-359f-bb2a-a0c6a9998b85 | -18.867399 | -43.601799 | 2024-10-05 00:20:15 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a558098-e638-3034-9da6-6393ed4b9302 | -18.857599 | -43.603901 | 2024-10-05 00:20:15 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 48e7fb35-934f-3974-895a-e512fa58353d | -18.8596 | -43.613499 | 2024-10-05 00:20:15 | METOP-C | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3d8f6c6d-3555-3225-815a-d8782d420126 | -18.834299 | -43.589001 | 2024-10-05 00:20:15 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c5d337f5-990d-3faa-9660-510602387862 | -18.836201 | -43.598598 | 2024-10-05 00:20:15 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dcaaec55-e38c-3e0c-baea-35486f28af60 | -18.5219 | -42.2575 | 2024-10-05 00:20:16 | METOP-C | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3704c647-d39f-3537-b2d5-103977f58b36 | -18.5553 | -42.616901 | 2024-10-05 00:20:17 | METOP-C | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 64c10f29-5866-377b-92a5-bc45eda42ac0 | -18.5571 | -42.625401 | 2024-10-05 00:20:17 | METOP-C | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11666a31-f7c5-3a9c-bdc0-06fec3739096 | -18.6315 | -43.1394 | 2024-10-05 00:20:17 | METOP-C | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8bffd3e6-d5aa-3602-80f8-9a1dbce6e0df | -18.292299 | -42.138599 | 2024-10-05 00:20:19 | METOP-C | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5aca9741-f49d-3518-8e5e-94c9204d48f7 | -18.294001 | -42.146702 | 2024-10-05 00:20:19 | METOP-C | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8f24550-9d81-3027-92a0-a0b0346a1c27 | -18.214399 | -42.7995 | 2024-10-05 00:20:23 | METOP-C | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a48dab60-8621-303d-a41d-b04cb6ddb140 | -18.2162 | -42.808102 | 2024-10-05 00:20:23 | METOP-C | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d0a3673-e433-3875-92fa-724a107075cc | -18.178699 | -42.5769 | 2024-10-05 00:20:23 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 336ae426-8651-33d7-8a3d-f28022bdc0ca | -18.180401 | -42.5853 | 2024-10-05 00:20:23 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d389ddb-30f6-3b92-82e1-38e86c21dade | -17.9363 | -41.472801 | 2024-10-05 00:20:23 | METOP-C | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab1e74f9-526e-3496-866e-c75da9b60af1 | -17.937901 | -41.4804 | 2024-10-05 00:20:23 | METOP-C | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a87e27f-72cd-369e-b9bb-f811a3409ee5 | -19.132799 | -48.207802 | 2024-10-05 00:20:25 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| effd42d0-db51-3169-94cb-3f63f0c144b7 | -19.136101 | -48.226601 | 2024-10-05 00:20:25 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3ba17a2a-ab8a-377e-9b88-ef63280bd1c3 | -19.1231 | -48.209702 | 2024-10-05 00:20:25 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fca88b03-9d4a-385e-ba12-225046fccfda | -19.0875 | -48.235699 | 2024-10-05 00:20:25 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fa782502-4630-3ff0-b727-842f4675d7f4 | -17.4522 | -40.0518 | 2024-10-05 00:20:26 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f19c611c-ed73-3baf-9e38-e8df36a0c8a0 | -17.4538 | -40.058998 | 2024-10-05 00:20:26 | METOP-C | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eb3d2b5a-5877-3201-839d-7469485ab624 | -17.4554 | -40.0662 | 2024-10-05 00:20:26 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9a57e72-e521-3589-82d1-09fa9aefbb11 | -17.7882 | -42.226501 | 2024-10-05 00:20:28 | METOP-C | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e28b2e05-e744-31df-ba2e-0bf8304dde28 | -17.8708 | -42.671501 | 2024-10-05 00:20:28 | METOP-C | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 65093d4e-a68d-31ee-8fde-c83a89671c76 | -17.872601 | -42.679901 | 2024-10-05 00:20:28 | METOP-C | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11c5d86c-444a-34ab-b99a-267bf29e2011 | -17.8743 | -42.688301 | 2024-10-05 00:20:28 | METOP-C | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85fcbc60-a197-38ef-941d-3914b5aa3d64 | -17.675699 | -42.6189 | 2024-10-05 00:20:31 | METOP-C | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d817d30b-72c9-30db-9009-40a54468f099 | -17.677401 | -42.627201 | 2024-10-05 00:20:31 | METOP-C | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09ae5d8c-b6ea-3a0c-8ef7-6f0fd010cfeb | -17.7372 | -43.815399 | 2024-10-05 00:20:34 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ab9c7d3c-c719-3ba1-9910-e1016e63a16e | -17.7391 | -43.824799 | 2024-10-05 00:20:34 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 582bb9f3-ee48-303b-9c5b-a65d83bc9c2f | -17.740999 | -43.834301 | 2024-10-05 00:20:34 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5cea54c6-157e-3755-8600-c405383c5bfd | -18.0867 | -45.588501 | 2024-10-05 00:20:34 | METOP-C | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8e7effb0-fbfa-3b08-9f38-4c1a7e6b8b2c | -18.089001 | -45.6007 | 2024-10-05 00:20:34 | METOP-C | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e3555566-3f8d-35fc-bc96-ce54dcdd8142 | -17.6119 | -43.250301 | 2024-10-05 00:20:34 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3393eef5-add6-3c50-ac09-0af98a91ffa2 | -17.613701 | -43.259201 | 2024-10-05 00:20:34 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 78c6943b-0568-3268-86b5-42d3734fc61b | -17.615499 | -43.268002 | 2024-10-05 00:20:34 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4b7a8f91-c43a-3bbd-b3a1-510a4385e15a | -17.690399 | -43.7859 | 2024-10-05 00:20:35 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b4edd5f8-ba9a-35c5-8522-4a332d99a5ad | -17.692301 | -43.795399 | 2024-10-05 00:20:35 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf23ce03-4cef-3d4a-9c08-d0ad55ae22d0 | -17.612301 | -44.310001 | 2024-10-05 00:20:38 | METOP-C | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d7e2a61e-fbef-3230-bfc5-ac9a88eeeb88 | -17.6143 | -44.320099 | 2024-10-05 00:20:38 | METOP-C | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 33e6d290-59f8-39aa-80a7-31ac03cece3c | -16.993099 | -45.812199 | 2024-10-05 00:20:53 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fe3459ac-e8e9-335d-a07d-1be90fd0bf08 | -16.995501 | -45.824402 | 2024-10-05 00:20:53 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| df70b73e-3fcc-36c8-8f70-4a242e33a398 | -15.2487 | -40.3769 | 2024-10-05 00:21:02 | METOP-C | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69b2ddd5-b3b0-3438-96ba-37c49160b946 | -15.2502 | -40.383999 | 2024-10-05 00:21:02 | METOP-C | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6121fdbc-041c-3ea0-8e98-8c595001bcd6 | -16.344 | -45.662701 | 2024-10-05 00:21:03 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8079e7f9-0a04-3c42-b4c2-899701c6aa85 | -16.3463 | -45.674198 | 2024-10-05 00:21:03 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2cf67d0c-eef4-3975-85ae-d93647061fb8 | -15.7487 | -43.832001 | 2024-10-05 00:21:06 | METOP-C | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| ec9a3390-2608-3381-be29-158fccec1593 | -15.7505 | -43.8409 | 2024-10-05 00:21:06 | METOP-C | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 20ae6c90-3df8-3a6b-a639-bf2728a4b942 | -15.7182 | -44.827099 | 2024-10-05 00:21:10 | METOP-C | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ec904018-2198-3b8f-b04b-b40ed7751b7c | -16.104401 | -47.9403 | 2024-10-05 00:21:14 | METOP-C | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c552578-0813-3ac8-af3d-6cf077006d7b | -15.7781 | -48.190701 | 2024-10-05 00:21:20 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 79f6ad65-0e19-3bbd-a37f-8cb390a96abe | -15.7812 | -48.207401 | 2024-10-05 00:21:20 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| b94835f6-36f0-30a2-bb51-031f120844d2 | -15.7715 | -48.209202 | 2024-10-05 00:21:20 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 87badb08-8f89-359e-b84c-d624496ef546 | -16.091801 | -50.2295 | 2024-10-05 00:21:21 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb2b96f-d822-3373-ad0d-d9d3bfaf14d7 | -15.3998 | -47.689301 | 2024-10-05 00:21:25 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0569fd71-0b03-3a9e-aa97-ab5c40c70452 | -15.4027 | -47.704399 | 2024-10-05 00:21:25 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 820d66e6-0273-3e84-92a0-3eb51b436c5d | -14.863 | -45.134899 | 2024-10-05 00:21:25 | METOP-C | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e4ed7eea-ef55-3204-8abd-835f12a3914c | -15.167 | -48.0574 | 2024-10-05 00:21:30 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 947e03dd-1a9b-31cb-ae05-f97387c1f3fd | -13.9342 | -42.3876 | 2024-10-05 00:21:31 | METOP-C | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 00ff5c10-dff5-3540-9f1b-8615e132dfdb | -13.9358 | -42.3951 | 2024-10-05 00:21:31 | METOP-C | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c36f003e-1b0e-36b2-be46-7da2af50a8b2 | -13.9374 | -42.402599 | 2024-10-05 00:21:31 | METOP-C | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 05d3e5b3-b245-3b3e-85ed-ac71d02fac2f | -14.0647 | -43.950298 | 2024-10-05 00:21:34 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f6626b01-b25c-3479-bd90-b3017dac3534 | -13.9894 | -44.0299 | 2024-10-05 00:21:36 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 815222e4-5959-3b9b-a931-50126f78054c | -13.9875 | -44.021198 | 2024-10-05 00:21:36 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4e2e58a4-f702-3efe-89aa-0380c66fd575 | -14.7689 | -48.037701 | 2024-10-05 00:21:36 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1ab8157-8c5d-363f-bb0c-e02dffe63cb8 | -14.7562 | -48.024101 | 2024-10-05 00:21:36 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 873332b7-ea98-3f63-a70d-5ac65b5d19ed | -14.7592 | -48.0397 | 2024-10-05 00:21:36 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4c4d2dfb-4024-3083-829c-7f27b933c571 | -14.9698 | -49.308201 | 2024-10-05 00:21:37 | METOP-C | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1ac686cc-723c-3708-b0bc-9bca0696b1d3 | -14.9601 | -49.310101 | 2024-10-05 00:21:37 | METOP-C | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 91af732f-e62f-331b-ab2c-25e052e63ff3 | -13.4478 | -42.418999 | 2024-10-05 00:21:39 | METOP-C | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ef187d1a-db67-392a-98c3-5441a5c72e30 | -13.4494 | -42.426399 | 2024-10-05 00:21:39 | METOP-C | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bdf14963-7369-37ac-a9d1-d4f3bb9053e0 | -14.1949 | -46.462101 | 2024-10-05 00:21:41 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c87960de-6bbf-3929-9a44-a26a791595e2 | -14.1973 | -46.474201 | 2024-10-05 00:21:41 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a8e95f70-a12b-3b9a-b7bd-af9e426de5e1 | -14.1875 | -46.4762 | 2024-10-05 00:21:41 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4522a44b-ce9d-33c8-813e-4263e6352fd8 | -13.6641 | -44.283199 | 2024-10-05 00:21:42 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 144d4cb0-b2c7-3d1b-9ea5-a0289065cabd | -14.5612 | -48.7985 | 2024-10-05 00:21:42 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7d0c1dee-26e7-38ee-8082-27277fa1d597 | -14.5515 | -48.8004 | 2024-10-05 00:21:42 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c1287518-efb9-363f-9752-5e9655dcc77d | -12.7153 | -40.206001 | 2024-10-05 00:21:43 | METOP-C | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 41db3657-23a3-3728-82df-f367d464bf21 | -12.7169 | -40.213001 | 2024-10-05 00:21:43 | METOP-C | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a543da6e-f34a-3606-87bf-bdce76304ab1 | -14.0414 | -46.357101 | 2024-10-05 00:21:43 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c922d0e7-ce37-3a5c-8c52-8893f490bbb8 | -14.0438 | -46.3689 | 2024-10-05 00:21:43 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d781c415-b638-39c3-ad0c-faaa3fbca1b9 | -14.0317 | -46.3592 | 2024-10-05 00:21:43 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
