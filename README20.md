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
| c5069480-13a8-365c-9ca2-a079a28e915f | -10.94055 | -56.83834 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8c78265-43a5-3940-af13-04689b5a3e4c | -11.80692 | -57.34785 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f2f28c80-5dc9-360d-8a81-d7029c49458b | -10.9367 | -56.8413 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 1732e091-52e8-38f0-9f26-a11ee5240c57 | -14.67129 | -53.39007 | 2025-06-14 05:06:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ff990548-6e90-3c68-8989-590bbe3d16e8 | -14.22329 | -57.40655 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38f87171-2f8f-3aa0-933c-e626b06c65c8 | -10.65455 | -44.49126 | 2025-06-14 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8705b978-d91e-362a-8e28-706e591707a5 | -14.04515 | -56.05312 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 179141a5-9c54-3ba0-9b64-fa09e68a0876 | -13.49507 | -53.48567 | 2025-06-14 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d5df76b-2ad0-3f5f-944b-a97cfffcb831 | -14.03661 | -55.14141 | 2025-06-14 05:06:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44169822-b8f9-3ade-87ff-be7d1428b93e | -9.46377 | -57.84972 | 2025-06-14 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce68d478-ed91-3134-b5ab-79d271142607 | -9.79049 | -57.42245 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a7737ec-e22a-3ca6-9cab-38559d5678db | -11.89872 | -47.45653 | 2025-06-14 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67d8be46-8081-3d84-ab2a-ba6221136489 | -13.89298 | -54.61693 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| aef75d1b-0de0-3410-a32f-875f5bfb88ac | -12.62219 | -57.896 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64edb32e-9e3b-3c3c-ab6f-75248e6e4271 | -16.19574 | -46.46537 | 2025-06-14 05:06:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5a8b21cc-cca0-3de8-8ac3-ca0800f1ab57 | -10.92014 | -56.79575 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52887121-dc04-334b-89b0-4ee8b2f15341 | -15.40004 | -47.86827 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e735527c-35f2-3f32-ace5-bc9a36989fd4 | -10.30169 | -57.13884 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2507784-9fb8-34c0-baf3-4c479ed22431 | -11.91468 | -57.46227 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f49c0ec-f95a-3fe0-8a66-13d3b189dbd7 | -11.80362 | -57.34732 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7ef6e875-31fe-34ea-ba25-7caa5c92db7b | -10.52502 | -47.58384 | 2025-06-14 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d17719e-487c-3819-83dc-7f1a8a067119 | -9.28497 | -62.69049 | 2025-06-14 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 886c88c1-311e-3b9d-879c-da4eaeac57a0 | -13.89359 | -54.61275 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5863c787-7bd5-3b20-9136-a434700e1b0c | -10.94522 | -54.36847 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0341fcc9-981d-3886-a30e-2f8652ce1566 | -10.04629 | -64.98205 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a07fbb4d-b162-3704-b530-6a23ee16b80f | -12.08854 | -57.37593 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27cc7541-5b16-363c-9853-c6e4f6048200 | -10.93372 | -55.31367 | 2025-06-14 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ef06b7f-a47e-3330-be1d-78c5b411c1c2 | -14.20568 | -57.41096 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 46b59aef-5efe-3f96-a7a6-33b4ab88c686 | -11.12601 | -53.94912 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc8092cc-d482-3b64-a179-1bfe4697ab6e | -12.43069 | -54.86785 | 2025-06-14 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61d2e25a-cd2b-3964-ae3c-e9fd02078d0f | -10.56902 | -52.01268 | 2025-06-14 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf83e09b-e283-3a11-9c66-dfe83c71a860 | -12.61781 | -57.88077 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74c40f6a-73a4-358b-915e-124f0c3f6f94 | -14.68935 | -53.37277 | 2025-06-14 05:06:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45931667-a85b-33b6-932e-db31f8d6cf9b | -12.16646 | -56.54561 | 2025-06-14 05:06:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d25f8dc4-7c50-3344-8a84-0910f5514cc7 | -14.07184 | -53.39812 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f37ae9b3-23e1-372b-8c19-e2d743e1cfab | -12.2784 | -57.26992 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c30a9e0f-f8bd-3e19-8994-971ccdda1a0d | -10.92296 | -56.84269 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f256317a-44fc-37be-9c05-e447fd7a36b2 | -12.68793 | -52.40335 | 2025-06-14 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e20ae20-b560-37f1-88dc-d5892c9de080 | -12.47222 | -58.47166 | 2025-06-14 05:06:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d248c8f-989a-3abf-a5a1-5a60c1ddbe6f | -13.89676 | -54.63691 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcce4e1a-ac12-3300-9b80-cf2fb1f7d3c8 | -12.68545 | -52.40193 | 2025-06-14 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ad0477b7-4c43-3c12-b31f-cbdefe5510e7 | -14.21999 | -57.40602 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3e15bce-f204-3b67-9046-e0ed9f11bc02 | -10.92735 | -56.83624 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2eed3ca8-5bce-3729-83df-1ca5829e459a | -12.56514 | -57.76357 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39d89c5b-de35-3222-a177-5579fd169abf | -9.68205 | -56.98865 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00262e5f-fcd6-3b3f-9ed7-03893818c29e | -10.85748 | -53.78549 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1984dadd-47e9-3fca-9e5f-5130b0c44503 | -10.85645 | -46.69699 | 2025-06-14 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5baecb50-ca08-3d60-9f83-5bce25688f41 | -13.36529 | -52.66573 | 2025-06-14 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7dd2be25-b7e1-3d32-b496-c638a3696f62 | -10.93395 | -56.83729 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cfcf3ac-3f94-3c67-9628-0359cd684079 | -14.03838 | -55.12947 | 2025-06-14 05:06:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a7dad86-0dfd-3fff-8d95-407819e12dd2 | -14.07103 | -53.39951 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0900e6b-adc3-3415-b7fc-2f4d0276ab7c | -13.96099 | -54.44108 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6639f0e1-2eb0-369a-ba56-f04d16d42def | -10.86453 | -54.3003 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4b25e5a-d14d-3a12-8456-8ff15a2b429a | -15.40045 | -47.86463 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 992f455d-39d9-34d5-87d3-221f74c8ab88 | -10.289 | -60.55118 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76630905-9201-3e65-ab07-db930e6b847c | -10.07722 | -52.74451 | 2025-06-14 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de672e41-d73c-38a5-9063-ca5822764ad7 | -9.63702 | -67.28793 | 2025-06-14 05:06:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 778c12ce-e172-3503-822e-2fce5fd5754c | -12.68222 | -52.39604 | 2025-06-14 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e2352c7-0e25-3b8e-a5ea-17f4ef0658c2 | -14.03199 | -55.12442 | 2025-06-14 05:06:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0496175-8897-33de-868e-f97c8a06b466 | -11.37246 | -56.55632 | 2025-06-14 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaedb296-c6f6-3aee-aed4-ee1d5756ed76 | -12.61283 | -57.89084 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6efd853d-9ce2-3bed-97d6-9d0a6cc4d5cf | -12.27894 | -57.26641 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8c6fef3-7118-3ce4-a2a1-ca2488f83416 | -10.52462 | -47.58714 | 2025-06-14 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95525b11-a155-3a01-bf8d-077f3cc9c822 | -10.91581 | -56.84512 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e7e39b4-95d5-385f-a456-5e17d823b0e0 | -16.20142 | -46.46819 | 2025-06-14 05:06:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2b29c2ae-0a88-3055-bb33-39a4ec7c83a3 | -12.50918 | -58.3485 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec43187a-a521-3a06-b366-aac98a501ff7 | -11.56679 | -54.57077 | 2025-06-14 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 031581b9-891c-3998-85a1-a054c672b82f | -10.55899 | -55.49784 | 2025-06-14 05:06:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84343093-c8c4-38a2-9f74-c5223f11c49d | -10.92184 | -56.82821 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f3f43d55-1e11-3fe4-b179-fc6d8119eae9 | -11.14156 | -53.91771 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a9c8082-7fd4-36e5-a4f2-0d26dbe5259d | -14.20733 | -57.40034 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c13f7820-c502-37c2-9160-e86bcc441c0d | -15.39093 | -47.88989 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e538f254-1409-34ab-b5b1-c695203acbff | -11.01452 | -55.08328 | 2025-06-14 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8480cbcf-2785-3691-b96c-59ecee195928 | -11.57492 | -54.56396 | 2025-06-14 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55f2cf9b-7242-3fa5-b683-315384a57e44 | -12.59075 | -47.06776 | 2025-06-14 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5dec73f-a008-3515-b939-67f9b52a4d1d | -11.00911 | -55.09093 | 2025-06-14 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3523ddb8-7292-355c-bdab-5fa8d7155326 | -11.91522 | -57.48035 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49396a73-cc97-32a8-9389-45de635280be | -13.97056 | -54.45122 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8224f0a-a43f-3299-bb79-aa7065ffd9ae | -10.91738 | -56.79173 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 270c4b4e-d9cd-39c7-86ef-a34ff765a541 | -10.86744 | -54.30481 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a68ed1d3-a2dc-3c10-82d0-1cbef29ddf87 | -13.89766 | -54.63465 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 865102a1-4091-3845-b61d-7957798d9903 | -10.85966 | -46.69645 | 2025-06-14 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9619312-d402-3771-aa4d-72e886ae7252 | -9.93965 | -57.48979 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16b98da4-5f46-390f-8b5b-23f433f8124f | -15.99548 | -49.82446 | 2025-06-14 05:06:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01a8c188-5350-3585-b000-041273bca9a0 | -9.39366 | -57.52025 | 2025-06-14 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0ba3473f-d0c2-3f3f-99bf-fc137ca3a22b | -10.22747 | -56.74509 | 2025-06-14 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da260677-0c9f-3de9-a6e1-c06419ca599c | -12.5657 | -57.76005 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98c5c8be-d224-3c41-9807-b74e5da5743a | -10.91636 | -56.84164 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c4c72546-bdcd-344c-80b5-020d5fe47fd1 | -16.19527 | -46.46728 | 2025-06-14 05:06:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8a795fec-7df9-3bea-a60b-4ee346b9f572 | -15.39201 | -47.88907 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c479932c-1fe4-35d3-8e07-67c4801df88b | -13.8942 | -54.60854 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5b167cc0-0642-3062-a8a8-f44457a1bf3f | -14.07877 | -53.40407 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 674736d0-f2f3-307b-b320-a5508b0159b2 | -10.9202 | -56.83867 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f03f417f-fdcb-3404-b81b-52d51573d1c4 | -12.61669 | -57.88784 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24e2b315-0489-369b-be9e-78933609ac37 | -10.29839 | -57.13831 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b51556d9-70d0-3601-8322-23b31c3b8a97 | -13.71556 | -57.47959 | 2025-06-14 05:06:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49926427-5e32-389b-adc6-d87543cdd5c7 | -15.3965 | -47.89069 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adebb907-6429-3d4b-ac02-159965205142 | -10.85598 | -46.7009 | 2025-06-14 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a036383-1ebd-31ae-9a18-b95003654f88 | -9.46491 | -57.84254 | 2025-06-14 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 99bfbe5d-cff4-3e2f-a788-c52c6a696f9b | -13.89654 | -54.61747 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |


[Clique aqui para ver as próximas entradas](README21.md)
