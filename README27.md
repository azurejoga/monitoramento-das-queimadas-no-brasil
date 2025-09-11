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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81118ce5-075d-3328-8811-5407cc256b04 | -11.35115 | -46.52576 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7affd84b-91e0-3f00-97be-5a42f1189b41 | -7.85911 | -45.5134 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b042b4e7-fc66-39c0-8c47-4ed309478fe7 | -8.87448 | -49.56336 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 43e8950e-78c7-3e28-b368-82bd51d10cb7 | -12.52999 | -45.35037 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e872133-0671-3710-baee-72185a13fad4 | -10.19968 | -46.83504 | 2025-09-11 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9bbe5985-7548-37ba-a241-b1488a2e435c | -11.46703 | -43.69851 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1cd8613e-f944-3c4c-abe9-d13af321afc7 | -6.358 | -43.05463 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f880b24-5330-3487-a739-b4e560148458 | -9.0771 | -47.06868 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 81223775-2967-3fdd-a562-25101d4abba7 | -7.53506 | -44.67826 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8d12f0fa-6322-3779-8ccc-f74ac3132a9d | -11.81018 | -46.75406 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 451f2aa5-7fdb-33b0-8ca8-28d3304ca076 | -6.39595 | -43.50817 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 466a480e-0167-31e5-b2cf-5a239a5a14f7 | -7.2053 | -44.95057 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0d31ac4d-f6ff-3229-96af-f4d64f8a3a1d | -6.6694 | -44.09411 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d896abe-511c-3fe1-8bf6-b24643553f4b | -11.10659 | -48.40589 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8869d4f-22ee-3f1a-a4c7-74bb7f8d3ac7 | -12.07161 | -50.99995 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6cd81a32-c414-348b-869f-4e2baea04c61 | -11.6536 | -46.91271 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a03ed03-ad34-3cda-b132-dfb720be0fe2 | -6.6582 | -44.54417 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 624835f7-7b39-3ece-866a-c9d4ecab16c3 | -11.4314 | -43.5685 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43d61c36-e7ce-3fd6-870c-af7f057e9346 | -8.74656 | -47.12299 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3f4cec4-dac8-3b5f-badb-931554a5ee5f | -12.13265 | -44.86828 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 917881a0-a58f-3e2f-a49b-26d0c10947d3 | -6.1932 | -43.49486 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f523ca9d-2e48-3d0b-88fe-9b104b9443f6 | -8.04018 | -49.04432 | 2025-09-11 03:55:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6da7893a-ea37-307e-ac80-a34bb4b41a44 | -10.56984 | -43.66509 | 2025-09-11 03:55:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c6e3adf-0957-3f89-9ba8-df8277b28164 | -9.78388 | -51.10912 | 2025-09-11 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 651462eb-8f93-35f0-a1a5-5bca670d856f | -11.40684 | -43.54694 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec9012f5-76f5-3d77-bf42-4af8136007da | -8.20052 | -50.10514 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 478a006e-910a-3ebf-bac4-a5f6a7fabbb9 | -11.79866 | -50.58747 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f224bc07-e37c-3bc1-bc8c-347e41d74c97 | -6.46894 | -44.11972 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2281e6e-386b-3579-9ee5-be759195e92d | -8.81199 | -48.09275 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a9d2abf-2cc0-3054-94e9-41d6d9914b50 | -10.30558 | -48.79723 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a159505-09c1-317e-8d30-bdcc960abc4b | -11.44479 | -43.58015 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 766789db-ec5f-3f04-a995-0b589b61fd16 | -6.48923 | -44.49239 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06228efb-03af-3788-8a86-fc3ee4c7be20 | -10.54117 | -49.8902 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f61c1e1a-5d78-3e7d-810e-d7a61b412a29 | -5.7395 | -45.29809 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 57500849-d485-323d-a3bb-0166cd713fab | -11.42844 | -43.57881 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bc10b26-4ac7-3934-b585-88af1f877d05 | -11.3443 | -46.47696 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec61b874-fdc3-3f54-9d89-a1262e42e473 | -5.69801 | -45.32021 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bf814a8-1649-39c4-9ab7-a35f9b1c1384 | -6.21335 | -43.49797 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 236123b2-4bc6-3c76-8f98-58102fe7981f | -6.21721 | -43.37345 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e97196c5-8168-300c-b55d-306040264b66 | -9.02278 | -49.76252 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ba0f6f5d-e788-31a2-a811-f72a6e2c9d20 | -12.22408 | -43.8675 | 2025-09-11 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d92f469e-7c14-3700-97b6-4ee8e0a68eee | -11.65911 | -46.90863 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d8cb768-f12e-372c-85c9-7bc7c655c765 | -12.42517 | -47.78948 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7cbb9fb-d723-3840-be82-6863d3edfc3a | -9.08539 | -47.09141 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d94b750-1368-3d2a-adf1-9239257861aa | -11.72269 | -50.64064 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| a49f99ae-aa62-3f3c-a88b-2dd3b550e48f | -6.96473 | -44.8179 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ac24aa5-3a6c-3976-8cb7-1ef5695ae75f | -13.27006 | -43.7449 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 46102202-9c4f-3e28-acfd-5363e07bd028 | -6.19723 | -43.49545 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7483fc29-903b-34c4-b6a9-b74acfa34928 | -11.80469 | -46.75842 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6325163b-d25f-3656-961c-35c46265f612 | -11.16764 | -45.28066 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3688e1e-1157-368d-bc35-6beebf7f9905 | -9.67657 | -43.52302 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1be21f0e-ce0e-3961-a3ea-ca3fe6d72072 | -6.64092 | -44.07436 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 571615d4-6ab4-31f0-817b-ee61ea5689a5 | -10.19135 | -46.21191 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 816e666d-8950-3485-b51d-d567793de525 | -11.384 | -45.58356 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ffe57ed3-e306-37b5-86a4-840a9e5b6882 | -9.0856 | -46.96764 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 77e9b554-0d01-3b60-9d08-f00f5c20ce8f | -8.9386 | -46.11421 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6afb4ab1-3002-3631-8f25-3a5c9cf677fb | -11.47061 | -43.63208 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8f42f75-7354-372f-a45f-063f765c3d55 | -7.03466 | -42.13066 | 2025-09-11 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 39a2b5fa-9985-33d1-9aea-75ef167b0773 | -11.37926 | -43.52816 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c68e2769-71cc-3c4c-bf65-4822f32b90b2 | -12.47658 | -47.49279 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 147493bc-bc52-34e3-938f-cc06a04c1a2e | -7.46365 | -45.28927 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 027e8e48-063a-37de-9aba-5c579c68c85d | -8.49022 | -47.31144 | 2025-09-11 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7478504d-3397-3739-9a63-acdd1257659e | -10.66761 | -48.63044 | 2025-09-11 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb4ab58d-0b13-338a-a243-29f25c97225e | -6.18387 | -45.78452 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec036a29-fb70-39d9-a6ca-32c30368679c | -11.10349 | -48.42207 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f7474df-1733-396d-abd9-559259096def | -11.63331 | -46.76469 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 182c5f6a-39ea-3727-bfbb-8849bc0fde88 | -10.54464 | -51.52349 | 2025-09-11 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8ea1512-414b-35a7-954e-d38bcdf6ff2b | -9.07563 | -47.08959 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d39e5c0-488e-308e-a570-44734fb2daab | -6.44348 | -44.77637 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 99a0ccf7-1fb1-3458-8274-86b63eaaa349 | -11.10608 | -48.42741 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b8004e2-cc25-3c3e-a30c-a979be67a6eb | -11.43295 | -43.57488 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cccbe99-da75-340c-b089-a6822c54773d | -9.03283 | -49.77306 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff8827b8-25b9-3587-8063-af984631c260 | -6.25818 | -44.85318 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b086510f-c700-360d-8c3c-828a9ebd939b | -7.56069 | -48.21345 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfa7e568-75f5-3922-884e-e19188c1aeb3 | -9.0851 | -49.8485 | 2025-09-11 03:55:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2624c1de-a2ae-3b63-a857-f5cc59d4733f | -9.01747 | -49.76106 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3131e8e0-a064-3a5b-936f-4047d7a05271 | -8.10996 | -44.84751 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dd9252b-a673-3a45-8c9c-fb3a099377be | -8.58156 | -50.80019 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c03ea27-f983-3e4d-824c-94986fb1dc17 | -11.4574 | -43.59648 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10327a4e-3b3e-3581-9297-a520a5100e2e | -6.27379 | -43.39135 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12925ebc-9c3d-38ff-8766-db966ae82836 | -12.13704 | -44.84321 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a7cbd39-8690-3408-bb40-e40561540eba | -12.55283 | -44.65691 | 2025-09-11 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e35103e1-aa3d-37ae-b9db-ad10eea3d4e3 | -11.09951 | -48.41499 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9052ae99-f342-3645-9324-c7f5f336dd2c | -7.91875 | -44.84929 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af8ad7ff-f2d2-333c-8dd0-ebe5d57f234f | -8.06781 | -50.17881 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d1570d9b-261e-380a-9a47-84c7fd8cda64 | -8.51151 | -45.69476 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 090d0f86-58ce-3ffa-adc3-1378efa88eaf | -8.07301 | -42.95087 | 2025-09-11 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 72828893-6d01-3582-b495-f8c3ef4452b7 | -10.26658 | -43.82831 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50271393-e654-3465-a2ba-c5edea00d39e | -9.59118 | -48.06708 | 2025-09-11 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58c3c2bc-f9b7-3933-84db-efdc0e1b0053 | -11.46922 | -43.61758 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6213b8e-d5da-3b9e-8f93-4e63febdd7b4 | -6.41438 | -44.38948 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60f8174c-eed6-380e-9a2b-27b67cc20475 | -11.64902 | -46.91169 | 2025-09-11 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b05b806-4382-34bc-8c74-c15e25b217ab | -6.16265 | -45.81321 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc16d3ca-cd2f-3613-a6f0-3a4407d7b157 | -12.03195 | -47.54174 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec6d49ea-051f-31a1-9797-2a057a632553 | -9.6844 | -46.76487 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0883208f-8e1c-3420-96b1-489e923c6f0c | -9.30616 | -46.75873 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 099516ce-47df-307e-a555-8e464fbc2137 | -10.30996 | -48.80341 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f522e40d-795d-34a6-978b-6478731081db | -12.01653 | -47.59936 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 4a81ee90-e8c4-3756-adab-28fe15dc9a52 | -6.54151 | -44.78007 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e963efa-c9fe-358c-a04f-1d2325269bd0 | -11.4781 | -43.63344 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README28.md)
