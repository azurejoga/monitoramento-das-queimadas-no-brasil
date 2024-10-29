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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bdba5c0-d614-30c7-96d0-72800bd34a47 | -1.25784 | -55.92005 | 2024-10-29 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 899a5e7e-9e4f-3f24-ac51-ff74ce54f6d4 | -1.25646 | -55.9101 | 2024-10-29 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8a2bf76f-d288-3f2a-a1d3-7256b2e60d00 | -1.21191 | -55.86549 | 2024-10-29 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 151944f8-e1b0-3f1d-b687-4957cfb684ec | -1.2082 | -55.90697 | 2024-10-29 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c757b79e-3e59-3df5-9759-c189d6c514db | -1.20395 | -55.87695 | 2024-10-29 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ce879a5e-9936-32c4-a0d5-f30fd3c25811 | -2.83025 | -57.673 | 2024-10-29 01:32:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 08011257-a785-37c3-8a1f-82dd60ed182a | -2.55874 | -58.11209 | 2024-10-29 01:32:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 463da7e3-dcf6-3de7-ba39-2918f9d0d7cb | -2.46785 | -57.52439 | 2024-10-29 01:32:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 29e63a6c-2886-3ca5-845d-ced8e4f81198 | -2.34296 | -57.16014 | 2024-10-29 01:32:00 | TERRA_M-M | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| efb2ddf5-ec9a-3e0b-86ca-22dfa50b588b | -2.34171 | -57.15122 | 2024-10-29 01:32:00 | TERRA_M-M | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c190b7c1-0c2d-3c98-963b-5c7b595f9ee7 | -2.32394 | -57.15374 | 2024-10-29 01:32:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 852d0621-6e03-33ea-bf3b-46f6abe2aa43 | -3.43652 | -59.26111 | 2024-10-29 01:32:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4f672c4d-3d59-3735-bb24-b6eb52cbe042 | -3.43522 | -59.25162 | 2024-10-29 01:32:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 59966d88-34f9-3f98-b86f-8beee5fe7d67 | -1.71528 | -60.13731 | 2024-10-29 01:32:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a282a5e6-8352-3caf-80fb-973a8e9980da | -1.43093 | -60.28691 | 2024-10-29 01:32:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c90bf48b-3b3c-3ff4-9ebf-e6dce2628635 | -1.42616 | -60.294 | 2024-10-29 01:32:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a9723a62-13cb-39cc-addd-57cac647b838 | -1.42474 | -60.28393 | 2024-10-29 01:32:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 3a209208-890f-38ab-86de-5654b6751f73 | -1.30517 | -60.22478 | 2024-10-29 01:32:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a3549f02-89b2-30c2-9e06-aae4294959c0 | -1.29581 | -60.22612 | 2024-10-29 01:32:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b67bd5f4-afdb-3a91-977f-86c0390d0f31 | 4.06075 | -61.24926 | 2024-10-29 01:32:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4255f3cb-3fb6-33e9-b946-4d8e9b792081 | 2.22443 | -61.67648 | 2024-10-29 01:32:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e616c278-52ed-371b-a3c4-e8bc2011088b | -1.714 | -54.5335 | 2024-10-29 01:35:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 39fe99c4-5345-395d-8ae6-efa455cfee23 | -2.3353 | -48.9137 | 2024-10-29 01:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 82b47aac-aad9-3c23-bd0c-2ae361a1d234 | -2.3537 | -48.9133 | 2024-10-29 01:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 380d58eb-385d-3ec8-9061-9d9a1a4fe066 | -2.5251 | -47.442 | 2024-10-29 01:35:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 912acc68-584c-3d5c-983e-b915ab0f9f61 | -2.8555 | -53.3459 | 2024-10-29 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 64ae578c-c356-37f2-ae6b-351ad9ff73c7 | -3.0913 | -54.287 | 2024-10-29 01:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| eaae3b2e-e630-361e-8ee1-57ce469486a2 | -3.1097 | -54.2865 | 2024-10-29 01:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 9b7cb44a-f997-3198-9e5c-721db141e48a | -3.1098 | -54.2665 | 2024-10-29 01:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| b286ccf6-2cb1-3df8-9a90-19a0b227ca62 | -3.1281 | -54.286 | 2024-10-29 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9b15e932-77e1-37e1-bb36-11104ecca52d | -3.1281 | -54.266 | 2024-10-29 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 9637e80f-c037-35ec-bc5c-fb0cf360336f | -3.1794 | -50.3922 | 2024-10-29 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7037657f-8ad6-3d8d-9d9a-6aa35bda1c55 | -3.2503 | -46.8709 | 2024-10-29 01:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4f5d6f48-c869-3c16-9d6a-ec5ecaae0b8c | -3.3044 | -47.198 | 2024-10-29 01:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 996720b4-8290-3008-a9b0-122697fe90f2 | -4.3471 | -43.8021 | 2024-10-29 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 3580a4ff-8a1f-3c19-9cab-1d9912cefbf7 | -4.3473 | -43.779 | 2024-10-29 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 352.9 |
| ffd7129d-4ef6-3482-be1e-404818f4ac55 | -4.3475 | -43.7559 | 2024-10-29 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 358c242a-75cd-3044-ad93-5f94c3e88343 | -4.366 | -43.778 | 2024-10-29 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 600e4e95-f4df-329a-8d8e-b75a8d03eafe | -4.3661 | -43.7548 | 2024-10-29 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 8631410e-c644-3d58-8756-d0e729474bb3 | -4.2576 | -46.0965 | 2024-10-29 01:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| fb1bb531-32f9-3555-bfd2-0b2578d823c6 | -4.2761 | -46.1178 | 2024-10-29 01:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f758d3a7-1249-340f-a3a1-946d05921704 | -4.2762 | -46.0956 | 2024-10-29 01:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 6033ca92-ce91-3d30-8c29-ae126d2f4dc1 | -6.5956 | -47.3867 | 2024-10-29 01:35:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 82e3e4e6-5d7a-3235-831f-6008264d4eb7 | -6.6143 | -47.3853 | 2024-10-29 01:35:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 9c85369d-9afb-3c5b-8668-3b7788393e4f | -11.138 | -55.5313 | 2024-10-29 01:36:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9094f5d2-ef67-3fa3-a500-2301125d3fdc | -12.3334 | -49.9208 | 2024-10-29 01:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| c04c006e-ca07-3692-a7c0-fbcf365c28b0 | -12.3522 | -49.94 | 2024-10-29 01:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 722fe33b-3d72-33c5-8993-74d5141330a7 | -12.3526 | -49.9184 | 2024-10-29 01:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 7c40a352-a03a-3725-928d-59bcc7fcec17 | -12.673 | -43.8042 | 2024-10-29 01:36:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 2fed8213-428e-3b5f-82d2-65d614b31949 | -1.7509 | -54.4531 | 2024-10-29 01:45:16 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 09fa6879-9c12-371a-9fcb-cd9e8866c716 | -2.3353 | -48.9137 | 2024-10-29 01:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 8a3ef844-0ca8-3874-9d40-1aa8cd3770b0 | -2.3353 | -48.8924 | 2024-10-29 01:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| bca527aa-9ade-30e4-ab91-cbeb98b45a02 | -2.3537 | -48.9133 | 2024-10-29 01:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 73929817-2f90-38da-84f0-94331f50b046 | -2.5251 | -47.442 | 2024-10-29 01:45:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e75f3652-4f72-35e5-8f4a-c4c68ea1cab3 | -2.8146 | -49.2206 | 2024-10-29 01:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 6e152f2a-0cbe-32b7-acae-6f641594c55d | -2.8555 | -53.3459 | 2024-10-29 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 01c562af-ee7e-39e7-b366-ae8833b1fdda | -3.0913 | -54.287 | 2024-10-29 01:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 47338260-5162-370b-9863-2c2acabe468d | -3.1097 | -54.2865 | 2024-10-29 01:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| b6ee7b94-3f3e-316e-a82a-3fdb8bac4d87 | -3.1098 | -54.2665 | 2024-10-29 01:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| e89b7c4a-273f-312f-b4db-f6ae008ad5f7 | -3.1281 | -54.286 | 2024-10-29 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 83d771d6-4e3c-3968-bac4-84a8a4c1a525 | -3.1281 | -54.266 | 2024-10-29 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 558706c2-ae87-398b-ad59-86c162a851c8 | -3.1794 | -50.3922 | 2024-10-29 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 96d48f88-0877-39c3-b8a7-53695be848ff | -3.2503 | -46.8709 | 2024-10-29 01:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0689dde3-0e8f-3cc0-8c97-a6f34bb768d4 | -3.3044 | -47.198 | 2024-10-29 01:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| aa18a802-6e00-3019-a56a-f6facf6f597c | -3.48 | -45.4842 | 2024-10-29 01:45:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| aa47ea0c-3e63-3811-a61b-202db68f5f29 | -4.3661 | -43.7548 | 2024-10-29 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 1c948c3b-9072-3046-8eb1-78641438f03b | -4.3471 | -43.8021 | 2024-10-29 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 7c4ae2b4-ce1b-3f4c-b549-ce195cb2b886 | -4.3473 | -43.779 | 2024-10-29 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 227.1 |
| 9fcb1c7e-7093-38e1-8c12-6b5f15af1ed3 | -4.3475 | -43.7559 | 2024-10-29 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 8c261fdb-b161-31d1-afd8-fc8c850da34a | -4.366 | -43.778 | 2024-10-29 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 77c84eee-e9bf-3fc4-b269-a0500fdaeb65 | -4.2761 | -46.1178 | 2024-10-29 01:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 99aeb172-6ce2-3d8a-9850-60b2b19652e4 | -4.2762 | -46.0956 | 2024-10-29 01:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 21d62782-6875-36be-b3b5-de6dc0786f3c | -6.5956 | -47.3867 | 2024-10-29 01:45:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| aa1f0103-4d98-3f24-85e7-d665419aa65c | -6.6143 | -47.3853 | 2024-10-29 01:45:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 5d4af7f2-753e-3e17-9416-a53648c6f402 | -10.2304 | -36.7167 | 2024-10-29 01:46:03 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| 13b54143-7bdc-3b9e-9687-e05aad5adba5 | -11.138 | -55.5313 | 2024-10-29 01:46:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f95b501a-02b7-3e54-932a-2aefcfa7eb6e | -12.3522 | -49.94 | 2024-10-29 01:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 6eaee03d-fb9b-3c5c-907f-c7af78d12dd7 | -12.3526 | -49.9184 | 2024-10-29 01:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 161a48c0-445c-3294-9ded-8cc634e2172a | -12.3331 | -49.9424 | 2024-10-29 01:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2ecfc555-9b85-345f-9289-af736f3ceab2 | -12.3334 | -49.9208 | 2024-10-29 01:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a60fdaf6-6d07-34d9-acd7-3b5efd4416ac | -13.6887 | -46.1247 | 2024-10-29 01:46:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 9decaceb-996d-3b0b-bbef-afdc7c05b2a2 | -13.6891 | -46.1017 | 2024-10-29 01:46:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 651ff560-947f-32f8-82a2-377cce2df171 | -13.7081 | -46.1215 | 2024-10-29 01:46:23 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| df86ccba-e9b9-32c7-b095-03af9bc9ecf0 | -13.7086 | -46.0985 | 2024-10-29 01:46:23 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b25c01a2-2f12-3d2e-b9fe-0ac4ba8e0033 | -14.1391 | -44.0662 | 2024-10-29 01:46:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 6485c695-2989-3989-97c3-5a112f9a418e | 3.4526 | -51.2595 | 2024-10-29 01:54:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b339a22c-73c4-32fe-b3cb-b59c4682b435 | -1.7509 | -54.4531 | 2024-10-29 01:55:16 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| ca01d91a-0280-3e27-926b-f6ea7173f257 | -2.3537 | -48.9133 | 2024-10-29 01:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| c6a216dc-0d0f-3308-a613-e029b8c55062 | -2.3353 | -48.9137 | 2024-10-29 01:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 728c7038-5c9b-3c19-8981-2c06e49ec578 | -2.5066 | -47.4425 | 2024-10-29 01:55:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 47af05e6-7d88-343d-a53d-b624ef5cab3b | -2.8555 | -53.3459 | 2024-10-29 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 45685348-6645-3ee2-af86-102be5209a76 | -3.0913 | -54.287 | 2024-10-29 01:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 0d812aaa-4db5-3d9a-a69e-73b8346784e6 | -3.0914 | -54.2669 | 2024-10-29 01:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 2cabb745-4cfc-3ee9-8dd9-d45f72d85984 | -3.1097 | -54.2865 | 2024-10-29 01:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 54a800e3-b6f7-31ff-bb61-4aba693a1e9e | -3.1098 | -54.2665 | 2024-10-29 01:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| e4b02a3e-d294-36b7-a455-ea473c95027f | -3.1281 | -54.286 | 2024-10-29 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 82dafb2f-f66e-3354-a06e-9f4e2cbd8fc9 | -3.1281 | -54.266 | 2024-10-29 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b8d36009-a1ff-3d35-a37b-6fd05ebfa87e | -3.1794 | -50.3922 | 2024-10-29 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1cecb1b0-278e-3b72-a7c7-15a68bfa5ce6 | -3.2503 | -46.8709 | 2024-10-29 01:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| b879f386-a6ff-3838-aa07-4d7246e2b8f9 | -3.3044 | -47.198 | 2024-10-29 01:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |


[Clique aqui para ver as próximas entradas](README20.md)
