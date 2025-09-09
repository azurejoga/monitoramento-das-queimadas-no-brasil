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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f014b4b-5787-3ca0-9ec3-83dba72bb6ff | -11.95571 | -50.97692 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fb6ba77d-dd5a-3555-b7a5-24810ac1e364 | -11.98441 | -51.01838 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98ce8caa-8a17-3c06-9b5f-02cf02525680 | -9.20486 | -67.56022 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2909aa3-e283-38b2-82ea-3acfa4e6fdb4 | -9.05798 | -60.44263 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d12f52dd-c9a3-3465-9a66-efdc9aed147f | -10.08692 | -59.1807 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab20228f-b3d0-3183-9e43-7cb07df7f21e | -9.69474 | -57.80532 | 2025-09-09 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d57c87b-b189-3a9e-9951-35e928b9547e | -10.15037 | -61.14291 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15e96bbd-641b-3616-b128-0b9b525cf599 | -9.22043 | -60.81608 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf3e3e27-c8da-3e28-b7e2-68da70aab6fb | -9.17846 | -60.82343 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68492f4f-f601-3177-b914-142400bd97e7 | -10.41583 | -60.74625 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f63f9ef-4478-329f-93b0-c1589a688b8b | -11.21706 | -55.00501 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0f51ea8-f2db-3b4f-8c89-91fd933b3a97 | -9.05028 | -58.95816 | 2025-09-09 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21c06528-e27c-3080-85d5-db6e7c966623 | -9.16953 | -59.3727 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2475008a-754c-36a4-b58e-e7702ff5e7a4 | -11.94438 | -50.9711 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 83f5b9c3-20fc-35f3-b22e-cc17563eee96 | -9.81438 | -65.21723 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b304f515-2b47-3584-a422-98fd179a05d7 | -9.18601 | -59.37906 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2564b643-15b5-338e-959d-bf89b2ff5476 | -9.39213 | -65.94538 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82b82b6b-d294-31ed-aaec-3cffb2c5cdf4 | -9.18034 | -59.37056 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aa59b0c-7114-3b61-b07e-ff56abaa6e75 | -10.41481 | -60.79676 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cccdd89b-9e3d-3e0a-b2d3-d4d5276db87a | -12.02492 | -51.08065 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4341e700-2fc5-3001-9d60-08814fd2da5e | -9.98789 | -64.99139 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 938780dd-59ef-3321-a123-72a9dd9123ed | -10.70048 | -55.38395 | 2025-09-09 05:25:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed9b58aa-877b-3495-bc2b-c3db3277a310 | -8.63181 | -69.79686 | 2025-09-09 05:25:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cb408c6-fb16-3c06-a69b-f6fac3998cdc | -9.44875 | -61.82207 | 2025-09-09 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ef74f4c-9150-3336-b108-117a803932a8 | -12.01955 | -51.07558 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 27652f88-4a76-3892-8e18-6ab7003faf86 | -10.4226 | -60.81242 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0176c8a6-9b67-34a1-9544-e18ca42a4a98 | -12.82486 | -47.9829 | 2025-09-09 05:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffbb9f3b-b43d-3aa9-a017-82df12f2ee1c | -9.69675 | -64.19374 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad3e8217-3e2e-3ac0-8d0f-934138276a23 | -8.98177 | -67.12447 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4514fcc-c034-3a80-bc81-22c87cf85fbe | -9.69106 | -57.80476 | 2025-09-09 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07c1a525-0102-352e-b159-0cee91d23f56 | -9.98494 | -64.98634 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf86f857-4b67-3f41-90fe-3395ad8b59c5 | -11.2282 | -59.12865 | 2025-09-09 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67cd73c7-8335-35d4-9e4c-bedace582403 | -9.44647 | -60.52136 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e014345-dea6-3346-b972-46765287383c | -9.07583 | -60.50304 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1f12728-dfbd-38d0-8d6c-b65e4d119e7a | -10.88963 | -55.6981 | 2025-09-09 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd55bdab-98bc-3e68-b261-d3d473029c90 | -9.57286 | -57.74381 | 2025-09-09 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 882b6df7-3d84-33bd-b9dd-4b45666c7fa0 | -11.22411 | -59.13208 | 2025-09-09 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c4a0b86-59a1-3ea7-9952-8e3539e5518c | -12.01365 | -51.07483 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5786c12-b0bb-3ff0-87d7-821a6462124d | -11.96111 | -50.982 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e256f1ef-4ff9-3237-8464-47bceb34571f | -11.94801 | -50.96949 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e2e0b9d-bf00-3556-83ef-ad20b1db2e0c | -8.72718 | -69.11618 | 2025-09-09 05:25:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c5ece6c-6b21-3fc1-b972-4bf95966ebc6 | -9.47302 | -65.51427 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72a8f4fd-2691-3d10-ad08-b20e7382c3bd | -9.22374 | -60.8166 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd511038-d7dd-3e4c-b878-a6ec0bcd30fc | -12.02866 | -51.08656 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4b78ee4-7b3b-37c3-89b0-9b410d65a386 | -9.62992 | -63.10071 | 2025-09-09 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af55350c-e3b2-3d08-90fb-8b1149de2729 | -11.3078 | -50.41945 | 2025-09-09 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b1aae87-f2a3-3d1b-b4c1-1ae14c01a6ba | -10.5788 | -52.03046 | 2025-09-09 05:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f188fbcc-304f-3526-a56d-a962d70aacf0 | -18.82752 | -49.67775 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| da4b4260-3faf-3df4-b7cc-31b6fe9bee74 | -9.29493 | -60.86008 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d25026ed-4001-39bb-8168-7140840cda5e | -10.01069 | -64.92297 | 2025-09-09 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 28c089fb-1c5d-3c8e-98b7-de076400bf5e | -18.82696 | -49.6841 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| bfe282b2-f73a-3595-91b8-143d61f91395 | -11.21574 | -54.99778 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d2e8bf57-5444-3398-b663-5d192b53f556 | -9.93534 | -60.10568 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fc24a56-e369-38ef-b7d4-b83c87a9862e | -9.4522 | -60.5261 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33a41e28-4989-365d-96be-171302ad1da6 | -9.44592 | -60.52488 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68377550-c661-3f21-917d-be3315c94d48 | -9.05688 | -60.44967 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9949e46a-c965-3581-8a5b-40c155c42099 | -17.67764 | -52.25247 | 2025-09-09 05:25:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c250615d-2ef1-30e0-ab3b-6a7729c12a34 | -10.41638 | -60.74272 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b28965e-86f9-3ecc-b965-5e1d9816cfd1 | -9.4516 | -60.50796 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9ac47c4-661c-37d3-ac10-4eac664345be | -9.12787 | -65.95869 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f6186c8-4342-30ab-8c75-0eb104c1685e | -9.19432 | -59.37258 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 995b8121-d5ea-3fbd-a16d-2e31741b9e33 | -9.49768 | -60.54049 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48529eb1-4310-363a-a603-5ce11f8f0f72 | -10.42581 | -60.74785 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9357f82-a4d0-37a6-a25c-c1a4d141e0aa | -8.94941 | -64.3868 | 2025-09-09 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1efb14e1-6c12-3207-8db2-e50643026baf | -9.94522 | -60.14415 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d4a205d3-ae83-39b3-99b7-dabbb4fffb01 | -12.01313 | -51.07915 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47a6ba9b-4119-3aea-9852-e1e4935a3cab | -9.3466 | -65.45677 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bfe652e-d9ab-34df-a49d-b3723d095b6f | -8.76811 | -68.99917 | 2025-09-09 05:25:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c79f3f88-9165-3cfc-a462-6a927a845e33 | -8.44726 | -70.1338 | 2025-09-09 05:25:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3708004a-39dd-3bea-8073-ff6a201697f6 | -9.13593 | -60.52985 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6fc7909-023e-3109-ace9-cb17b8543c0a | -9.93254 | -60.10155 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4e7fa9a-2037-3aab-b45a-49e61d1738a4 | -16.32347 | -52.92981 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d844f4c-6a43-30dc-b175-4a2577bd1bd3 | -12.0303 | -51.08569 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d582299-1b6b-3702-a478-e381829346ce | -9.83616 | -64.22367 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c529284-749b-31e8-a990-3b0b08677ed6 | -10.86825 | -55.72714 | 2025-09-09 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c336d89-6abb-3835-aab0-bfbd14bf6a65 | -16.34425 | -52.94455 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d02e0d29-54a9-3131-9a85-3f00394b695a | -11.93614 | -50.96798 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8535fa89-cd51-3c7a-826f-5c8e98aa7e32 | -9.47261 | -60.48238 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07a566ce-050f-31e1-90ab-6d5dd536a031 | -9.69319 | -64.19315 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 681d6af1-53a0-3f86-9c87-a40038fc9ff8 | -9.44703 | -60.51783 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7adf1ef-f73d-3f6c-82bf-42b5b78310b0 | -10.41625 | -59.5979 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 043a0def-e9fb-3d02-9343-5cfa491e8c05 | -9.75077 | -65.01787 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0050b6af-786e-390f-a62c-c678c7807420 | -9.08084 | -65.37874 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bbb6dea6-f0b6-3271-bd28-ada97af68aaf | -9.67505 | -65.53503 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e2a33749-cf81-38bd-877d-23ad9d0b57b4 | -18.82704 | -49.67717 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 81991351-94d5-380f-8e36-63d8dbe743ba | -11.95518 | -50.98129 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a02d0497-5cdf-3608-afb1-70a3aa17e1f6 | -9.47818 | -60.49049 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34e3ef36-8ffc-3d3a-af97-c7b17886f1f6 | -9.08574 | -65.41154 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 91f5c33d-5383-3c4d-8018-f94c5adfe42f | -9.94351 | -60.13284 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c49f4d60-5fbc-340c-b491-4b119fa31b1b | -9.4692 | -65.51359 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ad25f9a-453a-3651-8d23-0e95cca67ef9 | -9.11133 | -60.96994 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 696ada6e-c9f6-3785-a4cb-20e6e8cae5a5 | -8.45552 | -62.55306 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a5ec540-8728-33a5-bc5d-1c5910f68b8b | -9.29547 | -60.85659 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a106584-af8d-3adb-a8e8-4347418a3b63 | -10.08867 | -59.17743 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 194c561d-2eb7-3162-aa2d-016f360f6666 | -8.87572 | -64.0314 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3582d8df-116a-3022-9070-208bef9987e9 | -18.81909 | -49.68907 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 20.5 |
| c37b0df0-0b78-3aea-a107-42d25de2f309 | -9.17294 | -59.37323 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5a2d262-93ba-36f7-9c4f-bd85335d0b54 | -9.34058 | -65.44595 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a7ca087-2bfe-36e7-9be1-d1b9d3c0e0b1 | -10.00702 | -64.92233 | 2025-09-09 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e00ce030-8ef1-3815-a7b7-7a4ab0b2820e | -9.08907 | -61.41254 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README65.md)
