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
| abf1e182-5bf6-3497-81f2-37fd26ffeeb2 | -17.47531 | -48.86855 | 2026-08-19 04:42:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a378d62-47a0-3a60-befc-994221b361dc | -19.7747 | -57.96025 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| bda4c1da-161d-3ee8-9e81-4ad81bdd3c97 | -21.40011 | -45.95135 | 2026-08-19 04:42:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 30aa393b-e4d0-3835-b041-b12e567f5952 | -17.61286 | -54.87012 | 2026-08-19 04:42:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41242229-c1c1-3927-b42f-da36b890c4f5 | -19.07027 | -57.35604 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c44fd5ff-e2bb-385c-a046-fa7e4568edae | -19.77032 | -57.95926 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 3dfcff3f-a579-36d9-b690-a913ef1777e2 | -19.67719 | -45.91365 | 2026-08-19 04:42:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96627e7d-6cf3-3b45-8171-329d77a392cc | -15.89462 | -55.5479 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88ff4d78-b432-32d0-8b30-b23e0c623758 | -17.9366 | -44.42462 | 2026-08-19 04:42:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0fcde23-0363-35af-b794-edf373498465 | -19.06944 | -57.36029 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 37ddc50b-3a15-3e32-a7d6-d51e84bc2613 | -18.58376 | -41.32245 | 2026-08-19 04:42:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 327efbb9-c54a-33f8-82ff-e3aee25b2713 | -20.58283 | -45.91574 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbaa5e1d-98c6-3304-abdf-6fcda020dedd | -20.57636 | -45.9343 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 227e53c3-a77d-37c2-9fae-e64f7fc29bf2 | -21.20094 | -48.52723 | 2026-08-19 04:42:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ad9f0ec6-0cf9-31cb-bd54-05a6ff592f42 | -19.3947 | -46.418 | 2026-08-19 04:42:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2a18536-7c99-366d-ad52-5e202259d186 | -19.73269 | -57.9414 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d8cc3cfb-c154-3078-88bd-17798011629e | -20.28073 | -46.47524 | 2026-08-19 04:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ba58ad5-31aa-328f-b353-dd833ebef87f | -16.2648 | -57.66719 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 40034800-9957-38ff-9a71-1ae738796f63 | -20.57593 | -45.93778 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f7ab4ef-a8f0-3a08-bd34-45962e33de83 | -17.32245 | -54.9233 | 2026-08-19 04:42:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 39e20841-bc4c-3b4b-9ef9-469b0f4eaea8 | -15.87607 | -55.55637 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98d65a3b-9abe-3120-b9a8-42dba745c7a1 | -15.93856 | -55.53627 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6164aa6e-a368-3e9b-9d44-d8d58ec19877 | -18.58278 | -41.33152 | 2026-08-19 04:42:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b24d83fe-5bcf-37a7-a8d3-b5d332177f4b | -19.67317 | -45.91297 | 2026-08-19 04:42:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37a9bb43-b73f-3923-8be7-7ddddba11148 | -19.47913 | -45.97983 | 2026-08-19 04:42:00 | NOAA-20 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be73c4be-9e3f-3e47-811b-a3d2547fb72f | -19.46557 | -44.17691 | 2026-08-19 04:42:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ca24137-394d-330a-b02d-e97453806226 | -21.44813 | -48.51366 | 2026-08-19 04:42:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a88f9c31-95d0-3de1-83a7-e615f970e801 | -19.66965 | -45.90854 | 2026-08-19 04:42:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b689770-5fce-3624-bcde-5f5fbe51a1b0 | -19.74842 | -57.95436 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f47d965c-a4d1-3ae9-8f06-74de129d02af | -16.32227 | -55.38247 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 32ffd4e1-35e7-3ff9-8764-6a1cef31c7e5 | -15.88201 | -55.56993 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8bc5c9f5-a99a-34b2-b2a9-09616e52a592 | -19.76682 | -57.95375 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 2c2e165b-1673-3ac7-80ca-da58384e7c58 | -19.465 | -44.18193 | 2026-08-19 04:42:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4bf05b7-be43-36b1-813f-dbecec0950cb | -17.98857 | -48.54231 | 2026-08-19 04:42:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9383d92f-9212-3e2a-aa22-1f128969dbba | -16.26376 | -57.67247 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 859f3869-ce71-3725-b3ec-5a9ac2fa08c0 | -17.95174 | -44.44481 | 2026-08-19 04:42:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91d100d2-6524-3e64-b7ef-ca80eb556f20 | -21.74737 | -45.00449 | 2026-08-19 04:42:00 | NOAA-20 | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 97b66d79-9937-3054-ab6e-9699b08b0ac9 | -15.89541 | -55.51851 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 951a5724-f1b2-300b-810d-052ec4ea50be | -15.87271 | -55.55178 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ee535ae-0e5b-3d2c-82db-f39653711878 | -20.28608 | -46.46461 | 2026-08-19 04:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a639ac85-4ee4-3909-aa42-c732eb3bccc4 | -20.28535 | -46.47038 | 2026-08-19 04:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 539210db-98cf-301f-8369-1798496bfe7f | -15.91724 | -55.56125 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65f77385-a0be-3830-ae49-275a34ba6322 | -21.5231 | -52.00761 | 2026-08-19 04:42:00 | NOAA-20 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| cc6ed5cd-2b8d-3a6d-a26c-afb16295d93e | -19.73358 | -57.93688 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.3 |
| c5f8f238-7f13-318e-9166-57d611e15816 | -17.60146 | -52.62325 | 2026-08-19 04:42:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d492624-3a49-3ee7-82a7-831782e76f77 | -19.07454 | -57.35696 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8be582c3-fbc4-3dcf-8556-fa671ddd6baf | -21.39741 | -45.95204 | 2026-08-19 04:42:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c4107885-30f3-32dd-a634-82a9cdd84256 | -18.8447 | -47.14335 | 2026-08-19 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75a8a848-c296-3b38-ba85-b5060fd77bb0 | -19.76333 | -57.94825 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| c8cfa9cf-393e-3a14-b1cc-bc686540ff13 | -19.73617 | -57.9469 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d481c048-d4eb-30bb-a778-711f6cad1dc5 | -21.39692 | -45.95591 | 2026-08-19 04:42:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ded0ed3a-4ac0-32aa-9a8b-4c1eefeea089 | -17.60083 | -52.62709 | 2026-08-19 04:42:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f314a10-8255-3f66-b7c8-7b1da42c6407 | -19.76245 | -57.95277 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 8377046e-e1cd-3e43-a28f-12cb52798b27 | -17.45646 | -47.85978 | 2026-08-19 04:42:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddb6150d-fc64-3e91-98e3-094718690385 | -19.05662 | -57.35751 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 59608b41-9b97-3bbd-ae3f-6a17d944bd4c | -19.07537 | -57.3527 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 99cea13c-e11d-376a-90fc-05c01ff053b1 | -22.98109 | -50.02436 | 2026-08-19 04:42:00 | NOAA-20 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 99475b0b-015b-3484-bfdf-ab2a88800958 | -19.07371 | -57.36122 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 866651e4-18a3-3b82-907d-74709700fc34 | -16.26064 | -57.66984 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 883e1497-a50d-37cd-ad62-4084f8c45ebe | -18.67819 | -52.65092 | 2026-08-19 04:42:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1e33c41e-ac13-3b60-9a66-40b9263d861b | -16.24743 | -57.65834 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1b4947d2-d742-3313-adc7-6b3099a1dc34 | -19.06516 | -57.35937 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1b612769-7b9b-3cfd-80a5-5fd9cc218cd0 | -20.18715 | -45.40068 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3b6d00a9-ff2c-35f3-8cad-9913ba404bd0 | -20.48961 | -45.24428 | 2026-08-19 04:42:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f55a2d51-71dd-33c4-8837-3eee24e8ff29 | -19.66613 | -45.90406 | 2026-08-19 04:42:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 70a22232-9133-372d-996a-89a7409bfe38 | -18.58344 | -41.3254 | 2026-08-19 04:42:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 11d7ad68-4b88-3d23-9c41-79a1e7e30e8a | -19.74404 | -57.95338 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9eb2cfae-73c6-3aeb-9c77-0c1e3f81c77b | -20.57679 | -45.93087 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7545d26a-0feb-3264-9cf6-0c32cbb62f2b | -16.07411 | -54.81286 | 2026-08-19 04:42:00 | NOAA-20 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc166e49-c91a-35c6-97b9-f96c657d416c | -19.73885 | -57.93335 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.8 |
| 78305d09-ec03-3ab2-9fac-25bf60f24d8e | -19.67065 | -45.90089 | 2026-08-19 04:42:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4e7ffdf-8f51-306e-b1a2-c2aac20f662f | -19.67366 | -45.90924 | 2026-08-19 04:42:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ab1a675-6c72-3740-a308-9cddc6efa8ce | -15.93388 | -55.53904 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94491873-4a78-3aa9-a92d-e568aa952e81 | -19.73706 | -57.94239 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d5152c69-b567-3c59-a8d0-c1914a2f7cd7 | -17.99145 | -48.54675 | 2026-08-19 04:42:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c98af92f-6d8f-3ae2-89ec-7904e2494a9c | -16.525 | -54.68512 | 2026-08-19 04:42:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ec65451-06f9-37ab-a879-7c02de22bbec | -18.48706 | -47.2492 | 2026-08-19 04:42:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cceaba5-6f6f-3f45-a2db-79d17d607940 | -21.03346 | -51.609 | 2026-08-19 04:42:00 | NOAA-20 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| accc4ae2-1a45-345e-9094-b4501dd90e9d | -21.52369 | -52.0039 | 2026-08-19 04:42:00 | NOAA-20 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 67e3163c-e70d-3bb9-bdb8-f3b036dcb39a | -17.32152 | -54.92841 | 2026-08-19 04:42:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e3e5b1b-5ee2-3f42-bf04-f0f6b3a0be73 | -20.32921 | -42.40419 | 2026-08-19 04:42:00 | NOAA-20 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 920b5b93-a015-3f67-9cd8-ed31e360d0c5 | -20.18668 | -45.40456 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4d0d6cb0-2e63-3f9a-a507-2a972cdd72c1 | -15.88344 | -55.56192 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db9c4435-2666-35f9-bd6f-185c19474f30 | -17.94092 | -44.42527 | 2026-08-19 04:42:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8cc8113-6c1a-388c-a152-a430449b4730 | -15.88272 | -55.56593 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ed6fa88-c6ba-362b-b1a6-b354d7d51849 | -15.89589 | -55.51866 | 2026-08-19 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9664370c-0e5a-3270-871d-81f053cd18bd | -20.32957 | -42.40074 | 2026-08-19 04:42:00 | NOAA-20 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbd5c2b6-1d98-3d3b-91fb-e63c74d90f6a | -19.05485 | -57.3438 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e484d734-0975-31a7-a4ab-7bde3071c02c | -16.26021 | -57.66619 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b8e7d5bd-dd8b-3b46-b396-cac61af4464f | -16.25708 | -57.66339 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| bc587ba5-e72a-3d6b-a8d8-16bb50b51d0c | -16.52119 | -54.68447 | 2026-08-19 04:42:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6abad32-ee32-3497-b869-0687076fd32a | -17.6091 | -54.86928 | 2026-08-19 04:42:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d80bf980-53c3-35c1-8f6b-114c8bd97721 | -20.87798 | -45.29499 | 2026-08-19 04:42:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b2a8224e-3972-39a6-9817-e2271715a701 | -20.57228 | -45.93382 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9d1a62e-e5f8-3fd2-8cb9-77dd3801dd4f | -20.59966 | -45.91394 | 2026-08-19 04:42:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 1b616260-8af8-3637-8ba7-6e5fd1297de3 | -16.25563 | -57.66518 | 2026-08-19 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c3fba1c0-6f35-33e9-81f5-6ad6682ee7dd | -21.1349 | -51.06845 | 2026-08-19 04:42:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 18594eeb-e94f-3cb2-8fdd-9c50d9cd5b0a | -19.73796 | -57.93787 | 2026-08-19 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.8 |
| a31b7041-2b45-3f72-b71e-e3c8a43df499 | -18.4638 | -47.22731 | 2026-08-19 04:42:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8033c172-cdf8-342d-ab41-61cefde2be2e | -24.76579 | -49.08476 | 2026-08-19 04:44:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README48.md)
