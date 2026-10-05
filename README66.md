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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bee4f0cf-00c7-3660-a47c-5715add81f31 | -9.7874 | -65.0173 | 2026-10-05 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 7407cfb5-c786-3071-a55e-15e59e06fe8a | -13.5007 | -61.1333 | 2026-10-05 15:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 6814cd81-b904-3e96-be44-fa9a07b1fccc | -13.5008 | -61.1137 | 2026-10-05 15:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 948318d4-4122-3025-93ec-f96c7e811480 | -9.1334 | -65.9 | 2026-10-05 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| d9af5f5e-b89a-345b-b852-c728dfa74e80 | -13.5197 | -61.1319 | 2026-10-05 15:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 95578a93-98b4-3a9b-84f2-8635199ec94c | -9.4565 | -64.3344 | 2026-10-05 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 12f78236-8cb3-38f6-93fc-8a767489fdf4 | -8.593 | -66.8081 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 2321c4d6-93ea-32ed-afc3-d00c0d718e28 | -3.2755 | -54.1819 | 2026-10-05 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 208.1 |
| 03128f85-3a4a-3f36-b941-672c184c7142 | -9.1408 | -64.3836 | 2026-10-05 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| cf2912f5-58a8-3769-930f-6e25ed0043bc | -9.9175 | -65.0313 | 2026-10-05 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 49b8afe5-4222-3132-80ce-e017365da410 | -9.8246 | -65.016 | 2026-10-05 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b71f0003-cd51-31fc-817e-106ca66aef49 | -9.0046 | -65.6988 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 27b1b767-3681-35a1-bcb3-5e1ab04149a4 | -9.0982 | -65.4904 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5759445b-281f-37d7-bf99-f0e1bd9e0791 | -9.0988 | -65.3596 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| da2632c2-22c6-337f-b0d9-b504cdd240ab | -13.5199 | -61.1124 | 2026-10-05 15:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 95.9 |
| f58a607a-749f-369d-acbe-90f8f89aadb6 | -9.4116 | -65.8912 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 6e4a6b08-1110-3abc-8fde-a4e85bf78d15 | -9.0059 | -65.4186 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ce9363f0-ef17-3278-ab08-1f6c460056bd | -9.1334 | -65.9 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 189be3f7-9f12-3613-af1f-61e36dee4aa1 | -9.1426 | -68.2941 | 2026-10-05 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 7954b0b7-ab87-3e64-9b18-fa5dc3aaeb72 | -1.9535 | -54.0493 | 2026-10-05 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 1b3b7b6b-34c9-3aec-b4a7-aa1c54f8532a | -9.1259 | -67.7581 | 2026-10-05 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 81f2c941-9a24-3ed9-80f2-bc3366c87fec | -9.0987 | -65.3783 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5c6ee7c1-cb36-3077-9320-54c8d93a9653 | -8.6214 | -69.5026 | 2026-10-05 15:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c35d2b34-7faf-3e80-b10c-4a1db825ea6b | -9.1335 | -65.8813 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 3a81e989-b3d1-3d27-a852-f46d86713a70 | -9.1222 | -64.3843 | 2026-10-05 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| ae252bf6-f9b5-3eba-8796-3c74573ce31d | -9.1445 | -67.7577 | 2026-10-05 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 271d38f9-a3c4-365d-b581-53e4e259e84d | -9.1535 | -65.5634 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d6bb3f05-cecf-3b88-9ca2-5631c5e3949f | -9.043 | -65.4175 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 122c0d7d-da90-3dcf-9ac4-1a5fa5ec4dca | -13.5197 | -61.1319 | 2026-10-05 15:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 45238642-635b-3295-8f89-4b15bfa5ff16 | -13.5008 | -61.1137 | 2026-10-05 15:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 83.5 |
| b1bb6f96-36b6-3684-bd7c-1ad1d1b75f58 | -1.4569 | -54.796 | 2026-10-05 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ca5ee401-9290-3802-b161-c31c452e7259 | -13.5007 | -61.1333 | 2026-10-05 15:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 46ee3edc-b687-3f1f-a1a9-106f8a508208 | -9.1174 | -65.359 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 83ef8b95-a42c-3687-a734-6882a3130192 | -1.2455 | -49.0194 | 2026-10-05 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| ac575b15-a306-36cb-a9ca-9318fff7d447 | -9.1905 | -65.5809 | 2026-10-05 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 4b7fd500-0418-3f1c-be37-857da9f470ff | -10.97 | -45.46 | 2026-10-05 15:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e42d80c7-193b-3c18-a72e-ab230cb5e58e | -10.97 | -45.41 | 2026-10-05 15:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6bd10440-ffa4-3425-a585-248fc811b272 | 1.978 | -60.6099 | 2026-10-05 15:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 623.1 |
| dc273b8d-b518-31a0-bfcd-551c98e4b4b3 | -13.5008 | -61.1137 | 2026-10-05 15:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 7c614b01-440b-3f4b-a05b-dbd51aa2c861 | -9.043 | -65.4175 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5f1b0631-e1a0-3d04-adc4-f8f1502fd92f | -8.6115 | -66.8076 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d2393ae0-ac5e-3dc3-9fd1-f3b28b867b14 | -9.4751 | -64.3336 | 2026-10-05 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| cda5e22f-761d-39c3-a986-9f9642127092 | 1.7399 | -50.8235 | 2026-10-05 15:20:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 76.5 |
| aa97dd14-b5a8-3877-bdc8-43c9a0a7ee38 | -9.1407 | -64.4024 | 2026-10-05 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 88ffdfed-ef7e-3337-9e18-d5194080f78f | -13.5007 | -61.1333 | 2026-10-05 15:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 64ad9302-1cb4-3309-bf75-6cf2255dbf2a | -1.4588 | -53.6136 | 2026-10-05 15:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 15a82585-dca2-3799-b452-392bf2b21c23 | -1.6396 | -55.1319 | 2026-10-05 15:20:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d8bdf80d-78d7-3f33-b279-4dd457e5457b | -9.0615 | -65.4169 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6231b095-05af-3687-b6bd-9c2850e6b158 | -9.9175 | -65.0313 | 2026-10-05 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 759c7ce4-02c0-36cb-9212-b9178e91edc5 | -1.1094 | -54.1401 | 2026-10-05 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b72b3cce-ae6e-3f35-89a4-69e8cae2e62d | -9.7872 | -65.0549 | 2026-10-05 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7a437160-4709-3025-8015-cd508538594a | -2.0447 | -54.3085 | 2026-10-05 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 81102ef6-e3b1-33e2-81d4-b14dde35ebb3 | -9.4565 | -64.3344 | 2026-10-05 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3670f6e8-9dfe-3487-bcf0-84371328f3a0 | -9.1259 | -67.7581 | 2026-10-05 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 211.6 |
| fd414437-cd94-3131-8b95-d6360c873928 | -9.006 | -65.4 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 249a9d18-762a-341d-b905-0f144df2908c | -9.1173 | -65.3777 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a26e5a12-8d52-30bf-96e7-cdd4bf60ea27 | -9.1613 | -68.2383 | 2026-10-05 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 9204e33f-70ed-349e-b21d-a6a54a0b08b8 | -3.0734 | -54.147 | 2026-10-05 15:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 80507445-4d7c-3d1d-ac6f-45530d8abad4 | -8.956 | -68.7966 | 2026-10-05 15:20:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5011beea-cfba-31a7-a6ad-f1413f0d9b4d | -9.1445 | -67.7577 | 2026-10-05 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 6d6fc88c-6cd9-3778-90ff-c5db8af39e2b | -8.5918 | -67.1418 | 2026-10-05 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a0c5fab8-0a91-37c6-9008-1881f7f711a9 | -9.0059 | -65.4186 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b905af9e-593b-3847-a6f7-7579fa462599 | -13.5197 | -61.1319 | 2026-10-05 15:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 97.2 |
| a9a8fffb-6b23-3d7d-bd6e-194ded37730c | -9.1426 | -68.2941 | 2026-10-05 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6e7a7bb5-7f12-3c01-b93f-52d2de30d392 | -3.3135 | -53.839 | 2026-10-05 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| e4d833ad-8a37-3ff5-b4fc-5825d0460929 | -9.1222 | -64.3843 | 2026-10-05 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8092f7dc-191e-3fe9-a88f-f2a81904acd3 | -9.0046 | -65.6988 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| fb024942-4745-385e-a5d8-2e5586bd7b28 | -9.0244 | -65.4181 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 681b4ae4-4daf-36e7-bc1d-8835777d66ea | -9.1535 | -65.5634 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 6dfce828-9bee-341e-8231-dc600f488bc7 | -9.1408 | -64.3836 | 2026-10-05 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 23b898e9-b6ad-3450-9bb2-fbf6fd69adc5 | -13.5199 | -61.1124 | 2026-10-05 15:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 16d61fe9-2063-35e8-8bc4-0ab315443af0 | -9.1335 | -65.8813 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 355b0bcc-5683-32ff-bb2f-c378cb5635c8 | -9.0982 | -65.4904 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 06927894-2801-3238-a87a-cbbac6ef20d6 | -8.593 | -66.8081 | 2026-10-05 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f91b2561-6cc9-3a26-891c-35da88ada0eb | -8.6115 | -66.8076 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 43ceaeb3-fd10-3242-868f-79495afb838f | -9.8246 | -65.016 | 2026-10-05 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 325ea7d6-addf-3bc2-aa3c-120a71549911 | 1.7399 | -50.8235 | 2026-10-05 15:30:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 1ae4923b-ec94-3d13-b772-e5a7ad8042d2 | -2.0447 | -54.3085 | 2026-10-05 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 12c72ba1-6844-3b1d-ba11-3c53f4557e30 | -9.0987 | -65.3783 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 75d09332-6bce-3ec7-bebb-8f1bf28e2bc6 | -9.0982 | -65.4904 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6ebd7003-499b-3e07-8179-9b3bccfc85b2 | -9.1259 | -67.7581 | 2026-10-05 15:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 230.2 |
| 5a923c5f-1cb0-3fb3-9435-63226f74f7a4 | -9.1536 | -65.5447 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 21ce3c27-3271-36e4-ad0d-03b5027ef3ea | -9.4751 | -64.3336 | 2026-10-05 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 30385b3b-a5d5-3d04-9b8b-8307d05dfffc | 1.7583 | -50.8232 | 2026-10-05 15:30:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 73.0 |
| bd851780-f8ba-3544-b60d-8eceeb8bf624 | -9.1407 | -64.4024 | 2026-10-05 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 06a58554-5452-309a-aca3-3482f82e8063 | -8.5918 | -67.1418 | 2026-10-05 15:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 86d7c796-0e5c-32b1-9f8d-9a5e0cfc4bed | -9.1335 | -65.8813 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 91d27520-1704-362a-8027-22a9fbbe36a4 | -12.6109 | -63.0852 | 2026-10-05 15:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| dbbe2fe6-d075-3e0b-a6b1-673b03ace1ff | -9.0046 | -65.6988 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| bd2621ec-99c2-30d4-81d4-2d9f17b84821 | -9.1535 | -65.5634 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 802296f6-d43c-3310-ad1e-b2be2cc744c1 | -1.9535 | -54.0493 | 2026-10-05 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 240459bb-abff-3d6f-a599-98dbafae05cb | -9.0232 | -65.6982 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 574bc560-612c-33dc-aab1-0b5c8f6bc463 | -1.639 | -55.5282 | 2026-10-05 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4b8ac47b-486e-3304-a2cb-5943f8550792 | -9.135 | -65.5453 | 2026-10-05 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 17209abb-b630-3df0-a808-996b7f32776a | -8.956 | -68.7966 | 2026-10-05 15:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 66b5d928-d76b-3bb8-8e7f-357e9ac07f7c | -13.5199 | -61.1124 | 2026-10-05 15:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 23ae0ef5-b28d-3304-b86c-c40db3be286b | -9.4565 | -64.3344 | 2026-10-05 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 2d2209a7-4a36-3a13-95e4-35ec53d1d8c3 | -8.5733 | -67.1422 | 2026-10-05 15:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| fabc541d-29c5-3fdd-8500-98cc0d650d5a | -13.5007 | -61.1333 | 2026-10-05 15:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 140.1 |
| ffacc5d1-7f43-3ee4-8814-5b33af01f0a9 | -1.4756 | -54.5365 | 2026-10-05 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |


[Clique aqui para ver as próximas entradas](README67.md)
