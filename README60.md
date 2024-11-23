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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ef4f507-643b-3c98-b8e6-bf25c803d350 | -5.32814 | -44.785 | 2024-11-23 05:12:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ffc77c7-b4dc-38ac-9734-a545674716ce | -6.05694 | -44.0498 | 2024-11-23 05:12:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cbac1e16-c45d-3007-9d08-3c9f9c447556 | -4.27255 | -46.29142 | 2024-11-23 05:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f579dd4-511b-3e66-add8-b2563b5d8b82 | -2.82064 | -54.02864 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68c94316-b97a-3a05-b491-c540bc0fc3c9 | -3.21138 | -53.84087 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d724d7f5-d2a3-3379-bf4c-bfe79efd3d2f | -4.0029 | -47.91607 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da9d6860-0146-3fe0-acb0-9f71da7b2bd7 | -3.50725 | -53.80828 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c57578a-db87-31a7-a646-949d6b5d3c72 | -3.90384 | -47.9356 | 2024-11-23 05:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70c8d8a2-f585-348c-9a81-efe8fba80c9c | -4.25664 | -48.70024 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c1b498a9-b9a1-3e19-906b-257527ca4d2f | -4.11148 | -53.63177 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44b5d830-3937-3228-a8a5-ba7ae1fc65ea | -3.0638 | -53.28206 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4cfad1a7-6675-3ff2-be40-103fff3b2920 | -2.83306 | -54.0183 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 259531fa-83ca-302b-8d29-cf8f03a3ef4c | -3.70627 | -51.79259 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0e477be-6c3a-3d27-9e6a-e282a0370bd0 | -3.7533 | -50.00777 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 07f687d3-60b4-3782-b68a-e916697ba886 | -3.22339 | -53.93021 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e65d83fd-6632-3ebd-94cf-650847b7ad78 | -3.97199 | -46.64453 | 2024-11-23 05:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b68885cb-2538-3dc6-b526-8a31424afdd9 | -3.57839 | -54.51979 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faaab524-c173-3289-a086-ea0517e2f56c | -3.25293 | -53.27349 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c9b4ef3-336e-333d-a6e2-0c71a2212f58 | -3.25073 | -54.22489 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f00b8826-c22d-36ef-9ac0-c6d410d48476 | -4.3737 | -48.50406 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c0f0fdc-9f4e-3014-b758-7e2e206cfd1f | -3.51924 | -53.8125 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2699afbe-a8f9-373e-9633-cb350f36ad90 | -3.25477 | -54.24572 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f0e8c1f-8c7e-3707-87ec-7c29924c7031 | -3.261 | -53.27026 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a1dce73-3348-3c33-a554-a28d31721aa4 | -3.29176 | -53.85698 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32c889fb-81de-3178-bbe8-e4e984a6a50f | -3.4593 | -49.68805 | 2024-11-23 05:12:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 77b699fb-f144-3943-ba4e-9605339ef8f3 | -3.51312 | -54.73686 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f03662d-7df6-301a-bcf7-ef646f8a8670 | -4.4511 | -48.19525 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3abbaf78-f100-3f2a-bc25-535e06709c21 | -3.23249 | -54.25015 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0e0fc30-2e90-35a8-835f-f83c79938c51 | -2.94791 | -53.7206 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fde03d9f-0263-3b3d-8fb3-0b5b49d8d2fc | -3.22991 | -53.93529 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0a9be98e-2e52-3b01-84b2-d9a6ab034d3f | -3.22573 | -53.93877 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66ec80e1-a497-3b56-bf98-d7becd7d2cc9 | -3.46868 | -54.64091 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cf534d9-6fd3-3a28-85bf-c0ec4646629a | -4.10609 | -48.50494 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 535455ea-5d1d-33c0-9b89-d42a95313c56 | -4.27571 | -48.6014 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02381dc2-834c-3d31-9ef0-336f47438d8f | -4.69378 | -45.84492 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8d6c181-c612-3464-9892-a8f7e3b22fcb | -3.81013 | -51.99062 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 398d8a0d-b4fd-3867-a8fe-61795259468b | -3.70152 | -51.79651 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 73a855cd-3c72-3512-8b3d-6e46da449251 | -3.25545 | -54.21756 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98a38a18-6dde-3168-af55-88aa5d3496a6 | -3.82743 | -48.9833 | 2024-11-23 05:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4c5db2e5-849d-39e4-bf6a-75c8bb53d568 | -2.89926 | -54.01219 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d24ac9cf-b58d-36c5-ae24-7eb6e9e9adc7 | -2.89571 | -54.01164 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 981b0922-a576-34ea-bca1-ac609a5146d5 | -3.1 | -53.73732 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b2dddfe-53ae-3f2d-a99c-fcfe00a68c3f | -6.48271 | -47.49888 | 2024-11-23 05:12:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b3e3788-0e38-3ad5-b715-5f15bd6464b2 | -4.54532 | -45.87841 | 2024-11-23 05:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 09366367-4b36-323c-bbc6-3a1477ec619d | -2.85867 | -53.96907 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7d7f2c5c-9092-320c-9f2f-0cfd4a64110c | -3.3019 | -52.57326 | 2024-11-23 05:12:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bc3d890-5390-33c3-a264-908cfec7c9ff | -4.70539 | -45.85212 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffec6e9b-138f-341b-bc55-d06015d10d28 | -2.88278 | -54.21196 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b19be3dd-b3be-307c-b6f6-fbc3f5591647 | -4.45062 | -48.19576 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 484e575c-5195-341b-900c-a1673da8fdec | -3.89854 | -47.93461 | 2024-11-23 05:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dd900af-9407-3f43-909e-8f753f09bcdb | -3.74854 | -50.01056 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92088450-7b17-319e-9f85-da4675e5c103 | -2.87983 | -53.99692 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5012bac-0802-319e-84a7-87413557931a | -3.10449 | -53.99652 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3b3a152-8517-33f9-a05b-abb91fd621f1 | -4.38529 | -47.77716 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6245fa32-52f3-32c0-84fd-d9be43a9540d | -3.31442 | -53.28502 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 87d929d1-a208-3c3f-8bc8-31a4f64418dc | -3.23837 | -54.23509 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 30344ef8-1846-3a99-8c1f-f01c5cb6aff9 | -3.24368 | -54.2238 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6730c92-b85c-3238-bdcc-0641359463ad | -2.82658 | -54.01323 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a31de97-de98-307b-8f7d-d3999b5e7a81 | -3.52533 | -53.79655 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b32a020-c347-33a9-bf2d-dd332752849d | -3.22634 | -53.93475 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0638fcf4-16d5-3e94-af2f-381810f8211a | -3.22663 | -54.24127 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afacef84-09ea-31f8-8132-f72bd415b0c2 | -3.1235 | -54.18156 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54e88135-52ff-3543-89b3-bc2d014029e2 | -3.97135 | -46.64898 | 2024-11-23 05:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0745efae-73cb-3f73-b7bc-c1355aa6395a | -4.70059 | -45.84127 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a295760-79d7-359d-84dd-b97b473878b1 | -3.1051 | -53.99253 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c60a5323-8553-3b14-ab1a-7ecefc88181f | -3.23952 | -54.25126 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbc708ce-e0bc-3d77-b315-6414ee3d1a86 | -4.74803 | -49.09535 | 2024-11-23 05:12:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d72f36c4-9ae9-3fa1-a822-eac1eebff745 | -4.08984 | -47.03056 | 2024-11-23 05:12:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 278ce05a-6f00-3eff-b5cd-a9a01450fc4f | -3.22696 | -53.93076 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab3928c2-b3ad-3a1a-acd0-064ba01ca6a4 | -3.63846 | -54.29338 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72e47386-121f-3e4d-8731-fb293c2b38ce | -2.94855 | -53.71647 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a50b31d-0da2-3da4-ac92-4667c43ae3da | -3.2596 | -53.27223 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1082d3d-0f04-3061-8f9b-d5edb30c731e | -3.2559 | -53.27166 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b7b6014-deb5-3592-9f3a-e8e5994aebc9 | -4.54521 | -45.87846 | 2024-11-23 05:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7452c024-a706-3bb2-9c82-21412ef68884 | -3.06986 | -53.29195 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 086fe001-ac4b-39f1-a322-7c8f3df13f0f | -3.81311 | -51.99837 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e0cbe77-790d-374b-9673-1c6b1d96cf59 | -3.34045 | -54.62988 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07326513-efc3-392e-9910-0baa23a63dfc | -3.1852 | -54.31937 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f85266e-fb4f-3851-9e7e-ae6375a4a690 | -3.18231 | -54.31488 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58661c16-8a62-3e3a-905c-eb2e7c586798 | -2.80698 | -54.02372 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2f161bd-6cc8-3430-a8a5-6cfefe9279cc | -2.82304 | -54.0127 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 047d6283-fedf-31e9-b6a3-34f1f4f02dac | -3.67018 | -54.27685 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7abc4652-c729-36f1-b10c-ec0f9da3d31f | -3.27319 | -53.82105 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b28c4e16-03d7-3760-8ea7-22c886a7cce4 | -4.25838 | -48.70047 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d206c46c-6264-39a5-9ed8-39abc9e070eb | -3.58004 | -54.71601 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a22e0cb0-f44b-3df7-8072-d711a109e875 | -5.12797 | -47.0305 | 2024-11-23 05:12:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3db32a39-a9e7-379a-888a-6a2c5721ceaa | -3.10094 | -53.99596 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41aa844e-254b-35e4-bc8b-a2a3fd7b7d4c | -3.24715 | -54.24848 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f982de9b-d00d-34ea-b5b3-b9d9c93a37e8 | -2.82538 | -54.02121 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50672d12-0e05-3cf7-afbd-383f4b321592 | -3.68391 | -54.58645 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d88079d-f3fe-3b12-9e6a-ebc004b4b96a | -4.55711 | -48.0201 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c2cf2de4-3970-3467-a931-0541333a52b3 | -3.29115 | -53.86108 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4e357d3-6427-3343-bdc9-5ac2caf7d2bb | -3.50427 | -53.8037 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78961b4b-7c1b-38ca-b91e-4c43764a7d33 | -3.1776 | -54.32214 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 252cdddc-17c7-388c-99ef-e419cea37bbe | -4.74761 | -49.09819 | 2024-11-23 05:12:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca52631a-367b-347c-9152-e2eb5ca8cfed | -5.56583 | -46.29303 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b544e5f-3908-3900-bcbd-2fa3a08e9365 | -3.28879 | -53.85232 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55dac232-943a-33a9-851d-d69d2fce0dab | -2.73253 | -54.38807 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e3d44cf-ebae-3997-a9c6-42303dee690a | -4.45018 | -48.19889 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b9bae67f-042d-3819-bccd-85ad59e566a5 | -2.86638 | -53.96616 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README61.md)
