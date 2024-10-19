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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 147658a0-3bd3-3713-bd99-d173fc904794 | -2.9489 | -52.897 | 2024-10-19 02:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 389f6116-2903-3aab-9566-a9231994f4ef | -2.9673 | -52.9169 | 2024-10-19 02:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 8e85fec1-36e2-364c-bad6-5da9e2088e03 | -2.9673 | -52.8966 | 2024-10-19 02:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 1098956f-fa78-32c4-a72d-96443550fc80 | -3.4388 | -50.1948 | 2024-10-19 02:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 5a1e3b51-4e07-3b45-98ab-d7b9ea178506 | -3.4202 | -50.2164 | 2024-10-19 02:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| bd75b23b-4df7-3b2c-b5b0-a5dca683d060 | -3.4387 | -50.2158 | 2024-10-19 02:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 95ac52f5-eedc-363a-ba37-b0215f9e0750 | -3.4203 | -50.1954 | 2024-10-19 02:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 73995b7f-2984-3fe0-9085-5714c48e731d | -4.7061 | -45.8269 | 2024-10-19 02:55:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 0a1c44ce-2343-3a67-a01a-2ab001c1b76a | -4.706 | -45.8493 | 2024-10-19 02:55:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 313c2a3d-4fc6-34ac-8fd1-ff0e539280d3 | -9.053 | -67.4451 | 2024-10-19 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 140d394c-95ef-3111-ad25-f3409936c210 | -9.053 | -67.4636 | 2024-10-19 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| f959d84b-a770-3396-b863-bf30e9b7527f | -9.0345 | -67.4455 | 2024-10-19 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 87a7d76e-fc84-3261-a47d-39b17a44006e | -9.0344 | -67.4641 | 2024-10-19 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| e0905e3e-52f5-383d-a46b-783000f0a059 | -7.7024 | -73.05009 | 2024-10-19 03:00:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 21.4 |
| bad3ae87-9389-302f-9476-74a5b2fa1ef8 | -7.6353 | -73.12634 | 2024-10-19 03:00:00 | TERRA_M-M | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 40cdae75-8b28-3579-851c-6e458d985717 | -7.63233 | -73.1071 | 2024-10-19 03:00:00 | TERRA_M-M | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 24.6 |
| a433624f-96c0-37f3-a2f7-355ac57676fa | -7.31707 | -72.76437 | 2024-10-19 03:00:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| dbd04405-1082-3f1c-8100-0ead45f6da53 | -7.31424 | -72.75841 | 2024-10-19 03:00:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 29ad1afb-2e37-3672-86d8-d41b89deb74f | -1.1348 | -49.0421 | 2024-10-19 03:05:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 817ac38a-5f54-3a05-9aef-a4483858598a | -1.1163 | -49.0423 | 2024-10-19 03:05:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 985e8e0d-fd05-3f3f-becd-faafaae0fc6f | -2.7007 | -45.1763 | 2024-10-19 03:05:21 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 5e389180-f5af-3aad-9f89-c5ea4c12e7f3 | -2.8069 | -51.3613 | 2024-10-19 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8f88a695-87d0-31a7-8428-504b511a1770 | -2.9489 | -52.897 | 2024-10-19 03:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| f32d6639-b8cf-302a-b25d-5ded3ff9c817 | -2.9489 | -52.9174 | 2024-10-19 03:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| cd21fd08-bbd7-337b-8f56-a7e6d039795a | -3.4388 | -50.1948 | 2024-10-19 03:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 09f87d62-526e-3b79-9cb5-e98170c2140c | -3.4387 | -50.2158 | 2024-10-19 03:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 9958ff2d-4bb2-3400-a9d5-a930726a1446 | -3.4203 | -50.1954 | 2024-10-19 03:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 460c346b-5b5e-38d3-9c4d-5bbc6e28c584 | -3.4202 | -50.2164 | 2024-10-19 03:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 749260bf-571b-37e3-89a1-7e5c24acaec7 | -9.053 | -67.4451 | 2024-10-19 03:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0f6c3fd2-cbfa-3a5e-80ba-25075e31216e | -9.053 | -67.4636 | 2024-10-19 03:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c268c056-46a4-3a74-a240-6f805ef57c29 | -9.0345 | -67.4455 | 2024-10-19 03:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 50d6e9b2-3d82-3406-b199-06b2f19c8be7 | -9.0344 | -67.4641 | 2024-10-19 03:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 302cfd16-e604-3083-8857-8915cfa80462 | -7.45688 | -35.24822 | 2024-10-19 03:10:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 86b92b74-a040-3e68-a012-7088b71179b9 | -7.45201 | -35.24728 | 2024-10-19 03:10:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7514115d-fa56-34b0-8b14-f6bf9e667bfd | -7.45104 | -35.25273 | 2024-10-19 03:10:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1c2bda3c-d712-3847-8ccc-d2996557b4f4 | -7.44712 | -35.24638 | 2024-10-19 03:10:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 48fb91bd-13e7-3877-9250-b221ed7758d4 | -7.44223 | -35.24554 | 2024-10-19 03:10:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4862ae3b-d6c9-33ae-bfbf-637378e43cff | -5.39471 | -35.86808 | 2024-10-19 03:10:00 | NPP-375D | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a0125c9-1c04-3e89-b768-3221b45aec26 | -5.39413 | -35.87138 | 2024-10-19 03:10:00 | NPP-375D | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ce55d7f-048d-36b6-8be2-ef9d74c04407 | -17.39667 | -41.43111 | 2024-10-19 03:13:00 | NPP-375D | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 87d06e51-0ede-36d8-8514-e3274b78385a | -17.39557 | -41.43617 | 2024-10-19 03:13:00 | NPP-375D | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| dfb6e4f5-22da-30a2-87a1-e683e5cbf800 | -16.86344 | -42.10839 | 2024-10-19 03:13:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5ede0733-0a8c-3300-853f-8cc1652e36aa | -16.66833 | -42.07863 | 2024-10-19 03:13:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 55799b54-7124-303b-a0d3-0a02e9307732 | -16.66714 | -42.08396 | 2024-10-19 03:13:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8e12c763-13c0-3195-bfc3-bb9134accc87 | -15.52548 | -43.1348 | 2024-10-19 03:13:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a87a1108-e6e0-34af-b4dd-43f12b65965e | -15.52058 | -43.13194 | 2024-10-19 03:13:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.9 |
| e9615be2-8f73-38cb-8f2c-67187095ac75 | -15.51912 | -43.13852 | 2024-10-19 03:13:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 003591ed-288e-30dd-bc27-7f9208520991 | -15.51858 | -43.13322 | 2024-10-19 03:13:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 961d13be-f876-3861-8e18-e1475d2b007b | -15.51707 | -43.1398 | 2024-10-19 03:13:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 48d6b278-858b-352b-911a-283b704a99ea | -18.33731 | -41.22316 | 2024-10-19 03:15:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f02656f7-8da0-3c1c-aa8e-9c86fdff427b | -18.33478 | -41.2198 | 2024-10-19 03:15:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 24f967fe-a060-3847-9e97-05f41a1acbaf | -18.33377 | -41.22427 | 2024-10-19 03:15:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d2eb2437-77e1-3cf5-b691-2fa0c5f2bfc7 | -18.33132 | -41.2223 | 2024-10-19 03:15:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5776bc74-8ecc-3b54-8069-10c514eb12a5 | -18.33041 | -41.22651 | 2024-10-19 03:15:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e6cb07b3-d97c-3228-a13d-954707e0af58 | -18.05462 | -41.70238 | 2024-10-19 03:15:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 61275de7-f800-357a-a38f-662e7e204b3b | -18.05359 | -41.70704 | 2024-10-19 03:15:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5a5f6215-4a9a-32b3-8ab7-1b591ff2efa6 | -18.43281 | -42.26384 | 2024-10-19 03:15:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 478cd892-d771-33fd-8206-e311a4e826fa | -18.43176 | -42.26856 | 2024-10-19 03:15:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e0c05190-d3e3-38ba-b3cc-4812837685c9 | -18.42953 | -42.26418 | 2024-10-19 03:15:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| a7fe284c-1b55-3d8d-8018-4b73d2d5b404 | -18.42667 | -42.26197 | 2024-10-19 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d808f2ca-0027-3ca4-9f03-ebfe3f30e545 | -18.42551 | -42.26718 | 2024-10-19 03:15:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b9e35d76-3821-311f-8496-143187d6a47a | -18.25158 | -42.2401 | 2024-10-19 03:15:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1ca29986-5266-3483-b54f-1538bebd1131 | -18.25048 | -42.24495 | 2024-10-19 03:15:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 81f6bbd7-f9d2-3a7c-aa38-d722cbb1305f | -2.8069 | -51.3613 | 2024-10-19 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 7e63f3a3-42b5-3a50-8d7d-a96b292d216e | -2.9673 | -52.9169 | 2024-10-19 03:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f8922d5a-0d5e-3a59-a025-a24116fb19a8 | -2.9489 | -52.897 | 2024-10-19 03:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 1b9bfc87-2bd4-3a84-bab2-8541fb4526cb | -2.9489 | -52.9174 | 2024-10-19 03:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 61ff9c23-379e-32b1-b471-8de92f1ce4bf | -3.4202 | -50.2164 | 2024-10-19 03:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 190.6 |
| 85af3c08-761e-368c-93e9-ad9219ba6fe4 | -3.4388 | -50.1948 | 2024-10-19 03:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 7727f109-f52f-3a81-9f98-255c19b4fba1 | -3.4203 | -50.1954 | 2024-10-19 03:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 50491892-6727-33d5-a2fa-aad79d783bf7 | -3.4387 | -50.2158 | 2024-10-19 03:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 901a40df-9ff6-3e0e-bb67-50118e6e5758 | -9.0344 | -67.4641 | 2024-10-19 03:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ca6101b5-6099-333b-9d7a-171f8a9e3ecd | -9.0345 | -67.4455 | 2024-10-19 03:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 92b73100-bdbc-318c-80c5-3ea4b846d1d8 | -9.053 | -67.4636 | 2024-10-19 03:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 7bb4d521-eafa-39af-8409-49268f0f546e | -9.053 | -67.4451 | 2024-10-19 03:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| cdd3f273-2167-35c1-bf2e-2a61c9f56c5c | -1.1348 | -49.0421 | 2024-10-19 03:25:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0815799e-588a-3f8b-9523-461b547153c8 | -2.5635 | -47.0694 | 2024-10-19 03:25:20 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f51fce41-b341-3ae0-aed0-7c814f861057 | -2.8069 | -51.3613 | 2024-10-19 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| e03924d5-50de-3313-a544-a1fa0e002596 | -2.9489 | -52.9174 | 2024-10-19 03:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 93f952f3-33fe-3f43-bf29-30a2dab8587a | -2.9489 | -52.897 | 2024-10-19 03:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 3a24e938-863e-3ef9-8199-620da2016036 | -3.4202 | -50.2164 | 2024-10-19 03:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 145.8 |
| a1451f73-fe5f-3572-aecd-a09dc896164b | -3.4203 | -50.1954 | 2024-10-19 03:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 87284d79-4d93-3c40-a946-6280e11d09bd | -3.4387 | -50.2158 | 2024-10-19 03:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| c1532501-bb08-3ead-828f-1eee1c33007c | -3.4388 | -50.1948 | 2024-10-19 03:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ddebe214-9d29-3947-8684-93779429093e | -9.0344 | -67.4641 | 2024-10-19 03:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| f4a3887e-b0dc-352d-830a-4453b166a2ed | -9.0345 | -67.4455 | 2024-10-19 03:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 1a71833f-26e8-3ac3-b7d8-ecadf9a68a7d | -11.2854 | -54.2369 | 2024-10-19 03:26:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 30f4e74e-27ae-31bf-b687-c25fbe399283 | -5.8975 | -35.43528 | 2024-10-19 03:34:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 018cd918-fb91-3938-a509-ef912639e4d3 | -7.37753 | -34.88557 | 2024-10-19 03:34:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 90a0b4b6-76fe-32bc-94b9-8a015c7a393f | -5.39411 | -35.86778 | 2024-10-19 03:34:00 | NOAA-20 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67025edb-8600-3a1a-be77-b443af7afa70 | -5.39349 | -35.87169 | 2024-10-19 03:34:00 | NOAA-20 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b4f287e-a256-3833-9fc2-82767fc6ce85 | -10.43614 | -36.82839 | 2024-10-19 03:34:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f89a496e-1611-3fb6-9da7-bcd242dcde01 | -5.25236 | -37.50507 | 2024-10-19 03:34:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5de07a7b-a47e-3ded-84ab-1d8919c8737f | -5.25158 | -37.50975 | 2024-10-19 03:34:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ffbe0f1c-c3c3-30b2-b776-71a2ea15386f | -5.24854 | -37.50444 | 2024-10-19 03:34:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 624f360a-a8d4-3287-8b70-0dcc50c75d8b | -3.43731 | -39.22341 | 2024-10-19 03:34:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c90935b7-129c-3c76-9eea-6e6b9d9d56e7 | -3.43706 | -39.22507 | 2024-10-19 03:34:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 939be2ad-2464-351c-941a-516eb356fcdb | -3.56496 | -42.0388 | 2024-10-19 03:34:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e7d8f98c-9469-3195-bc8b-23199170c64c | -3.5644 | -42.04213 | 2024-10-19 03:34:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7287bb70-caf4-345b-84f2-d23d92ae34c4 | -3.55967 | -42.03778 | 2024-10-19 03:34:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README13.md)
