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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8728073f-a2f4-3920-8979-3b0483ebf7f3 | -8.1874 | -54.742 | 2026-09-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| a034aa1f-09be-313c-bbc2-121e9ece4460 | -2.4636 | -49.2089 | 2026-09-20 00:10:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 04187444-3811-345a-99c2-58bab8eef80d | -3.3492 | -59.867 | 2026-09-20 00:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 40b47d71-e8d6-3e5b-b637-c0dce8fbd71d | -11.0259 | -48.2944 | 2026-09-20 00:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 5edbc131-9ae2-3da7-8c6d-0164ec3b0c77 | -6.9498 | -62.9166 | 2026-09-20 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f39c63d3-4120-3c37-a5f0-045fe6ba8b03 | -11.041 | -54.1567 | 2026-09-20 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e6106c05-a207-30fd-9b26-a0e92f575f27 | -8.1872 | -54.7622 | 2026-09-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 3ca9aeda-c827-357b-8e47-1a839eb239e4 | -3.3493 | -59.8479 | 2026-09-20 00:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 29.2 |
| fe0dc0a8-dedf-3c93-bdaa-b48625ee103a | -5.4087 | -44.2644 | 2026-09-20 00:10:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 1a1a415c-1ad8-31b5-b2f5-345ba3d356c4 | -10.2787 | -50.2605 | 2026-09-20 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 06df949e-e3d0-36e0-aa01-f7685d43afd1 | -11.2118 | -54.0797 | 2026-09-20 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| ad14f9f5-87c6-3d26-8f8d-72740d93eb44 | -11.0991 | -54.0285 | 2026-09-20 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 74b91dd6-41ae-3ce2-8058-48d1aa632529 | -11.1369 | -54.0251 | 2026-09-20 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| d1c1c033-cf7d-3a26-b253-e06b9cda6a5a | -9.131 | -45.7273 | 2026-09-20 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 63051959-87b9-3bf7-b392-0e40676499cb | -13.037 | -46.9096 | 2026-09-20 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 4d987a59-1c44-3a5e-b690-39e2fab48c4a | -6.9314 | -62.9172 | 2026-09-20 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e599777e-1c98-3a39-b032-0712e828279a | -6.1466 | -47.5065 | 2026-09-20 00:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ee9a61a0-837f-3083-8b85-b2cc9c7edaf8 | -8.0465 | -61.3427 | 2026-09-20 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 450d7e01-c600-32e0-8db7-5faeab6ed1ff | -10.4231 | -48.0133 | 2026-09-20 00:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 27131ea1-514c-36df-a15f-495a566909a4 | -11.118 | -54.0268 | 2026-09-20 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 6d8759bf-e11f-3f63-ba2f-6cfc2f4ec18a | -11.8739 | -47.657 | 2026-09-20 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| b81a6e4e-3be8-3f0a-8b0c-6560c6fe7fd0 | -2.8791 | -57.799 | 2026-09-20 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 2c1bc842-22c6-3f1f-9e63-4e12b34b1d6b | -2.8791 | -57.8184 | 2026-09-20 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 58f72148-c8b5-35f9-95f5-77719fd2acfa | -12.74 | -46.18 | 2026-09-20 00:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c0f6877-8119-34a5-9dcd-bfa7c9d1beb8 | -5.83 | -47.76 | 2026-09-20 00:15:00 | MSG-03 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ba85d9e-ca6b-3487-8f6b-fa67dcb3c3c6 | -11.379 | -51.42 | 2026-09-20 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 78f058ab-6b97-34af-a0fc-9c49c85677fb | -12.7432 | -46.1601 | 2026-09-20 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 956b52fd-934c-34c1-a172-c682210464a1 | -6.1466 | -47.5065 | 2026-09-20 00:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 8c989ae6-7f73-3fef-8785-d1cb71a6f802 | -7.3259 | -55.6153 | 2026-09-20 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f1a7f52f-ef64-3824-a0a7-c6dae043feb5 | -7.5522 | -45.435 | 2026-09-20 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| f4b35313-00ba-3158-a8c6-c3f71e022e37 | -5.8593 | -53.5399 | 2026-09-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 2d1fa695-6cc8-343f-8ae2-fb8f68af8113 | -5.4087 | -44.2644 | 2026-09-20 00:20:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 18752153-57f3-3e89-9b1a-a30bdd3704c8 | -5.8595 | -53.5196 | 2026-09-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 92720391-ef17-320d-a50a-0329c2d521fa | -6.1832 | -47.5915 | 2026-09-20 00:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 385518d0-574d-3918-a0ce-a381d1a08cea | -8.1686 | -54.7634 | 2026-09-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| b757f67f-9586-36d6-a95e-e6910e8ff007 | -3.6946 | -60.5835 | 2026-09-20 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3eab9783-f72b-37c3-8a44-40d979942a4e | -12.8893 | -51.0124 | 2026-09-20 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| acfdcc69-ff92-3621-87d8-561d59f9d4eb | -12.8896 | -50.991 | 2026-09-20 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 80c02a6c-7bb7-3c5d-b009-8a779aaebdf3 | -11.1369 | -54.0251 | 2026-09-20 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 94c96446-f6df-3b7e-bb2a-f1919481a0c5 | -3.6945 | -60.6215 | 2026-09-20 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b926917e-d33c-320f-81df-ebdeaebb86e8 | -2.8791 | -57.799 | 2026-09-20 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 530de621-b132-31c3-8c32-d99a949d03d0 | -11.8547 | -47.6596 | 2026-09-20 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| ab612160-dd1e-341c-a971-88aaed7a11cb | -7.3073 | -55.6163 | 2026-09-20 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 810afc44-f976-307d-8aad-683370d96e25 | -11.0991 | -54.0285 | 2026-09-20 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 27340da8-74df-38b0-9b2a-cfbd89649e5d | -7.5334 | -45.4367 | 2026-09-20 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| ece92244-3ece-325f-87fa-a8e3938cc64f | -12.7629 | -46.1343 | 2026-09-20 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 0bbf9272-01c9-3352-81f2-a95a8eecdd24 | -11.8739 | -47.657 | 2026-09-20 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 0ce3c209-231c-3fb1-bc32-02410be3e26f | -2.4636 | -49.2089 | 2026-09-20 00:20:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 5c04343c-d262-3cc4-8d2a-b136c566d41e | -3.6946 | -60.6025 | 2026-09-20 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 1802766b-8f56-3ba8-99ce-0986101a8673 | -11.0259 | -48.2944 | 2026-09-20 00:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 174cb836-95a8-374d-95b1-170d64502a75 | -14.6856 | -46.6886 | 2026-09-20 00:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 228b20ff-dfa0-3da3-b190-80d0adfa3877 | -11.3793 | -51.3989 | 2026-09-20 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| ca0aabb9-3af8-3952-9a56-9e7dcedd0fce | -2.8974 | -57.8181 | 2026-09-20 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e15b5385-b4c7-3bff-a1c7-5126ee8d9934 | -8.0465 | -61.3427 | 2026-09-20 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| bd8b0620-910b-3700-8222-ac49b3e51fb1 | -11.118 | -54.0268 | 2026-09-20 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 154.0 |
| f973c4bf-b413-3ce7-8007-60108caab452 | -5.841 | -53.5205 | 2026-09-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 5afe65fb-9adb-3c23-8405-d1d820c7b7c8 | -11.0802 | -54.0302 | 2026-09-20 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4ebd5a10-11f6-3701-b084-b9bd7f5bcc38 | -8.1872 | -54.7622 | 2026-09-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 443da3c6-f0a8-3738-a5f5-14228da4186e | -7.5525 | -45.4123 | 2026-09-20 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| ee5660f4-f817-3b26-9444-680b20c8a909 | -12.7621 | -46.18 | 2026-09-20 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| bef6d0a8-04ea-3d42-b34e-283635f130e7 | -11.2307 | -54.078 | 2026-09-20 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| e037e56b-219a-3835-a3d2-5717062879ba | -11.2118 | -54.0797 | 2026-09-20 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| a77b949b-0aef-32e0-a696-27c2e4cec265 | -12.7625 | -46.1572 | 2026-09-20 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 5c81a33f-0e5d-3f59-856d-87698b625a2a | -13.037 | -46.9096 | 2026-09-20 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 66ef27b1-ff81-3ea4-a472-47152554fd65 | -11.041 | -54.1567 | 2026-09-20 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0dc8ca9e-de33-36bf-ab71-bc2ccc129d86 | -5.8408 | -53.5408 | 2026-09-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 9a0203f0-b375-3100-818f-679c45231377 | -3.3493 | -59.8479 | 2026-09-20 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 7c7f579d-be71-3e8b-8d76-9e8d21f21aec | -3.3492 | -59.867 | 2026-09-20 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| b115219d-2bb4-3161-a7fd-5946d40ff3c1 | -9.131 | -45.7273 | 2026-09-20 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 5f949018-8abe-3baf-b9d1-6870b3fe6996 | -5.4085 | -44.2874 | 2026-09-20 00:20:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 123ee3e1-a3c7-31cb-8b64-a195f4eddac1 | -3.3311 | -59.8101 | 2026-09-20 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| e4dd6c20-e59e-34bb-8bbf-17e201d3f6f5 | -8.1874 | -54.742 | 2026-09-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 5ee9c5f8-1df1-37aa-bfec-57753e8339a4 | -8.1688 | -54.7432 | 2026-09-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1d1a8bd4-c212-3204-b6fd-62015c3771de | -2.4451 | -49.2093 | 2026-09-20 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 50893975-5ef3-3377-b8fa-8a6ccfa4bdd4 | -11.0223 | -54.1379 | 2026-09-20 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 1b12c65f-ed57-3148-b186-3a0afe5b1011 | -12.7428 | -46.183 | 2026-09-20 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 309.1 |
| 45121329-76d7-3573-8114-06b47a02b7b2 | -2.8791 | -57.8184 | 2026-09-20 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| e4bf0924-64b2-3fd8-8d82-fd4549527bf2 | -13.0177 | -46.9125 | 2026-09-20 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 208.0 |
| e4b6617c-42c8-3b4e-9ef4-17bbda07f43c | -9.131 | -45.7273 | 2026-09-20 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 7d59043a-f484-337c-8699-887ff59e35a1 | -14.6856 | -46.6886 | 2026-09-20 00:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| dd45297f-9d36-3099-9cfd-1fbf9ec60f14 | -11.4905 | -47.7736 | 2026-09-20 00:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d6921ba0-ea61-35b3-9568-c8558d8a4202 | -12.7621 | -46.18 | 2026-09-20 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| ee5915e9-b424-3bb7-a5e6-f94800ad4706 | -5.4085 | -44.2874 | 2026-09-20 00:30:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 0576a4f9-25ba-3241-ba15-a07f146380df | -10.3917 | -48.8915 | 2026-09-20 00:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5638e257-48ca-34a2-b03e-e73116168fa9 | -8.1872 | -54.7622 | 2026-09-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 5c43b3ca-5c5a-3536-a54b-a9870df15e9c | -11.041 | -54.1567 | 2026-09-20 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ee8d5507-fe30-375c-aa52-b2dc3866893a | -8.0464 | -61.3618 | 2026-09-20 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| c5881bb6-f8a6-3ed4-8a77-a01cf48ce23d | -11.8739 | -47.657 | 2026-09-20 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| e5a8a1d6-f947-3a52-9e6f-b8c2e3cda11a | -3.6763 | -60.6029 | 2026-09-20 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a460d651-92fb-34de-a528-8ba80a590213 | -12.8893 | -51.0124 | 2026-09-20 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c8d854c2-3cdf-3f99-8afd-7bfb0b839a5e | -8.0465 | -61.3427 | 2026-09-20 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 6c478592-1f8e-3053-a84c-fe4e5adb53f6 | -13.037 | -46.9096 | 2026-09-20 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 088b439f-bd65-3ff2-ab2c-fa8569bf4e42 | -11.2118 | -54.0797 | 2026-09-20 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 0b041929-7817-31b5-8bec-854a66084aa8 | -11.0991 | -54.0285 | 2026-09-20 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 0ccdbf63-a518-336f-9271-6a7e29db9c03 | -7.5525 | -45.4123 | 2026-09-20 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4b35dfa7-f3b2-38f0-aa73-b8215295ce92 | -3.3367 | -57.8673 | 2026-09-20 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6eb4d7f6-1b96-32a5-aaf0-62f17a63160f | -2.8791 | -57.8184 | 2026-09-20 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c47f763b-24dc-3376-b23c-d158f711fdf0 | -1.6041 | -54.455 | 2026-09-20 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 577826fa-4656-35cd-ab50-aa4ddf030191 | -2.4451 | -49.2093 | 2026-09-20 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b578b69c-b9a7-3583-8deb-ea834bad300e | -8.028 | -61.3435 | 2026-09-20 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |


[Clique aqui para ver as próximas entradas](README3.md)
