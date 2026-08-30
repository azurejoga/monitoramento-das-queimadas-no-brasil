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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80056c58-3eeb-3061-b981-e7eee055966c | -6.67778 | -58.74186 | 2026-08-30 00:48:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3d27122d-6c0a-31c5-94ce-35efb39d9d4c | -9.15342 | -59.50136 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 2c476697-dee3-3e49-9233-d569ddcd7064 | -10.4903 | -64.50775 | 2026-08-30 00:48:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 24.3 |
| e5512c32-00f3-3561-81ae-ce7180d44edf | -9.14299 | -59.62078 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 973897bf-1b18-314c-86f7-d73f543ac066 | -6.95634 | -55.70057 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 21f365da-9b0e-32d2-8af8-d6837bd63a48 | -8.94335 | -62.36989 | 2026-08-30 00:48:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f982e4fd-86ab-3cf2-b6ca-9f6be32b034c | -9.71253 | -60.74476 | 2026-08-30 00:48:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| bebe9cf9-3b7a-322c-bbc7-2dbc3b7609ea | -6.94736 | -55.717 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 034c6c1e-7364-34c6-b6c5-a091a6aa87a2 | -3.49964 | -54.66382 | 2026-08-30 00:48:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 0e999d64-c3c9-3415-b450-d06cecec7a8b | -3.238 | -61.25294 | 2026-08-30 00:48:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 128e8680-2775-39b0-beda-08d302bb97a5 | -8.22797 | -61.41885 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1dc5ee02-8206-3617-823e-8c8887df92d2 | -8.91758 | -66.95995 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 140b73a4-f27f-38fa-b4fa-f8a0e9551fb3 | -9.89514 | -60.26691 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| aee6ece3-b4d9-3da4-b283-09c701ee1999 | -7.00963 | -59.65857 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 93ff1d65-c92a-32c4-a807-52abf71b22cd | -7.5928 | -61.35359 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f860d949-8d65-384d-b6c7-ee78b9cb470d | -6.07545 | -57.89629 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 825e24fa-3826-3638-bc43-1a6331660b40 | -4.96554 | -55.8559 | 2026-08-30 00:48:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 08184abf-d4f2-3368-8532-cdd45c2aebef | -6.91147 | -59.48658 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| cd92173b-0bd4-30ab-b0da-5c8a0fc184ee | -8.61542 | -54.78724 | 2026-08-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 18709f6c-cb78-339d-a286-f80d2ab91dc2 | -10.57258 | -59.61628 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 037df9e1-fa49-3327-af38-a709d3c555b7 | -8.49624 | -55.29189 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3bd49296-4ac7-330c-8dfa-e95d652a5b2c | -6.82843 | -59.42139 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ed7f4828-5c1f-3800-a672-c0ad6a48fbd7 | -9.15588 | -59.51917 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5558c803-de67-3430-9f82-54377e54c44a | -3.23679 | -61.2442 | 2026-08-30 00:48:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c9124a2f-ba4d-3ef0-85c9-09b8c227eb35 | -7.0901 | -51.59048 | 2026-08-30 00:48:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 0b439d6d-b963-34d5-8cce-9f82bd680eb4 | -4.15891 | -60.72393 | 2026-08-30 00:48:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 05e69541-916d-3840-96c9-f57ce60b2ac8 | -7.56068 | -61.32727 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 166759d6-6474-31ca-813f-639f7f233563 | -9.04547 | -65.41814 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 8abf4961-216c-3a91-8079-d6af75927f9a | -9.18224 | -59.62697 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6a25dfb8-943e-317e-9f78-a5bb34cc917d | -8.9447 | -62.38018 | 2026-08-30 00:48:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 69e5be89-6e98-3c7d-a56b-cc755f6e7352 | -7.29803 | -60.60584 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| c388b82d-f563-3d51-9975-dc543f437f83 | -6.6967 | -60.12592 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| aaf7f16d-ee16-3a06-8fcd-a4a39faf047b | -7.29682 | -60.59701 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 468dac83-f3fc-3c75-809e-67b656842d73 | -10.49819 | -59.61478 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 98a4e45d-f42a-3c28-a0f6-3a4316fc750a | -6.86321 | -59.46586 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| af26fd23-611d-34af-a890-52c824eea686 | -6.90738 | -58.99464 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d83806a8-661a-350f-99d2-e2516ed46077 | -6.12494 | -57.69045 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0a339469-9be3-388b-b3b5-5cd5f4d9fd5f | -9.06839 | -60.48448 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e238aa23-5c18-3f0a-aa21-2ad3740a8c31 | -6.12649 | -57.7014 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d454acab-fa84-304f-abf9-be0ebfa56855 | -6.93839 | -55.73325 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 4c45c2ab-0932-365a-9853-9cec991ce2cb | -8.17766 | -54.93569 | 2026-08-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7fa12f73-5ab3-30ac-b3f2-2d7ae8acec14 | -3.63159 | -60.56838 | 2026-08-30 00:48:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5abcded2-e94f-3a2e-bdfe-8cebfc99c0dd | -7.55944 | -61.3182 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 6503f7d9-1d1e-39a4-b0b8-0d19375659d5 | -9.71375 | -60.75385 | 2026-08-30 00:48:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b987fdbf-8ec5-3408-9236-e1503c2d4367 | -6.7728 | -60.01011 | 2026-08-30 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8d028557-18d0-361f-b48f-3d7e9d54a629 | -7.31683 | -60.61219 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b5fd5739-914a-3a90-91a2-c79cbbbf45b1 | -3.63037 | -60.55956 | 2026-08-30 00:48:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 4d9761c2-076f-3cc8-81d2-1d4f6981bfd9 | -4.15771 | -60.71516 | 2026-08-30 00:48:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f0f484c4-57bd-39d1-8fdb-779d7b6fb411 | -4.12221 | -60.78273 | 2026-08-30 00:48:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9a38b31e-6cd1-350b-9191-76c1ca29f0dc | -6.08913 | -57.71807 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eb951cf0-2769-308a-af65-5698c735bb9d | -9.97831 | -60.26736 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4b7e3d43-5c0a-3597-9598-9734d78b1266 | -9.7101 | -60.72666 | 2026-08-30 00:48:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 1dc8004b-587f-3eaa-999e-9241306b86ef | -8.58359 | -66.96409 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 80e33d0b-59b0-3539-a1ca-65b0683ed82b | -4.15408 | -60.68883 | 2026-08-30 00:48:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 9d4e9123-ee1f-37d6-97f9-0fdca38f90b8 | -6.70832 | -58.56049 | 2026-08-30 00:48:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 577cc8a7-a3b9-3c49-8351-c47a6b9bbefe | -5.89895 | -57.7471 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b2fd0a8c-05f2-39f7-9d18-1e5635281b6a | -4.95158 | -55.8334 | 2026-08-30 00:48:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8b3d1bdc-9c0f-3303-b941-a54d325560bc | -9.2195 | -59.76637 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7039f882-e8c0-352c-8056-39b88bdf18b4 | -9.9084 | -60.15007 | 2026-08-30 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8cad0c84-deb1-31b6-9413-e4d8e3d90574 | -3.19661 | -61.16661 | 2026-08-30 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7510dd9b-0f52-398a-9bca-aa5fde5c30f8 | -9.70364 | -60.74604 | 2026-08-30 00:48:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 609c026e-3fcd-3ad0-8a57-62a82a06f685 | -8.95415 | -62.37889 | 2026-08-30 00:48:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9d3fc623-da6c-38e3-a73a-16a84c2b7e43 | -6.18431 | -55.45079 | 2026-08-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 28393478-e628-3d95-81a4-57dca8fcab95 | -8.93149 | -67.3808 | 2026-08-30 00:48:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| dd71c4d3-8007-3a82-bb3d-b776fd36b0c3 | -9.30555 | -56.79986 | 2026-08-30 00:48:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4145a972-51dd-3a49-9f66-7d40fbcb848c | -9.05727 | -65.41666 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 001b1afd-40eb-3bd3-ba61-8d2e72f86f22 | -7.06379 | -59.72369 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4355b44d-bab3-382f-ac5a-1558601f46e2 | -9.01109 | -60.60765 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0be55b59-bf3d-3362-b240-5a2b358f2a71 | -9.05933 | -65.43328 | 2026-08-30 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 04b5d8e2-50c0-358f-82c3-69ebc900526b | -7.57776 | -61.30938 | 2026-08-30 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7546bddb-f954-3644-bdad-aacf355c1767 | -6.94731 | -58.95079 | 2026-08-30 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83564a34-c041-3c88-9079-f44c9e32c86c | -3.90295 | -60.93874 | 2026-08-30 00:48:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 44d94a06-f865-3a10-9780-7111c5375eb1 | -5.87096 | -57.77937 | 2026-08-30 00:48:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 0860dd9f-b8a9-3176-90be-64122b04e629 | -6.11579 | -53.56381 | 2026-08-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c2ec0d53-6c50-33d3-82ce-8892e5759bb5 | -9.16741 | -59.5203 | 2026-08-30 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8a35be37-33d1-3ee1-bcac-4a7c9e1f9048 | -11.3431 | -45.1521 | 2026-08-30 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 97454da8-5fef-389d-998c-fee38ba654e2 | -7.5477 | -61.3247 | 2026-08-30 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ac63a036-ca65-3364-aa2b-0aacb985b2b0 | -4.9604 | -55.8424 | 2026-08-30 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| d0dff84c-eca6-3831-a5b1-93afcd01067c | -11.3068 | -54.0299 | 2026-08-30 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| dcda6223-8aad-3cea-83ae-32d118ad5d4b | -7.5661 | -61.3239 | 2026-08-30 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 29e5aba8-673e-343a-8b2c-41f88c615795 | -10.9401 | -43.0355 | 2026-08-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| bf06bb8a-d835-39b6-a7ab-5c7c778ff90e | -10.7407 | -54.0401 | 2026-08-30 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 861b0cea-ce93-32c8-8bf4-29ed419ef0c7 | -10.8062 | -45.3178 | 2026-08-30 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| dea458c3-0442-3a5b-82c4-84af2143b1af | -6.9361 | -55.7157 | 2026-08-30 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 233.2 |
| 20952a2f-ce02-3819-9a71-aa57f1223417 | -3.6215 | -60.566 | 2026-08-30 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 15dbe82f-10ad-3466-95ee-4f1c52312789 | -13.8563 | -54.0967 | 2026-08-30 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 270.7 |
| 4794e219-5427-34b5-8369-37f3634a0424 | -6.9546 | -55.7147 | 2026-08-30 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| c2c2790f-bc03-3225-b208-29bd9cc2d811 | -10.9593 | -43.0326 | 2026-08-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 2aa530cd-d92f-3b21-ab55-4ab056a496da | -10.9405 | -43.0117 | 2026-08-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a7b1796c-2cf2-3dfa-90c6-ea24b132bfd7 | -3.6398 | -60.5656 | 2026-08-30 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 27d90019-121c-3b55-9d54-7e7eb93c4ed4 | -4.1516 | -60.6878 | 2026-08-30 00:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 15a01bb3-d1d9-338d-988d-23e97a70613f | -9.043 | -65.4175 | 2026-08-30 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f92a4ab3-33ba-3a9c-a4c4-3a046bf606e5 | -6.9363 | -55.6958 | 2026-08-30 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| b8f7d966-dc82-3258-b313-d5f81f4877b8 | -13.8368 | -54.1197 | 2026-08-30 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 264.3 |
| c75a4d2f-fec1-3063-9a0e-48b04ad5951f | -3.6216 | -60.547 | 2026-08-30 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| da8f9015-69b2-3734-82e0-ec7d7386ae63 | -10.8253 | -45.3152 | 2026-08-30 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| bde6e2ec-f1ad-3f34-b1ac-d243ac9937ab | -13.8557 | -54.1383 | 2026-08-30 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e3d2440f-55df-3c4d-8cbb-a2a741cf2697 | -11.3066 | -54.0505 | 2026-08-30 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 53b493c4-eb67-3b4c-a8b7-80f1ca382b9e | -5.4876 | -57.1416 | 2026-08-30 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 7313fb11-99f0-3037-87df-7b573af7e2db | -5.8894 | -57.7708 | 2026-08-30 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |


[Clique aqui para ver as próximas entradas](README13.md)
