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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77078239-f6d6-3ed1-8229-d63ec26e940f | -10.55721 | -46.23879 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa2ed768-f6c0-3412-b7fc-78b25338bad9 | -10.42873 | -49.44064 | 2026-06-17 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ddca65a-2f48-3c0e-b2d0-a371a8fcc135 | -12.20349 | -52.77556 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 032958ce-b190-30ac-8c00-f178007e6566 | -11.51457 | -56.13168 | 2026-06-17 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9d106da-6204-389c-bb80-b0084905a83b | -9.37187 | -50.53882 | 2026-06-17 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a066c606-3645-3b5f-98b0-f8ffc0984211 | -12.21421 | -52.78205 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 87fec67b-a5b7-3cf4-a9fb-8ecd746be663 | -11.51179 | -56.12763 | 2026-06-17 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7848ff7-f872-3d9c-a085-69ddd4c7f27d | -12.1952 | -52.77919 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 22e25fea-dfc9-3d08-bde1-0cd06e29de76 | -12.19384 | -52.78874 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 1413f243-bf3e-34e0-aeca-a79f613b40cb | -12.20904 | -52.79101 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| c911c481-6b4a-3d21-91a6-5b61f3c1c9e8 | -12.20642 | -52.77774 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 216c177f-c957-3470-9056-644e890ff54e | -11.23481 | -46.60637 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8602d1f7-08b5-3f98-ace5-c8beb1218f96 | -12.07959 | -54.60163 | 2026-06-17 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 32a88d8e-7c92-3d9e-be99-d3775e3757c7 | -12.22033 | -52.78958 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e1f30e34-ef86-3cad-9c56-9c535986d6ec | -12.847 | -44.36609 | 2026-06-17 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 301ffdc0-1ea5-3eec-9459-722883467a79 | -12.91885 | -54.22359 | 2026-06-17 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e630828c-3343-39a9-9193-14240070ddb3 | -14.09746 | -59.46078 | 2026-06-17 05:06:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01d89d97-508c-354e-9151-5a03bda8a002 | -13.28104 | -46.05628 | 2026-06-17 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e6bf7dfd-1089-36a9-8efd-90fa0d2847d5 | -9.46363 | -57.83691 | 2026-06-17 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e224b93-d931-33e7-8c0e-b21582642ff1 | -11.80142 | -58.16247 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21c66afc-7ff3-3039-9aae-63efb5dac3a6 | -12.18446 | -52.77271 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6b4b7c2c-1029-3154-a379-0ebf2500f6ba | -12.1064 | -51.99054 | 2026-06-17 05:06:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 29d9e89f-6b55-335c-8c05-bd87bc1fa262 | -12.20892 | -52.78787 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 563d0da8-5ddc-3664-8989-16b239b763eb | -10.58771 | -53.51297 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| effcc699-3da3-38fd-87a9-b10eebd04b21 | -10.49515 | -53.58097 | 2026-06-17 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d22377cd-6e4f-3bdf-ac3b-4da81cb7a3c7 | -10.15477 | -56.60937 | 2026-06-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 902a64ac-7876-35e5-92c1-32a7a0bfca7f | -12.18514 | -52.76791 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b348b2ea-80eb-3bd5-a04e-0a9b884eefa9 | -12.20577 | -52.78251 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d8db551e-88f4-36bf-a303-e25d1a79514f | -10.12453 | -52.16794 | 2026-06-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53f5dc38-4e70-37bc-9267-e1d07c913cf6 | -12.50581 | -46.35163 | 2026-06-17 05:06:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15791552-f3f9-3f7c-aa3a-03d9f125a12e | -11.59828 | -55.33803 | 2026-06-17 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58134dcc-867e-359d-b97e-38adf393e11b | -11.48123 | -57.11396 | 2026-06-17 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 368fb201-36d5-3a9b-93ac-292e19e78c75 | -10.76884 | -54.10924 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 642f4764-980f-3a7e-bba7-8789aa3278d1 | -10.58533 | -53.51427 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76b7d59f-89bc-3714-a29d-482fec20279b | -10.15256 | -56.60188 | 2026-06-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09e5e4af-37c5-30aa-a9a1-c06623635e73 | -12.10462 | -51.98976 | 2026-06-17 05:06:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bca320a5-2b61-39fd-a2c5-d92cf68c8a4a | -12.19764 | -52.78931 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d03690fe-8b58-35c1-8cd9-91662702b882 | -12.42958 | -58.40746 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91fd823b-99a0-3d22-b011-0fe0d0b7c71a | -9.62914 | -49.01689 | 2026-06-17 05:06:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a0cf3cd-d786-3edc-99fb-785cd73df25e | -11.66844 | -56.76394 | 2026-06-17 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6fabcdf-abc1-3407-9a8d-e1d2b1c91dea | -12.80487 | -54.86206 | 2026-06-17 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1c7a40b-2e0b-3997-88b9-a8164ae5c553 | -10.27431 | -60.54951 | 2026-06-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e712d578-7d1c-3f52-97fa-0acaf03b48fe | -13.28054 | -46.06088 | 2026-06-17 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4b05869c-ad73-3609-9206-23b06ce58253 | -12.84578 | -44.3777 | 2026-06-17 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 1210b25c-8c4c-364c-86ff-5d1e9838ae9c | -7.86516 | -61.48878 | 2026-06-17 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba97ff4-4202-3c17-9a65-cd1c2e1a966c | -12.22479 | -52.78538 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| c85473a3-e3b9-3be8-a63c-fabbf8481215 | -11.58763 | -55.34011 | 2026-06-17 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd1ac21d-3b3d-3434-bf81-ce75609a6671 | -11.51125 | -56.13115 | 2026-06-17 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93072eee-2e04-349f-b30c-19dcf8633a88 | -12.20144 | -52.78987 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5af8c149-21db-3a51-a89b-fafb4bd6ec2e | -12.85302 | -44.37276 | 2026-06-17 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 736ce00c-09fd-38cc-92f9-fe0e31d4f2af | -11.20531 | -55.03793 | 2026-06-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5e56549-fca5-3467-82ae-338515028627 | -12.1717 | -52.78056 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3357c6fd-d32f-3ac0-a833-3f0ba797dadc | -11.51233 | -56.1241 | 2026-06-17 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcafb748-34f1-3966-b3a8-5eae6d9c368d | -9.73171 | -57.6727 | 2026-06-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c54a6621-ec74-38f1-8333-896e5c37fae1 | -12.50629 | -46.34735 | 2026-06-17 05:06:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 957752ed-3cff-335f-a5c7-6ad3d17c7ef3 | -12.19275 | -52.76905 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c426df52-8527-3e2c-9f90-cf98f431793f | -12.19207 | -52.77384 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e256bdfa-af43-3c15-8a89-7ef7bc739363 | -12.67161 | -54.5799 | 2026-06-17 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0dca80e-b380-30ca-b1f2-97bbd448c5f2 | -10.55295 | -46.22594 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85d41f93-7767-3583-89e9-8ac3e7c09d16 | -11.79201 | -56.99525 | 2026-06-17 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8698e5d5-a77b-3ce4-b3bf-be005d7f22ad | -11.79916 | -56.99281 | 2026-06-17 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1a6db94-ee63-35d8-ae7a-4fd6ab9dd1fa | -12.21284 | -52.79157 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 310.0 |
| aaa37f6a-2378-3ed7-ac6f-47bacb56d58e | -10.15147 | -56.60884 | 2026-06-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 92b4581a-3a1f-31da-b2e3-53b2ac804a1c | -11.34844 | -51.40411 | 2026-06-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1c0a2d7-a68b-30bf-9e4b-842e5f85780b | -11.88871 | -55.13686 | 2026-06-17 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf410575-740f-3a51-b035-cefc6e2e0415 | -12.65415 | -47.67273 | 2026-06-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3192a33-41f4-3415-a786-daca5a679a53 | -11.54578 | -52.77598 | 2026-06-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 32ed87bf-0ead-3c91-9824-c3f8922568c1 | -12.923 | -54.22001 | 2026-06-17 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0ef8199-1e67-359c-9f83-77ba800598c2 | -11.71954 | -54.48249 | 2026-06-17 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56b1a98f-69a5-3bba-8347-2de685f64af5 | -11.54645 | -52.7713 | 2026-06-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 35307b33-df79-307f-968c-e75f12577240 | -12.22729 | -52.79546 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6eed55a3-73a1-39fd-9cab-a5280a2ab535 | -12.19139 | -52.77863 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2e0bbe27-6e1e-35da-aa22-880a79379d6f | -10.27962 | -60.54099 | 2026-06-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec09fb14-9f9f-3e95-92f7-ef894ec12b7c | -10.71389 | -56.24938 | 2026-06-17 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73e6b451-ed47-37d7-a471-584a0d52266a | -12.19968 | -52.77498 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e907ed08-b0d8-314b-ab63-5a7125b03fef | -12.19832 | -52.78454 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f3a5b9f2-d93f-3a72-8156-56284f7caf86 | -12.22348 | -52.79489 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 81bfe0b6-658e-3a43-a1b4-d5e5964c1fb6 | -10.12244 | -52.1824 | 2026-06-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9157fa8c-3631-38a3-9e62-1b4ec0e7c166 | -12.1755 | -52.78114 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3619a761-fcf3-3390-ab00-85aec3321a65 | -12.67509 | -54.58043 | 2026-06-17 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07bcdc8f-f709-38d0-94c2-7b8a9dba8ee1 | -12.17685 | -52.77157 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a044ad4c-4b54-3eb7-81a4-ab95afbad085 | -12.17483 | -52.7859 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ef0971c6-4fdd-3881-abc1-43b6b103ece0 | -12.21216 | -52.79632 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e61e9692-bdbd-3386-9673-2edab507fbeb | -12.20456 | -52.79519 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9c6bb37d-018a-33b0-b349-499f11bb0273 | -12.18311 | -52.78227 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a7ffae8e-4e84-375f-ac80-5b8cb37ddc05 | -10.02657 | -59.34277 | 2026-06-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3658ceef-fd85-33ee-a1e6-3a42764e90db | -12.46851 | -55.12484 | 2026-06-17 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c56beaf-7ad6-3a29-a4ad-14e040e14e8a | -14.09809 | -59.45696 | 2026-06-17 05:06:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac9ed4fc-45d7-36e3-bccf-2868d6b5f143 | -10.76942 | -54.10531 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 879df59d-2f81-38dd-b673-ac98be37706a | -10.60327 | -44.32417 | 2026-06-17 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cca0fae8-97c1-351f-94b8-6472dff831a6 | -9.21195 | -58.07 | 2026-06-17 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ee57aca-cfd7-3acb-956f-bedc85d827c5 | -12.06286 | -58.03961 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b6dd08f-acf3-3da3-a94e-e442f6b074de | -12.08248 | -54.60608 | 2026-06-17 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e5201089-6744-3ead-a877-ec7d1bf6b13c | -12.18895 | -52.76848 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 406e4527-10ba-36d4-b560-eaeb96db2a2c | -11.2087 | -55.03846 | 2026-06-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae9c0448-d726-3057-a420-5ca225f22143 | -10.90559 | -54.13673 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f28aecd6-5a52-3d0e-b5c2-80af9f0c2497 | -11.48068 | -57.11746 | 2026-06-17 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 992d7523-df34-3475-87d9-7e4cbce9a288 | -12.22414 | -52.79014 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d34f9419-d9f7-3461-a328-9b578365cabd | -10.1531 | -56.5984 | 2026-06-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4f67a6c-99a3-3fc9-92aa-dce01599c5e2 | -13.57702 | -48.20644 | 2026-06-17 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
