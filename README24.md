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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f08a6ac-bca1-375e-b16f-8398f34d8b50 | -13.3014 | -45.1976 | 2026-07-08 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| af630146-8947-3a9c-a4df-17a9860a7616 | -9.0095 | -40.9926 | 2026-07-08 12:50:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 9dcc138a-61b9-383e-b679-93534c2995b6 | -13.3009 | -45.2209 | 2026-07-08 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 3429d72c-5ba1-321a-9003-c971d0de4324 | -13.2824 | -45.1776 | 2026-07-08 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2f500071-a2ca-3d22-8ecb-f1c2a51b20a8 | -13.3014 | -45.1976 | 2026-07-08 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 2b79af18-831e-3872-8eb5-26cfa7fb9a1a | -13.3009 | -45.2209 | 2026-07-08 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 3344e5a1-738e-356d-a3d0-0cd82aad2500 | -13.282 | -45.2009 | 2026-07-08 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 197.3 |
| 08890e62-7f22-3820-97cf-1b4544563d73 | -4.81301 | -54.79213 | 2026-07-08 13:04:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 8a76b184-c6ed-31dc-a255-dc033a862809 | -13.2824 | -45.1776 | 2026-07-08 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 2df97e85-74cc-3bb7-8ff3-254ef5c69250 | -13.3009 | -45.2209 | 2026-07-08 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 0308b51e-dee5-3820-9cd3-1ef238fac2b0 | -14.1442 | -52.8926 | 2026-07-08 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 73ce2f05-081b-31a7-909e-7822816e15fc | -13.282 | -45.2009 | 2026-07-08 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 194.3 |
| d8009eaf-f870-39a1-9497-2433be004b0e | -13.3014 | -45.1976 | 2026-07-08 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 55d8c6ae-ceb7-3de4-8e15-53cf8125f24d | -13.3014 | -45.1976 | 2026-07-08 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| a3ae76de-a286-3f5f-883d-987f7165925f | -13.2824 | -45.1776 | 2026-07-08 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 201.6 |
| c2f25ea7-05c9-3f64-82a8-7995e807c5df | -14.3158 | -45.7884 | 2026-07-08 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| d17a0236-17aa-345b-afed-77a9e8b82376 | -13.282 | -45.2009 | 2026-07-08 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 275.4 |
| e56a09c4-c7ff-352d-b922-2477f7a8896b | -14.1442 | -52.8926 | 2026-07-08 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| a86fde5b-f475-3606-8d0c-c8b8bd374874 | -8.3839 | -48.2445 | 2026-07-08 13:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 420833fc-af56-387d-a2fa-31e5b2f87ffd | -13.3009 | -45.2209 | 2026-07-08 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 9c3953fb-4dba-364e-bf02-141de748ba01 | -13.3014 | -45.1976 | 2026-07-08 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 53ce45a6-ddcc-380f-909b-645370b52c1c | -14.1445 | -52.8715 | 2026-07-08 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 601d57da-78da-336d-bb07-407d8aa9e8d4 | -14.1442 | -52.8926 | 2026-07-08 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 4de717ce-bd50-3a0d-8d59-3e9edd495237 | -8.3839 | -48.2445 | 2026-07-08 13:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 59214c52-7cc6-39ba-aa66-3d0f6594d33b | -13.2966 | -54.4068 | 2026-07-08 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 755eab68-f543-3d4d-9dcd-c1b520326a6a | -13.3018 | -45.1744 | 2026-07-08 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 9e44ac59-502a-3390-8905-f331b06ab5d9 | -13.2824 | -45.1776 | 2026-07-08 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 225.3 |
| 0c38a66b-3833-395d-90c4-fff0f1ea4cf5 | -13.2774 | -54.4088 | 2026-07-08 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 76d54c37-c8b7-34c3-8213-0b74b0730683 | -13.282 | -45.2009 | 2026-07-08 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 239.7 |
| 247b2c7a-d96f-302d-9e50-ec5e637fd61d | -13.3014 | -45.1976 | 2026-07-08 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 2686206f-0be1-323f-aab0-9b7904d0b6ba | -13.3009 | -45.2209 | 2026-07-08 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 527e0e50-8c1a-3306-a11b-25784b06eb21 | -13.282 | -45.2009 | 2026-07-08 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 268.0 |
| 48210650-e2b7-36ee-bd70-1b086ad337d3 | -13.2824 | -45.1776 | 2026-07-08 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 314.1 |
| 07d46b1f-f0c7-347d-8638-9502ac52a1b7 | -13.2774 | -54.4088 | 2026-07-08 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 5b53e4bf-f5f2-3766-842c-840ea639842e | -14.1445 | -52.8715 | 2026-07-08 13:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 77479f6b-bf57-3658-8001-1d2bec071c23 | -8.3651 | -48.2463 | 2026-07-08 13:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 82ebc1d3-bc67-3c5c-a0a4-24191e736a6d | -14.1442 | -52.8926 | 2026-07-08 13:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 9c2f369b-7acf-3f08-980c-cd1f98c85f87 | -13.2966 | -54.4068 | 2026-07-08 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 1b5e18bb-7580-31a7-becf-5179f7f23afd | -17.5509 | -54.0157 | 2026-07-08 13:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 82.2 |
| d450415a-aba3-3b89-95f0-9b78c9c6c2b5 | -13.3014 | -45.1976 | 2026-07-08 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 8667415a-f31b-3594-8785-eb87c9115a52 | -13.2966 | -54.4068 | 2026-07-08 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| ab63add5-ae88-3be6-a9ab-26a41c39f866 | -14.1442 | -52.8926 | 2026-07-08 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| a0ed78ea-5369-34dd-a6d6-5605c8958e7c | -13.282 | -45.2009 | 2026-07-08 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 9563aefb-c956-3b00-8fdd-360a741aa5d3 | -13.2774 | -54.4088 | 2026-07-08 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 55e1efee-2355-3e1c-9c00-b4d839f75a26 | -13.2824 | -45.1776 | 2026-07-08 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 361.3 |
| 190a978f-0f3c-374f-80a3-0d8be64c9907 | -14.1445 | -52.8715 | 2026-07-08 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| a3558944-3051-318f-96c2-516800916299 | -8.3651 | -48.2463 | 2026-07-08 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 6259081d-c1d1-3769-b55f-62367eb75158 | -8.3651 | -48.2463 | 2026-07-08 14:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 9200b9f1-73b1-3890-a874-396de2af5efa | -13.3014 | -45.1976 | 2026-07-08 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 9ef44e49-e021-3329-bb95-7de79babf7f6 | -17.5311 | -54.0186 | 2026-07-08 14:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7db8c630-b2d1-378c-93b8-83d7904453a4 | -13.2772 | -54.4295 | 2026-07-08 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 2240ba33-012d-30d7-8636-808295727aa9 | -13.2963 | -54.4275 | 2026-07-08 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 158.3 |
| c95c742a-e8d6-3979-8fdb-d34278de1b3b | -13.2966 | -54.4068 | 2026-07-08 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 173.5 |
| dfcc38ab-960e-3d1f-b2fe-64fcce7e20d5 | -13.2824 | -45.1776 | 2026-07-08 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 405.4 |
| 1e03bb33-5eec-3fb0-9036-38cdc0dbfa85 | -13.2774 | -54.4088 | 2026-07-08 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.0 |
| e154f897-0104-3d4d-aa83-217603ca0bad | -6.4973 | -42.2142 | 2026-07-08 14:00:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| cc1375df-eeed-39d1-8672-b369b2eda548 | -14.1445 | -52.8715 | 2026-07-08 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 02ea5156-7c1a-357a-afce-4f983dae6e05 | -14.1442 | -52.8926 | 2026-07-08 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 131.7 |
| c3be23d6-5b07-3844-98c4-17c25d6f4d43 | -17.5509 | -54.0157 | 2026-07-08 14:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 2920d917-466a-3d43-a860-8391700a842b | -13.2631 | -45.1808 | 2026-07-08 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 95d2cd41-1b6a-3640-a075-ee56fcb0c9a4 | -13.282 | -45.2009 | 2026-07-08 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 244.5 |
| 9c185373-2ba7-390a-b13a-ba44d5269dfb | -13.2772 | -54.4295 | 2026-07-08 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e6a37e72-3219-3135-9484-c0f9e71d6205 | -14.3163 | -45.7653 | 2026-07-08 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a28c6852-35d6-3c56-b63c-097e3ec24b3b | -17.5509 | -54.0157 | 2026-07-08 14:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 01895333-1f43-3c96-823e-f0d17edf4eb7 | -13.3014 | -45.1976 | 2026-07-08 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 802eeb10-2bce-39f3-bf30-76715515e09b | -13.2824 | -45.1776 | 2026-07-08 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 369.9 |
| 7be845d3-a9fa-3063-bc3e-dfe54efd7f13 | -13.2963 | -54.4275 | 2026-07-08 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| e8a4d5ce-17b7-34e1-993b-3df6d1ddf7b7 | -13.2966 | -54.4068 | 2026-07-08 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 9315fc66-bcc9-3a1b-91c0-d370df802a09 | -14.1445 | -52.8715 | 2026-07-08 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 4cb9dd96-59a0-362a-892a-7dd4de821af2 | -13.2631 | -45.1808 | 2026-07-08 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 95940a2b-bfe2-30c8-bb64-2f73cf92c164 | -14.1442 | -52.8926 | 2026-07-08 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 6843c9da-dbe1-3560-89da-17e20559c227 | -2.5752 | -48.9929 | 2026-07-08 14:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 59215ab1-421c-3c01-8a8b-71a1a0aa44cb | -17.5311 | -54.0186 | 2026-07-08 14:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b2a2ef31-6637-3bcc-903a-2b6d8313fb8f | -13.282 | -45.2009 | 2026-07-08 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 201.6 |
| 122c3921-ac18-3e84-92cb-57f5beb054fe | -13.2774 | -54.4088 | 2026-07-08 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| b8247b5b-c96f-32aa-8e45-1320f524890b | -13.2772 | -54.4295 | 2026-07-08 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4aabaf9e-262d-3b6b-a060-f4edb785a27e | -2.5752 | -48.9929 | 2026-07-08 14:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 326ccc0d-a9dd-3272-b616-dc33821d0eb4 | -14.1442 | -52.8926 | 2026-07-08 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 650404d8-4920-3099-b8f7-1878b3d0442a | -13.2966 | -54.4068 | 2026-07-08 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 4c9cea4e-02df-3531-95de-e43a64fc2064 | -6.4973 | -42.2142 | 2026-07-08 14:20:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 1603a37d-5f6f-3614-b745-39854a01df51 | -17.5311 | -54.0186 | 2026-07-08 14:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 14fc3e7d-56be-3779-b645-3c11d312c191 | -13.2774 | -54.4088 | 2026-07-08 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 51e4f9de-21fd-37da-9c96-b0f0fed545b5 | -13.2963 | -54.4275 | 2026-07-08 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 1007de71-23d4-3a6d-8d80-a1d318e0244d | -17.5509 | -54.0157 | 2026-07-08 14:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 98.1 |
| b0da2356-d965-31e7-b186-fe22c5deb089 | -14.1445 | -52.8715 | 2026-07-08 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| af95be95-0933-3a01-b16c-373efaef965e | -13.2631 | -45.1808 | 2026-07-08 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 48156f57-9769-3745-9c0c-e3c3baccac05 | -13.2824 | -45.1776 | 2026-07-08 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 392.7 |
| 590be8cd-80e2-3c81-b2d4-0debc816fd19 | -13.3014 | -45.1976 | 2026-07-08 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3326b5ff-84b5-37e5-8034-349c0c3ed75d | -13.282 | -45.2009 | 2026-07-08 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 3334e46c-c783-32e6-9ad6-1597ca7dbcbb | -13.282 | -45.2009 | 2026-07-08 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 27797931-30f8-3e83-a37b-97e56490eea0 | -13.2631 | -45.1808 | 2026-07-08 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 48a1ddac-21de-3ed7-80fa-dfbc7716f2bc | -14.1445 | -52.8715 | 2026-07-08 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| efd60bc0-e598-3e71-b848-2e148dac3655 | -6.4973 | -42.2142 | 2026-07-08 14:30:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 76185e28-7441-3065-b4e5-8f42cfb7a7f4 | -13.2966 | -54.4068 | 2026-07-08 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 74bf363f-1fdc-38e2-836d-b42f58201c24 | -13.2963 | -54.4275 | 2026-07-08 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| f5a39b9f-d16b-3e87-993f-bce44597f47c | -14.1442 | -52.8926 | 2026-07-08 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 8416ad23-f509-3677-9434-d5791d1f54a7 | -5.9177 | -43.8584 | 2026-07-08 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 4c624bf8-95e4-327e-b727-7a8b63ee4b20 | -11.6472 | -46.3646 | 2026-07-08 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| ffcced1a-bcd5-3f10-ba42-fa7afd6f5225 | -13.2774 | -54.4088 | 2026-07-08 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| eb017edf-010a-36af-a2c1-58867fd234cc | -13.3014 | -45.1976 | 2026-07-08 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |


[Clique aqui para ver as próximas entradas](README25.md)
