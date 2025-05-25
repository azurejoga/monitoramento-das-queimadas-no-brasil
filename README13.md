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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baa4a478-5e43-3228-bbb2-6c0752baebd7 | -8.0507 | -43.1472 | 2025-05-25 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.3 |
| 8e0ad1ce-3124-3dde-af3d-9cd0985b0f3a | -8.0696 | -43.1452 | 2025-05-25 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 4b4efdbd-2563-352a-8c9d-2c14bb6182bb | -8.0696 | -43.1452 | 2025-05-25 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 195.9 |
| 9d0273ea-a056-313b-b8d1-4b2d0bc3294e | -7.6574 | -46.1013 | 2025-05-25 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 278fb0ff-c1e6-3aa7-8e79-3f899a794cd7 | -8.0507 | -43.1472 | 2025-05-25 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 696.0 |
| f2f45ff4-57be-33c5-a2ea-5cc2e0484dd7 | -8.051 | -43.1237 | 2025-05-25 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 249.5 |
| 6bfa0ede-582f-314c-92e2-7d93c841c6f5 | -7.6574 | -46.1013 | 2025-05-25 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 794d0512-210b-34dd-9528-e4a1b81a4b78 | -8.051 | -43.1237 | 2025-05-25 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 212.3 |
| b4eadb4a-b00d-308c-a49a-a35ed3800643 | -8.0507 | -43.1472 | 2025-05-25 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 610.5 |
| e9c9e0f2-77bd-37c3-8be7-4977860cb572 | -8.051 | -43.1237 | 2025-05-25 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 152.1 |
| e0782872-2b3f-3374-97c3-706525bdcef9 | -7.6574 | -46.1013 | 2025-05-25 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 07256741-5443-34a2-a08b-b8a75017350b | -8.0507 | -43.1472 | 2025-05-25 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 399.0 |
| e1f63501-c818-3305-bdec-56d247296637 | -8.051 | -43.1237 | 2025-05-25 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 9bf306ad-9378-3efa-9159-2d93b99a0bf2 | -7.5956 | -43.3359 | 2025-05-25 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 60833609-c597-3b94-a59f-ef7ba987f0e6 | -7.6574 | -46.1013 | 2025-05-25 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 1e3724d1-c7cc-373c-a2df-1e56e4224153 | -8.0507 | -43.1472 | 2025-05-25 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 264.1 |
| 36f046bc-87d7-37be-9fef-87d43788766a | -9.3786 | -48.4106 | 2025-05-25 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 7fdd1f35-9564-37f3-843d-965a5bf08c42 | -8.051 | -43.1237 | 2025-05-25 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.1 |
| b9b664f4-6ca7-31c8-9123-2a1cd83f998c | -7.5956 | -43.3359 | 2025-05-25 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 131.0 |
| e9d990e1-582b-3613-9d77-494c6e240003 | -8.0889 | -43.1196 | 2025-05-25 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| 78d7c4be-90bc-3f33-93de-a2b5757f2e31 | -7.5479 | -45.8192 | 2025-05-25 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 4a397ba7-e998-3765-9217-47bafde52fb1 | -7.6574 | -46.1013 | 2025-05-25 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| e4046bca-033b-3931-ba23-84f45428388b | -8.07 | -43.1216 | 2025-05-25 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 311.9 |
| 71f9dbb6-7572-38d9-87fd-f89a7fbc5dbd | -10.8701 | -49.8766 | 2025-05-25 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 6f19faf0-d089-3e45-b654-618e65ee311f | -8.07 | -43.1216 | 2025-05-25 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 378.4 |
| 7759985c-a922-31f9-acb4-7bb22b889f7d | -7.1985 | -43.4687 | 2025-05-25 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 5484f84a-8c7e-3a93-ba51-05c2e83fc65c | -8.051 | -43.1237 | 2025-05-25 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 178.7 |
| 81647269-d64b-3f75-b094-713da1d719b0 | -7.6574 | -46.1013 | 2025-05-25 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 6a4014f6-de8a-3ac9-9be4-54ef15c43aaf | -7.5956 | -43.3359 | 2025-05-25 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 1960c1e6-4557-35dc-bd7b-6b660ca79c09 | -8.0889 | -43.1196 | 2025-05-25 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 160.9 |
| 88d09c06-2802-3ea4-a60c-97c1be932f53 | -7.5959 | -43.3125 | 2025-05-25 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 9d3d869d-a007-3650-87cb-2bb3479c91e4 | -13.6871 | -45.2487 | 2025-05-25 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 2750db0e-44d5-31df-a6ff-dd1edcca59d6 | -7.5956 | -43.3359 | 2025-05-25 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 38d6b86b-ff72-35a0-ae50-740e7e101df9 | -8.051 | -43.1237 | 2025-05-25 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 196.4 |
| 3e35c6a5-7ac6-315c-b9cb-664d3d8cfd8a | -7.5477 | -45.8417 | 2025-05-25 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 3487337b-3761-37c5-a50e-035a623b8ac0 | -8.0703 | -43.0981 | 2025-05-25 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.3 |
| b5820270-6576-3f4e-8289-dd0ef62b443a | -8.0696 | -43.1452 | 2025-05-25 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 302.4 |
| 3a420eb4-c52d-371a-9b3f-33df4b8a613f | -8.0507 | -43.1472 | 2025-05-25 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 425.2 |
| 40cb1a66-649a-3d8c-b562-28d450d16c17 | -7.6574 | -46.1013 | 2025-05-25 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 38001ccb-10e9-3931-a436-224722d597e1 | -7.5767 | -43.3378 | 2025-05-25 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| f4f6daaf-df6f-33ef-be63-0b71b4080ca2 | -7.5477 | -45.8417 | 2025-05-25 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 715c8b55-f48b-328b-9918-b82159fda23c | -8.0507 | -43.1472 | 2025-05-25 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 503.9 |
| 7378a464-2079-3ef2-b22b-71a99552ef92 | -7.5956 | -43.3359 | 2025-05-25 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 131.5 |
| a60f6b5a-fe1c-320d-b6d9-cc243f2dc459 | -7.5767 | -43.3378 | 2025-05-25 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 4c5153c3-80ea-34b5-83b1-120f036bbce6 | -7.6574 | -46.1013 | 2025-05-25 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| c624f39c-ccad-3b82-8b56-e3e03e6be810 | -8.0696 | -43.1452 | 2025-05-25 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 354.1 |
| e14d2638-e156-38f7-91e8-a716f2375f05 | -8.051 | -43.1237 | 2025-05-25 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 216.4 |
| 0b50db80-1aba-3582-a8c8-1bc183be0dcc | -13.6871 | -45.2487 | 2025-05-25 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 6548fa85-63c2-3ca1-a492-01df9e968f49 | -8.0703 | -43.0981 | 2025-05-25 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 23688187-3f7a-38d1-8fd3-04b5fba3005a | -8.0889 | -43.1196 | 2025-05-25 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 225.9 |
| 02b2e09f-6e35-30c1-b416-3c66f070556b | -7.5959 | -43.3125 | 2025-05-25 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| ea44a135-3490-3506-afcf-dc173a8c0faa | -7.6574 | -46.1013 | 2025-05-25 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| d70add0e-d544-3414-b6d5-21e62f4c4945 | -8.0703 | -43.0981 | 2025-05-25 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.5 |
| 51111c13-2381-37b1-a2fb-9896e75ea5f0 | -13.6871 | -45.2487 | 2025-05-25 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8cb39b9f-3df5-3fd5-a779-cb2deec45e0a | -7.5956 | -43.3359 | 2025-05-25 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| da2135bb-2fe7-358e-92a2-92cd8e17ce19 | -8.051 | -43.1237 | 2025-05-25 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 301.5 |
| 2bb9f70d-21e4-30b4-bd68-5390cc5d31bc | -7.5477 | -45.8417 | 2025-05-25 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c53f217c-f66a-340e-ba58-55d4bd309559 | -8.0696 | -43.1452 | 2025-05-25 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 371.6 |
| 39822af8-c7e3-3ffe-9e57-bf5364084266 | -8.0886 | -43.1431 | 2025-05-25 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.0 |


