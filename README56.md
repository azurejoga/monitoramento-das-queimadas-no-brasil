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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70b6fa3a-acb3-3937-bac2-6b214d0918b0 | -6.79227 | -62.97796 | 2026-09-15 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bfcf770-1097-30ab-9091-17de1e29552b | -6.56595 | -58.98139 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72236131-8fdd-3ecd-888c-80f7acf172bd | -6.67038 | -58.70426 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1abcca44-6bea-334e-8bfb-95a945ee514b | -5.81179 | -53.80087 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cff54bc6-fc78-3151-a140-d626f1f0574d | -6.85122 | -55.55606 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f30044cc-5276-3bde-a332-a55a56e65100 | -9.49466 | -56.74926 | 2026-09-15 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f2d6eb7-395b-3972-8e57-bda20d3a6e58 | -9.40785 | -62.7064 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 057815c4-85f4-3ac6-b3db-19d922a988d6 | -10.80652 | -46.22034 | 2026-09-15 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 707ea991-4d91-3cc3-95ab-f5fcfea98e08 | -6.37781 | -58.28759 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4634d524-1ce6-3fbd-af0e-6699288bf337 | -6.83336 | -55.54879 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15924279-eca8-3914-bcf5-2b5814a6bd88 | -10.89899 | -51.55872 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd2614e6-fe16-3aa0-b94a-a5be9e572e0f | -6.32557 | -59.99479 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e7dd740-b918-39f0-a351-f57999adb6ac | -7.56109 | -62.32724 | 2026-09-15 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 976762f9-e6c8-34e9-916b-e15b04be5852 | -5.88089 | -52.0802 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 044efa69-b3ec-3e15-a919-7cd00d1688cc | -9.71597 | -64.90799 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d485e2d2-9f7a-3308-a4b4-5565ac931544 | -6.69794 | -58.70144 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1be4c84f-3f90-3a2d-b3ab-d9402a27fd1b | -6.02237 | -59.93233 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 1eec4b68-2103-3bfd-b883-9d31efe1e8f4 | -5.07461 | -56.24936 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25fa5043-29a6-3141-a8ec-4ef7149966e5 | -10.68019 | -54.18431 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0557b1c-0d4e-3ccd-9517-c50a8b25b5a2 | -5.59069 | -60.1895 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0c4757ac-2ee0-32a4-a59e-28f544a13e04 | -7.86904 | -54.72098 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8fc1aa6-69c0-37d1-b454-07801676b682 | -5.0793 | -56.24207 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7617f92b-b14e-3975-8298-efd3329f8f62 | -8.40984 | -54.72965 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a44723b-10ee-3131-8dba-f790975fa1d8 | -9.35883 | -50.1098 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b39cde40-1825-37a1-921e-41657b2870ea | -8.22151 | -61.36033 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e868a6d2-240a-3a7c-959d-b4a8a3aacedf | -7.87692 | -54.72231 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47bb186e-26ba-39ef-a5af-227343ef4fe9 | -6.72632 | -48.12711 | 2026-09-15 05:18:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00c74471-0996-3640-ae3a-d954840a8139 | -7.56013 | -62.31045 | 2026-09-15 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b47c7c6-57eb-3800-bcd5-640547c3b689 | -10.90052 | -51.54642 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f5b5693-92c1-3c39-92db-85c65bb499d6 | -5.45932 | -60.22367 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b8575a6-e6f3-3e51-958c-79676f545a83 | -10.66966 | -54.13318 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86445610-54a2-33e1-8e31-9a33c9fb4677 | -5.93198 | -53.547 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0e17f290-267c-3510-a7ee-d05d41257d5b | -7.30712 | -55.61213 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b94210f3-905a-354b-96b6-3079dd6f2c38 | -6.62604 | -58.37587 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b62ab07-b46f-32da-ae16-0eb6f46180b3 | -6.83401 | -55.54436 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86c78f2f-533f-337f-8c29-9b935a704cef | -9.88455 | -47.77696 | 2026-09-15 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dc183a4c-0b3c-3f25-b3fc-2dfc46e6c46f | -10.95547 | -57.19183 | 2026-09-15 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0903d16c-282e-3682-81ef-20ba313f5cff | -7.87789 | -54.72094 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4424e0b4-fef7-3ecc-88d8-c88c3ded8162 | -10.66131 | -58.76405 | 2026-09-15 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dbdfe20a-bde5-3317-a006-c21893c39e88 | -6.15715 | -52.73781 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15d2d3a5-def5-360e-b0c4-d421d314f500 | -7.68425 | -55.05495 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4fc72ca-1158-38a7-9268-3968d5249a3c | -5.12779 | -55.94444 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c0df88f-beed-3f39-bd54-27ef742bfecb | -7.10622 | -47.48499 | 2026-09-15 05:18:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6878d9ce-10eb-3992-aba7-006a41cb5061 | -9.35895 | -50.1984 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ac4e56b-70ad-3fc7-ba66-766c1fd88fad | -6.06606 | -57.70716 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4bc66b9b-0415-3d3d-aa06-0355c1c77feb | -6.1091 | -57.67344 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6dd4311d-7df8-3308-99f4-8be1ddbc1aee | -9.4154 | -50.10654 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a58c89b5-83a8-3bc7-b348-7196b24faf69 | -9.87756 | -47.77304 | 2026-09-15 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f66d8fa-b70c-304a-95e7-2e6faf87e896 | -5.45596 | -60.22314 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f24088a-e03d-3d2f-98d2-3f9d497876c0 | -9.71356 | -64.92216 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16087c84-c4f3-3fd6-8cae-52429b671826 | -9.87748 | -47.78143 | 2026-09-15 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e96a53d-df6c-35c2-9d27-03907cf187b7 | -9.13647 | -65.83173 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e30cf139-6d8b-3635-83fd-95933e2b2c12 | -6.62936 | -58.37638 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 522d3e57-405a-31e9-928e-effa4a6c8297 | -6.11361 | -57.6888 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 562c4ff6-01fe-33d7-ab33-e46c7af071ae | -9.25894 | -56.87526 | 2026-09-15 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff74f834-7675-316a-be72-7fb3e10b6130 | -8.56543 | -50.15592 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 389527a1-677f-306c-9b37-1251528fd812 | -7.32134 | -59.56866 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5296079c-e751-3332-8e61-b6c121d96a00 | -9.21761 | -56.57106 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35d2fc49-631b-31ec-afc4-3f27e69b4ab7 | -6.68854 | -58.69643 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b094fd1c-05ad-39d6-9fa7-4a5b841d698c | -5.88138 | -52.07719 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2da6e986-d99f-3997-b4bd-492f458e1ba9 | -6.63333 | -58.68076 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c116f7bf-acb8-3165-9d02-9a469edeab9a | -6.29018 | -59.939 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f267f4b-0fdf-3f55-b2ff-b9f13fd583f3 | -6.02532 | -51.78293 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1da1296-7299-39ba-859e-a4852a35b6b2 | -9.87687 | -47.77855 | 2026-09-15 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8628d432-bf5a-3859-bc68-a7f8ded2821e | -9.53207 | -63.62612 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a53a7681-e2dc-3a0e-8f2a-151e258252dd | -9.84324 | -57.69602 | 2026-09-15 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f21751b0-f401-3080-ab6e-ca8b209422a4 | -6.84951 | -55.54215 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 38536386-537e-30f2-93c3-883fad3cfe8b | -10.68074 | -54.18021 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef675f05-f6f1-3d37-bc9d-3bda13c65ed0 | -5.35633 | -55.89293 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5c7f7db4-147f-3e10-bb5c-65d84966ed71 | -8.09057 | -61.79848 | 2026-09-15 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d20cae0-4cf9-3691-ad70-048006c9a1ce | -9.69785 | -58.17655 | 2026-09-15 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c015ea70-db67-34a0-a92f-77e1bf8f9539 | -7.86925 | -54.72477 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b575d51d-c78a-3cd1-8acc-8a2af6bd9f47 | -6.688 | -58.6999 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b14495de-68ee-343f-9897-de261ab0d4a6 | -6.72303 | -48.11759 | 2026-09-15 05:18:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ab8953f8-31c7-381a-888b-1af2b73ec168 | -5.13845 | -55.94617 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 603b3308-3260-32f7-a48b-5914a8586b7c | -9.42186 | -50.10001 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9bab2004-8fee-3da1-8552-e781fee49a78 | -6.13967 | -59.87953 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0459813-b5a4-3ffe-95be-7659c93d7f5d | -9.71537 | -64.91152 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 523ce23f-db11-3047-8be1-a885ca8c124f | -6.68192 | -58.69541 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b82b72a0-f2e7-3c38-95b9-c42965665322 | -10.9519 | -57.19132 | 2026-09-15 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 004cdda4-279b-3534-8509-e8cce92927fd | -9.25684 | -48.54044 | 2026-09-15 05:18:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aacd6e4d-1a46-3f21-b1fe-de52b7d9f3f0 | -10.67921 | -54.15934 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39dc62f6-6da8-3b21-be1d-0cf04e07cd35 | -9.12145 | -65.84194 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc0d528e-65a1-3766-9aa3-b07e481a5013 | -9.45647 | -56.70931 | 2026-09-15 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad055a8a-0664-31f6-896c-c0e932b9be00 | -8.54599 | -54.69324 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 402ff5fc-1cb5-3c75-a5b2-9154ee323144 | -9.70955 | -64.92147 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d8b358d-7f5a-3ad3-b6e5-20a4b632c99e | -8.97145 | -57.43966 | 2026-09-15 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96e17946-a5ae-3a5f-9245-1387eab2cad8 | -6.85188 | -55.55162 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ced5a3d-05ba-30d9-bd66-491fe94366d0 | -8.40727 | -54.7195 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 510c9234-ea97-32a3-8ff7-a91c3f3356c1 | -10.66057 | -54.13605 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac031536-cda4-3cc8-bc4c-a8398ee8c6a2 | -7.23455 | -46.17075 | 2026-09-15 05:18:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a945752a-020f-3b0b-aa2a-4c01d6bd3070 | -9.16074 | -49.99215 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44152617-f822-374e-97f4-bd45e1ee188f | -9.20226 | -60.39388 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7462bb78-a3f3-35ec-85e6-c2b926483348 | -10.67649 | -54.17958 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3db7acba-9cea-35ba-a74a-44fde2203280 | -5.8077 | -53.80038 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 43d2d68e-0c72-3f4b-98bd-73f65955dcbe | -9.84919 | -65.1818 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1df8d737-d365-370d-a5aa-9bd2d1f277d2 | -9.25935 | -59.63907 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2964ff06-6035-368a-a46d-17eca8b5fd2c | -6.06932 | -57.86445 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 660ecb17-eebf-3b60-9e71-cd86f54e1b1c | -9.61855 | -61.82507 | 2026-09-15 05:18:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96c01dfa-fc7c-3aeb-9eaa-390ac5a18612 | -6.10824 | -59.88476 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README57.md)
