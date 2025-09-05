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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 596ef709-dded-3333-aa1e-a5d4bd8d9b28 | -15.61302 | -52.91709 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 0714157f-1e3a-34a7-90b4-eaf786e81e5e | -12.95827 | -54.78944 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 41ddbe66-cef3-3674-b018-83b4bef40a3e | -15.21301 | -52.37827 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71563904-4564-3886-b2fe-5ea4a8516d0d | -15.85516 | -52.29593 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2127f929-5c5a-3b6e-b2b5-ffe52f50c0a2 | -14.58838 | -52.1833 | 2025-09-05 04:38:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6f349ed-39e4-314f-8b8e-48a43b8d316d | -18.46564 | -53.03811 | 2025-09-05 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 940cbe53-109b-369a-8fa4-91280f7b365f | -15.58234 | -52.88096 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0aeefd9-eba2-378d-8d5c-4dbb57b2876d | -15.04605 | -50.04598 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb1abe41-e471-3396-ab79-c74317e7a900 | -15.70756 | -53.60366 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e07df18-a10a-35e5-bcbb-6777161508e1 | -14.99994 | -50.08659 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 639b58a8-9584-3d90-801b-e7b901ae7e75 | -15.73024 | -53.62694 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 548d8fba-7ba9-3efe-b541-f1b05becd71c | -12.98511 | -54.80634 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1aeb66c-3635-3bb9-b1ed-fde749b82431 | -15.20179 | -52.3804 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7b329ee-3218-31a0-9cb2-3769e85deaa2 | -15.5859 | -52.88167 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7b71137b-2211-30df-862f-b86639fee490 | -17.66419 | -52.26366 | 2025-09-05 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8dbe9363-8d31-3429-bec4-8fc973ecea56 | -19.07941 | -48.15054 | 2025-09-05 04:38:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 16fe1448-8ca2-3529-a4b9-c3d8f560929e | -15.85234 | -52.29133 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c12f00b4-fac6-3654-ad1d-b69eda5c4196 | -18.92827 | -48.35272 | 2025-09-05 04:38:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e19c27c-2389-3e89-bfb2-fcc13666464a | -14.73968 | -47.49345 | 2025-09-05 04:38:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2467fe6c-c6c8-3835-b3c1-7b9dd81314e8 | -12.98236 | -54.82161 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 45f11f7b-3ef3-3c98-beff-708a9c66cf24 | -12.98991 | -54.80334 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9bea062-8da4-3039-b676-b53ee54a2f72 | -12.983 | -54.79428 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dc6c6e4-2639-3475-99f1-7cbcc26e010e | -14.585 | -48.01455 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f48dd6b8-551c-3513-9e8b-7af875b67350 | -14.75761 | -47.49237 | 2025-09-05 04:38:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e97d8075-5f65-3935-a444-9ad440725bdc | -14.48626 | -54.02391 | 2025-09-05 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 054c98f4-cbd1-381b-9555-bfa09298e1a8 | -12.98368 | -54.79051 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20572565-d7a9-3992-8aa7-9a8e63084cdf | -20.24259 | -51.30089 | 2025-09-05 04:38:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 1926727a-f00f-3b37-a37c-1625048ffb43 | -12.64256 | -56.98759 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 254ab340-9f58-3db4-9c4d-85d425c1532d | -12.63837 | -56.98935 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 020187de-098f-3587-9c68-690efb0a0b04 | -12.96858 | -54.80324 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad9b67b1-31ee-3d00-a351-5a6a822912b0 | -16.31186 | -52.94519 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a3026cb-2bc5-3ad2-b59a-89e9223c21a2 | -15.53817 | -48.41799 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 678e06ef-255f-329d-a005-1becf4a93661 | -15.72809 | -53.61729 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85538182-1e8a-3f1d-bc89-474ccc48ca3b | -16.37509 | -43.04039 | 2025-09-05 04:38:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41ad063d-849f-3e72-8db2-a2e9d93338c6 | -12.9796 | -54.81319 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 74e84bae-b959-314f-8ec8-c752db995a4d | -15.99192 | -55.97599 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9124b582-6630-302a-9140-8de74cfed77c | -19.68027 | -54.8045 | 2025-09-05 04:38:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 667cfffa-85b4-3795-9b40-dead3d02ebfb | -17.48503 | -43.33345 | 2025-09-05 04:38:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73df3230-b31c-3881-a998-0cfb94a2cf4d | -16.30916 | -45.69257 | 2025-09-05 04:38:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bf11d10a-9b96-3903-9a51-c49c5e8d7418 | -16.32611 | -52.94761 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73faf49a-9570-346f-a479-64a75ca17c7c | -14.98995 | -50.0849 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4c0d9d7-48c2-33ce-924f-438d877f11b4 | -13.87078 | -48.01446 | 2025-09-05 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0070e04f-09fb-3171-8257-2b18d2ad854e | -17.53423 | -46.60391 | 2025-09-05 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a889fb8-02d6-3fb5-90fd-dc07e98843bd | -15.75809 | -53.67134 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46f48f05-12e7-3c9c-b79d-6e5e32f723d6 | -17.58198 | -52.56197 | 2025-09-05 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ea4fa66-5a20-3b0c-8219-a2a787f310c7 | -16.31543 | -52.94579 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b549c13e-ce8d-3940-8eeb-12376efa957a | -14.13122 | -51.72214 | 2025-09-05 04:38:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a297ce4c-6715-39ed-b145-3699c427e614 | -15.55001 | -48.40859 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5feaeef7-dc6b-3ab6-bc47-d33d7b5b38a5 | -15.57198 | -50.33662 | 2025-09-05 04:38:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 552ac898-883f-3401-bc50-92b6c1ec082b | -13.88435 | -47.99369 | 2025-09-05 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be2feed9-206d-306b-8627-b024222169de | -15.54494 | -48.41914 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 060bab90-6c29-3e73-aadc-8e77635be805 | -17.58264 | -49.78225 | 2025-09-05 04:38:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b98617af-0c24-3438-bbf6-87a5d009322b | -20.75471 | -47.13644 | 2025-09-05 04:38:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8128998-0399-312d-8a42-b319f66b9135 | -12.95895 | -54.78568 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a3e2abc4-ee6f-3e88-ad0d-4868ae00edde | -19.40752 | -44.32814 | 2025-09-05 04:38:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46357a05-ec44-3937-9bba-cd8d3b7d5f2c | -14.58862 | -52.18019 | 2025-09-05 04:38:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b6095d2-c35c-3be1-9b59-1d0ba7521f95 | -15.61016 | -52.9122 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ab1140e-15e2-3f30-acf8-73d7f64fb179 | -15.5714 | -50.34023 | 2025-09-05 04:38:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4019cf64-75a0-3141-93d5-22b5bf9315d5 | -18.87076 | -46.36877 | 2025-09-05 04:38:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bfe7d15-a5ca-304c-8c94-2d1cad9efd06 | -12.6076 | -56.99426 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e3f8961-a62f-34bf-95cd-5b334677179b | -15.72733 | -53.62172 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f58c4ae-f5fc-3995-8a28-432068750397 | -15.73101 | -53.62249 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19d24fe6-55bf-3ec3-858f-b66dc07d6749 | -13.99231 | -49.55021 | 2025-09-05 04:38:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79a3995d-ed1d-361e-9ab8-9834148e597e | -15.72442 | -53.61644 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 878716ff-ce4d-3172-99af-71956d1114ca | -15.18194 | -52.39069 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2def9b1b-a4db-3806-a3d7-dc651aee581f | -13.33055 | -51.73243 | 2025-09-05 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 563a278f-df8a-3a64-9d28-99ea8e8b1b9f | -15.20555 | -52.35771 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be4e989e-20b9-3a3a-a726-747de709c653 | -15.55228 | -48.41656 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6da22939-8be8-3409-9af4-4904a308dec6 | -16.45634 | -45.25202 | 2025-09-05 04:38:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70ab3119-f300-3690-9933-2011d09770cb | -15.0743 | -50.06174 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efb73a7d-4466-3ada-829d-6dfc9fa8b075 | -15.54211 | -48.41486 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4577dc6b-1e86-3795-9c2e-cd4694ce4cde | -15.54606 | -48.41174 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffa89988-b68b-3690-8a91-01e3455b2bac | -15.20224 | -52.37749 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a6bf8fc-412d-3274-80a2-00fec2d443ab | -15.14167 | -52.37194 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8648135a-3bd9-3f80-914d-4144bab04084 | -15.21221 | -52.36179 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd7715df-dfdd-3666-93cd-6b442da8abc5 | -12.96579 | -54.77151 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfe32a6d-9d1f-3895-8d03-4b63c741e18c | -12.97822 | -54.82087 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3539c2a9-8b88-3db0-a482-1d71c83592ba | -16.30762 | -52.94855 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c17b87f-c859-386c-91a1-5a342658229b | -12.88097 | -56.95053 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eda98670-e692-3f1f-b7fa-a559073c5d40 | -12.96855 | -54.77979 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f143f620-caf6-388f-90c4-a8272f438928 | -15.14806 | -52.37698 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7988797f-123f-3adc-bfde-5d7b3f208aec | -15.13324 | -52.33642 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c704223-e44b-3bf6-a71e-9319af388bc0 | -14.56492 | -54.52673 | 2025-09-05 04:38:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51b0c018-60a8-362e-8033-102ff5081a85 | -19.68399 | -54.80526 | 2025-09-05 04:38:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61f64a8f-b310-3a30-86ba-f7df95aecf6b | -15.22206 | -52.36766 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73f8525f-ba7f-3e64-9a64-b1f3869b72ed | -19.11059 | -48.74982 | 2025-09-05 04:38:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85abebbe-157c-3361-8e2d-97639c4a06eb | -12.96102 | -54.79782 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 5c700199-6828-3650-9c52-bb9d37a2c3de | -21.36618 | -46.94705 | 2025-09-05 04:38:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f466bf0-75bc-3e43-8bd1-adfb971d2225 | -15.56902 | -46.49621 | 2025-09-05 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f34bd5bc-8022-3d3f-9873-695022a1cce6 | -17.66992 | -52.29269 | 2025-09-05 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd3d8fe4-915d-374f-afc4-4b8222db22f4 | -15.31536 | -52.73239 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6443bee-fe73-3c5e-812a-fa00e4f7f2cf | -15.3182 | -52.73726 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d45357d-4949-3151-a2c0-5d47ce454c9b | -14.56352 | -48.08727 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3932e80e-4496-3298-ab81-9f971a3740ae | -20.24592 | -51.30149 | 2025-09-05 04:38:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0ce40227-8174-3e47-b10b-166b8f4adc66 | -17.96272 | -41.70858 | 2025-09-05 04:38:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| cd048975-a79e-3ebd-92bf-bf88ede1cf60 | -15.71495 | -46.2282 | 2025-09-05 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fbbb89b-d369-3488-8710-4bb3d5d896ce | -20.52011 | -46.46067 | 2025-09-05 04:38:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8225222-7858-3877-95a9-bf4f06324536 | -14.59354 | -48.00433 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e40465c9-7941-3ec2-836f-58c7345800fe | -15.53872 | -48.41427 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4be81464-eae0-3b1c-a93a-e857cc2e9042 | -12.9624 | -54.79022 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |


[Clique aqui para ver as próximas entradas](README35.md)
