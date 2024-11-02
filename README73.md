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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00bfe9b4-1748-3562-8385-185aa69c8a97 | -1.81689 | -52.41654 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b56106af-82a1-31ce-8fdd-b76010c89138 | -1.7755 | -52.33969 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2beae5e-5502-33a2-aef6-4dc297bf08f7 | -1.76094 | -52.36491 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0e5728b-f3fb-3bc5-a4d7-33f44b61c1ac | -1.75688 | -52.36821 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d071c1ef-7244-3e4d-a1c2-999cad20e15a | -1.75517 | -52.35618 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d01faf6e-81ef-3838-8d9a-3198c0ef37fe | -1.64441 | -52.25345 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c98e9a6-d0d2-3bba-99b9-94ebc616a420 | -1.64382 | -52.25731 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 194e0849-3fc5-3e98-a967-702f7a07a541 | -1.63685 | -52.25624 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b1408b8-9f13-3f92-863a-7bcdb9b238bc | -1.63336 | -52.2557 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ede6ecb-1e46-3d35-982f-7c92a1a1e4a1 | -1.63268 | -52.24868 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f259a80d-8050-36a4-a847-b488e0e75228 | -1.61224 | -52.37895 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a4d1b8a-e8a0-3d83-97c8-e77fed228e4f | -1.61121 | -52.3779 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5be6a91-6b96-35e3-976d-31f3c8598889 | -1.60877 | -52.37841 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b6f50eb-fc45-31fe-a1e9-a56c29458d2d | -1.60243 | -52.37354 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b29531cc-906f-3e65-85c9-4e13552757c8 | -1.5646 | -52.27367 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93b4690a-040b-3101-8af4-42012fbbec8d | -1.56401 | -52.27751 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ace7fdb4-4ef1-313d-a6b5-9f612844aa13 | -1.56342 | -52.28135 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60ae996a-778c-37f4-b076-6e7014fb64b0 | -1.56112 | -52.27314 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84232e19-2b70-3a44-8f85-5402622259e1 | -1.47377 | -52.34212 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 891cb364-caae-3536-a5a8-3f867969d8cc | -1.47259 | -52.34974 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2ba05d4-eed8-313f-bd73-a148d235b957 | -1.4703 | -52.34158 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d915ab24-cb1c-309e-ac56-b7e8cde32c09 | -1.46971 | -52.3454 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abec8c8c-b66f-3c2f-b136-4d0ac32a2b90 | -1.46649 | -52.27446 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d45f4fa3-68ff-3924-b0c8-e03de2095ef4 | -1.46219 | -52.34814 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 999b79ce-95f0-3271-8779-e35fd23782a7 | -1.454 | -52.37806 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92bf58a4-465c-37dc-bc42-94fae80e8b3e | -1.45113 | -52.37373 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6c86e8f-4b6c-3cf6-8a58-6bf821115d50 | -1.41542 | -52.32922 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba91af4a-b113-3f68-beed-9f6ff4ed6e21 | -1.41483 | -52.33304 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd977059-cdf6-304f-98a6-0d2707cef5ae | -1.41262 | -52.25438 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1986c945-531c-3524-bd9b-323982b157c6 | -1.4105 | -52.25513 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be96f457-cfad-3421-a292-c837e20d5fb5 | -1.4085 | -52.30472 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9bd4cfc-7131-32cb-acb2-475e326a3485 | -1.40616 | -52.3054 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdcbf505-5b0c-38e5-88c3-5966491f7b83 | -1.40503 | -52.3042 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edd4d9c2-7751-3387-b207-060fb0c1d434 | -1.38664 | -52.27111 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a0e0e53-4eac-30c3-a471-0baddf0267c6 | -1.38316 | -52.27057 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeaf7663-5bbc-3592-b682-8e5475b48f91 | -2.08927 | -53.23759 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeb86cab-63ba-34f0-926d-ae8b97b6e0a4 | -2.0859 | -53.23705 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3630453c-2f16-3f37-979d-5c52097dfd14 | -2.05103 | -53.23901 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6247438d-5b55-31f0-bd21-c9801b5e9700 | -2.04544 | -53.25289 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 948e0454-1ce5-37bf-96f3-6b187861c267 | -2.04428 | -53.23796 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44df5bac-fd1f-3117-82c2-aa2ad5e04f2a | -2.04206 | -53.25237 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc0475fc-2cbb-306b-a263-583aa1559b82 | -2.04151 | -53.25597 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e571db76-822b-3566-be87-c30251336ef4 | -2.0409 | -53.23745 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9bdb6dd-6106-3c87-ad76-f899fc10a9e2 | -2.03753 | -53.23693 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe2676a5-175b-3b7a-ab2f-84df31180088 | -2.03697 | -53.24053 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2391888b-e864-3cf3-89e8-22f561e7df06 | -2.01802 | -53.29649 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d49140d1-bfe8-310f-ab13-72a31516eed9 | -2.01239 | -53.29893 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c3ce7b9-0502-3763-aba4-f3803006acd5 | -2.00619 | -53.2281 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9016a38-6be4-31ee-975b-a62a25e964f2 | -1.99882 | -53.11973 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff77782a-92b6-3e7e-873f-1118ebc282ee | -1.9311 | -52.67287 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2b9cce5-5abf-353b-9d09-66d09eb1dc85 | -1.93053 | -52.67658 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c8e08587-6fed-3ec1-8fb5-3466f54af03a | -1.91104 | -52.93879 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f87791c7-dbcc-3b00-997d-f10951d26ac3 | -1.80023 | -53.04172 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b95dc14-4b3d-3381-be63-ae42781a924a | -1.79684 | -53.0412 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe28b08d-5080-3364-8987-1dce1e66b760 | -1.71215 | -52.68198 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11b63388-8d7d-3968-affe-9cccf42927b6 | -1.70756 | -52.71173 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0676b8ab-c342-3418-a938-7df24b5ef6c8 | -1.70534 | -52.49656 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb28d9b3-36bf-3b29-8d0e-08ebc5eca2ee | -1.69843 | -52.70272 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1b11d43-1a72-32b8-b68c-57612202f6d8 | -1.66257 | -52.79955 | 2024-11-02 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65b8e842-bcc7-396d-bb56-fd8511daaaa2 | -1.59374 | -53.14734 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ca66e049-5a69-3a22-b6e9-5fcf2b8efdeb | -1.57462 | -53.11486 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df33621b-8da8-3a0b-bf76-9a19eeb7004c | -1.51559 | -53.13906 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20e2be6f-690c-3f08-a1d7-3ef4059a80d2 | -1.51552 | -52.56898 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d19dfbe-d21e-32d2-9348-609a1ac60148 | -1.51503 | -53.14265 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f094947-6152-300a-8a23-f06a233e6a45 | -1.51222 | -53.13851 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f69862bc-79d8-3534-bceb-640cd0a1cae5 | -1.51166 | -53.14212 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1e81f35-52bb-35f9-9400-a894b45f1428 | -1.50885 | -53.13799 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 612c26e9-1450-3860-a5f6-55c36e09701f | -1.44828 | -52.86922 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8fa1fd6-75b4-36ae-879c-c8ac0b1b0fd4 | -1.34873 | -52.53659 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 61946232-03e5-3dba-a077-4f83cc854433 | -1.34529 | -52.53607 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c066e2fb-2349-3dab-9c69-adaa265d4cc4 | -1.34244 | -52.5318 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86f0b526-13fa-39e4-b9fe-3e3ffd40652e | -1.32846 | -52.80555 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7100269f-0206-35bc-b1aa-9caaa746cc85 | -1.32754 | -52.80608 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 984f6612-10bf-305a-a7fd-88c896e4cfdb | -1.32414 | -52.80558 | 2024-11-02 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13c6c4f3-e03e-35c1-a3a8-2e3cc7008b1f | -3.30009 | -53.37265 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41a0e938-4dd5-3ecc-a3c8-1cee0475aa01 | -3.27463 | -53.33526 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6ecda89-f7c0-3c39-88ec-51c17789bf91 | -3.27187 | -53.42033 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a8c83746-8bca-3d64-9be1-5f1c37353bac | -3.27131 | -53.42395 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4de0b241-4105-3f9c-814d-b95bdef88dec | -3.26961 | -53.41254 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 764de250-33cb-3b69-ad3f-9c60cbe750ef | -3.26905 | -53.41617 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2cd3d962-3b55-305e-94af-f33a35fbe4a9 | -3.26849 | -53.4198 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5b059efe-0534-37c3-bcdf-900892518eb2 | -3.26793 | -53.42343 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b8ae7422-0d89-335c-adad-1623cc95dd60 | -3.26735 | -53.40479 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6acabc07-ea35-3a91-b368-31e1b6d1af94 | -3.26679 | -53.40841 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7efd17a5-e5ae-3d58-a67b-cbfcbd90a3af | -3.26623 | -53.41201 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 91cccb82-4efb-362d-beec-0c01ee81ddb2 | -3.26567 | -53.41564 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 929c6515-61b5-3139-9fa4-c8c8337e2517 | -3.26511 | -53.41927 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 122fc71d-1ea1-3e2f-af97-9bb3291ad540 | -3.26455 | -53.4229 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 69d7bac1-ffb3-3f12-b1bf-7e3d432c85f6 | -3.26396 | -53.40427 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c155fe9-1c88-3681-bea7-a801b1f566dc | -3.2634 | -53.40788 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8c53ac8-1f17-3eae-859e-93dd04720223 | -3.26285 | -53.41149 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 46c25806-2950-3ae1-9b3b-56e9347547fe | -3.26228 | -53.41511 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dc17915e-5208-3c57-a88f-df7bad048eb2 | -3.26172 | -53.41874 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dfcf19d3-3f23-3c98-acbf-e0b370341af1 | -3.26164 | -53.35191 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 61848097-6f6d-3776-896f-4676a8148b29 | -3.26116 | -53.42237 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 24610c6c-fe12-3825-a8e6-d4d1614dbf6b | -3.26108 | -53.35553 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 841153e0-dc52-377a-8707-4ebdcdda601d | -3.26057 | -53.40376 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 164dd2f7-e21d-3cf0-8cd7-fe0f6b5bf356 | -3.26002 | -53.40737 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e70a4528-25ed-39f7-a776-efe6a1c92d28 | -3.25946 | -53.41098 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 047429e6-43cc-3499-9d1f-b3b6840e5401 | -3.2589 | -53.41459 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README74.md)
