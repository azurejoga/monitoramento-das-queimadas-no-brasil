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
| 3b4a9414-e65e-3871-9be8-d5d0fbfde33c | -6.6978 | -59.966801 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cffb60dc-18ac-368e-a49b-d00f8175596b | -7.5859 | -57.674 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a43e3f8-14fb-3ad4-90be-9e7e594986e0 | -4.2665 | -55.438499 | 2026-09-22 01:19:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8236cd-4d98-379e-ab95-1c8f60575920 | -12.9392 | -51.055698 | 2026-09-22 01:19:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e79a22b-cb11-3526-9a08-1caa54067970 | -2.5627 | -57.5042 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46ccafbb-881a-3144-be32-4cc25a04e139 | -6.1303 | -55.816502 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf929524-fe81-3cee-a3a2-ff59d1b9e0fd | -2.4214 | -58.2756 | 2026-09-22 01:19:00 | METOP-C | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ffbbeb18-3ed8-3c98-a873-edb35a4cb8f5 | -2.8608 | -57.811699 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6e8e485-5da0-32ee-8a29-6c788cece4da | -5.9805 | -57.7822 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ace5d9b-c51f-33b9-8851-707e5a7ed527 | -11.0533 | -54.1493 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e617f483-1d7e-33e4-a9e7-c4eb40331e7d | -3.4043 | -61.2976 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44819265-3616-3c09-9928-f76789e53ec8 | -6.0997 | -57.673199 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 060cf85d-3c66-30fb-b224-6b948aa539e7 | -6.3007 | -57.7388 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47c8c8b5-82ce-3f1a-9579-defd53ce1166 | -17.629499 | -46.674301 | 2026-09-22 01:19:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5c45f52f-fc52-3c83-9d43-d566fab5d556 | -6.8695 | -59.9063 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0847c28f-053f-32d1-b951-56993d76b036 | -2.7864 | -59.949299 | 2026-09-22 01:19:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3963fec-e939-35b7-9642-912ca3e83d43 | -6.0605 | -57.8601 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67c2ce54-52dd-3d32-b960-8932704badbf | -3.7099 | -60.559399 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76616cf4-1cae-3afb-aeb2-93223b66e908 | -3.7229 | -60.571098 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c7014831-1c2e-326f-95c6-de843e55239e | -4.3484 | -55.6549 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbee741c-331e-3146-998d-5f057ea85f7e | -2.788 | -59.9561 | 2026-09-22 01:19:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4799e3b-ee83-3600-9837-d8842021430e | -11.7697 | -50.810101 | 2026-09-22 01:19:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3fe34d6a-54b3-364c-a7b0-a2f9c9005995 | -6.3543 | -58.2836 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a7831ea-a28a-35b1-9aa2-c306b77cd465 | -6.3532 | -55.842602 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b44aa335-bd0e-3bb3-a943-0aac2d351749 | -6.0278 | -55.339001 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc3734bc-c6ce-3359-8236-7b4a50c56635 | -11.8771 | -46.847099 | 2026-09-22 01:19:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70166f44-69ba-39aa-8d4b-f49f0e53cf3e | -1.9389 | -56.594799 | 2026-09-22 01:19:00 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08e2c157-ed53-33b5-83fb-3210b2d1997e | -11.2592 | -54.145802 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57f2f9ce-7914-3c07-acd7-06b0eba69447 | -8.4904 | -57.613701 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba2880d1-011f-3987-b40a-0bcde6558069 | -6.4576 | -59.998199 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c4f98ae-21cd-30c4-af95-2fa473c7e114 | -7.5957 | -57.671799 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0555cb09-3890-33b7-9329-f5fc56de5b55 | -5.9838 | -57.707199 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e3d3647-bce5-37f3-8642-be23deeaf021 | -11.4165 | -47.319 | 2026-09-22 01:19:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 752b69d3-61ec-37f3-aa63-029804169fa1 | 0.1734 | -60.489498 | 2026-09-22 01:19:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dc9d2ba4-aeda-32ba-8f16-dd27e22ce5d1 | -6.5254 | -58.310001 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f9de3d4-63be-3842-896a-88a43a16b79f | -11.7565 | -50.798801 | 2026-09-22 01:19:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1515ca68-3586-3363-b833-8636683ed994 | -1.3342 | -54.6623 | 2026-09-22 01:19:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d466a98-4d8f-3ede-b1f0-585acd242677 | 3.3044 | -61.2761 | 2026-09-22 01:19:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e3dc8d17-5acc-388e-8d42-516aa5a7e61a | -18.737301 | -46.918098 | 2026-09-22 01:19:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c332e356-a747-3da8-9dcd-cdd1bb8c612e | -2.7896 | -59.962898 | 2026-09-22 01:19:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58993eef-ccce-3b20-b3f3-5cac2c5bde2c | -6.7507 | -59.067101 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee2b4cb1-9f06-37c9-b9df-53be1553cc6c | -6.1193 | -57.757999 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f605736b-0253-3841-8bcb-1ec04ab6c435 | 2.0945 | -60.2104 | 2026-09-22 01:19:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9e89e651-3877-3d3f-ab71-64cf0d0f2171 | -5.9151 | -57.678101 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b53f0fe-a5d5-3421-a591-1559c4e772af | -6.0637 | -57.874199 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60778818-0632-3050-8776-3950937ef9f7 | 0.1719 | -60.4963 | 2026-09-22 01:19:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9ba11d0f-c17c-3670-b4c8-56af206d3d58 | 0.8806 | -60.554798 | 2026-09-22 01:19:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 734b414c-74ec-31d2-a1ce-4cf29888967f | -8.2511 | -55.2668 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a43e251-2d34-31f2-b358-59087f272a8a | -3.2323 | -53.939701 | 2026-09-22 01:19:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 866e3cb6-85ec-311e-a85f-bbe5d57dc0ca | -3.5828 | -59.061199 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b6838f4-9835-3cd8-bf3b-d8fccd40641f | -6.8361 | -58.990101 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db0084f0-4986-3e5e-af24-19e40ae6969d | -3.6835 | -60.624001 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d57f96f1-5d60-3132-9c7b-14d19f39c860 | -3.4205 | -60.195499 | 2026-09-22 01:19:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f779d066-d2d7-38fc-9004-891be51c7950 | -2.8591 | -57.804401 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba0761fe-d338-3b34-8c8d-39396e1d4ca8 | -8.2571 | -55.291801 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e704d782-8e09-3f0d-ad59-3ba2e3e5203a | -5.7697 | -56.5228 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a35eea8a-4f87-3554-8dcb-987c7ac5f5a3 | -7.8844 | -54.723999 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9b3901e-4586-3b52-9390-f06c8a89cc0c | -5.9169 | -55.699299 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5345866-ffae-335f-8038-e3b1a19e8ce7 | -6.1417 | -59.877899 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9aae5e9c-e8eb-3d3e-b933-304526ed5a8e | -12.1327 | -47.373402 | 2026-09-22 01:19:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c709dd2-7fcb-3b9c-89f2-d5fbc5a1a168 | -11.3181 | -54.047001 | 2026-09-22 01:19:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b8addf4-f8f2-33d0-886d-84bd69f8b20b | -8.5953 | -54.630199 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c71a284-9761-3830-aec8-54c425e872d4 | -3.3883 | -56.929199 | 2026-09-22 01:19:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b087a96f-99c0-3bfd-bbb9-7ca604188da0 | -7.5843 | -57.667 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09603731-93cf-3d30-a595-0e7d437cdf61 | -3.4784 | -59.5938 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05561688-f24d-3033-a56b-9aa45afb487d | -5.7706 | -57.455502 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d01afbc7-126a-3d65-94ea-78f3b5ebbef1 | 0.2986 | -60.4389 | 2026-09-22 01:19:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 80e38b2f-4711-3cac-9ecb-dca04685a72b | -3.4819 | -59.5644 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7303a7e3-50c2-3575-964f-1599e37ed2ed | -3.3976 | -59.5117 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a394fdb3-3f6c-3faa-a72f-14acd3fcc313 | -10.9006 | -54.073502 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4cbacfd5-ac9c-3e77-b52f-e0ae3fdccd0a | -8.2688 | -55.297798 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0209195-29e1-3bbb-aad6-947ef82f6501 | -11.76 | -50.812599 | 2026-09-22 01:19:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3266a4b1-868f-3a8f-9798-547f6ffa95a5 | -11.4163 | -46.782398 | 2026-09-22 01:19:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d43bfe7d-1c1a-3bc3-b9e2-4a9b2a8c7039 | -8.7994 | -60.801399 | 2026-09-22 01:19:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f24e43c4-9065-353c-956f-d49eab4a4c1e | 1.814 | -56.0779 | 2026-09-22 01:19:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c03d933-790a-30e1-83e6-fd232bfc359e | 2.3136 | -60.918201 | 2026-09-22 01:19:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ff7d664d-467d-377a-94cc-f064168025b6 | -2.9426 | -57.808498 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73e0255a-cfeb-3baf-9c98-ea52abc0c6c3 | -8.259 | -55.300098 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 016e45a7-23ee-3e1a-a7e2-76e944c356a8 | -3.069 | -61.273701 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7232dfec-39ff-3c15-8928-9d1918ba0001 | -3.4026 | -61.290401 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 708ac9c1-2069-39f0-a223-39183a44f66b | -3.3405 | -59.846802 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95a2e4f6-3cfb-36c4-b098-740c47bd3e74 | -3.5399 | -60.582699 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd3de700-a318-3534-927d-a98afda9f00b | -8.6148 | -54.6255 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b98797cd-7d34-38c0-a1ad-a4169428c372 | -3.4007 | -59.525299 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 803bdb0f-e17b-3beb-a9a2-ec4d9ef8967d | -10.9348 | -58.337601 | 2026-09-22 01:19:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57585b09-3690-3ff8-b66b-b2d090b2731c | -8.6051 | -54.6278 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eeddc26-95bf-3990-b504-20c97428d2df | -6.3513 | -55.834499 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e71f007e-1056-3374-97ed-3acc74644244 | -11.4389 | -47.364101 | 2026-09-22 01:19:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 085c0c71-7918-3af5-a039-ef1f676d00cb | -3.6951 | -60.584702 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f4dd76e-201f-3e84-a553-92b0cd69c1dc | -9.6614 | -54.3363 | 2026-09-22 01:19:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d9e84e6-6db0-3add-b43f-d593149c76f2 | -2.4133 | -58.284901 | 2026-09-22 01:19:00 | METOP-C | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f19ee24-b0a6-39ed-8808-d571ffbb0872 | -6.7408 | -59.430698 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9dfdb0f2-e5fd-3811-8022-f3e9d7326c15 | -3.4741 | -59.5303 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 775a13d9-f230-34c5-9f4d-f0a7b0b3f2c4 | -3.4628 | -59.5257 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70436d42-7b69-3aa6-a3ab-113a9f8f8de3 | -11.4069 | -47.321701 | 2026-09-22 01:19:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d67ebbd1-53c0-37b8-9ad3-36301fd307dc | -3.5256 | -59.934502 | 2026-09-22 01:19:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 25b859aa-a5b7-329d-a0dd-ea476d7fae13 | -8.2649 | -55.281101 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a59591b0-5431-36fd-ace3-19fdf66173c4 | -6.8581 | -59.901501 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1940324-e598-3a44-bfad-e2b0109f8ad0 | -7.5794 | -57.690201 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 332a170d-95f3-3086-b56d-5138d50e35a8 | -3.7147 | -60.580299 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
