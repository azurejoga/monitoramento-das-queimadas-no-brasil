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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d87014e-6d6e-3a65-ac0b-d5cad4ecdf05 | -12.90419 | -56.94903 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 148930d8-9f69-3019-b877-47a29fa2d2f7 | -7.78461 | -61.56609 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdb7ffae-0630-3c98-aef6-153fe101bcdd | -7.6023 | -61.60767 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e96895f4-ae56-3fc1-ad35-a29b05c9fc5f | -9.49688 | -57.80401 | 2025-09-02 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e84c32e-a3de-3a3f-b816-6d0c11d29f26 | -12.92682 | -56.95631 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 088104b1-8086-30b9-8d56-f80c280b064b | -14.4952 | -45.95031 | 2025-09-02 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 330daf7b-e17c-309f-8188-089c8464d252 | -13.53028 | -46.99302 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f3a1b09-e8dd-3317-a127-1629522b4c02 | -13.54965 | -46.97846 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d234b370-faf1-3ddb-88b3-d930b8682f72 | -11.83802 | -51.54094 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ac529cc-0432-3cf8-a38b-edb3f14b042e | -14.73427 | -46.75005 | 2025-09-02 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba88e7f9-b096-3825-a414-f5f4b0e34f2a | -9.92018 | -51.6266 | 2025-09-02 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5f4593f-e873-3b2c-9721-443865b4d12a | -11.65539 | -52.18052 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3bc61cd7-4497-3d7d-8311-12cdb21f853f | -8.79897 | -52.09101 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08dc58b4-5714-353a-a600-3078b388ad50 | -13.0907 | -57.12774 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9dbec4ea-524d-3efb-93fa-52a4b5187804 | -12.98356 | -48.09644 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4c0fa4b5-f5e3-34d7-b96e-9b21e6d8f796 | -7.60167 | -61.61145 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 78a1f2ae-06a1-384f-8304-1d86155b49cf | -11.67438 | -52.19049 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 1eac0d61-4257-32e6-a819-690834aa74d5 | -10.75659 | -49.5764 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a515dfab-ea9b-3a82-afed-8aaff1083d6b | -10.26171 | -47.52261 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f32bb732-a0c6-3a8b-8a00-ce6ce507087a | -7.45775 | -63.15889 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2cb2c63-27ee-3d60-a705-538a92c9fef9 | -13.89293 | -48.10974 | 2025-09-02 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d40a6ddc-d37f-3631-a705-4475dfa13cb1 | -14.26045 | -45.24606 | 2025-09-02 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74f65fd0-69f0-31c7-b95d-0d0eac174dfd | -8.70549 | -62.40705 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81cf30af-c99f-36d4-bf36-96a6851af9e5 | -7.53146 | -63.85106 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec314a96-1d95-30cd-8c07-54808c883d52 | -11.67291 | -52.20102 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f439b300-2c7b-3e91-8a1c-a46c7e3f5960 | -9.73751 | -48.98252 | 2025-09-02 05:06:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 66b926a2-d85a-3e11-a16e-eeb5d5417824 | -8.86446 | -52.03238 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50a35ba1-5a68-3996-b42c-053f567b0507 | -8.69346 | -62.40073 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5c7cce4-e162-3c04-95cf-cadd72287fd4 | -9.95549 | -66.87069 | 2025-09-02 05:06:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d4167cc-f2da-3d4c-a305-b93a3cb8c50c | -12.9335 | -57.00082 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e50b0d2-6fe4-3789-94a9-935070af7fec | -11.10297 | -44.63979 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| bdb1dbbf-dacc-32ba-b93c-4a62341ddeac | -11.65346 | -52.19448 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 66e9ced6-3115-3d70-9104-f3e8d14465af | -9.76121 | -54.7638 | 2025-09-02 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03c5d2c8-2375-3152-bc53-2f00acced931 | -11.66532 | -52.1677 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0144bff3-a901-3bb1-933e-42c96d2b0e3b | -14.58956 | -54.56676 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5da86413-83b2-33ca-9cb0-572aabd1bada | -8.6727 | -62.39827 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da06ad58-06b2-3145-bdc0-cb2fb77032c6 | -11.86195 | -46.71499 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59fd652a-967a-3f78-9a26-aa32f8f73820 | -12.92187 | -56.96637 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddb42e81-8c82-3eb2-91ba-69114575d281 | -14.78658 | -48.18332 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5e8802d-6005-318a-9d11-1003981f6add | -14.62358 | -48.93633 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d1894fa-6a4e-398d-9209-651517d27b3b | -11.66541 | -52.19636 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5d6beb1a-9b71-348e-93ec-e2c92b2d95da | -12.98886 | -48.09762 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 11c682b1-6602-333b-8745-aa9c829fda99 | -14.58656 | -54.56192 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d57d9e1a-d289-361a-ac25-2efe74bd41fd | -12.89702 | -56.9515 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b4a923b-2b00-392c-9afe-0d26bf58390b | -10.05365 | -48.09778 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2136e393-03f7-3d22-902f-95f8b8df44f2 | -11.67283 | -52.17238 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 54b344e7-63f8-3d41-afc7-9f0df2868f69 | -9.25954 | -56.8966 | 2025-09-02 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 792035c5-101f-3387-bf86-6772db034529 | -11.67038 | -52.18995 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f1a86bd0-d8ad-3ee2-8a73-5c1a43d49912 | -8.68122 | -62.39968 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a8d8175-d425-3841-bd64-275e41c381f9 | -10.05994 | -48.12988 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb9989ad-d176-3d36-b7ca-f468051f16c6 | -10.25548 | -47.52858 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4c7c21b-bb0a-358a-ade1-cb70fbb0634f | -7.59882 | -61.60324 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b796a16-c3c3-35c4-8d85-bc7c37477368 | -12.88761 | -48.1721 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a02df707-42ae-3454-b03f-f833ca6b68ba | -15.11796 | -48.18535 | 2025-09-02 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7434c02c-e1b2-3a87-9b8b-a54bbd77506b | -13.53705 | -46.98542 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77e2a5f1-9533-3331-8450-bb278b6360c8 | -14.21246 | -48.06176 | 2025-09-02 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2437304-6ac1-3138-911c-8d82af3d021c | -12.9985 | -48.10773 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4de7b300-84c3-30e2-8d55-4212400703c7 | -11.09584 | -44.64428 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 62479091-c632-3c91-a20e-3ce908d62727 | -9.91969 | -51.63007 | 2025-09-02 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c78c8a52-e9c3-3395-b9d2-8b9c04b4aa7d | -9.27846 | -59.74171 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3233fba-2a5b-3467-91a1-9a9d156a6e80 | -12.8811 | -48.06253 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62a7c6cc-73d1-3497-bd9e-bec897286c50 | -12.4413 | -48.72306 | 2025-09-02 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39c20517-2265-3e72-9e2f-5ebac1076a8b | -9.64545 | -63.11287 | 2025-09-02 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b46c0b20-e014-3a69-96b1-a49d2afca5e8 | -11.6665 | -52.21781 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| da1dc307-8bba-3e58-a302-1893f7be4c8a | -11.91945 | -50.62974 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88d289a1-2ed3-37f2-80cd-2a18b111f90e | -8.68849 | -62.40405 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19120f56-0b61-3ef9-b2dd-bf50e1151c89 | -7.55013 | -61.34373 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a83a9faf-5ef4-325d-8ba6-b88d3a877d2d | -11.80571 | -46.40141 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e4c314dc-e925-3b9e-9e60-5f4158da9d46 | -9.83685 | -48.31424 | 2025-09-02 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f94baca-9d9d-34eb-855e-baef53d16797 | -12.3297 | -45.71693 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95b87ed6-90cf-35a3-a9c7-482269427b51 | -11.66203 | -52.22066 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0cf4f6e9-b4bc-3dc7-a1a8-3ce2306a585e | -10.05176 | -48.11231 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 283b58fd-15a1-359a-bee7-25479ffd3edf | -11.06803 | -52.0062 | 2025-09-02 05:06:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 121076f2-0837-3098-9a69-02198a2381a8 | -11.68041 | -52.20562 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2db6631-4a6d-3c2f-a2d1-edc455fe79c1 | -14.7375 | -46.75005 | 2025-09-02 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8776a62b-a544-3637-9e27-5071bd198ebf | -12.92903 | -56.96391 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5925ee58-fed7-3d60-9153-f6d6206d3715 | -11.79784 | -46.40337 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 14b99b13-ea2e-32d9-b467-d175ac3bf35c | -12.58231 | -44.79987 | 2025-09-02 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 35172454-3492-32a3-9c86-c114ba01df5e | -9.20467 | -60.24997 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9730b115-99d1-3947-ae16-861f36c99a39 | -13.32552 | -51.76947 | 2025-09-02 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d23ad9d0-9b78-37ce-b98c-baf42fc89d06 | -11.66483 | -52.17124 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3597e2e2-9659-33b3-96e6-0bc1547a2286 | -13.82277 | -56.60947 | 2025-09-02 05:06:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30a6862d-6e01-3188-975c-fe56c6c7db1c | -11.68244 | -52.22016 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0585bbed-c4f1-3270-965e-0bdc82259020 | -11.54105 | -44.8474 | 2025-09-02 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15b60365-6eca-3ea1-a5dc-8559849d51c6 | -11.85533 | -51.47581 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f657d5d3-70b2-3d3c-89e5-958ed42e3ed4 | -11.67145 | -52.21148 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 82efc723-0263-3368-901e-9a6e382b011c | -13.49592 | -46.93293 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a1a38ac-2242-3a9a-8cc2-89594d07cd42 | -8.7346 | -62.41599 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1eb22a7-86ff-3fff-829c-ec7ee65656ca | -12.62626 | -48.17741 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| af69957c-808d-39b4-889b-c19bb0f6cafc | -13.59153 | -48.13811 | 2025-09-02 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bbcd6308-63c7-3808-a880-58b9118dc3bb | -11.92313 | -46.45616 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17607d00-9b72-32ee-a3ef-c9fadce1a146 | -12.44168 | -48.72003 | 2025-09-02 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39255e63-b3dd-3bda-890b-092aca8cb626 | -8.73319 | -62.42411 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e24bbec5-81b6-3c96-87ae-18f0d0063134 | -12.21106 | -50.12662 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 108d45b4-3f8f-3966-a2be-b2d7fefce83f | -12.88723 | -48.17526 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58ab15b2-9748-3c80-9f98-e1d6c73d0b56 | -11.6708 | -52.15764 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb38510f-5467-3dbc-a270-e30ad1c2a363 | -14.79236 | -48.19207 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13a2fc61-06d6-32e8-8cc5-f14e90fef3f8 | -11.43368 | -55.17834 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3c7111b-784d-3fcd-998c-1085ec63965e | -11.89648 | -46.67314 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e44e2ddd-2c6d-37b2-b576-6d87995f5576 | -11.65744 | -52.19511 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README68.md)
