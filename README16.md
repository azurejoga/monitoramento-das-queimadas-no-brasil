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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d2923b0-1a3e-3875-ac30-e23837eb8528 | -13.13229 | -47.31757 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 431419c5-4912-39b7-9aae-477c48ea8bf6 | -13.13018 | -47.31596 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c108d193-9de9-3680-bf23-eb098b367a5f | -10.90323 | -49.20925 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 84ad2f37-1cbf-3eca-94cb-c397694d2731 | -12.41941 | -43.49512 | 2025-07-12 05:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8ef4536-2998-3ac9-bdcd-ed5e1c4e7b37 | -11.94608 | -49.30034 | 2025-07-12 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| db19d717-d7b3-371b-babe-9a746616f48f | -10.13224 | -57.77837 | 2025-07-12 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3604a9a-8223-3ec5-b83c-0e7c277cc187 | -10.69014 | -48.30698 | 2025-07-12 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c46e5459-8309-3cfd-9578-d802fa1fb8cf | -13.13053 | -47.31292 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6751e9d8-8eb5-31e5-b823-145a5c179d88 | -11.46053 | -45.10736 | 2025-07-12 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60a63352-916f-32d2-9d2d-136579f6b087 | -11.88115 | -58.72036 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79ce5c2d-0595-38d5-8ce8-5537b5e1bae1 | -11.27962 | -46.40274 | 2025-07-12 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 589af91f-7fe6-3818-a1dd-15e2233e1241 | -15.68494 | -48.27227 | 2025-07-12 05:08:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e5fc34c-b861-31fa-94f6-bb9649c7e350 | -13.16036 | -47.30204 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1815f6e5-808d-3aec-823d-eaa5d80de9c7 | -11.84174 | -47.50697 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d731768b-fdcf-380b-b5f4-1e5d90fb99be | -11.4187 | -46.37691 | 2025-07-12 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 775217b0-f1d0-33ce-89b8-5c08b8d5342d | -9.64661 | -65.73917 | 2025-07-12 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28383d4d-efb8-3625-aaf3-7b554968e6f1 | -11.10086 | -60.85021 | 2025-07-12 05:08:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b712c87-bfc5-3591-99bb-0b12eb1d64f5 | -11.9306 | -51.68967 | 2025-07-12 05:08:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 701a6ce3-53cf-3986-89dc-5367a2bd058f | -11.72808 | -47.47289 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2c5410bd-36a9-3efe-81c5-65a22ec2a3ed | -10.89776 | -49.21371 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 09904ac7-ac81-3644-8d5a-d91f58fb00d8 | -9.88564 | -63.10979 | 2025-07-12 05:08:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91a139dc-38eb-34a9-9826-3dbc38a27f6f | -10.05791 | -59.10581 | 2025-07-12 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f251c0fd-d221-3363-a552-399e746834cf | -10.89845 | -49.20841 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7eb8c530-3417-345e-9f8d-7bc6429230dc | -10.04958 | -59.11253 | 2025-07-12 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcbca918-007b-355e-9056-5d4a3f563dbc | -10.05024 | -59.10859 | 2025-07-12 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e8c915b-576c-33cd-82f1-31fa356732dc | -13.13869 | -47.31201 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cb33fcc-a5ac-3f50-b96c-7864e7e90fe9 | -10.8534 | -49.11478 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 70758629-fd76-31ee-9b67-826b667a3424 | -11.87556 | -58.71179 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 23d68e05-d3ba-32fd-b52b-7cda28428c60 | -10.54725 | -52.03448 | 2025-07-12 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cbbc7c7-27b8-3a17-9a66-c11e4d05290f | -12.48842 | -51.27623 | 2025-07-12 05:08:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2507612-e738-35f2-8a0f-1356062233d3 | -11.9362 | -51.69054 | 2025-07-12 05:08:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 032353fe-6041-3df2-b4b5-e82e4aa923e3 | -11.84131 | -47.51052 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 02d15e87-7741-3b5c-8edc-20bf79d573da | -11.93934 | -51.68716 | 2025-07-12 05:08:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80b5b947-e0d3-337c-a2cb-3bfab75eb796 | -10.90254 | -49.21451 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| df3e077f-0ef1-3468-bdc2-87fed131c395 | -10.67027 | -49.50062 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a33ecf9-2157-393a-8c7f-067364479301 | -11.44211 | -45.09992 | 2025-07-12 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d524b4c-cc14-32ad-a69c-b83da92846e7 | -13.12211 | -47.3074 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5244a82a-b675-3696-89bd-af39aadc423b | -9.01627 | -59.54543 | 2025-07-12 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c701c9d-3f8c-36d9-b9ef-8e71a2f6f64c | -9.83026 | -60.76844 | 2025-07-12 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47931c1b-8684-3a33-a1a7-0caee0326673 | -11.84217 | -47.50341 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c6c2d7d-5f25-33fd-8491-38d1a9a9a279 | -11.84058 | -47.5078 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 135e4910-5626-3d2c-9831-c48c7bd7e8b4 | -14.74835 | -50.55332 | 2025-07-12 05:08:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 236c77e8-f57c-3076-ae75-a99948ae9a92 | -12.41142 | -45.35514 | 2025-07-12 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2592fd5-334c-374b-9959-85346e543496 | -10.57508 | -49.12611 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fc01a8a5-f31a-3cfb-be44-d3a35c7d6e30 | -13.6596 | -53.94159 | 2025-07-12 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8547d09e-4f4b-370a-828c-37fce5ddc681 | -12.58302 | -56.98531 | 2025-07-12 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55144603-cc1f-3d55-b6f6-8bd47af2684f | -10.57651 | -49.11575 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dce6981c-29d0-35e9-87c7-f46cea4cabad | -13.12452 | -47.31553 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0b6e9d9-b963-3a41-8c68-4a82e9a45f97 | -10.57016 | -49.12138 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ea218fc5-73b8-3c88-bd79-c22edb1b4802 | -10.66493 | -49.50487 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e065439d-d61c-30d4-9673-8a4953e7ad34 | -12.11379 | -44.97558 | 2025-07-12 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70f478fb-8b06-3874-820d-b4266b142c29 | -13.01953 | -47.82901 | 2025-07-12 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 583b298f-f197-3de7-85b7-edaa4a25246c | -8.8021 | -67.26984 | 2025-07-12 05:08:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc52421c-7ed4-3679-b15c-8463062b05ee | -10.09666 | -60.49767 | 2025-07-12 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 443f113b-cf63-3226-a189-d524379327b9 | -10.21817 | -55.44569 | 2025-07-12 05:08:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78eb170d-7daa-3216-98cd-a679f43883bd | -13.15455 | -47.30282 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 868a4505-a70b-3c5d-a454-a85f564dc5e5 | -14.78366 | -48.20508 | 2025-07-12 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1502373e-01e2-3fa6-812a-b80fbdc875ae | -11.86535 | -58.71009 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3de2ffca-1047-3a7f-abb9-df893ab090c7 | -11.42679 | -46.4074 | 2025-07-12 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f193085-fe88-3fa8-969f-6763d0865bce | -16.66983 | -50.63088 | 2025-07-12 05:08:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9107fce8-74aa-3bd4-8462-7ef1dd8bf8aa | -10.57029 | -49.12534 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f7ff36dc-e118-3e98-8153-e1969d1a73f7 | -11.72901 | -47.46562 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1a9c53df-7d55-38b4-8532-bbc112892a15 | -10.66961 | -49.50555 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b119885c-880a-30f4-8319-8b521f6054c0 | -11.93674 | -51.68678 | 2025-07-12 05:08:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e78abcd8-6191-3bff-b81d-d1e8848a2785 | -10.89434 | -49.20237 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f018190d-af01-3a75-8224-ac7ce968ce8c | -11.7371 | -48.52998 | 2025-07-12 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d02197f-37dd-3ad8-8703-0ce68a8f0800 | -12.58247 | -56.98884 | 2025-07-12 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5dd1b42-869e-3a53-9f77-731dea3e201a | -11.87836 | -58.71607 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79f8e21a-2b23-3795-871d-ea726051c362 | -13.29149 | -49.15668 | 2025-07-12 05:08:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81cdb9b5-3d76-3fbd-9ae3-f3eb1fb8b208 | -12.99856 | -46.26823 | 2025-07-12 05:08:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d890eb5-1d4c-3fa0-87ab-2211dc7e250c | -11.83627 | -47.50632 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f2b4dac-a721-3605-a8c0-7e8a5284586d | -10.31923 | -67.34966 | 2025-07-12 05:08:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57ea4bfd-a93a-3f4a-80a4-7dd5e84f87d9 | -11.60589 | -47.61124 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d3d81e6e-8058-3aee-a461-ad8a5c1dc9b4 | -11.32445 | -51.44043 | 2025-07-12 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9243e011-0807-31a8-be01-65577e2db0ec | -8.80389 | -67.27181 | 2025-07-12 05:08:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed4bf01d-6bfb-3121-aa04-ee1bdb1cc094 | -12.41835 | -45.3507 | 2025-07-12 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7effca3-ba72-3310-9cfa-08c111f179e5 | -11.83584 | -47.50987 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a91753d5-e66e-3c32-b3f7-c42c3f6efa82 | -11.93209 | -51.6899 | 2025-07-12 05:08:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20f81e04-3027-3169-bbcd-a2b9bd23acb3 | -12.41425 | -45.35067 | 2025-07-12 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a11afb3-086d-30be-8928-73ed13d464e2 | -10.57437 | -49.13126 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8be8fcbf-16b0-3822-8b80-1c3ff9181828 | -11.8849 | -58.74013 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d15af59-56d3-3259-b034-6dfbfd3b1c10 | -9.78693 | -62.48379 | 2025-07-12 05:08:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecfeba8c-485e-3d37-9c04-c9dd2e85b03f | -11.41917 | -46.37311 | 2025-07-12 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fe2e736-26e3-34c3-85a1-8ae7cc9c6fe0 | -10.3664 | -57.49754 | 2025-07-12 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa48ed8-fc5d-3fe7-a659-e7fccf097838 | -9.01892 | -61.2305 | 2025-07-12 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70a9aebf-4d8b-3205-881f-224d88249801 | -10.571 | -49.12017 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 89c55b66-30fd-3b82-bb7b-8a3061e8466b | -13.14799 | -47.31016 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d580dce-4805-30fb-97dd-a8515a2b74fe | -10.57563 | -49.11695 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| fa6b910a-465e-3298-a58e-527332a66004 | -13.37654 | -49.12775 | 2025-07-12 05:08:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bffce31-44a3-3da6-accd-e83ba80387fe | -12.41368 | -45.35575 | 2025-07-12 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b53e14e7-0a1d-321f-93ad-cf342e0cfde0 | -12.4231 | -43.49062 | 2025-07-12 05:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4f5e45a-7d7b-300b-b1a1-7dfd13cc32e8 | -10.69517 | -48.30815 | 2025-07-12 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eec52cf1-a808-324a-8394-762c8bb441ba | -15.10215 | -56.23407 | 2025-07-12 05:08:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c470bd15-c6a3-3399-bf92-17ad7a438ed9 | -10.83893 | -49.11261 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eb677f1e-d1a5-35f3-8b16-7448670c9ab5 | -13.13614 | -47.31379 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 082c846d-dde9-32c1-b578-443769b1f617 | -14.78328 | -48.20838 | 2025-07-12 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9911187d-a29c-3c37-a8b9-15a36659296d | -10.57579 | -49.12099 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b315bcf9-6642-3589-861e-d0d23ae7f1c5 | -10.85824 | -49.11538 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2b929239-4dbe-3dce-8903-2a2bcfb42079 | -11.94461 | -49.29568 | 2025-07-12 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6558af1c-7216-320c-8aeb-fc89525d0888 | -13.65404 | -53.93849 | 2025-07-12 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README17.md)
