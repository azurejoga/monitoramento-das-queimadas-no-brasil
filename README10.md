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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f8deef4-7343-3698-864c-fd63b5a9acc0 | -9.9788 | -36.35108 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 46.8 |
| 4aa66ada-3f4c-3b97-977b-6f7d31bc7126 | -9.9792 | -36.35473 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 37.0 |
| 1e198e33-d629-33ad-9107-a78295e35901 | -6.7258 | -35.0571 | 2025-11-13 03:02:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d58a299f-404a-31c2-9b16-828680595411 | -6.4948 | -35.11584 | 2025-11-13 03:02:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 64d2d94d-2b9f-3680-bdda-a933ec0ab52f | -6.48633 | -35.12814 | 2025-11-13 03:02:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f62b0b89-936c-3741-8b0b-09bbf4d2e293 | -6.92023 | -35.13185 | 2025-11-13 03:02:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ca4bd8db-db58-3c3c-a62d-69e024beeb36 | -9.97793 | -36.35548 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| 867d1c74-ec96-344e-b46e-edb434f19a96 | -9.98532 | -36.356 | 2025-11-13 03:02:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 37.0 |
| 241d0e44-c1a5-3836-bd17-45aa7c3445e1 | -4.5344 | -46.4376 | 2025-11-13 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 39.1 |
| d912be5e-5dd7-3a73-87db-4f0d04d096c0 | -3.0916 | -49.2759 | 2025-11-13 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 7109ff2e-48b0-37b6-8161-313adeca8bba | -4.7204 | -46.4497 | 2025-11-13 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 108.2 |
| ecdad546-b8c8-37fc-9b90-01e5de0d2d5b | -4.7206 | -46.4276 | 2025-11-13 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 272d6d0d-be48-3dba-b400-d77a4dc55a18 | -12.6557 | -46.7407 | 2025-11-13 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f46cf8ac-8f0f-38cf-9b2d-6df3d18bb690 | -4.7018 | -46.4508 | 2025-11-13 03:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| f09f9a00-32a9-3cee-a253-e94fcdc40dbe | -3.8658 | -49.7998 | 2025-11-13 03:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| f636dfd0-3f5b-3ded-8221-36dd16df29d9 | -5.6436 | -41.0629 | 2025-11-13 03:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 20d404a8-9ab0-31f9-b296-3eb5429597ad | -3.0916 | -49.2759 | 2025-11-13 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 938334b3-162e-3e92-8c2f-bb2045a69c81 | -4.7018 | -46.4508 | 2025-11-13 03:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 8389d9f0-78e2-39cd-805d-330d62758705 | -3.8658 | -49.7998 | 2025-11-13 03:20:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| da74c983-6ee5-3b25-a871-73a4d2503927 | -4.7206 | -46.4276 | 2025-11-13 03:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 1708019d-bd4a-39f1-8539-9445e056ffb1 | -4.7204 | -46.4497 | 2025-11-13 03:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 108.6 |
| cde82974-845b-31dc-83ca-ca3c6fdc6613 | -21.8957 | -56.7489 | 2025-11-13 03:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9d34981f-fd69-3c11-a879-262855845bbf | -12.6557 | -46.7407 | 2025-11-13 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| f502cc4c-b961-3d97-b877-8986b646dd82 | -6.28908 | -41.73949 | 2025-11-13 03:21:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3981f09e-b4b6-3d7d-a8bd-727016c74290 | -4.45794 | -38.39074 | 2025-11-13 03:21:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| fa6dcf2c-5d51-3126-b2d2-7e4acc59e2cf | -3.7795 | -42.75807 | 2025-11-13 03:21:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a17dcda-37f9-3077-aa2f-951638a7bce4 | -6.72578 | -35.05177 | 2025-11-13 03:21:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1fd8c36-11ec-34a6-9b0e-1061e950830e | -5.61098 | -37.94448 | 2025-11-13 03:21:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 530ebe07-c71e-30cc-8d98-7680e05808dc | -5.25742 | -36.64879 | 2025-11-13 03:21:00 | NOAA-20 | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 327990e1-dd14-3334-a3f0-17ada13d3765 | -5.32897 | -35.55526 | 2025-11-13 03:21:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 67470066-cd09-3e96-b2ee-059b375cf6a9 | -5.60451 | -41.07245 | 2025-11-13 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bac1e7bb-251a-388c-abdb-640cc44b3f8f | -5.64485 | -41.07016 | 2025-11-13 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c267eb0f-5ef6-30c6-a8d1-b30484415351 | -3.47538 | -39.05738 | 2025-11-13 03:21:00 | NOAA-20 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6328129f-39ea-3f2a-a969-9f04b120bcd0 | -3.46738 | -43.19855 | 2025-11-13 03:21:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf7310bf-6f75-3936-b5e6-e7c9e553769e | -5.57783 | -42.31069 | 2025-11-13 03:21:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1a53e26c-825b-3654-b72a-d6261ab3f776 | -5.61005 | -37.94984 | 2025-11-13 03:21:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 09f4bc17-1e4c-3ce1-8a4a-a7513538a499 | -5.60843 | -41.06864 | 2025-11-13 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ef22b8c-4f02-3053-afd2-6b7974737c8e | -6.10234 | -41.58453 | 2025-11-13 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0c579ea0-ba9d-3cd4-ab36-1fb2a5eff913 | -5.09077 | -40.24311 | 2025-11-13 03:21:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3314c2ca-b9e6-314d-84ca-158161f1e914 | -6.31598 | -43.81621 | 2025-11-13 03:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9af9290e-908e-363c-b6f3-1282d8cfdc6b | -3.46852 | -43.19195 | 2025-11-13 03:21:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a436971a-b73b-35e3-94ff-ab6a8581b869 | -7.03088 | -37.25631 | 2025-11-13 03:21:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 237e91be-ed89-3155-afd1-1a7cce71896c | -5.64763 | -41.08899 | 2025-11-13 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9e048e1c-5f69-33cd-8eba-f90202587fca | -5.26421 | -43.00181 | 2025-11-13 03:21:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ec18eaa-86bc-3d75-8472-4f09131496a0 | -3.06008 | -40.0858 | 2025-11-13 03:21:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 79d5949c-66dc-3cd3-8ddb-c42cdaeb57c0 | -5.60638 | -37.94838 | 2025-11-13 03:21:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1bcb5f4c-70e5-363c-8236-0e990239608d | -6.05527 | -43.68798 | 2025-11-13 03:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64156d09-e916-3ea4-a361-756c14c808a9 | -6.48609 | -35.11574 | 2025-11-13 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b3345abc-1c43-34d5-82a0-5035e68c08d0 | -3.06588 | -40.0868 | 2025-11-13 03:21:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a67a6b1a-eb0e-3d03-ae1c-6f58680a4553 | -4.25015 | -43.79172 | 2025-11-13 03:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13cff9bc-834e-3ddb-a155-483f3fe9819e | -6.10153 | -41.58904 | 2025-11-13 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a5364781-7541-3e5a-a750-918653cc0fc2 | -5.83655 | -38.3585 | 2025-11-13 03:21:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 233066b0-5e77-3536-997e-f735d37cd9bd | -3.78445 | -42.75875 | 2025-11-13 03:21:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b19f3291-6a22-38e5-8b69-e6c9dda8ba8b | -5.08745 | -40.24134 | 2025-11-13 03:21:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6ed4f41b-ac4d-317d-8670-75aec9b1375b | -5.83751 | -38.35284 | 2025-11-13 03:21:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 2e432c55-dc8d-37e8-a335-584102515f6d | -3.05977 | -40.08751 | 2025-11-13 03:21:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 858023c6-60dc-3fd1-a167-8b6f326f4e24 | -5.84335 | -38.35504 | 2025-11-13 03:21:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 73e4f6a6-56c6-385e-bc01-f16433bf31bd | -6.72496 | -35.05676 | 2025-11-13 03:21:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3933309c-9804-3415-aa7b-3ea59ee2c681 | -6.67236 | -35.15578 | 2025-11-13 03:21:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 49716dd0-06b6-32e9-980c-82f61b093bc1 | -6.51151 | -35.32262 | 2025-11-13 03:21:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0f0fac9e-7a1f-32a4-b7af-8f7ef921b32f | -7.45163 | -35.21074 | 2025-11-13 03:21:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f8ffe7b5-b552-3ceb-8156-63d27d8d7044 | -6.28818 | -41.74448 | 2025-11-13 03:21:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9a9f66c-f084-35f4-b9d0-06fac99cdba7 | -3.46156 | -43.19069 | 2025-11-13 03:21:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 00d4bcb1-53b3-3791-8142-9a50d2accdf0 | -5.64249 | -41.08348 | 2025-11-13 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 92bbfe74-1c31-35d6-b035-9aa5dbbb9365 | -6.79414 | -35.27223 | 2025-11-13 03:21:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 08c82c98-de3f-3cb2-9359-c0141682b730 | -3.78623 | -42.75942 | 2025-11-13 03:21:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67a67613-23f6-3670-9694-24547c65c2c5 | -3.06048 | -40.08342 | 2025-11-13 03:21:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| deb9c8f7-0a59-3804-8b88-15447c85f5ac | -5.6053 | -41.06787 | 2025-11-13 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 25799546-676b-310a-921b-34b460c84dd3 | -5.61432 | -41.06989 | 2025-11-13 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 61300997-5bf6-37cf-849b-b6cda098e7f6 | -5.83841 | -38.35419 | 2025-11-13 03:21:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| de85a56e-814b-37bc-bf0a-363ff2bc2add | -3.06558 | -40.08848 | 2025-11-13 03:21:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 92f56ea0-3d26-3c5d-a1fc-614e5f2e5015 | -4.86168 | -38.67598 | 2025-11-13 03:21:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 63d4fb58-2251-3a85-9f13-2dabeba2531e | -5.6211 | -41.06618 | 2025-11-13 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 348d06b1-2df7-358e-a668-056d2e117af1 | -5.32486 | -35.55455 | 2025-11-13 03:21:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7eacaf27-dd58-3a27-91c6-457de60a3ee2 | -3.06628 | -40.08439 | 2025-11-13 03:21:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 704000b3-febb-37f1-a65e-de7e2e847c7e | -5.64407 | -41.07457 | 2025-11-13 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 1713300b-2d7e-38e8-9462-4b93973fb813 | -5.60727 | -37.94302 | 2025-11-13 03:21:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8cfe831c-3d62-37fd-81f3-d4ee689830a9 | -6.72573 | -35.05429 | 2025-11-13 03:21:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aeaf4e2b-c1ec-3dc0-8ca2-bbd6c1326340 | -5.26115 | -43.00377 | 2025-11-13 03:21:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cea515ff-20b3-3aa4-8c5c-bf2e4f39b41d | -5.26217 | -42.99798 | 2025-11-13 03:21:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f39cdb6-f300-3af7-a86d-4c38aab4f588 | -5.60174 | -41.07178 | 2025-11-13 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 638e8f63-e626-3282-9901-6d90f7949803 | -3.46272 | -43.18402 | 2025-11-13 03:21:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c33f7d8-40d1-3ea5-94cb-557c66766475 | -6.72186 | -35.05124 | 2025-11-13 03:21:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b034a572-1eb3-3660-8748-f08c2d497ebb | -5.64328 | -41.07901 | 2025-11-13 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| b2595c75-7f32-34e5-80a0-aa9b0d3fc7a2 | -5.84245 | -38.35369 | 2025-11-13 03:21:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 8d0623f1-94d8-396f-a1e0-83bc1a6229a2 | -4.45743 | -38.3937 | 2025-11-13 03:21:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 006b46ad-3f37-3c1e-bee5-75f62daa33fb | -6.29425 | -41.74585 | 2025-11-13 03:21:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 968622fe-f1c4-325a-9c78-f839b957fafa | -6.30906 | -43.81496 | 2025-11-13 03:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 102c3500-41ce-34e6-a859-ebf86a5d934a | -10.04804 | -36.46306 | 2025-11-13 03:23:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 77757723-964b-3274-9d2d-516c42880905 | -9.63664 | -44.54991 | 2025-11-13 03:23:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14855f55-3257-361c-a911-6c5286e0947f | -10.75527 | -44.91671 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 462de0d6-00db-3a04-a296-f20bf2dad3c4 | -8.74195 | -44.23711 | 2025-11-13 03:23:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0290413a-c52c-31a0-9650-d15cf1771b4b | -7.82611 | -41.77217 | 2025-11-13 03:23:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 96cacf7f-d12c-31f5-aa96-573a8082d209 | -7.1473 | -41.70877 | 2025-11-13 03:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ace2c5e1-1c51-37e5-a32f-84c5d9c255ce | -9.64224 | -44.55755 | 2025-11-13 03:23:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5c5bc18-ae48-34b3-a0db-4f54156e289c | -7.24392 | -41.63222 | 2025-11-13 03:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 31c89fb0-f74e-32e7-ae3f-fbbb4c40da6e | -10.7472 | -44.92131 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1ab8c2b-0fb4-3abb-853e-6fb5c55be486 | -6.54037 | -43.11078 | 2025-11-13 03:23:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2539044-1f1d-3537-900a-a4332e050793 | -6.87532 | -42.85861 | 2025-11-13 03:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| cbf72a98-b4d4-345c-a7b0-4be59a340658 | -10.62866 | -45.25445 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README11.md)
