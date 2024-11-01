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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ac9b4b8-50c8-3582-87ee-b7bbf81f2291 | -3.17123 | -50.58439 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc81353d-4a97-37b3-937a-d158a73f34ee | -3.17054 | -50.58867 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a808e948-822d-3bf0-9ec9-cf1196eeafd1 | -3.16758 | -50.58381 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38845fdf-89a4-3041-848a-035582abcfaa | -3.16688 | -50.58809 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ca0c705-c9fc-325a-a1ad-35d6753c25eb | -3.12194 | -50.42577 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4b142fe-1bb5-3f94-8baf-a0fce3c20c3a | -3.03079 | -49.6157 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04cfdfa6-9335-3d6f-a21d-6c2e2fad6248 | -3.02393 | -50.42871 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e1f5fcc-71be-3074-9f93-8aa506c21de3 | -3.02325 | -50.43296 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c815d10-dd3c-36c2-9847-e09b33898491 | -3.01208 | -49.62066 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0207d93-8d55-36d9-9493-e513481a6b74 | -2.98733 | -50.47065 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0a9d931-b086-3896-8033-ae9713dad949 | -2.97253 | -49.10123 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5b20862-4d08-336b-850f-ca7354961326 | -2.48848 | -49.81282 | 2024-11-01 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a044dc10-8e5a-3f8f-a28a-e0da510b78c4 | -2.46712 | -49.76447 | 2024-11-01 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f3ba3c7-6cf3-33ca-90ff-417a81a582f9 | -2.46648 | -49.76845 | 2024-11-01 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 359eabe2-0dd8-3621-bddf-f614865b65e1 | -2.4413 | -49.6548 | 2024-11-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f6b1012-e4cb-399a-98ed-75723b9117bb | -2.44086 | -49.6557 | 2024-11-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85ca7d8b-fcf7-3897-b5ab-e5eef9aa551b | -2.41356 | -50.42874 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c795fcbb-2f73-3e83-b7b4-32bc0bdc1aad | -2.41057 | -50.42388 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1a08c45-4a2c-32ab-b3ba-8ced65624c21 | -2.40989 | -50.42816 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a27e9537-57f9-32d8-b7f2-73b7d6fcaa4e | -2.40758 | -50.41903 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2879aa34-3129-3b05-8b4c-a1e0e05f39e7 | -2.40536 | -49.81307 | 2024-11-01 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14734488-0305-30bc-8221-b8657ac457ae | -2.38669 | -49.72421 | 2024-11-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8de2d3f-5504-31e2-bd4f-fd3ca89edab0 | -2.38316 | -49.72365 | 2024-11-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64570551-4ad9-31c7-b5dc-a20b452a6805 | -2.36272 | -50.32447 | 2024-11-01 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7494a70b-f85d-3752-be03-d21c31bdd405 | -2.36254 | -49.55877 | 2024-11-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c556c23b-13fd-34e7-911b-aef7048b3be5 | -2.21846 | -49.57362 | 2024-11-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcf78c32-91a2-3780-89cf-b165e4e3d904 | -2.21495 | -49.57307 | 2024-11-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 388823ac-6828-3f52-b545-036caef0a78b | -2.21019 | -49.58038 | 2024-11-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 922ac04a-160c-33f8-96e1-f3153fb30c86 | -3.05236 | -49.48081 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b30391e3-3944-3734-9246-72b927cc19ca | -3.05175 | -49.48463 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fb978762-41ad-34d4-b654-18003560983f | -3.05114 | -49.48845 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 09c8915b-b2b7-3637-9262-692476dc2588 | -3.05011 | -49.47262 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2843ece2-e59e-3519-872a-7466d45c091a | -3.0495 | -49.47642 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5bd0a831-d348-39c3-83e5-b99d6ecb2844 | -3.04889 | -49.48024 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 601d5b56-4a80-3368-90c6-c139898c0ffd | -3.04827 | -49.48407 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 877a25fe-12de-3d9a-9520-6e4a22311b8d | -3.04766 | -49.4879 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9f187b77-b4b7-3e8b-8e83-cf641e7beb73 | -3.04664 | -49.47205 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7beea1a1-cedc-36af-b9f8-b8549b963f12 | -3.04603 | -49.47586 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2d019b85-2d5f-3f48-b182-f89d835b7dde | -3.04541 | -49.47968 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8a1460d3-bb3a-3f9b-8516-1b82c2dd3250 | -3.0448 | -49.48351 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4150327d-5ede-33d0-905b-5398cbce72fe | -3.04419 | -49.48734 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 847a6e57-72e6-306e-bc0b-04f38b92a064 | -3.04358 | -49.49117 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 18859fa8-8379-3712-97f3-d7a2f44013a1 | -3.04316 | -49.4715 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1aaf2f05-3fd5-3630-a307-34c1fa32483c | -3.04255 | -49.47532 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b9299d36-ac27-30f1-9782-06f2716cd49f | -3.04194 | -49.47914 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1d069a65-1e89-3839-a493-550df134de88 | -3.04133 | -49.48296 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 500ef6cd-fd6e-3d51-a298-d343d81bad41 | -3.04071 | -49.4868 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0cfb89d2-669b-3348-b14a-0ed9c4950d32 | -3.0401 | -49.49062 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f916a08d-fd12-3c28-903d-1964fc8f743b | -3.03908 | -49.47477 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d6a644c6-2be5-31d1-a264-750ba9a9f376 | -3.03847 | -49.47858 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e106b94a-3e4b-31d5-ba81-b7f5d8c7370c | -3.03785 | -49.48241 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3518bc50-cfbf-3152-bd4e-b7c33c298341 | -3.03724 | -49.48625 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 04af39b6-1e35-335c-a6c5-8e91c24f365d | -3.0356 | -49.47422 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2953391d-3190-3cc5-b5af-6667f951f450 | -3.03499 | -49.47804 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce1ba649-535b-3beb-bfdc-966de2494c41 | -3.03438 | -49.48187 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecbdb705-23b7-371d-9a14-64fcffa33885 | -2.97452 | -49.55566 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 768bb6b4-4ea6-3ebd-bd04-8df428f48fa1 | -2.95684 | -49.50938 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c59cc24-13cd-3f13-b801-7f9c5b94e002 | -2.95397 | -49.505 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e24e8f3e-341d-30ba-9b78-aa8d7e9783ac | -2.95336 | -49.50883 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d0fe3d6-b64a-327f-a948-e9f915864bf2 | -2.90114 | -49.5006 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 747d7e8f-ca77-3b8d-aeb3-3e0def5ab045 | -2.89954 | -49.50112 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 313d611d-d7d3-3bf1-a415-257231bbc7ed | -2.89766 | -49.50005 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcc093b2-43c9-38b1-b009-71c879e8edea | -2.89704 | -49.50389 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fe467ff-681f-3a0f-ba20-209e553820cc | -2.89691 | -49.35952 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6da948aa-2f5a-355f-be4d-3ce1d946f6b0 | -2.8963 | -49.36333 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df78244b-6d72-3722-956c-707645bbd435 | -2.89606 | -49.50057 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d87e0021-0ca5-3bec-89ae-b0c87eeccaf8 | -2.8895 | -49.24973 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48c30e53-1972-3852-81db-d50d4722f717 | -2.88665 | -49.24542 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa927104-9571-3a52-8de2-569817054234 | -2.88168 | -49.12175 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7da594b9-db37-3ae1-9ec3-36e5add9576d | -2.88036 | -49.24055 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a02076cb-5c31-3759-9877-65650c5f9c45 | -2.87691 | -49.24001 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ac89dfa-2132-3e87-8308-738d67051f87 | -2.87346 | -49.23946 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e360c7a-82e8-370d-8775-f58a90a4370a | -2.87062 | -49.23516 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1f10ae1-646d-3aef-9502-64977a1beb76 | -2.87002 | -49.23892 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 255e6884-4b9b-30a1-a118-a7eb38b957aa | -2.86717 | -49.23461 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaca44f4-265b-38c5-9985-623a16c66bb5 | -2.86373 | -49.23407 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9c4483c-24a8-326c-b113-374f15f59ea2 | -2.86028 | -49.23353 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb5653e6-d15f-3b2f-aac6-281049cd6e58 | -2.85968 | -49.2373 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82be49b2-e89d-3769-9a9d-d8a6c9bb7eb9 | -2.85563 | -49.24054 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20632f66-56cb-3353-9091-1bbe128daf75 | -2.84045 | -49.26904 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5b58051-9e02-3d1d-8f15-69341e99c44a | -2.837 | -49.26849 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4caaa49-6096-3ded-b486-342f5eeaba2e | -2.83646 | -49.03097 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee4e1cf5-fa95-3b4f-aa6a-8a34e02dd9c5 | -2.83355 | -49.26795 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 073185ef-6164-39c1-9b61-d5c576f17f8c | -2.82649 | -49.22846 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 666d433a-3753-37be-a15a-0f7b9209c7b7 | -2.82628 | -49.27484 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8a6b719-a4b6-32ab-9ace-29a3bb3ba94a | -2.82542 | -49.27442 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c76ec34-a671-350c-9cf2-b17276e77fad | -2.82304 | -49.22791 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 449fd55e-39bf-3af8-a2db-63564da9d8f3 | -2.82283 | -49.27429 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0000accb-e1d9-37cf-af94-8c22beeddb5b | -2.8196 | -49.22737 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 551b73c4-d316-3ce8-bc10-7d1ee7c0469d | -2.81938 | -49.27375 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a06dc88-3161-3054-83f1-a2ebf5f811e5 | -2.80355 | -49.21713 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa00b9a8-abc1-3668-a0d2-ce15252d939a | -2.80296 | -49.22088 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92d00b68-05d9-3ec4-ba26-4708b2a37011 | -2.80236 | -49.22464 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34550a25-d078-345a-9e04-caa74e979c06 | -2.80177 | -49.22841 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a40ae70-2385-3680-90ca-4f7449a62534 | -2.80011 | -49.21658 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7e88563e-07d4-30c0-9840-53e8496d0699 | -2.79951 | -49.22034 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b33d7bc0-3352-3717-adff-de3971ffab6d | -2.79892 | -49.2241 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1ae26f35-7533-3630-b9db-46c12b4dbf83 | -2.79666 | -49.21603 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c365eb57-cdda-36db-a4d5-89f6b0234d88 | -2.79607 | -49.21979 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9843389a-5592-32e3-9fe8-c1285689a327 | -4.96816 | -49.78184 | 2024-11-01 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README38.md)
