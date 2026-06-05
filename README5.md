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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bed51e0a-93ca-31e8-87c5-860f99facefa | -7.34754 | -49.83372 | 2026-06-05 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b1271dab-4cc0-3d38-b5c0-535ecfdb8765 | -9.92787 | -48.00408 | 2026-06-05 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9675c2d6-187a-36fd-9be4-0c9d45144502 | -9.90466 | -47.48054 | 2026-06-05 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d51a2b41-ae18-346d-8909-c2152c534004 | -7.64841 | -45.2393 | 2026-06-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a2460a1-dce2-3369-926c-a1d0a1f2c614 | -12.53402 | -45.67605 | 2026-06-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21b911b6-721f-3254-9f95-ee886d537655 | -11.38879 | -47.81844 | 2026-06-05 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f486f73b-54ae-3bf3-8973-63319ff4f869 | -8.3689 | -46.79813 | 2026-06-05 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 668db665-e6fe-3371-b64a-39672208bd1b | -10.51878 | -42.37595 | 2026-06-05 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 6230df84-64ca-3c0c-ab85-8fee686de877 | -12.00024 | -45.35016 | 2026-06-05 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97bc6af3-e4eb-36eb-bb4e-b7b930121a54 | -12.50397 | -46.34441 | 2026-06-05 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 166c7bc6-1427-3332-a2f1-852b52a7bb3f | -9.68447 | -47.0435 | 2026-06-05 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddc187f1-ab9b-3a29-b017-91d8179a0130 | -10.51967 | -42.37084 | 2026-06-05 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 086d7692-f52b-3735-bae4-ffd09e615f95 | -12.06417 | -48.07459 | 2026-06-05 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4a4fe6f-a8b0-3f24-a7db-d5dad4b40aba | -13.66959 | -47.75132 | 2026-06-05 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1219019-9bc5-3b5b-b71e-8a2cf7bc432a | -19.28158 | -40.44042 | 2026-06-05 03:51:00 | NOAA-21 | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 421f6432-123e-3ce0-83b2-4bb9b05e7b9f | -13.66892 | -47.75468 | 2026-06-05 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b41ef955-1183-3675-a870-3fdc0a02b4c7 | -14.76946 | -52.67859 | 2026-06-05 03:51:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 20ac7e41-3995-393a-9681-3f1a6be3e98b | -19.0574 | -44.80401 | 2026-06-05 03:51:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71d2931d-6330-361d-b123-f48edab6c28e | -14.1567 | -51.59317 | 2026-06-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee240fbc-4180-32fe-a7cd-dda72319790e | -15.31698 | -41.90177 | 2026-06-05 03:51:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 7fee9913-7580-31d1-b845-669fb045727d | -17.78425 | -50.47028 | 2026-06-05 03:51:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 56e22931-2673-34d9-a338-50e6fd53763a | -13.66541 | -47.75337 | 2026-06-05 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18054119-99b7-32db-8da6-4ffa0119f724 | -14.79767 | -42.80801 | 2026-06-05 03:51:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc9793c2-c303-3d52-8172-520e40aa8312 | -13.6676 | -47.76134 | 2026-06-05 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4fe748d-7f2b-3a02-95d2-8545c2bffcd8 | -17.78455 | -50.47244 | 2026-06-05 03:51:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7cd0df62-5f10-3374-af97-3a825e7c0946 | -21.6589 | -41.3249 | 2026-06-05 03:51:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8dadc1d4-8789-3821-a911-e73cf4be1f99 | -14.37416 | -45.56016 | 2026-06-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95f392c8-f446-335a-ac0d-ace31a1b1554 | -13.66412 | -47.76012 | 2026-06-05 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdf42374-dc53-3a91-81c4-5dc137047c6a | -14.37328 | -45.56493 | 2026-06-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a0ac0b9-a8d2-39fe-8441-bca4bc202e51 | -20.66247 | -45.50362 | 2026-06-05 03:51:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ab7acb6-df57-39d0-bbcc-0f8e271166ab | -13.66826 | -47.75801 | 2026-06-05 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 318607a4-97d7-3b33-b137-e4fce5e44489 | -14.76851 | -52.67531 | 2026-06-05 03:51:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18b3bac7-4c0e-386c-80b7-ad99b3c5ed75 | -15.31413 | -41.89688 | 2026-06-05 03:51:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9d11a8b5-25f4-3e89-8d34-063bd9a91016 | -17.78544 | -50.46822 | 2026-06-05 03:51:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 30127071-baaf-3d0a-94a7-ac4652ff86d1 | -16.22939 | -40.14861 | 2026-06-05 03:51:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 081a2cd2-e745-3361-8d27-7e1966faccc9 | -17.7784 | -50.46912 | 2026-06-05 03:51:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 820f06f0-86c7-3aa3-b8f9-b4e5f266c2ec | -14.37883 | -45.58575 | 2026-06-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d67ce31f-9210-3de6-ace5-f63f21bdf6a0 | -14.37429 | -45.58487 | 2026-06-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19a691f2-4270-3b89-92ab-f754d685975c | -20.28131 | -46.48098 | 2026-06-05 03:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff3f5d25-6bf6-3e88-a4be-bc1cc2985b51 | -14.77537 | -52.67727 | 2026-06-05 03:51:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8f022a8-2bc7-3919-ba58-a787ffefb978 | -13.66476 | -47.75676 | 2026-06-05 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77096bfb-3d4f-354f-b8b9-89b6ef6e7088 | -16.22815 | -42.78574 | 2026-06-05 03:51:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 952f92f3-bd6e-3b4d-a23f-6a728b0ef124 | -20.28218 | -46.47654 | 2026-06-05 03:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b885731-fff1-3fb4-9afb-3710488ad4d5 | -19.97908 | -44.85659 | 2026-06-05 03:51:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f96e2c36-9694-35df-a6ba-60bfcaf468ff | -17.77871 | -50.47127 | 2026-06-05 03:51:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2becbe16-0e17-3090-ab74-556c99d5f58a | -14.1534 | -51.59409 | 2026-06-05 03:51:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d640326-04e0-35b7-88db-dc598a9716d0 | -15.31772 | -41.89749 | 2026-06-05 03:51:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 2b80df14-891a-3c84-bfec-2d88e214b1b1 | -20.36976 | -41.9111 | 2026-06-05 03:51:00 | NOAA-21 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3e032fee-180d-3458-aa07-967a30799a13 | -21.80806 | -49.11515 | 2026-06-05 03:53:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d68382ac-24ca-3664-9472-236267d38296 | -21.80671 | -49.12149 | 2026-06-05 03:53:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aa66abea-17b3-32c1-ae56-36151bdb9453 | -23.14793 | -47.08496 | 2026-06-05 03:53:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 853257c9-d380-3ab7-8a86-cfa0fe1ed21e | -23.31502 | -46.11341 | 2026-06-05 03:53:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 626fd0e2-6a5b-3e89-b770-e0ed3ead2fe0 | -22.09053 | -47.0635 | 2026-06-05 03:53:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 602ce5bb-13d5-3d70-9a26-6b7d720f5fcb | -19.72119 | -54.6577 | 2026-06-05 03:53:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0e062cec-4614-3f7a-b241-57a6e9e5cbcd | -22.67366 | -47.40839 | 2026-06-05 03:53:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1661ead7-9301-39a9-af0a-f6236d39862d | -19.72615 | -54.65189 | 2026-06-05 03:53:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1a8413f8-944a-3f78-9236-3e2005e74fbf | -19.73654 | -53.54652 | 2026-06-05 03:53:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 16.4 |
| feda1427-59f3-3838-aec0-c252d89eae42 | -21.81231 | -49.11958 | 2026-06-05 03:53:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8d2cb7f7-3274-389c-bf2e-41d7999aee34 | -19.71916 | -54.64988 | 2026-06-05 03:53:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 16401e23-96f6-3985-98b6-5f1dc87beaba | -23.81984 | -48.70983 | 2026-06-05 03:53:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b80ad5ed-df68-34fe-a3a1-c76cd830df43 | -22.67456 | -47.40382 | 2026-06-05 03:53:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55a63a9b-a8ae-39ac-a526-2358f3f04683 | -23.81747 | -48.71107 | 2026-06-05 03:53:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e52a015-cb31-37d7-9225-e97c50bd517b | -22.08936 | -47.06496 | 2026-06-05 03:53:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c445ae36-2c03-361f-aa76-fd35d1ba195a | -21.80738 | -49.11834 | 2026-06-05 03:53:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e7e3098-4d49-3a0e-8b42-d369bb49f94d | -22.67377 | -47.40651 | 2026-06-05 03:53:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 419faf6a-896a-3ea0-8de8-6de8d1af5974 | -21.27694 | -48.61798 | 2026-06-05 03:53:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a29daf6b-ebe5-38d0-b2ad-335b925ab53b | -22.58208 | -46.1163 | 2026-06-05 03:53:00 | NOAA-21 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 44ccbcf8-1c0b-30d8-b783-63f38cb914e9 | -19.72288 | -54.65078 | 2026-06-05 03:53:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0d5ad8f4-232e-3145-b13b-721039dc6d1d | -21.80605 | -49.12458 | 2026-06-05 03:53:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9a7c5e70-0d2f-314f-9178-8c27c232c09a | -19.74315 | -53.54836 | 2026-06-05 03:53:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 823c6298-6ec2-3c6d-8e07-a9a29cb29c48 | -5.30193 | -47.24202 | 2026-06-05 04:21:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 462cb5a9-3096-3147-ad16-3b764e335840 | -3.98836 | -47.93297 | 2026-06-05 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ea0d19a-3be0-3beb-9928-d0f4b498d4c7 | -4.63597 | -43.05014 | 2026-06-05 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44f63456-f734-3927-bcf7-95ee11bb52af | -5.8134 | -43.793 | 2026-06-05 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa64cfa4-83e3-312a-9440-582fc72e98a5 | -5.72276 | -45.03648 | 2026-06-05 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 710e3569-e92f-377f-9050-992b665f5672 | -5.05812 | -39.93523 | 2026-06-05 04:21:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c5446526-b82d-3bfe-940e-6acba0a13ab3 | -5.93021 | -43.48299 | 2026-06-05 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20fad6cb-c67f-3fab-a2f2-83a76dc52cc5 | -3.98571 | -47.93232 | 2026-06-05 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78eb66d5-a159-3ef8-aafc-0467f62498ee | -4.63264 | -43.04961 | 2026-06-05 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4819177-83fc-34de-b5c8-6e235cf085d8 | -5.92966 | -43.48647 | 2026-06-05 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57102889-2b51-3397-bb0e-71be69dcf32d | -5.81396 | -43.7895 | 2026-06-05 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 945fbab3-ce63-3362-b4ac-0eb86a5c20c6 | -3.98629 | -47.92869 | 2026-06-05 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98dede0d-421f-3e2a-a475-8dedc6c2982b | -5.93409 | -43.48005 | 2026-06-05 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a3dbec0-1329-334d-961e-102da75484fd | -5.92744 | -43.47898 | 2026-06-05 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0fd26929-7c2d-3e9e-a4f5-a84cb5192f65 | -5.93077 | -43.47952 | 2026-06-05 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e8a1995-76ec-32da-ba2d-3224a04a3e34 | -3.95923 | -43.11375 | 2026-06-05 04:21:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7e079cc-e13c-34ff-9307-95734cdb6544 | -3.98898 | -47.92933 | 2026-06-05 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ec29f19-f98b-36f0-956b-26b6f5b1fcd5 | -5.72395 | -45.02903 | 2026-06-05 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79117b8f-e875-320c-b8d2-56115567d1ed | -5.81006 | -43.79247 | 2026-06-05 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 998361b4-989c-3e4d-b1ed-5da9002a9273 | -5.93354 | -43.48352 | 2026-06-05 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0830a677-69f0-3ca6-982d-f0bee03d3543 | -5.30657 | -47.23787 | 2026-06-05 04:21:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9abdfdfc-acd4-32aa-96a8-8022269420ad | -5.93299 | -43.48699 | 2026-06-05 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0e25333-e9a3-3084-a14d-1e23ba2150fd | -3.98487 | -47.92876 | 2026-06-05 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f9edc4e-313d-34c8-8b91-772ab103d852 | -12.00047 | -45.35733 | 2026-06-05 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9d40204-b605-3947-98ca-b51b760fd9e4 | -12.00105 | -45.35376 | 2026-06-05 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4a82553-a692-37ad-99c3-f841f494496e | -8.40981 | -46.89745 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 181a41aa-eb37-38eb-a386-185a3fdf88b9 | -11.04625 | -49.61469 | 2026-06-05 04:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca6d76f8-2318-3102-bca6-5e03930c7eb1 | -8.64629 | -45.76881 | 2026-06-05 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a388f1-ddd0-3310-b4b2-a8d2a557a316 | -9.37575 | -50.54045 | 2026-06-05 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 657e53cc-d6bd-3b14-9079-8fa633d85baa | -10.93617 | -46.94809 | 2026-06-05 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
