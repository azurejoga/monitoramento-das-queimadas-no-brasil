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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecb66346-d10c-34be-9560-d5905d3be733 | -14.82442 | -47.41477 | 2025-10-28 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0223010-b0ee-3b8d-b224-acde4890851b | -14.37744 | -44.7966 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0d62a28-d797-3737-9086-80765607c792 | -13.73994 | -48.41412 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb9dfe85-0f97-37e6-8cf2-0da77f61aa7a | -14.29903 | -44.53706 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80e5f722-81d0-3963-bbe4-b9657e21f532 | -13.24469 | -47.72935 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c05bff82-e409-3de4-b952-4f48a91368a3 | -14.61416 | -48.40672 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 91e63d32-1451-32de-a502-8338ec995b6d | -13.55791 | -47.16488 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbf75d1b-d689-3fc3-938b-450be1cc8b07 | -17.32651 | -46.09582 | 2025-10-28 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 963527f2-5d70-35a1-90c5-45bf69322e29 | -14.22416 | -44.38334 | 2025-10-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0948b707-a92e-31fc-a2bf-899b25d6f2a4 | -14.45837 | -47.77557 | 2025-10-28 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d594e3b9-5c09-34fe-b82e-c91cecfd688e | -13.24977 | -47.96302 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 09e49b75-43ad-354b-9816-1e13adcd99cb | -15.18141 | -47.21586 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 421d8b25-e8c7-3df8-bd92-f6008c6256dc | -13.85684 | -43.7868 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3b3af65-d125-38e7-b0a7-ad1be0a0319c | -14.08564 | -44.15684 | 2025-10-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea95e8f4-4d47-3c63-b037-6f8fd372547b | -13.69071 | -48.33222 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1291a91d-f5ca-3c05-a8b0-e69b8e1f8dfa | -14.08233 | -44.15631 | 2025-10-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 781798db-23b4-325b-9a57-9096c1c96869 | -14.59822 | -47.39923 | 2025-10-28 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71fbe159-d9de-3c3f-aff7-475dee0c9cce | -15.17389 | -47.21851 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63e6338a-de41-317d-a24f-5c9053f3ce74 | -13.94638 | -43.8014 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed18579e-0c20-330c-9445-fa1659ba5fc9 | -13.61275 | -47.02864 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33a3b362-7f9e-3e7f-8011-bc68991d4930 | -16.05003 | -43.53822 | 2025-10-28 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4947e03-03a7-3e99-ab53-cd37a8455b02 | -14.43399 | -49.4224 | 2025-10-28 04:17:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8453b60b-1462-3e7e-a182-a912f0e269a1 | -14.73781 | -48.16542 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c81a470b-2d74-311b-a005-8976b3280bfc | -13.57551 | -48.52354 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c24d723-5904-3c7c-9e0b-2e33e3f1c643 | -15.17796 | -47.21534 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fceaed8b-bcb7-3a53-b068-4b7a8698901b | -13.90797 | -43.89779 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ed29bf3-15f1-3696-b29e-4ea8ea3d28f7 | -15.19988 | -47.21118 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7677a851-5af2-3ebb-91bd-6d110a943579 | -13.22015 | -47.10017 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eef87516-704c-35f5-bbdd-dd8d43c0be45 | -13.22995 | -47.10594 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c6bccea-0c7e-3411-a4c3-1db325000928 | -14.73417 | -48.16502 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6eeb5173-b0f9-3ce1-98cf-9461959d581b | -15.14147 | -47.94668 | 2025-10-28 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d821f80-4eb2-32c5-a204-1ce108863313 | -14.64852 | -48.4037 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 53e9118a-27f5-3dfd-a500-daaf930e05ad | -13.93361 | -47.74126 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6003e67-b5d9-3a88-8886-a2b728a0506d | -13.62033 | -47.02589 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a2c8d1a3-c546-33eb-8b0f-7c90b3699126 | -13.31978 | -48.34272 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf600041-cdaf-36dc-913a-2c36613b4fb2 | -14.50456 | -47.88645 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a36fb683-91d3-3dc0-b574-20b71b53a3b9 | -13.22577 | -47.10947 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8ba60543-fedd-3301-b9db-a5e09c3288c5 | -15.93744 | -44.73642 | 2025-10-28 04:17:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6015155-3a4f-3e19-ace7-c72bdd4a0bdc | -13.93934 | -47.75084 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30d3ef5b-3499-3617-8516-50534191851f | -14.56094 | -47.98734 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86436a03-d261-373f-9588-b4b5b8481845 | -13.87681 | -48.49592 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48fb3ae7-bf15-3467-ad53-cccfcbaddf0e | -13.37571 | -47.40639 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61d4b78e-bca0-3578-a382-e2c39bce52db | -13.00374 | -48.77117 | 2025-10-28 04:17:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19e1a80d-84d3-3950-a146-79541afd459d | -14.81239 | -46.70647 | 2025-10-28 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbb76334-cd47-3d1d-9f9b-4edde8192ed4 | -15.19299 | -47.21008 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35afd619-0cdb-3e34-9da2-4aa6820ae2c9 | -15.61743 | -43.66607 | 2025-10-28 04:17:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e56d1de7-536e-3013-a97b-568a7cf2839d | -14.01737 | -43.8275 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6859ae7d-731f-3971-b173-38838d411888 | -16.5976 | -47.03524 | 2025-10-28 04:17:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2da736fa-0baa-3f13-aaa9-cce68c31ce6d | -18.24771 | -44.19349 | 2025-10-28 04:17:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 052cc315-2c21-37bc-b6db-299716da8267 | -13.31128 | -47.69761 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24f8fb73-99a2-3c4c-aafa-97cf05fe9dd7 | -14.30068 | -44.52645 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a47ef6f-056d-3374-ba38-e57fb9845d5f | -13.62253 | -47.03418 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fda1156-d684-357b-8c3d-ae634c8c4ce5 | -13.18585 | -48.44126 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71688bb7-9821-3a54-8120-b9f1b043c323 | -14.44291 | -49.43956 | 2025-10-28 04:17:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a7f1975-02b8-3350-b594-48f41c7ad596 | -13.39443 | -48.50968 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 151d9f6a-1cba-3b40-b2ec-fb1697b056e7 | -16.70884 | -42.88203 | 2025-10-28 04:17:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 030a300b-ee94-3b5e-abee-e04064de1b76 | -13.36333 | -47.39259 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 67e1f49a-6a75-3688-b6b8-0e30d25da8fb | -20.14938 | -42.40384 | 2025-10-28 04:17:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| eb268847-723e-346e-86c7-2669c4a0d5fe | -13.88534 | -48.51278 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b064dbe-be3f-37c8-8a50-e9489873d354 | -13.53492 | -47.17355 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a4d989a-758b-37d2-b448-94f2dd3ba5e1 | -13.30968 | -47.69381 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 510e8c48-54d7-3e92-86ed-0aece72bebb4 | -13.74601 | -48.40115 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9efd7c9a-8053-3413-b12d-1c470dd70e81 | -15.16915 | -47.2257 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55f0289a-4bec-3f09-a12e-72b5669b7dd0 | -13.5429 | -49.57679 | 2025-10-28 04:17:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 09504706-88f1-3a83-b969-f265db8d52da | -14.53954 | -47.98319 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f7b474a-c10f-35e3-b0c6-9913c013387a | -15.80655 | -43.83165 | 2025-10-28 04:17:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7e02594b-8429-3ef8-b5d9-894661fc91a2 | -13.54757 | -47.14117 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 671ff033-1325-3403-9183-7d50a4fef710 | -16.05058 | -43.53447 | 2025-10-28 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e70cde2f-5e10-3580-8f7b-1bbe2dfa8e53 | -20.66744 | -42.73882 | 2025-10-28 04:17:00 | NOAA-21 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f78d63ed-5523-3370-8131-c341ef583875 | -15.20496 | -47.39439 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bc12ee2-6da9-3a16-88fb-6cded96680f7 | -14.78897 | -42.96707 | 2025-10-28 04:17:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3079d9e0-5f08-333c-8f6a-cb13866e46e5 | -13.7402 | -48.42067 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a73d4fd5-ff09-30dd-95bc-b99886802083 | -13.86158 | -48.51772 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b21452af-60a3-338e-91dd-30303ead430e | -20.12358 | -42.39936 | 2025-10-28 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 75c7885f-75ae-3bc4-bcbb-229476212084 | -16.74881 | -41.6912 | 2025-10-28 04:17:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a58a16fc-9d65-389c-99b3-6d7440df1d14 | -15.1559 | -46.60648 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b1b2c6e-d65b-3cbc-8177-27ad51da771e | -13.37287 | -47.40174 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 695ca975-92d6-3de5-a2fa-77b88cb1980e | -14.05706 | -44.4069 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aac6e6a0-ddc9-301a-afe7-c28a31af724c | -19.12956 | -42.66497 | 2025-10-28 04:17:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7058fc2e-87a5-3abb-b6b1-684420e2478e | -15.43386 | -44.18649 | 2025-10-28 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ad5f912-7624-3c20-9427-68c04da131b2 | -14.76926 | -44.96708 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83fc48fe-addf-32ac-b7a9-4a8bd509bbf0 | -13.3063 | -47.07796 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfd51f87-e8f7-3256-b441-77d5ba4991ee | -19.033 | -42.03217 | 2025-10-28 04:17:00 | NOAA-21 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6b2d334e-e0c9-32f4-a50e-709ad9d7ea50 | -13.25341 | -47.96359 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a8dc2f6-6433-3ca7-b5a3-00cb92ecb9c3 | -18.53169 | -43.47047 | 2025-10-28 04:17:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2c14358a-6043-3ba5-aa7e-42bf7a8dec50 | -16.7476 | -41.69315 | 2025-10-28 04:17:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0fac6c8f-338a-30ba-bb26-288af215883b | -16.1883 | -45.07111 | 2025-10-28 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ce935cf-132e-3dcd-80d6-b97097fb900c | -13.31488 | -47.6981 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50a0e537-ecef-397b-b7bd-cf92dff4643a | -15.32204 | -46.81522 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8717a66c-e46c-363e-91d0-636ce0471ba4 | -14.73196 | -48.17807 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6c97ad3-1842-3575-9555-4cac4a3b2eed | -14.62703 | -48.44084 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c0c50bd-21ed-3ede-800e-c68761182b41 | -14.73135 | -47.3627 | 2025-10-28 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae08ae8e-b6d7-3d1d-b8ad-2e74ca43f9d1 | -13.23051 | -47.08121 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7bf7512-90ae-360a-a750-c1ebfb865e88 | -15.4049 | -42.92186 | 2025-10-28 04:17:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28382c16-568c-31c6-9e46-6c13d6635523 | -13.36718 | -47.39251 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 77a59fbc-8d1d-3d80-a020-672de6147e28 | -13.236 | -47.06985 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a170acc-5337-39ba-8567-e4afc7131256 | -14.29958 | -44.53353 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21df660d-b6f3-3abe-90b7-3c5c35b13fa4 | -16.08793 | -45.16826 | 2025-10-28 04:17:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a38d906d-7503-367b-822d-7b8eb379f38c | -16.46944 | -45.0117 | 2025-10-28 04:17:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f3cdf87-32f7-37e0-9ef8-ffdbdec3e732 | -14.0576 | -44.40337 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README38.md)
