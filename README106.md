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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e58c166-0300-3b2a-bd66-f88efb56b57e | -7.50938 | -44.28061 | 2025-10-02 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68955160-fa28-3b0f-bb06-185940897b54 | -2.2465 | -47.88805 | 2025-10-02 04:49:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e5c5cc0-b7e3-379f-88a8-6266d8f6f144 | -8.81314 | -46.68308 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 4f27f03c-6ca1-30db-abb5-ab5239b7470f | -6.77945 | -45.57565 | 2025-10-02 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5e0b3b8-67d5-3d24-8234-d812dc67e0f7 | -2.33639 | -52.80259 | 2025-10-02 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 417b3af5-d0ba-3dc8-adeb-cf05e1e73ff1 | -5.63488 | -45.96207 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53e76083-4251-3cdf-beb2-c9bd063584b2 | -3.81328 | -47.58702 | 2025-10-02 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 651bb9e9-b820-3e70-aa31-8c4529238afd | -6.38319 | -43.8658 | 2025-10-02 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59540142-7aad-3e34-8219-f457f0f17391 | -7.05346 | -43.27809 | 2025-10-02 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b1c95a6e-1f2c-324a-958b-424e3dd59e2c | -3.49632 | -50.26707 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 334196d9-9943-3616-aec7-2a7e154ae493 | -6.5994 | -50.03537 | 2025-10-02 04:49:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20552612-638e-36e9-a213-d2e111d0df57 | -4.00732 | -43.27458 | 2025-10-02 04:49:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de3856b9-4620-3d3f-ac4e-ecff8fe241ec | -5.89275 | -43.20486 | 2025-10-02 04:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d4552354-9d63-3b17-9c0a-f30d7e5f474b | -8.80812 | -46.68685 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 333f8969-5bcf-3dd1-812b-2cafc97dbe10 | -3.46431 | -50.08706 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16df4c3a-4ae9-3926-9467-a3a6390c6553 | -7.77951 | -42.52401 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ab27a564-b7c0-3b5d-80b4-a560b677854f | -7.17017 | -41.69789 | 2025-10-02 04:49:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fe01016c-e189-39cc-bef4-1e132a4765eb | -8.87203 | -46.58564 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f43783f-ad22-33d8-97cf-bdc09cfce7b8 | -3.56561 | -51.12934 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 84ba7b1c-3eaa-381b-8689-31e5294c1340 | -3.4886 | -48.95609 | 2025-10-02 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae7d9661-38f8-3ac5-ae2e-b20aba74171d | -3.69455 | -49.57111 | 2025-10-02 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6680949c-ebde-358d-b9f4-a04b0e620ad8 | -3.69861 | -49.56781 | 2025-10-02 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4542732-ea77-3154-ae5a-d8427e316a9e | -4.11274 | -47.93453 | 2025-10-02 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d71838cb-8b04-342b-b1f1-ca4bd6d99e86 | -8.71295 | -47.14779 | 2025-10-02 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b3328bd-7442-3a0f-a822-972345b7e1b1 | -6.3915 | -43.88174 | 2025-10-02 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b06f995-99bc-3fb2-8de2-6ce757c37165 | -3.45975 | -50.09388 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4613f26-81d0-31c5-8913-ebb26fc8aecf | -4.25202 | -48.5616 | 2025-10-02 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 253299f2-e00e-3166-a3e3-5af321215c34 | -8.89158 | -46.5998 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a0ede08-ce21-3dc8-b5b0-2e34da2ec758 | -6.68989 | -42.81933 | 2025-10-02 04:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7773f423-0626-3bf5-8feb-449121507a12 | -3.87315 | -42.52021 | 2025-10-02 04:49:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 69ace16f-d177-3a5a-aa51-32243950ad26 | -6.32667 | -43.04528 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b63e492-f7f5-3de8-a018-ea5b0c30fec6 | -9.33348 | -45.70536 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de1e8bdc-67c0-3bbe-a7df-accf413b2845 | -3.87754 | -52.31945 | 2025-10-02 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16b8ca28-8eb7-3105-ab27-d7d52c49c693 | -8.51309 | -47.80328 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce2d2184-3294-3d6b-8e80-9c363137ef79 | -9.33415 | -45.70055 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb67ae20-99a7-39bb-ac10-c1fde64539dc | -8.82112 | -44.80289 | 2025-10-02 04:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ef5ba2b-22da-3403-bf52-2caa4dce1f57 | -6.04769 | -42.43974 | 2025-10-02 04:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 21509df5-fe84-372d-b690-4049749a6bca | -5.6393 | -45.96269 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b49959f-9e3d-3e88-9c1d-01a13ddc9187 | -3.70009 | -49.41115 | 2025-10-02 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 048eec33-997f-3a60-88be-83ff10867c62 | -6.96362 | -45.33426 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1a06f6f6-4672-3ee5-bb6b-ed90e77eb57f | -3.82481 | -49.09855 | 2025-10-02 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f0120a80-d7fb-367f-9bb0-ac6fb5dc56fb | -6.78136 | -45.59565 | 2025-10-02 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b5ea5df0-3f83-35ca-8a3e-ff437c66b3e1 | -5.62428 | -43.24275 | 2025-10-02 04:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 56ff2b8f-25e0-3280-8415-238624cbce63 | -3.48811 | -50.09078 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4914d5c9-d097-3366-86fb-421a590137c4 | -7.5511 | -42.63795 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04cf4962-ca49-3376-8fdd-398fc4069deb | -5.48835 | -42.76648 | 2025-10-02 04:49:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dc8b211a-f670-34fe-a5fb-67111c3e1a69 | -6.82048 | -47.97716 | 2025-10-02 04:49:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03cee6fa-221d-3938-962c-1426704758da | -2.24279 | -47.88748 | 2025-10-02 04:49:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 124f60c3-af73-3a6f-8947-fee6451dfa4e | -3.82224 | -52.08806 | 2025-10-02 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7bbd180-91ad-3457-903b-341c793d27ff | -8.80752 | -46.69117 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19e3e329-4ad3-35df-ad85-72737c6a4888 | -6.67019 | -42.79768 | 2025-10-02 04:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d9d9698f-4628-3bb9-ac93-873cdc7acce5 | -7.77031 | -45.71227 | 2025-10-02 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36faf25e-1b2f-3d83-a5f8-62ea5c7ee3c0 | -8.87968 | -46.59545 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c472fdd-164f-3ff5-b841-ebc5fbfe3f78 | -7.77898 | -42.52797 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c71602c3-61c3-34bd-baed-6fe1db5a791f | -3.65248 | -51.22465 | 2025-10-02 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e96f28dc-47cb-3f6d-8c9f-a1f307ce4fe2 | -4.84664 | -45.22108 | 2025-10-02 04:49:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38dbd2d2-9e31-39e4-acdc-63c1df2f6f17 | -7.76581 | -42.53877 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2ef1d7ac-ccc9-36b4-acb0-93758580a51e | -5.78653 | -45.74848 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7b71d66-fdc5-3aa4-81c9-a5492df0331e | -4.3138 | -48.08708 | 2025-10-02 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3f2194b-5e72-3268-83fc-d84588e08b5d | -8.84541 | -46.58181 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e98f8bc-725d-3b4a-af8d-f8af2e35c54f | -4.3131 | -48.09164 | 2025-10-02 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60dccd1f-7f3f-3d30-88e4-839610f08d7d | -3.25592 | -52.85609 | 2025-10-02 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06a0f4c0-f2c8-3e6f-89f6-49d25717ebad | -7.79373 | -42.50547 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 360ec4f1-a89f-34b2-a667-6fdfb9143bbd | -3.82478 | -51.36127 | 2025-10-02 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00a8003a-9abb-3e2c-bba9-17032c4dbf38 | -4.25569 | -48.56211 | 2025-10-02 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3b25f07-f331-3dc1-bc3e-91911d425f1c | -6.79016 | -44.90279 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d6820df-3b94-3bf0-ab79-e6fbd362168c | -7.7705 | -42.54754 | 2025-10-02 04:49:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| cb28d6da-3a60-355a-8fa9-c21725c034b2 | -7.79153 | -42.52183 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| fd8c9f36-ef72-3ba6-9e7c-22f910fee686 | -3.78923 | -48.62785 | 2025-10-02 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 870d3971-da73-3e18-ab7f-15ed5250a8cb | -6.48211 | -44.29348 | 2025-10-02 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 458f4c42-f8f9-3c1c-a072-23aa5f8e83e4 | -6.32459 | -43.89347 | 2025-10-02 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f7c322c8-f3f0-3a3c-8f5c-5e13299b65ef | -5.67673 | -46.19724 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d30265b-8ed9-3462-9595-bc8c4111f6e8 | -8.88332 | -46.59406 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d10fd3d0-6751-3609-abea-8fb823d4a8a3 | -5.45516 | -42.84401 | 2025-10-02 04:49:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b45633e6-bf36-3a25-b0fa-8f1fe89c2d22 | -8.5676 | -48.64877 | 2025-10-02 04:49:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4729858f-a7af-3f26-aa6f-f905c583dc0a | -8.859 | -47.30531 | 2025-10-02 04:49:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a90b24e6-9637-343b-a25b-e09d9b21a78d | -3.87483 | -42.51672 | 2025-10-02 04:49:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ac39d48a-5602-33aa-a3b6-18e1859beb65 | -5.70559 | -42.7014 | 2025-10-02 04:49:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4d86ba6d-c819-3ade-8d49-0e2c2249c2dd | -5.82858 | -42.86478 | 2025-10-02 04:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5ebdc936-66e3-3544-835a-cc554f3a8299 | -5.81056 | -51.86423 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 903f66d6-fbb5-3d43-96f6-5f2195a29f3d | -6.79087 | -44.89775 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b23f0c6-fc7a-398f-ac54-89afc63d3f72 | -3.52111 | -44.03859 | 2025-10-02 04:49:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89294a66-d7e5-3ff6-894b-0807a479a144 | -8.87946 | -46.58912 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d93f1799-3f8a-3c2b-af6b-15f1f47b109f | -5.93877 | -45.8836 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 554cfb97-9644-3c03-98d2-4606dd94eb86 | -4.374 | -48.71707 | 2025-10-02 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9b529bb-0829-384c-984b-677a117464a9 | -4.30161 | -49.19505 | 2025-10-02 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc3a3075-79b5-33f1-ae6a-457f19d9ba5b | -8.82261 | -44.79168 | 2025-10-02 04:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d12c808c-b166-33c1-930f-68332519da9a | -3.38032 | -52.71411 | 2025-10-02 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91e39bdc-1a21-3004-9a26-7d45402515d9 | -3.78132 | -48.63096 | 2025-10-02 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c85eab9c-b37e-32a3-8b70-52f113b36725 | -7.79208 | -42.51775 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8a9aac47-72bd-3c2d-b64b-8b664cb3d473 | -3.45918 | -50.09755 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96b755f1-0f5b-36e1-8e6e-e6a0dd201f4f | -5.83373 | -43.96367 | 2025-10-02 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37f71c38-3435-3891-9085-a12a5eccd424 | -3.46373 | -50.09074 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d382c4a8-3928-3c43-ba09-ddafb355f0f1 | -3.89915 | -49.08477 | 2025-10-02 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77795835-06c8-367d-b57b-b2f52aec66bb | -3.80756 | -51.31959 | 2025-10-02 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be0ad7f3-6c8a-3b68-ac8a-f11d9be274d6 | -8.56055 | -48.64314 | 2025-10-02 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8280fa19-a68c-32dc-a5ab-84c092249a08 | -6.16933 | -47.26976 | 2025-10-02 04:49:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb00f3b5-93c8-3317-a814-d4e150c78aff | -7.08639 | -49.16467 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e254688-df18-3b20-99e4-9ab3d8196544 | -9.0857 | -46.7239 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 991ba3eb-68a3-3e18-b3f8-ca284e560609 | -2.4252 | -47.14513 | 2025-10-02 04:49:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README107.md)
