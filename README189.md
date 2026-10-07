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

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79718499-b515-38a7-8c9e-3163f855c65a | -7.90494 | -54.71911 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| aedd2969-54f2-3a23-b738-e5d86c7b9043 | -5.44583 | -47.52818 | 2026-10-07 16:37:00 | NPP-375 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1181bdd4-8acf-3a3f-94de-55ed7cbbd8af | -16.05851 | -39.84556 | 2026-10-07 16:37:00 | NPP-375 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 50ff5d8a-b786-394f-a703-f5abc6c7e507 | -3.87204 | -44.12601 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b06a219a-df26-3dab-8ea5-593c79eba371 | -10.38031 | -46.25059 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 18ea7472-fd0c-3d58-95d0-804c9f7ecda3 | -6.14999 | -52.64996 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7aa75ac7-9f3c-3305-b839-6ebc5c65be4a | -8.919 | -44.54873 | 2026-10-07 16:37:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c9edc84-7a8c-3cc5-8338-43568e350403 | -4.76843 | -49.38511 | 2026-10-07 16:37:00 | NPP-375 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5e5051ff-3beb-30e3-b537-365f87b660ff | -6.07634 | -44.38954 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d0a632a3-49d6-38dd-a50d-ebfae82b65e8 | -6.81225 | -55.29378 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f962413a-4dd3-3719-9315-863cb367f6c3 | -9.40536 | -36.68514 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b764ec14-12ce-3b21-94c5-dcc2a3dba765 | -10.88196 | -46.68342 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 037edd42-c095-3f43-b35c-59af91fb66ea | -5.3375 | -48.55403 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d77c01d0-4869-3bea-8a6a-16f16b6c56a1 | -4.5272 | -43.72873 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e2747beb-a509-3cd1-bcfa-aab48a3ff89a | -6.33768 | -43.82286 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 21fceb1d-d727-3d9a-b472-b406da805ddb | -5.84436 | -44.22098 | 2026-10-07 16:37:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89a461e3-25cb-346f-bbb4-1205f5a1b294 | -6.79878 | -41.24372 | 2026-10-07 16:37:00 | NPP-375 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e2df850c-ab57-319d-a8b0-4436057911b5 | -5.97126 | -40.9386 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 1fce0587-12a2-3165-9527-9c76e3117c06 | -7.17121 | -47.79259 | 2026-10-07 16:37:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 488ff1e8-5416-35b3-ac9f-210bd85770a3 | -8.76353 | -47.57896 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 17d039ca-76b8-3ccf-998a-ee111015c389 | -7.87665 | -54.9754 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d42e641c-0dfb-36cc-823e-853cbbeac81f | -5.46763 | -45.68668 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5842d914-a8d9-3423-b45b-cca6ff38b3b1 | -5.84772 | -42.65924 | 2026-10-07 16:37:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 130.9 |
| cf9d00b1-3776-3fb9-87c3-e20ad0b9554d | -5.10132 | -47.43925 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5bc86ee6-5c4f-3398-bfe6-0d902c284a85 | -7.71663 | -49.97684 | 2026-10-07 16:37:00 | NPP-375 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 87f188d7-9bf0-3be9-8608-768d556bcdaa | -7.19933 | -55.11857 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e80dce2a-7e13-3955-9b04-2a25ebc35d8b | -6.90984 | -47.393 | 2026-10-07 16:37:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7b3b730d-89a7-3481-b6d1-01c467b6228c | -3.22881 | -40.03071 | 2026-10-07 16:37:00 | NPP-375 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 28.2 |
| aaf00fba-8bae-37f9-a352-4c85c8de5188 | -11.05641 | -45.85696 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 036b84c7-1e5b-3b63-ac93-811138ad2f50 | -11.09732 | -47.62889 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1fc579d8-dbe6-380c-b91b-8d7a05e77b7f | -6.50622 | -41.83075 | 2026-10-07 16:37:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e1122127-9394-35d5-8f66-ffff2d3617a4 | -4.20804 | -44.61831 | 2026-10-07 16:37:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 831037d8-be82-39e7-be91-801851e42ab3 | -15.79781 | -43.27444 | 2026-10-07 16:37:00 | NPP-375 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7959c5d3-8104-36af-b272-fb13f1ae9161 | -4.02706 | -42.84791 | 2026-10-07 16:37:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 6.9 |
| eac27797-cd72-318a-9e2d-23a97cdedf67 | -10.86511 | -50.68264 | 2026-10-07 16:37:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c3c1d6ea-db2f-3fee-8bcc-f51466515a7a | -3.75008 | -41.70758 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 13db0be1-457e-3fb8-94fc-56daabcc945d | -8.3911 | -48.0782 | 2026-10-07 16:37:00 | NPP-375 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 62d213d8-5b22-3711-9ee5-6f17451b2af5 | -3.7702 | -41.77967 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 44.3 |
| 21df5839-e949-3431-8e3e-458ac8342acf | -10.94153 | -45.38609 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| af6d1dc0-b4de-337e-bba5-7f24e400763f | -16.35588 | -42.00505 | 2026-10-07 16:37:00 | NPP-375 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| ada03751-22cf-3fff-9fde-71872563d636 | -5.58939 | -47.26264 | 2026-10-07 16:37:00 | NPP-375 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ea74035f-aa37-3fd7-80a2-d183af2ac12e | -5.73057 | -41.74186 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 824301f2-74a0-3944-bff6-23009c29208e | -7.77331 | -43.81718 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| ae0fb749-f108-3205-9824-c2ed6785898a | -5.71808 | -41.66358 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0824302b-305a-374a-894e-1f4efaf5da5e | -14.93339 | -41.1031 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 86a5779e-7d63-35ff-a2da-ee158fa62b91 | -6.31289 | -53.30581 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5952b34d-c436-353b-8393-8e219323ec56 | -15.51394 | -40.60445 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| bdc934f7-a4d7-3b99-a582-fd5c9a2acfc9 | -7.17499 | -47.79211 | 2026-10-07 16:37:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 96900f45-fd11-318f-a5a5-5e8048141103 | -5.87633 | -57.67365 | 2026-10-07 16:37:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6db668eb-6158-3b49-9f56-92e17d997558 | -6.73348 | -55.12695 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 1146c344-c0e3-38ad-bced-6f7592d85a7c | -4.09754 | -43.28285 | 2026-10-07 16:37:00 | NPP-375 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7978750-bea4-3ed7-bcaa-87f3b4ff0657 | -9.80333 | -48.92144 | 2026-10-07 16:37:00 | NPP-375 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 46fbd396-abfd-3d2d-a8da-fa8daf00784c | -8.83541 | -45.81809 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c93af16f-d816-3087-b8f9-ae1222533cee | -4.59083 | -40.29459 | 2026-10-07 16:37:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f90beb23-1f02-3e87-bc55-680aaf6df064 | -7.87576 | -39.9073 | 2026-10-07 16:37:00 | NPP-375 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 30.6 |
| db532942-56a6-3275-a7cb-55f1927ec067 | -10.37382 | -45.02635 | 2026-10-07 16:37:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6b841612-7c5a-3dd6-9b49-830b7ffd05bc | -6.0242 | -51.71775 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78bb30a7-de14-32f8-acda-933cc6cd0bcf | -9.76869 | -48.32954 | 2026-10-07 16:37:00 | NPP-375 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9e8536bc-e92a-398b-a9d6-3956e99e39cc | -9.95706 | -45.96455 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a07f850f-a4bd-36dd-a35b-166609422d4d | -17.44242 | -44.72212 | 2026-10-07 16:37:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c7d64439-8041-3341-b14e-344fe28c7aee | -9.86406 | -45.74733 | 2026-10-07 16:37:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3a608b90-34a4-3a2a-be60-87f0d69dbcc2 | -6.14641 | -53.4807 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b803e6c9-4831-338c-94cb-b74d0fdd0a9f | -4.28416 | -50.78461 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| db78854e-3b05-3c73-98e4-e5b544bb49de | -10.35089 | -46.25077 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| a8c375f1-9856-36b5-997a-9e4c47fc0f0b | -6.85786 | -43.8854 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| edc83d93-4b78-34b9-adad-37cbdf1a0df1 | -15.66961 | -39.70395 | 2026-10-07 16:37:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 06377e2a-a997-3df5-b95d-b56600d44421 | -5.73471 | -41.74523 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a3a4dcc5-d6ed-3e15-bdb2-40ca5ea92641 | -5.95357 | -43.87646 | 2026-10-07 16:37:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9b6b2b62-e351-355c-baab-053116f68fff | -6.2612 | -52.8625 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 54206722-1a13-317f-b8ce-05a2fe948d83 | -4.85055 | -43.36435 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f43f45cc-ddc8-3fe2-aef8-2cb7fe46e7f0 | -9.97198 | -43.55922 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d40c58e5-1c65-34d9-8bc1-97b5776b93dd | -7.92741 | -54.74888 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c5c83baf-f3cb-3f32-bdda-1cd93ee62347 | -17.28157 | -43.89844 | 2026-10-07 16:37:00 | NPP-375 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c3afdcd9-ec65-324d-b2a5-e75a203a6ce3 | -10.33946 | -46.24806 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6eeec1cd-1b8e-39ed-b504-4a002c449607 | -4.96551 | -40.56635 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 42f654de-fb19-3b40-abc5-3b846d32d9af | -4.93417 | -45.10673 | 2026-10-07 16:37:00 | NPP-375 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b0839c81-dce9-3f73-8129-ff0e23d7d62e | -7.59166 | -55.73654 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 111411ea-a9ee-3ec1-9b8e-824a12420190 | -15.11112 | -43.63015 | 2026-10-07 16:37:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 47.6 |
| f43ce6a6-80ec-3300-acd7-b7dacd63a39e | -6.2472 | -52.83876 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f825a0ef-dba4-3791-bafb-8765e5c363bd | -3.66754 | -41.43968 | 2026-10-07 16:37:00 | NPP-375 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a929b965-9a46-3d8e-a8c1-405b64a05425 | -5.97593 | -43.73436 | 2026-10-07 16:37:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b7f4a7d1-bbe1-31c8-ae85-5d3408d119fe | -8.14773 | -39.70215 | 2026-10-07 16:37:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 0eee6202-f518-3411-983c-49565a7f275d | -6.03023 | -43.76134 | 2026-10-07 16:37:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 937823e0-000c-3505-90da-d49cc42091d3 | -8.76566 | -44.16064 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f6ceba1c-916f-3c1e-b76a-e30d814a31f4 | -6.15248 | -52.65057 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 90a4bb6e-695e-34e0-b4d8-3aaca8d64a12 | -3.3326 | -44.47005 | 2026-10-07 16:37:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b856a14b-5816-3944-83f6-8b23f4945bc2 | -16.05634 | -39.85394 | 2026-10-07 16:37:00 | NPP-375 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 6554037c-58ce-3aca-a4a6-8d93b31f0b99 | -5.45701 | -45.59285 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 14687cfd-069c-3138-9b08-e501c6feb885 | -7.47228 | -42.82643 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 3d728312-53dc-3032-812e-2979bbeec4f1 | -9.80848 | -44.78385 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| eb8a44e2-d979-3ad6-9ad1-838c5d453baf | -8.06937 | -55.30137 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| ddf982c5-d373-3cd5-ab8f-bdc7572a7ab0 | -5.74075 | -53.46112 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 53e819c6-dea2-376e-8985-ab2095628c68 | -3.80542 | -40.46099 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 8cf71b09-1aba-3b08-860b-fbc740e6eb62 | -8.10549 | -47.12501 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6db72624-a85d-3565-a4fc-d02add195e36 | -5.33787 | -46.19487 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cd64a091-2f95-3d3b-8bd4-ead6d608bd79 | -16.12299 | -42.23202 | 2026-10-07 16:37:00 | NPP-375 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 39b69ece-4fb0-378b-a373-5e9807decce6 | -7.03154 | -45.4251 | 2026-10-07 16:37:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| baa70fe6-a8b5-311a-922f-732ce1b68e74 | -5.55246 | -45.62203 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| f6bdc5e3-b85b-334b-8b45-946270c38eed | -3.90146 | -44.11797 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 39e15bdd-c97c-3e4e-8972-50636ee966ea | -6.9451 | -45.2644 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README190.md)
