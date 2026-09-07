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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a54ce6b-8c91-3a06-a087-d8eec5629f22 | -13.25788 | -61.72546 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 33b259c4-13e7-3d60-813f-79711c42d864 | -13.07393 | -62.21098 | 2026-09-07 05:25:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| addbe459-373f-3a83-a9b9-82f61d019598 | -7.78858 | -56.34395 | 2026-09-07 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69758db8-0318-3480-b684-7d392f277894 | -13.27539 | -61.71742 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28098b7a-8ca6-3564-8170-d928a82537f3 | -13.27561 | -61.75815 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 26e901c4-0669-353a-b596-b3a9c140d366 | -13.28405 | -61.74847 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cca62c88-2994-3eed-9748-20172d8a774b | -13.2512 | -61.72432 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 626c2911-2571-394e-aa3d-853bd3f79777 | -8.50193 | -54.64896 | 2026-09-07 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af659a3f-6632-3824-a9c0-ef7dc8112bb2 | -13.2762 | -61.75455 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a81f577-4bd7-3af3-bc41-0702c1a2e972 | -13.22182 | -61.7786 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cc7ff2c-624f-32e2-b9ae-0d8175867009 | -6.76812 | -59.43333 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b0a7dc3-7ce1-3f28-b557-e84e9f7d2e60 | -7.61126 | -57.61122 | 2026-09-07 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f687f0ba-1165-3d6d-aff5-1f83d99fb097 | -13.2554 | -61.76206 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1ac9b61-c00d-3ef8-a8f3-5420a900d639 | -13.29132 | -61.746 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e845498c-c824-326f-ad46-89bdb9aef995 | -7.61808 | -57.61228 | 2026-09-07 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85007945-6c74-3256-ae19-09abf8d3271f | -13.25846 | -61.72185 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f7607920-a69f-3554-8f29-c74d446ed3f9 | -13.23609 | -61.73287 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 31.5 |
| aa8c3db4-a07e-3ed6-8854-9a0c5e66a78d | -13.21062 | -61.78411 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3611a1e4-6c88-31ea-9d1e-85f04384f887 | -13.22516 | -61.77917 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0e4a13d-a2c4-3224-ab5e-38bc396d909f | -6.70394 | -58.93688 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86720252-e79e-3324-a3b1-88f5cd7a0ec1 | -13.23636 | -61.77365 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65604ed2-d36b-3095-81ab-068b00d0cd68 | -13.22215 | -61.7342 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f0843419-e899-37d3-bdd9-da4b0bbbd8fe | -13.2618 | -61.72242 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 72a935e0-5448-3fd7-a8b4-145b986fd25e | -13.25816 | -61.76623 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce815117-a59d-3bb1-bd9b-da870adcab0e | -13.23275 | -61.7323 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 17702030-ece3-3dad-90d2-1dafe0704143 | -13.28207 | -61.71854 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b25ad004-7999-30b4-83da-29aafbe7ab8a | -13.27873 | -61.71798 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a96650f7-0249-33b0-a9e4-b42d4b5b8b96 | -13.26572 | -61.71939 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b46dcc79-b6d7-3b37-a63d-b09ba8a3f467 | -7.17075 | -59.5508 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57a017d1-a812-346f-a559-97710e4e65ca | -13.28347 | -61.75208 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6244b42e-75ef-3fc5-9f45-e5e9ce34bde6 | -13.22549 | -61.73477 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 3d4491cc-efb3-3b52-a752-12bae1384b11 | -13.27814 | -61.72158 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3bfc8966-1c59-32a6-b561-21c478fe14f5 | -13.27954 | -61.75512 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6095e41-691a-3038-9ebf-2b18f3ac5297 | -13.25148 | -61.76509 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 750b6bb9-6675-30e3-a288-9f51186228b4 | -13.25062 | -61.72792 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 92b1bf86-fe7a-350e-93ae-7873fba95f1e | -13.21396 | -61.78468 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a957700c-88c4-3eec-bb20-61c2e9c2d60f | -13.22157 | -61.73781 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 0e280352-49a0-3ff6-8845-8ff32c8225c3 | -8.50144 | -54.65245 | 2026-09-07 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f6a9f10-ec9b-3bfc-9da9-c2e5aa5ebdd8 | -13.2724 | -61.72051 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b3e52708-c691-3e3a-82f9-a18a2c1b69fb | -13.29817 | -61.72497 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c44f4783-45a2-3600-8872-606672883869 | -13.25482 | -61.76566 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 063606aa-484b-3606-872c-1a3e45bef8d7 | -13.26514 | -61.72298 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 75c8c42d-b09c-3d32-bda8-436619e7de66 | -7.69834 | -55.38106 | 2026-09-07 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f845b7fb-032c-3bfb-8c89-49b99369e69c | -6.82002 | -58.99815 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac30bef7-6537-3c9e-a8e6-72607ab7476e | -13.27227 | -61.75758 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da1e0dfd-9b3b-341a-bd97-67fa91a283a7 | -13.29191 | -61.7424 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01433d21-2a98-3863-96fc-6bc9de648504 | -13.23334 | -61.7287 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 10f67626-a0a9-34b5-8a67-6148570ecf01 | -9.93404 | -48.04958 | 2026-09-07 05:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fa07074-2205-34f8-862f-fce6f57887b4 | -6.65037 | -59.95967 | 2026-09-07 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 440c496c-4a0a-35e6-8044-cefa2fd1cc03 | -13.26906 | -61.71995 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e430a76e-b4f8-3fb8-ba01-623f36069acf | -13.22883 | -61.73533 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 1bc2ed9e-668b-3bd4-bdb8-49e8366ad606 | -13.22123 | -61.78221 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b13da4fd-b494-3dc5-9601-ab3da80b0641 | -13.23243 | -61.77669 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ef09ba0-c6b4-3822-a0ab-5cc67e391227 | -13.07453 | -62.20729 | 2026-09-07 05:25:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28581f46-e73c-3763-bc5d-5655297a2733 | -13.2406 | -61.72623 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 2704c824-29e6-3219-9bd1-f1e0dc22a9bd | -7.69764 | -55.3857 | 2026-09-07 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c240a38-2871-3638-b4ad-b138f26c7627 | -6.63781 | -59.44067 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a2e9b0b-f761-331d-b641-3b642bd4c066 | -13.26267 | -61.75959 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6405a592-d8a3-382d-b18e-f6aca0c6d5cc | -13.24161 | -61.7412 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd56be00-c087-35ca-8fa7-3dc09af7d8d6 | -14.52516 | -59.80454 | 2026-09-07 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00ab49b0-0548-3aa7-97a5-3bdda219332d | -13.2285 | -61.77974 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 424da180-8316-336c-8db8-6fc743b52a37 | -13.24028 | -61.77061 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cef0fcf-8dbb-327d-a8c8-63ad1e48c867 | -6.76481 | -59.4328 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83e94f55-e28f-35ce-a5a7-e928fad59ec8 | -7.69005 | -55.38459 | 2026-09-07 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbeb4bc9-7687-301a-99d9-b9d33af35220 | -7.70144 | -55.38625 | 2026-09-07 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44faef5e-aea2-3e7c-83b8-ad5f367c63a7 | -13.22607 | -61.73117 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| cd86f8cc-1735-34ca-92a8-38ecc652f643 | -13.25454 | -61.72489 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fb99d0d4-9e2a-3d67-a04d-b4fb4782cb12 | -13.2143 | -61.74028 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| ffd11346-7e89-306b-b28a-9509b59cea73 | -13.24697 | -61.77174 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6dc841b8-eb87-3193-958e-e5cfd68e0012 | -13.28739 | -61.74904 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2217ade-d47b-393e-8f77-559b9d100169 | -13.2748 | -61.72101 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f8073c4-0071-3c48-8b6b-27ba44662f95 | -7.61467 | -57.61175 | 2026-09-07 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63044dcf-1af7-3302-b073-3fc78eec0724 | -13.24394 | -61.7268 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b3264b58-98c8-3a9e-9ac6-0a831e3431d4 | -13.24363 | -61.77117 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ec5ee76-40f6-3301-83fe-070901e22d22 | -13.24728 | -61.72736 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5e663356-bd0d-30f4-ac50-5cdea5151d28 | -13.23668 | -61.72927 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 54fe332b-13fd-3e9b-9598-ccdee0411ff9 | -14.52851 | -59.80513 | 2026-09-07 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8576c43a-f7b0-3559-b8bc-091c5701b169 | -13.26848 | -61.72355 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0cecbe8b-73fe-3bc7-a02d-d63e89b51d95 | -13.26208 | -61.7632 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f0fe2e6d-b20c-3c2d-9c7d-6fbfb657de73 | -13.21789 | -61.78164 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0313d4c9-f107-35be-b64e-fbfa98fa63ca | -6.6537 | -59.96019 | 2026-09-07 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| da28dddb-100f-3fd5-9b13-1a945063b0b1 | -13.2397 | -61.77422 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dde4a34e-241d-39e2-a2aa-5509eef4a8d7 | -13.25874 | -61.76263 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aec43475-a68c-3d2b-bf24-ace7c791aca7 | -13.22909 | -61.77612 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fafa0c94-6904-3b13-be23-409904e7fe5b | -6.82056 | -58.99469 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b717ab7-10d5-3c75-a55f-dce5d6832422 | -13.21822 | -61.73724 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 20aa7bee-46fa-3369-bd36-d7fa2ff2bd6f | -13.07055 | -62.2104 | 2026-09-07 05:25:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f30c14f-fd93-3f95-98e8-b07dceebb2c8 | -13.23 | -61.72813 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| aa5b77b9-0a3e-3bae-af8e-56c8c3093f8f | -7.70213 | -55.38163 | 2026-09-07 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9c751e5-b640-3398-b8d1-98f48b1603f0 | -7.6141 | -57.61544 | 2026-09-07 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4625a396-dc29-3a3a-98b9-928d139baf7e | -13.24336 | -61.7304 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 8d4c5db2-fbbe-3ca7-9b6a-caeb92e0d9ec | -13.29484 | -61.72441 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95dba0d9-67c8-352f-ab9c-554e44d12040 | -7.61069 | -57.61492 | 2026-09-07 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51677821-c1d1-31a2-80c7-52f650c87c52 | -13.24755 | -61.76813 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 802314b8-8296-3733-b900-f1e691b503bc | -13.23827 | -61.74063 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eaec3af-fe32-3871-b182-f1ad17e8fc10 | -7.69384 | -55.38515 | 2026-09-07 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7d78602-1432-35c1-8c1b-59a622b5ff04 | -6.59825 | -59.11173 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 453d5ca0-5377-37be-9bd7-2e302589717b | -6.75816 | -58.95998 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 301f03f7-b8fc-3a84-83a3-53e066741b8c | -6.64112 | -59.4412 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6acff79d-8be1-3ac4-9db1-a742fc10fcb6 | -13.21764 | -61.74084 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README35.md)
