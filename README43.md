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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d715d198-afbf-3184-b0bf-ffb3e3b1b743 | 1.5102 | -55.8456 | 2026-09-25 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| a21da5be-fa4c-3adf-aa95-602d82b0ab00 | -10.8189 | -57.1993 | 2026-09-25 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 402d548f-6fe6-3759-bf1a-dbf3b6656513 | -10.8567 | -57.1767 | 2026-09-25 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 6c5ffe74-7221-3bbc-b728-d23a74f3697a | -8.8736 | -62.4115 | 2026-09-25 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 42169382-9cfc-320b-a81b-b46d14cee23e | -11.2002 | -55.0398 | 2026-09-25 15:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6ceeb6f6-c142-3107-86e1-35ebf2681063 | -12.8056 | -54.0462 | 2026-09-25 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 521ab032-efaa-3d71-8c31-bdbf93675bb0 | -7.4735 | -61.3846 | 2026-09-25 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| fd70bd93-383b-30b3-b1c8-d042b55f43b6 | -12.7865 | -54.0482 | 2026-09-25 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 8c5c308b-dcd4-313e-858b-b02e94f3602f | -8.9428 | -63.2797 | 2026-09-25 15:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 29dca822-feb7-381b-8ed5-4d8f3817c4a9 | -12.8056 | -54.0462 | 2026-09-25 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| cbab421b-9ebf-3021-a9ac-202c7fe7984b | 1.6017 | -55.9037 | 2026-09-25 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| f3569be8-4506-3b4b-b083-770f34c38ea6 | -7.5098 | -61.4974 | 2026-09-25 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| ecf58006-4905-3b85-a001-3e662d4cdc46 | -10.8921 | -53.9857 | 2026-09-25 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f7211177-af50-39c0-af80-5b6686e8a8ac | 1.565 | -55.9238 | 2026-09-25 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| d32dcc1a-19b2-3ee9-832f-18a95d6b5632 | 1.5835 | -55.8448 | 2026-09-25 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 37fe17d6-48d7-3abe-b522-6a1a96785cfa | -11.2488 | -54.1378 | 2026-09-25 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4e1b4ff7-5d80-3728-a8d5-a1421eaf0cbc | -9.043 | -65.4175 | 2026-09-25 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 9ec82e67-cdf3-366a-ac33-d139d6181f54 | -14.3503 | -52.0838 | 2026-09-25 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 8cca1bcc-5ca1-3011-862f-15fa5a2f9688 | -11.9832 | -57.5867 | 2026-09-25 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d55fd7dc-fe39-3baa-8c62-e89055b43a77 | -7.5661 | -61.3239 | 2026-09-25 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| ae7ee729-1e84-32a8-8244-766b594897c1 | -12.7868 | -54.0275 | 2026-09-25 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 2603bb98-d3a5-3e96-88bd-072a771b89e4 | -8.8921 | -62.4297 | 2026-09-25 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5b24c8e1-9098-3971-ab85-da0ac6926116 | -7.5467 | -61.496 | 2026-09-25 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| b34f8c87-2695-3dfb-8805-8065eddb9d76 | -8.8551 | -62.4123 | 2026-09-25 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 132a033e-83d7-32d2-8327-c8f4e72f31a6 | -9.0401 | -66.052 | 2026-09-25 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| a25c414a-ce2b-3b7c-b483-41dff81bc6cd | -12.7865 | -54.0482 | 2026-09-25 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 2eb43e2f-d8df-3725-a39e-0a3d2851b2ab | -8.8922 | -62.4107 | 2026-09-25 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6ff5e46a-5853-3c25-95b9-0e1ba660a133 | -7.5283 | -61.4967 | 2026-09-25 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 1c67eccd-2b70-3ca0-a872-0dffcce9fb34 | 1.5099 | -56.0426 | 2026-09-25 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 1d792dde-85fd-3175-8465-ba2d20678e05 | -12.6071 | -51.9595 | 2026-09-25 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 5e627882-4fd6-347f-8eb2-893305be042a | -10.8569 | -57.1568 | 2026-09-25 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 7ebaa9f2-7703-3357-9cf5-ffad9db01dc2 | -7.566 | -61.343 | 2026-09-25 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 0e407312-813e-3cd8-8767-fc53ddef3b6c | -11.983 | -57.6066 | 2026-09-25 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 23d0bc1b-d1a7-3ab2-88dd-71e87cca4cb8 | -10.6827 | -54.1679 | 2026-09-25 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| abdf17d1-8f27-3311-84dd-ac8352363430 | -12.8059 | -54.0255 | 2026-09-25 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 44072217-6344-34d8-b9a9-5b3d5cd640f7 | -8.8736 | -62.4115 | 2026-09-25 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 242267a8-0a2b-3cac-a6e2-59ffb3b1533b | 1.6018 | -55.8643 | 2026-09-25 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| e0055ead-eb0c-3fac-88a4-5ee828aae24f | -8.8736 | -62.4115 | 2026-09-25 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 45388769-9c2c-3b70-b14b-78117045cb78 | -6.9862 | -63.0096 | 2026-09-25 15:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 8ef963a2-a744-398d-b15c-61388725f30c | -7.5098 | -61.4974 | 2026-09-25 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 77a1fa69-c181-34f9-a60d-dc8e493a3644 | -8.9428 | -63.2797 | 2026-09-25 15:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ae86f2e3-6a22-3bd1-aaab-ac521f6b1f20 | -8.8921 | -62.4297 | 2026-09-25 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d6af88e6-4321-36ee-b2f8-ba7f69c9c76f | -8.8551 | -62.4123 | 2026-09-25 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 77d79672-eba6-313f-89d7-97e39bf38d93 | -10.8532 | -54.0916 | 2026-09-25 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| e18274f8-5994-3232-888a-865c2a01ba26 | 1.5468 | -55.8846 | 2026-09-25 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 5cbe6482-9f56-3ff9-b1f2-26775673152f | -8.8735 | -62.4305 | 2026-09-25 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d7a63ae0-8a7a-3c98-8e4c-f60ecd6b59bf | -11.3255 | -54.0487 | 2026-09-25 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f732befd-bb5a-3f28-a920-fc2a65546a9a | -8.8922 | -62.4107 | 2026-09-25 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f4f2ade9-a2e2-32ba-80a8-b9ceb248ef7d | -14.3503 | -52.0838 | 2026-09-25 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 161d7d55-9e61-3c51-874f-6e23f5c2f641 | -14.3693 | -52.1026 | 2026-09-25 15:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 3efab9ba-65e4-3b8c-9622-a98d5df417d8 | -11.983 | -57.6066 | 2026-09-25 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 52b3142b-4eb1-30e0-bad9-05f4d71ebb4a | -11.2488 | -54.1378 | 2026-09-25 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5ec7fa68-26c0-3b53-a6d0-023161cb850f | -13.203 | -51.7406 | 2026-09-25 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8446f8ab-cc99-3d7d-9efb-346e17347696 | -10.8921 | -53.9857 | 2026-09-25 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| e035f8e1-ca9f-326b-bf58-e27c07ce43e1 | -8.8736 | -62.4115 | 2026-09-25 15:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ec4a12a0-bb86-37ae-baa9-b4a52e9a639e | -10.7115 | -60.7312 | 2026-09-25 15:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 5054562e-2c97-31e0-b38a-a8f679867f58 | -8.9663 | -72.8525 | 2026-09-25 15:50:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 64.9 |
| bcecd8b6-533d-3d7a-b70f-f863217fd11f | -8.8922 | -62.4107 | 2026-09-25 15:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d03afa28-aa1f-34c6-8163-cb043c4f3f85 | -8.8551 | -62.4123 | 2026-09-25 15:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 00dda32e-5070-393d-a015-d64275aca7ff | -11.2488 | -54.1378 | 2026-09-25 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b7dbda05-066d-33d2-b2f6-c2fa4ac29e0b | -13.2061 | -51.549 | 2026-09-25 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| fd79c25c-8040-3d9c-b862-8c364cb6b6ca | -13.2249 | -51.5679 | 2026-09-25 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 72da5a13-0ac6-3334-a99b-ede43b3776e5 | -6.9862 | -63.0096 | 2026-09-25 15:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| efaf1eba-af20-3b58-9fa3-b3e0fff72a64 | -11.983 | -57.6066 | 2026-09-25 15:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 139b7fb0-fd6b-3ef9-800a-b3a6af5c70b7 | -13.2057 | -51.5703 | 2026-09-25 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 32ed9f70-8324-37c5-bc70-2e637708f170 | -13.2054 | -51.5916 | 2026-09-25 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 74ed64d5-d43c-3955-b143-5c5bd852a75b | -11.3255 | -54.0487 | 2026-09-25 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ced15909-005b-302f-9cf6-c37702aab520 | -8.9428 | -63.2797 | 2026-09-25 15:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2a56e3bb-1f6a-3ef5-b09c-5aa618f791eb | -10.6928 | -60.7322 | 2026-09-25 15:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f86f1ce5-b558-31e9-93f1-cc043e3e4cdd | -7.0051 | -62.9149 | 2026-09-25 15:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 20ebf07c-2584-32fe-a250-972065156674 | -8.8921 | -62.4297 | 2026-09-25 15:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| db657da0-6a41-3cad-b03f-72c7b3000fa5 | -12.8059 | -54.0255 | 2026-09-25 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e5545f4d-ba59-3266-b4bc-89cb57202efa | -11.2677 | -54.1361 | 2026-09-25 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| f6a8c14f-2745-3d9f-85a8-8bde7d469ae8 | -12.8994 | -52.8301 | 2026-09-25 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 82055e6a-2335-344b-a646-bbbd31620f6c | -13.2253 | -51.5466 | 2026-09-25 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 1db39099-aff8-373a-a7f3-acb4361bf3cc | -10.6928 | -60.7322 | 2026-09-25 16:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 50ed31b7-34b4-3b2e-b055-7c163cb77a6a | -10.7115 | -60.7312 | 2026-09-25 16:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1d80eea2-c906-3910-b1ad-d30f28465e03 | -13.3247 | -51.3211 | 2026-09-25 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 53e0bc3f-20aa-389d-838f-6d0adc501920 | -9.0402 | -66.0333 | 2026-09-25 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| a9119dbb-6bdc-30e4-b34c-1c162576365d | -7.3641 | -72.4622 | 2026-09-25 16:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b27fe47e-8f6c-39a2-9c6e-a77dd0eac9db | -12.1952 | -52.7821 | 2026-09-25 16:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| ada72530-ca4c-3d49-951b-3b979b232d3b | -13.3251 | -51.2997 | 2026-09-25 16:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| ba0cceb9-fafc-3344-b98a-95e45f99a017 | -7.0234 | -62.9331 | 2026-09-25 16:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| cb252e3b-ea65-3369-ad79-8b86980186b3 | -8.9428 | -63.2797 | 2026-09-25 16:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3bdbc776-4849-366d-af1b-20f51ca80bab | -13.3632 | -51.3163 | 2026-09-25 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 292.2 |
| 88d272d4-6398-3117-9ac4-fc618b980b63 | -13.2057 | -51.5703 | 2026-09-25 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 0a7f1a10-0f76-3c9e-bacf-0d4e41b30bfe | -7.0051 | -62.9149 | 2026-09-25 16:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 4d8252f9-9b8e-3285-99a5-50e3603159d4 | -8.7129 | -69.8135 | 2026-09-25 16:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 4687bce9-0ac3-32a7-b81c-06fffac2f991 | 1.6199 | -55.9429 | 2026-09-25 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| ecc2ea9c-f829-3677-9231-0b01c652f7c4 | -9.0402 | -66.0333 | 2026-09-25 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 820e9cc8-4bc2-3a22-aa0f-b2b100d07acf | -9.0401 | -66.052 | 2026-09-25 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 16dda3b6-6854-3e85-9f0f-2dd4b5a08aaa | -10.6928 | -60.7322 | 2026-09-25 16:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1e955f40-0bd5-3468-9c9f-40f68a9bfe78 | -8.9428 | -63.2797 | 2026-09-25 16:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b909f1bd-dff5-3f04-8b5d-dd01140a8de8 | -13.38 | -51.35 | 2026-09-25 16:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0486d466-04bb-3e02-9dc1-d04808d9e8e5 | -13.38 | -51.3 | 2026-09-25 16:15:00 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24949a66-c6a9-3c03-9caf-7abf48be262e | -12.0 | -50.74 | 2026-09-25 16:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c506b523-89e4-3e10-a8e3-d849ab2f3e15 | -11.97 | -50.73 | 2026-09-25 16:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2426284e-c5bb-3811-8d71-6f540bd995a9 | -10.6928 | -60.7322 | 2026-09-25 16:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 01e9eb60-88a9-32bd-a67b-48d06f4713f5 | 1.62 | -55.9232 | 2026-09-25 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 9e554a19-bf2b-3225-a9e7-76ded9a60490 | -8.7129 | -69.8135 | 2026-09-25 16:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 49.8 |


[Clique aqui para ver as próximas entradas](README44.md)
