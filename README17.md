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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a262899-ee8a-3126-a11e-109913242464 | -10.87765 | -45.0796 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4592ddc8-9d58-3dd9-8c10-41f1b90c7089 | -3.02375 | -49.45284 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e4341efa-ab57-3c24-9387-a7f0478f872e | -3.05437 | -48.7171 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b9808ef-f08a-3c2e-96d4-783426740b91 | -10.01216 | -47.10433 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2737ddac-c287-35d0-83b8-34868925a70c | -10.42282 | -49.367 | 2025-10-24 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f262fbda-9a83-316a-b76a-3d8dbf6cdc26 | -9.23158 | -51.83802 | 2025-10-24 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 811c8a57-9412-3ec2-af9a-9be114ad2fd2 | -9.78325 | -43.85813 | 2025-10-24 04:17:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a77d6112-eaf9-38af-a69b-35ca6ee5c290 | -12.07646 | -46.43365 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b7e3663-999d-3f93-9c29-b61760fddddc | -3.99924 | -43.75657 | 2025-10-24 04:17:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6080856d-77de-3346-ba53-1c1967ff8fe2 | -5.58019 | -41.31842 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 02f8a4a2-2581-3991-a165-f5ec1193b235 | -3.64522 | -48.97416 | 2025-10-24 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27a4be80-b6f4-3ff9-aa16-75ff0768808a | -11.86839 | -46.75502 | 2025-10-24 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| edc1ae46-5505-3ac0-a0f1-556343c77e92 | -9.99939 | -48.09719 | 2025-10-24 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2b0f1249-fcfa-34e7-a858-eb775ef75e5c | -4.14754 | -47.67445 | 2025-10-24 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2ca8acb-03c8-3cd7-bea3-10eade01c55c | -10.94883 | -50.378 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b1804cf-266a-3b40-b42f-4cbb3ba9fb01 | -12.01792 | -43.88396 | 2025-10-24 04:17:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19fdb5cd-9340-3b47-afb4-8a2c05f2d9c2 | -3.84888 | -49.13052 | 2025-10-24 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac20a0f3-6516-39f5-9b6c-8774632a3f3a | -11.06735 | -44.78633 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3336a78-0952-39d4-8af5-dcffb1b3073f | -5.59844 | -47.49754 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fb1eb54-6e8b-3249-bef7-176cb471f018 | -11.996 | -45.42817 | 2025-10-24 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9064bba2-e2c5-31c5-b8f8-884972d763d0 | -11.36887 | -45.93081 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b00d795b-01ce-31f7-b001-ea9b9ed1f72b | -9.94188 | -47.45762 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53d25267-d5db-3d56-87de-45d4ebd07bf2 | -6.11676 | -41.74949 | 2025-10-24 04:17:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cbf03f3d-9aa5-315d-9e2b-ee8407d081da | -4.98735 | -44.14598 | 2025-10-24 04:17:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c920b608-4d5b-37e2-937e-4d5efd6423ba | -3.92419 | -47.69354 | 2025-10-24 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55aff18b-c96c-3bb2-af4a-c6c7f768a07f | -10.90867 | -45.17621 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8783c9ea-1e95-3ba5-b4eb-f08cb10a6054 | -9.30622 | -45.20742 | 2025-10-24 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebf0e305-b55b-3947-9036-912bd8ef9076 | -9.19291 | -45.69285 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c641e55-2402-326a-8ad9-ebf84947b031 | -11.04177 | -47.88608 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58d62b6e-3881-3986-bc67-b7b4bf2fdc38 | -9.96874 | -46.3418 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fb73c18-137a-3291-9758-8b8b39f19416 | -10.01842 | -47.0667 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8f655be-9535-37f4-a4ab-cf0e97aa676d | -12.27789 | -43.82346 | 2025-10-24 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11b978e3-17e0-38ac-938c-fdb4e274b6fc | -6.53553 | -41.6833 | 2025-10-24 04:17:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c1c60f9c-649a-3fd3-93ce-6d87b3f38f47 | -10.91261 | -50.17111 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a131d35-ae4d-3dc6-8144-3c23115ffaa2 | -12.17924 | -43.60627 | 2025-10-24 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f12d6689-500a-3071-974b-f6835fd67242 | -2.41598 | -48.44353 | 2025-10-24 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cd392003-39e7-32e5-8627-6a632e258f4b | -2.81771 | -49.13756 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93e58747-ebff-3ae8-ac83-3b32f1e62dcf | -12.22537 | -43.30714 | 2025-10-24 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddf5a01b-16c0-3bf1-bc5f-0db4d76d79a5 | -3.11641 | -51.20832 | 2025-10-24 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b72c61fa-8229-3c63-9d8a-c07a81411dff | -11.04545 | -47.88692 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 133850c0-e1a8-3173-84d7-b5d48a811e01 | -12.07553 | -46.41777 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 107438df-5852-3826-b1ac-fece416b38a6 | -4.64365 | -42.51286 | 2025-10-24 04:17:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5cdb40f8-c9a2-34ac-8290-91db5c84baa4 | -6.31248 | -41.85966 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c862048d-95b6-38bd-bde0-c63c3a89bb4e | -9.60066 | -46.90713 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| aeda6619-c0de-3c7b-a4ff-b75f8cd36c37 | -11.35438 | -45.95518 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d10d5551-8a62-3272-8275-00fb5fe2adca | -12.07365 | -46.42924 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72b66ab8-32e3-3bf7-81a0-291189eaaf93 | -11.02221 | -47.91097 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 236cda60-baf0-3ecb-b5f2-9493b34c8a67 | -3.7021 | -47.65444 | 2025-10-24 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 520e0816-0be4-3982-9001-d285f29cc0f5 | -3.81377 | -44.08348 | 2025-10-24 04:17:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1048bc6-91a2-3edb-9eee-8769c171227e | -9.97737 | -47.06818 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63d01d0a-6dee-3d01-9d58-848b6c835baa | -3.80761 | -43.30769 | 2025-10-24 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5508eb4f-f1a8-3577-8b86-9bc4e563c7f9 | -10.65615 | -44.7262 | 2025-10-24 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 60f94f31-d9d1-39ab-98f8-50aa197f8330 | -10.89056 | -50.12095 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0e75636-a285-3d8a-9363-dd081e2c6bc5 | -9.24394 | -45.58918 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffe52f47-7b74-37a6-a5ef-eb43638a8aea | -4.2809 | -40.69992 | 2025-10-24 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 02a386f7-ce53-34aa-ba56-f266e465d51d | -4.28494 | -40.69658 | 2025-10-24 04:17:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 3b419f80-207a-37c7-aa82-28ed232c9d1c | 0.40466 | -50.9511 | 2025-10-24 04:17:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4147bb94-c87b-3b69-a5e9-b81c6d8203ed | -6.80292 | -42.39315 | 2025-10-24 04:17:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cab4ab6b-53f1-3943-9f27-615e59a4c008 | -12.29172 | -47.45984 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0b54349-0a3b-3f51-87c1-f2de8992e13e | -9.2324 | -51.83003 | 2025-10-24 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae8d1bb7-4c01-39b8-9dc5-0d6e3fc04676 | -9.1967 | -44.54443 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4614e555-dca3-398f-9ad8-1f5145cf2c28 | -11.46179 | -43.70403 | 2025-10-24 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea134b3b-79b7-3e20-8b01-0a5a7eb9d2d7 | -9.24844 | -43.19504 | 2025-10-24 04:17:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b518131e-6bff-33e1-b495-f45ae824d4da | -10.63948 | -42.29963 | 2025-10-24 04:17:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2416afd7-12c6-338a-825f-7b235e3afc5d | -6.51907 | -43.93798 | 2025-10-24 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3da333fe-b18d-3f63-9676-2697fa2cfce2 | -10.01926 | -47.08398 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ca68d1b-8726-3732-80a3-e1b6929a88bb | -9.63933 | -46.89665 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 522e8597-8c2e-39b6-88ef-df5c3fde4207 | -3.29221 | -50.19455 | 2025-10-24 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d08109c1-8238-34d1-ac68-dbd19d1e7f42 | -6.13138 | -41.72236 | 2025-10-24 04:17:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f44d3c76-ad16-3c0c-b134-332914fd5ffc | -6.84873 | -41.5516 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ea70031b-6fff-3ef7-afc2-2988ec5c42f1 | -6.12631 | -41.73265 | 2025-10-24 04:17:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 61faa5eb-848e-3751-846d-7acae94073a9 | -11.48209 | -43.24268 | 2025-10-24 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed6bf4da-3942-3c96-8477-8e9b161fcfcb | -6.15049 | -44.58439 | 2025-10-24 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23be51e2-68bf-3c10-8825-59880e7ddca8 | 0.40582 | -50.95076 | 2025-10-24 04:17:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f008dc9-8135-3eae-8604-75e784b55845 | -9.23222 | -45.61783 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e724f783-e66e-33e0-9642-38618f02516d | -11.01579 | -47.88156 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ec2749e-9af0-3b69-9adb-0d080c737fdb | -5.61528 | -41.11318 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e32c3913-dbd3-3b8c-adc6-c3c06b1db885 | -5.61585 | -41.10951 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d5e63a62-fdb5-3fef-84da-b9ad17ca1d9e | -11.36302 | -45.94519 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31553656-695a-34a8-bf29-b3aa13a6c84b | -11.02747 | -47.90265 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3e17726-d585-3a32-aca3-2273d3364384 | -10.00925 | -47.09951 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f47fa41e-7cd2-36e0-b011-d9b3ec328a77 | -4.84545 | -47.80084 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03cc6753-a6b4-3a9b-a08d-e823b2c59a9a | -9.60658 | -44.6252 | 2025-10-24 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9061d634-3364-30e5-874d-9d3795501a74 | -10.42625 | -49.37146 | 2025-10-24 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20cb0b8b-d4b2-3153-a9ee-d17ea7f748cf | -10.01286 | -47.10012 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fa2bb7b-b199-31ce-902b-c24a2fe6e07d | -2.87047 | -41.74509 | 2025-10-24 04:17:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9f47765-1bb3-3617-81e3-d43504915f31 | -4.83137 | -42.9108 | 2025-10-24 04:17:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 343d46eb-12a0-3233-a19b-160195420764 | -4.83441 | -45.35397 | 2025-10-24 04:17:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc0914c2-b98f-3203-a559-36eec3e3d597 | -8.56449 | -48.51274 | 2025-10-24 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0405404-8223-3747-80c2-c7b9a2a1f01c | -5.47681 | -46.47049 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eae9e34d-ed41-3c3a-8878-556b1d18f846 | -9.61146 | -46.90882 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c47f7c99-fad2-3eaa-a259-13c5fa1861ba | -3.14212 | -50.16534 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0491c381-b9e6-348e-9ce4-f38732c78e90 | -11.47873 | -43.24214 | 2025-10-24 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 342a1d94-53e4-37ed-87b9-9fc4548f2b75 | -12.03127 | -46.53573 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a6e6ecb-cc46-3af0-98f0-148a7948406d | -2.26185 | -47.85042 | 2025-10-24 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| efb463dc-5034-3723-8c9c-10edca972262 | -6.13026 | -41.72955 | 2025-10-24 04:17:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0c30dba1-facf-3895-ba31-b2c871463b85 | -10.40655 | -47.11467 | 2025-10-24 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4454bcfd-e809-338c-95cd-b1b90c2f01a0 | -2.8725 | -50.71453 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a1af945-95b2-3515-8a78-d4914369bdfb | -10.97851 | -50.36189 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60e6e704-65a3-383d-a04f-ac90353899bd | -10.97925 | -50.3577 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README18.md)
