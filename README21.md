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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db242aaa-48f7-3a3d-8d38-0d72e7f2846a | -12.16994 | -56.54614 | 2025-07-04 05:31:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1dde09af-edf7-3281-8eda-ed89886ebf8c | -12.06761 | -61.29692 | 2025-07-04 05:31:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1a6079e-ce03-30b1-b1e6-575dea27096d | -11.02036 | -56.25854 | 2025-07-04 05:31:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3ad7368-532a-3f05-90c9-2a3119e70d88 | -12.58259 | -56.9703 | 2025-07-04 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9fd28387-be33-3fcd-afa1-e7b55939219a | -11.02048 | -56.25615 | 2025-07-04 05:31:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f68733e1-8ba0-3287-94f3-b210bfff6d2e | -10.89521 | -56.45533 | 2025-07-04 05:31:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| db1ff422-e824-3826-b0ef-5d317686e82b | -12.58199 | -56.97492 | 2025-07-04 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c790babc-f6b0-3351-af64-585d9872a6af | -9.51561 | -65.58708 | 2025-07-04 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3fc16b6b-93ff-3110-b1a0-c4b01d06b9d3 | -12.58139 | -56.97953 | 2025-07-04 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b88a43a-ca74-3bc6-8b61-cec525ff1cd8 | -12.58528 | -56.98471 | 2025-07-04 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e488ff2-3830-3b49-aedf-a37f11bd6b7f | -11.88021 | -58.73513 | 2025-07-04 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8208c59c-c292-3a92-a429-42b345b8aef1 | -9.84196 | -68.34534 | 2025-07-04 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfc585fe-8407-32b9-8197-70b686ebd1d7 | -10.05564 | -59.36542 | 2025-07-04 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c77297b-8050-331a-8e09-ff3cc425160a | -9.51211 | -65.58649 | 2025-07-04 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e23d46e1-4c4b-3622-a154-6692b0dd4c12 | -10.05427 | -59.36279 | 2025-07-04 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba0b8504-2aaf-3dca-b52e-e31cb864c16d | -9.48316 | -63.38255 | 2025-07-04 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b8be4a0-0055-3646-a766-db481f78beee | -9.64023 | -63.50772 | 2025-07-04 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f8a4d1a-8ec6-3d79-bae7-9ec98276453c | -12.58469 | -56.98927 | 2025-07-04 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4489f11e-e2bd-3cf0-8b18-b6f7f538136c | -9.52763 | -63.57581 | 2025-07-04 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2d2e4c7a-2d87-310a-885a-0d38ddfd3f68 | -12.17058 | -56.54131 | 2025-07-04 05:31:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3bb75bf-c385-31fd-b964-be2affad2436 | -9.66295 | -65.75352 | 2025-07-04 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc5f9346-d97b-3766-9ca4-341ddea459a9 | -12.10437 | -54.58933 | 2025-07-04 05:31:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0beca3ba-1748-34d8-9b44-8a5cffc93291 | -12.17033 | -56.5427 | 2025-07-04 05:31:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d548bcd3-3a52-34f7-afd9-3fb9afaa3434 | -9.64354 | -63.50825 | 2025-07-04 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5fe5dd1-5ee8-3c36-9337-c6bd6e302c77 | -10.89068 | -56.45465 | 2025-07-04 05:31:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8829396-067a-3fbf-bd2a-a5bb07aca848 | -9.52819 | -63.57232 | 2025-07-04 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 609d5a80-07c6-3074-bbe3-80cadb9319a7 | -9.585 | -68.56888 | 2025-07-04 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 227f7c0f-257d-3291-ae09-0677a8c3ec54 | -9.5337 | -63.58037 | 2025-07-04 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58d2c96c-6e48-3c2d-93db-8328b2319287 | -9.84602 | -63.67052 | 2025-07-04 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdd95a27-964a-34ac-9719-32eb95b1961f | -11.8307 | -62.76534 | 2025-07-04 05:31:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcce44e5-6e41-3600-8805-04ce2e0d4cf8 | -12.10999 | -54.58685 | 2025-07-04 05:31:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d509b1a-9a39-3544-8061-ee054fafee84 | -10.89178 | -56.45641 | 2025-07-04 05:31:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5403fbb2-4667-3898-95a0-ccf744d910e9 | -11.83016 | -62.76887 | 2025-07-04 05:31:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcec0ada-8ce0-30f8-aa9f-737dd72a11d6 | -12.46144 | -58.57432 | 2025-07-04 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ece4f75-edb0-36da-9255-fdf8e30f7600 | -10.05631 | -59.36092 | 2025-07-04 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fff4aa20-52bc-3a47-a785-8ddbe6614665 | -9.63692 | -63.50719 | 2025-07-04 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2b819ba-b8fc-3dc4-9ded-2f2b39a2e6f9 | -9.99911 | -67.79073 | 2025-07-04 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97dd92b6-4809-34b2-a387-bbf853052257 | -10.85379 | -54.03327 | 2025-07-04 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29898d0a-579c-308d-b345-4caa90e7a15c | -9.69172 | -64.63077 | 2025-07-04 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ded3bb64-217a-3064-97f3-ca46d2bbf576 | -12.4796 | -58.47 | 2025-07-04 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e0c0fcf-f4c9-3a30-895b-2774d626b200 | -18.44713 | -54.67812 | 2025-07-04 05:33:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0348f0d-c213-3229-9a38-d587a21edd40 | -18.6547 | -55.74065 | 2025-07-04 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6a713151-1cf1-36c8-a044-56233c65ed54 | -18.44755 | -54.67401 | 2025-07-04 05:33:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c4cb785f-5ab4-3bc2-934d-35ba02b9f36b | -20.72675 | -56.65712 | 2025-07-04 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77712890-8bdb-3d3f-9a14-0b7afc43cd03 | -18.66072 | -55.73447 | 2025-07-04 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6a9bab27-92c8-361a-a839-14f7f5a53ea7 | -20.7271 | -56.65358 | 2025-07-04 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5edd70f3-e9ff-3b78-8733-a95a99c87d9e | -18.44233 | -54.66913 | 2025-07-04 05:33:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3401abba-5962-3e1d-a557-55c3fd19d91d | -18.67057 | -55.74259 | 2025-07-04 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9bcd522b-ebc4-3a55-a61f-b86c62176fdf | -18.6702 | -55.746 | 2025-07-04 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b2be899c-73c8-3a29-95f1-bc11cf2cfbae | -20.73219 | -56.65453 | 2025-07-04 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2718d41-9584-3c8d-b5c8-2cca8771ed1f | -18.65543 | -55.7338 | 2025-07-04 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 04b069c5-0b37-3907-9d5a-580236fb160b | -18.65999 | -55.74129 | 2025-07-04 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b66ce087-4da7-36f9-bd34-d1bc7e8519a1 | -20.73253 | -56.6511 | 2025-07-04 05:33:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3603c218-d1da-3ef0-acb6-a36a121021b7 | -18.66035 | -55.73787 | 2025-07-04 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ffb72cba-2e94-3e31-b2d2-e3af41a7cf38 | -21.95576 | -57.58804 | 2025-07-04 05:33:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15352a26-ad4a-3680-9f8c-c033774fb033 | -21.0417 | -55.99746 | 2025-07-04 05:33:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9373c059-54e1-3607-a792-464a9babf823 | -24.74599 | -53.80776 | 2025-07-04 05:33:00 | NOAA-21 | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 81e9ceac-d3c4-30dc-b712-89674ef897b1 | -18.44797 | -54.66988 | 2025-07-04 05:33:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8f48ea80-8322-30b4-9bcc-868691d909ac | -21.12889 | -57.51992 | 2025-07-04 05:33:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 313f3948-0ce8-398e-82ea-380e91eac8f0 | -21.04135 | -56.00114 | 2025-07-04 05:33:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bbbf9c6-c5c4-30e9-b135-c76c8110881e | -18.66983 | -55.74941 | 2025-07-04 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c1500a2c-3362-39d5-925b-db55aa72b163 | -19.81528 | -54.41321 | 2025-07-04 05:33:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5df2a3b9-3e54-3516-ae03-d0fe463fc1ff | -19.74793 | -53.99662 | 2025-07-04 05:33:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0d071bf-d007-3bf7-b038-8c4fe0a89dc9 | -19.74749 | -54.0014 | 2025-07-04 05:33:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6ec46c34-89cb-3192-bf3a-8f7ea179fde5 | -18.44191 | -54.67327 | 2025-07-04 05:33:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d840957-d532-3ea5-b9eb-d249e083a265 | -6.6112 | -43.8941 | 2025-07-04 05:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 2732b278-806b-304e-ad29-c0dab9bcaea0 | -6.6112 | -43.8941 | 2025-07-04 05:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 4b65721e-8dc5-3b85-88b9-264ecd9830c5 | -8.52853 | -54.77694 | 2025-07-04 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d23568eb-67ce-38ae-a7a2-40591a93e383 | -9.52964 | -63.57513 | 2025-07-04 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 14895f42-caf7-3ffc-8f35-07a6d2481ad3 | -8.98093 | -68.97577 | 2025-07-04 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22452ef7-5e93-3e34-bbd6-8dfdaa92b759 | -10.89389 | -56.45688 | 2025-07-04 05:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e3001315-d919-3d0a-a0b8-a9dd9aa9e5cd | -9.6422 | -63.50674 | 2025-07-04 05:57:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ffed1f2-d1f5-3fc0-9816-435ca6222689 | -9.6327 | -61.46027 | 2025-07-04 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f11f291-76a9-3583-8b7a-89e0de98d1ea | -9.18975 | -61.84819 | 2025-07-04 05:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce990a8d-76ec-3352-8e6d-7f427195b084 | -9.84652 | -63.67015 | 2025-07-04 05:57:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 745d1d92-0f88-38e9-a273-8731f901baa5 | -9.58254 | -68.56881 | 2025-07-04 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa9f31a4-0429-3d9f-874e-e956e1f7bc2a | -10.89427 | -56.45634 | 2025-07-04 05:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc523f0f-4f2f-3b67-9a9d-bcc03393e1ee | -10.30469 | -57.13973 | 2025-07-04 05:57:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64742db6-726d-3ef3-942d-6c37c337cb40 | -9.62912 | -61.46762 | 2025-07-04 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e534ac8-bf38-363e-a6a7-f820b9af568c | -10.10281 | -67.90984 | 2025-07-04 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e0ccd3e7-bfd7-3030-821a-be2e4e3ec186 | -10.30534 | -57.13419 | 2025-07-04 05:57:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5669ec9-6d36-313d-9458-e890e1db7cb1 | -9.6347 | -61.46285 | 2025-07-04 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76802be1-890d-399b-8ba2-49f8da6a121e | -10.52839 | -68.04544 | 2025-07-04 05:57:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0737fa9a-a5ab-3f4b-92b8-8d13bddf7d5b | -12.58644 | -56.98353 | 2025-07-04 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85864ebc-872a-3223-aba5-abd7633ded51 | -9.63399 | -61.46827 | 2025-07-04 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66b86a39-7934-3998-8795-5104ff51a1d9 | -9.22284 | -67.90829 | 2025-07-04 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c5a78b9-2cf8-332d-84ac-2029da4a5834 | -9.21948 | -67.90776 | 2025-07-04 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b8617355-5e30-31ad-900e-8d944c43835d | -9.62983 | -61.4622 | 2025-07-04 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aeb29638-6401-387b-b18b-b02d377e5cac | -9.0361 | -63.98536 | 2025-07-04 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba9b7a29-2e06-32e6-839e-1cd851bc77aa | -8.71804 | -64.17361 | 2025-07-04 05:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a5ac6c7-97c2-3f8c-bad7-7797118a69ee | -9.52544 | -63.57452 | 2025-07-04 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| db08f88c-ea8a-335c-abce-d1021f79ccd3 | -12.58036 | -56.97665 | 2025-07-04 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6aaeac63-0638-36db-b472-01ec97935482 | -8.65375 | -64.05294 | 2025-07-04 05:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcd3c6a3-2f30-3d20-8c37-8c0a8827257b | -12.58106 | -56.9704 | 2025-07-04 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 734caa4f-8154-352a-8ba8-c7b891194c60 | -10.30477 | -57.13995 | 2025-07-04 05:57:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41e50289-728d-3998-94b3-6d397cd7a3ef | -8.72034 | -64.17033 | 2025-07-04 05:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bd9c9c4-f1eb-3538-b6ec-2b0b2a437852 | -8.71961 | -64.17552 | 2025-07-04 05:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da420624-7a6f-3ad5-95a9-31858e143b41 | -9.53329 | -63.57963 | 2025-07-04 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7da5af37-f4b4-39a4-b179-beb8c88e09d0 | -9.63195 | -61.46568 | 2025-07-04 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 776c415a-c1c8-3481-ab7c-aa443ad557f0 | -9.58588 | -68.56934 | 2025-07-04 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README22.md)
