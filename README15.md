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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29f06c76-7f68-3f72-832a-fc58170fbb91 | -12.786 | -62.4982 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5120473f-64a9-354c-83be-e574e1d57016 | -12.8047 | -62.5163 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 552cb9d7-852f-39f0-bacb-45a9c4ddd2e4 | -12.8049 | -62.497 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 0651bc16-f605-3b41-a9a3-0ad163e410cf | -12.8238 | -62.4959 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 28bf3cc9-0082-32a1-b5de-1cedbe815fb7 | -12.824 | -62.4766 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.3 |
| efac4ea6-fe7e-318c-9053-fe67f219f569 | -12.8619 | -62.4743 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| f07a1bed-a084-317c-9449-c68e02181a08 | -12.8802 | -62.5503 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b63132b7-e0d8-342b-8fba-b19ea6d31992 | -12.8803 | -62.531 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5e4276e9-1b54-3682-a47b-e0ee0c68c637 | -12.8808 | -62.4731 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 96.9 |
| c2f3faaf-74dc-3e98-b2aa-9210d284f57e | -12.881 | -62.4538 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 00748a47-255e-3f94-8cc0-94618630a5ca | -12.8996 | -62.4913 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 112.7 |
| ed232c0c-6cb8-31a9-b40d-afc7b0d2c82a | -12.8998 | -62.472 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 744f2f55-5651-3d51-8409-a918f55ba95c | -12.8999 | -62.4527 | 2024-10-03 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| f1a87e5f-7b2e-3290-9d97-97bbfea20743 | -12.9741 | -62.6409 | 2024-10-03 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 87cc48b3-aec0-3e0f-94b1-6ef878cbb46b | -13.5002 | -51.1492 | 2024-10-03 00:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4f478650-73ca-32c8-bb67-58aa03fdbafc | -13.5195 | -51.1467 | 2024-10-03 00:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| cb0948d7-303e-3c2d-af9a-7b3d8c216f7e | -13.5198 | -51.1252 | 2024-10-03 00:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b5afb781-9135-320a-8d34-deb70afb9568 | -15.2332 | -47.5032 | 2024-10-03 00:26:31 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 4c2df833-556a-3f2f-bc9a-80107610601a | -15.2528 | -47.4999 | 2024-10-03 00:26:31 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 26f26c00-a931-3836-87e0-f2e1c320f916 | -16.7594 | -57.8328 | 2024-10-03 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| f6660f90-4bf2-3938-98d7-97d570baaa76 | -16.7597 | -57.8124 | 2024-10-03 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 6dc80932-6f76-3be2-a5ac-533afb5153a9 | -16.779 | -57.8306 | 2024-10-03 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.0 |
| 2932514e-baf4-3b29-9804-67e613401f29 | -16.7793 | -57.8102 | 2024-10-03 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 8196af8a-a5c8-30c2-8bdd-f05503f558a7 | -16.7985 | -57.8284 | 2024-10-03 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.6 |
| 2e358a4b-0044-3eb0-8c43-9055b3782a76 | -17.3283 | -42.4889 | 2024-10-03 00:26:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 60a6a6b0-ed40-335d-8182-9a8c9486076e | -17.1967 | -57.3946 | 2024-10-03 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.7 |
| 49997b57-4d3d-387e-9484-640313440e73 | -17.197 | -57.3741 | 2024-10-03 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| a34d37c5-a9ce-38a7-91c8-01e2dbab789d | -17.8403 | -57.7076 | 2024-10-03 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 9d84fed2-3ee4-3698-8ae7-1d35cfe2c08c | -17.8407 | -57.6871 | 2024-10-03 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| e5624cbf-dc4e-39ec-b61e-20d7e191f505 | -18.5386 | -42.231 | 2024-10-03 00:26:48 | GOES-16 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.0 |
| ccbc5080-7d7a-3d45-bb1e-e6529872595f | -18.8927 | -41.2248 | 2024-10-03 00:26:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.5 |
| 0fb108c9-084f-3453-a525-1932587eb741 | -18.7172 | -57.3305 | 2024-10-03 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 2abc7496-dcb1-3f40-92d2-851d69a51627 | -20.6617 | -42.0115 | 2024-10-03 00:26:59 | GOES-16 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.2 |
| 912d6623-68d4-381d-b3b5-9f8165051fca | -20.6625 | -41.9858 | 2024-10-03 00:26:59 | GOES-16 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| 86f57ad5-297e-39a2-972c-4063482765fa | -21.306 | -47.6227 | 2024-10-03 00:27:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 3c68c0f2-208f-39ee-9955-b0dc01f0b835 | -21.3067 | -47.599 | 2024-10-03 00:27:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 5d1f96a7-012e-3449-84e9-3e65161b2681 | -21.3868 | -47.6734 | 2024-10-03 00:27:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 05f82123-2867-3592-ab1b-a37e798c67a3 | -21.3875 | -47.6497 | 2024-10-03 00:27:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 2836820d-c378-3835-9146-a5d8d10bc32a | -21.3882 | -47.6261 | 2024-10-03 00:27:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 876ace4d-7e07-3e6a-a31e-79998bc820c3 | -21.3456 | -55.6841 | 2024-10-03 00:27:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 9ce84df0-36de-3f3f-ad3a-1c24bb3be224 | -21.346 | -55.6626 | 2024-10-03 00:27:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 3eb9d451-012f-3284-8a13-96b9b71f5e1a | -22.2314 | -48.4272 | 2024-10-03 00:27:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 72e693b3-d3e1-3c86-935b-ebc942f1e395 | -22.2307 | -48.4507 | 2024-10-03 00:27:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b5cadf3e-2dc2-36fb-a320-f35573d078ce | -22.3704 | -47.9462 | 2024-10-03 00:27:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 350f7413-ae66-3e3e-8daf-a4ccd7ae7430 | -22.3495 | -47.9515 | 2024-10-03 00:27:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 119.6 |
| b265edc9-40b7-3e5d-9c71-328b2c1d3251 | -22.3502 | -47.9278 | 2024-10-03 00:27:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 359bee2d-4e1e-3c62-9c71-f4ce89c0067b | -22.3711 | -47.9225 | 2024-10-03 00:27:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 218.4 |
| eddffda5-1d4b-3cb5-924a-947340c2cc20 | -22.3719 | -47.8987 | 2024-10-03 00:27:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 69d2b057-5085-3b90-9b23-260d2267eb46 | -22.446 | -46.8576 | 2024-10-03 00:27:09 | GOES-16 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 5b2cecf1-d5d2-3acc-ab0c-0cb102324bd5 | -10.91754 | -46.31754 | 2024-10-03 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| da075ae8-1ebb-3874-837a-a63f60e3b2e2 | -12.19364 | -46.75841 | 2024-10-03 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 533d9799-62bb-3f14-a0b7-fd3c848090ea | -11.26348 | -46.93184 | 2024-10-03 00:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 382c9102-2955-3da9-b373-c1fd98a2b4bc | -11.26125 | -46.9126 | 2024-10-03 00:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d567075a-0840-3ba0-89e7-c6a30eedeaec | -11.25974 | -46.91906 | 2024-10-03 00:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| b0591e94-ab5c-3950-9f89-d858f14c3c38 | -11.2472 | -46.92065 | 2024-10-03 00:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 045b9ad1-7ee3-3ec9-b719-0d3eb1a1d514 | -11.0335 | -46.52585 | 2024-10-03 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ccd38779-9376-3289-929b-ca712b9c3eb4 | -11.02682 | -46.51507 | 2024-10-03 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f12168bc-4b16-3db5-a8ce-0dd1e8f3f577 | -10.9827 | -46.55643 | 2024-10-03 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 0e653ead-e973-37af-bf7f-ba9f9fa80975 | -9.37178 | -35.85239 | 2024-10-03 00:28:00 | TERRA_M-M | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| d590c890-86be-3813-89e5-d8b2e66e4d23 | -9.37028 | -35.86245 | 2024-10-03 00:28:00 | TERRA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 7c3b9389-ab9f-3bbd-a603-7bf204753319 | -9.36773 | -35.84655 | 2024-10-03 00:28:00 | TERRA_M-M | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| 7467fffc-be2e-3614-8577-3936557dfd38 | -10.72123 | -46.20306 | 2024-10-03 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 9ab19a03-91d7-3fe9-83eb-6a8433811e44 | -17.11355 | -47.13668 | 2024-10-03 00:28:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 198edccb-5238-35f7-9128-1167ae185240 | -16.34018 | -42.30145 | 2024-10-03 00:28:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 01378f22-44b0-30a3-a9cf-9892784b76fe | -16.33058 | -42.30299 | 2024-10-03 00:28:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 6ffffa7d-f9b7-374c-9a7c-c82095bae984 | -16.3292 | -42.29212 | 2024-10-03 00:28:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 92a970b0-148f-3c14-81fc-4da4dd71ff8f | -16.09852 | -50.29439 | 2024-10-03 00:28:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| b75c757a-8bac-335e-bc28-8b8d3df6c206 | -15.8132 | -42.4873 | 2024-10-03 00:28:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 28.2 |
| dfda0515-0f8d-367d-bf98-a8d038fc69bc | -15.80355 | -42.48877 | 2024-10-03 00:28:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3b21c7bc-8188-345a-ad01-aa1fd13ab163 | -15.78196 | -49.97551 | 2024-10-03 00:28:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 34.8 |
| ae4577ad-5b90-317e-8436-1c9dab737d45 | -15.7743 | -49.94325 | 2024-10-03 00:28:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 6d7c8b89-c772-33eb-8a83-4e02e1b862c4 | -15.67594 | -39.21851 | 2024-10-03 00:28:00 | TERRA_M-M | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| d718f57b-666d-3435-bf80-83edb5a65d1b | -15.65281 | -47.19905 | 2024-10-03 00:28:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 56657c7c-dfaf-31fe-a546-ac669facab70 | -15.51549 | -42.23832 | 2024-10-03 00:28:00 | TERRA_M-M | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d53d5ec0-6cd6-3e0f-ae87-32fd4682927b | -15.44425 | -41.14193 | 2024-10-03 00:28:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 170070c0-41b3-371e-926a-4ed98fd712c7 | -15.25269 | -47.51157 | 2024-10-03 00:28:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f9e7617b-b46f-3795-9841-6be6c6187efd | -15.24775 | -47.5172 | 2024-10-03 00:28:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| d207cedb-56e7-3ca2-912e-89fb3b8fde91 | -15.24535 | -47.49543 | 2024-10-03 00:28:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 31.6 |
| b58dbaa6-dcbd-36ce-adc1-ea702f1caabc | -15.23881 | -43.34902 | 2024-10-03 00:28:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f99a632e-abb8-35c1-bd5f-37effb141b48 | -15.23866 | -47.51293 | 2024-10-03 00:28:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 18d5657d-31d6-3b71-9503-e8ab210ba162 | -15.23733 | -43.33692 | 2024-10-03 00:28:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 56.1 |
| e315fe57-9967-3057-a2fa-dba360ce312d | -15.23373 | -47.51862 | 2024-10-03 00:28:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 0224e770-3a38-382c-a9bf-6630a0db9246 | -15.23138 | -47.49712 | 2024-10-03 00:28:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 7a3b69c9-f8c5-3cec-9fbf-7731c944db77 | -15.14633 | -48.09548 | 2024-10-03 00:28:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 20b1050b-f265-32b9-8aaf-9c7c0ed818e3 | -15.08122 | -41.94482 | 2024-10-03 00:28:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| eb710468-1fb1-3feb-ae77-ed05b7641f49 | -15.07988 | -41.93457 | 2024-10-03 00:28:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| c9738bb5-0e8c-3ae4-a032-bd1267713d1f | -14.99358 | -42.24138 | 2024-10-03 00:28:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 32ab212a-ae01-31c5-a932-b055e3fd513e | -14.51558 | -45.23881 | 2024-10-03 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 3fdfc2ac-d1b6-38ba-ad7b-f2d3200ef215 | -14.51363 | -45.22263 | 2024-10-03 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 76c29787-4f66-3e08-bce5-2dde38947d83 | -14.20935 | -42.01598 | 2024-10-03 00:28:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f5924035-3fd3-3895-974f-6888f0d9f42b | -14.1988 | -42.07898 | 2024-10-03 00:28:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 57f437ba-f22a-3262-a8a2-681a24ea4e2a | -13.99114 | -44.03817 | 2024-10-03 00:28:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 52b66c2d-0f2d-379a-bf00-9fe90cbe4af4 | -13.88379 | -42.55367 | 2024-10-03 00:28:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| dd85b16c-58ad-340e-b16e-70677af8076b | -13.75648 | -42.61578 | 2024-10-03 00:28:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d8e2e5b4-58da-3c29-abf8-9637f8205552 | -13.74869 | -48.31865 | 2024-10-03 00:28:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 33.0 |
| e884bb43-4cf7-36ff-b5e8-220c42772452 | -10.91147 | -46.32463 | 2024-10-03 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 6cd85703-f8fa-38a1-998c-9293758ea1e8 | -13.38253 | -40.45951 | 2024-10-03 00:28:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a521a6a1-9dd0-3801-aa97-94ee9f0ed710 | -13.30877 | -43.71646 | 2024-10-03 00:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 7a5e80f4-c35a-3ad2-8034-567f12904ca7 | -13.30724 | -43.70449 | 2024-10-03 00:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8f1de38c-691c-35a9-8b35-65c9f912ca99 | -13.02378 | -40.33437 | 2024-10-03 00:28:00 | TERRA_M-M | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |


[Clique aqui para ver as próximas entradas](README16.md)
