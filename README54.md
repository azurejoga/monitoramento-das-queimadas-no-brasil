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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5146d98e-cc08-3179-89dd-a7db7d98104c | -11.84895 | -47.92227 | 2025-10-29 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b539d25f-1a79-32c1-b873-887fbf24dcba | -14.57711 | -47.99657 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f04a1322-06a3-3ec7-877d-f12315ecec72 | -13.35388 | -47.39002 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b37f2b3c-c588-3372-b2b7-fbb110f7cfe2 | -15.4364 | -44.18987 | 2025-10-29 04:25:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90591ff7-6e4c-39a5-9a6b-350d1d62f986 | -13.2295 | -47.72881 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99ec4baf-6a14-3a69-9f31-92ff3602316c | -13.21263 | -47.0631 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59610e53-daad-3748-94c0-0fad74af4bf4 | -13.35527 | -47.66652 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e4f5ffd1-cf96-3d73-b1b9-e9a581cce478 | -17.26555 | -45.28291 | 2025-10-29 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6255385d-6dbd-395f-944d-58b129dad55d | -13.36161 | -43.77326 | 2025-10-29 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 153eca95-f108-31bf-b284-52ee11342ecc | -15.57405 | -43.54475 | 2025-10-29 04:25:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef62bc87-aad3-3f41-bf35-c725eae4393d | -13.46678 | -47.45612 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d93af1b-ec35-3b2a-a8d7-8e1839decf13 | -12.69433 | -46.32797 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26dd05fa-2c9a-3a0a-a1fa-a257e4b32d92 | -12.52865 | -47.54833 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8c217d0-d5e5-3e08-bacd-8b58dd64b029 | -13.94639 | -48.47423 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3378fdc-0aed-34f6-8b4a-3489cecc63d8 | -18.78106 | -44.34143 | 2025-10-29 04:25:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f9ee967-a5ff-3cb9-9bca-cd4d7417fb9f | -10.63703 | -52.18547 | 2025-10-29 04:25:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a69cdbe-b5af-3809-9586-031e643ea520 | -11.7078 | -46.70063 | 2025-10-29 04:25:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59f08c94-7353-3b1d-b054-0d5f172d70f1 | -12.70267 | -46.31845 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1fb75641-543c-30e5-848c-8e26b4807c18 | -13.56335 | -49.56693 | 2025-10-29 04:25:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45a0e6b1-40a0-3d9c-8cb1-4ecb293af292 | -14.79086 | -46.17837 | 2025-10-29 04:25:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57576132-16e7-3594-b687-66d18de8932a | -13.37163 | -47.41842 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e36ea926-6fc8-35b1-ad40-f1e68c65a399 | -13.63658 | -46.48594 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c2c73ad-7bd9-3850-8d14-df3f58d23538 | -12.40843 | -46.78348 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 216367dc-a6b9-3a37-b584-0181cb1f9fee | -13.20928 | -47.06256 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 347cf87e-bc07-3ef9-a633-28f2d63b7716 | -12.00943 | -46.78349 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6c06e27c-583a-388e-bea9-7a8fda8f275f | -13.54961 | -47.13665 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a561a52-955c-34e7-809f-8774b4ee56fc | -13.3216 | -47.44031 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c85f5f0-0d7f-3734-82ec-9e5d878beaa1 | -19.33447 | -43.04144 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0e04cb08-ac48-33c3-a01a-afd50a004f37 | -10.85991 | -50.14812 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbb3480b-946d-39be-8516-14bbd42a5257 | -13.93833 | -48.43722 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be7881db-3a22-3f76-8f0b-75ce09f4a7e8 | -13.4123 | -47.38033 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7354747-9af8-33d7-8a66-3873a132dce6 | -13.87329 | -48.44553 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5af092fd-7b3f-3157-8060-43031ffc7d49 | -13.31764 | -47.70547 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11299618-8afe-3bb6-b072-0900b04ef094 | -14.67825 | -46.33944 | 2025-10-29 04:25:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e323cbe-400f-320a-9005-206850f49ad5 | -13.53682 | -47.13091 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6f97b41-0f2d-314f-b5da-03a3608069ce | -13.419 | -47.38151 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94526df8-d9e7-30e4-94a6-fcb2d6a6e379 | -12.91156 | -45.04405 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aadfb4e3-4787-39d2-9f52-5e41eb63abb8 | -14.61354 | -48.42906 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69450cbb-efbb-3ee3-b925-983fda9d1dd9 | -12.56146 | -44.96346 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06fd35ad-586b-3fa1-aa52-f842882ac068 | -12.22571 | -46.48696 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c6f4109-7d33-3d36-b668-a65b77494707 | -13.54328 | -47.32464 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56b5f46b-c740-3637-9144-71eb573142d1 | -15.1762 | -47.21035 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61991f01-00f1-326e-a8a2-321d879bd021 | -12.18208 | -43.57429 | 2025-10-29 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed3cc965-5508-3221-a109-5b8da7629a89 | -12.19652 | -46.71164 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8a6f2b10-0698-323e-8cd1-5541d37e0ee4 | -13.34352 | -46.35107 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98270a28-858d-3fa4-a375-a371131d71e1 | -15.09732 | -43.84372 | 2025-10-29 04:25:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7bdb02bd-b58d-3f38-8b2a-c86238247683 | -13.56049 | -47.34585 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acfdc4b2-b9b2-31b9-998e-b4e29959a4e9 | -14.31733 | -46.52544 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57836405-a64c-30da-9598-580bd434402a | -14.26417 | -48.11172 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92574fea-5c19-3e53-9367-9ea30d805a8f | -12.15835 | -47.69552 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 42192d03-1533-35cb-86d4-65e9fe42945e | -18.78168 | -44.33707 | 2025-10-29 04:25:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cbde6bb-a3dd-3fad-aa72-921a3cd32e8b | -15.74585 | -45.10983 | 2025-10-29 04:25:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bed3a7f1-1074-3a2d-ae2b-546106a11fb6 | -15.91867 | -43.5246 | 2025-10-29 04:25:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9b538ef-63c4-3263-b550-118ee4bfa142 | -13.31776 | -42.41838 | 2025-10-29 04:25:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d612f2fe-64ed-362f-9fd3-a0132aec3b08 | -12.31728 | -48.04561 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3467c50-f528-316f-9ff4-b627196933b3 | -12.08123 | -47.99129 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ee27683-64d8-3d58-8236-bf85c06c2c6b | -14.98521 | -48.21455 | 2025-10-29 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52e47455-ada1-39a0-a7bb-f4b5d3194375 | -12.01334 | -46.78048 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cb1dbcfe-3960-3ddb-b3d6-a47486ac77dc | -12.2115 | -47.90361 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90cee55d-0749-32e4-9796-19d7562a902d | -17.12667 | -46.18384 | 2025-10-29 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4f97755-5781-3b3f-92eb-50ee58f117f0 | -13.6303 | -47.01832 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 837ca283-9043-3230-9763-15709e53ec00 | -15.10208 | -43.83595 | 2025-10-29 04:25:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| fa78b1d8-c2f7-3114-926e-79b24d3b6476 | -13.46612 | -48.01217 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2cd129c-fd90-327f-9fcd-2d91ea382a90 | -13.86168 | -48.49387 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cccb95e0-28c4-3cdd-acaa-7811573cf90d | -12.20091 | -46.49752 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c212ef0d-5055-3619-9d3f-f4d438bceff7 | -14.92684 | -49.65611 | 2025-10-29 04:25:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3fb90f5b-1138-3e23-84ec-f3b00c531e28 | -13.48853 | -44.0825 | 2025-10-29 04:25:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1473093d-fc85-3e17-a909-92539dd89518 | -13.67115 | -47.18364 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7d47e79-c821-3208-a6d5-35b63586d7a2 | -13.56398 | -47.32425 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 229051cb-3e7d-373c-bf3a-01b3b0f58ab3 | -13.61263 | -48.4183 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5463a8cf-4eca-3b93-bf4e-797f39d485ee | -15.84078 | -49.10171 | 2025-10-29 04:25:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a51bfb36-11c2-3a01-a69c-db53226b3a30 | -13.63387 | -46.46 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eab6fe1f-d303-3355-b538-b72219d5997a | -19.24133 | -43.99525 | 2025-10-29 04:25:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 083c3b13-e7d3-3de3-b639-4859e6fbeb3e | -18.91921 | -45.03099 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7548db7c-cf25-3ea7-b7a9-568be766c32d | -15.11403 | -47.93663 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e1c224d-7b17-31a9-a960-c734cb6f27f3 | -14.31124 | -46.52078 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1943b6f0-9829-3eae-8b53-1cf201027990 | -14.48374 | -43.94139 | 2025-10-29 04:25:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adc478ad-ac21-34e1-b1f1-cc1e98055839 | -13.69339 | -47.6704 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f444e3d-1a45-3905-90ed-d97a8718d4eb | -12.19319 | -46.71109 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 22abba6c-54f9-38f7-a584-b0e8432ee1ff | -13.64272 | -46.46875 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4140d036-85d2-3d48-a09f-ab42e8c9e840 | -13.30429 | -47.69639 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd0e8b02-82ff-3993-a47c-7d7d568f84b7 | -13.53959 | -47.13499 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 07a82705-9d01-38fd-babb-6afabd5c1d2b | -18.92684 | -45.028 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d22a1fdb-9ccc-364c-8b8d-a930c497b16e | -15.17953 | -47.21089 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2b068de-451e-3d66-bddb-1cb9dd5bf2c2 | -19.45597 | -43.60052 | 2025-10-29 04:27:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 76738454-7e2e-3a11-ab62-bddc4da49fa5 | -19.743 | -47.74329 | 2025-10-29 04:27:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| befb9ec3-09db-3c0c-a089-98f5e400dd2f | -20.53575 | -45.76338 | 2025-10-29 04:27:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 743e1366-a95e-3811-ba5f-ce8504e4235e | -20.56535 | -43.23552 | 2025-10-29 04:27:00 | NPP-375D | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1fe879fd-05a5-3a09-9da2-d75ca94e101d | -19.89669 | -44.62035 | 2025-10-29 04:27:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0f13ec95-52b3-336c-a66d-c97b214b0fd4 | -21.25706 | -48.26721 | 2025-10-29 04:27:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47d3c7c7-62b3-3a63-8603-4a3e1e5ee61b | -19.75739 | -43.84524 | 2025-10-29 04:27:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 427198dc-a2d3-3740-a4e7-fca270fc42a0 | -19.67676 | -44.19173 | 2025-10-29 04:27:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ce70832-d5f9-3a99-87c9-de466ffae293 | -19.67983 | -44.19695 | 2025-10-29 04:27:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91b5ec7c-e138-3da5-a85f-9f50796a4111 | -19.46167 | -43.58681 | 2025-10-29 04:27:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b8d8bbb-b560-328d-b9a9-1193e2c01c83 | -19.45097 | -49.32953 | 2025-10-29 04:27:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fecdaf4d-46dd-35ba-935c-95d1d2a8e80e | -19.45161 | -49.32573 | 2025-10-29 04:27:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77ffc23a-c213-39dc-ad01-5bfa46042644 | -19.96562 | -47.20745 | 2025-10-29 04:27:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52ac67d3-ff1a-3cfe-9643-9898bc337530 | -19.71844 | -43.93623 | 2025-10-29 04:27:00 | NPP-375D | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f651d33e-beb1-3f83-857c-5e59a3cc961f | -19.67794 | -44.1945 | 2025-10-29 04:27:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5b24c96-ff4b-302e-aa2e-c3e1128f3ac7 | -19.42224 | -48.06496 | 2025-10-29 04:27:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README55.md)
