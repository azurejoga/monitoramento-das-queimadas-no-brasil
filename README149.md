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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2479457-c04f-37a1-934f-b9086211edfc | -14.8021 | -45.7946 | 2025-10-01 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| b064a6f2-dfe7-38a4-a7b8-619bdef89d86 | -8.672 | -47.7144 | 2025-10-01 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 7f63d840-a5c8-342e-b93c-8fb9f67a2a36 | -13.6703 | -48.07 | 2025-10-01 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 454a1147-c6cc-390d-a4b7-c28ffad9aa2f | -8.5081 | -47.2676 | 2025-10-01 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| d6213fd4-4a0e-324b-8581-c93a4ed11d2e | -12.763 | -50.5352 | 2025-10-01 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 42adda52-6ba5-33ee-85f7-f1e852664be1 | -12.8831 | -46.9101 | 2025-10-01 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 3b5bd913-7103-3455-aabf-563c44a4809a | -10.3441 | -48.2419 | 2025-10-01 12:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 7911d8e1-45d2-3220-9635-d726b944cac9 | -15.9381 | -43.3223 | 2025-10-01 12:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 140.8 |
| d4e58ec3-244c-3f4d-9331-4c0776bbdfff | -13.3203 | -47.2048 | 2025-10-01 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c61970cf-5aa1-315a-9d86-161d4f347c26 | -14.0597 | -45.0444 | 2025-10-01 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| f3dd7103-8c60-3333-8b24-afe06361b2de | -8.483 | -47.7983 | 2025-10-01 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6bae8d19-93fb-315c-b0be-571533559eb7 | -8.5407 | -44.6745 | 2025-10-01 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6933f6f4-bba2-385c-ad10-f96f103a9c4b | -14.0402 | -45.0479 | 2025-10-01 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 6811381d-c33c-39cd-a5dd-66a0a4f94bb1 | -10.9579 | -46.5467 | 2025-10-01 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 223b2a63-8736-3a09-95f4-34b174f5f236 | -7.8002 | -46.7578 | 2025-10-01 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 0507d188-1ec6-3e03-9468-cbc0dcf79f2e | -12.7022 | -45.2715 | 2025-10-01 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| bdc93c25-5ec5-3ecf-9abf-e2a2d8d79109 | -14.4943 | -48.4553 | 2025-10-01 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 69d5d235-7d90-3898-93f7-a09958595468 | -11.8618 | -45.0307 | 2025-10-01 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 6da09c0d-5b34-3571-affd-5338996e8615 | -14.3514 | -45.9437 | 2025-10-01 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 6a77318d-84eb-3e1d-a796-a0a9ce59659a | -7.5561 | -46.7795 | 2025-10-01 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 0f8f68dd-8c72-3e05-ab5f-842b294ea128 | -8.8609 | -47.6521 | 2025-10-01 12:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| ddfd5cf0-e29b-3e9a-ab47-92c0e224c3d8 | -14.3519 | -45.9206 | 2025-10-01 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 121.5 |
| e6a48986-abd6-3d7a-82d8-d33c4052fc26 | -10.9769 | -46.5443 | 2025-10-01 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 06736f28-2a2b-3024-aa2a-298c547d3174 | -8.5018 | -47.7965 | 2025-10-01 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 1cfa89d7-d472-3f10-b2c6-f173b950ca64 | -15.5031 | -45.8969 | 2025-10-01 12:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 1fda227f-ef18-3910-9daf-3f12c1f2dc0c | -14.4947 | -48.4329 | 2025-10-01 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| c2d203bd-f2c3-312d-bc91-86b1aaabb9cd | -12.7627 | -50.5567 | 2025-10-01 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 274.4 |
| 56e580a4-ae6c-31d2-ba4d-9303ab795a70 | -14.9733 | -46.8896 | 2025-10-01 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| abceeafb-2e0c-34b7-91f5-7b91bafc6591 | -8.5079 | -47.2897 | 2025-10-01 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 163.0 |
| d81cd202-2d5e-37aa-980e-71dadda0f554 | -8.5587 | -44.7414 | 2025-10-01 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| dbd7a650-6031-3be9-8533-9e7207d1a0fe | -10.1084 | -50.299 | 2025-10-01 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 8f7af641-126a-34e8-84b3-de7353e48c5a | -10.1081 | -50.3203 | 2025-10-01 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 6dd1ee32-7600-3ebd-933c-84210909f4b0 | -8.5081 | -47.2676 | 2025-10-01 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| d757f215-af4a-3433-884a-963d94f2540e | -11.9411 | -47.0675 | 2025-10-01 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| b6cb7a8f-e6fc-36de-ab23-f75ffbc6eb80 | -8.5773 | -44.7623 | 2025-10-01 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 07abd3f8-2bbc-3389-a884-f14aa18cf01e | -15.9388 | -43.2979 | 2025-10-01 12:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 373.5 |
| ec43cc28-9be0-3cd1-bc4d-42aeae5b3879 | -12.7002 | -48.5637 | 2025-10-01 12:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4563e868-4501-340f-ac0d-a389c57b6ccc | -14.4938 | -48.4776 | 2025-10-01 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 5e687db3-bd54-3239-ab99-a18a33d51837 | -11.4596 | -45.0433 | 2025-10-01 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 290f603c-fa52-3564-bf9c-2cf95a11b418 | -8.5867 | -45.4914 | 2025-10-01 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| b667b6f4-013d-3734-8441-c9d94b809d19 | -12.7022 | -45.2715 | 2025-10-01 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 81486f2f-d450-33b8-86b0-b9067b6e38bd | -10.8421 | -46.6514 | 2025-10-01 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ef304b9e-cf34-3278-ad05-95a22309422c | -7.8882 | -47.281 | 2025-10-01 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 7628dc4f-bacb-35fa-83b3-399aa6b1b5ec | -7.5749 | -46.7778 | 2025-10-01 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 254.6 |
| a75a54ce-abb7-34c5-874f-06e62cd4c165 | -8.8926 | -46.6296 | 2025-10-01 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b9122fcd-0df5-37fb-8231-1149377f4e52 | -8.8609 | -47.6521 | 2025-10-01 12:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 773237ba-059a-31ec-baf8-da8637df686e | -11.4405 | -45.0461 | 2025-10-01 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 0d4578e2-c67d-339c-b68d-bb99096e3fb2 | -9.1248 | -47.6256 | 2025-10-01 12:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| ed98b686-512b-3d0f-81e1-19f105b452e2 | -9.4115 | -47.3308 | 2025-10-01 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 35601d65-0f66-35b5-8de0-568013d60334 | -9.4644 | -47.6124 | 2025-10-01 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 91be5221-0a03-3db3-a709-0cb9c3d88aac | -8.672 | -47.7144 | 2025-10-01 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 694b3119-c5fc-3868-910b-629f647cc8f0 | -8.8797 | -47.6502 | 2025-10-01 12:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 57676279-b4aa-3dc1-a609-06abb7ac4678 | -11.4409 | -45.0229 | 2025-10-01 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 919505f3-5104-3729-b98d-5759d73bd209 | -14.3519 | -45.9206 | 2025-10-01 12:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 3d133bf1-1132-32ac-981d-a00c0044e1f3 | -11.8622 | -45.0075 | 2025-10-01 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 530c3214-bea2-3591-827a-3b7f72344d9a | -11.8626 | -44.9844 | 2025-10-01 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| b64f01e2-b31f-3449-8d78-871d015335c1 | -8.6722 | -47.6924 | 2025-10-01 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 9db27ba5-58bf-36cc-a23d-2a85ef6eae9d | -9.8201 | -47.8386 | 2025-10-01 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| a4c59d0e-a493-3aa4-961e-276961a689d4 | -17.385 | -47.1471 | 2025-10-01 12:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| d44d3c84-840b-397e-889b-c639336d8b12 | -8.5404 | -44.6975 | 2025-10-01 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 9c452b7e-f572-3377-82f8-f6479e3251e0 | -11.829 | -48.0619 | 2025-10-01 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 7a8c4a60-5bb5-3146-8f69-b93ffd3ee10b | -14.9738 | -46.8668 | 2025-10-01 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 8d6dee7d-b0d2-3786-8f9c-3a3843c1ba82 | -11.46 | -45.0202 | 2025-10-01 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 61200d7e-96a4-39bc-891e-59aa8e590736 | -14.4943 | -48.4553 | 2025-10-01 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| d99b1585-725e-3990-a344-cdbf9cb9cf76 | -14.1926 | -46.1091 | 2025-10-01 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 1f4e63cb-0cba-34a8-b48d-8cc3005a8a82 | -8.5407 | -44.6745 | 2025-10-01 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 93e3c314-2dc1-30ce-9119-fae5845fbd0a | -11.8482 | -48.0595 | 2025-10-01 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 08760f86-cb3f-3e02-a0b1-8771bf93390e | -11.8618 | -45.0307 | 2025-10-01 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 038685f2-d872-3eb5-af80-03b012ba5b80 | -7.5561 | -46.7795 | 2025-10-01 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 4ecd5262-bd1a-39f5-b764-9474aa6e31e5 | -15.9381 | -43.3223 | 2025-10-01 12:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 251.8 |
| 6ddd71f3-3841-3f75-bc56-d67c9dcec907 | -7.5751 | -46.7556 | 2025-10-01 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9f7aba79-081d-3f5b-8835-08913d8d5a2c | -14.3514 | -45.9437 | 2025-10-01 12:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 211.4 |
| f9f87ea5-dbd5-37ab-9fe8-06ffa70e8ade | -15.5031 | -45.8969 | 2025-10-01 12:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 51cbadbd-b7c8-37fa-9fdb-c1ec533b91cb | -11.7797 | -47.5806 | 2025-10-01 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| e1a4c9f1-f46f-3c9c-8b3b-24ca76524d3e | -11.4596 | -45.0433 | 2025-10-01 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 369.3 |
| e1a77ad6-5b11-306d-8284-2aa6de843c51 | -15.2742 | -49.2852 | 2025-10-01 12:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 1c59de89-e547-3f81-91e3-44e33a1b0584 | -8.9188 | -46.0664 | 2025-10-01 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 4640eefe-9634-3a5f-9b1c-1bbd93003f90 | -13.0307 | -45.2189 | 2025-10-01 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| b6fe4528-db5a-35c9-a3a1-ef9c84576cef | -14.9738 | -46.8668 | 2025-10-01 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 0cfb2f8f-6a4e-3bb7-8217-728d46fd22ab | -12.7819 | -50.5543 | 2025-10-01 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 294.9 |
| 3fc660bc-2b66-3872-a5c7-2dd9d4a0a860 | -14.5137 | -48.4522 | 2025-10-01 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 0f46d85e-6952-3019-967f-a1683c6ae3f3 | -15.9388 | -43.2979 | 2025-10-01 12:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 505.4 |
| b274c207-2e3b-3dba-a4a4-78736c0e505e | -15.9381 | -43.3223 | 2025-10-01 12:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 636.9 |
| 7df53446-3c08-3775-a348-2314a39bcc09 | -13.2969 | -50.6821 | 2025-10-01 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| bc54856d-1721-38a5-b545-cab755df1796 | -8.8609 | -47.6521 | 2025-10-01 12:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 6b99b7ed-7d57-3ef3-8021-f71c72e511c8 | -9.9189 | -43.6743 | 2025-10-01 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 954029dc-30d9-3475-83d9-b9a7635094c6 | -11.46 | -45.0202 | 2025-10-01 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 9569a8e6-d9ce-3cbf-a059-20bdadb6155a | -8.8929 | -46.6072 | 2025-10-01 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| c716b24f-0960-372e-8d84-faa2937038a9 | -13.3203 | -47.2048 | 2025-10-01 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| eeac4402-1664-3ae8-94bb-cf980d3a9923 | -8.8926 | -46.6296 | 2025-10-01 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 6c97570a-3ecf-3f94-b7dc-87a1a695b648 | -14.5133 | -48.4745 | 2025-10-01 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 45b9927f-de55-379f-9ba5-8cb158c524f5 | -14.4938 | -48.4776 | 2025-10-01 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 7d436ed3-f2bc-3742-bf47-03be84cdc710 | -8.6722 | -47.6924 | 2025-10-01 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| fb1001a7-79df-306d-b4bd-af1b471461ba | -14.9733 | -46.8896 | 2025-10-01 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 946d6f09-71b8-3688-bd7a-9f276550ef92 | -11.8618 | -45.0307 | 2025-10-01 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 1f539f1d-e97a-3f14-bbdb-012d15088f52 | -9.1889 | -48.5166 | 2025-10-01 12:50:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 1ddd11c6-b9ef-3a04-8f4c-6b67fc1702c7 | -8.6908 | -47.7126 | 2025-10-01 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| c2355488-7b2b-37e1-89da-53e18aca14f8 | -11.8622 | -45.0075 | 2025-10-01 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| a4ce3a8e-3c99-38f5-adf8-5655d257dbc1 | -13.0119 | -45.1988 | 2025-10-01 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 182.0 |
| bb4d4fab-c1ee-325f-9d15-1496f36f49e1 | -12.7822 | -50.5328 | 2025-10-01 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |


[Clique aqui para ver as próximas entradas](README150.md)
