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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0ead0e9-9a14-3989-bc6e-744513053b3b | -3.0949 | -44.3677 | 2024-10-17 14:05:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b002b602-f90b-3bc6-ba75-a8bbdad342b9 | -0.784 | -49.1945 | 2024-10-17 14:15:10 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0d0733ac-dac0-3316-b9ac-3aeeea41c1a8 | -0.7661 | -48.6828 | 2024-10-17 14:15:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a196e8ba-6425-3028-ae10-9bc63830189c | -0.766 | -48.7042 | 2024-10-17 14:15:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 1e221b7b-8e61-3393-b8ea-3854a79bc8e3 | -2.6355 | -47.6347 | 2024-10-17 14:15:21 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| fa22c47f-4a4e-3463-8086-dd6f0e47c2c6 | -2.6303 | -49.0767 | 2024-10-17 14:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 44994833-78c9-301c-9758-5dcdf8b0e76b | -3.0572 | -44.4605 | 2024-10-17 14:15:23 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 82934d5e-d8c2-31f6-a93a-65c0bfdd2670 | -3.0949 | -44.3677 | 2024-10-17 14:15:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| fbe848e9-bcc9-3b31-9f48-d24f6caeb567 | -3.6329 | -41.512 | 2024-10-17 14:15:26 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 2d803136-edcc-382e-853c-aa023e916978 | -3.7007 | -45.9223 | 2024-10-17 14:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 5e2e1412-7a14-3fe5-adc4-640cadb6db82 | -5.1904 | -41.2923 | 2024-10-17 14:15:35 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 338557d3-76ea-3cca-bb43-c117333c0677 | -1.0057 | -48.9583 | 2024-10-17 14:25:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9192d969-c622-3e13-98bf-37d02d5ac7c6 | -1.0607 | -49.1919 | 2024-10-17 14:25:12 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 07de74ae-3969-3419-81e8-cf25a584a2de | -1.3875 | -52.2942 | 2024-10-17 14:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 190.1 |
| 0b84af45-ab8f-3b10-99f3-c79b5be820ec | -1.5262 | -47.2029 | 2024-10-17 14:25:15 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 44e60a13-8770-381d-9061-59dfe345e333 | -1.7479 | -47.3734 | 2024-10-17 14:25:16 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| ccdf50c8-7e8f-3f86-92a0-52b554770e3e | -2.2896 | -45.8838 | 2024-10-17 14:25:19 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6dba0b1b-4b7e-381a-b4c0-326c4e9dadea | -2.4665 | -48.3531 | 2024-10-17 14:25:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a0ca73e3-300a-3ec0-afaa-835d8973ce63 | -2.6355 | -47.6347 | 2024-10-17 14:25:21 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| fe470452-6f30-367a-87ea-0e02ff7cbfcf | -3.0577 | -44.3692 | 2024-10-17 14:25:23 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| be4327aa-388f-3a78-9e98-60d70a5ea04d | -3.0572 | -44.4605 | 2024-10-17 14:25:23 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 65725df4-efe6-362d-aa21-84adcf5cfaa8 | -3.0949 | -44.3677 | 2024-10-17 14:25:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 05d12730-11e2-35fe-aa7a-fd1929d1fefd | -3.7007 | -45.9223 | 2024-10-17 14:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 45ddfc60-a0f6-363d-a19e-9cce63ed6bb9 | -3.7009 | -45.9 | 2024-10-17 14:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 548fbbdd-a48f-3939-ac26-fea64c6d49d4 | -4.2083 | -42.243 | 2024-10-17 14:25:30 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 24700ab3-5ded-3ff8-abf5-492906de3bd2 | -4.5515 | -46.6801 | 2024-10-17 14:25:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 84ed8a12-04fe-3784-a809-3ecccb8eaa04 | -0.766 | -48.7042 | 2024-10-17 14:35:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| c6721193-5fc3-3ce6-a98c-681606788987 | -0.803 | -48.6397 | 2024-10-17 14:35:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 66457f95-951f-348a-9538-ef28a50b1cc6 | -1.0607 | -49.1919 | 2024-10-17 14:35:12 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 91ce2275-f9fb-3d04-a32e-3b14063b0070 | -1.5262 | -47.2029 | 2024-10-17 14:35:15 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 267d4f29-0826-39fe-93b4-9a8204ce32ff | -1.7479 | -47.3734 | 2024-10-17 14:35:16 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 1eaa3ac2-b9b6-3d10-b8d0-458bb6cc6b80 | -2.3828 | -45.7696 | 2024-10-17 14:35:20 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6b856daf-fcfb-344b-8f52-f8fd33480257 | -2.6336 | -48.1545 | 2024-10-17 14:35:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 53a8ece2-40ef-3418-b383-63fb40ea648f | -2.6355 | -47.6347 | 2024-10-17 14:35:21 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 45c2b2ba-d115-3d74-bb3d-e2061d19a61a | -3.0572 | -44.4605 | 2024-10-17 14:35:23 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 65e625a7-6e8e-3cb1-9fca-830a370d7ab4 | -3.0571 | -44.4833 | 2024-10-17 14:35:23 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 5e31d51b-4867-36d8-b2c6-ee97f061d57f | -3.0949 | -44.3677 | 2024-10-17 14:35:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 77cbddba-a3ea-344a-8f1f-dcb5100f161e | -3.6329 | -41.512 | 2024-10-17 14:35:26 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 53622fbf-2a59-3d4d-98c7-6e7a0ec28fd5 | -3.7007 | -45.9223 | 2024-10-17 14:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 118.2 |
| cd840086-581f-3bc0-bbb5-13c80a4c47da | -3.7009 | -45.9 | 2024-10-17 14:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 98e5f049-6588-345b-a231-3d175f79b745 | -3.9669 | -41.9719 | 2024-10-17 14:35:28 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 35618a95-544c-307d-93ec-24f7ae895702 | -4.5515 | -46.6801 | 2024-10-17 14:35:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| cfb380e4-22f8-39be-b314-b5ae80893b4b | -0.7845 | -48.6827 | 2024-10-17 14:45:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 521c14e3-1836-3269-9d4b-2b3d3f518fc4 | -0.7661 | -48.6828 | 2024-10-17 14:45:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 51ac1348-07c2-362b-9a99-12d56e4f9153 | -0.766 | -48.7042 | 2024-10-17 14:45:10 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 3bb5550c-c4d7-3390-af2d-ccab3f987d7e | -0.8583 | -48.7034 | 2024-10-17 14:45:11 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 799f16b0-9bae-374f-8541-8ed60f697482 | -1.0057 | -48.9796 | 2024-10-17 14:45:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 301f6e94-8fcc-3678-8733-30c6545b7b66 | -1.2457 | -48.9128 | 2024-10-17 14:45:13 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 054ac6ed-bd6a-38e5-92b9-38c9006a808d | -1.5262 | -47.2029 | 2024-10-17 14:45:15 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 901ce2df-5923-3bf4-816a-426c07458389 | -2.2711 | -45.862 | 2024-10-17 14:45:19 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 8bc909da-e755-36c2-b01c-14fb38e73aae | -2.2896 | -45.8838 | 2024-10-17 14:45:19 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 4688104f-3487-3c0b-aff2-a3e0333aefbd | -2.3828 | -45.7696 | 2024-10-17 14:45:20 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 59d4536f-e2d0-3aee-8379-d5f4fa017ab5 | -2.4665 | -48.3531 | 2024-10-17 14:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 9e9eddb1-c3a2-3df0-ae32-6338c96bb73e | -2.6355 | -47.6347 | 2024-10-17 14:45:21 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 144.7 |
| c2bf3ce2-fe99-33c4-8cb7-945cb7cb9d56 | -3.0571 | -44.4833 | 2024-10-17 14:45:23 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 93ae063c-aa0f-3a99-b26c-2097ee6a85fc | -3.0572 | -44.4605 | 2024-10-17 14:45:23 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| cfa25c1e-b36f-3360-80d4-1eab9c22e7ff | -3.7007 | -45.9223 | 2024-10-17 14:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 5e2f42aa-dfb6-3ee4-8219-1734389c4e46 | -3.7009 | -45.9 | 2024-10-17 14:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 8af85a95-3d0d-3fe5-9373-f111be4074dd | -4.4084 | -45.7985 | 2024-10-17 14:45:31 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 410e46aa-090c-388e-b71e-a3d3e40edc6e | -4.5515 | -46.6801 | 2024-10-17 14:45:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |


