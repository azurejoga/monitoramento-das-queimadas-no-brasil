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
| 09e67fe3-3df4-337c-a573-61bacc31894d | -11.0953 | -44.68336 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f718149-2f21-3a4a-bf17-47d6890b1ffa | -14.59795 | -48.05237 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76ec26bd-8340-3888-955a-56cf8675e371 | -9.73454 | -48.96984 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5f5bad2-2d44-323b-9ec0-e8e5f7dbe457 | -14.59924 | -48.04602 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7addf82e-a6c0-3c84-acb4-0deda54e895f | -8.81679 | -47.83798 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c28af5ac-167d-30b4-b0ff-8b5ff5a063fb | -10.04917 | -48.09969 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| afb020f9-1644-3d25-89e7-7216b1a45e37 | -11.91311 | -46.45392 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a5660b61-5407-332f-8d21-565b6c82ba39 | -11.65314 | -52.18965 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a890aa6a-26ac-3587-87c0-c452006e7554 | -10.80303 | -46.33769 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 57d180b4-abaa-319b-8161-2d484f5db256 | -9.47482 | -47.60802 | 2025-09-02 03:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc197e05-bab8-322d-829d-84ade35885ad | -7.91718 | -46.45105 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 922af6a7-0dde-3c45-a249-bae0fbb1bc4b | -13.28327 | -46.89178 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddeb991f-2d3f-3966-881f-61877be21e44 | -12.0691 | -45.81037 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbd18b3e-0cf0-3bdf-bad6-e46f565be699 | -7.49549 | -45.35447 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e22439a-e255-3e58-9d6d-350588c4e070 | -11.10488 | -44.65593 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d621d753-3e70-32dd-9ae6-ae811e4b5db5 | -11.80999 | -46.40216 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4722c763-2bbd-3b05-8ede-f9bb698a6f85 | -11.66667 | -52.16179 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f21a779b-e636-3770-b080-f6944f7baa0b | -9.83343 | -48.61716 | 2025-09-02 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ba90f72-70d9-3bb6-bf0a-3b3ba6926782 | -13.7031 | -46.88804 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5055cc95-c466-30eb-b1ff-5b1098616efd | -11.10501 | -44.65421 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45e4b886-2616-37a2-9338-39e837382847 | -12.62164 | -48.18798 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7aea0080-7d8f-3943-accf-9d9ba1a0401c | -10.04761 | -48.11514 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9cae48d4-234d-3d00-9eb5-fa8e27e4cb7f | -7.69211 | -50.27295 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 028c5592-793c-3f03-ad94-779a5383ad75 | -13.34023 | -46.95152 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf4fa4b2-ca09-3928-954a-08aa1a03c823 | -11.04663 | -46.89859 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba3b66da-2a4d-346d-b5e7-19c7c3dee655 | -7.47765 | -45.36644 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5546f5c4-ef9d-3cc0-baf3-da1c51ab081d | -9.74163 | -48.96622 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cf9a94a-9927-3c69-ab10-49112109cb45 | -7.98108 | -46.47409 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9e9ef3cf-db50-3c53-b575-d8193de6e1e5 | -13.52977 | -47.00676 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bdc288d-fc27-3180-8470-cb0ce8ad1b27 | -13.69526 | -46.87451 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10025c79-b52a-392d-bd0a-f3bfaa776518 | -14.60032 | -48.0682 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1e8b6bdb-67c0-3bd0-8d3a-b367c3c3bbbf | -13.30404 | -46.83965 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60d5a9e0-4129-3e65-8d52-353c0bfdca31 | -11.65428 | -52.17461 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d9181d6b-17e4-31ee-81a4-220715ce6466 | -13.53155 | -46.99761 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d78d938-e0de-3c50-a69f-d5eab4e92ac7 | -10.66851 | -47.33138 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3eac5f4-9b76-3047-a442-9241492d6b40 | -14.59391 | -48.04487 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d31e2e87-c6c3-3fcb-94e8-f3c9e87bf212 | -12.57923 | -44.79416 | 2025-09-02 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f2dded1-0ef0-3ea9-bca9-ce877b5840cf | -12.85372 | -48.05552 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4fb5d232-1443-3c1a-84c7-d221078ee6b3 | -13.69235 | -46.94445 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 258c6a2a-0e84-3780-bba3-f810738d5dab | -8.74537 | -46.12742 | 2025-09-02 03:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23602bc3-5f88-3a7a-955f-f50326377f73 | -7.92445 | -46.44185 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20f1e6be-bd83-3249-be7f-e56d1b8586f7 | -11.37908 | -43.61404 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21851b96-302c-398e-ad84-b9232fcafcba | -9.1148 | -46.04995 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e49ae2d5-b247-366a-a36c-3199bd139e7b | -11.64961 | -52.19678 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| b520be62-3029-308a-aafb-d4e461794b6b | -7.72339 | -50.25401 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ab3ea21-85d3-3e35-a95c-f6ceeb9305cd | -13.68789 | -46.94032 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fee6d1d7-a32b-36a1-bb51-58d6535d7887 | -14.26078 | -45.24319 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24562cfc-a3cb-358f-b571-24ae1da1ac47 | -12.79823 | -48.07536 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eaed3e0b-a17e-36f8-a376-ddb4bcc05635 | -11.48187 | -46.79471 | 2025-09-02 03:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3be462bb-4155-3586-9ac0-686647bbcc70 | -12.87059 | -48.04951 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51683d5b-9217-352f-a82e-bff12808b228 | -12.61912 | -48.18534 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 31f93c53-f785-3c28-a84b-d43a7072fe13 | -11.66802 | -52.21625 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 8f66c8c2-e8fe-3bff-a0d7-2a84fbfd3e9b | -11.80483 | -46.40183 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ade7c427-4f8b-3446-a841-dd8686990640 | -7.53654 | -45.35921 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d74fb562-39fe-30c2-b92a-c9b52bfe8772 | -13.4976 | -46.92857 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9613575-3635-339a-85b2-4946c3f6a57e | -7.8524 | -46.7429 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d269cf55-42c8-33c1-b47a-92b15c2b5873 | -10.73554 | -44.80136 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eba0c05a-8156-33d6-886c-7da0be82831c | -11.67574 | -52.17939 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4daba964-714e-3b36-b8c2-a7af717fb461 | -11.64994 | -52.20436 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| a1c1b77b-2f9f-3dbc-bce6-7ba377f524e8 | -9.83463 | -48.61754 | 2025-09-02 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c59ba2f-4a33-3f56-88ea-4a0ae69c0d27 | -11.66303 | -52.16859 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b0c6800-6534-3888-9a06-7d060db19c9d | -12.57112 | -44.78788 | 2025-09-02 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 725cef0c-9c66-3896-b062-c126ad233110 | -14.04985 | -44.5972 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f29d33c7-a9c2-34b7-9e6e-93b2445119d9 | -12.87375 | -48.06244 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ac55c82-cff7-3e51-bc4f-ce2f6af5662c | -14.00384 | -46.31185 | 2025-09-02 03:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa5ff73f-36e1-3882-b413-03f38de88dae | -12.61835 | -48.18938 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| aaf293c0-4d3c-3433-a6d9-a90d5e24a123 | -11.1074 | -44.64178 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7ff1b642-3db9-30d8-b1e4-1f7bbab883f0 | -14.73703 | -46.75216 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75612952-769b-3464-8ee6-cddf7901d187 | -7.98847 | -46.46447 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9389901f-a8a7-3698-86a3-2f15da6c1cfe | -12.33212 | -45.71638 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 14bb01f7-ce35-359d-8e7b-dac74f32959f | -10.05191 | -48.12433 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 66435bd9-309d-3461-9ab4-d23d10f43980 | -10.258 | -47.53003 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2aa8490-4244-3422-9ff7-d28f7f8b6fb0 | -7.48165 | -45.37346 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a873e687-2c00-3268-9821-ee7327bf9ee3 | -13.48557 | -46.92302 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 824f646b-60c3-33f8-9208-b7fac515620c | -11.55033 | -44.84075 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7f1f804-b412-3b5c-b8de-c4a414c1f934 | -7.99138 | -44.04563 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e87e1bd2-c7ed-351a-a88b-56db76107567 | -11.64551 | -52.18065 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| faff0da1-7864-3b63-9582-1c234a06b6a8 | -11.48296 | -46.78802 | 2025-09-02 03:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c534743-62ec-38b4-9120-69e2c4c58c92 | -13.89827 | -48.08083 | 2025-09-02 03:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 192cb220-2073-3781-8ff9-410c2196dd8c | -11.79411 | -46.4032 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 78486aac-399e-3afb-8774-8ce533c4a155 | -14.73808 | -46.74664 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98ee58f5-0348-3f95-aa89-2f73eca104ac | -11.09291 | -44.6441 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| fdd5abfe-194f-3861-9c2a-c5773a15d6ec | -11.02412 | -46.8513 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d6f627c-d1b4-3464-8433-9228096a632a | -12.85914 | -48.04949 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33bc1813-9a04-3b22-a311-fd7504baf645 | -11.3719 | -43.5561 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4a02259-3734-31cf-a69e-56f741fc1397 | -11.65793 | -52.16758 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fb37e0fb-1d00-3d9b-b05b-0a48138da3ef | -14.71876 | -46.75032 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44235d9d-6991-3675-a00b-344a1e28acc8 | -12.95777 | -48.09682 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 257af15b-5021-3856-8edd-d7e30d18b238 | -12.92795 | -48.10773 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 352204d6-e02b-3d1a-9882-a9a6178312cb | -11.97544 | -45.88182 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bddedc6c-0231-371d-b53d-0e7145965fb2 | -14.27418 | -45.25373 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 86f87e70-8037-39ac-908b-e360299c9284 | -11.91888 | -46.67593 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dacdf2d-fa0d-3c54-b298-a7462baf11ff | -13.53274 | -46.99146 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6122135a-df2a-3193-b644-42c1a83a06c7 | -11.67546 | -52.22527 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9e76eb7f-209a-36cd-ad6d-d38d72ed4e1f | -7.98177 | -46.47041 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f36a5ea8-9061-3347-aa2e-5add88e2b68d | -8.83288 | -45.79078 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a74bb75-a4ac-348f-9139-f737501740ee | -13.28254 | -46.91058 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33572ef6-882f-327a-baa2-46c9381a9c06 | -11.66036 | -52.19092 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| d54a2bf9-dff8-3744-8324-01ab579e11be | -9.47409 | -47.61195 | 2025-09-02 03:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c84abfb-c7c8-3344-b52e-8698f8cd4b58 | -9.25375 | -40.51657 | 2025-09-02 03:51:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README25.md)
