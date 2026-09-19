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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0ac13bd-43bf-329e-ae85-3dabc6512143 | -11.43404 | -51.46836 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69b6d88b-f05c-3057-94c8-26e6951bbb81 | -12.48882 | -50.0446 | 2026-09-19 04:40:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a52b372-8c59-3791-9086-98c533b68c8e | -11.07747 | -48.31002 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00dfcc2a-96b0-3213-868c-f6948fae8042 | -11.50017 | -47.72419 | 2026-09-19 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3f91c0d-bbcf-3927-bbf3-e59409370772 | -13.63407 | -46.93091 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfae32cc-9be1-31a9-9db9-0da7289ca17d | -13.62225 | -46.9626 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee0b3ce2-661c-3fe5-a12e-73288e085690 | -10.85816 | -56.19426 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcbf323f-ae96-3b23-bdcd-32436f1ebb17 | -10.93466 | -47.85272 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f80bb7d-1977-39cb-b27c-c40378445086 | -10.93409 | -47.85626 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f658c7f-31f6-3955-8e47-7000fb6675e7 | -11.32135 | -47.35873 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc0309d3-3b2f-34ba-ae07-f7518bb39e11 | -10.83663 | -50.17758 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2468cbe0-1631-3591-897e-d5f88710005a | -11.30583 | -51.72292 | 2026-09-19 04:40:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c3004fd-e9de-3982-b923-3c91aa138ee6 | -10.12858 | -45.56123 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52e35834-a3bd-39fa-b61a-c73703269ad3 | -9.76166 | -45.06641 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2946a965-e8b6-3613-8168-145176273d72 | -12.34744 | -48.20502 | 2026-09-19 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5807e624-b784-3856-a435-bcca8ddf01c3 | -10.98606 | -48.2919 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4b5f5d2-caf4-313d-a1f5-6fb5c39e210d | -12.57487 | -49.11327 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 291fc418-d007-39e2-b2cf-6cfd556819c9 | -11.0747 | -48.30591 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2adc806-fead-3d8e-a838-08e49efd4173 | -10.44176 | -47.50876 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d24ee060-2f9c-3320-ba3e-f2da196b211f | -10.58005 | -46.54641 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9df8c4d6-6424-327a-a3a4-9b46065006ed | -12.54297 | -47.09143 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b83a89a-50ba-3a9a-ae43-90bfad260d1c | -10.47855 | -51.33442 | 2026-09-19 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a0c46c59-03a5-32a1-b7f9-8ec8d1e1c624 | -11.82219 | -45.4676 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4591684-d1ff-37e8-b8a7-2a6f0ad6e69b | -11.11677 | -45.29556 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 030b6d0c-6709-34ca-a5b0-2dafe075d199 | -12.70344 | -45.95735 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0cd83f0-36f2-3380-af36-771663c88ee6 | -14.14933 | -45.21772 | 2026-09-19 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ee96ef9-44a6-3c44-ab9d-b91a10137322 | -15.80682 | -49.01012 | 2026-09-19 04:40:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02fb54b0-02c8-3529-8cdd-9bef787fc1cb | -12.99893 | -46.98516 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a14b4746-0ca1-3ca3-93ce-2feb5c397838 | -11.30827 | -46.75242 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90d7d81c-b4f1-3bc9-8692-df7637e8712f | -10.798 | -46.64582 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 316e1f78-bcbf-3089-ad03-bad24d660f14 | -12.57468 | -47.08574 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5d294fa-d6f7-3fd6-b633-e87ad1dd8f37 | -10.32376 | -53.58337 | 2026-09-19 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8893d315-b35d-360d-b95e-02cfa80033a6 | -14.16887 | -47.84845 | 2026-09-19 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73ff489c-243f-3012-acfd-92cfccf8af99 | -7.59184 | -55.69741 | 2026-09-19 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd6d5914-7548-3eb3-9142-e0c473ab2ca6 | -10.53839 | -46.60101 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cc14874-51ba-30d9-bc97-94575fb46edd | -14.68693 | -46.66256 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| ccec11cc-5aef-33de-aec3-248aaf83a114 | -9.75016 | -45.07239 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93d4718c-2c82-3ccd-bc54-fe0a769aacd4 | -11.12368 | -45.29665 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cffa46bc-85ae-3c96-864d-1eb621df9ae3 | -10.40207 | -48.33987 | 2026-09-19 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e4c414df-347b-3df5-9cd5-4bae7d16b575 | -13.39183 | -49.45779 | 2026-09-19 04:40:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04736754-39a1-30c7-af27-1ed36ab19147 | -14.67785 | -46.65345 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00358da6-d185-3b98-afa9-18c2f52b66b0 | -12.16091 | -46.96466 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fe902ac-5093-35cc-9323-ce5246cde8dc | -14.12919 | -45.55153 | 2026-09-19 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a645b98c-195c-37bb-87ea-89d85f542f3b | -14.94155 | -49.93567 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 904c03c5-351d-3336-8ec2-c0317d1fea72 | -10.16635 | -48.52025 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c49221e3-bdd7-3830-abd4-4f323aa6ee58 | -8.7714 | -48.6756 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73390dde-41b7-33a7-962d-3f62714ef88d | -11.08208 | -48.2816 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c17eeb9d-99c3-3e1a-8e37-3549a40904b0 | -12.85348 | -44.39252 | 2026-09-19 04:40:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 75044de5-a72d-3c6b-a2e4-968367fc935b | -12.48765 | -50.04952 | 2026-09-19 04:40:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 705246e3-e347-32e2-bdf9-c42e188c9667 | -9.24342 | -46.18625 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c744d3b-36a4-311c-9e07-b673e4838753 | -14.67049 | -46.65609 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 13be3fc2-a3b5-31d7-8832-ccaea273a9e9 | -11.02383 | -54.13356 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47cd1075-d727-39e7-bc7f-948ff0f64035 | -9.23619 | -46.18875 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48adbfbf-c392-31d9-86b5-cdda5ad1ad41 | -10.9241 | -47.85456 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c62e70a9-e8e4-3154-b911-c3a2997be27d | -13.02069 | -46.97756 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2482e2e6-90b1-3c8b-aab5-7b3c40511b94 | -12.13976 | -46.99053 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a9037217-f9c3-3eab-878d-e85b5fbfd2a9 | -11.40904 | -47.63705 | 2026-09-19 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0de68ac2-786e-3a84-afec-8ffb47fb605f | -13.61775 | -46.96943 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc7ca65d-67f4-3ef3-a7ea-b2ab1763dba0 | -9.75837 | -46.5928 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 515042bf-6a2b-3a15-a84b-39de3031f102 | -14.93801 | -47.05081 | 2026-09-19 04:40:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34ff7a92-c6a3-3e7c-b205-e1e166d41a54 | -10.79958 | -50.88002 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c6bf255-8ebc-338a-9ccb-4b3a5ff10808 | -11.91172 | -50.12464 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ad8f4ef5-562c-3666-ab7f-796da9788933 | -10.72245 | -60.7319 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2572cbd-161e-317c-88cf-4d096d6a8920 | -10.93056 | -53.95633 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db44c6e8-4616-3aec-ad6d-728a4df81ee3 | -10.23565 | -48.84486 | 2026-09-19 04:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df5bee39-d52a-3443-88ed-d27fd1e29aa8 | -12.12531 | -46.9954 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d06422b3-8345-3ab5-afb9-a63e44a112a9 | -12.13366 | -47.00771 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f862455-1ec5-3d4d-a42d-cc6425f72358 | -10.32321 | -45.33579 | 2026-09-19 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad5d57c9-6847-3530-bbad-a431400e8516 | -10.91026 | -53.9831 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 848fbb7e-4081-310a-9cc6-75c9a5750a4d | -10.99428 | -48.3263 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6043cdfd-ee12-3da6-8701-13b2f43d277d | -9.75094 | -46.08061 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fa95a7d-48b5-3c87-b2cc-7042c512beca | -9.46096 | -45.43629 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a38311b9-1376-33cf-9542-73dd9dfe8de4 | -9.36108 | -48.29281 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dcfc5d8-7832-300c-8fe4-55b09c34a74a | -10.10338 | -48.41349 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9cf60325-c605-339b-8371-25f74a4f2378 | -13.39894 | -48.03538 | 2026-09-19 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 366505ee-043e-3d91-89de-f913ca5b060e | -9.2517 | -57.13799 | 2026-09-19 04:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a49e3c5c-793a-388d-8fe1-7daa2d593558 | -10.86574 | -54.10168 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed87512a-d34e-39c6-a2a9-3bb13286b18b | -10.13821 | -45.56655 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bc5b231-a190-34b7-a57f-c738efe5b74b | -12.12864 | -46.97403 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a9967ef-105d-3e55-9bb5-ba025a50185e | -10.50077 | -46.27075 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9a742ef-45e2-37e6-9b43-9f6cc557c6ae | -12.90831 | -53.90067 | 2026-09-19 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24729d63-b8e3-3e23-a996-0f0cd5d94af4 | -10.32031 | -45.30845 | 2026-09-19 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e885ef69-9b84-3ac1-80f5-54f83863b30e | -10.58395 | -46.54335 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12dc8964-9a7e-325d-9391-1e58fc9b180e | -12.5875 | -42.22362 | 2026-09-19 04:40:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 222f3b42-0591-3bec-8622-c4698d9f707d | -12.02 | -55.54453 | 2026-09-19 04:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7834e96-7d62-3fb0-96df-0cf8baaf6639 | -11.11964 | -45.27655 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddc04488-4822-3585-a51d-6a0931ce89ed | -9.94574 | -45.27525 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6b0099e-92b3-37fb-b6ea-4965c793c85d | -13.62168 | -46.96629 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1781613f-be31-3216-8a4b-06aa26a5b755 | -13.25192 | -46.94751 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d367adec-3a44-332b-a3ad-5c9c88b60a4b | -11.31161 | -46.75294 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fff4fe98-8cb0-361e-948d-a68c7a5eb6a8 | -10.16694 | -48.51661 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b82eb274-9413-3108-a611-79692ced5869 | -9.91074 | -46.58782 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec508f8a-2967-38ce-a862-d2066caded1f | -9.76883 | -46.07612 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a0ad309-44da-347d-9a38-c8665c7a261c | -10.31754 | -45.30796 | 2026-09-19 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da573eee-e3e9-3c1b-bbe0-a7769a0a2046 | -11.81895 | -46.85892 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2024981-fc3d-34f2-9e7a-5f70305f99ed | -12.98828 | -46.9431 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11fc9e49-31ae-345d-9515-8f01e828362e | -9.94956 | -46.53642 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a359bbce-24c3-3be6-b046-de2e6c61024b | -11.00552 | -48.32066 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d25c714d-accc-3221-b0f5-581cb05799ca | -7.59977 | -55.70017 | 2026-09-19 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b20bc22-5180-3ba7-aa85-d10b2a790e25 | -10.92808 | -53.96975 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README56.md)
