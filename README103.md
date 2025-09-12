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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e21b2bb-3723-36d7-be8f-621c985a4afe | -9.7228 | -64.92994 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0360e89-4576-38be-a301-871daecef8cc | -10.85322 | -48.16253 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a5d6d2ab-1f34-3618-bde7-a8980cfe3d29 | -9.8945 | -51.86877 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b9739243-2b93-3758-b0e0-9de45c2d8f28 | -9.89865 | -51.87524 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fe805995-12c8-3975-9e15-ff5f1cf55308 | -12.5661 | -49.14589 | 2025-09-12 05:18:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3683f9dd-ca0e-3ad7-8580-9d10d6862206 | -11.94925 | -51.17276 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| fee082d5-65a4-30d3-94e5-4a8782336a63 | -9.29333 | -65.59553 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4a6eca7-87a7-3a54-aff7-bb99ee647cf9 | -12.47023 | -53.82714 | 2025-09-12 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5097a7ed-2c47-3fa1-ad5b-f8a70ded3c48 | -10.67278 | -48.59129 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae80c67c-c77a-302e-92d6-8b0d99b2cf93 | -10.42154 | -50.62147 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8c4ad76-7a5c-39e7-8589-bec237931546 | -11.95324 | -51.17408 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 9e2cf713-6375-3a25-ae6e-e759b1469237 | -11.18173 | -55.05851 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 648c6642-8d58-36b8-9e06-351c1866d7f0 | -7.94673 | -63.67551 | 2025-09-12 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 628d4564-caa7-3464-9d13-b66bc1ec1547 | -9.07742 | -50.50116 | 2025-09-12 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5456d549-fd62-3cc8-975c-fe6f8df93d90 | -11.94309 | -51.1788 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ce479550-7ee7-3181-8d4f-580577c8e1a7 | -10.42966 | -50.62168 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 753861f7-0e45-3820-a935-003cafd3d19d | -7.73221 | -50.74458 | 2025-09-12 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da728332-e723-3aaf-8cd4-7e7689c72bbb | -10.53032 | -51.50318 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cbd1c32-7eb2-3b39-ad8f-670633f01982 | -9.04118 | -47.04935 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e0bd735d-3aed-33ff-a068-9417e8109553 | -8.89212 | -49.93159 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fc913328-0e47-3bf8-95d1-0448a0f0fd0e | -11.19386 | -55.08958 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b82191b9-f769-3883-8cf3-4738785b6dc6 | -9.67012 | -47.54095 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6a72c167-7c5a-3a37-99a5-3b0d415805e8 | -9.3401 | -65.45048 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b26b000a-2fa7-354d-914e-faddb3237e58 | -10.40287 | -50.02942 | 2025-09-12 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70ae9386-3342-3b1d-ba85-d46dc3ad1bce | -11.95404 | -51.16736 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 31d204e7-3309-3795-9ed9-9fa4a2cc692d | -11.9656 | -51.17154 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 05b4a20a-ac0a-3f40-a1c6-df797722ad3f | -11.96475 | -51.17825 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f6f243e2-7ae1-3d45-8400-9dbd8f8ff821 | -8.08257 | -50.17952 | 2025-09-12 05:18:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c49b3b7a-6005-3245-9f89-754798aa95a1 | -9.83377 | -54.5309 | 2025-09-12 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18665f36-a671-3ec5-8a1f-72c780d08f34 | -8.88014 | -49.54047 | 2025-09-12 05:18:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89c1fb39-4225-3bb3-acd0-06511e07ef26 | -9.8965 | -51.89143 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0b22f243-61fe-33a4-ac22-ec8c82ac0c18 | -10.58399 | -60.20033 | 2025-09-12 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f457d01d-1217-3107-982b-5a7c6f7bb1ad | -11.65245 | -50.58348 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 972961cb-a473-3c60-944a-870556244e0b | -11.87378 | -58.82597 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 695eb596-b05d-3c5a-b337-3ff9d429016b | -7.7932 | -50.775 | 2025-09-12 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0553650-7908-3495-b24f-c0784629bb25 | -9.04355 | -47.05057 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2eae8d55-6703-364e-b8f7-585be1aaf8ad | -9.78331 | -47.85893 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 31d86782-aa45-3914-8936-bdaae918e83b | -9.5959 | -55.00366 | 2025-09-12 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3c8f872-6544-33a2-bee7-2a2ade18cdc6 | -11.79507 | -50.56537 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6d81e88-db53-3920-b47f-6eb5763566b6 | -8.88063 | -49.53664 | 2025-09-12 05:18:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e482297d-d733-3140-8f7d-6e1dbeda026d | -10.09184 | -50.39307 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6344cd9b-8d50-3c76-8220-50246e668800 | -12.98278 | -48.01431 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6a8ab0f1-336d-3f1c-ad6e-a97c4481e145 | -9.79793 | -48.88765 | 2025-09-12 05:18:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b02b296-3feb-3ade-b3ec-8ced77f2332f | -9.99146 | -51.71577 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dce8f80-9f89-39ce-a6b4-8248b10445f1 | -12.50238 | -47.43969 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 684b1dec-2ef9-339a-9283-fa015b6ca221 | -9.04034 | -47.07626 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4fd41ae7-1ae5-3fc8-ba98-84007251da77 | -11.1898 | -55.05973 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ceb01d9-3c6c-3297-a342-58143d4238f1 | -10.00068 | -51.72291 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed0d24bf-c6cc-331d-a23e-b470f65249c1 | -7.72098 | -51.07779 | 2025-09-12 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4092f96-5a56-3987-aa8c-368b821666e1 | -11.54302 | -50.6071 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 537ab60f-243a-3162-8705-2891f1fc40d3 | -10.64821 | -61.65729 | 2025-09-12 05:18:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 467430d3-3e1b-3af0-b849-48d9f56149ee | -9.07521 | -46.95988 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5d197165-7c8b-3f8e-8bfe-d16565e43ac7 | -9.87186 | -46.48501 | 2025-09-12 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af01efc1-9271-347f-bafb-e434584c5c9b | -11.96466 | -51.16882 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1424b6cb-ed8a-3e85-9b50-22c0045e04a4 | -8.95789 | -46.07783 | 2025-09-12 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3f42c5f-6d68-3cf5-b02c-3dc6b43a7c97 | -11.08809 | -51.39074 | 2025-09-12 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50dd50b5-ebe3-3263-a854-dc961be66c0f | -11.80013 | -50.56977 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 526c7d23-46f9-313d-9033-1419c442ddf5 | -8.95114 | -46.72118 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6bd6516b-e70c-3a40-bb6f-4034335dafe4 | -13.16621 | -50.0849 | 2025-09-12 05:18:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 259f59cd-7b87-302d-ae46-1d54adc676d8 | -11.94793 | -51.17338 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| f1c4ff94-b825-3748-a928-14a57b4c012f | -10.20583 | -51.6766 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a532ecbf-1286-363f-8336-b27a35e618dc | -12.82161 | -47.97423 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0b854d91-8ce3-375a-ad6b-6f4d55f008bf | -10.39341 | -50.49714 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fba5acc1-9ba8-38e4-b1a7-07b7081ac84c | -11.66106 | -60.59769 | 2025-09-12 05:18:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b966d064-f236-3747-ae40-84a4b6beb54b | -9.03617 | -47.09182 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 88015fcc-7729-33f6-81c0-7122f5349544 | -11.11589 | -51.97774 | 2025-09-12 05:18:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1b1a0d7d-f5f3-35e4-a402-0d8991d4353c | -11.69604 | -46.52694 | 2025-09-12 05:18:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8f6afb37-3dde-3e05-898c-83a2f956a862 | -11.20294 | -55.0835 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbccf536-7266-30fd-adf9-5a95eb5040da | -9.04535 | -47.07116 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48621905-26c7-3b1c-9b3a-f3c526c0c26c | -11.10591 | -51.33205 | 2025-09-12 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22ced569-896d-3f3a-8ca2-27ff1089c9b2 | -8.95714 | -46.72837 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| eba9b266-5166-3917-8c10-ce37a57bcd67 | -8.64289 | -55.24912 | 2025-09-12 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0272d7f-02c0-335e-96b2-2b6271077947 | -8.0777 | -50.17491 | 2025-09-12 05:18:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d4af8966-b6d0-3921-a5aa-7ca94e4c315e | -9.04823 | -47.06708 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 81258203-49e6-3dca-a2e5-1c370161a103 | -9.04662 | -47.06047 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b6b1d1a5-d695-3135-8ce8-7369747e3064 | -10.42373 | -50.62532 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95b7e1c1-6b6d-3b40-96ea-c8154bfd2ffe | -9.71774 | -46.88847 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29a10ef8-810c-3212-925f-c7cb0dbe4c6e | -9.9626 | -51.69891 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 61d648e0-b890-3ed6-943d-5e4049feb801 | -10.5504 | -51.53644 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0cb8147-2f80-33cc-816d-760c9825de4c | -12.93111 | -47.99977 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7dfac43-08a3-3056-8953-86e77a3dd205 | -10.52204 | -51.52651 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0ab958ae-87eb-3398-b7a8-5d74d4f3e3c2 | -9.08592 | -46.95753 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 22ebed55-cf1e-3981-af64-da352faf6f75 | -11.53337 | -50.59474 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 609a7ca1-7615-39c4-8a34-747883a4318b | -11.87545 | -58.81503 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93242d9b-7f20-3c68-88e6-6015779546c0 | -12.99644 | -47.99932 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| be15e6fc-308e-3cbc-8b60-06a8ca07bad3 | -7.4131 | -50.64737 | 2025-09-12 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9411da7-795a-36ea-994d-e8698f3e31ed | -10.27366 | -47.01567 | 2025-09-12 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14f29338-eb1a-31a2-b3d7-e46e53bb99c5 | -11.08291 | -51.39001 | 2025-09-12 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acd7a0d7-163b-36d3-805f-053b3eca0a30 | -11.87263 | -58.81083 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0d7964d-1490-3839-9952-0b17ea05aff7 | -10.74055 | -48.90347 | 2025-09-12 05:18:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db78ea49-22e2-3102-b914-437439bacdc5 | -10.5649 | -52.02561 | 2025-09-12 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5386c4ab-4ae1-31c0-a2c7-43fa56802bcb | -8.96485 | -46.07932 | 2025-09-12 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e030f92-221c-36bd-81d4-a59dc63742cb | -11.19486 | -55.08243 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee1b478c-c300-3b36-9208-62cb12211a34 | -12.24676 | -46.74979 | 2025-09-12 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b7cef842-00da-31d8-b901-cedcc6a88dab | -9.68895 | -47.5491 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70993b05-1b7a-30ed-b4d0-f76a01b7fded | -11.97488 | -51.17368 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 080d3fa5-7ba7-3737-ad21-f2368d3a8ffa | -8.67129 | -64.31486 | 2025-09-12 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b57170b4-ff50-33cf-9324-527a6be5a814 | -9.03825 | -47.09304 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94f2e219-f610-33e3-b5c6-ed3770fad857 | -9.72144 | -48.3081 | 2025-09-12 05:18:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e3acfc30-e90f-32cd-84eb-de51ac71dbf8 | -10.5409 | -51.5298 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README104.md)
