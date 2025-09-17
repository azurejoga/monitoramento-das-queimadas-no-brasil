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
| 79a824ca-dfd7-3cb3-9917-e0061b4d6a48 | -14.82037 | -48.10848 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9130bb2d-3bd6-39ad-8920-c50add41f19e | -16.69615 | -54.96659 | 2025-09-17 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 174a6f9e-f997-392c-97b5-b79b4c055ac9 | -14.85878 | -45.12188 | 2025-09-17 04:34:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1e0e4f1-8a7d-3e79-8d28-c96823ed344a | -14.83037 | -46.7135 | 2025-09-17 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 965e61f4-6479-3a56-a755-7b6b8c4ac408 | -12.69657 | -47.76197 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67fdf102-7b0f-3ce6-b234-b379f9725fa9 | -18.19241 | -44.54156 | 2025-09-17 04:34:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e32a573-1f7b-3bdb-be73-49070229f10c | -12.74787 | -47.95782 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1194981d-78c4-3a9c-8b7e-919660dd11ee | -17.55891 | -43.79191 | 2025-09-17 04:34:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb0abf83-8be0-308b-adbc-27163419fbc8 | -11.07072 | -49.75972 | 2025-09-17 04:34:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f44e0c0-58e5-3450-b148-94b11f9982b9 | -15.12725 | -48.66373 | 2025-09-17 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b03db3e7-ed3f-37bb-bf3c-03178b867f93 | -15.98805 | -46.4425 | 2025-09-17 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3e76be5-fbe9-3f24-b18b-f7cb9b4bfa07 | -14.15607 | -46.13799 | 2025-09-17 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc4cde46-2a88-355b-a3bf-ee4e97f35771 | -12.35678 | -47.06563 | 2025-09-17 04:34:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fcd02f6-19a8-36a2-b71f-6ab1e9701a81 | -17.74607 | -44.43458 | 2025-09-17 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff40cb20-a2cd-38b0-876a-42665fe5bdcd | -12.7114 | -47.98187 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f597c8f4-a735-3c6e-bf13-fbe843dc04c3 | -13.20773 | -46.77869 | 2025-09-17 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25205c3e-c1a4-3c64-8c8e-075e9d954d71 | -13.22412 | -47.30062 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 640d2237-1680-3a81-9db9-5e5a18027fe2 | -13.21955 | -47.30766 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19962d0b-0b69-34c9-b997-ea9114d5c260 | -12.97649 | -47.94917 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc8030f0-215c-3f86-899e-b32c32f5009c | -14.62344 | -46.39014 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f2199d4-96ed-3dcd-9909-90c2808c6635 | -16.69661 | -54.96288 | 2025-09-17 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7432d1e1-5985-3e1c-9b63-44f0a505c10a | -12.84818 | -47.19802 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3673541-cb02-39c1-a860-74c091292e6f | -12.98714 | -47.94714 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dff98fc3-a2af-34f1-9820-178b9b56077c | -15.4129 | -46.1549 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1fd3cbc-eb44-3ba5-912d-69c033b7782a | -12.59348 | -62.96065 | 2025-09-17 04:34:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1315f3f4-77e9-3856-9be7-e0bc2a92d158 | -12.11476 | -44.8281 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e616b959-0907-32e6-9fc2-89ac4818e228 | -13.09 | -50.09238 | 2025-09-17 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 208a5560-4778-3275-bdf8-2bb2e51553a2 | -14.93964 | -51.67665 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15553277-2d30-3d3a-9e3e-1a77572632f6 | -14.81923 | -48.11608 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3955ddcb-b4ce-3054-8831-ac178edacd9c | -14.50097 | -47.36373 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5441195-6199-3ec4-91a4-2a2f091ae078 | -14.56785 | -51.46206 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 970ca7f0-a200-3eef-838b-8e1d3da271e8 | -12.70577 | -47.95115 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 97818906-d46d-3b59-a8b9-2e8c11233629 | -12.59205 | -62.9672 | 2025-09-17 04:34:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e5cea32-81b5-367f-ba8f-eeef05235319 | -13.32643 | -43.10382 | 2025-09-17 04:34:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fdfa0194-0cd5-35ac-89fa-28848d04c026 | -14.91753 | -51.70409 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fcbb3ba-38e2-30a6-9a57-c8f1932cd064 | -15.40839 | -47.32817 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01606fd1-13ee-33ef-afb6-6335e990598f | -12.6387 | -45.7436 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98674fae-7ac3-3fce-bd63-96533a4aa96d | -16.69712 | -54.9611 | 2025-09-17 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96b71680-6c43-3dba-beb4-38d44ef1020c | -15.1239 | -48.66319 | 2025-09-17 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f0a4a4a-f052-3778-b387-fb0329e0257a | -12.86145 | -47.13354 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8a31058-8873-33de-ad4d-a2093ec7810b | -13.08609 | -50.09539 | 2025-09-17 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f5fa3b7-0da7-34c2-a1e4-93407fde71cc | -12.98378 | -47.94654 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed15cb1b-8dfc-351d-8a77-7f737b34e4b7 | -14.91045 | -51.68325 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ccd3132-0d3e-390b-ab1c-d70c2face70c | -14.47134 | -46.35638 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a2cd097-6d73-38c3-b38c-d563861b87c2 | -14.85 | -51.68895 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98801b3a-b3d8-350a-91b1-d671b2c433bc | -14.91197 | -51.69527 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 3d918b06-56cb-3ddc-9416-2bbf07faffe5 | -12.7215 | -48.0058 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 155d07d6-3c15-3766-a4b4-9a0b2ac8ba6f | -13.15224 | -51.61554 | 2025-09-17 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 750f3b50-9d45-3994-9137-1a6d6d267a5f | -12.694 | -47.96054 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1abf2e22-42e2-3d26-971c-7881ceaf4ac4 | -14.9126 | -51.69146 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 472be7fc-dab6-3c0a-b349-f868f57a0f42 | -12.7187 | -48.00163 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 978b1690-70d5-3524-a835-a970ca422365 | -14.83912 | -51.69095 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e7c51e1-e924-3761-85c9-25c1660cc4f9 | -16.69322 | -54.96033 | 2025-09-17 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 730d8bb3-3af4-37e7-8bc7-3b3522984c7e | -13.21554 | -47.31089 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10a4a672-42d8-3ddb-be3b-05308ff80177 | -13.22234 | -47.28891 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef52876f-095a-331e-af8e-7590b445e6e5 | -13.70882 | -49.85538 | 2025-09-17 04:34:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2f845a5-3163-369d-acbd-a68714670199 | -15.69266 | -47.0141 | 2025-09-17 04:34:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20176b37-7c2a-3ba8-bf21-36accd7e0ab5 | -14.80003 | -51.67231 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6ea9401-8a0f-3eba-b775-29c1024d17f5 | -14.83724 | -51.70239 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61665a0e-d6ab-3af2-ba97-d9df1b5b5d01 | -12.86428 | -47.13811 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1578d914-8e37-3c35-b7e2-57777f8504aa | -14.60653 | -46.3784 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36b1e190-1842-3988-a311-3e4bff8ffd56 | -12.06719 | -46.55397 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acc00416-4798-3516-ab0a-b0ffb16b99b9 | -14.55557 | -47.35503 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1c4f270e-5c17-30f5-b364-19f12bfa36d8 | -12.69287 | -45.80988 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7ce0b00-c076-3e9b-a8e7-fd1fb8738ad4 | -14.77039 | -51.70239 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ed4684c-e0e6-38e6-a466-968f32a544d9 | -14.31485 | -52.9611 | 2025-09-17 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f2a11d1-073f-367c-900c-c338038a9d3b | -14.9064 | -51.68645 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39dd9589-0c78-32aa-8f5c-c0e6fd25fa0d | -12.10593 | -44.81956 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 135b1773-6acb-3d7e-ad4f-76b24aebb606 | -12.38989 | -51.41435 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2122c03f-3c67-3a95-a70d-0d2951359c16 | -11.07129 | -49.75616 | 2025-09-17 04:34:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78b82521-9a43-332b-a1ea-aad4214b1ad6 | -16.50502 | -54.65834 | 2025-09-17 04:34:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 503e1226-2d1b-37f0-8c33-a6a20f0e0c5b | -13.65051 | -44.26237 | 2025-09-17 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e64cf90f-7a96-307f-ac10-57f1bc25e3da | -17.19496 | -45.9192 | 2025-09-17 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 580a20ef-2eb2-3fde-9703-334a6872936b | -14.77831 | -60.22777 | 2025-09-17 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e68b365a-4728-38d8-a026-24ff807464c9 | -12.86568 | -47.14568 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a86479f0-b90e-37c5-a761-9c965ddc1214 | -14.81736 | -51.69497 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9c959225-4c05-3689-870b-625a693c773e | -12.97313 | -47.94854 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1bf5b5f-46d5-3781-bd76-0e8d78ea777a | -12.70241 | -47.95061 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f1db4057-3789-3a0f-a4fa-b0a31ff0beec | -12.70222 | -47.77039 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 718da16b-1f7c-3942-8366-c505f7d7b3b2 | -14.80684 | -48.12922 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6421fe7a-8636-3392-b50d-1669419cd90e | -17.04546 | -45.89394 | 2025-09-17 04:34:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 28217631-45be-3252-a51c-5f2638ce3d42 | -18.52551 | -48.15306 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47c5485e-0dbd-31ec-92f2-26f645fbea88 | -17.00335 | -45.85749 | 2025-09-17 04:34:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 404d53b7-310c-31c0-8dd3-5864abee9cd1 | -14.60043 | -46.39216 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08cdf01b-e8a6-306a-b4ca-5eccd18bf836 | -18.54124 | -48.14313 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d91c39b-1c1e-3c40-b86f-a61071d1acdb | -12.98321 | -47.95037 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1ef8c4c-d2de-3749-8748-75bc5cbc2c4f | -12.06368 | -46.55345 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f61b7c85-c711-330d-8f04-fd09acc45dd3 | -14.54773 | -47.4311 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 897d556f-7519-3283-a91e-1252181c913c | -14.81641 | -48.11172 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 107c2a17-6c87-3cff-94fa-6311b78db4f9 | -18.17511 | -45.17734 | 2025-09-17 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81416976-0ac4-30e2-a0dc-279f2db2f273 | -14.7809 | -60.21501 | 2025-09-17 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06e0057f-ea79-334a-a2b4-8595db6a2e96 | -12.8483 | -47.12706 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5ce43e8-8bf7-3ba1-8f52-008f82fddc8d | -12.35102 | -47.05689 | 2025-09-17 04:34:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f847a09-2455-3a86-afd4-9393df1a45fe | -12.8546 | -47.13212 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61c5d37b-bc4d-391c-9f45-480358f85ebe | -16.69519 | -54.97205 | 2025-09-17 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3803e1f-68c5-3642-bdd3-a36e3e5eb170 | -14.60775 | -46.39612 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96d9b995-0f30-3d87-bd37-b7bb999125a0 | -12.70082 | -45.80665 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af62d769-6f70-3a4b-ae78-7686c1b9414b | -13.64895 | -48.69894 | 2025-09-17 04:34:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42997fbb-6132-3373-b679-0eee8b5fafaf | -12.10007 | -44.83306 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4b6ec79-f2b0-3b2a-8b56-11ad81c9c0b3 | -12.86278 | -47.1414 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README50.md)
