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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da486ca4-dc8e-3c5d-9a8b-7896e4744bd7 | -9.68269 | -47.0484 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bb50ed2-88ac-38f5-8ab4-174256ddbf2d | -13.02753 | -56.89965 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98c1f59d-2432-3db2-b354-a0b58928cce9 | -11.90072 | -46.42708 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7206cb81-5dfd-386a-a3cc-41c285b41e9a | -13.01126 | -56.9057 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55304ebb-5005-3e09-a100-4a0712a5b81d | -13.46664 | -46.97928 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21f0a6d9-c0ac-30f5-8cbd-15b3fe480fed | -10.0396 | -48.09468 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 35fd816c-9f3d-373b-bf9e-bd960472fcbc | -13.47053 | -46.97625 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6bbd0379-fd1d-3923-9427-9804351908d6 | -11.78152 | -47.40059 | 2025-08-31 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 730436d1-11b1-3a10-a606-5aa6329d9c26 | -11.83861 | -46.42849 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b324af4-77d2-32fc-bb4a-c6f33af23b3b | -13.33479 | -47.01015 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 039f3b64-ec94-310f-a71b-5030bebc485d | -12.87381 | -48.0869 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1532f317-359c-3762-b415-3e6cd11dfaf7 | -13.34594 | -46.98253 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bbb9176-50c1-3916-b8c1-d8700bc30ae6 | -10.92932 | -46.84493 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 391c6441-2851-3fcc-872c-840499029a12 | -13.40439 | -46.94741 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffe927e1-dfce-3a30-97a3-ae7f28a8cddc | -11.07646 | -44.62914 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4324927b-342d-37ac-96dc-7b19f8121fd2 | -11.06727 | -52.04409 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d28cf1be-1392-3105-83ee-d716bb70cc7f | -12.65278 | -48.22188 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be21a862-c285-3def-84d7-56fa4b8b10d3 | -9.62103 | -47.80024 | 2025-08-31 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af20e35e-25b9-3f53-ac77-5ea92dc25db8 | -10.42193 | -50.86517 | 2025-08-31 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e8ea33a-8e71-31f2-8b3b-e6d9dfb8c836 | -12.40438 | -46.46505 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7a05eab-530a-303a-9ba2-02556d0a6c98 | -10.23996 | -50.84302 | 2025-08-31 04:29:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4748f580-2caf-320e-8667-fe8a6effc550 | -11.82635 | -46.44116 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fd2c98f-40c9-313a-9621-c04f5e4842a0 | -13.34315 | -47.00045 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbed6a82-c9db-355b-9926-a9709680252d | -13.0223 | -56.89841 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc80108d-4fe8-3433-8c5b-520d4b6c8318 | -13.02302 | -56.90149 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52b49cbb-52e5-3e5f-a4a1-fb2da07bc0c6 | -11.81609 | -46.42878 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f149d4e7-45c7-323d-bfb7-d0a252373301 | -13.35318 | -46.95796 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9599bb2c-b5d9-3a02-b94b-953f88ccd234 | -11.82313 | -46.5068 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f872f38c-b1d4-3d8f-96b9-f57a1f42b637 | -13.02035 | -56.90821 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a6ade4c-1087-3cf3-87d0-c9b327ce3669 | -10.10327 | -49.28469 | 2025-08-31 04:29:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46e1c17c-19a3-399a-834b-1e2d3d81a2ae | -11.07765 | -44.62114 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6b79c5e1-5396-3cf1-87ef-bda8757eb779 | -12.82096 | -48.08126 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b5cb6ba-9454-3014-8952-9b65bdb4096e | -11.35523 | -43.62515 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5ec8778-5c26-3f95-8413-8ddef7e79f9b | -12.64115 | -48.20897 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8679e278-f1a2-333e-bcd8-6c4fc302ad85 | -11.06761 | -44.63999 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6db495c2-d44b-3e64-bc82-dc68b992c8af | -13.99061 | -44.53388 | 2025-08-31 04:29:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33e8b92a-d978-3765-b1dc-5fdbdc5ec1ed | -11.07999 | -44.62967 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e69f8fc-b9b2-313a-b587-d6c62ae60bf3 | -12.4919 | -53.83406 | 2025-08-31 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37d70907-c46d-3468-a963-e38a6c05f3a9 | -11.83191 | -46.4274 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d033457a-592e-3c24-9dbb-79f7304d9be4 | -12.1791 | -50.09461 | 2025-08-31 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b992549-20c7-32c7-84d6-c0c76257cee1 | -11.21612 | -55.06501 | 2025-08-31 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e254046-a819-3546-87db-b4e94cbb4fab | -13.4921 | -46.83572 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99235eb3-2caa-356c-a159-bfdd748e2642 | -10.03585 | -48.08643 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 866b13fb-bd6e-3ece-b19c-2517ebf35546 | -11.2149 | -45.0267 | 2025-08-31 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d734b88-cbcc-35c8-9455-c75a38349451 | -13.50608 | -46.83421 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7519e444-c1cc-344d-bfcb-186604ce0db4 | -13.02239 | -56.90477 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f7d62fa-eb20-3153-8e6e-f88f9ef0aec8 | -11.80156 | -46.45596 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08ae7ab4-c95b-3aaf-aad2-9c1fb082985d | -13.334 | -51.77784 | 2025-08-31 04:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09914607-a5f2-3b8b-b4ed-e1776e2cf9c7 | -10.96097 | -50.85756 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0a00eb36-08d4-3373-9f89-efaa6b601321 | -13.31968 | -46.88622 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9724f316-f4bb-3fe2-99a7-74751cf8af32 | -11.88376 | -46.72455 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e35207c0-b5d9-38b1-a491-72e429cd234c | -12.83577 | -48.13857 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5628747-0207-3a11-bdd7-7410edfc93f8 | -10.95802 | -50.85246 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 10bbda5e-0c7f-30c1-823a-e43f05f8c879 | -11.36359 | -43.59423 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0384a314-cd2d-3f49-ba1c-586d07f698fa | -11.06408 | -44.63947 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6189c6a3-d175-33cb-92b5-47f1d4cddf11 | -12.91376 | -56.98294 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8097fd8a-6d90-3317-b1e1-2c03a2348794 | -14.03743 | -44.57194 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ded7ec14-ff3c-31df-a7a6-d2e3ad24fda0 | -11.31702 | -43.67849 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cf25247-d20c-31b9-ba85-6e5264147113 | -13.48775 | -46.95362 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f0e80af-c250-37e2-8e22-70e3829944f1 | -14.13783 | -47.05664 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cde989a5-5cbe-37d0-9ae9-fdc9d71e7729 | -12.80204 | -48.09272 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92e6c60a-78c6-3e72-8a9e-a0c4ea048b01 | -11.35894 | -43.62576 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4197a1a-9678-3dcb-9ca8-9abb4106d3ee | -14.26025 | -48.05218 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9594a92e-b254-3873-a632-682a36158a5a | -11.91132 | -46.40303 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 593e7a62-1f2b-3906-8320-e7d2f0fb4d56 | -11.35033 | -43.28807 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcb25efa-577d-3d41-88e6-1595365c0cc7 | -12.91763 | -56.97675 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da9e1d0c-432c-31bc-9b00-05d0da61a560 | -11.05996 | -44.6429 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4104708-1465-39c9-99af-1b021687413d | -11.90009 | -46.3866 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bff3b726-463f-3408-bc48-e325a9c9ed65 | -11.07945 | -44.60914 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b719fdc-425b-3dc8-8352-1deb9f97e7c0 | -14.83681 | -46.74726 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e99b11fa-4a91-3c28-90a1-06c9ad45160e | -13.67909 | -46.92494 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0105e4a4-f7ab-3270-9dfe-b0c6d4d014ea | -12.83187 | -48.14158 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9801b328-6f7f-3d37-bcaa-28ff4693db4d | -13.49601 | -46.83261 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e7bc5b2-7b85-3b79-aab8-61ed7a952374 | -14.22581 | -48.07569 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b47786e-d726-3c00-8a34-11a0c5190d5d | -11.00757 | -46.94741 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9635825-04f1-3874-9197-256ae75516b4 | -12.92971 | -56.98596 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9eaa68c-162c-3c8e-872f-77f162c35312 | -11.36279 | -43.54773 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8155a9f3-5a5a-315d-9244-36c1c2fd4057 | -11.07885 | -44.61314 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6259806e-bb47-3ff8-aa5d-1a7ab21f9be5 | -11.81553 | -46.43237 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2403cc7a-777b-3dd6-a801-388c08752c6a | -11.86387 | -46.48752 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80a60a8d-c57c-3aaf-b4d8-cf3eac13a5e4 | -13.98887 | -46.31636 | 2025-08-31 04:29:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58a6f2d5-cdc9-3a16-a03f-0c81c05e634a | -13.65502 | -46.92502 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d044a35f-e86c-31ff-9560-c1b70dc77ece | -13.33692 | -46.86348 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fa8040f-0627-3ad0-a5b7-5352d1ca9be9 | -14.4919 | -40.48404 | 2025-08-31 04:29:00 | NPP-375D | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c9a6487d-9b74-36cb-a122-935927541f64 | -13.34942 | -51.75655 | 2025-08-31 04:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f08f9f21-6c7f-3059-9867-d2959a5bf1bb | -11.77819 | -47.40004 | 2025-08-31 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c561853-cf43-3336-a13a-f6076ab351d5 | -10.66715 | -46.26651 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72b25b92-5b29-335a-88e6-800c5442d417 | -9.4497 | -62.3485 | 2025-08-31 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 7208d7d9-c48e-36c0-8e0b-50521a55dfc9 | -6.7093 | -51.4165 | 2025-08-31 04:30:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 6fa7327f-ceca-3288-834b-c8435be78629 | -7.0951 | -44.3128 | 2025-08-31 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f753760e-b921-3992-9f4b-c34febd090c0 | -9.4495 | -62.3675 | 2025-08-31 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 3afeb586-6180-36fa-8937-f3397f5ce406 | -9.4432 | -60.5692 | 2025-08-31 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 354032e4-7b0c-3c22-adaa-be1a9dd466da | -9.4498 | -62.3294 | 2025-08-31 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 89.2 |
| f109e20f-59dd-3acd-8fa9-fe927203ea73 | -9.4684 | -62.3286 | 2025-08-31 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 087ecc7f-f7ce-3c62-be36-dd297b35f582 | -9.0614 | -65.4355 | 2025-08-31 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 9175a095-9486-3a39-929f-b47449b6bae8 | -9.4683 | -62.3476 | 2025-08-31 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 12b5cca3-bb97-3450-8a4a-97b80c0d6bab | -6.1667 | -43.3039 | 2025-08-31 04:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 52.5 |
| e1415bbe-9221-301e-8e4f-1b74fc9f05bf | -6.1665 | -43.3273 | 2025-08-31 04:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 11cb2a3f-7a11-37e9-9a2f-a0ba4e5ca883 | -16.49479 | -43.65395 | 2025-08-31 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c28a7c40-0e37-3976-b2da-42a19d87419c | -17.15117 | -46.08415 | 2025-08-31 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README50.md)
