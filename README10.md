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
| b0c8ee3a-f5a4-3f5b-a343-b15fdd957953 | -10.20771 | -51.66154 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b899b7e8-aae4-3bb2-af1a-6834bfe35370 | -10.10046 | -59.14933 | 2025-09-13 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| fe4cfcf2-7b7b-39ed-8173-a56926b06fcb | -9.95351 | -51.68358 | 2025-09-13 00:52:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fde5c95b-072b-3536-8cd0-e1f3acbc3f52 | -9.51947 | -54.62256 | 2025-09-13 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 8992f0df-0aad-307a-914e-510b7d49fcf1 | -10.00747 | -59.98185 | 2025-09-13 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 38883820-424a-3334-828c-f4fabe4d99ed | -9.52767 | -54.6252 | 2025-09-13 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| dadbb40b-a829-305b-813b-79f5747058d0 | -4.62386 | -47.42264 | 2025-09-13 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 382a1c0f-d4ad-3810-8fc5-604d71fa969b | -9.26076 | -59.43047 | 2025-09-13 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 1976cb6a-7e46-33c3-ae16-264da12d6cc8 | -9.4992 | -50.89828 | 2025-09-13 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 238f671e-3ffd-3c2d-98f5-d5c926e590e4 | -9.23664 | -51.24849 | 2025-09-13 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 955d28fd-b06e-360c-8970-6d1222ba0f64 | -7.97032 | -55.30141 | 2025-09-13 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 350e41af-baae-350f-ab08-64a39fdf5126 | -3.79645 | -48.63705 | 2025-09-13 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f33f79e9-61f8-39d5-95b4-0220935c799e | -10.42019 | -50.62797 | 2025-09-13 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9f02e28f-8bc1-312b-b006-78ef815a4267 | -10.51442 | -51.54481 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 0f151b6f-1049-3183-a549-d1abd562fdd7 | -10.50421 | -51.53722 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 695003d8-a179-3511-9a6d-83ab476a32c2 | -5.70943 | -46.4521 | 2025-09-13 00:52:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| f96317a4-2775-3c08-bc87-91e2deacf4c8 | -9.7924 | -47.78905 | 2025-09-13 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4cccd93a-9ec8-3b46-85d5-47e0500cb810 | -10.43082 | -50.63618 | 2025-09-13 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e53a29be-fd35-3119-b98b-7223638a9480 | -9.90779 | -51.88223 | 2025-09-13 00:52:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 1a413eaf-75fe-3dc5-9d2d-a723958435b0 | -9.44465 | -46.40813 | 2025-09-13 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ff6028bf-051b-3d47-8315-62cc067e2282 | -4.64386 | -47.56002 | 2025-09-13 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a9220199-a189-30ad-a500-540f8814191d | -9.25466 | -51.24918 | 2025-09-13 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 080c2f2c-da5e-3002-9b37-ca9dfe49d88e | -10.51312 | -51.53565 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1f8b8359-770f-380c-a39a-64b955b26718 | -9.72182 | -47.5616 | 2025-09-13 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 3649e1e2-69fc-3bbb-b434-1f37755652de | -5.64646 | -45.95075 | 2025-09-13 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c04f98cf-def1-3d57-8c9d-1efae2de392e | -9.50842 | -50.89688 | 2025-09-13 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 07206510-39e6-3e6b-ae9c-909d43bdeba0 | -9.95481 | -51.69268 | 2025-09-13 00:52:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1432757b-a3ef-337c-aa86-4ddb63b165f9 | -3.23456 | -46.79107 | 2025-09-13 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| d14fe1af-30dd-3685-af4c-f89c3cce07a7 | -3.22735 | -47.12049 | 2025-09-13 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 8734631b-cb8b-324a-bc31-782ecc801aa5 | -9.50157 | -46.43292 | 2025-09-13 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 20f32a36-b584-37f9-965c-6edc32b5af10 | -9.06904 | -47.0396 | 2025-09-13 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 17408d29-0724-328a-bb20-27cc26ca0833 | -3.22371 | -47.6227 | 2025-09-13 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| b0051ea5-433c-3ef5-955f-e7fd438c3fd6 | -9.24418 | -51.24101 | 2025-09-13 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 41363d97-ed0e-3f63-9c31-bddc7f6ba814 | -9.24141 | -51.22193 | 2025-09-13 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| fe01ff1c-52f9-3fef-933d-7366aba64aeb | -10.531 | -51.53309 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c9c83754-a906-3680-b29f-d310e4731222 | -10.10221 | -59.16283 | 2025-09-13 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a047b2b1-e169-3503-af1b-5168238361a8 | -5.35077 | -47.2832 | 2025-09-13 00:52:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f106e94b-4100-39a6-9bae-18185e921dea | -3.79492 | -47.58238 | 2025-09-13 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 9eddf304-eab5-3e3c-975d-2f81e76e8fb3 | -3.22232 | -47.14902 | 2025-09-13 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3e6c9f8d-0b17-33e8-bbb2-f51787a29b02 | -9.27121 | -59.40849 | 2025-09-13 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 138.1 |
| f808d273-c498-3860-808b-f12d0d5422b5 | -9.90907 | -51.89128 | 2025-09-13 00:52:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| e42650bb-2237-313a-9b02-b88e75e7e20e | -9.9065 | -51.87311 | 2025-09-13 00:52:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3d7cfcb2-2f02-35ff-806c-4f4b48ba6d4f | -7.38838 | -48.17781 | 2025-09-13 00:52:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| f611e3fb-70e9-3613-bd8e-e376ab8bc184 | -10.37348 | -50.50199 | 2025-09-13 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| afbc3f74-dc6f-3075-8234-925a967e01e3 | -8.07046 | -54.73902 | 2025-09-13 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8fa186ec-6d5b-32e1-bb97-797730ad8969 | -10.08937 | -59.16452 | 2025-09-13 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 16bd33f8-bc45-3b5e-a9cf-1b352c2a646a | -3.24036 | -46.78352 | 2025-09-13 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 569517bb-b068-33ac-96bb-9d3c3ea5b23b | -6.10506 | -45.94969 | 2025-09-13 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| f27f8a63-cc61-3086-9f23-e1f91ce0d0f9 | -9.90018 | -51.89258 | 2025-09-13 00:52:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0f576ee5-dc14-33a3-a85b-a6e01f3c9914 | -9.25828 | -59.41013 | 2025-09-13 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 6bdf7c4a-818a-3882-a404-b9cc12a8e949 | -7.97165 | -55.31146 | 2025-09-13 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ac73e09c-aaa0-3992-b89b-f0fbabcdef60 | -6.17778 | -48.93582 | 2025-09-13 00:52:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 12d9c540-3566-35cf-bb90-faff582d62d6 | -9.03514 | -47.06223 | 2025-09-13 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b1183a1e-6548-3e5b-8f4a-93074bb8089c | -9.71932 | -47.54573 | 2025-09-13 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 814e433c-cdca-3eb0-a62b-9a553b721651 | -6.47176 | -46.04022 | 2025-09-13 00:52:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 4c27f067-1602-3474-abae-20e6727419a1 | -5.35317 | -47.29582 | 2025-09-13 00:52:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 14187559-cda8-3b6d-bb59-b1743ec1d42f | -9.24555 | -51.2505 | 2025-09-13 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 0cc46ece-2afe-3f3d-a025-8f96ddc16687 | -9.32306 | -48.94462 | 2025-09-13 00:52:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 027994c3-2feb-3ce1-86fb-9154ed39a704 | -9.23394 | -51.22941 | 2025-09-13 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2b15cb6a-d516-3815-a8ac-58bb8d9d7535 | -3.77149 | -59.35703 | 2025-09-13 00:52:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 605e72de-1b23-361b-b6f5-a8a701d9748d | -9.05696 | -47.04215 | 2025-09-13 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 8e922ba2-2a12-3039-a4d7-7146e1f9f73d | -10.50289 | -51.52795 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b782e38d-fcd8-302d-8371-3a43ffcbffc1 | -10.52205 | -51.53432 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a0e06fd0-a18e-3039-b7d7-4e46326f2637 | -9.89633 | -51.86541 | 2025-09-13 00:52:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 7e7dd8c1-c3e7-3c60-bb67-e8a326d8f306 | -10.209 | -51.67069 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7704caad-0b35-3efd-8360-14df143d5b1d | -10.0005 | -59.97615 | 2025-09-13 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 1d69c900-c90a-383b-bac5-fc1ec7bbda71 | -9.52077 | -54.63219 | 2025-09-13 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 171.0 |
| 327ca0a8-5fac-3ef2-b007-aa10fa5b365a | -5.48949 | -57.10059 | 2025-09-13 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| dfca237d-4926-3feb-80ff-d9f2b5bb2e46 | -10.08179 | -48.18225 | 2025-09-13 00:52:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7daf5900-7bc3-329c-9885-3d0044ade44d | -9.9039 | -57.06282 | 2025-09-13 00:52:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5605e360-5a9f-3ee1-84d9-653b461bab53 | -3.6681 | -52.16926 | 2025-09-13 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1081646b-3e87-3237-b43c-2d4792696a9e | -5.25121 | -49.85993 | 2025-09-13 00:52:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0144faed-279f-3b14-92d0-64d8e3ef30d7 | -9.2533 | -51.23973 | 2025-09-13 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| c6f253a6-52db-3434-8914-feb4b74d1cd9 | -8.86434 | -52.00671 | 2025-09-13 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f21c69c3-e898-3df3-93b3-1bf54944e76f | -4.64404 | -47.55346 | 2025-09-13 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| adea8cc3-e838-3589-8a8d-307cdd3dcb2a | -10.70886 | -54.44289 | 2025-09-13 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 30c17b70-3ed8-3f50-ad82-13dce2174097 | -10.50551 | -51.54634 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| cf9ba7b7-8df5-3050-99a5-fd1dbbebf13c | -9.71678 | -47.52965 | 2025-09-13 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4d1fbec1-e803-39a6-8d6c-585773eafb43 | -5.3259 | -55.88785 | 2025-09-13 00:52:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 5bf0c2a9-cc62-3d87-bd34-b48a0bb664bc | -5.43416 | -49.99849 | 2025-09-13 00:52:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b7b6d76e-a11b-30c7-8a91-700162c9dc5c | -9.52213 | -54.64212 | 2025-09-13 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3ed6805e-21e1-3186-8e3e-58c81fa53c3d | -9.27372 | -59.42885 | 2025-09-13 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 3529cdd8-d235-398e-9316-7475a9de4137 | -3.21718 | -47.14435 | 2025-09-13 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| e40522f2-8b2d-30e0-ba52-bf417de0a194 | -10.51572 | -51.55395 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 373a30d6-c117-3241-a122-4c3a5c56fd36 | 0.68475 | -50.64824 | 2025-09-13 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 26.1 |
| a860a9f9-c19f-380d-a5e2-a596c2790a04 | -3.44398 | -59.55948 | 2025-09-13 00:54:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f6cea65a-abb7-3c2f-87af-a77bfcc32db7 | -3.44627 | -59.57629 | 2025-09-13 00:54:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| e179aacb-6514-380a-be96-711d0bd19c01 | 0.67205 | -50.66026 | 2025-09-13 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 16526cb5-5341-376c-aae6-69ce76e4cf0d | 0.67016 | -50.67373 | 2025-09-13 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 89bddc95-9121-3183-91c0-68790abbe3ff | 0.69846 | -50.65605 | 2025-09-13 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 25.2 |
| ccfeaea7-4022-38e3-a19a-5844c34d08a0 | 0.69555 | -50.64975 | 2025-09-13 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 93.9 |
| dd5b0be1-e2b1-38c0-8a7c-ec30638aa391 | 0.70029 | -50.64246 | 2025-09-13 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 196552a3-34b7-393b-920a-f559d831688a | 0.69363 | -50.66328 | 2025-09-13 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 50186fcd-9ec4-3ac4-a017-9e6f8447adf5 | -9.4807 | -46.4096 | 2025-09-13 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| ce1cfdcb-6363-33ac-9e5a-d608bf9aae5a | -21.1648 | -47.5396 | 2025-09-13 01:00:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 57.9 |
| be18fb29-9068-3822-b82f-b91c9af365af | -11.7424 | -44.2117 | 2025-09-13 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| c28a075a-92d3-355a-9269-ff54080dcedb | -10.7664 | -50.5299 | 2025-09-13 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| becd1df7-a634-300c-8d95-759c3c89abec | -9.2503 | -51.2472 | 2025-09-13 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| a7aea760-99c8-3434-a715-42930303644e | -9.5137 | -54.6292 | 2025-09-13 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 182.6 |
| 81fb662b-bf84-3920-9322-b07f161702dd | -3.2283 | -47.6154 | 2025-09-13 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |


[Clique aqui para ver as próximas entradas](README11.md)
