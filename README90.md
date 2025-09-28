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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c163112-1036-3c33-a94d-44d0256e5824 | -9.64597 | -62.84334 | 2025-09-28 05:46:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 32.2 |
| cc35e2bb-35e6-3cf5-8e5f-231609791f1f | -11.62045 | -52.84736 | 2025-09-28 05:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d16f3e92-5326-37e1-84ac-e1b8a3412d42 | -12.234 | -60.84785 | 2025-09-28 05:46:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e3595d7-9da9-33e2-ac37-345f4ef04484 | -9.78315 | -64.98236 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 786d043d-1961-37c3-bc66-6ded1e569e49 | -9.89928 | -65.13259 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b5ba31c-d21b-38e2-9f35-e6bd39cba2da | -12.0198 | -63.23135 | 2025-09-28 05:46:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 758d94cf-b8d2-3138-92a6-05ac54961771 | -9.934 | -65.15272 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2a00fc6-fb6f-3f0d-92df-7a8d58f88e2e | -9.91475 | -65.0102 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afcafbed-0565-3609-a5e6-8595c8651f04 | -10.99263 | -57.06756 | 2025-09-28 05:46:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96debfb0-b10e-33b6-9b6d-730e9a215182 | -9.93965 | -65.20481 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1eaa8b4-76cd-3f7d-8204-a8dc0870f1a1 | -11.5187 | -54.31192 | 2025-09-28 05:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08db5873-fac5-37f6-be70-d3cf61ae9448 | -9.77978 | -64.98183 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 419945b3-d7ec-385f-95e0-2d1bd2203e10 | -10.00291 | -64.24975 | 2025-09-28 05:46:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd18d9eb-3dc8-3275-9d0f-cb608c55f331 | -9.80235 | -61.49288 | 2025-09-28 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 782cd853-0925-3aae-b596-ca9ecddc21d6 | -9.94769 | -66.86323 | 2025-09-28 05:46:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41884ede-a91e-3d8d-91c0-482eec8614b1 | -10.99307 | -57.06421 | 2025-09-28 05:46:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 247d647f-1b37-3f50-bd7e-faf672a70410 | -10.37911 | -57.48352 | 2025-09-28 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f00e28a1-5eb2-3777-aaa0-347903eb18c3 | -9.74548 | -62.36085 | 2025-09-28 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d23bea4-0e69-38f1-bdb2-4b41f9c05d6f | -9.56576 | -63.20518 | 2025-09-28 05:46:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25dd16d1-e038-39eb-8269-4b91010b2e1f | -9.9368 | -65.15681 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2744502b-c010-3557-bd8a-89bea4fa0ac5 | -9.943 | -65.20535 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46a65716-c3e0-3ba5-bddd-6333bae51aa7 | -9.65326 | -62.84439 | 2025-09-28 05:46:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 10c90cb6-a044-3883-9c3d-f32b63a897bd | -9.81024 | -61.49405 | 2025-09-28 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79447c75-18db-351c-93b0-42d0660aa691 | -9.57292 | -63.20624 | 2025-09-28 05:46:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a349dd1-588b-33f8-82f0-722dbb782b5a | -11.62327 | -52.8538 | 2025-09-28 05:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7448f82-f314-3e11-bc48-860a4e1ebb86 | -10.39559 | -69.04956 | 2025-09-28 05:46:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69d44808-c473-3189-9e84-a08dd6a8146d | -10.14412 | -67.2236 | 2025-09-28 05:46:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44bc187f-6460-3ebe-95a9-fb9194ca4b50 | -10.99892 | -57.06156 | 2025-09-28 05:46:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42c848ba-43c1-3282-acf2-812f122f590b | -9.65089 | -62.83543 | 2025-09-28 05:46:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 34512b81-361e-3141-8685-113f7e8bd444 | -9.88402 | -58.29089 | 2025-09-28 05:46:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f259671-c47c-36a0-b818-7c2229b6a2b1 | -7.86106 | -63.3145 | 2025-09-28 05:46:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7113a71-477f-3d0d-899d-64a89cb1c60c | -10.51548 | -69.04439 | 2025-09-28 05:46:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f18068ce-26ec-3922-8fe6-7c2ed7d64982 | -8.9473 | -65.92426 | 2025-09-28 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6da67f26-c3d9-37d1-9e07-5faf0645303f | -9.50924 | -54.6672 | 2025-09-28 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b6d1992-ec87-30a7-8538-3f22fa72f263 | -10.1625 | -64.73704 | 2025-09-28 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bb59733-4893-3841-8d1a-9e858a6d8256 | -9.56219 | -63.20466 | 2025-09-28 05:46:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff074aaa-4cb0-323e-84a2-6e02ba2381ef | -7.86166 | -63.31062 | 2025-09-28 05:46:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfb113b5-fe2e-3e92-bbc7-872e32c2bad7 | -11.15105 | -54.31041 | 2025-09-28 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27d9f6a0-2c48-3d3c-b410-af2e3329be14 | -9.79842 | -61.49228 | 2025-09-28 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d956acd-29e9-325a-9c5b-cf6a198f79b0 | -9.50978 | -54.66279 | 2025-09-28 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a39fca7-0998-3956-8ba3-2a4af9bcee0a | -9.56157 | -63.20874 | 2025-09-28 05:46:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 592981a8-8676-382f-809a-720b4b82aa54 | -9.56515 | -63.20926 | 2025-09-28 05:46:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51d0592a-1c79-3d40-931b-4bcfd6c3d698 | -10.99488 | -57.06744 | 2025-09-28 05:46:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9367b7a7-9a09-34b2-a629-3bd7809f9f58 | -11.62405 | -52.84668 | 2025-09-28 05:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5a905ca-49e6-32ba-aa16-3113194aa30c | -10.99529 | -57.0641 | 2025-09-28 05:46:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3449f84e-1386-39f0-88b9-9fddf34bd474 | -10.99847 | -57.06494 | 2025-09-28 05:46:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df2c6e1b-e6ac-3ba6-ae5c-0be0d0867171 | -8.61759 | -54.98771 | 2025-09-28 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6e8a60a-ccc8-3158-93dc-1be4fd6ae3d1 | -11.52462 | -54.31513 | 2025-09-28 05:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2b5cadf-1d19-3e42-814b-378a97c7bae8 | -9.88553 | -58.29211 | 2025-09-28 05:46:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5476821-b10c-354e-92cc-9dfde8825c68 | -12.23454 | -60.84389 | 2025-09-28 05:46:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a664654-ee95-351e-a9fb-4380a6c52236 | -9.75684 | -65.03378 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b816e5a2-f1d4-38e2-a2c0-89df98009290 | -9.73362 | -62.36359 | 2025-09-28 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03ce07e9-37fb-3473-9d36-09e9e11dfb12 | -9.5784 | -64.42964 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7feb5fb1-bb7e-3a1c-9f23-a07b300b7ccf | -12.23028 | -60.84331 | 2025-09-28 05:46:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2657db12-289b-356d-8473-f82ed412a0ac | -10.20342 | -61.41309 | 2025-09-28 05:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 841af6c1-a33e-3999-ab01-8993b3e76482 | -9.73651 | -62.36654 | 2025-09-28 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29e609fb-9a40-3836-be5a-93a5d8f8af09 | -8.61704 | -54.992 | 2025-09-28 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6014467c-7ae2-3057-817f-9036b2c668ad | -11.24956 | -61.16903 | 2025-09-28 05:46:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db938cdc-84e4-36b2-9445-68cf614cbd0b | -10.14748 | -67.22415 | 2025-09-28 05:46:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 547ace49-ac46-382f-a9cb-5be9e24c5980 | -9.76021 | -65.0343 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e0c148e-9641-33c6-9914-22ec40c577cd | -12.19391 | -63.66688 | 2025-09-28 05:46:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd555a06-2235-3815-ab4f-51a615d09655 | -9.40675 | -54.69669 | 2025-09-28 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42aae735-4c05-3d36-bc25-dfa15ff0c74e | -8.61555 | -54.99059 | 2025-09-28 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59d58eed-10c3-3ef5-b388-6cd5a39242b6 | -10.18791 | -62.2261 | 2025-09-28 05:46:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ad351a6-f5cd-34e5-82eb-d8f033459709 | -9.51163 | -54.66251 | 2025-09-28 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f7ffff9-0369-3a67-a55b-994992cd297f | -9.17649 | -61.79948 | 2025-09-28 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d278195b-2cce-3aae-9c3f-9ab72a85b8b0 | -10.00348 | -64.246 | 2025-09-28 05:46:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdbddf6e-2b54-3541-8437-7a4f1b31eedc | -11.14398 | -54.31483 | 2025-09-28 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cdd5e3f9-7ec8-321e-baa3-75872e205e47 | -9.62024 | -67.37863 | 2025-09-28 05:46:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8298b52-1410-35f1-b35c-efc7838fe604 | -10.04771 | -62.45496 | 2025-09-28 05:46:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ae66769-a4ac-3813-826b-2fd36675741d | -10.82144 | -69.09293 | 2025-09-28 05:46:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 576911c2-3141-3ba7-b8ef-16711be42bfc | -7.1942 | -71.50138 | 2025-09-28 05:46:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05b31501-5949-39c2-8f25-a4df884d490f | -9.93736 | -65.15325 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c96dbac1-935a-3141-81e9-11a112268d4e | -10.41526 | -67.51564 | 2025-09-28 05:46:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25d17fc4-7892-3b01-9a1a-4acd216fe02f | -11.6225 | -52.86077 | 2025-09-28 05:46:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f63018d-570c-36d7-bc0c-28b0c02460f4 | -11.15041 | -54.31583 | 2025-09-28 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c88abd79-c7d8-3e67-b695-e70060298723 | -9.67515 | -62.39404 | 2025-09-28 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 934f27af-a2a0-3d65-8fb5-8dfc3f9f1310 | -9.64775 | -64.56783 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a76cef6-32a4-3428-9cd6-b5685c4873e5 | -10.04707 | -62.45946 | 2025-09-28 05:46:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec76e1f7-57b5-361a-9a46-dd2279df2293 | -9.51105 | -54.66695 | 2025-09-28 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dbafc5f-ce1d-3026-a254-c40863d716f6 | -8.93878 | -63.87223 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93bab433-7c6b-358d-b948-323d3e4a86f3 | -9.86579 | -65.1712 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d125f416-4ea0-30d4-a0bb-526ac580e6b2 | -12.4051 | -63.89484 | 2025-09-28 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 171084a2-d30c-3b86-8a0b-45458385a69e | -10.29059 | -67.27345 | 2025-09-28 05:46:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33220a4f-bf93-323e-a2fb-523bf08d2662 | -9.91083 | -65.01326 | 2025-09-28 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f7fa12c-1897-3f13-bef0-85a38566b1ea | -12.22974 | -60.84727 | 2025-09-28 05:46:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 310d881a-ed2a-38b7-9b01-f1e27d8c01ab | -12.89066 | -62.0999 | 2025-09-28 05:46:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cafdba4-6999-3ea5-87b3-b3427d506004 | -11.51814 | -54.31425 | 2025-09-28 05:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b3edc1a-40c0-3447-922c-7c6763258af8 | -10.28723 | -67.2729 | 2025-09-28 05:46:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4013515c-d300-3997-8c1e-5a69bb3c8f88 | -9.91347 | -58.56275 | 2025-09-28 05:46:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6154746f-07c8-3102-855b-c3476ebe9179 | -11.14298 | -54.31662 | 2025-09-28 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cac77820-c055-329f-a169-726c28056899 | -9.4135 | -54.69281 | 2025-09-28 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7283ec29-a606-31b6-83c1-a7c2dae8f115 | -10.04638 | -62.45622 | 2025-09-28 05:46:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79e65eab-2952-3aa6-b798-ffc2fa43c633 | -12.01613 | -63.23079 | 2025-09-28 05:46:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0229a13a-6087-307c-b944-913f56fe82b8 | -9.73736 | -62.3642 | 2025-09-28 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f796fbf-a58c-3e68-a409-1aac6a592163 | -7.8651 | -63.31425 | 2025-09-28 05:46:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b5b99ae-2c41-31d9-8c25-8b052e98d99b | -9.5628 | -63.20058 | 2025-09-28 05:46:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f7629dc-97ee-3ed8-935d-9e2da5f7bf15 | -10.42528 | -64.88555 | 2025-09-28 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca263b98-a5c7-349b-ba84-7bd2d84b3adf | -9.73718 | -62.36205 | 2025-09-28 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fb26fc7-3e2f-3641-8e78-7b012e2c050a | -9.55861 | -63.20412 | 2025-09-28 05:46:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README91.md)
