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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97d77799-41ed-381f-b4ac-8730484f93e6 | -12.40987 | -50.26675 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4f589ec-7830-3cea-b0ce-c96cf6dc5c46 | -10.43112 | -50.31893 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 27a073c9-6d32-31db-969a-f2a7e8850b3f | -14.93117 | -51.4731 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b22d92f1-c0c5-3779-a6ef-4b040f599634 | -10.88875 | -51.03074 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5773378c-f90e-38c1-9780-82eef5768b78 | -9.92129 | -49.96605 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ae00a2b0-e28e-3cbc-afb5-72cc3fe4e48b | -8.62038 | -54.9872 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 238ca53a-e637-3350-9993-e3fecef6f258 | -13.53446 | -42.99846 | 2025-10-07 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| dcd16921-ce93-3299-bfe4-01c5b63a669f | -10.42292 | -50.29192 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 982c24c8-3e81-3290-8caa-ee48b7fc5911 | -13.25103 | -48.05898 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfd9a728-4eac-334d-8c83-a6977996ab8a | -13.07916 | -47.8458 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| caad1866-b2a3-37e5-a52a-7f3b0768c63a | -8.74646 | -48.87304 | 2025-10-07 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d732bb5-3831-3c94-9007-456c15ffeed4 | -14.91186 | -46.82819 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0076745-0909-3c8b-9101-1e0554086cdd | -13.04718 | -49.15673 | 2025-10-07 04:57:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d835ecd-754c-3b9c-ae16-1bba6ec31eb4 | -11.01014 | -52.31328 | 2025-10-07 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88d79a69-37ff-357a-87a5-9748198cc93b | -10.92132 | -47.07112 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05b7127d-afc3-3892-aaee-c29a8c69b322 | -14.77378 | -46.06992 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a3179a3d-d2e4-3195-a1cd-385e1b797dda | -11.84629 | -44.92472 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05325064-b22a-3bd3-828c-d0a682ef9da5 | -10.39396 | -50.29803 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7ae360a7-64f4-3951-a47d-553f0a17668e | -11.02476 | -50.91838 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3240606b-af61-304f-ad41-fffb75dbca2b | -13.0258 | -51.03303 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79425a38-ebf2-39df-98ba-07a3955d208b | -10.81122 | -48.59518 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e548333-141f-3cf0-a547-bca1e658e164 | -14.91235 | -46.87093 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 118cb9b0-5a54-3cdd-8ce0-b90fd03bb8c0 | -13.07051 | -47.83045 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 477aa997-44ee-30da-be3e-1949e37aea09 | -14.74015 | -46.0199 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6305eef7-77bc-37b8-bff7-d7e8bb6de756 | -10.02629 | -48.2985 | 2025-10-07 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbaa2994-4884-377c-8aac-58213198f582 | -8.84889 | -46.094 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ef9eb18-54e7-383f-8d3f-08a140e4fa4d | -8.41387 | -50.7022 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7fd2de08-5928-3a79-aee6-e9a79e64647c | -10.38324 | -57.50095 | 2025-10-07 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27b46ec5-bbf6-3d8b-b8ce-15e2094f6bcf | -7.48016 | -63.56076 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a70bbece-69f4-3204-a31d-0de2f24ae3de | -12.98178 | -51.02929 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1939debc-8ffe-3f19-a314-054295db92b0 | -13.37133 | -47.23786 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c44358b-6a20-31c0-9388-ca46544f51c5 | -13.23816 | -47.24821 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24b5956f-f5d6-37ab-bd79-98fc451a213f | -8.22895 | -61.1711 | 2025-10-07 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf51aad8-38a3-3337-889d-d3e45a7d9523 | -9.01858 | -50.68852 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5b69e7b-9985-31e8-9fea-0b1a3b3b60b5 | -10.1086 | -58.53025 | 2025-10-07 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc90717c-4ab0-3f43-82b5-f3822086117e | -10.15366 | -56.89579 | 2025-10-07 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29fbd6f1-142b-35b8-9a1c-58f1da5a6b85 | -13.78686 | -50.78295 | 2025-10-07 04:57:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8035efb4-ccef-31ce-acdc-e7d2330b1971 | -9.25119 | -59.02382 | 2025-10-07 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 090d59f5-b926-39c7-aa88-b27c0920d6f8 | -13.38014 | -47.53779 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cda13bc4-8bf7-3b04-afb0-de19dce9ca89 | -14.90809 | -51.439 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8581ac95-b89f-3fbd-9b83-2fdeb0396280 | -10.41362 | -50.3009 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d20ffeaa-213e-3efc-a552-412d64c33830 | -11.95405 | -45.49072 | 2025-10-07 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 931445a0-b97b-3ccd-b67d-2109ba589025 | -10.38534 | -50.30517 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c54b8ac6-ad90-3cb4-bba6-6c3c15025337 | -10.81259 | -56.23442 | 2025-10-07 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab456037-a039-3212-bf71-3c562157223d | -9.95802 | -64.21406 | 2025-10-07 04:57:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 285f2c12-fad8-32b1-af71-caa52a1e503d | -12.24341 | -47.02105 | 2025-10-07 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a39d225-e9d1-3bf7-879b-9fc7e0318c9c | -12.37899 | -51.08189 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05eeae85-da28-391d-bd10-f74bd53e4d01 | -13.9701 | -53.89582 | 2025-10-07 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a556b8f-99b2-3905-8590-9038a1e0bdec | -11.50311 | -44.97915 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d944622-d1c2-37ee-8bb8-5252c42b0b22 | -12.98677 | -46.78485 | 2025-10-07 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bb13631-8d96-3e7a-94ac-4bde38e16264 | -12.3436 | -50.2683 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 054e4c5f-9662-3fb2-8d58-3c21b51e5abc | -12.31291 | -55.1127 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cce6ac0e-acf0-342c-bdee-5f8a6b8dffaf | -15.26597 | -46.35873 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52af58a0-2b1f-3473-8cd4-4676818fd29a | -10.37822 | -50.29898 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c40af056-158b-3618-b285-810fa4a0c90d | -13.1843 | -51.04507 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abd4e06c-a390-3ef9-ac3e-cc961c67e814 | -11.0432 | -50.9189 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 3a0da2e0-4b95-3ed6-b14a-3d895bd28ccc | -8.61708 | -54.96523 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca57be74-0b25-3833-ba1a-38cbb5c7e258 | -15.22131 | -49.30144 | 2025-10-07 04:57:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9319fb5f-84ee-3ee9-a445-0aceb8e57bd0 | -15.27904 | -46.34207 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0170d857-97ad-38a7-920f-787016efb6c0 | -9.58451 | -54.94937 | 2025-10-07 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a889857-c704-3430-9d94-7b785a107cb0 | -13.54109 | -42.99919 | 2025-10-07 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 765b86d1-8a2d-38d3-9268-8277ec33cdae | -12.89736 | -54.76003 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d31dfe61-73a9-3bc2-a48d-d42f516c896e | -14.92965 | -51.42672 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98808280-09c4-3401-b710-fffefb35fa7f | -11.64577 | -46.87641 | 2025-10-07 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c47c792a-a246-3363-8b5a-d9de4c841fa6 | -12.05919 | -51.21442 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7014681f-5b82-31cb-81d6-769f3c8bfacd | -9.18216 | -47.83315 | 2025-10-07 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1a8e006-152e-3ebc-8d2a-4c46dedce2ee | -14.90596 | -46.84021 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09bf5b28-092e-3b16-9e7c-078f4a4c77af | -10.38215 | -50.29956 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 9304ec84-8569-34be-9d49-e14eebf2b96b | -13.67518 | -47.33378 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27d30c34-8e3f-3915-84a1-781199055de7 | -12.97165 | -46.7798 | 2025-10-07 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc1f99fb-d917-3735-96fa-3901219b1b6a | -10.41684 | -50.30653 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1da23fb2-ef9b-3d1f-a101-eed3688ced1b | -9.60486 | -57.14037 | 2025-10-07 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4a53bcc-d14a-3431-81a3-e3732128008a | -10.26296 | -44.36799 | 2025-10-07 04:57:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d98027f8-97ef-3fa1-a6be-17d469e0c3ef | -13.717 | -48.0713 | 2025-10-07 04:57:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ade77f9-3ccc-34eb-825f-015a04dcc760 | -8.54479 | -55.01439 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 860c44ec-7c8b-3f0f-8e6a-b2e3d48dcd27 | -10.62812 | -57.61851 | 2025-10-07 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58aee1b1-10f2-3812-9901-15a6ef21f52b | -8.54093 | -55.01734 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74b4cfa2-2858-3d6a-8771-48d459d0d737 | -14.64824 | -48.37131 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b70f08c6-7282-33f5-9a32-de7be59c93dc | -12.93061 | -54.72145 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 806e6d0a-7487-38d6-8911-f493b61a56ad | -9.44868 | -56.65816 | 2025-10-07 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 00b58b60-8039-37a2-bbd2-f0a00a729646 | -14.28521 | -45.84811 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49e51ff2-7ccf-3fb9-8c49-f266911b1c95 | -14.73457 | -46.01937 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d88682ca-92a3-3977-915d-d12af6531d5a | -13.23907 | -51.68392 | 2025-10-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5cc842c5-db99-3873-ac69-0a7aa255fa68 | -13.25328 | -47.16932 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f811cf21-a7ac-3aef-b019-64fe789bb5cb | -9.13695 | -50.69772 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 502df2b1-dcc4-353d-a6ae-88b385378451 | -8.936 | -49.8611 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0469800-b802-33b9-8901-19f3ca01dbf8 | -14.27963 | -45.84734 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10b365b4-e857-3d5c-9a65-c2d96f340287 | -15.16822 | -52.77733 | 2025-10-07 04:57:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 719b2ca7-1b4b-31b4-81ab-1d100222a5d3 | -13.28004 | -47.16089 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 15862851-eef9-37a3-8619-cb504a2e8f94 | -9.9631 | -58.70041 | 2025-10-07 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6bc565f-9b40-3e0e-9010-9d9ca18b7c56 | -9.00166 | -61.5475 | 2025-10-07 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c951422e-9610-3723-9861-16f8c2dcfbee | -12.98567 | -51.02986 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32e270a6-5efb-3d2a-9d74-cfdb2a83baa3 | -10.41755 | -50.30148 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 83c39b71-33fc-33e2-86a4-8b8ea2a40de1 | -9.18606 | -47.83849 | 2025-10-07 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cabd92d-3b3f-3e8a-8447-11265f5a4e5c | -8.41452 | -50.69781 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 536442e8-f903-394b-b7e1-7f65ea189445 | -14.63994 | -52.53295 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 070fa9fa-c406-345a-a266-d1bf9ada94a5 | -13.22164 | -48.46211 | 2025-10-07 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3c18fc2d-d35d-3270-94ba-ada4f78ab63a | -15.43879 | -49.09676 | 2025-10-07 04:57:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7244e89-7732-3107-b651-e2125c246152 | -12.98298 | -51.02679 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e52ece74-76f1-3d49-9396-59503442558b | -14.7294 | -46.01518 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README87.md)
