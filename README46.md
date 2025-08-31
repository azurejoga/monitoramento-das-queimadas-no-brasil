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
| 1bb2c639-9aa0-3149-bcd7-30fc3da6d8d7 | -11.81218 | -46.45391 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8e2fc39a-2981-3d9a-898f-171345e70578 | -11.0594 | -44.62234 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6441212d-1744-3566-a9c6-4d9a69bc5d4f | -11.83064 | -51.4989 | 2025-08-31 04:29:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d41ab64-3dbf-3751-8e0e-0dbbda271c4d | -14.85287 | -42.79052 | 2025-08-31 04:29:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8099ac73-bf87-3349-8568-6e00135a69a8 | -12.02261 | -49.70864 | 2025-08-31 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43c475ce-2974-30a6-92cc-c72d791022b3 | -11.31637 | -43.68293 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb57eb2f-1257-3b33-9418-7350bd187ac6 | -13.57602 | -46.91557 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b758baad-c125-3f22-8a34-afe6c733cda7 | -9.68656 | -47.04544 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9a2663d-4135-35d0-9ac8-d806abbf8e31 | -14.55226 | -51.98551 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa6cc3df-86a1-32bd-9be9-e7a3c7e687a2 | -13.50562 | -46.97117 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e76f14f-7e59-3422-8bff-c79a28b97b2f | -14.23528 | -48.05899 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 354ca88c-f2b4-3041-b76d-8ad0db73a7c5 | -11.01589 | -46.95956 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1abf5a6a-2cf0-3f2f-b7c0-5cc6cd104273 | -9.32085 | -48.51551 | 2025-08-31 04:29:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f9e1d65b-ee59-3c10-9c80-1bd88b3f1e65 | -13.34538 | -46.98611 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b77ce8be-386b-32fe-b28a-0c8da10907b8 | -13.35033 | -46.86559 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e10fd498-cbcb-3eb1-9f6d-2b9217420527 | -15.94237 | -41.40084 | 2025-08-31 04:29:00 | NPP-375D | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0c5c6afa-c9d3-3197-bf22-14911e60fa98 | -9.68213 | -47.0519 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a602fa4-9d3b-3053-90be-95a442228919 | -14.03378 | -44.57136 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1302c83f-c93d-31ca-8b4a-2cb2bbe19279 | -11.29903 | -43.566 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76632fc9-97db-3543-abff-59f952bbc131 | -11.02248 | -46.87401 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0360f7f-75aa-3490-bd16-8efe5d30665c | -10.04018 | -48.09112 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8a749676-c24c-30d4-9b70-d1565a8b3011 | -13.34147 | -46.945 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 953d9725-aaa5-32cf-a6a2-7aafe089f330 | -13.47881 | -46.94489 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5fed1b3-b1cb-3920-a5c7-a8c8f2019c8b | -13.39703 | -46.83909 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7a8172d-98c0-3a3d-921f-dc021e24affe | -10.61051 | -44.90273 | 2025-08-31 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88761a36-c080-3d35-9b8e-87af76ad1cbc | -9.74696 | -47.13773 | 2025-08-31 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9ab2458-be41-3a46-87c9-581436fb1c4a | -13.50228 | -46.9706 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bc4c7e3-d0a8-3dd2-8456-e23cf8df4dd5 | -11.81162 | -46.43541 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5146988b-4b08-3419-b62f-ecbf43ba759d | -10.92987 | -46.84141 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30666f05-e9af-342d-a27b-d05970b9f220 | -14.9918 | -46.71096 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5d4afde-ae63-3a4d-a331-bb0e979d9990 | -11.88772 | -46.35523 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd35786e-273b-3a59-9d6a-5a05a015ba0a | -14.22081 | -42.79807 | 2025-08-31 04:29:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 57edc402-2770-335a-a5a2-2a5fae19d899 | -12.55833 | -44.79821 | 2025-08-31 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c5eb69e-5b9d-3164-b7a3-c547e5a76cd2 | -12.63563 | -48.20072 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc053752-f079-3f7c-adda-3e54f2fe72ea | -13.68018 | -46.87343 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 929ff259-eef6-3426-a618-6b84b49f3b6f | -9.95909 | -46.34831 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 605f9bf6-f593-3454-af3a-c3c94d7f44fc | -11.90933 | -46.6921 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 044f73b9-6ff2-38b6-b5c1-b04a055dd9e3 | -9.47165 | -47.60849 | 2025-08-31 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 861aa79a-8e9c-3a86-a249-d2498071306b | -13.35764 | -46.95134 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| fd09106e-be57-3216-8fe0-5e7b8080226f | -14.32582 | -51.86288 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66fd0b16-94b1-36d0-a97d-ce98704d7339 | -13.02424 | -56.88863 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96de3b79-f6aa-3381-92d2-094a2f9713cb | -13.53913 | -46.95417 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b26b5b6-d304-34ea-b55e-13c56095851c | -11.88882 | -46.34809 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1b794da-5ad8-3c59-8417-62e2ea97e2b9 | -11.35324 | -43.63866 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6bcc9f6b-251e-3685-ac22-e66aa911b944 | -11.33009 | -43.66693 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57a9dcc4-69fe-35d5-b083-43a5e1e29fe3 | -13.97415 | -46.32151 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b8a0148-42fa-3a63-a5be-bd1339dcdea5 | -14.27896 | -51.8876 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85c07515-c4b6-3733-8edd-7ceb62ef2370 | -11.36345 | -43.54319 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb78380d-89d3-3228-9430-5e1d268da085 | -11.0761 | -52.0403 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edc42263-f555-38be-a248-add8d4e09f89 | -11.89673 | -46.3861 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| dc232d5b-1072-3f9e-a80f-0923356f1f4b | -14.22694 | -48.06856 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5196d7b5-f0c4-3ead-9f72-40f0fbc06510 | -12.85718 | -48.08408 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8a8c6eb-3c6a-3d54-aa36-ccb185794f28 | -13.3938 | -46.94937 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0eb2a717-d0ea-37ae-9f1b-009281cc84a3 | -11.02693 | -46.88918 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef65e09a-cd32-3b19-a835-9ec12773fa22 | -13.36231 | -51.7495 | 2025-08-31 04:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd5238bc-db78-32ee-995d-0dd9a4faaada | -11.83595 | -46.49044 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1be7c44c-6694-375a-ba5b-0dca60d2edca | -9.32081 | -48.51591 | 2025-08-31 04:29:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| af29dc09-8323-3172-83f0-80422492cc0f | -13.34363 | -46.86454 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62bb9209-2930-3831-b1ab-3116587b01fa | -12.87242 | -48.15972 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8891abde-6f26-30a8-ba6f-25bf39dd9c1c | -10.66995 | -46.27058 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8279060-262b-3890-983e-a5afd27189c2 | -13.36201 | -46.95535 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94a61dc3-97e6-3c64-ab59-b2e210e583ec | -11.81387 | -46.44311 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 28223e81-1c45-3a92-8176-79e241a3e018 | -11.57477 | -49.51575 | 2025-08-31 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84ce4f5d-7efb-358c-9b74-e879d5765ff0 | -12.62954 | -48.19603 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17d4a92c-6e2b-3027-bdae-2d98dabb558c | -10.73282 | -46.13038 | 2025-08-31 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 15f08ee0-aba9-3e6c-ba75-385c6420ea3f | -11.33027 | -43.63969 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8b61060-a574-346a-9064-8f6798600254 | -10.6143 | -54.92241 | 2025-08-31 04:29:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7509ca52-1aa5-3f9f-bbdb-17189c0e55f2 | -14.33463 | -51.87877 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7eaaa76a-9802-3202-a28b-e3b29faa8ce1 | -12.63011 | -48.19247 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9857bcf-cb62-34f3-baed-5ba0a31725be | -14.37614 | -53.05747 | 2025-08-31 04:29:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d207735e-d10d-324f-a2a6-946d074b20b0 | -11.36665 | -43.59935 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09c9db27-6b46-3367-9979-5cf8c4c465cc | -11.0247 | -46.8816 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63e58a53-2ec0-3348-98fc-86a173f59bb1 | -10.47144 | -51.63915 | 2025-08-31 04:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e68769ed-183c-3716-8f35-6b21c11d4883 | -11.21261 | -45.042 | 2025-08-31 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a11c541-c0a0-3e14-b9d1-0b7c5ecfe682 | -11.90378 | -46.70576 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e996f73d-c609-33c9-a422-d38c851d2cc4 | -11.81794 | -46.42883 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8ca9359-3ebc-30a9-885a-65bad251ca1a | -11.83377 | -46.52682 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 588d5e8f-73f8-35dc-aab6-554496266df7 | -12.63276 | -48.21856 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35e60bda-3533-370f-99c2-9cb76d48664a | -11.83136 | -46.43095 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5da62277-1d3b-33d4-8b77-011327cd7167 | -12.40774 | -46.46558 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b3e2b47-f831-3c3c-9743-38450a25b2f7 | -10.17884 | -46.58088 | 2025-08-31 04:29:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75059bca-6912-38e8-93e7-a69a9d279840 | -11.02367 | -46.99689 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56d3061d-d9f0-35f8-bb3c-6114cab34377 | -13.30963 | -46.88461 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e201e83f-0b3a-37e8-9705-5f52ca092475 | -11.34341 | -43.62786 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 265833ff-47da-3800-a5db-224fd7c17505 | -11.02415 | -46.88512 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd6415a6-0236-31dd-ad4a-3bf3c3dd8cfc | -10.94556 | -50.79099 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad14482b-6f30-3564-be37-02ccc2c80096 | -13.65557 | -46.92148 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b00c1f2-3f69-3992-b642-96c919d3b279 | -11.35457 | -43.62961 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a9d625dd-3ae6-36d7-a5ef-541edeb6151c | -13.30519 | -46.91336 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43c4e15c-05da-36b6-9807-a584b95172d3 | -12.56901 | -44.79985 | 2025-08-31 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df702431-b651-344d-93cd-450e9a75249a | -11.42192 | -46.91256 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 404bda70-5307-339a-a697-dc5b6f9ca615 | -11.91468 | -46.40355 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9650d17-e04b-34f5-9563-d017e2159a5f | -14.04125 | -44.54588 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61cf1b6b-ed10-3d47-afb9-1953525a68a5 | -12.39599 | -46.47482 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b1024a9-b68b-30e3-b2ee-fed092b0c5c1 | -13.46383 | -46.97522 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3572998d-a389-3251-8212-10dddd832397 | -9.54326 | -45.84285 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8233cc32-556d-32dc-9b19-db3733fc5aea | -13.35932 | -46.94053 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc5bf43f-2db8-3fd7-bd67-e663065cf904 | -13.53745 | -46.96502 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b9347eb-d201-3141-b88f-7935964e8702 | -12.40046 | -46.46814 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be3c6c10-aa34-30b6-a583-10b00c73dbff | -12.75224 | -44.41253 | 2025-08-31 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README47.md)
