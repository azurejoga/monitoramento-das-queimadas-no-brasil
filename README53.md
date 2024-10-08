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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0926a0b5-4754-3206-b8fe-833047d08748 | -2.87421 | -52.90154 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1de65612-c0ad-38f9-8efb-f319cf50fc97 | -2.87357 | -52.90548 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1782b7c-1083-328f-bec1-f8ea4a1e37fa | -2.87293 | -52.90944 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40de3658-1d26-3c83-a47d-605c24f31500 | -2.87229 | -52.9134 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e21d6290-062c-340d-b7a4-cdec43ef0eae | -2.86995 | -52.90094 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e077ee3b-ef8d-3b87-9465-956e622ca6ef | -2.86931 | -52.9049 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6273507-e96d-3cc7-b182-fadf62aa5d0c | -2.86867 | -52.90886 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf36dbd8-a670-3cd1-bdc1-2c072c21c69a | -2.86802 | -52.91281 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c8c3e29-3254-3cec-8317-e69a0ae9bf7f | -2.86569 | -52.90035 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4156e764-248b-3e53-be9d-0de2d9de4925 | -2.86504 | -52.90432 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee9ae83e-bd65-3c83-b1ec-0e7c135e5fb9 | -2.8644 | -52.90828 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 057aaa9c-7abc-37cb-ac98-3dc1374f4f79 | -2.86376 | -52.91223 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4895087-6240-3aaf-9a5a-50f18736f9df | -2.86143 | -52.89975 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6973a6d4-e618-366b-8eee-2f2f585a495d | -2.84713 | -53.3171 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac2114b8-7ffb-312d-933f-468790b000db | -2.84646 | -53.32135 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cd54f7d-5f1c-3192-b9f9-c6dcea1967d9 | -2.77497 | -53.211 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5364e98-06f2-31af-8d40-7b8dd4f52655 | -2.77328 | -53.21207 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e29994b4-a030-39c3-a08d-ead02e5584e4 | -2.77062 | -53.21035 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8867f12-0672-3476-b278-142a4493e172 | -3.90298 | -52.38056 | 2024-10-08 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a62c078-a8bb-3779-a94b-ec6d96eb05e9 | -2.21817 | -53.69103 | 2024-10-08 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40094d10-250b-38fe-aa7a-f4bcdf745b4f | -2.21743 | -53.69564 | 2024-10-08 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcb28a3f-6888-3072-8036-9641db527098 | -1.23202 | -54.70118 | 2024-10-08 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e05a17b-f16a-3d91-bda4-b1f0cc0370df | -1.19908 | -54.22161 | 2024-10-08 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b12ba634-8a02-3908-b050-4e89cbf80af7 | -1.09199 | -54.15715 | 2024-10-08 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7560fa40-6209-360a-ba06-e93270da62bd | -1.09104 | -54.159 | 2024-10-08 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8841f8d-690e-3a98-88cc-4feac8c6a5ea | -1.08721 | -54.15649 | 2024-10-08 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bc782e5-77c3-3915-b2d1-3c15a57a72ee | -1.08627 | -54.15828 | 2024-10-08 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edaaf657-e4a6-3e77-a01a-6fa01d2cb1d3 | -1.04271 | -53.53803 | 2024-10-08 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ee04310-0747-39eb-a0a7-8e8c61360448 | -1.03085 | -53.73204 | 2024-10-08 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c85075a9-922c-390d-8340-51f899ceb83b | -1.03019 | -53.73624 | 2024-10-08 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0fd3a795-d95d-34b2-bce5-f064a092a40b | -1.02692 | -53.72689 | 2024-10-08 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f0fe8e62-a028-3a46-bf16-1d27e7e143e2 | -1.02622 | -53.73132 | 2024-10-08 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ccdbfb1-7ffa-3503-82c0-5434403f181b | -1.02554 | -53.73563 | 2024-10-08 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14982e57-d961-3d7e-a1e1-d73e78837ea7 | -1.02238 | -53.72558 | 2024-10-08 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8bd19a6-fc7d-3240-8c56-600eecb20aa5 | -1.02165 | -53.7302 | 2024-10-08 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f1cf51d-1b48-3368-8650-7619d4de1c5c | -3.56903 | -54.3348 | 2024-10-08 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9efff7ac-d8e1-3d6a-97ff-50ed13e5b82f | -3.56825 | -54.33969 | 2024-10-08 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a46dd2e7-08d8-3ce1-8b25-b96f4d9e51bc | -3.56746 | -54.34462 | 2024-10-08 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70bee925-c817-3186-bbcf-41f7af6fde4c | -3.56746 | -54.33699 | 2024-10-08 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e13cd189-9255-347f-8ba8-997d1f6b485f | -3.56663 | -54.3419 | 2024-10-08 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e50ab654-d2f4-3a04-9e37-385a6d30f5b0 | -3.56443 | -54.33385 | 2024-10-08 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9bfb068a-c9d5-32a2-aafa-5641eb1daa10 | -3.43888 | -54.06261 | 2024-10-08 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 728be0b0-d4f7-3818-b4d0-70bf181d455f | -3.3777 | -54.90794 | 2024-10-08 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16f49375-cebf-33de-8c50-963707439476 | -3.37289 | -54.90698 | 2024-10-08 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e83238d1-1058-3f60-af2b-fc8d14c2154e | -3.07026 | -54.77496 | 2024-10-08 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 342de9d8-0a91-3ca4-97db-31212ac6db68 | -3.06561 | -54.77758 | 2024-10-08 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 287fcc4f-4734-3a15-ac90-17dc5d8da18f | -3.06544 | -54.77424 | 2024-10-08 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6df1392b-a6d6-374b-848b-cec1043e80f5 | -2.95097 | -53.70648 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0771b0d-eac3-3f74-bff2-112039691a8e | -2.95024 | -53.71096 | 2024-10-08 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ad879a3-4f98-30c3-a9dc-78e331756a16 | -2.63994 | -53.9664 | 2024-10-08 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26a4aea5-a286-3736-9a9f-57d752d904bd | -2.63947 | -53.96873 | 2024-10-08 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cac21284-433b-3cf3-ad8c-864d3324c01b | -2.81498 | -54.35886 | 2024-10-08 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ede2c667-0b2d-36ad-87b9-c2eca2b01405 | -1.46866 | -54.96222 | 2024-10-08 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78614d5f-9671-3609-868c-5be3a7a02190 | -1.4682 | -54.96508 | 2024-10-08 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d83ced12-4ac2-30db-82de-41674b049aec | -1.26177 | -55.85248 | 2024-10-08 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba22a47e-d5c8-34cd-ac5c-7c382af5b3fc | -1.26125 | -55.85582 | 2024-10-08 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ae6f11c-85f6-32a0-a63b-07eb23a69839 | -1.26002 | -55.85251 | 2024-10-08 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb210f36-d6cc-37a0-8b17-7d58cbb00049 | -1.25947 | -55.85582 | 2024-10-08 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39701971-af85-31f5-a72c-87ca52ead5de | -5.781 | -49.32617 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d117416-c40c-316e-b6fc-ef59051caca4 | -8.7129 | -44.01801 | 2024-10-08 04:34:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0db2b879-8a34-3653-b115-b0e8c00bebf4 | -9.95385 | -44.1134 | 2024-10-08 04:34:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7796af00-84a5-35b4-b328-ddca88b9131a | -9.94189 | -44.08622 | 2024-10-08 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee8885b2-2dd9-3ec9-b017-2d53cc660b40 | -9.42809 | -44.12419 | 2024-10-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b911aa5-aba5-36b9-8878-1f5312bc2edf | -9.42425 | -44.1235 | 2024-10-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5084fa4-16d2-39f6-9a99-65cba1f40578 | -7.8475 | -45.35659 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e8dee602-b1cb-37f0-b5d2-6282b5970afe | -7.75596 | -45.16851 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49b6c02c-5e44-36a6-ae02-d73c9f2e01e3 | -7.75239 | -45.16797 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7d8b59e-331a-3b9e-b054-6c43af12b78a | -8.00607 | -44.38158 | 2024-10-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12362e65-5edb-383f-ab58-3e8ab9052a66 | -7.97993 | -45.17116 | 2024-10-08 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62922f4d-cbe2-3ad8-a4d1-5a9926ddeedb | -7.95479 | -45.24265 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 170f83a2-3a90-3287-a3b7-c2cecd55e63b | -7.86226 | -45.35474 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a4051004-cd17-3033-97e4-0ca5668105a3 | -7.86166 | -45.35875 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 22d9e418-1708-3089-9e0c-29e64392ec52 | -7.85872 | -45.3542 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1a4245bc-5f11-3c63-bff5-acb71ce538df | -7.85812 | -45.35822 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a05e2941-b044-3c34-8cdb-f958784dfb64 | -7.85752 | -45.36223 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 847f6ae9-ecfc-3833-91c1-ec7f16b808a4 | -7.85458 | -45.35768 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3ee9264b-e456-3a1f-8b88-928e71b98488 | -7.85164 | -45.35312 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 52a52923-6ec5-3a6d-a10b-b8ab2310288c | -7.85104 | -45.35714 | 2024-10-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7b1c9f8d-4e28-3c4e-9514-01c441e791b5 | -10.50077 | -44.01961 | 2024-10-08 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a68f5d0a-6000-392a-afef-b759ab9fc9aa | -10.5001 | -44.02084 | 2024-10-08 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 356b4972-1f91-325a-8929-2b35559bc0fe | -10.74709 | -45.561 | 2024-10-08 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf048b27-a37f-3359-99b4-1936a9c305df | -10.66508 | -44.5063 | 2024-10-08 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e52008e-2dbb-34fd-a6b5-635820fe05a2 | -6.69808 | -43.95254 | 2024-10-08 04:34:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a72a9d8-cb5c-3b1e-8def-cc66ecfa90cc | -6.69739 | -43.95713 | 2024-10-08 04:34:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9997964e-8e67-340e-9e6c-825863a32d2a | -6.48453 | -43.87831 | 2024-10-08 04:34:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5afdc3ee-2ca1-3eca-8afe-0093d8c2a33e | -6.48076 | -43.87776 | 2024-10-08 04:34:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7525e4f-c842-3fb2-bee3-69a2bb5066e4 | -13.85772 | -44.58239 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc5c6d46-4036-38cd-8546-8544288ed022 | -13.85325 | -44.58534 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 879093da-9ab1-33fb-9129-e9a491851764 | -13.84927 | -44.58472 | 2024-10-08 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50017be5-44db-3674-9a23-daa5da7e2899 | -10.66441 | -44.51112 | 2024-10-08 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fee96698-c6d1-3add-aabd-cea83a6b9c62 | -10.66206 | -44.50924 | 2024-10-08 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fa4192c-b102-3f60-9c97-18dd77f21a50 | -10.61011 | -45.18938 | 2024-10-08 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7759da9d-4e62-3f9b-9bf4-d48315f5add3 | -10.51503 | -45.12291 | 2024-10-08 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4974e53c-7f83-3821-a8cd-793731fc5bbe | -10.47133 | -45.11167 | 2024-10-08 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dfb974c7-85f0-3ab6-bea1-9c6f7f76e7ce | -10.26644 | -45.4925 | 2024-10-08 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f04b00a3-0bd7-354c-8323-10a42c72d59b | -10.23924 | -45.12008 | 2024-10-08 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93ff0480-27ac-35bb-9688-493a6d9289f9 | -10.11964 | -45.21957 | 2024-10-08 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7187374-21d8-3079-9c54-f1f1e58e6045 | -10.07054 | -45.274 | 2024-10-08 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba7e40f0-651b-360f-9ac6-80cb66615517 | -7.25309 | -39.85376 | 2024-10-08 04:34:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f17ad2dd-3eb1-3cac-9648-d8428d019f14 | -7.25269 | -39.85663 | 2024-10-08 04:34:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README54.md)
