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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f5257d8-6fc0-33b4-90fa-849ae1dbbc5b | -11.4743 | -44.2053 | 2025-10-17 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 7119f738-25cf-35ef-9d3a-f294a732cc36 | -11.4172 | -44.1904 | 2025-10-17 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 31bef0c2-5f1c-3a85-8a14-ee3cc3984533 | -11.3972 | -44.2401 | 2025-10-17 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 85ecca74-0da3-3e24-b724-8e37c0f26d02 | -11.4748 | -44.1819 | 2025-10-17 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 0465ff5e-28a4-3b17-a9af-2699e0a461f4 | -12.4678 | -45.4694 | 2025-10-17 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 022e2e87-4750-3dec-8b37-80d21ac6acae | -11.398 | -44.1933 | 2025-10-17 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| df8a8b87-340b-3c8b-b545-9f50f1efb265 | -11.4168 | -44.2139 | 2025-10-17 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 1eec7cff-75f8-3837-8b77-bc44354bdafe | -13.0488 | -47.3131 | 2025-10-17 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 53fb107b-2641-3e02-92da-4b3d12e4a37e | -12.487 | -45.4664 | 2025-10-17 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7d1aaad4-f5e8-3e2f-bec5-f6c600cad362 | -12.0687 | -47.4303 | 2025-10-17 12:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c4b381ef-1a59-3e4c-b12b-b822da0a13cf | -10.938 | -45.4146 | 2025-10-17 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 20e3828a-3e43-3386-b40e-b925d54e993d | -11.496 | -44.0617 | 2025-10-17 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 9f7f7baa-1815-3e9b-aac1-386a1ab690f0 | -11.1403 | -45.8665 | 2025-10-17 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9d430aae-e270-351d-a38e-91f51ef28f21 | -10.9189 | -45.4171 | 2025-10-17 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 8ebde4a0-300a-3414-9140-27dcd0fc4b42 | -13.4412 | -47.9483 | 2025-10-17 12:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 8162ffcb-6622-3dee-906c-c6aa90bda9bf | -10.534 | -49.5471 | 2025-10-17 12:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 7d56bcd4-b8be-3803-9850-be46a05c01c4 | -11.5729 | -44.0501 | 2025-10-17 12:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 9a654cae-4c12-3c51-96aa-56c4cfe1ee12 | -11.3976 | -44.2167 | 2025-10-17 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| a6e8a2fd-4874-3572-886b-68beb8c0fc1e | -12.1678 | -45.0771 | 2025-10-17 12:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 4c489c4d-a106-3989-a3dc-374f8a842634 | -13.0483 | -47.3356 | 2025-10-17 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 88f23797-4216-31f5-86b2-bffdf31f2aca | -11.5917 | -44.0707 | 2025-10-17 12:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 39a7ee98-c6df-3c02-ba3b-1aeeddae0bf2 | -10.938 | -45.4146 | 2025-10-17 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 34d71dcf-1113-32b4-9cc3-016a0421cff3 | -10.9189 | -45.4171 | 2025-10-17 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 74b21dd5-e2da-31b8-b0de-2794c7ebef3d | -11.9521 | -45.3401 | 2025-10-17 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a175959e-f5d6-38ac-859f-598b385f13f6 | -13.4219 | -47.9511 | 2025-10-17 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 33b78866-2b72-398a-9700-783057c7209b | -12.5054 | -45.5096 | 2025-10-17 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4798020d-bdc3-3316-9a06-2f9f7f0b86d9 | -11.5921 | -44.0472 | 2025-10-17 12:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 78c8dde2-13f7-3ceb-a034-f3c9127939c0 | -12.487 | -45.4664 | 2025-10-17 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 87673574-5fef-3f34-a336-eff583b03303 | -12.1678 | -45.0771 | 2025-10-17 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| e0079e55-c9e4-3469-a119-45c1416dd8fe | -12.4866 | -45.4895 | 2025-10-17 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 49da059c-901a-327e-8b8a-ad93509f801a | -11.9709 | -45.3603 | 2025-10-17 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 61705b21-529a-35ea-ace7-e2f368445fb3 | -11.5729 | -44.0501 | 2025-10-17 12:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 3ec2fd47-a809-3931-b107-07e62538b724 | -11.4743 | -44.2053 | 2025-10-17 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| f54a8dc3-171c-3d44-bcc5-1a020cc12b98 | -11.9516 | -45.3632 | 2025-10-17 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 2e8176eb-89b3-3056-b112-38a5456aa0cc | -11.5724 | -44.0736 | 2025-10-17 12:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| a1264971-f50b-3468-a15c-4997af3b838f | -13.4412 | -47.9483 | 2025-10-17 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| f81d5a70-59d1-321e-ad59-0a076fecd3d6 | -10.534 | -49.5471 | 2025-10-17 12:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| e76c01a5-07f2-3967-9e78-8eefd2c89e87 | -11.4748 | -44.1819 | 2025-10-17 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| de54e3d2-435b-3e05-bfd0-3e16da8c2347 | -10.9748 | -47.9042 | 2025-10-17 12:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| e46f69ad-93f8-370c-80b3-f6d6b4c0b01f | -13.0483 | -47.3356 | 2025-10-17 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 778c9880-79c0-3a24-aa35-d4e402d696c5 | -10.9185 | -45.4401 | 2025-10-17 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| b01d5614-c9ad-37b7-871f-9bdff0e47904 | -12.4678 | -45.4694 | 2025-10-17 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 09bf3154-8088-335f-b879-e6dcd5a37f28 | -11.5917 | -44.0707 | 2025-10-17 12:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| e37ea01d-571b-3fa6-9be7-7b1b70499a43 | -13.0488 | -47.3131 | 2025-10-17 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 7006cc8c-eb8e-37b5-969b-ea64017cc7b4 | -13.0483 | -47.3356 | 2025-10-17 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 160.1 |
| ac2f4a90-ef76-3bac-83cd-7fbb7670483f | -13.0488 | -47.3131 | 2025-10-17 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 242.5 |
| d05a50e6-439e-3ccc-93fe-e495576f2f7c | -10.938 | -45.4146 | 2025-10-17 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 377.2 |
| 942da298-fbea-3e00-be57-297b5a48160e | -13.0295 | -47.316 | 2025-10-17 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9685297d-27db-3e3e-82b2-2f6ab375c758 | -11.3976 | -44.2167 | 2025-10-17 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 8ea5a663-93f8-341d-9a3b-c213449a8e6c | -10.6363 | -45.2257 | 2025-10-17 12:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| e0875b14-ad03-3467-8a5f-d65e1241e107 | -11.3972 | -44.2401 | 2025-10-17 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| bfb1e477-8169-394f-b043-51d496dfdd4e | -10.9185 | -45.4401 | 2025-10-17 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9dbf5dee-ff7b-31b3-8412-3789ac12a285 | -11.5729 | -44.0501 | 2025-10-17 12:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 58f0639a-6d00-3de8-b890-43bf5983b573 | -11.3784 | -44.2195 | 2025-10-17 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 524fe429-aead-3151-b1cd-a528a5d5d709 | -13.4412 | -47.9483 | 2025-10-17 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| cc9423c2-b79e-3ddc-91c5-b49af26c9b66 | -13.4408 | -47.9706 | 2025-10-17 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 3284153e-e304-3d02-89ad-48f61121a5b8 | -12.9414 | -47.9322 | 2025-10-17 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1b019fff-51f2-372d-a63f-ee96f62dd200 | -10.9189 | -45.4171 | 2025-10-17 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 369fa76b-b077-347e-bb8b-a5b71b331537 | -12.9607 | -47.9294 | 2025-10-17 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| bedcd632-45a6-3eb1-8162-348d8de01ef5 | -11.5917 | -44.0707 | 2025-10-17 12:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 55b3aa6f-24a8-3981-b8ce-3e197c2f913f | -13.4219 | -47.9511 | 2025-10-17 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 64640905-e74d-37a3-bee9-e2ce2ac0e36b | -11.4172 | -44.1904 | 2025-10-17 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| f1240190-7520-3f7a-931e-f21ddfdbbe50 | -11.5921 | -44.0472 | 2025-10-17 12:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 9b5d0ece-f57c-3ae4-ad0c-7fd7a2fe68c3 | -12.5054 | -45.5096 | 2025-10-17 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 3cb2e27b-d165-3ab9-9035-ecd9cd9e9dc2 | -10.534 | -49.5471 | 2025-10-17 12:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 1c28fc27-339b-3d04-9a63-348a1e550bf9 | -11.496 | -44.0617 | 2025-10-17 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 059576b3-9199-3ef4-85e5-69620263c63d | -12.487 | -45.4664 | 2025-10-17 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 55d4ba30-6b59-3460-a0c5-aaa7fcf32065 | -11.4168 | -44.2139 | 2025-10-17 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 9f03f453-4588-3161-b3b7-b574b1ff50fe | -12.4866 | -45.4895 | 2025-10-17 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| cd36c750-ead6-3e75-ab95-5cfa75e9cfee | -11.398 | -44.1933 | 2025-10-17 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 29359a69-a0b8-3754-8ab7-596602707891 | -12.4678 | -45.4694 | 2025-10-17 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 91d51631-0d16-3298-af9a-4f6ef9faebc8 | -11.4735 | -44.2522 | 2025-10-17 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 816321d5-65f2-3c11-979b-ff7afc328ba8 | -10.6172 | -45.2282 | 2025-10-17 12:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 7420bb7d-5854-395f-9f61-a52675d8e19d | -10.9189 | -45.4171 | 2025-10-17 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4a1a5cee-d8e0-3080-94e5-65263de76ae5 | -10.938 | -45.4146 | 2025-10-17 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 8b405451-1855-30a5-9805-021a8915b775 | -10.6172 | -45.2282 | 2025-10-17 12:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 5b5451d3-ca9a-3d41-8bcf-30628e250a1b | -11.5917 | -44.0707 | 2025-10-17 12:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 8decb35f-2e7a-3ece-a1c0-e236f5528388 | -12.9414 | -47.9322 | 2025-10-17 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 2a1f30a2-34b6-347f-b955-0f0b4b46beb6 | -13.4412 | -47.9483 | 2025-10-17 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| be38a580-9aff-3773-8660-b7d36caab6a9 | -12.4866 | -45.4895 | 2025-10-17 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 20d6b6aa-081a-33b2-a067-8829bf292cb3 | -10.6363 | -45.2257 | 2025-10-17 12:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| fdbcc29e-a30e-3052-9bb7-3cb75710118c | -11.1212 | -45.8691 | 2025-10-17 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4b569961-a476-35d5-8db5-d1e0c7ee7217 | -12.9607 | -47.9294 | 2025-10-17 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| eb9b21a2-b6fb-348f-b637-283e4abb2356 | -13.0488 | -47.3131 | 2025-10-17 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 62ff0c0b-8037-3db1-967b-02b3d87b5647 | -12.284 | -47.1544 | 2025-10-17 12:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 2cdfcbce-69d5-3366-b073-ecb9fad2bfc3 | -11.5729 | -44.0501 | 2025-10-17 12:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 0c6087ed-9b5a-3c68-98b2-451e321c743d | -13.4408 | -47.9706 | 2025-10-17 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| bb01c7b8-44aa-302b-8be8-1131bb8c3ec7 | -10.534 | -49.5471 | 2025-10-17 12:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 559152c0-97ca-3b50-9c21-7aceda6a7595 | -13.0483 | -47.3356 | 2025-10-17 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| a3dc9328-8a6c-3d12-bee0-a1ba6c19f14f | -12.487 | -45.4664 | 2025-10-17 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| c36e564c-67eb-340f-8e35-a5b76188e752 | -13.4219 | -47.9511 | 2025-10-17 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 92c4b92b-18d2-398e-94b4-1567761ce53d | -11.5921 | -44.0472 | 2025-10-17 12:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 0b0e3af7-4318-3064-83b9-a54552413320 | -11.9257 | -46.845 | 2025-10-17 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 36aaa445-8c35-3c22-bcf4-7a426b7c1d2d | -11.3603 | -45.2646 | 2025-10-17 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 11add9ae-12f7-3eed-b994-b6c13513b233 | -12.4678 | -45.4694 | 2025-10-17 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 0b5eb25b-a0e0-3330-b15a-7b6a7cc2f6eb | 1.77877 | -55.91518 | 2025-10-17 12:34:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 3a308fc0-c493-32cc-b99b-526a0a217fc7 | 1.78347 | -55.92151 | 2025-10-17 12:34:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 41dc1d07-5a39-3074-9e75-9dc02def490f | 1.04075 | -51.21755 | 2025-10-17 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f92b75be-0bf0-39e8-aa77-88242dc55b41 | 1.10379 | -51.15507 | 2025-10-17 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 48b16c06-f635-356b-bcca-e69df3839522 | 1.09496 | -51.15629 | 2025-10-17 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 45.4 |


[Clique aqui para ver as próximas entradas](README118.md)
