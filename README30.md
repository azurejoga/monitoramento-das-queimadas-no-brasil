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
| fda4324e-0862-3194-b54e-538a10d7cb26 | -13.7194 | -51.45868 | 2025-11-01 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 986be4fa-33fb-33af-a768-8326d76f2226 | -11.74072 | -59.31023 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbc617e9-1dcb-3951-ab4f-69571760eaf8 | -12.02606 | -63.74157 | 2025-11-01 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecfc8fd5-0231-3d52-a204-9d7c77899790 | -10.01067 | -67.01286 | 2025-11-01 05:29:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cf5722e-ced8-392c-8391-fcdf5cc0ca6f | -13.71885 | -51.45734 | 2025-11-01 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f18649c-a3fe-3e31-bb2b-85b3a2a2ea8a | -12.0255 | -63.74509 | 2025-11-01 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 883f2ddd-128c-3980-ae8d-149b9fb1829d | -12.31969 | -57.72592 | 2025-11-01 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05e12880-1e82-379c-9df0-abbd1ea22a88 | -10.05638 | -64.99171 | 2025-11-01 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3400d4ff-48e2-30f3-9ad4-6056fad78424 | -11.72945 | -59.30853 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8b75e0e-a9c2-35e1-a255-95e870733d29 | -12.65122 | -60.42654 | 2025-11-01 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2e8e772-f1c2-3435-a44d-4f9fc7bbaccc | -12.02438 | -63.75214 | 2025-11-01 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2f437a9-5d7c-3e66-9c5b-d79df55abc23 | -11.85756 | -58.8177 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a26d763-316b-36a6-b9c3-d5ae0c2437bd | -11.20026 | -62.53516 | 2025-11-01 05:29:00 | NOAA-20 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89d696a0-abfc-3595-9830-f1ad82011a72 | -10.96445 | -59.0177 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5a544561-34c4-357d-9f30-3f5ba87968f2 | -13.72585 | -51.45942 | 2025-11-01 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a2c003b-a924-32d9-aa90-e6de1cf8f64b | -11.74517 | -59.30615 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 580e1f5e-2114-3919-b694-7dc26139c31d | -13.32244 | -60.72095 | 2025-11-01 05:29:00 | NOAA-20 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a853f709-f234-3007-b81a-0a06df778fec | -10.53412 | -53.71475 | 2025-11-01 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76458eda-2be3-3354-a692-8f9945eeb327 | -9.36813 | -63.57201 | 2025-11-01 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20c5c255-16c2-323b-94b7-535ffe6a3361 | -12.1403 | -64.0899 | 2025-11-01 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 677680ef-0566-328a-bea2-611bfcf1848c | -11.74619 | -59.30355 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ad4fc55-a307-3c0c-a856-7322c91afa6e | -8.85479 | -49.8805 | 2025-11-01 05:29:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd7872fb-6dc8-3cfb-a0b8-828c9d137bdd | -11.74553 | -59.3082 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b46f706a-ec11-334a-a7a0-6bdd42ead3ba | -9.61886 | -67.17637 | 2025-11-01 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00aa8c1a-0e31-399f-b626-f9617f2c8e99 | -11.74585 | -59.30151 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6247e90c-04a1-3b3f-ab08-f89566a7359a | -9.22769 | -65.74696 | 2025-11-01 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2ffd2e2-3d37-32be-8cc0-6e633c41db1e | -12.44672 | -63.12095 | 2025-11-01 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e56c731-93d1-3ecf-b915-359131d1b709 | -11.74684 | -59.2989 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b964cab-5ed6-305f-8f73-f7c2032ae07c | -11.73735 | -59.31174 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0a571395-7f01-3ffe-9f52-49cbebcab452 | -11.73388 | -59.30447 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f1c3cac-0cef-3654-9799-9463ae8e3f2d | -10.4476 | -62.85291 | 2025-11-01 05:29:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5feb7d4f-a43f-3e8d-93b6-5c150065bad9 | -9.06958 | -48.83686 | 2025-11-01 05:29:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afff6b0b-cb5c-38bb-b328-a32c13428bb7 | -9.23197 | -65.74342 | 2025-11-01 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77573c79-ec8e-3cc6-8f6c-7448bb1b38cd | -13.71823 | -51.46281 | 2025-11-01 05:29:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82f2c64a-fba3-3c13-988f-350140e4508a | -9.61501 | -67.17567 | 2025-11-01 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a443ff27-9428-3705-9acd-43d641e2a0ac | -13.3272 | -60.71325 | 2025-11-01 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 090bc441-f474-342f-8591-f7187e26feb3 | -11.74112 | -59.3123 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a48242fa-4d4c-3c40-8f5c-5a1eff47a3a1 | -11.74209 | -59.30095 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd30b2ff-8a7c-3f32-b5ba-d7ad7c6e7a40 | -13.33016 | -60.71791 | 2025-11-01 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb874df1-bb31-3289-aee0-68994f7b4d0c | -11.19694 | -62.53463 | 2025-11-01 05:29:00 | NOAA-20 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3dbfadd7-2165-3622-bf60-1c2b842a102d | -12.43788 | -57.86832 | 2025-11-01 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 422776d5-9c65-3a3c-93a6-2503f601bd55 | -9.65091 | -64.55306 | 2025-11-01 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56360af6-54b2-3149-8329-acfe85ff093c | -13.32304 | -60.71682 | 2025-11-01 05:29:00 | NOAA-20 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3acecd69-4f5f-315b-81b4-44f3e40086f2 | -9.84895 | -61.98881 | 2025-11-01 05:29:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| feae6d5d-f171-3bcc-945f-68de14f81ba1 | -11.98503 | -60.80352 | 2025-11-01 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 891ad86e-335b-3445-add2-35aa17864514 | -11.97394 | -60.73276 | 2025-11-01 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6d1bb11-0bec-331f-97b2-1b6eae245540 | -12.02382 | -63.75566 | 2025-11-01 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c852226c-6b40-3359-95d6-4c8fbae1c8de | -12.26016 | -64.42465 | 2025-11-01 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac6ad8d9-f7a3-33c9-aeeb-3ca535affdf0 | -12.44286 | -63.12393 | 2025-11-01 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e5a2b2c-e60e-3b5e-94e1-d873ccca242e | -9.22838 | -65.74283 | 2025-11-01 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53159e4d-ec88-3c1c-bbfe-5ba4e4f8b587 | -12.17739 | -60.69685 | 2025-11-01 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3b689db-e82c-3cec-bf17-879e95f7ebd4 | -9.83856 | -65.23267 | 2025-11-01 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4692f3d9-1446-3368-b5df-3530e0050d25 | -12.6572 | -60.42571 | 2025-11-01 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c97a0a4-a588-3b85-bf8a-49193cfe3625 | -12.76533 | -61.46079 | 2025-11-01 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 759bf5bc-1cd1-3735-af22-504780da9349 | -10.08934 | -64.91948 | 2025-11-01 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe6cdaf3-de48-368a-95f0-b5291dd030c0 | -11.73013 | -59.30389 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6eeb765b-0dc2-31e9-8f21-664d767a8599 | -11.74242 | -59.30301 | 2025-11-01 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 250e4583-a32d-3d48-8d4f-3d899acd73dc | -13.3266 | -60.71738 | 2025-11-01 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 26da6d67-d654-3b86-852b-a0e88deb567a | -12.88514 | -54.75748 | 2025-11-01 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5061ac6-a372-3801-a332-1f1ec02e53ef | -12.76589 | -61.45698 | 2025-11-01 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52d653d9-3dc9-3141-9dbb-fa2b761d58fd | -9.48732 | -64.49996 | 2025-11-01 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ea18fcd-53a6-3d92-85eb-7dea9a8bdcec | -12.88551 | -54.7544 | 2025-11-01 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a7d5f4a-5051-3468-aa93-1c27454b0490 | -9.01731 | -63.65979 | 2025-11-01 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9888dc5-5d56-3b95-9560-f11226e63fb6 | -11.97745 | -60.73332 | 2025-11-01 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df6f2624-380d-38f2-a768-d2e0f3970a00 | -12.65479 | -60.42711 | 2025-11-01 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d5d7321-241e-386b-90eb-62f4e916813d | -7.02673 | -37.24527 | 2025-11-01 05:31:00 | AQUA_M-M | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 1c2aa829-a697-3b07-91b3-2467b16b69c5 | -15.0314 | -56.45984 | 2025-11-01 05:31:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb989e8-10b4-3d21-9615-749ce7788d79 | -15.03003 | -56.46338 | 2025-11-01 05:31:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cae1467d-1b4b-33c4-8b23-a154b748fa5e | -6.55043 | -43.23512 | 2025-11-01 05:31:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 14.4 |
| f78b145c-604d-35c9-b60e-9cf7d9b6bcd3 | -3.76315 | -42.35358 | 2025-11-01 05:31:00 | AQUA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 7dc7aec8-798d-35dd-bdc1-743e1ba4a14b | -6.87982 | -42.84131 | 2025-11-01 05:31:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| f70f1585-a3f0-3fff-94c2-2b589a5810d9 | -15.03071 | -56.45812 | 2025-11-01 05:31:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df6e2d5e-cf62-3600-ade3-3fecc3b4e796 | -6.87802 | -42.85279 | 2025-11-01 05:31:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 5eed2617-91f7-3e06-b64d-25b15fb8bd18 | -15.02666 | -56.45919 | 2025-11-01 05:31:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 591f4936-9054-3fcc-975d-e2fd69071f54 | -12.02393 | -42.70428 | 2025-11-01 05:33:00 | AQUA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e2620ebc-563a-3723-9bbc-eeaf55aa832d | -10.41663 | -44.34996 | 2025-11-01 05:33:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 9ee901f0-369d-3a50-9e65-327f2c3ceb0d | -10.40612 | -44.34847 | 2025-11-01 05:33:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 4b0e7f6b-c2d5-36ec-b56b-2887be583c61 | -10.4083 | -44.3352 | 2025-11-01 05:33:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0c8d31ab-d774-3aad-bfdd-ae11de051db9 | -13.70878 | -43.77992 | 2025-11-01 05:33:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6dcea109-9546-3435-8aea-2a7332815451 | -10.40397 | -44.36152 | 2025-11-01 05:33:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f4665f57-98cc-3337-a335-0ffb1fb20eeb | -10.63177 | -42.31927 | 2025-11-01 05:33:00 | AQUA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2c5f4f17-542a-3c92-9147-f993662f1cf0 | -10.41446 | -44.36319 | 2025-11-01 05:33:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 12889733-0d6c-3533-8b94-f69a4b1f4257 | -10.63332 | -42.30947 | 2025-11-01 05:33:00 | AQUA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| ddeb0180-6f0b-38bb-9f79-ed120b331cba | -13.7479 | -43.60062 | 2025-11-01 05:33:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0756e25b-0c79-3846-ae04-e903f295eb81 | -14.59123 | -42.96174 | 2025-11-01 05:36:00 | AQUA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ccfb84c-17e8-3c87-9691-d3e84bedaaf9 | -15.34736 | -43.03691 | 2025-11-01 05:36:00 | AQUA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 850393bd-b78c-3b79-b3be-b4d00121a023 | -16.66999 | -40.90438 | 2025-11-01 05:36:00 | AQUA_M-M | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| d9c1c472-dede-33fd-8440-e2e0773bf8ab | -3.234 | -50.5789 | 2025-11-01 05:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3d0a4410-fc3b-3145-88dd-c501fc962db5 | -3.234 | -50.5789 | 2025-11-01 05:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4686f4b2-2d2b-3e0c-8e29-0a52688bb579 | -4.8224 | -42.7242 | 2025-11-01 05:50:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| df987d00-632a-37ef-aa12-b443a9d798a0 | -3.234 | -50.5789 | 2025-11-01 06:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 66f02b39-4e3b-34e5-80e1-7a0461cbfa5a | -3.6748 | -43.9066 | 2025-11-01 06:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 99865594-f0f1-3b07-9348-da61fa134efc | -3.234 | -50.5789 | 2025-11-01 06:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| abe3fa2b-8970-3368-961a-48af2e59a70e | -9.22802 | -65.74458 | 2025-11-01 06:20:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a8381d3-bc5c-383a-ad36-126c75e77156 | -9.23342 | -67.61333 | 2025-11-01 06:20:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e54dc8b4-f916-36f7-a921-00067891abf5 | -9.23435 | -67.61134 | 2025-11-01 06:20:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8894b61-9ba6-390d-ba01-5ab03731624e | -9.23362 | -67.61661 | 2025-11-01 06:20:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ad26d3f-ee07-3680-9aea-909758b8f6e2 | -9.23348 | -65.74539 | 2025-11-01 06:20:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3685827-42c1-3316-b025-ea4328287249 | -11.73323 | -59.30423 | 2025-11-01 07:12:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b23bfac4-7fd4-358d-b29d-632cf0873cb5 | -13.32625 | -60.71108 | 2025-11-01 07:12:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |


[Clique aqui para ver as próximas entradas](README31.md)
