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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bf913a6-9d1f-3bf2-80d2-03af74b6b459 | -12.6476 | -54.0075 | 2024-10-06 01:41:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6118305-166d-39c7-a8f2-ab2cd3523497 | -12.6512 | -54.021599 | 2024-10-06 01:41:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b39c1ead-7fdb-3ac9-9b3d-a361865fac9b | -12.6548 | -54.035702 | 2024-10-06 01:41:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed0d8ec-ce4d-3735-9db7-5650e4ab7ab9 | -12.6415 | -54.0242 | 2024-10-06 01:41:54 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca821143-58ae-3a42-aea3-49190b6281e1 | -12.6451 | -54.0382 | 2024-10-06 01:41:54 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72a7ea34-ebb4-392c-9cb9-eaaf77e969d3 | -13.7296 | -60.648399 | 2024-10-06 01:42:02 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95f52188-940b-3c3f-b5f1-b63ec851593b | -13.7312 | -60.655399 | 2024-10-06 01:42:02 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff71d8c2-9af1-3aef-b457-a5f3bdeb263c | -12.1428 | -54.259102 | 2024-10-06 01:42:03 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c54d457c-f095-3d17-886b-b0828e2e670f | -13.1391 | -59.689201 | 2024-10-06 01:42:08 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ed9d650-f2b3-3f3a-96fd-61c3bd729fbc | -13.1407 | -59.6964 | 2024-10-06 01:42:08 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0cd4fcc2-0c99-3f8a-a133-cdd682171e7a | -13.0237 | -59.8605 | 2024-10-06 01:42:10 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8a36bf35-5b2b-38f4-874b-3be576dc5513 | -13.0254 | -59.867699 | 2024-10-06 01:42:10 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 22f87591-ea5a-3fe9-a21e-a866c0044f64 | -13.4259 | -61.914398 | 2024-10-06 01:42:11 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b79cacf7-da56-323b-b94f-30ca67eb83c4 | -11.6405 | -54.520901 | 2024-10-06 01:42:12 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f620eff-ea71-383a-aa1b-00349151c46b | -12.9718 | -60.083302 | 2024-10-06 01:42:12 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec457194-3d64-30ab-8513-c430ff8c83d3 | -12.9734 | -60.090401 | 2024-10-06 01:42:12 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 308533f6-5c9b-310b-8497-0530e40eb8fd | -13.3899 | -61.937698 | 2024-10-06 01:42:12 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cec46649-3b99-33a0-97d5-4479cb609294 | -13.3915 | -61.944901 | 2024-10-06 01:42:12 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 21d47a75-bd34-34c7-94a2-b5017529eaf3 | -13.3947 | -61.959202 | 2024-10-06 01:42:12 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c1dbec8-b66c-329e-b506-88cee62a17ca | -13.3801 | -61.939899 | 2024-10-06 01:42:12 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 306fe89c-4929-301d-8c1d-9393ba64ecdd | -13.3817 | -61.947102 | 2024-10-06 01:42:12 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2546269-09a8-38ea-9c01-d4153c0beab3 | -13.3833 | -61.954201 | 2024-10-06 01:42:12 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 71381c12-48fa-3621-b0ea-408eb66be319 | -13.3849 | -61.961399 | 2024-10-06 01:42:12 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d758bfa2-f803-3260-b84e-a96af76bbf83 | -13.3864 | -61.968601 | 2024-10-06 01:42:12 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 826922e2-ea1e-3ec6-bd06-082b4f1a60f8 | -13.388 | -61.9758 | 2024-10-06 01:42:12 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 62a918db-1958-3edd-90fb-aecf2243fb01 | -12.1461 | -56.682499 | 2024-10-06 01:42:12 | METOP-C | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 306a62ce-545f-3503-b512-cf01912c634e | -10.8902 | -52.3634 | 2024-10-06 01:42:15 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6660642b-924a-3d88-b27c-8989850390a7 | -10.4342 | -50.674599 | 2024-10-06 01:42:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87d76e7e-6915-3642-9e1d-75cd94c238e9 | -10.441 | -50.700199 | 2024-10-06 01:42:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94a21e87-3367-3a86-bf53-d68092c286a9 | -12.873 | -60.508202 | 2024-10-06 01:42:15 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d2090ca2-cda7-3601-9513-0c989a8c3283 | -10.4177 | -50.651501 | 2024-10-06 01:42:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8511e19c-df42-3206-9bba-30a1ccb02164 | -10.4246 | -50.677299 | 2024-10-06 01:42:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef0527d5-7f59-3a50-8498-c8468f35d00a | -10.4314 | -50.7029 | 2024-10-06 01:42:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e02d7c08-786b-3ebe-a95e-a583f93f02ec | -10.4382 | -50.728401 | 2024-10-06 01:42:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c63eceb2-a839-3739-b780-e8243251ce96 | -10.4081 | -50.654099 | 2024-10-06 01:42:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0137902-3dcc-3e47-a3e9-0bff93523ad9 | -10.415 | -50.679901 | 2024-10-06 01:42:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b135489-1125-3e9c-9477-cb5065bc0a08 | -10.4218 | -50.705502 | 2024-10-06 01:42:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa872358-0e39-36bb-9a20-5fc9b536d36d | -10.4286 | -50.730999 | 2024-10-06 01:42:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cecc8ecc-1ad8-3fef-8132-91d5aa171c10 | -10.4054 | -50.682499 | 2024-10-06 01:42:16 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ea03416-9c6e-3c96-becf-a59565467799 | -10.4123 | -50.708099 | 2024-10-06 01:42:16 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e91bdc5-7271-3c42-b36e-a2312558148f | -10.4191 | -50.733601 | 2024-10-06 01:42:16 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78042120-28a3-311b-b5ec-46ca2dd0d4f0 | -10.4027 | -50.710701 | 2024-10-06 01:42:16 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77824507-f4fa-334c-93f0-54bb6e6b832a | -11.0978 | -54.214401 | 2024-10-06 01:42:19 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52b6446b-e9cc-3b32-9c90-ae1406b31f3f | -11.1015 | -54.228901 | 2024-10-06 01:42:19 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41a8a212-fbc4-3057-8bf4-b1c84e13cdba | -11.0882 | -54.2169 | 2024-10-06 01:42:19 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95dc684f-8295-31b7-8183-2f483252b683 | -11.0919 | -54.2314 | 2024-10-06 01:42:19 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d06561a7-8994-30f7-ba36-2b4548558687 | -11.0818 | -54.764702 | 2024-10-06 01:42:22 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7b0a2b2-e092-3454-b0d2-7501a0aec356 | -11.072 | -54.7672 | 2024-10-06 01:42:22 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f18dd87-232e-367e-91de-9e65851d7894 | -12.0263 | -63.732399 | 2024-10-06 01:42:40 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b07b94a4-c19e-3f85-9071-fcb1358a67d1 | -12.0148 | -63.7267 | 2024-10-06 01:42:41 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd17958-bf08-385a-8aa5-eae686ca20f4 | -12.0165 | -63.7346 | 2024-10-06 01:42:41 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 434c99e4-620f-3419-96c9-58aee970aa50 | -12.0182 | -63.7425 | 2024-10-06 01:42:41 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| afaee386-a8bf-3206-b631-b8370f5bdc7f | -12.0199 | -63.750401 | 2024-10-06 01:42:41 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c7cc9bde-d46a-3555-8fad-91a75a55b68f | -9.9075 | -57.467499 | 2024-10-06 01:42:51 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d23a5d5-92b6-3b82-8405-5f7f118fb915 | -10.2108 | -59.394199 | 2024-10-06 01:42:54 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f103428-999b-395d-b144-5b719485198d | -10.2126 | -59.401798 | 2024-10-06 01:42:54 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db869c75-f16b-315c-9973-a6606097d330 | -10.9955 | -63.9016 | 2024-10-06 01:42:58 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 791f46fc-9e65-3fb9-ac7b-4c425ee54d4f | -10.9972 | -63.909401 | 2024-10-06 01:42:58 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 801ac6b0-3b22-3c6a-9f91-1d5ab1496bf5 | -10.3738 | -61.1679 | 2024-10-06 01:42:58 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 586d6510-7942-330f-b342-42d4ff4a103a | -10.3754 | -61.1749 | 2024-10-06 01:42:58 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1917e95c-d32a-3d84-92ae-5abc25df3a33 | -9.8817 | -59.4879 | 2024-10-06 01:43:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa4edf5a-2a15-3abd-ab0a-c5faa37a5e73 | -9.8835 | -59.495399 | 2024-10-06 01:43:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc0e61fe-e539-39f1-a4ec-2c3969cb1b65 | -10.881 | -63.8941 | 2024-10-06 01:43:00 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 938c513f-3756-32ca-8c49-074cb42aa52d | -10.8827 | -63.901901 | 2024-10-06 01:43:00 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b7331bcb-8907-300b-b5f2-719602838f3e | -9.8719 | -59.4902 | 2024-10-06 01:43:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4660221f-0035-3ec4-ac00-77a5723a92ab | -9.7632 | -59.379002 | 2024-10-06 01:43:01 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 365a1bf5-1167-37aa-ba13-9d5f89a091a1 | -9.765 | -59.3867 | 2024-10-06 01:43:01 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1962290-4def-3083-bdb8-f36f3e683c4e | -10.0708 | -61.105801 | 2024-10-06 01:43:03 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc872a5-4206-3a52-98b6-2f73547ce89f | -9.8775 | -60.311501 | 2024-10-06 01:43:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 339700a5-4731-31f8-b97b-acb3b1a429e1 | -9.8627 | -60.292198 | 2024-10-06 01:43:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fe8ebec-ca54-3ec8-b820-8675b9f93056 | -9.8496 | -60.280102 | 2024-10-06 01:43:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 062ea0e6-fcea-3ac6-a0f5-6b36896b1574 | -9.8513 | -60.287201 | 2024-10-06 01:43:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0a16593-e77e-3892-b98e-d62e23ad7fad | -9.8529 | -60.294399 | 2024-10-06 01:43:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a800c73-1773-3f41-a17f-57d8a6b6587c | -9.8546 | -60.301601 | 2024-10-06 01:43:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af641ad9-4efc-305a-ad08-4dcda04e8030 | -9.8398 | -60.282398 | 2024-10-06 01:43:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8b05c3f-eee8-3112-8728-b1035ca5de65 | -9.8415 | -60.289501 | 2024-10-06 01:43:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adbacf09-d10b-3e6c-b78f-0da95add633a | -9.8431 | -60.2967 | 2024-10-06 01:43:03 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1a730ca-70d8-3baf-a702-ad1f5c1523ea | -9.4809 | -61.006599 | 2024-10-06 01:43:12 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02d0ec61-63f4-39f3-b0f4-16cdce07e1e2 | -9.1517 | -60.652599 | 2024-10-06 01:43:16 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76cf0c09-7873-39b9-87c7-a0ab86cda735 | -9.1533 | -60.659698 | 2024-10-06 01:43:16 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a965f939-a74b-3817-895c-200b591181f0 | -9.1403 | -60.6478 | 2024-10-06 01:43:16 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c4a0c6b-dfa4-320a-81a9-935b3475ec93 | -9.1419 | -60.6548 | 2024-10-06 01:43:16 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8f26160-e085-329c-9cbd-66f0c37866c5 | -9.1435 | -60.6619 | 2024-10-06 01:43:16 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd64c922-2ea6-3895-8ea8-1ad7b926f36f | -9.1305 | -60.650101 | 2024-10-06 01:43:16 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d476943-7319-3562-8338-da9d07491a51 | -9.1321 | -60.657101 | 2024-10-06 01:43:16 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ddd9c5d-f85b-3add-8b86-20028a1bc7a1 | -9.1207 | -60.652401 | 2024-10-06 01:43:16 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 949121a0-2eb3-3e74-b1ba-dd8354f23889 | -9.1647 | -61.561501 | 2024-10-06 01:43:19 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f93eaf30-9c9d-3af4-a0d5-9a95394a9565 | -9.1662 | -61.568401 | 2024-10-06 01:43:19 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 05cc1ae3-d2d3-3099-abae-22eead26942d | -9.1678 | -61.575298 | 2024-10-06 01:43:19 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8f4e6f6d-43d2-3eec-ba97-9c388fa77bc1 | -9.6095 | -64.044403 | 2024-10-06 01:43:21 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 22bc4b92-0d0d-30d7-81ba-cbe599ec35a1 | -9.6835 | -64.614502 | 2024-10-06 01:43:22 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a5838df2-fc1c-363e-a5bb-300f76dc0e99 | -9.6852 | -64.622597 | 2024-10-06 01:43:22 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 36b987fb-b9b4-3564-85dd-73c5cd05fd85 | -9.687 | -64.630699 | 2024-10-06 01:43:22 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 00d5ba65-8692-365d-9941-8dc46a7dce95 | -9.6754 | -64.624702 | 2024-10-06 01:43:22 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ce8464f0-63a5-3b11-b91c-e2228431bbec | -8.8375 | -61.483299 | 2024-10-06 01:43:24 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37312dcf-e896-3686-a514-b11a163f1d73 | -8.8391 | -61.4902 | 2024-10-06 01:43:24 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85b52b06-4022-3024-89fa-86279fdfd0e6 | -9.3697 | -64.307999 | 2024-10-06 01:43:26 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 573cd4f9-1d96-3cf6-b453-b523686b7316 | -9.3714 | -64.315804 | 2024-10-06 01:43:26 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad33205-a145-3a83-bc72-b728bb42aeaf | -9.3599 | -64.310204 | 2024-10-06 01:43:26 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 279e3660-147f-3196-82bf-a2136ddf3e78 | -9.3616 | -64.318001 | 2024-10-06 01:43:26 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README32.md)
