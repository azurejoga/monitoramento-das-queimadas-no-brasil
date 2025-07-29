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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccd44fd3-6be4-3f06-91b2-0a2249337d9b | -22.53129 | -43.56573 | 2025-07-29 04:53:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 82433d13-8f6e-34fd-8c5f-0b334050d69c | -22.53164 | -43.56166 | 2025-07-29 04:53:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| d4ade696-f4c8-332c-9ba6-1bb832d39e1d | -22.52618 | -43.55607 | 2025-07-29 04:53:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| a82f45af-a055-36eb-a8a2-ab078303e0ce | -21.33381 | -55.63485 | 2025-07-29 04:53:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7caebf6f-00f5-39ac-b22a-a2bcf349fdfa | -21.33717 | -55.63548 | 2025-07-29 04:53:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d68c1da7-c1d8-3c07-826b-4c935b9fe81f | -11.4389 | -45.1385 | 2025-07-29 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 080cdc63-6339-31ba-856d-3ba111ddafc9 | -11.4197 | -45.1412 | 2025-07-29 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 69eaed74-880a-3094-aeec-d25908c98f00 | -11.4393 | -45.1154 | 2025-07-29 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| fa1a7f8f-057a-37cf-9be9-774d34279942 | -11.4201 | -45.1181 | 2025-07-29 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 5ee18fca-bf85-350b-ae0a-5722131ea88a | -3.11121 | -46.80143 | 2025-07-29 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d675326-3960-3667-b952-b937c542b7d2 | -4.59683 | -43.30803 | 2025-07-29 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6ec4e7c6-4983-3aba-b562-0bce54040121 | -1.55775 | -55.02453 | 2025-07-29 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fac2e1b4-28a0-3a10-ae44-42c94cf3c47f | -3.08778 | -52.92595 | 2025-07-29 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e5d3f4e-6cbf-3e41-a95b-71dc66706032 | -2.89887 | -48.28858 | 2025-07-29 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2847231d-6097-3910-89d0-1e675b7c5c41 | -2.89798 | -48.29462 | 2025-07-29 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 03db5ae8-24f5-387e-b296-6a995048a373 | -3.27682 | -49.14279 | 2025-07-29 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 388a0c13-c966-3123-ab99-0bbf26c7d839 | -2.90351 | -48.29234 | 2025-07-29 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8ee63920-d816-341c-a00e-43071a50d239 | -3.25319 | -43.26521 | 2025-07-29 05:08:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a845e2b-b234-34b4-89c6-86ef180e8f7e | -2.39102 | -47.6246 | 2025-07-29 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d211162e-f098-3a3f-862d-a4c110188598 | -3.11177 | -46.79757 | 2025-07-29 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcf0bee7-bfdc-399f-af14-0e17b61b7d8f | -3.04219 | -49.42483 | 2025-07-29 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88ac96fb-bc1c-327f-a9ad-1bcd21948c7f | -3.11385 | -46.8027 | 2025-07-29 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aeceac9e-1f23-3e26-920d-118072814374 | -2.49959 | -56.08097 | 2025-07-29 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a429021f-11dc-3487-962e-2742ac1bc778 | -2.89333 | -48.29083 | 2025-07-29 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9e0b211-abce-355b-a129-b1c57acfde3d | -3.11444 | -46.79886 | 2025-07-29 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57da775f-1963-3af0-b93d-89edc0b31869 | -3.31605 | -48.71904 | 2025-07-29 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02383ef4-a5ca-3339-ba6d-a5566f5ac35c | -2.39631 | -47.62537 | 2025-07-29 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4888a83-6933-34f4-a623-db9aba13b824 | -2.97726 | -54.50754 | 2025-07-29 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 067fbbe2-6da0-3ff2-a3ee-057b84a9631c | -4.60014 | -43.3107 | 2025-07-29 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 19ad340e-0acc-3fcc-afe2-bac7a2695280 | -3.32017 | -48.72542 | 2025-07-29 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 380f46c2-ef39-3e37-a135-136df7ef7c6e | -3.27603 | -49.14802 | 2025-07-29 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bd269a0-628c-3fcc-b4ff-eab46a24ac9e | -2.77383 | -49.19871 | 2025-07-29 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 304d86d1-8010-3cb4-a91d-5e609b06c3b1 | -2.90307 | -48.29535 | 2025-07-29 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6ba84bbb-2a31-3ec0-b964-e513a2383830 | -2.89842 | -48.2916 | 2025-07-29 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cad2eed7-2932-37fe-ada9-5607a2e11c21 | -3.08847 | -52.92146 | 2025-07-29 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b53c4a7-2707-3025-b196-2c2eddc390e5 | -2.83011 | -52.35735 | 2025-07-29 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c7c2e7f-29f7-3b55-a5c9-0eb3680e6080 | -2.83397 | -52.35792 | 2025-07-29 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eab74363-d107-3cf3-b6a9-e4124a96dc02 | -11.4393 | -45.1154 | 2025-07-29 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 9bb46804-483e-35ac-9f87-4fd9b6169fa3 | -11.4197 | -45.1412 | 2025-07-29 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 7cbb9acb-febb-3c25-8bdb-d2c2d4ab86e8 | -11.4201 | -45.1181 | 2025-07-29 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 3ccdb93e-0d6d-3105-a291-0ecbab24cfd2 | -7.8022 | -44.9566 | 2025-07-29 05:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| fd367763-d498-33ac-aee7-c618bd376cc1 | -11.4389 | -45.1385 | 2025-07-29 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 114bc63e-f13d-38a5-91e4-0e6a71fb2fac | -6.38294 | -53.34332 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9795976-f125-3204-ab2d-eec3ca8ffa8d | -6.39057 | -53.34449 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d895e51c-5c9a-3fe2-990d-d5bcf44c641e | -6.39921 | -53.36485 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b37258c-8785-39fb-8dcc-8b33e34be1c1 | -6.39197 | -53.33508 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 417271b7-ec34-3268-9fb5-145e209b2edc | -6.40241 | -53.31742 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96030f27-515f-3ce3-84aa-3aba52fdec0b | -10.23635 | -47.75062 | 2025-07-29 05:10:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a8aa2b9-7230-33c9-9781-aab266c9afe3 | -7.92917 | -44.08943 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 77289eb3-82f6-3ff4-9905-bb09be0edfa6 | -6.50406 | -56.20966 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14a13e95-2dd7-382e-80ed-067009e4133b | -6.401 | -53.32684 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc350388-534d-3109-8597-19c689701e89 | -6.40171 | -53.32213 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d2aafd3-8e5e-3b00-9056-c8e0e2cbebd8 | -7.92458 | -44.09687 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 805d3ff1-2ae1-3d8f-a9a9-668666ba14d1 | -7.73442 | -51.10324 | 2025-07-29 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd9d4464-e94d-32dc-ae3f-3d8f5a173191 | -5.349 | -45.27518 | 2025-07-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bf7f735-0413-373a-abfd-fa025af82c31 | -6.49454 | -56.20452 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 571ad80d-24c4-35df-bcdf-02f2bf1f7552 | -6.49118 | -56.204 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50c7fa9d-7210-30f3-a671-a800b84e8c4c | -6.95864 | -58.37721 | 2025-07-29 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e052a23e-6e82-357a-904c-c2be5ce1aedd | -9.99893 | -48.13055 | 2025-07-29 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2f42e36-21bb-3d2c-9827-3b89183238f5 | -6.41655 | -53.35316 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfbab684-0c09-3898-92d2-b103c21c8412 | -3.88458 | -54.21322 | 2025-07-29 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac6df92d-9f5c-3d78-9970-df9513ab808f | -6.63781 | -58.85441 | 2025-07-29 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7b085d7-b940-39b2-ba0d-494dba996908 | -9.86819 | -44.69577 | 2025-07-29 05:10:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 641ae1da-8064-3c7e-89ca-31e44a39adc4 | -6.52476 | -56.20919 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 858fef13-650f-314f-bc72-0e71fc89fad7 | -6.38886 | -53.32977 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2a134e1-cf68-3564-b3bd-d41e8787359f | -9.36177 | -45.73888 | 2025-07-29 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a899c90-aaca-3503-9015-c27f95a473e4 | -6.38364 | -53.33865 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16342be0-acf5-37b2-99c9-0a7c205d2f9b | -7.86137 | -47.87598 | 2025-07-29 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afb45fc5-23eb-3029-8210-6f7fcd134c9d | -6.38815 | -53.33451 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d27e973-83d8-35f9-a189-a7b5936f6ee4 | -11.73994 | -48.18737 | 2025-07-29 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 689844c2-ea50-3266-8d91-b27bbe3191e7 | -7.93364 | -44.08278 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b8b2f7f9-9b06-3f11-81c6-d022ba24a436 | -9.46138 | -57.84628 | 2025-07-29 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2bdee6c0-4561-3a31-9d60-96515f922eff | -7.92293 | -44.08134 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4e2cf397-757b-3c7c-a65a-67df034fc763 | -6.39368 | -53.3497 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 204c464f-2b3d-3db5-a8ae-c91cf2506631 | -9.22124 | -48.59748 | 2025-07-29 05:10:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c609888c-7521-3465-a830-17dba9a026bc | -6.44958 | -53.36026 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64e7b2b0-82d9-3578-bad4-0a1fc03b74ab | -8.66351 | -63.85299 | 2025-07-29 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aace80aa-b82c-3e37-b4d0-cab9aa032909 | -8.95404 | -46.75378 | 2025-07-29 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 80cf760a-324a-3e64-b41a-e3ad7593729c | -6.45015 | -53.36289 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f52c855-8408-3228-a5eb-1957118d011b | -6.38434 | -53.33393 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 499bc6fb-0c94-3dd8-a81b-f7a5387aa0d9 | -6.63446 | -58.85386 | 2025-07-29 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ea4c327-46af-32dd-9415-0d356eacdfa3 | -7.81213 | -50.22296 | 2025-07-29 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17ad67fd-4470-3b46-a9d6-659798ba6c2c | -7.92826 | -44.09684 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec802c8d-9ab0-333a-a030-70b8bc0d3806 | -6.50181 | -56.20198 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dbfbac3-0c9d-34c4-beb6-7aa443ba339d | -10.55165 | -50.24582 | 2025-07-29 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4b44301-ec94-3d5c-86d4-f115b41ee568 | -6.39578 | -53.33566 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efa23468-f6d3-3724-80dc-9c37e7a7cda1 | -7.93264 | -44.09052 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fec87291-bf02-30c5-a076-07286714ac5f | -6.38155 | -53.35271 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4424fba2-7105-3155-ba84-ae9f24a3e466 | -9.45422 | -57.84872 | 2025-07-29 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 033110b5-551f-349c-a947-27b356556f1f | -5.99425 | -52.20161 | 2025-07-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bce6cfaa-b68b-37e1-a442-0343aa8a8213 | -6.49623 | -56.21577 | 2025-07-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf0a8ac5-e513-3a35-9a0a-64c09cf67ecd | -6.41584 | -53.35785 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aaed926f-43a0-3932-be3e-1e14624d393e | -6.39438 | -53.34503 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4360f3aa-4635-3127-8286-cfe7d51c5c9b | -9.21578 | -48.59669 | 2025-07-29 05:10:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 526661b1-9a87-36b3-8007-c17142358775 | -6.39337 | -53.32567 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54616c59-dba1-383a-9660-e697daf447f2 | -6.77396 | -50.49009 | 2025-07-29 05:10:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5cb0939-f6f4-3ce9-aa6b-09fa51d00818 | -5.9907 | -52.19744 | 2025-07-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1faaf106-d7bc-386b-a9df-fdb0a88fed7c | -6.40623 | -53.31801 | 2025-07-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d16193d2-074e-375c-86a9-1012c635976f | -7.74344 | -51.10443 | 2025-07-29 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebb81a49-231e-3fd4-a103-bd72da69ef00 | -7.93169 | -44.0978 | 2025-07-29 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |


[Clique aqui para ver as próximas entradas](README21.md)
