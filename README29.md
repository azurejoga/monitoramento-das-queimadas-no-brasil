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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b71e04fd-9912-3410-9d83-17d4248223c9 | -4.5429 | -48.0151 | 2025-06-21 08:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 3b7eb028-2f47-3792-ac41-c324e2460f8b | -11.798 | -57.243 | 2025-06-21 08:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| dbfc9918-fcda-3909-814d-706b94a179ae | -11.8853 | -54.6722 | 2025-06-21 08:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| f8d6ecaa-4319-30b8-b03b-c51118f8f717 | -11.798 | -57.243 | 2025-06-21 08:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 976c8613-66d2-3b0b-8128-2bb921f5d5cd | -4.5429 | -48.0151 | 2025-06-21 08:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| b5037a37-5e62-3b4e-90f3-c3c88669990c | -4.543 | -47.9934 | 2025-06-21 08:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a6548f27-4e95-392d-a39d-df711c0fe204 | -4.5429 | -48.0151 | 2025-06-21 08:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 855a07c7-11fb-3c85-a322-b1c60f03a450 | -4.5243 | -48.016 | 2025-06-21 08:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d5007145-280c-300d-ae94-884041cde002 | -11.798 | -57.243 | 2025-06-21 08:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| c6869a66-d061-3e96-ba3a-7ae3e26a091c | -4.5243 | -48.016 | 2025-06-21 08:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f4a2ca47-81d1-3bc9-8894-010d28c3d9f2 | -4.5429 | -48.0151 | 2025-06-21 08:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| f0accb74-77d3-3017-ab7e-5a2f0312a4e4 | -11.798 | -57.243 | 2025-06-21 08:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 58748500-2049-39c1-97c0-556908c9bc4a | -11.798 | -57.243 | 2025-06-21 08:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 7e4c8ace-149b-3624-8ac1-5ca4424ce8cc | -11.798 | -57.243 | 2025-06-21 09:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 42dd5b96-0f05-39fa-bc9c-cc0a17c396ca | -11.798 | -57.243 | 2025-06-21 09:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| ec51d183-0041-3d56-9602-3a3082bfb1ae | -8.5911 | -51.5537 | 2025-06-21 11:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| a4cb5cb3-89e2-3930-9174-a13f7b60aacb | -8.5911 | -51.5537 | 2025-06-21 12:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 79f4fd0d-8630-38d5-9b32-351757c0f28d | -11.5779 | -44.8413 | 2025-06-21 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| b0d888d3-cf75-355e-aff5-c25383d0295d | -4.54928 | -48.01117 | 2025-06-21 12:04:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 12cffaaa-d8cf-3872-bc5a-afd3749d492e | -11.57691 | -44.8359 | 2025-06-21 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 080be762-5725-35f9-9b14-a5997e4d73d5 | -9.30869 | -40.37701 | 2025-06-21 12:06:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 080821f3-4477-3722-bd3b-9f64a70564b6 | -11.45506 | -42.24735 | 2025-06-21 12:06:00 | TERRA_M-T | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f9512017-e479-377c-82a5-d143dd2b004a | -7.07016 | -43.42367 | 2025-06-21 12:06:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d25b6a02-ac92-3ae6-be82-e3820481453a | -6.23254 | -44.52254 | 2025-06-21 12:06:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 71d566a8-4f32-33b8-9726-1c7540c3ce0d | -8.28175 | -44.94648 | 2025-06-21 12:06:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 720651c8-127d-304e-844e-f3d3b976c26b | -7.23179 | -43.07333 | 2025-06-21 12:06:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b47fe9b1-0357-3a97-b9a3-7697970c1538 | -6.04374 | -42.93285 | 2025-06-21 12:06:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 94b971c2-90f2-32ea-b99e-724c68a742f1 | -6.86442 | -45.5612 | 2025-06-21 12:06:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4336b45f-7c10-3300-9e42-b7bbc8f209fb | -5.49307 | -43.97816 | 2025-06-21 12:06:00 | TERRA_M-T | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 4683b6ea-a1e7-39c4-a6bb-ba8c810e3111 | -9.25948 | -46.93368 | 2025-06-21 12:06:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7a35535c-9894-3605-87ab-07ac19b4f0df | -6.50386 | -43.63598 | 2025-06-21 12:06:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 9504b665-959c-3cfd-9f99-56dabc0e88c6 | -11.9305 | -47.85205 | 2025-06-21 12:06:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 919b9454-0d62-3718-ac5b-68cca27770b5 | -7.16703 | -47.13931 | 2025-06-21 12:06:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| a1c507e0-1259-3551-887c-d65034097e1f | -6.93613 | -47.7575 | 2025-06-21 12:06:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e083c313-5560-378c-9168-b2140f72e1e1 | -8.28972 | -44.95795 | 2025-06-21 12:06:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8082b8cd-e2e8-3e4d-bfce-4c1c96308508 | -8.29127 | -44.94778 | 2025-06-21 12:06:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4986d46b-518d-3a77-a24a-ac84f4a70fd8 | -11.76502 | -43.3717 | 2025-06-21 12:06:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6d5ff133-c420-3e35-a9c1-f0238fbd0eaf | -6.96127 | -42.90594 | 2025-06-21 12:06:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| c25f33e1-ff60-3a96-905d-225a78a7a796 | -6.93005 | -47.76224 | 2025-06-21 12:06:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 813a1bc9-02a0-311f-aa3e-9eb17a7b9c50 | -11.57548 | -44.8455 | 2025-06-21 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 4e9729e7-2453-358e-84cc-70e89521e575 | -6.24205 | -44.52389 | 2025-06-21 12:06:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 01a4dc2a-813d-3a66-9557-8489c4c6bb1e | -7.2242 | -43.06308 | 2025-06-21 12:06:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 0b3774bf-1977-3bb7-821b-9a97d3b8d0cb | -6.87482 | -44.12181 | 2025-06-21 12:06:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 19a92e1a-5972-35fa-9c72-e2e78663be68 | -8.4678 | -46.99841 | 2025-06-21 12:06:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 61c8f009-7922-32e9-8203-2edbe4d25c7c | -7.34802 | -43.91693 | 2025-06-21 12:06:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4952dad-7f89-353d-a692-b77cc4863466 | -8.33552 | -47.47872 | 2025-06-21 12:06:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2487fa46-9a79-3bef-9a20-eab696e22131 | -8.7379 | -47.98376 | 2025-06-21 12:06:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 83ed4ece-b002-37c5-ac36-e3c39b0a14ed | -7.87075 | -47.86945 | 2025-06-21 12:06:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5fd17a18-be88-3fff-8fee-dd74ccf9fb0c | -8.38096 | -46.96444 | 2025-06-21 12:06:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e200ce98-8901-3fc5-8b0f-d6b45418350a | -7.22289 | -43.07207 | 2025-06-21 12:06:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| afde66e5-00d8-36e8-a359-9443d9ba3e09 | -8.18637 | -47.77085 | 2025-06-21 12:06:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4a8a0d0a-1730-357c-be2d-88f833c504cd | -5.50239 | -43.97952 | 2025-06-21 12:06:00 | TERRA_M-T | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| e2525a61-5da9-33b0-bb94-f3fdaba62f6c | -5.49161 | -43.98804 | 2025-06-21 12:06:00 | TERRA_M-T | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f6d3f131-933b-32d4-b6d7-0040523f29d8 | -7.73875 | -43.95995 | 2025-06-21 12:06:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ddd53836-6901-3d0f-af90-c7590c06c8dd | -10.50894 | -47.57994 | 2025-06-21 12:06:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 49d86a61-0c6a-304d-b575-b89200d114ae | -8.33787 | -47.46342 | 2025-06-21 12:06:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7e45318f-27db-34b7-8c93-801ea08086d5 | -6.50249 | -43.64536 | 2025-06-21 12:06:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b940a2c4-e338-3de9-8367-fbc0bf4db53f | -8.28022 | -44.95654 | 2025-06-21 12:06:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| c4d4f1a8-3a0f-39dc-801d-c365b8f9bcfc | -8.01851 | -47.66624 | 2025-06-21 12:06:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 79454808-07a1-3d6e-bbf3-0eafcbbbf463 | -7.86815 | -47.88602 | 2025-06-21 12:06:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b5e7f585-4cc0-3bd0-8717-8c1852d5176d | -7.23768 | -43.79184 | 2025-06-21 12:06:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 28c4a2b4-cd39-3649-aa74-ca21d137bb66 | -7.16471 | -47.15439 | 2025-06-21 12:06:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6e894062-d781-37a1-97f8-3103b3eb12f4 | -11.32821 | -45.45361 | 2025-06-21 12:06:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| af65315e-18a5-3f17-b9db-8eb1f1be12c3 | -8.46558 | -47.01268 | 2025-06-21 12:06:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 5f7fb1a4-b03f-3a70-92a4-4f095a3005ca | -6.66621 | -42.45823 | 2025-06-21 12:06:00 | TERRA_M-T | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8188ceb0-f508-349d-9235-c94fb15f8ae1 | -6.93931 | -47.78082 | 2025-06-21 12:06:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 68b25c8d-0da6-33a6-a3f5-9f5ba844052c | -7.27245 | -45.36702 | 2025-06-21 12:06:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 81f63c7e-9d9a-39da-a43b-028133919bc3 | -6.93361 | -47.77424 | 2025-06-21 12:06:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| c597e71a-d87c-3d98-8b55-0f99f02c5fab | -7.27413 | -45.35579 | 2025-06-21 12:06:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e3e7cce0-9131-37d3-93b2-3153b6d9631b | -7.23463 | -44.67492 | 2025-06-21 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6b250245-5797-3864-b78a-9f1999b994c8 | -11.45634 | -42.23816 | 2025-06-21 12:06:00 | TERRA_M-T | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 59ba5ed9-a662-389e-bed8-cdc7bb6e3ca4 | -11.58604 | -44.83726 | 2025-06-21 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 8312a533-3a9b-34c6-9765-99d786e30db8 | -11.58461 | -44.84686 | 2025-06-21 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 81b48967-3ab2-3e50-9d4b-1986dd1cf237 | -10.51994 | -47.5817 | 2025-06-21 12:06:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 39d258fb-4b17-3d96-afcc-5810dd76e0b6 | -11.82772 | -44.82387 | 2025-06-21 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 785ecfb1-bf92-307f-8f03-16d9010f37ca | -6.23098 | -44.53287 | 2025-06-21 12:06:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| f277856f-3fb2-3dc5-9882-495045de831e | -8.17221 | -47.78513 | 2025-06-21 12:06:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 8f3aa104-b16d-3c60-9201-8219974a90a5 | -15.41952 | -42.01099 | 2025-06-21 12:08:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 477da9a2-fb41-36c4-ab80-28c64684948a | -15.16029 | -43.92646 | 2025-06-21 12:08:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 90e22632-1f64-322d-b41c-b71750a20848 | -17.62094 | -44.64156 | 2025-06-21 12:08:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 26bddea4-ee89-3d43-937a-8d70bd0f9780 | -17.66072 | -46.84543 | 2025-06-21 12:08:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 47d76485-76d4-378c-b95c-dba61d7aea9d | -15.15899 | -43.93555 | 2025-06-21 12:08:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ed9f3437-c5b4-35c6-9e95-b02ab2de2dec | -13.33991 | -43.8987 | 2025-06-21 12:08:00 | TERRA_M-T | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 706376c4-e79f-304e-9e9c-a4fe5c86e37d | -14.19634 | -45.46737 | 2025-06-21 12:08:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ccd152a2-5cf1-3138-b77d-718afd83509d | -15.41814 | -42.02112 | 2025-06-21 12:08:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 4035c813-9d2c-32d9-a14d-76112d19227c | -13.67165 | -47.48864 | 2025-06-21 12:08:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 58e3631a-c70a-358d-a3d5-13a5412ac8f2 | -17.65909 | -46.85596 | 2025-06-21 12:08:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a7060069-5f19-3a1c-850d-9dd285fbe225 | -15.90753 | -42.74554 | 2025-06-21 12:08:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d27a677f-60df-3eea-886c-71fdebf912b0 | -17.6121 | -44.64021 | 2025-06-21 12:08:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e40a476c-9216-3a37-8001-48720801f328 | -15.72047 | -43.49627 | 2025-06-21 12:08:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bbeda3e5-59c3-3f62-af4d-d9541c9f56a1 | -15.72176 | -43.48707 | 2025-06-21 12:08:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 63d9412e-b0be-33c2-ade7-802af1f506fa | -19.37883 | -44.8014 | 2025-06-21 12:08:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0425d667-5595-3826-b3b7-e43323f4d978 | -11.5779 | -44.8413 | 2025-06-21 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| cda59f29-f3e5-3dbc-9d7e-70aec9b83b43 | -19.99023 | -47.18623 | 2025-06-21 12:10:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9165ad52-2abf-3ed8-acb8-1fbb8faf2317 | -19.91367 | -46.17928 | 2025-06-21 12:10:00 | TERRA_M-T | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a25a36f1-c5ae-38b7-a4b8-8130af4e92cc | -22.44987 | -42.33285 | 2025-06-21 12:10:00 | TERRA_M-T | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 5181c14b-bde7-3d10-b633-87b8285102d0 | -22.28067 | -46.32577 | 2025-06-21 12:10:00 | TERRA_M-T | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c5ac4851-f0ae-322d-8729-5640d1f6117c | -8.5911 | -51.5537 | 2025-06-21 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| c472aee8-5933-3717-a809-08ef7a63d7ae | -8.1827 | -47.7821 | 2025-06-21 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 21583af8-973c-3103-9f26-0c691e0e0f53 | -11.7791 | -57.2445 | 2025-06-21 12:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |


[Clique aqui para ver as próximas entradas](README30.md)
