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

## Dados Diários - Página 217

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b8d346f-a62a-3834-afcc-0acedfec649c | -13.46189 | -61.11662 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b34475c3-712c-38ef-be5e-e2c1eb67085e | -13.16432 | -54.35353 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63301756-128c-3042-a39f-3dec91b6fd39 | -11.99524 | -57.61149 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c48f6d9e-de28-3287-8632-d4010964bf09 | -5.68801 | -53.47464 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0148180-92a0-3bc2-add9-fe25f1d7e91d | -12.20943 | -57.10249 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 424e87fd-3233-3053-b853-5a13e8ae5d74 | -12.78221 | -60.60638 | 2026-10-09 05:25:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff9eb3ce-c15a-3835-bc96-a615adaaae6d | -7.61283 | -46.53113 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed103711-6879-3fa5-9c4d-e74132af0442 | -6.11321 | -57.85992 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cbf7d7b-a712-3814-9d38-7e1c80874c4f | -6.43861 | -55.0423 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df0ae750-ad84-368d-a37e-cb7f39c18987 | -6.50004 | -55.38568 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38e458bb-2d0d-3609-bdbd-35aff2b0c856 | -5.69284 | -53.49877 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7286c4f0-8932-3305-8565-f2a37bb96279 | -6.53924 | -56.04996 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 324347cb-fc1e-345e-bd01-305dcfb45125 | -8.21886 | -46.41656 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2bf8a3e3-9b26-3d74-a78c-92f39f7686df | -5.69333 | -53.46759 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8a4451e-dfa2-3ed4-bc86-9c2dd69f325d | -4.80794 | -56.14274 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ed87bd6-703d-3ebc-9992-6c375154d1dd | -6.5123 | -55.40588 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5bf1d9aa-b785-3c71-b8af-f14165a78c2a | -6.53986 | -56.04584 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 181f27c0-c0b5-3dca-a488-b72e27d425c4 | -4.06689 | -59.83406 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f2cb823-4091-32c7-8a53-cb5499bca864 | -6.50857 | -55.40533 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8dcd841-7c6c-33fe-832a-f88d6515d81a | -5.21949 | -60.04946 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cbde9baa-1ba1-3618-9faa-f01fe3a8a326 | -6.23614 | -52.88608 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e758e083-0e23-334f-8b14-8b2462d563ec | -4.74178 | -55.67603 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 232e07da-1bfc-3d51-9d08-ca3fd8e350a2 | -5.97193 | -55.34858 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1d0c21ba-ef17-32ce-851b-241f82acb6da | -7.5067 | -47.33717 | 2026-10-09 05:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd33a000-ef12-398d-966b-ee13e6321d72 | -4.73346 | -55.6581 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8979a3e2-4461-3a0c-addb-b2da74425237 | -5.70501 | -53.45652 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46f3d4e5-804b-342d-8930-e68117291925 | -6.4469 | -55.0388 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8af4a78-b60e-3990-aaa1-a018bd5be439 | -4.74301 | -55.66791 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d56573d5-8b52-3112-94b8-467bc9969a5b | -12.20996 | -57.12464 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 660c13a8-759c-3e1a-a869-493e3d5ad0c6 | -5.70825 | -53.49279 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 319d632f-66cb-3384-aa85-fb0f617b51e3 | -12.21919 | -57.08636 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| b0abca78-3eb0-37f0-a487-3cf87cf67314 | -6.22761 | -52.78924 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7579217-5916-342e-b743-3f5361854157 | -5.87589 | -53.5211 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b9f5ee5f-767e-3b92-8c63-46a2e63ce6d9 | -6.37757 | -56.23261 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7790d815-8b52-32f8-beb2-c4f18e04d552 | -13.15995 | -54.35292 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a283c8ca-fffa-38c2-bde0-a77c177dcc68 | -5.25197 | -60.33319 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4f9c9eb-aa92-363e-b566-4a0089851313 | -6.16845 | -52.85629 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e6cf90c-cd26-332d-87c6-5883fb4b3b59 | -6.12117 | -55.70015 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec6bdcf7-061e-3dde-bee2-61a9ab83eaa9 | -12.83827 | -62.16968 | 2026-10-09 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffea72d5-ad64-3cf8-8962-0c5d011f9661 | -5.7029 | -53.48847 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52cf7e60-cd63-3a8e-828b-0a43eb5879b2 | -11.75286 | -61.07352 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7737b2d6-4e14-3efb-b510-c3bc281a8b86 | -5.25477 | -60.33734 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dcdcbd8-2c35-3267-ad9c-637977612aed | -12.23252 | -57.09725 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 82c459ae-a760-3143-a76b-76daeb301963 | -5.96515 | -55.34304 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e56373cc-ada6-3905-b820-36687d5d3a13 | -5.70697 | -53.47233 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ef6827e8-8fd3-3c3b-bacb-3d13eee7b001 | -14.97303 | -47.5515 | 2026-10-09 05:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa6f1a98-e986-34c1-a197-422124cf0060 | -6.02757 | -55.35739 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0206a1d1-e792-3a27-884f-ffa0668f8268 | -5.30877 | -60.08576 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f73c3082-1ae8-3462-98a1-6b0192bd8579 | -11.7579 | -61.06344 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9359e61c-849b-3372-8236-9732eb7ec994 | -10.85672 | -59.11243 | 2026-10-09 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 616b9f81-c391-31c9-9bdb-72883e641a12 | -5.93029 | -51.82895 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b035a34-fea7-3964-bce8-830a1da3e697 | -6.22345 | -60.03556 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d778425a-0749-3e8c-9bc1-f00f429df473 | -6.38989 | -55.26284 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d9e1abd-a36b-34fb-8b23-39e1371de9ea | -5.70468 | -53.48808 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c369888d-5d6e-30ce-9b64-4a8e92c095aa | -5.7039 | -53.46418 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d8372d5-147f-3ea8-bc43-7a3d36a19c66 | -7.03151 | -55.68291 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bb36b2b-36c9-37a8-ac34-cd153d63703a | -5.70862 | -53.46093 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cb1f71d-0139-300a-a71f-43119ec4cb2f | -12.22409 | -57.07822 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39e8affa-1f9e-3849-8c2e-1fca7bab081b | -6.28099 | -55.26709 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 288de7da-85ed-354d-bac9-7480f6cb4f5c | -6.44685 | -52.70526 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a87679f-228e-3592-9d9b-7d7355285d38 | -5.30542 | -60.08523 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9556aea2-0043-380a-89dd-4ca7f8d5b02e | -6.44551 | -55.04823 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a35a071-b51a-3ea7-b87b-5eedaab26e52 | -6.25727 | -52.86332 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4f05b99-c4bb-30f6-ba4f-2e36721d1209 | -5.99457 | -55.37477 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0f72d1c6-35ba-3274-ac1a-1e1eb875d3e7 | -11.97986 | -57.61747 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17e60169-3a78-3322-bfd1-58cf443bee2d | -6.49345 | -55.29489 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7421e7df-0cd2-3d89-acb3-3a11b059d32d | -11.754 | -61.06643 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1b3ae792-7357-3856-bb4c-9c09a84d9afa | -4.94078 | -56.86799 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbc5022c-0962-3935-b22b-d17e50f501e8 | -4.07973 | -59.83973 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d23e5404-a06d-3166-8a02-da21c56c8a43 | -12.12538 | -57.1658 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85cc4a11-4a4b-3511-925d-37aa725ca835 | -12.2057 | -57.12844 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 055ef6af-8456-30dd-83ef-a152a4f68dcf | -6.12053 | -55.70441 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0af037ab-6fcc-37f2-93ae-e6c60f4af3ac | -5.68929 | -53.49417 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e7631e4-31ff-381c-967f-724750bd9acd | -12.21599 | -57.1344 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b73ed11-ee3e-3665-a4ab-368866157105 | -4.92675 | -55.86166 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 775ac59e-762e-3b54-81b4-c624a53aeb42 | -6.22465 | -55.65881 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 497c8664-7d3d-3f2d-87c6-8259019a1448 | -6.45313 | -55.04926 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6342cc34-e859-3bff-a860-4020c6d681bc | -6.10239 | -55.69926 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 745ccdcb-6942-372c-a801-9fa2d7ddfbae | -5.70821 | -53.45376 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 567350e1-f57f-30b6-969d-dfb8ecc6198f | -7.51227 | -47.33519 | 2026-10-09 05:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 91a471a6-8d69-31f2-bcea-e5b7eab9bac7 | -15.11469 | -48.52887 | 2026-10-09 05:25:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dc5bb82-0a96-39d8-9ad3-150c74ea5245 | -4.66337 | -56.21286 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22ceded3-af02-3510-ab32-d126fa6129ef | -6.46984 | -55.47413 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e478203-63e1-36bb-bf92-a559c8d0a0b4 | -10.85561 | -59.11958 | 2026-10-09 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19549e6c-0c66-3a24-be47-cb49cc4f0d88 | -7.53086 | -45.87892 | 2026-10-09 05:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a3b40518-ba19-35eb-9512-3cf252c986a8 | -4.30109 | -60.94979 | 2026-10-09 05:25:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb67fd5e-977b-315f-9bba-68e18e7aa1e7 | -13.17629 | -54.36396 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8cc1d4cf-c03f-35fa-8c00-2764b597ace7 | -5.9658 | -55.33869 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87cab647-c703-3e83-8cfd-6432a9ad9309 | -5.69582 | -53.47918 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 910b6c29-2df0-38a8-8821-91fd421d7c23 | -6.47876 | -53.68315 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4003ed15-6baf-339e-aed9-8c69dcb8a660 | -6.12756 | -55.6814 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a3f8cf2-d39d-3f92-a0a8-e0f750071818 | -4.22561 | -59.54525 | 2026-10-09 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9ea38c71-2a71-3d55-8a0c-5d3b1913062d | -6.4897 | -55.29433 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5956e29e-4f47-3054-b508-b077435f1776 | -5.95172 | -55.34269 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d08936df-197b-37a1-89f2-885db74fc3db | -6.38854 | -55.27168 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ecc5b7af-9325-3245-b3b8-2db8c237c27e | -6.57518 | -53.02499 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b76448f0-08c3-3dc4-83eb-4d67bfb05954 | -5.69806 | -53.47512 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2cfeac20-9af0-38f6-a686-8d87e50d6344 | -12.23629 | -57.07119 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e850a5a-f9ca-30b1-9378-c70d4bba52ca | -5.98647 | -55.3782 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44482353-53f5-3956-bf10-23abec262862 | -4.74239 | -55.67196 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README218.md)
