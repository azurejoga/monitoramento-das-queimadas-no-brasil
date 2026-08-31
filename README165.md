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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 448a4795-d0f0-3777-921e-691960ad2764 | -9.21014 | -60.90123 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 028ca989-7437-3816-84c7-40019099a2d6 | -7.82625 | -44.47435 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7e3f3262-63ce-3f7b-9e8e-ce0289687435 | -9.66159 | -48.28591 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6f25ec0a-2fc0-3328-9932-79e85c7cc6f0 | -11.18839 | -55.08968 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5338aa2c-0fc6-3d67-b670-c70bc622a846 | -8.38459 | -44.99743 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 716c5974-b60f-3d11-a788-537075bc07bf | -11.68061 | -47.59866 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6b846ae5-f74f-3b55-9eda-d64a37caa770 | -13.97883 | -54.41038 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b12a6713-bfb3-394c-9be7-ab9d392a5928 | -11.24831 | -45.35312 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d2f5336d-f440-301f-b281-5cef04d5d0a2 | -13.84834 | -54.08644 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0fe9072c-a82f-3b9f-b2cb-a0f696378cfc | -7.96273 | -43.86441 | 2026-08-31 16:50:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a293628c-8a12-3ca3-ac16-4779c1397357 | -11.37858 | -45.17486 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 63d731a4-0a86-33ca-b441-f3806727a107 | -11.19571 | -46.11755 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 869bbe14-fd54-3e79-939a-1e23828e2f75 | -11.24005 | -51.25809 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| deccd463-8979-3622-a1ad-8c6c3e32a2c2 | -7.94516 | -44.24668 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 91696df6-7a94-393c-8af7-40ed90a9de8c | -9.21532 | -51.57834 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 28ab77f4-0706-31f4-83ee-c0dcc7ddd34d | -12.89417 | -45.84333 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9a87785c-622c-3513-bd93-0b88f00a8087 | -12.10316 | -44.99741 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| db410769-009b-3298-9bab-b385fdd6a48e | -9.65455 | -48.26202 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37ce0b30-e257-34ef-8b8b-83c6d694a48d | -10.14867 | -45.77039 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e32f6fc9-c05f-3bfb-8e7a-9341fc929969 | -7.00724 | -52.8921 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c7dc0aca-574f-3c5a-a9c3-a9482cd8ff2d | -9.15422 | -59.5438 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 87eeeb29-7285-384c-968f-da74ea35cc2a | -8.90119 | -57.25669 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 25fa44e9-17d8-332a-b61f-af2a4c77cb7f | -8.24547 | -49.88947 | 2026-08-31 16:50:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ae4992e8-e44d-3777-94c2-38d1fadb1b11 | -13.42691 | -51.69847 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06f647ec-91be-363a-a6a8-e054dc9db95c | -13.43421 | -51.69996 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 18c46e3f-85b2-302d-a19b-0f46931795e2 | -10.34088 | -49.96111 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| eea7f16b-a0be-3e68-a88b-4ae909c77f81 | -10.4963 | -59.60328 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8540fb1c-30c2-3523-81cf-38b9dee2614c | -11.96135 | -47.74773 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| fb1fa79c-9084-3166-8c7b-87a13d70ae68 | -9.93438 | -48.33791 | 2026-08-31 16:50:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e19acb62-7eee-3cf6-bc5d-1a0eba6e2510 | -9.66106 | -48.28242 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a0598fc9-ce98-366e-a33d-6ad1b869cbbb | -7.60126 | -44.99557 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 05557bd6-55e6-39aa-b7c0-f9c51fc75ab4 | -7.521 | -44.45419 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 67261095-1539-3187-8dda-e002c1b258b8 | -11.20912 | -45.33451 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5dfd19cb-65c5-3aae-8520-34da2faf147b | -7.60919 | -46.1947 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe3fd0c7-de23-36aa-b964-38eeab6e2a48 | -5.90404 | -46.12968 | 2026-08-31 16:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 86e06c5a-9d6e-33ee-8248-91b12d578637 | -7.3615 | -55.19638 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 85a5a0aa-f6ff-318e-83c4-928893ba77e3 | -9.8351 | -46.35834 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4b75cea2-7e61-3edf-a6eb-8db41962b5c4 | -8.77033 | -46.45287 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3abd665d-0747-317b-b9f8-8e2621c53255 | -8.369 | -57.67565 | 2026-08-31 16:50:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2d9a8d96-f9b3-3cb9-a6f2-4cb722b78cf7 | -10.62434 | -48.68227 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 66304521-a8ba-3fae-b4ff-aaded2939bce | -7.21573 | -42.74259 | 2026-08-31 16:50:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| bd86bf53-f33f-3ab3-b522-68ffc72d254a | -12.07629 | -44.9854 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9d739705-02e9-3f80-b0ec-64483be0b515 | -10.96236 | -48.40577 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| aa159ccc-1147-3d10-ae61-471fc123db9e | -10.86824 | -50.4787 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1f46b35a-d0fd-3319-aa4f-1869e575ce5c | -11.93781 | -45.07101 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 7b9b6ef6-1f2b-3a35-b175-10debc48fb57 | -10.39911 | -45.08202 | 2026-08-31 16:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 962d368e-2e01-3859-aa6e-9c04945a04ab | -13.46074 | -57.03769 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ec1f2e69-1f7d-36f5-a987-859d3102af43 | -11.83512 | -46.75425 | 2026-08-31 16:50:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 94659b95-f876-37ed-b35f-66ddf25d10d6 | -7.64878 | -46.7169 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3767b88f-8c30-3ebf-9d62-04b4cbb70fd9 | -7.13904 | -44.30605 | 2026-08-31 16:50:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6c9bb3a9-cd5a-358f-a833-c6cd89b44636 | -9.66425 | -50.85786 | 2026-08-31 16:50:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 6aad6eec-22f0-3ced-8f05-d076e98e7501 | -7.43534 | -44.95115 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6fd163fb-8e3a-3600-a51e-641313c828ae | -10.30728 | -49.99268 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8f944872-ffb7-3702-8df9-f577bf4c2be2 | -11.6723 | -47.61078 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a601024b-8e66-3d5e-b1dd-cf09b30cbe8e | -7.79723 | -44.07821 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d0996a8a-f034-36e4-8d31-3c1532e19bb6 | -8.14136 | -45.58119 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 86b669b2-10eb-3f9a-ab80-b456473cfebf | -10.11334 | -50.31678 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 6fc90089-b146-3072-b431-2e45c03f98be | -10.83044 | -47.23539 | 2026-08-31 16:50:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| edd47979-cedd-30ba-9c2c-234a7cf7c433 | -10.45098 | -46.74746 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 6aa2fa9e-ffd5-354d-9e27-f586018ee141 | -13.42914 | -51.69099 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4688b9be-8aac-3845-ac39-ca856f60a1a1 | -9.66774 | -50.85735 | 2026-08-31 16:50:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| e42f27a3-54d0-3f67-ab52-be448e55c62b | -10.85837 | -50.48415 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a1bcd028-b243-3c25-b150-c222050fd463 | -12.10193 | -45.03148 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f047e08b-f164-3bf8-a36a-0b0beaeadc5e | -9.46753 | -48.19181 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 41113d4d-f1b1-35ca-aa21-2e30f58f2fec | -10.98988 | -49.68531 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b49fec74-0f8b-364d-aae9-8d0a470bb21b | -7.92897 | -45.00714 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| a84ac2dd-c2f4-33b2-b527-9660e9a7420b | -12.0925 | -44.99563 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| ea3dbc77-be50-3caf-af02-523a432f278d | -7.41471 | -44.24796 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2a255331-42b9-3bb0-83ee-31b444c04ddf | -7.9162 | -44.24096 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 544af097-3655-3bbc-8289-fb4409a53fe9 | -7.64893 | -46.74018 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 59a8cde9-215d-37ce-8279-7af73887bdff | -12.95937 | -45.94348 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| ffaed9a5-7e4a-3b79-a498-e7c410465880 | -7.92321 | -44.23484 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.3 |
| dedeb0df-cced-30bd-b7f4-48aea9e647ff | -11.2396 | -45.142 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f5e0c78b-ba01-3efc-9509-b3979c52a466 | -5.77379 | -44.12713 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b5ce5473-a3b3-37c3-b792-fd2f141abf92 | -11.23605 | -45.1426 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 794fccb8-028f-3228-83ab-ee89730a4c04 | -11.23317 | -45.14735 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 1eae1a30-46c7-385c-9a83-15bd2e335156 | -10.62381 | -48.67876 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 356dc42d-14fa-3d0c-bb02-2e38bdc12b68 | -6.81055 | -43.5334 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 46cf85dd-6016-34f0-b345-2bebca9997c0 | -12.11135 | -45.02486 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 31c9349b-7c34-3650-b4e9-f482b87a3414 | -10.99388 | -48.39011 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e54e8920-09a6-37df-88d8-0cc7939725ae | -11.71081 | -47.64064 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4dcf124f-7e56-3909-a15a-95b93ce2d3bd | -10.09867 | -50.28811 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 37d23ec8-a9f8-3406-9ae8-52b2a447961d | -6.87191 | -41.6535 | 2026-08-31 16:50:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 59747467-1130-382c-816b-9582cf11e2a6 | -8.82929 | -47.94841 | 2026-08-31 16:50:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 901c9401-6d79-34a7-b18e-bc62294b1fd7 | -7.99915 | -44.32694 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 797da698-a144-3f1c-bd1b-363a318481be | -12.10479 | -45.02671 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| debf5a1d-026f-33eb-a042-ef4ca7ee4735 | -11.3359 | -45.15623 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 59936494-f404-3856-b836-9e35db8496af | -12.09936 | -47.25501 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 82b6111b-3894-38a8-afb3-d26f60023ee4 | -11.91584 | -45.07006 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b8ad40b6-fa84-38ae-bf09-11fd120d0076 | -7.62251 | -44.93635 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| e5cc20b3-0a1e-3770-aa0d-31e625972736 | -11.69219 | -54.54766 | 2026-08-31 16:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b9d66f23-a7d9-3de3-b418-562c831c7e90 | -7.52649 | -60.7599 | 2026-08-31 16:50:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c4fa8119-d382-3826-a4ee-3180bb32e37e | -13.46939 | -51.87607 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4acb636b-e534-30c3-a590-d44135b590bb | -10.25262 | -42.46101 | 2026-08-31 16:50:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c54b53bc-b362-348d-b813-685dd8fd1e36 | -7.26609 | -45.35153 | 2026-08-31 16:50:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| db0ddc87-7a5b-349d-9e3d-2b10c8b741dd | -10.0951 | -46.60302 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9da68a33-3157-3b1b-9360-c6a1862ccb7c | -11.37692 | -45.20876 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 81e6e302-b13f-322a-8cae-527ee1f863d1 | -8.37997 | -45.76052 | 2026-08-31 16:50:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bfee5719-9dc8-3681-be8e-efb452623dd2 | -7.77324 | -44.05569 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 72c4f6a1-9390-3ac7-9142-ca5fb2b15fc4 | -7.58386 | -61.35451 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |


[Clique aqui para ver as próximas entradas](README166.md)
