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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53b02220-534c-3323-9360-4ab41334e5df | -2.28815 | -47.85055 | 2024-10-19 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3c309fea-8267-3083-8c81-0aadbf846c8f | -2.28754 | -47.85443 | 2024-10-19 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b4fbc8a-e092-3266-924d-2b15cbc74600 | -2.28545 | -47.85354 | 2024-10-19 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00dbaa2f-9e4d-3399-8b9f-ea31b1ea4423 | -2.25747 | -47.66054 | 2024-10-19 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed5f81a1-7c14-3dfe-bf60-7e166803bacf | -2.25339 | -47.66382 | 2024-10-19 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c3a4059-4eeb-3984-90da-c3ce2b00e40a | -2.32972 | -48.83247 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c683cbd-bf5c-3d58-9633-5b4dd4461a28 | -2.31479 | -48.80813 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f5f641a-957c-3b64-a842-fe92c87d4759 | -2.26668 | -48.82708 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bc7fce4-d6f4-3506-a30c-87ae1bb057b4 | -2.26301 | -48.8265 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 221e816c-0dba-33a8-bf01-02615bbb0044 | -2.26005 | -48.82159 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3acce3e0-61aa-32a2-86ad-798a655365ba | -2.25934 | -48.82593 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9fbf05a-7e10-31e7-8636-1d8097740270 | -2.25638 | -48.82103 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd02aa8e-99a6-3926-9e1f-3fe3f757e949 | -2.25568 | -48.82536 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e857ace-04cf-3fb5-8ce5-6238cfa2a258 | -2.25201 | -48.82478 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71365c3a-ab28-382b-bd2e-27d639f5a95b | -2.18363 | -48.73655 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4cf34b3-1657-301c-939c-1b87ac185697 | -2.16525 | -48.42527 | 2024-10-19 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c58e2630-e4cc-38eb-b5b9-9400a6dc647d | -2.15816 | -48.82497 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 593a3d4e-6a89-3c0e-91b2-4f82b66bc464 | -2.1235 | -48.73731 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 449b518d-5462-32b9-9c8f-933d05acdaab | -3.46393 | -47.67125 | 2024-10-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 737d06cb-76c2-3ca9-b4ab-e5f55bda6288 | -3.4605 | -47.67073 | 2024-10-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3a3a0b22-a65d-3032-9a46-d3a7ec7b6879 | -3.4599 | -47.6745 | 2024-10-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5863313-f964-37cf-85e0-6ee780c61ada | -2.87134 | -48.24847 | 2024-10-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2bfe60c-02f0-31e1-9c7b-df16353a0d8b | -2.80114 | -48.67184 | 2024-10-19 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3596705c-9143-36ac-ac3d-763b4262c8f1 | -2.79099 | -48.57239 | 2024-10-19 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb973c9e-9a17-3528-b36a-5eeb4befbfce | -2.71987 | -48.83207 | 2024-10-19 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 630450f7-ab35-3fbc-b554-89245c7b28e2 | -2.71919 | -48.83632 | 2024-10-19 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b35bea2e-d76c-38dd-b30d-9120ae18aced | -2.57547 | -48.39735 | 2024-10-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b101b2a-63c2-3a51-b5fd-9d3d89105b43 | -2.5719 | -48.3968 | 2024-10-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 031df5ae-0a09-3ce5-81b5-6b806a1d303d | -2.50209 | -48.31206 | 2024-10-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ccff7063-0937-320f-91c1-132e4bf2d7ba | -2.44917 | -48.43734 | 2024-10-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c530fae-c7e5-3329-869a-7caf4a04c1c2 | -2.44559 | -48.43678 | 2024-10-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1796d1ff-f271-3cf5-ad62-173a8a83ee63 | -2.44553 | -48.48307 | 2024-10-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d6f71a1-a34f-39cb-9332-ae4dfaf53446 | -2.44487 | -48.48719 | 2024-10-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6448f3b-8c2a-361b-8a23-de01983a882b | -2.42224 | -48.62852 | 2024-10-19 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b7503f8-5f2d-300b-b0cb-ad3e00a42e7c | -2.41574 | -48.88044 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16aab8b9-5568-31fb-b1ca-8f929d6de1f5 | -2.41503 | -48.5122 | 2024-10-19 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4071afab-6e5f-318a-b0a3-dc07a4d42ccf | -3.48593 | -48.23965 | 2024-10-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e59db7fe-a80c-3972-96e8-0f18c41b4a74 | -3.4853 | -48.24359 | 2024-10-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 51a2fe08-f74e-36cb-a345-bd1815bf7918 | -3.46334 | -47.675 | 2024-10-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a2e1e5c9-077c-3d71-aeab-e20e77fd9ff0 | -4.95481 | -49.14495 | 2024-10-19 04:25:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc478345-6612-3464-b580-107e15cfbe9c | -4.79805 | -48.2265 | 2024-10-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 584d544f-4849-33c5-8bfc-79fca52eed0b | -4.79078 | -48.74645 | 2024-10-19 04:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62d70f72-ea65-3564-a545-21a9a131da28 | -4.6854 | -47.87596 | 2024-10-19 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7874a792-7a2d-3786-9afd-933011624629 | -4.57095 | -48.01939 | 2024-10-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2217f958-1462-3983-91bf-05413fe46bca | -4.56755 | -49.22042 | 2024-10-19 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e68fb8f-9c5f-3252-a802-1a48434b4094 | -4.52665 | -48.83545 | 2024-10-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20520b64-acd9-34a2-8dda-ea3a65c62dba | -3.90707 | -47.95186 | 2024-10-19 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9da365d-c39e-330a-866c-07fece9a2bb8 | -3.90645 | -47.95568 | 2024-10-19 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9226dbeb-4ce9-39cc-be2c-61a184d23562 | -3.77301 | -47.73806 | 2024-10-19 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f38fa8fe-97c0-3a57-b262-0e1721dd4efa | -4.56682 | -49.22099 | 2024-10-19 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 59f6f8fd-dfee-35db-8cf5-a9d13964e93d | -4.50619 | -48.80299 | 2024-10-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 670417fb-3f0e-3a0e-92af-75393c2dac6d | -4.36549 | -48.48198 | 2024-10-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5076960-3066-3f5d-a018-d2a2cd78b909 | -4.36496 | -48.48202 | 2024-10-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 502addd1-716f-3b34-b1f5-332b932b96ba | -4.35062 | -48.72944 | 2024-10-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9764c8f-db72-3694-8257-b426d6569122 | -4.26726 | -48.00766 | 2024-10-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be4dd0ea-419e-37af-96b3-3cc6698a1b78 | -4.03447 | -48.93917 | 2024-10-19 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 328a6720-e87f-3c9e-a6e9-e0e761d27756 | -3.58775 | -48.94124 | 2024-10-19 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a3fbc4f7-698c-380b-b5ab-fbff75e32b92 | -3.58707 | -48.94545 | 2024-10-19 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9450e49c-96fb-33b4-9f3a-adddace75ca6 | -3.58412 | -48.94067 | 2024-10-19 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 04903605-85ab-3a75-a6f1-6a2982823dce | -6.01371 | -48.18061 | 2024-10-19 04:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| add8e1b2-b33d-3590-9f07-687e413c7ef1 | -5.28927 | -48.31435 | 2024-10-19 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eed57f23-fe17-3997-baa7-0b82b46a9d2f | -5.28864 | -48.31818 | 2024-10-19 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c0cca10-ce9c-323b-b004-da150a5b717a | -1.9167 | -49.52625 | 2024-10-19 04:25:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f04afd43-13a3-397d-bac1-7180e864e0df | -1.91461 | -49.52341 | 2024-10-19 04:25:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f74776b9-3515-3cc8-b0a2-5126f9a4360b | -1.5639 | -48.71817 | 2024-10-19 04:25:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3df79a27-cb93-3cc4-9bc0-4dced04c010d | -1.56022 | -48.7176 | 2024-10-19 04:25:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f55a465-aa47-3012-b693-7a377e8e6b48 | -1.13632 | -49.04354 | 2024-10-19 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5f08d4d-0e4d-3e7c-9873-a76594b08dd0 | -1.13559 | -49.0481 | 2024-10-19 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef507219-d453-3154-96b1-2cbf990033fd | -1.13329 | -49.03839 | 2024-10-19 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6adc8218-db58-3dfa-9e0f-95dcdf54080c | -1.13255 | -49.04295 | 2024-10-19 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba970fa9-2a4a-3759-97cf-5b6ef770c462 | -1.13182 | -49.04752 | 2024-10-19 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abe75e49-4cd8-3783-9091-4eb1445e35dc | -1.12878 | -49.04237 | 2024-10-19 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aeedec6c-016c-3d7f-8b2f-89f9e97a2b39 | -1.12575 | -49.03723 | 2024-10-19 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30a2a080-85ec-3808-9f70-9c003b4d8956 | -1.12547 | -49.03465 | 2024-10-19 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| deaed5b7-e42d-3e33-b0b7-e2b9f202789c | -1.12476 | -49.03922 | 2024-10-19 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1effcdf7-796b-32c6-8afb-15413760458e | -2.19733 | -49.12848 | 2024-10-19 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fb50420-4a01-3b3d-9136-366344d31f78 | -2.19663 | -49.13298 | 2024-10-19 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef8e2809-0ff6-3324-bf97-0e638d4005c6 | -2.19475 | -49.13073 | 2024-10-19 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d25716f-5dbf-368f-ae8a-92f6baf8a30c | -3.27998 | -50.17793 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2c866bdd-f092-3139-98a6-b9674205ac98 | -3.27533 | -49.08859 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f00c864e-3339-371f-8b2e-1c9d6f85eb70 | -3.27234 | -49.08369 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae643b0f-c0a8-3a98-8d8a-afc0b08516be | -3.27156 | -50.13076 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0eb64d23-ef79-36ba-ba9f-e3eff792081f | -3.26798 | -49.08741 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f678afd7-4d87-3d31-95ac-2152d4c18d55 | -3.26765 | -50.13015 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97660e1c-7a22-36cf-8eb1-132e9b46b3f9 | -3.26431 | -49.08683 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 511396d6-7293-377a-ac10-ac7cb1464c96 | -3.22901 | -50.3676 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a57c4f9c-4990-33b5-a1f2-4ad2e90b507a | -3.22219 | -50.3595 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c5b41b4e-46ef-30cb-b8cf-d5fa240e81d8 | -3.21892 | -50.35459 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a144e0cd-1093-3077-b805-9cef60277eec | -3.21821 | -50.35889 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3872c21e-79ea-3ba5-8682-38fe9f16c3cc | -3.19444 | -50.312 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd0f388e-0381-355d-bf8a-ef7596a778bb | -3.19308 | -50.31398 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0e8f116-70c9-3e68-b600-94699c95c568 | -3.18027 | -49.76399 | 2024-10-19 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02f98d6e-4f48-38a4-959d-45b56cd1e25b | -3.17709 | -50.29355 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6630540e-73d7-3a4b-8f8b-5027dfa66916 | -3.10032 | -50.19348 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a02a1ff-223e-3237-a882-16b52b1420b4 | -3.10014 | -50.19567 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5b3faf2-b015-3db6-b1cf-70300ad39e36 | -3.09833 | -49.47227 | 2024-10-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1847472d-e357-3b8f-9a89-4fb00c23c366 | -3.0726 | -50.36953 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 245d51d7-0c64-30b7-adbd-adb574274cf2 | -3.06978 | -50.50158 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7fcda32-ffb0-37e1-ad97-35657ef266f6 | -3.0697 | -50.36206 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2746b290-3612-3434-b9db-256a0c26277a | -3.06916 | -50.36549 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README19.md)
