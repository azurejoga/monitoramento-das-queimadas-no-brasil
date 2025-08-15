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
| c1f32bab-fd34-3818-886f-12d119126898 | -6.0807 | -59.9465 | 2025-08-15 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e92096e7-ea14-3d4e-a0c8-4806cebb3a8f | -6.9645 | -60.0097 | 2025-08-15 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| fa7fd035-3f6e-3427-ac17-468eae54271a | -11.3466 | -55.4326 | 2025-08-15 03:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1a694417-4f52-3b90-8640-9e68eca98b82 | -6.9646 | -59.9905 | 2025-08-15 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 424bcd01-fd70-3052-a94c-ecbcd00a2fa8 | -6.6576 | -58.8274 | 2025-08-15 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6eee8b29-3af9-3d63-b349-b8810f1b13eb | -9.1706 | -59.6762 | 2025-08-15 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| dda5f968-18b4-3079-9ce7-65b1f7d3c4ea | -6.6577 | -58.8081 | 2025-08-15 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c1bdd3e5-636a-3843-8663-0ac11803c190 | -11.3655 | -55.431 | 2025-08-15 03:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 0d5711f9-616f-30c2-a9b8-9e9d0be88482 | -9.4994 | -60.5278 | 2025-08-15 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| ed04d006-3fc0-33d7-af9e-9e5ff663088d | -9.1894 | -59.6558 | 2025-08-15 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f188db56-d5d7-3910-a568-efab449ac4e0 | -9.4992 | -60.547 | 2025-08-15 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 032a9cdb-76f5-3ed7-926b-1394b8dea96e | -7.3116 | -60.628 | 2025-08-15 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 769a8cd5-a45b-33ab-ba0b-12b9e13e532d | -9.1892 | -59.6752 | 2025-08-15 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| c1aa4a4f-9dc0-36bb-b5b3-3a39b9c2f489 | -9.1708 | -59.6568 | 2025-08-15 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 440d1b8c-8356-3c68-95c1-056c462cc127 | -11.3657 | -55.4107 | 2025-08-15 03:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2a056618-5b13-3f67-8d7d-5e4286faf1fb | -5.455 | -60.12 | 2025-08-15 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 2dab2522-ab62-34ba-8987-0ecda7025fd6 | -6.6945 | -58.8259 | 2025-08-15 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 7e940b92-59aa-3f7b-b4b7-1a4de353dbd1 | -9.208 | -59.6548 | 2025-08-15 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 12bd8e32-e4de-3147-b1b8-e3c1da2459cf | -7.5291 | -61.3444 | 2025-08-15 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f6dfb0fc-c4b2-31a2-a5a8-eb4a91c27fef | -6.9303 | -59.5305 | 2025-08-15 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 882fed4d-c555-3f86-867c-12f457ecdcb6 | -5.4366 | -60.1397 | 2025-08-15 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| ec17a98a-1722-3202-a47d-bf88553c6d57 | -7.5292 | -61.3254 | 2025-08-15 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0100adb3-c950-3be5-88c7-9a435ed33b64 | -7.0797 | -59.2157 | 2025-08-15 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d371f35d-f1f9-3ad1-aee7-31cd8747d17d | -6.0623 | -59.9472 | 2025-08-15 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 33336282-8b37-3a2b-a118-035506d61227 | -6.9461 | -59.9912 | 2025-08-15 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 21a5f2a1-3b5f-31ed-9a64-3daf445d772c | -6.0806 | -59.9657 | 2025-08-15 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 61432105-07d1-344b-bc50-0a8d53c459e3 | -6.7129 | -58.8251 | 2025-08-15 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| cede3446-6bf6-3f72-9c52-be1dce29649e | -9.1892 | -59.6752 | 2025-08-15 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 4f4b6ffa-93b4-3586-9f7e-578097e7a448 | -9.4994 | -60.5278 | 2025-08-15 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 49f871e3-a4a0-396e-8316-25540fba59d3 | -7.5292 | -61.3254 | 2025-08-15 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c3a65549-7cd7-3ada-b254-4e167c022d52 | -6.6576 | -58.8274 | 2025-08-15 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 86935246-9886-3726-a54a-13b363ea6652 | -6.6577 | -58.8081 | 2025-08-15 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ec967e25-6384-3d11-b7fb-8a443db8ff4b | -6.946 | -60.0104 | 2025-08-15 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.4 |
| fddee485-f33c-33d7-8062-3c8acbb1644a | -9.1706 | -59.6762 | 2025-08-15 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| fe372682-2252-393c-8852-80f70a8b44ea | -7.0797 | -59.2157 | 2025-08-15 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e2aad985-ff94-338a-b732-190c3db7a4db | -6.9302 | -59.5497 | 2025-08-15 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 3167317a-66dc-3f85-ab1e-dcb72f43d1e8 | -6.6945 | -58.8259 | 2025-08-15 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d49441d8-15cb-3403-bed6-2bcd5c6f8b29 | -11.3468 | -55.4124 | 2025-08-15 03:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 3105b011-7c51-3914-af53-4ec6fe939624 | -6.9303 | -59.5305 | 2025-08-15 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2c5f3b7c-53a5-39ec-b2d3-93921fdcbe9f | -6.7129 | -58.8251 | 2025-08-15 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a07ffaf1-17f9-36e7-9014-8eb2b92a13a9 | -6.9645 | -60.0097 | 2025-08-15 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| edd6e4c1-2680-3d35-a90d-23ed1fc5ef2a | -6.676 | -58.8267 | 2025-08-15 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 305682ae-ae82-35bd-a960-c44da18c5426 | -11.3657 | -55.4107 | 2025-08-15 03:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7068cfb9-6c32-3d60-a628-ccce3a0fac97 | -9.518 | -60.5268 | 2025-08-15 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 2071fbba-c5f7-3d4b-9e30-7fb8bb021a3c | -9.1894 | -59.6558 | 2025-08-15 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 47fbc529-ea7b-3323-b406-c8b592045ea3 | -9.208 | -59.6548 | 2025-08-15 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 79b26bc2-bedb-3a56-b704-4cf36e9ff5bb | -11.3655 | -55.431 | 2025-08-15 03:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 43338dc1-11a8-35ff-89b4-005c8c77dd9b | -9.4992 | -60.547 | 2025-08-15 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f4d101b8-5b48-3280-bfdd-44d0ba0e156e | -7.5291 | -61.3444 | 2025-08-15 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 691d5d54-8f84-337a-b4e3-84d0fb0e7d73 | -6.6944 | -58.8453 | 2025-08-15 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| b498082a-b8b5-3909-9f42-ba1ea2ed2074 | -5.455 | -60.1391 | 2025-08-15 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 77329721-b7bd-38b7-b379-b0b887a6f0f6 | -6.9461 | -59.9912 | 2025-08-15 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 772da792-37ae-3097-9849-8cb8bd29fef9 | -9.1708 | -59.6568 | 2025-08-15 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 78c380c9-408c-39f2-8ae5-aa04d5c7e519 | -11.3466 | -55.4326 | 2025-08-15 03:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c76a5209-af03-3b9d-a41b-c4ce61eee48f | -9.51663 | -40.34301 | 2025-08-15 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 28418776-8714-32bd-b171-69a4e2c7efa1 | -8.33331 | -40.98627 | 2025-08-15 03:10:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fb88d1e0-2c52-3abd-9802-69d11ba2cb37 | -9.03899 | -40.52101 | 2025-08-15 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 32be19dd-625c-3998-8f18-b5e9b732f1d6 | -9.03299 | -40.52515 | 2025-08-15 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4fe85f17-5721-3254-8406-52bf5cf69718 | -9.02645 | -40.52384 | 2025-08-15 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 75b08c89-7802-3d38-85cf-0c08ba959922 | -9.03132 | -40.52546 | 2025-08-15 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f9b2d1e2-4a38-3d75-ac37-3488a0712909 | -9.03019 | -40.53123 | 2025-08-15 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cfff514d-c721-3b09-b959-60823cc3c2f5 | -7.15905 | -40.41671 | 2025-08-15 03:10:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 02295764-e0c0-3783-b4de-313e39a932ab | -9.03244 | -40.51974 | 2025-08-15 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 80c77718-1882-361c-b87d-3395542c3454 | -9.51557 | -40.34842 | 2025-08-15 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| cbb2e4d0-7c15-3e73-b2ea-18fc24b3f2b4 | -9.0319 | -40.53093 | 2025-08-15 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 97b81d73-34dc-3a70-a065-c55b89b6dc58 | -9.02477 | -40.52421 | 2025-08-15 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b7a9d309-03f7-38c1-914d-d134ae74ef4c | -9.03408 | -40.51941 | 2025-08-15 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 370ba360-09ce-3e9d-8fe5-0c01ebdb5788 | -13.87143 | -43.49956 | 2025-08-15 03:13:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d5fe04e-02b8-3971-8f48-0a3cb1e3d9a0 | -14.79256 | -42.73079 | 2025-08-15 03:13:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0388a20b-e6c2-3b2f-93ab-2f85428aae23 | -13.8684 | -43.4925 | 2025-08-15 03:13:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12d3a316-9294-33e3-a94c-fb0af692feb7 | -13.87302 | -43.49224 | 2025-08-15 03:13:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80dcb256-91ca-36bb-8ded-ff828ba86d8c | -20.00507 | -42.2044 | 2025-08-15 03:15:00 | NOAA-20 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 108a21ad-dbca-3f29-8857-6ddfc4ae336c | -17.36275 | -44.14355 | 2025-08-15 03:15:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18276a7d-b3f4-3087-bc96-54d929a42274 | -17.36083 | -44.14472 | 2025-08-15 03:15:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a616f96a-d789-36f4-93f1-fa9baa751828 | -17.36245 | -44.13795 | 2025-08-15 03:15:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a217f49f-1f85-3e6b-a3c5-2c499a325573 | -17.64008 | -44.50216 | 2025-08-15 03:15:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd0acab2-5460-374c-8144-add91a3a8dcb | -20.39619 | -45.40471 | 2025-08-15 03:15:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| ed8946d3-0e43-36f7-b599-eea0f9f92f1e | -21.18946 | -45.68807 | 2025-08-15 03:15:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbf570e6-cc9e-3a51-be82-40d999fd7c20 | -16.69243 | -41.01423 | 2025-08-15 03:15:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e41cbe90-1bf6-3bf0-be31-1998328e2111 | -17.96321 | -41.71009 | 2025-08-15 03:15:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 45bb5853-925b-304c-a506-35f3d9ae80fe | -21.28213 | -44.04054 | 2025-08-15 03:15:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1e27cca1-1d57-3990-8974-f013f72bc57c | -20.32648 | -45.23052 | 2025-08-15 03:15:00 | NOAA-20 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2971b516-154f-3e06-9793-83a9a88e893c | -17.64387 | -44.50236 | 2025-08-15 03:15:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 470a4626-5438-37d2-ab31-4413abd39877 | -21.28248 | -44.03785 | 2025-08-15 03:15:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 73c173bf-a5e0-3b06-bb85-9d3f712fdcae | -20.39901 | -45.40646 | 2025-08-15 03:15:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 4ba67bb7-4834-3956-aa01-39268297a078 | -17.64688 | -44.50484 | 2025-08-15 03:15:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af5d2527-09a6-3bcc-a0ac-f5a3ae1eaced | -21.28347 | -44.03508 | 2025-08-15 03:15:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 895b89d1-f239-3cf9-b89d-9218bfec025c | -6.6577 | -58.8081 | 2025-08-15 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 10119c17-a9f5-3f56-9629-f8ce5ded7d87 | -9.5179 | -60.5461 | 2025-08-15 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 0e5a86c5-70fd-3f6d-a9e0-829317b4ec70 | -9.5147 | -40.3558 | 2025-08-15 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 116.8 |
| b3f66331-f771-3f76-9097-d7e84bd8a563 | -6.6945 | -58.8259 | 2025-08-15 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 124877f4-dc0e-3c33-a6a6-c586a88c0b48 | -6.9303 | -59.5305 | 2025-08-15 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 40c4aa60-e064-3702-a160-01aa56f9c906 | -9.1708 | -59.6568 | 2025-08-15 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| a6922864-fb1f-338a-b6fc-4a5f53f92f96 | -6.9302 | -59.5497 | 2025-08-15 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 17da42ac-e25d-3630-a690-de2697b27f6f | -11.3655 | -55.431 | 2025-08-15 03:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c691e912-1598-3605-b96b-ebf20f331da0 | -11.3468 | -55.4124 | 2025-08-15 03:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 454a7130-eb52-3d42-98bc-382f9cc82267 | -11.3466 | -55.4326 | 2025-08-15 03:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| e29c8e1e-b469-3237-bf43-c7508ff360bf | -9.4994 | -60.5278 | 2025-08-15 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| db64c8d0-d37c-3b51-b9db-566d4b0abca4 | -9.208 | -59.6548 | 2025-08-15 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 915b00a8-fd41-3895-a165-344294d546f9 | -9.4992 | -60.547 | 2025-08-15 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |


[Clique aqui para ver as próximas entradas](README18.md)
