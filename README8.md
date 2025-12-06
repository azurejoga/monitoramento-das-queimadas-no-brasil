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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83656a63-0b29-37cb-91af-317d62ee9fee | -19.66181 | -56.8247 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d8728240-3323-3191-813b-0ac319708218 | -22.47558 | -50.24013 | 2025-12-06 04:38:00 | NOAA-20 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c21efdc-ab52-3cf6-8fa5-65dbc78d4cab | -22.07728 | -46.82312 | 2025-12-06 04:38:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 603afa02-8355-331d-a910-d13be1637572 | -26.1535 | -51.49636 | 2025-12-06 04:38:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e994cd2f-161f-33a0-8aa5-8467170f156d | -22.99036 | -48.65799 | 2025-12-06 04:38:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ab91dc5-480d-3259-892b-79282544b7bf | -26.15685 | -51.49698 | 2025-12-06 04:38:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| efaeb71e-7b2d-35bd-88ce-9f11a71f3c22 | -19.65358 | -56.82294 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3b6f97c7-9c99-37a4-a56c-36ea2321444c | -26.91312 | -48.78302 | 2025-12-06 04:38:00 | NOAA-20 | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7d3c8617-c12f-3e2a-94e3-237477a82937 | -19.65077 | -56.82682 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 45df8e1e-62c1-3884-89f9-0790b0bd693a | -27.31336 | -50.55555 | 2025-12-06 04:38:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 48e7208f-1219-31df-afc7-5440fdf917da | -19.64871 | -56.82598 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2b15b5fa-1491-3642-a0e3-384920f68ad2 | -20.91323 | -56.3777 | 2025-12-06 04:38:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5fd3d6dc-8e3b-34f1-a2b1-644a647ce099 | -19.66669 | -56.82166 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c9f1a979-ecce-3bf7-981d-e71f9599bf65 | -27.31623 | -50.5604 | 2025-12-06 04:38:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c58e8304-bb97-3635-bf0e-df215d90ec38 | -27.31683 | -50.55616 | 2025-12-06 04:38:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9616730f-8a4b-337b-9162-158023bd8560 | -19.6708 | -56.82255 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 55c802c2-9200-3486-ae98-00e5546513d9 | -22.74923 | -42.00366 | 2025-12-06 04:38:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a2b5b88f-4084-3fa4-aaaf-9f165d8de4b6 | -24.58043 | -50.97704 | 2025-12-06 04:38:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce6d0098-e4ab-3bfd-9768-806f1282353a | -19.6577 | -56.82382 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2ccbcb7c-c667-3d48-9e04-2f8de5f961ef | -23.51216 | -46.59589 | 2025-12-06 04:38:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 68af1252-b1e2-3610-9adb-d5a04d22fdf8 | -19.64671 | -56.85836 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a108ad6c-ccbb-3ec9-9f96-266947ea6260 | -19.65007 | -56.86319 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 86fc9fb8-317c-36ca-bc97-ebd942b575a1 | -22.72818 | -49.3486 | 2025-12-06 04:38:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7ac1044-deef-3693-b2a1-a7f0bbda13a1 | -19.65562 | -56.82377 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fe74fcf0-59ef-3653-9e4d-9c81916beeea | -20.3303 | -50.195 | 2025-12-06 04:38:00 | NOAA-20 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0cadfb73-34da-379a-92d3-474e8a07708c | -26.41322 | -51.84341 | 2025-12-06 04:38:00 | NOAA-20 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0c05c6f6-ce3b-3e29-9faf-59b4814c7960 | -19.64592 | -56.82987 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d37afde4-1b23-3335-82eb-280f7cf5f172 | -27.10218 | -50.83419 | 2025-12-06 04:38:00 | NOAA-20 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7ff226cd-27e2-3839-a678-8465f71cb138 | -20.31102 | -54.91046 | 2025-12-06 04:38:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cc7031d-eb68-3e97-af13-949956463571 | -20.91224 | -56.38301 | 2025-12-06 04:38:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9d1bff2-f75b-36da-8c0c-0cd07b9f4727 | -27.2882 | -53.05748 | 2025-12-06 04:38:00 | NOAA-20 | PLANALTO | RIO GRANDE DO SUL | Brasil | 4314704 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 63a01175-8ae9-3468-b4b8-be23051c7c84 | -19.64665 | -56.82593 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| dcc9bb8e-9a6f-3bfb-9432-891cd6c27433 | -19.65083 | -56.85925 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8207a231-6764-303d-9b12-b6a9eca5d559 | -19.64899 | -56.8593 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 01e02920-cd1b-3e85-ba02-816182d52649 | -19.6418 | -56.82898 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f51509d2-5161-35e9-95c7-18fc64d8b42c | -22.42878 | -48.5616 | 2025-12-06 04:38:00 | NOAA-20 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4ea90017-09a1-3ad2-9713-1bb7e5b1f944 | -19.65282 | -56.82686 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d6aea106-a3da-3669-98ee-c99a781a7fd6 | -23.43808 | -47.05981 | 2025-12-06 04:38:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| eb2f01b2-a4cc-33cb-8e11-fd6427ff4b0c | -22.73166 | -49.34915 | 2025-12-06 04:38:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e3b9f04-7e2d-3016-8197-0145052e148b | -19.67004 | -56.82647 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 16774c5b-ba41-31f4-979d-abd013aec65f | -20.91716 | -56.37852 | 2025-12-06 04:38:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78b6b4ed-650d-36a3-ae77-8d3d00ff780b | -25.33617 | -49.87619 | 2025-12-06 04:38:00 | NOAA-20 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 47b4ec87-e9ce-3e03-82d3-738fbee177a2 | -20.91373 | -49.24042 | 2025-12-06 04:38:00 | NOAA-20 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3f6806d1-3ed2-362d-9d21-890507fe0d53 | -20.48382 | -55.079 | 2025-12-06 04:38:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29946a02-5a30-39da-83b3-fe96dc3b598a | -25.32918 | -49.87506 | 2025-12-06 04:38:00 | NOAA-20 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8f6304d8-3b70-3752-8ddc-1ca76461237e | -24.16683 | -49.58047 | 2025-12-06 04:38:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0f00006-a71a-38bd-b7e0-130f246e7ad9 | -22.89894 | -47.1922 | 2025-12-06 04:38:00 | NOAA-20 | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c981342a-de4e-381a-bab2-1de1c90317f4 | -24.16334 | -49.57985 | 2025-12-06 04:38:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b29cffb5-f262-3d01-a526-0e8b93780594 | -20.91717 | -49.24097 | 2025-12-06 04:38:00 | NOAA-20 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 847359b5-c7e8-358e-8506-26904bab7129 | -27.44694 | -50.34761 | 2025-12-06 04:38:00 | NOAA-20 | PONTE ALTA | SANTA CATARINA | Brasil | 4213302 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d5ba7a05-b5fb-3f61-94ca-d49008826e6d | -23.59075 | -46.3528 | 2025-12-06 04:38:00 | NOAA-20 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 46a85bff-e8fd-329f-99f1-3b780048a42c | -25.33558 | -49.88042 | 2025-12-06 04:38:00 | NOAA-20 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 762ace47-dd0c-36ca-95dc-9a83564dee14 | -20.91422 | -56.37239 | 2025-12-06 04:38:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bc24abe-4963-3570-8ccb-2d3faecf2e64 | -19.66593 | -56.82558 | 2025-12-06 04:38:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1a257231-1ffc-38b6-b7ca-449b5cc87603 | -28.16675 | -55.26934 | 2025-12-06 04:40:00 | NOAA-20 | SÃO NICOLAU | RIO GRANDE DO SUL | Brasil | 4319208 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| defc0d28-b0fc-311e-bb71-3a451aa36ae6 | -29.56043 | -49.9139 | 2025-12-06 04:40:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 23e5bc08-d63f-34cf-9711-3e23d50f5811 | -28.16627 | -49.05951 | 2025-12-06 04:40:00 | NOAA-20 | ARMAZÉM | SANTA CATARINA | Brasil | 4201505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b20c63c7-8d78-3fdf-a82d-01d357c4b75e | -28.17016 | -55.27007 | 2025-12-06 04:40:00 | NOAA-20 | SÃO NICOLAU | RIO GRANDE DO SUL | Brasil | 4319208 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| 68828926-996b-3b82-bc3d-3c869c83d1e0 | -29.07436 | -52.1754 | 2025-12-06 04:40:00 | NOAA-20 | PUTINGA | RIO GRANDE DO SUL | Brasil | 4315206 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0ec3fcf9-83b2-3147-821b-b09c55b7544f | -29.92476 | -51.21258 | 2025-12-06 04:40:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| 376f6e94-2dec-3816-b07f-e8795cb2415c | -29.5598 | -49.91872 | 2025-12-06 04:40:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 171d175b-2ff3-3d95-b541-5b576c26e83c | -29.56344 | -49.91934 | 2025-12-06 04:40:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| e5f70037-dc3c-30f3-8aff-776a3a2b3092 | 2.7983 | -61.0916 | 2025-12-06 05:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 0adce7bd-8f43-35f5-9980-31dabbce7bba | 2.7982 | -61.1105 | 2025-12-06 05:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 34f01f4c-f298-339f-8fd8-b5bafa117e9e | 3.50046 | -51.24682 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 692787d1-bb94-31bc-bbec-cb854cbc9c80 | 3.41751 | -51.25716 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1026ffe9-d4b5-385f-a23e-730e405be341 | 3.46682 | -51.23895 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 347b499d-6487-3103-b5b1-81dba35a635a | 3.45372 | -51.24611 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a27a0644-a139-36c1-9932-ae7b5fabca6a | 3.50588 | -51.25085 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 27532390-6b43-339b-b4a6-9afa88d54fe1 | 3.40906 | -51.26352 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0fa598ec-cf2d-3410-8d59-401d3eb8c007 | 2.18417 | -55.77698 | 2025-12-06 05:20:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ece9c56a-204c-372b-8d02-9579dccaec7c | 3.98349 | -51.6813 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 551263f9-dca4-30ef-8711-e7e75ce3c8a0 | 2.52885 | -50.84308 | 2025-12-06 05:20:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67c11b7c-1143-358a-b6df-eceacbaf8b4e | 3.50667 | -51.25563 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3034bf8e-80a0-324f-99e5-9fba54f52c0e | 3.42213 | -51.25638 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4a1bc550-5af3-3313-b700-a92e0f442406 | 3.50747 | -51.26043 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ff2a2a8-1c08-3139-b13e-e3b3c79bde37 | 3.40985 | -51.26832 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 79554582-82f9-3cf7-baf6-e530bf4d13df | 3.42676 | -51.25562 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68b37f9c-538e-3b9b-8a9a-9d8a6150ced2 | 3.48609 | -51.24063 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| deead488-1a7e-3885-aa85-d852c8142c23 | 3.49504 | -51.24281 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b31f98f-e966-38b9-bc88-7ef914f5fab7 | 3.98444 | -51.67952 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67eed067-0b9b-3ace-91ad-ac1b17b01bdd | 3.45449 | -51.25093 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b6f987d-5cb2-3f6d-ae11-fb8195111583 | 3.45834 | -51.24533 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8de84fc5-0319-31cd-90bc-97b5309094ee | 3.41368 | -51.26274 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fa2cbbc1-6086-364b-ba56-a570f2ae4d93 | 3.44987 | -51.25171 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3b38200b-7463-3556-b33f-d1f6dccd3d6c | 3.40523 | -51.2691 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e652849-d531-3107-a169-531d82487b62 | 3.45065 | -51.25652 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22057e43-0e29-370b-a001-1618f04ef3fa | 3.46219 | -51.23973 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59551531-9f5c-3c15-9531-faac6d01ab67 | 3.48685 | -51.24544 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a9e3d22-49d7-382a-89e5-cd227c4522a1 | 3.46569 | -51.23785 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9d62ffc-df21-3b20-bfd7-7098c1839aea | 3.49042 | -51.24358 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 03c62f13-7a30-3fd2-b5d6-33a2aa506415 | 3.98515 | -51.68394 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac3fba79-8320-3fa0-b9bc-85af8553babe | 3.4858 | -51.24435 | 2025-12-06 05:20:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f004ec6a-cd02-365d-8fe4-778a6c80ac9c | 1.22879 | -50.90949 | 2025-12-06 05:22:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8006c458-9976-34ee-802f-4189b6d6cb2e | -2.11275 | -53.57881 | 2025-12-06 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12c5c18f-0e48-30ec-a27a-0bb3ba793895 | 1.99336 | -55.69231 | 2025-12-06 05:22:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c93bbd58-1177-3fb3-8365-103f9fedf1fc | -2.10972 | -53.45617 | 2025-12-06 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7d1e0e7-f83d-324d-a52b-8fea7d2b4f71 | -1.37576 | -53.13033 | 2025-12-06 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8aa68bb1-bbc1-30a9-a608-cee06c1b33f6 | 0.44 | -50.92137 | 2025-12-06 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 342e7397-32e7-3f36-9132-e66621316024 | 2.5595 | -60.3103 | 2025-12-06 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README9.md)
