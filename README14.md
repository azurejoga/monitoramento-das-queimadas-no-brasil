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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25c1bd8a-b085-3f2d-a428-2ecb7f95152c | -6.6577 | -58.8081 | 2025-08-15 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ae0d693b-b5ab-306f-aca8-d942df74eca5 | -11.3468 | -55.4124 | 2025-08-15 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 207.9 |
| 170c7aa4-e08b-3138-9c0d-fd9afc9cb452 | -6.9302 | -59.5497 | 2025-08-15 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| f6207709-f7fc-3b3d-a67e-4ea51f4705b0 | -11.3653 | -55.4512 | 2025-08-15 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| fe955e38-55c5-3944-b108-34de7d151fda | -6.946 | -60.0104 | 2025-08-15 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 219fd105-6831-33ca-bdc1-956150022d95 | -6.7129 | -58.8251 | 2025-08-15 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 19518307-62e1-3859-b8f0-82b82d627820 | -9.518 | -60.5268 | 2025-08-15 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| b0bfb545-9f77-3227-8d28-0172b4c377de | -5.4366 | -60.1397 | 2025-08-15 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| cdd5ef9c-f2a6-3694-9dfa-3bcf5a10a276 | -9.5179 | -60.5461 | 2025-08-15 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 831dcf3a-06fb-3658-966d-694abe076bbb | -6.6945 | -58.8259 | 2025-08-15 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 16b6ce7a-f2ea-3413-b5ff-f8005315ee20 | -6.9303 | -59.5305 | 2025-08-15 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 63334697-3b95-3de9-9417-b20c9b1c3963 | -6.6576 | -58.8274 | 2025-08-15 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 15b45978-ba48-3eba-a73f-db46c21de019 | -6.676 | -58.8267 | 2025-08-15 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 0d6deb76-41c2-396f-8144-7a3054a7fb52 | -6.0623 | -59.9472 | 2025-08-15 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| fe59ef92-c3ff-34f1-a64b-73f5dc21958c | -9.1708 | -59.6568 | 2025-08-15 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 6d185426-d9df-3b4d-9a06-24ad2f6a99ab | -3.4254 | -49.0517 | 2025-08-15 02:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 49fc13ac-1817-33ae-b1e1-0dde1685e207 | -9.4956 | -40.3586 | 2025-08-15 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 6a136b61-569c-34c5-9400-7302ebf8a92c | -15.8998 | -50.1757 | 2025-08-15 02:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 36bc5eb0-cfef-37a7-8236-d1b1c6023eab | -9.208 | -59.6548 | 2025-08-15 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 4ba65366-b61f-35b6-bc28-c268a258a21f | -11.3657 | -55.4107 | 2025-08-15 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 58ca2b95-0884-3f81-aba9-eaa613d61bc8 | -8.5718 | -63.908501 | 2025-08-15 02:00:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac83b5bd-80a4-3ba7-84cb-c926702bb808 | -9.1751 | -59.698399 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60a073ae-b9d6-31a4-9177-149ea7591804 | -6.6705 | -58.8293 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b25f641b-db3f-3fef-aa11-be0eee54f75b | -7.284 | -64.700897 | 2025-08-15 02:00:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d744300a-3f9f-3ee3-aa62-12e0e663528d | -13.0768 | -57.1283 | 2025-08-15 02:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aae757da-beb8-3cc5-a198-873f8f1d2245 | -9.4012 | -60.5532 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0decea4d-bda9-3093-be8e-095fc00f934e | -7.9453 | -61.753799 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd34c6e5-57a1-3c22-be2e-0ee4ea596b18 | -6.7091 | -58.819599 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b224bf3d-78d7-3f14-9a0c-8136f3f9d839 | -9.176 | -59.661598 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae691227-9c09-3035-808d-c3a6382861a4 | -7.5307 | -61.326401 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d3cfa14-65b3-3733-bd7f-c24941877cee | -7.0946 | -59.207199 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57211c70-2bdd-3163-bdeb-986825c8a77c | -6.6994 | -58.821999 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1cfa4f21-9151-312b-811d-5358a32879d4 | -9.1901 | -59.6763 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 012a1aca-f510-3b06-9596-110b8b16eb5b | -9.1997 | -59.673801 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3cf1b09c-d484-3423-8ad2-103e7d654670 | -7.6216 | -63.520802 | 2025-08-15 02:00:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03522b78-12b5-3450-b970-5cf435017aa4 | -11.3732 | -55.4548 | 2025-08-15 02:00:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af3eee0c-1e15-3287-9917-560ddc58b057 | -8.1075 | -61.198799 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f656c00-4198-3573-a54b-77253b2c3db5 | -7.0802 | -59.231998 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94e687b1-9d86-338b-b49e-0629605b0571 | -11.7421 | -64.8974 | 2025-08-15 02:00:00 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| af4bf9a2-dc7e-3413-a82c-40ad4aacfb6a | -11.3552 | -55.426998 | 2025-08-15 02:00:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c41942ca-cd0e-3cf2-9742-8a9e1c41c66d | -6.7187 | -58.817101 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a020e258-2b33-3c6d-a3f0-140b3616d7d1 | -7.0752 | -59.212101 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 359a7942-7f54-3b4e-abb1-9a9b7b410e97 | -7.6069 | -63.502899 | 2025-08-15 02:00:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c108632-1bba-33a1-bc64-9fcc0c1d42af | -6.7145 | -58.841099 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce1704a-c27e-33a7-a791-ddc6c47f225b | -7.0996 | -59.2271 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 642c03ca-2991-3da7-978d-8072c86899a7 | -9.1707 | -59.681301 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 977d7d14-a94a-3f95-a8ef-d985c3aa3d5c | -6.0683 | -59.951698 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d70c585-2667-346c-8aca-211b8e00dca4 | -6.6952 | -58.845901 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11bf76f1-42e1-327c-b94c-be6a61abc8dc | -9.1804 | -59.678799 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e54d8369-65bb-37d9-a595-880fceee89ed | -7.968 | -61.762001 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35e83ee7-8baa-3c4e-bed8-58d632ee9001 | -7.3245 | -60.618599 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 850f2d02-da0a-3874-8309-772cd02a0ae2 | -11.7439 | -64.905197 | 2025-08-15 02:00:00 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f2aabc2b-c16f-3384-95c2-0fa5ca8f10bd | -6.9409 | -59.5359 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11ceb762-f057-36b7-a7db-20dd9b89abe4 | -9.3483 | -62.591301 | 2025-08-15 02:00:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb1edc4-e75b-365f-b432-57c3906c5843 | -10.3347 | -64.453499 | 2025-08-15 02:00:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f8f50495-5119-3173-b06b-ccbd6dd32189 | -7.5342 | -61.3405 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f3215e7a-8cef-3d9a-a42f-29203de2e5e0 | -9.1567 | -59.666599 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e63f9e4-e8b0-3b68-af53-6998c92d5120 | -7.3148 | -60.620998 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18992e53-cafa-3565-80e7-e4844b2f46d1 | -9.1664 | -59.664101 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7924c74a-a554-3812-a627-0f756a403168 | -7.3381 | -60.632 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59b2d448-2524-37af-8afe-4bcb977c3068 | -7.5312 | -61.3708 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 439b9fdf-dece-3133-b23e-0444dfd016a0 | -8.104 | -61.184799 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 143dac59-efbb-3a36-86e7-f5ab877c986c | -9.1847 | -59.6959 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c564e3d-2eee-3a7d-aef1-4fa5a0ea1043 | -9.161 | -59.683701 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff308bb4-93b6-3a87-8618-9e462620594c | -9.5117 | -60.540901 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0df6ae5b-09e4-3e3b-b280-56b2aadc83b6 | -9.1954 | -59.6567 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6290e2da-e8bb-3a05-bfc4-e228dc52fcfb | -7.8802 | -61.824501 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a140735-8c79-35b4-b628-8e1f9d330ba6 | -6.7338 | -58.836201 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 870f2434-fb9b-3914-a1e3-8b4b9de92b13 | -6.0876 | -59.946899 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 40761894-92b3-3472-b112-bf3cce41335e | -7.9583 | -63.461399 | 2025-08-15 02:00:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 278f576b-b38a-3ab3-a48d-963279a00243 | -6.4913 | -62.941502 | 2025-08-15 02:00:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdbc4d9d-bfe1-39a2-99a9-1fe42e4b399d | -13.0731 | -57.152802 | 2025-08-15 02:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca6933d9-887f-3464-bb65-887f5ba875b3 | -10.3425 | -64.442902 | 2025-08-15 02:00:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 056bea4c-2fdb-338a-95d6-2255076d7772 | -10.8677 | -62.002399 | 2025-08-15 02:00:00 | METOP-C | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| da3c3147-d374-3578-be82-fefb4d9545f5 | -6.9312 | -59.5383 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c488aa47-b74c-3ccf-9c78-5dcc9e87f7ef | -6.6898 | -58.824402 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d2a9364-ae8f-3523-9fb6-5257c5f61e3f | -9.2094 | -59.671398 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e388e99-7370-387d-8741-b85e321ad226 | -5.4479 | -60.142899 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e29ccc43-6078-3c02-bde3-4fbe3b64b1a3 | -9.508 | -60.5261 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 906eaa5b-56f2-35fc-9689-bd427256bf86 | -10.3327 | -64.445198 | 2025-08-15 02:00:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6bed007d-8076-3c7b-b014-75200a400521 | -9.5057 | -60.558102 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb18964a-1e05-37d4-b5fc-454315e9ad0a | -6.6608 | -58.831699 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2233fcba-029a-32b8-91da-cbcd4ba2b9db | -9.5154 | -60.555698 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7654598d-f50f-3216-b097-fb3fc4dd772a | -7.5347 | -61.3848 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ffe82ae1-9595-3b21-bb2e-681229698abe | -7.955 | -61.7514 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05e1782f-0f62-3fb1-8608-71c22ab1bb35 | -7.0849 | -59.209599 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbdd786c-6488-3028-836e-764dbe2e578b | -9.5214 | -60.538399 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34e9969c-e894-3a2e-a509-625c22b95435 | -10.3445 | -64.451202 | 2025-08-15 02:00:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| acaf9334-aac6-3c8a-adcd-d3f3a95b5d84 | -13.1212 | -57.1394 | 2025-08-15 02:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16f05875-f33c-3d85-b4c9-5ee125713cdd | -6.0922 | -59.965302 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdc839ee-5916-3430-b64f-51696f584804 | -7.2819 | -64.692101 | 2025-08-15 02:00:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da3bd563-ee82-3772-b4e6-a0c96f30dffb | -6.7049 | -58.843498 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af46959b-8a78-3910-bb6e-25073ae49525 | -9.2148 | -59.651699 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86545536-debd-3f19-9c68-360c77a8500f | -7.5439 | -61.3381 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6272535-cb39-3644-8b4b-0fe27b299d5e | -6.6554 | -58.810101 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3764c2e-4426-376e-b1ad-2ed0a013c388 | -7.5376 | -61.3545 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 585722ab-8349-3a02-915b-cd8ad33b99ef | -9.502 | -60.543301 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 142d1d72-3cae-3233-be23-d0111f0e9dfc | -6.7103 | -58.864899 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e894293-2264-35fa-a4e5-0d15d0cbdf33 | -7.2937 | -64.698601 | 2025-08-15 02:00:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2873967-fe2d-3b72-84f6-7944fc7f79e9 | -6.4886 | -62.930099 | 2025-08-15 02:00:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
