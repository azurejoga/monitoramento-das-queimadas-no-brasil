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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d65df12b-3274-3463-a90e-3331db77f517 | -6.85833 | -59.43332 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05141a01-fef5-3519-b526-81b31c995252 | -8.39093 | -62.68156 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| abf1d69d-6d08-34a6-866e-d0c4e8bd8e76 | -9.41013 | -60.41658 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 911cc743-1c03-3934-85ea-af106594bbdf | -10.51937 | -50.82667 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb7b24c2-98f0-3f25-9495-57428688cd7b | -6.20578 | -55.64085 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a7dc8d9-b322-36bf-ab39-8eca71f44dba | -8.02808 | -54.02215 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab1e949d-52b7-351b-9558-88747c5d7e94 | -9.51744 | -51.63434 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0e08050-e1cf-3f76-994e-817f80c467b9 | -6.4322 | -54.95952 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69c537ff-97cf-35d9-8ce5-1280f9858352 | -8.17337 | -54.98088 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf93dec9-2e3d-3e73-a41a-b43cf2bfe06c | -9.05048 | -50.87489 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad813840-f1ec-327f-8c30-c9ff73599eb2 | -8.45768 | -51.56055 | 2026-08-22 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60132aec-3e8a-3447-b69e-ca13a9167d9d | -8.58894 | -54.74611 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa457a6e-cdf5-3c11-b9ac-4c3eb684d76f | -10.74227 | -50.25386 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5c7b3e45-693f-385c-a7ee-ba032c25c37c | -7.36061 | -55.68188 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f1a6f29-a3d2-3c1b-9f25-b24e915447a3 | -6.77084 | -58.68422 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ece0c5e-913f-32f1-addf-c97692c66976 | -7.25082 | -49.91697 | 2026-08-22 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| feb64927-79f1-38e8-b720-f55f14f0cddb | -8.99477 | -50.74129 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60a5d7e1-d441-32b4-b3f8-05b86775bce2 | -6.8203 | -59.41296 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b125593-0e48-3293-8d7a-bdfe1c5975a0 | -8.17619 | -54.98508 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd6711a3-0dc8-3d69-a96e-9f2abb0078f7 | -6.55014 | -58.51532 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3acab50c-11a2-3178-a9d4-cf3af01ae041 | -6.02906 | -57.68124 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f42b65ca-5149-3d13-bef8-cc1f987b42ac | -6.75922 | -58.71263 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf9cebac-07a7-3b7a-8508-336af7f8d325 | -9.28745 | -60.89984 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ca0cb42-13e5-378b-8110-f3e9311eec83 | -6.01329 | -57.82534 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 249d64c7-393f-35b0-a152-bc4042c9fe65 | -9.11772 | -61.59231 | 2026-08-22 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 02cfd344-7e7a-3480-8c8c-8b5a8cb1ed52 | -8.39446 | -62.69296 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c7e65aaa-e608-357e-b7c9-e468907943a4 | -6.67323 | -58.75165 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e62befa3-99c2-33ed-b34f-28f4062e7497 | -10.30172 | -48.22742 | 2026-08-22 05:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a88da94-c631-3b6f-9105-00ae688de0bc | -7.54895 | -61.18354 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c34fe77-ca2c-34f7-9f7e-3ccf854832e8 | -9.00477 | -50.74672 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 06628911-cfa4-361c-bd21-84f8560855ab | -6.13754 | -59.90981 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bc5c61a-700b-3945-94f5-e1f926c2b004 | -9.40205 | -60.41166 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87091b7d-9730-3471-8ec2-f4387b11ccb4 | -8.52216 | -54.81398 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b37b709b-e2c5-38a4-bc49-e9921637ecdb | -9.04884 | -60.44474 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2de5bb8-ca02-3c81-9306-aa13353053fb | -10.53024 | -50.80317 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ae2ca0a-742d-3edd-b2b5-546d26bb5848 | -8.03257 | -54.01557 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d83c9940-33b6-3093-b02f-0cfb424d9c02 | -12.76385 | -48.39757 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0564b32b-5056-3a61-8621-f54e4d4ecdb0 | -9.42967 | -51.66256 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8249780-9086-308e-8335-7dad94d40b47 | -6.77868 | -58.68962 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 810ab946-a4f0-3215-bef9-c496ced1ee75 | -6.65948 | -56.33536 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1de58e9a-37ab-383b-b982-3a376ab8470f | -10.74595 | -50.25442 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b221c05-4836-39ad-85b8-532f261592c7 | -6.23035 | -55.42032 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76daf333-3032-34a0-bd3b-b33d806b9c6f | -6.7835 | -59.43888 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a5937451-2922-362a-92c4-cebee85b956e | -8.5586 | -54.71875 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b28a29c-c3f3-3127-a0f6-4e35318c1139 | -6.7956 | -59.42239 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 04cb97f4-5520-393d-b8b5-4ac45c2049c3 | -6.27532 | -62.53249 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fefa2bf-8c74-390d-990c-9d7eac13b90e | -9.17134 | -59.45936 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 82750155-24e3-300d-a355-901f586ca32e | -6.13743 | -59.90184 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cf1cb2d-0385-3c0d-bfb9-531c220236d7 | -12.77421 | -48.38499 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 512637ce-1092-3ce1-8e00-685308c8e245 | -6.80993 | -59.39286 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ef8f1d2-35da-35e2-bf9f-da6f1b4b3eee | -7.33448 | -55.68574 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a86b9d9-2df1-3b37-8f74-346de0c22fac | -10.65673 | -51.5912 | 2026-08-22 05:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dbf8ef2-1497-3427-a177-2a23aa7510c2 | -8.52656 | -54.82973 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 46d5bc52-6aa7-3b45-ac41-c5214fb904cc | -9.1915 | -59.44591 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62fe1749-38f4-3da0-8a82-48b8577f90bc | -6.37714 | -54.95899 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 533e4310-ce13-336e-b293-704839203411 | -6.7884 | -58.63379 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13258404-54f0-3840-b5aa-b7c8b17aa901 | -6.66245 | -56.34032 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87680244-fad6-390d-93c7-f3da8a9d4346 | -6.4338 | -56.18578 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 513181f5-da25-38f6-89a5-d7688e769fb7 | -8.52824 | -55.31604 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aeabd651-c01b-32c6-b3bf-e24daf83d945 | -6.01057 | -57.79153 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51bf1371-731b-3d44-902c-d93565ee7980 | -6.90123 | -58.99271 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9065616e-4655-33ef-8a95-969ebc70f17d | -6.24655 | -55.42588 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff7bc189-5d55-3108-975e-10a73f34f492 | -10.89189 | -50.27883 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feb4e50f-d5b5-33c4-b7af-7d215994ebca | -12.76338 | -48.40104 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e7f0c7d1-58c3-36f4-b9f6-02f33bd277a9 | -7.10034 | -59.77483 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9913e43b-7f39-3919-9a59-e4ddb4a4400a | -13.47535 | -44.04301 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5c56727-2d9a-3226-b39c-264bbb3e28fb | -6.13108 | -59.91092 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2dc627d-6246-3bd2-9d43-a704de790b1c | -7.07347 | -44.99602 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ed3d0f2-61a6-346c-820b-da1accc4af99 | -6.80252 | -58.62806 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b828f9a4-084e-3e5c-a1c8-e966071b1d75 | -10.83496 | -57.52045 | 2026-08-22 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2acf62a3-be0e-31b9-8c42-3f611f3e0112 | -7.02116 | -59.55426 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a8ffba4-13a9-32a6-865f-a2d403726542 | -6.12337 | -59.89943 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54872fee-d853-36c4-a938-c9b8c62cb999 | -12.01128 | -53.42554 | 2026-08-22 05:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34248e0d-fca1-3f81-b6cf-6bcc10395e03 | -9.10967 | -60.3346 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85e598a5-f78f-373a-921d-340dee7b5443 | -8.58184 | -54.78997 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d145171c-c3de-3c5d-98df-5cda9afe1df4 | -6.77014 | -58.68822 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dc63e8dd-7226-3d1e-b8b2-07496ff9779b | -6.76194 | -58.69641 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d17198a5-e6a9-3014-8671-456a6061633e | -9.21397 | -60.76562 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f09af23-2f01-3392-9037-334182c9d0fc | -5.90799 | -61.29448 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9beea83-7f2d-38b4-a299-b52c10a05ba1 | -9.22041 | -59.76678 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18d0d18d-be4f-39bb-805f-edae1d5c922c | -6.13908 | -59.89201 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36dcdb68-4491-39c0-8d9d-206e9db838b7 | -6.76553 | -58.70121 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44468b65-f7b7-394f-8625-7b92b4b2456e | -8.52335 | -54.80668 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3092e2f-dddc-3cd3-8601-0d4f0f891763 | -5.99714 | -57.79676 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f6b6a55-11cf-3dc8-82b5-d1961df8182c | -8.63278 | -54.73812 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75adb980-593c-3b94-82b9-e3652d3d9cfd | -8.53436 | -54.84607 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d894c77-1032-3290-98a8-27d740837a53 | -11.17173 | -54.00893 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80616e94-f2aa-362e-9cbc-4b71ff7da57d | -6.69405 | -58.94123 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14a29d32-3ae7-3724-bf64-c41a42b7fd7b | -7.36639 | -55.69103 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a8ddfff-b7c5-3b91-b989-b881c4d5744c | -11.20763 | -55.04609 | 2026-08-22 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b222cd35-ec52-3c12-b218-e5e5d8325ffd | -6.17545 | -55.44437 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 469e2fed-9eb9-3f1b-8578-8f67a6d9b51f | -6.53482 | -58.52865 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3ad566a9-6ce6-34a6-945e-c08e0b5b6966 | -6.0923 | -57.8724 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b99b1627-86db-30e2-9f97-014e9308a039 | -6.78351 | -58.66188 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94216202-cb84-31cb-b423-92ef6416e6b4 | -6.8606 | -59.41988 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01055361-46f0-338e-b87b-f80bf9786025 | -6.76804 | -58.7002 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ba41175-ccfc-3246-86d7-fce6cfbcc56f | -7.08169 | -44.99572 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f737cd46-66ea-3835-8445-691f9b3f0de1 | -8.04155 | -51.79537 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40f8996d-f214-3dcc-aa16-f04be1123803 | -8.59495 | -54.68748 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ecfa511-84b9-3fce-beac-8a89030d2f3d | -6.77048 | -58.69786 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README46.md)
