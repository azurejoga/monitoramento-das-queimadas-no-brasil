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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63ada537-1f16-378d-b093-fe52887ad8c5 | -13.44812 | -47.00966 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdf422d0-fa28-325e-84e9-d0ca09c7c2d7 | -13.51725 | -46.89231 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18566d8c-3690-3545-8970-4a57137e043e | -13.41257 | -46.88958 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1c4fbb43-757f-3f2e-8b9b-2a3b958fc1d6 | -11.04913 | -52.02097 | 2025-08-26 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fc8d29f-db4c-31e3-9395-e2a113bcebdd | -13.44432 | -46.99057 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f25a628-198b-3647-9f7f-66fa7c3f50d9 | -13.64782 | -45.70594 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fa9fc3d-1c84-319a-925a-273db85b73d7 | -14.2942 | -60.36543 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d0d645a-46f2-3280-b6d9-a44a79d61ea8 | -9.16407 | -59.45569 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce9d86e1-1d9f-38a3-b749-3d490bb6f544 | -16.74522 | -47.59809 | 2025-08-26 04:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea58eeba-e6d5-32e9-ba0a-14ad2a4ce132 | -13.61202 | -48.15112 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d1165705-4161-36bd-8b89-cca1ad664682 | -11.53617 | -52.1224 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3e0dd74-479c-3243-a74f-193535b3dde9 | -12.76099 | -48.14294 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51a61713-73a6-3ddd-8ca7-5630244d4b74 | -15.64484 | -52.73403 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8b2b3cd-c959-32c2-af68-f014e98ef5ce | -11.52744 | -50.45369 | 2025-08-26 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3a6f8c8-0998-3ad7-95e9-e42a526d4114 | -13.41371 | -46.88249 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3b744e8f-5c3a-3082-a27c-9ae995c0b22a | -14.76017 | -59.71243 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54508bef-7c6a-3ccc-bd9a-0f59fe523a0b | -11.62728 | -46.20895 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2dfd9f1-c3f6-3746-aac3-a1107257d2fa | -14.27547 | -49.13565 | 2025-08-26 04:23:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ce109ff-549a-3b0c-bcfb-a0bf4ece4974 | -12.77196 | -48.10784 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 289b04a9-8dde-3542-b22c-ebf39a686053 | -11.52057 | -52.13123 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c9c1d032-087d-39ea-b7b3-d1b583c9b71e | -9.18304 | -59.50776 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3f121c3d-7d7c-334e-b3c2-62a181ef2238 | -13.44535 | -47.00549 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 536b82cc-4146-3579-a3b7-2557d9539da4 | -12.4299 | -45.97025 | 2025-08-26 04:23:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1ecb8020-fd38-3407-9015-ee9de4cdad06 | -11.63231 | -46.41336 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 837ef7db-d6ba-3df3-8e96-e63aa82eab35 | -13.49668 | -46.87813 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50608d89-4b73-341c-a7f9-33dd9d226d74 | -14.6395 | -49.07626 | 2025-08-26 04:23:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 709ab457-a5df-3bfd-aa5f-e97c4fea6c1e | -13.10925 | -49.33358 | 2025-08-26 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8a445ef-13b0-39c8-a9a2-df54c6a853aa | -12.94302 | -46.34112 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc701d68-2b05-302a-9af9-2007a8c8cb2a | -11.91596 | -47.60165 | 2025-08-26 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7276b60a-55e9-3ddb-9351-fac8d6607943 | -15.07815 | -48.66217 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60b1a2ff-c850-3cef-85a2-185e4927295b | -12.72927 | -48.14132 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f52aa64d-095f-3029-8643-1c9d615dbf20 | -13.52436 | -46.91197 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4822bed1-fb64-34f6-9b9c-98fd7a04a76d | -14.80243 | -48.96724 | 2025-08-26 04:23:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ce2ca89-517c-3b33-b7f4-4709cdd66bfd | -11.62904 | -46.3909 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68997c83-716f-3003-b11b-85e5aacee8b3 | -12.77836 | -48.13321 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e71a5478-8d5d-3263-95b3-dfcaa86b1c3d | -11.54801 | -52.10524 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fd331a1-9bda-3c47-adf0-86800b3f348d | -9.17377 | -59.5189 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 53521676-dbdb-3770-97b3-0196a5113126 | -10.54247 | -57.9632 | 2025-08-26 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 381de700-2e1d-3e6c-8545-51e126612e07 | -13.43692 | -47.01519 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a031e8c3-c592-3c30-a3bf-2f696406b8ed | -13.45389 | -46.86713 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c302d36c-7463-3af7-a9b1-cd0c8b8e7b35 | -17.20094 | -44.3216 | 2025-08-26 04:23:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a529a087-fb86-3440-9886-54b04f99337d | -10.87216 | -55.79548 | 2025-08-26 04:23:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a374bf8f-c7fb-367c-8681-5c4f854dd31c | -11.52948 | -52.13464 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d1922249-d3f5-3f64-83dd-d324e751a7cf | -11.55445 | -52.11962 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9929a2aa-503e-31d5-bf56-650c197ba315 | -9.15833 | -59.55672 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e77fc3d3-42be-3540-a24e-246e547dd7cc | -9.16563 | -59.51971 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8dfcd0d3-5eef-3b42-b9e6-82534d48ea58 | -9.18015 | -59.44607 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0bbe8675-ef48-35e2-b43c-bb332a7121d0 | -13.83097 | -46.69201 | 2025-08-26 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35ce0d0d-3902-39fc-bde2-e799f0e82e38 | -12.70895 | -47.87947 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be0d43d9-11f8-38d7-b70d-c912d8cabf66 | -13.41464 | -46.9193 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75726fb6-9634-347e-beed-5d509f47c53d | -13.4961 | -46.88171 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65fcd3f4-ab44-3b3e-9f2d-227851b0a664 | -13.42406 | -46.92466 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2eb3862c-f045-3af3-83f9-0c0449631cdd | -15.07535 | -48.65774 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aaf65847-0daf-3f25-8129-5fb84be889a7 | -9.65125 | -59.63211 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c68abf1-b27b-3ed8-baa6-f8e0f1d35129 | -15.05282 | -48.69819 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ee4d9e0-7a44-3983-a224-696b16f9db68 | -11.53533 | -50.45511 | 2025-08-26 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f56c3c04-fa84-3b34-94af-38dd7768090b | -12.76162 | -48.1391 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3349f100-516d-3ac2-b151-e0622e4e39fc | -11.53892 | -52.13012 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 38893d9f-c1af-3dff-8c77-761602651584 | -12.48396 | -47.22874 | 2025-08-26 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9c1db77-8214-3728-bb3c-1d2ca5753516 | -13.83373 | -46.69614 | 2025-08-26 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2150e24e-1e7e-3770-b60b-7c469d6ed87a | -9.17529 | -59.51141 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0b999199-7315-3d47-84b4-8653656f81d4 | -11.56993 | -52.10921 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d96bce80-00ca-3a5c-9b3d-f973a4695fd3 | -17.79357 | -44.49475 | 2025-08-26 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 316e2358-97d2-3034-a765-2074cf419692 | -19.92226 | -44.62007 | 2025-08-26 04:25:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fc71a918-7362-30fc-bfd1-e923c79b4dff | -19.17885 | -48.73398 | 2025-08-26 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ffab29f7-943f-33a4-9a8d-a5bd2ff04b7b | -22.55268 | -49.76915 | 2025-08-26 04:25:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bcafd798-c7a1-3a24-a671-d22a25ed0fd9 | -20.37908 | -42.19983 | 2025-08-26 04:25:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 348cf77a-87dc-35b6-9055-a4965481cd0a | -18.85426 | -47.00441 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b256216-c087-3ffe-b586-fc02a9d80f83 | -21.54532 | -41.22932 | 2025-08-26 04:25:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ebde12c1-1711-30d5-8982-d1cb453a915a | -20.36935 | -43.98306 | 2025-08-26 04:25:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20d2aa90-0e3d-3d08-adc0-bc3c43b5791b | -18.34821 | -44.96302 | 2025-08-26 04:25:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54a39120-04b5-3ca2-b27f-998cb8a946f6 | -20.02689 | -45.55457 | 2025-08-26 04:25:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09309b95-79c3-3eef-980a-0450147a060d | -18.8927 | -44.69977 | 2025-08-26 04:25:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4be6aeb8-d7ee-31f8-a51e-6cb3ff70cda6 | -23.32915 | -47.84514 | 2025-08-26 04:25:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 26ff0875-670a-3333-9f3d-5b459c25fff7 | -19.92526 | -44.62495 | 2025-08-26 04:25:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 769ff91b-a64c-3e07-bc2d-759a86950898 | -18.34428 | -44.95886 | 2025-08-26 04:25:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13088d2b-6163-3130-aa04-7e218891201a | -17.68787 | -48.63713 | 2025-08-26 04:25:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91e657a0-aacf-313e-ae8b-6d86d836be06 | -22.89988 | -49.05506 | 2025-08-26 04:25:00 | NPP-375D | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11eca41d-c510-33b0-a9bc-c85f70df2290 | -20.8815 | -49.03008 | 2025-08-26 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| bdf46a48-c309-30d8-88eb-27d3579d2a80 | -17.78402 | -44.4856 | 2025-08-26 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16c3d75d-9f91-37ad-83a8-b826659b6982 | -17.68364 | -46.3149 | 2025-08-26 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 09cbf3e4-fdc9-3311-8e57-e74d4c9bf535 | -20.49354 | -44.08563 | 2025-08-26 04:25:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7fa1dd1c-9b48-3403-9b10-20cab410336e | -17.79711 | -44.49527 | 2025-08-26 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f76d530-6f03-343e-8662-6dd9a974e8b6 | -17.56694 | -49.75841 | 2025-08-26 04:25:00 | NPP-375D | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04cd2c26-987a-364a-8081-5c93c01cb18f | -20.20359 | -47.01386 | 2025-08-26 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62a7b85c-24f8-3062-a09f-d23816afca3a | -20.05057 | -44.46807 | 2025-08-26 04:25:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7795d489-7bbb-3b2f-aed4-58a640375b66 | -19.49087 | -46.12322 | 2025-08-26 04:25:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5eb7b8d6-26c9-311a-9089-ecf8db9963da | -22.55332 | -49.76527 | 2025-08-26 04:25:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 226ba7cc-24b3-3994-8834-9cd5eace6cb2 | -19.94424 | -47.03628 | 2025-08-26 04:25:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a49547e5-f9d6-3e74-8d02-57c42eca655c | -19.16553 | -47.66895 | 2025-08-26 04:25:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f67f6d2-4e95-3032-91ce-dba5f7f47e23 | -20.20416 | -47.01012 | 2025-08-26 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ed3468a-0669-3f22-a02c-3771e210f34b | -18.2438 | -51.26778 | 2025-08-26 04:25:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e26e3008-a7ad-3ce4-991d-3619cc74891c | -21.0927 | -40.93642 | 2025-08-26 04:25:00 | NPP-375D | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f331b599-0398-3da2-81c1-7aa49151f445 | -18.717 | -43.81762 | 2025-08-26 04:25:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c140156b-6f67-31ce-a4d0-97c6df95fd43 | -19.92167 | -44.62439 | 2025-08-26 04:25:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0039672b-b591-37e7-8121-250a26dadc63 | -21.38588 | -45.49744 | 2025-08-26 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| b300fd92-faad-3165-907f-6a1905fa5a87 | -20.81266 | -42.78213 | 2025-08-26 04:25:00 | NPP-375D | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 218054f8-b7d8-3756-9a1e-312291c4fd74 | -20.88486 | -49.03072 | 2025-08-26 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b6f30afa-ce9d-3be3-9fa3-5d7e86420951 | -18.8082 | -47.59662 | 2025-08-26 04:25:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5d0b64e-ef15-3785-ab55-bfab47c7727d | -18.84313 | -47.00999 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README51.md)
