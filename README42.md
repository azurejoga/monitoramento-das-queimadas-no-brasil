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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae9bc500-ce1e-392f-bbd7-3fec0e7c913a | -4.40736 | -48.94465 | 2025-08-22 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 628f9b0b-fe5f-3b78-868f-024fe91b1456 | -6.0418 | -44.36712 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef03f3a3-3a6a-3809-b3f4-913f73ceaaa2 | -5.8762 | -53.63445 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62179615-ef75-3fa4-ba05-1c5c047dc3ea | -5.79628 | -59.21638 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ee0827b-beae-39c9-91ee-428267841248 | -5.4379 | -60.16645 | 2025-08-22 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3541327f-e36e-3a13-a7de-c534d182ed8d | -5.8806 | -53.63055 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e17ca8c-f1d6-3e39-896a-e7d94a52035b | -7.85724 | -46.9902 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cd3687c5-2344-3228-ba4e-598f87f2a017 | -6.42825 | -44.68282 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1c7a98a-c2ea-3be6-aea4-e9059d029411 | -5.87736 | -57.75602 | 2025-08-22 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e836053-6d37-3f5f-a83c-a276f294849a | -3.83654 | -47.73622 | 2025-08-22 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0c778e0-fafe-3a22-9acf-0b2d4c21a2cf | -3.17271 | -49.48135 | 2025-08-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77b3d127-a2e3-3759-9526-d7f52b049f41 | -2.25669 | -47.84792 | 2025-08-22 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 596c6483-7ad9-32fb-b239-5b68aa641051 | -7.64994 | -45.24789 | 2025-08-22 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3906185a-dd09-392d-bd04-85f1a5c47d31 | -4.83451 | -55.76251 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94d9a65d-8912-3107-bf14-319ae3fa329a | -4.55424 | -55.96747 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36728d3c-b1b3-3624-aaf9-e9efaee13041 | -5.885 | -53.62669 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f967cbc-0b19-3b8a-9b57-a7b86a6a6315 | -7.02797 | -44.62945 | 2025-08-22 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f2851ad-9d0d-3a75-a22b-a69443e7e870 | -3.26749 | -46.91549 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6e33f4f-da0e-30c4-ad2c-9109cf45b9bd | -2.47313 | -47.77067 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 4566e1cd-fe3d-375f-8a10-cd9c42386a97 | -5.80533 | -59.22535 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33ca2a37-9d6d-3805-b3b7-8c00499cd237 | -2.45488 | -47.74813 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15f709d1-f390-387d-a545-e5d9e1220c0c | -7.85615 | -46.9987 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18e01245-3762-3759-af69-c5d775c38ed0 | -6.89745 | -52.86103 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f7a4a60-684e-3ff0-925e-ec415f1b9483 | -5.80251 | -59.2211 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 869a59f9-75b9-3381-a890-d9a7cf56f8cd | -2.26139 | -47.85202 | 2025-08-22 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 95b66ba4-0cc2-3947-9567-ba4a318f429a | -6.25153 | -53.6842 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0039c92e-c267-30a2-9aa1-b8b617f6ccdc | -5.38639 | -51.43116 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da2c342d-a1ea-39d3-942c-c63f4b4aeee0 | -6.43935 | -53.38753 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f501713f-af2f-3959-9a0c-0428c505df4d | -2.58803 | -51.92292 | 2025-08-22 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9e0e6f0b-23d2-3364-8824-d45f6f115779 | -3.23635 | -46.78993 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e16aab8-f304-39e4-b8c1-10b42d67be39 | -5.8065 | -59.21796 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a79c262d-1509-3cf1-bc8f-2b7e6d7d29f2 | -6.63713 | -47.90495 | 2025-08-22 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 68180eec-18c7-3c98-93b9-975d66a7ecd7 | -7.64335 | -45.24666 | 2025-08-22 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 52e30007-19e5-3e28-bc7b-6395d829295a | -7.84645 | -46.97946 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8677caa5-becc-3045-be60-6cc22c83eff0 | -4.32555 | -55.13075 | 2025-08-22 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3878ac10-9ece-3292-a055-b3e09c915b4d | -6.74421 | -50.95869 | 2025-08-22 05:10:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80995e44-0e09-3a89-b704-51ddca8b0c4c | -4.88789 | -55.98629 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46fe5f7c-33fd-3c5b-8801-a8fb0b49e59d | -6.94579 | -44.55545 | 2025-08-22 05:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea7c74ff-a3eb-322e-bec8-4411f1cc7110 | -4.77462 | -45.32129 | 2025-08-22 05:10:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f39bee21-9462-39a1-88ec-2e5700dc9ade | -4.40106 | -44.08673 | 2025-08-22 05:10:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 267f1955-91a1-39d3-a75e-453759d8e8c7 | -5.89111 | -53.63681 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a82b750-1736-37cb-9bf0-94d25c46b8fe | -6.89668 | -52.86617 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2146251f-9622-3411-b8a6-e9a9ad9adc07 | -5.52686 | -46.42255 | 2025-08-22 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64b1294f-4c8f-3139-82ce-e87d2279398c | -5.22177 | -60.28695 | 2025-08-22 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ccd6e3f-3c60-3279-80a5-da2a50e6d7d1 | -4.10181 | -54.41227 | 2025-08-22 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a7c8c87-bd85-348b-8e08-42cdd5cf5978 | -7.62125 | -46.24617 | 2025-08-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92946ff7-ab02-3dd4-afd7-b734be52d8ac | -5.88012 | -57.75999 | 2025-08-22 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc5fe1b4-7762-355f-8b93-af94420ecc1d | -2.83522 | -54.56052 | 2025-08-22 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e136385-fbc5-3fa5-a467-c4c3d4146ee5 | -3.59517 | -49.4441 | 2025-08-22 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2e62fba-0d27-32d5-a238-9e36ab07d080 | -4.09735 | -60.66661 | 2025-08-22 05:10:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 226821c2-98a9-38fe-ad95-1f2861a8301a | -2.69239 | -48.20926 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9975626a-a4ad-3798-ae7c-a0c5b32c4e76 | -3.2375 | -46.7822 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba4c6e43-be43-3121-8e2d-fe3fdd184a8c | -2.93628 | -53.69627 | 2025-08-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0f7af7f-10d7-307e-a9fe-fdb685d79bdd | -6.16598 | -53.7718 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58661a5d-1e2f-368c-a000-b7e77de43680 | -0.48901 | -50.36116 | 2025-08-22 05:10:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3da6753-4e4a-3fc0-9a90-c0a9c697f307 | -2.6933 | -48.20317 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2bb5149-dcf5-3f6e-9d4f-b386d7b7cec0 | -4.89124 | -55.98681 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 677d91f3-ccb4-320e-b982-69c813157d0c | -5.88067 | -57.75653 | 2025-08-22 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3d089f9-9f09-3250-bb04-ad7b838f41d4 | -2.94041 | -49.46321 | 2025-08-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d97ce97c-d1db-385d-93a2-77076b0ee02d | -5.13455 | -56.98158 | 2025-08-22 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7072a83-bd7d-3bea-bd0f-02267974674a | -7.59763 | -49.57793 | 2025-08-22 05:10:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b24e4bb3-b7bd-3bcd-932e-491bf9cf7b24 | -7.63744 | -45.24024 | 2025-08-22 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a6cca06a-c53c-3ac6-adde-edd2056e2f2b | -3.26694 | -46.91932 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 716c704f-e58e-31e3-8025-bec671473f26 | -5.88805 | -53.63176 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59625392-fabd-3085-8106-75afde86c890 | -5.8826 | -53.61713 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd5d2f01-56a8-3365-a604-52764df9d52d | -2.47268 | -47.7738 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7abd2309-fdd7-336b-a192-1e45c97b215a | -7.86863 | -46.99623 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61894a72-1962-3e1d-9360-c8fb27ddeb89 | -2.91987 | -48.30117 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f6f6248-4796-3225-b5ca-9b4b453d09cf | -5.3869 | -51.43314 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcd369da-f860-37a8-bbad-2117c60ccf12 | -0.75308 | -47.75492 | 2025-08-22 05:10:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 022f42dd-2332-3967-8e6f-a929b892d076 | -3.84474 | -52.29246 | 2025-08-22 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5853df44-80a5-3422-83b3-7f4bf9862dac | -6.44767 | -53.38393 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e4151c4-c3cf-3ee1-9586-330627d8c1b5 | -4.37017 | -54.88457 | 2025-08-22 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf7f664f-ebf4-3850-8b75-e261d6bfc3d0 | -3.38743 | -47.6095 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b38f2140-018b-3d2d-a840-f068b9b0da95 | -2.91388 | -48.30638 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5735c8f0-955f-3440-804f-086909385447 | -5.88739 | -53.63617 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4833925-dfe1-33bc-8190-0721f01abd1d | -0.75356 | -47.75187 | 2025-08-22 05:10:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e761429-7b8f-3051-8979-a3659f5c6899 | -6.44004 | -53.38279 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d747194d-5609-34ea-bd45-8185d733c0a8 | -7.8567 | -46.99443 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e41a24b5-1f45-3573-9770-406b2308fc75 | -4.09365 | -60.66603 | 2025-08-22 05:10:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d58ebb9-df72-3fa9-ab16-f61a77e88c23 | -6.45149 | -53.38451 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 560d11ca-1498-3593-9cd8-59fed4466941 | -7.65068 | -45.24231 | 2025-08-22 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6593bbc3-7b12-3b88-bd11-522f95cdb3a7 | -5.44307 | -60.17966 | 2025-08-22 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceae8e1d-689f-3961-bd55-3fc7c8d31630 | -5.21936 | -60.28752 | 2025-08-22 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abcfdebc-8085-39e3-8d3c-24729085f9f1 | -5.23696 | -56.06164 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70a67d5b-5bae-36e3-94b3-74a20fa79989 | -5.79156 | -45.07623 | 2025-08-22 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 44f73df4-1ec9-305b-b26f-b44ffc4b9fe8 | -4.24846 | -54.92416 | 2025-08-22 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54680a0b-850c-3f9c-a0e0-8b4bf4b4e206 | -6.45218 | -53.3798 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9ba4efe-4b3c-3dfe-91a1-a2f3d750a2f2 | -7.62716 | -46.26168 | 2025-08-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 897c6d79-2679-342c-ad43-6cb19d66be56 | -2.93269 | -53.69573 | 2025-08-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2bf3fba-9b95-3d95-836f-656e6b11f344 | -5.03279 | -56.12418 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e4c0605-2618-3324-923a-35110256809c | -5.52089 | -46.42149 | 2025-08-22 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaebac97-f408-3510-a9cb-fdf5c2daa9bd | -6.26746 | -53.68889 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 611ef46d-648c-31dc-9b0d-314f4b8a403c | -4.6046 | -55.75324 | 2025-08-22 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72a87a88-d53d-3473-b57d-56cbdde67ede | -5.88633 | -53.61774 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 027260f2-bfa1-397b-a504-92253a479918 | -4.32612 | -55.12705 | 2025-08-22 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1b95609-0ace-3917-b75a-2ec57614d3a9 | -6.45079 | -53.38923 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e543916-31b0-3a16-9ebf-17285c531b1a | -2.97014 | -49.29754 | 2025-08-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 331c155e-6ff3-313c-8831-51d0adef103e | -4.60796 | -55.75375 | 2025-08-22 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c18828d8-82bc-32e4-afc9-d50c8f28c9b4 | -6.54714 | -45.52489 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README43.md)
