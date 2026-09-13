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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f112de64-341d-33d4-8601-fcd8535dc8e8 | -3.8279 | -58.899 | 2026-09-13 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 7ad816d2-83dc-3604-9f3c-433e8d141890 | -3.8461 | -58.9178 | 2026-09-13 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 4f75bbc8-f83e-3004-a2c8-8b1ce6a43be0 | -6.7515 | -55.6455 | 2026-09-13 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ecd74578-2aa5-38ad-bb72-1914981378eb | -13.3199 | -51.62 | 2026-09-13 16:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |
| a9876b49-90b2-370a-bb16-386d26099587 | -6.863 | -55.5801 | 2026-09-13 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 255.3 |
| 164f86e5-1ee5-370a-b5a8-5ba9543a77ca | -12.6826 | -54.6763 | 2026-09-13 16:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 8f11449b-5b23-3be4-a593-0588da314970 | -2.6785 | -57.5115 | 2026-09-13 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 4d5d3c2c-d40c-3a23-8fe9-6a6c71e03a9b | -8.6005 | -44.4378 | 2026-09-13 16:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 12022b73-e9cd-3c00-9771-754fc4759f3d | -1.2268 | -49.1899 | 2026-09-13 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 8ef06cf1-796e-30f1-8328-366fcaaf7dd5 | -2.7149 | -57.608 | 2026-09-13 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 6ea0b0b3-0969-3f3a-9aa2-99d172c7feb1 | -3.4058 | -59.2538 | 2026-09-13 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 4449dbb6-055f-3def-8cb2-498798b4b6e2 | -3.8278 | -58.9182 | 2026-09-13 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 5d0c7189-8e58-3ac7-b3af-250f6609483a | -2.7149 | -57.5886 | 2026-09-13 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| f7c33bbf-05b7-3dbf-8bbe-38dbba9b2316 | -3.8462 | -58.8985 | 2026-09-13 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0c7d1149-0b50-3396-84f3-656a9dded7cc | -10.8028 | -50.6326 | 2026-09-13 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 2817f084-b82c-3496-a6c3-73007c8bf987 | -3.4242 | -59.2151 | 2026-09-13 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 3273deb2-530e-3403-b545-f0539c576d39 | -10.69 | -54.2 | 2026-09-13 16:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a657b347-8155-30a7-a137-015be368833b | -2.88 | -50.45 | 2026-09-13 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b0929b5-ef4a-3659-bb6d-3acd9a13b5b7 | -2.7 | -57.58 | 2026-09-13 16:15:00 | MSG-03 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a2c2db6-990d-32f3-b649-34cd65fa0627 | -10.69 | -54.13 | 2026-09-13 16:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9268f1c4-cb6b-36b6-91e0-f9f7280046f5 | -2.7 | -57.51 | 2026-09-13 16:15:00 | MSG-03 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90e320a4-4017-3a41-9c37-24e044e73e98 | -15.51 | -43.87 | 2026-09-13 16:15:00 | MSG-03 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2a2c2826-4a31-3195-a6c6-d5f81fbbb8ad | -10.73 | -54.53 | 2026-09-13 16:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59f5a474-70ad-3cce-b99b-a802234cdd8e | -10.7 | -54.52 | 2026-09-13 16:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8aba3e8-ebb8-388d-ae05-640f3f24a599 | -15.51 | -43.82 | 2026-09-13 16:15:00 | MSG-03 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| f97e65c6-4b99-3665-9c3d-a0fa9d0c2784 | -10.73 | -54.46 | 2026-09-13 16:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2da98fa-0e37-359f-b797-662ab5f49105 | -2.91 | -50.4 | 2026-09-13 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2415d32-2c7f-325e-a9cc-a57658f08c36 | -2.91 | -50.35 | 2026-09-13 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d999867-d541-3744-913a-3d52fc71d84c | -2.94 | -50.4 | 2026-09-13 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5142b37b-6d33-31db-abe2-0608f14e1e66 | -2.88 | -50.4 | 2026-09-13 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2347f91e-82cc-3f5c-ab52-1ab8cef6b0f7 | -9.39 | -50.14 | 2026-09-13 16:15:00 | MSG-03 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0510fa5d-be28-3a6b-955a-14149582aaa0 | -2.91 | -50.45 | 2026-09-13 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f021e1c9-ffd7-3567-a8fb-645b7c54b4cb | -12.6826 | -54.6763 | 2026-09-13 16:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f60280da-45f0-39c7-bb17-ff3eaa572afe | -2.6785 | -57.5115 | 2026-09-13 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| e8399b32-3b54-3478-874f-3ee54bfaafa4 | -9.3948 | -50.1334 | 2026-09-13 16:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 280.3 |
| 6c5d45fa-8f84-3a47-bb80-9ad6f4375fe6 | -3.6997 | -58.8827 | 2026-09-13 16:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a39d25ce-f63a-3c37-a4f5-caa46d793d65 | -3.4241 | -59.2343 | 2026-09-13 16:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9ea183e8-0291-3219-af21-e1d0ccacf3f6 | -9.3763 | -50.1139 | 2026-09-13 16:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 02f6a89d-8cf4-3107-afd0-fe5a157463bd | -5.3645 | -56.0447 | 2026-09-13 16:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8136dc9e-60cb-34eb-9c99-eab006fb4e52 | -3.8461 | -58.9178 | 2026-09-13 16:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 5c2a6b46-acb8-3d35-a205-46a056ed6d3e | -10.7532 | -46.2573 | 2026-09-13 16:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 06aa5c3a-3687-36cf-852d-60784fa16ca5 | -3.6998 | -58.8634 | 2026-09-13 16:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 07db3d1d-0d84-3160-82ce-2b1157427a0e | -10.8223 | -50.5879 | 2026-09-13 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 73917fb1-8640-32a4-98e8-4456484a2786 | -7.12 | -42.107 | 2026-09-13 16:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 156.8 |
| 21787c24-45e1-3701-9cb6-6f56e1224d50 | -2.7149 | -57.608 | 2026-09-13 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 195.6 |
| c53047f8-bfba-3179-97f3-b1dc0711a72f | -2.6602 | -57.5119 | 2026-09-13 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| fd04662e-57a6-347f-b52b-7e02e464f858 | -9.3951 | -50.1121 | 2026-09-13 16:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 4c766a1b-fc9f-33a4-83ee-fd290af81561 | -3.8278 | -58.9182 | 2026-09-13 16:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 0a6544e7-6d5c-3464-8eea-6da535665be1 | -9.6755 | -46.0047 | 2026-09-13 16:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.0 |
| fe7d9e17-9db8-3147-9c3d-b781f68a36f1 | -1.3007 | -49.1464 | 2026-09-13 16:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 88044fe6-8306-3d02-b810-f9c47a46fea6 | -3.3504 | -59.4274 | 2026-09-13 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| fe7af8e3-ede8-3045-80c5-305fef18517c | -3.4058 | -59.2347 | 2026-09-13 16:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 2b13c873-0d4b-357b-8c3f-e74746c4b156 | -9.3765 | -50.0925 | 2026-09-13 16:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 0b7fd60a-c2d2-3ee2-8f89-c2d75323afaa | -6.7515 | -55.6455 | 2026-09-13 16:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e251d5d4-b701-310a-8432-d56a5734417d | -6.8445 | -55.581 | 2026-09-13 16:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| caf41cd2-b2ed-3854-ad75-cfc1648923a9 | -6.7515 | -55.6455 | 2026-09-13 16:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 2d1a8d74-d49c-3b54-bbdb-8a4187e66e7f | -7.12 | -42.107 | 2026-09-13 16:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 128.6 |
| f50bdc72-0681-3db2-b63b-7792d7844096 | -13.3387 | -51.6389 | 2026-09-13 16:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 310.4 |
| d2d241ab-373f-3c19-ad93-bf87b131a193 | -1.3007 | -49.1464 | 2026-09-13 16:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 88778487-51b6-34a0-80ee-37c213cfbe58 | -2.6785 | -57.5115 | 2026-09-13 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 97030900-9797-3e64-91e5-a4e0582a62e1 | -1.2268 | -49.1899 | 2026-09-13 16:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| b0732556-22fb-323d-8bb4-b45a86bbb752 | -12.6636 | -54.6782 | 2026-09-13 16:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 94772fda-222d-3ddf-9537-1c3811437f0d | -9.3763 | -50.1139 | 2026-09-13 16:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| a218ea8a-7a88-3011-a25d-b83e4c867a87 | -2.6602 | -57.5119 | 2026-09-13 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 063970d0-5518-362f-a426-805c330e752a | -11.4905 | -50.2581 | 2026-09-13 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 2f998a85-7b05-35d3-8937-e2f20677f85b | -3.3687 | -59.427 | 2026-09-13 16:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 941adff7-36c6-3f35-9e26-bad81dc1d141 | -3.6076 | -59.0769 | 2026-09-13 16:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 173.4 |
| 00027a73-86c5-356e-9033-32340a24bb3c | -6.8445 | -55.581 | 2026-09-13 16:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 3f39333a-bb70-371f-89e5-e2067c466a28 | -3.4058 | -59.2347 | 2026-09-13 16:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| d9dc0a7e-3fed-38dc-b16d-962fb1b0b032 | -3.3504 | -59.4274 | 2026-09-13 16:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ece2bce5-072b-3789-a7f3-89d6a1530c2b | -12.6824 | -54.6968 | 2026-09-13 16:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| ea3eec74-1fbb-3fb7-a3f3-74399f204ecc | -3.3504 | -59.4274 | 2026-09-13 16:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 3b93a772-74a6-3b12-9fad-bdb43555eebe | -9.3765 | -50.0925 | 2026-09-13 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 254.7 |
| e27fbd79-4e9d-3207-aac9-57edf7d22fa6 | -13.3387 | -51.6389 | 2026-09-13 16:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 9dd84d2a-31f8-3e79-84a7-b97ac461a122 | -13.3758 | -51.7193 | 2026-09-13 16:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 46ecb3d6-6df0-3ae8-b1e1-41175ecc537a | -3.3687 | -59.427 | 2026-09-13 16:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 43a1c248-2b02-33cf-95d3-7f2ea01d1808 | -2.6602 | -57.5119 | 2026-09-13 16:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| b2d5d196-7c1a-3fb1-b97f-72ff20cbcce2 | -9.3951 | -50.1121 | 2026-09-13 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| fd4bce91-8f80-3f0b-a128-90157c388f6a | -3.4058 | -59.2347 | 2026-09-13 16:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| e012343c-2396-37ba-b88a-36a848827a5e | -11.2488 | -54.1378 | 2026-09-13 16:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 01f936e0-f384-3c61-9d27-8cf557203c13 | -11.4905 | -50.2581 | 2026-09-13 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 5ed41579-eba3-364b-a9cb-a9483ef3dd10 | -1.3007 | -49.1464 | 2026-09-13 16:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |


