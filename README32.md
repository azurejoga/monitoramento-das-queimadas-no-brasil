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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41ba5202-343d-3ef8-93bd-fb3ae49117d0 | -5.04608 | -46.88325 | 2025-10-23 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23e99285-db59-3758-9bf3-e108552a5fd7 | -6.45519 | -52.82597 | 2025-10-23 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3db0390-2190-3cac-93a4-162658261339 | -3.02149 | -49.45054 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c47df9bd-6e06-3293-a64e-83ed165b0570 | -7.07783 | -46.19385 | 2025-10-23 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56b09a9a-994e-3ef0-ac27-a91eadc7e9fa | -3.67688 | -47.63315 | 2025-10-23 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 574d2950-7a84-3a51-a556-4cad30f17be6 | -0.84336 | -48.73522 | 2025-10-23 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a98cc200-9f77-3b29-84f5-60b51397c6fa | -5.63358 | -50.03149 | 2025-10-23 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 078a2cb4-6a5b-34fe-bfdf-1d7247fdef4e | -7.32464 | -45.28734 | 2025-10-23 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 550948d4-75aa-3c35-a3a5-1b2df0e51d1a | -3.81599 | -51.70005 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af9597ff-ccad-323e-8b13-9a369d18b0ef | -2.56205 | -50.63858 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df37a101-0762-3b38-9b27-33f3f29e3a57 | -6.78848 | -45.44763 | 2025-10-23 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de7cd179-c4d9-3e9e-85b8-57cbbcc5fc01 | -3.47314 | -50.07242 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a31759d7-fd01-3bfb-9656-012bdab13492 | -7.06424 | -44.09668 | 2025-10-23 04:55:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d66cfea2-85b2-30cc-b204-4e734c23844c | -2.83439 | -48.55952 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8406b445-0e4f-3845-8c4c-992b28f790ba | -2.73655 | -48.28809 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dc4256d-0089-3fa4-8097-040e2e2d8d86 | -6.73088 | -44.1519 | 2025-10-23 04:55:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d110d19d-2d98-3db7-8212-113925e2a7c7 | -3.48276 | -50.08263 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| abaf61d6-3747-3369-9495-6f2005c94477 | -3.22983 | -49.35001 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b856b8c-ba37-3691-b0de-91ab9abf34f0 | -6.96217 | -44.01871 | 2025-10-23 04:55:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ca625b9-a17b-3ac7-aae1-8509292081c1 | -2.444 | -49.37423 | 2025-10-23 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 872d0fb1-89c6-30b7-b5e1-48a8e233a37a | -7.62734 | -42.19286 | 2025-10-23 04:55:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66ac8c36-90d9-3966-970c-21aa1a748ce3 | -5.37079 | -46.87219 | 2025-10-23 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c9e816d-e296-396e-a4ab-95f9a9cf16b9 | -3.46887 | -50.07608 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d253a41-6096-3ed1-82b4-faf5ac15b14e | -13.79242 | -52.77329 | 2025-10-23 04:57:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ec12656-d4fa-3dfc-9178-679b410f9bae | -12.37877 | -63.87021 | 2025-10-23 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f76cbde6-8513-3b75-8a43-ad5f4bd6ae4f | -9.92953 | -47.46418 | 2025-10-23 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a556c26-e220-3256-8842-6c5a311ed7fa | -11.0521 | -45.39585 | 2025-10-23 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 41700bc0-781d-3c87-a6c6-54fbdda9bbb6 | -13.62352 | -49.45091 | 2025-10-23 04:57:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2b1f258-5145-3bbc-8c3f-36d789ae661d | -9.67726 | -47.63747 | 2025-10-23 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 771c15f1-7f34-3243-8c89-3f7d651e5010 | -10.48737 | -51.86995 | 2025-10-23 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebbb1222-061e-3b6e-925c-fc5ae86ba7bd | -12.01252 | -46.74913 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84ac6809-40d2-3e66-ac7b-3586353b0bdd | -9.55183 | -66.6516 | 2025-10-23 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 676247d1-ffc5-3b0e-8e33-8ea765f26053 | -9.92481 | -47.46346 | 2025-10-23 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b969ea2-ab62-3ef4-b20a-e98a50c0faff | -11.34421 | -51.44576 | 2025-10-23 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d263381b-2b3d-31f5-81af-041416dbb655 | -11.35525 | -49.79468 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| fc6b78ae-28a4-30f8-9194-cbae693a3b57 | -10.39105 | -47.10711 | 2025-10-23 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12ba7c60-84bf-3ad1-b53d-6bdd5ef07aa0 | -12.13142 | -62.96543 | 2025-10-23 04:57:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dfc1f63d-d8c2-3212-9b57-71431bb60cfc | -14.2121 | -44.52269 | 2025-10-23 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84b41572-4b1d-3e03-8ff2-3e311f9d7bd2 | -11.9936 | -46.77504 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 69f835e6-eb12-3aa1-8c3b-850902f3b6ca | -14.10121 | -44.24056 | 2025-10-23 04:57:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68871f32-62b5-3372-a4d1-477394455c19 | -11.35935 | -49.7953 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 51d1a941-6d82-31f5-ab14-d83186c568eb | -10.53028 | -50.23134 | 2025-10-23 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0ba9e08-6094-36fb-887c-d3a1bff037d1 | -13.04702 | -47.21875 | 2025-10-23 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1223bed-d430-3afa-80bc-557319853271 | -12.38812 | -57.52224 | 2025-10-23 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea58d62b-28dd-32dd-b008-2c7d96f5d181 | -11.35114 | -49.79408 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 048ac46a-c390-3448-b667-c9ca3a21f65e | -8.35096 | -46.18221 | 2025-10-23 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 377b9bd6-f0c7-3973-aea2-76e7d5a0130c | -8.35058 | -46.18489 | 2025-10-23 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42ac1d63-69be-358e-a651-6d866059b0f9 | -12.04308 | -55.2499 | 2025-10-23 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccb96bfe-9f04-33cf-a79f-20660ad44b29 | -8.21304 | -46.98587 | 2025-10-23 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf6df945-2a20-3451-a8a3-3c18e8a41b47 | -12.80446 | -51.33114 | 2025-10-23 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| add889a2-cb19-36ef-adf0-1c2eb48337f8 | -12.52115 | -48.58104 | 2025-10-23 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1252d8f-f0be-393a-8046-9cdf90a0892a | -13.04024 | -47.23253 | 2025-10-23 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72626274-709b-3a5a-8bb9-f203b587571f | -10.9153 | -50.11614 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04eb37ca-c537-3ea7-9583-f5c3c479f41a | -9.97548 | -47.08249 | 2025-10-23 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67883a68-38c5-3909-b8bd-ad05d2a9c82d | -9.86299 | -47.71323 | 2025-10-23 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf6ec7ea-26a9-3f89-b6bd-75e944c026f5 | -14.20599 | -44.52225 | 2025-10-23 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f01db593-3384-37b1-95e1-1eccf95e23dd | -11.99909 | -46.77266 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d7434915-3a92-3b9d-a8db-94fa7ab4f9b4 | -10.02768 | -47.06193 | 2025-10-23 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a0ae801-4573-3efc-a67b-45f5fa528b67 | -8.61952 | -44.8103 | 2025-10-23 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6fef5fd-b6cc-3a86-93f0-ee829c7a6e16 | -11.79307 | -47.06768 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 991559b9-5905-32e9-80cc-308f6e4e1261 | -13.36763 | -46.63953 | 2025-10-23 04:57:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 955e72c7-d142-3718-b362-54fcb29efafd | -10.9158 | -50.11263 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 369ad6f0-fc45-38c8-915f-79a56b36b1e3 | -12.67466 | -48.62538 | 2025-10-23 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6a0ba93-2fed-3720-a87b-878a207cef0b | -11.07229 | -51.56831 | 2025-10-23 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 982066ab-2b44-3466-ae63-b5bf5105a357 | -10.38905 | -47.10022 | 2025-10-23 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b63a435-67f8-3d4a-b30a-36fad11c7b07 | -13.04167 | -47.22084 | 2025-10-23 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a379c86-9086-3def-b312-e153f309e24a | -10.53496 | -50.22679 | 2025-10-23 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff91ab7e-df50-363f-bf16-324569871ec8 | -9.68189 | -47.63817 | 2025-10-23 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86156166-6b95-3730-8cce-79c5dbdcdb85 | -12.9022 | -48.48994 | 2025-10-23 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fe28bfc-0259-3e1c-8e7d-d22bfd28ed54 | -12.37264 | -63.8751 | 2025-10-23 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d47f8380-d388-39d1-a2e9-28f61772c559 | -12.00419 | -46.77331 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dcd05ced-00b2-3615-bdcf-ff67307d65cc | -12.37377 | -63.86922 | 2025-10-23 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e9c5317-0f4d-3818-8905-b9426a961110 | -11.24888 | -49.87447 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a0ae488-3271-3367-a572-9d118ea9b18d | -10.21159 | -46.64578 | 2025-10-23 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6d5c0e6-1d3c-3fbc-a8e3-8997cf137fd8 | -13.89121 | -48.37442 | 2025-10-23 04:57:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d732fa9e-c4f1-3a09-975d-ad1dc790a8be | -10.62311 | -48.07236 | 2025-10-23 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c28276d9-eb05-3ca5-9a8b-5f669e8c2e11 | -12.24076 | -46.78249 | 2025-10-23 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1085bba4-0628-3026-83bb-f04eeff6bd70 | -11.35884 | -49.79903 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 38cab6b2-58ce-394a-8f0d-69753b3c7313 | -10.38686 | -47.10116 | 2025-10-23 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4bfdf5bc-e0a5-334b-9304-88517bb78411 | -13.05201 | -47.21967 | 2025-10-23 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf52889f-74dd-39d3-aeac-f5526e099de2 | -12.69044 | -48.64585 | 2025-10-23 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bae0bf96-1458-3cf7-aa33-b48d4c666c2f | -13.12639 | -48.24502 | 2025-10-23 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9db81c6b-282e-3b5a-bbe0-2a757e72b746 | -10.9073 | -50.11498 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27d5aa6a-e0a8-36cf-b028-3ebd92a0f8e7 | -12.24578 | -49.58872 | 2025-10-23 04:57:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bb7ec8e-09a8-37da-9089-c5acc596de4a | -12.54851 | -52.22089 | 2025-10-23 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1830fc83-7afc-3325-b386-2280bcb3b477 | -10.85234 | -52.35936 | 2025-10-23 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f1864ef-ab45-30db-b34c-1f34032474e6 | -12.13045 | -62.97062 | 2025-10-23 04:57:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf3b69d8-9101-36c2-8ed7-ab818920ab5e | -12.78376 | -48.57514 | 2025-10-23 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17055acc-4a03-309a-b549-ccc47e8bf32b | -12.25422 | -49.58994 | 2025-10-23 04:57:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73210567-2f4f-3877-8137-465f2a1de3d3 | -8.4484 | -48.10825 | 2025-10-23 04:57:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4791292f-4435-30cb-a9e4-e417aee613e8 | -11.35988 | -49.79153 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a460fb8f-2b71-30f7-89ad-ed7949c4b9c6 | -11.24992 | -49.8671 | 2025-10-23 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06989944-c4c0-3ee9-a992-a2b04c6dba7d | -12.01885 | -46.74038 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66bec1b6-8d3e-3181-8e56-c0d047d0d667 | -11.05764 | -45.39637 | 2025-10-23 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 500339e8-1f50-31d4-9623-6a7164bcd62a | -11.07166 | -51.5727 | 2025-10-23 04:57:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0eb4d039-0e23-34f4-87d3-99078dc2b8ad | -13.37247 | -46.64347 | 2025-10-23 04:57:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79d0786b-c90c-36cb-ad2e-ac93b465415d | -12.24038 | -46.78554 | 2025-10-23 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0976c672-3f96-3234-8a9c-6a6a826273d5 | -10.39589 | -47.10797 | 2025-10-23 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b07dd49-fbf9-3831-a74e-eba5840c18f2 | -12.38468 | -57.52165 | 2025-10-23 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71c9ae60-e499-395e-a917-b6577c70dac5 | -11.98811 | -46.77742 | 2025-10-23 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README33.md)
