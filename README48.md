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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe9be09c-8192-3d5d-8b83-f1c82a13c162 | -2.68541 | -57.54606 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| abfa2609-b621-3588-b609-0b013b94a480 | -8.17348 | -55.10489 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80efb23a-b01a-3c7e-a6c2-bb6b67a87cc3 | -3.57724 | -57.59604 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41eb0512-e72e-38d5-a2e4-f2a5c03621bc | -6.23332 | -51.69293 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7a19feb-a4fc-3a89-8b9c-41d637d3d646 | -7.46607 | -46.14737 | 2026-09-13 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 48768529-33b9-300f-bdb6-bf8497397b0f | -3.16144 | -58.64791 | 2026-09-13 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e461caa7-be46-325e-80b4-139d072ced48 | -4.36153 | -54.77264 | 2026-09-13 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4427fa26-2e08-3107-9b91-6dad8ef133fe | -3.36996 | -57.70918 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a02405f8-c0df-3200-9d8c-6981259915c2 | -5.90341 | -52.1059 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54a8812f-1a1a-3a5f-b1f3-36b0b2f498bc | -6.16817 | -57.71367 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 063df27d-366b-306b-b9b7-7eb2c21a3fba | -7.46289 | -46.14697 | 2026-09-13 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5a8d8db-e4fd-3788-a218-22c1c672d5a1 | -8.60614 | -55.22671 | 2026-09-13 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b52cfa53-5b4f-3dca-bda6-c39989af3024 | -5.61549 | -44.84602 | 2026-09-13 05:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37d2a051-80d7-35a7-8809-39e364e36d53 | -3.40637 | -48.89299 | 2026-09-13 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e7b59ce1-fcde-3054-95fc-1b15b1a6ee89 | -6.23517 | -51.69581 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f490da56-7742-3415-93a2-be8b4dc196bb | -6.86323 | -47.4254 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0062c7f0-a281-3a26-afc3-ff4672aae401 | -6.13926 | -57.71659 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8986aeac-807e-35f6-94ab-746b8d16a633 | -7.15035 | -44.72337 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bec1dda-e7a3-3e9a-9b2f-9bfbf83f3304 | -9.36534 | -50.09544 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19e49ee8-4825-34ac-851a-94c9c0a1f579 | -5.6134 | -44.84809 | 2026-09-13 05:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23cea165-9bf2-357c-a2a9-744add5deb38 | -4.39634 | -55.04831 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a49037c6-612a-3a1f-b6a1-56efa0b8e640 | -6.51227 | -47.60187 | 2026-09-13 05:10:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3eed52e6-2f40-386a-95ed-4d5cdd772682 | -2.53841 | -54.66117 | 2026-09-13 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 12979a85-be08-39a1-8f86-b2032ce9fa3a | -7.86559 | -54.72083 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4387a08-d581-3788-9ce1-e23412025a60 | -1.22665 | -54.12578 | 2026-09-13 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2106ecab-feb5-39d2-99dd-6c8d48d0f5fc | -4.57108 | -54.90907 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 484dbba2-a31c-35d6-93d5-be1978afb6e1 | -2.6768 | -57.53285 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb7df841-9e2f-3b78-9083-50815c7c2922 | -5.20581 | -49.33399 | 2026-09-13 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92d33bd1-0e1a-3cdd-b975-29c98a05331c | -7.85879 | -54.69732 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46fca535-8dd0-3097-9a78-da38b566e5ac | -6.13259 | -57.69289 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 56db7890-f8d2-3b34-8150-2fc5c7a184db | -5.13125 | -55.96379 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37d13c81-15bd-3f96-bc83-ff702544e07c | -8.02307 | -54.85324 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd93f7cc-b731-3c79-a8b5-c4974b5aabfa | -6.85079 | -47.43927 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e601ec9-7bcf-36e8-9fa4-e12f6d2e44b9 | -4.60569 | -46.31855 | 2026-09-13 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79631bdf-82d5-3738-b91e-92d9a66a6033 | -8.09591 | -54.85999 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6043a4b0-fb81-387f-a416-50267f75ea1d | -3.75194 | -61.20044 | 2026-09-13 05:10:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c561f6f-5379-304a-a561-6255ed908af6 | -7.8701 | -54.7141 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d45d5e5f-ab1f-3910-8fa6-e351bdcf65d6 | -6.09234 | -57.68253 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d08871e-8f23-34ea-b12b-462c6a339158 | -5.97755 | -57.76341 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52f8f3a7-27e2-3241-a40c-39c1dca4c20c | -6.23342 | -51.68099 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1615fd0-fc3c-38a3-b5c1-c8fa5bfe446e | -9.36854 | -50.10497 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 40f2fe59-aff2-3f31-bed7-7601f97ea089 | -6.23259 | -51.69768 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9311367b-dc62-3eb6-b03d-56f0d65c76fd | -6.72717 | -45.41153 | 2026-09-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c02c8e31-8acf-33fa-84c7-33d5bb8f874b | -6.30306 | -59.96211 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a209cbe-4dd0-309e-87ef-4a445391130f | -3.73071 | -61.75617 | 2026-09-13 05:10:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6e44522-3695-3178-858b-0faf6c1cc7bd | -3.40692 | -48.89441 | 2026-09-13 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 943eb553-b6db-3b17-8cb7-0c6b241d2dfd | -9.37619 | -50.11511 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 670a4f2b-bf29-3107-8d40-04587bb8ec9c | -5.37285 | -56.04824 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53774215-ae3b-37b8-914a-bb1c3ff1cc3f | -6.68373 | -58.87659 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ffa6202-1110-3715-8d4a-c36d0235b606 | -6.11038 | -57.70061 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 929502aa-c400-3623-b561-df178c5150a6 | -9.36981 | -50.09607 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b73f1911-e569-35c2-a7ac-5125222f3671 | -0.97318 | -55.38425 | 2026-09-13 05:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1df6879-68f1-332b-af11-e0d94428fe58 | -8.04466 | -54.85564 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1a82507-57bf-3ff5-b8d2-295ca9a6e2b6 | -3.16103 | -48.61233 | 2026-09-13 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5904d30e-524a-3591-af01-9c6825546d04 | -8.1196 | -54.79657 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e881f964-7c95-36e3-acec-9d15cab055ee | -2.8249 | -49.23608 | 2026-09-13 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c81c97ec-a163-3921-9fc6-9e0203d7a2ec | -4.36098 | -54.77613 | 2026-09-13 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 787f2477-baac-33f3-a57b-da7c105318e5 | -7.865 | -54.7021 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27b1c2dd-6074-3c7d-ba5b-80efe67d23f7 | -6.31591 | -59.97834 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18e619bc-6349-37d7-b1b8-9585f630e294 | -4.15493 | -50.21268 | 2026-09-13 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a41bab04-5ec8-35c7-aaf6-a34725038353 | -8.03452 | -54.85405 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5df2f2d8-85d9-30e7-ad6f-760f763c2a02 | -6.87883 | -47.427 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa7406a7-bddc-341b-9568-ff3c0030d2f0 | -3.78693 | -59.36552 | 2026-09-13 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a49d524b-68e0-382c-af91-b7e5378172db | -2.67209 | -57.53999 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9efb6b9d-ca24-3995-99e2-786c2f670f14 | -7.01782 | -44.63768 | 2026-09-13 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fcbff1c-d7ae-3a99-8577-f25b8c2d86a4 | -8.04971 | -54.84528 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2e3b1d1-998a-32ea-ae52-95797cb8b945 | -7.8718 | -54.72557 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26a77b15-fe23-31cf-b130-4615780574b1 | -2.68028 | -57.53341 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0199e4f1-02a0-3e7d-b919-401524bfc5d5 | -1.22 | -54.12478 | 2026-09-13 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 42afe18b-354e-3547-95f5-992315e4c571 | -3.16441 | -58.65278 | 2026-09-13 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef88167b-0e00-3d79-a90b-4df3ec30c383 | -4.45251 | -50.16621 | 2026-09-13 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ef1f63d-75cc-3369-aab7-107f47320590 | -3.70993 | -58.86702 | 2026-09-13 05:10:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3847a2d2-3fd7-3c17-8a0f-ab2ca1cac56e | -4.87076 | -56.00008 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0860d9c-8483-3e0d-b542-96ea7b41b9d4 | -6.09616 | -59.89949 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87b736df-5bda-3926-993e-c8f3c3df3cf0 | -9.37937 | -50.12461 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cb4244a8-9255-3faa-a69e-09b276288695 | -6.19199 | -57.71762 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b01b7300-4cbc-3afb-a128-b032f722d3e0 | -6.11683 | -57.83434 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ad84b1d-1efc-3c1f-9f1a-4c2e8e617637 | -6.30759 | -59.95814 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9dd7a4f-5716-399a-9b81-13be9577bcca | -3.70984 | -45.38964 | 2026-09-13 05:10:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23d77a6b-e3a0-3cce-9671-5caa221aaed6 | -2.95903 | -50.42251 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faa8e8cd-d46a-30a5-8645-5a9a03d1f98f | -6.65756 | -58.88052 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 902afdb2-16a6-3a6c-a275-6b4b03bc0106 | -3.04484 | -51.2655 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80f09f39-48fa-3a8f-93ec-3c30fa92da26 | -3.16553 | -48.61303 | 2026-09-13 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 828200bf-7e66-3ad4-88e3-a2a0ff1eb8a9 | -2.66717 | -57.50375 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b537042-0bda-37a7-a945-2d96f4f02514 | -8.03169 | -54.84991 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84eab915-f4f7-3d27-9409-cb1e2320a77d | -2.95601 | -50.42494 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed75b45a-0410-3db8-a2f4-05bf714f79ea | -2.96475 | -50.42105 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7eae0cd6-bb21-3a1d-86b1-03be5949a067 | -6.66466 | -58.8817 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c67704d4-9116-3dfe-941f-075c1f02247a | -6.69503 | -45.90615 | 2026-09-13 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b80b762d-1597-3a42-a552-c8a5db8862c9 | -2.95736 | -50.40654 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d14842e-7a7b-358c-84ad-98eae29d2129 | -7.86897 | -54.6989 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a500db91-2e7e-344e-a3a8-1b2e94a3a4f2 | -2.73665 | -57.63699 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb8c6886-31a1-3d30-ae54-0aced512ae4d | -6.30835 | -60.00081 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b771907-e72d-3311-abac-408bb2e9c55c | -2.71792 | -57.64194 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18dfe9e2-47be-3c98-aa1a-dacb4ce4acc8 | -2.82296 | -51.34397 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 77e916b9-1d9f-3816-8ce7-e939c041305c | -9.38383 | -50.12524 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0918e4b6-61a4-3a69-b397-1cde19f530ff | -8.11565 | -54.79968 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 472b6c12-7b57-35b9-b51a-e8ad18faf5c5 | -6.79485 | -58.79493 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7200e112-e3a3-3ed5-869f-748482625f11 | -6.06572 | -57.86798 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd4aeb39-6f2b-3787-99da-71dc81b0bf83 | -2.82777 | -49.22944 | 2026-09-13 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README49.md)
