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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73eb59a3-bd7d-3984-89ae-4d6c6f241bdb | -17.58212 | -57.56667 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| ba25a39d-d8dd-3f0d-a729-0cc116401877 | -23.65405 | -55.23476 | 2024-11-15 04:25:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9d656fcc-8a89-3f5b-98a6-2504721531e1 | -17.56112 | -57.53104 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 84ae76a1-67b0-3081-a10e-4e37cc64510a | -18.43998 | -51.69783 | 2024-11-15 04:25:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4d03c4f-b4aa-32cd-833d-ca339f138d5f | -17.70979 | -57.53016 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e99e8765-f330-3b31-ad6b-62247f86f39c | -17.61234 | -57.55804 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b1a486e2-3bfb-3179-b756-1a13ff218e76 | -17.59528 | -57.55807 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 748d01ce-4748-3c18-ba0c-3925e6bf6485 | -17.26333 | -57.47476 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 74390a11-55a8-38a1-8f49-b270d9efcc7f | -17.59596 | -57.55838 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 33ca0e2c-5adc-3960-bc10-499b7edab222 | -17.64789 | -57.44768 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 907de19a-5631-3594-b200-ed2f69ffac66 | -16.01645 | -59.38401 | 2024-11-15 04:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f02fea3-00a8-3c06-9eae-b060b2ac1eb7 | -17.69982 | -57.55091 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0d95c43e-d77a-3b3e-9795-d469aad02c1b | -17.57869 | -57.44699 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b973f7a8-825a-31f3-9a1e-cb0315d20d88 | -16.09995 | -60.09329 | 2024-11-15 04:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f5e0f449-f420-3b27-8023-35fbdc60ff55 | -17.64408 | -57.54602 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c5fe7e6e-fbcb-3652-87ca-8a2bd2fea601 | -17.2641 | -57.47106 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 8e1ee327-6dff-3269-8897-6475119d5aee | -17.64173 | -57.4501 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c1eb4812-0083-3e9c-8828-898c13b8e4a6 | -16.95235 | -57.64596 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 7ff665ba-9717-33cf-8639-77dd3bf6f563 | -17.58679 | -57.5716 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 69f7bb5d-9db8-3d5f-821c-f8b955a39db8 | -17.57433 | -57.54944 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 97acb47c-3d82-35dc-8d36-f5ff337cd003 | -21.57815 | -55.81609 | 2024-11-15 04:25:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91fff360-95bb-3213-9fd4-e95b73b9d6fb | -23.3801 | -50.26704 | 2024-11-15 04:25:00 | NOAA-21 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ffa3cd7d-0d65-39a6-bc7b-af4f85fce905 | -22.87185 | -54.66441 | 2024-11-15 04:25:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d9b61e59-9506-39fb-b67b-ffc014a7731f | -21.55676 | -55.82405 | 2024-11-15 04:25:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 324dfd11-517c-37ef-ab61-789710f62801 | -17.57356 | -57.55313 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| f8fce308-17fd-3b39-8cdb-ddec0b8d6ac0 | -17.71921 | -57.49212 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4f7ad58f-7a3f-3870-9c1b-f4bd224952de | -17.25009 | -57.45636 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 28b9a110-a3b8-33ab-9afc-c81cd796791c | -17.25476 | -57.46126 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 7634fc74-0a38-3f5f-861e-098f8e048083 | -17.6982 | -57.53141 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 6243a512-a05b-3ffd-a29a-2270b2c4cb95 | -22.23239 | -49.62584 | 2024-11-15 04:25:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b43ed5d3-e771-3531-b2ef-92db416d6cb4 | -17.22318 | -57.19687 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8984d803-a485-3c1c-b057-3b6e62f583dc | -19.77728 | -55.40997 | 2024-11-15 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb70c0a0-0601-3ded-b9e8-e8614325ca14 | -17.5857 | -57.46763 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 9f978e07-585e-3529-83e0-1fb898721b82 | -17.24389 | -57.45884 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| e26dcf34-b279-3ffd-b3a3-aa2439257b75 | -17.59517 | -57.56206 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f7caa9a4-03b8-362c-a4a4-7279e9cbb682 | -17.72384 | -57.49694 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2d351206-5190-3257-9ee9-f147b6a49a8b | -16.95316 | -57.64215 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| decc484c-1e30-3da9-81fd-9cbe47822182 | -17.5735 | -57.52613 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| e135c7da-5f2a-3d9f-8f78-4c1082924a96 | -17.23922 | -57.45395 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| ee55a0ee-d945-3238-a45b-0526e7df982e | -17.59726 | -57.46641 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8097fc70-5cbf-37eb-a0e6-bcf4de96709d | -16.9508 | -57.63184 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 28ea125c-fa39-3bc0-aadb-a391bac25770 | -16.94528 | -57.6306 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| b2e30bc7-2753-3825-8bb2-264b5d2a0efc | -17.57592 | -57.56912 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| f3b2b732-0664-34b0-a545-d3519fafee86 | -17.66189 | -57.54235 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b812d360-8242-3e5a-8f28-6894ca3ef0b7 | -17.63943 | -57.54113 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 7c949b33-b004-322b-9e6b-57e254be0748 | -17.70438 | -57.56136 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| eb1df243-91de-3aa7-8954-51ff858d2f5a | -17.23768 | -57.46131 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| cb68e62a-19c9-3e94-a758-b8c3ddb4d1f1 | -17.58442 | -57.55559 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ba4ba3c1-ff48-3b96-8b8d-3dc014fbbce5 | -17.57279 | -57.55682 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| bd66332a-da0e-3b39-a6b0-fdf0961e7559 | -17.28708 | -57.4739 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 53c752c4-45f0-33c2-9301-eb5b219a0c80 | -17.56035 | -57.5347 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| ee1588a9-fd77-380e-bbb4-a3a65122f18f | -17.71733 | -57.49369 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0b002811-af57-355b-955e-60c262f8af4c | -17.58958 | -57.47614 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 845a1131-b5a4-3876-b2b1-963b6395f3ce | -17.24312 | -57.46252 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 9be72ded-0f55-3884-9393-6004b7133172 | -17.59964 | -57.48222 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 49751526-85f5-3f9d-98a8-71f209d0797e | -17.59438 | -57.56575 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c1a04309-5117-3199-b8da-8981f17766be | -16.94371 | -57.63826 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 590a01bd-be9c-3e43-a39c-7f5909f17c3f | -17.70448 | -57.55581 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| a6dcf14c-097c-343a-861e-f7314db12f8d | -23.59508 | -47.43845 | 2024-11-15 04:25:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 732af76e-9d32-35b3-a8f8-69bddd41b1a4 | -17.56808 | -57.5249 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 00420072-49d0-3a34-8ac1-3c0208a74070 | -17.69279 | -57.53019 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 0ff3224d-4bb5-3f15-b79f-5dac7d68ea50 | -18.0293 | -57.34864 | 2024-11-15 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b2870630-74ac-3806-a04f-8de4b233f273 | -16.94449 | -57.63443 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 863c8de2-ce70-376d-b4f1-314660406df0 | -23.65449 | -55.23352 | 2024-11-15 04:25:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 093ca8b6-66a4-3ddf-9dad-3ef2f0a7c1ac | -17.56189 | -57.52736 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| bcedc6b1-496f-38f4-bcd8-82e3df5e8672 | -17.58722 | -57.4603 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9f54f03e-dfbe-36f9-a595-9749d47ebc40 | -17.69972 | -57.5241 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 34aa9b6c-9d39-3eed-b4c8-8e4113efa61a | -17.58266 | -57.4822 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| d2117535-6ca9-35ea-a65c-57f3cc8b77f7 | -17.72812 | -57.49613 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 68061adb-479e-38f5-abe3-40f234198477 | -16.0987 | -60.09902 | 2024-11-15 04:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99640b63-a82b-342d-a376-b15521ffe6dc | -16.9595 | -57.63954 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3f079a61-a3c3-3c3d-abc4-05c834339b25 | -17.56885 | -57.52123 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 0f534ee4-d41c-3f6b-bd9c-805602259220 | -17.2928 | -57.46976 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e249aaa5-0982-3ec3-a95e-11451727fc61 | -17.59034 | -57.4725 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| fc6a7ab5-2609-3b57-b700-74fe8e79601e | -30.15014 | -52.02404 | 2024-11-15 04:27:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| bbf072c8-65b9-36d4-9f7a-97ea70320cdf | -30.51867 | -51.65677 | 2024-11-15 04:27:00 | NOAA-21 | SERTÃO SANTANA | RIO GRANDE DO SUL | Brasil | 4320552 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 03363ed1-fe9e-35f4-8630-9d80932a3f9d | -27.03491 | -48.80331 | 2024-11-15 04:27:00 | NOAA-21 | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 61156752-85fb-38f5-8dde-04c571b05dd6 | -25.46645 | -52.74877 | 2024-11-15 04:27:00 | NOAA-21 | RIO BONITO DO IGUAÇU | PARANÁ | Brasil | 4122156 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d934969d-5e32-3ceb-a228-8d39068555e5 | -30.0252 | -50.67284 | 2024-11-15 04:27:00 | NOAA-21 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| b0499840-3e5c-32f3-b130-7bd74fc7f6f6 | -31.59119 | -52.93611 | 2024-11-15 04:27:00 | NOAA-21 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| b9c9096a-f7fc-345d-8893-d1d1d604ea05 | -17.2347 | -57.4721 | 2024-11-15 04:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 471d940e-3bec-308b-b78b-699863b1763e | -17.5879 | -57.4917 | 2024-11-15 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| c616a455-1437-36ee-967c-472dfece2e74 | -17.5882 | -57.4711 | 2024-11-15 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| 639ce6fb-4143-356f-99cd-0250d7246ae4 | -17.7048 | -57.5597 | 2024-11-15 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| e3f383be-4dcd-3e24-be8f-455176e5b3a7 | -17.2547 | -57.4493 | 2024-11-15 04:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| abb73bdc-8915-3601-b413-76695fd166d0 | -17.5672 | -57.5557 | 2024-11-15 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 7961a9fb-2759-37f8-a7a0-e07fd9b8bee7 | -17.5865 | -57.5739 | 2024-11-15 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.5 |
| 4eac8b73-0fc9-3759-a364-a67c55d8466e | -17.5678 | -57.5146 | 2024-11-15 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 9477bc00-5347-3086-a045-a88a4e97d729 | -17.646 | -57.5463 | 2024-11-15 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 5efcfee5-27c5-3b4c-9c40-9ffd242a291d | -17.274 | -57.4675 | 2024-11-15 04:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 749647ee-d89c-3207-9b50-578bdfff9fec | -17.235 | -57.4516 | 2024-11-15 04:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 949bfa4d-9643-32d1-816d-006896e638aa | -17.6263 | -57.5486 | 2024-11-15 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| ca3d77d7-a19b-3eba-975d-6c208fc6ca8e | -17.5869 | -57.5533 | 2024-11-15 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.1 |
| d2750379-e9f4-3617-a806-535338035c41 | -17.5668 | -57.5762 | 2024-11-15 04:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| b7e3e9d0-37c7-3872-9d91-095130a338f4 | -17.5675 | -57.5351 | 2024-11-15 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.7 |
| 16c5ea8f-5435-3644-a620-553a1c64c790 | -17.2543 | -57.4698 | 2024-11-15 04:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.9 |
| c5aa2df9-9f84-36bc-bb87-8b2f2a967d95 | -17.626 | -57.5692 | 2024-11-15 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| a82a276d-e198-3b43-b9cf-16c613722d95 | -4.01556 | -38.23919 | 2024-11-15 04:38:00 | AQUA_M-M | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 02d44731-adf3-3664-a0cc-6953a1597948 | -4.01364 | -38.25171 | 2024-11-15 04:38:00 | AQUA_M-M | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| c91d9644-9b78-37f8-8f3f-3683c24d4156 | -3.71159 | -41.68081 | 2024-11-15 04:38:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |


[Clique aqui para ver as próximas entradas](README18.md)
