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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6019cfbb-043a-3827-93e1-223607ea9590 | -13.90054 | -48.09168 | 2025-09-02 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adfa8cbf-901a-31d9-a5ed-e51bb1cdea3d | -8.85423 | -52.02079 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1da7872-1a8d-35aa-b82a-3a9b27176e76 | -11.6448 | -52.04882 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98516e5e-9815-364b-af78-0fd0decdfee3 | -9.19729 | -60.2487 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c6d13b7-51eb-378a-9598-8d64e1c6a868 | -13.31157 | -46.84297 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 920c3f09-fb83-39f5-ba5b-ff39f73f6ec4 | -11.65636 | -52.17349 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| de8bb796-6885-3e27-99ec-2b8ba25d4655 | -10.05779 | -48.14637 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfcd17e0-1262-32fd-9bfd-6f5e34e2964b | -12.9191 | -56.96231 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f41fcd43-ef21-3f95-b4fd-a18815757ebc | -11.79835 | -46.39892 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 17c6aca9-02a6-3049-b543-da8810cd535a | -14.60701 | -48.04381 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cafec794-20ec-347a-9ee2-a558c4d2846d | -9.83869 | -48.61202 | 2025-09-02 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbf273aa-88ca-343f-91aa-a288736361ec | -12.15785 | -60.76093 | 2025-09-02 05:06:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e13a80df-0cd4-3c2a-b3cf-ca09e87dad5e | -10.45069 | -54.77002 | 2025-09-02 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5ed268d0-6efc-3769-a2e8-3f72659adc7b | -13.10668 | -56.80366 | 2025-09-02 05:06:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a77670aa-c311-3674-9e93-d0bd0a0112ff | -9.83179 | -48.31356 | 2025-09-02 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d12d11e-4c62-3aa1-947c-b52b6d6176d0 | -10.39361 | -59.41526 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce5690d2-48e9-3e11-98b3-0e12b5a12a23 | -10.45915 | -49.05976 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 231cfbaa-fe3e-32d3-a758-f91d023c5190 | -9.27278 | -59.75362 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1c67758-262c-36ce-9a9a-6a255583d553 | -12.861 | -48.04854 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cdacbc7f-eaa3-3ce0-9916-c49b44ea31e4 | -11.66083 | -52.17062 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33debd24-caca-38e1-bc33-dcb44a6aad22 | -14.77279 | -48.15896 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39ccaf44-4087-3b0c-80be-2874f16d7a91 | -11.01322 | -46.82956 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2969b5a0-43b4-3f56-933e-121e423e3e58 | -7.67348 | -61.0836 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fc5c45ae-8fdb-3cd7-8130-52823d5aa639 | -8.65313 | -62.60392 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d62b962d-1a9d-3b5c-a54d-49be12a650da | -11.8626 | -46.71592 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a7238fa-2a4b-3410-8216-971835787c5b | -11.83386 | -51.54024 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 363b1abf-47f6-34bb-b9ca-cbeb5c09d083 | -9.08947 | -58.88702 | 2025-09-02 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb38f65a-66a8-3a7e-b910-20fe8a9aeaea | -10.4525 | -59.12539 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40806fa5-ae5d-3ee2-9f4d-dc2fcdcc14a6 | -10.0675 | -48.88623 | 2025-09-02 05:06:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b80d7633-db6e-3591-9584-975ea72712dc | -8.67696 | -62.39898 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e53aa2b3-3295-3237-9944-413120d116f6 | -13.32289 | -51.78931 | 2025-09-02 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01db2f3e-f607-34dc-bc33-27fd399b28d6 | -14.59542 | -48.04342 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2e27749a-95a8-3863-be61-254ef17b86b0 | -12.93398 | -56.95384 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e41fa4c7-c6a7-365e-b8af-3f8658646b27 | -11.66981 | -52.16475 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86a1e374-c6c0-3de6-ba5a-49ea921b29b3 | -11.07954 | -52.01152 | 2025-09-02 05:06:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c33ff03b-f6ee-3b1e-8fe6-e409d759f721 | -11.83853 | -51.53715 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 172f3917-10f7-3dda-8731-4684b9b01bb2 | -11.66883 | -52.17182 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 9ba08da5-9073-3ec1-90c4-f25ddcbb58b0 | -13.50562 | -47.00273 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15947a85-9c37-330a-9528-8dc548ddce92 | -9.83207 | -48.61488 | 2025-09-02 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22984873-9058-3827-a1c4-caa994039045 | -9.49631 | -57.80757 | 2025-09-02 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a319f12-4cda-3c78-904a-520007de2036 | -12.77872 | -47.66168 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 492ce62b-40e5-3126-87ae-cd79b95415ac | -11.86306 | -46.71184 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc75c2a6-e02b-38b7-b948-27d0ca46b138 | -9.73822 | -48.97725 | 2025-09-02 05:06:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8bbba366-3928-3270-924d-246c56b8874e | -11.09391 | -44.66115 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 01436bbf-a837-34e6-8e2f-624b1ac48ee9 | -14.76774 | -48.1547 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0cf2469-211f-3591-ae1f-2f78149b05df | -13.54239 | -46.9901 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b07fac69-141c-3ea5-8bf6-3954f195b8df | -9.75215 | -46.9404 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dd125c2-16a2-340f-af85-eb64aaadad06 | -12.59586 | -48.20594 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ff01b59-6be1-3232-8a70-53b266e9cd1b | -12.2803 | -53.59942 | 2025-09-02 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e09da66b-204f-35da-ad47-6f8dda31aace | -12.67405 | -48.21944 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1ad05b9-555b-3576-85ed-6674ce8baadf | -11.67592 | -52.20857 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 634788a6-3322-368b-ba0c-edebf3f60cd8 | -13.52884 | -47.00545 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5187e428-29b0-319f-b62c-76e080b54822 | -11.66736 | -52.18235 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7e562a6a-b191-3c08-82c8-d7f0018e4fd3 | -11.92632 | -50.61252 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06e9fd42-91a1-30e8-85a8-9bb2222ccd76 | -11.00671 | -46.83543 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| dd228cd5-a6e1-318d-a3be-d05b67b49020 | -11.68195 | -52.22364 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bb9319e6-6774-3cd0-acce-5d0b1f8bf781 | -12.4215 | -63.91116 | 2025-09-02 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b29666e7-c7d5-3a17-8d6f-8c356d5cc489 | -12.99057 | -48.11205 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33900259-cd58-36a1-aa19-5e20821ba2c1 | -14.48896 | -45.94931 | 2025-09-02 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8854c36-d901-3b38-b318-193c742f5972 | -12.91965 | -56.95878 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50e1f521-f142-3374-9869-01ee8d64b13d | -12.94006 | -56.95844 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07576e22-f163-3eef-8394-84b000e72fd5 | -11.67844 | -52.21962 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bd30abde-2dba-33b4-b4e2-dd1864905ccf | -12.79806 | -48.0738 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ce56900-82a9-38ce-9623-8cd9a3a2779d | -12.92241 | -56.96285 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a522f1d0-1481-3d0c-bf94-83c1d262f502 | -12.62056 | -48.18001 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 27fcb3a6-8c43-3d02-8ac8-70f256f8e51e | -10.28823 | -47.51077 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34ca1fd3-c5f3-3587-ae98-1ae7a1d7f2bf | -11.97495 | -45.88298 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3e857b5d-6368-3c04-ae52-542365acba1b | -13.53684 | -46.9903 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f893484-b4b9-39f2-a3c6-d1e607ae1d8b | -14.27376 | -45.24858 | 2025-09-02 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 84e16851-b940-3d0b-ae9a-51fac0c6da30 | -14.58218 | -48.06143 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04f619dc-3cff-3bb6-a2d8-dd0d0a366153 | -12.99019 | -48.1153 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adffee5b-321b-319f-a589-145836cb8d61 | -11.92405 | -50.61985 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c2e22b6-4247-3853-a463-4d22745cb3a7 | -12.96667 | -48.10099 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ed4cf84-0a19-3590-a1cc-9c57852c5e17 | -11.66337 | -52.18176 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e98af050-17c5-3c22-b201-5d96c21006a4 | -12.93125 | -56.9715 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88c528a4-e216-3c23-a190-b8161ad958bb | -10.27694 | -54.26603 | 2025-09-02 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80244721-684c-34f8-8eed-c13b194414c3 | -11.65998 | -52.20617 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 22829806-5542-3e6e-92ce-e21853d3e3d5 | -11.02528 | -46.84866 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 599eb2cc-5556-3818-8bcf-9ae0dc92ad4a | -7.47651 | -63.82745 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9afa788d-6c42-3404-a1db-74f3badf1ae5 | -14.79873 | -48.22116 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 849a525a-46e6-3f38-9bee-d2e69f504975 | -12.99234 | -48.11346 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5632acd-c901-3291-80df-8222ea640851 | -11.93411 | -50.61217 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8a02fbb-3532-3b6c-9da0-ad84aaa80983 | -14.8002 | -48.2213 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5065bf07-6ed8-3b7e-be31-1ab0781a1392 | -10.05865 | -48.1398 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 267906c6-22d1-3217-bbb1-c859cf42589a | -10.75959 | -49.56909 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5b60e848-3e74-30de-b0fe-7dac40d70f40 | -11.65889 | -52.18465 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 72404c1c-a0f0-3fc7-b16d-64ac45698d8b | -9.76065 | -54.76752 | 2025-09-02 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe1fac86-0464-3a0b-9210-f7e96ae932e2 | -7.90072 | -61.52274 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0935fcf6-858b-3ae7-8fea-9f7777fe75b8 | -12.98337 | -54.75367 | 2025-09-02 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26b42172-da10-38d4-ba1f-84b7cb8ef3f2 | -7.47682 | -63.82552 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf40944b-3bff-3c39-90aa-43c40d044af6 | -12.99201 | -48.09973 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8bc51670-80fc-3137-a1d1-c1bd4efa1ed4 | -11.65188 | -52.17636 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b4472ea8-7c50-3b5d-9d77-b6123541a5a8 | -11.65599 | -52.20554 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d9bb2fbf-dceb-36fe-8210-b4b9476e0087 | -12.87865 | -48.06269 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba863162-29a0-3e8d-9fb4-cff3c961501c | -7.5938 | -61.63316 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40f0d477-54f7-3714-8be9-0576e20a6302 | -11.09456 | -44.65546 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 612d5ac4-b94e-3055-8927-a4550583ec07 | -9.34751 | -65.42587 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a3ca73b7-5353-38f3-b30b-0064db425a0e | -12.99313 | -48.10712 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29ecd0fc-02be-3cca-b7fd-aa63d776a64b | -9.83375 | -48.6112 | 2025-09-02 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| af84b49b-9a92-367d-b4b6-61232fa8c0df | -12.34028 | -45.6785 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README65.md)
