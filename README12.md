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
| deb3cdf5-aaff-3f4a-8c38-175ac2c013ff | -4.7004 | -60.8077 | 2024-10-12 01:05:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 312daf81-370d-3713-8867-3c998c66b3ff | -4.7188 | -60.8072 | 2024-10-12 01:05:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 9bdc68c8-1257-32c6-adda-7e9fa0a0d7dd | -4.7188 | -60.7882 | 2024-10-12 01:05:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 401a4408-0dcd-3bcc-be0d-80a00d128ac3 | -4.7371 | -60.7877 | 2024-10-12 01:05:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 450d2ceb-7503-389a-b6e8-f6c35253da3e | -5.1919 | -48.1756 | 2024-10-12 01:05:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 98f33b47-b481-3794-a8b2-36b1db03858d | -5.2105 | -48.1745 | 2024-10-12 01:05:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| fe26beb9-cdcd-31bb-bccf-4d1da540ddd8 | -6.0791 | -44.6276 | 2024-10-12 01:05:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 51b739b1-c69d-3016-b6a8-c78e808738b4 | -6.7284 | -59.346 | 2024-10-12 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f3ecdc0a-47ec-3103-932b-c60460007d48 | -6.7285 | -59.3267 | 2024-10-12 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 9da66b92-9138-397e-9138-bf658e56d580 | -6.7469 | -59.3452 | 2024-10-12 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.8 |
| fcd8a738-ff67-3159-8279-71117a45e47a | -6.747 | -59.3259 | 2024-10-12 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 224.2 |
| 0c804ffa-5437-3ab4-a719-33f2c5f6dde9 | -6.7653 | -59.3445 | 2024-10-12 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 28ed7206-dace-3867-9abb-f978718dcbed | -6.7654 | -59.3252 | 2024-10-12 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 8525569e-78c8-3611-920b-12d72f6a1929 | -8.9667 | -62.3506 | 2024-10-12 01:05:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 93e6850b-64fd-3606-b51a-339bb95d9035 | -9.9304 | -36.287 | 2024-10-12 01:06:01 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| 15135b5f-4844-34e4-bcda-6d4f311b65dc | -10.3708 | -61.232 | 2024-10-12 01:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 3f45039a-e11f-367d-8cb1-f422bcb829de | -10.3892 | -61.2695 | 2024-10-12 01:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 256fa576-121f-392f-a71c-0f1bf920c017 | -10.3895 | -61.231 | 2024-10-12 01:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 4f7570b9-75c7-37cd-8fec-96afda35ebc8 | -10.3897 | -61.2118 | 2024-10-12 01:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 6ec3a04c-938b-385a-a030-2031516b5568 | -10.3898 | -61.1925 | 2024-10-12 01:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| b824f9f4-689f-324d-bc08-f5bb05077e34 | -10.4079 | -61.2685 | 2024-10-12 01:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 48515972-4fe7-30d5-83e4-faaebd17c606 | -10.5328 | -51.0425 | 2024-10-12 01:06:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 34b529f3-2a32-3ca3-8b93-608b07209354 | -10.9506 | -44.653 | 2024-10-12 01:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 87bbb98c-7dcc-3093-b56b-2885cc037ced | -10.8362 | -64.2027 | 2024-10-12 01:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 179dae86-f145-37e9-83e4-29a28e869dee | -11.2761 | -60.5038 | 2024-10-12 01:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 4a49bf38-ada7-32c9-81ca-311385e7a5f5 | -11.2763 | -60.4844 | 2024-10-12 01:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7b150c45-3075-3b27-a4dc-c56fbec4d1b6 | -11.8375 | -58.8642 | 2024-10-12 01:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 45537594-86f4-33cb-aa93-fba880c40166 | -11.8377 | -58.8445 | 2024-10-12 01:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 01c4dd82-5f1d-3b2c-a3ad-bca906ab4c88 | -12.6034 | -48.6209 | 2024-10-12 01:06:17 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9d4c2fe0-bab6-38b1-b158-648d8dc65476 | -12.6038 | -48.5988 | 2024-10-12 01:06:17 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 33b210d7-95b7-3f4c-9eeb-c237a0bb602f | -12.9655 | -53.5319 | 2024-10-12 01:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| f8944488-ad9c-3b0a-a45d-c979a08dc908 | -14.3246 | -57.6002 | 2024-10-12 01:06:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 202.9 |
| aa06c9a1-b927-3fa7-ba6c-9893f2e13c57 | -14.3249 | -57.58 | 2024-10-12 01:06:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 164.4 |
| 7e45ce14-854a-381a-909c-184ee9dca4bf | -14.3438 | -57.5983 | 2024-10-12 01:06:28 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 166d98c6-b135-3339-b0f1-e13db7e1df68 | -14.3441 | -57.5782 | 2024-10-12 01:06:28 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| fc6a8eb5-9473-3459-8582-6db6029edd5e | -15.0524 | -45.073 | 2024-10-12 01:06:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 67fbdd71-1722-380e-82e7-a27ca39a001a | -16.9802 | -57.4609 | 2024-10-12 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| c0ed8884-64ff-3116-89ff-0518c9ab8163 | -16.9805 | -57.4404 | 2024-10-12 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 23ff047a-b5ae-3010-9c03-28261874bfae | -16.9998 | -57.4586 | 2024-10-12 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 2af90cef-5c10-3462-8f60-dcd92862ad5e | -17.1758 | -57.479 | 2024-10-12 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 12b2f77e-a371-3ad1-baae-b28af7d1bd9c | -17.1761 | -57.4585 | 2024-10-12 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 4813fe04-705d-34d3-9bbb-9d81abdd78f5 | -17.627 | -56.3318 | 2024-10-12 01:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.2 |
| f7a94fd7-e91f-35fa-92c5-b9e6bba3a9b6 | -17.6273 | -56.311 | 2024-10-12 01:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| a6260162-d5e5-37bc-9532-a92b2124e7bc | -17.6467 | -56.3292 | 2024-10-12 01:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 179.4 |
| 4b4db58f-862d-3613-86ce-449aeb7ff239 | -17.6471 | -56.3084 | 2024-10-12 01:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| a9365df5-0517-35ec-b3cf-b0b2b9c24c29 | -17.964 | -57.3843 | 2024-10-12 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| bc72b102-d321-3807-b0e5-e056e3cdf724 | -17.9643 | -57.3637 | 2024-10-12 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| b35008f8-f5b3-3d84-89bc-8e6ef234ce3e | -17.9837 | -57.3819 | 2024-10-12 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.9 |
| c4b0002d-1ef9-3e04-86c3-44697024dae0 | -17.9841 | -57.3612 | 2024-10-12 01:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 00c3cd52-65c6-3676-a402-7f9cdea34f18 | -18.196 | -56.5275 | 2024-10-12 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 39cf07d8-83df-3d3d-bbb0-e4b245ad69bb | -1.5877 | -53.3494 | 2024-10-12 01:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5b9880bf-c5f5-34db-86e1-322c53730f08 | -1.6061 | -53.3492 | 2024-10-12 01:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 2003c2c7-dcbf-3b97-b924-0a5370e7f7de | -2.77 | -51.3829 | 2024-10-12 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 1a5eeab5-50e8-36ab-9f49-1fcc26d09afe | -2.7701 | -51.3622 | 2024-10-12 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| cc30269c-ecce-3bf5-afaf-53dc0aad938a | -2.7884 | -51.3825 | 2024-10-12 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| d7256298-8ef2-3290-bce2-96d0cf251098 | -2.7885 | -51.3618 | 2024-10-12 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| f734befb-0102-3f5c-9e43-836de0976522 | -2.8319 | -49.5385 | 2024-10-12 01:15:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f3668329-8145-3fc9-9d61-e31eba843a3f | -2.832 | -49.5173 | 2024-10-12 01:15:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b242278f-6feb-3b7e-ba3a-1326ed1ea324 | -3.0311 | -50.5642 | 2024-10-12 01:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| d72d1909-42fa-39d8-b14f-3d542f9a4a57 | -3.1426 | -50.3724 | 2024-10-12 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 390ad452-bc1d-3013-9a92-9591a641e2ed | -3.1427 | -50.3514 | 2024-10-12 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a6cbf647-e811-3825-a416-68afac052bb8 | -3.161 | -50.3718 | 2024-10-12 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 2f1877cb-61aa-318a-ac72-8129e0f9d523 | -3.1611 | -50.3508 | 2024-10-12 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| cdb34922-e233-3109-94f3-405c883ea4ea | -3.2136 | -46.7843 | 2024-10-12 01:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 00f6a160-b1ff-39d7-bd06-afc4ac7a1050 | -3.2137 | -46.7623 | 2024-10-12 01:15:24 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 5f093152-68f1-3e01-be15-f015beb20df7 | -3.6901 | -47.9234 | 2024-10-12 01:15:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| a657daec-37b0-3799-81e5-060c12bc75c8 | -3.7087 | -47.9227 | 2024-10-12 01:15:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 2a73622f-1676-31ef-93c6-5f97d87ef57e | -3.9396 | -46.4229 | 2024-10-12 01:15:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 40.8 |
| c5afcf65-12f1-378a-b7d8-2ad2b441a690 | -4.2665 | -50.9594 | 2024-10-12 01:15:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| ba7a42f4-1f45-3167-88c5-21bf054ffc89 | -4.285 | -50.9586 | 2024-10-12 01:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 408d5294-bbcb-3b6c-9c83-7e53951faa82 | -4.3782 | -50.8087 | 2024-10-12 01:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 84ea7e92-7be3-31a0-8e8d-1d8323f7c54b | -4.7188 | -60.7882 | 2024-10-12 01:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| ce8d8b6c-5841-3c91-81a8-ee8207e8a104 | -6.0791 | -44.6276 | 2024-10-12 01:15:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| a1ce84ee-0f19-3a37-bc33-d1e1c76366ce | -6.7285 | -59.3267 | 2024-10-12 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 24232670-608a-3832-85e8-e54b796afe8c | -6.7469 | -59.3452 | 2024-10-12 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 6bb202db-e9ba-3c4e-8b5e-c593e8eef2d9 | -6.747 | -59.3259 | 2024-10-12 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 250.6 |
| 44424114-7d1a-3778-b773-a6b23531f6d3 | -6.7471 | -59.3067 | 2024-10-12 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 7dfa881c-c481-395a-9621-03ecfad252e9 | -6.7654 | -59.3252 | 2024-10-12 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 0513b01f-0516-31ab-9ce7-44d4667059d3 | -6.8591 | -59.0705 | 2024-10-12 01:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 92ddd50d-5930-337a-b779-361629fe4562 | -6.8776 | -59.0697 | 2024-10-12 01:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 3273564e-9ee8-36a4-a5e9-d8d0916641c3 | -9.9304 | -36.287 | 2024-10-12 01:16:01 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| a9bcaa22-7e2c-3fd5-ac28-7cfd4d37948f | -9.9497 | -36.2836 | 2024-10-12 01:16:01 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 59.4 |
| 03a6a532-1260-3831-b288-d2e5975182c3 | -9.8815 | -64.8072 | 2024-10-12 01:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 87172ce7-4013-3646-a76b-d67b255464e3 | -10.3708 | -61.232 | 2024-10-12 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ba4bb6ec-0f26-3cd4-9ce1-694a9b655701 | -10.3892 | -61.2695 | 2024-10-12 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 8c53f3ba-d669-30c0-8ab3-0a6c16da6781 | -10.3895 | -61.231 | 2024-10-12 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| c34b70b7-cdb0-31e7-939a-6c5e381ff133 | -10.3897 | -61.2118 | 2024-10-12 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 977e2555-d9b2-3039-a4ce-30022e4c8304 | -10.3898 | -61.1925 | 2024-10-12 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| ba1d1dae-990a-3f5a-a13e-e06e2266c116 | -10.4078 | -61.2877 | 2024-10-12 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 8164c4a0-cc95-381a-827d-ed6cbda8c86a | -10.4079 | -61.2685 | 2024-10-12 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| dcac62a7-3133-3f65-afb7-5bef4acafa8e | -10.9506 | -44.653 | 2024-10-12 01:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 3de7007f-477a-3711-9197-fca3166cc369 | -11.2761 | -60.5038 | 2024-10-12 01:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b5ac4e37-9a88-352a-92a5-f69bb6b6289c | -11.8375 | -58.8642 | 2024-10-12 01:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 4dc12ccf-d1e1-38f3-90e9-0a6b5850b082 | -11.8377 | -58.8445 | 2024-10-12 01:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 133ccf8d-9f21-39b9-9fb0-e1c2d213051e | -12.6034 | -48.6209 | 2024-10-12 01:16:17 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 66464a41-8926-3a88-aec9-6eb81948b10e | -12.7866 | -44.8873 | 2024-10-12 01:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 96e86f2f-70c7-3a58-aa31-840c7bc05ba6 | -12.7871 | -44.8639 | 2024-10-12 01:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 211.3 |
| f66b98b1-7397-3a25-b654-033422d9b93d | -12.7875 | -44.8406 | 2024-10-12 01:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 47affd2c-09b8-398b-a2b5-f810ef640d79 | -12.806 | -44.8841 | 2024-10-12 01:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 775e1ef4-ed75-3add-80b4-6630c09aa451 | -12.8064 | -44.8608 | 2024-10-12 01:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |


[Clique aqui para ver as próximas entradas](README13.md)
