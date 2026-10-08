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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85cd97af-19ac-31e4-b2b5-dcc993a9d692 | -3.01403 | -54.24096 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b03497d-b003-34a5-b905-5a4cec911107 | -10.98357 | -49.67393 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e78b44e6-3724-35ef-98db-684234b453f7 | -3.08383 | -54.24552 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0c5e129-e762-3751-afc1-44c54b609fcc | -3.5218 | -54.66389 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1471c13a-1710-3988-a3cd-a1d78e8f46a0 | -3.00903 | -54.10448 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| e80ba7c8-2812-31f9-a4e0-3a36539581ec | -3.00673 | -54.09513 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 27c9c85e-e0a7-3639-8a1e-901ce7938cc4 | -7.14234 | -46.52681 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1cd837e-399a-315f-9134-0f71c5b5b1e8 | -3.70364 | -61.32316 | 2026-10-08 04:46:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10b8e3da-4410-3c0b-a894-1d50cc42d052 | -9.14554 | -45.83407 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 929a4e5c-5a0c-3847-990a-c908975b46b9 | -4.21745 | -51.23653 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67f85e98-17fb-3261-b367-3e194fdb2dd5 | -3.84881 | -58.89828 | 2026-10-08 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37829a04-73ad-38af-a02f-eb459c0559ce | -3.28624 | -54.08117 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f593e624-0bb9-30be-b4eb-93800a2e27f4 | -3.30007 | -54.06553 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f485ab68-cc20-3b77-981e-51a8ec345a8f | -2.93566 | -54.14438 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2c61819-f4b8-323b-8c91-75b4135e223f | -2.5668 | -56.16777 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 729f5e5a-684a-35fa-90cb-3ec335985204 | -4.29886 | -50.78098 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8687fd63-c212-3d77-bd34-991b0198bf02 | -7.21374 | -44.28675 | 2026-10-08 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 96a9ad41-2ef8-3d88-8528-a3ee9fe3efe9 | -3.67137 | -54.5077 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b187185-4c81-3174-959a-70d6e118fb20 | -6.93284 | -43.67086 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebc28e46-0939-321e-b2fa-ffe7747207e4 | -3.27225 | -54.05378 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac292441-0a04-3110-8338-74207808efb9 | -3.71532 | -60.54572 | 2026-10-08 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abf5a784-5b6c-3cc7-903e-439fe1bb9e97 | -3.03257 | -54.09916 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8c7bc769-2d76-384d-8ca6-c795bb92a949 | -4.91794 | -55.85589 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9aaf6e00-ea46-3c04-9004-d28a751d5592 | -2.94519 | -54.17124 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7cb68212-9155-31da-bf1e-3c430a239b1c | -2.94904 | -54.19444 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97a952ce-209b-3b75-bf8b-790673efc9df | -3.01897 | -54.06569 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22a21458-881d-3091-8267-0b360f04f0d8 | -3.29483 | -54.05144 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab0c2376-74d2-36de-a1cb-f4471ed55c3b | -4.29503 | -50.78391 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a58d0858-d57f-3e2f-8ec7-5831aed70f27 | -10.12834 | -55.65166 | 2026-10-08 04:46:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b0d12c7-6591-345a-a2de-7f2fffec763b | -3.07777 | -53.95521 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 47522a84-5b9e-3034-a921-a8b4ac34ebf0 | -3.97732 | -56.11761 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e6a4981c-4c3f-3067-9438-1f6dab0b6672 | -3.36593 | -50.47961 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b28d4c3e-ebf8-3660-9bea-8c53fe597d0e | -2.49634 | -56.12035 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 304e73a0-c402-3a25-899c-e71623cc3ec0 | -8.08413 | -55.29334 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7ed9b81-ad16-3aff-bb02-04876a66b023 | -3.51193 | -54.65296 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 717acae2-7b0e-365e-b01f-036def0119f5 | -2.79939 | -54.0789 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48ea75fc-6b5f-35f0-92b3-b32d377266e7 | -3.10245 | -54.98261 | 2026-10-08 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 150ba2c6-0f9c-33aa-b96c-916484193576 | -5.23845 | -48.40499 | 2026-10-08 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95c8a860-5f8d-3f22-8475-f0c17e0e2ec5 | -2.39657 | -57.89771 | 2026-10-08 04:46:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b46fb74c-2786-357a-91c1-0ffc2cf54e59 | -3.28453 | -54.04538 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d616ffb7-6069-319e-b83d-96b392e62a20 | -6.08413 | -53.49377 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5d59669f-875a-316b-ae66-b8f50596ab70 | -11.20949 | -44.86427 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc6a1d06-5bf2-35a5-a45c-5fff2f0bc6cd | -4.2943 | -49.09469 | 2026-10-08 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 21bebb5f-2a48-3e37-8f8d-bdeacba2e4e1 | -3.79105 | -59.37217 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84973ad0-5150-3133-883a-e6fe7603d0ac | -2.89703 | -56.67221 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fb9074f-2878-3c10-99eb-24000dd16ef9 | -3.01736 | -54.05208 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4239fb35-94e3-360e-82dd-b60c86ea88a8 | -4.51953 | -54.97977 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96b4ac5f-1ad1-39a9-8608-debdc2f129c2 | -3.29377 | -54.0116 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e9b37c9e-d0fe-30b1-ad1d-473898dc90a6 | -3.59447 | -54.67085 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d078e042-854d-35e6-a937-f2353621e0d8 | -7.2038 | -55.10329 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a5ee703-8ea9-321b-b8a7-a42383d01914 | -3.70501 | -50.6593 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61f74bba-2ced-375d-83ad-09084a8d9df0 | -9.83587 | -47.47361 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4df9d178-c0f3-3c92-96a0-85483719d137 | -2.88785 | -54.1823 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a806055-01b0-3d9f-93f6-b6d4cae2eefd | -3.08454 | -53.95931 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 0f77ff8f-fbf5-34cf-b13a-ec29476c03bd | -3.71968 | -54.23271 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ba0a44a-d6cc-3f38-9c6d-5588da6a72bf | -3.74259 | -59.47085 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f90033df-d7aa-39f9-8e27-b24420efc545 | -10.77379 | -46.58133 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7eb06ac5-a6df-3b0a-b836-dd8d9b7e1211 | -3.54704 | -59.47821 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8710f262-aecd-3fb0-9619-1a0afbd4724c | -3.54793 | -50.09701 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8da3c5b8-ed06-3cb7-a7d0-7f0de5449187 | -6.00467 | -52.7608 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93c310c3-a4bf-31c1-8cf0-c3d775dadc34 | -2.78919 | -54.09533 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d622ede4-3a30-3056-b7fd-e1398296c14c | -2.78249 | -54.08978 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1fc2a00f-50c8-3832-9934-97e45913f508 | -3.31068 | -53.86151 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dc0e3fc3-e7ba-3469-a9fd-18f6eb557fb9 | -3.28731 | -54.02962 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 186d5156-2bb8-3170-9b25-d663f9d4344e | -2.7816 | -54.07162 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c2bce044-d5b7-3cce-b6bd-83a53b022fae | -3.84177 | -55.97756 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68063539-b0b5-3211-a029-71d0eb64f13e | -8.98349 | -45.9436 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b990c195-d911-3920-9c02-08c226856e34 | -3.55386 | -59.4695 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34ec87e8-1d5b-372d-9a7d-cf631f3d6bcf | -2.99387 | -54.05733 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c999f70d-48e9-364b-82f5-6709cd5be7f9 | -2.76715 | -54.11452 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0914e94c-ee64-3d8e-9a08-78adff835a96 | -5.23546 | -56.11626 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44c7c1b1-1aed-3194-a05f-b336a0bed553 | -4.85725 | -42.82889 | 2026-10-08 04:46:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce552405-18f4-39b5-b41b-81c4e215c252 | -3.08613 | -54.25502 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae69afd7-ec3a-339a-89e9-cafaec12044e | -9.14233 | -45.82563 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcdd16cc-faa0-3515-b809-e666867995e6 | -2.84501 | -57.47972 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60c28147-87be-3165-a142-9509042d43c8 | -2.89177 | -59.2039 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b012ce0f-b472-3dea-8dda-52fc810cbb52 | -3.2793 | -54.03277 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 170bf294-4390-3cc5-9cf8-42cc5cac3e84 | -3.27129 | -54.03592 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8658975a-cd78-3500-9123-567f2a2ebab1 | -8.09148 | -55.31738 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97354b52-772c-34fe-8c85-3ac798273dd8 | -2.9347 | -53.93461 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 205456f9-6268-3fcf-b1ce-2a0b3c314882 | -2.64589 | -56.54486 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9cdcb71-5582-325f-8b0e-f809e06ba5ab | -5.69667 | -53.49609 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d430fc47-90d3-3101-9212-301ce3173943 | -3.73898 | -51.20737 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59a07229-8866-33b9-b6ad-8068a3ac1ab3 | -7.66405 | -44.95152 | 2026-10-08 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd877cd2-8205-3f61-8d9d-8a4202e5dca3 | -3.05553 | -53.92973 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24260efb-4c5e-337e-8bf6-6b86632144da | -3.12293 | -53.7912 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 7b046298-f58c-389f-ad18-5991a64f9464 | -3.48239 | -50.08338 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f03f81e-4beb-3bf7-a4a0-b043f811f0c7 | -4.44635 | -54.97324 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cd82946-ebe8-388e-9ffa-563c82d7d71f | -4.11613 | -59.88081 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 341e174d-1bc2-3b11-ac0d-544a6145318e | -3.96847 | -56.11996 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c352cfd-2183-375a-9956-6eab9af8282a | -8.20482 | -54.70467 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a8ea7c6-86cc-33d3-aed4-4eab16f3aa6f | -3.85662 | -52.03654 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3dbfc75-6ff9-3d14-aa8e-b2d6186e7253 | -3.84753 | -55.91484 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7387b13-13f9-3da7-83ad-bf3e687ba338 | -5.73357 | -45.15424 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f9bf4500-90a0-3adc-ae70-3f01846b9f9b | -3.25428 | -54.66118 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f5303b2-823c-3889-a749-654b65d9b4f4 | -2.50426 | -56.17822 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 77f54490-d5b8-3596-9b97-ff29e89998f6 | -6.02236 | -53.54659 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9326c7a5-685a-33f4-8b54-0a9d22623c1e | -8.21516 | -46.33602 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad8059cf-38e8-30ba-ac88-e8212c4ee593 | -4.12259 | -59.87492 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8840d8d4-7db2-31cf-9103-15f203d24ded | -4.06846 | -59.8485 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README87.md)
