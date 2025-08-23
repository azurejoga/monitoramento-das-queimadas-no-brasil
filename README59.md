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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0494bd1-c0ac-3483-b8dd-1002f2859ea2 | -6.53884 | -55.30781 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35bbe4c2-4bc5-348f-9757-ce0aa6525550 | -7.61325 | -46.26947 | 2025-08-23 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a9865d1-e1c0-3e1d-acc4-9a64c99f56ae | -5.75245 | -57.59643 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a39e242e-9a44-32aa-b43c-bf7bd93fe679 | -6.28437 | -52.82253 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ef25208c-fddb-3bce-9960-2052ba098cef | -6.56085 | -60.06046 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0651d019-3169-3e64-a012-b0eaf78f73a6 | -6.28375 | -52.82664 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f898a91-4533-367b-9dce-a5062bd91037 | -5.87579 | -57.75335 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2eb43787-a8a2-3687-8ddb-7fc654a82b78 | -6.43726 | -53.3849 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e36efac9-4649-3cf3-8c7b-1cc0c154e22c | -6.57578 | -59.88032 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04ec45c4-9135-34df-8221-692471145558 | -6.68943 | -58.8634 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19fe84cb-65fd-3ef5-b813-86422ad035cb | -5.99446 | -53.29646 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b48e67a-9861-305b-83b4-2481e71203fe | -5.24009 | -60.30502 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a92d976-43e6-3677-b59a-df193eeddfc0 | -6.56816 | -60.05796 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54444f84-c82b-32c1-a1d4-0aa59a4f56ca | -6.25542 | -53.67114 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b6d2896-aa25-3779-9b38-2c35a39a3788 | -6.25787 | -53.68245 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77cf4ab8-c028-3d29-8db4-45b7132f5a91 | -6.46168 | -53.39236 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 897554bd-5dfb-357e-b74b-8b44395a8664 | -7.63211 | -45.23782 | 2025-08-23 05:18:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a1df33d-e700-3c93-b6c2-db40b544f66e | -5.7985 | -59.21333 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 502832a3-03b5-325a-a6c9-04288a4c8fc1 | -6.63182 | -58.41249 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b92ef8c6-e8b4-38a9-9721-deb9b04d25d8 | -6.57076 | -59.86864 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77016274-a627-3f8a-88b1-51d55d457714 | -5.02961 | -56.12459 | 2025-08-23 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45c5f43a-4234-361c-819f-2b3755ddcd43 | -7.43665 | -45.41618 | 2025-08-23 05:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ed26f2b-be8e-319f-92a0-45a3d49371e1 | -6.64599 | -58.82061 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e29440f-e6b2-3b51-b166-a5036b7422f3 | -5.7502 | -57.58882 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 7d5b5c3f-083b-3616-beb8-a0be92de8ea0 | -4.12342 | -60.77472 | 2025-08-23 05:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 937cbfe3-1c84-3a48-b312-8154cfcd442f | -5.99808 | -53.30085 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99cbfae1-2f16-3cec-a6f7-e1dbdbe733ac | -5.80183 | -59.21386 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad81720a-4e30-3765-92c8-d31691be8586 | -7.87032 | -46.28925 | 2025-08-23 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8b0eff8-20a4-3dd5-b1a2-142dd4cdf34e | -6.63431 | -60.02075 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 179e2b24-4587-36d4-98e9-e63d92bc6f7b | -7.64691 | -46.28535 | 2025-08-23 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0dec926-12f4-3b34-ae03-be533c96b32e | -5.80461 | -59.21787 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d83b0ecb-3c2f-3f90-9053-0fd9995bdbbd | -5.87913 | -57.75388 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b4b7787-fccd-3066-86ec-9312a837d42b | -5.79461 | -59.2163 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 273b2b39-3174-3bf0-acd6-a4e52239db56 | -3.13128 | -58.0404 | 2025-08-23 05:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62951532-3e1c-3ae2-b648-4afdb738503c | -5.88139 | -57.76146 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79dcd99d-0779-3903-a039-410f457dd266 | -5.753 | -57.59289 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 432d6857-52a1-3882-8837-9bb9ce7f2d5f | -6.36896 | -45.56289 | 2025-08-23 05:18:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de0b5508-b60c-376b-9d04-1687575e71b1 | -7.62957 | -45.23575 | 2025-08-23 05:18:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b684fd3e-e811-323f-a3e1-15a40c0ac011 | -5.79517 | -59.21281 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6566f05a-7a18-3c76-b457-6fde2702ebd2 | -6.79337 | -45.00023 | 2025-08-23 05:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7ecf558d-82db-3684-aa82-28969ffba87f | -6.68333 | -58.85888 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 206b669a-39b8-35e8-ba45-1d92c32f102f | -6.63214 | -58.54092 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffe2a918-c912-3cfa-ab71-3c2e0fa6b3e0 | -5.44298 | -60.17148 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2e35260-d8a6-351c-884c-924727a008d2 | -4.23277 | -54.92694 | 2025-08-23 05:18:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57647694-8c5c-31ea-b802-9017466a9d4b | -5.45383 | -60.14713 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 134841de-df96-3627-87ec-66125be128e7 | -6.27444 | -53.7102 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2aab6be4-62ac-35cb-b4de-77f439885831 | -6.45752 | -53.39175 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59ae86ea-fcd1-3e79-8a4c-7de7faf7898a | -5.89204 | -53.63679 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92a7b711-7cd3-36ed-b745-29023c3437ce | -6.47465 | -55.87971 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47d5a726-5130-3ba7-b2ed-43fed3bce560 | -5.03065 | -56.12389 | 2025-08-23 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba15bd0b-f31d-3f74-9bce-6995703633de | -5.8774 | -53.62354 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bba1cc3-b3d8-32eb-bf90-4fd665dbd961 | -6.18302 | -45.43494 | 2025-08-23 05:18:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 26179293-027b-3f4a-8f09-30cb3d4b0689 | -7.17878 | -48.4223 | 2025-08-23 05:18:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3256cc4-144a-3a49-a4e6-e36845a74465 | -7.39258 | -48.18344 | 2025-08-23 05:18:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9f3c27c-9479-39f5-8520-2630702a1674 | -4.36393 | -54.89075 | 2025-08-23 05:18:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84339c5b-9589-33a3-b2c9-51b9868b8db5 | -3.66252 | -54.75547 | 2025-08-23 05:18:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1814f64-ed14-3f05-97d9-02254d9186fa | -6.75877 | -56.85057 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a4d261c-546d-3d18-bdf1-788422b3a9ac | -6.14618 | -57.71523 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63d9b36b-e843-3611-9c89-008ef1ee86c8 | -6.62494 | -58.54335 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 726fb495-4cc3-32ba-9754-270a68e4d6e2 | -6.37138 | -45.55003 | 2025-08-23 05:18:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6797b4d-0a17-3013-8ef8-2625048b505e | -5.74964 | -57.59237 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 6cee4f2e-6512-3e3b-87fa-6d43d9199de5 | -5.43735 | -60.16311 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b77e9536-1883-3593-9ef0-83772a45b8f2 | -6.67329 | -58.81461 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3692ff5d-7238-3049-b4ab-b67711ba6e85 | -5.74182 | -57.5984 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b44a77d8-db0d-304b-87a8-579264381c78 | -5.81127 | -59.21893 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24feb356-e757-3169-bbe0-6eac6ac5675a | -5.4424 | -60.17511 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cb930af-3eb8-3aa8-96cd-3c4246c0256a | -6.58361 | -59.87432 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e136218-a784-3d66-8ff1-bf0788198fb2 | -5.88023 | -57.74682 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f66a4037-34a3-3d91-9f18-43e9f5a81f81 | -5.74238 | -57.59486 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9473a7e5-96b5-3ab8-988c-c3ca173e3f85 | -6.2817 | -52.82036 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f23dcf61-2fe9-37a5-9e71-e382e7408371 | -7.42956 | -45.41515 | 2025-08-23 05:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5030469d-4d26-3de0-81f0-0946c168c7a4 | -5.80128 | -59.21734 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2e4b1f5-bfdd-3167-9c38-03c30a9f8f9e | -5.79406 | -59.21978 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1610c58c-ece5-3228-a2e1-9d9647e09954 | -5.80516 | -59.21439 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 059affb6-bc0a-36fe-ac98-7acf957c9ba9 | -6.47405 | -55.88376 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b36e5c19-6ba3-394a-8703-c7113ba04487 | -5.88041 | -53.63126 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0477d3c-c0bc-341b-b9a8-e2bcf01e885a | -4.55749 | -55.96404 | 2025-08-23 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3746b7f7-8ca4-3f9f-8a53-abbcc8c9d341 | -7.86955 | -46.29527 | 2025-08-23 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af9da3a9-7d7d-3a93-a80a-afd3e695a9ef | -5.74684 | -57.58829 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| a97d77ee-ff7a-3bd8-aad6-d9773f75b204 | -3.1346 | -58.04092 | 2025-08-23 05:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 063031cb-9f2b-3d9f-9593-f0b540e43c29 | -6.622 | -60.01148 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a0dcdaf-e9cc-3847-b67c-f1e90e0eb65d | -6.18724 | -55.46267 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 925bc595-f828-32c9-938c-b0ad1ece9ee1 | -6.27514 | -52.8253 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fea050c-7500-393d-a1a7-1e788e4935d5 | -5.89151 | -53.64035 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 896a33fd-06fc-34f6-a015-e71d18929b59 | -5.23745 | -56.06361 | 2025-08-23 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8e2c67a-323c-31b2-9238-f5f6b1bbd605 | -5.81016 | -59.2259 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40bc4564-5826-3027-a81c-c0e26411dda3 | -6.18393 | -45.42816 | 2025-08-23 05:18:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f9c0d5a6-8943-3523-80fb-c6e7762fdf54 | -5.44016 | -60.16729 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76cbc58e-0804-3517-bac0-d6dd71e94699 | -3.04438 | -59.1633 | 2025-08-23 05:18:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52938dc5-3f72-37e2-bbc8-3be053b459d1 | -5.7474 | -57.58475 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 8eb83a4f-115f-3f3a-88d5-7dad3ef97af7 | -6.60388 | -57.64368 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47bb8fc1-6a21-36e6-81e6-71f38fda1a25 | -5.75075 | -57.58528 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 78cd527e-68e8-315f-936d-9c754f337264 | -5.73957 | -57.59078 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9af5dbdc-41ca-31b2-8da7-9708c46b5b3f | -5.88199 | -53.62057 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb09d5ab-13cd-34fb-95de-bf792842e0be | -6.36953 | -45.56337 | 2025-08-23 05:18:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 155dd320-ee4c-3bb9-9a8f-0c19ea809938 | -4.83278 | -55.7678 | 2025-08-23 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a79fa68-cf74-30da-9829-f95152060477 | -6.30908 | -59.89223 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0500eb86-b843-30ff-be6d-24817dd0ab7a | -5.14367 | -62.53151 | 2025-08-23 05:18:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f178c019-9a82-3e13-9ba5-d602d1d0237a | -7.39799 | -48.18874 | 2025-08-23 05:18:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f309d3d0-b8da-33ae-9623-5c87b7ae9200 | -7.64647 | -45.23999 | 2025-08-23 05:18:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README60.md)
