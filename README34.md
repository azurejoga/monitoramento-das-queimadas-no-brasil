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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b1eb8cc-f93f-3b49-a899-4d36d54061bf | -15.6427 | -45.92667 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 94b2f808-8b51-3254-a5a6-134b552969dd | -11.01759 | -49.66069 | 2026-08-29 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc7d25ef-8775-32c4-bec5-688d9057726a | -13.32099 | -48.19272 | 2026-08-29 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| daf0e0fd-5bf5-3454-a5c2-8613f8957b87 | -12.77455 | -46.46027 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a9802f2a-a6af-37c8-a793-38d02eab71b6 | -11.04295 | -57.22432 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e39866e8-8fb6-393f-b7be-0c3af8ea2cc3 | -11.2386 | -53.99113 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e32748b-a97f-33b6-a388-bf922f9abf8b | -11.49455 | -46.94608 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e35257c4-1ebe-392f-975e-2d24c19424b9 | -14.40398 | -52.57785 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7c4f45a-e5d2-313d-8180-066ca0cef687 | -11.4912 | -46.94553 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7e0628a-af91-33f8-aa22-c576ccdaa30e | -14.75832 | -48.7522 | 2026-08-29 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f65337e3-affd-3c75-b534-99eecd44fca0 | -14.89619 | -56.33526 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af44225d-479e-3892-9a94-16b2895ab893 | -15.6497 | -45.93454 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 41.8 |
| b36ea6c0-5436-3e6a-84ca-00c391d0d6f1 | -10.82824 | -50.51334 | 2026-08-29 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddd7701c-692e-3e50-9f3c-8873e0caf059 | -14.2064 | -52.84944 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d855f64e-80a4-3f4c-964c-3e3f0e6c43a2 | -14.07532 | -44.06135 | 2026-08-29 04:34:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d6548f3-7db1-31a3-a901-ffed1c3a3719 | -14.07883 | -44.06189 | 2026-08-29 04:34:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d570197-415f-313a-9d9b-3391f8452aa4 | -15.64746 | -45.92675 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 403db37f-3885-3836-9bdc-c0d8a4f58403 | -11.02339 | -57.22922 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fd08746-27ea-3e66-9659-bc233681e0d6 | -11.03779 | -57.21856 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4021e541-e5c5-3e10-8e56-67c0eb848f19 | -11.69079 | -47.62599 | 2026-08-29 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 172d301a-0308-3b75-9dbe-f060edc0c799 | -15.1495 | -43.79576 | 2026-08-29 04:34:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a57db64e-11e3-3437-beac-b82588e148cf | -11.70596 | -54.5393 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9369e50f-5fbc-3ae2-a011-05b260e529f1 | -14.85626 | -49.32413 | 2026-08-29 04:34:00 | NPP-375D | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e87802ac-c1c9-3f89-bf68-31ace747a5cf | -11.48391 | -46.94804 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04de53d4-fc40-31af-b2f3-4f4ba61d5ce1 | -10.75982 | -54.04984 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41c89a38-7e46-36de-8288-2cf9d628e334 | -14.46845 | -58.52855 | 2026-08-29 04:34:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db38bf6d-5873-30aa-a06b-67eb5efcc006 | -14.208 | -52.84073 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73bff852-c622-3680-be3e-6d909b0f7bc8 | -13.02543 | -46.77462 | 2026-08-29 04:34:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9b7d6fe-4407-3d21-a548-121cd6bfb92c | -11.26882 | -54.02031 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9bca5c2-6159-3c6c-9ec5-50b9a4facbe1 | -14.40134 | -50.06277 | 2026-08-29 04:34:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71feeb1a-5862-33bb-ad31-cac039569423 | -12.79561 | -46.4565 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b515679-00ca-388a-a585-49e441d54fce | -11.83371 | -46.77455 | 2026-08-29 04:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b525ea34-8614-3d98-9bc6-ebf3cd918a2b | -13.026 | -46.77107 | 2026-08-29 04:34:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f9cae5d-ab08-359d-be0c-420fd5cf0d5f | -14.21418 | -45.30599 | 2026-08-29 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35fb313e-6e2e-345e-837a-982e38627741 | -12.78953 | -46.45185 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0213280-6a2b-3cb6-9668-7d98f3e2d85c | -11.02282 | -57.23006 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af53a48b-657e-3e58-80e9-7079e3348346 | -12.18993 | -50.55428 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b48fcda5-cb8e-393c-af05-5d8ddc422a84 | -14.19703 | -52.8516 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd08f128-2c5a-345b-8ca9-2431b05772db | -14.8981 | -52.62456 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32c91181-ba09-3a0a-bace-5e33599d6ef4 | -16.6854 | -49.46981 | 2026-08-29 04:34:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| faa72831-af0b-33a9-92e6-a3ea7ac40915 | -11.48593 | -45.0619 | 2026-08-29 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9f2e7df-c17b-364b-9d82-30ea1f4257c4 | -13.32442 | -48.19327 | 2026-08-29 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d2b775e-3bc4-3762-87aa-fe1fbce9473b | -12.25998 | -50.5417 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c10371d-3ca3-3386-a704-f137e5079acb | -17.28244 | -46.01823 | 2026-08-29 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff353ea8-43f5-3fea-98d8-0ee9a19977c8 | -9.96903 | -53.93238 | 2026-08-29 04:34:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b26b376e-07b4-34c0-a1ff-04bf833ced70 | -11.01136 | -51.39762 | 2026-08-29 04:34:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87bf7c24-ac66-3e9a-8457-c6c7255e96fd | -11.48986 | -45.10282 | 2026-08-29 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed8d9e95-cb54-397e-b864-023c55567737 | -14.90458 | -47.74205 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 794b8544-9b91-3733-903f-28da3ac71f89 | -11.20406 | -51.26765 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 898fecf8-ae03-301e-a4e6-727a360bf96a | -11.03218 | -57.21656 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6f80aa90-a5b5-3be7-9cfc-30a901870068 | -11.02947 | -57.23044 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb988b69-9ecd-33fb-bba2-6e1ecec1ba89 | -10.53926 | -50.47225 | 2026-08-29 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b781c2d-b90f-356e-8ce5-d639c0397278 | -15.1015 | -48.14403 | 2026-08-29 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9c6a887-ee03-3f4b-a668-b188b0338f29 | -10.88776 | -50.49782 | 2026-08-29 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62620631-b508-3475-8c51-8384ee4c8e0a | -12.18644 | -50.57397 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 257f90fb-23b6-347e-a203-f5c7d2560096 | -12.76648 | -44.26313 | 2026-08-29 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5127a00-7a8d-3edf-b835-b53b46b7bcac | -11.01155 | -49.67372 | 2026-08-29 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 980d7eec-c04a-3382-8d95-dcd41c43f2ae | -11.71664 | -54.53834 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1385820d-20a3-3c0a-99e8-559161ea762c | -11.72339 | -54.53038 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fea722c-4121-380e-89b6-4fc1eb3bf736 | -11.20472 | -51.26392 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e2438fb-8336-30a9-bd56-21cd5ed0cd50 | -14.89887 | -52.6204 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 30f4e6f6-ab13-37d6-aa00-482cb58f1abe | -17.6126 | -51.61481 | 2026-08-29 04:34:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26926f64-3af2-32f0-bccd-955a10a98898 | -14.11739 | -44.21687 | 2026-08-29 04:34:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34dfdd5c-5fa3-3ae4-8045-58f14fe07722 | -12.43431 | -42.88978 | 2026-08-29 04:34:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46602c0e-071d-3c88-84dc-d6cfe14c6618 | -11.63084 | -46.75234 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5e36373-1d9c-3e6c-a8cb-8af1e7b85288 | -15.64802 | -45.9231 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8d0c1f6-beed-3556-81cd-5faee3ae10e9 | -14.15375 | -52.84324 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41abebbf-e120-3153-95ab-0ef4d63f4aba | -11.29627 | -54.0374 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8451ef39-9954-3eda-b0a1-a9f855391c4e | -14.76177 | -48.75275 | 2026-08-29 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4caa4a8d-795b-3e4e-8003-4881865baa39 | -11.01077 | -49.67828 | 2026-08-29 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e276dc2-3395-3cb7-a3bd-bfb5a9cf16c2 | -16.61026 | -49.40709 | 2026-08-29 04:34:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd8fbbe9-042f-33e3-b890-ec6d8b54badc | -11.27551 | -54.03915 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbd6fda9-e4a8-3e02-8b89-80ad3b40aad5 | -11.17283 | -51.26258 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fcd3b94b-1650-3908-8671-f0490412bf96 | -11.4805 | -46.93644 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43ed7f68-7919-32ec-bc3c-bdfabf61333b | -17.82419 | -39.68987 | 2026-08-29 04:34:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c10d2936-d0ad-3e4d-906b-12034407f003 | -11.18866 | -55.10319 | 2026-08-29 04:34:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4809c2a4-4948-3399-ab32-5fd9c1cda663 | -11.1946 | -55.10082 | 2026-08-29 04:34:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f1b3f2c-2743-3c6d-995e-f7676a92a594 | -17.82482 | -39.68452 | 2026-08-29 04:34:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7f27e2c2-006b-3139-9da9-bde2ec3b6cfc | -11.49237 | -46.93836 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc2564f3-e869-32e7-b4cf-31502e27b930 | -14.92416 | -52.62523 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41497785-d9fe-3d7b-ad31-00de1afa8781 | -14.47569 | -58.52486 | 2026-08-29 04:34:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dac36ce-88b7-3e36-a315-dcd278ad4c93 | -11.23754 | -53.99672 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3c46a47-1a7b-3f7f-a04d-4b91b0ade61b | -11.26387 | -54.01944 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4445e46b-e558-3465-81ce-7977b718902e | -11.18291 | -51.29079 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bc8915f-6fa2-3427-9b7c-9a6ededf6f1a | -11.62679 | -54.58039 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1623e57-effa-31f1-9da9-14c1779853e7 | -12.22047 | -50.53956 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55d85215-9b79-3d5c-8462-1278cd1961dc | -11.0289 | -57.23125 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0f67f62-a036-3933-a21c-72cbcdb5de96 | -11.60841 | -46.7303 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 436a1e14-6a67-3c7a-bbcb-875152abad19 | -11.17873 | -51.26689 | 2026-08-29 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 351da0e5-83a9-34cc-b3f4-6125ea0669ec | -11.04107 | -57.23363 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8afbe1ef-5e51-3638-a068-32a4a6abff3e | -13.86921 | -54.12271 | 2026-08-29 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38cf9402-8069-35f3-90f6-f75a6dbfb225 | -15.12072 | -53.58277 | 2026-08-29 04:34:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 3413eff8-2aa4-3ec6-9760-ff63238cd7e4 | -11.04163 | -57.23287 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2815e633-0466-3143-be34-78691cb06c33 | -11.62735 | -54.5774 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65ae38ec-3f1a-3a19-83d4-34216f961232 | -11.22414 | -54.01055 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee4bd619-ff67-3d49-8b9b-dbfa5076b951 | -14.46225 | -58.52727 | 2026-08-29 04:34:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51a50e36-bedb-36d9-a920-7c36471e619e | -14.1502 | -52.83824 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e96acca7-1aeb-38e4-bd60-000f527532b1 | -15.63767 | -45.93695 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| feaa8c02-92d3-3aa4-8f16-3d39ac8ff72c | -17.24063 | -46.92445 | 2026-08-29 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 739629a8-47d6-3b8f-9e1b-1fa972ae05d4 | -15.64549 | -45.93085 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |


[Clique aqui para ver as próximas entradas](README35.md)
