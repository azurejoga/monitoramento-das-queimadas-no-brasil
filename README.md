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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdd2d059-32db-3327-b26f-d92930505448 | -11.18 | -39.92 | 2024-10-14 00:04:21 | MSG-03 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1c726eb6-4457-345b-87a8-328a2359a696 | -10.05 | -44.22 | 2024-10-14 00:04:26 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| feb99ec7-906a-3507-a8b8-cf50310f14b8 | -10.08 | -44.22 | 2024-10-14 00:04:26 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ccfd40f-a35c-3b42-9ac5-28e1600f19e1 | -10.01 | -47.32 | 2024-10-14 00:04:28 | MSG-03 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80903178-ec4d-3309-bbc0-e4b306d20c65 | -7.95 | -49.05 | 2024-10-14 00:04:42 | MSG-03 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 91d1bfb1-0f43-30ea-8c1a-3f699fc8cbed | -3.29 | -42.87 | 2024-10-14 00:05:08 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59164479-43d9-3e9e-bcd7-6c5963fca187 | -3.29 | -42.83 | 2024-10-14 00:05:08 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d044b0e9-7aba-3078-92cc-4ad4af7931bc | -3.32 | -42.83 | 2024-10-14 00:05:08 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e60da1de-043e-35e5-bb78-c62e1ae1bfb4 | -2.4344 | -46.9195 | 2024-10-14 00:05:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 41d126a7-172c-38a3-aa50-139df0baeb2e | -2.4529 | -46.919 | 2024-10-14 00:05:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| ccd3eb4d-7a18-3bb7-8163-ad54d5354f5d | -2.6117 | -49.1198 | 2024-10-14 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 4f71d66f-ffa6-3c1c-98e5-20aeaeef11c3 | -2.6118 | -49.0985 | 2024-10-14 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 85c64b56-b9b8-3da0-a1c9-b426ad60038b | -2.6303 | -49.098 | 2024-10-14 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| c98c0d66-45fe-3cc9-abbb-003a9ec1680b | -3.0656 | -51.1883 | 2024-10-14 00:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| adb9d910-f934-3a23-beb3-65587ce5a6ae | -3.084 | -51.1878 | 2024-10-14 00:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f4debaed-72a8-3d78-8b0f-eee86de847f6 | -3.1606 | -50.4766 | 2024-10-14 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| ecbf99f4-c9e2-3f0e-a663-8bc2efbad913 | -3.1607 | -50.4556 | 2024-10-14 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 538a13bb-41a9-3628-9d55-fe186c63b927 | -3.1791 | -50.476 | 2024-10-14 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 01e96fda-04eb-3908-9e83-3edd9c513b85 | -3.1792 | -50.4551 | 2024-10-14 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| f5e84b35-675f-31d0-8163-fd09728c6ad2 | -3.1798 | -50.3083 | 2024-10-14 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| f7415d5e-1dab-3184-80df-9c29c9cb3379 | -3.2889 | -42.8561 | 2024-10-14 00:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 7182d267-87c7-3de8-8c47-1982828d015a | -3.289 | -42.8327 | 2024-10-14 00:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| d526c0bd-a859-3891-a8ad-bb6294145d1e | -3.3076 | -42.8553 | 2024-10-14 00:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 241.7 |
| 7815d75f-f649-3ba4-9f11-a7160f387f65 | -3.3077 | -42.8318 | 2024-10-14 00:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 386.4 |
| d97c4e97-a034-387b-9620-52e7797a4248 | -3.1982 | -50.3077 | 2024-10-14 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 3847c111-553c-3d65-86a0-0534c1cef178 | -3.3274 | -50.3245 | 2024-10-14 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 380aa113-f836-35c0-a629-49980e954d5c | -3.3643 | -50.3233 | 2024-10-14 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 4ea9549b-908b-3ac6-abff-7173e031bc96 | -3.4279 | -52.782 | 2024-10-14 00:05:26 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 71dc3bce-2da5-3ce7-be16-b26ede10d451 | -3.428 | -52.7616 | 2024-10-14 00:05:26 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 53df8dee-f835-33c3-83c7-ca6f68b29487 | -3.8722 | -52.2974 | 2024-10-14 00:05:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 3d3882a2-5338-36fb-8f51-443b8f286843 | -3.8723 | -52.2769 | 2024-10-14 00:05:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b872a74b-6f47-3c21-8c18-47473f78f520 | -3.9103 | -48.3466 | 2024-10-14 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e3a6e4ac-470c-356b-a218-184054f7d4e8 | -4.1145 | -48.2947 | 2024-10-14 00:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 6facb0f2-05a6-3609-8468-78d6c50c4ef6 | -4.1146 | -48.2731 | 2024-10-14 00:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| d37103cb-44db-3414-9df0-da1a2a7bebfa | -4.1149 | -48.2299 | 2024-10-14 00:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 376c5eec-61a4-337c-a76d-adf574dd9d74 | -4.3428 | -50.5172 | 2024-10-14 00:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 77beaadc-725b-363e-8fa6-4057ba4349fb | -4.343 | -50.4962 | 2024-10-14 00:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| dc9ffa27-5e01-3f4f-a3a7-4fa274953d09 | -4.3613 | -50.5164 | 2024-10-14 00:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 260cc65d-cf88-32fa-92bc-67ed4f4ee7f5 | -4.6197 | -44.8626 | 2024-10-14 00:05:32 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| fe04b371-3e97-317c-b846-986136ccbb5f | -4.9097 | -46.0163 | 2024-10-14 00:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1749d90c-22e8-38fe-b815-2758279a1cd1 | -4.9099 | -45.994 | 2024-10-14 00:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 07fabdae-4551-375f-ba5f-69b858392ade | -5.7065 | -57.5243 | 2024-10-14 00:05:39 | GOES-16 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ad13b9db-7ddc-378c-917b-c3f6de78b6ef | -6.1342 | -42.7906 | 2024-10-14 00:05:41 | GOES-16 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| ec9e1867-001e-310a-a315-e0b48d44b92d | -6.3749 | -59.9936 | 2024-10-14 00:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 493315ff-e64b-3108-8344-f43e580654b1 | -6.3933 | -59.9929 | 2024-10-14 00:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a5d9e281-d13c-3400-a303-a57852e07cfd | -7.257 | -44.9623 | 2024-10-14 00:05:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d9ab1683-7b65-3701-a060-e249fa09928a | -7.9437 | -49.0623 | 2024-10-14 00:05:51 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 5659fdd1-66d7-33fc-a325-7a2e7438948a | -7.9623 | -49.0823 | 2024-10-14 00:05:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 55971cb9-9163-3f25-b9ac-df5b775fe887 | -7.9625 | -49.0607 | 2024-10-14 00:05:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 273.4 |
| 53db7bd3-5288-3eef-a086-a681d8ae8b34 | -7.9627 | -49.0392 | 2024-10-14 00:05:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 39e0651c-5edf-3e2d-8755-f283911f08b7 | -7.9418 | -63.6365 | 2024-10-14 00:05:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 563b2d10-e68d-3169-840c-7ab31c1979b0 | -7.9419 | -63.6177 | 2024-10-14 00:05:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 336a7eb9-90b5-35c6-bb21-74742f05e0c8 | -7.9603 | -63.6359 | 2024-10-14 00:05:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| d2b94ba3-d7b4-3dd4-a536-d44cc6fea64c | -7.9604 | -63.6171 | 2024-10-14 00:05:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f4db0944-3a72-3af1-a3fd-4d6652e52e4a | -8.3207 | -42.7394 | 2024-10-14 00:05:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 18bd8e4a-5cc2-38c2-8cff-8a21c670f01f | -8.3396 | -42.7372 | 2024-10-14 00:05:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 7f525a1a-862d-3921-936a-d41d80ec45f5 | -8.5097 | -41.398 | 2024-10-14 00:05:54 | GOES-16 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 70fc3820-9c96-3166-a493-60ab73714705 | -8.4734 | -48.6276 | 2024-10-14 00:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 542e633f-dede-3020-80ba-3271963e68c7 | -8.4921 | -48.6259 | 2024-10-14 00:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 8daef1b8-9023-36d1-a5ed-bfcb85d8253e | -9.1021 | -47.9355 | 2024-10-14 00:05:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 72d76def-bbf9-3a40-86aa-1f8aced059ba | -9.1042 | -61.1811 | 2024-10-14 00:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 35ac3582-8baa-3e31-97e5-0b9c563fcda7 | -9.1043 | -61.162 | 2024-10-14 00:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| e8694bc6-266a-374e-a112-70bbd2711cb6 | -9.6928 | -47.4774 | 2024-10-14 00:06:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 0bdb3ea9-8460-3d8a-b799-3b7e8d8723a6 | -9.7117 | -47.4754 | 2024-10-14 00:06:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 7f72fe0d-9c4d-3725-9f1f-5fc8be10ff7a | -9.7825 | -46.4651 | 2024-10-14 00:06:02 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 69dcf0f1-7188-305b-a781-83f1e8ab3d98 | -10.0622 | -44.2391 | 2024-10-14 00:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 67a2da01-e558-3a45-9f70-9177066704f8 | -10.0626 | -44.2158 | 2024-10-14 00:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 99bd8713-cde2-3dc5-9017-0615e9437580 | -10.0629 | -44.1925 | 2024-10-14 00:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| de6353b0-0b99-33c3-a556-b819cbdb89ff | -10.0813 | -44.2366 | 2024-10-14 00:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 3ee7be2d-049d-3223-8807-cd85c0679498 | -10.0816 | -44.2133 | 2024-10-14 00:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 43f078a0-7215-3bf7-a3eb-9a2dae7fdcc7 | -10.082 | -44.19 | 2024-10-14 00:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| f0c72049-ba0e-3f1d-8d19-aa0973ffc097 | -10.4317 | -44.931 | 2024-10-14 00:06:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3e4c98b8-1d09-3de3-8c74-2cc348166886 | -10.4918 | -42.433 | 2024-10-14 00:06:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 7892e639-e282-3e4d-b357-04ccb6f3b7b8 | -11.17 | -39.9192 | 2024-10-14 00:06:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 835b01df-c734-352b-87c2-b3e61028ee31 | -11.1705 | -39.894 | 2024-10-14 00:06:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 150.9 |
| 13560ca6-63c6-3969-af08-daae8f2b5de0 | -11.1898 | -39.8906 | 2024-10-14 00:06:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 2e0d3fe8-bdd9-30ec-8543-894ad9ac9d3f | -12.0925 | -50.7023 | 2024-10-14 00:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| e23bceb4-7bef-3eff-9d83-4e8c392772d4 | -12.0928 | -50.6809 | 2024-10-14 00:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 49c1ce45-6051-3c65-8797-fc73dc925e57 | -12.4231 | -43.7748 | 2024-10-14 00:06:16 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 586c09ea-7e02-3ca5-9a1a-22ca7e3a5500 | -12.4424 | -43.7716 | 2024-10-14 00:06:16 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 702b0566-c1d5-311c-92ab-154e9f6e0162 | -12.4981 | -63.0148 | 2024-10-14 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 7cc92e88-f796-305d-83c1-9916f5876402 | -12.4983 | -62.9956 | 2024-10-14 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 6f723c8f-09e8-3282-ad00-e15fa9bf4099 | -12.517 | -63.0137 | 2024-10-14 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| da8047a8-c383-3333-8f81-ec5058ac67a5 | -13.0782 | -48.8858 | 2024-10-14 00:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| cc6b8e40-f600-3712-8927-67fe5d1f4199 | -14.55 | -43.127 | 2024-10-14 00:06:27 | GOES-16 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 0a538903-a797-3e9b-8b3f-6e3f02f1a5b2 | -17.0626 | -56.01 | 2024-10-14 00:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 2414644b-df81-3332-b939-3f043d80ec73 | -17.0823 | -56.0076 | 2024-10-14 00:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 768e4bc9-4fc7-3c8b-abc9-2614b0b477a4 | -17.0826 | -55.9868 | 2024-10-14 00:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.2 |
| ddbf5b0a-60b6-3abe-82ae-ccf632f44b4a | -17.1267 | -56.8693 | 2024-10-14 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.2 |
| 748fbe52-f53b-31fe-97ea-5f209e431b2e | -17.1464 | -56.8669 | 2024-10-14 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 82d184d8-a345-3961-b53b-93e9d4ebe91e | -17.6471 | -56.3084 | 2024-10-14 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 83f0bef9-ff51-31ba-8cdb-1fff41ef275f | -17.6474 | -56.2876 | 2024-10-14 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 1bc91bcd-4e55-36d4-92c1-995273b3a2b3 | -17.6668 | -56.3059 | 2024-10-14 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| f6def592-61dc-31da-934a-c4bd2d300daa | -17.6672 | -56.2851 | 2024-10-14 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 25a80223-a5fd-31c9-a33c-238029e9ae81 | -17.6873 | -56.2617 | 2024-10-14 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.0 |
| fe184040-0078-339e-9ffb-51418dcb103c | -17.6876 | -56.2409 | 2024-10-14 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 066bd393-c535-3954-abda-6db89174144f | -17.7074 | -56.2383 | 2024-10-14 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| ab4b43d1-4e0a-3150-a232-68b10c2af83f | -17.7264 | -56.2774 | 2024-10-14 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 5d8fd6ca-9162-30e2-9861-2b152aa8aa6e | -18.2342 | -56.6055 | 2024-10-14 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 4991c250-010e-3e83-b53b-74b5e38b8563 | -18.2346 | -56.5847 | 2024-10-14 00:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.8 |


[Clique aqui para ver as próximas entradas](README2.md)
