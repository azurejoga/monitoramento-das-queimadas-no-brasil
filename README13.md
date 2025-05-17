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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1d7a4fb-4ce3-3892-8583-a59e12ce0341 | -8.75288 | -49.75199 | 2025-05-17 05:29:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e2aff69-8d63-398a-8e6e-f727254d21e0 | -10.39892 | -57.55276 | 2025-05-17 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ebbeb34f-5da5-3cd4-984c-6c971dab6d51 | -9.32711 | -65.92122 | 2025-05-17 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50919593-0f66-37f2-afa7-a3e3cb3b8b8a | -12.35515 | -49.97268 | 2025-05-17 05:29:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33e1b93f-2888-3ceb-8bdb-2b9cd2d6df49 | -11.35583 | -52.95805 | 2025-05-17 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d659e123-e5a6-327e-8b00-946e79e79cae | -7.94848 | -49.75845 | 2025-05-17 05:29:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6ea7a616-ae99-3427-b00c-f3af765e1700 | -9.25315 | -60.32058 | 2025-05-17 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ce39c22b-e470-35fc-b52b-c240111e6667 | -11.66559 | -54.94502 | 2025-05-17 05:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff8c149b-ad58-3529-a078-fdf2e84a4ce5 | -12.35585 | -49.96605 | 2025-05-17 05:29:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55e69b1f-fe1d-3758-bf91-9b48d3bc7268 | -8.74957 | -49.7565 | 2025-05-17 05:29:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69789282-24d3-37ca-a08c-699fe68684b7 | -10.70268 | -59.11512 | 2025-05-17 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 648ea721-06b4-3f5f-b8c4-af253908e7ab | -11.35923 | -52.96148 | 2025-05-17 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f06c7dcf-8820-33a3-92ae-e64aa6b12833 | -12.29763 | -52.47446 | 2025-05-17 05:29:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b86a2a55-59cb-340f-8efe-166d29c162f6 | -9.45723 | -63.49525 | 2025-05-17 05:29:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d41bb7b-1416-34d7-97c4-15d903e035e4 | -11.42132 | -54.32587 | 2025-05-17 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d320f755-9655-3c5a-99ed-164514ff1ffc | -10.00892 | -62.09546 | 2025-05-17 05:29:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd0a7d11-70f1-3a96-bf30-b778e375c66a | -7.94775 | -49.76434 | 2025-05-17 05:29:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 739677ea-f844-3f9e-911e-a54932e71afd | -10.05137 | -64.99654 | 2025-05-17 05:29:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0651b9fb-bd3d-36d2-aede-21ade0e37f7d | -11.6514 | -58.2611 | 2025-05-17 05:29:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92a8e1f6-e620-3310-936b-8e2ccc3dc13c | -9.6462 | -67.22462 | 2025-05-17 05:29:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf88ec23-122c-3e8d-b7d0-596516d4a280 | -7.9512 | -49.76007 | 2025-05-17 05:29:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 22a93640-6057-38c6-83f3-5959f7e2248c | -11.35973 | -52.95744 | 2025-05-17 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1667026-4b62-3691-9ff3-d9908246a287 | -9.42475 | -55.7808 | 2025-05-17 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b604156-614c-308e-9545-9a31a96a044b | -11.66523 | -54.94796 | 2025-05-17 05:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86666866-af08-3bda-8b81-f080a73d0de0 | -9.31666 | -62.61268 | 2025-05-17 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14f193ed-e60a-3831-95a4-0ce6b51aff26 | -11.35351 | -52.96071 | 2025-05-17 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa4fbcd1-39ad-3b6e-bebe-220ce4c9086e | -8.75033 | -49.7504 | 2025-05-17 05:29:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 436d44bd-f306-3b27-82bb-3a301d133068 | -10.39477 | -57.55231 | 2025-05-17 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4d0f644-378c-3373-adc1-3c379dad3f40 | -10.68673 | -57.59995 | 2025-05-17 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e9a79f9-f43a-3d5a-a747-5a6039bc2557 | -11.42212 | -54.3194 | 2025-05-17 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f979fa2-acf5-3c4f-b216-a96679ca7527 | -11.35402 | -52.95667 | 2025-05-17 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b5b1acc-466f-3704-be9f-28893f7ecb86 | -9.92369 | -59.92505 | 2025-05-17 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0852b177-2eab-3af3-bba0-ca45e56daa5d | -11.42172 | -54.32266 | 2025-05-17 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ca8338a-19b7-37df-b169-c02e45181fb7 | -11.42451 | -54.29992 | 2025-05-17 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3c3a75f-5fb1-3795-9fb0-1a6fefb8dae8 | -10.67741 | -57.60635 | 2025-05-17 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84178b19-6f7c-3226-8cfc-bd2fc3f536f7 | -11.36024 | -52.95338 | 2025-05-17 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5da3597-c752-3cf6-8c98-43db5f3ce161 | -9.26129 | -60.31385 | 2025-05-17 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74eafc39-3195-3c03-b41c-e1c8c6b43fa1 | -11.36203 | -52.95479 | 2025-05-17 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bbeb5cd8-9674-3c16-a1d3-eec91acb45a3 | -11.4165 | -54.32183 | 2025-05-17 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3ba3bbd-818f-3529-9ca9-f5f623ca3415 | -9.64237 | -67.22397 | 2025-05-17 05:29:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66934514-5e25-3095-8276-0ac576516e5e | -11.36155 | -52.95884 | 2025-05-17 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bc02ced-e5cc-314f-94b5-ea05f6f909a4 | -11.4161 | -54.32505 | 2025-05-17 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e76a6995-6307-301f-81b0-819867265bd3 | -11.36596 | -52.95417 | 2025-05-17 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ee11557-126a-317d-8e19-92b48161b7c2 | -10.08177 | -64.91665 | 2025-05-17 05:29:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 013230b2-bd99-37bd-9ef9-81fefec982ff | -7.95515 | -49.75955 | 2025-05-17 05:29:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 892e27be-5ed2-30ed-be16-95cc2d6712ae | -11.35536 | -52.96209 | 2025-05-17 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a3b5c3a-2830-3e0d-8868-6a23cd1e5d44 | -11.36545 | -52.95822 | 2025-05-17 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 313940d4-0f7d-358b-8b9c-a13678a22b4f | -15.26395 | -51.47948 | 2025-05-17 05:31:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c2b4b3b-e88f-3e9e-bef2-cf8209fd8955 | -15.714 | -58.82559 | 2025-05-17 05:31:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9aa33a3-5d15-392f-bc01-63ed927f5d78 | -11.94204 | -61.9929 | 2025-05-17 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df99c633-6d69-38b2-b92c-dbbfdb645eec | -14.02687 | -55.1377 | 2025-05-17 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a36db4c6-5895-3893-8fec-752514d5c4c4 | -17.75855 | -56.30794 | 2025-05-17 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e42b3b6c-a5b5-32e3-b276-baf62c37388e | -13.85264 | -59.72662 | 2025-05-17 05:31:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d18e09d-e868-344c-9147-7a2bdf18de71 | -12.72685 | -54.97647 | 2025-05-17 05:31:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f8f702b-aeb8-35e6-9831-2015eab69790 | -15.26451 | -51.47372 | 2025-05-17 05:31:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 90bb0b73-ab2b-3ee0-a0c8-5eb716c839d1 | -12.14195 | -63.06103 | 2025-05-17 05:31:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fabf958-6e2f-3f0e-8dfc-2f0169d3085d | -13.14794 | -56.81149 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c3c0b8be-22c8-3966-a2a9-6714c63030e2 | -13.3961 | -56.91141 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b3ee53b0-9929-3a5e-9687-dd973ce7db05 | -13.04387 | -53.71983 | 2025-05-17 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5402a7a-e3ea-356d-9665-0345bb07d223 | -13.8495 | -59.72138 | 2025-05-17 05:31:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65d1e667-92df-35a8-b14b-fbeff0393c07 | -13.83014 | -59.66523 | 2025-05-17 05:31:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f5b988b-5948-382c-b12e-5b2e73c7b1ff | -12.82666 | -62.00874 | 2025-05-17 05:31:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05f2b3af-81c6-3863-8493-0961e208b3d0 | -14.02288 | -55.12743 | 2025-05-17 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 582aebe5-8fa2-3416-b80e-19ceecde180e | -15.60797 | -59.29174 | 2025-05-17 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 107d5b6c-8d9a-31b1-bf7b-050bfe8f0872 | -13.3916 | -56.91076 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f4b9bdfd-b6b4-3e12-ad49-5fe434005f87 | -12.65188 | -57.18509 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b5df038-48fc-3056-a389-37f6b91f34da | -12.45723 | -57.19767 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 256da128-878f-309f-9a56-ae862032a334 | -18.95252 | -52.24463 | 2025-05-17 05:31:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec5919ab-2b76-30f5-8dee-626e4648d125 | -17.76353 | -56.30858 | 2025-05-17 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5618c428-3e04-363f-8762-fe53d93d3572 | -13.82634 | -59.66472 | 2025-05-17 05:31:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06447c29-faf3-31b1-af2b-4e0e852b9990 | -15.7105 | -58.94721 | 2025-05-17 05:31:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a77c6528-7773-30ad-bb7a-87a531ed61f8 | -13.85642 | -59.72718 | 2025-05-17 05:31:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ec2d83f-3ca4-3f3a-a984-a454b54623c7 | -13.14461 | -56.80147 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54a1d0cd-16ef-3d50-aac3-4a94f884059d | -18.95861 | -52.24443 | 2025-05-17 05:31:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b11619b-6081-30df-96e0-f2883a912480 | -12.64637 | -57.19332 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7bd357e8-a2c7-3c81-ae61-3901ebf8b790 | -14.02649 | -55.14087 | 2025-05-17 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f84b7098-ecb1-3f4b-a22b-4edf3aee2a9c | -13.83774 | -59.66626 | 2025-05-17 05:31:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af1eba74-b036-3ccb-9da2-6ff05c17cf22 | -13.16089 | -56.81822 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4031bbe-096f-3096-80ac-096167b4b824 | -14.02763 | -55.13137 | 2025-05-17 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92ca5d4b-ca0b-3451-b7e3-5c870c98d143 | -12.45287 | -57.19704 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f868d63a-5b2e-333a-b41d-7168f9fffd05 | -14.02611 | -55.14402 | 2025-05-17 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7631aab-c5fe-3dbd-bac1-c63e33082c58 | -12.45667 | -57.20191 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25042ede-c8fb-38ab-a7c2-55bb14f9b12b | -14.02175 | -55.13696 | 2025-05-17 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b28c3fd-8e83-3959-b4dd-e1125d168cae | -18.95207 | -52.24384 | 2025-05-17 05:31:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46d57462-9f56-3936-85d7-d78fe0c11ad4 | -12.68671 | -58.12983 | 2025-05-17 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f0909ba-8712-3cc3-8768-f2cb0a70138d | -13.14854 | -56.80677 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0f794069-eeba-31b0-8c9a-227b138e99a2 | -19.06878 | -53.45652 | 2025-05-17 05:31:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ad07212-fbd2-3fdc-b43b-6a893fe4184c | -12.1425 | -63.05751 | 2025-05-17 05:31:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 538358d7-8421-3d3d-9737-8d8b9febf319 | -13.13948 | -56.8056 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 013a8685-ffaf-31ef-b831-6af8b602110d | -18.95906 | -52.2452 | 2025-05-17 05:31:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ae355a9-fd71-3aae-9386-047b58110458 | -19.0627 | -53.4559 | 2025-05-17 05:31:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0271ae97-4095-3edc-9b5c-904b052669e3 | -15.27108 | -51.47461 | 2025-05-17 05:31:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 184d3b72-39cb-39ba-9789-9d2850b9ae3c | -12.64661 | -57.18674 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e9f0068-502c-3ef0-abdd-6fb2b910bc3f | -13.04945 | -53.72042 | 2025-05-17 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0de37170-4624-3d40-97e2-efad262510c4 | -13.14401 | -56.80618 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 698c1544-6a4e-3e06-b841-a9e4ae0d9dad | -14.02725 | -55.13453 | 2025-05-17 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e100348-544e-3178-87d3-e0a70ff17cdd | -13.83329 | -59.67051 | 2025-05-17 05:31:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bddcd183-7006-3bec-bd7a-99aa31dc058f | -13.15638 | -56.8175 | 2025-05-17 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46dd8fae-0a0d-3564-a793-e45fb656563c | -14.01813 | -55.1235 | 2025-05-17 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb013cb2-ef64-3e15-8c29-20a43100cb3d | -12.64601 | -57.19113 | 2025-05-17 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README14.md)
