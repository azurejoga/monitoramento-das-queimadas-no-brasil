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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a31cd2e4-c3c0-36f0-bced-e9860e6248d1 | -9.40899 | -48.44402 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0773136d-b0a5-3f5a-a72f-5ecc3604425e | -11.12159 | -54.63833 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8e358732-213b-3190-ab1e-19c2d4af5974 | -11.79353 | -48.08408 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14a2c88a-bc06-34fe-99b2-3723dbc15e40 | -12.54203 | -45.41459 | 2025-06-08 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8e50751-5401-3712-81d1-3da5e0ca63ee | -9.07601 | -47.14297 | 2025-06-08 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79097e76-57cc-37d8-ab20-921dee4bea77 | -12.53131 | -58.35995 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d46fb886-e631-3044-bcae-b57f73238354 | -11.36938 | -54.34005 | 2025-06-08 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 101617ff-e99c-304e-976f-485cc82f1ec9 | -11.37023 | -54.33541 | 2025-06-08 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c1a0c8f-ddea-3267-a7ff-d56468fc9e27 | -9.40561 | -48.44347 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 95d962f6-2982-309f-8102-247174b0d9d2 | -13.64828 | -47.76114 | 2025-06-08 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 173df521-5159-317a-a99e-bf0b3dcab884 | -9.69938 | -49.48039 | 2025-06-08 04:25:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15ae3ea9-3915-3473-8947-a321b4951112 | -9.92739 | -48.69289 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa725626-1227-368c-bf36-c4c3658da8ab | -7.73645 | -44.17914 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7fc91ac7-8a87-3772-b6a5-1c98cc66801a | -8.87164 | -50.18958 | 2025-06-08 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d9d41cf-74d6-3e97-a68a-7d30fbb2d0b0 | -8.18889 | -42.83427 | 2025-06-08 04:25:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec65ed38-99bd-3574-883a-4e47b7a70d38 | -11.37288 | -56.55085 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa0340af-6064-300c-9593-cdac959918c0 | -11.53768 | -56.45459 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d19486dc-f4d0-37b9-8245-fe458ba91c90 | -8.62658 | -47.1495 | 2025-06-08 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 740bc19b-07a9-3012-a53b-c0d203d3d9af | -8.30961 | -55.09928 | 2025-06-08 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d8b69a2-b1dc-344a-a27a-fd07fd9e1748 | -8.59984 | -49.70471 | 2025-06-08 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61388207-d37b-3447-96d2-35b57f2c9330 | -12.53053 | -58.36246 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faee33d7-ffd1-3f17-ba98-28bfa90480df | -12.26309 | -46.62891 | 2025-06-08 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 447237d0-f95f-36c2-a5b4-6809f2f7156f | -11.11886 | -54.65333 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dedfed9e-d0c5-3cab-bf95-0ec42f2c5759 | -13.54143 | -44.14639 | 2025-06-08 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c799259b-b62c-3ab7-bde5-96784c6c984c | -11.78104 | -48.31126 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb4c165d-018e-3f24-b694-fdc104255541 | -12.54549 | -45.41512 | 2025-06-08 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7f7423f-ab7b-359e-ab13-013ef718ecec | -8.08816 | -47.1165 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f8d5283-1f3a-3923-bfcd-6daa5afaf6ef | -12.06641 | -45.76327 | 2025-06-08 04:25:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| beeaabe5-f085-3146-88d7-899a776fd455 | -8.10359 | -47.16935 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5163168f-f8ce-3148-b387-710208760441 | -12.36349 | -57.40246 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 235d00d0-4095-3072-93cf-9908dd61de51 | -13.54379 | -44.1442 | 2025-06-08 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad5286b1-1e12-329c-93eb-285f0aad0c29 | -7.73474 | -44.16697 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 16395eba-2cdc-3a1d-b711-2c55f0bf368f | -7.41521 | -44.6108 | 2025-06-08 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d55d9f9-cba6-3d24-be81-b97ad9e5c26a | -9.38886 | -48.4183 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 236b304d-de90-3627-b910-0aecddaa34c8 | -10.49212 | -53.66299 | 2025-06-08 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0abac8b2-77b3-332c-addf-a1e0629c0589 | -11.79021 | -48.08353 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 241311ec-1dbc-34bd-b30e-5500097f0cd8 | -12.66798 | -58.21823 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24878e82-ba02-3ebb-8ebe-60664fb65119 | -13.36933 | -54.24954 | 2025-06-08 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a47bfed-1d0f-35b5-a9ad-181cd20a4198 | -7.86325 | -47.89122 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1405424f-ef90-3c1c-8229-9443ca93fa26 | -9.01418 | -49.14792 | 2025-06-08 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66a6e130-cf5b-3844-9e1c-b23a2a7c3ad5 | -8.52236 | -46.34526 | 2025-06-08 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c5d5804-9803-3641-948b-8b149298d9e0 | -7.72429 | -44.16542 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7c366f5-3e14-3b34-94e6-d59ad617631c | -12.51887 | -58.36212 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64f7473b-3e05-325b-9ed7-427387288cd7 | -11.80236 | -48.09279 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 88180748-7096-373b-86a2-a7b19edf0a5d | -9.03283 | -47.60586 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6a05230-4f4c-3e74-aee2-b007c4620c16 | -12.42105 | -51.16227 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93099564-9c0f-347f-a0de-7b59f17bf86f | -8.59404 | -45.86497 | 2025-06-08 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c104937-c6db-3424-81d7-e00cf81672f0 | -12.52052 | -58.35369 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b3d1fec-2144-3ae8-abe8-2843465d5610 | -12.36752 | -57.41098 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3b624a36-38c7-3c6e-ba01-51c4353fc4e7 | -12.51805 | -58.36464 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6ae966c-7c22-3a7b-bc27-fb6a23315cb2 | -9.86444 | -47.33412 | 2025-06-08 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98407994-a3fa-3f7c-b0d6-b2a10162891e | -7.86547 | -47.89896 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c6c8558b-4fe9-36e6-add3-8e94b441914c | -12.21146 | -49.63534 | 2025-06-08 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4b8e050-a8b4-3a4e-803f-2f66a6e7ebcc | -8.7773 | -47.18462 | 2025-06-08 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 905b8873-1e2a-3b5e-9f19-831224111e5b | -12.78236 | -48.71885 | 2025-06-08 04:25:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 743e0fe2-f921-3f8b-94eb-e85462a1a468 | -12.54607 | -45.41124 | 2025-06-08 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4a27ada-b82d-3b94-83d2-f43c0f4c4936 | -8.11457 | -47.61387 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfa17cbd-f936-37f5-a10f-5ae3ad61a8f1 | -11.3762 | -56.56194 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d4015bf-f842-332b-b738-5142e16721bd | -11.80568 | -48.09334 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5884ad4f-ae26-3fa8-a5f0-42ade7454ff7 | -12.37297 | -57.41213 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f1418830-e98e-3fe2-a4f2-819c5585952c | -9.052 | -47.91383 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d53fe76-b736-3f03-9108-88eedcede2f2 | -11.12068 | -54.64331 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 346299b0-006c-3477-aef1-347a26eb9118 | -13.5407 | -44.13914 | 2025-06-08 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae425b0c-4dec-3e8b-bd67-98ec37029ca8 | -12.9728 | -46.75628 | 2025-06-08 04:25:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 841b674c-5e37-311f-81be-0b170bdbdddd | -10.94652 | -55.33399 | 2025-06-08 04:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e439172-d921-3513-8206-4e42cc7c83de | -9.02505 | -47.61184 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be839d7b-f866-3c5f-b560-90bcb03b8f51 | -11.12532 | -54.64428 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 59080d6f-7446-316f-b21e-af9ba92cb866 | -9.58829 | -48.72858 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0a1466b-73d3-3772-ae33-3b1cf10f3728 | -10.19942 | -47.3203 | 2025-06-08 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7ab8d99-b23c-3ded-ad80-315f4efd442c | -12.37307 | -57.41456 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46f22da9-7d6c-3c28-949b-3bff83c270c7 | -9.07323 | -47.13897 | 2025-06-08 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bc7f75e-8d51-37fb-a831-40fec9538812 | -11.79685 | -48.08463 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db3ae996-842c-3e1d-a7bb-25ea453f4323 | -9.50709 | -47.40191 | 2025-06-08 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63c248b0-3a73-3252-882c-5e75d8ba5911 | -12.37852 | -57.4157 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7152720e-30f7-3df8-811d-0dc6ac10252d | -12.10471 | -49.4741 | 2025-06-08 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1023da3d-0780-37ff-9238-363500e7c003 | -11.11977 | -54.64832 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 789620ec-a294-376c-b575-b2a7a0176cf7 | -11.13848 | -53.94538 | 2025-06-08 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 343a7554-ebcd-3052-a59c-2df23e5897a1 | -8.09147 | -47.11705 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 492c0cae-29f5-3bdf-b3c2-578c724c512d | -13.94392 | -47.19371 | 2025-06-08 04:25:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52f23590-d004-352c-a620-af5a4acbafd6 | -12.37381 | -57.41089 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9fddfed5-c27d-39ac-ab03-5a5cedc15111 | -12.5255 | -58.35893 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6edaecd0-be4d-3374-98f9-d2a1d46a34c4 | -11.37813 | -56.55193 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fb88c93-7402-3e6f-a05a-117b32ed8a8c | -9.07268 | -47.14245 | 2025-06-08 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4b6d72a-7053-381e-b3e3-dd79cb16553a | -13.28243 | -44.17977 | 2025-06-08 04:25:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7dc6957-1e32-3432-94db-9eb64f9cb1fc | -9.84301 | -48.60792 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96d53997-fef1-3569-8515-8f8405a9c629 | -12.97505 | -46.76391 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94ec4988-7d95-3a46-9c2f-b459206c13f9 | -7.73297 | -44.17861 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 796bafb7-811d-3759-885c-6e4352f087d3 | -9.40972 | -48.44791 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c17c8bdc-cc8e-372a-9702-f7a99589942a | -11.36724 | -56.55664 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7fa4154-b7dd-3f82-ad8d-2c5f62be4d54 | -8.72523 | -50.03539 | 2025-06-08 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29e1f821-dd6e-36a0-b0ea-c8f122bcc8e8 | -10.64579 | -44.48933 | 2025-06-08 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 235002c9-9695-3cb9-9afd-a59331d6d52e | -7.73763 | -44.17138 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26595322-11b9-37a9-b25a-c5238f700ec9 | -12.36823 | -57.40727 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2c66fef1-9785-37cc-a60b-3b1278df7d3e | -9.37724 | -48.81686 | 2025-06-08 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e3943c54-7c8e-33fc-9933-07a74caf9760 | -12.9875 | -47.12452 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f087ebd-e860-365d-bb8c-b0e86f302864 | -11.53706 | -56.45789 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16c4e535-40b5-3af9-a125-60c29db5fba2 | -9.43726 | -40.34941 | 2025-06-08 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8b40de58-fa6a-31ae-9297-0b474cd9d9ef | -8.41125 | -47.05043 | 2025-06-08 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1548852f-8847-3614-a45d-64c613105d27 | -9.05534 | -47.91438 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5688bb5e-d74b-3107-a576-e54aef1f0870 | -9.02838 | -47.61237 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
