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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 642f3a8e-ae42-30f1-ab76-3b24f9b1c0af | -10.75811 | -57.22958 | 2025-05-18 05:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cf206d15-4d7a-384a-bddf-1bd37ea89a57 | -12.68681 | -58.1328 | 2025-05-18 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8c97e60-e528-377d-91d9-47621139ce5f | -10.04224 | -64.97764 | 2025-05-18 05:38:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94092415-e7ac-35f1-9a6b-9b54a72cd70a | -12.12187 | -54.66562 | 2025-05-18 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3a05ad1-d245-310c-93d0-8d71fa351a5e | -14.0178 | -55.12852 | 2025-05-18 05:38:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a492883-7185-38eb-9423-9aadf575ae02 | -14.02235 | -55.1315 | 2025-05-18 05:38:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efab911d-0895-3c54-9e86-805f69207ffa | -12.03719 | -54.97055 | 2025-05-18 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02742e83-29db-35d7-937c-754d8ed0c45f | -12.03979 | -54.96317 | 2025-05-18 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92d0a340-6c2e-38e1-a84a-4bd2ef13f489 | -12.04335 | -54.96741 | 2025-05-18 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 075f54ce-8f5a-35a1-8eba-eb0480b510e7 | -12.12765 | -54.6665 | 2025-05-18 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11165825-7230-3052-b2a4-6ab1b696b354 | -12.03671 | -54.97432 | 2025-05-18 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da500101-de35-3c2b-be0f-630ed95d8e4a | -13.14321 | -56.8066 | 2025-05-18 05:38:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d678fa0e-0afc-370d-b69d-3d77d35b7572 | -14.02264 | -55.13757 | 2025-05-18 05:38:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ede361d-3128-3751-b14f-09d65a1b1784 | -14.02137 | -55.13979 | 2025-05-18 05:38:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 062be3ca-1f0d-3b3e-bbef-d4d926940da1 | -12.03844 | -54.97458 | 2025-05-18 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7aff651c-02d9-3c0f-9459-1c62e80898d8 | -12.03888 | -54.97081 | 2025-05-18 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16d1f595-468c-38c8-8c5d-363c284163a0 | -12.03934 | -54.967 | 2025-05-18 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bfb0617-2a9f-3bc4-bde3-3673e7ea0a6c | -9.24237 | -63.28731 | 2025-05-18 05:38:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 539445c8-c0c3-3775-b03e-59723736c061 | -10.75741 | -57.23478 | 2025-05-18 05:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e7742fa0-3c9f-38b4-aa0c-f5be42cc8454 | -11.65063 | -54.39145 | 2025-05-18 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 393a1234-3fdd-3972-8cc5-8b028d446ec8 | -10.05667 | -64.99439 | 2025-05-18 05:38:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f32c421f-3be1-3805-9867-33721e885658 | -13.04113 | -53.71817 | 2025-05-18 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e405d32-34cb-33b0-bca4-fab2ea7ab700 | -9.5803 | -63.2474 | 2025-05-18 05:38:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 595aa938-c297-3693-aa9c-032e24555f06 | -12.12237 | -54.66149 | 2025-05-18 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ac19baa-f700-37c1-ab61-a59e77818b8f | -11.4269 | -54.29652 | 2025-05-18 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5e9adc0-5cdf-3bec-84da-78ddf64a07c0 | -12.03366 | -54.96622 | 2025-05-18 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c2ee1db-8512-3e6c-aa2a-38adac6a942a | -14.02356 | -55.12929 | 2025-05-18 05:38:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95301728-695b-39c2-9f8d-b322f55c2b65 | -12.03322 | -54.97002 | 2025-05-18 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a22fd416-b620-3467-9771-3772bd8779ef | -14.01688 | -55.13681 | 2025-05-18 05:38:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7eb13b6a-fb4b-35f5-9579-ef9b7583b718 | -10.66957 | -57.63823 | 2025-05-18 05:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c8fc8f2-c38c-3ebf-ac4e-6855e03a31ae | -13.14831 | -56.80722 | 2025-05-18 05:38:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6537a0f-bc1e-30b7-a212-7cc8767db4a1 | -12.30229 | -52.47139 | 2025-05-18 05:38:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b683bc2-8644-3ebd-a623-0e100332f74c | -10.05278 | -64.99737 | 2025-05-18 05:38:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a23ea1c-5881-3982-b7f3-74e359b805b4 | -11.29672 | -53.97719 | 2025-05-18 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7e63134-ec39-30c7-ab5d-df514856f409 | -13.04737 | -53.71877 | 2025-05-18 05:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d235d88-1ae2-32bd-a7ff-90b4591216b9 | -9.23844 | -63.29037 | 2025-05-18 05:38:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4817573-8764-368c-b624-5ec36ddbb7a4 | -12.03766 | -54.96675 | 2025-05-18 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8ad46d28-b1ca-3e1d-ae9a-c103636b7a48 | -12.12865 | -54.65819 | 2025-05-18 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e703ae32-1711-3fa2-a34b-d25ff9910269 | -13.14793 | -56.81027 | 2025-05-18 05:38:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fba7ba63-cb49-3023-9570-712c06cbc634 | -10.68348 | -57.60527 | 2025-05-18 05:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 816ad2cf-f93b-3273-b251-2e1cb8ce33a4 | -9.58367 | -63.24793 | 2025-05-18 05:38:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f9add9f-a52c-3140-bc51-699a151a2f80 | -10.05334 | -64.99385 | 2025-05-18 05:38:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e373e250-c0a2-37eb-9d43-fd7737f54644 | -11.65011 | -54.39573 | 2025-05-18 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d435dd4a-8f8b-30d9-b358-eec2d524d438 | -11.64478 | -54.39061 | 2025-05-18 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88c731ad-d8af-3249-a28f-b52850d33068 | -9.28714 | -57.54826 | 2025-05-18 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fed1a228-b06c-3545-88be-61f2fb50d936 | -10.68281 | -57.61025 | 2025-05-18 05:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8abf9288-1979-3a5d-9d0d-0329dc92bbc8 | -14.0281 | -55.1323 | 2025-05-18 05:38:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcfddf9e-bc8b-341b-a401-542981910176 | -12.12815 | -54.66235 | 2025-05-18 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18f10c1a-5ef4-3438-ad3f-087b297a696e | -10.37219 | -57.50218 | 2025-05-18 05:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a76478f-2d38-38e2-8863-ce8291ca0d6a | -11.41848 | -54.31668 | 2025-05-18 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58d3b000-556a-3a83-be4f-065ba339e6de | -11.13109 | -58.61612 | 2025-05-18 05:38:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b34f270-07f4-3092-a4b0-da6816350607 | -13.14282 | -56.80966 | 2025-05-18 05:38:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11d56198-7e91-3c3e-81a3-6b0d31c75506 | -14.01562 | -55.13903 | 2025-05-18 05:38:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b13b33a-1866-3ed9-8ee9-3f0826d48aaa | -9.29172 | -57.54892 | 2025-05-18 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 945c3a45-96cb-3e2b-b550-8cf61d0cedb3 | -19.06534 | -53.45399 | 2025-05-18 05:40:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c3f71b7-cc91-3f96-ac08-37ba18df7c29 | -20.95193 | -56.60743 | 2025-05-18 05:40:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 72728766-63db-3dd7-8df4-f5636e86a06d | -20.95722 | -56.6124 | 2025-05-18 05:40:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 754845c2-d257-3863-b9ca-7c5c7255e36c | -20.95088 | -56.60568 | 2025-05-18 05:40:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7d87f21e-46f6-35b0-9c04-a98da2df0ad7 | -20.95232 | -56.60318 | 2025-05-18 05:40:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3be55a83-980a-3d52-b369-bdfbfe6c99a6 | -13.85063 | -59.72486 | 2025-05-18 05:40:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9168ddde-c441-30af-8887-2258253815c1 | -17.75418 | -56.30875 | 2025-05-18 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 55214d2f-26c0-347c-b358-1f9b07de3616 | -20.95153 | -56.61165 | 2025-05-18 05:40:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 724203a4-c4fe-3ba2-bf55-d79778f0686b | -20.95045 | -56.60992 | 2025-05-18 05:40:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4563bde0-937f-382f-866c-13b4842f6525 | -19.06484 | -53.45988 | 2025-05-18 05:40:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f1f84319-ad69-3065-88ef-fdb76e5f2df0 | -20.95762 | -56.60814 | 2025-05-18 05:40:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c045f64a-060d-314d-adc5-3989c4de36d8 | -17.74858 | -56.30808 | 2025-05-18 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| f5350773-0032-3346-b2de-24df4aa172c6 | -20.9513 | -56.60148 | 2025-05-18 05:40:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73c45015-734b-39bf-b160-9df2c92074de | -6.6431 | -41.995 | 2025-05-18 05:44:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 599a52c8-587e-314b-aec1-27e6258ca5d9 | -9.5654 | -47.58171 | 2025-05-18 05:44:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aec7afa9-49b1-3e8d-b991-de1fc8c77336 | -7.94716 | -49.75831 | 2025-05-18 05:44:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b44fb603-2207-3b20-83a4-35d426f4d992 | -10.48873 | -46.51475 | 2025-05-18 05:44:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8e38c7d4-e4c6-316d-a2af-23f48979dffe | -10.47968 | -46.5134 | 2025-05-18 05:44:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a94d78e0-adab-3911-a1b3-bcab8d072198 | -11.78756 | -49.31697 | 2025-05-18 05:46:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 049ea62e-e1b1-39e3-b6d5-1e7008cf1255 | -11.57529 | -47.60759 | 2025-05-18 05:46:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 81884430-3c0c-38f2-85ea-fd032a77a8d2 | -12.09921 | -44.75459 | 2025-05-18 05:46:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3d6f7294-2c36-3612-8f13-85f3d9e73ac1 | -19.06498 | -53.45546 | 2025-05-18 05:48:00 | AQUA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f0b898f6-f5e8-3a75-b6bf-80204cb9c817 | -20.94257 | -56.61058 | 2025-05-18 05:48:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8d58af5c-bb52-3203-a6df-b55d8986724a | -22.77259 | -47.62822 | 2025-05-18 05:48:00 | AQUA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| ecf57d97-da27-3ed1-a150-db94577a5d9a | -20.94608 | -56.59191 | 2025-05-18 05:48:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 20bbcdad-7d97-3aee-bb45-83ef1668a663 | -10.05315 | -64.99899 | 2025-05-18 05:59:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb89a6ef-23d9-3896-a97d-ae429c672a59 | -10.05369 | -64.99502 | 2025-05-18 05:59:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab1b4463-7a05-37b1-8351-c2fba148dd98 | -10.04944 | -64.9944 | 2025-05-18 05:59:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d988657c-eff8-39a8-8395-70cd8620d193 | -9.24299 | -63.28865 | 2025-05-18 05:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e63b554-5bf6-3100-ab65-4ad83ac1131a | -10.75749 | -57.23767 | 2025-05-18 05:59:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14840a8b-0161-3e94-a1b6-0de9b82beb38 | -10.0489 | -64.99836 | 2025-05-18 05:59:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05cba2e0-b316-37d9-91b3-7d282beec078 | -10.75829 | -57.23073 | 2025-05-18 05:59:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ed3f9cf-218f-34c7-971d-c56ec591fa7a | -12.461 | -57.1879 | 2025-05-18 11:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| ed3628eb-d9a7-313b-825f-bf66221014e5 | -12.461 | -57.1879 | 2025-05-18 11:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 48feb1da-07d2-3fe2-aba9-73da9ca33d6b | -12.461 | -57.1879 | 2025-05-18 11:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 512847a9-b5ce-30a5-a20b-7553d0057664 | -12.4608 | -57.2079 | 2025-05-18 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 9facd127-b4b2-3d2d-a188-53f7bf39751e | -12.461 | -57.1879 | 2025-05-18 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 213.6 |
| f342387c-3e67-39bb-90ee-9c651d190b73 | -12.461 | -57.1879 | 2025-05-18 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 209.0 |
| 2020bffb-aa4a-3412-98e9-64a520165ee8 | -12.4608 | -57.2079 | 2025-05-18 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 0dedcc27-e5e0-3a55-8451-fc4976c13738 | -12.4608 | -57.2079 | 2025-05-18 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 897d5ff8-8edf-3733-b9c2-4f9b70bf05a1 | -12.442 | -57.1895 | 2025-05-18 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| b81a2cab-dfde-30bd-b715-81ddb1d337c2 | -12.461 | -57.1879 | 2025-05-18 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 194.0 |
| 8cb29dab-2bd9-3a85-9baf-01b7b7dcf297 | -12.4608 | -57.2079 | 2025-05-18 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 51e2d85f-f34d-3080-aad2-49b6ded05cbf | -12.442 | -57.1895 | 2025-05-18 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| dc8cf377-1adb-3d5d-9cc8-082a87d640ab | -12.461 | -57.1879 | 2025-05-18 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 280.5 |
| e469e0c2-6886-3cba-9582-c684a9433ccb | -12.461 | -57.1879 | 2025-05-18 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 262.2 |


[Clique aqui para ver as próximas entradas](README9.md)
