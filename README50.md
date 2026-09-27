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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a1b7ba7-3074-3ff5-9e25-44156f738798 | -4.49811 | -54.95537 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| fea25e01-29db-319a-8104-ace10c2e7249 | -6.07265 | -57.81723 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebe2c7b1-1ec0-301d-9431-42e1c2966383 | -4.54389 | -54.97368 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e1ed248-0885-348a-a425-1f43440dffcb | -6.86994 | -59.8737 | 2026-09-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8e61b10-7536-374f-b2f0-a8ec37d6eaed | -6.86572 | -59.87307 | 2026-09-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dc33c2a-f132-3399-b7a5-e5f8fb787bd2 | -6.63963 | -59.94492 | 2026-09-27 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64aed4ad-b72d-32d2-9e0d-5cde075ff90d | -5.16927 | -56.00353 | 2026-09-27 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02782b49-fb9c-37ef-9f92-2205a05bec12 | -3.83884 | -55.91218 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00cbe6e7-70ef-353d-9067-ef8e9516a0f3 | -6.64327 | -59.9493 | 2026-09-27 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16bbc8d6-1851-3ad3-87bb-8dd390daa3a2 | -3.84831 | -55.81214 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d754e6cc-8f8f-3cd6-a900-b5cefe76dbed | -3.86429 | -55.81466 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d50e61b-2735-39c6-8246-b19a081bb003 | -6.06773 | -57.8127 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3aa0416b-1452-36d8-bc92-1a61a5b3d864 | -5.16838 | -56.00981 | 2026-09-27 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80e48dc0-de37-35cb-b113-c3740a6a6a12 | -6.06785 | -57.81646 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99af536c-8894-3ef1-be36-5a9ff1470f65 | -6.07658 | -57.81959 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38451885-4a26-3ad8-8801-afd87d73662c | -4.50491 | -54.94865 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07f2a820-5f8a-37f1-9234-8eafbc19ba9c | -6.06074 | -57.83138 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29a9fef0-0441-317b-ab92-b39301852ce9 | -6.04642 | -53.60818 | 2026-09-27 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67496df3-da9a-31ee-8c83-481f51171d82 | -6.07031 | -57.83294 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 051ea1d4-36fc-3766-b108-df53a55981af | -4.54245 | -54.97063 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65279e05-b4c3-3239-9815-2930ebd1adec | -6.05284 | -53.60856 | 2026-09-27 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ac2b5c9-3955-3b10-8260-e577a0d51f3f | -6.08981 | -57.63446 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87a44168-7eda-3c62-ba8d-915034c632f5 | -6.08905 | -57.62477 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e235ef1-52f7-3e03-89b6-324aa6c4dfac | -6.09139 | -57.6237 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7cef5211-e090-3781-ab74-4e93d97aa3d6 | -4.36566 | -55.28639 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 685ccd89-73d9-33ef-8991-9da93128eaaf | -6.08755 | -57.63557 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54a29227-a1b1-300f-a8a0-ae1ff1c8509f | -4.24269 | -55.16312 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 284511bd-dee2-3337-b407-619c7f3a5975 | -6.0703 | -57.82933 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cde2846f-fc17-3997-bde7-5f01a5bcea95 | -3.86379 | -55.81798 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dc7df1c-43af-3203-8281-383cae40dc76 | -4.09794 | -54.32627 | 2026-09-27 05:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c2574f3-3571-3ec2-b198-8f80a98f2c29 | -4.54443 | -54.96984 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5df71612-4aaa-3bcb-9491-63afa95a4d43 | -3.83835 | -55.91545 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ee9de5f-2537-37f1-9eb1-883bcc9bf052 | -3.83403 | -55.90812 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2ba8d49-f5a1-36cc-a0af-1cbcd3c970ac | -6.06 | -57.83289 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adab6aa1-69a7-3dc6-b322-1a11c5acf0c0 | -4.0973 | -54.33059 | 2026-09-27 05:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18786ffb-97cc-3df5-abef-80a7cae33d0a | -3.83354 | -55.9114 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a142f63-58ed-319c-b970-c603c2886a2e | -4.49867 | -54.9515 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ad06bea0-843a-30d2-822f-c6961055296d | -6.07342 | -57.812 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92744742-0697-3502-9407-b967cbd3b9e2 | -6.12799 | -53.05518 | 2026-09-27 05:48:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9df00072-7468-38c8-a5b1-8301a86774cf | -10.03904 | -62.45947 | 2026-09-27 05:50:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 571264a9-3d08-37bb-8946-6cefe6c7df7c | -12.89779 | -61.71961 | 2026-09-27 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9e45882-fd11-30af-9466-43da2a03865f | -10.44997 | -61.30917 | 2026-09-27 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6a986ae-bad0-3fa4-85d4-c80d2bd94166 | -12.89371 | -61.71902 | 2026-09-27 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f612c7c0-278e-3a5e-8fea-76d7a429ff8c | -12.90594 | -61.72077 | 2026-09-27 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01ba79ff-677c-3b0b-b062-835b225ceee3 | -9.56809 | -62.70375 | 2026-09-27 05:50:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0954530-66e2-35f6-9d2e-1c668291da30 | -10.81496 | -60.73057 | 2026-09-27 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 09220812-f212-3ed8-b6bc-4c3e04ef3b65 | -11.02592 | -54.03961 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9d537909-78df-33f8-bdf1-8110693eb591 | -9.27593 | -67.64877 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a743c4d-afce-3f0a-b06a-c0a4ef775709 | -11.02041 | -54.04412 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74353206-e40c-363b-8be8-3c5a0268096b | -12.11036 | -63.79857 | 2026-09-27 05:50:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7a67516-89ae-3c9c-97b7-f14a4f47198a | -10.45397 | -61.31012 | 2026-09-27 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1b5f79d-f140-377f-916a-699351d82645 | -12.88963 | -61.71844 | 2026-09-27 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aca693d7-045f-3a43-a34f-f1259b5c5506 | -10.40828 | -53.81808 | 2026-09-27 05:50:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e53d5985-3c11-32ac-bc56-ed11b4914cb7 | -9.5969 | -66.13549 | 2026-09-27 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a7b4365-e5bd-347a-9e67-556dd5933c2e | -9.57176 | -62.7043 | 2026-09-27 05:50:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66a33f07-74e4-32f6-a149-27b93580251e | -11.99238 | -57.60174 | 2026-09-27 05:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3d4deae8-4421-3166-817c-30ce381a4f51 | -9.04425 | -66.10731 | 2026-09-27 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a94d06a-3320-3780-8cf6-c8c881b62fd7 | -9.07969 | -66.09903 | 2026-09-27 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54e5f3a7-6707-35f1-8905-651fac732308 | -9.07914 | -66.10252 | 2026-09-27 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e235217d-59e3-3d7f-9ff8-4d97282d0da2 | -9.57072 | -62.70713 | 2026-09-27 05:50:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be0bcd09-1fe8-397d-91a8-e907a76222f1 | -10.81828 | -60.73706 | 2026-09-27 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b73954d5-37ec-3256-9db9-6d8c837ba60d | -11.98662 | -57.60455 | 2026-09-27 05:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8931b1c1-bb09-3d1b-a948-f67be6b844ab | -9.03818 | -66.05997 | 2026-09-27 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f40e177-6a88-39f5-b2a7-83123eb458f1 | -12.89422 | -61.71535 | 2026-09-27 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 275ebf5a-4167-3034-bae0-14a7b3bbd378 | -9.57136 | -62.70277 | 2026-09-27 05:50:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e0e476c-e55e-3657-b679-b43faead2717 | -10.24922 | -59.12741 | 2026-09-27 05:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d84ee6ac-9208-33a4-93b8-e5c67d972a83 | -9.27534 | -67.65241 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b97d24fa-c539-352d-a0c0-945696e48f15 | -8.59115 | -54.65255 | 2026-09-27 05:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da38b90b-81c9-3a40-9809-2128c6067e06 | -9.27931 | -67.64933 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 318aec28-524a-38e4-8633-859e32805d13 | -9.56743 | -62.7081 | 2026-09-27 05:50:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bb32a22-0d63-3bb5-a6a4-87d993583da0 | -9.07583 | -66.10198 | 2026-09-27 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23cf5af8-df2a-3241-9adb-f3d84036a3cb | -8.66549 | -63.41117 | 2026-09-27 05:50:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 757304b2-d4d7-39b1-857d-1c8d790f16cd | -10.67386 | -57.63587 | 2026-09-27 05:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f91c594c-560a-3f8e-964c-685ebbbb598e | -9.07252 | -66.10145 | 2026-09-27 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d06563e0-8cc2-3f37-862a-bf20cf8bcb9c | -6.93297 | -62.94297 | 2026-09-27 05:50:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7cdfd153-6309-3369-b167-12b9b7b516c4 | -9.04094 | -66.10678 | 2026-09-27 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c73e4ed-bda0-337a-b2dc-04b5f0aff2e8 | -9.28269 | -67.64988 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9448a61-7833-3265-aa84-cd2dc2ccaa2f | -12.90543 | -61.72445 | 2026-09-27 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d2b2af1-3416-32ec-a83e-563690b8f414 | -10.67907 | -57.63652 | 2026-09-27 05:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f949f81b-039d-349b-8794-5972fb1a5737 | -9.2799 | -67.64569 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b67b977e-e55e-31cc-8721-c88314100f2e | -9.0477 | -66.10818 | 2026-09-27 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0453c778-3d0c-3dba-94f2-5f570af1e9cf | -9.60021 | -66.13602 | 2026-09-27 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 107c69f5-5dea-316f-87ee-cebdb035e50a | -10.67428 | -57.63269 | 2026-09-27 05:50:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7e55ef2-25dd-3920-b702-1934bf89f9ac | -11.01802 | -54.05037 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af4ce86b-712c-3d6d-bfec-88684613e72b | -10.0397 | -62.45488 | 2026-09-27 05:50:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04e2214a-3940-3346-88f4-5edca2c6dde8 | -11.01865 | -54.04478 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ad4dd92-f6b9-32e2-8a97-136724bb7029 | -9.16271 | -67.67556 | 2026-09-27 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 356a78b4-966f-3a8e-933f-a726d0285aab | -10.25387 | -59.1282 | 2026-09-27 05:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 197631eb-ed34-30ab-b0fe-fda1ca4add54 | -11.02527 | -54.04533 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25b46cad-3c9b-39d9-935e-f38a8607460b | -11.73277 | -62.33078 | 2026-09-27 05:50:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01c3e33c-31c9-3dbe-ab12-4d5fec6141bc | -8.49884 | -54.78308 | 2026-09-27 05:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cfdf2b3-cc95-3e16-a28a-ee98bc0d4829 | -10.26654 | -67.17841 | 2026-09-27 05:50:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec0ddaa2-1fde-3736-a489-83fd49ad3585 | -10.82283 | -60.73581 | 2026-09-27 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1029910e-2a87-3d45-b520-e04afb0cf220 | -11.02703 | -54.04462 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38a34c9e-f81e-3e03-b527-6a056db5022c | -10.81882 | -60.7331 | 2026-09-27 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0bebe835-7b4d-35aa-9f1c-15d97d9d9d7c | -11.03366 | -54.04512 | 2026-09-27 05:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a35facc6-178d-3da7-b331-1b23f8ab0439 | -11.16223 | -62.86711 | 2026-09-27 05:50:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1ae3683-3af1-3317-8100-8f68c702d4ae | -9.04148 | -66.06049 | 2026-09-27 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26a372dc-dcaa-3e25-b1ca-79e94e339103 | -8.83808 | -62.39213 | 2026-09-27 05:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0f6af0f-50e0-3973-82e5-9ab9d992aeda | -9.05101 | -66.10871 | 2026-09-27 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README51.md)
