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
| b9ddd55f-9345-3260-aca1-2cc1507514bf | -6.0785 | -37.3271 | 2025-01-05 00:00:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 7fb40777-998d-33e7-aa8c-e21975e62341 | -6.0788 | -37.301 | 2025-01-05 00:00:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 9dbbadf7-c1ba-3588-b160-5e1f8749b70b | -6.0785 | -37.3271 | 2025-01-05 00:10:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 59.8 |
| a7666956-5c14-3dad-97ca-2510bca76308 | -6.0788 | -37.301 | 2025-01-05 00:10:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 254bcd79-ea3b-35bf-81a8-224db529073c | -9.5603 | -40.306999 | 2025-01-05 00:14:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 507025d0-03bc-3e59-9372-1a23843baafb | -9.5587 | -40.300098 | 2025-01-05 00:14:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7d1cd80e-723c-3722-a105-847e35f6c7a4 | -6.0722 | -37.3046 | 2025-01-05 00:14:00 | METOP-C | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 5b4280b4-8f55-3279-8be0-12e7713c0d87 | -5.9837 | -39.740501 | 2025-01-05 00:14:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d67955bd-5b39-3856-a5e5-3719c36acffb | -10.427 | -39.8587 | 2025-01-05 00:14:00 | METOP-C | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6991f560-3eca-3497-82bb-ebad58651aee | -8.7158 | -41.261398 | 2025-01-05 00:14:00 | METOP-C | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 8c2590f4-a822-3465-ba75-bf2f00fadd31 | -4.328 | -39.142502 | 2025-01-05 00:14:00 | METOP-C | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b5e5f2d5-4abb-3799-adf3-a56d8c3ffb24 | -12.3536 | -39.262699 | 2025-01-05 00:14:00 | METOP-C | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2492a373-a90b-3c07-8417-c468b4d11f13 | -6.9085 | -38.838299 | 2025-01-05 00:14:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a40638c5-3957-33fa-bdd6-8f841264bfc6 | -9.5113 | -40.318199 | 2025-01-05 00:14:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 42147f68-9529-3969-86e9-e29cb8d04caf | -11.2855 | -40.276501 | 2025-01-05 00:14:00 | METOP-C | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 84a3195e-23b4-3191-bb34-48b2d8f10cfc | -12.4194 | -41.476898 | 2025-01-05 00:14:00 | METOP-C | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 46811537-223a-3958-b0aa-68a16e14b8a9 | -6.0841 | -37.311699 | 2025-01-05 00:14:00 | METOP-C | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| b316912c-af2e-3162-b4eb-0005ba01a0fc | -6.3722 | -39.858299 | 2025-01-05 00:14:00 | METOP-C | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d1e8688a-73ab-315f-ba91-144165c0c773 | -12.4096 | -41.479099 | 2025-01-05 00:14:00 | METOP-C | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5d70ceb4-5a99-3e7e-b4ba-4f6a6bad7999 | -12.4178 | -41.469601 | 2025-01-05 00:14:00 | METOP-C | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a6727b80-bde3-32a1-a34c-104abfa16b55 | -12.421 | -41.4841 | 2025-01-05 00:14:00 | METOP-C | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5e8076be-9f3a-3c4f-8b63-8939bad1eaa5 | -6.038 | -40.465599 | 2025-01-05 00:14:00 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6644d9b8-20cd-3bd4-ab2e-1a5a44eaba66 | -6.0744 | -37.313999 | 2025-01-05 00:14:00 | METOP-C | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| e48313ef-5913-3a1a-b887-2cd819051381 | -11.3955 | -37.807201 | 2025-01-05 00:14:00 | METOP-C | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 29078f15-b3b0-3d29-8577-aa36f41a1063 | -7.1327 | -40.1572 | 2025-01-05 00:14:00 | METOP-C | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fa8e6fc7-ef58-3567-96b4-3418ca6e07bb | -12.408 | -41.471802 | 2025-01-05 00:14:00 | METOP-C | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fc70190b-8b1e-368b-be96-beb2223c67a5 | -12.3552 | -39.269798 | 2025-01-05 00:14:00 | METOP-C | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b7af989-48aa-38ab-8067-ff8c9a1be11d | -5.9586 | -39.6768 | 2025-01-05 00:14:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 127bba4f-fdbf-3a62-8ba9-a4a6e8169b12 | -6.0819 | -37.302299 | 2025-01-05 00:14:00 | METOP-C | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| b13ef37f-7e65-3336-bc8f-04109257cdff | -8.583 | -37.750999 | 2025-01-05 00:14:00 | METOP-C | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 78f402de-ee25-3ceb-a847-9dc9a5fe2ed9 | -5.7034 | -39.555901 | 2025-01-05 00:14:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a0535255-0542-38eb-92b5-3adcff9da14b | -6.3738 | -39.865501 | 2025-01-05 00:14:00 | METOP-C | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5695646f-790a-3302-a4a4-c403ce64775f | -2.942 | -40.057899 | 2025-01-05 00:14:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6c05a58d-9518-32f3-a051-3068bab22fe1 | -4.3298 | -39.150501 | 2025-01-05 00:14:00 | METOP-C | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a22e049f-03f6-3c3d-bbb3-9c26046437b6 | -9.4942 | -41.012798 | 2025-01-05 00:14:00 | METOP-C | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 06246bc6-1c1a-3e3b-994b-c9f51570f24e | -9.5097 | -40.311298 | 2025-01-05 00:14:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3a9162ca-3d28-3132-b1b6-53c29486100a | -12.4112 | -41.486301 | 2025-01-05 00:14:00 | METOP-C | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ed9e2906-c42d-35ee-bfb1-42f7eb2eef20 | -7.131 | -40.150101 | 2025-01-05 00:14:00 | METOP-C | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e70a2451-da3d-398a-b228-b0d8d74f5c7a | -6.0364 | -40.458599 | 2025-01-05 00:14:00 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f51f1f71-7beb-331f-82ac-8253483feb06 | -6.0796 | -37.292801 | 2025-01-05 00:14:00 | METOP-C | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 76439a35-e08f-3353-a0af-d023dc06cfb1 | -6.0785 | -37.3271 | 2025-01-05 00:20:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 34fe3a35-13f8-36ba-838f-9e0dc8f524a9 | -6.0788 | -37.301 | 2025-01-05 00:20:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 56.6 |
| eef87ed4-bc70-36b9-9db0-c2a4426d0bef | -10.6674 | -44.4835 | 2025-01-05 00:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 20875a82-92d1-39a2-adf2-88f4f59ab142 | -6.0788 | -37.301 | 2025-01-05 00:30:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 71.0 |
| f700f7bc-63be-3b7d-b445-58d9648b8202 | -6.0785 | -37.3271 | 2025-01-05 00:30:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 52.4 |
| 9f7c0a9f-7051-35ae-8157-ae93d6e1c003 | -6.0785 | -37.3271 | 2025-01-05 00:40:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 926b3531-2786-3db3-b468-9de6ab2921c4 | -2.6435 | -45.5603 | 2025-01-05 00:40:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f72fc52a-5baf-35d1-8ca1-73abebf2dc8b | -6.0788 | -37.301 | 2025-01-05 00:40:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 77.4 |
| e4a0358f-3179-30eb-a097-2f87f5d7ce26 | -12.41222 | -41.48795 | 2025-01-05 00:49:00 | TERRA_M-M | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 38.7 |
| d9320cf5-68e6-3bfa-a96b-f22d22a29395 | -12.40024 | -41.48972 | 2025-01-05 00:49:00 | TERRA_M-M | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| ef485324-fc7a-334d-9d4d-67fe7dc2c815 | -10.21621 | -44.76425 | 2025-01-05 00:49:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1890d246-f55c-3257-ab33-33efe112f4d6 | -9.55303 | -40.30868 | 2025-01-05 00:49:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 1f381082-b0a2-339e-be0a-b6ca45faad81 | -6.0788 | -37.301 | 2025-01-05 00:50:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 57c1db29-c376-3a03-868e-2013d41b5b28 | -6.0785 | -37.3271 | 2025-01-05 00:50:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 65.3 |
| ddd8d5c9-7911-359f-9a52-595f7f48f31f | -2.63609 | -45.56365 | 2025-01-05 00:52:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| bc284b7b-e856-3427-b761-8ad74c9943ba | -2.64641 | -45.56215 | 2025-01-05 00:52:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 40.9 |
| b49173c8-622e-3260-af4a-61b425f28ae7 | -2.64814 | -45.57442 | 2025-01-05 00:52:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e629913c-1e2e-3f5f-ac7d-a6fff48f1bd2 | 1.3366 | -60.2929 | 2025-01-05 00:55:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 776aea4d-b11e-3f26-8567-aae202a09d8d | -21.853201 | -56.3904 | 2025-01-05 00:55:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f94aa546-5336-3a27-9a5c-b212aa49a5b4 | -21.8514 | -56.3815 | 2025-01-05 00:55:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2c6e6fdb-bc4f-3b97-8c98-d3dd8b2bcfb2 | -2.6435 | -45.5603 | 2025-01-05 01:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bc3b1612-605c-3f47-bc94-6afae6409c46 | -6.0785 | -37.3271 | 2025-01-05 01:00:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 61.7 |
| e5539a0d-f0e0-3463-85ac-f77b61883c5e | -6.0788 | -37.301 | 2025-01-05 01:00:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 37c2643b-4fec-3ad3-b5de-844cbb332823 | -6.0598 | -37.303 | 2025-01-05 01:10:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 48.2 |
| 87c10f06-6def-3359-9e56-b42eccbbd053 | -6.0788 | -37.301 | 2025-01-05 01:10:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 1ee4a10b-3952-3d20-a3bb-4dd03db794e4 | -2.6435 | -45.5603 | 2025-01-05 01:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 79b7854f-e337-386a-b786-73282ef7091e | -6.0785 | -37.3271 | 2025-01-05 01:10:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 0dca0b43-6f65-3166-a020-0e9fe54c9910 | -6.0788 | -37.301 | 2025-01-05 01:20:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 85.3 |
| e7d06e6b-2161-34f7-9570-71f900de9513 | -6.0785 | -37.3271 | 2025-01-05 01:20:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 48.2 |
| 496a7da3-3826-3b78-89ce-857fa40f18c7 | -6.0785 | -37.3271 | 2025-01-05 01:30:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 4a1bb782-4f4e-3a46-a690-24113e94c379 | -6.0788 | -37.301 | 2025-01-05 01:30:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 5fd459b0-70f8-316e-acda-e05e95e15eaa | -6.0785 | -37.3271 | 2025-01-05 01:40:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 46.5 |
| efb74dda-e674-3b58-bfa9-9bdfe6f91f62 | -6.0788 | -37.301 | 2025-01-05 01:40:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 6711671f-d5e9-3f1c-b855-0aa294470158 | -6.0785 | -37.3271 | 2025-01-05 01:50:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 36.7 |
| f85c7603-0d64-3eef-b94f-44cf57f2cecc | -6.0788 | -37.301 | 2025-01-05 01:50:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 50.4 |
| e8abcf3b-5167-3670-86fd-fc45ebada397 | -9.7238 | -64.531303 | 2025-01-05 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1256313b-83e6-3d61-ba40-36f320098989 | -9.7254 | -64.538597 | 2025-01-05 01:53:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 75a33670-e510-3a59-abc4-79dd02737528 | -6.0788 | -37.301 | 2025-01-05 02:00:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 51.4 |
| 56d291e1-a143-367b-abcc-6035e88e3842 | -6.0788 | -37.301 | 2025-01-05 02:10:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 41.2 |
| f3b9e111-0f7e-3ae5-a8a6-070a0c0bec0c | -6.0788 | -37.301 | 2025-01-05 02:20:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 42.5 |
| ce5d97c8-cc9d-3951-bde4-97369bf33b97 | -6.0788 | -37.301 | 2025-01-05 02:30:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 40.8 |
| 5d0b760d-3380-3577-9fa0-09bf118cf428 | -6.0788 | -37.301 | 2025-01-05 02:40:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 48.9 |
| 9710148c-e4b4-3f53-9e97-579f0d83d885 | -6.0788 | -37.301 | 2025-01-05 02:50:00 | GOES-16 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 38.7 |
| c80aea45-4cff-3738-bec0-87030408384d | -7.12421 | -40.16546 | 2025-01-05 03:23:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2f9e3e39-5dd7-3473-b8a7-e042dc46dd39 | -8.67593 | -35.37448 | 2025-01-05 03:23:00 | NOAA-21 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d295f1bb-1099-3070-b776-a35b12162556 | -8.6416 | -35.77377 | 2025-01-05 03:23:00 | NOAA-21 | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f05c7f5f-5682-3f72-85e3-ee12762acd13 | -7.12826 | -40.16224 | 2025-01-05 03:23:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e9460521-23e5-31e6-9837-9e80a0c5708c | -6.07545 | -37.30654 | 2025-01-05 03:23:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 219e1dca-cb66-359f-a468-0888de996566 | -6.07467 | -37.31121 | 2025-01-05 03:23:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 17.7 |
| d95c8b3f-d3f3-3cea-a471-75204fb606d1 | -7.12764 | -40.16583 | 2025-01-05 03:23:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0bfd2f2c-4f3d-3037-927d-dc607cb5a1d5 | -6.06707 | -35.243 | 2025-01-05 03:23:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9559f55a-5122-3003-b56f-b7078882076e | -6.83626 | -35.19505 | 2025-01-05 03:23:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 709556fa-8b9f-354a-b520-0ac680b91d1d | -6.07389 | -37.31586 | 2025-01-05 03:23:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 21454cc4-5ab9-3604-9960-9a1a6c880ad3 | -7.12486 | -40.1619 | 2025-01-05 03:23:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ea546a83-1333-3a5a-ab7b-ac12a96dc3ba | -9.1903 | -35.41159 | 2025-01-05 03:23:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d50989ba-c0ab-3a53-a7de-6d858166acbb | -9.49536 | -36.8374 | 2025-01-05 03:23:00 | NOAA-21 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dea5b3e0-463a-3762-ae5e-1b998a298ed9 | -9.1895 | -35.41632 | 2025-01-05 03:23:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c58cdca2-019f-3fe0-9fd6-140f86186cd5 | -8.42028 | -40.54124 | 2025-01-05 03:23:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ffc83c33-31ab-3863-a5f4-238630662611 | -6.84015 | -35.19574 | 2025-01-05 03:23:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c9001e4d-aaa2-340a-b4c8-a92de5731fcb | -8.85964 | -35.34245 | 2025-01-05 03:23:00 | NOAA-21 | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README2.md)
