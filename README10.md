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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f551f10-bf16-3c1e-99fb-4aae8417a508 | -5.82315 | -44.14106 | 2026-07-30 04:57:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0478fa58-e4f7-3784-a7bb-9d7390f106c7 | -3.16866 | -48.13234 | 2026-07-30 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdc7fe4d-01c8-3c7a-904e-f35e11397d6a | -3.18109 | -48.02003 | 2026-07-30 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d05c529c-b36a-38cd-831d-500210bbd21a | -2.48545 | -47.08819 | 2026-07-30 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65e080f8-91e3-3823-b795-e800b3cffb80 | -7.33958 | -45.85553 | 2026-07-30 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae750340-8d69-31e2-abb8-d748ad99f3f4 | -3.18469 | -48.02442 | 2026-07-30 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04c4aa1d-c786-3492-8688-7a05a7400d53 | -9.61476 | -47.76195 | 2026-07-30 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1f73fa89-1148-3994-9c92-1c5bd7fc0742 | -4.90704 | -43.47441 | 2026-07-30 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31969660-98ed-31dd-942f-a933f2b3ec34 | -3.96071 | -43.11875 | 2026-07-30 04:57:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dffdd07-874c-36fe-978e-9eb95fe32279 | -2.60878 | -47.35439 | 2026-07-30 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4890248b-4336-3210-afe3-b7b50ad9d284 | -5.75133 | -51.7115 | 2026-07-30 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91597c78-5cbd-3a4d-b79c-576c599b2532 | -4.28497 | -48.24556 | 2026-07-30 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb0fcca7-1671-3415-923a-45d4b19b2266 | -3.24168 | -47.9283 | 2026-07-30 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 951abce5-a1f7-34d0-8b1c-8ee520e8f5b5 | -7.19926 | -45.49743 | 2026-07-30 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfb90005-b66c-380a-83fc-ca0e4cfb48fd | -7.24294 | -55.03473 | 2026-07-30 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b95cf044-8af5-3ab5-a50e-ccdb846714bf | -4.18535 | -49.22952 | 2026-07-30 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df1a6120-28a2-36c6-80dd-c0e85ac4f0c2 | -6.33888 | -44.60553 | 2026-07-30 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f581d37-0769-3fc8-b775-30e41cc4258a | -5.04804 | -43.26921 | 2026-07-30 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 54b9827e-092e-39ab-9d0d-a923367fbf9a | -7.20246 | -44.87853 | 2026-07-30 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1dce727-9683-3bb9-958c-6ea83917e3ae | -4.36938 | -47.77008 | 2026-07-30 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 03312f93-427e-3b11-ba83-b6fb75124165 | -2.48983 | -47.08885 | 2026-07-30 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c09b1bec-6ac9-3ac5-9591-b1873f4abf0d | -7.34513 | -45.85313 | 2026-07-30 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18608a17-93ef-33ad-af35-a4fa06233653 | -2.61049 | -47.35634 | 2026-07-30 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9a8cbb4-7bed-3a04-b03e-03b28ebb7bc0 | -4.38899 | -47.75663 | 2026-07-30 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 92da0e68-0733-3175-b8bd-53b0d74b7bc5 | -5.04862 | -43.26495 | 2026-07-30 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ccd721d-2bc6-3540-af6a-ca33bd7c1e49 | -5.82932 | -44.13801 | 2026-07-30 04:57:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 188d4997-240c-384f-8ff8-584d6597d6cc | -2.71828 | -54.62237 | 2026-07-30 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac7724d-d180-38b4-b948-957aca1f659b | -3.1775 | -48.0156 | 2026-07-30 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25f005c7-316b-333a-aa24-1d6ead066b1a | -4.90763 | -43.47038 | 2026-07-30 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 987b13ca-f236-391d-8b62-31326f7f4b3d | -6.86003 | -46.01038 | 2026-07-30 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f695716-c35a-324c-baa9-f764f47d97be | -4.55704 | -50.30319 | 2026-07-30 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98e58d1b-6fe0-37b7-98e8-c6b923677ab1 | -5.7519 | -51.70767 | 2026-07-30 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4278b349-b5f5-3298-ad9e-d482e7e1229a | -3.64117 | -49.70892 | 2026-07-30 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adfe43aa-c7e1-30b2-9d3c-844ac2f33516 | -1.7305 | -55.84572 | 2026-07-30 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84333e6e-fdac-3069-a689-6b679978417e | -3.13698 | -48.59197 | 2026-07-30 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a113136d-44c4-3cd4-8877-e99c5d8fa909 | -6.33861 | -44.60392 | 2026-07-30 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c079fbb1-f3fc-3301-a811-c01533203f50 | -2.90852 | -54.5616 | 2026-07-30 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36c005c3-6653-3af1-960b-0307158312d8 | -3.17639 | -48.02315 | 2026-07-30 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bca6a06f-d3be-3314-839d-fd203aa762f5 | -7.34816 | -45.85069 | 2026-07-30 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0ab81ca-ff2b-3a42-9670-5340db781b73 | -3.6795 | -49.48432 | 2026-07-30 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fb1254b-2f4e-3d5f-b8ec-c740a9a53e83 | -4.02565 | -53.63757 | 2026-07-30 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58b82fba-142f-3297-b5bd-e2fb8c7171dd | -8.13068 | -46.77654 | 2026-07-30 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a66618b-384e-39bf-92ce-b5e418686e54 | -4.56112 | -48.01997 | 2026-07-30 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7744c59-0d29-33cb-8263-34ea55f891c3 | -5.74785 | -51.71098 | 2026-07-30 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 09b82d6e-1345-3a23-aada-2bc2d7a1868b | -11.39512 | -50.12534 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab25463e-0110-3eb7-bdc0-dde71bb7376f | -13.33269 | -54.29418 | 2026-07-30 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffe492a1-af80-33a7-9312-58e94c535e60 | -11.41943 | -50.099 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca010d88-1045-3062-95f2-9625f40c86eb | -13.05865 | -60.65422 | 2026-07-30 04:59:00 | NOAA-21 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93388ca2-bca1-3790-a748-22ef543e6592 | -11.38664 | -50.12524 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08cb368e-b2b8-3692-bc47-9e1075ba763b | -9.48285 | -57.3235 | 2026-07-30 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7222b5e-e62b-3e80-aaab-5c0a01512c1a | -13.74387 | -51.89486 | 2026-07-30 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2eef8c6-1145-34f4-9ba3-a72bfa06a686 | -9.47041 | -63.27834 | 2026-07-30 04:59:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e6144ca-8923-3cd3-9ec3-03d1e42117ee | -8.92196 | -65.01067 | 2026-07-30 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3eb5fc4-8da5-30be-92d5-f696e85107c1 | -11.39529 | -50.12277 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b30db818-aace-3080-8886-e0fa9c794a6b | -11.41992 | -50.09533 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d258dc1b-d206-33c8-bc6e-cfcf90a6bf0b | -13.32146 | -43.59284 | 2026-07-30 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5c0079e-ad6f-3ff4-9b89-bffacd15e69b | -11.39154 | -50.12109 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5f5c8b2-d032-3d28-af23-773893af756d | -11.41684 | -50.08738 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfdccaaf-272b-3742-a363-33b9a64f9f89 | -11.19378 | -50.61068 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfde44b8-4b97-3ba2-bf45-adda029aae91 | -11.84318 | -50.15736 | 2026-07-30 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 652caf53-da75-3dda-b916-0acb3d739dbf | -13.7405 | -51.8961 | 2026-07-30 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17f182a9-6679-36cf-a185-3cf139e26046 | -11.08966 | -47.80379 | 2026-07-30 04:59:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 43316eb1-a61f-3b3e-b921-2565440511d8 | -13.74011 | -51.89428 | 2026-07-30 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9766a90-2c82-301e-ac8b-3262d5059c35 | -14.21185 | -51.92141 | 2026-07-30 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d60a093b-9041-315e-a72d-489f64aa24a9 | -13.32987 | -54.28995 | 2026-07-30 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91ea8d3c-bdaf-3360-985b-b8e8d8c6c004 | -14.70649 | -50.54879 | 2026-07-30 04:59:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c76f348f-60be-3fd4-95a2-fdbb6d025145 | -11.41634 | -50.09106 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6032dcbd-28ce-3ab7-8673-4cf6b6986342 | -11.41276 | -50.08678 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0017f145-5d86-3dc5-b864-86b2e2cf08de | -14.21563 | -51.92197 | 2026-07-30 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ddd5ead-b4ad-3229-a7d7-f46c77e114b1 | -9.57447 | -60.63227 | 2026-07-30 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e5121e8-bb43-39d9-88e2-5165bc44971f | -11.44047 | -58.77005 | 2026-07-30 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a65612b2-7ca2-366c-97a5-347bd1156414 | -11.42042 | -50.09166 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fbe8f355-0c3a-3c2a-8a50-23f10337d76f | -11.93072 | -43.44106 | 2026-07-30 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8428a0f-bcbd-3fe0-96e7-957bb217661a | -14.20807 | -51.92084 | 2026-07-30 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 744de7b7-ffea-30fa-b32c-b117db309984 | -9.48001 | -57.31905 | 2026-07-30 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfcd8d04-2f9f-384a-a183-ebddb136b480 | -11.39122 | -50.12218 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a06bbf59-34d6-34b9-b933-e8ae3228968d | -12.42973 | -50.54963 | 2026-07-30 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e634e718-1d82-34b1-9c98-d1f468c107a7 | -9.37796 | -58.2093 | 2026-07-30 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de61c5a9-f906-31c0-8e56-30b021a27114 | -8.82349 | -66.75294 | 2026-07-30 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc1dd7ed-6604-35b5-b552-19e1f5a9f4d0 | -8.9121 | -65.00077 | 2026-07-30 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8759c7e8-fb1a-3c3e-bec2-b4a81ac31c84 | -12.28661 | -50.34663 | 2026-07-30 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7bcae18-d4dd-330b-85ab-5ddf01396ae5 | -11.39478 | -50.12642 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7ea7ba6-9089-39a9-b1a9-cce962d0d40d | -12.15056 | -48.9503 | 2026-07-30 04:59:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a6df65f-f1d1-369a-90d1-3d1071e7b605 | -8.91703 | -65.00571 | 2026-07-30 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc4ccf83-64f8-384f-9d49-c11cfdea18b1 | -13.33324 | -54.29049 | 2026-07-30 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9dc6446-de3d-3abe-8832-67ae036574ab | -10.63271 | -47.48851 | 2026-07-30 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c984ab2f-7213-3490-a13a-78cdb5ee99bb | -10.93897 | -43.0582 | 2026-07-30 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 7fc4e4a0-0bd0-313e-b0f2-af54cbe034a5 | -10.93834 | -43.06363 | 2026-07-30 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 9d289fd4-1f04-383c-900a-4db78a142279 | -11.92503 | -43.43443 | 2026-07-30 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62e81858-c94d-328d-a124-8899fb5f1b68 | -10.93252 | -43.05735 | 2026-07-30 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66a813ce-d653-38a0-8390-29f32e1663db | -13.32932 | -54.29364 | 2026-07-30 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b23f068-addb-3fe6-b564-46e816d98f56 | -11.4046 | -50.08559 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70d78f07-f729-321e-baef-50fa36adc0c6 | -13.31503 | -43.59201 | 2026-07-30 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61983b80-848e-36bc-ba57-f95ca0123ab4 | -10.84717 | -54.04486 | 2026-07-30 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4174620e-83b2-3613-9cc7-52472d39baf7 | -10.47198 | -62.44957 | 2026-07-30 04:59:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de4f509e-a1ba-3b72-acf6-7649988fc3e9 | -11.38206 | -50.1283 | 2026-07-30 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f394b74b-3e86-3f0e-a133-750a0bd56b00 | -12.31319 | -46.75443 | 2026-07-30 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cc121bf-6eb0-3fdd-8c72-7357340a8047 | -12.43021 | -50.54606 | 2026-07-30 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a42a34f-8b5a-3c94-8b74-4424b5a7c3a0 | -10.63343 | -47.4831 | 2026-07-30 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be62a8b5-5a76-3dec-8cbd-ebb9d756aed2 | -12.14612 | -48.94964 | 2026-07-30 04:59:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README11.md)
