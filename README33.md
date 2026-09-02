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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ea8e3a1-0ce3-3129-9e82-1d7d5f4b1366 | -6.73875 | -56.34276 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c1a9334-9bb7-3ca1-8c3d-593b21634cd9 | -7.34891 | -60.58608 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48311be0-d9e9-3ecf-a766-21fc5066e259 | -11.66326 | -50.19313 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17015577-fd1a-36f8-8f50-d4cc6b94b1a3 | -13.40864 | -43.87529 | 2026-09-02 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c0e2ae3-39aa-32d8-90f1-d748041c77c4 | -9.46469 | -50.31499 | 2026-09-02 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fdaff33-8cbd-3eeb-83bf-11e805d7fd92 | -7.76942 | -61.19574 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e499dd7-8445-3921-9e1b-80fab92eeb56 | -7.21407 | -60.67437 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3674f459-e9ac-374e-8ab8-9111f86684f9 | -11.68319 | -50.50319 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 947b3ba1-e619-3276-a227-1f6cf8a48b16 | -14.11667 | -45.5017 | 2026-09-02 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9789154d-579e-3e45-9c5c-6d8b1a80f92b | -9.39452 | -60.56375 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfe889d0-eb4c-3da6-ab6a-c788d4f6a0aa | -10.06094 | -59.40099 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb29d147-1bac-3988-83b1-4ce1e58b13bb | -8.44739 | -54.6957 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8798318-b1ef-3207-a42d-1f1c212e1491 | -7.97652 | -52.08886 | 2026-09-02 04:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2696d26d-35c5-3397-bb8d-db052dfed39d | -7.15426 | -46.84494 | 2026-09-02 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16727a6d-614b-332a-8715-9851cce19c1d | -10.78706 | -44.74691 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fa698e1-60fb-373d-84ba-db326ab5a759 | -6.73468 | -56.34208 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a847605e-d35d-3596-90eb-2a00ebbf7bb6 | -12.08571 | -47.11068 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35ab36ce-6603-3603-9c0d-6c1bd92b71f1 | -6.2541 | -55.42605 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c458793d-f7ee-331f-bbc7-3f0851187002 | -6.95246 | -56.45315 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a051c01e-2f0f-384b-a798-ac9b713cd5c6 | -7.34475 | -60.57845 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67c6807a-b29d-3623-9343-7f80738da85b | -9.87768 | -64.98151 | 2026-09-02 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 400a3d83-86ec-351a-93d5-0f735a4d8ffe | -8.45028 | -54.70058 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17927cb2-2bbb-32b3-abe5-bac8a6fd409a | -8.21669 | -61.47837 | 2026-09-02 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0dbbf8e-7d88-395d-8062-82db0f8b2e76 | -11.90904 | -45.04693 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18c1bb7e-083c-3107-8177-4ffc262fcfcf | -7.6657 | -45.87179 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4078ab65-1837-3381-a2f9-f72827632cc8 | -9.55513 | -48.38623 | 2026-09-02 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b50d18e1-7f81-3f1a-9674-5d0d480520a7 | -11.32782 | -50.5955 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96debaec-35fd-390b-ad08-bbdb0b452ca5 | -6.75529 | -59.43904 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eba009fa-e280-33ae-b902-28d45db7dfe0 | -5.58568 | -60.19926 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 378d4d2d-5352-3f9c-82ac-dcc246962de8 | -8.28399 | -54.91493 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb148f97-e079-32a8-a6f2-f9c866c0693b | -11.34691 | -45.41135 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7b4baf4-e127-3601-a637-ab9438079591 | -11.29356 | -45.15767 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d14247e-e988-30ee-9cbc-518d6e1140b9 | -9.87559 | -64.98125 | 2026-09-02 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d0e217c-e91a-37e5-89cc-11974768fb8f | -11.33746 | -50.62357 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbf515b7-a21d-3234-8265-01878dff1abb | -11.30923 | -45.17212 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b7f392b-784a-3a63-8531-79ff31f7e699 | -10.37711 | -49.98427 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fcb664e-f722-377d-9605-6f1eede09f32 | -10.88155 | -45.34558 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d79bb9c0-4bce-3cd8-bb07-591c9354ec0f | -6.94722 | -56.38905 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0c217cd-2acb-3ba9-a683-9399f1100f30 | -6.943 | -56.45918 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9da61d8a-57a6-30e7-80a3-717fd047d8bd | -5.58089 | -60.19494 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73d89332-967f-31de-9cf5-1b8b16496e65 | -11.90835 | -45.05207 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b55f6b13-0de4-37f2-b79b-e60ea24ce392 | -6.15178 | -55.67482 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca2e72f3-ca90-37fd-8a00-b705ca2cf69b | -10.96742 | -50.48202 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 4db318ad-72d6-3cdb-aa79-d9d6718dd41f | -6.6949 | -58.75897 | 2026-09-02 04:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbf9d836-2a9e-3b03-85d6-155158b72d15 | -12.37674 | -48.14336 | 2026-09-02 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55c3499a-f1c3-3805-bde5-0cd2a1459536 | -6.07938 | -57.95818 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e0ee470-14b9-3d2a-abb0-088f6914d75b | -6.26187 | -55.42714 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fd049ecc-b87f-3a2f-9103-e5124d37368b | -9.01782 | -65.45731 | 2026-09-02 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0c4dbd5f-f7e0-3080-9f51-77e6947c5320 | -7.18592 | -55.48349 | 2026-09-02 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a64ba79-27ab-38e0-892a-7a43adad20bf | -11.53252 | -45.48951 | 2026-09-02 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ee3528c-3bbc-3ad9-9dbb-23f349c662f1 | -8.92236 | -62.35744 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db178995-5156-3e8f-b65a-b77af5c8907e | -12.12563 | -47.05188 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f66d278-d031-3c61-928f-b838764c78de | -8.71065 | -52.35893 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25789794-55d2-358c-a195-35f0af06bcd6 | -10.3219 | -49.95239 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efe82963-5a8b-3706-8cf2-30ef7ffde6bf | -8.76047 | -62.58289 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a70dd00-e532-3258-ba53-50761c35173d | -8.76121 | -62.57891 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45304959-2e44-3f2c-996e-075a82580bb8 | -9.46232 | -56.74137 | 2026-09-02 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cda5c866-e946-3e2e-82ff-5b402026a0fd | -10.71728 | -46.22319 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 696b6f55-c494-3ed3-a42f-4668cad333df | -5.32959 | -60.14917 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc04c675-2ea2-33ae-84d1-8d9878dd46f4 | -10.4952 | -59.60358 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fee787de-46c0-3b8d-bd65-2b00827684bf | -7.73148 | -60.97298 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44a82dc0-b81e-34a4-a586-46b0dbd0af00 | -11.03585 | -49.66717 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e62f7ef-a0ed-3816-9819-f90336b2b4ec | -11.29201 | -45.15964 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d8455c0-3ce9-3ec3-9e9f-bee5d674856e | -6.95183 | -56.45681 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0184d7a-5456-38c7-8d8f-2d31646a84a0 | -10.78164 | -44.75125 | 2026-09-02 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3551d4c8-55f9-3f22-ac5f-9c1a490ca8c1 | -8.61991 | -54.8487 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89b16d5c-9f34-390c-8848-be7849f2d5dc | -7.19777 | -60.6719 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cfc3ecf-b552-390f-a0c1-81f89c62a43b | -11.35178 | -45.41045 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cfc18ee-9b96-3462-b9c0-77fb998af115 | -8.43017 | -54.70748 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| cf823837-0492-3898-85d7-c7ebb9edcd21 | -11.33691 | -50.58173 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24b1040d-a4dc-389e-8f9c-c4005251dd65 | -10.70764 | -46.1979 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ead1cfc4-187f-35ba-af22-86c42e49b4b1 | -12.14312 | -47.13781 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1a90a51b-3aa5-3a5d-811b-0c1856652df2 | -8.43081 | -54.70591 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e9b4f231-1b3e-3db5-97c4-e31c9910e97a | -6.93258 | -59.64312 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd42c98c-81e4-3e2d-bb9b-f80636a216a1 | -6.05248 | -53.83872 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8ca1b17-df50-3b49-b8ff-f0e8f57e5cd9 | -9.70191 | -47.20746 | 2026-09-02 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4e4841f-6f04-32f3-90c9-b6ece62020be | -12.08784 | -47.09576 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b558c18d-7cb8-3ca5-97dd-379fe0ace250 | -8.77012 | -62.58135 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97f6bb37-5d67-3d54-9f2f-5978cd35cf9b | -7.76808 | -61.20304 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2d7ba84-d6df-3eed-b08d-241918adeee8 | -8.93757 | -62.36336 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89545f1b-0769-3ec3-8fd3-d23f4cd1e216 | -8.46986 | -54.71677 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 31799e03-9396-3660-88b6-05fad18aaa65 | -11.30778 | -45.14742 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4a87cca7-2bda-3f92-9dc6-c27bb2e8b59c | -9.45172 | -50.30526 | 2026-09-02 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f54153d0-0280-3cca-8cd8-9e3f8707fb99 | -10.7089 | -46.19939 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88f5e14c-10c8-3e02-b29d-0bbce700a475 | -10.78027 | -44.76127 | 2026-09-02 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 0f607188-0477-3b0f-8291-82eadf0026fb | -7.64787 | -45.87709 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8afb883d-2c43-3cf1-a825-5f00c792e258 | -10.87169 | -50.47092 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4740fb46-df52-38e8-aad8-4240cf1ef866 | -8.43171 | -46.89503 | 2026-09-02 04:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4717195f-56df-3866-a938-17ce604758d1 | -12.08966 | -47.10006 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 385da13b-eae0-326e-ad97-d95f158e62bd | -7.20737 | -60.68052 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bf6526b-eb56-305e-9bdf-13dafbb78f7d | -11.83086 | -46.0565 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b1db453-3ec7-3ef7-bdcd-023408352eaa | -7.29143 | -49.81541 | 2026-09-02 04:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0eada32-3ed9-3829-bbe4-41543c4ff431 | -9.70221 | -47.19865 | 2026-09-02 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6fc48b2-acc8-3d70-be6b-a562c6b260e3 | -10.50272 | -59.61597 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70039dd1-63f1-38c7-b7fb-3b704a371eec | -9.47439 | -57.03389 | 2026-09-02 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d83edc7-9c8b-339e-82da-6d4adbc87638 | -7.65151 | -45.8815 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e85c9b2-4d27-3552-a7d1-b0e13a0863e8 | -6.15726 | -57.77679 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9757ce8-531e-3294-b4e3-666ccfb446e8 | -11.05498 | -51.52662 | 2026-09-02 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7eafe7a5-60d2-3ea5-8013-910502251645 | -10.44061 | -46.73561 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b250449f-61d3-34d4-921e-ec17b9e8c7e9 | -10.74301 | -54.03358 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README34.md)
