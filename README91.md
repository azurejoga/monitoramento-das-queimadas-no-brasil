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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8387c133-a03a-316d-90a2-982f66082bce | -10.09595 | -59.16647 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d85c5a3-8a04-36ce-8bc2-2a79afdd77d4 | -14.74093 | -60.22661 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60809a88-d479-3f9b-8d8f-809d240f5617 | -14.20865 | -46.23033 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 449813d7-31db-32b2-a35a-9eea24490e01 | -11.55815 | -50.57414 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b148058-08bb-3d27-95a3-b5f74064741a | -10.78995 | -50.54165 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ced67a27-620d-3dd8-a4f1-d7a0f0feee84 | -12.56942 | -45.67 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16b0d5a8-9966-3a26-b058-df194c7ee95f | -14.21458 | -46.278 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b898ed0e-2084-3e9e-9cad-9d9e6a5544ff | -15.2034 | -56.68241 | 2025-09-13 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 13aa490a-ac30-3c25-a7e5-32098d8bcc96 | -13.13269 | -47.13493 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0ee5c6e-6da3-3835-b7b0-34a397fa181c | -13.91833 | -48.28405 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 317bd79d-87b9-3125-a104-dfe5373252f7 | -14.44082 | -47.33461 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 420fe76b-6d09-3218-a2b4-ee780d6c8abf | -10.50519 | -51.52559 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01321a34-ea2f-35da-a72c-20fc498cdb27 | -12.85293 | -52.97906 | 2025-09-13 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b5c2a99-d92c-3416-92a4-981e248ad32c | -15.77344 | -52.23842 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 844b5511-c4a0-308d-8c84-80911ed1a44b | -13.4564 | -51.78592 | 2025-09-13 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e1d46cc-f297-341a-994a-fca17f0b50c2 | -10.40555 | -50.59808 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ed495c58-2388-3ad5-8bb6-9d121d9ffe64 | -15.59174 | -54.76502 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f7f500d-530e-3405-9d6e-5c78b0a873f9 | -15.68059 | -49.89902 | 2025-09-13 04:59:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 76d8b5fe-4030-325d-9935-1d144a878b38 | -11.42764 | -45.61225 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 76dc719f-6464-371c-a9a0-252b0b3a1c6b | -11.8485 | -50.58332 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06d0b4fc-cb1c-384e-a343-d344655f5747 | -14.2125 | -46.24631 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b68bb8a-c79a-3b58-9874-d3a9ab423895 | -13.11567 | -56.79809 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75ec61f8-96e6-3d78-a08d-803bac617916 | -14.20076 | -46.25274 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ee866a90-da03-378c-b4e2-bdcc361a8152 | -11.39653 | -50.47546 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f661560d-8ade-32e2-a03b-d758ed694425 | -15.77077 | -53.49641 | 2025-09-13 04:59:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 828f2343-3ff6-35a9-81c2-bf6213934c80 | -12.76709 | -47.15983 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dce61a19-017f-3660-99ff-5d1cb9e73bba | -14.18837 | -46.26277 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0e7a5bf-d732-3fd8-9799-f48ca7b0edb0 | -12.99944 | -47.99328 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6dec1c62-106a-3c7d-91bd-2f9e2fdb7d5d | -11.73049 | -46.59288 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 50eae46e-1d62-3562-8132-09035623d883 | -16.413 | -49.23761 | 2025-09-13 04:59:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1480b782-dccb-3c9a-a661-a9efa1beb18b | -12.84983 | -47.93886 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de692ff4-5111-3220-8196-41185866c559 | -15.09911 | -52.50429 | 2025-09-13 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f07bf2de-4e5e-3096-b898-48ea4c4e4e89 | -9.27467 | -59.4161 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4bf2fa22-d234-3156-bb40-c7a4e325853b | -12.12528 | -59.83882 | 2025-09-13 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2d49dc0-99ac-3beb-a63d-9e08794de208 | -12.56379 | -45.66938 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6427d530-7e8d-3a58-a4bc-8c7c1a69f7bc | -16.25514 | -50.0676 | 2025-09-13 04:59:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b0c43626-9cb3-366a-a444-30b239fa2b37 | -12.11498 | -44.84902 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e0ed29a-71f2-3b39-a160-b33130f3d24a | -14.13095 | -45.37516 | 2025-09-13 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c033d302-afbd-3e79-bb06-18d1d52d50ad | -9.163 | -60.30125 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4429d03b-645d-3ad9-ac03-17d9018287b5 | -13.77644 | -46.28858 | 2025-09-13 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3017483-7650-3337-aeea-646bb8be593f | -10.19105 | -57.53485 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f79a22d6-1580-3d37-8baa-96a3b512232e | -11.1784 | -51.41068 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 0ae6d86a-31f7-38f2-8e54-fd66d00de20f | -15.56052 | -54.80315 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5bb4511d-5bf2-3edd-b965-52f419d04030 | -14.63811 | -52.09595 | 2025-09-13 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de78c234-de37-3e35-b6dd-0d867c993ef8 | -11.18814 | -55.06066 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da334079-0bb5-31bf-a5ac-4276b8727ab0 | -11.86243 | -50.57093 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7799665e-f12c-31f2-b4e4-ef4b28a3dc4c | -11.85586 | -50.55912 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 376e719d-3b20-3a2c-a16e-276b1e43aab6 | -14.19936 | -46.2646 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ac3f9f12-5eee-3151-8dc1-d420d1c35fbf | -15.16446 | -50.15384 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e0a47f1-4a6b-3a3c-ab3a-d5e2a2252d61 | -15.15146 | -50.11775 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3c44cda-89d6-3be1-8861-5c75eb336de6 | -15.20945 | -56.68707 | 2025-09-13 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea68ebaf-4716-3d54-b2dc-065f0aa62199 | -12.93956 | -48.00006 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4037b4bb-cd7b-378c-b97c-7f63c9718907 | -11.20116 | -48.42517 | 2025-09-13 04:59:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| baac2aca-d3bb-3627-8382-d02b72253088 | -14.17908 | -46.24623 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| deebaa0f-3dff-3606-bd82-9a814b48eff2 | -12.12981 | -47.59608 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b54c70e6-267b-3aef-b038-abae9a97075d | -14.19847 | -46.27222 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4cd3d008-56c7-35fd-b6b3-133be77b3458 | -15.12643 | -52.49913 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7eded828-70e7-3c64-ab50-a22e180dcf36 | -9.82289 | -53.33559 | 2025-09-13 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbd333b2-0aa4-3ca4-982e-9f7c0781e7ba | -9.49503 | -55.95987 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6f32b820-8150-332e-9396-5bdd4ee2b25f | -10.53056 | -51.53385 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cfa1f1bd-15f6-39af-a7ea-6da10f81a5d3 | -10.70199 | -54.44267 | 2025-09-13 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c9c40616-afd6-344f-8162-03809aaa4bdb | -9.27963 | -56.89385 | 2025-09-13 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b321f07-a219-3f3f-9900-a1522e646e0f | -11.78789 | -47.40248 | 2025-09-13 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7a130909-c80c-3106-abaf-0d78aaefef3a | -10.52864 | -49.87222 | 2025-09-13 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef7d3e80-cc9d-34a8-aafd-b7db20168b0e | -14.20035 | -46.25482 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2198148e-c041-3ead-87f2-d436c50e2323 | -11.87493 | -50.56914 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 5b148409-392d-32a3-90aa-73c6f500ef3a | -11.79569 | -62.73682 | 2025-09-13 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 341a2e9e-aa68-31e2-8dce-ce72e0800040 | -16.41743 | -49.04535 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c0abbbc-65df-3d45-9c7a-50684e6c208e | -15.86596 | -51.85259 | 2025-09-13 04:59:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea21c565-60a6-3499-8872-7c68e8080d2b | -12.80854 | -47.96221 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82802cc7-eabb-32cc-9bbb-80f7e3d535cd | -11.61349 | -52.22055 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6c4c761-db3c-33c0-b5bf-bfb973127553 | -11.99374 | -47.76771 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 500f07d3-8835-338d-a78c-aae1a8051465 | -11.18087 | -51.42052 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f14aae6f-1278-349a-9f80-9d3e2a924d31 | -15.24729 | -51.39528 | 2025-09-13 04:59:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3afb9e44-9db4-3ccb-8414-214ab22add7a | -11.85705 | -49.77707 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c36769a3-5516-3a12-9e3d-5c3a65662df1 | -11.12428 | -50.70036 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 488c9dc9-dc6c-3cac-9132-3143037dbc8e | -14.21386 | -46.23682 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97a70e71-3df8-346f-bbf0-1fb4e3ea3fdd | -12.06774 | -50.94261 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95941980-78c3-363e-b143-aa7a876d4016 | -14.19992 | -46.25875 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b379086f-2de9-31aa-a996-7d22dba6118c | -9.27165 | -59.4106 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2af1bad8-d6d2-31e9-bb63-bde424617ce9 | -11.04267 | -51.41022 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 675551cd-adcf-3002-9088-fb2dbde870f8 | -11.31086 | -50.79804 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3956d4d8-2aca-33d9-9f99-caea1c54abe7 | -12.10597 | -47.58716 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed661096-b5d5-3f8a-a7eb-0d14c96f84d6 | -10.87952 | -47.2364 | 2025-09-13 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d98cf6df-002f-30be-8d55-0b32eac31afb | -13.00449 | -46.74683 | 2025-09-13 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17587f02-96a2-32c0-a099-fe3f1467be16 | -16.41572 | -49.23874 | 2025-09-13 04:59:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4c370029-83e0-34b5-ba6a-2e771f1d62a2 | -9.25882 | -59.40594 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f319529d-1272-3450-a5e6-f2ec50a72b9e | -9.29126 | -60.189 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b6576b9-f58a-303e-8e87-147fe643acde | -10.51133 | -51.5469 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d649f442-3c99-3833-ba26-718101d92222 | -12.56897 | -45.67393 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7eeecac-6812-3f25-9bff-1fb919df4cfd | -15.81618 | -52.21045 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 739d6421-bb33-3c3b-8091-2d634ba30770 | -11.42203 | -45.61195 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c253f046-cfb0-3a02-9a70-129dad4c9ac0 | -10.70167 | -48.65065 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07412917-68ac-30b1-bf86-2c325eeac07b | -14.43544 | -47.3358 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc7bebd0-7f76-3f93-a02e-0d2e172ef6cd | -12.83326 | -47.9234 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 754e0f2b-6c6b-37de-bae9-03591d4e8701 | -12.13357 | -44.84383 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12505d64-7106-3044-9822-45efa18b1c8f | -13.46021 | -51.78641 | 2025-09-13 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13a6fc25-0efc-3a7c-8ca8-a9f918ae7cc0 | -10.4063 | -50.59284 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1224b74b-cade-3565-86f2-283bfff836d0 | -12.02246 | -50.6082 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f3cdc30-3d56-3748-aef3-86e29ab3ae8f | -9.9113 | -60.21282 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README92.md)
