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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 906ca22c-7697-33ae-bf1a-f3020cad5b49 | -3.93638 | -49.99109 | 2024-10-01 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7538efb3-7178-3d1a-859a-8be2ac94bb1a | -3.93583 | -49.99473 | 2024-10-01 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0fa85bb-5906-379e-bd14-ec1371373906 | -6.20745 | -50.90728 | 2024-10-01 05:04:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdfe56ea-e911-3f70-b2dc-536525ffc6df | -6.19633 | -50.90028 | 2024-10-01 05:04:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0fe56a33-7b68-3565-b463-0682f5376f4c | -6.19237 | -50.89963 | 2024-10-01 05:04:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b531ab1-1c07-384d-b892-e3edcad6bfde | -6.19162 | -50.90471 | 2024-10-01 05:04:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54037c23-90cd-33e4-b1b1-ee6004d3bf5f | -6.17971 | -50.90303 | 2024-10-01 05:04:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b098368-638c-3c13-86fc-4a374c14f301 | -6.175 | -50.90745 | 2024-10-01 05:04:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28b99f0b-ccef-3270-827b-1750bdf87ee6 | -5.35946 | -50.02911 | 2024-10-01 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 433d77f3-77e4-3f3d-a3a2-31f3ff3f933f | -5.35532 | -50.02845 | 2024-10-01 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00c4b9d5-ef07-3041-9d91-ca89f5485e7b | -1.62497 | -50.53856 | 2024-10-01 05:04:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e76c6b2-0a41-3b71-a9dd-8b26021a55dd | -3.44334 | -51.56225 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c80388cd-99fa-3279-b9c3-3dcf44a9caba | -3.19017 | -51.47996 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1d62459-b5ae-3887-abd3-d51fb4c8903e | -3.07284 | -51.21567 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 997b9693-f85f-3216-8027-c83fa1fe1a6a | -3.07217 | -51.2201 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7595ab6-9758-3f9d-8b31-990942be3f04 | -3.06912 | -51.2151 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31c67be0-bd55-36b5-9aba-ead6070ab2d6 | -3.04922 | -51.27117 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44726226-1917-3a23-808a-2ef4c5cfa62a | -3.0436 | -51.33354 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e76bec9d-664c-305e-8e8d-dc7ccae78f84 | -3.04054 | -51.32867 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dae75ac4-a2f3-3b1b-a429-93bb10dce19d | -3.03989 | -51.33304 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91649cf7-c7d4-3973-b854-21fcba1c7803 | -3.03618 | -51.3325 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2393b8c5-1cf3-30b4-a6d7-91482cc2f6d1 | -3.03248 | -51.33192 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 81d2c84e-49de-35ac-b457-e9aed85da791 | -3.02878 | -51.33135 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d1d2ab3-9be2-3ca6-ba30-90543216e09b | -3.02812 | -51.33573 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 26792cf8-60aa-306c-9205-a0049294d2df | -3.02747 | -51.34007 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dfe552a6-d7fc-33f7-9d0f-4d9f5673613f | -3.02586 | -51.33323 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82e32f70-24c1-3c55-bef3-9ba62c7cee99 | -3.02517 | -51.33758 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc21ac35-5b8a-3dbb-be3a-cb36b88c7c99 | -3.0245 | -51.3419 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22f2f600-d965-3109-b1e9-9f5d8c99100a | -3.02442 | -51.33515 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b6b62f3c-32b6-3cac-91ca-8fc00ac39c81 | -3.02377 | -51.33949 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5b68be0d-83bf-3531-80ec-6344cd4661b4 | -3.02148 | -51.33699 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6274bfd-eca9-3111-aa8a-1d2fbf917f72 | -3.0208 | -51.34133 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3fde2be9-e41a-3003-85e0-62183e0213c7 | -3.02012 | -51.34565 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efd0c5a3-4ebd-3315-b4bf-910707e03cd3 | -3.02007 | -51.33891 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aeeb19e0-8250-3005-be9e-4a6d94fc4310 | -3.01942 | -51.34325 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 350e3fda-87ba-3c0d-af9e-9bf2da857db5 | -3.01876 | -51.3476 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab3c7258-3bcd-308a-93a6-0ba97bc8cfd0 | -3.01643 | -51.34506 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad7f85d9-0d11-3c01-a93a-8c211783de9a | -3.01575 | -51.34945 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 806d4fff-8b0c-3e17-bbe3-90f21862ee12 | -2.88129 | -51.66304 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6c728c6-ec03-3bd8-882c-dda5f919e4f8 | -2.87766 | -51.66248 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad5f0005-a88d-3a06-b033-aa207b0aa655 | -2.87702 | -51.66671 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb79fb5f-aae0-35b1-85b6-7862c7da4653 | -2.87531 | -51.65348 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d12e55e5-97d7-3694-8c8e-d6716462a4e3 | -2.87467 | -51.65771 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e7ee0d3-c0ef-3acd-9bbb-9142b9469766 | -2.87168 | -51.65294 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4173efd3-0e09-36b2-a2d7-99a9dd072a99 | -2.86201 | -51.6618 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e0a5c8a-98ff-37c5-8150-2c21e7d6fb97 | -2.85839 | -51.66123 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 450d01bd-a9b9-3232-bc5e-f75c8696a588 | -2.70102 | -51.34468 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b66073b9-9d09-3589-b8c4-227a5a5b8dad | -2.84633 | -50.74186 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e43e990e-5bed-32c9-ad7f-a0a332ecb3bd | -2.8456 | -50.74657 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb936199-4954-3fc9-b219-a2f16ab7838c | -2.8425 | -50.74126 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 705c2303-30ba-315c-bc25-0fc32da452e4 | -2.83868 | -50.74067 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e52daed6-8fc2-3081-b456-cc471e10b23d | -2.70471 | -51.34525 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4de1f9a6-ff3c-308b-8b96-8422ed3c62f3 | -2.67947 | -51.7075 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 15b4a293-26eb-3378-b4f9-4577ee213b9e | -2.67883 | -51.71165 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3125b2a9-9a9e-3f53-bb66-a44735475f8e | -2.58546 | -51.92175 | 2024-10-01 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82ca66f0-f27b-3e81-a299-e0440c56b5fa | -2.27748 | -51.25338 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d863e35-c4ff-39bd-9e9f-d3a18e9a2620 | -2.91907 | -50.74601 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 403dcfb1-05d3-37b1-8487-2e08f1e0598d | -2.91836 | -50.75073 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc065f89-baf3-3372-97de-c1f5c5d039ab | -2.91596 | -50.74068 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3640447d-fbf2-3f06-a213-e93182b7c47f | -2.91525 | -50.74541 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 011ef901-1d54-34fd-8f62-4f4c17492e55 | -2.91383 | -50.75485 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9c6a184-1293-361b-9fb0-6922c1fb890a | -2.91312 | -50.75957 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5d526b8-8bb6-3be5-9040-d8bb4a619600 | -2.91213 | -50.74009 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b7cf606-a120-3bc1-a3a9-471aea86585e | -2.91 | -50.75425 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baa19796-5744-36e5-8382-fb5a492d15d3 | -2.90929 | -50.75897 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4cbf972-dc78-368b-b490-f76b30d468da | -2.90859 | -50.76369 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f24dc625-d9ef-388f-a9ae-819976583534 | -2.9076 | -50.74423 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d885ecd4-783c-3b3c-a9b4-cc96eae6e498 | -2.90689 | -50.74895 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f37abaa-3345-3c2e-aaf9-c183a25d04be | -2.90618 | -50.75365 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d2b8bf60-ad1e-3a6c-8798-9ecafd59c1b6 | -2.90547 | -50.75837 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f8afa48b-8bb6-3f2c-941d-f52d2e058a0b | -2.90477 | -50.76308 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 113b0c7b-4d5d-3aab-931a-ce43271dbccf | -2.90236 | -50.75307 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 518fa193-aae3-3d63-b2a8-8b69dd2183c3 | -2.90165 | -50.75779 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 32da9380-ef59-330a-afe3-49da8e188285 | -2.90095 | -50.7625 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a99f0e4-66bb-386e-8984-6cb2369f2f6b | -2.89909 | -50.75484 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eb53ebef-ae87-3aa7-b429-2839de015100 | -2.89853 | -50.75249 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 05a85017-342b-3124-9bf7-d6655ad5348c | -2.89836 | -50.75954 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a150fd2b-6899-39c1-a305-136b326fa5f4 | -2.89783 | -50.75721 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d003f425-623d-3220-aa58-1d2a39b91a8c | -2.89712 | -50.76192 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c7c9afe-a2af-3902-a724-d9f4557812c9 | -2.89674 | -50.74483 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d54031aa-cc3e-314d-9d58-a5e15889d94d | -2.89642 | -50.76663 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e1491b9-19f4-30d5-b23c-61b500cfff4b | -2.89541 | -50.74718 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b0cc44c4-ce4e-33d9-b470-e404efe7598c | -2.89454 | -50.75896 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9e66fdad-1d82-33d7-9d85-d4b3642340d6 | -2.8933 | -50.76133 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3dd9124-7d82-385b-a29e-7da34bda2ac7 | -2.89072 | -50.75837 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e61254c8-707d-334d-8804-1470a3b8b73d | -2.89018 | -50.75602 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19543287-9ee3-3623-bd4f-a1018ceba360 | -2.88998 | -50.76308 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40cd09d6-55a2-3b46-8729-c6e77de3d50b | -2.88948 | -50.76074 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 234c2b75-686e-3475-8c45-5e38f507eea0 | -2.88763 | -50.75307 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f6773f85-7d0a-32b9-aa90-49a41cf37f8f | -2.88707 | -50.7507 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b6e1ccc-30be-30fd-98f0-684a15e7bba1 | -2.88636 | -50.75542 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9b1a7f1-6254-3c1f-9ee8-7ccd719044b4 | -2.88616 | -50.76249 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93f361b3-fcce-382c-a3d2-886cbb541308 | -2.88566 | -50.76014 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 342af519-f509-3df2-80a3-68c8fefa0a2c | -2.88381 | -50.75248 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 089da534-5bfc-3f16-8331-2148806da7ab | -2.88308 | -50.75718 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed20d250-9b85-398d-9dab-4c5532ac4f6f | -2.88072 | -50.74718 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ed1bc05-d1de-316c-9d64-c0be9b49c32d | -2.87999 | -50.75189 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 333e0a93-a67e-3148-b846-4a08c673e975 | -2.87926 | -50.7566 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62d0140a-c69f-33ba-a5d3-5e94153026ec | -2.87544 | -50.75601 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 935a1437-f0ec-3926-8c1d-2b883c0281ee | -2.87308 | -50.746 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README101.md)
