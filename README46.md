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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1cb9f78-0beb-338c-89cf-4e99379a79cf | -19.88121 | -45.83273 | 2025-10-25 04:21:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3cdfa7d-38fd-3234-9195-f0a5766ececb | -15.31164 | -48.07508 | 2025-10-25 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96c108dd-a875-3ce3-99ad-b11d80302e36 | -14.86214 | -48.08969 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 24d0aa27-63d2-3a54-a96a-2041c5d2c816 | -15.30827 | -48.07452 | 2025-10-25 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e006f87-f7a5-3d59-9d74-911178950f5f | -19.65243 | -44.90445 | 2025-10-25 04:21:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 43e4ad7f-366c-3856-b65f-4a91b9530991 | -17.38167 | -45.49681 | 2025-10-25 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 873433f9-b89b-3522-b3b8-9f96922362ee | -15.22985 | -47.93171 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 65056c86-a6af-34e2-b8a3-e3fca000d3b5 | -14.52126 | -48.34985 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a2d443b-105d-362e-9955-eeb78dc8dbe2 | -19.87293 | -48.31997 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f341db9-bd7f-3581-b941-7cd19c034712 | -15.82938 | -49.0947 | 2025-10-25 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 904e8212-4e0f-39d2-a63c-88eacc0548d0 | -18.48446 | -50.42809 | 2025-10-25 04:21:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 98ced040-c82d-3d80-b982-5792effac017 | -15.01423 | -46.20445 | 2025-10-25 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dce4b82-8dff-33f6-b720-eb20c7907cbe | -14.20046 | -47.30527 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d374114c-c0d6-3899-a910-dbd740a78c20 | -21.05125 | -47.33055 | 2025-10-25 04:21:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3b43f8f-35ee-33b2-9eb0-22725df5e743 | -14.9361 | -48.13332 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 042db714-7222-39b8-b143-710cd39a6db3 | -18.85439 | -46.85503 | 2025-10-25 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c36e764f-059d-3565-9b4a-acdf36d18550 | -14.92998 | -48.12824 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9751607d-a783-3a73-9e62-5e5678f93384 | -14.86275 | -48.08595 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 560ae943-3967-33c2-a01f-0a3006f0452c | -16.94457 | -44.48523 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e09806f5-5f6b-3955-bc32-af0f03e9aa7c | -18.5541 | -50.27407 | 2025-10-25 04:21:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b6b44d70-af08-31f7-a679-fef56a6e4297 | -14.41321 | -47.91896 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f908c7c8-c065-3503-9318-2c8a7e37848f | -14.89491 | -47.86721 | 2025-10-25 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0d82b4b-8143-3916-8ee2-a147ee3bcbeb | -17.41738 | -46.88229 | 2025-10-25 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e8c2ea6c-4564-341d-80cd-30fcb227aeba | -14.89517 | -52.45197 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fdc78df-3c0a-31ef-87ba-c22333c795fe | -15.5348 | -45.69307 | 2025-10-25 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db1aad0f-3f15-3f52-8191-941a08b908b9 | -14.55858 | -54.17525 | 2025-10-25 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2086b50-051f-356a-bf99-7cb49349fc38 | -17.37886 | -45.49244 | 2025-10-25 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e829670-5dd4-366a-af80-d20e58eeaf0f | -20.43876 | -46.58073 | 2025-10-25 04:21:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0c5f2bb-3c37-3ef9-bcef-adfc5194e646 | -15.9575 | -50.16476 | 2025-10-25 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9d8cdf9-305f-3da2-95e4-5d52e9df01be | -14.86275 | -48.09354 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2386d76b-845d-3ae6-9b6d-fb8f4fac3e10 | -19.83626 | -46.13361 | 2025-10-25 04:21:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 054e68ae-02a1-3f26-b238-9846203d2d02 | -15.5758 | -43.22379 | 2025-10-25 04:21:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b2aea9d-5c54-3c0d-a7a7-7d7074a97699 | -19.7611 | -48.29601 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0ea1e941-8cc0-374f-8482-e3c7e194f724 | -17.55008 | -43.79054 | 2025-10-25 04:21:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 640a25e1-1e04-3f09-804e-eff6bef57f56 | -14.52189 | -47.94147 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adaeab2e-c354-37fc-b6e3-7bdc5e88b48d | -14.37958 | -51.51946 | 2025-10-25 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 236d895f-1c6f-3019-9e7e-05e5e4743f1a | -18.56188 | -50.27127 | 2025-10-25 04:21:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5a3ffaf1-be62-3161-9895-e0bbee487ee8 | -21.09781 | -49.24879 | 2025-10-25 04:21:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b207eeca-f203-35d6-80d7-230585bfc9db | -14.81132 | -46.75842 | 2025-10-25 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 004cb4f5-5c4b-3874-adeb-12868fc0c199 | -15.23932 | -47.93711 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d3b69a74-9aed-3479-8ceb-477cdcec8900 | -19.8778 | -45.83216 | 2025-10-25 04:21:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf13d33b-d298-3306-b710-89a77147ac39 | -17.47166 | -44.79015 | 2025-10-25 04:21:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ae90565-6081-373e-bd0a-e0c4fe6b8fdd | -18.56398 | -50.28023 | 2025-10-25 04:21:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| eb300015-dd6c-3af0-83cf-0ad46d4a9a4a | -14.52403 | -48.35429 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e19fef89-5f44-3d74-9dba-9e83df93d459 | -15.4721 | -50.46837 | 2025-10-25 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 35917899-9bcb-371d-b0cc-70de2a47d5be | -15.93896 | -56.11285 | 2025-10-25 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8e4e8339-c730-3b80-ae88-830e60d8ec60 | -17.46918 | -48.40199 | 2025-10-25 04:21:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94a3288e-d891-33bd-bc29-8e35d782a459 | -14.92181 | -52.44938 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bc42c71-1a28-3073-bffb-514824c9d33f | -15.32019 | -52.99542 | 2025-10-25 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 377ab450-2d4a-34a6-883a-174ac19c77ff | -16.22004 | -46.4839 | 2025-10-25 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 95d28ee9-1b5a-3bae-97f0-d38704ef9bb9 | -14.47692 | -47.89882 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb27e109-424c-3860-b361-749db028cbc3 | -16.94595 | -44.48468 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a57651c-832a-35c4-b220-2c22a6cccbe4 | -14.8769 | -48.09203 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 7285f5ef-ccd2-3f30-9c56-800724400afb | -14.52528 | -47.94195 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 247933b2-fd90-32ff-aacc-69cbf5614808 | -15.21767 | -47.9219 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2493dc09-f399-3060-a8d2-553b4f221bd2 | -15.58435 | -43.21614 | 2025-10-25 04:21:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db4786b9-b0bf-31ee-970e-3434ff815361 | -14.65335 | -50.18969 | 2025-10-25 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88da565c-56e6-3882-8d52-a35f1a139209 | -19.32878 | -49.08954 | 2025-10-25 04:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6464a7d-3177-3cad-94b2-814bc1247ff2 | -13.87261 | -48.38595 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d2be292-51b2-3f8e-ab80-3effa5f12546 | -14.43495 | -48.0681 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7005813c-f13c-327d-add4-f76354b7ed73 | -21.05068 | -47.33426 | 2025-10-25 04:21:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1667b631-6016-3fec-99fa-2dd88aed6a67 | -15.27146 | -50.76639 | 2025-10-25 04:21:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90d269d3-abdc-32f0-b9a1-578104c2b222 | -16.17373 | -45.08124 | 2025-10-25 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94825060-5151-3319-b58d-1dee2ab66c8f | -15.23993 | -47.93342 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 279aced0-1585-3197-b954-0516a9630b71 | -15.93374 | -56.11168 | 2025-10-25 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8c86ac91-dc53-34ca-ad68-763767a61b9f | -19.04887 | -54.01664 | 2025-10-25 04:21:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c470b8c-fc5d-3289-8a4b-7f3d9fa11e51 | -13.88414 | -49.05042 | 2025-10-25 04:21:00 | NOAA-20 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 849220f1-31e2-3013-845e-9367432cdab0 | -19.26565 | -45.83488 | 2025-10-25 04:21:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5f233e3-0381-3fd5-9914-cccc1f9a56c3 | -14.40024 | -51.51971 | 2025-10-25 04:21:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d72ca6ae-8ffd-30a4-82e1-e037151dc118 | -13.89007 | -48.40849 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee563cf7-8969-3699-a6c2-1220bbfc920b | -19.62903 | -44.76345 | 2025-10-25 04:21:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0769aa7e-b2f5-374e-b57c-925455ac7a29 | -15.53312 | -45.70396 | 2025-10-25 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91382be0-568e-3007-a12d-6f81bc47d8de | -15.52923 | -45.70706 | 2025-10-25 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff7bcd0b-e0cb-3d11-b8bb-26fa3c042626 | -14.20321 | -47.30946 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a7ffcf2-822b-33b8-81d9-bbae3ca4db5a | -14.17754 | -47.32011 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af3e5620-aece-3b1b-982b-f991ba769bc3 | -15.84122 | -49.10909 | 2025-10-25 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 565043a2-5695-3f87-b661-928ae59eb54d | -14.93334 | -48.12891 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4705fb5-d049-32a4-98ca-28c3021d9fe6 | -19.15546 | -49.12101 | 2025-10-25 04:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07725a2c-d824-3bc5-9a0a-820244ca68ae | -14.8917 | -52.44719 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 824e90b7-126a-3295-bc45-ab3f438e6149 | -18.74904 | -43.74508 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7de6742-6635-3e39-acb9-50bf2a559527 | -15.9431 | -51.06147 | 2025-10-25 04:21:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93d26b4a-7c52-3544-b111-874d3caeef06 | -15.94283 | -56.12073 | 2025-10-25 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 610e7be3-c6b4-3783-add5-72e628e0fb8c | -14.33922 | -43.73766 | 2025-10-25 04:21:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| bfe12024-c0de-37e6-8fac-c3bfe1c34672 | -14.28419 | -43.72096 | 2025-10-25 04:21:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 963f5c8f-91c0-3d99-af1a-7deae0ee0981 | -15.65668 | -46.15566 | 2025-10-25 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 78f46408-4a5a-37a3-b939-0ec5de2f46da | -13.84811 | -46.89706 | 2025-10-25 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb0d2998-4fd8-389f-b312-39acd8eaa3fe | -20.29476 | -47.15295 | 2025-10-25 04:21:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 067f7ec5-cede-3aa0-8c15-f9beb44cf83e | -15.19944 | -43.78202 | 2025-10-25 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0073e18e-bb88-38ec-976b-34bad9d351ee | -15.21828 | -47.91819 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51a22df0-4db4-366b-b37b-591df9fc95e7 | -13.61932 | -48.45002 | 2025-10-25 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ee4b565-7865-3c61-a7a1-f18e72161d85 | -17.21021 | -47.6538 | 2025-10-25 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9d74f4e-910c-354d-9501-ad080e62e828 | -19.75957 | -48.28438 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d7f91a1-31be-3285-9870-d3b20545b15e | -13.906 | -48.419 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2857127f-bd87-3668-a6d9-4141cf26c4a7 | -17.37605 | -45.48806 | 2025-10-25 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b1b3b4d-f7cc-307e-a90c-93510adccf47 | -14.40424 | -51.52048 | 2025-10-25 04:21:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 686e5707-aa05-3b86-9a0a-0059aa9a02f9 | -14.38227 | -51.5274 | 2025-10-25 04:21:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81fb628a-8d7e-3b07-be95-fd325605a7fc | -18.78958 | -48.03901 | 2025-10-25 04:21:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3cafd6b1-c264-3b00-9637-086a369329b6 | -17.37097 | -45.49885 | 2025-10-25 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f69644ef-9825-3648-bfc3-f3acaad43a54 | -14.91762 | -52.44847 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fede82b9-98ef-3720-947f-386642b71bc1 | -20.4382 | -46.5845 | 2025-10-25 04:21:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README47.md)
