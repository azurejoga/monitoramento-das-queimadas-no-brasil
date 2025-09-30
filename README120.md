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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c3734b7-4785-302f-bada-272562970ec7 | -8.1616 | -46.3675 | 2025-09-30 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 338fa513-617e-3419-81c6-844067277e40 | -6.5599 | -43.4105 | 2025-09-30 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 262f0888-8495-3122-851f-7aa31d3a80b9 | -11.1753 | -47.2358 | 2025-09-30 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| c1e8a7cf-bae7-3745-87d1-24d6b286a76b | -8.1428 | -46.3693 | 2025-09-30 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| aba56b40-94e4-38e8-ad58-f41832b0900d | -10.6423 | -48.5802 | 2025-09-30 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e948667a-98fe-3d7a-9997-412174353049 | -12.7634 | -50.5136 | 2025-09-30 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.5 |
| b138e697-69a8-398d-993d-f9cd90020001 | -11.252 | -47.2037 | 2025-09-30 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 9af7123d-38d6-336e-935e-293054abab93 | -9.8662 | -45.9145 | 2025-09-30 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 58bab555-287f-3deb-8c8f-67b825692463 | -15.9273 | -46.2101 | 2025-09-30 14:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 222.9 |
| 17964066-634d-3a22-b4bb-3927d789c400 | -14.7361 | -45.2489 | 2025-09-30 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 297.1 |
| 42af7bb7-96fd-3f79-9721-b03e88ba024f | -9.8852 | -45.9122 | 2025-09-30 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 257101b5-a1fd-3e48-a854-35525fbe082e | -12.863 | -46.9582 | 2025-09-30 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 0b2c5209-7b1c-331d-8b9f-cfa0ec682083 | -12.2348 | -47.7863 | 2025-09-30 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| ccf188d1-ee08-3a57-8514-85b86102329f | -12.4058 | -50.1708 | 2025-09-30 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 302.6 |
| 3c495679-4a0a-3326-8fc7-6f277138362c | -6.0813 | -42.4407 | 2025-09-30 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 5433769d-7aa4-3c90-b8b8-402ef4d52534 | -7.7416 | -46.9626 | 2025-09-30 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2a11c3ce-3deb-34a8-aee5-17b830d96c07 | -7.8375 | -46.7766 | 2025-09-30 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 3856a2e5-3e2e-351b-ae14-5420b8c2e6ab | -11.1948 | -47.211 | 2025-09-30 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| d166c79e-44e8-3dc8-a902-b0fc5882060d | -5.826 | -45.7334 | 2025-09-30 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 147a466b-7791-30ca-8a06-c39174a00132 | -15.7917 | -43.6672 | 2025-09-30 14:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 427.8 |
| b6b95770-dde1-3327-9d86-d86d64886343 | -7.8348 | -47.0207 | 2025-09-30 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 6e73080b-e458-3c38-aef8-06313099d8c1 | -5.2869 | -43.1613 | 2025-09-30 14:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 8536a264-a19b-3f01-a9ab-344fe8803340 | -6.5042 | -45.2085 | 2025-09-30 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 7efde854-1cd3-3fad-93d7-d34f2816435f | -11.1548 | -54.1054 | 2025-09-30 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 6e571787-05a8-3ad4-8780-3e2e712c517c | -9.7681 | -46.1519 | 2025-09-30 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 6ff7eb1b-b125-399a-87cb-3ea2157188d9 | -5.8428 | -45.9564 | 2025-09-30 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 47ac2a5a-2eef-316b-9d88-951c998f00c6 | -7.8696 | -47.2606 | 2025-09-30 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 182.4 |
| f186def7-67d3-361a-88e0-4b5c98660fb8 | -13.8264 | -47.9794 | 2025-09-30 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 0cab6b3f-759f-3ff4-a8eb-94c3100a6475 | -9.8198 | -47.8606 | 2025-09-30 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 213352d2-6685-376c-a308-c85808e2c1bd | -5.843 | -45.934 | 2025-09-30 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 474080a4-a9b8-3dac-abb1-33c5d97aa322 | -5.8445 | -45.7545 | 2025-09-30 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| aafb344b-33f5-3b6a-85bd-795cf4e992a9 | -5.7681 | -43.8235 | 2025-09-30 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| fba9d2e4-557d-3947-98e5-7fa9baf160ba | -8.2474 | -45.5037 | 2025-09-30 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 8ae553aa-810c-3cca-bc0d-03fad0990dbd | -17.7149 | -46.6631 | 2025-09-30 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 99.0 |
| dbb54f2a-4dc7-350a-bcb0-de17420a58db | -8.672 | -47.7144 | 2025-09-30 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 6a7a7f30-c68e-3e2e-922c-308036ce3548 | -15.9268 | -46.2334 | 2025-09-30 14:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 219.4 |
| 7cd7fc15-7398-38c4-8dc2-39c312774251 | -11.1181 | -49.7629 | 2025-09-30 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 4c3df0a2-4122-3389-bc11-d37f76e70ab3 | -5.8616 | -45.9327 | 2025-09-30 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| f75dbd1d-0667-31b4-ba0f-42b06db68da7 | -5.7599 | -42.6797 | 2025-09-30 14:10:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| 050c0c48-0599-3b33-bc68-39b39af85844 | -5.7411 | -42.6812 | 2025-09-30 14:10:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 302.2 |
| a5948f60-1f4e-3b4f-92e8-394d0d88d87b | -10.1234 | -47.783 | 2025-09-30 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 89512269-6b55-3637-9f5d-0836ca5eb403 | -13.8259 | -48.0018 | 2025-09-30 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 891cc8c0-815b-31e3-bdcf-02e5a8fb7037 | -9.4206 | -54.5753 | 2025-09-30 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 210.7 |
| 49c5a860-f557-38dc-9f47-c509c6f111bd | -9.939 | -55.1632 | 2025-09-30 14:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 30755ee1-8abd-361a-b5a7-c666a3b63496 | -7.5146 | -45.4385 | 2025-09-30 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 6f555493-525e-3df7-b3ff-f1a377cfaf67 | -13.3603 | -48.1605 | 2025-09-30 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| fd85e918-ba0a-31e7-9a89-31ca70b51c0c | -9.1248 | -47.6256 | 2025-09-30 14:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 21612a76-a2ce-3903-89e1-50db50e4c9ab | -12.952 | -48.4185 | 2025-09-30 14:10:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 343a8167-5325-398e-9b30-cf6741ebddab | -10.1855 | -44.8709 | 2025-09-30 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 3441e765-30d8-3a31-ad1e-e19c1202a830 | -7.2996 | -42.8722 | 2025-09-30 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| abbd85c6-b214-30dc-ac1a-54371563dc97 | -11.071 | -47.8262 | 2025-09-30 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2d332885-aa99-3012-bb1d-3b90f1d518c4 | -10.3058 | -48.2681 | 2025-09-30 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 3faf6ec0-a0e4-3590-ac1d-656d94dc2613 | -18.1981 | -53.2993 | 2025-09-30 14:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 033f7877-7ce6-3948-bd07-103f796d7803 | -9.1246 | -47.6476 | 2025-09-30 14:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 58ab4b09-89cd-3f25-9b48-27bf2d5dc42c | -18.2176 | -53.3177 | 2025-09-30 14:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 318.9 |
| 6138b2da-3625-3906-9295-c9d622965662 | -8.874 | -46.6092 | 2025-09-30 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 8a43d7b6-ce44-35ec-8e1d-8d0d67d06adc | -15.1688 | -52.8241 | 2025-09-30 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 2cc89565-50aa-36cb-93f4-ed62f49a41fb | -11.2138 | -47.2086 | 2025-09-30 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 854b9775-2d61-3bb0-8462-968f76a227be | -14.5141 | -48.4299 | 2025-09-30 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 3945a239-59c4-3187-80c7-8f9f8b0fd2cb | -7.8378 | -46.7544 | 2025-09-30 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 5e991dae-11c4-3b5f-a57d-b565ff746fa0 | -6.4948 | -44.2732 | 2025-09-30 14:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| e5c1d330-2484-3836-8547-45f3419768b1 | -6.4948 | -44.2732 | 2025-09-30 14:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 37d772e4-902d-3c5d-bf81-7c3c5f2fb97e | -15.9071 | -46.2371 | 2025-09-30 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 1eb55ec2-c4a9-3a93-ad6c-a2d3afb3c105 | -6.5042 | -45.2085 | 2025-09-30 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 49af11ce-b366-3d5a-8078-14f97f1f0a43 | -10.1045 | -47.7851 | 2025-09-30 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| a973d7d6-a357-3d65-8394-33baa177d3fe | -12.3867 | -50.1731 | 2025-09-30 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 1cc061af-90ef-3288-93d4-8cd5a89808be | -18.2176 | -53.3177 | 2025-09-30 14:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 287.1 |
| 4ef77975-7f63-3e8a-a568-5cb7873583dc | -7.8378 | -46.7544 | 2025-09-30 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| a48470fe-b622-3ac7-84b9-73b4f2cc6022 | -15.1684 | -52.8453 | 2025-09-30 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 539429cb-7031-3f74-bd8b-1bf6d852e6e4 | -11.1548 | -54.1054 | 2025-09-30 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 5be16e43-e439-3eaf-a2bc-124a0624187d | -10.8055 | -45.3637 | 2025-09-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 2524d057-b439-391f-bb66-857f7d79e981 | -6.8148 | -45.9947 | 2025-09-30 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 853d0d13-c4c3-3b3a-8ebb-92a3d2174c13 | -15.9268 | -46.2334 | 2025-09-30 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 254.4 |
| 8285bab5-1562-3527-9c47-bb952b5c2ff1 | -10.0531 | -50.1978 | 2025-09-30 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| c4ca318e-c41d-318e-ace1-4acc8efc9b86 | -14.5853 | -45.0197 | 2025-09-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 03834f48-c077-38c5-9d3c-0cfff36f05e1 | -18.1977 | -53.3208 | 2025-09-30 14:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 785d1ab0-599c-3066-b96b-5a7a5ed99d93 | -7.0478 | -45.2083 | 2025-09-30 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 87da63bf-5a15-3198-a830-ce521363de48 | -14.6049 | -45.0161 | 2025-09-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 1d28f34e-f0f7-322a-b21c-9b95ae095c6e | -7.2996 | -42.8722 | 2025-09-30 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.6 |
| 51910625-ba1b-3701-bf04-5f8f52d0c188 | -15.6272 | -49.1837 | 2025-09-30 14:20:00 | GOES-19 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 63c68b6b-9410-366d-bac5-7b25b8e04b25 | -6.7963 | -45.9738 | 2025-09-30 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| d276e9c6-1204-3404-a182-a0557953a0f8 | -5.7698 | -43.638 | 2025-09-30 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| f0d46cf8-55da-3878-a301-25cfaf797468 | -10.0717 | -50.2173 | 2025-09-30 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 337eeb8c-8981-3575-b010-c3e684144051 | -9.8845 | -45.9576 | 2025-09-30 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 200.9 |
| ac5828cd-0ec1-3f2c-99e5-bd18262a6152 | -5.8428 | -45.9564 | 2025-09-30 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 8f31da7d-db86-30b7-bded-795d667e17eb | -11.2711 | -47.2012 | 2025-09-30 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 8831b08a-aed0-3305-a8db-03e96607b434 | -11.1944 | -47.2334 | 2025-09-30 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 5d75b021-a213-3b66-bfcc-483965b1a4d5 | -12.2348 | -47.7863 | 2025-09-30 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| ea1deda0-b68b-30c6-b235-3610507dcd30 | -10.6423 | -48.5802 | 2025-09-30 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 53d68b40-2dfa-39ed-9f6b-5bca6b2b4178 | -12.7018 | -45.2947 | 2025-09-30 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 4ff5d025-63c5-3769-9e03-cb88d0a74ba8 | -10.6419 | -48.6021 | 2025-09-30 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 09d5bac8-1cfd-37b5-978a-5e4b0c5b61f5 | -7.1815 | -41.6931 | 2025-09-30 14:20:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 79d3c24d-77de-3ac4-9884-b923d8b78121 | -6.098 | -42.6521 | 2025-09-30 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 94a7db32-3481-3168-8c9a-df5a7e0d9585 | -8.5407 | -44.6745 | 2025-09-30 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 86264e84-f1fc-3b64-9262-689244857725 | -7.8696 | -47.2606 | 2025-09-30 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 195.0 |
| b8a5070f-f134-347b-b109-ff5bc11918c6 | -9.1248 | -47.6256 | 2025-09-30 14:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 549ffc4d-d6ef-3cbc-9396-bceb2a38b7c9 | -10.0342 | -50.1997 | 2025-09-30 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 93350478-3e76-3552-ad9f-552301452402 | -6.2996 | -45.066 | 2025-09-30 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| f8f7e019-af6d-3fa1-9e98-23d22aeb65e8 | -11.2707 | -47.2236 | 2025-09-30 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 0a00f265-b306-3044-91bb-42c0e878042b | -13.8264 | -47.9794 | 2025-09-30 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |


[Clique aqui para ver as próximas entradas](README121.md)
