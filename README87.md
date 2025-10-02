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
| 0e0f1802-b97a-3f1a-8c8d-fbbaa8db7ed1 | -14.39943 | -46.08434 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96b0b151-e918-34ea-98d9-79da6d236601 | -13.17668 | -47.82716 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdadeb96-5808-36c6-bef2-337dcb43ad28 | -17.91124 | -44.60973 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 460d7051-e25a-3786-8baa-c0780f90157e | -18.62508 | -50.68615 | 2025-10-02 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 664bcfdd-7cfb-3c03-812a-1bfd640522b9 | -12.68107 | -48.5747 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 195ebe84-eb69-3a71-8658-54d4ffb5e01f | -14.59827 | -46.71088 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1337a12-5e7d-379c-b5d0-1b7b32a3e7d1 | -13.67859 | -48.07291 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c443d0d6-799d-39c5-b92c-cc452ba4055f | -14.48065 | -48.43195 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9e5b3839-7672-3b32-96bb-9533e5069cd4 | -13.40707 | -47.78139 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e19f28b-ecf8-315c-bb43-ce004ebdf7ba | -14.31534 | -45.99708 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 877b5a13-90d3-3739-bb1b-f74d7928aba4 | -13.21282 | -48.51562 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32d0683b-c2e6-36ea-b660-646080394881 | -13.30568 | -47.84505 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3eec1327-a767-3221-bc79-1c244a67f265 | -13.75784 | -47.95511 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6208b8a8-e5be-30ba-8a48-dd582bf8e204 | -14.47188 | -48.40117 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 54e811cd-13b8-3dc1-abf4-8e309f22b19f | -15.17186 | -43.62782 | 2025-10-02 04:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 0cb53fd0-c90b-380f-b5ea-f4ca0f518d92 | -12.8147 | -47.02452 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec4174d5-ba13-38a6-974f-0adc986a61df | -16.36888 | -47.05186 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02e6c74c-3f27-3629-903d-d06a48f98b0f | -14.41439 | -46.10262 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d402c850-59d6-3ec9-a3d0-c75623dbd421 | -13.0731 | -46.99623 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 302d3924-ba07-33e4-a0ba-d656b71a5404 | -15.3973 | -47.04556 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65aef136-7ef3-3ac8-b5eb-d93ae072d1d6 | -11.82586 | -48.06838 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a72eb9c5-26ca-326e-b96c-04eddfcb6d7c | -15.29308 | -46.3953 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78911623-0d3f-3fe9-af15-ea72d28f6bcc | -11.86492 | -48.01661 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d33c3b32-ef26-374c-a761-d7dfdc06d8cf | -14.36797 | -45.95371 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98766b00-7acc-3994-b75d-ab1136dcdf45 | -12.00172 | -47.19444 | 2025-10-02 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68ca5a21-120a-3acb-a656-0c37aae22476 | -15.23393 | -50.11715 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 98aaf096-2196-30b7-a60b-ca233571d4fa | -15.45791 | -45.88248 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d19054e4-a024-3084-a1ff-70c058410ada | -13.70292 | -48.62245 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f92aeda9-b10f-3b69-994d-b2dbf9a565f4 | -15.8227 | -46.26061 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31cc23bc-e92f-3b2d-a968-7278108152ae | -14.64371 | -48.15178 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80658ff3-f997-387b-b090-bc46dd6b324c | -13.75564 | -47.94744 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5648c652-7daf-3b83-92c2-bb84da785978 | -16.3676 | -47.05853 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60ee2832-9800-3525-b649-c45d97c0594a | -18.44267 | -43.81448 | 2025-10-02 04:32:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf7cc62f-8027-327c-8ea7-64be10cbc32e | -12.85583 | -46.93594 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b001642a-48e3-3225-b27e-f39c1c07b6c7 | -13.31879 | -47.00535 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 359ef4d6-d452-3b3d-a9b2-ba02e044d860 | -14.98125 | -46.91643 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21e2870a-8a73-3df1-8e97-3b4a501ad622 | -14.36391 | -45.95707 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad529762-cfcb-397c-bad1-b137d2b3cb78 | -14.70062 | -48.21586 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34357672-23ed-36a4-bfe4-54fb9b078386 | -13.79932 | -48.03864 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d191217-9395-36f6-808a-9ee2b9f1ff82 | -12.47641 | -47.26665 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 29d080f0-92e1-3323-ba89-594f3108c240 | -11.92624 | -47.88109 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 808b912c-a3db-3f2d-a09d-f507813ba459 | -13.80982 | -47.53621 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af1eb153-8ec6-3560-bce5-5659f0fd5003 | -19.44473 | -44.16129 | 2025-10-02 04:32:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5055f5d6-1528-33f7-9d50-b3d7cf78e8aa | -19.45615 | -44.29195 | 2025-10-02 04:32:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f66e081-4e83-3e4f-9f51-cc7c084c77d1 | -13.76334 | -47.98523 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44042345-e9dc-3524-9a67-03dbb8552c71 | -12.85248 | -46.93538 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec1ef029-3f1b-3b73-b8e3-973a5b786373 | -11.87476 | -49.91261 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7da00be-41e8-3956-bca9-06ee85eb1aec | -15.54872 | -48.17572 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e83eae14-cbf8-371a-bc7a-9d8fed291145 | -15.14361 | -48.02093 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 827f870e-20ab-3616-a47a-e146b82ee130 | -13.63929 | -47.6585 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 123463ac-3063-3295-8a40-025ab194fcc3 | -13.01401 | -45.21452 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afd1c580-91a1-3501-b01a-9b5100d1a45a | -13.15729 | -47.79849 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4afa5f7-0f7f-3389-a60a-7e87da4f5815 | -13.32513 | -47.80825 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ae68bc5-7f5d-3dd3-ab79-4e1ed88edcb8 | -13.15446 | -47.83807 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a6f30d1-33bf-33f8-b77a-1b99ff96599b | -14.89651 | -48.32491 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7be6f3dd-eefa-3d70-b095-31412d945582 | -14.47131 | -48.40474 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 900255a6-aa48-3051-884b-31b7764fa378 | -13.46842 | -47.25789 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c21e964-1af2-3f4f-ac10-e41446e16a88 | -12.45629 | -54.31627 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6bc9c97-ca24-3b4c-ad18-7eccb11f2965 | -15.22947 | -48.72598 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46fba7b1-3b0a-3ecf-9f3c-b6f3512df8ed | -13.57579 | -47.58998 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58b6c379-b2f9-3fc1-aa43-6fb040d75457 | -15.14417 | -48.01735 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f91d2eda-c875-3fe4-a148-3894892becb6 | -13.78929 | -48.05888 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7c990ef5-fb23-3e8e-abfb-8917ceea2c45 | -13.01695 | -45.21908 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b139bf2-98fc-3205-b043-f6ef026e7c24 | -15.78466 | -43.68024 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 757ae2fe-bb65-37f6-9bb2-0d1ffc52df62 | -14.34882 | -43.84951 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4982e88e-498d-3ac8-a0ef-013cbdb26fb8 | -13.6814 | -48.05514 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c09f2edd-3bc0-3111-b859-f322e5346fd5 | -12.8231 | -47.05885 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0246a145-8efe-3910-a969-978a9b773ef4 | -13.31654 | -46.99762 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96bcce6b-2092-36fb-9d53-d8246c5165e0 | -15.59933 | -47.64053 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 757217ba-d7d2-3baf-a2b2-10de673c7e1f | -13.64511 | -47.19017 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58cb3700-10cc-3f1b-8940-c710d6b09dbf | -12.9034 | -47.17107 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9875de59-25aa-3053-b82e-58fdaa8465d7 | -15.26164 | -49.31691 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 41c1cb15-d5f0-3212-977c-0fb1079df40a | -14.97279 | -46.92641 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 002131bb-cafa-39d5-ba9c-5ef5d4060b88 | -14.02604 | -47.99517 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46cdf697-3dcb-324c-989e-98be0ec5dde6 | -12.88429 | -46.92944 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 70d6b7c6-0729-3dfa-a01c-543b67a5b53e | -12.84625 | -46.86434 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7d759e5-ce4a-3e12-936d-6521845aa0e1 | -14.44347 | -46.34948 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54e74e83-3ce2-3e7b-a649-a9658d79ce5d | -18.66927 | -43.87936 | 2025-10-02 04:32:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee0482e8-739b-342b-8699-4961295e42f0 | -13.21233 | -48.49723 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e34752a1-1c83-302a-94ef-a05bf75c1af7 | -11.58904 | -50.17593 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1bf44e4-8ad7-35c6-a09a-79727306fdc8 | -15.24279 | -48.72826 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad5d3a33-0e22-35ad-9468-5ccd45b90ab0 | -12.70728 | -48.58269 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f8cce248-1bae-3e58-974b-0fa7270cb474 | -14.90486 | -48.31531 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07c8f27f-98f5-3496-84ef-380d51418b1e | -12.95233 | -46.37362 | 2025-10-02 04:32:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1afbb980-1253-3b8a-9bc7-8cc1863d3e77 | -17.51629 | -43.48643 | 2025-10-02 04:32:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5be07d36-6f89-3be6-be3a-da06d77b1511 | -15.2289 | -48.72955 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dbbf7a3-c6b9-3b70-aa5a-7c289cba1d8b | -16.36097 | -47.03509 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b17ca933-1609-3fa6-8dd8-c0a10ec733fd | -14.30259 | -45.96354 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0c35e11-6818-3982-adfc-c72bf4e8e810 | -15.78396 | -43.68547 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd0cd1fb-a787-3241-b735-2d4a396905e4 | -13.82115 | -47.94366 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da24e52f-0fdc-3d8d-a84d-dd8a6a481220 | -13.28474 | -47.24668 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1e97dd4-25cb-3393-a99f-beb33aca99d9 | -13.05637 | -47.01566 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38aaec29-384b-3486-869a-4f20a1f5eae4 | -12.81525 | -47.02095 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 339007fb-b30b-3807-9dd9-17ee8960a5c9 | -15.23587 | -50.10558 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a72f93d5-31ad-32b5-8f06-fe44b9d602ba | -12.8699 | -47.02238 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02d798f6-512e-3fc4-ae8a-7e9894688b5b | -14.61667 | -48.30115 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb0082f1-8ad8-34a3-97d1-bc57f23f7865 | -12.00899 | -46.64042 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5b1331d-16d7-3e39-97dc-a036251a68ff | -11.95057 | -47.10627 | 2025-10-02 04:32:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b78e27d2-362d-3e33-b2ff-4c0354ea2117 | -14.03049 | -47.98861 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20ef7844-17e8-3a95-8835-81d1f31b5bae | -17.02114 | -49.15 | 2025-10-02 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README88.md)
