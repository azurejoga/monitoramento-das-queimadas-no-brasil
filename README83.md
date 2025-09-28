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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c10920d-cf69-3be4-bcbb-ba65acd8a032 | -7.80309 | -47.0128 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6482bc92-24b0-3c23-bda8-0253ea078a30 | -7.80745 | -47.03025 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 62ca70da-2980-3b86-a569-287093a4c24b | 0.96683 | -60.40942 | 2025-09-28 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dcfff90-fce8-37a6-8dd9-a9e968bca0fb | -2.9861 | -49.54096 | 2025-09-28 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90e3fef5-7799-3c65-aac9-81f7098de474 | -7.79147 | -46.99987 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5a4dcad5-ebd1-345f-9120-8851d64851cf | -7.78981 | -47.00953 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e09a7fbe-2a40-3ff6-bd66-787fc37086f3 | -7.81593 | -47.01339 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b5a662b7-5fa0-3481-b1bd-f916ec7ca6a4 | -7.37789 | -47.02406 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10538685-6158-3022-bfe7-545b5284b595 | -7.37676 | -47.03014 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b549edd0-7d07-3878-b23c-7773765648b9 | -7.75739 | -47.00615 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fcad8d3a-0e48-3149-b71c-ac14950307c6 | -8.17349 | -46.40207 | 2025-09-28 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dbb949e0-eb73-393b-a05b-164c79a88eae | -4.91866 | -48.16367 | 2025-09-28 05:16:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e078809-dfe1-35a6-a3eb-7c97901b7e6d | -7.74434 | -47.0042 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7dc789ab-72c5-32d9-baa2-0bae3d2a3ab1 | -7.79501 | -47.0213 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6fe70cb7-fbab-3fa1-b1af-01b737cce50a | -7.79587 | -47.01717 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a23808ee-20a5-32db-b6b1-65c550c61114 | -5.34075 | -45.64268 | 2025-09-28 05:16:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cebdac63-1307-3e47-a4ff-bb50f6f7e14e | -7.81144 | -46.99609 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 26940a32-f87d-341e-af74-a240c3346b9a | -7.37026 | -47.0293 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44c4e6d0-43ca-3f5b-a19b-45f76db7684a | -2.53926 | -54.7378 | 2025-09-28 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e9f74a5-c644-35d7-8f62-29ee17653cb5 | -7.80819 | -47.02462 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 6599a513-4bc6-332c-8bfc-cbf865509617 | -4.81839 | -48.24329 | 2025-09-28 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d036472e-a6a6-31ae-bae8-42a4bab893cb | -3.33352 | -50.25111 | 2025-09-28 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d95d5f2-ad3b-3dbe-8c8c-7a5d94c9d644 | -7.8042 | -47.00074 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef37e45b-9017-3bdb-91a5-c6af375b9fd1 | -7.78213 | -47.02058 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cf5a3496-3d5e-3a09-a553-1476cc99d680 | -7.81029 | -46.89729 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54a180ee-2147-3da0-b696-cc006e45f9cf | -7.81545 | -47.02002 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| fc73d99b-e251-34bd-8135-b7e21f6774d0 | -2.97205 | -49.23251 | 2025-09-28 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f817faa9-842b-38eb-b6c7-209ea97318be | -7.74947 | -47.01614 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c64f1da-2297-36a5-8ff6-7cd591c1769f | -8.16881 | -46.42662 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 6bc69d3a-d21c-3e96-b0c0-7c6dc467a84e | -7.79075 | -47.00539 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13a775f6-e9a6-31e4-8f1b-f9f3d1c827c1 | -2.58647 | -48.40971 | 2025-09-28 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6f401eac-3914-3fc2-b193-22551b4ccdb3 | -7.79432 | -47.02683 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7dcec036-3716-30c3-ab5d-f023191cfc9c | -8.17415 | -46.43905 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 56622bcd-c4fd-3c31-b3f0-97572619c6e1 | -3.33394 | -50.24821 | 2025-09-28 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2d9d1b0-826d-3a7c-af4d-b578758f7781 | -7.78282 | -47.01521 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9ac5810f-3044-38e2-9bc6-15393ece8e3d | -7.74878 | -47.02148 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da5d551e-a5fb-32c5-a6e8-14810b9be602 | -8.1703 | -46.41489 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| bf5cbeda-bd21-340f-a8db-822027457ad1 | -2.62165 | -54.73708 | 2025-09-28 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88e46b84-a075-3a44-93bf-22ab05c8559a | -7.53483 | -46.1003 | 2025-09-28 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bae83c31-406c-38f8-b851-41abc46ab96e | -7.16654 | -45.50399 | 2025-09-28 05:16:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2f55696-4a92-367d-8373-23f53ba3d5ad | -8.16954 | -46.42092 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f756212d-be9f-3a15-b379-1975e64da427 | -7.78196 | -47.01928 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ac15c70-594e-3d37-abff-0912e363321e | -7.54247 | -46.09518 | 2025-09-28 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 37b5ec82-e537-382e-a754-c226bba9b6a7 | -7.79769 | -46.99961 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3a446d3-b4e9-3ec5-8250-20b6bc8b9c81 | -7.81128 | -46.89886 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f6188f0-78eb-3bda-b6ec-fdb212806a2f | -2.98566 | -49.54401 | 2025-09-28 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3b85921-d4c3-3ebf-9e55-0b8f2bcdd817 | -7.79634 | -47.01052 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 376ce5df-e423-3cf3-8a2d-83461f1aeffc | -7.80522 | -46.99652 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d06762aa-c90b-35a4-879c-f6aaebbfe824 | -7.78353 | -47.0098 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5c53914-c9b8-3023-a5b0-de3de0e42200 | -7.80734 | -47.029 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| cd3eb801-9a00-3fa8-9967-4af4106ff429 | -8.17261 | -46.3966 | 2025-09-28 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 414fd6f4-61d7-3ce1-89d9-0992b53d0926 | -7.80595 | -46.99096 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 15a95ce7-c31b-3119-9d99-1270067ac746 | -7.54854 | -46.10249 | 2025-09-28 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 982fba86-08a6-31e4-9e48-b0388c657655 | -7.79004 | -47.01083 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 331b232a-8a8d-34bc-9ce7-93f84383a3c2 | -7.81177 | -46.99738 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1b69218d-55dd-3312-82dc-ee2b26f7493f | -7.75516 | -46.9715 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd3f7a60-8ebd-3f13-83f7-3b6b33f4f0b0 | -3.03269 | -50.43854 | 2025-09-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5355763-eed9-37af-89f1-24ac1ec65aaa | -8.16431 | -46.40744 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9603c26f-8a2b-3554-ba3f-bdb8e96378b7 | -2.68833 | -54.76733 | 2025-09-28 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34871f2f-3dac-308f-86b6-10801d7cd4c7 | -7.74157 | -47.02597 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6a04069-76c8-3c3e-b363-83d95961a0c1 | -7.3707 | -47.02864 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 49409f58-de6a-3e10-8928-640d79bda60b | -7.81688 | -46.89821 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 10e9ed29-d443-3b83-83d1-12062588e583 | -7.81032 | -47.00839 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ec48fe32-ec51-3408-bfac-bbb43c7fb224 | -3.80741 | -47.58413 | 2025-09-28 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26a63ae8-0232-3677-b41c-197316ace6e1 | -7.79837 | -46.99409 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8c6e541-8884-30da-8448-479b2ff3f55f | -7.81006 | -47.00716 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3bc24305-81f6-36fc-bbb1-1e2766c52a6c | -7.80168 | -47.02356 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1a40f50b-1091-3bba-b992-89017f55628d | -8.1749 | -46.43318 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4c72d932-c5a2-3158-aa69-6ffa2526a9ab | -7.81526 | -47.01883 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| e1e8069e-7b44-3c2d-a38f-baac0207580b | -1.62593 | -55.16812 | 2025-09-28 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 40b774e1-e586-345e-9fb0-8983c3c22df5 | -8.16736 | -46.43814 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 11794975-46cd-3590-96bd-b802e308da23 | -7.81786 | -46.89975 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d73a1a34-1edd-3c00-be6e-060a104e9fc1 | -7.79567 | -47.01591 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cdb6a156-0a57-3ff1-9650-c5e4b9637ba4 | -2.58759 | -48.40231 | 2025-09-28 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 28453939-c57f-3663-bbd4-0dcc6f064ead | -7.81616 | -47.0146 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 387c9d4c-d80e-3845-bc27-ffe4af7999ea | -2.83242 | -54.56133 | 2025-09-28 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30b56053-53b0-3cf6-982a-bf483b67bb1f | -2.19228 | -54.46045 | 2025-09-28 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 173d2f1d-17cf-3c43-bb04-da8ab21aaf10 | -2.19597 | -54.46101 | 2025-09-28 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40526947-fe0c-392d-b9f0-a21a0fbecdff | -3.80805 | -47.57963 | 2025-09-28 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d041b338-9fc9-3210-893b-e2b1834955e2 | -7.78915 | -47.01494 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0fd60ea-da38-3abb-85eb-ce779395b389 | -8.17633 | -46.42193 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1956a79b-159c-3aad-8b91-8b3f3c0c9a12 | -7.81661 | -47.00796 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ab6b53df-7de3-3184-88d0-fc08e6208168 | -8.16925 | -46.43745 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 149d2100-8a1e-39f8-8534-10e7992a1336 | -7.74792 | -46.97602 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f23e8be-4988-335f-b4e2-0a4deb91641a | -4.48419 | -47.67237 | 2025-09-28 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 95626990-a171-3228-af43-65c6af2bf1ef | -1.22852 | -54.12389 | 2025-09-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5403d551-c6c9-3241-9265-359994e95659 | -7.78129 | -47.02476 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 07edcc9f-b31b-3ba8-b1cb-6248ec74298a | -7.79516 | -47.02258 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dfc24c2e-2085-3039-ac1d-265df77f3108 | -7.80095 | -47.02914 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| cf112222-bedf-3aea-a139-9ce75cbe661e | -8.16809 | -46.43237 | 2025-09-28 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 00625b6e-9678-3f31-98b9-1447ca85f36e | -7.00323 | -45.62323 | 2025-09-28 05:16:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8efa785d-d69c-32ad-84dc-12cf3a4423be | -7.74721 | -46.98158 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41598324-bec3-382a-a8ff-d799860d2b3c | -7.81759 | -47.00372 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce7982f7-1d52-3668-b1f8-5dc9be1680f5 | -7.80558 | -46.98962 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| daa9d9bd-d113-3bec-b38e-ab7bee753a69 | -7.78142 | -47.02607 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 200ead69-22c7-33e4-ab46-79b2d1e1a6ee | -7.8045 | -47.00203 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95b3b7da-dcae-34c0-87ba-8f6043deb92f | -2.98655 | -49.53788 | 2025-09-28 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f085f0ee-3779-3617-8b94-b4350b1a90bb | -7.78423 | -47.00435 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dc2ff80-f815-38d9-a087-dc3022105d31 | -7.8022 | -47.0169 | 2025-09-28 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f6084dd-3efa-3be7-8812-1ea299f05fc9 | -2.79984 | -49.5973 | 2025-09-28 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README84.md)
