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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 953a31e4-dc17-38d9-a6f3-4212e55344b0 | -11.87946 | -47.61611 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3296008-440a-3008-bc12-563f1e029555 | -9.94901 | -46.53995 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 482486b4-9f94-3d9a-9367-593b64854dae | -10.27807 | -50.00492 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1cb0b79-f7ba-3bae-9557-bb8c4a8fae5d | -11.4157 | -47.28016 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d8563da-ea12-3c12-a60f-df84aa9b5b02 | -9.32451 | -48.19377 | 2026-09-19 04:40:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ed802e0-f049-3c47-b4e3-958edc9b703b | -10.8649 | -54.10631 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53ad0ea1-6d38-375b-ad12-64c21a0380e5 | -15.99182 | -46.74188 | 2026-09-19 04:40:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51de74ce-c3ec-3c22-9c4a-47cd1f6926b7 | -12.86098 | -46.33853 | 2026-09-19 04:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9baa2901-bb87-33c0-a81f-b76ef52feae9 | -11.29815 | -54.88047 | 2026-09-19 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d7ab760-8751-3de3-ac96-5898438353b2 | -9.25063 | -45.93242 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3b327a6-e9f5-3ba3-a6ba-7853edd89eda | -13.68029 | -48.58316 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6104eb82-e12d-3e5c-8af7-7e61d5d3edde | -10.91296 | -50.84853 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b7134c4-adb6-3708-b6f8-e19e46ee8044 | -11.21876 | -42.82473 | 2026-09-19 04:40:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0c646718-f157-32f3-858f-075c76ef979f | -10.23846 | -48.84913 | 2026-09-19 04:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 944d42c1-2831-3aa9-9a0b-c853eb4eb4ad | -9.02862 | -48.74409 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 422b10b0-079f-38a3-bb17-05b58bf2b1f6 | -11.35504 | -44.11969 | 2026-09-19 04:40:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 044fdb24-f2f9-324e-972e-de2c51bde55a | -9.34043 | -48.18542 | 2026-09-19 04:40:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc6ffa80-0ae3-3088-a5bb-e77770f38543 | -14.92513 | -49.92898 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 607916a9-6446-3182-aa79-a7123d7ce2d1 | -12.13978 | -47.01235 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1da75048-786e-3ea6-8c80-9d49d0ce5c5a | -14.92576 | -49.92516 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 22494a20-203a-3daa-b2c5-654a902d94d2 | -9.70495 | -45.97824 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 364af861-a217-378a-beaf-ce5e9b75ba4c | -13.5214 | -48.94105 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdf30123-1da8-33ac-8db5-e467fd0d55ed | -10.45436 | -48.68377 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4727741d-68ca-3f32-90e6-b2a68c32f36e | -10.05171 | -44.88359 | 2026-09-19 04:40:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c19a201c-1b70-3cde-a750-8fc6d275c8c0 | -9.31486 | -45.41015 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fbcc9b7-f52d-3a39-bd67-c3288c3f3e20 | -11.12574 | -47.72097 | 2026-09-19 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bafa7615-9f4c-37ee-8add-2932b7bff74e | -14.10259 | -44.82415 | 2026-09-19 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67ee31c5-20b9-3f3e-a37b-2a4eba51ef80 | -10.55452 | -51.31641 | 2026-09-19 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db6e0b60-1409-3be4-8eac-30456c6dccef | -11.1325 | -49.04515 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dff3efad-51a2-3e61-8f84-9d6435a45270 | -10.85934 | -56.18569 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d51b40a-41e0-34bc-bd44-0a013e2c5f71 | -10.63327 | -48.69766 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 276d0a6f-9dab-338e-a9e2-cab3952dcf79 | -9.03048 | -48.73283 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d07ddfbc-82f1-3259-a4c9-d2e8e1b35ec3 | -14.79435 | -48.57428 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54bd1c14-3fcf-3968-96f9-1f3ef1902fef | -10.07382 | -45.64586 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51efbdf1-4c32-305c-a951-e93ad8b11d79 | -16.05218 | -49.98273 | 2026-09-19 04:40:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8a5ab4a-3d90-33c7-9773-07619771a717 | -8.33567 | -50.74734 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc64ef98-1767-3ba0-9a69-e02d5c968f18 | -13.74064 | -48.79599 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bde106b7-fcc0-3035-8ff6-ec616e8acb04 | -14.69429 | -46.65992 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e97903c8-567a-30a4-a800-697447149c87 | -12.58345 | -49.10339 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e4f8449-2ade-3f0a-a3dd-242f789d4a49 | -12.7006 | -45.95305 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cc7d5a36-9463-3799-91b5-80ff4cdd2e0b | -16.04879 | -49.98214 | 2026-09-19 04:40:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50e6763e-534a-31be-b9d6-0f073ca9b534 | -9.80417 | -46.10321 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e69dd3d-bb6a-3c3e-b719-d896b8a9f21b | -9.70048 | -54.83651 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bc04583-5432-3675-b48b-222287b7fd2a | -11.82229 | -46.85946 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ccbdaeb-bc5f-3424-a5a4-37a249943241 | -10.69018 | -60.74413 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94dde511-99c6-3003-ac61-5f447d7dc7e0 | -9.67635 | -48.33224 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e610089-ed7e-3e86-96ad-58595252336f | -14.81995 | -48.56395 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 551754ba-e27d-3265-93ca-6c10b649689e | -9.96687 | -45.29764 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6296dd5-6b0e-3c73-a0e0-c5d787c14e55 | -11.11562 | -49.441 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 196c73f1-a2f6-3a3e-9484-04509d8cea70 | -9.55241 | -46.59212 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3efed37-da17-38c5-afe6-4ce8fc2a7e59 | -13.39562 | -48.03482 | 2026-09-19 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18818e0f-644b-3593-a895-d5c5d51d3692 | -9.82705 | -49.24243 | 2026-09-19 04:40:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0fdeb68-0aaf-37b8-9bc7-f3e8b317d8df | -12.16425 | -46.9652 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1727bf4b-e3e2-3b5d-9397-5d1e706109c6 | -11.97927 | -52.45689 | 2026-09-19 04:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2998a432-b2d7-3bb2-a372-f4c3465a8d60 | -10.49742 | -46.27023 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f4fc24d-c7cb-3209-9ffd-8dda48150759 | -12.34467 | -48.20091 | 2026-09-19 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9248f61c-4cf4-331d-ad5f-4bd006d76966 | -14.25988 | -52.79712 | 2026-09-19 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d049e86b-f6b6-3096-8e3d-d9260b02a706 | -13.62414 | -48.3023 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a20dfdf-4c45-33b8-84bb-75e9266ee0f1 | -10.87602 | -54.07053 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ea0b44b-0de6-3aeb-9aa8-5f91986ffe31 | -12.85759 | -46.338 | 2026-09-19 04:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f5d379f-ad13-3466-b38a-3ed51dcb6ecf | -8.16619 | -54.82571 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 581f1474-d9e1-3535-903a-abaa11285555 | -14.9403 | -49.94319 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52d2c4ea-fde4-3a5b-870e-711a4083b9e3 | -13.60854 | -48.31435 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e84b7a85-1d34-3a9c-99de-46ba7992940f | -11.30052 | -46.78015 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f76ceda-5adf-33aa-a4b0-324ca8e60a7d | -13.64256 | -46.95065 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5f68d02-18fa-3608-88ab-7679d61b117a | -9.55407 | -46.5816 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3531dd21-d928-3049-863a-49bf176907bd | -11.07644 | -48.29514 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 79002ab3-c958-312e-9953-f53c3a0f5857 | -10.87131 | -56.21001 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca851914-73be-329d-8513-8f562d7d4b26 | -14.66257 | -46.66247 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 535ba8af-c812-3d3c-9721-ac984e023035 | -9.8411 | -48.37452 | 2026-09-19 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a2df9df7-eeb5-38af-abc2-7e5c88ce1976 | -10.63109 | -46.0524 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18b9592b-0c15-332e-bdb1-39464512a135 | -14.95519 | -49.93802 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1184e780-d46f-30cc-b536-fc559d43b454 | -13.7434 | -48.8002 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d150c546-714c-38fc-a1bc-503c6e90fc86 | -12.1968 | -46.48878 | 2026-09-19 04:40:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4dfe3df-4319-3c57-9ff2-64d1fc7ac8b7 | -11.77223 | -47.43906 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebc2ce50-1e73-3aa7-96f4-4847e994ad77 | -10.86407 | -54.11094 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 923c5542-2f04-31af-9487-c0ecdd331159 | -13.6113 | -48.31847 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0000a444-6a28-326a-9bf8-60f3d0d7984a | -16.60179 | -46.99487 | 2026-09-19 04:40:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52db2ab4-e5f6-3dd8-afd7-5dd82582fad9 | -10.16112 | -45.37235 | 2026-09-19 04:40:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a53ecc0-6be6-3c42-af65-5419ea114200 | -10.89149 | -50.88558 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af423deb-d33f-30a3-b5c0-47c13daeb2e7 | -12.70117 | -45.9493 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3cf56ae7-d956-30bb-97bc-4a2bc1b183e9 | -13.64703 | -46.9439 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7e44bef-1879-34c0-85e0-32ac0f6e41d1 | -9.76855 | -45.06751 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5324813a-3bc2-3aea-a1bf-e61a09349762 | -13.00838 | -46.96844 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aaa3862f-842b-3e76-9ec4-f8d04f332c5f | -10.88585 | -54.06765 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34ec4c61-3b93-36e2-b509-14d355cba5da | -11.40014 | -47.65006 | 2026-09-19 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90582c52-f633-3249-a4b6-16da66d72493 | -11.305 | -51.72776 | 2026-09-19 04:40:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5192232c-cc47-3238-9f19-70d19e762e1c | -10.92083 | -53.97569 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 056a1ba6-67ea-3250-9027-6089c3821d77 | -11.01614 | -54.12996 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 63c07719-d109-3e93-8b23-9feb16e05544 | -9.75782 | -46.59632 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a997cff5-fe57-3ad0-b702-57b363bc5250 | -15.0603 | -48.58612 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdb37b13-e1bb-3489-ae21-40bbc3bc1d52 | -10.87107 | -54.09798 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a0a16d6-756a-3f57-a116-d14a1a190a61 | -12.15312 | -46.97075 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d063f645-cc6a-3154-937b-32b69f33d7b0 | -10.47694 | -46.30405 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c1beda2-1536-36ef-a23f-dc38c16b44ff | -11.49746 | -50.72819 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55ade322-55bf-354d-a517-0115ea1d0541 | -9.91585 | -48.12786 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9bdc088-3666-35bb-a599-9fbf08d8335f | -10.54284 | -46.59447 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 422fc64e-3f26-32f7-9a14-dcd265ff3962 | -13.74005 | -48.79966 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dd24f96-2918-3576-bfed-7b4a49970cb2 | -12.16759 | -46.96573 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdd14eee-9ba8-3dbf-a6ba-339bdf6c47af | -10.59235 | -46.59911 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README55.md)
