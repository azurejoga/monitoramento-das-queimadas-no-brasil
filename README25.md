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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0470d4f7-d119-3f6d-abf2-1909d12c84ad | -11.14613 | -49.05204 | 2026-09-29 04:17:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 90fe6832-015a-30cc-ab6e-74d8406120ab | -13.53765 | -49.17678 | 2026-09-29 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e7e3a6bb-e2db-308f-83e1-2b356f8a6c2a | -13.06625 | -47.45293 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f9e2243-814c-356f-a6b8-fa210643da88 | -16.19715 | -42.8768 | 2026-09-29 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ba1b44b-0b2e-31ef-b1a2-297f4a2bbc58 | -11.96929 | -50.92682 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f929549-de65-32cd-8456-b99495827393 | -15.22484 | -46.18106 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3615b47e-edc9-369d-a807-2edc5d219250 | -12.02429 | -50.94568 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5d328f21-c095-355a-8a5e-28e3831ad158 | -16.35519 | -42.58363 | 2026-09-29 04:17:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4394481-a5ad-3000-985f-7984d9fae312 | -11.42581 | -43.43382 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 0a645977-99b7-3f1b-8fd6-3ab47fed34bd | -11.4286 | -43.4379 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc611a7d-a1ed-3fcb-9dd8-deb7a226e0fe | -11.43472 | -43.44251 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a2139ae-94be-33b9-a817-9adbd9b30e0d | -11.43084 | -43.44556 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 511f478d-1f5a-34ae-b193-c94a3694dd78 | -11.33594 | -54.12045 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 377aad59-e4db-3efa-a782-2b359418067a | -10.2802 | -44.63421 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12a3b278-341b-322d-a013-1a401cea1c3e | -11.93145 | -50.88172 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33868248-0bb5-3df3-8f3a-0ad4c836e117 | -10.01197 | -50.24725 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42b570f2-6014-35b4-b3b4-0bc0d10b994d | -11.45032 | -43.47418 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e659c46-cef5-3aeb-bb9d-ad5655d746c3 | -15.47061 | -46.13423 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e76305f-e09d-3dab-82bc-d55e627daeb4 | -9.20261 | -45.84634 | 2026-09-29 04:17:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6dbd7dc3-821f-37b9-b851-c9163cd6541b | -15.21604 | -46.17211 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d425e3b-b134-317a-b7e2-a2744ba78eb9 | -15.18199 | -46.12938 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0779512-ad42-35b1-a0bc-c17c1ef000b3 | -10.19957 | -49.99066 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0e2b2fc-e684-3318-9f1f-9e2f7cade99e | -13.18763 | -48.56436 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3571c8e8-015c-37e9-bcb6-25f4c87c7b57 | -11.26446 | -43.53203 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acd12d68-370c-31a3-8a83-d3f31edb66ab | -13.54226 | -49.17274 | 2026-09-29 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b2ff7c35-6ccc-3769-986f-5a7629e3deb9 | -11.38699 | -43.44235 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d32b902-7242-30f1-8258-d630fe9adfbd | -13.19132 | -48.56501 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85981e21-2f07-316c-a02e-d76b4c22a018 | -12.55949 | -47.15792 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3d812886-8ed9-332d-a562-4bf6b97445a9 | -13.86828 | -43.99732 | 2026-09-29 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8b1adae5-5ccc-34ab-8cb3-0933297f020f | -11.41363 | -43.44652 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63f75312-7d40-325c-8bf3-bb02ed87b067 | -11.6428 | -43.50398 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a101621-3299-3beb-b30c-aa36cd37ed92 | -11.2149 | -44.77143 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a6036b6-7763-3f9f-8374-36032081f7dc | -11.40364 | -43.44497 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32bda14a-8c8d-36cb-912e-08ee2d4d4462 | -14.449 | -40.74964 | 2026-09-29 04:17:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8fd310e4-17a6-3197-80e7-f66b8c86ad12 | -15.09339 | -53.88147 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbe5498d-f776-3b9b-b769-3352af668d30 | -12.76827 | -43.92252 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8fb3b45-b182-3388-b358-8440522e382e | -11.26059 | -43.53506 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3654feb0-2312-3e7c-9b56-31fc8a6a84b3 | -11.36567 | -54.05228 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2f12dff-60de-3a1f-ba83-07ee587500ca | -9.14537 | -49.97392 | 2026-09-29 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86662de8-d07a-3419-96fd-648398371ae8 | -13.16841 | -48.56565 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbc04e7f-d9f3-365e-b48e-536de0e4ddbf | -15.83354 | -42.56499 | 2026-09-29 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9f90d8b5-67f6-3d4b-a53a-b451c1092bea | -9.78204 | -44.81569 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edc40eb2-1541-3288-b9d8-4b34142a6815 | -13.79448 | -43.67789 | 2026-09-29 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c6cabac-8d74-363e-a34b-90f2b0fc1c1c | -14.20024 | -44.93396 | 2026-09-29 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67d33833-4031-3cda-84ff-e1163c08f504 | -11.86318 | -47.08043 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 727a24fc-eca5-3ee7-b44e-fd2c680a5c50 | -19.25208 | -46.68907 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86eb456c-e0f4-354b-9a57-0e130540d24a | -9.85431 | -44.93971 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 043787d3-194c-3910-af5e-c3a9bb521c37 | -9.01839 | -45.98647 | 2026-09-29 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a45a385-48c0-3ea2-94e4-1cb209d6278b | -16.90518 | -42.10173 | 2026-09-29 04:17:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 401bdb50-0fa5-37b2-9afb-ae4f6489fd15 | -12.00429 | -50.98192 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d8ee7531-f843-3d78-918c-c4835d63ab85 | -10.26091 | -44.60603 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b2bb93f-2775-3fe0-aeee-9d33d612717f | -16.79311 | -43.00747 | 2026-09-29 04:17:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e64933b6-f799-3547-8869-9f17ac98c487 | -10.27304 | -44.63662 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c9ad443-fb2c-3fdd-b8cb-d20e95a2b77a | -12.39534 | -50.22591 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ec4b836-0c79-303b-aca2-a3bd8732b1c9 | -11.44809 | -43.46653 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8aa93193-6a07-36a6-8737-8d60879232f5 | -11.12347 | -50.05524 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 232bda2d-4c2e-3b7a-8e55-f2b64f21ebbd | -10.13138 | -45.14433 | 2026-09-29 04:17:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 227485f0-f1d5-3c0a-b7c2-7c1e8d4fd7e1 | -10.8061 | -48.72557 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 943cdb5e-13b9-33b6-91d9-38c4a0143d2e | -11.40806 | -43.43834 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 282e8023-dae3-3dc3-bcad-2c1417ce452c | -15.17608 | -46.12484 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de35112f-a3ee-32a9-9c73-08df071cdebd | -20.44544 | -46.34447 | 2026-09-29 04:17:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73cf22e0-c66f-3c06-adaf-401795da996a | -12.66072 | -46.98984 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| deb0b620-caf3-3225-b561-48e899739157 | -15.22815 | -46.18167 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9dd12440-e782-34d0-b46c-ade16b9c75fc | -12.05114 | -50.9462 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9185193-8dc6-3d41-a342-1c6801dd4219 | -11.43919 | -43.45783 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b95e773-c206-371c-8809-958e38bc58fa | -11.34944 | -54.04918 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26373e54-ebfa-3d2b-bc86-ad711aa702e7 | -12.94945 | -46.64661 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e1bb481e-6317-39c9-8ee7-869d6e1271a1 | -9.43484 | -46.32265 | 2026-09-29 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56c0145f-7e80-3388-9b18-60bd372829eb | -13.26726 | -43.54725 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e75c1d58-68b8-36a9-b5f1-fa8fc9d5f212 | -12.69852 | -47.25776 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a229bd8d-03ae-37d9-a821-35e7800b8689 | -12.21241 | -47.14922 | 2026-09-29 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5334a59-68e2-3e09-9bbe-df7466b30b05 | -11.3677 | -54.04146 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a285dd8-8979-3606-9a34-db5db3b030e6 | -19.18822 | -46.8125 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 652b4764-133f-3fcb-a1e0-3a84c4145ab9 | -13.52636 | -46.90134 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbd3290b-540d-3359-b068-b9bef6f2482d | -13.74137 | -43.66575 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8307e712-c102-35c1-8b30-bfa628a6ebc4 | -12.5967 | -51.96465 | 2026-09-29 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 105691f2-1226-3739-b1dd-3b4a3db03b3c | -12.76914 | -44.53459 | 2026-09-29 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| eae56634-ec1a-3a82-8e87-ca4921327da2 | -12.00253 | -50.9417 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3498c58c-21fd-36a5-aaac-25ed75e9bbc4 | -15.45344 | -46.13511 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1933496c-4220-3c66-9633-d4ab48e69e72 | -21.06297 | -48.83349 | 2026-09-29 04:17:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 39d51def-6b15-3ff1-8f44-35ac265fe8b9 | -11.41921 | -43.4547 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| efeeb7b3-767e-377e-8980-0ea8baa59873 | -9.30837 | -46.25534 | 2026-09-29 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73e9c027-0fc7-3204-bdf7-602bcd3dbd02 | -20.08254 | -42.21458 | 2026-09-29 04:17:00 | NOAA-21 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d9026c33-0b4b-3da0-a21f-9234d6539bd2 | -13.08924 | -47.44453 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48e30f18-7ce2-32ea-8f34-6aefacd7c227 | -13.14201 | -48.54856 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73933e68-f63e-3b6b-8924-f7a66a72402c | -11.98357 | -50.94708 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9bce869-5a78-3ca7-9ac3-ef02f250a7da | -11.53409 | -47.1649 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 644d7399-5950-325b-a637-ea8cc9b88a75 | -11.43586 | -43.45731 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7a62df3-f946-3187-ad74-5a736b0b9638 | -13.21057 | -48.56355 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0f77e24e-1663-3859-91eb-540924c7429b | -9.07149 | -49.87415 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9322d18e-24c0-360d-89b8-0118696fa8cc | -11.80653 | -49.05918 | 2026-09-29 04:17:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4be3a09a-767d-304d-b69d-88fb0cbefa8b | -13.86743 | -43.82316 | 2026-09-29 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a16b6b5-b4a2-3799-b469-c65476bc45cc | -8.65855 | -48.88463 | 2026-09-29 04:17:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f451aed4-b262-387e-b086-30c22ef244ed | -13.32863 | -43.94846 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34261fdd-250b-335d-8168-5a3c619c348d | -9.04729 | -49.63681 | 2026-09-29 04:17:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ad4c898-5baf-375f-a3fb-956c1a88bfe0 | -14.51614 | -48.29523 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 220b613a-fb1a-3237-8b69-0db4806714d4 | -12.01583 | -50.99294 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e0afe0a-8104-3f86-8830-d057b5c793b8 | -11.38325 | -54.0481 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f497f2f-8fbd-348c-b747-278f86326a74 | -16.0664 | -47.91634 | 2026-09-29 04:17:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aab8f5f2-31db-32ae-ac55-be4fdb7ee12a | -12.66545 | -46.98272 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README26.md)
