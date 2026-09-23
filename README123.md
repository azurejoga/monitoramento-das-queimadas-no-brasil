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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f9200fd-1412-3d20-9286-d4f42d9f740c | -7.13198 | -48.4297 | 2026-09-23 05:25:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58dcfeb6-8d98-3edd-9128-f6a8c3913f4f | -5.76574 | -56.52209 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 498e1546-590e-3f31-b35e-a18309fb654f | -6.7747 | -59.63034 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6d7e15e-c2d3-306f-a0c9-c36b78e4c6cb | -6.25054 | -57.7777 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63fb2bc5-8818-389f-8cdd-56d34603cf16 | -6.63202 | -59.92842 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5de3c61-c24e-3a3d-ab4f-d3a9943c8a6c | -5.81799 | -57.74377 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42a319e2-d295-34ad-a982-3ea0537ac507 | -6.91036 | -59.84474 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89615186-5f46-324e-8aed-a810cfd7e742 | -5.24692 | -59.98164 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 471efeff-4691-3703-8b1a-35b81536db70 | -7.09413 | -52.75019 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a4518b1-5d33-30ae-bb9c-bbcb4b99b754 | -7.03298 | -59.50134 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b424628f-6411-37be-9058-e4233868ca8d | -7.12151 | -56.54774 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5168c64-caee-3567-b1f3-ec0690d3231e | -5.81854 | -57.74018 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c13269ca-2348-3d88-8bdd-768adb3ea2f8 | -6.77856 | -59.62741 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f86cecd-308e-36a7-a6a8-cd7ad1b55176 | -6.71496 | -58.99965 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c23b0c1-990b-3611-bf0d-aa12ed5564de | -6.62538 | -59.92737 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f5affefe-a048-3708-9172-58c465bb4e13 | -6.67383 | -58.57033 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4557af9a-d1df-37fb-89b3-292e7cb0b3fa | -6.61 | -43.7 | 2026-09-23 05:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 853520b4-8149-3f5f-a225-a30fd084f7ea | -6.61 | -43.74 | 2026-09-23 05:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92ee20e1-8ead-36ff-8ef5-d792f3270a07 | -6.64 | -43.75 | 2026-09-23 05:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 051b7fc5-bebc-3649-85ec-6107ab73363b | -8.935 | -61.495 | 2026-09-23 06:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c2a14808-0e1f-331f-942b-35c180e507bd | -9.1024 | -61.4491 | 2026-09-23 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 273f3939-a99a-35a8-8b42-46e7e291f858 | -8.9164 | -61.4958 | 2026-09-23 06:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| a098e02f-9980-342e-bc74-b4cd1f5ede3e | -11.65 | -50.96 | 2026-09-23 06:00:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f83f534-ab1c-30cf-89c9-0c2c184b9244 | -10.29 | -50.54 | 2026-09-23 06:00:00 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 768b7144-2e12-3bdf-ad57-68e95362a3b7 | -6.61 | -43.74 | 2026-09-23 06:00:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dcda8ca7-40e8-3454-be52-41c20aee7bc1 | -6.61 | -43.7 | 2026-09-23 06:00:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69920789-9ba2-39f9-99a2-1edbee04739e | -6.64 | -43.75 | 2026-09-23 06:00:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7df99269-14f3-3a67-98cd-602d752bbf0f | 4.09899 | -60.99717 | 2026-09-23 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2c35707-9aa5-3e0b-bfc4-6a362865676d | 4.09949 | -61.00018 | 2026-09-23 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27b5171a-4405-3d23-8cfc-fd060e44b9d9 | 2.76545 | -60.26187 | 2026-09-23 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe445113-3641-3cd7-9cb9-fd3040a7c2da | 1.77053 | -60.23321 | 2026-09-23 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6548ab6-9ac8-3937-97cc-a1e78c71cebc | 2.76641 | -60.26111 | 2026-09-23 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72c746aa-cb26-3a72-92b5-bc68afe121b0 | 2.77198 | -60.22729 | 2026-09-23 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67de47ac-714e-389c-90c3-26903c96f79e | -2.86022 | -57.78661 | 2026-09-23 06:05:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4de34e24-e8a7-39fc-a403-3e91edb1f73f | 1.07692 | -60.67527 | 2026-09-23 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29571afd-8f0e-3987-ad3f-a5afdaa915fc | 1.16935 | -60.36836 | 2026-09-23 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3d5ae74-8d1a-332b-bb4e-efce66bb1276 | 1.1706 | -60.37191 | 2026-09-23 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 842aca9f-9c99-3140-b351-941ee0738c62 | 1.07747 | -60.67879 | 2026-09-23 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81e0025c-8fdb-3146-80bd-feaf72589260 | 0.17679 | -60.48763 | 2026-09-23 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d41d997-1dbb-3a7a-abb1-488910c616cd | 2.76602 | -60.26541 | 2026-09-23 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78fc3c7b-1720-3cdb-900e-bb62a20e8e67 | -2.86713 | -57.78774 | 2026-09-23 06:05:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ebd685d2-0d93-33b6-94ff-ad8fee0c8f8b | 2.767 | -60.26463 | 2026-09-23 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 619167b4-a89c-31ad-aa2e-1140668269f7 | 1.91115 | -60.58049 | 2026-09-23 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcc24d1d-c0c1-36b2-ba7f-c975e5f30c4c | 1.16873 | -60.36459 | 2026-09-23 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63d68949-881d-320f-8aa3-9308f9078bed | 1.90573 | -60.58136 | 2026-09-23 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20eef319-f788-3aa4-bea4-46e0533a0681 | 2.7709 | -60.26094 | 2026-09-23 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f9afbdd-382e-37b8-95cc-3853e7dc5608 | 1.07145 | -60.67605 | 2026-09-23 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4095a09-4932-3b7c-9ef8-a5751bc1944f | 1.77112 | -60.23691 | 2026-09-23 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7339eb19-1076-3ae6-bba0-d9fe44ff97dd | 1.17002 | -60.36816 | 2026-09-23 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a779277-86cc-3d1d-b4dc-31a887c12c4d | 1.16944 | -60.36439 | 2026-09-23 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c390d7f3-db53-3f8b-849f-56ee11068da7 | 2.77745 | -60.22639 | 2026-09-23 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e937b138-edff-3a8b-aace-fba2973bdf9f | -3.6122 | -60.56414 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61c5b52a-876b-3798-a39a-f23fd92bcb49 | -3.1132 | -61.0938 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3664303-cd41-3d02-96f4-f24cd0570391 | -6.12185 | -59.93662 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 281173e5-eb6b-3e39-ad79-6ac5894cd5a1 | -6.67166 | -58.56139 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| deec4030-26ba-37e3-b57d-c54163e881ed | -9.14008 | -67.94855 | 2026-09-23 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9385523b-2b29-3882-a574-cea54b02edd8 | -3.39952 | -61.05458 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bff8b85-db54-35a2-b4b9-e7399dffb5cc | -9.18847 | -65.85323 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ffbf2f4-3045-3b9f-907c-e68d048019ee | -6.67661 | -58.57346 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 14fe4a4c-c54a-3aa6-a5d5-b93f2c211f2b | -8.22717 | -62.83403 | 2026-09-23 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cebccf14-6233-3940-b602-4d261aae6e41 | -9.13708 | -67.94954 | 2026-09-23 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6d44521-c0f9-3f20-8bc8-d635c02852a0 | -6.46762 | -59.99446 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d51d0054-e400-3822-9e70-cb1d6b01f787 | -9.16217 | -61.3635 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22a7c737-5f4f-3507-9858-ce3069a88d27 | -3.53781 | -59.61364 | 2026-09-23 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 010a3efb-bedb-3348-b0f2-cc736f56259d | -4.15622 | -60.79161 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d3cc1c6-880a-3330-a92f-cf3ab55eec5d | -6.65351 | -59.93137 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 064649b0-1888-3a69-a332-40b33a45e0d1 | -9.10141 | -61.44062 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fb34cf9a-eb75-3a40-8314-96523deff463 | -8.29215 | -72.83407 | 2026-09-23 06:08:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e56e76fd-2f72-3004-8d97-35a90a9c9345 | -6.77887 | -59.63338 | 2026-09-23 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c287a19-7d83-33af-8f80-7464212443d2 | -3.11073 | -61.09125 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d67e7a30-5619-3a4a-bf3e-55dcf33f5070 | -3.39326 | -61.05767 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de10a5cc-31a7-3d55-87ce-3b81017f388b | -8.53977 | -67.00874 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53d41400-6ed1-3762-b185-5c5dcc464af9 | -3.78859 | -60.74953 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39f60404-4bd7-3c26-b7bb-262353b7e366 | -5.92522 | -59.91544 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6c3c2534-35c0-3722-aacc-eef5fd5875b1 | -4.09447 | -62.09815 | 2026-09-23 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89a10b49-1c50-316e-9398-d32997dc9afc | -9.22206 | -67.39321 | 2026-09-23 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 054c6163-f965-3265-81b0-b457affbac92 | -9.184 | -65.85258 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a1f2ab0-633b-353e-931b-e13ddb011196 | -8.6165 | -66.73199 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e2839882-e4d5-30c4-a4d4-d6feae9657b7 | -6.62658 | -59.93807 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 09e8cf79-d931-3048-9ad5-0913cbae93ee | -8.85862 | -62.42355 | 2026-09-23 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f69b4ca0-6733-354a-886b-be71661c291a | -6.61108 | -59.95716 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4186b5eb-695e-398e-a1be-0ef53292f8a2 | -7.50929 | -63.88 | 2026-09-23 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62bc4573-3f2a-3218-a069-431b006fd1f1 | -6.30687 | -59.9472 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 357b9941-fb32-3ccd-b810-e4806321c416 | -3.46904 | -59.5743 | 2026-09-23 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f75ea01f-a8a2-3a1f-9e05-43e8beabebc3 | -9.16162 | -61.36804 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8d16191-0b08-3241-b471-5d5af1f0899b | -6.61676 | -59.96339 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 391846b3-d90b-3718-ab33-d8852a0eff51 | -3.81875 | -58.88603 | 2026-09-23 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d3e37b5b-a599-3b90-ac1e-cd220526f662 | -6.61976 | -59.99006 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d04723bd-8b8f-3685-853e-0b1988d208e8 | -6.67743 | -58.56705 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f1fafd39-a0dd-399e-9c5f-f8a2404bf4f5 | -6.64071 | -59.92962 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 21a15d60-96c7-3bc9-85cd-72ccad7ed136 | -8.52339 | -67.00629 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6b157ae-74e5-376b-bbe2-cf6e06e4eff8 | -3.86625 | -58.82367 | 2026-09-23 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 500d6478-0c8a-3080-a525-19505330ac16 | -6.73917 | -59.42174 | 2026-09-23 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 28039770-95cd-39b2-a5da-b87832991d77 | -3.68817 | -60.5803 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f670f616-ffa5-38ed-be98-46e7e4b6851c | -6.61522 | -59.91045 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 21f7ba5b-c9ab-3aa7-a8ed-0c2de35f31ac | -3.68229 | -60.57936 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 50fc309f-0d42-38e1-b66a-5713524579c5 | -5.42046 | -60.21698 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6276d608-0cdc-3ab3-a1f8-d6c6778a3aed | -8.52698 | -67.01058 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a59426d-35a2-3178-bd70-909739caf0f5 | -6.66998 | -58.57397 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5c61af74-e0f4-3950-a401-7c0fb3b2075d | -3.76826 | -60.72512 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README124.md)
