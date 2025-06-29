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
| da9055b1-209d-3eb8-8703-c35b4c98fe5e | -15.72763 | -49.55103 | 2025-06-29 04:12:00 | NPP-375D | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e3e86d1-e6a7-355b-9227-d9dafca0e296 | -17.39583 | -42.629 | 2025-06-29 04:12:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0fca1bbb-65f2-3fc4-9000-ba5a77a9c30a | -19.68202 | -45.3799 | 2025-06-29 04:12:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab33b458-5806-3ce5-8ade-9b899f7ebd34 | -13.01562 | -53.42106 | 2025-06-29 04:12:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 831f0ff5-1621-3a08-9974-0ab89acc6d6f | -17.75262 | -42.89316 | 2025-06-29 04:12:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5956ae6a-fb78-3acb-afa6-a5714b7d5a71 | -14.21614 | -45.50504 | 2025-06-29 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15091c40-ee6f-3dfc-9949-d0ce86ecf1cb | -12.61504 | -54.21155 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61e37ef3-2d92-360e-a8b6-b10aa718d36a | -14.03429 | -54.48253 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49297270-7d2f-32f3-8bb7-066a521a3769 | -14.2196 | -45.50565 | 2025-06-29 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39776f41-0769-39b2-bffd-ff58df735edc | -14.30428 | -46.93378 | 2025-06-29 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae27086d-e67c-387f-8675-d3854850cde9 | -17.06658 | -43.72649 | 2025-06-29 04:12:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c88e7c0-9991-3732-b0fe-6f568a83878e | -12.62015 | -54.21141 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 72db01eb-aaf0-3549-a659-a4ff6d877207 | -14.48503 | -46.51122 | 2025-06-29 04:12:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab764938-940e-3f79-80d1-0420042900f8 | -14.88361 | -48.3884 | 2025-06-29 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a0fdc51-bccb-327c-8bcd-d0e56486069a | -17.40261 | -42.63011 | 2025-06-29 04:12:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 456f504d-985b-3850-ad12-30acea4af610 | -15.65047 | -49.72923 | 2025-06-29 04:12:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9930fa27-cd88-3540-a8c0-3497ab2f8a78 | -14.21451 | -45.5059 | 2025-06-29 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f67c6b7-7419-31de-bfe3-5cad0223746f | -14.89254 | -48.40742 | 2025-06-29 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc9105b9-1d27-3476-8634-532862c5ed87 | -18.78595 | -52.58705 | 2025-06-29 04:12:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c72f3084-848f-3b70-8cb2-b97501724d20 | -17.76199 | -52.4454 | 2025-06-29 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4afb1da9-5a45-319f-8db0-5ab23b3560e3 | -14.69268 | -53.38967 | 2025-06-29 04:12:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4201aede-be54-34e7-b595-dd4cc1072a3c | -15.34062 | -49.13389 | 2025-06-29 04:12:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1efe27b-5c83-332b-958a-b07c02cfb4b2 | -13.10424 | -52.29551 | 2025-06-29 04:12:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a51a4f53-f2e8-3fca-9e1e-77e445f4225d | -17.59483 | -43.19757 | 2025-06-29 04:12:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b9fa0a9-6722-3d49-a89f-debb86261c0b | -13.95151 | -54.49245 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47db9f88-9313-3c36-9ee1-7d6dfc08b5b1 | -14.23968 | -45.51318 | 2025-06-29 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d59f4456-ca46-3d8e-8040-78fd4011678e | -19.52423 | -43.37265 | 2025-06-29 04:12:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20623969-e6af-3acb-9261-6dc79bf1dfd2 | -19.5276 | -43.37323 | 2025-06-29 04:12:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee025b01-27c9-38f6-92c4-e133da9a4431 | -16.16247 | -45.68701 | 2025-06-29 04:12:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 559774cb-fa64-3b4f-80ca-680918eb724c | -18.79079 | -52.58807 | 2025-06-29 04:12:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1a4288e9-ed1a-350f-a2f3-dfbfb0a5233f | -17.09398 | -43.80533 | 2025-06-29 04:12:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1f1a782-c898-3648-b298-bcfc907a3357 | -14.88762 | -48.38888 | 2025-06-29 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa572b13-94e3-304d-8c39-ca2838596699 | -15.7269 | -49.55494 | 2025-06-29 04:12:00 | NPP-375D | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fcfda54-dcde-3468-a053-9395da4a995b | -16.90994 | -43.88178 | 2025-06-29 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b501986-96f7-3f19-878c-d7e0aa25eba1 | -12.62614 | -54.21267 | 2025-06-29 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c809e5f6-b064-3757-8592-706f230320ca | -20.25207 | -46.73176 | 2025-06-29 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f174e8c9-82fc-3300-b71c-7d2aca8c16bf | -23.59399 | -47.43912 | 2025-06-29 04:14:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f4c2668-abdb-3d5e-998f-2fdfa38e6122 | -22.54036 | -48.81549 | 2025-06-29 04:14:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e3e75a0-3eac-3c69-b81d-ebc1a72d64a2 | -23.40541 | -46.55637 | 2025-06-29 04:14:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 23f5e508-a93d-3d6d-a6db-7aa0a8929ec3 | -23.15989 | -48.33809 | 2025-06-29 04:14:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2eff575e-355c-302b-a872-9c9bd611b899 | -23.30606 | -46.5022 | 2025-06-29 04:14:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fef44b59-9634-33ad-8c20-ac2122d0c01d | -21.53759 | -45.46435 | 2025-06-29 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eafeb109-b5b8-3c14-af5d-ce172fcfd77a | -22.40952 | -46.8241 | 2025-06-29 04:14:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eabc070-98c2-313f-a969-a8eb62b35048 | -20.51274 | -49.0492 | 2025-06-29 04:14:00 | NPP-375D | ALTAIR | SÃO PAULO | Brasil | 3500907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 65b2b606-139f-3902-bc69-fea327a0579a | -20.37855 | -45.60263 | 2025-06-29 04:14:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13a76a67-fa16-371c-99e4-49f87448b3ab | -21.53427 | -45.46375 | 2025-06-29 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 263c4cae-b264-398f-8ad9-4bb250b3e574 | -23.45899 | -46.93134 | 2025-06-29 04:14:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 04db0fcc-9e82-3b8b-b3a0-aaf5c60059f5 | -22.90271 | -43.75285 | 2025-06-29 04:14:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 68c423f7-a750-3e96-83fe-795eccd35307 | -21.19267 | -45.06036 | 2025-06-29 04:14:00 | NPP-375D | RIBEIRÃO VERMELHO | MINAS GERAIS | Brasil | 3154705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 15a69781-9f04-3731-91c3-445adad7ab12 | -23.31227 | -46.11303 | 2025-06-29 04:14:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1168178c-cde4-31fd-af84-4bc4c0d797ba | -22.40679 | -46.81953 | 2025-06-29 04:14:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a4c17db1-9658-39b0-b2ea-a03880b146b0 | -22.54025 | -48.81311 | 2025-06-29 04:14:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e5db069-f59d-306a-a1f7-4e4f6fe12cdc | -22.72086 | -43.59395 | 2025-06-29 04:14:00 | NPP-375D | QUEIMADOS | RIO DE JANEIRO | Brasil | 3304144 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1c502f1c-e9f4-3fc8-ba4b-1e60a680c71a | -22.35097 | -45.77512 | 2025-06-29 04:14:00 | NPP-375D | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a60336b9-ca0c-373b-855b-f3de2b964020 | -22.59944 | -48.43786 | 2025-06-29 04:14:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89c536c5-b5b0-3f1a-985f-1cea5c10ef29 | -23.11156 | -45.82079 | 2025-06-29 04:14:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b358e0ce-cdee-3157-97dc-74cd99516622 | -21.01657 | -50.17295 | 2025-06-29 04:14:00 | NPP-375D | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4f1696b5-6dd4-3bfa-9a2d-ea32777eb000 | -21.40354 | -48.48905 | 2025-06-29 04:14:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af423361-b46a-3885-8ebb-d31199253c52 | -21.13069 | -48.58964 | 2025-06-29 04:14:00 | NPP-375D | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a4e3c078-cba0-3c05-a430-26326e693f34 | -22.83057 | -45.26464 | 2025-06-29 04:14:00 | NPP-375D | POTIM | SÃO PAULO | Brasil | 3540754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6039533a-e866-3e14-9f1a-b4afd75e7e73 | -21.537 | -45.46807 | 2025-06-29 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 56580ece-a210-3248-8ff1-3feb2933521f | -22.93486 | -45.69952 | 2025-06-29 04:14:00 | NPP-375D | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| bc01caf5-dd30-3673-b1ef-ccb597d676af | -20.76337 | -46.76892 | 2025-06-29 04:14:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5d0593fc-d4c0-335b-a95d-a006da0c0c4b | -23.40889 | -52.76754 | 2025-06-29 04:14:00 | NPP-375D | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5507eb57-6dfa-3ab7-a4b0-39af54dff49c | -23.41213 | -52.76606 | 2025-06-29 04:14:00 | NPP-375D | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7f9e308c-ae86-3a75-80eb-873e52af8782 | -21.17948 | -43.97995 | 2025-06-29 04:14:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 91c53a2b-3c48-3141-95c3-21b14af53f68 | -20.9005 | -43.81867 | 2025-06-29 04:14:00 | NPP-375D | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 87e1e256-f1d4-3a06-a581-eafb562e88b2 | -21.18935 | -45.05976 | 2025-06-29 04:14:00 | NPP-375D | RIBEIRÃO VERMELHO | MINAS GERAIS | Brasil | 3154705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 637561fe-8f8a-3074-9b22-3ab15edd2a63 | -22.40614 | -46.82342 | 2025-06-29 04:14:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7e7cd4db-bd2d-313f-92f0-50be5cc7f9c7 | -23.98367 | -48.91899 | 2025-06-29 04:14:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15f11d21-9808-320d-8fed-5fdba0c53b07 | -22.78689 | -43.75763 | 2025-06-29 04:14:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1d5aba88-19c2-376a-b868-8fcb85b85a24 | -25.19325 | -49.325 | 2025-06-29 04:14:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 37e419ce-bf8c-3b53-a8aa-3ed3b22de835 | -21.34168 | -55.63128 | 2025-06-29 04:14:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94a566ba-94f9-3421-bfac-3cc47698ab6b | -23.33841 | -46.77308 | 2025-06-29 04:14:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0dab4adc-d4b8-3a7f-a2ac-eb181f7a53b8 | -23.2704 | -51.20818 | 2025-06-29 04:14:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4d77f710-1ebc-333e-bec0-df019d623d78 | -22.71744 | -43.59334 | 2025-06-29 04:14:00 | NPP-375D | QUEIMADOS | RIO DE JANEIRO | Brasil | 3304144 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a106f3de-0ba6-3c78-ae81-c6ffb061835a | -22.93818 | -45.70014 | 2025-06-29 04:14:00 | NPP-375D | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2e97e8a6-025b-3657-8aba-aa868b0e42e4 | -25.19245 | -49.32938 | 2025-06-29 04:14:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0ae58ae1-93db-321b-81f8-c2aec89a5e83 | -22.1908 | -45.81919 | 2025-06-29 04:14:00 | NPP-375D | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d98810fb-087b-3212-ba4e-0bf9e0bca58e | -22.6768 | -42.85583 | 2025-06-29 04:14:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 133da90c-e582-356e-b01d-754557c26b91 | -22.93545 | -45.69576 | 2025-06-29 04:14:00 | NPP-375D | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 695a8ac4-6f57-3d5c-a9ca-2efcce455071 | -22.7445 | -47.14059 | 2025-06-29 04:14:00 | NPP-375D | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 499dcf2d-c95d-3094-8fb2-3111957e58db | -22.69265 | -46.50697 | 2025-06-29 04:14:00 | NPP-375D | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d18fc438-e9ea-357d-a593-3d7c16763566 | -20.24796 | -46.73516 | 2025-06-29 04:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83fad401-8556-3397-b929-72e78706f199 | -22.55659 | -42.11852 | 2025-06-29 04:14:00 | NPP-375D | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e45e943a-f366-3cc4-af72-c1a887a26d01 | -23.52173 | -46.97469 | 2025-06-29 04:14:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6d0bdce6-af77-3111-b15b-7ed3932d204a | -20.57869 | -44.57451 | 2025-06-29 04:14:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fb2e6a59-743e-3d7c-947f-7143e93a5434 | -22.58367 | -43.64886 | 2025-06-29 04:14:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 476e2c7a-383b-3de9-9e93-1f673ca2cbb3 | -21.6355 | -49.84216 | 2025-06-29 04:14:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 88c4b137-de12-3a5d-abbf-22986e53c545 | -21.33616 | -55.62985 | 2025-06-29 04:14:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32083775-9121-3b53-b7fa-c03fb8d6d5e8 | -23.30669 | -46.49838 | 2025-06-29 04:14:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 25faacc9-e193-3039-b16a-5d4ccbc13c46 | -22.99612 | -47.12267 | 2025-06-29 04:14:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ce21aae3-e3d4-3632-ae65-85a0486b23f3 | -22.85664 | -42.98061 | 2025-06-29 04:14:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f0747b15-d721-32d4-91d8-a1a9996d7e37 | -21.02055 | -50.17383 | 2025-06-29 04:14:00 | NPP-375D | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| d1a4369d-8d12-3eda-ad92-7917549d0d66 | -21.19473 | -44.93896 | 2025-06-29 04:14:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39761bc2-074c-39d5-8ebf-ef059d5740ea | -20.31185 | -50.1847 | 2025-06-29 04:14:00 | NPP-375D | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a1b55e2f-8d49-3422-9ad6-9c1d66b70ed1 | -22.93878 | -45.69638 | 2025-06-29 04:14:00 | NPP-375D | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 866c1888-6cc1-3de9-8108-a472b4a66051 | -23.11549 | -45.81766 | 2025-06-29 04:14:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 23246117-1118-3fb2-8948-3c0b12439def | -21.53367 | -45.46747 | 2025-06-29 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 71815b59-0bf1-3361-8cee-1364b558abf4 | -11.5312 | -52.7678 | 2025-06-29 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |


[Clique aqui para ver as próximas entradas](README16.md)
