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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5938b1f5-3511-3ff9-b6a1-584e88c0fcef | -8.9449 | -46.9582 | 2026-06-16 16:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 2ec85389-6ba8-3ef0-a006-63bf5bb92d6e | -8.8695 | -46.966 | 2026-06-16 16:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| d603be1e-59aa-364d-aaa3-5d187aff2b7d | -12.1114 | -51.9944 | 2026-06-16 16:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 04021d15-c9f8-3778-832c-fe12c71e990c | -8.9641 | -46.934 | 2026-06-16 16:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 4ad64e69-be88-384a-b710-506c6fa657ae | -7.375 | -49.8558 | 2026-06-16 16:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c8ddc4f1-e96b-32ac-a525-6fa0db29f71c | -11.5933 | -55.33 | 2026-06-16 17:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 333f1efb-85e9-387b-beb3-a5393d1f79c3 | -7.7724 | -47.5773 | 2026-06-16 17:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e09b8cb3-ae24-33e4-b7f8-944642969c51 | -7.0617 | -47.5046 | 2026-06-16 17:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 60d7e6f2-02d7-3d8f-9648-c82319374ff9 | -8.9446 | -46.9805 | 2026-06-16 17:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c5dde1a0-ef00-3ee0-a323-fb182438858a | -7.043 | -47.506 | 2026-06-16 17:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| b31d568c-3715-3c9a-809a-8a106907e34c | -12.9175 | -54.2202 | 2026-06-16 17:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 2b98ef36-4b38-3efd-a69b-2b8023e17b17 | -8.8222 | -44.8043 | 2026-06-16 17:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b6dee388-1fee-362a-a9bd-347a1526ebb0 | -8.8695 | -46.966 | 2026-06-16 17:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 12616022-3be9-3db5-8217-42d149d13924 | -8.9641 | -46.934 | 2026-06-16 17:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| e72e9251-d316-3280-bca1-03c0bfde1230 | -9.3662 | -46.4895 | 2026-06-16 17:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c2fff380-2634-3024-b402-a1bee4c429a9 | -8.9449 | -46.9582 | 2026-06-16 17:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 51944b9b-70fe-3990-b828-725262bcc8e6 | -7.375 | -49.8558 | 2026-06-16 17:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 211.1 |
| 1433db21-a3f3-3e77-ad79-32b09d4056f7 | -11.3606 | -51.3797 | 2026-06-16 17:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 6d7f4cd5-b1fb-3e98-b35d-07e4218aa02d | -8.9446 | -46.9805 | 2026-06-16 17:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 998e63ff-e129-3024-9cd5-502421c30299 | -11.5933 | -55.33 | 2026-06-16 17:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 41f70851-360f-34b5-96db-74c1d1a57101 | -12.1114 | -51.9944 | 2026-06-16 17:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c7b7bb07-3acd-3ef0-9054-9fc01a8e38d4 | -8.8695 | -46.966 | 2026-06-16 17:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 96a3c90c-45fb-3aef-965c-8a6f2dfe7743 | -7.7724 | -47.5773 | 2026-06-16 17:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| cd60b290-0ab2-3298-a158-fdd060c9c555 | -6.1754 | -48.5045 | 2026-06-16 17:10:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 6ded863c-728a-30c0-98d7-2e42b2546d1f | -13.962 | -46.0104 | 2026-06-16 17:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 7edffa46-50c7-30f2-ae21-14b355aa1703 | -13.9421 | -46.0367 | 2026-06-16 17:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 80a2ca9b-9d40-30cd-8769-5f86d9712efd | -11.3606 | -51.3797 | 2026-06-16 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 90d1a601-1bfc-3e5f-ad3c-15382828795b | -7.375 | -49.8558 | 2026-06-16 17:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 208.6 |
| 1911cb63-fbb0-3c14-a454-0586b310da0c | -8.8222 | -44.8043 | 2026-06-16 17:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 3c7557fe-3921-346c-9bf0-f8116b0800d2 | -7.7724 | -47.5773 | 2026-06-16 17:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f788e607-7d6b-3b32-a4e3-70cf8b7abc2e | -12.9175 | -54.2202 | 2026-06-16 17:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 6c81225f-9cd0-3b57-80b6-ce77e87de557 | -8.8695 | -46.966 | 2026-06-16 17:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 6274dc21-be71-356a-84fe-97f0ddd35226 | -8.9449 | -46.9582 | 2026-06-16 17:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 430e3f16-a907-36af-ae65-cdf3653e681a | -8.9641 | -46.934 | 2026-06-16 17:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 77744bcb-1b2d-3832-b3df-15a6bbf6ed6a | -7.3748 | -49.8771 | 2026-06-16 17:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 30234540-37c4-31c7-bd19-1fda7a4f6aeb | -7.375 | -49.8558 | 2026-06-16 17:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 224.7 |
| 13ec62ed-d158-3898-bef1-2f2df0c4df2d | -12.9175 | -54.2202 | 2026-06-16 17:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 5d7d3613-4cfb-3379-bef2-ecc1c4bd1a34 | -7.3563 | -49.8572 | 2026-06-16 17:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d42e2215-4838-326b-910d-eed8fe6d10c3 | -11.3606 | -51.3797 | 2026-06-16 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 35c50f40-051e-3809-b2c2-bc7d9e85ee82 | -5.813 | -45.0799 | 2026-06-16 17:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 198.0 |
| ef901324-5a78-3191-9903-adedf0d9cc56 | -8.9638 | -46.9563 | 2026-06-16 17:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 218.5 |
| c10be5da-f42e-38cc-a576-c4faaa58e967 | -7.7724 | -47.5773 | 2026-06-16 17:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 290518bf-f061-3dc2-a4e8-702cfba24b14 | -8.9641 | -46.934 | 2026-06-16 17:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 838e1369-3e1b-3e1e-b7f7-eb7c23aae475 | -9.6989 | -47.0332 | 2026-06-16 17:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| b59ff5bc-50dd-33e4-a7c3-0e9f20ce6f11 | -7.375 | -49.8558 | 2026-06-16 17:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 186.5 |
| a32fb4c1-dd5d-306e-811a-bef4c72f5091 | -12.9175 | -54.2202 | 2026-06-16 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 1416e4b6-eb72-332e-a4f8-8b3f15f955f1 | -11.1954 | -49.6679 | 2026-06-16 17:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 4d51297d-ca4e-308e-aec6-664650941ff8 | -8.9638 | -46.9563 | 2026-06-16 17:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 277.3 |
| dcdfba97-a6ef-3ec9-b067-16db75384d3a | -8.8695 | -46.966 | 2026-06-16 17:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 7f31ec0d-2d66-3d33-8dde-bba3fb8fdda1 | -11.195 | -49.6895 | 2026-06-16 17:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 46706d17-d6b5-3936-a138-814ef14bce52 | -11.5933 | -55.33 | 2026-06-16 17:40:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 37e9b4f3-3ea3-3c36-907c-0aeb92bd07ad | -11.3606 | -51.3797 | 2026-06-16 17:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |


