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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b77a9aa-fa89-3186-ad37-920469d9115e | -12.2861 | -52.490898 | 2025-05-22 00:28:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be479201-ba66-388c-986e-3b915040bf24 | -8.5988 | -49.516701 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2a9b350-4723-3e34-a99f-b79796fe5dec | -10.0289 | -48.686001 | 2025-05-22 00:28:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3db1ebb6-89de-3698-95c0-666695c566a4 | -12.3468 | -49.968201 | 2025-05-22 00:28:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2c7c844-8938-34db-bc7e-8bc44a757fe8 | -16.3168 | -49.8879 | 2025-05-22 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 6700cb48-63c6-3627-b59e-750cc178adad | -12.3515 | -49.9833 | 2025-05-22 00:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| bf1993e2-5e91-3e42-9616-95a37a0d26cf | -20.9606 | -56.5755 | 2025-05-22 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 38787691-867c-35cf-8555-b4b7a10d3e88 | -11.5532 | -47.4323 | 2025-05-22 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 138ef82f-a523-32d7-bbd2-64fc6abeeac7 | -11.5719 | -47.4521 | 2025-05-22 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 2566ff6c-3bce-37a7-a090-8ddd158d52de | -11.9737 | -44.1526 | 2025-05-22 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| ee2c846c-95c3-39c9-8fa3-b7cf96704446 | -12.2946 | -52.4785 | 2025-05-22 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| e9a5fb88-0c91-327c-bb05-1c1389935fac | -11.5528 | -47.4546 | 2025-05-22 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 36fae021-9994-398f-9967-2cfc56a21749 | -20.9398 | -56.5998 | 2025-05-22 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 1e320e6b-8d75-3fe4-9e9a-dfc228ed7262 | -20.9402 | -56.5786 | 2025-05-22 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 373d3463-36dc-3978-a783-9dc302e98845 | -11.5723 | -47.4298 | 2025-05-22 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| ce074522-951c-3de2-9b01-324e65812f4d | -20.9601 | -56.5967 | 2025-05-22 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 6892b72e-84b4-37f7-95cd-c01ebe37c3b1 | -12.2943 | -52.4995 | 2025-05-22 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 4e0a3da0-4587-3ee0-8c88-9cd04fa65e14 | -11.9737 | -44.1526 | 2025-05-22 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 4c4d306b-8b14-3c57-adbc-af270cf82e6d | -20.9606 | -56.5755 | 2025-05-22 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 1e22d824-1548-349b-a11d-c1d724208e9c | -11.5719 | -47.4521 | 2025-05-22 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 68948787-3d3f-3d9b-b7cf-8e1236d57c5b | -11.5723 | -47.4298 | 2025-05-22 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 40f59653-bdbf-35e0-b2b2-ce42f7569b5a | -11.5532 | -47.4323 | 2025-05-22 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 83d7d21b-923d-37f3-b05a-d645cc01b057 | -20.9601 | -56.5967 | 2025-05-22 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 61191208-d834-300e-800f-269179d14024 | -11.5528 | -47.4546 | 2025-05-22 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| e570b206-1572-349b-a2cd-be0b6db32bd1 | -20.9398 | -56.5998 | 2025-05-22 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 797a1139-643a-31b9-a3a0-cb26dcf1f45f | -20.9402 | -56.5786 | 2025-05-22 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 151.1 |
| ad7cb31d-3f62-3246-8531-4c7b1a94fa0e | -10.8213 | -56.9604 | 2025-05-22 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| cc5c06b8-45d1-3d09-a701-5be7f049eb73 | -12.2943 | -52.4995 | 2025-05-22 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| d44e176a-c922-348a-a801-9c831f05fea4 | -12.2943 | -52.4995 | 2025-05-22 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 51146b96-7420-37d1-aff0-f132faf2b078 | -11.5532 | -47.4323 | 2025-05-22 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| ea11f386-ee7d-32ac-9f8d-9c3521c80841 | -11.9737 | -44.1526 | 2025-05-22 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| fec66e5c-313c-314b-a911-ea24e48ec17f | -11.5528 | -47.4546 | 2025-05-22 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 500b56ac-5aa5-34aa-b47b-d8b35a627aa7 | -12.3515 | -49.9833 | 2025-05-22 00:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 12e0f3ea-3358-3628-b1ca-b9792d57bdae | -10.3237 | -47.0283 | 2025-05-22 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 971eacf2-a324-36ea-b244-7474903a8b95 | -20.9398 | -56.5998 | 2025-05-22 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 120.9 |
| a0b82645-1a0f-3f87-8120-bbd6f298c258 | -11.5719 | -47.4521 | 2025-05-22 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 525733e7-4055-30ab-a326-be9ac436995f | -20.9606 | -56.5755 | 2025-05-22 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 0eb45dda-9f46-3e53-b93d-be86b31d1ef4 | -20.9402 | -56.5786 | 2025-05-22 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 8aba28b8-6a20-3ac7-8b7d-3c3fbc5079bf | -11.5723 | -47.4298 | 2025-05-22 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 8119354f-99ae-329b-aa00-08a70c3a087f | -20.9601 | -56.5967 | 2025-05-22 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 53cbca3e-9194-3f10-94f5-1ca26246e0f7 | -10.324 | -47.0059 | 2025-05-22 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e51cc075-86b1-377f-b247-7dd4882c7c2e | -11.5532 | -47.4323 | 2025-05-22 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5e4fbb46-7055-35cb-a1c7-149992467253 | -11.5528 | -47.4546 | 2025-05-22 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 0ac40e3d-f497-3015-9dc5-831db1f63ccc | -10.3237 | -47.0283 | 2025-05-22 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 0572b961-d0ce-3b87-8b45-b2bf846e4c1f | -11.5719 | -47.4521 | 2025-05-22 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 03aee8b0-4886-3eaa-a3bf-5c486984fd76 | -20.9601 | -56.5967 | 2025-05-22 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 0aa13f77-2c43-3c8b-aa08-ebdd1c4b2d9c | -11.5723 | -47.4298 | 2025-05-22 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 61800200-3260-355a-bdda-40d0cf038f99 | -20.9606 | -56.5755 | 2025-05-22 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 23494802-3252-3cb6-8f2e-51a3e1be5ac9 | -12.3515 | -49.9833 | 2025-05-22 01:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 569aba19-f486-3d2a-a9f6-179fb98f2793 | -10.324 | -47.0059 | 2025-05-22 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| ba73c2b3-b7ba-394c-b2c3-d727521adaf5 | -20.9398 | -56.5998 | 2025-05-22 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 139.8 |
| a6c828da-cd78-37c2-88ba-019a4a43c760 | -20.9402 | -56.5786 | 2025-05-22 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 8ee3ea0e-08a4-3287-a3c4-c2d255d733ee | -12.2943 | -52.4995 | 2025-05-22 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 42991107-3f52-369e-9a2f-7b0e86fee3f4 | -20.9398 | -56.5998 | 2025-05-22 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 5202fd12-a56c-33dc-9136-5fec8a4d6eda | -11.5719 | -47.4521 | 2025-05-22 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c84c32a3-44b2-3632-b164-63da44292cd1 | -20.9606 | -56.5755 | 2025-05-22 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 3be53295-758e-3412-a3a3-89a9652f0413 | -20.9402 | -56.5786 | 2025-05-22 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 122.1 |
| e21cb227-a596-300b-b371-be5599bcf257 | -20.9601 | -56.5967 | 2025-05-22 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 5dbf7f06-084b-3d6f-a449-3c1d64f0d5f6 | -11.5723 | -47.4298 | 2025-05-22 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 1b2ca775-2130-3c7c-b508-b41fa079a93c | -12.2943 | -52.4995 | 2025-05-22 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1c46a0c1-414f-3d8a-a542-9408b3ad9838 | -11.5532 | -47.4323 | 2025-05-22 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| c7bb1fae-4499-377e-9f85-eb03e7902c16 | -12.3515 | -49.9833 | 2025-05-22 01:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 393400ac-e9df-3970-874e-8d5a16ee3624 | -11.5528 | -47.4546 | 2025-05-22 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| e89c8584-a819-37a3-a44c-25cfe31dbd3d | -19.06355 | -53.46491 | 2025-05-22 01:11:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a1d8e2c8-1b9f-3373-b6d2-d82bd866b102 | -20.94633 | -56.58208 | 2025-05-22 01:11:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 76212456-be7b-3077-90b4-a5478fccba42 | -21.48055 | -57.12114 | 2025-05-22 01:11:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 326aa06d-c994-33d9-843f-d20031a031aa | -19.05322 | -53.45683 | 2025-05-22 01:11:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9c5dd34e-9494-3b21-997e-cd6c7b4a9ac6 | -20.94768 | -56.59297 | 2025-05-22 01:11:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 368.5 |
| 817d6a57-d01d-320f-8f01-653e0f8012f8 | -19.06217 | -53.45539 | 2025-05-22 01:11:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 32.5 |
| fabfa1e9-8750-3879-924b-839e2d2deff3 | -19.73747 | -54.51117 | 2025-05-22 01:11:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0e1bc933-42a2-3a42-92b8-634841401a53 | -20.61181 | -48.87194 | 2025-05-22 01:11:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 14d84b8d-6f07-3d83-a4bb-e800b0a1e3a1 | -20.94902 | -56.60385 | 2025-05-22 01:11:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4ccd444e-164b-3a3c-9b81-1f72636d484f | -21.01184 | -55.65029 | 2025-05-22 01:11:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c00f6c83-126e-3119-b13b-f41d3aef0fd4 | -19.11537 | -52.69095 | 2025-05-22 01:11:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e57c8264-da68-3958-b175-67d1014c251d | -12.35074 | -49.9756 | 2025-05-22 01:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 1df91402-c4bb-3139-b2ae-b3b6cf4c99b5 | -14.03121 | -53.3789 | 2025-05-22 01:13:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 9475e6b1-9f72-3439-b127-1af149500271 | -14.17791 | -58.30816 | 2025-05-22 01:13:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9ccffb0a-186e-3311-911c-918bdb1d83d1 | -12.68487 | -58.13076 | 2025-05-22 01:13:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1c6719ca-1e2d-3c5b-9a92-b616ca4d221f | -14.04059 | -53.37741 | 2025-05-22 01:13:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 8b9913fb-f16c-39c2-8b62-80bdc276d169 | -17.61567 | -54.16912 | 2025-05-22 01:13:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e0dd5cad-59bf-391a-8be9-b9b1446f0755 | -14.04861 | -56.06672 | 2025-05-22 01:13:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| abab95da-4fd3-3f3e-ac17-59505f22ef9d | -13.67241 | -53.93953 | 2025-05-22 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 33685612-4432-3926-9a0d-a87188795511 | -14.02097 | -55.13988 | 2025-05-22 01:13:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 4efb14f0-0e00-353b-aab5-2351aed78a00 | -13.78171 | -54.3076 | 2025-05-22 01:13:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 93ff5940-7344-3a72-89a9-29d86dbc9e45 | -14.02982 | -55.13854 | 2025-05-22 01:13:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5ec1062f-c3f6-3bb8-b93e-aee9c01c840e | -12.28755 | -52.50772 | 2025-05-22 01:13:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 6d9034ee-a5fc-3a82-83ad-f42c203c2045 | -13.47365 | -52.28393 | 2025-05-22 01:13:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ddd9f0b0-0e83-36cd-91ab-30916c57d502 | -12.29585 | -52.494 | 2025-05-22 01:13:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 3b13f38d-9694-3bd9-8879-c7a02b84c81a | -12.0773 | -47.34015 | 2025-05-22 01:13:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 0a2823e2-581b-34e6-be2f-7c98a3d91072 | -12.29768 | -52.50609 | 2025-05-22 01:13:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 78c8c98d-117f-3f6a-9d31-c8fbcad251bb | -14.01839 | -55.12165 | 2025-05-22 01:13:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0cb91936-9392-33a5-9c23-e041bac64ec5 | -17.61699 | -54.17846 | 2025-05-22 01:13:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 57c49904-3db0-33f5-8e57-8055c3f7fe0f | -12.33846 | -49.97762 | 2025-05-22 01:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 43c360ca-265e-3579-87a0-76962064efc9 | -13.78308 | -54.3171 | 2025-05-22 01:13:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5aff3a27-d22a-3564-b772-3ad337e10805 | -12.30599 | -52.49235 | 2025-05-22 01:13:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8908585b-a1bd-3969-bb11-53999f31ebe7 | -14.17928 | -58.31897 | 2025-05-22 01:13:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c22a2b79-925d-3713-ab61-37b8286c5714 | -11.60446 | -47.61621 | 2025-05-22 01:13:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 68747631-556e-319e-8e1d-bf59aed43817 | -12.72459 | -54.97304 | 2025-05-22 01:13:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f3e9c3c1-6c9c-337d-80c0-6434995001c7 | -14.03111 | -55.14765 | 2025-05-22 01:13:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4e97e8da-2a6b-3662-ac84-2cdc97e4f792 | -11.86352 | -52.28416 | 2025-05-22 01:13:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README4.md)
