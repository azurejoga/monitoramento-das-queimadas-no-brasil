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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e2242b6-0f35-3255-8c9a-4f26b6425ff9 | -2.23092 | -46.42323 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04af1fa5-19ec-379a-b7dd-e52855516cd9 | -6.31534 | -42.75296 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6567fe4c-73ab-364d-b75b-0e3eb1fddc5f | -1.31771 | -54.63893 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec88d25b-bca7-3858-8aa3-58babb16ce63 | -2.87407 | -50.41882 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c26208e2-00f1-3752-b18b-c44f31b7e11a | -3.06228 | -51.38242 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a295a30f-b95e-338d-9ae8-0d0a281c3655 | -1.93282 | -52.17004 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb9ac68e-9298-312d-b716-ce23b4d51b77 | -4.92613 | -47.6393 | 2024-11-10 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f33d4fb0-69cc-3336-abd6-f23e9ab32354 | -1.97656 | -52.06853 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d2b9b79-1735-39e0-a6c9-c1195ab96c07 | -6.09841 | -45.53734 | 2024-11-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d80a1b19-845a-31b8-925f-378b8af1c0a0 | -3.2284 | -50.44817 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4f9376e-0f10-3d4e-a255-66eebc1f2946 | -5.07435 | -46.05716 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a89b1413-2127-371f-a5d6-d60939c1edfc | -3.10724 | -45.78031 | 2024-11-10 04:14:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad94bc14-d54e-371a-9160-c800264b6de3 | -2.37514 | -46.73774 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea605ae3-e62f-363e-b7e8-6e9d004bcd9d | -2.89716 | -49.25956 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81f99c91-5cfe-3113-b6df-b4a0e6cd50ad | -2.61844 | -46.16367 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f46d1cd7-fe90-3669-a5ec-4600959ee2e1 | -2.10245 | -46.54998 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c8b2980-f700-3d37-9971-cb498848e6e6 | -2.04561 | -46.53636 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad80f518-7a24-3264-886c-fe221ca55c11 | -2.62646 | -46.13773 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a6acf1a-825d-34b4-901c-6b6d28caf6fd | -4.17086 | -46.59594 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34311d1c-8a80-3b6c-a351-3476a961d288 | -6.15726 | -43.071 | 2024-11-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 731bd4d2-629a-3435-a059-6f39a6f90042 | -4.61327 | -45.98824 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a65e2319-db80-3db5-9b1e-9b208c4115fa | -2.86923 | -49.51488 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ed5e2b31-0308-340a-89da-44a8566716dd | -3.23476 | -50.30652 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 7f15583e-0c5e-351e-a4cb-352b8c6226dd | -2.87989 | -50.41404 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ad64a9a-c7ac-369d-bdb2-92584581c758 | -4.41374 | -50.08323 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| beaecd31-8597-3ace-b531-06ae652721c5 | -4.36538 | -48.15209 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e79f57d0-ddfe-3242-8265-6f7236b52605 | -2.67896 | -51.82532 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19a22ee6-99be-3a3e-a0fc-b0de1d450b13 | -2.87468 | -51.47474 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 1f770bed-00d0-36e8-810a-9e8dc2d548fe | -2.18001 | -46.42474 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f8ef6de-4e7a-3406-8ded-55ef209eef9d | -2.87046 | -50.31731 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62817460-19b7-3086-917b-285cd08ee25e | -2.83689 | -46.63981 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 493ee1e1-5555-391b-90b1-9eb599ae3f45 | -4.08646 | -42.93191 | 2024-11-10 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c457cad1-b39d-3a1e-b1fa-97e0b395a638 | -3.53234 | -50.32639 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee526a0d-0277-3e20-a52d-8ce23ffd64f6 | -4.71762 | -50.85158 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 715fe0ba-4a80-3f28-9e6b-4deb85a865af | -3.54557 | -49.97888 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 584fc828-9980-3353-b000-62dfd940f492 | -2.68112 | -51.82243 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5755c5d-b229-31ca-a3e2-b66a51e1c958 | -2.89938 | -49.38852 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0cd42e1a-5f0c-399b-b73c-24c8bd551c82 | -2.91526 | -51.67923 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f9ea654-d926-38bd-99e2-7650a50615ee | -3.78407 | -47.46244 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e078c10-5b47-36b8-b04b-415f3a707efc | -4.2582 | -45.85605 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 031b03a8-2828-3ecb-8204-b1e712edbafd | -3.0937 | -49.40993 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c387199-b166-30ae-ae6e-3c30fe035134 | -3.11775 | -44.99485 | 2024-11-10 04:14:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3c8e66a-6518-35d0-a5d5-2b4993b12f39 | -2.61631 | -46.16526 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9236257-3f66-3cea-94ed-24dbb3e31334 | -1.97788 | -52.06873 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1f01874c-ab75-3784-83ce-a079f209a084 | -4.40579 | -41.90754 | 2024-11-10 04:14:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9783773d-7272-3a4b-9c7b-95e8294d63ce | -2.89199 | -45.36949 | 2024-11-10 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e87f61d9-8268-3c49-9236-7e9cb257a908 | -3.11836 | -45.97273 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19e08141-b53f-3a00-ae34-c2dd26957501 | -1.53687 | -52.21374 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4a574948-b11c-3776-9b4a-e32df672362c | -5.1471 | -47.71613 | 2024-11-10 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47e83d3b-9341-3338-aab5-895d891c6dc8 | -2.23013 | -53.77978 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23b4c196-34de-3ed3-876f-b1d7673bce89 | -3.04765 | -49.55045 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1c1cf225-cd21-3f2b-ba58-28721587fc16 | -2.43406 | -48.46992 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c72f94e1-9e45-3019-8cc7-93244ef8f069 | -1.95818 | -53.07011 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be06098c-a019-3526-973d-a479bca9c849 | -0.86311 | -47.29871 | 2024-11-10 04:14:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d1b1ccb-aeb8-3795-8056-21664f10638f | -3.95289 | -48.99406 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 385d6a74-4c45-30fc-944b-b04079694efa | -4.19925 | -48.54914 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 337a8437-8050-3697-9287-fa10b4ec4e22 | -2.69333 | -46.81025 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e36fd420-47a2-31bf-a459-9c8ef5d6e608 | -0.14638 | -51.56195 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3740c722-d051-3176-9169-43cb0103b03a | -3.95537 | -46.70811 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ba1e3f9-881d-30b7-9432-362e5890d48c | -2.22669 | -51.99651 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c80e3b4c-b92e-36d0-9f15-09918db67abb | -3.2369 | -50.32336 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f14bedc8-18b9-3b87-8da7-6aad3cc9fa02 | -1.23612 | -54.15876 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de0f1e89-0216-3057-9398-60dc2eada4d0 | -6.46447 | -40.78223 | 2024-11-10 04:14:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dcdf5fbe-6064-335c-b16e-795b1cb67ac6 | -2.6469 | -46.80307 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97f285f2-77ff-3b60-a7bc-0dddce69ac68 | -1.16517 | -51.91948 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5f78e41-915f-3e2b-b920-52ccad4e6dd8 | -2.31459 | -50.66883 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d085deee-2d91-3180-93d4-91138a1d9d25 | -2.89756 | -46.81752 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 680eeb4d-7670-35b2-92e7-b9902b9ebcb8 | -3.25082 | -53.40462 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 46b9a4b3-3c89-3ce6-a0f9-d77750fb8857 | -3.03386 | -50.30376 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f2730240-0b6c-3be9-bdf6-6ecf9ca2b0f3 | -4.69349 | -45.74129 | 2024-11-10 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1da06c65-c146-38d7-97e5-c7bb3fd6e5df | -4.2618 | -45.85653 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 588e884b-5808-3a2f-9f3f-1e074ec278ec | -3.06139 | -48.04208 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2192a4e2-e779-3df7-8a8f-a0d2ad739b01 | -2.72046 | -49.30116 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7be0190f-b984-360a-ab16-043ec7273716 | -6.44967 | -42.74177 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 825e2ba7-1732-3e0c-b61f-9d5c55b9b996 | -4.11124 | -45.70443 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bfcf065d-c74c-39db-b3f1-a088abe679c3 | -6.15623 | -41.14921 | 2024-11-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 46e0d36f-148b-34cf-a3e3-33ee208dd949 | -3.24523 | -49.57876 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2459f044-4193-30b8-b4cf-617d6fb16500 | -3.48125 | -48.23795 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c203375-625c-3638-b2d0-dd56397123f2 | -3.96202 | -48.16856 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 34fe13dc-a7a4-3718-a904-3dd235cc1049 | -4.38436 | -45.86191 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 255da781-0ead-3b6e-951d-c69cf8047abf | -3.25962 | -51.012 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2830a436-4f5f-329f-8193-ad53317f9b88 | -2.81936 | -51.80698 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 715e7c53-20bb-3ad3-987a-cfbd54fbea10 | -2.39226 | -46.78016 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 029d0c04-c55e-36a3-8819-a9a8fd48d65a | -4.38605 | -48.57428 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8f30da58-9ce2-36e6-857f-572369a157f0 | -4.89542 | -48.6185 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 391e32ce-6abf-38e1-978d-7716f677a7f9 | -3.59512 | -50.24143 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 76f44798-8cc1-3608-b2b8-8178b769040c | -2.20209 | -48.37141 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5210594b-6cdd-3f2d-b048-9d13346c7c1f | -3.23643 | -50.30478 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 063c7d43-5404-30f0-8503-43c5009a27a0 | -5.54918 | -47.5018 | 2024-11-10 04:14:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2239cb6-feb6-318a-aaf4-9b356d852fb6 | -2.68169 | -49.19547 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d8d50ab-745f-345c-bd1f-359186c01c7f | -5.09896 | -37.95697 | 2024-11-10 04:14:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| db8a9073-5657-357a-a101-75e817afaeb7 | -3.24927 | -46.48759 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae585fa3-ca30-308b-ac1a-01a47247a5f1 | -3.23869 | -50.32165 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4f67ac2-ffeb-3822-8bbb-2b0de06712f2 | -3.22325 | -50.32467 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97719689-7305-3085-83ee-00439e018c55 | -3.12271 | -45.96904 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e9408c1-1636-39df-96d0-2466b33ce0c1 | -2.93659 | -52.78046 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 699fac04-763d-31c3-9474-470f8b848d5d | -1.72534 | -47.12811 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aca37801-4ba2-3215-8602-d3da94209e25 | -4.85965 | -43.96785 | 2024-11-10 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 828a7593-3b1e-3318-9226-0239be7a9b7e | -3.05782 | -48.03762 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9517a28-a898-3e19-ace7-57727577c7f1 | -4.30924 | -48.61842 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README34.md)
