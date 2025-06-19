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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b928953-79ba-384c-bece-83ebb7b5e9ac | -8.96124 | -47.98026 | 2025-06-19 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5758c5a0-1f15-3cc0-b873-454b968bd39f | -12.26749 | -44.60032 | 2025-06-19 03:57:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e2969aa-5389-3afa-9408-d99aae6bec78 | -11.57122 | -47.43724 | 2025-06-19 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be048de7-b723-3543-809d-b2e38eb2b438 | -10.65364 | -49.45263 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47c735fc-c861-3240-ba6f-960f76051e0f | -11.12992 | -53.94031 | 2025-06-19 03:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1df3db81-c673-3b65-8914-6e685dbfb916 | -10.64803 | -49.45147 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be6fb7a3-7700-32a9-969c-8ac40e5f7111 | -14.21207 | -45.5168 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d91b9ce4-b826-305d-835f-fa2209545e31 | -11.13718 | -53.9418 | 2025-06-19 03:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0925fdf-39ba-3380-a742-f9f8938e0f0d | -12.26655 | -44.60555 | 2025-06-19 03:57:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6b51676c-2a30-367c-ada4-a3bb0f634906 | -9.88164 | -47.81221 | 2025-06-19 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 204246ce-7a98-30fd-bdea-cf377f0e05cc | -11.29025 | -48.69706 | 2025-06-19 03:57:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 626e7530-0ddb-35fb-93ce-c48226189684 | -9.32912 | -47.82935 | 2025-06-19 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54650718-aaca-38bd-a778-beeb00fea6f6 | -11.62529 | -41.83628 | 2025-06-19 03:57:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 628c3b34-0dc9-3d6a-970b-65b4b3d13d70 | -9.37993 | -47.64087 | 2025-06-19 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c81a71f-744d-3432-994f-19a07dbb467b | -9.38048 | -47.63784 | 2025-06-19 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8d998c9-b43a-33ab-918c-6610846acc25 | -13.44146 | -44.48059 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3d55a1c-1bd9-351e-9820-8dd22afb4ee4 | -10.64579 | -49.46308 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4bc58116-7cec-36ff-8f5c-0fb56a1506ca | -11.90956 | -44.17442 | 2025-06-19 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33b5890d-187c-3957-b638-d0c907781335 | -14.07194 | -53.39416 | 2025-06-19 03:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb712645-ee39-3bd1-8ca7-4cb8717c5543 | -11.91312 | -44.17798 | 2025-06-19 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5794008-8b2c-3a14-8d42-945cf2cedc0d | -14.2114 | -45.5205 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d6451e8-79ea-3d3b-b177-abd75192d2c4 | -10.1549 | -48.98432 | 2025-06-19 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36e402d6-c62a-3973-b54e-2d1181fb8c20 | -8.12945 | -49.59044 | 2025-06-19 03:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da569497-7755-3e94-89c3-67df38ed0d73 | -9.42636 | -40.38648 | 2025-06-19 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c67e649-33dd-348a-9c9c-0e5f0d0b483d | -11.91346 | -44.17511 | 2025-06-19 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bccd713a-0643-35d9-8566-1e00092048eb | -10.63942 | -49.46584 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36000406-cc09-3952-af48-21b3bd4394dc | -12.26516 | -44.60266 | 2025-06-19 03:57:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e2550528-2241-3310-b682-08eca7667b43 | -9.7972 | -47.18468 | 2025-06-19 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0477459-9eaa-3a71-9952-9784a0553e3b | -10.12396 | -47.55841 | 2025-06-19 03:57:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1720bca-7461-3cf7-bd7e-c8ce0cabc39c | -11.62592 | -41.8324 | 2025-06-19 03:57:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d64a16d2-ebd5-31f0-858f-02d8283c5276 | -9.24715 | -50.02949 | 2025-06-19 03:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ba1960c-f7c3-31d9-949d-832ab4e532f3 | -10.09313 | -52.74365 | 2025-06-19 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4529d215-c310-3857-9a74-0dea14a98cc5 | -9.88222 | -47.80909 | 2025-06-19 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ae67e56-4781-315d-b2ca-2c8be9219bba | -12.26425 | -44.60791 | 2025-06-19 03:57:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73288f76-3f35-3028-bb91-7137c0d259e8 | -12.2656 | -44.61081 | 2025-06-19 03:57:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3d0db146-d2cf-3f3e-b002-102e9ee8a4cb | -8.95597 | -47.97932 | 2025-06-19 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b033a3f8-9217-35b9-888f-3b804f39d17d | -10.08627 | -52.74203 | 2025-06-19 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e992f2d-dcad-3023-8956-c53e0590fa74 | -14.60388 | -42.888 | 2025-06-19 03:57:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d2492ad3-e955-3d0d-9665-4334027f2522 | -9.50616 | -45.44917 | 2025-06-19 03:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0c7a7a9-806d-3e3d-a4ae-90b904c6e215 | -9.42974 | -40.38703 | 2025-06-19 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 845afe1c-cc95-3e6e-bf4d-b913f4f3bc40 | -8.95659 | -47.97604 | 2025-06-19 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7513ae5-174f-3927-9941-70df815db447 | -8.75187 | -46.94596 | 2025-06-19 03:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56a28564-b1c9-39c2-85d7-ba62249e1b37 | -8.13304 | -49.58891 | 2025-06-19 03:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e733565c-cbbf-3918-8e8c-27ac3e1cda94 | -14.81792 | -48.46923 | 2025-06-19 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 37bcbffb-2ceb-31c1-a9f1-e6a5e7462ac1 | -11.32936 | -45.20966 | 2025-06-19 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e143aa8-d1da-3caa-acbb-1952c3eaf562 | -14.21548 | -45.52129 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31cb76b5-6256-331d-a7da-1d1467375f14 | -10.15972 | -48.98902 | 2025-06-19 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9513000-dec9-3035-a79e-faeb461b3afa | -14.44078 | -48.90146 | 2025-06-19 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 68721321-4b52-3ece-b47c-6980034dc058 | -14.22022 | -45.51837 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32b0f37d-0dbe-341d-a710-108e2b0e14fd | -14.21073 | -45.52422 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eada75ed-fdde-3aaa-b7d5-21cefc5649dd | -11.42059 | -41.39911 | 2025-06-19 03:57:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ba17b3f6-94c4-36ee-91e5-9ced064cc8ed | -12.26822 | -44.60869 | 2025-06-19 03:57:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89e7ba25-99c6-3789-92c2-a549d9e5e195 | -15.2919 | -48.66016 | 2025-06-19 03:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceb6eeb9-1cf1-3dbc-ac3a-a7137550fcbb | -12.79844 | -48.73091 | 2025-06-19 03:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3540e3d-321c-333d-9591-aa39bf4dcc15 | -14.06392 | -53.39878 | 2025-06-19 03:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f746974d-4857-32c7-80c9-82b474637ad3 | -10.08718 | -52.7421 | 2025-06-19 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72dccb86-5953-3d44-9dcb-b90cf913d2fc | -8.95723 | -47.97965 | 2025-06-19 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f86556c-3604-30fd-9270-db523d99ce10 | -14.81928 | -48.47092 | 2025-06-19 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| aa8814f5-17ed-3526-aade-702e9a4cd431 | -14.21681 | -45.51389 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82fcb514-ca11-3052-bb08-f08b8d084777 | -12.27145 | -44.60108 | 2025-06-19 03:57:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6209e49c-fb2d-3bc7-b817-d93c6e3e72a2 | -10.0945 | -52.73698 | 2025-06-19 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d7ffb33a-a57b-3012-8941-608bc9a44600 | -13.44534 | -44.48125 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41144c33-341b-360a-9f14-6cb0f6017f16 | -11.90871 | -44.1794 | 2025-06-19 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93f26bbb-02f3-3581-bc93-78f96f37c227 | -12.26913 | -44.60342 | 2025-06-19 03:57:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d1f71230-47ab-3ff1-869f-4ed23a38a7d5 | -8.95782 | -47.97636 | 2025-06-19 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d1003a3-2620-35a9-b09f-a1954e911f57 | -9.37537 | -47.63694 | 2025-06-19 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 08c53a76-81a0-3fa0-9060-0b818f79cfe0 | -8.72258 | -47.99826 | 2025-06-19 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 418303b7-b3a8-3f66-b5c3-9aca033826b7 | -10.15422 | -48.98796 | 2025-06-19 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c6c92bf-d46f-3186-b1ba-85d593c8116a | -8.74693 | -46.94514 | 2025-06-19 03:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 335602e1-44ed-32d1-a8a6-59c775b16dc4 | -11.16456 | -50.08287 | 2025-06-19 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27f359c8-7df5-33c7-9ea2-6b00af1fe6f1 | -9.53162 | -43.21358 | 2025-06-19 03:57:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 312e8dd8-468d-388d-96a3-5a5909fb9b53 | -9.43311 | -40.38758 | 2025-06-19 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1b2ade0e-e630-3332-9c4f-0df299bcbe5b | -10.52665 | -46.65769 | 2025-06-19 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec2413d8-27c9-3dd0-913e-bf7655cd25dd | -10.64728 | -49.45535 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 597f3a7d-bd4d-3611-9cf1-e0859f29ed13 | -11.28962 | -48.7004 | 2025-06-19 03:57:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31b43b32-aa2c-3626-962b-ae3451de0c0d | -10.95337 | -49.25272 | 2025-06-19 03:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| affd0768-4240-3209-b70b-f3f7e6c5fafb | -14.07061 | -53.4003 | 2025-06-19 03:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8eb17e0c-e3bb-3e86-852a-b906ce2de445 | -8.72198 | -48.00156 | 2025-06-19 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2799a291-d4d6-3e91-a4e1-62213dbcf126 | -12.79872 | -48.73505 | 2025-06-19 03:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c45b641-9999-3e87-9d69-ab86f42303ba | -11.5722 | -47.43198 | 2025-06-19 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ddb64d24-e7fb-3eb4-a857-dde22a9978a7 | -15.80074 | -42.03625 | 2025-06-19 03:57:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ea9c8c2d-2580-3652-939f-bebca38f33a6 | -9.32799 | -47.8354 | 2025-06-19 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cff6be80-5443-3d0c-8801-ff69dc5a8823 | -10.65289 | -49.45654 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd2ece8f-5950-39a8-89ca-c58f33a98d9e | -14.43961 | -48.90742 | 2025-06-19 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 25b9c64a-30cf-3732-ae95-fb320a0f7fa6 | -14.60456 | -42.88393 | 2025-06-19 03:57:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 769f63f6-db2c-34d0-93ba-efb18bf368ea | -14.22088 | -45.51469 | 2025-06-19 03:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 699d29ef-0496-396c-aeaf-c3adef2a8077 | -11.29088 | -48.69369 | 2025-06-19 03:57:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ad325bf-abbf-3264-9630-e58ef253c5a8 | -9.20957 | -45.33988 | 2025-06-19 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8066e3d-65ac-3c2c-b04f-de23e39e4ba4 | -9.37481 | -47.63997 | 2025-06-19 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f8de4efb-17d7-3f9d-b81c-d62bf385e5c7 | -11.78603 | -44.2817 | 2025-06-19 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99d0cab6-d68f-3dab-b945-bef71c549b15 | -10.64017 | -49.46194 | 2025-06-19 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f985fffe-52d4-3cd0-a4e6-7157f0cef7fc | -8.96308 | -47.97731 | 2025-06-19 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06d8d727-0818-34dc-8d8b-82d2b942ac69 | -12.06735 | -48.46444 | 2025-06-19 03:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a366836e-59b8-3bd4-a3cd-11a3187da7d6 | -10.12379 | -46.26758 | 2025-06-19 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 164d8aa6-aa89-3678-8796-7affc742f7f8 | -12.79785 | -48.73404 | 2025-06-19 03:57:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a71203f4-71e5-334e-a2a6-860927f048d9 | -11.89039 | -49.33349 | 2025-06-19 03:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0584b83a-bf47-3b2e-bf4b-4c0950779525 | -10.12525 | -47.55817 | 2025-06-19 03:57:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4633b908-9ff4-39d1-bcb4-e0ac9d53aa06 | -9.79823 | -47.17908 | 2025-06-19 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f872d92-bf54-3401-a259-4138799c96ed | -12.26334 | -44.61318 | 2025-06-19 03:57:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 059b567e-d245-3b3e-9b33-803f1ef11548 | -10.07896 | -52.74728 | 2025-06-19 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README11.md)
