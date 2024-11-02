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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acb03852-c842-3144-9210-d0f9bb1a0c6f | -4.73724 | -46.15868 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12a63d13-991b-3898-8adf-cead453ffd66 | -4.73118 | -45.68971 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a5e4e4a-6c95-3090-a616-803c864b447f | -4.729 | -45.74829 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa3636b7-891e-3c71-98ee-29b8ed67be4e | -4.72608 | -45.74369 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8b4229dc-2c32-3702-a5c1-c08d934fdbff | -4.72541 | -45.7478 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccc385da-47b5-3877-951c-b3b77736f633 | -4.72249 | -45.74319 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90e8f00e-5557-38a5-8305-231a3a273ce5 | -4.72182 | -45.74734 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba6afe5e-c3fe-377c-8d13-41b51839458a | -4.72056 | -45.64266 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9219457-a61c-366a-be9e-7cf4128fbeeb | -4.7 | -45.83626 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 383c142d-6ab1-3e90-b675-b9ea2be56293 | -4.69214 | -45.48297 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a9d4d08-55c1-3b49-a446-de997b35beb7 | -4.6895 | -45.65897 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84cd9609-3a4a-3bbe-9196-1390594fd3af | -4.68886 | -45.663 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86b33fa4-a84f-3c5f-9b7b-135fc9d62c63 | -4.67783 | -45.68638 | 2024-11-02 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2b68895-c902-3f79-8aed-7fa81e7e5a67 | -4.67479 | -46.05939 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4abb4d59-b4c8-369e-8f76-4e9507161f7a | -4.61496 | -46.03363 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01218190-d702-3e53-b49c-f6225266eb0a | -4.57407 | -45.67915 | 2024-11-02 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc1f7ca0-ec8c-3d79-a5e6-3aa40f67706f | -4.57342 | -45.68328 | 2024-11-02 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e989fed1-b398-3e68-8782-08831f45bca1 | -4.5705 | -45.67859 | 2024-11-02 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4cd019e-290b-336a-9d91-b042ba80d806 | -4.56984 | -45.68272 | 2024-11-02 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 444a50ea-6565-3e42-b75c-aa9417f61a8b | -4.55141 | -45.54716 | 2024-11-02 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2b780c0-e581-37b8-8593-ce971e271099 | -4.54721 | -45.55064 | 2024-11-02 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e462f61-11ce-3528-9777-4aa2a47c0df1 | -4.52287 | -45.63343 | 2024-11-02 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cb4b7ff-ea22-33a5-ab30-6af6c099e28e | -4.48523 | -45.55431 | 2024-11-02 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b2f29bb-4323-3612-93e1-f80a31f23fcb | -4.4846 | -45.55827 | 2024-11-02 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fffc38f7-a28b-3ed6-aa43-e02c1042a434 | -4.43741 | -45.62492 | 2024-11-02 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51adad03-8ac1-3b1b-a41d-0249f246b0c1 | -4.42783 | -45.86844 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1af50399-23d0-3211-b140-92492db0b2a4 | -4.41563 | -45.64646 | 2024-11-02 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed8666cd-f4e8-3c63-afd4-098e535bf9d5 | -4.41138 | -45.65006 | 2024-11-02 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dcbbf64-6702-3707-84d2-c0b747cd5128 | -4.40551 | -45.86898 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f91b7d3-add6-31b5-b04c-c80fec8da0ef | -4.38378 | -45.79745 | 2024-11-02 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a0e021c-256a-3286-b11f-ebc9fda00eb1 | -4.35366 | -45.81525 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cdf222d-b560-388d-8b05-c5ac925f613d | -4.3534 | -46.00724 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c33719b-4fb3-3672-8409-8b908ed55abd | -4.35005 | -45.81474 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b738dbce-4350-37a5-9d35-f14415cca8a9 | -4.32801 | -45.88357 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3ff9e79-a0e8-3c83-9199-e2e68e207bbc | -4.27786 | -45.56099 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2f08db5-a2bd-39af-8be2-36cf983fe26d | -4.2253 | -44.93731 | 2024-11-02 04:12:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b7646a7-8e6f-32bb-8af7-9fa03bb59368 | -4.21714 | -45.94804 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcef7ff3-b36c-3dcc-b573-bc400501f251 | -4.21626 | -45.94984 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6113dd6b-cf70-3b52-9268-db88ea6411f3 | -4.20747 | -45.88803 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f145b1db-b323-360b-9f00-d6348efdda73 | -4.20023 | -45.88684 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ef83ad92-3deb-3bef-9728-4e14f9332d6a | -4.16395 | -45.81253 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b8541d3-e4ae-314a-9aeb-66b7ce0ecc57 | -4.12718 | -45.00462 | 2024-11-02 04:12:00 | NOAA-20 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a92079be-8e28-3aac-83e9-e5c7d51b7796 | -3.89619 | -44.93336 | 2024-11-02 04:12:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ef1c498-e329-338e-9b55-30f8b292d891 | -3.80949 | -44.72956 | 2024-11-02 04:12:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb69f6b4-ba23-389d-a709-904675a3dc38 | -3.73967 | -46.05054 | 2024-11-02 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e668aff7-66d0-38a9-ab3e-d7bf32f15f67 | -3.66477 | -45.3166 | 2024-11-02 04:12:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 331012be-1d6a-3161-ab8e-eb253c9b7a50 | -4.43708 | -45.81046 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1252f2fb-a0bf-301e-b981-0e58c0879c43 | -4.42969 | -45.53707 | 2024-11-02 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dee0eadb-a62e-3293-be08-861eced5321a | -4.35773 | -46.00357 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cacbad9a-75a5-3843-8dbf-6c652fb8833b | -4.35704 | -46.00779 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71958207-c8fd-3cb5-8b8b-017f452cac2f | -4.35159 | -45.81356 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffe7500e-a9ac-379f-b9b4-9c54ba8a217d | -4.31114 | -46.03676 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f017dcc-0809-37ee-a907-cd7c2fca0083 | -4.30749 | -46.03621 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af4b7623-d905-31c7-be9d-489b6129f745 | -4.30664 | -45.73989 | 2024-11-02 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 149db2ab-9696-330a-b231-c48a9ab2599c | -4.28121 | -45.64726 | 2024-11-02 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0be61f9b-c06b-37f5-81fc-2bb2c3983371 | -4.27763 | -45.64671 | 2024-11-02 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 27c70715-923f-3bad-873a-067589401f2b | -4.27721 | -45.56504 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2285fd9-a79b-35ad-9457-870ae77c8353 | -4.24125 | -45.58425 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71a415f5-c7a0-33aa-98de-7895af7585d8 | -4.23768 | -45.58369 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa80cf63-2f5f-3253-87f2-d78e304416a4 | -4.20814 | -45.88385 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9261f6a-d64b-3ab4-8e4a-73aea5e08ab1 | -4.20518 | -45.8791 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79be8013-1b9c-3ac2-919d-6897b98da0a4 | -4.20452 | -45.88326 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ee3270ba-eb29-3999-9f33-4f559a760c5e | -4.20385 | -45.88742 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 138ecf8b-9451-3d4d-86cc-469cbb69595e | -4.20089 | -45.88268 | 2024-11-02 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 9baec966-1b39-39d9-89ed-17883262542a | -5.59193 | -45.20588 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5708fbe-81c7-3d14-baf6-7c134619efe7 | -5.51788 | -45.44291 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eff1d371-7b4a-3ca9-94e1-402f5bbbdc99 | -5.49438 | -45.40407 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fb61da5-4458-3d23-b842-ad1072993c8b | -5.49375 | -45.40797 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd2af839-434a-3106-a9bb-47b86ac1a129 | -5.48282 | -45.45411 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a12238a5-7c85-3135-b95f-ac1825bd2e97 | -5.46533 | -45.05386 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78db1cf1-68bb-3d10-9d9f-c28769921a2d | -5.33893 | -45.35996 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 800fcc89-eff9-33e1-b032-84b916725db4 | -5.33545 | -45.35939 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75a63355-5564-3458-885c-8246c5b5a6f6 | -5.329 | -45.15739 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c7b4752-ce49-3da9-a196-4b74f2b49f6b | -5.324 | -45.15337 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c32d4ba-00f4-3756-a304-14f0fe61c6e1 | -5.32339 | -45.15718 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 570f0a90-c0ad-30db-80ab-adde8d1d93aa | -5.32054 | -45.1528 | 2024-11-02 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c84e2e1-cef4-35b0-9308-ad9e09b96ddc | -5.16933 | -45.32983 | 2024-11-02 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa7c1e0a-229c-3ec9-a1d0-ede0c0c74c1a | -5.16871 | -45.33375 | 2024-11-02 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4541e8e5-7c9c-3535-bbd2-d4f2ad1272eb | -6.43606 | -46.30999 | 2024-11-02 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af9d25c4-85cf-368d-ae76-97d6e7601ffe | -6.31816 | -46.09317 | 2024-11-02 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06a3666e-acd6-3f10-8366-f7d1eea0276b | -6.27235 | -46.14865 | 2024-11-02 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5e7e28c-1549-31c2-b5e3-69e7c5d53976 | -6.04807 | -45.81567 | 2024-11-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ad6a9ea-d158-3094-8bb2-ea12f553e87e | -5.72576 | -46.21177 | 2024-11-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1ac1e4e-1af3-3598-8cd7-8ed67718bbd5 | -5.63716 | -46.38578 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da78acfa-0dee-3412-8c77-833907a94656 | -5.63351 | -46.38515 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9403209c-a05a-3983-9a1f-aabae88df0a0 | -5.59834 | -46.25694 | 2024-11-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 104048b8-7c77-35ec-a60a-884cf675b875 | -5.49133 | -45.94277 | 2024-11-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 014d5592-0178-3612-9a21-946c54362da8 | -5.4418 | -46.27309 | 2024-11-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa50a972-fbd2-3ea6-8cb7-0d8ed8b4fb56 | -5.43885 | -46.26823 | 2024-11-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f26eb17-561e-32b3-8d5b-d0b9d5492559 | -5.27754 | -46.24747 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a62d6ab-3433-3f57-943b-12b7b72b12d9 | -5.27683 | -46.25177 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5747b264-d7e0-3bbb-bd3a-824432a82f74 | -5.27247 | -46.2555 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14feb64c-e2ea-3829-8832-0b93f8f70a1a | -5.26397 | -46.30714 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a86ed28d-3de2-3ffa-8d9a-27cedfeec79f | -5.26004 | -46.16821 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 619e97f8-5521-398d-b5e0-16a0cd2054ec | -5.25646 | -46.26175 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfe495d8-5487-3398-87d9-8eb09e89704b | -5.25282 | -46.26112 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16ecda67-2411-3bd7-a58a-2c16bb378911 | -5.21851 | -46.14856 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b3ddb76d-b5ce-3687-bdd4-96b15b95cb57 | -5.21782 | -46.15281 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| de8ded09-442d-37af-bb72-9cd07d2cd452 | -5.19537 | -46.15343 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ef85c786-aa6e-31ad-9cd7-0842aaef5bb4 | -5.19415 | -46.18367 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README40.md)
