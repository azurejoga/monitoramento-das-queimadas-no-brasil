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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fab64cf0-498b-3c72-855a-8a6bca0050b6 | -14.97847 | -46.86655 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53940c84-7509-3e03-9767-7014316b8d5a | -16.03063 | -50.91626 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f08dabdf-4565-3778-85fb-1fbb8882b46b | -15.35165 | -47.07226 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1df23915-9176-35b7-80e3-d07ab9f328ba | -14.47456 | -48.42728 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 095e05ee-59da-3cc2-ae5a-7463d0dc3401 | -14.91153 | -47.23576 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a6478b0-5bfd-373b-8619-af8cd4af2bad | -13.19887 | -47.83809 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2feb7b77-9b39-3726-bfaf-7772f773886c | -12.67772 | -48.57415 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9136cfde-541d-35d1-88ce-4cddb80672b7 | -14.5778 | -48.30931 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1860ecce-332c-3861-8dd5-fd9cdf8465b9 | -14.98635 | -46.9058 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 896a5c61-abf9-315d-965a-54635b6cfe1e | -11.98008 | -51.40678 | 2025-10-02 04:32:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9fc32314-f4be-3109-8a38-913ba2857e0a | -12.15303 | -46.67392 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6174c2a4-ea97-3c9c-b7f3-d9658bb90a69 | -14.21004 | -46.11958 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 722f1dd7-0226-3a98-9780-3258d0592df6 | -14.02772 | -47.9845 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 812b18a2-6a6f-38db-b7ce-467b59f854ca | -12.03082 | -47.90527 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5fc97c8-914d-370b-bf7b-c24dd02c995a | -14.58979 | -46.72096 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9dedba84-0ab7-3dcb-866c-720a4ec0dcdb | -15.26617 | -49.31023 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 86011779-bf94-32a0-aaee-b1d68d13d573 | -13.69221 | -48.64648 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 782ce7c2-537f-3300-aa3f-24ecc847e332 | -19.26576 | -47.42636 | 2025-10-02 04:32:00 | NPP-375D | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 096af9a4-816a-3211-b9b2-37bfc78520f7 | -13.3126 | -47.58407 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be286e15-1b6f-34bc-9a5d-c0e7f90d8838 | -13.81205 | -47.5439 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5d08b1d8-484f-3b24-a990-cad448549311 | -15.35897 | -47.06968 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f520ded2-745f-375a-85c7-24f69a4ef120 | -12.42607 | -44.09758 | 2025-10-02 04:32:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38d078f0-871d-3a68-a0e9-b4016a731123 | -15.14473 | -48.01376 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d71cb95-e772-3498-9883-511b8c0953f2 | -12.91508 | -47.16196 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd5bb567-0722-3a8e-b5f9-b18a1fc66b04 | -16.36482 | -47.07852 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b212cd02-459c-33e3-9aa6-a4f6f19a2d20 | -12.25757 | -47.79755 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cf5e2e6-f57c-3631-897e-93a817313900 | -15.25829 | -49.31631 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 785bfc76-31a3-3fea-b8a2-85c032d56066 | -12.85764 | -47.03508 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6785292-0443-34c5-b876-dcfec856b5ac | -15.25153 | -47.89898 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ff813e1-a4af-3840-94d5-b58958038b56 | -14.30609 | -45.98774 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 007cca96-3584-3ae8-b9d7-48cb86638021 | -14.88424 | -48.12898 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 701c80a2-2365-317e-82c7-e1e1dc21bd0f | -14.85555 | -48.28918 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e5c1f87-2c16-3a2c-9b6d-1fa85cdb85c4 | -13.3068 | -47.83796 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee347771-be1e-3f79-be5f-bc65ef453703 | -16.7766 | -43.03621 | 2025-10-02 04:32:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9333cf37-5749-3894-93eb-1e93a37218a4 | -14.96626 | -49.96308 | 2025-10-02 04:32:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83fbc1ea-8d8c-39f4-b95c-7f9d25cb6d7a | -12.58303 | -49.89333 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 020792ec-790d-34d4-a58a-39f7418a6dcc | -19.59757 | -44.86961 | 2025-10-02 04:32:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec242181-1e84-3726-a836-fdb169d7f137 | -17.17122 | -47.01928 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83509497-a6c4-3b7e-8385-ba1063e103f2 | -12.83509 | -46.86989 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf8c374f-8305-31b9-94a5-0c0bc58f5528 | -11.86085 | -48.08507 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b3561b5-f3ec-3a48-8b09-15ca0a39f4d1 | -13.16168 | -47.83562 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ccbcb77-8801-3e2e-9d2a-bc2914972697 | -13.21616 | -48.51619 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00285b0c-feb3-342b-9dc4-aadf51d3de75 | -15.23537 | -50.11374 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7d9b28d6-af10-3a60-a0b6-f04637448be2 | -15.9467 | -43.32937 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c90f530-a0a9-37c5-9627-b5f15f2950c7 | -14.03879 | -48.00094 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fe1f035-029d-3760-a108-b8cab2aba8e6 | -19.02316 | -49.74886 | 2025-10-02 04:32:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e245036-5700-35cf-8154-41cdea66a6eb | -12.86935 | -47.02595 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4aa1738-9f5c-3abf-9e3b-e4fa4ad63c6f | -13.40595 | -47.78849 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe8c43e1-6481-35fb-966b-e3d0ae350e4b | -14.40403 | -46.07722 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5de6af66-5ccf-39f2-a3c7-c1a1a4a95539 | -17.954 | -45.034 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f9cceed-920b-3b73-b804-311637b9806e | -14.42418 | -46.10806 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59a30025-92f9-3682-9d1b-fadc5652f097 | -13.96418 | -48.12734 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a52838ac-80c5-3766-90b5-ac85fcec89d5 | -13.67966 | -48.08769 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bb50a5c-0bb7-373d-8b3e-a19e084f227e | -14.9835 | -46.92437 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87bcec49-b610-30c4-99aa-9701a4f4c946 | -14.89706 | -48.09082 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f35bae7-9e49-3da5-9806-8e68b3235bb4 | -13.32457 | -47.81179 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 407d7de5-7db8-3bcf-9c35-67df7d477df5 | -15.64454 | -46.25336 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b55e0b27-a113-35a1-8e2b-d379284f8229 | -13.21756 | -48.44312 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e850433c-d96d-3bdb-857e-dbbe67d021c5 | -13.67587 | -48.04693 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f6780fd-4870-3999-85fc-53b7c67abac6 | -14.33989 | -47.1489 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 741facc6-dccd-3ea1-a540-a0f0637bf19f | -15.31428 | -46.39496 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbda6f37-8277-3b35-832a-f53fdc45001b | -12.2492 | -47.8288 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf952c00-6ba0-35aa-aa37-2574253a7076 | -15.20528 | -47.99806 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2880fa2e-370a-39c9-9f66-9fb5d6d699fa | -14.42531 | -46.12406 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c796939-3668-3218-b27d-8b5132ddca41 | -14.22831 | -44.78623 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db244e53-de8b-358a-9814-39bf075fda18 | -14.36969 | -45.96589 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0c899ca-55f5-3436-80b0-9e02b1ddb1f1 | -12.70831 | -46.89077 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cad71e9f-122e-3afc-ba3c-3ac1acc8db91 | -12.31295 | -46.8824 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de003ed7-55e7-3e19-bd23-20ea49bf43f5 | -16.13527 | -46.6804 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b898f32-73a2-32c7-9a88-03f79b262184 | -15.3235 | -46.4041 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec49bf76-0920-362e-bb4e-5a2eb2c86b0b | -14.31764 | -45.98164 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b372406-1764-31d1-b045-edee6d2d298d | -12.27916 | -45.3679 | 2025-10-02 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ea99041-3eb6-3086-969a-b4e0697409c4 | -14.03546 | -48.00039 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee60c95c-ff15-3c18-9155-67a28584ed94 | -12.76059 | -50.5591 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79c5fa52-d067-307a-a022-69baab011d73 | -13.80755 | -47.53545 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a9cd5be-2b8b-3eb4-81cc-6bf932543cbe | -14.59494 | -48.33047 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61ad5b21-bccc-38f2-b138-78eb081cea79 | -12.8169 | -47.01023 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6970058e-3430-3eaa-abbb-c862a1f8a9f7 | -13.31204 | -47.58765 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0e45f80-a569-3879-ab89-9657ce6dec51 | -12.8766 | -47.02344 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 781ff060-abb3-3b6d-b2db-25d722917c2b | -13.47398 | -47.24417 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0841e547-be73-3ec9-adf1-c63c75557ec8 | -14.86829 | -48.29498 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e5a9174-2ed5-3e02-ae17-e1f4c766eb1a | -14.48341 | -48.43607 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2625e91c-728e-3445-bf77-01890ae5d848 | -16.37156 | -47.05534 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7e99ed5-be7a-36df-847e-881ff1201e9e | -12.87325 | -47.0229 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8049bd7f-a73a-3731-a44a-95ce4093ac1c | -14.88095 | -48.33697 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03b668dc-01a8-315a-a55b-84700af0786f | -19.7855 | -44.29996 | 2025-10-02 04:32:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c49ceb52-7a74-31cf-84e8-6ff55704e3ec | -12.43223 | -50.1661 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52db0655-9188-3e15-8725-b6dc74886639 | -13.22033 | -48.44721 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28bb5d64-36cc-3afd-8c9c-2584147cfc45 | -12.2768 | -45.38354 | 2025-10-02 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75c1bc73-1b09-37f0-8eea-f1dccdb5f9aa | -15.59954 | -46.90891 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51b707fd-5805-3fad-8247-cce222176874 | -14.41956 | -46.13885 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6551b28-24dc-3819-b5df-eb5530b019ad | -13.32789 | -47.81234 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 462dbfec-8f25-329f-9737-ae02907cbffc | -13.68945 | -48.64232 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fced3cb-7a95-3a5a-81cb-905c7260568d | -15.2328 | -48.72654 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d338da44-ec56-3f56-9268-57eaccf620d0 | -19.71934 | -45.90746 | 2025-10-02 04:32:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 683b3b6b-f19b-38e7-986c-ce0c29e01a0d | -16.02187 | -50.8619 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a72fb1fe-cfd9-339a-8bf8-8d1a5842f551 | -14.6654 | -48.12245 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af86cda8-583b-3cc9-92df-2841e842e62d | -14.08731 | -46.6549 | 2025-10-02 04:32:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f027160-3893-3c92-8446-13235f91be7a | -13.05692 | -47.01207 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f07845b-63c7-3083-8739-2fea310ff1f4 | -12.6357 | -44.85314 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README98.md)
