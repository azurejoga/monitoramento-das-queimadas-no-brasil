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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50c369d7-5bb8-347c-9a3d-09ba8f38e2bd | -6.01336 | -53.48235 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d08d197-a4d9-38a3-97c2-0d768f862215 | -12.84244 | -50.57948 | 2026-10-09 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f58230f5-da40-3c1d-8c77-6fa62912eef0 | -6.03539 | -53.48857 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3d54648-376e-3424-aa1f-91947eeb667b | -11.90737 | -46.56662 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| adf327dc-39c7-3d48-9334-19b1f0d9309e | -9.95697 | -55.33102 | 2026-10-09 04:27:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5968cf4-7a85-3352-9193-d662666fea0d | -9.86643 | -44.86773 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17b6e208-4f8c-35a7-a4e7-ce8efe471731 | -11.28547 | -45.20163 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d142894-9645-3996-9795-bbcb64e3b5c9 | -6.64776 | -47.91448 | 2026-10-09 04:27:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c20a79e0-7dc2-3e75-b942-cbe65bc3483d | -9.34865 | -46.58172 | 2026-10-09 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c91e16b3-fcda-314b-b550-3cf6bec73c40 | -12.8176 | -44.64261 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc082a58-7592-3b52-821f-a434e38acfb2 | -11.39175 | -46.67255 | 2026-10-09 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2297587-88c5-3fe2-8d5a-9925bfb216dc | -6.86768 | -52.18707 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1fb6595-c198-3bd2-9a6f-674f95a8e851 | -12.0029 | -43.47836 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc7e6e32-4379-38ec-a6b7-274416e3b922 | -6.11551 | -55.70765 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9edf846-1df0-3193-b5a8-a2cb9e36b9f0 | -13.26315 | -44.00328 | 2026-10-09 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de8e28ea-e57c-32b8-93b4-5e26a4c05221 | -6.10006 | -53.49879 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 871e0a3d-2126-380d-bef1-bef713918e10 | -10.40567 | -47.52826 | 2026-10-09 04:27:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec532b06-91ce-3015-a9f5-c94349494263 | -6.40298 | -55.27415 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 215f05f8-b1b1-3eff-9054-63e4356a3c91 | -12.2384 | -57.08763 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 85ed65f6-2aae-38d8-973c-6fad850e92bf | -9.92733 | -44.79353 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6da6a308-5c8a-3248-b176-3e6db85c9cd3 | -9.22433 | -45.66209 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c65bc77d-9427-3cf6-adf2-7fdff5200053 | -6.24468 | -52.85414 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 39d579bd-53fa-3c2d-ad70-9a455bece4ac | -6.456 | -55.49344 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7b976c6-deb4-3b98-930e-98cf5c925b63 | -10.87444 | -44.80431 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b0d7958-12a8-32bc-a680-d74e7a1cf99b | -11.59856 | -43.71254 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6d62a4e-60f7-31c8-b030-9f301249dee7 | -9.26729 | -47.45169 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 798ab3ac-42dd-3450-ac59-fbe918cc57e7 | -7.81808 | -44.57235 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 909a5d49-e6de-3d17-8c7b-7628959367a1 | -14.39903 | -43.81264 | 2026-10-09 04:27:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4d2fa1f-5d5b-33c1-9e3f-b4777336a706 | -6.32787 | -55.32902 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e73b304-29b5-321e-8cf6-052158462ede | -7.48596 | -42.79198 | 2026-10-09 04:27:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 992362d2-8900-36a8-9be4-8efd170a5166 | -11.77769 | -45.56508 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21a468f7-60c1-3952-8ee7-50c21dac68e6 | -9.12774 | -45.84602 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a2dff24-5269-30e6-af05-f0b299ac60ef | -11.62427 | -43.6998 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b3f22d7-a8f1-314d-8098-a27cc7ab67ea | -13.25279 | -42.25112 | 2026-10-09 04:27:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 36.9 |
| 0f9966c4-484b-35d6-afb0-80e24f0c786e | -12.00602 | -43.48404 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cb6b77c-43d0-3008-9dbf-2febed647902 | -11.76422 | -46.7927 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6e95dfc-969f-3ba9-b593-5118868d2716 | -7.23708 | -46.00333 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 802d9fb6-df46-3cb8-8a37-281a30ad8a00 | -8.13197 | -49.44803 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eda53993-8526-3a3c-93a9-dbedd5805904 | -12.20691 | -57.13666 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7890d017-5189-3683-9191-0d3a0e26a90f | -8.72735 | -45.14877 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f029e757-bda5-3cda-b48a-924b5779e719 | -8.0743 | -45.64381 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 104ac22a-5a4d-3ce7-b59f-13b94409d457 | -7.40456 | -55.14973 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42faeae6-f7bb-35e6-bedd-beeb98936fcb | -8.73583 | -45.13868 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| be5f53a6-d9ff-376f-af66-144c58bf9ba3 | -13.87911 | -43.80223 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97411104-877a-3358-851b-aed659222855 | -11.32633 | -46.65503 | 2026-10-09 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aac2263b-99b9-37ee-8bb4-4eb7a4dd74c3 | -8.90214 | -45.24717 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c36a7e0f-e9b8-30fb-96a0-40f7c6d74174 | -6.9813 | -46.05228 | 2026-10-09 04:27:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 510a5b3c-b956-3723-a389-c109f9e26a7c | -8.24899 | -54.72512 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46243c4b-c3ce-31b6-897d-61bafdbf50d1 | -13.15448 | -54.34626 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 09827e4d-04e6-329b-be6c-14e877cc5856 | -11.20375 | -49.41285 | 2026-10-09 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d847195d-652a-3b70-afa9-320efcabc06b | -10.90742 | -45.52429 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81fd1eea-6c07-3047-a23c-c70a003e623c | -9.29806 | -47.42807 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 15511a94-da52-3888-933f-f17b936b4070 | -6.23612 | -52.87962 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d98077c-3471-3923-9e1d-9684e58e4545 | -10.27998 | -47.82934 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a5cfbc3-3d57-393c-8d97-2dd3e4d08f7e | -9.45144 | -45.8629 | 2026-10-09 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 924e7170-29db-398f-b50b-8556456d8d01 | -9.2278 | -60.87351 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e148fc0-e083-303a-abb3-81109c90c162 | -8.30292 | -54.70151 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3007f88a-5b96-3fe0-a926-8577b05176ea | -12.21399 | -57.10637 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75e84011-aff8-3186-8476-6e9d5b2e6a54 | -12.21993 | -57.10392 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| a74da3bd-5c38-3276-af0d-5cfd8b8dcd4c | -7.30038 | -43.9861 | 2026-10-09 04:27:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8ca395d-5695-3def-9c67-63e890d94bd6 | -7.34167 | -45.30444 | 2026-10-09 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94d5fc93-2d2d-3d07-9ba4-874ad2e7cfa5 | -9.12584 | -48.51817 | 2026-10-09 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81585f8f-f4c4-349b-a2d2-add2dcff8a9f | -12.21482 | -44.61844 | 2026-10-09 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ec13328-f093-30ec-89eb-2aee31f49589 | -6.47578 | -55.47344 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a032653-153e-3eab-9b19-921664837db0 | -8.97051 | -45.16291 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e208c51c-3c3a-36a9-bd1b-db9f33b20e3e | -12.01499 | -43.47565 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db86abe1-fecc-3aee-b639-531392cb7bfe | -12.03893 | -43.44424 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1919842d-c021-3e16-8952-3d863b1476a7 | -11.65631 | -43.6901 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8b6b8f80-229c-3b7c-b65a-ee6311ea5872 | -9.22542 | -45.65489 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b31468e-5e87-3f00-a5a6-24765601cd03 | -12.2523 | -44.75504 | 2026-10-09 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f995d4e5-9a47-37b0-8ad4-a8b1fa47bdb5 | -8.18099 | -46.39021 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db1d348e-456f-38dc-82cd-380fb46ed2a1 | -5.99172 | -55.36733 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be3f9144-f94f-3bd6-a85d-50666d0133e0 | -8.91321 | -45.17315 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0a05f09-8611-395e-98c1-216a5fcbb226 | -11.19733 | -45.31833 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab4b08ca-28bf-3bd4-9487-30041eee9af9 | -13.1639 | -43.27663 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b640df59-25ad-398a-b9a3-2f1067b9e2bb | -8.7336 | -45.15351 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1395f590-d62b-3f87-98db-cd378c5efc04 | -11.97503 | -57.61678 | 2026-10-09 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2e95c49-73dc-318a-b286-e07f04dcb158 | -10.77126 | -46.5497 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37843c32-bcc6-3e2b-8c50-8aa21424a613 | -7.47785 | -42.84677 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7bc3df7d-c71e-33d1-a462-527ba1b0d885 | -10.57676 | -46.28972 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cf48b999-5af6-3d0e-9661-6edd92f47fa1 | -8.07095 | -45.64331 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a746f648-9068-3381-bf0d-1d62fe254049 | -6.43908 | -55.03974 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24ffcdc9-3589-391f-a318-ea3588ebe034 | -9.87798 | -50.51443 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b55f5b2b-7ea6-34b5-a751-1799b58fc704 | -8.9694 | -45.17026 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 41efac22-5291-352d-a93f-7954952b604d | -12.00943 | -43.45951 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46d32d14-204d-3cb4-954e-38b52fc0cd08 | -6.318 | -55.32412 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f60133b5-441e-31ac-9fcc-0754766f76f6 | -11.4597 | -43.38208 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c1f04bb-e46f-3326-98a3-340560f047c0 | -13.17505 | -54.3401 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c77b40c1-39b3-3e8f-9352-5aec4f061911 | -7.28549 | -46.15313 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 222f0291-8745-3622-9e6b-a97b1ff3f033 | -11.31586 | -44.82925 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| e1bfd6c8-a15c-3556-b182-f005c9640e39 | -11.76808 | -44.95445 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 59b4e161-ea85-3cce-b20d-87a1e51e8a0b | -11.76863 | -58.28392 | 2026-10-09 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51a4d12c-80da-3e17-b8a4-9b5035edb232 | -13.17624 | -54.35789 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8d55edfb-9b36-37ba-99f2-97c4cb98a946 | -8.80349 | -47.58785 | 2026-10-09 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb61b726-666d-35f3-8213-0ab89fcf7f50 | -11.82855 | -43.59315 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 607cf6c9-c9d1-3633-a729-c1ce7b15cb1b | -7.07411 | -47.39602 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a61626c1-7ac0-3427-a8c6-926dbcd0f859 | -6.53902 | -56.04097 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a170c6ad-d28c-3af7-ae8b-6ba7369b5c40 | -9.27059 | -47.45222 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 93dee1ff-ee7d-39f0-8e18-7341a05ef3d1 | -5.98281 | -55.35637 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 198e9050-c6a2-3dc4-9ef8-123f60f067ee | -12.20942 | -57.09588 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README108.md)
