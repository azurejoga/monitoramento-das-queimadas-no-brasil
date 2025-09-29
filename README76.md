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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 615f343d-c23e-344b-9b96-ca42c469bd07 | -13.63876 | -48.06169 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c8ef7548-b4d8-30eb-a0bb-483a0e2b2e2e | -15.3547 | -56.95389 | 2025-09-29 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81a408d9-5453-3e95-8d4e-18d86bc55d28 | -13.22603 | -50.9581 | 2025-09-29 05:27:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a2cc82b-ea9b-3980-9665-8310c8574a31 | -14.54688 | -48.40449 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfc13d81-1fd3-304f-a5a5-a476df8ee41b | -15.21782 | -50.1109 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1eebe375-f70a-373c-9ce6-60835e0680dc | -11.92625 | -48.07314 | 2025-09-29 05:27:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b9a10d2-2f42-3f36-b264-7bb18634807c | -15.21344 | -50.09884 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17f0738d-1792-3ab7-8387-54fccace5045 | -15.42531 | -48.2447 | 2025-09-29 05:27:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2134d0f7-2282-38e2-adfc-c9c8d2285095 | -13.65993 | -48.07936 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c5c2a56-b46f-3ae7-b332-c6771e41188c | -14.53784 | -48.45504 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4ada7c58-911e-30bb-8d7d-c1a4a236ef3c | -16.01155 | -59.49949 | 2025-09-29 05:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ae7c9c9-9c91-3aa4-95b4-0461b3653c67 | -10.81909 | -47.93295 | 2025-09-29 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bf7b164-74cb-30f2-9956-96c350597474 | -11.84132 | -51.80599 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2ab1c0bd-775c-3d1f-8a2b-555649a3e27b | -10.82172 | -47.93443 | 2025-09-29 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bef100cd-06f9-37eb-827c-84c8404105cc | -13.75067 | -47.91034 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 23b98c36-f052-3904-9d1f-234cce9cb8c7 | -10.04406 | -52.10432 | 2025-09-29 05:27:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f3c1f42-14db-3b0f-9c9a-b75419cede4a | -13.62622 | -48.04976 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| acde2e93-a42e-390b-b8a7-b8ee1328202a | -17.08559 | -48.57434 | 2025-09-29 05:27:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27fb015d-1d81-3803-b460-6b138405a05e | -15.25406 | -48.76826 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39e68f39-eba1-34b3-8654-60d02ec82af8 | -14.56896 | -48.28151 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca30f3e7-ac6a-3072-9e69-9cbd48a373e5 | -11.62155 | -52.86415 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d87d97e-15ec-3cc2-887c-10db3050dccc | -11.80735 | -51.80217 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44c4fa40-98bc-3720-bb47-d2b57e666f0f | -13.80832 | -47.93496 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ab3ff8b-0643-32cf-b310-c3038faeda7d | -13.79877 | -47.95664 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c552b06f-e045-3058-a86b-d33115f39d66 | -11.82057 | -51.78808 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2fe816e5-7ec7-3446-8641-9f9a835f8aa5 | -11.21498 | -47.75148 | 2025-09-29 05:27:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 295f396b-e799-330e-ab1e-591a34d983a2 | -15.26049 | -48.77544 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 69c5524e-d231-3c69-9475-ff7c659fa74b | -15.28956 | -49.50297 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1163f20a-2661-3f0e-b0b7-46ea4b212049 | -15.28461 | -49.50153 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7512096f-7ea6-34a4-ba1f-83277d14eb48 | -13.76503 | -47.91458 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cb6d1f06-5391-3aec-bd8e-3c6e44f18db7 | -14.51888 | -48.39437 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a466fe8b-22e6-3b95-9459-4fde6889ca8c | -13.79957 | -47.94854 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c00712b-5c14-3b43-af78-21b6045624bf | -13.6015 | -48.06767 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e38dbc02-8c26-3026-b6c7-f23f080f87c3 | -15.35411 | -56.95829 | 2025-09-29 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54e6fde5-8251-3c5b-976d-5d4c8e670ced | -15.43141 | -48.24844 | 2025-09-29 05:27:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42d46e6a-5a2b-371a-b1ba-00386fb13d09 | -14.54697 | -48.4352 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41ba0d86-0e44-3aa2-8c58-e82ec2dcb0d3 | -11.62488 | -52.84479 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32b328e6-2b42-3cc0-80ca-7a02b7b9b5f9 | -13.75128 | -47.9044 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c361c353-213c-3426-b2d1-b0e382f3be9b | -10.99536 | -57.06155 | 2025-09-29 05:27:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f6884e6-c708-3f4c-bef6-d587720a962f | -15.28789 | -49.51899 | 2025-09-29 05:27:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c3d1966e-2bad-3cd7-a9bb-f9199a027857 | -15.26889 | -48.76321 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6bdd3f78-55ac-3509-bc19-d3b7551a354d | -15.18587 | -48.47784 | 2025-09-29 05:27:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fe79874a-ece7-35fa-ae04-0b61978318d7 | -11.62841 | -52.85186 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e803530a-466c-3258-a1a6-7ab464323780 | -11.83756 | -51.79007 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 3038ecaa-3665-3ca0-9be6-6d612258475c | -11.62275 | -52.85437 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b73fe10-652a-3559-8932-3bcc512b8b0b | -11.82672 | -51.78482 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7f92dd32-abea-3a76-b19b-c4e1ed525a49 | -15.25111 | -48.75997 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eddaf496-dfa4-3c1a-95a9-d3adc13ee035 | -12.35235 | -54.1529 | 2025-09-29 05:27:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e529b36-9e5a-33c9-979d-4c007d870c03 | -13.62002 | -48.03818 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae50a592-0cb9-38e3-b6af-bb4f0750db42 | -16.01825 | -59.50479 | 2025-09-29 05:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de56742e-dcfe-31c2-bf84-a9d2b588a9c7 | -10.47956 | -49.37128 | 2025-09-29 05:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5361ee56-39a4-38e5-834c-98a04ab6d874 | -14.57877 | -48.23475 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28d38560-be91-371d-9d2a-e4127ba1e83c | -13.79795 | -47.89048 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26fe6efa-e315-3009-8087-8015e29924cc | -13.23066 | -50.96207 | 2025-09-29 05:27:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17580cf4-8350-36be-96c9-a492a7dfc291 | -13.63293 | -48.04726 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 28.8 |
| bf543283-c147-38d1-a8b6-0e39f2aad50f | -14.54263 | -48.44614 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 03693a24-cb06-31a2-b4a4-b41ed04b8c6f | -15.21183 | -50.10459 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dc8fbf0-f387-3d03-a705-589b262d6cb7 | -10.99144 | -57.06092 | 2025-09-29 05:27:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af9adb63-6afd-3f4b-bece-4c388fd64c61 | -16.01764 | -59.50906 | 2025-09-29 05:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2e61082-972f-3e5a-b995-0eabd0afec24 | -15.28287 | -49.50133 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3e43c205-3328-3bf0-959f-6fe78406e352 | -13.6525 | -48.08048 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af56ca51-ec76-37f3-ac94-c1b1aaed4cc8 | -11.62397 | -52.84443 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a31dc64e-6002-3544-a06d-3e3dda821a6d | -13.63402 | -48.04507 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 5b6ed186-032b-385f-8e0a-821a381814d3 | -15.19589 | -48.47846 | 2025-09-29 05:27:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 176575a6-3ec3-3429-954d-f778cd568eb2 | -14.54125 | -48.45961 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4aee5f5b-f1c6-3f31-9df4-ad46f9a2221a | -14.54395 | -48.43319 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c31801c0-80b0-3cfa-b52f-473998cc1c80 | -10.22118 | -67.0491 | 2025-09-29 05:27:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ca40f7d-2f13-32fd-9a2e-4e1924bab3f4 | -11.63013 | -52.84559 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1474e0f8-1647-3af0-a935-bd611546cccf | -11.62235 | -52.85764 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49245f7f-3c65-38b6-93b0-4eaa3f0cfc7c | -15.25754 | -48.76765 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8d16163a-e5c3-3d4f-a748-a08a84c5ff94 | -12.47789 | -54.42527 | 2025-09-29 05:27:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f4ebf8b-a685-3190-b4d5-818584a73f9b | -13.38349 | -48.16206 | 2025-09-29 05:27:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 4b94fe26-c5ea-30a5-b52a-d3d4a33d6370 | -17.7499 | -48.77146 | 2025-09-29 05:27:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47ece0ca-f351-3149-9618-02e1825b04fc | -15.2884 | -49.51415 | 2025-09-29 05:27:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 646f113d-d1e8-38b7-8cc8-1db947a9a1aa | -13.02289 | -49.45181 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 30023dae-545e-382e-9cf2-30918596d13e | -14.53919 | -48.44089 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f662fbde-0dbb-3d50-9cd6-9298921de975 | -15.25345 | -48.77433 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b2afcc14-6dc9-334d-89aa-5a360b5ae2b1 | -14.53853 | -48.44784 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ad244de9-ec15-3563-9e72-899e5e257a9c | -15.42422 | -48.24649 | 2025-09-29 05:27:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dee8a482-e852-3143-a378-9d78ee5c08a1 | -10.38314 | -58.51492 | 2025-09-29 05:27:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f1711e3-253b-330f-8a57-8247d9ddf4b0 | -17.09289 | -48.57485 | 2025-09-29 05:27:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 072887b4-eb29-397f-93fe-7a2582c74526 | -15.28976 | -49.51905 | 2025-09-29 05:27:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 22667948-2a9d-301f-926a-49bf1d9e428b | -13.75787 | -47.91227 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 09262fe4-6a63-34a5-878f-98d433fc95a9 | -13.76577 | -47.91663 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 78bac209-0db8-3a1a-ab09-f08b17e91e69 | -14.56179 | -48.2578 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4b4d510-d0f7-387a-ad83-ad7ffd47fe13 | -12.01674 | -47.79263 | 2025-09-29 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e38c39a5-688f-31e1-b698-7057b0fa9025 | -15.26163 | -48.76411 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34b8fddc-3b62-3bf6-bc0b-5942f0ca46aa | -11.9318 | -48.02275 | 2025-09-29 05:27:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0f709897-32c1-30c0-87be-e4e2ba3c830f | -13.57826 | -48.08023 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b9c0fb5-d613-3993-9632-6962e2d9130f | -15.08183 | -48.33651 | 2025-09-29 05:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c47aab95-d334-3dfb-9830-faf98dfa0495 | -14.53332 | -48.42654 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 85688b47-75a8-3417-8608-7b15dd19b4f2 | -13.64005 | -48.05828 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 812ea23d-1458-3bbd-8bd3-bbf02db05a3a | -11.92244 | -48.04223 | 2025-09-29 05:27:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3da9aff4-933e-34e5-a743-8a2ffd3ea0f4 | -13.75139 | -47.91241 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aa27ada6-2d86-37a3-ab6d-eadb9f4f6d55 | -17.09355 | -48.56744 | 2025-09-29 05:27:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f95f7df0-c73d-37f7-aaec-81f33ea47546 | -14.58207 | -48.27393 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e796e71-25ca-33a1-83b2-d9d530b615ac | -14.57108 | -48.25928 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8130f88c-dcb5-3383-a935-e9f2041f3917 | -15.29575 | -49.50945 | 2025-09-29 05:27:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ffc37c4e-f9b2-36d0-a87a-6d7b2e5e0d5f | -10.4806 | -49.36636 | 2025-09-29 05:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b7d7ffd-880c-3af1-b76a-8d38b32da529 | -15.25859 | -56.80564 | 2025-09-29 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README77.md)
