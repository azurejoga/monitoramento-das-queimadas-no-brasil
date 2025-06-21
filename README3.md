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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85781e14-4ebd-3a06-8119-428d0f1a12ad | -11.8666 | -54.6535 | 2025-06-21 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 0ab9f41a-cb5b-3aaa-bce7-14b7fb1a5c13 | -9.4648 | -57.8449 | 2025-06-21 00:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 7f99dc31-9809-3d2f-b0a9-0fee5772bd22 | -5.7686 | -45.8944 | 2025-06-21 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| c543dd04-2480-358d-8047-4991c6eb88f1 | -11.7791 | -57.2445 | 2025-06-21 00:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 059ecefe-4de8-32fe-b7c0-60ce1f28610b | -3.967 | -48.15 | 2025-06-21 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| ff9706e0-4626-3407-a42f-c0b3bb041ec2 | -7.2408 | -43.0664 | 2025-06-21 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 891191bd-7a76-3a91-90f6-6e90902302f1 | -7.2219 | -43.0682 | 2025-06-21 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 198.3 |
| b7216254-fa81-380a-80b7-8f969558ea97 | -11.798 | -57.243 | 2025-06-21 00:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 179.8 |
| 9a536281-f9f5-3a25-854e-8696d8c8c679 | -11.866 | -54.6944 | 2025-06-21 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 0ec216f3-fa95-3b65-a061-ed71ac8ac7a9 | -11.8663 | -54.6739 | 2025-06-21 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 338.7 |
| ef4635d1-7dc5-34a4-8354-5fc9943ce1e4 | -11.885 | -54.6926 | 2025-06-21 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 9179f297-8534-307c-8ef8-f8f0137b05f7 | -3.9671 | -48.1283 | 2025-06-21 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 8f60e76e-8de6-3a52-a4d0-bd6498975d30 | -11.798 | -57.243 | 2025-06-21 01:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 84dc4de7-045b-30c1-80b4-534f5a9218ec | -11.8663 | -54.6739 | 2025-06-21 01:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 239.9 |
| 0b71e728-c2e3-3996-ae56-5a05c6705471 | -9.4837 | -57.8241 | 2025-06-21 01:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 27d2ab6c-0d48-3a04-8660-98882350548c | -4.5427 | -48.0367 | 2025-06-21 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| eff4afe4-c922-3085-90ee-76a60bb6c41a | -11.8853 | -54.6722 | 2025-06-21 01:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 396.3 |
| 13c2c9c5-e972-3896-b4b7-ba64b5453b06 | -8.0152 | -47.6656 | 2025-06-21 01:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 7dbe3168-f4d6-33e5-8994-2972f458b8cd | -7.2408 | -43.0664 | 2025-06-21 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 4eacab06-c666-3432-930d-2f48b11893e7 | -4.543 | -47.9934 | 2025-06-21 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 051b117f-73e4-32fc-8db4-247b869c2b0a | -7.2031 | -43.0701 | 2025-06-21 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 9a96408e-38c5-3999-8c2f-dd54b31c4678 | -4.5243 | -48.016 | 2025-06-21 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 189.5 |
| c505485e-b15b-3fbd-b912-5cd9871a16ff | -11.8666 | -54.6535 | 2025-06-21 01:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 2be6775c-ec7b-3481-921f-7a6ae1972f6b | -11.9518 | -58.7574 | 2025-06-21 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 7611faaa-b042-339a-b6fd-e2bf860cf7e8 | -11.7983 | -57.2231 | 2025-06-21 01:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 01752fd9-d66f-3a7b-b860-426ed8c4f0ef | -13.2343 | -49.8475 | 2025-06-21 01:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| eaae78de-eb2d-340a-ad53-3f82351e456c | -9.4648 | -57.8449 | 2025-06-21 01:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 0c7e7fd2-d24f-3d46-8959-f43faed5d505 | -13.2346 | -49.8258 | 2025-06-21 01:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 8930f330-e262-37ee-aaa4-6cbf68f72408 | -5.7873 | -45.8931 | 2025-06-21 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2026f26a-5c0e-3b38-9d8e-d3e62fa7bdc3 | -9.4835 | -57.8438 | 2025-06-21 01:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 0d759415-0eab-355f-96c9-61b18d0fbddb | -13.0392 | -53.7107 | 2025-06-21 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 5f9e4067-a720-3547-a20c-91a98cd67136 | -4.5244 | -47.9943 | 2025-06-21 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| c1fd7e78-7086-3027-a15e-3418a1ae5c79 | -9.2624 | -57.5228 | 2025-06-21 01:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 50300687-45fa-3e07-af3d-736649e535b6 | -7.2219 | -43.0682 | 2025-06-21 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 162.6 |
| 1ce2f854-32ee-30aa-ba2a-46115bbfac6a | -5.7871 | -45.9155 | 2025-06-21 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f42960cd-fad3-3e43-9c7e-fe957a387a39 | -4.5429 | -48.0151 | 2025-06-21 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 380.8 |
| 3038b8e0-12c0-39d3-9e1b-7c63e4d4007a | -11.7791 | -57.2445 | 2025-06-21 01:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| a614ae47-960c-3fe9-a2a1-3ca4859ef776 | -11.8855 | -54.6517 | 2025-06-21 01:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 419d9110-a051-35c6-a723-8b8ede3f1099 | -3.967 | -48.15 | 2025-06-21 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| a358fdb8-cd76-3267-969a-f70719350a03 | -7.2222 | -43.0447 | 2025-06-21 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| d80f50e8-45be-3fa0-a922-64d814c0be35 | -11.885 | -54.6926 | 2025-06-21 01:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 1caf4be4-4b4e-32b5-86fa-4719967c5762 | -11.866 | -54.6944 | 2025-06-21 01:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 350946fd-48b4-3b15-b863-1ebad765b4d4 | -9.465 | -57.8252 | 2025-06-21 01:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 8ab580ea-bcd3-3dfb-b59e-56caffbe60fa | -4.5614 | -48.0141 | 2025-06-21 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 035fe68a-9a2f-3382-9b89-071cf5504549 | -13.2346 | -49.8258 | 2025-06-21 01:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| c6942e93-4f41-3ff2-8c50-2cd4a78b534d | -11.9518 | -58.7574 | 2025-06-21 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 42438ad0-0a66-34fe-ae14-5d442a801b8c | -11.7983 | -57.2231 | 2025-06-21 01:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d93f39c6-8a5d-3fe5-be52-b42f952fa2d2 | -11.8855 | -54.6517 | 2025-06-21 01:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 167.0 |
| f1265f84-9030-3783-866d-0ea1ba4f263a | -11.885 | -54.6926 | 2025-06-21 01:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 247b911f-bada-384d-8a50-27967c9c8f0c | -11.7791 | -57.2445 | 2025-06-21 01:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 82f9dcbb-246d-33db-b02c-40c48955f3a9 | -9.2624 | -57.5228 | 2025-06-21 01:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 42105422-e675-3137-92e6-c83c2d25f483 | -11.8663 | -54.6739 | 2025-06-21 01:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 191.6 |
| e47b9128-ee5b-3584-8fec-82f08083e4e1 | -11.8666 | -54.6535 | 2025-06-21 01:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| de18a536-365f-35ed-883f-b48946249ca2 | -9.4648 | -57.8449 | 2025-06-21 01:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e83b03f3-955c-3793-a4c9-0d1eaccdf0ec | -4.5614 | -48.0141 | 2025-06-21 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7c62c0c5-18f6-3fde-8c0e-58a7618f7937 | -13.2343 | -49.8475 | 2025-06-21 01:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f5d5a625-da17-36a7-befd-3550d2300962 | -7.2408 | -43.0664 | 2025-06-21 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 36969fef-b6e3-3c5d-9266-f00e7803278f | -4.5427 | -48.0367 | 2025-06-21 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 8c4c46d7-958f-3627-a015-1fd2798ea1d9 | -11.7794 | -57.2246 | 2025-06-21 01:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| eb04d811-50f1-3f29-ba47-abfe733f8f85 | -3.9671 | -48.1283 | 2025-06-21 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 910b1e56-b7b9-3f8f-bd57-a654686380c3 | -11.798 | -57.243 | 2025-06-21 01:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 0406f69a-036c-3248-b371-b65e96e8da17 | -8.0152 | -47.6656 | 2025-06-21 01:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 55f52848-2a78-322e-850a-ac2fb6d49a94 | -4.543 | -47.9934 | 2025-06-21 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| f298b032-b2ad-381c-8596-1f2df04934a3 | -9.465 | -57.8252 | 2025-06-21 01:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c7a92bff-60ed-3733-8c1b-4dc468b2d52d | -11.8853 | -54.6722 | 2025-06-21 01:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 384.9 |
| 6386a4b5-41d8-3628-b049-a32fc8434bcf | -11.866 | -54.6944 | 2025-06-21 01:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7c3a03fa-8736-3164-bcca-e7f42e923e76 | -5.7873 | -45.8931 | 2025-06-21 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| cd697690-586b-37d3-8318-c1a2de09b5b4 | -9.4837 | -57.8241 | 2025-06-21 01:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 05bb6cd5-97bc-3b06-ac6e-8ee32fe67cdc | -13.0392 | -53.7107 | 2025-06-21 01:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 147d8e3c-a112-372a-bd6a-94ad22581ba0 | -5.7871 | -45.9155 | 2025-06-21 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| e16b22a1-b7cb-3dd6-8816-61dad93f554b | -4.5429 | -48.0151 | 2025-06-21 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 355.4 |
| aa8e0cd2-dbfb-3a6f-86bc-12c1fb64abae | -3.967 | -48.15 | 2025-06-21 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 3c3f3a3f-aef6-33d3-9436-8dddd4cc9398 | -4.5244 | -47.9943 | 2025-06-21 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 1cd43713-91e8-33a3-a169-e1ab730ff28a | -9.4835 | -57.8438 | 2025-06-21 01:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 471a13c6-76cd-3da1-9232-245fc50cccc7 | -7.2219 | -43.0682 | 2025-06-21 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 154.8 |
| fbbd2a15-2e30-3abb-9ad8-fb194509beda | -4.5243 | -48.016 | 2025-06-21 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 164.3 |
| cb1dd657-8ce4-36ac-925a-9d845efcc24d | -21.01572 | -52.82056 | 2025-06-21 01:17:00 | TERRA_M-M | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b9e80783-b3f9-3dc1-aff2-2319368f3acb | -21.69296 | -49.51665 | 2025-06-21 01:17:00 | TERRA_M-M | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| b24bc472-5387-37d8-add1-dc9342d9f472 | -21.68961 | -49.49789 | 2025-06-21 01:17:00 | TERRA_M-M | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 43.2 |
| ea15827b-8f2c-3151-8ea4-e62606580553 | -21.79695 | -52.77045 | 2025-06-21 01:17:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a81300fd-d55e-37a9-8d89-ae1c300a1ac5 | -21.01758 | -52.83224 | 2025-06-21 01:17:00 | TERRA_M-M | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c564cf24-0db5-31ec-82d3-89f596e4d35f | -21.80665 | -52.76869 | 2025-06-21 01:17:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a5312e76-e3c9-3090-bd46-a04d1e22ab79 | -11.885 | -54.6926 | 2025-06-21 01:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| eeb87e56-6766-33c9-b81c-8ba6fa1bb95f | -11.7794 | -57.2246 | 2025-06-21 01:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 7e8015ec-b070-3e6b-8167-933d0969f6f2 | -4.5429 | -48.0151 | 2025-06-21 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 373.2 |
| fc47ea5f-e49d-355d-9fb0-17dd4f553f4a | -4.5244 | -47.9943 | 2025-06-21 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 10aa746a-1676-3837-b026-4bf32a958f17 | -4.5427 | -48.0367 | 2025-06-21 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 7417181e-b548-3ae5-a1f7-5a5d3b5e5056 | -3.9671 | -48.1283 | 2025-06-21 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 97b2a9f6-9572-3a16-ae0f-3181c15cf6cf | -9.465 | -57.8252 | 2025-06-21 01:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| eadf414b-3040-329b-acf8-d0fb44a34f73 | -8.0152 | -47.6656 | 2025-06-21 01:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| c9df2125-f7af-3ed3-bec6-5e64dafac7a1 | -11.8666 | -54.6535 | 2025-06-21 01:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d0a1857b-2429-34f3-94a4-98808aba7a07 | -11.8853 | -54.6722 | 2025-06-21 01:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 354.7 |
| 825f3fd0-2fec-30b2-a238-2fd43be9be5d | -4.543 | -47.9934 | 2025-06-21 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| e9e55c20-faaf-3b1e-aff9-e540fe3dc1d8 | -11.9518 | -58.7574 | 2025-06-21 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| f3c41f7e-545d-3d30-81c6-a111bef05e19 | -9.2624 | -57.5228 | 2025-06-21 01:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 83f485cc-590a-3052-a55e-480d6d43b77f | -11.8855 | -54.6517 | 2025-06-21 01:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 6810d518-11fc-34d6-9566-38998573f6da | -9.4835 | -57.8438 | 2025-06-21 01:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 1e653da1-b815-325c-adf1-3a1a96129ef6 | -11.866 | -54.6944 | 2025-06-21 01:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c8767d90-a9c6-39d8-87ac-46ba78732ca5 | -11.7791 | -57.2445 | 2025-06-21 01:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 6693297e-6883-3251-a551-cdbcd551f326 | -7.2219 | -43.0682 | 2025-06-21 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.5 |


[Clique aqui para ver as próximas entradas](README4.md)
