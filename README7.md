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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5b025dd-c96f-3f21-b2be-926800339c2d | -9.46489 | -57.83665 | 2025-08-03 01:47:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| b7ba8cdd-819d-3cca-87b5-5a62beabaf5f | -12.6591 | -44.5117 | 2025-08-03 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 3619c6b8-5bb6-3977-bbd5-6081c3956030 | -4.5684 | -44.2036 | 2025-08-03 01:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 8d09b455-bc11-3aa7-b7e7-435d188306bb | -6.633 | -59.9457 | 2025-08-03 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 12fab7d5-13cc-3037-9656-bb29076e2f61 | -12.6402 | -44.4913 | 2025-08-03 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ab33f207-2268-308d-a161-41e68ddea96e | -7.0208 | -59.8346 | 2025-08-03 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| b7262d86-923c-31fd-8b92-4bfa430e2d96 | -6.6329 | -59.9649 | 2025-08-03 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| bb3d12cf-66c1-3713-8c60-47fff383d881 | -18.8407 | -46.4417 | 2025-08-03 01:50:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 506e1270-1d5c-3314-9eaa-8ffdcb192d10 | -9.3989 | -45.4928 | 2025-08-03 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 33e47f5d-234b-30ca-8573-96156421aa1c | -6.6375 | -59.1181 | 2025-08-03 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6b42dd9f-776e-3cf9-8e5f-4c3d0424fedd | -12.6789 | -44.4851 | 2025-08-03 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 5b7f766b-6bc2-305e-bf2c-a21bf55f88d3 | -12.6595 | -44.4882 | 2025-08-03 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 0a66a08e-f40c-36f4-b673-cc58ddde44eb | -6.6376 | -59.0988 | 2025-08-03 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e00943f9-272c-36e0-bec3-69634ce56795 | -6.6144 | -59.9656 | 2025-08-03 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 5764a028-8a8f-3211-9246-b187b852528c | -6.6559 | -59.1174 | 2025-08-03 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e7bfd279-bf7d-375a-bf26-11a77cabca48 | -6.656 | -59.0981 | 2025-08-03 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 558b48e4-215c-390b-8489-2030791ddbb4 | -21.7159 | -47.6864 | 2025-08-03 02:00:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 47.1 |
| f25df267-0443-3169-b33d-470d6ba22253 | -6.6329 | -59.9649 | 2025-08-03 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a1c31a97-3e65-3b36-9994-0e8ca2b52d68 | -6.6741 | -59.1746 | 2025-08-03 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f82a6d3d-9903-3245-817e-060ac9b6bf98 | -6.6144 | -59.9656 | 2025-08-03 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 06bdcb6b-8e34-31e2-bc5f-f053f4b88dd6 | -12.6595 | -44.4882 | 2025-08-03 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 8ea609af-21d5-325e-9a82-25af4a8d3326 | -6.656 | -59.0981 | 2025-08-03 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 10a37d53-6ff6-3d26-960b-667def512570 | -6.6145 | -59.9464 | 2025-08-03 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 47d473ea-3f72-38a5-b247-a3a11c3b9b9f | -9.3989 | -45.4928 | 2025-08-03 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 0ae707bc-957f-3678-97f2-9bb88f092f74 | -4.5684 | -44.2036 | 2025-08-03 02:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| d8b16da7-3bc7-38c2-92cf-f49ab9800639 | -6.633 | -59.9457 | 2025-08-03 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 59fee253-5547-3343-8b86-cc2c7130a5ba | -12.6591 | -44.5117 | 2025-08-03 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| abf15b34-199c-3590-990b-71e54baa23dc | -6.6559 | -59.1174 | 2025-08-03 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d01aefda-0749-3efc-9487-9f1ff2a63035 | -12.6398 | -44.5148 | 2025-08-03 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 7237d544-84a5-3032-b2d3-e0874c99ff9f | -12.6402 | -44.4913 | 2025-08-03 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a15d1d44-f95d-32f1-b9d2-d2c87bf263bc | -18.8407 | -46.4417 | 2025-08-03 02:00:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b6cab7db-28a9-3d5d-9d45-e894892410f7 | -9.3989 | -45.4928 | 2025-08-03 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a69cd536-7cdc-353b-90b8-99a9f45764a9 | -18.8407 | -46.4417 | 2025-08-03 02:10:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b4f78816-0413-3e52-8a87-63cbaeeef125 | -12.6595 | -44.4882 | 2025-08-03 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 0e94f3f2-dea0-3a93-b184-bb91b9a70b83 | -7.0208 | -59.8346 | 2025-08-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 16c5d0bb-fafa-3a1c-bd9f-f76ed1d6b548 | -4.5684 | -44.2036 | 2025-08-03 02:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 5e103a33-6ecf-3bbc-9338-b40c68b77937 | -12.6402 | -44.4913 | 2025-08-03 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c5f4a1fa-55f8-34ca-a8d3-97cfe9c9c25e | -6.6144 | -59.9656 | 2025-08-03 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 9d98c48c-e481-34a6-b932-ff19a6d9b339 | -6.6559 | -59.1174 | 2025-08-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| b8e0bafb-c681-333e-b569-1bf20eb4b179 | -6.6376 | -59.0988 | 2025-08-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6afa75d8-820b-30ed-9224-be74a498c947 | -12.6591 | -44.5117 | 2025-08-03 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a7cb926f-8883-3267-979e-0a7f0cf27393 | -6.656 | -59.0981 | 2025-08-03 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 37c6e767-6614-39ce-86e5-c3096357ee8d | -18.8407 | -46.4417 | 2025-08-03 02:20:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8b593cf4-2ed6-39b7-99dc-faa4a98266d6 | -12.6402 | -44.4913 | 2025-08-03 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| bf8a1106-b2d8-351e-86ee-bd81e2151820 | -4.5684 | -44.2036 | 2025-08-03 02:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| c4fd47dd-fb81-396d-b830-0b08f8e9272e | -12.6595 | -44.4882 | 2025-08-03 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a9e862e4-504b-34be-a3cd-4c773a472670 | -6.6376 | -59.0988 | 2025-08-03 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 59668ad6-6f61-352d-8330-06a67bc6a37a | -7.0208 | -59.8346 | 2025-08-03 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 778f243a-e61b-3b9f-bc65-408e9e6920f3 | -6.6144 | -59.9656 | 2025-08-03 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 99ffe9be-a993-3dd8-a252-a459c2fef8bd | -9.3989 | -45.4928 | 2025-08-03 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 267012df-2383-3674-9180-9bc957ec49bb | -12.6591 | -44.5117 | 2025-08-03 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 02dad853-25f4-3b23-9249-ac20bdcf3d88 | -6.6329 | -59.9649 | 2025-08-03 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 3a2c346a-23ce-3efa-ad08-f21087f43e20 | -6.656 | -59.0981 | 2025-08-03 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a5756f2f-3e4e-3d51-b158-6e877e052e57 | -6.6144 | -59.9656 | 2025-08-03 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2b7f49f2-389a-3b3b-a6f7-baa70ca13517 | -6.6329 | -59.9649 | 2025-08-03 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 9d4e2774-30b2-380f-a4b0-b3ff95dae922 | -12.6591 | -44.5117 | 2025-08-03 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 35302893-9c0a-3981-b76d-23588f00ce61 | -9.3989 | -45.4928 | 2025-08-03 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a2d83b9f-4888-3ccc-9b09-d5fde7fa02c0 | -12.6595 | -44.4882 | 2025-08-03 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| dfe32f7e-7ba6-36c5-bab8-c2bbd2c8fef8 | -12.6402 | -44.4913 | 2025-08-03 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 20864c55-2e1c-3382-9a5c-57f76e3450da | -6.633 | -59.9457 | 2025-08-03 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| de968461-ca09-342e-a9af-6639a2b28390 | -4.5684 | -44.2036 | 2025-08-03 02:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 6aef351b-6df8-35c6-9ec0-05ccff9095b6 | -6.6145 | -59.9464 | 2025-08-03 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d452a28a-9703-3110-895b-41cdf81bb268 | -4.5684 | -44.2036 | 2025-08-03 02:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3e27809e-7d31-3ddd-a47c-ecc2ef60a5ae | -6.6144 | -59.9656 | 2025-08-03 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9489aa5f-a9a3-369c-8f41-d1d371379a79 | -12.6595 | -44.4882 | 2025-08-03 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| cedf1bc9-eedb-336f-85a7-7e0cd7874cb8 | -12.6402 | -44.4913 | 2025-08-03 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| b43749a0-5d29-396a-9972-03c6a3e4c394 | -12.6591 | -44.5117 | 2025-08-03 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 1a6b9939-966e-3821-a2cd-6017b622bf7f | -4.5497 | -44.2047 | 2025-08-03 02:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 4fe0d058-e0b0-3d5b-95ef-7fda2f20b049 | -6.6375 | -59.1181 | 2025-08-03 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 12b94f87-8831-34d3-93e6-9666c6834665 | -18.8407 | -46.4417 | 2025-08-03 02:40:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 1abebafb-569f-3260-953b-669acc830722 | -12.6595 | -44.4882 | 2025-08-03 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b6710faf-c620-3ecb-984e-c986c973cb6c | -6.656 | -59.0981 | 2025-08-03 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 56b0015a-0bdf-3778-9ff1-371da030d61c | -12.6402 | -44.4913 | 2025-08-03 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| a3f5b1dc-a17a-37ff-93a5-582967559b02 | -6.6376 | -59.0988 | 2025-08-03 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6e3acf62-8d1e-3857-9893-b440360ec14e | -6.6375 | -59.1181 | 2025-08-03 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 0dabb9a4-66ea-37c6-ae8f-41ed7e88aa19 | -18.8407 | -46.4417 | 2025-08-03 02:50:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 44.0 |
| fcdbb855-92e6-3cf9-bbb2-09d217f5561d | -4.5497 | -44.2047 | 2025-08-03 02:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 9004f65c-7190-3285-a664-d900f11c7c9c | -4.5684 | -44.2036 | 2025-08-03 02:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| dcc1c4c1-5a05-3eb6-9756-3dca5f3b0a62 | -6.6559 | -59.1174 | 2025-08-03 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 68ad7a76-7c21-3a4f-a1bc-d6c9fd6bf65b | -6.6375 | -59.1181 | 2025-08-03 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e6376dbe-d377-37bf-9d1d-c06dfd6a023e | -6.656 | -59.0981 | 2025-08-03 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 5d5c0fb3-a9a7-337a-ad18-a2fedca8fe47 | -6.6559 | -59.1174 | 2025-08-03 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9cfad771-19a1-3bb1-b0c9-250da16dee0a | -12.6402 | -44.4913 | 2025-08-03 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 698a4808-158e-3b8e-b32a-8844536039e8 | -6.6376 | -59.0988 | 2025-08-03 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| a9a1bfbc-fe9a-35f2-9f2c-bb43dd78a246 | -12.6595 | -44.4882 | 2025-08-03 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d83d8759-724f-3f9d-8b00-0e61a6d8b756 | -12.6595 | -44.4882 | 2025-08-03 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| b21e9577-c001-3854-8ffe-9fca5a6fa669 | -6.6741 | -59.1746 | 2025-08-03 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 2a9a1fba-5dba-3ddc-85ee-765dfc61fcf9 | -6.6559 | -59.1174 | 2025-08-03 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e6e75ba2-2d4f-3592-b931-be5e09e14626 | -12.6591 | -44.5117 | 2025-08-03 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 8d4c94c5-1034-35b2-966a-9d9def87fe2f | -6.656 | -59.0981 | 2025-08-03 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7dfe119a-a9a7-3604-9431-de69c2b7dde0 | -6.6376 | -59.0988 | 2025-08-03 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 42362d39-6003-3f96-bd89-7c40f211c18a | -12.6402 | -44.4913 | 2025-08-03 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2d19403b-61b3-39d8-b5bd-7876ccb278ef | -4.5684 | -44.2036 | 2025-08-03 03:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| abf6d8ad-840c-3034-9ca5-199942c74d3a | -13.67121 | -41.37034 | 2025-08-03 03:15:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 032e35b5-68af-3d33-b489-e66b96bf4373 | -13.67706 | -41.37192 | 2025-08-03 03:15:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0d0516b4-7697-3ad1-a6a8-be518896769b | -13.68419 | -41.37267 | 2025-08-03 03:15:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2a81d454-eea0-37c0-aff0-b155d62366e8 | -13.67826 | -41.36639 | 2025-08-03 03:15:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f3e6aa98-0396-3c2b-8a87-a5f3423150e4 | -13.6777 | -41.3715 | 2025-08-03 03:15:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 17d2b997-80ff-3904-ab3f-431bba6214d8 | -13.67885 | -41.36599 | 2025-08-03 03:15:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 85cb39d3-11c7-32ee-9638-a0e8b5f3c973 | -13.69066 | -41.37391 | 2025-08-03 03:15:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README8.md)
