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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eea827c-87a7-3a95-b2ac-8ed8bc45acea | -11.2211 | -54.8754 | 2026-08-04 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 39cbf20e-304a-3afc-822d-7c67fccdbf64 | -6.5514 | -55.1569 | 2026-08-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| d6e7e673-7a44-3591-9cbe-31b38e02df75 | -11.2022 | -54.8771 | 2026-08-04 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 40744fb7-4964-3b30-b472-d43407c887e8 | -13.4448 | -43.8604 | 2026-08-04 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| d1bd0af8-ea41-3919-a12a-b999964f5473 | -6.5329 | -55.1578 | 2026-08-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7577b2fe-b8aa-3f09-80c7-08a66e86920c | -11.2213 | -54.855 | 2026-08-04 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 73c9c341-fce8-3dbf-8633-c78473be5d05 | -3.6639 | -49.4686 | 2026-08-04 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 31567d6b-4cb1-3a56-b05a-7505bf2aaabb | -13.4254 | -43.8639 | 2026-08-04 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 5161606a-5f1c-3d60-8c07-ed999b80b4dc | -1.6408 | -54.4545 | 2026-08-04 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8db863cc-4e61-3296-9701-4458c3202dc3 | -7.226 | -59.4604 | 2026-08-04 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 54e3662e-a780-3f63-a9d9-da155354b43a | -5.1506 | -46.2026 | 2026-08-04 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 46f9727a-861f-31ae-9234-a39ef8e1416c | -7.2446 | -59.4403 | 2026-08-04 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3b3a5c80-f3af-367d-8f9c-47dfb614992a | -7.2445 | -59.4596 | 2026-08-04 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| cd1a5f34-144a-34b0-a588-37a631e165bf | -7.2261 | -59.4411 | 2026-08-04 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 6bcaaea9-bffa-36c4-bf83-f6277e4c50d3 | -3.6638 | -49.4898 | 2026-08-04 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 61e2e84d-6e76-312b-b53f-a2c0621489a4 | -13.4259 | -43.8401 | 2026-08-04 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| fa79c676-3104-35ec-b80e-97bf4fc80235 | -5.1319 | -46.2037 | 2026-08-04 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 181f609c-75b6-37d6-87e7-fd6fd7d40f64 | -6.5512 | -55.1769 | 2026-08-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 1d5af078-9622-3d76-be33-b79f44938dba | -8.3544 | -45.9897 | 2026-08-04 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 038cee1c-c801-301b-aed3-ddeb4fe69342 | -13.4453 | -43.8366 | 2026-08-04 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 64c61919-6d24-3cdf-827a-aa91264fbf17 | -6.5699 | -55.156 | 2026-08-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| bad235a1-7699-3566-b21c-f110127d605c | -11.2024 | -54.8567 | 2026-08-04 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| ba167b3e-cb30-3bb9-a184-344fd2ac9606 | -6.5697 | -55.176 | 2026-08-04 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| a5e1ce76-c249-3487-b54b-81e70761ff7f | -20.50108 | -41.67078 | 2026-08-04 00:09:00 | TERRA_M-M | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| 4cffe513-1b82-3269-a230-09908947d1d8 | -20.25185 | -46.10043 | 2026-08-04 00:09:00 | TERRA_M-M | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a93b21f1-6d96-3c4d-9ee1-a9e56bdd366d | -20.51182 | -41.66293 | 2026-08-04 00:09:00 | TERRA_M-M | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 38.6 |
| 7d301315-7da0-32a1-b7df-2cdecaf7c8bd | -21.71735 | -47.137 | 2026-08-04 00:09:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 212e90c7-103d-352b-9ea8-6c4e727d642f | -22.35141 | -47.18658 | 2026-08-04 00:09:00 | TERRA_M-M | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4b6b3e3d-113a-3d74-a2de-5f0b85922524 | -20.51571 | -41.6842 | 2026-08-04 00:09:00 | TERRA_M-M | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 4b426c17-88b3-38ab-953d-4f68e048943a | -3.6638 | -49.4898 | 2026-08-04 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 451d747d-8a14-3006-bd8b-2fb742577bfa | -5.1506 | -46.2026 | 2026-08-04 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 5b4e1379-8336-3cc9-830c-85e2b4871a64 | -6.5699 | -55.156 | 2026-08-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| c9850d25-b1af-3fa8-98e7-38e635f328ed | -1.6408 | -54.4545 | 2026-08-04 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| e43fe663-a484-367e-bc21-9d77938242aa | -6.5697 | -55.176 | 2026-08-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a48fcf30-8a14-3694-8dab-4869ed08ef98 | -6.5514 | -55.1569 | 2026-08-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 505e7a4d-96a6-3b5b-8053-ea3837595582 | -20.5087 | -41.6745 | 2026-08-04 00:10:00 | GOES-19 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 64.9 |
| 1afad2a8-7152-3242-854b-3bd0f38f674c | -6.5329 | -55.1578 | 2026-08-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| e1cb72c2-eb65-307f-a7f8-3747d7c89102 | -6.5512 | -55.1769 | 2026-08-04 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| f6d3400f-34e6-3091-8a93-bdc92a08ebe5 | -8.3546 | -45.9671 | 2026-08-04 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 37821ec8-fabd-35c6-acb2-06fa5da9b9c6 | -11.2022 | -54.8771 | 2026-08-04 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 049e80b2-1213-3a7c-bfae-5ac3a2adc7e3 | -13.4448 | -43.8604 | 2026-08-04 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e4c380a4-5532-3bff-9f58-e86baa70b5a9 | -7.2445 | -59.4596 | 2026-08-04 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| f4eecb9a-b6e6-333b-b2db-517b977b3d6e | -3.6639 | -49.4686 | 2026-08-04 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| b853ff71-7801-3737-a25a-0ffe1e7eb57c | -11.2211 | -54.8754 | 2026-08-04 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f95e19c1-92ab-3f42-b148-4982045a89ee | -7.2446 | -59.4403 | 2026-08-04 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| e0442c9b-c8b0-3a86-b114-4b7923d947ae | -7.226 | -59.4604 | 2026-08-04 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 911c9389-5848-3ea4-8ab9-5430e3f3f660 | -8.3544 | -45.9897 | 2026-08-04 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 58d05079-d033-3db4-8e4a-77c76cd3abbf | -5.1319 | -46.2037 | 2026-08-04 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 99.5 |
| e28c625c-602b-33a0-b534-92ac025f6bbf | -11.2024 | -54.8567 | 2026-08-04 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 506dbe69-e6c2-3e05-a1d6-46764e4ff326 | -3.6824 | -49.4679 | 2026-08-04 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 95802485-7dcf-3e97-94f0-b7bc48373fe0 | -11.2213 | -54.855 | 2026-08-04 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| f8bb2d45-df68-3d88-9c97-62c62ef00aa5 | -11.2019 | -54.8974 | 2026-08-04 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 215c2f23-2715-3a92-b692-92c0018e6c4b | -7.2261 | -59.4411 | 2026-08-04 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 8a400af3-ba43-3d66-87dc-1b5afab7a089 | -17.97685 | -47.17337 | 2026-08-04 00:11:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 06576499-e5e2-31bf-9546-c4a4d31103e2 | -11.94496 | -45.8004 | 2026-08-04 00:11:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7fe49000-2596-3931-b20c-0d5557bb8c8a | -18.0533 | -51.32139 | 2026-08-04 00:11:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 5828eddd-57c4-34f2-98b1-671cb070dad4 | -18.51696 | -48.33872 | 2026-08-04 00:11:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32f3828e-e78e-393d-ab4a-0c517c7cce6f | -13.44328 | -43.85831 | 2026-08-04 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| f356097e-33ec-3d93-9e8b-336e6b54adc1 | -11.94741 | -45.80921 | 2026-08-04 00:11:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 23bbe2a9-2f19-36f8-a51f-20733b163b70 | -18.6806 | -48.19411 | 2026-08-04 00:11:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 4b42c430-4d12-3539-aa33-c2a02ed308bb | -14.25842 | -45.25981 | 2026-08-04 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4121e201-bc18-3b3f-88b5-be16cb95961c | -14.34759 | -53.14886 | 2026-08-04 00:11:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bcc463ec-f566-38ff-bc87-d9cddd91a076 | -13.43062 | -43.86 | 2026-08-04 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 18df0ced-f6b8-3876-81e0-4cee928f196e | -12.44176 | -44.3207 | 2026-08-04 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 3ba18df0-017b-31ee-95be-9d0247d34854 | -11.94721 | -45.81512 | 2026-08-04 00:11:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 08449fa4-cc05-3dd1-a309-4bba071987f9 | -12.15287 | -48.44624 | 2026-08-04 00:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dcf2539b-4291-3610-a501-61bafd951d6e | -18.50767 | -48.34644 | 2026-08-04 00:11:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8336f841-b02e-33ac-b006-fcad2ab46508 | -14.2582 | -45.26552 | 2026-08-04 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| bdc5a4ef-e07c-339f-ac7c-22ccd9119388 | -17.98613 | -47.17187 | 2026-08-04 00:11:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cbb0a69f-83ed-3d0b-ad04-14299116bfba | -11.94976 | -45.82386 | 2026-08-04 00:11:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 85f49072-a156-3b72-afe8-881ed474ccef | -14.26086 | -45.27472 | 2026-08-04 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 251f3632-0808-39d8-9d67-a39758a5ff2b | -17.9753 | -47.16309 | 2026-08-04 00:11:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6479b2e6-bd40-30e2-91f5-96b7ca7ee759 | -14.49944 | -51.91495 | 2026-08-04 00:11:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ebe204ec-ea9d-3278-abf2-6816f2682039 | -12.43965 | -44.32669 | 2026-08-04 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 5c9bfd4f-f68c-338d-86ea-fc96ddb6c7ef | -11.20686 | -54.8547 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0d62df39-5824-3a6f-a8e1-b4d8d14793be | -6.56486 | -55.15012 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| cbeed9bc-9aa4-3e76-8934-0dc662299873 | -8.92594 | -45.21009 | 2026-08-04 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f68e1e0d-b251-3f08-9333-89c825925bb9 | -6.56795 | -55.17398 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| fca593ae-05e3-31c2-8d79-77d22f9fb370 | -11.19624 | -54.85619 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 80ed718e-21f7-388e-8a17-ee6393f8b990 | -5.14606 | -46.19225 | 2026-08-04 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 39892218-c689-3150-9595-7f5bd1461410 | -5.13646 | -46.2113 | 2026-08-04 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e33dbd42-3f60-3cca-b582-31ab6f1383ed | -6.5578 | -55.17532 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 0e6714bf-9227-3079-8d70-0dfeabb206d1 | -8.35824 | -48.25504 | 2026-08-04 00:13:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3547519b-84c5-3ef5-94a9-51ed94d8aeb4 | -6.95606 | -52.8232 | 2026-08-04 00:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 540d2729-6ded-3f41-a1b0-463c22067bc3 | -5.63091 | -45.91535 | 2026-08-04 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b1ff437d-df5d-3699-a018-b5fb33bb4cb6 | -6.57499 | -55.14875 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3963f77d-c9ed-358d-b1e0-1251b644540e | -7.10988 | -46.71201 | 2026-08-04 00:13:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 41a67178-1cde-337f-80c2-dc9ba0e258ab | -9.12511 | -48.38284 | 2026-08-04 00:13:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a6576cd3-994b-32a1-9fec-5d24cb846918 | -11.21016 | -54.88156 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 273efe78-f6db-35e4-adfd-0b3490677de3 | -6.98905 | -51.31018 | 2026-08-04 00:13:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a53312c9-5631-383f-92e9-1995a402f157 | -5.14861 | -46.20935 | 2026-08-04 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 8db704cb-dc81-302e-b7af-283f6f0eadc9 | -8.35594 | -48.25041 | 2026-08-04 00:13:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 724e8ab8-363f-3679-9a69-1aef209aa9bb | -9.1235 | -48.37199 | 2026-08-04 00:13:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 21a6cc69-2cff-3e3e-b69b-2dadc3068900 | -8.34676 | -45.98593 | 2026-08-04 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 985c32c6-89b9-3045-9786-0d329d6d6b65 | -8.35658 | -48.24389 | 2026-08-04 00:13:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| d0f62524-a849-357a-8cff-121e51ab63c7 | -6.57809 | -55.17255 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 81dc13a3-c8ce-3a06-bfbd-b64773f49465 | -6.06298 | -44.87403 | 2026-08-04 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 3a7e24c6-1461-3f52-9897-867b8bd78eb7 | -11.21915 | -54.86668 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1b91ccfb-ce1b-30f4-89b9-573e613cfefe | -6.48379 | -42.23123 | 2026-08-04 00:13:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 4aa36eaa-f6ef-3604-a384-b1333d111db9 | -11.19786 | -54.86944 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |


[Clique aqui para ver as próximas entradas](README2.md)
