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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b706081b-38d3-3e2e-aae2-2b7f62be8913 | -10.7457 | -50.6599 | 2026-08-31 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 08679af9-6794-38cb-8bfc-4a3b5bcc8ef4 | -11.8018 | -51.0556 | 2026-08-31 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 96a6d8fa-bf3d-3456-b36e-8f2b4c8a704a | -10.5607 | -50.3595 | 2026-08-31 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 03fdefc9-e4b9-3387-a7dd-b8ef46c8b954 | -9.4342 | -45.6704 | 2026-08-31 16:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 66cfd337-4adc-325e-a09e-64b7b42e8a25 | -9.5964 | -47.6204 | 2026-08-31 16:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| e3379015-d6e1-3ce6-8c6d-31de12045927 | -19.0744 | -57.3876 | 2026-08-31 16:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 13e68e88-fad8-3417-a58b-d34028852d57 | -10.1531 | -45.7438 | 2026-08-31 16:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 36eb9b38-d091-399d-a221-f41e49997b49 | -13.4519 | -57.039 | 2026-08-31 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 0fad39dd-912e-3a71-a995-f01d2b266add | -12.2086 | -50.5815 | 2026-08-31 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| f29ada5a-6d2a-33a2-88ef-638fa9adb097 | -10.9559 | -50.5098 | 2026-08-31 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 72442886-2fcf-3ff2-b9c4-1d2a5b639fbb | -7.5844 | -61.3613 | 2026-08-31 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 12000054-6909-3cb6-9726-5436228bba9c | -19.154 | -57.3978 | 2026-08-31 16:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 366.8 |
| c76e9d75-1669-3cf2-9707-81dad615e11a | -13.8384 | -54.0158 | 2026-08-31 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| a138c1eb-5b71-3743-99e0-f7b6a4dfd392 | -10.1087 | -50.2776 | 2026-08-31 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| df6adc0a-b6ea-3820-b23f-640c76f6f039 | -7.3476 | -55.1945 | 2026-08-31 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 0e64bade-9603-3ac7-81ab-166dd3956498 | -10.9592 | -50.2744 | 2026-08-31 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| d7800c88-d48d-3200-8c99-ddeec4a5ca81 | -10.1528 | -45.7665 | 2026-08-31 16:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 93ed1d9b-8926-3332-89fc-65473cb93f77 | -9.4156 | -45.6499 | 2026-08-31 16:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| c9f251e3-5cd1-3ff3-8433-ed2a742c1a1f | -15.2275 | -56.3716 | 2026-08-31 16:00:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 307.9 |
| 915c3cec-7b66-3033-919b-e154ec752c11 | -5.2363 | -55.8914 | 2026-08-31 16:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5def70ce-8305-3f1b-a3a3-dbc475c566ad | -19.1536 | -57.4186 | 2026-08-31 16:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 222.1 |
| 51fb16ad-61be-31dd-99ec-611b3f3156d2 | -8.7039 | -62.9111 | 2026-08-31 16:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9d7e0fcf-b4a2-3f5b-b70d-6643df6c3c0c | -8.7772 | -49.955 | 2026-08-31 16:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| e5d744e8-72c6-3ab4-8cb5-48c6a6cc45a9 | -10.5796 | -50.3575 | 2026-08-31 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| be5a4f74-0ceb-3e4b-8247-4f81512044c3 | -3.4185 | -61.3273 | 2026-08-31 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| dd8628cb-f82c-3f38-82f6-aff758ada0e8 | -14.8316 | -55.7399 | 2026-08-31 16:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 8b3240c9-f11a-36a1-9f6d-868af6ae1e9e | -8.9873 | -65.4379 | 2026-08-31 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| ee39b301-227f-3d0a-8649-fb33315130ae | -15.6139 | -56.4103 | 2026-08-31 16:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3651ef88-b73d-3bab-b2a7-7f5ed2c6c605 | -11.6786 | -54.5484 | 2026-08-31 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 197.0 |
| 664f4f9f-0afc-3903-b655-d30ec4c4ad77 | -10.8235 | -50.5026 | 2026-08-31 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| db294a5e-9294-3a9f-b9ae-5a10e627f74d | -19.0948 | -57.3641 | 2026-08-31 16:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.6 |
| 253a4916-e64f-303b-b505-7b79d16d1e66 | -5.9636 | -57.6704 | 2026-08-31 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 2f00d2d8-64da-33d9-ae51-02f1d4c76070 | -14.483 | -49.0333 | 2026-08-31 16:00:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 110.7 |
| ca85d6c7-4960-39fa-8776-40bc6144493e | -10.8444 | -45.3126 | 2026-08-31 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| beb120c0-65dc-3908-b9f8-0f593dc88a43 | -8.9428 | -63.2797 | 2026-08-31 16:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4e53215b-b400-3d21-b6c2-0f82b6eafe35 | -11.8208 | -51.0535 | 2026-08-31 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| cdd20168-b03f-3147-894f-ee36aa18326a | -14.8319 | -55.7194 | 2026-08-31 16:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 180d803b-16cd-3bc8-80e5-6510e4139071 | -10.5601 | -50.4022 | 2026-08-31 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 612691a3-e0a6-34bc-917a-ca72ecf05b87 | -7.6079 | -57.616 | 2026-08-31 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c575f8b9-ea5f-360a-80af-482fa1b00b1c | -12.9032 | -45.8382 | 2026-08-31 16:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 3c782834-b9b3-3075-90a4-7f9353ce06ab | -8.8819 | -46.0028 | 2026-08-31 16:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 16e8af29-70aa-38af-9bf3-ca8e335398ba | -10.8046 | -50.5046 | 2026-08-31 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| f1f04c62-e522-3c86-994f-c7b7528f51bc | -11.3806 | -45.1928 | 2026-08-31 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 197eea9f-504e-3132-afbb-ac2baf0bf709 | -12.2468 | -50.577 | 2026-08-31 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d9b79d46-f399-38bf-be33-302b4f0894dd | -10.7407 | -54.0401 | 2026-08-31 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 253.6 |
| b55bdca7-2347-38ad-8def-58cb600650b0 | -13.9474 | -54.4179 | 2026-08-31 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 269.4 |
| 4f2d130f-c7d1-3348-805d-8317003e1498 | -6.9872 | -59.2582 | 2026-08-31 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f061a941-3c56-364e-b0a3-803fab7cbee7 | -19.134 | -57.4005 | 2026-08-31 16:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 433.9 |
| 9d420226-3faf-3587-b44a-cf292a29b644 | -8.7989 | -62.5095 | 2026-08-31 16:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 290.7 |
| 9b8dd583-f76e-3cc5-b672-24091345baed | -8.7631 | -46.4418 | 2026-08-31 16:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 39a43d3f-34a2-361f-970f-5d43a00ed9da | -13.4899 | -57.0556 | 2026-08-31 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 319c7914-d792-3c80-b1bf-c81af116b79c | -7.9239 | -44.2327 | 2026-08-31 16:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 428902bb-75f8-3ee6-bdb3-3d90292c682b | -5.8537 | -57.5576 | 2026-08-31 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 80a37619-1006-34f2-8277-5d73b8faf6ac | -10.7856 | -50.5066 | 2026-08-31 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e35b03c6-515e-38d0-9e29-0f6ec145ed0a | -10.5719 | -57.495 | 2026-08-31 16:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ad56e28f-d70c-38ee-941d-d6b890c27c98 | -3.1998 | -61.161 | 2026-08-31 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 7d98ce8f-d4cc-34e9-aa11-98d26e580d8b | -10.937 | -50.5118 | 2026-08-31 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b821fab7-ac2c-3a46-b9b1-685687fe19df | -5.9451 | -57.6906 | 2026-08-31 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 8768c391-514d-31f9-85b1-a2f9a26b39ae | -9.6939 | -65.1145 | 2026-08-31 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 191.6 |
| ad2865b8-27a6-323e-80e6-c2eaea69a8cf | -12.1714 | -50.5217 | 2026-08-31 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3cd75c72-e4cd-30be-a217-c698b9256ea6 | -7.6264 | -57.615 | 2026-08-31 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 411de1da-85a7-3740-a986-22d923cb4f70 | -12.1711 | -50.5432 | 2026-08-31 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 43a99583-acde-3915-a627-11c0d471386c | -9.694 | -65.0958 | 2026-08-31 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 4ac890ee-646e-3527-ab16-18ac116d8a6a | -11.0434 | -49.6851 | 2026-08-31 16:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| b559030b-423b-3fa4-beca-68c00271c17d | -6.6541 | -59.4452 | 2026-08-31 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| e3c29ad0-7b99-3c13-a28c-aa44e801d8df | -10.7268 | -50.6618 | 2026-08-31 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 49008535-06ee-383f-9613-b0a6e5b273dc | -2.6559 | -59.3631 | 2026-08-31 16:00:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 2e9e51b0-c194-348c-9511-dbb6dc5dbcbb | -10.8614 | -50.4985 | 2026-08-31 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 06e1492a-08e8-304f-93d2-765be6fa1e56 | -7.9425 | -44.2538 | 2026-08-31 16:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 0133135f-44a3-3883-88f8-47dbdc31f1d0 | -7.685 | -63.3255 | 2026-08-31 16:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6b8bbcb0-bf9a-36a8-a56d-0ed9ba7e948d | -3.1839 | -60.1559 | 2026-08-31 16:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a90597ea-66f2-36bc-8c19-93499b86b110 | -3.8114 | -65.0747 | 2026-08-31 16:00:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 3d28521d-6323-3ae7-82c0-6813678cfce7 | -11.2128 | -53.9976 | 2026-08-31 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 3d8b3b22-d8e1-3384-aff2-5845f08795fe | -6.1295 | -57.6637 | 2026-08-31 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 840c4a4e-481d-3302-891c-cb5002d498cf | -10.844 | -45.3356 | 2026-08-31 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 2fc560c6-5439-392c-a6d4-ac956103e12b | -7.5662 | -61.3049 | 2026-08-31 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 59c53273-b0b4-39b0-b48e-170e67180225 | -6.9368 | -55.6161 | 2026-08-31 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8987815b-d64b-3e0e-8c8d-35f3aa9e2cbd | -6.9177 | -55.6967 | 2026-08-31 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 7bcdbf06-1efd-3257-9530-70a1070aec02 | -7.3087 | -72.8449 | 2026-08-31 16:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| fb685c3e-3cdf-375a-bfe7-cd7c3d33e4c8 | -8.1671 | -54.9447 | 2026-08-31 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 8445c530-001f-33ae-b47f-15127430d3c5 | -9.806 | -59.4468 | 2026-08-31 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| c44e1eba-0c7f-3b97-9fd2-a866704f3806 | -19.1336 | -57.4213 | 2026-08-31 16:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 1515938d-e30d-3297-97cb-68d0964a7eba | -8.9253 | -66.9477 | 2026-08-31 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| cc3aa79a-79f7-3ced-9928-6e3049a1e331 | -2.6741 | -59.3628 | 2026-08-31 16:00:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 031d838a-482d-329f-900b-357e99c8d267 | -5.5647 | -60.2312 | 2026-08-31 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 431c08a0-1c83-328e-804b-5fa8548bd845 | -5.4876 | -57.1416 | 2026-08-31 16:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| e5f98ef1-e0ad-3066-a8df-e9dca807e134 | -12.9054 | -59.8857 | 2026-08-31 16:00:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b2207c61-96ab-31a6-b222-11a07e7612b1 | -6.1109 | -57.684 | 2026-08-31 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 272.2 |
| de88190f-7239-31c7-a8be-8a4ef16fa372 | -11.6975 | -54.5467 | 2026-08-31 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 91ef6e88-7d71-3d32-8711-85ce14a623c2 | -13.4707 | -57.0574 | 2026-08-31 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 767d5743-60cb-303b-873e-557bc952fa14 | -7.9236 | -44.2558 | 2026-08-31 16:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| c3ff9f5d-41e4-392e-8b42-8db28c39c77a | -9.7126 | -65.0951 | 2026-08-31 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 7ef84693-f23c-3106-bf0e-f249d70edb80 | -13.4899 | -57.0556 | 2026-08-31 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| f30aab2b-9209-39ab-aa17-0af13afce4ef | -6.9872 | -59.2582 | 2026-08-31 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 05a6e471-d9e5-3d12-a132-4c8ee398e8e6 | -15.2275 | -56.3716 | 2026-08-31 16:10:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 135.1 |
| c81eeca6-9269-30b8-a681-d9d558aecba6 | -9.4345 | -45.6477 | 2026-08-31 16:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 6557ad96-6d94-37b2-bf76-266cef9a5dff | -8.6852 | -62.9496 | 2026-08-31 16:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 17e98581-51ca-32b0-9dc5-cc53acea572c | -8.7039 | -62.9111 | 2026-08-31 16:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| bbceb8c9-38b8-3682-b99e-63e7b9f72377 | -11.2317 | -53.9958 | 2026-08-31 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| d2a39fc6-2afb-307e-85df-d733d5591448 | -13.4767 | -51.4086 | 2026-08-31 16:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |


[Clique aqui para ver as próximas entradas](README105.md)
