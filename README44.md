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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfc1ccf7-cfae-39af-8c24-266eb5e7ef1c | -13.32418 | -43.59486 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05f1ea59-3fdc-3366-8ae3-29ee26a0c659 | -11.49567 | -50.37529 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 123b040d-1d7b-34fd-9a56-b26005550385 | -15.78643 | -52.25344 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ad730a6-cb7c-335d-964d-50bea1168f23 | -12.87421 | -47.95189 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8744c79a-9777-3eab-b652-5e11cf4bac51 | -17.13962 | -48.49149 | 2025-09-12 04:06:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a63255db-de0e-3c11-acd8-2b75d439d150 | -11.18623 | -55.06559 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 103fbdcd-5787-34da-b916-269fbd1f92d1 | -11.18741 | -55.08245 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e4cb0aab-9a70-33f8-8a7d-e50c6eafbfa4 | -16.60337 | -49.78748 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 15d471a8-65a3-33a7-a3be-63dc9b4c8aec | -11.51937 | -50.3795 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41f0d222-4b87-3cc8-80b2-0384f420be48 | -14.268 | -49.66332 | 2025-09-12 04:06:00 | NPP-375D | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f0f6cb8-2f24-3150-a433-eb82af9dbaeb | -17.86305 | -44.17428 | 2025-09-12 04:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a88c0e49-4117-3128-b385-a3d2ecb4fe6d | -11.51805 | -50.38625 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4670dfb6-0448-3943-b6f0-0a76955ec59c | -18.05083 | -45.43361 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0069631-dcda-37f5-9590-1f0a3c8f5c07 | -13.8993 | -48.23765 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fb5c410f-0bdf-383f-9212-6731c38c880d | -12.83394 | -47.95834 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2d1491b-0fcc-3f4c-b060-201982c01d59 | -11.51837 | -50.58611 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a4451da0-07aa-317c-bf9c-8fb5bd5ffc8b | -13.89116 | -48.23206 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e8b45d01-e1af-3c3e-a82a-88db24389c88 | -17.75222 | -44.44278 | 2025-09-12 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1c6aca5c-1b04-3c0d-a0e4-01ff3bccbb68 | -12.01114 | -48.55027 | 2025-09-12 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e521afdf-3e30-3072-81fd-983f96e0363c | -15.68567 | -47.04869 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 298233d3-2f34-326e-a789-1e8a039cb894 | -13.14689 | -47.14736 | 2025-09-12 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c25567d7-4986-3acd-85b5-659fd11a9fca | -14.51278 | -53.90605 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a34f3237-e179-3c75-9386-426db48a9ee8 | -12.15098 | -48.69403 | 2025-09-12 04:06:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4f17c7f-6af1-36d1-964b-d60ff692cd30 | -13.30925 | -42.38384 | 2025-09-12 04:06:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a926f281-a0b8-326b-a5a4-da8297f938fb | -14.14864 | -44.44922 | 2025-09-12 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89d5472e-344a-3faa-8484-c14cfeb6a44c | -18.05107 | -45.44499 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| deef65e3-7168-32b4-a0cc-83b34a70872f | -15.1505 | -52.46745 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 50db927d-f195-3422-b5dd-63c00f5bc391 | -12.82276 | -47.96947 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5da18e04-c2fe-3e80-a2bf-d6884fad11ff | -14.32381 | -54.12863 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 692b3613-bb7e-3cf4-b79d-feb4d74ac4d0 | -17.36287 | -46.69904 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7f244468-a2ea-3392-836c-1cc9e90e7fb8 | -18.30569 | -45.0144 | 2025-09-12 04:06:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa56fc84-0806-33ac-9a7b-47f7d21d81f4 | -16.60718 | -49.78683 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 722a6846-dea5-3e2e-966c-314807ce0bb9 | -15.83568 | -47.09863 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4089989c-3f0c-3d22-8c18-adfc7cc8fe87 | -15.10367 | -48.00667 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 406f0c44-d989-39ed-b4bb-00e7251d82f7 | -16.59925 | -49.80824 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d11a918f-3824-3843-b106-066cb796bb76 | -13.78265 | -46.28504 | 2025-09-12 04:06:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 80f62709-3061-3877-acea-50e79ae90bd5 | -11.52108 | -50.60116 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ced8a8c-e276-3f63-bcd5-f09b74a6be1d | -13.37008 | -41.91958 | 2025-09-12 04:06:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a4426850-9842-3b60-a440-b78cb1550a4f | -14.04079 | -42.15168 | 2025-09-12 04:06:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 16c119b9-56f3-3394-b30c-796acd196f62 | -12.98999 | -46.74354 | 2025-09-12 04:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d0ae176-b0db-3706-a9bc-00d4440975c3 | -11.9818 | -51.12463 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0020e1da-c495-35f3-a729-b95408bfb18e | -13.1476 | -47.14342 | 2025-09-12 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7af59064-814b-3f07-91f4-96e249e227e8 | -16.28429 | -45.67967 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97105859-8807-352f-b2a7-055c0a69782e | -15.74635 | -48.38101 | 2025-09-12 04:06:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05762911-4bf7-348d-87a5-dfa779bee305 | -16.43763 | -45.68342 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f5105ae-ebdd-3f8b-981f-95150b7872e0 | -18.05181 | -45.44078 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b922261-0cd6-3cd1-b76f-dc79ba309281 | -14.11702 | -44.31959 | 2025-09-12 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdd392b4-7588-3a17-b92c-146571c26808 | -12.81748 | -47.97333 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fa3f96d6-dd75-3ef4-be2d-dbc81b7d11a7 | -15.53007 | -48.55032 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8f346f2a-8944-3e3d-8615-31d2e25e2248 | -18.05328 | -45.43236 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5f6daed4-9388-38c7-bfce-56fffa8d16c2 | -17.34354 | -46.67499 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 774d7641-879e-3632-bd1a-4c45b1873034 | -17.2141 | -48.69717 | 2025-09-12 04:06:00 | NPP-375D | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 343b951d-8b89-3c2e-85c8-15b6c6c5686e | -11.10852 | -50.71397 | 2025-09-12 04:06:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e304de8-f2d5-357f-8964-cc50a9e9fddc | -17.55117 | -44.54012 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2eaca231-a51d-33cd-8561-ebd5a029a37e | -11.53189 | -50.60335 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b40cccaf-2951-3534-ae1d-092dd5b99ee0 | -14.03746 | -42.15112 | 2025-09-12 04:06:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 97cd9fba-918a-3842-9dab-8683e6beddba | -17.85965 | -44.17366 | 2025-09-12 04:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d4f3a7ab-5755-3825-a465-d87798547d01 | -11.86179 | -46.75497 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93368524-4d3a-37c4-bc9f-9b6457f8a009 | -17.47267 | -43.72274 | 2025-09-12 04:06:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc09d99a-4a96-3ffa-809a-959ea936724c | -12.86464 | -47.95399 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e034bf53-3228-3c8e-9c08-4bce2449fb47 | -17.8203 | -46.73433 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ed0a06f-911d-325d-975e-9373a3113eb0 | -11.86018 | -46.75944 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20d877db-10a1-3873-a59a-37e5c8a9f0fe | -16.42353 | -45.69929 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84f7dbe5-ed69-319d-b1bb-f4b907c416d3 | -13.37065 | -41.916 | 2025-09-12 04:06:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 548ee4b7-73dc-3539-8ed2-bf360246eedb | -15.51448 | -47.61892 | 2025-09-12 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afde2612-bf13-3a8e-9d92-8ecd7de04cb5 | -13.16691 | -50.09005 | 2025-09-12 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e64573e1-db90-350d-8def-2e165f016e6a | -15.52811 | -48.55353 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| db599794-7961-35ee-99a5-f10a49b4a1de | -13.26227 | -43.75175 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a01bc996-cc3f-3440-9fb2-4060b8018971 | -17.47206 | -43.72649 | 2025-09-12 04:06:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f20b084-983e-3041-a6f6-1185ed8e50b2 | -11.8433 | -47.09888 | 2025-09-12 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaafddb8-2031-36fe-ac4d-261a33695cbb | -15.57473 | -54.75357 | 2025-09-12 04:06:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e105f7b6-3f5d-3c96-872d-c45d7591be10 | -13.98783 | -48.22149 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| febe216d-038e-39fc-845e-2377664cc59a | -11.86086 | -46.75554 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af466690-19d4-31da-9447-adf0c5019800 | -11.92466 | -50.71502 | 2025-09-12 04:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e123c64b-588d-3ed5-888b-f45e9be08115 | -12.81908 | -47.97664 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cb9a58a1-6c0c-3b5a-b998-430cc0969ccc | -13.35896 | -41.92498 | 2025-09-12 04:06:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9822d00f-f0ec-3b19-a0d4-89dc486301dd | -14.18036 | -46.21166 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f5378674-0170-38c4-b507-79b3ae5606a8 | -11.99873 | -47.76661 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2d8b945-7325-3596-85d3-b89fa7ee967b | -11.70211 | -48.28535 | 2025-09-12 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18672352-9b7e-3acf-93e3-da97a74ebd64 | -12.58401 | -45.68105 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99babf72-97cd-3017-bae9-3fecbec7dda7 | -13.91663 | -47.9747 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc503354-4388-3cd7-b7d7-c5c7b22e475d | -11.92265 | -50.69645 | 2025-09-12 04:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66c68386-29a6-39b1-9350-5b19b8f48dfc | -16.49198 | -51.97057 | 2025-09-12 04:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f62daf5-fa33-349b-b581-02c3ce10f96f | -17.66401 | -46.67941 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| add0c55c-08a4-3a16-8a15-8c380bbc0408 | -16.41543 | -45.70236 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4786e99d-d7f9-3ffa-a4be-d73927666218 | -11.53675 | -50.40405 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 2a7bfeaa-eec8-3633-84a2-00abb4506c40 | -12.81063 | -44.75626 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43ccd99a-e58c-3e5d-a795-78edec3ad90c | -15.57343 | -54.75323 | 2025-09-12 04:06:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d60cb60f-4c1b-38d0-ae65-ce7e31641c91 | -11.95353 | -51.181 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 19f9aec0-a5c6-3107-b2f6-01c00d8d92ff | -17.94757 | -45.274 | 2025-09-12 04:06:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9611e0c-85cc-3581-bfcc-f0efcff3887e | -16.65257 | -47.62777 | 2025-09-12 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e322b25a-3d10-3911-8a27-71d1401fc0c4 | -15.6617 | -47.04437 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7b6bd3eb-7ae4-3c55-818f-26cab7640ca9 | -17.82278 | -46.72798 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c31fa29b-1326-34fc-a921-06e0fa3ccdee | -15.10214 | -48.01477 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07eecf5d-a48f-3b1e-81ff-afc0965c2460 | -17.72766 | -46.15145 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44df065d-4151-3288-a08c-32d053bb7be6 | -16.49353 | -51.97035 | 2025-09-12 04:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed05c862-7102-3b88-96a7-66641ee1a2f2 | -14.77158 | -48.23246 | 2025-09-12 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5228490-aed0-344d-b913-0ea370dfc037 | -11.53322 | -50.59636 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d0baa2af-e488-3e4e-9979-a19b06b8e280 | -13.7787 | -46.28448 | 2025-09-12 04:06:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d919e8bd-8b5f-3313-888e-cb8a93ac0834 | -12.86977 | -47.95106 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README45.md)
