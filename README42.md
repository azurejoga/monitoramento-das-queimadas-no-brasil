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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e7e677f-1cb0-3ee7-841b-864a3f8053c1 | -8.6311 | -66.5287 | 2026-09-11 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3ae42c62-a0d6-395b-b9ee-72e40bba6cbe | -8.0934 | -54.8488 | 2026-09-11 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 33a1a258-8703-3ebf-ba84-7f8971adaace | -8.619 | -47.4335 | 2026-09-11 14:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 136bc804-407a-3cac-8fda-9391f61d0201 | -13.249 | -61.5983 | 2026-09-11 14:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| e103878f-831c-3278-96d7-5e78950f6e98 | -6.6888 | -45.4877 | 2026-09-11 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 6df34975-aef2-353e-af74-565e1f17683f | -9.6947 | -43.4217 | 2026-09-11 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 142.3 |
| b54f1c3e-9fbb-354d-8381-38a0359dc3c3 | -8.0936 | -54.8286 | 2026-09-11 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| c64d7e7d-f4c3-35ec-9b74-f19f71e698c2 | -6.4047 | -54.9642 | 2026-09-11 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| ba5030c9-c322-3a74-b459-cc88da074610 | -7.12 | -42.107 | 2026-09-11 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 165.0 |
| 881d175c-df13-3829-be5c-24a6b482048b | -8.7252 | -62.4367 | 2026-09-11 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1bfccfc8-b91d-31c6-81d8-6764d7e4a308 | -13.268 | -61.597 | 2026-09-11 14:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 56f98e1a-a59f-3165-902b-f70b2e341293 | -11.9547 | -49.7512 | 2026-09-11 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 26f2bdd9-11f5-3af2-9142-7af8e1c44692 | -15.038 | -48.4573 | 2026-09-11 14:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| e9a7c534-69a1-3b4f-8897-8be9c7919097 | -10.4295 | -42.7291 | 2026-09-11 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 141.2 |
| 427c3e54-2358-3e77-b89d-731ef4e845eb | -8.6311 | -66.5101 | 2026-09-11 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 88a72e20-f7ba-3d84-80b9-35251cb95f08 | -9.209 | -65.5803 | 2026-09-11 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9c3446d3-34ec-3b25-9f0f-8314f8cc5519 | -8.7439 | -62.3979 | 2026-09-11 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 789169ec-b59a-3d54-80cf-2d28444679a0 | -11.0434 | -49.6851 | 2026-09-11 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 7d7c2f98-f01c-37e2-98d6-db03fa6ae8c7 | -6.2427 | -51.7146 | 2026-09-11 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 69b619c5-e545-3a10-81b1-38d8d7eb3727 | -8.8175 | -62.4898 | 2026-09-11 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 645044f5-aba1-34cf-8767-e79c05b27d42 | -8.7438 | -62.4169 | 2026-09-11 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 85078588-eb72-38a6-b405-4f5ed59ce688 | -6.7648 | -59.4408 | 2026-09-11 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| b07294c7-fda2-3383-ae20-597d55384c3a | -7.9831 | -44.0183 | 2026-09-11 15:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 12f22424-7931-3773-afef-d0e6cbdcb868 | -10.5289 | -51.3386 | 2026-09-11 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 21bfc4e1-5624-3c69-8be6-7c70ac5be411 | -10.5475 | -51.3578 | 2026-09-11 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1098.4 |
| 5ae75496-d806-36dd-9c63-7de78b79d2ca | -6.7649 | -59.4216 | 2026-09-11 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0b12fff6-77b9-300d-873f-f019f9f56fac | -8.7928 | -44.1851 | 2026-09-11 15:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| d55b0bc5-cc67-37d0-b195-8a9d6183385d | -12.1501 | -64.1414 | 2026-09-11 15:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c6602cd4-0032-3048-ab94-3003e8466008 | -12.169 | -64.1404 | 2026-09-11 15:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| b9652457-65fb-3308-b632-10974543e3ea | -13.3552 | -51.8068 | 2026-09-11 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| ca69599a-35b9-318d-9a5d-8f32e318abd9 | -9.043 | -65.4175 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 4f8433b0-ad7d-3d7b-a5da-efe2a7397173 | -13.3245 | -61.6514 | 2026-09-11 15:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 87973f9b-d615-3c64-a1d0-e6dffe3387fd | -6.7075 | -45.4861 | 2026-09-11 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 957f9503-20d6-37b6-9b7c-df4f4e18e454 | -6.2429 | -51.6939 | 2026-09-11 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 1c0d5545-3f99-3493-88e9-20de44538cbf | -6.325 | -55.8451 | 2026-09-11 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 7fc537f1-de01-33e6-9bb0-6d736ddbb3bc | -6.2707 | -52.9483 | 2026-09-11 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 86aea0b0-3eaf-3c90-8ea9-b110c151ae18 | -5.9817 | -57.7282 | 2026-09-11 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1f4a3ee7-e43a-3741-9fc2-cb8049cccf13 | -8.8361 | -62.489 | 2026-09-11 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2dc5bb48-a629-33bd-b7bf-6518ad1c5a54 | -13.4198 | -51.3731 | 2026-09-11 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| db889885-fe39-3496-9864-44ea5159971d | -8.619 | -47.4335 | 2026-09-11 15:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 26ff3d2e-2171-362f-8085-500d7cc1948a | -11.9547 | -49.7512 | 2026-09-11 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 4e73953e-4f3f-33e8-a354-e0336bfc40cc | -8.0934 | -54.8488 | 2026-09-11 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| dc8d7149-390c-3c05-a370-95344886b123 | -9.9045 | -45.8873 | 2026-09-11 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 68e44496-7e0a-3d7c-8cae-b294a8ea9027 | -11.0434 | -49.6851 | 2026-09-11 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 2972cc74-bcb6-3f74-947a-f28ab3b3888d | -6.1993 | -55.2739 | 2026-09-11 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 943653f6-b69f-3b26-b74b-a17a0fb1dbb4 | -9.8075 | -43.5011 | 2026-09-11 15:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1009.0 |
| d15b2eed-3e0a-3ee3-934b-09bddfa56eb5 | -9.0981 | -65.5091 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2101e0f4-558a-351d-afb8-90d2558d9627 | -9.0982 | -65.4904 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| eae22a29-96f5-3c21-a656-276c92d2744e | -10.5286 | -51.3597 | 2026-09-11 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 166.2 |
| 97350d6e-373a-3088-b345-a246975cc58e | -8.0748 | -54.8499 | 2026-09-11 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 98212aa3-2f7e-3d4d-af04-06e9ac77fa42 | -8.6311 | -66.5101 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3ee87419-cb02-3fbc-83d9-9c28ebc230f0 | -8.9874 | -65.4192 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 6af79bf4-bc05-39d0-9bc3-ee199cb512b2 | -11.3513 | -45.7922 | 2026-09-11 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 154285c0-d8fe-3533-be22-44f1d813eb22 | -9.7885 | -43.5036 | 2026-09-11 15:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 323.2 |
| 81a3e949-b4e9-3242-b845-728d0f1e0537 | -10.4295 | -42.7291 | 2026-09-11 15:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 152.8 |
| 3477baea-60d3-31cf-ab27-2ca2dd61cbc8 | -8.6496 | -66.5096 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 42be8294-10ef-3063-8f95-b61eaf46f77c | -22.2856 | -55.828 | 2026-09-11 15:00:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 55adaea7-61e9-3382-bfbb-c68cce5b5d7a | -6.5002 | -47.6128 | 2026-09-11 15:00:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| bae7435d-4180-3909-bf3a-976f7c6687f3 | -6.4045 | -54.9842 | 2026-09-11 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 02e29472-b401-30d3-bef6-6bffa52f23c2 | -9.6857 | -48.0069 | 2026-09-11 15:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 80d9db7b-92be-37df-a527-b322989810c6 | -6.641 | -58.4987 | 2026-09-11 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 30e79475-197d-3919-9b5f-d4a740f42ea1 | -9.006 | -65.4 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| da5f7b9c-373a-32cb-b61e-7297fd7827bf | -13.3053 | -61.6721 | 2026-09-11 15:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2df108b1-477b-3395-b025-d7caad25ac22 | -9.1799 | -68.2194 | 2026-09-11 15:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f6bc43a9-55dc-38a0-80f5-10af6bb715be | -14.6221 | -48.8571 | 2026-09-11 15:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6c052af7-ee76-3eef-84a0-150b739bbf6c | -6.4047 | -54.9642 | 2026-09-11 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 74d7d3b5-3e2f-3e78-ab54-d8aea50a1854 | -11.4021 | -43.9585 | 2026-09-11 15:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 9585db03-8700-33e1-9f96-098977efd4ed | -22.2649 | -55.8315 | 2026-09-11 15:00:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 6ee188b9-12b3-391b-91fc-2c8ef0fa54fa | -6.1994 | -55.254 | 2026-09-11 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| e1475965-3f5f-3649-8f99-25492814ef78 | -6.5004 | -47.5909 | 2026-09-11 15:00:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8594e54b-830f-3b2b-8d37-0f3e08552dec | -8.6311 | -66.5287 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 30f281f9-9934-3846-a8ea-c63e59db2f4c | -15.4553 | -41.3901 | 2026-09-11 15:00:00 | GOES-19 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 72.5 |
| 6fe80dbe-4513-30a2-9201-e87e3bba0bf0 | -7.5553 | -45.1624 | 2026-09-11 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 5f14aeac-c447-33ce-b039-d4767c0e414d | -11.2488 | -54.1378 | 2026-09-11 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 73a76305-5aa9-3c92-961a-e1effbd02975 | -6.6888 | -45.4877 | 2026-09-11 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| fa9beed8-66eb-3b93-a572-62075c4857b2 | -10.5478 | -51.3367 | 2026-09-11 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 286.1 |
| 3ab9d7ba-01b8-3241-8798-cf4afc247361 | -15.038 | -48.4573 | 2026-09-11 15:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e55579e2-010b-31bc-a983-1fe2992063d1 | -8.6495 | -66.5282 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| fe730f6d-52b0-3761-9fe0-917417e16642 | -9.1703 | -65.9361 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 5d5610dc-5296-3768-8954-3b25cf987b20 | -13.3555 | -51.7855 | 2026-09-11 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 04d02164-762e-3d03-a4db-1629f6c0178d | -9.0059 | -65.4186 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e7a8f13c-574a-3831-a280-5685d7424340 | -9.1407 | -64.4024 | 2026-09-11 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 3df3a0cc-f028-3c51-9b5a-7f16f53fb8e2 | -6.7263 | -45.4846 | 2026-09-11 15:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 5fd7c556-a0fd-3015-a030-a8fb4b43811d | -9.9041 | -45.91 | 2026-09-11 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 223.0 |
| 58427a8c-be40-3401-8b03-8c0994bfa528 | -6.2427 | -51.7146 | 2026-09-11 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 216e4646-5888-3ac6-b5bd-233b827ddb8c | -22.2645 | -55.8532 | 2026-09-11 15:00:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 84.5 |
| fb854e25-5031-31a4-9e59-fcb154ea4af4 | -13.3038 | -61.8275 | 2026-09-11 15:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 3baef05e-9549-3482-acec-bfa275e7d0ec | -9.6947 | -43.4217 | 2026-09-11 15:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 164.2 |
| c1c334ba-c8e9-3db0-b2ee-69641e662136 | -9.0058 | -65.4373 | 2026-09-11 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 753816ad-3a5c-35d8-9f9b-5671445814e2 | -5.3462 | -56.0256 | 2026-09-11 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ecedcf58-9ba8-37f9-acab-2a229e78c437 | -9.0981 | -65.5091 | 2026-09-11 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c422d16e-c32c-3398-aeae-6923d03ab5a4 | -11.2488 | -54.1378 | 2026-09-11 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 242.0 |
| 4764b378-be65-3404-a94e-9c5ac77ce35a | -10.5286 | -51.3597 | 2026-09-11 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 72fdcfa3-3dac-3fdb-a41f-3249fada4c6a | -13.2848 | -61.8287 | 2026-09-11 15:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d8fd268a-8d88-30b5-afe3-7c1e72b156d1 | -8.6495 | -66.5282 | 2026-09-11 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 810e1139-02c9-36af-b6f8-a976590337c1 | -9.0058 | -65.4373 | 2026-09-11 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 26718891-1ea9-3d82-9a15-09f663510935 | -8.8892 | -66.7259 | 2026-09-11 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| a525aa8e-df2a-3d2c-9c00-0d1d16ffbbff | -6.7833 | -59.4208 | 2026-09-11 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4ca4a80c-b788-3068-9e63-0da04dff8405 | 0.2851 | -51.439 | 2026-09-11 15:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 3bb75aa5-9a24-325e-a2df-b8e311485dee | -8.6311 | -66.5287 | 2026-09-11 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |


[Clique aqui para ver as próximas entradas](README43.md)
