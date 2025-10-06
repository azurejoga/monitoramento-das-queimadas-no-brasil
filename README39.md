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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e13c9c93-8d27-3856-97e6-8fc4f1c8f33b | -13.32893 | -47.17197 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1714edf7-d4ad-35cc-b977-693c0e4ef912 | -11.0132 | -50.67208 | 2025-10-06 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9270c410-ec84-3088-a03d-e45467bde120 | -14.36287 | -47.72161 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2ef1ce87-2a94-3860-84b8-ae6b5cfc3fac | -10.35877 | -48.14622 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7afa6d48-5c33-31ce-91c4-e14b604fb7ca | -11.11142 | -47.71391 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd55e310-4966-3fe6-a155-30f7287b6ce9 | -13.62903 | -48.71087 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25088061-9ce5-3f35-a366-86570a82a8df | -14.86471 | -51.50299 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16569462-e1b7-34c6-8963-e3cdd30cdad8 | -14.63095 | -52.54984 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cd26737-584b-38e9-9c9a-fece96491404 | -15.23986 | -49.28318 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08b5ab09-54a4-38f5-afee-2d72483090ad | -11.11416 | -47.65347 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a23e126a-e604-3459-b1ee-37fe66c4498f | -14.88962 | -51.51912 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b95a0b04-b441-327a-8608-b3f741b55c36 | -16.00854 | -50.84353 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea7851eb-5357-3a91-a2c7-9eb03421a567 | -11.84009 | -44.92025 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d1f5a8a-9737-3d67-9bfc-af03c9cf1350 | -15.92839 | -48.61346 | 2025-10-06 04:27:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2acaa0d7-e63f-33b3-ad65-999216b2c9c8 | -14.65245 | -56.01271 | 2025-10-06 04:27:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 245644de-a84a-3854-ab20-5ccf8988debf | -14.68976 | -48.37409 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2964799-d125-3659-beff-fa961d19172b | -13.26075 | -47.8091 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f29a371a-e9f9-3204-ba6f-dd864310fac6 | -12.45983 | -45.53641 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2af2a443-b437-3284-ae39-e25feb125519 | -14.68661 | -48.28642 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2910893-4bfc-30c3-a336-85ba14b7c3b5 | -12.90891 | -47.29348 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2793a603-bce1-3fd3-8734-f541515d9924 | -11.83134 | -45.10019 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10930f7d-14fd-3153-b95f-8f3d0d6e2f25 | -16.06867 | -50.9231 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a5a58d0-7aa4-3239-96ea-a09e1882882d | -11.06339 | -47.91091 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa7fa9f5-9aaf-38f5-8512-e9434a658865 | -13.07826 | -47.89117 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da8d1e95-166f-39d9-bc8c-8b13898e560d | -10.3759 | -48.14565 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca891516-49e5-371f-b805-9d0d7130fab8 | -9.27308 | -51.80978 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6e00e1f-03fb-380a-a012-0653403ea1f8 | -13.0555 | -47.90193 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1654c48-8275-309c-b212-fa04d77f61d9 | -13.36902 | -47.57444 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed617620-2227-3153-a55e-ee4fe7b05583 | -14.92837 | -46.8218 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ce442ef4-9ec0-327c-b080-647923484a43 | -13.0821 | -47.8882 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28326d54-24f0-34a8-a519-2af9fd030895 | -13.30467 | -48.07284 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c4ef155-2f0d-36eb-81bd-10761b14c363 | -13.08541 | -47.82387 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3fd9d74d-1c07-3aad-a684-7a30fbbb8147 | -9.15826 | -50.05555 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5a08dcc-ab55-3e74-816c-c10d8a42ff2c | -12.90323 | -54.74282 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 701ae1ce-ae93-3553-9b6c-e53b99a47800 | -13.25823 | -47.23367 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b44f132-996d-363d-ac12-d294055abe4d | -10.05079 | -49.20642 | 2025-10-06 04:27:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1c08bb0-4776-3a7c-b1bb-80525018057c | -14.444 | -46.09768 | 2025-10-06 04:27:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cde0a9e-df39-363d-a43e-e5b1dd248702 | -13.08703 | -47.8782 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32da156e-485b-3ac3-8afc-19d4f8209054 | -14.74394 | -54.6656 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0480e640-bad3-339f-bc8d-c5484d021b9a | -14.62258 | -52.50818 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4db7e112-71e1-3ba4-8306-47c9361e3ee8 | -13.69128 | -48.05703 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3a8cb1d-9770-3198-ae4f-cf28486e4e24 | -15.24261 | -49.28735 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fe18281-e557-3f0a-98b2-440e32efb43d | -10.67803 | -48.47261 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ae9c8d8-abca-3506-b52e-24887a34083d | -12.31299 | -55.11741 | 2025-10-06 04:27:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 635cc701-9ba9-3796-acff-01166d56be28 | -11.94775 | -51.47374 | 2025-10-06 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8af6139a-b3bb-3482-9709-e33cb2a1c1d3 | -10.36568 | -51.18561 | 2025-10-06 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6082cf50-2c22-3eed-8ebd-45542ac77299 | -14.20013 | -46.67399 | 2025-10-06 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fdc32d8-fb0c-3e3d-ab40-e83a46d632e5 | -11.83426 | -45.10445 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b563d55-54e3-3212-8776-4697d2e78672 | -11.23974 | -47.74158 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30d95d62-366e-3725-a193-fd65dc905383 | -9.91632 | -50.23964 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0761054c-357e-3ebf-b870-b62a2513c4f9 | -14.67491 | -48.38252 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6f17d0e-245d-3876-9b46-1464b82c0ca8 | -11.07826 | -47.9241 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c8a75ac-659e-3384-9745-bdeedf69903d | -8.95884 | -50.80284 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ba58bfc-65c5-3b6b-9725-4359d3b41cd2 | -13.37009 | -47.54544 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a46d647a-ed70-315d-b06b-dcfe185a38ae | -10.45378 | -48.36249 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3a43af7-c86b-3bd0-9349-7b316db4ff35 | -14.71233 | -48.35964 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4149f0ea-27a3-3be8-bbfd-1a3a6c7ba0db | -10.82919 | -49.39137 | 2025-10-06 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5be6810c-16f0-396f-8c71-cc100b1b3a24 | -9.67682 | -49.9532 | 2025-10-06 04:27:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a2864b0-92fc-3f93-b925-9ff53e3f42d2 | -14.67597 | -48.39724 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fae22cd9-87fd-3a43-8673-6323fa60a941 | -13.77124 | -45.74207 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bd453b2-699f-3449-a4be-babc8c132191 | -13.37562 | -47.57552 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29fa3718-38c8-3c8c-a99b-d7c51e40b2ba | -9.33793 | -54.52134 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0501d1b4-28b4-3f76-a64f-0a1e2bee5bc2 | -16.03976 | -50.95469 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e874cbb0-41e2-394f-8a53-f57cf9d0014b | -13.30578 | -48.06579 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1007a058-f3d5-358c-b66d-98e74d8c6315 | -14.26758 | -45.86698 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 91c97fab-e0ad-352c-b0d8-8ca04fe52720 | -15.34488 | -47.34743 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78728de0-0ba6-39d7-a5fb-1dd26f4a7803 | -9.3341 | -54.51538 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67e49b4a-6180-3cfb-8be7-9756c07e2f31 | -14.48776 | -47.55215 | 2025-10-06 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1666c761-1617-3ece-82ee-2620f573dbb1 | -13.25244 | -47.62362 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47c1e802-3723-355c-b34c-d5b111db6770 | -14.71559 | -48.38199 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23fc1272-ac01-3c9c-a07b-33d669472c2e | -10.70173 | -47.9813 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f49cdc28-2579-3703-be16-07a9c4302bec | -12.38752 | -51.0812 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 497f6820-b5d7-3888-ae9e-d72b2605eaa1 | -10.3952 | -51.64622 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a46b53e8-ff16-3a1b-b3b4-e249d3ed9701 | -13.72217 | -48.07998 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 47837f32-f9ff-3614-8156-14936e82db6b | -15.7669 | -49.09589 | 2025-10-06 04:27:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7cfb51b-ae8e-3144-8808-388d0cf35bd7 | -10.34374 | -47.01059 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1d62f51-c353-3814-975c-ea5befcf288d | -15.00681 | -49.96719 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a53ca63-b7fe-36aa-8811-d32129a0bb3f | -14.34634 | -47.67529 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 82601612-a5c3-395e-a8c7-777541e94739 | -14.65791 | -48.36155 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d05cf5d-0033-3b2f-8021-ec0e299ffe48 | -12.91606 | -47.29101 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3afebff0-7f90-3ab6-8ec3-0e1f93bd4f52 | -13.38003 | -47.5907 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89fed4da-1616-37a3-b1d1-f6b63e0583a7 | -11.84941 | -44.92994 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66db9fb8-7597-32f2-abb1-52188f2c4cdb | -15.60983 | -52.54629 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 918ad2a9-a6bf-30fd-acfa-6d886aaf9805 | -15.88161 | -46.25325 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11117e20-0a06-32b4-b98e-2a6d517bcbfd | -13.35658 | -47.19099 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 100050fb-b112-3bc0-89a4-8ca4250b6a53 | -14.69758 | -48.30276 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae1653fc-5480-32e4-87fc-3e3406cb6ef6 | -13.07442 | -47.89414 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e43cf3d7-032b-3837-b1fc-fa5f1bc7da78 | -14.67871 | -48.40134 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71656d62-5d8d-30a8-83e0-cfcc7b555d1a | -13.30137 | -48.0723 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8ba0356-58be-322b-ad9d-f04b8ba1a417 | -15.35505 | -47.99266 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 950dab89-69dc-341d-afb5-8b70d3ed53ab | -12.71333 | -45.85822 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3832f21c-8a60-37c0-a9bb-024897210de3 | -15.77021 | -49.09645 | 2025-10-06 04:27:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdf86366-66d0-340e-bb17-bf97429cf945 | -14.56593 | -46.65083 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c80983c-8ab6-376f-9000-f5cbf8b2a35c | -8.61282 | -54.97943 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f6ad0f9e-d9d2-3182-a8c2-4bb565e5abfb | -15.20452 | -56.82685 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d6a2c60-685a-3a85-89b9-13fdc7946500 | -11.50475 | -54.46818 | 2025-10-06 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2cdac0a6-cccb-34f4-b577-d5dfcab2d565 | -10.86401 | -47.20865 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 333a5be9-f8d8-3aee-8631-aa069a8f7d64 | -9.27004 | -51.80384 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 406f0b34-4fad-3577-a696-37a647d3eba0 | -11.8766 | -57.81755 | 2025-10-06 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4cfd8b26-aac0-3497-a309-26d3a73bcbf7 | -13.24372 | -47.80993 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README40.md)
