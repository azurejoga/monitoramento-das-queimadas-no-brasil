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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c844a4d6-b55e-31e2-a031-e51733ef753d | -7.5522 | -45.435 | 2026-09-20 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 208.0 |
| 6fb6e8d0-901d-32fd-9633-c5532ba038ba | -7.5334 | -45.4367 | 2026-09-20 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 2064a649-791b-3f02-a301-f64adaae75bc | -11.8739 | -47.657 | 2026-09-20 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| bad1a15d-f7cd-3640-9201-49f8d2fd0b62 | -11.8679 | -46.8755 | 2026-09-20 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 25be7c96-14d0-37ee-a613-e861a0cf1bb9 | -2.8791 | -57.799 | 2026-09-20 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2fe440c5-a980-346f-b6f2-a1c24cedb68d | -2.8791 | -57.8184 | 2026-09-20 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 9d85bfc3-a82f-35b2-a2b3-26acdd745c55 | -8.1872 | -54.7622 | 2026-09-20 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 298b2bfd-333d-3f9d-b7bb-8bf4a36da75b | -3.3367 | -57.8673 | 2026-09-20 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6eb0bec4-1342-3a5a-89b0-9997dacd4e9b | -11.0991 | -54.0285 | 2026-09-20 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 3dbe5d52-6128-34b6-8b4c-8ed0fd1444af | -5.8408 | -53.5408 | 2026-09-20 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 0ba84043-056e-3324-9fbe-c8b80f81efac | -11.2307 | -54.078 | 2026-09-20 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| d7fda826-4a8f-33f6-8ba0-fea4e6e1f8a7 | -9.7334 | -47.2737 | 2026-09-20 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 36919230-967c-3147-88b2-8de1fe2206f4 | -9.131 | -45.7273 | 2026-09-20 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 986be7f9-ed79-3b44-93d1-d5fa1c8bf15f | -5.8593 | -53.5399 | 2026-09-20 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 79eae9cd-9830-3321-a009-a864da871f22 | -3.7268 | -51.8295 | 2026-09-20 01:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f66ef502-3c78-3841-875b-bcbfd326e756 | -6.2024 | -47.5245 | 2026-09-20 01:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 5b09fecd-12c6-3f95-aca4-fa642780daf1 | -11.2118 | -54.0797 | 2026-09-20 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5e77b199-d019-39ec-a330-c69244b0911c | -13.0177 | -46.9125 | 2026-09-20 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 4d2d171a-0bba-39f3-a5af-4329a238ed0c | -15.2284 | -53.8691 | 2026-09-20 01:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3167aab5-84c2-35a9-b4f3-b7f00d1530b9 | -3.7454 | -51.8082 | 2026-09-20 01:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 7941f83e-b3c8-3585-8f9a-09c7d5d3d02b | -9.2185 | -46.2365 | 2026-09-20 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3e526ce7-d3c9-39ad-8f37-c9b2e729e3b6 | -3.7269 | -51.8088 | 2026-09-20 01:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 403e1084-6040-3a53-8057-e0acd674e6c0 | -5.841 | -53.5205 | 2026-09-20 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| f584810b-2930-3565-a6f3-90b32976351b | -3.7268 | -51.8295 | 2026-09-20 01:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| fcd27300-baa3-3032-b37d-e017272581b7 | -14.6856 | -46.6886 | 2026-09-20 01:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 8541b916-fb72-3e8d-bdbd-05be7d3586ee | -7.5522 | -45.435 | 2026-09-20 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 71129f4c-5c94-3a35-852b-342af3f7a5a5 | -3.3367 | -57.8673 | 2026-09-20 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| af2b0548-03cd-362c-99cb-18485c2a5f61 | -7.5472 | -45.8868 | 2026-09-20 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ba9d2a4f-c760-3a91-9d31-13b86b0e69b6 | -11.0991 | -54.0285 | 2026-09-20 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 834b1d3e-45e0-38b3-9cb2-6bf19b65115a | -12.7629 | -46.1343 | 2026-09-20 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| dd6e137b-de40-3ea5-af70-bbaecf129d1a | -7.5525 | -45.4123 | 2026-09-20 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 003bf906-c4e3-33af-9dab-8f2e8f114772 | -8.1686 | -54.7634 | 2026-09-20 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b84e856c-c971-3f96-8e97-9828a45e9d38 | -7.5284 | -45.8885 | 2026-09-20 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 77ba9e38-a14e-3fb0-88d7-db80792d1dce | -6.2946 | -47.6493 | 2026-09-20 01:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 67add0fb-bcf9-3302-a845-3f8a3771d05f | -6.3136 | -47.6042 | 2026-09-20 01:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 7bc2a8c9-aed6-35a2-b307-fc4ec1b0cecd | -7.5334 | -45.4367 | 2026-09-20 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| e00b1e53-b6bd-3d60-857e-a6dfcd0da335 | -11.118 | -54.0268 | 2026-09-20 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| c8f9c851-1771-378b-94ef-176ef91e5666 | -13.0177 | -46.9125 | 2026-09-20 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 25b05fe6-9428-3eb8-932b-7b2339e8b2d7 | -11.0802 | -54.0302 | 2026-09-20 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4ac09797-7468-380d-b383-7e077c1d3f3a | -3.6946 | -60.6025 | 2026-09-20 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 79f5d076-ae71-3a0d-aeac-e3dc922c2476 | -2.8791 | -57.8184 | 2026-09-20 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6b460aa4-788d-32fd-8482-71a371ea416f | -2.8791 | -57.799 | 2026-09-20 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e548c025-fbb5-3153-8807-b80934d1f4ee | -11.2309 | -54.0575 | 2026-09-20 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5feea3b7-1e12-30ef-a929-5b5191da4f32 | -11.2307 | -54.078 | 2026-09-20 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 682453b0-904b-3905-a2e1-0d80ed9a8627 | -8.1688 | -54.7432 | 2026-09-20 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 5eb8e6c8-62b9-30f4-acaf-782faedcb7bb | -9.2374 | -46.2344 | 2026-09-20 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| b2bc4ae5-ed57-373f-88c4-add478beb74f | -11.2118 | -54.0797 | 2026-09-20 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d0aad717-d029-33d4-b64a-4b318681cde8 | -2.8974 | -57.8181 | 2026-09-20 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 9983ed8f-da8e-3288-8f9f-207e1405a0ae | -6.295 | -47.6055 | 2026-09-20 01:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 534d3b68-d793-34fb-b4b9-32340ccb52a5 | -13.037 | -46.9096 | 2026-09-20 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 404cb8c6-da21-3728-bcc4-e25e3b352ad6 | -3.7453 | -51.8288 | 2026-09-20 01:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 2d6acf47-7214-3637-9e5d-ea9a56d6c620 | -8.1874 | -54.742 | 2026-09-20 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 83247fb8-a991-3e28-a93b-70574b9509e8 | -6.2948 | -47.6274 | 2026-09-20 01:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 387.7 |
| f3bb7daa-c989-324b-a925-def02f3d0d58 | -6.3134 | -47.6261 | 2026-09-20 01:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 194.1 |
| 18f3364c-0571-3a4e-adde-55217d9ce042 | -11.8739 | -47.657 | 2026-09-20 01:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 78c27afa-2ef4-371d-bc02-ade38af30d37 | -7.4286 | -44.7409 | 2026-09-20 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 6238f443-7c9a-3c83-a319-cb5fc6f09629 | -8.1872 | -54.7622 | 2026-09-20 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 5dd1fecb-7c74-3287-adc9-146cd9f89eea | -7.3259 | -55.6153 | 2026-09-20 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| cf009965-64c0-3001-bf3f-dc8442976670 | -7.3073 | -55.6163 | 2026-09-20 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 5fcdf268-0cdb-3f71-a61a-8f60a6fdc884 | -3.7454 | -51.8082 | 2026-09-20 01:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 3fd000bd-41de-3468-9ed5-82eef70073cf | -7.5525 | -45.4123 | 2026-09-20 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 23902da6-8287-38ae-939b-d3395e02315d | -7.3259 | -55.6153 | 2026-09-20 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 226642f4-1f93-3b0b-b5df-9ed56994b002 | -11.0989 | -54.049 | 2026-09-20 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1e82fc40-5549-3476-9575-c20a2b93fdce | -2.4636 | -49.2089 | 2026-09-20 01:50:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 5c1b7146-372b-31f6-84e1-55eb2d146fba | -2.8791 | -57.8184 | 2026-09-20 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c9a7d991-cf6e-3fcb-aa65-fa454df84d71 | -11.8739 | -47.657 | 2026-09-20 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 6efa0812-0768-38e5-b014-a1dd416ae520 | -3.6946 | -60.6025 | 2026-09-20 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 22150b78-a102-38ee-b7b2-9064f12ee41a | -7.5472 | -45.8868 | 2026-09-20 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9cc2c924-7d9c-3afe-87bd-66f895e1969b | -10.9308 | -61.4128 | 2026-09-20 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 6647d54c-dbc2-3087-b316-34002b88614f | -11.0991 | -54.0285 | 2026-09-20 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 197.7 |
| cd31ffb4-790e-3996-ab62-ef724bb18c29 | -7.5522 | -45.435 | 2026-09-20 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 117ae92d-3b7a-3868-87ad-0a2eb2c32fad | -8.1874 | -54.742 | 2026-09-20 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 50d9db3d-f7c6-3a81-8b5d-42cb15cbd094 | -6.295 | -47.6055 | 2026-09-20 01:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 186.5 |
| f0c53480-52cd-3b40-8e51-5a315a4303af | -12.5415 | -50.046 | 2026-09-20 01:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 47b35683-ce6b-3b94-beb4-320a231e45a0 | -12.7629 | -46.1343 | 2026-09-20 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e2bed0ab-f12b-3e48-b6d1-e2fae07be51f | -12.5224 | -50.0484 | 2026-09-20 01:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f8c13f61-c65f-383b-83c9-c35a3d5618af | -6.3136 | -47.6042 | 2026-09-20 01:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| aacb894c-c203-316b-bae3-dd9309ad4368 | -6.2946 | -47.6493 | 2026-09-20 01:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 54be5159-6152-3531-991c-9b98b47382e6 | -7.3257 | -55.6352 | 2026-09-20 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 3c5b7f6a-884c-3462-9aea-d927a8c71249 | -13.037 | -46.9096 | 2026-09-20 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| c54f84ff-1b4b-3bc6-9f25-f1a9e57a7b90 | -3.7453 | -51.8288 | 2026-09-20 01:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 8a3cdb82-9185-3609-aa62-1ec546b1dee2 | -8.7911 | -60.7935 | 2026-09-20 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 69e1df81-70bd-353d-9eee-50470e08e70f | -14.6856 | -46.6886 | 2026-09-20 01:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 6da196be-d858-3531-b618-40ef4f5ad2ad | -12.5419 | -50.0243 | 2026-09-20 01:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 73a9df37-4f93-3da2-9166-565e1b04cf9a | -7.326 | -55.5953 | 2026-09-20 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a6506221-8bfb-33c1-902b-8a86cb0fc0d8 | -3.7268 | -51.8295 | 2026-09-20 01:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c77031e5-ebc3-3f14-b197-a60ad7cfb72b | -5.8593 | -53.5399 | 2026-09-20 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| c1d11c9a-02c8-30c8-92c5-c6ec50ac5e99 | -11.2307 | -54.078 | 2026-09-20 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.9 |
| fe257402-8836-3e25-b36d-b70728cd82d1 | -14.6661 | -46.6919 | 2026-09-20 01:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 31897bf6-581b-3959-b20b-9bdb15630ce3 | -9.2185 | -46.2365 | 2026-09-20 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| e7707b25-4116-3f30-b4ae-599712c75ba1 | -5.8408 | -53.5408 | 2026-09-20 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 74d77884-3a42-3492-9d54-b6341f99becf | -7.5284 | -45.8885 | 2026-09-20 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d86daf83-933e-3735-b6d3-ff02947aa047 | -11.2118 | -54.0797 | 2026-09-20 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| ee91158b-5751-3438-87aa-1335f0847ebd | -2.8974 | -57.8181 | 2026-09-20 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7fd9f9eb-54fc-3d80-b804-ecf277037c95 | -3.3367 | -57.8673 | 2026-09-20 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 807fd998-0440-3e97-99db-c16635fadc51 | -6.2948 | -47.6274 | 2026-09-20 01:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 285.6 |
| d4da0c9b-8381-3814-ab44-840a20b90008 | -8.8097 | -60.7926 | 2026-09-20 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ed3007ef-1c20-3589-8a9a-77614b1f6f3b | -11.0802 | -54.0302 | 2026-09-20 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 5c0d379c-af6c-3acb-bd2f-b87f844875c5 | -3.7269 | -51.8088 | 2026-09-20 01:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8fa6dab5-aa0f-3f3c-ab1d-60276a669786 | -9.2374 | -46.2344 | 2026-09-20 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |


[Clique aqui para ver as próximas entradas](README7.md)
