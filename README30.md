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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5f3b814-f83b-3c14-9038-c8c1f0a85249 | -1.81471 | -47.99228 | 2024-11-08 04:53:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca0272ff-07ab-3207-a073-26d1a9580767 | -3.13887 | -51.2004 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3b8934f-5729-3045-807b-29334b3a7958 | -1.64174 | -50.43853 | 2024-11-08 04:53:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74a29491-5058-364e-9e10-cfa31b54861b | -1.69966 | -52.33597 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc9e647f-5887-3b9e-b097-543fbe24b04b | -1.20051 | -53.62582 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41f7fe1f-ccc1-3d38-8524-fb3b2c1b8ae5 | -3.14009 | -45.25286 | 2024-11-08 04:53:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a3bfe40-3be0-3612-9499-b6a410e56eda | -5.37749 | -46.26522 | 2024-11-08 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d361614e-9502-391f-bdd6-8cb5e3eed474 | -5.73631 | -42.00193 | 2024-11-08 04:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 88b8226c-7148-3628-9b32-ff8961659d06 | -3.24248 | -45.69074 | 2024-11-08 04:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c05bf236-ecfd-36cd-82fc-aa3a8b035a5f | -3.0296 | -51.53054 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 79666a0d-a478-3a67-b480-a24e9df19e4c | -3.45693 | -52.02011 | 2024-11-08 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec29f214-b539-3a2e-bb6a-0a706a86ab7c | -2.92981 | -45.15065 | 2024-11-08 04:53:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a6a7506-ee7a-300b-b1ca-0d13071deff4 | -2.63237 | -46.77707 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e82f94fa-7649-3c1c-ba70-3af9514ba6f8 | -4.11392 | -48.50349 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae5ff93e-089d-34df-b8c6-b251ebe8d460 | -3.71618 | -41.69069 | 2024-11-08 04:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7c617103-36db-3b2f-b967-1fa3ca6958fe | -4.15956 | -48.25309 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4f50061-8d14-350b-8466-3503835af47f | -4.78404 | -48.67934 | 2024-11-08 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 905dab42-0a5f-3333-843e-54b3a00b942d | -4.86995 | -42.94574 | 2024-11-08 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9878476c-f3f4-371b-b7b9-e4f9e251b1d8 | -3.72073 | -53.40133 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eca4526e-d344-3115-8846-c880d6d8ebbf | -4.53118 | -45.68236 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 872de414-eb42-36aa-aadc-7e109f25433e | -3.25369 | -46.47393 | 2024-11-08 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfbe2646-b353-37c5-a9f3-09e71404dc92 | -2.76616 | -53.21966 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee7cd6da-c594-3ca7-bb48-f6c01c1ddc6a | -3.50109 | -51.14591 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e692c150-ab71-3453-89ca-647f291d4b45 | -3.55595 | -47.38308 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| f2bad51f-8ee9-396a-abf4-9d535dff1b4a | -3.31316 | -50.09391 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5324809f-beb3-3551-9b60-f13e663fe9b3 | -6.23246 | -46.22754 | 2024-11-08 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a56c543-9425-3853-91dc-4b4ec18a7245 | -2.80574 | -52.94394 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 657856e3-2d4f-3ecd-9b61-f0e2477c828e | -2.61833 | -51.74791 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d9ad5b9f-b311-324a-bb81-6a75ba4b0864 | -5.2081 | -47.4677 | 2024-11-08 04:53:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 762b08c7-dd49-354c-b3ae-13c5531163d6 | -2.79628 | -52.93892 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2228b34c-f2e4-3f3b-8145-cedb27c91d7a | -5.74275 | -41.99855 | 2024-11-08 04:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2a157a3e-3e07-3f24-a36c-3289d8d1420a | -4.8085 | -50.68619 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7daf660d-ab01-3e72-98aa-ac1eec3b6453 | -3.24816 | -53.3971 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bddd13d-2af3-3279-a1c0-d44d47589385 | -3.9534 | -48.15572 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 725bb81c-fb29-300e-8c49-5ec2e4d8bce4 | -3.09168 | -53.32847 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f38e0b15-3960-313f-8871-a2548f9a2a92 | -2.05342 | -53.29232 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f589e7d5-4702-357f-950d-404a8ab63168 | -2.85225 | -51.77418 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b359dbb-b2bf-3c06-b74b-c337a4928585 | -2.66336 | -51.94101 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df4ced6b-ef23-3d98-bcc5-102d55376c0f | -6.31464 | -46.90358 | 2024-11-08 04:53:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0342620-01a5-30cf-be19-3298c81f009a | -1.46302 | -52.56606 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b86db67c-4f6c-374e-8bb1-2c1270c2ee2d | -4.26563 | -46.85861 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92bc8bc9-36b8-339b-9828-87b5d8b3013b | -3.01373 | -53.43744 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aac1180-032f-3268-b1eb-222565500cc0 | -3.25067 | -46.46578 | 2024-11-08 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce792e0a-633c-3aa7-a3f0-83bff2be0310 | -4.91892 | -44.04088 | 2024-11-08 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 174064fa-50c6-3501-9178-f74d5c2def53 | 0.74548 | -59.77504 | 2024-11-08 04:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bd5e719-e63d-3029-8bba-1f197d70f8e8 | -2.01655 | -46.57861 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2367dadb-2267-3d89-973f-0f24cc270d3f | -1.33675 | -54.60001 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2de18ada-8994-32fc-bf2c-fe82da80f3fe | -4.37102 | -44.66736 | 2024-11-08 04:53:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d880b23d-b280-385f-8d91-3ccccf0a52b2 | -2.6211 | -51.75185 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e85f5237-2c7f-397f-ac09-089d5f4b95f2 | -2.84263 | -51.96587 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f5529d5-e3d0-3de7-bd8a-4eeecddfa9c9 | -4.91706 | -44.04795 | 2024-11-08 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a61343e-bfcb-304f-a477-adf906c30f5d | -3.49461 | -51.58236 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9dd43ba-5733-3b53-b718-f8515cb5f209 | -1.50179 | -52.55783 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 995af453-8deb-3e89-b129-ea28ab09cf50 | -4.52021 | -45.69468 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ef851308-88e1-34e8-bda4-0cadd2466ccc | -5.40033 | -45.12946 | 2024-11-08 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29129b25-a3ff-34da-9783-2e9364d271d1 | -2.63695 | -46.77415 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4d8ddf7-53fb-3cd7-b405-414423f340f6 | -2.83581 | -52.90198 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5446cb3c-e04c-3ee8-9176-f8ceecfcb6a7 | -1.13878 | -54.2196 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d820d69e-48fb-30a6-b39e-383aff67df0e | -3.19997 | -53.41884 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3872c73-ff73-3f53-85a4-4c7d7788008e | -2.81809 | -52.94941 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0c87f88-6914-3ec0-aa5c-24b329569f63 | -2.61503 | -51.7474 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a7967ae8-fd37-3ecb-956a-865ab0124527 | -2.74175 | -51.89338 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff381c57-ee57-39f4-8a6d-6413d03883f3 | -3.3877 | -50.22607 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ece7945a-ac6d-3954-96c2-8ae7c77c3ed0 | -2.73005 | -51.73003 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6850c1aa-6114-34b1-96be-c265a5832861 | -1.15095 | -53.65191 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9e396c32-7c69-3b6c-a23d-5ede53a295d2 | -2.2798 | -53.81742 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a325ab1b-77f9-391a-8ab3-d5e16031dbd9 | -4.99958 | -49.91663 | 2024-11-08 04:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c329fac2-400f-3db9-ac9e-a1ad7d9ef8ed | -6.5236 | -47.0124 | 2024-11-08 04:53:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efbfde9f-c8e2-30d4-aab4-299255d086f5 | -3.29037 | -50.08286 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b79b7c7-cc36-30e2-ac72-f026b2a72b7d | -1.63331 | -53.43929 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dba2094f-8263-3c90-830a-4fbad8c96a16 | -4.68211 | -46.44952 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d23aec6d-50ea-39fd-8274-38b02bfa898c | -2.76817 | -54.03725 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11221376-322b-3ce2-bac7-d08701d8e87b | -1.38091 | -51.41377 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45336e1c-730d-3898-9860-6cc6f803c23d | -1.21804 | -51.76043 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecefeb2c-9f24-354f-b683-7513403ef712 | -1.32056 | -52.2378 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff718fcb-13fa-361b-8852-d069e32cb642 | -3.84104 | -45.99531 | 2024-11-08 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdab2674-638b-3cca-9461-48073426a3df | -3.22354 | -50.38358 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1ebf578-5038-3a61-ac0b-c28345a53f63 | -3.12082 | -53.12276 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 566e81a9-ab3f-36ad-b22a-9d66f83f7409 | -1.82918 | -53.6914 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afb5a30e-55bb-3b9b-9bc2-e6c212933788 | -4.35027 | -48.62588 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 15bc77d1-cbae-36e6-9459-f0c8b220d3d9 | -2.2132 | -53.72758 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bbbc102-65e2-344c-a087-139acb9d1922 | -2.23486 | -48.3761 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83a6bd88-721b-31f9-a5b2-a521f29d22dc | -2.08526 | -54.70415 | 2024-11-08 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2dd20937-6d0d-3ecd-a93a-46c702b3818f | -1.50859 | -52.16492 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 993e8f5d-c430-3a91-b955-d29731a34f90 | -2.97627 | -50.29799 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a671e4c6-c263-323f-a577-22efa3e5e9a5 | -2.72744 | -54.14274 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13d02203-5354-3a44-8fce-3601ed05ac07 | -4.38244 | -48.57906 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 379fb4ce-28af-358c-8bb4-fc6739f82072 | -3.83571 | -44.1214 | 2024-11-08 04:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb485d58-40a0-3a25-98fd-a4cd1dfefe54 | -2.1715 | -46.43818 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c20c91e-98e7-34b5-b803-432fab462501 | -1.45786 | -53.4195 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2f92867c-1cfd-3b0e-b364-b462a72e9b80 | -2.17592 | -47.56015 | 2024-11-08 04:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf26b303-416c-39d3-ac43-c6d998256fd0 | -2.2401 | -53.66754 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b2f881e-020d-3071-ae1f-d0150dfa664c | -1.52804 | -52.62983 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3af43920-4c11-3bad-85a9-28e63af2f769 | -5.37083 | -44.7312 | 2024-11-08 04:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31f50dd6-30f8-3c7c-bad3-61967e2931cd | -2.79962 | -52.93943 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| d62cbe14-5c85-3d2f-86b8-ebbf99e36af8 | -3.01543 | -53.42665 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e655a950-dd7e-33f7-b663-c89babc46696 | -1.37419 | -52.26373 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef2f41e3-cc06-31ee-8148-c7912a3e7711 | -2.90651 | -51.46934 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| acfc3c35-2e61-3c4e-9c24-a547914cae7c | -2.61924 | -51.30431 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75c7edb6-7f01-38ca-81ce-1b481ae82657 | -3.37849 | -46.10765 | 2024-11-08 04:53:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README31.md)
