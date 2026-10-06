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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f238990-0ae1-3b8d-b4a7-3368b538ebe3 | -3.5036 | -54.62666 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8df67592-9750-3879-82e5-3a773e6eaca6 | -5.67588 | -53.4954 | 2026-10-06 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7169cea3-a2b6-31c5-8d09-d6b99146bcb1 | -2.7737 | -54.10066 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4c559709-0a86-3a01-93e0-d24cb4f692eb | -3.50575 | -54.61209 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c3b8f3d-0294-3a73-a28f-d1bfb45f4b4e | -2.94052 | -54.13779 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e67a4e2b-2e2a-3528-8d33-c97b26417f33 | -3.67553 | -55.94304 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 38f8f98e-2efd-3fbd-9536-60cbc8d521e5 | -2.80737 | -54.1377 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e8bb08c-bfce-3e6d-a8b1-656025c293a4 | -3.49593 | -54.63525 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa2952c4-21a5-381c-8393-7f350046fe4a | -3.09639 | -54.15997 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8ab51298-a0cd-3503-b226-ec270926c413 | -3.02768 | -53.90142 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ee3ae1c6-c6da-35ca-af44-6f62f5f88e74 | -3.23596 | -53.87573 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e900f037-bb46-3587-b43c-16d95ad2a6a2 | -3.27737 | -54.18171 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 595d1492-db04-305f-85fe-30e15489949f | -2.7803 | -57.67762 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce59abec-8381-38a4-8f9d-3a84c6107e65 | -3.06198 | -54.16249 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88dd01cd-13ed-3617-9f4d-9a21c3e885a1 | -3.22469 | -53.87383 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebf62730-2a65-3158-b6b4-34c2466de04c | -6.69338 | -55.20931 | 2026-10-06 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccbf1fa9-f740-33fa-a685-1718cc97aa96 | -3.07861 | -54.23774 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99e03cb6-e86d-3d11-8d30-2162b180a46c | -4.46756 | -54.9744 | 2026-10-06 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25181d93-1ee5-3501-b08d-daf373459c86 | -3.07004 | -54.25187 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3aa66bc7-457e-382b-877e-75b303b4d984 | -2.93409 | -54.13687 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b0293dd-aa49-3c08-81e9-2666f11d272b | -3.0985 | -53.73777 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa1ff74d-6f2c-3d17-bf78-8e5cfbc1d8b8 | -3.35286 | -59.49443 | 2026-10-06 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0ca2c90-e6cf-3a98-874a-ac2a419ca5dc | -3.22785 | -53.88567 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d93db93e-dd10-30d6-bba7-c51c902d2c9e | -3.05902 | -54.22593 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1cab3d41-198e-3a8a-b55f-12fb93565ab1 | -2.78538 | -57.67838 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bd1425b-baa9-35f2-b0b5-81953a4e4213 | -2.98143 | -54.12769 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 87815bff-f5d5-3bcd-b9a1-3b3f490da140 | -2.88152 | -54.12848 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad867d81-bfe3-3801-9da4-8aa9769ae84d | -2.99673 | -54.11506 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f13ef63-15ed-307a-99da-6ab70a468b33 | -3.08224 | -54.24528 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 526aeb98-c550-3cbf-892d-da08063b7d51 | -2.78048 | -54.10204 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19ad90ca-be6e-395e-b9be-2befc1a04cc3 | -3.06042 | -54.17296 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3242da10-6a42-3966-bf9b-8253acc6293b | -3.95537 | -56.04921 | 2026-10-06 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2bc7b44-350c-34de-be75-ed404dfe6fa4 | -3.07324 | -54.1749 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdbca843-1ebd-3621-bc72-6aa3c2354a5a | -2.92921 | -54.12551 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ec27d6f7-7104-369d-915f-3c6e6d147bf1 | -2.78493 | -57.68132 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb5bb0ee-b8df-3fd0-8053-92162e5e8680 | -2.52853 | -58.09211 | 2026-10-06 05:59:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60fed56f-f267-35e6-8996-47a5810ffb4a | -3.09438 | -53.71997 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e27502cf-ec83-3ab1-8052-8d9c1edaf75e | -4.46135 | -54.9734 | 2026-10-06 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da1eeaf5-c7d2-3b06-8c08-e70978b2b8c0 | -2.78347 | -57.679 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2d165c0-60da-3c44-8332-b3514f15fdfc | -1.28247 | -56.98428 | 2026-10-06 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8aa6b6ff-b87c-3632-8154-ff79f6af717f | -2.87511 | -54.12749 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74a5ecd8-b272-395e-976f-fa95af4c3119 | -3.62862 | -58.94104 | 2026-10-06 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dde5888d-081c-3ec1-a918-eea5cd1282bd | -2.77407 | -54.10103 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1819824e-9186-3a9e-8672-ae3e3d6a21d5 | -2.89183 | -54.15682 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5aa4e0ee-c749-3e61-91ff-f834bafd3286 | -2.93974 | -54.14301 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ab7c889-c648-3907-b6ba-5e405adb1069 | -2.77888 | -57.65324 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98956601-af08-369e-9438-d0ed9626ff39 | -3.50649 | -54.607 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59b6a4d7-58c2-3073-ae88-ceeb934e3dcc | -2.99597 | -54.12027 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2bd6dd0-6348-3037-aa8a-15570f7fd2c5 | -3.68593 | -55.95288 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 91eeb466-9380-3736-b6f3-bafe55b2cdd1 | -3.08211 | -54.15961 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8e9fcec-8b1b-3b77-8f65-6ebbded0b7e6 | -2.79455 | -54.13586 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5bdaa918-dcfb-3c00-b9c2-f835fd77425f | -2.78168 | -57.66877 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91f85d93-c82a-37ec-950d-0305f811f978 | -3.22942 | -53.8747 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4691f92-7fd2-322c-a464-5c6ab9a515a6 | -3.10949 | -59.16811 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cc97fcc-6357-32bf-9627-53de772005e8 | -3.70422 | -58.92867 | 2026-10-06 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90f6dceb-e701-3c7f-9a9e-6d367243f07e | -2.77448 | -54.0955 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 342eae38-2e22-33d5-b115-0c88efaa68f1 | -3.69174 | -55.95358 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d8088d9-d36a-375e-a304-32f78f73c9e0 | -2.94538 | -54.14916 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90887297-a1bb-3394-8541-f2761ad6aac5 | -2.77556 | -54.09071 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0394d7a6-f683-37d4-a2c5-41637f06b33a | -2.78011 | -54.10164 | 2026-10-06 05:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa633dc9-08ab-3ad9-9e1d-6eba5beb9ee8 | -3.07566 | -54.15882 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97d7a638-2bed-33dc-836a-043e32d63a07 | -6.48766 | -62.85854 | 2026-10-06 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 488b93f6-3c39-3376-87ae-1b8419c6e027 | -3.23777 | -53.87589 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91a72783-03c0-3a5c-90a7-1976c6449a6c | -2.99501 | -54.1248 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49cf3548-f64c-3b97-855a-54d8fad80cf6 | -9.48884 | -63.96024 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca89f150-c962-3e70-a001-30e64b7e249a | -7.68862 | -69.93615 | 2026-10-06 06:01:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b171959-12e8-3ce6-af11-e68982a7decc | -8.59279 | -66.81274 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8360232b-0bd8-3805-8976-4c2fac922d4b | -8.59223 | -66.81625 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d91dcd44-0af1-3fb2-9e44-f230b9be3d24 | -8.97033 | -65.43982 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24e4f938-8b65-39cb-8106-abb6ac52dceb | -8.62336 | -67.00047 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82e45563-0d14-38b5-b1e8-fa8481b005bc | -9.49254 | -67.79266 | 2026-10-06 06:01:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aca2abf9-b99b-397d-a1c3-7ec03ecf5a9d | -9.17294 | -67.67328 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81bdf41f-146f-3927-a86b-31d46c7b2069 | -9.10702 | -67.75208 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6465675e-8fc2-339a-b3ef-50664537c3d5 | -8.60157 | -72.7318 | 2026-10-06 06:01:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b35fa255-9d0f-343e-81de-64912e6359bf | -10.09044 | -68.46864 | 2026-10-06 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96b58432-df56-3f89-9bea-fb8d99a2aa82 | -8.62624 | -69.51113 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86144975-b4b9-30e6-9d1b-a361918be3de | -8.8733 | -68.53463 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2d989d9-1939-3ec3-a87d-eef8f35a8bbb | -8.78055 | -69.53622 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac780fa6-c5d0-3042-9212-8e296a6090fd | -8.85863 | -66.79378 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e29d61a-452e-3de9-831a-a8cdbbfef594 | -9.54713 | -64.81805 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b60a36e-104c-3245-b2ad-2d43bbb6c47e | -8.78027 | -62.87393 | 2026-10-06 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22c1f624-cf2c-3b78-a4a8-9bc9b0fe5e0b | -9.15284 | -68.24 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5649b09-d148-3156-b3a3-8b5515aff1c4 | -9.35981 | -67.43766 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dbdc5fc-68ff-31ee-8c70-dd782427e4f0 | -9.11261 | -65.35332 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0e8b08b-c6fd-30db-be77-ebc01aa8977a | -7.36746 | -72.4641 | 2026-10-06 06:01:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a639ddf-4366-3aca-94be-acf3216e1d1f | -7.44878 | -63.56023 | 2026-10-06 06:01:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a98dfed2-5ec9-3dc9-a51b-03789a806dc6 | -9.13235 | -67.75645 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32b8a4b8-1050-36ce-9359-703242f95ec7 | -9.16509 | -68.24926 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00ce9bd1-7d27-3e21-bc5c-c16d1c8632ae | -12.1297 | -63.15563 | 2026-10-06 06:01:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de6ee72d-b592-31b7-9beb-a22e6f0f388f | -7.36888 | -72.46474 | 2026-10-06 06:01:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fefb3a9f-28ab-3192-8e26-7df832b9ef55 | -8.27498 | -62.86916 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b823576d-636d-35dc-9ce1-5364178579d5 | -7.84883 | -72.46114 | 2026-10-06 06:01:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bf8123d-1893-35ce-9bcc-21960de1375c | -8.39383 | -70.11035 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4136ce4e-0ecc-39bd-94d9-5c8a44b482ac | -8.82685 | -67.38451 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6701c40-0c82-3400-9712-655d4aa2a397 | -7.81936 | -72.83505 | 2026-10-06 06:01:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 65e74b38-0221-3268-aedf-d3eb48c03c3b | -7.88874 | -72.35085 | 2026-10-06 06:01:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5b011c25-5cf2-3585-b293-369190605c71 | -8.92264 | -66.84359 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af82a32e-d4bc-3240-8772-f664dbd74eec | -9.67242 | -66.82802 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f8b7980-cd01-3994-a3fd-f57499a118f7 | -8.92931 | -66.84465 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 10a733b8-6f64-3e42-8329-079c46a00522 | -8.88308 | -66.76881 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README72.md)
