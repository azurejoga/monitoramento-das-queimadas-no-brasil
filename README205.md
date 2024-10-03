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

## Dados Diários - Página 205

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 999821cf-332f-383c-9fa7-8cdd2bfda695 | -16.6688 | -57.374 | 2024-10-03 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 9606ed7f-1aa6-3053-877c-0407e2b2e0b6 | -17.197 | -57.3741 | 2024-10-03 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 2d863c8d-f4c8-315a-b924-0094e53c93b3 | -17.1967 | -57.3946 | 2024-10-03 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.1 |
| fbbed4c9-e2b2-3d60-aa46-eba58f0d77f1 | -17.1771 | -57.3969 | 2024-10-03 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 247.4 |
| 31417fd9-f0fd-3d13-b5f0-4732fb8dc9b3 | -17.1574 | -57.3993 | 2024-10-03 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| 0a4c0b86-777e-3ff9-b6f2-63c985a8c0a2 | -17.1774 | -57.3764 | 2024-10-03 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 203.5 |
| 307cdbb4-1f92-3e10-bcb2-71f6ff444367 | -17.1577 | -57.3787 | 2024-10-03 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| fd7fb6a3-f481-36d5-84c6-d05edd338edb | -19.0344 | -43.1944 | 2024-10-03 07:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 165.5 |
| 03b52a0b-2929-3529-b408-e01b561a1632 | -22.3711 | -47.9225 | 2024-10-03 07:47:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 6811f314-35f5-3e18-9d20-199dbe99e06e | -22.3719 | -47.8987 | 2024-10-03 07:47:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 86885c82-8943-3e08-a8a9-3fc5ecd7b176 | -22.3921 | -47.9172 | 2024-10-03 07:47:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 46c6fbe3-ac91-3d01-9ccc-c6cb442f056d | -22.3928 | -47.8934 | 2024-10-03 07:47:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 1050beba-11a6-3e57-89be-2cc4ae041ac4 | -22.3935 | -47.8696 | 2024-10-03 07:47:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 69955810-338a-3c16-8383-aa14e7543259 | -22.4137 | -47.8881 | 2024-10-03 07:47:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 85.7 |
| c2206ce4-5b19-3636-9d5b-f33d084a72a8 | -8.9976 | -67.4094 | 2024-10-03 07:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| ebd6bd07-59c7-36d4-90c4-abf3c13b1070 | -12.4228 | -62.9807 | 2024-10-03 07:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 232.5 |
| 704c0b13-69aa-3efa-bf65-c6036e67fdc8 | -12.4227 | -62.9999 | 2024-10-03 07:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 394.4 |
| e9c1b27f-6141-3500-9e95-bbc6a6489807 | -12.404 | -62.9817 | 2024-10-03 07:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 114.0 |
| d4960b2c-2c29-3c15-8ef2-a2e6c8b5558b | -12.4038 | -63.0009 | 2024-10-03 07:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 181.0 |
| 7ffd2d10-6a8e-3364-90a1-d8e47359aa4b | -12.9741 | -62.6409 | 2024-10-03 07:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e5fdc93c-0301-3dda-b276-ca6554702f03 | -13.0594 | -51.1409 | 2024-10-03 07:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| face0664-ebe1-30fb-8688-fa2752aee267 | -13.0591 | -51.1623 | 2024-10-03 07:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 846a5e2e-3ec2-3a4e-a9c8-7456edede2ed | -13.0402 | -51.1432 | 2024-10-03 07:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| d87ceeeb-9a46-30ac-8010-982ba48b27a0 | -12.8991 | -62.5491 | 2024-10-03 07:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 4d6b8869-6898-3ce4-b6f6-93c7c5b0697b | -16.6919 | -57.1465 | 2024-10-03 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 1fb40b13-960a-31a7-b534-953b699ac5c6 | -16.6893 | -57.3104 | 2024-10-03 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 72230957-3e3b-3758-92ff-29fbac9cea87 | -16.6723 | -57.1488 | 2024-10-03 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| aa8ff2cf-e031-304d-9eb9-6b11f64e83c1 | -16.6698 | -57.3126 | 2024-10-03 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.0 |
| 554440b8-b201-36a2-b31f-fb735660cb7d | -16.6694 | -57.3331 | 2024-10-03 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 72e0a52e-7964-39f7-b74f-d0224b1e60bb | -17.197 | -57.3741 | 2024-10-03 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.3 |
| 62dfe462-5513-3237-a6d6-e3d9f8b25a3c | -17.1967 | -57.3946 | 2024-10-03 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 179fc46e-b1f0-3ab1-8f44-194a58046dca | -17.1774 | -57.3764 | 2024-10-03 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 206.0 |
| bbe1a036-2e3c-384e-ba60-6854cae1539b | -17.1771 | -57.3969 | 2024-10-03 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 248.2 |
| c821031e-6a99-3644-8c05-022a8c5fc442 | -17.1577 | -57.3787 | 2024-10-03 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| c5282eed-be4f-3273-8ffb-d2901f7f240b | -17.1574 | -57.3993 | 2024-10-03 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.8 |
| 3c3a45d4-88b3-3f61-9555-66cf586bf77f | -18.5386 | -42.231 | 2024-10-03 07:56:48 | GOES-16 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| c021b619-8961-3e0b-ad48-51f3718844b0 | -18.5379 | -42.2562 | 2024-10-03 07:56:48 | GOES-16 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| efc13a71-9d78-3c0b-b149-f153c453306c | -19.0344 | -43.1944 | 2024-10-03 07:56:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.7 |
| 0f2b3ff1-7d52-3cee-9067-2b492ff5838c | -22.4137 | -47.8881 | 2024-10-03 07:57:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 67aec01c-e663-305d-8633-ed0f0fc5c1e7 | -22.3928 | -47.8934 | 2024-10-03 07:57:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 8fb43028-d1b3-33e0-8399-b639fb9d867e | -22.3921 | -47.9172 | 2024-10-03 07:57:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 170.0 |
| c4499e63-c50f-3291-89bc-4269a83005ab | -22.3719 | -47.8987 | 2024-10-03 07:57:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e7097645-a85d-31fb-a05a-fb4c16ea0fa2 | -22.3711 | -47.9225 | 2024-10-03 07:57:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 93.7 |
| fa4cb7bf-8496-3a06-8c70-fd60b4ff17e0 | -12.4228 | -62.9807 | 2024-10-03 08:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 204.6 |
| fc93d3d6-ffbb-30e3-b75f-78560109e42c | -12.4227 | -62.9999 | 2024-10-03 08:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 313.0 |
| bed9ed2c-d3ac-3300-bbc3-01323e663430 | -12.404 | -62.9817 | 2024-10-03 08:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 5d0e6a64-5ca2-3c92-8d8d-85411f4e36a5 | -12.4038 | -63.0009 | 2024-10-03 08:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 262.3 |
| 21bf7b95-8b56-3d74-92b0-f64734db91c3 | -12.9741 | -62.6409 | 2024-10-03 08:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fc4a129c-d6d2-34d3-a542-7b4dc148500e | -13.0594 | -51.1409 | 2024-10-03 08:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 0828259e-b24d-396b-91a6-fe734db88c73 | -12.8999 | -62.4527 | 2024-10-03 08:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 6bcbad7d-f383-38b5-aa0a-cb64b7fce131 | -12.8998 | -62.472 | 2024-10-03 08:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 94dd7efe-4870-3a11-90f6-9c65a805cff2 | -12.8996 | -62.4913 | 2024-10-03 08:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 12dc9e70-eb5a-35aa-a1e5-130cc934e918 | -16.1098 | -50.427 | 2024-10-03 08:06:36 | GOES-16 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d84591eb-3400-34d8-8b77-1be07fe99e85 | -16.1094 | -50.4489 | 2024-10-03 08:06:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 85352341-efd2-317b-9bc0-332e169e275a | -16.5393 | -58.2022 | 2024-10-03 08:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| a25bcc07-ff38-37ff-899a-067a12c050a3 | -16.539 | -58.2225 | 2024-10-03 08:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.3 |
| 2e7221d6-d7e2-3b36-a071-c4e28845ef1c | -16.5387 | -58.2427 | 2024-10-03 08:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 11f6a658-c3b2-399a-9c23-7bc49bc48d0f | -16.5582 | -58.2407 | 2024-10-03 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| b1040126-ee7b-3567-8524-d3d5d2b5cbf8 | -16.5585 | -58.2204 | 2024-10-03 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 0d7f02a8-79a8-3943-ad83-1682f828b480 | -16.5588 | -58.2001 | 2024-10-03 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.5 |
| 987918b1-17a6-3f00-80fb-fcb2f7c01f6c | -16.6868 | -57.4741 | 2024-10-03 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 270365b1-dbc0-399a-97f1-408e1145060c | -16.6723 | -57.1488 | 2024-10-03 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| e471ed2e-0301-3760-bb8d-c3dee316d013 | -16.6698 | -57.3126 | 2024-10-03 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.1 |
| 442c9f2f-0727-366b-9409-c80449ad192c | -16.672 | -57.1693 | 2024-10-03 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 3aab08f2-4741-3ba1-aeb3-3a29085886eb | -16.6893 | -57.3104 | 2024-10-03 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 14736fea-da9c-3a7a-a4d5-b9f5590129e8 | -16.6919 | -57.1465 | 2024-10-03 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 7f8cecb8-e4de-35c1-945d-3570cf9fc2e2 | -17.0502 | -56.7551 | 2024-10-03 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 5df8c365-8c59-3234-92bf-9765b36de398 | -17.0306 | -56.7575 | 2024-10-03 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| a092db36-4c88-3303-ab8d-0839b371314a | -17.0309 | -56.7368 | 2024-10-03 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| c6e9c19f-9efa-3d79-8b5c-02154d7a5173 | -17.197 | -57.3741 | 2024-10-03 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 9a7e27a9-6a46-3dc0-acfa-3c84be775251 | -17.1574 | -57.3993 | 2024-10-03 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| fcf6c489-cba9-3a0e-9f08-aa0d85083185 | -17.1577 | -57.3787 | 2024-10-03 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 9a875ec8-4fd9-3ec5-8408-edfa0093cd9d | -17.1771 | -57.3969 | 2024-10-03 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 328.6 |
| 1891fbea-5e30-38dc-8e47-d578b78c1bdf | -17.1774 | -57.3764 | 2024-10-03 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 228.2 |
| f335fbd6-401a-3682-9985-d10f2ed6d83c | -17.1967 | -57.3946 | 2024-10-03 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 9ca0100e-28c5-3095-9c02-02effe99800e | -22.3928 | -47.8934 | 2024-10-03 08:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 823e8776-1b4b-3fa0-bd3a-e6b63ef8e6e4 | -22.3921 | -47.9172 | 2024-10-03 08:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 47aa04f5-7e6a-320e-8c0b-182e6eafbd2a | -12.4038 | -63.0009 | 2024-10-03 08:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 1c77465f-b74e-35b1-9d2f-9eb825abf56f | -12.404 | -62.9817 | 2024-10-03 08:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 6c8ab682-a26e-371d-b93a-4d0e47bd0284 | -12.4227 | -62.9999 | 2024-10-03 08:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 360.0 |
| a57b2a29-0372-301f-979f-b7b63439a33f | -12.4228 | -62.9807 | 2024-10-03 08:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 2775ebc9-3a19-3582-b581-89918d80c93b | -12.4416 | -62.9988 | 2024-10-03 08:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 0c112f2c-904a-39ee-9d75-8abf12a3c308 | -12.8996 | -62.4913 | 2024-10-03 08:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| b923e743-39b9-325a-9317-a615f757be0f | -12.8998 | -62.472 | 2024-10-03 08:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 98.4 |
| c987a1bb-0949-392a-90aa-f19d3538b186 | -12.8999 | -62.4527 | 2024-10-03 08:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 55babf8e-391d-38a4-b55a-1dea8077cda5 | -16.1094 | -50.4489 | 2024-10-03 08:16:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| dbf9fbd4-6481-3d57-b336-46c8fa09c280 | -16.1098 | -50.427 | 2024-10-03 08:16:36 | GOES-16 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| f0385679-904b-3713-9065-5f1f882bdbd2 | -16.5512 | -57.4078 | 2024-10-03 08:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.2 |
| 81e33a98-417e-3275-939f-69288ba942bc | -16.5733 | -57.2419 | 2024-10-03 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 0e4c4d1d-624f-3457-8927-93e9ab024f77 | -16.5925 | -57.2602 | 2024-10-03 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 6a949f34-e731-35e0-b96a-cf8c17624876 | -16.5928 | -57.2397 | 2024-10-03 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 288.8 |
| 33b37b5b-a4d2-3a18-bd77-dd24411035ed | -16.5931 | -57.2192 | 2024-10-03 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 7f4c538e-f390-3ac1-865b-c44554097f87 | -16.6124 | -57.2375 | 2024-10-03 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 3d199601-90d0-3dd5-bab6-d8f72c737979 | -16.6127 | -57.217 | 2024-10-03 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| 9b7b0f76-7659-3013-bc50-01e11a5b5911 | -16.6698 | -57.3126 | 2024-10-03 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| e22d0e4c-3254-3265-a2c9-2efaa9620277 | -16.6723 | -57.1488 | 2024-10-03 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 2b4af7fc-9f3e-3208-ab03-f2234c783078 | -16.6868 | -57.4741 | 2024-10-03 08:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 76d94ae4-3302-30cb-80fe-884060c8bc44 | -16.6893 | -57.3104 | 2024-10-03 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| cad7f4cf-359e-3b86-a03a-070d249c362f | -16.6919 | -57.1465 | 2024-10-03 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 7b0af8d7-1c32-351d-8b2d-20f58101c008 | -17.0502 | -56.7551 | 2024-10-03 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |


[Clique aqui para ver as próximas entradas](README206.md)
