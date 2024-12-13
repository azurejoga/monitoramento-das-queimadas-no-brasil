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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3ce8d2c-f60c-337f-89f7-77604ab444ad | -13.06009 | -52.04343 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d62f491-b0eb-3385-b07d-d955a1985e23 | -8.27165 | -48.02731 | 2024-12-13 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c7c40a7-0919-39e7-a859-6683fd8a5cc3 | -11.43819 | -55.91796 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1387bb42-d989-312a-bd61-cfd94471eadf | -12.02871 | -49.5542 | 2024-12-13 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acec61fe-f2bb-3c05-9a07-87e6fb9543bc | -11.20179 | -53.83194 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 595831bb-a9df-35eb-aa82-5cf9a6538fef | -12.05382 | -46.89015 | 2024-12-13 04:44:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15147425-d031-36b4-b19e-46911d2c1fb3 | -12.76488 | -49.30915 | 2024-12-13 04:44:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c57ad51-813e-37ba-be34-d9b0d8c12353 | -11.20459 | -53.83625 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ff0585f-4443-3461-a4b8-56db20165f9f | -13.06782 | -52.03744 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cfb046ce-ae8c-32f3-8a4a-7ac414982926 | -11.80879 | -49.33036 | 2024-12-13 04:44:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28c33b25-05b0-3de8-b06a-b6344938789f | -13.23866 | -53.06373 | 2024-12-13 04:44:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ff73f7d-750e-3d8e-b387-0cdf515dff98 | -11.54008 | -51.27468 | 2024-12-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c6755dd-b797-31b3-bb1f-e14f9472d5d2 | -7.40557 | -50.47057 | 2024-12-13 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4419eb0e-6a89-3818-bd66-ff225fdbf8f1 | -10.20667 | -47.58439 | 2024-12-13 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 543c0618-01ee-399a-bd23-eab4845f3f01 | -6.86437 | -51.98259 | 2024-12-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df8ec5f9-34c6-39b7-9d79-2a84e182befd | -10.46245 | -53.95168 | 2024-12-13 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4f3b09b-79bf-38a6-b747-643a10bc0a16 | -13.06174 | -52.03282 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dde1c969-d266-32ab-a824-4294cef580fe | -11.68413 | -48.07491 | 2024-12-13 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f512ecd-1d29-3a27-a257-81b0fe19c24b | -12.28412 | -45.50105 | 2024-12-13 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 503b31ef-a873-3b50-91bf-b784b7bd5635 | -13.69951 | -54.76845 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b9818a8-524a-3061-b04e-fc2a9ab01bc0 | -8.2644 | -48.02616 | 2024-12-13 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fec13597-f74b-34c6-a624-451c66e02bf3 | -8.54796 | -54.60583 | 2024-12-13 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db6cc63e-1472-3594-9f95-27622106156d | -12.01932 | -49.54461 | 2024-12-13 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06e14dab-94d3-3083-8cb7-58da4c85ad1a | -9.19479 | -49.47837 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffefe097-06c1-3a99-9fd6-864db0d678de | -10.6482 | -51.66339 | 2024-12-13 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3fa249b1-b7e6-3bf6-ac13-a989684b6eeb | -13.5448 | -55.3831 | 2024-12-13 04:44:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af076c95-373f-3f8f-beb7-8f1f7a5ee1c7 | -7.57847 | -47.11796 | 2024-12-13 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3d7c91d-8477-3ad5-8571-7bddfc9cd51f | -13.07445 | -52.03851 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abd72f45-b345-3b2e-ac73-c595cd620f4c | -11.81444 | -46.60739 | 2024-12-13 04:44:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd068c47-efb6-331b-8e7a-64e841d01efd | -13.06119 | -52.03636 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b5574cec-b5b5-3b4f-a152-a48bd9c2fcd9 | -13.36814 | -54.25113 | 2024-12-13 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eee515e7-6c81-35cc-9f75-984bc14c7c9c | -13.69295 | -54.7523 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40c408e0-2edb-3eb5-8b1d-e59f917d9578 | -10.72678 | -47.5893 | 2024-12-13 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4850cf62-bb76-3478-a7d2-4af50d31b078 | -12.38469 | -51.45232 | 2024-12-13 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8687230f-8301-3cd1-8a0d-abf6ab366a51 | -13.06505 | -52.03336 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa89f868-b1cc-3617-a323-aefb9a3cf358 | -12.53641 | -57.72492 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ca6333-9bd9-359f-84ab-76c1663e35bc | -9.15928 | -49.48071 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f3a5f58-4533-3503-950d-42c505b67b6e | -11.20923 | -53.82933 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31aa5396-0a1d-3a4f-b007-8b84e5049042 | -13.68605 | -54.75106 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcf6ab18-2e1f-3e43-b47a-03b322d0f6cb | -12.54663 | -57.71533 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13f87566-d3cf-3c5e-8de4-31fe0d7b91d7 | -13.40047 | -51.07119 | 2024-12-13 04:44:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9dc31a48-efb6-30bf-8c36-a67c1f848a02 | -12.53917 | -57.73314 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4812a578-0aa9-3fe4-afc3-b0a4f27dbf96 | -13.05456 | -52.03528 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d11276b-695c-3c6a-a4da-8b00b583426e | -11.11769 | -54.65255 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 135827ff-440c-3cdd-bb00-3a20ce3e6f43 | -12.05434 | -46.88647 | 2024-12-13 04:44:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c7f56aa-b302-36ed-a31f-f340b9c51056 | -13.0645 | -52.0369 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6b830541-b4d3-33ff-94aa-8d050a1368fe | -12.33805 | -43.67416 | 2024-12-13 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2b0311c-2b78-386a-b286-a5a348cd1a7a | -11.11836 | -54.64853 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 01008dd7-3bc3-3298-8d57-7d3572760de0 | -9.16328 | -49.47747 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 38c68b8b-81b7-363f-b437-136ec5b7ea31 | -11.43787 | -54.46882 | 2024-12-13 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3a1b1bf-35eb-3e1b-82b8-673ee933d6fa | -12.56796 | -57.76183 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 577bfacb-0a8c-37c1-98f7-4eccc133eec9 | -13.68668 | -54.74722 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2648b61-6e93-359f-b377-063d991d6edc | -12.53355 | -57.72601 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a764fbf-3a31-3c2c-a1ca-e7472f84d52d | -11.68856 | -48.07079 | 2024-12-13 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25ff92db-d149-30f5-b0b3-755bfa32b810 | -11.43922 | -55.88988 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9fb1da2-2ebc-3bf0-970e-ae11a2b15de0 | -13.0634 | -52.04397 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f772f14-75bb-327d-ad27-bed011ffbe08 | -13.54411 | -55.3872 | 2024-12-13 04:44:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1e2969c-d4f4-327c-af41-808dad4db685 | -7.98687 | -50.70465 | 2024-12-13 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcaa91f3-d156-3c3a-82ea-26f9e5f53ea9 | -13.37154 | -54.2517 | 2024-12-13 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95017ad8-b0e0-3730-9e03-4f8b5f2a519f | -10.66435 | -44.7201 | 2024-12-13 04:44:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8b3c634-4fae-3c8e-bfed-601d9213edb1 | -12.62716 | -54.88626 | 2024-12-13 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c574253a-6a54-3045-9e97-29101123b10b | -11.85914 | -46.94778 | 2024-12-13 04:44:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6d3f1c2-7f6b-3d5c-aca6-3b1b155b9d72 | -13.07223 | -52.0309 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 271274f4-5505-38b9-8b63-a1240a26ee76 | -12.56729 | -57.76555 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01341a83-f51f-3b28-a298-0942003fbf74 | -7.58294 | -47.11393 | 2024-12-13 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89424019-68e5-3d59-a651-a28d17b1293c | -13.69513 | -54.76061 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81bf2818-317e-3452-9c3c-35fe2e3028e5 | -13.24198 | -53.06428 | 2024-12-13 04:44:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9964f8e2-085c-357f-9439-954f1d3a5d25 | -13.37619 | -54.24475 | 2024-12-13 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37db1529-5589-39bc-9f4e-4da60fd2f83b | -13.54126 | -55.38247 | 2024-12-13 04:44:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec7e4002-e298-32c6-a51f-3665dd098410 | -9.16729 | -49.47421 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bc80249a-7d88-30a5-8bff-fdcb707187e4 | -13.69795 | -54.76507 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32012307-fd8f-302a-98c9-bd2964727be4 | -11.44193 | -55.91865 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2649e0b5-6317-3003-8cab-5cde1cc1168f | -11.16029 | -49.43862 | 2024-12-13 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 596f0938-77db-3fff-a72c-a391ec091784 | -11.19837 | -53.83138 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0724fb1e-92ff-351b-b7dc-ec6da1952cd5 | -12.76427 | -49.31331 | 2024-12-13 04:44:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71b618d2-a94b-3227-8413-a7301717d90f | -11.81858 | -46.60798 | 2024-12-13 04:44:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 180f927f-3ca5-3b93-84c4-92726640c021 | -12.07286 | -48.40131 | 2024-12-13 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e97a5e5-2f60-39c4-bbf7-0ef3e9c29bcc | -11.19776 | -53.83511 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d64a4d8-6063-30ec-9ca3-83342e6a479a | -12.90486 | -55.04764 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 738b0786-1aa2-36ae-9c79-74ab8b1c6189 | -13.05842 | -52.03228 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5594b92-ecbd-34bd-8914-063fa5c8fece | -13.39654 | -51.07433 | 2024-12-13 04:44:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bb74c03-cd19-398d-867b-153263591861 | -11.21045 | -53.82185 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdb1c5a4-0b3d-36aa-a10c-d6d14c618242 | -11.49359 | -54.46508 | 2024-12-13 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcb88362-a28b-3a4b-9fac-82ffedb2cbd3 | -11.2024 | -53.8282 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 3c750b3b-dbb7-3014-be7e-3c6027fbb447 | -11.61253 | -54.5329 | 2024-12-13 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8ce58ca-f8c6-3f74-b701-cba349713dc4 | -11.21203 | -53.83364 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a8f97a9-5c15-3fef-9996-dc053bd8064b | -6.86771 | -51.98313 | 2024-12-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e27184d-7c34-379d-9a10-6d0fc421d6a1 | -7.58225 | -47.11852 | 2024-12-13 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29e015a9-f77c-3037-b332-0f067c8fc917 | -13.65906 | -55.24247 | 2024-12-13 04:44:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52d1535f-eebd-300d-8606-a25c34bf2f3b | -12.35542 | -44.71585 | 2024-12-13 04:44:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b51f875-c147-35a3-a591-3bcb08fcc5c5 | -12.5473 | -57.71158 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cf4f631-70a3-38c6-8f05-6c8ebbf0a7b7 | -11.42991 | -55.92122 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecbea062-00a0-3e2f-8575-b38c0574d19e | -11.11417 | -54.65193 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 492f71d4-add1-3d06-993b-d4a231cfb2bc | -12.91595 | -55.72919 | 2024-12-13 04:44:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23409a5f-5c62-3801-9645-8cdb7b9deb95 | -8.27103 | -48.03152 | 2024-12-13 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fb88888-c857-3e0d-b00f-4072bfc5f9bd | -11.43994 | -55.92494 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13676306-ba93-344f-9274-8eb072908274 | -9.13753 | -49.48508 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6091b655-6516-3689-802a-8f11f981f46a | -13.69576 | -54.75676 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4150d89b-eb29-38d4-ad20-65bab926a2d0 | -11.43739 | -55.92256 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04a9075f-b389-38fe-8916-8eead3c78014 | -12.53829 | -57.72313 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
