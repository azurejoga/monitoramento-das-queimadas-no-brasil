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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f24d9362-4a3b-3ca6-8498-676ed4851216 | -15.59692 | -48.34289 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 88c8ad75-687d-30dc-9105-2e33c37e56cc | -14.75716 | -46.75747 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a2643a94-bdbd-3e86-99e0-93d3ab5d207e | -15.69347 | -48.93689 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a26ed86b-ee04-322a-8bb7-4d51ee3d23f3 | -15.70665 | -48.90454 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4bda26c5-869f-378c-9591-1dad34bdcf38 | -15.72787 | -48.98053 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8aa06884-9c4c-387a-9e7d-1b9dfb24cd21 | -14.74954 | -46.76789 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a3831be-2b9b-34c1-a482-d2dee52feb1c | -16.96713 | -49.30518 | 2025-09-01 03:47:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f09e2017-b355-3bcd-8ac6-6867b1ccc6fb | -14.78722 | -46.74509 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e836f33b-8a20-3283-b1cd-4755619451ac | -15.70764 | -48.89989 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2014a34e-46d5-3b24-b0a2-a0957a4e815d | -18.07396 | -45.94308 | 2025-09-01 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a09d5ffe-e8d0-3e35-8423-d8b5a60818bc | -14.77298 | -46.76122 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34fdea8e-8ae0-3b66-a5e9-bdad8e31894a | -15.58812 | -48.32711 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4ddef0b7-9c99-33a7-9f40-07649cf865bb | -14.75451 | -46.74311 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9bb680c-c1e8-39ff-bb14-328fed7a3416 | -17.96888 | -42.98566 | 2025-09-01 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2069889a-3993-3ebf-b1b6-d4746bcb030b | -19.42525 | -43.73594 | 2025-09-01 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 075a4c41-895e-370b-8de0-e47f6b03b8ee | -15.58918 | -48.3513 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4c868132-9e16-3d38-8315-b1a001d66650 | -14.78345 | -46.76408 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c90e891a-c412-36f6-add3-516fc2bf10c0 | -14.75488 | -46.76887 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d390243-9a01-3c84-a1e9-8bf60b215309 | -14.79057 | -46.72822 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ddd74e9c-23ec-3546-b584-8d4414fc0205 | -15.69784 | -48.88755 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b4e2194-f34c-31dd-a084-da560a1246b9 | -15.72278 | -49.00452 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9bd4c988-e1db-3414-ba45-ed69ba433577 | -21.35772 | -49.05198 | 2025-09-01 03:47:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9a2cb3d3-ab88-3066-93b7-a40c85730736 | -17.20111 | -46.07009 | 2025-09-01 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 924d56ef-f8e4-3d5b-9115-d272bd9870e4 | -15.70033 | -48.90498 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f8867762-ef38-37c3-8027-6644999e01c6 | -21.35231 | -49.05083 | 2025-09-01 03:47:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| e03a8a4c-34a6-3482-904f-1d5872a28cd1 | -21.41636 | -45.98393 | 2025-09-01 03:47:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b7b1510d-cd92-311f-9fa8-91be411c8550 | -15.58712 | -48.33199 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3eba36d9-164b-31dd-a9cf-8ce21cf40ed1 | -14.78928 | -46.7347 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f5a1539-a588-30ef-b0c4-ab56a101a03a | -15.72383 | -48.99958 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ac62bf8e-5ffc-3206-ad0b-6c04a8d47e3f | -16.15895 | -40.34812 | 2025-09-01 03:47:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8eb9033a-b823-3a13-8852-3e9090a288dc | -14.79112 | -46.72545 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c66731f2-52cc-3be1-a4b9-defbb43056d1 | -15.72173 | -49.00948 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fa6ec030-afec-3743-8c87-c9e9e78b513e | -18.12299 | -48.53313 | 2025-09-01 03:47:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1eb1be01-d358-3da9-8710-a877ca34e1e1 | -20.40534 | -46.41924 | 2025-09-01 03:47:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8911d6f3-7714-35c9-aae6-757c0c64560f | -15.60433 | -48.33656 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84d12523-7659-3a7b-8a8d-10e94be2358e | -15.77942 | -47.80716 | 2025-09-01 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 23.1 |
| fe4fde9f-a56e-30b4-8bee-93dce0105802 | -15.69241 | -48.94183 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c4796612-2f8a-364b-b168-318be4890cf2 | -14.84389 | -47.09042 | 2025-09-01 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 11c883b0-b16a-32a9-9ebe-70cc68176f08 | -15.58615 | -48.33673 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d6c98a32-6c32-314c-b860-9053ff22208e | -15.59113 | -48.34179 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6d78213a-a3e1-3744-862e-49aa84a2bc1c | -14.82139 | -46.73177 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 642916c1-2639-34d1-a4f1-9e14cd4b5899 | -18.12054 | -44.98907 | 2025-09-01 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5761128a-c86d-3891-a5dc-fd7330ec371c | -15.71477 | -48.89565 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 49efe4b0-cc4e-3a6e-944e-2b52865631bc | -15.68742 | -48.95537 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a47c93b8-d44a-3d53-8c3f-03ede8ec272e | -18.11653 | -48.5361 | 2025-09-01 03:47:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a10e35e-4129-3658-b97d-420a5c882bab | -15.58218 | -48.32747 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| af80f840-f9fb-3910-a1b9-7d43272d87c0 | -23.73289 | -54.94213 | 2025-09-01 03:47:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| e653c990-f963-3933-8bbb-c0ef74c44294 | -20.41025 | -46.41904 | 2025-09-01 03:47:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8f374a61-23cd-38d7-a244-183be5acd620 | -14.84859 | -47.09515 | 2025-09-01 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f2f673d5-1817-3791-9225-02026dcf90c9 | -15.32807 | -46.10096 | 2025-09-01 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bc31a12-fac3-3581-9158-9e84741d214c | -14.74724 | -46.75187 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2590ec75-161f-3c57-b893-f9a632cf1d33 | -15.70001 | -48.96463 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| a98746d2-3abf-377b-af3e-815c2abaacdb | -15.61912 | -47.86068 | 2025-09-01 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9b082cb-b83b-3f6f-a9c5-c8b35153c7f7 | -15.58908 | -48.32331 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b3ea2390-54c8-3d5c-a904-711a4d83c1b8 | -16.16057 | -49.63647 | 2025-09-01 03:47:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c6bc0ac0-fa28-342f-9678-8d86c61a4577 | -15.58599 | -48.33786 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b258fc0c-29cf-3257-9d1f-b16658d018fa | -15.68865 | -48.94946 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4cd94c44-701b-3860-bb5c-b2f6416a7331 | -14.76689 | -46.76406 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b912f47-83ff-392c-8fb0-c1bfb39c87e6 | -19.50903 | -45.31487 | 2025-09-01 03:47:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a75ee9c-e9d6-3bad-8681-0d791a8ab2b1 | -15.69703 | -48.9203 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55487eb3-fe3e-38b7-a5b3-82864f7452f6 | -15.72642 | -48.89937 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3a2660c-4e28-3323-b8f5-f8a36278e81f | -14.74576 | -46.75919 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 086dc4df-20be-3bae-afa2-bfaed6719cf9 | -21.08872 | -48.23119 | 2025-09-01 03:47:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a4700dd2-7555-383c-9104-369b52016683 | -17.20597 | -46.07108 | 2025-09-01 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b4a54af-b4da-33b1-a228-97d830f79304 | -17.17325 | -46.0831 | 2025-09-01 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3b66de9-8590-3717-87ec-fed2754d0338 | -21.09318 | -48.23557 | 2025-09-01 03:47:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 568f1951-9262-32a5-9b35-021c3789d4e9 | -14.77675 | -46.77003 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08c238d6-ec4d-3833-8e5f-bd690829e7f5 | -15.59094 | -48.3429 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 30f92ae7-9323-3711-8363-b04f7b692ca9 | -14.75408 | -46.77284 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4893e3fa-5630-3700-a9d1-9fe2399c9695 | -15.58698 | -48.33318 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5822270d-6ffa-322d-829c-9b46431017f4 | -15.69932 | -48.89802 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5e12f575-b328-35c4-98f0-2cdecf1e4eb8 | -14.84787 | -47.09874 | 2025-09-01 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f43106ee-b7cf-3049-b730-37a6aa3409c2 | -14.78596 | -46.72369 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ed57a036-a76d-3b11-8a48-6fbb482a8afc | -16.97308 | -49.30655 | 2025-09-01 03:47:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14ac462d-7570-3f55-b838-85cece272e67 | -16.08144 | -43.62368 | 2025-09-01 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 170f97f0-0100-3d4c-9f0b-bdb40dd694b3 | -15.60343 | -48.34084 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 186e6078-7ea5-3fa9-82e4-5e0044111368 | -15.69077 | -48.9392 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0bf9b647-6a4b-3cc0-be16-58ffe1afbf62 | -18.65781 | -52.59505 | 2025-09-01 03:47:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d01aacf0-0d95-3075-afef-1e04a521ab8b | -15.61342 | -47.86001 | 2025-09-01 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a629696a-d372-36e3-b3fe-a0cb557d32f1 | -15.59144 | -48.19448 | 2025-09-01 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7d71a00-1f71-3948-b65b-d49a9e721426 | -14.79421 | -46.73766 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ec3c8e4-0254-3cde-985d-bce3cbd2145d | -19.72065 | -45.25748 | 2025-09-01 03:47:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de8f67cb-4ba1-3a6a-ab47-9559f68ed744 | -15.58231 | -48.32614 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9d038b42-65e8-30eb-87e7-690b188a7990 | -16.15542 | -40.34754 | 2025-09-01 03:47:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1e61ec0a-e6cc-30be-a054-5daf358fcc33 | -18.64731 | -40.67913 | 2025-09-01 03:47:00 | NOAA-21 | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f2e6ec37-f294-3dd7-ac0d-30a867698f4c | -15.77394 | -47.80562 | 2025-09-01 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 5a384ac5-1c66-3c67-8859-03322aa5e5ee | -15.32867 | -46.09789 | 2025-09-01 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e824dbd-1a86-3dba-84cf-dbf3d6a47eda | -18.65745 | -52.59079 | 2025-09-01 03:47:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8992c4ee-6785-3ac1-bd1f-6e49c109bfd1 | -16.19963 | -44.22096 | 2025-09-01 03:47:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52a665dd-e73f-387d-95c1-4423625a5734 | -19.12235 | -46.45153 | 2025-09-01 03:47:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1aa5dbe5-f5e6-3811-acaa-15c620318681 | -13.6942 | -50.76626 | 2025-09-01 03:47:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 273b57e1-032a-35a6-959f-aa373d03ae77 | -14.74315 | -46.74474 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6363fd7d-268e-30d3-8f1f-3ce092901620 | -15.59585 | -48.31977 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 221e1de5-2a64-3f27-bb31-2e7186cbd543 | -14.78792 | -46.74158 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3d6080a-92b9-3218-b1e5-440a2ec08eeb | -15.69442 | -48.93247 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5fa37a7c-f0bf-3ea3-a089-769e4a36d1c3 | -21.088 | -48.23451 | 2025-09-01 03:47:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 34741e9b-03aa-324a-8eeb-aff6d42bc3f9 | -15.68977 | -48.94402 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 64f22046-1f57-3594-a2fc-a3b585e5abd0 | -14.77146 | -46.76884 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ba32109-b81b-39e7-9811-9c19bbef0dd7 | -19.85786 | -45.01714 | 2025-09-01 03:47:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf8e28c9-c211-3709-9600-9c42cac57fb6 | -14.75645 | -46.76098 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README24.md)
