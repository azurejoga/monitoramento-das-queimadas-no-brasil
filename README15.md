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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbf4bcbb-ed58-3957-9690-2886b6f2645f | -12.98022 | -45.21605 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9f06e59f-d9d5-31e4-8af8-653be3aa5a37 | -6.53161 | -45.46209 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 290dde52-ba27-325a-b386-602fcf1185a2 | -5.87222 | -48.12078 | 2025-08-21 03:49:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc78ad59-9549-31d3-a631-acdf4269b93d | -12.95355 | -46.24606 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3572a5a7-c046-3cd5-8012-4b096dfdaccc | -7.02267 | -44.61078 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7c97070-797f-30e0-b0db-e69ed095d8fa | -7.9503 | -42.6439 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0d331db0-42ea-310f-ac84-e95b252eea46 | -12.95095 | -46.23354 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e6aa8115-45da-37a9-92af-76cf5effcfd8 | -11.81994 | -50.65178 | 2025-08-21 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1522a71c-b8c4-3ff0-9722-4d54abc187fb | -12.98209 | -45.21704 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| afc9c81e-b575-3328-9355-8315f417adbc | -6.29127 | -43.88317 | 2025-08-21 03:49:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c6c2065-08b6-39f3-b3d2-27595267eaeb | -8.14701 | -47.34114 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c398db0-aafb-3fe1-a472-63cbe5c708fb | -7.70215 | -44.01788 | 2025-08-21 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 799b025f-cd0f-3f24-b273-fd4ad4eab239 | -7.64108 | -45.24936 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ab10d06-58d5-3cc6-923c-451a4fe1c710 | -12.64434 | -46.87128 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b064f6a1-3b5b-3017-99f5-43a76c184709 | -12.09076 | -44.72729 | 2025-08-21 03:49:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3d8c537-6705-3e20-8a50-848d6ef5b4a9 | -8.26559 | -47.29174 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dcee3502-7205-338d-9e77-e888c1395bfa | -6.94734 | -42.86914 | 2025-08-21 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d3a3303e-20be-32d5-aa59-b766dc717651 | -6.42041 | -44.67598 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c926a4a7-716e-3cb3-9b08-4febcc0ade1b | -13.03565 | -45.16563 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a48daa0a-0bdd-3667-b5ad-fd604410b430 | -12.63769 | -46.87901 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3376dd1a-73ac-32e4-bc71-8bfdfba27fc0 | -12.98554 | -45.21229 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3682f6f5-b2e9-3cd4-8fe6-8de4eada5493 | -10.72577 | -48.23903 | 2025-08-21 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc439dc2-4191-3894-a84f-3603cf3e9c08 | -8.54002 | -39.58572 | 2025-08-21 03:49:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 572c601c-8757-3bc8-9f48-037bb58a5949 | -8.16242 | -47.3516 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fae644b-2660-3570-a78c-71d1c30dac39 | -6.95158 | -42.86979 | 2025-08-21 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 290f7c32-addc-3c72-8668-710430667ca4 | -10.3902 | -42.58193 | 2025-08-21 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 222b9a72-78ba-3ded-a36a-7c6eaa2e51fa | -9.65942 | -48.38325 | 2025-08-21 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6245131e-175f-3ada-bea4-440f01d5dd5d | -12.94741 | -46.22608 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 339ef76e-0595-3558-b36e-f3a00d4c6c97 | -12.98193 | -45.20692 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 02f886c3-623d-3dad-ab02-e677ec919b50 | -12.64452 | -46.89801 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4009a88c-642f-34b2-9b58-476c38e6b5dd | -9.48111 | -47.32774 | 2025-08-21 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2614d95-a790-363d-ad1f-39b228a7aea1 | -9.29879 | -48.4234 | 2025-08-21 03:49:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da9d2ee2-ed39-3a12-a9fe-7b256cf29c2d | -6.2802 | -43.72395 | 2025-08-21 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d07ea57-daac-322c-981c-65df3e848c1c | -7.69689 | -44.02142 | 2025-08-21 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 203b529d-8d27-3cff-9683-06064cb1d651 | -14.05544 | -43.53854 | 2025-08-21 03:49:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2192b57-20fd-3116-8291-8a1164be7fb8 | -10.28433 | -46.7639 | 2025-08-21 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6a174d8-bd18-3974-bf02-7f2d5f2de4d0 | -13.0376 | -45.18009 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 65daa746-fab8-35e2-8660-2a60d468bb37 | -11.17796 | -46.13617 | 2025-08-21 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 545e768f-e3d7-3d8e-a521-c55883bb917c | -6.74458 | -43.9342 | 2025-08-21 03:49:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac72023a-c26a-39ae-9de4-69e51f35195e | -10.99446 | -45.623 | 2025-08-21 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de942bbd-bb84-3397-8237-7662c2edca9d | -12.22053 | -45.4051 | 2025-08-21 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9ee9e41-fc03-3532-aa58-de536abb7201 | -6.7117 | -44.32303 | 2025-08-21 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fe1eb3b-1fe4-3999-ac7c-30e1a4ef3bdf | -13.01538 | -45.17576 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 0afc7bbe-f662-3d52-babf-3632ab94497c | -9.92632 | -48.68814 | 2025-08-21 03:49:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 740b2589-4764-3de2-8367-34cf2b2f45c5 | -9.66607 | -48.38015 | 2025-08-21 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8b5534d-abe6-32c0-9835-66777b7125d7 | -12.95381 | -46.2183 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b399ccb-71ee-3a33-ae85-9bdfc92e7f26 | -6.10457 | -45.41065 | 2025-08-21 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e15f16d-5e15-3a0b-af00-03c2c3869d3d | -6.10407 | -45.4136 | 2025-08-21 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a32198af-76be-35b5-92cb-7716ba58dec8 | -11.30258 | -44.9451 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 972202ed-e3c3-3880-8f83-60186a93f6af | -13.04286 | -45.17649 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5d854ad7-bd5e-3d5d-ba88-651e91831f7a | -11.02084 | -44.60055 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ee0b398-d0a4-31d4-9938-813c4ba75260 | -9.11846 | -40.31003 | 2025-08-21 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd2dad56-16fe-32a8-b974-1c44c7b85375 | -11.57892 | -47.00432 | 2025-08-21 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bb91278-a4c5-3680-a331-96a56fdbd055 | -7.25115 | -50.16394 | 2025-08-21 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df14df18-8102-3b1a-ba00-a7ec1c770328 | -6.27487 | -43.72796 | 2025-08-21 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baaae0ef-82fd-37e2-9d7c-44b1d8b50cc9 | -6.36709 | -43.25583 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be521170-a076-365b-9de7-4d205f7974dd | -12.63719 | -46.88169 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c78f2cb-812f-3d42-9bbb-14034fe934dc | -12.94894 | -46.24427 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4709e767-278d-3a58-b54b-a317039ca023 | -8.42866 | -49.57271 | 2025-08-21 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b01af18c-642d-3adb-93fd-58142ead511b | -7.59663 | -44.38596 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| feee5d27-37fe-3b18-b8e3-303b7d174d0d | -7.26271 | -43.68324 | 2025-08-21 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73088968-1968-33e8-9603-f4ba3d7ebc89 | -10.72489 | -48.24358 | 2025-08-21 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 70423082-e8b0-3970-b764-21cc3f5331e4 | -12.97563 | -45.20168 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81fdb4ac-1659-3189-9227-475d056d5c0a | -13.16578 | -46.8753 | 2025-08-21 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76c75c0b-8b0a-3cdf-8096-4c7d3f846f5b | -7.61748 | -45.26855 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44b67e1f-ee81-323e-85ec-b0a6c030126f | -9.6404 | -40.59948 | 2025-08-21 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c31cee43-a5cd-373b-8ce0-1a3fd52c5423 | -5.8542 | -48.79858 | 2025-08-21 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2700250-203d-301e-9892-2b1aa602ea8f | -6.34173 | -43.43005 | 2025-08-21 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c977f72b-be37-3432-b8a3-e81ce6d53f5a | -12.21965 | -45.40989 | 2025-08-21 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 18b43d37-75e6-35ab-8a4a-efc8a58be87f | -12.89465 | -46.08434 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 11e14711-0f34-3351-af67-03124ab40aa0 | -13.04177 | -46.82107 | 2025-08-21 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 01e07a7b-7b3b-30f6-aa72-153ab611d540 | -7.26567 | -43.69281 | 2025-08-21 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 548189c8-894f-30c2-86b9-315fac99c819 | -11.75934 | -40.18481 | 2025-08-21 03:49:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a12f6433-0961-3e10-a4b9-a44377ba8a92 | -7.03122 | -44.61787 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1c3321a8-d483-3a22-bba6-a02477605328 | -6.57297 | -43.00229 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bc4a1de-94f3-3de0-bed1-6e380d142c51 | -11.57831 | -47.00751 | 2025-08-21 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca469bda-92d3-3c34-8ae1-a1085e9fee14 | -7.63614 | -45.24861 | 2025-08-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f6fccb66-9fa1-3a1c-8feb-698a9c852f8c | -6.93078 | -41.7338 | 2025-08-21 03:49:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5c53b84f-10f9-37eb-a034-ba5bfd3278e1 | -13.04237 | -45.20433 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2e33b93e-1a0a-3e6e-a419-a3c81a7b75ef | -12.67004 | -44.9587 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0086f5a9-f17b-380b-a795-505fb61d84ce | -9.66026 | -48.37895 | 2025-08-21 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81ef7c22-61f7-31f2-b33d-de1451f915fc | -6.17935 | -44.73204 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4c70e964-f226-3c35-9430-7534be0623d4 | -13.03264 | -45.2071 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4bb23ba3-d43e-3238-acf3-dc33e304a093 | -13.02512 | -45.1729 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d1480196-7434-3766-9ab0-2b97140380c5 | -13.64867 | -45.71337 | 2025-08-21 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f270440-e3ba-30e6-9950-9e87539bd541 | -6.35898 | -43.65114 | 2025-08-21 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1fe1a40-8a0e-33c1-91e0-6b5e9265a8e7 | -7.5756 | -44.39732 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f51246c-8106-3708-83ef-08520942d5d9 | -13.02067 | -45.17205 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 39ebcd35-cc27-3a7d-a670-b2fd2f1a4f4a | -12.09086 | -44.72671 | 2025-08-21 03:49:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a505a73-40e6-3aef-b33e-d42aca135774 | -10.2789 | -46.76424 | 2025-08-21 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37bfa882-ef8a-3315-9162-135c0a5841f5 | -8.14231 | -47.3452 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00d62eab-fe25-3841-88f4-c4e5987f1b49 | -7.21298 | -45.31516 | 2025-08-21 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 822a4106-336c-3464-bb89-809083e48105 | -13.02819 | -45.20625 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cd7e0554-45e4-3fce-b970-b3417f7f0147 | -13.04973 | -46.83329 | 2025-08-21 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdba0e0e-064b-353e-8a55-2f44c3b3c63f | -7.14607 | -44.17794 | 2025-08-21 03:49:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ceef050a-5c76-32b3-9432-54ff4f17db78 | -6.95712 | -42.86265 | 2025-08-21 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 158cc342-adff-3efb-a706-99e8924e638f | -10.39021 | -42.57901 | 2025-08-21 03:49:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e993b602-5120-32e8-a413-766847733e06 | -12.63819 | -46.87634 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 93473df3-b4e8-3e0c-aa65-3f72b15de5a7 | -7.60045 | -44.38403 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bff35d3-ce19-338b-a311-e2ac0fc995d4 | -7.64654 | -46.27291 | 2025-08-21 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README16.md)
