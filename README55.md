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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b14ec229-6fea-3535-8f53-0d60c5bb94ca | -2.10772 | -52.04636 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aaecbe1-9eba-3290-a8db-e5b4fb2e21c8 | 2.7115 | -60.29744 | 2026-09-17 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 078423bc-c377-3497-b9fe-ed611afd123e | -2.09874 | -52.05726 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d707657-ab20-338b-af5e-a41085c3976b | 0.09904 | -51.06679 | 2026-09-17 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d9a2056-9b9f-35d4-a7db-e2ea828d78e4 | 0.78972 | -59.19937 | 2026-09-17 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a343861a-2488-356a-818a-bf5e3444c761 | -2.1006 | -52.04526 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4eb6e595-1fd4-393e-8207-2bdb50e4d506 | -5.76 | -45.09 | 2026-09-17 05:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11d6e4ad-8129-31ba-a5a4-a62239df8f69 | -8.47575 | -44.54892 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 96a11424-fb8e-3633-bc50-d8067df3a971 | -7.02065 | -43.38388 | 2026-09-17 05:16:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 506d50ba-a0f0-3014-874d-5e5c0b14e7b7 | -3.48152 | -54.68339 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49d00731-0777-3ba5-ba8a-b18e5b837903 | -5.83758 | -55.72221 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 348a05be-01e5-3be3-8d24-da2e702c1925 | -6.79931 | -58.78889 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 915b4994-128a-37fe-a641-b720a0a461b1 | -8.29277 | -45.64952 | 2026-09-17 05:16:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b41b8657-df51-38d6-b916-529be88ed1f1 | -7.00334 | -43.33363 | 2026-09-17 05:16:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| de1948c8-83fa-3884-8551-10af56f3452d | -3.33571 | -54.17117 | 2026-09-17 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 164ec617-b5c3-304e-9eb1-43e6439e1e99 | -5.98475 | -53.58524 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c931c03-f0c3-3797-aec5-c49a36f43bc7 | -8.48836 | -44.69865 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b9b9ec20-a100-3873-a6c1-333ebbaedddb | -3.47544 | -54.70022 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d12e6588-06c3-3db1-8e4c-dd5a7bcb4dae | -1.74635 | -55.25315 | 2026-09-17 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd3c3d71-57c4-3fc1-8160-684e8e8010ae | -6.81178 | -59.18769 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6923ae31-9785-374c-984b-c403406d8cab | -2.90531 | -54.17595 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 952b0d4b-38a8-358b-a44f-f79c4b0fb6f6 | -3.50898 | -54.48819 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb2c4ccf-1b00-371a-b2c4-2a94cab79c4a | -4.55923 | -42.9422 | 2026-09-17 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e2981bf5-b7e2-3183-9a10-dfb0f43a19fc | -9.59225 | -46.64639 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06578f7c-db3f-3d83-98b1-fd7ba92673b7 | -6.09902 | -53.54335 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e737c144-2cd6-3468-9920-148062d1827b | -3.75756 | -51.14104 | 2026-09-17 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51848b80-0095-3b0c-9f60-5b78a66c837d | -3.18015 | -48.58371 | 2026-09-17 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81ccc1bb-1416-3898-97c8-06b105948709 | -9.62557 | -45.36976 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c1548bab-5efa-3bb9-8bc2-133df15779f6 | -8.49039 | -57.63878 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dffa8be5-2ca8-3d1d-9dba-92d7dd9ebff5 | -4.52587 | -54.96818 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52574120-0c30-3c3c-ba5e-fb3c64ed1017 | -6.81828 | -59.1713 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77fe6e7c-b816-34aa-95a8-986b3b50682d | -7.97543 | -62.04232 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7174aaed-4807-3c94-a6a0-9af06b947173 | -6.1408 | -57.69356 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 549a2c2b-ce91-35b0-b1f1-22ad0305ed5c | -8.55221 | -44.47538 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db9d93dc-1c45-3750-8fcb-9b07fe96b3b8 | -3.37797 | -50.45738 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24567f2b-f8c7-31dd-9ee2-aa1b2ab5e0a4 | -6.80084 | -59.18588 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 274ea809-fe32-3075-bf62-15a14167e4d1 | -4.24142 | -54.88458 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0665b01-359b-3894-9e1f-b5efe497e4b2 | -3.17127 | -53.92824 | 2026-09-17 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9e9639c-dbc3-3604-a52b-6a58af758351 | -7.27637 | -46.79998 | 2026-09-17 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59a53aee-20cd-31c3-ac73-37a5dc8b18dc | -10.51007 | -46.28605 | 2026-09-17 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4825248-1634-35b1-b12c-d6284ecdd1ac | -3.02591 | -51.33712 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80848168-7ed3-3225-8dd8-64c2b58ae1dd | -6.37208 | -58.2938 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de9641e2-adbe-3575-b187-0da61eff523f | -9.87918 | -48.37869 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 679edb5d-9c56-3993-a016-d1c49a795040 | -2.90641 | -54.16896 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62292cc3-305f-3bb8-b9d4-f5e39ede522e | -2.89528 | -54.17438 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b1fabbb-1be7-3727-acdd-088190ad56bf | -8.4266 | -47.75493 | 2026-09-17 05:16:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5eb9621-c185-3b21-85d4-dd3b6c6fc808 | -6.31576 | -62.67387 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12282841-92a7-34e3-8d05-ec3c8fe4c87d | -6.81615 | -59.18403 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba2d90a9-f705-3c45-8641-917acf672ea6 | -10.12219 | -45.57469 | 2026-09-17 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e3777c4-a46f-3844-b2e1-b15177682c6d | -7.64751 | -44.32909 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 106bc4c7-de45-3700-9f7f-f5ae37d8b029 | -1.73135 | -55.24015 | 2026-09-17 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 336d047b-716e-307d-86f0-01d5333aae60 | -4.8793 | -56.06482 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 397902d7-334a-38da-b9c4-5c5827f5b5bc | -5.75213 | -57.59414 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d943f62e-63c2-3014-bf96-8c6cb727277c | -10.61599 | -46.09367 | 2026-09-17 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8a863de-cea2-3f70-91a4-a7a1e232a32f | -6.67595 | -43.64989 | 2026-09-17 05:16:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fb20dd11-c698-31fe-9246-b5ef550d43aa | -6.02937 | -59.92934 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f93e336f-263d-365e-8d8f-85648ec021fd | -4.80397 | -42.89541 | 2026-09-17 05:16:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1197205-9269-3a27-90d7-3481097f474d | -9.10115 | -45.71993 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| e1f52e54-3bcb-3cce-9c00-e3a5228228b3 | -2.9081 | -54.17997 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48fc4206-81c2-338e-a033-bd6c01ecfffe | -8.29648 | -45.64798 | 2026-09-17 05:16:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c421654d-15f8-3f12-909c-cc440cd98c55 | -5.83281 | -52.08928 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3de124bc-8539-32d7-8230-6ceb5eeb75e2 | -9.9458 | -45.2937 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdfc66a6-2c6c-37d5-b1c3-bcb28d3062e5 | -3.08061 | -50.5712 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4b15444-4618-3acd-aa8e-968754eea235 | -7.08503 | -41.84055 | 2026-09-17 05:16:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e8d4fc6c-a07f-3d1d-8d7b-0af087dafab1 | -7.38365 | -44.51136 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9473e4d4-a885-39c4-a601-c49fc4d7c7d7 | -7.36275 | -44.47755 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4dd3d85-95a5-3033-ba74-a2784fee6c9a | -6.35929 | -58.28365 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f24ddae-295a-398c-9b08-5fbd925a5e35 | -4.51479 | -54.97354 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de229563-8f76-36cc-ab58-e5a427eb0ba1 | -3.4222 | -58.23635 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dc2b05a-e504-3dd0-ab9f-0682edea2006 | -9.09522 | -45.71908 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3329d0f-0bca-31c7-9360-246f902007dd | -3.20596 | -54.5866 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfe4f009-a26a-38f7-8845-8883ffabae26 | -7.08962 | -42.09431 | 2026-09-17 05:16:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e0ea400e-e103-3dc9-8362-94f08e2382b4 | -4.39981 | -55.44125 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6cfa621-0129-3861-938e-a100f8d39913 | -6.43643 | -55.61125 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1719a864-f9bb-3193-bd38-6b7c9368fd47 | -5.86793 | -52.05868 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a459fa49-4167-3ef4-a20f-7d332ad29cca | -9.11834 | -45.72684 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6d3c9aa4-6682-308c-8402-0126bbf23c8c | -3.73496 | -55.94462 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c200cec-edf3-3f02-abbf-99eedbf94cb7 | -7.36207 | -44.48253 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13036322-b842-3a65-ab39-979be7ae4702 | -2.91197 | -54.15547 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 803846bb-de56-3a69-8ea6-51f603194f8f | -9.88257 | -48.39164 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 119453ce-9a65-334a-9120-5f01885f3c52 | -4.55177 | -42.94709 | 2026-09-17 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| aab8963a-d8bc-3837-8cb6-a8eaca9e6427 | -7.96584 | -44.83445 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce83159d-bdd2-3cc1-999c-caec64b30070 | -8.42823 | -47.75519 | 2026-09-17 05:16:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33d957a3-6053-304c-ba08-c59e63feec33 | -2.95774 | -50.33359 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dd2287a-eb3e-3d7e-928e-9a9342e40afa | -8.83973 | -46.9208 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6ff08f2-6e41-3a22-b81c-804d82114551 | -9.48253 | -47.23007 | 2026-09-17 05:16:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4acca480-b92a-38e7-bbc7-211c340d8de9 | -9.61997 | -45.36487 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 58a317b3-8561-3fa6-bb1a-16759a3415e3 | -4.55258 | -42.94134 | 2026-09-17 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0ace4ba2-eacf-329b-8241-68a651cf4b27 | -5.15314 | -55.94075 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d677721-0c78-33a8-b3be-51dca24e73d1 | -6.45558 | -52.83634 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5618078d-ff6b-3f16-9b7d-838f03400a51 | -9.56623 | -46.58162 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ea80979-4980-37b4-ae6c-87b254688cc5 | -5.91561 | -59.93733 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1de34959-d5be-3817-80ab-c2853cf56298 | -9.83263 | -48.35335 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff97dd24-e2e1-320d-a707-7f7891847c0e | -9.83108 | -48.36462 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75c825d6-0a54-391a-8ec5-a7a1cd99be49 | -8.56233 | -44.54865 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8a318fb7-0fa3-3575-902a-6f5783415328 | -4.5292 | -54.96871 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d69ce38a-0991-3ff0-98de-535061061fd9 | -6.81464 | -59.17067 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c055d468-d5cb-3268-962f-cc40d3d0d846 | -6.34731 | -51.77539 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ce58702-6d57-3d58-ab05-257d96305f39 | -6.78902 | -48.66301 | 2026-09-17 05:16:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04ed9764-abef-33e4-9972-0ebcf67d8994 | -7.37988 | -44.51652 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README56.md)
