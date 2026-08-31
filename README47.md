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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bae0f5b2-a980-31db-9f0c-856ac93c2eda | -15.09024 | -48.10885 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 23046e80-672f-3c32-aad8-e79b375e122c | -14.15811 | -52.78961 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d04367fc-2a9d-320d-b7ba-330ba3e2d516 | -14.42963 | -52.52557 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59c57b1b-6992-305d-9f85-568a5f8c3bf7 | -9.21256 | -59.40457 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f0af07d-c9e1-332a-90fa-3a2124e7146c | -9.15615 | -59.54342 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6cfc0a0a-17e4-3bf8-a1ae-e61bda8f3c6a | -10.44639 | -46.75906 | 2026-08-31 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b065bf53-55b8-3e85-abe8-48e045ce8eaa | -7.84536 | -62.3177 | 2026-08-31 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4c2b6f8-f1e9-307e-8a8e-8a03f936e319 | -11.34325 | -45.196 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d179a22f-8f9a-38b9-a329-c29c913cdb7f | -12.39878 | -46.4571 | 2026-08-31 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ce8e93a-0692-3525-a1c0-ff64a1d08987 | -11.16035 | -50.56128 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 8489c7dc-3aff-3e77-86bd-2d8fbdba58d7 | -9.36914 | -60.31537 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdc12d7f-15cf-3b41-882f-783b97213115 | -9.72208 | -65.00597 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fae8038-55fa-3343-9110-684c523a8371 | -13.46937 | -57.04078 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd1db557-0d08-342e-bf14-d9a6022ff065 | -13.481 | -57.05386 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75497415-7750-3c8a-8025-7262b61377c7 | -8.61374 | -54.76916 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8898338d-0ad2-3680-835b-682578d77d34 | -14.58685 | -54.08481 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 454935e1-bb4c-3c6d-b7b6-daf6c9e12a26 | -14.4413 | -52.52293 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 19d17c89-6b92-3dab-a741-5d94428e6f57 | -11.21871 | -45.10555 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd80e035-11c4-3c22-8419-829f97fbee0e | -7.57117 | -61.3779 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 130cc748-3886-31c6-b705-e3da0b15e179 | -9.00153 | -65.43602 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d3898e5-2c10-30a6-aa67-3d76f4005d6e | -10.99788 | -49.69444 | 2026-08-31 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60c8cd79-8ffc-3f08-9835-12b9334ac8bc | -10.06999 | -48.70383 | 2026-08-31 04:59:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bafdab32-1930-3050-8619-0b4882d47c63 | -9.80798 | -46.44871 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b8a2414-e5be-3884-94eb-387f2f2af271 | -9.19843 | -64.4458 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe1d3778-62b9-3b93-bdad-427d986d9d55 | -8.86738 | -66.77563 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0048eba0-20df-3083-acdf-3fd0c354a42b | -11.07691 | -51.51242 | 2026-08-31 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 780e2514-9df5-36fc-90b8-5902219341e1 | -8.79521 | -62.49052 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2392035b-21bb-3ee0-8e5e-e5f56b965a4a | -9.8944 | -60.27622 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dbb8e95-56d3-3b95-986a-3e09983561c3 | -10.74092 | -54.03922 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1ad72b2-c7e9-3e03-a3c7-05709f1681e4 | -9.12263 | -60.38794 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dee34ee3-615f-3101-b06f-1aff3437e84a | -10.79888 | -50.50895 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be7b5045-c315-30c6-9d8f-e11aba5d7c7b | -9.16863 | -59.37369 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4385ef8-e8f8-3714-a36d-eebf669b6078 | -11.92647 | -45.06279 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74354e78-0a83-3ae2-9b9d-8915ed5cbd0a | -14.39402 | -52.54541 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe1a8e60-0855-3081-bd84-dbc5f5fad528 | -14.20047 | -46.57109 | 2026-08-31 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6cc211ea-8c3e-3a95-baa3-862b3249b864 | -14.58286 | -54.08805 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da6ea614-771c-3d86-9ad0-754c69c57114 | -11.18103 | -54.00262 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e666a4d-a0c7-3bb2-b1ef-6cc1df206f4f | -8.79909 | -62.49839 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 75ce7ce4-51b1-372b-8d4e-40380c7da02a | -11.36704 | -45.19128 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa08e712-812d-3a0d-a1b6-0bb44144ccc4 | -10.15436 | -45.73973 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3939a3c2-ef01-39b5-bb3a-d8a60498b895 | -8.59347 | -54.81222 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19e174e6-5d5f-3f50-a4ce-c1373850fa39 | -11.22493 | -45.10231 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b913c3a-962e-30ed-8c9c-ff32e4f33686 | -14.16233 | -52.78588 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0ab7e72-0ead-3f20-a190-97fd5cff52de | -15.66856 | -45.93131 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6391d39-c84a-31a9-b37f-eefa7e3dcc4b | -10.15177 | -45.76052 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3ec0e3f-e08e-3ac0-ac00-ae6e9f434024 | -7.44803 | -60.73659 | 2026-08-31 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7326b0a0-6920-3ac0-abe5-9dacff575de3 | -10.13038 | -45.74012 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6385b15c-3666-33e8-834c-5354e1631739 | -10.84576 | -48.33929 | 2026-08-31 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68121693-f747-3278-874d-fc3de8354749 | -8.25607 | -62.75505 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92143708-28e5-3570-a9eb-a5c0bef3070c | -10.05408 | -48.68833 | 2026-08-31 04:59:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 310ef4cf-c645-3dff-9bc3-7673e0a1702d | -8.8709 | -66.77556 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c50cac2d-fe48-391b-b49f-e3700de75dbb | -10.74364 | -54.02116 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 100d96d0-7351-3518-ae3c-ab08774a29ea | -10.76372 | -54.00209 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0d3fe96-0131-3f48-9203-5f9ad3fd284f | -11.93301 | -45.05817 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a75eb3c5-b853-31e1-9f7b-41e4f86a487b | -11.21302 | -45.1044 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2686738f-e241-380c-b91f-0fec68d332de | -15.19469 | -46.24672 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab88755d-2f5e-3e55-9f04-be5337361801 | -14.4493 | -52.54675 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c4c90d8-cfd3-3285-8458-3ebdb6dcccb9 | -8.70546 | -63.96645 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1015ddc6-42d3-31ae-8ffa-ea4846643e42 | -10.746 | -54.05113 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 383e1d0b-ac9e-3b55-8ebc-adc88d9f205d | -12.93866 | -45.90878 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2898d19e-0444-3538-9349-b30521c7eddf | -15.6681 | -45.93544 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfcb579c-486d-3966-8d59-82538fd02c0e | -9.41006 | -51.69109 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc7c4371-7c92-3e3f-97c0-930a0d751214 | -9.5807 | -47.61314 | 2026-08-31 04:59:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4a22dbca-c53f-3cf8-8c98-d1c5c87c3e75 | -9.00524 | -60.59807 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bfb9463-0fa5-3dda-ac66-9a3190fc4657 | -14.14376 | -52.8071 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a03d92ea-568b-3460-95d5-fab9648d7f58 | -10.75364 | -54.00051 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44dd0793-6128-3db2-94a6-104ef1e1742f | -14.59147 | -54.10123 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bef5f53-6199-3bd9-9b1f-31c735fb6e83 | -9.1609 | -59.37243 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04202eda-bbc9-3da7-aa41-f583ddbaa461 | -14.30545 | -52.90675 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efeb99a6-6cd4-39d4-b8b4-984b976a48ad | -10.57605 | -50.36445 | 2026-08-31 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4571d0bd-e6be-384b-854f-08930173919a | -11.92592 | -45.06732 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa14ce4d-dcec-39ca-91cf-e5937b4dc663 | -7.69489 | -63.32981 | 2026-08-31 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f428a983-dcbd-3400-8e81-547bc584a017 | -11.34741 | -45.20947 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c3b13a5-6058-3665-b635-ccd7213951ae | -9.94216 | -60.50967 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13474a0a-cacd-3278-b63d-97d51c2a6f14 | -15.00154 | -48.16726 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6bd2dfef-e5be-304a-a4a1-1d8046b7354d | -9.16395 | -59.3779 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 130671d8-6c60-327a-b09b-64c6dc4e4e12 | -14.6041 | -54.11105 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9cda214-04d6-3883-85b1-d388fc507fcb | -14.23119 | -52.84905 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7805fe52-94aa-3f3a-8aa1-465887ccc2ee | -14.20174 | -46.56041 | 2026-08-31 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4430f77c-0bc5-3fd8-8b72-68443796a419 | -9.05943 | -65.41606 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 306bbe2f-3fcd-3d7b-b247-8184fbb3769f | -11.37573 | -45.1679 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20c36a56-205e-325a-aa7a-b29edaf3454f | -9.17647 | -59.63763 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a425121-0e89-3299-b324-395b362e7a2d | -11.35263 | -45.21425 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5a3335c-88b3-32bc-b9e1-4267c9c1be08 | -8.6138 | -54.79051 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e56e5661-067f-316c-ac2b-dcad90b68ff6 | -9.93616 | -60.51998 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 976ca643-ae8e-30a5-8090-279f173fe2b6 | -14.18169 | -52.83292 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 745e685c-2533-306e-b348-bc9b08795bd6 | -7.44089 | -61.43106 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b01e57a8-a261-382f-b016-c06fcaa5e896 | -8.86644 | -66.78066 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06ce2909-e501-389c-9f6f-ec3d4456f586 | -13.38458 | -51.78491 | 2026-08-31 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f00daf4-89ed-33fa-bdda-021ee39f151f | -12.13415 | -47.2315 | 2026-08-31 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55a20fd5-3153-3d01-ac68-c1a47e8888de | -13.46995 | -57.03717 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2df4dd9-29c4-32e6-a6b8-6cdec8031dd5 | -14.59835 | -54.10233 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 107ef532-a097-384b-9407-6b057c7c13e4 | -14.39706 | -52.55046 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb493695-3a03-39fd-9664-b25035eb318c | -15.02622 | -48.16998 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 24ac06fc-d843-3078-b0ad-f51d6086edec | -14.39276 | -52.55427 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c02e459-1fd9-3fd7-956b-4a640eb37c3a | -11.22442 | -45.10655 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 655de169-b26c-310e-a729-f7ba47d3c6b8 | -15.66369 | -45.92264 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 857ed165-6fe2-3a73-b592-fac04fd9cf2c | -10.73983 | -54.04646 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d557e07e-90bf-39ce-8a73-05a2bb7073dc | -9.79334 | -60.18196 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d181f4a-5b35-3f88-9392-19c081b08595 | -14.30004 | -52.89283 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README48.md)
