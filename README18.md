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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 774a22df-c520-38aa-96c1-428b7f410b86 | -8.9709 | -61.6842 | 2025-08-16 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 6f4020a1-c3e3-34c6-becc-b77466a59a9e | -14.9632 | -54.7143 | 2025-08-16 03:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 35674461-7732-3268-b96b-35f4de84a6cd | -6.9487 | -59.5297 | 2025-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| bdd77e2c-bec1-3847-9747-3ae86db51474 | -9.5179 | -60.5461 | 2025-08-16 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7d43d6b3-4b12-37a6-bc67-1f866a0c9269 | -7.9149 | -61.7288 | 2025-08-16 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 80757b48-2e53-3ce5-a5ce-7585a9a485a5 | -20.0725 | -49.4271 | 2025-08-16 03:20:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.2 |
| bb197a8b-910e-3d37-8d92-c6518b1e097d | -9.4994 | -60.5278 | 2025-08-16 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6594f865-ae64-30bb-bdab-ee3a234404ab | -14.9435 | -54.7374 | 2025-08-16 03:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d82f629c-44b6-3262-af91-989bc8fae3bd | -14.9438 | -54.7166 | 2025-08-16 03:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 206abbea-7121-3d07-abb7-da6a8e7aa0a9 | -14.9628 | -54.7351 | 2025-08-16 03:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 248715fc-b9b2-3560-8202-2b274b657c57 | -7.9148 | -61.7478 | 2025-08-16 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| cf95d07c-cbdd-350d-ad15-c83f6f80bee3 | -14.9441 | -54.6959 | 2025-08-16 03:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ff45569d-b261-36da-9b69-0401d680141d | -7.0796 | -59.2351 | 2025-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 2cd34e03-2f57-3c4f-8569-a0dedc253056 | -14.9632 | -54.7143 | 2025-08-16 03:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 4d10d1b5-d5a9-334a-810c-66e42c187903 | -8.9709 | -61.6842 | 2025-08-16 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 0b23a8f2-dc49-34d3-b440-3697d65fc3f2 | -6.9302 | -59.5497 | 2025-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| e10cb48e-cd5f-3b7d-aeb8-6da90515a110 | -9.518 | -60.5268 | 2025-08-16 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 0b423e3c-2a72-35bc-9c3d-ae0d9927c053 | -7.9148 | -61.7478 | 2025-08-16 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8dcd7baa-c392-3852-bbc0-9685c1268e06 | -9.5179 | -60.5461 | 2025-08-16 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b81f319b-d70e-3f7a-9fd6-b8a7935a2308 | -6.0807 | -59.9465 | 2025-08-16 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 685ed601-cafe-373c-9213-d6d26f0b24c3 | -6.9486 | -59.549 | 2025-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| cffdfdd4-357c-3533-b50f-741b4346439c | -9.4992 | -60.547 | 2025-08-16 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1260bce9-215f-3ca0-b9a4-f850642d7476 | -14.9628 | -54.7351 | 2025-08-16 03:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| eb776009-7b4f-375e-aafc-7548df753308 | -9.1708 | -59.6568 | 2025-08-16 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| f1e4111c-efa6-3725-b15c-2744e04e426e | -14.9441 | -54.6959 | 2025-08-16 03:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 4637bdd3-4587-3f49-8c4b-7dce1f8a630d | -14.9438 | -54.7166 | 2025-08-16 03:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 705c36a8-72ff-3a77-af19-9b98e6c56778 | -9.1523 | -59.6384 | 2025-08-16 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 284150cb-fdab-3f31-8598-ea0632266ab6 | -20.0929 | -49.4228 | 2025-08-16 03:30:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| 010c97f7-c047-3280-a0f3-bd0ef4c43d8e | -14.9435 | -54.7374 | 2025-08-16 03:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f67f6058-85c5-3334-b4f0-b3f67168692f | -6.9487 | -59.5297 | 2025-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| abe6af7c-38cb-352e-a8a1-46a68e58547a | -9.1709 | -59.6374 | 2025-08-16 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 9fa5a1cd-761a-316f-96a5-812fcfc8d480 | -8.9708 | -61.7033 | 2025-08-16 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 182f94c1-1591-39fa-b8e0-d279a35bf4a1 | -6.9303 | -59.5305 | 2025-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| b15cde09-4833-38c0-8a3c-d1e51b3e6030 | -9.4994 | -60.5278 | 2025-08-16 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 03d07045-eb00-369d-b770-b999ed1c21dc | -7.9149 | -61.7288 | 2025-08-16 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b69cba0b-e2a3-3c40-8942-e0611a8a32f8 | -7.0796 | -59.2351 | 2025-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b1463cd0-89ed-3b28-b993-528d8984df04 | -9.518 | -60.5268 | 2025-08-16 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 76533079-f4f1-328c-898d-274b33fb100b | -14.9628 | -54.7351 | 2025-08-16 03:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 548042ae-36e4-3eda-becf-1777d289300a | -9.1709 | -59.6374 | 2025-08-16 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8af7aac7-7df2-3458-9c71-154e6aa78503 | -14.9438 | -54.7166 | 2025-08-16 03:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| fe985361-8971-3726-8415-2e679db17adb | -6.9303 | -59.5305 | 2025-08-16 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 1f847a26-87b3-3b72-b475-7fce8ab2eb90 | -8.9708 | -61.7033 | 2025-08-16 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 6722a394-b091-32d8-875c-2480a1b6f108 | -7.0796 | -59.2351 | 2025-08-16 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 52c38988-fb07-3a50-b83f-fea95ab20ea5 | -14.9435 | -54.7374 | 2025-08-16 03:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 2659d712-6f4c-32d9-8cbb-35b45de40279 | -8.9709 | -61.6842 | 2025-08-16 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 12fce0c2-f989-3110-8caa-471679e12401 | -6.9486 | -59.549 | 2025-08-16 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 06a79fa5-5f5f-3c7b-8254-2416b6941caf | -7.9148 | -61.7478 | 2025-08-16 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 50fe68c8-2b4e-3512-a3dc-e87732f94f04 | -9.4994 | -60.5278 | 2025-08-16 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 10421455-694e-3c64-b38d-f6cfae3f1eb4 | -14.9441 | -54.6959 | 2025-08-16 03:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| a3c14e8b-123b-3684-b0c6-3130ebd74783 | -6.0807 | -59.9465 | 2025-08-16 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 7e647590-e247-3d1a-964c-76ea0781c32a | -8.9706 | -61.7224 | 2025-08-16 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| a6a05d12-dc46-3fe7-9b8c-9211ec0fa17a | -14.9632 | -54.7143 | 2025-08-16 03:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| d180ad76-f93d-3469-878b-7a5c5a5d8a37 | -9.5179 | -60.5461 | 2025-08-16 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5033bc70-3d78-390b-8c1f-cf2ef798306d | -6.9487 | -59.5297 | 2025-08-16 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3f86b263-418b-3573-8ee5-fbb859743784 | -4.9305 | -43.2558 | 2025-08-16 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a3cc4e22-5f23-34ae-a5ab-b53785138d49 | -9.4992 | -60.547 | 2025-08-16 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 532bc7bb-4e15-3568-a6d0-f2006efe51e7 | -6.9302 | -59.5497 | 2025-08-16 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 21a2f196-cb03-3fce-8332-ba4799cfc08f | -9.1708 | -59.6568 | 2025-08-16 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 13cf302f-df5c-34e5-ba7a-8d77fe38f703 | -4.9118 | -43.257 | 2025-08-16 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 174839fc-4b54-30de-9bea-77219cc78edf | -14.9248 | -54.6982 | 2025-08-16 03:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 57c54084-69e6-337c-bb13-f472b83eb442 | -7.9149 | -61.7288 | 2025-08-16 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 356461bb-54d8-384c-a0a8-a8a63d16a7b1 | -6.35703 | -44.69576 | 2025-08-16 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 92e45a06-a314-3560-aae1-1984cfa367fa | -2.96849 | -40.2411 | 2025-08-16 03:42:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc03e2f9-8272-348d-acb9-d597ac707ccd | -5.75475 | -46.67459 | 2025-08-16 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c0297ab1-20f7-3901-affe-02d2a8c60e83 | -3.83104 | -47.74241 | 2025-08-16 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a75d4386-f087-31bf-a443-a1f2093ba9a4 | -6.54683 | -43.05811 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9952527b-b500-3ca0-accb-3054e51aa00c | -6.92048 | -44.16732 | 2025-08-16 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63f0c302-a894-336e-9590-0e6d481317d5 | -5.76177 | -46.67096 | 2025-08-16 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c93b3773-3b22-30f6-8c0d-fdc51d6b559b | -3.98196 | -43.24212 | 2025-08-16 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cd80a3bf-ec83-3748-a41a-3ccf26527af7 | -5.75659 | -46.6681 | 2025-08-16 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2728a861-c938-3b4d-8254-b6002e13a70b | -6.6711 | -43.76582 | 2025-08-16 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 533cb34d-76d6-32bb-894e-644936143246 | -6.55163 | -43.05893 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06b0c6e9-c781-3ab9-a15f-b6c7429e9a80 | -3.98636 | -43.23802 | 2025-08-16 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ad8efb2f-bb20-3f60-bbb7-e5047070ba7c | -6.56486 | -43.03959 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b42f84c-b91e-3814-8230-4ce83e549a31 | -3.82421 | -47.74153 | 2025-08-16 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 9ca5a301-a79a-31d8-8b7f-72edea0538e5 | -2.38234 | -47.66373 | 2025-08-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a11d5a58-5dfa-37ac-a315-17769c83f4f3 | -5.75562 | -46.66983 | 2025-08-16 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f5cd38d2-088b-327c-b55b-83c3805e5d77 | -3.32816 | -42.7802 | 2025-08-16 03:42:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cbeeeb2f-6ca0-381b-8150-8ceb93cf21c0 | -6.54133 | -44.54377 | 2025-08-16 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12be27dd-c961-36d8-9dfb-a6a6823828b2 | -3.98444 | -47.88443 | 2025-08-16 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bab42d10-6a83-31e4-8356-ce1f3652dfe0 | -6.56753 | -43.02409 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5c1e3cf5-2d27-3c00-a914-4289acdbe6bb | -6.6716 | -43.76295 | 2025-08-16 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98e2b737-6a89-3777-a117-7c46356b452f | -3.98535 | -43.24393 | 2025-08-16 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a7f73331-45af-37d4-9329-f9432bd1b805 | -5.20031 | -46.09543 | 2025-08-16 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28a8b6b0-215d-365e-b3df-be96f34f8deb | -2.4778 | -47.21069 | 2025-08-16 03:42:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 019974d4-8df7-3474-8dab-3269218a0d65 | -4.78323 | -45.33022 | 2025-08-16 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af821f10-6457-3f09-89c9-3775bc7aa84e | -5.75575 | -46.67284 | 2025-08-16 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7df60b00-8450-3582-8b61-c454039bde74 | -6.67662 | -43.76385 | 2025-08-16 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7525284-6c58-343f-a26e-72a4df0254a4 | -5.60031 | -45.37922 | 2025-08-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d57ef5c1-7593-3d77-8663-468971561581 | -6.863 | -42.80368 | 2025-08-16 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 81e75e19-1d24-3a9e-bced-c37f2ea91b84 | -3.98076 | -43.24023 | 2025-08-16 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e25765c0-3e57-3ba5-8796-47b2c29a03a7 | -6.93789 | -44.55988 | 2025-08-16 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a954462-5d9a-3291-8f3d-37d0e899a107 | -7.13641 | -43.90304 | 2025-08-16 03:42:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d69c5b3-169d-30eb-b9ba-f7cc1fea291c | -6.55135 | -43.03207 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea726547-2c37-3a7e-9996-305d64d50164 | -6.55345 | -43.04842 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e549440f-c426-3ffe-a99e-1339f7879347 | -3.8253 | -47.73527 | 2025-08-16 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 5d70c291-7ef1-38ad-aac7-f1b52fdba868 | -6.55704 | -43.02769 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fd3cc7e5-5672-3739-8ac5-4e7d1cbf5ba0 | -2.38124 | -47.67005 | 2025-08-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1c08ba08-56fd-3960-9179-9d676f446b7a | -5.20105 | -46.09121 | 2025-08-16 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b4b2f9a-7c9f-38dc-857b-6ea21bbc575b | -6.54956 | -43.04239 | 2025-08-16 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README19.md)
