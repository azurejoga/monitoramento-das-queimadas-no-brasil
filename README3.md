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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ba680e3-db7c-3f8c-a479-f0b52c95a8a2 | -23.56691 | -51.72933 | 2026-04-22 04:19:00 | NOAA-21 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d6041a4d-547e-30f3-9e34-ba7549378619 | -23.54123 | -47.63211 | 2026-04-22 04:19:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5298e308-fb11-3135-a965-238151a10174 | -25.26677 | -49.281 | 2026-04-22 04:19:00 | NOAA-21 | ALMIRANTE TAMANDARÉ | PARANÁ | Brasil | 4100400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7a062721-d6d5-3829-84f6-d757fd31b665 | -15.88771 | -47.94962 | 2026-04-22 04:19:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 067ac8ba-5a01-34f1-b4a6-8c7589b23792 | -23.56561 | -51.72688 | 2026-04-22 04:19:00 | NOAA-21 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 11c3cb41-1740-379f-b216-81c52440a6cc | -22.68385 | -50.95562 | 2026-04-22 04:19:00 | NOAA-21 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 78d7e5cc-40fd-3140-9184-298329b7acec | -22.68472 | -50.95081 | 2026-04-22 04:19:00 | NOAA-21 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c09c297c-c58e-3410-bcd9-889ffa310b6c | -22.93367 | -47.17374 | 2026-04-22 04:19:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9b9c6dcc-71dd-38aa-b79c-03a5d1428c76 | -17.16971 | -46.83364 | 2026-04-22 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 919aaae3-dcf4-3235-a0b0-9c795d0fb594 | -25.81801 | -50.8641 | 2026-04-22 04:19:00 | NOAA-21 | MALLET | PARANÁ | Brasil | 4113908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a6d00f9b-81dc-3179-a8bb-2c2f54a07c9d | -26.78825 | -48.67162 | 2026-04-22 04:19:00 | NOAA-21 | PENHA | SANTA CATARINA | Brasil | 4212502 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4abaf0f3-8994-3206-bd86-35d6f2cdcaaa | -26.79642 | -50.40257 | 2026-04-22 04:19:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3b96f178-3834-3139-859a-eada7189ae1e | -23.64926 | -47.99969 | 2026-04-22 04:19:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1ed0c80-9e4b-338c-a0d8-1b7076e3b903 | -22.34513 | -48.97248 | 2026-04-22 04:19:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9795a669-e35f-3674-9ff1-fa1b8cfe2613 | -27.95411 | -51.06772 | 2026-04-22 04:19:00 | NOAA-21 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 73aa0a31-29e5-3e75-9ebf-1a2bc716768b | -17.91601 | -44.41047 | 2026-04-22 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddacf5ee-8203-30a9-a350-a75582c09f9f | -28.17678 | -50.05931 | 2026-04-22 04:19:00 | NOAA-21 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 96de66b8-fead-38d4-8603-e86810d3f58a | -24.93134 | -50.77735 | 2026-04-22 04:19:00 | NOAA-21 | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5f9ea030-5ab0-36dd-8e0f-6b7854214d42 | -26.89869 | -49.62433 | 2026-04-22 04:19:00 | NOAA-21 | JOSÉ BOITEUX | SANTA CATARINA | Brasil | 4209151 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 491e7f17-f100-3fa4-a815-68a0b5389c9c | -13.99038 | -56.65907 | 2026-04-22 04:19:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a327cae4-2022-317d-b137-dfc9dae57495 | -26.21689 | -52.33649 | 2026-04-22 04:19:00 | NOAA-21 | HONÓRIO SERPA | PARANÁ | Brasil | 4109658 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 86682d40-fed3-3ff6-8eac-218cdf3331a5 | -26.82806 | -50.48886 | 2026-04-22 04:19:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40bba6cc-5a4b-348d-bf73-dbe9cd2d6270 | -12.05134 | -45.33562 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 986b0838-808c-3aa8-b900-f5817ac7a50c | -12.30404 | -57.17949 | 2026-04-22 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9563c708-f04b-354c-8270-f79ecb2e606d | -12.8553 | -43.77768 | 2026-04-22 04:46:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4403b9c-4658-3b68-9005-e94e9b16d8ec | -12.50282 | -54.76279 | 2026-04-22 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bc0f711e-5494-3a22-8209-54de985f0c52 | -13.38224 | -45.33389 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d35baa61-93c3-385c-8014-eb7e9e8366e9 | -11.61189 | -47.10509 | 2026-04-22 04:46:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d4e6e21-3b1c-36e9-a9e0-f63e52340dce | -11.77151 | -43.65415 | 2026-04-22 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 39cd487f-4e21-3154-8207-3d13f3391561 | -12.01485 | -45.2283 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f2808f8-ae1d-399a-a2f6-a609278cb3bb | -12.01391 | -45.22937 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| badef388-c55e-381a-bcbb-3c3466fccc4f | -11.90845 | -43.84324 | 2026-04-22 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f235ea8b-7af6-3fee-80be-dfd1a2f54c2e | -11.77085 | -43.65909 | 2026-04-22 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ad191087-e336-36a9-a3f3-939bb03d48ad | -12.00917 | -45.23265 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 861b2555-eabd-3af4-97f5-03b25a2e36a7 | -12.34981 | -54.77259 | 2026-04-22 04:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 281caf0d-6907-31c4-98d2-6de5b88b045c | -13.3828 | -45.32989 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59cbaea2-c970-3efd-b571-65fd254a985d | -13.38593 | -45.3385 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81ed7f3f-2d0a-38b5-af84-c5e992335abf | -12.28598 | -44.62931 | 2026-04-22 04:46:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d14183b-aaed-3c53-8f3b-6a3aa2ead781 | -12.01956 | -45.22503 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8332e10-d30b-3e16-967e-66ab431b68f0 | -12.63695 | -52.14535 | 2026-04-22 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f45a0f25-864b-3a49-8df3-c2de85db1fd1 | -11.77615 | -43.65484 | 2026-04-22 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50a955c4-2f8b-3e95-89b7-3fbf9f9daf10 | -12.64031 | -52.14591 | 2026-04-22 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bfd9e14-d6a3-3824-8b07-9a6267c78fa2 | -12.01865 | -45.22609 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f7455cc-86d0-3aab-b5fc-0ffedfaafb87 | -12.02795 | -45.22624 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b8f3ee9-7523-30ef-83f3-abcdeb14e50f | -13.38977 | -45.33341 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a16d472-0479-3809-aa81-c136b3f46cec | -11.77682 | -43.64991 | 2026-04-22 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1859ebc3-afdd-37b7-bdc8-e635dc8352dd | -13.63461 | -44.44282 | 2026-04-22 04:46:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07a28822-30fd-3868-81b4-b55cf439fd49 | -13.39073 | -45.33509 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c0c61db-a524-36ff-b874-5e486b7bff0e | -12.85318 | -43.77579 | 2026-04-22 04:46:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77de85e5-750b-3a1e-a073-70beb2a62f62 | -13.39017 | -45.3391 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2600ff99-8315-39d0-a978-66e493a68edf | -11.97472 | -43.83809 | 2026-04-22 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a23b87a6-a8e0-33bd-905f-9ef60e654b21 | -13.38925 | -45.33742 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd203c1f-711c-30bd-a273-751f7c6d9a0c | -12.02376 | -45.22563 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27d212d1-721a-34a1-8975-ab8728728f6d | -11.77218 | -43.64923 | 2026-04-22 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 663cb30e-00b0-3489-bb0f-75129c5d63a9 | -11.90782 | -43.84799 | 2026-04-22 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f9c6f4f-a5d3-3105-bd1c-1cc5b3af58d6 | -12.05186 | -45.33183 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c855b807-2ed8-30a2-92f8-8ddc0004a8da | -13.37745 | -45.3373 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ae7ecb9-8b2c-3178-9fc4-386456d87836 | -11.99711 | -47.77212 | 2026-04-22 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1de811a-d43e-3af9-80c3-f3ffe0178d3d | -12.0181 | -45.22998 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea705acf-6db7-3eb1-839c-3583dfae5477 | -11.99773 | -47.76791 | 2026-04-22 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7acae0f-d3c7-3f93-8276-62a9da5bcbbe | -11.77549 | -43.65977 | 2026-04-22 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 89166514-baa4-34be-9546-df2a0aa9a2e9 | -12.30327 | -57.18368 | 2026-04-22 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9195a088-3b57-3ef5-9f14-6c7fb7a76dbe | -11.77284 | -43.6443 | 2026-04-22 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28e2a2eb-8278-3af8-ac18-f10a37590dbd | -12.01014 | -45.23158 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3120a23-c5c9-3a00-a17f-d4e215953d53 | -13.91014 | -47.38994 | 2026-04-22 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddfe095d-912c-37b9-a241-4cdfc9062fcb | -11.76753 | -43.64854 | 2026-04-22 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d126c4f-7056-3203-afe1-d35a63caf151 | -11.97407 | -43.84289 | 2026-04-22 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c6d3f98-8d75-3540-9f43-68bc75eb2c49 | -12.63754 | -52.14173 | 2026-04-22 04:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30a9ff3c-7acc-36ef-9aaa-994741559eab | -13.38169 | -45.3379 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2614038-6e94-3322-92ff-f868d29361da | -12.01904 | -45.22891 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73035120-7a93-3452-b038-5aa6373a12d0 | -11.78079 | -43.65554 | 2026-04-22 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 827e7ca3-3a8a-3c05-ae34-1dbedca672e0 | -11.9965 | -47.77632 | 2026-04-22 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da9ff98c-45a0-341b-bdde-d557db28d8dd | -13.21061 | -43.68711 | 2026-04-22 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 650df751-bb98-3e61-9332-877fa8a8a7b1 | -13.378 | -45.33329 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4263d252-c85a-30a7-bc15-4f475546b30d | -13.38114 | -45.34191 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d8fd2a8-505a-34a8-93af-a3091cf1cc3e | -12.02323 | -45.22952 | 2026-04-22 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e4bbcc7-4bb2-384a-93ce-1e8ce008b62d | -11.76687 | -43.65347 | 2026-04-22 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d524e293-8a6b-318d-81b8-06736ea8b7f2 | -13.38649 | -45.33449 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f87cc1e-a39a-3529-8d79-931ba7424863 | -12.28159 | -44.62877 | 2026-04-22 04:46:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af0f6b5d-36db-3854-8f28-33a6f8194c15 | -13.38704 | -45.33048 | 2026-04-22 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f91444f9-5a37-3a70-aaaf-4327e86f0392 | -13.9895 | -56.6432 | 2026-04-22 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f723b1af-facf-3d15-9e8d-a7940363eddd | -16.50639 | -52.81378 | 2026-04-22 04:49:00 | NPP-375D | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 63b7e5b6-b328-3c6e-81fe-de75da657239 | -21.5316 | -48.89805 | 2026-04-22 04:49:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c2ecf97b-4288-3e35-b259-86d16c6f0ec9 | -18.40315 | -51.4353 | 2026-04-22 04:49:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b70340f1-e174-347b-b1da-f2c244a4acda | -13.24587 | -53.28993 | 2026-04-22 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d78e162b-5281-3531-adf6-1dc43e384dc5 | -18.48528 | -51.67224 | 2026-04-22 04:49:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59305269-8493-39e9-8139-79ccbd482c72 | -21.53096 | -48.90291 | 2026-04-22 04:49:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 435e8797-6602-3ca6-b3df-95c05f921946 | -14.49841 | -47.77029 | 2026-04-22 04:49:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b490fcb2-de06-3156-b7e7-af47b3d967d7 | -20.86032 | -48.6174 | 2026-04-22 04:49:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0568d289-7445-33dc-8d53-28a9c990199a | -13.9875 | -56.66283 | 2026-04-22 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7033793f-b158-3e87-97b2-95231322c93e | -17.16808 | -46.83504 | 2026-04-22 04:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dcfd5b40-5b3e-3af2-b719-76e7a156a09d | -13.98675 | -56.65813 | 2026-04-22 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b47dfef9-f522-36b2-92c9-4bfe67b320df | -18.40707 | -51.43216 | 2026-04-22 04:49:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28fb7356-154a-3220-8fff-928edf24053f | -13.98881 | -56.64694 | 2026-04-22 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55a0908f-2934-31af-8bb0-fccc38b345db | -20.15715 | -50.98759 | 2026-04-22 04:49:00 | NPP-375D | RUBINÉIA | SÃO PAULO | Brasil | 3544509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 844e93a9-e48a-34aa-8e9d-43ac1f96e91d | -19.37207 | -50.908 | 2026-04-22 04:49:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2457813f-cd5d-3702-85f1-fbc79b6e9f1a | -16.93766 | -49.29276 | 2026-04-22 04:49:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8056f4d9-0d2a-3113-a4f2-052c4f8f268c | -14.49469 | -47.76983 | 2026-04-22 04:49:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7be88616-6ce7-3578-9910-1b4f4079b9ff | -13.98816 | -56.6591 | 2026-04-22 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7f00657-0abd-3198-a6cf-d11fe694954b | -13.24523 | -53.2938 | 2026-04-22 04:49:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)
