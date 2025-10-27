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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b240983-6e06-3696-b4b6-84fcce9c2339 | -5.65249 | -41.10436 | 2025-10-27 03:40:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 71d085cb-1444-3bee-8d86-0aadc3c60af0 | -2.8919 | -42.83632 | 2025-10-27 03:40:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b0105cc-bd50-3c93-8b97-7d0aedab786e | -6.16985 | -41.57334 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bcf958c6-37b1-3b1f-88dc-71f1aed39092 | -4.44977 | -45.45964 | 2025-10-27 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cf2566f3-c8e6-39d9-bac3-237d9d4b3b90 | -4.43329 | -45.98165 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 11661fa5-253c-336a-8642-d75e972179ef | -6.16772 | -41.57613 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 430c4839-ed17-3f3f-aa83-48397278529c | -4.95654 | -44.87629 | 2025-10-27 03:40:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42d902d7-1739-3b63-a614-2f5056d3bf6d | -5.96756 | -42.77328 | 2025-10-27 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 864b7f01-cc40-36c0-b986-a4c05dd8e729 | -4.43936 | -45.98316 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5ef93674-539b-38c9-9a24-2c37eb32de61 | -4.44911 | -43.42039 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7447dec2-8d43-3b97-b977-6d966ecec92f | -5.54639 | -41.4074 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9b9d4eb1-70e3-35c0-8e95-89aa26628451 | -4.45846 | -43.42503 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddc4fd51-7236-37cf-a420-3b7afcf881ac | -4.44593 | -43.43595 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e188e7e-b17b-35ff-bfa5-27988f088340 | -4.86581 | -43.25092 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7557b0e8-d26a-3442-b6fe-5197671fd849 | -3.71298 | -47.6545 | 2025-10-27 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b38847e-481a-3baf-bb39-234db2bd4107 | -4.4798 | -43.42883 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 14b55f6a-0954-3b14-825f-b44d85e28565 | -5.82686 | -40.81605 | 2025-10-27 03:40:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dd8c6a49-599a-3cd8-ab69-361c69d170f2 | -4.83475 | -45.34261 | 2025-10-27 03:40:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24c317f8-a896-3bc4-bdd7-c4b3fec253de | -6.08152 | -42.15097 | 2025-10-27 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 04a31a40-b629-3580-91a1-f6eecc7698ae | -3.70015 | -44.33995 | 2025-10-27 03:40:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ffc4085-145a-3002-9ecb-49532641e8a1 | -6.10983 | -41.73883 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3962c532-561e-3cfa-a76f-4ea815ee2013 | -4.80414 | -43.30289 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56c5ce7f-f6fe-3c18-acc2-36ea96a564ec | -4.44855 | -43.42358 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dad2fe0d-d18a-306f-8fd9-3244bfab990a | -4.26061 | -40.68412 | 2025-10-27 03:40:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| abc92ed7-2b81-31e9-ac02-a5a003177f3a | -5.77662 | -42.9758 | 2025-10-27 03:40:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2b8de301-a212-317b-9652-78b2fcdfcfa7 | -6.11595 | -41.73001 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 83cdabec-7f70-3933-9934-eb5357ff1f43 | -4.51979 | -44.04893 | 2025-10-27 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75c5699f-8050-3525-9fa8-b989826f6392 | -6.13879 | -41.8161 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e797045c-4181-3afd-b333-e4b6dbfe212e | -4.48446 | -43.43285 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0b34e8c-2565-3b15-ba92-969c52b432dd | -3.57094 | -44.53762 | 2025-10-27 03:40:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f6d808ec-9f05-326c-954b-c9af37b77126 | -4.95156 | -44.88367 | 2025-10-27 03:40:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf419f63-49e0-3e38-8257-6c0712b55fd1 | -5.81272 | -40.82207 | 2025-10-27 03:40:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1f93625a-f53d-33f6-9da4-b7c8be6cf135 | -3.71875 | -47.66214 | 2025-10-27 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a5a4e36-03db-3804-ae4d-684b89170fb9 | -5.96851 | -42.76788 | 2025-10-27 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 07d29e27-f4c3-3316-acf2-77122aaee29e | -5.79436 | -43.96552 | 2025-10-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9604a6fb-3031-3a9e-9fd0-71352c8842b1 | -3.57159 | -44.53379 | 2025-10-27 03:40:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 04ce9db3-969b-39a1-ad54-cc23ea3f11d5 | -4.48555 | -43.42653 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 069ad1e3-0af4-36b6-a9af-dc4c1158a318 | -6.20429 | -41.52363 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e1ed29c-e5d9-3538-867c-67effce2c7bc | -4.45264 | -43.4309 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32fcdd75-7536-3bbf-8712-65b6784adc0b | -4.02966 | -46.2043 | 2025-10-27 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 529f2218-d94a-3eca-946b-ba8846c4d859 | -5.2253 | -43.31786 | 2025-10-27 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8915e510-9085-31ed-a983-a7e35f16017d | -4.4573 | -43.43494 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07fef6c1-5628-3c77-8bbb-76b32ae338fc | -6.1175 | -41.72083 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 44dd37a3-41d2-34d9-99d5-e75ac8a5f7ad | -6.19544 | -41.52195 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0e40f2a7-9ac4-351c-8b31-944dbb8e131a | -5.47539 | -37.84977 | 2025-10-27 03:40:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 458c5408-55d4-3ade-a4a0-76ab19d58c41 | -4.81245 | -38.64687 | 2025-10-27 03:40:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 19.4 |
| b46f4401-1498-3ff2-8688-b1873a35fb89 | -5.96967 | -42.77137 | 2025-10-27 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b101c7d3-a638-3c3e-91cf-e00c9089ba93 | -5.89104 | -41.32397 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b340850c-915d-3764-8372-82f436a927b8 | -4.44279 | -43.42588 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 823a2ba5-56bd-37ff-b2a8-11f990c5b566 | -5.52537 | -41.71794 | 2025-10-27 03:40:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82e71ce3-83ca-3f19-a9f2-eb7dfdfc0919 | -4.47458 | -43.42803 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 28c8a39f-7100-3da0-b3dd-6d59bf637d85 | -4.2674 | -40.68781 | 2025-10-27 03:40:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e33da99e-1fcc-3424-8664-8425d14590a3 | -4.43604 | -43.43095 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 293e3a8b-9e97-3d8f-81ee-c59dfe55c3ea | -3.70626 | -47.65306 | 2025-10-27 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce1fd45d-837d-3b1e-97bb-666f342cbc33 | -6.55705 | -38.73127 | 2025-10-27 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ebed1277-1e0d-3ad4-91d2-ab51cd55acb0 | -5.88664 | -41.32325 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d065627d-7b83-3eb7-a293-6211b1154945 | -5.53946 | -41.40305 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 556d522b-8bb6-3a85-bd5a-61072faefb5a | -4.45094 | -43.65971 | 2025-10-27 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| eabb61ce-55fb-3aa1-929e-5f11496b7774 | -6.15951 | -41.5529 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0a6560a9-ea6d-32e5-b411-5873dcaea1ac | -5.64522 | -41.09436 | 2025-10-27 03:40:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 177b07d8-d8eb-3e52-bf91-0b60dc042f2f | -4.45273 | -43.4273 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be2c14c6-2d5b-3ca2-b53d-25f4b8c86d34 | -4.03053 | -46.19927 | 2025-10-27 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bef08d5-c387-3584-9323-707437ed23c1 | -4.78578 | -42.78562 | 2025-10-27 03:40:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 6350730e-1c21-3cc1-ab1f-901307e1d04f | -4.52037 | -44.04548 | 2025-10-27 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e1b97c1-15da-358e-a38f-1f7b91482b89 | -5.0136 | -41.03723 | 2025-10-27 03:40:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9c963435-55c7-3d5b-a1b4-35d3ff33e629 | -4.44447 | -43.41628 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bae5dba0-f8eb-3a9e-8821-412e037264fe | -5.83449 | -43.44931 | 2025-10-27 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2f3c249-5863-3dd5-9f6c-9cbf6314fdb7 | -5.5933 | -41.32039 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d61dc066-0b35-3b8d-85ed-4faccecd0eb4 | -4.45375 | -43.42451 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb66c95d-1a81-34b8-837d-b68e7bd57cdf | -5.81637 | -40.82642 | 2025-10-27 03:40:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cf697feb-2067-35ac-82f7-e71519c0ad58 | -5.96482 | -42.77054 | 2025-10-27 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5b7d8ebc-fd04-35cb-9e1a-013863cc2a93 | -3.57223 | -44.52997 | 2025-10-27 03:40:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 88676889-ade6-3403-98bb-e024c0c311b3 | -4.86478 | -43.25694 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 87867edd-ace9-3e76-a001-daae24434501 | -4.38569 | -43.31828 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8026f70b-b33d-37ed-8639-347a4651b0dd | -6.17215 | -41.57704 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0dc3d3a9-dddb-3b96-9e0d-619eed18f9be | -4.37172 | -46.80909 | 2025-10-27 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc97f4b0-924c-37f5-b5c0-cd6601371565 | -4.27165 | -40.69779 | 2025-10-27 03:40:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bb6fee1a-decb-3cf7-a7e1-29e933ba6c62 | -5.47474 | -37.85385 | 2025-10-27 03:40:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fede593f-2aeb-341d-87d0-ec9631b01880 | -4.44744 | -43.42995 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0221a92c-2c37-330f-914f-6846ec6085b6 | -4.46936 | -43.42722 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85b76b3f-c2a3-39fc-8824-a928e835e250 | -6.14014 | -41.81431 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| af1e2151-9e9f-36d4-8d4b-22bdaef8a6f1 | -5.22459 | -40.9383 | 2025-10-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a39bc6a-ab18-31ba-96b1-662dcac90477 | -4.44646 | -43.43274 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0a97a07-d7a8-35f1-9ea6-c9c14f24548a | -3.69889 | -44.3474 | 2025-10-27 03:40:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| deac1d98-340a-3c13-93db-d1a94fdf9a8b | -5.53872 | -41.40751 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 61f076e3-e91f-3978-851f-a4e8a0b2f81c | -5.6445 | -41.09865 | 2025-10-27 03:40:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fbd8fb89-59c9-3813-80ec-16d176b22617 | -5.86831 | -43.22038 | 2025-10-27 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4805746-6fbb-329c-b792-481793f8534c | -3.71424 | -47.64804 | 2025-10-27 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a605c5f-a1af-33e6-a2d7-8d0f7ac965c0 | -4.47403 | -43.43119 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 25adc165-8bb9-3eaf-9e47-19813a91f2f8 | -6.1144 | -41.73921 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 20dcbbe0-2419-3903-b7c9-8930804594c3 | -6.14476 | -41.81461 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8e614e16-dcc8-3a2e-a7bb-243bf4f95d6b | -5.65176 | -41.10864 | 2025-10-27 03:40:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 77166266-cac6-3047-ab8f-5ed9c2fa0e75 | -5.88654 | -41.32133 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c6bcee4-1fad-373e-8afa-0fb70df5df9b | -4.80521 | -43.29671 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a96a604d-b055-322c-abb1-2f577f2235ab | -4.45635 | -43.43774 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c6a770a-933d-360a-8fc0-8c7662f6f56d | -6.13723 | -41.82555 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 27b42c6f-f599-3830-9a19-fe79dd0419f5 | -6.11673 | -41.72542 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 08756c53-e995-3850-afda-cfd818b7afd7 | -6.11827 | -41.71625 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cc62d646-f158-3800-b1cc-07e3f955625b | -5.03318 | -41.19197 | 2025-10-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 854d5c05-0baf-36b8-834c-76bb20c7c933 | -4.90466 | -42.99212 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README15.md)
