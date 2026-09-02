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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b347c9d-bfa5-352b-b15a-3fe678656ab3 | -5.57526 | -60.19667 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35e077d2-89cc-32e6-98aa-98a9f2927a09 | -8.76383 | -62.58404 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5cc105fa-e304-303c-9f2c-5827816e7f22 | -9.87763 | -64.9835 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9f37405-254e-36f9-8769-e71af5f6d2fb | -9.09703 | -65.50279 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63c198f4-babc-32b6-b08e-60777e59d466 | -7.30105 | -60.62423 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c28d7e17-1984-3e5f-a02f-47b231634022 | -8.68868 | -66.9091 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7803c9f-8f8d-387e-a97b-e72b303ff042 | -7.20936 | -60.67557 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fbc44b2-3549-3042-b58e-5810bff602c7 | -8.91056 | -62.36255 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 92904081-8830-33fe-88a7-b9d91961618b | -6.68874 | -58.75647 | 2026-09-02 06:01:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6332399b-700f-3428-96ab-e736a403ca9b | -8.78749 | -62.4857 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b086ab1-37c9-38c3-b461-1f7748fc1efe | -9.02478 | -65.45061 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bde34aa-8f45-3189-8640-e28ac37b6318 | -6.93547 | -59.64011 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36a01c94-03eb-315a-be3e-461a6acb619a | -9.01073 | -65.40804 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a25f7309-485f-3efc-bcb1-61985eeedd39 | -10.09635 | -68.73621 | 2026-09-02 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d77e1231-7a61-3ba8-ad00-8b0524ee3a32 | -7.35159 | -60.57888 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fde770c-d3a2-37b8-8f67-6da9eb6abfec | -8.04735 | -70.57117 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1397ea96-7273-3353-9189-1f78ed442b83 | -4.09831 | -60.66216 | 2026-09-02 06:01:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc14c7c8-df47-314a-b5a6-19473f223899 | -9.25295 | -67.39216 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 098638b8-a802-3bc2-9cb0-b22532d3d2cd | -7.37479 | -70.10995 | 2026-09-02 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8dd2d20-258e-3f59-83aa-57e062ef4903 | -8.8875 | -70.54834 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33816a98-78bd-39f7-b917-7f54eb4ffc2f | -8.82264 | -68.61237 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4611f1d-7564-3bfd-b54f-74e5da8903d6 | -9.03329 | -65.42649 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04bdbb70-6455-3c8a-b3b0-3fe5b2f4f8e8 | -9.52211 | -67.69801 | 2026-09-02 06:01:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f9b5b56-5daa-389d-916c-45571e662b08 | -9.88136 | -64.9882 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd4490c4-0120-30e0-b016-3ce6749c090e | -6.85636 | -59.47813 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b18d7cd0-f230-3e4b-ba58-47b76c58282a | -9.09294 | -65.50219 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eab68d6-c6a7-387f-b4b1-023fb7eda673 | -7.35717 | -60.57972 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbbb6550-cf2a-3645-a020-31891ac510ca | -8.90673 | -62.362 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6f52d5ce-0cfa-3063-9f48-3904472c2833 | -9.02889 | -65.45121 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 734d5fdf-1998-34db-9fce-7a90fcb9d134 | -9.02597 | -65.44812 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b48ad34-4b67-33c5-ae7d-793af565f2ba | -8.78264 | -62.48487 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9cd5218-76ae-3821-9f0e-3b9754dca501 | -7.20434 | -60.67078 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b857699-7ab6-3cb7-bed7-a4d4edf35520 | -7.21394 | -60.68371 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d596a4b-b37f-3b4b-8cf5-8f8693e11f4e | -5.58136 | -60.19375 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0be9cf9a-7e5d-315e-9d6d-c9da219d7596 | -8.76386 | -68.86473 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b66d7b15-9956-3173-9e03-9cf0b840299f | -7.72705 | -60.97333 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04e8ae3d-48ac-3f38-895b-99fb6774c2e6 | -6.91862 | -59.64462 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 073d418e-b977-399a-9563-0e4eedd95288 | -4.23749 | -62.23313 | 2026-09-02 06:01:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b9ef8f6-4079-364a-8d32-56700b3d8c08 | -8.78803 | -62.48266 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aa743cf-0e86-396f-85b8-ade625324a10 | -4.69849 | -56.05243 | 2026-09-02 06:01:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c9253ff5-6491-3c74-9c5a-4a153a307e34 | -7.77081 | -61.20243 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef49c706-076e-34c5-b0fa-04c4674aece8 | -7.7574 | -61.2018 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff53a4a7-c6b1-3325-8aa5-b5440e25b864 | -9.00482 | -67.80173 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0a1ee5b8-603e-34dd-a714-706f9d9b7fd7 | -7.69151 | -67.12658 | 2026-09-02 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a08e3676-fe77-3184-b119-4333abafb4d5 | -6.88474 | -59.40118 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 70b7c285-f3a4-32ae-a292-346d1f8482fc | -7.45442 | -59.92831 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 992a9301-b637-3f47-bfe9-0031adb73dc4 | -7.35108 | -60.58277 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 484049ae-a9a2-30fb-ad13-1a8a4e081538 | -9.25716 | -65.80945 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02bb931a-fa6d-3bfd-bf8e-69e6137411d3 | -8.89453 | -71.39478 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 706b1f85-29c0-3ebf-896f-f3767b8d0fb9 | -6.94382 | -56.46253 | 2026-09-02 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f53ee815-00c9-351b-b439-2a7cb625d94e | -7.20864 | -60.68433 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72a9de68-e1a7-3d2a-84f9-1b0be8f37112 | -6.65571 | -59.43133 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd93a9a4-ee4f-3d8f-83ed-7ffd7397e1dd | -8.78766 | -62.48557 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfdfc0fe-110b-30fd-962a-efd149c04322 | -7.76865 | -61.19986 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b48878f6-c3be-3ad4-9284-1f7e758e0f87 | -8.91179 | -62.36271 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10df8835-5cb6-3df9-a956-ad4dce9293c7 | -9.44652 | -67.4487 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 594a3839-214b-366a-b7aa-54035bd0ccb2 | -8.91706 | -63.28633 | 2026-09-02 06:01:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c1018250-bf6e-3c5d-85e7-6a09d844e6e1 | -9.01669 | -65.45431 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21639556-d329-3e6b-ba13-ef4b28f2b06b | -8.6958 | -62.93518 | 2026-09-02 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| adb270e5-7a6f-3509-826b-c601cde31224 | -8.91017 | -62.36555 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f42ff8a9-e2cf-371e-a4ea-0fe31606dcad | -8.45788 | -72.53577 | 2026-09-02 06:01:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1294b8c-e041-3ebd-9532-098523adfe41 | -6.69498 | -58.75718 | 2026-09-02 06:01:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0223ac97-102f-38ef-b09c-3d00dc64b4e5 | -8.93042 | -62.36849 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec02d101-fd2f-3399-8f01-0e7347f5336a | -8.70983 | -70.7298 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cc4e1e2-a036-30db-9fc9-88a9890457fa | -7.94995 | -70.82582 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c690df67-c74f-338e-a689-09f092c490ef | -9.6234 | -68.60049 | 2026-09-02 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec713c79-baee-378b-9597-cbe5115b028b | -7.73253 | -60.97408 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 585bf855-e6ad-3eb3-a961-a813cf6df12f | -8.54121 | -66.96739 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f81d05e-caf7-3442-b5df-a59205f1f606 | -7.21031 | -60.66832 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0f10b53-4113-3b6d-ab7e-ca71146d6d0c | -8.00232 | -70.62094 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0059694d-e9f8-38bb-a6e5-fa6f385c8c76 | -5.18043 | -60.28601 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 205b58a7-8588-3c56-b869-a52b70482cba | -9.01722 | -65.45061 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0337728-21df-39de-bf4b-84825453ca6d | -9.09763 | -70.74879 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63221d9f-90d7-382d-b330-157e325d948a | -9.08917 | -65.38016 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 15da524b-0c08-306f-9548-088413941803 | -6.94759 | -56.45769 | 2026-09-02 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f89093d5-4b13-3e91-bcbb-aadf2d6f5ffe | -8.90591 | -62.36797 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e915e73-0112-3a17-b0d4-20bf39901824 | -9.22185 | -67.52784 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baac8364-856d-345f-b30a-5a6bd640709c | -9.10205 | -68.3139 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e20775a5-76dc-3765-abfc-129ad1cd60a7 | -7.90297 | -70.6692 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ed59a26-717b-303c-a5f2-45bc87340c8b | -7.35934 | -60.60625 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9815779b-8e42-3e15-8bb0-76ebc7c723e5 | -9.875 | -64.97059 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb9c5226-9251-31f7-9430-bc4ec1527be5 | -9.00491 | -65.44881 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc3d8857-4f6b-3569-af6a-06daf3b34ad4 | -6.94674 | -56.4644 | 2026-09-02 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f15aec9-cd59-3ca9-8aaf-3f8a6bc38bd0 | -8.56901 | -63.18318 | 2026-09-02 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47cb1dfb-3196-33ef-91a6-e9e7eba2ce81 | -7.53566 | -60.72042 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a88c8998-dc88-3f9d-8a05-f90082671a70 | -7.69516 | -67.12714 | 2026-09-02 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c808f581-fc23-3a12-bb97-8165986a0b08 | -9.19067 | -65.90397 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e629599-e4d5-33ee-995f-d286a79f31c8 | -8.69242 | -66.90965 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efe19f28-855e-3132-b2f1-a9dd8309d274 | -7.19882 | -60.66983 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a431accc-b159-32f1-b34b-8e18e0d60f54 | -7.341 | -60.5815 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa9b5cd3-9627-323d-a126-15a706db35e6 | -8.82492 | -70.84112 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a9cd560-0c87-3ed0-a468-7f1bb00ec124 | -8.65263 | -70.72436 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c80c1fec-f69d-3b58-abab-971a4a9ba001 | -7.35666 | -60.58358 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cb308ef-dc20-3918-8ab8-c486d140f1c8 | -9.00345 | -65.42966 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f36d72a-d24b-3f19-81f4-6031bf99c7e6 | -8.51302 | -67.13448 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c613b29-5701-30cc-8f33-b6e8154d54d0 | -8.05332 | -70.57923 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5133fd17-95bb-3b7a-a157-f835f7147940 | -6.9447 | -56.4559 | 2026-09-02 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40c0b1a8-6ce5-3a0f-ba1d-9729dc123995 | -9.5085 | -68.59578 | 2026-09-02 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c204aa8-c1e8-3092-8efd-ea8c45756349 | -9.00756 | -65.43027 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51054eb1-6623-3242-bf48-10f087816779 | -7.21062 | -60.66995 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README64.md)
