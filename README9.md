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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c98244a7-7114-37b1-938d-c347df38001c | -3.7752 | -53.4012 | 2024-10-21 00:55:28 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ac1e7c93-c2de-32ab-849a-70124b54b7bd | -4.8474 | -44.3472 | 2024-10-21 00:55:33 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 07b3fc6a-6228-33fe-a6b0-1971d09ca06f | -4.8476 | -44.3243 | 2024-10-21 00:55:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 832c98fe-6ed9-321a-988f-df84712557a7 | -4.8661 | -44.3461 | 2024-10-21 00:55:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 240cadb4-2b82-35ad-85e1-714afc7c162d | -4.8662 | -44.3232 | 2024-10-21 00:55:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 53cb544e-063d-3e01-9b0e-1533579cd735 | -4.8924 | -45.8386 | 2024-10-21 00:55:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5a9fbb6e-a6ac-3d7b-a41d-7d1d15a0eab6 | -4.911 | -45.8374 | 2024-10-21 00:55:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 3293d814-2a10-3036-b047-36274cce2d5f | -5.6707 | -46.4363 | 2024-10-21 00:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 1ab49089-f69a-33e0-b539-48369008786c | -5.6709 | -46.414 | 2024-10-21 00:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 21e6ea6a-d6d8-3d2d-b435-4eecb018296c | -5.6894 | -46.435 | 2024-10-21 00:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 149.9 |
| d1392e72-a9b1-3fab-888d-9dbaf29cf550 | -5.6896 | -46.4128 | 2024-10-21 00:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 15e10630-cf48-32f4-8791-12c5d3f11984 | -5.7081 | -46.4338 | 2024-10-21 00:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 4c9c3c8a-773b-3039-ab6d-4c6f78b54c46 | -9.3718 | -66.4891 | 2024-10-21 00:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 79ca4c34-4b54-30be-8de2-c0bc871c7b40 | -12.4778 | -63.1885 | 2024-10-21 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 52522e84-28bb-3593-8484-a0d154cf7f71 | -12.5147 | -63.3014 | 2024-10-21 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 444c2d14-121d-3c41-89d1-39d4cfb14656 | -12.5168 | -63.0329 | 2024-10-21 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6c03e548-8086-396c-86bc-f6fab0e80dc2 | -12.5357 | -63.0319 | 2024-10-21 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c27d88a8-d6fe-34f1-96c2-94b6215f2e41 | -17.7851 | -57.4679 | 2024-10-21 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 01fc9e80-5837-38ca-a7bf-9a565f4b3e66 | -17.7062 | -57.4774 | 2024-10-21 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 39c22bae-0bb5-3715-81d4-05bc487be877 | -17.7065 | -57.4569 | 2024-10-21 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 194.5 |
| a991b1b1-1d05-3b01-80fa-c74e64816a39 | -17.7069 | -57.4363 | 2024-10-21 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 58fe1326-78a0-3113-afb9-6f1db8e83f2e | -17.7259 | -57.4751 | 2024-10-21 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.4 |
| 46ed6baa-6a5d-34da-b8e3-c41625de644f | -17.8045 | -57.4861 | 2024-10-21 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.0 |
| f9dcd2dd-7d08-397d-b004-729b2d2403f0 | -17.7262 | -57.4545 | 2024-10-21 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 165.0 |
| 02bcdc16-f60c-361b-8867-ec8689cb392e | -17.7848 | -57.4885 | 2024-10-21 00:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.3 |
| 1d065c65-7352-31ee-b4d1-fb9bce3aa14f | -18.263 | -56.1021 | 2024-10-21 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.6 |
| abba3c79-65fa-30fd-ba11-be32dd62211a | -18.2828 | -56.0994 | 2024-10-21 00:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 235.3 |
| ba6f3237-c4f0-3cd3-8046-979fb7ab8356 | -18.2832 | -56.0785 | 2024-10-21 00:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| b3628443-d999-3830-bfb1-cf66c3880f29 | -19.546 | -56.63731 | 2024-10-21 01:02:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 44.4 |
| c431b309-39b8-33c0-a48c-7e761ad3c7f7 | -18.29861 | -56.19031 | 2024-10-21 01:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 0c390305-7d8a-36ff-bb06-14239ebc3f89 | -18.28597 | -56.08773 | 2024-10-21 01:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 201b2885-e99f-388d-9108-02e19201281c | -18.2762 | -56.10954 | 2024-10-21 01:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 232.1 |
| 3d82888e-11f7-3041-b94c-7c02efe993bc | -18.27427 | -56.11644 | 2024-10-21 01:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.3 |
| 2b0ce905-27b3-3298-9ef3-573b60c144a0 | -18.27362 | -56.08234 | 2024-10-21 01:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.1 |
| 35a5a484-0286-3c40-96c4-d3c0c447c193 | -18.27149 | -56.08926 | 2024-10-21 01:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.2 |
| d917aef6-b79c-3632-b0d3-6176b1b5a324 | -17.68039 | -57.41443 | 2024-10-21 01:02:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| b940feb5-d72d-3de4-b339-185a6e3e22b4 | -17.68368 | -57.44803 | 2024-10-21 01:02:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.8 |
| ab612b66-550e-33c8-818d-0935ac9ca398 | -17.68995 | -57.40679 | 2024-10-21 01:02:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.2 |
| abdb918e-bd0f-3170-b902-32f0690892b1 | -17.7698 | -57.57047 | 2024-10-21 01:02:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.8 |
| 09d548d6-8e03-387f-b348-7bb4d4eb6aa5 | -4.6645 | -45.70255 | 2024-10-21 01:05:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| d6e2fa61-882b-3263-963e-035a89788e50 | -4.66684 | -45.71829 | 2024-10-21 01:05:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 55f1fc62-29d2-3a44-ba6d-a1d8092e594d | -4.69655 | -45.83979 | 2024-10-21 01:05:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bdbbf776-22d6-3f33-b15e-bc8eb4102f0b | -5.50488 | -50.58401 | 2024-10-21 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e8d60c2c-8ba9-31db-8218-88d305fc85bb | -5.50365 | -50.5752 | 2024-10-21 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 66072f21-bf73-3359-b745-bdc06f3bb677 | -5.49729 | -50.59409 | 2024-10-21 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9912cdc3-4169-32bb-8060-cce93be8c6e3 | -5.49606 | -50.58527 | 2024-10-21 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 2cd61466-580a-348f-8466-89c5b1bfdd88 | -5.47226 | -50.5437 | 2024-10-21 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d89fad1c-23c8-3a38-8bc6-69946498a2f4 | -5.43972 | -46.36291 | 2024-10-21 01:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 09175a95-3373-332f-a2bd-df9801716780 | -5.4377 | -46.34906 | 2024-10-21 01:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| cb0b9720-fa3d-39b9-bd45-a5ddb5157931 | -5.34536 | -45.63607 | 2024-10-21 01:05:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8866aa63-e0aa-357d-884e-a6698f00acce | -5.28001 | -49.30537 | 2024-10-21 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| aef04a9b-0639-31d8-a032-059a43f5233d | -5.27868 | -49.29604 | 2024-10-21 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 89dc2fc5-7043-3921-85a1-703820db422e | -5.23149 | -50.07542 | 2024-10-21 01:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 02f9c116-dc33-3e4d-9863-33b5b01f9872 | -5.22925 | -49.92979 | 2024-10-21 01:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6518cb0e-e84c-349c-bed5-8793e6721968 | -5.22149 | -50.00399 | 2024-10-21 01:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d4c9576b-3824-36c7-be01-19ea5a798a2a | -5.16668 | -50.72201 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 992df52e-dbc5-39ef-94d1-07b602ebd79c | -5.16546 | -50.71321 | 2024-10-21 01:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| afb0b32e-6a16-33f1-9cdb-219207926ada | -5.06244 | -49.59038 | 2024-10-21 01:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d3239646-5074-3ca8-afda-cbcdd9f7d766 | -5.05345 | -49.59164 | 2024-10-21 01:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 175aff71-ba72-3227-b7f7-4c3669dd9590 | -5.00379 | -47.66218 | 2024-10-21 01:05:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 6004c837-2e5c-3fe7-8d16-1b0f4c61e8b6 | -4.74685 | -45.79617 | 2024-10-21 01:05:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 306f98ce-3309-3e39-8102-b1006a2e416d | -5.00213 | -47.65091 | 2024-10-21 01:05:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| d6b4f91d-0cfc-37da-bb06-ec08fd76b252 | -5.00204 | -47.65672 | 2024-10-21 01:05:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| f3a6e088-7b30-3958-ab92-e5bb245bec8d | -5.00044 | -47.6454 | 2024-10-21 01:05:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 08eb985b-d6d2-31bb-a2fd-558f8057473f | -4.94945 | -44.87128 | 2024-10-21 01:05:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| a682950c-51ea-3780-a1d2-06ae226505e0 | -4.94652 | -44.8774 | 2024-10-21 01:05:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0cdc1156-cf12-3f28-9af1-d08bfd19ea2b | -4.94386 | -44.85934 | 2024-10-21 01:05:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9dbb5218-b26d-30b9-bb0f-d6e73ea67cc8 | -4.90427 | -45.84333 | 2024-10-21 01:05:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 34.7 |
| cda1d290-3102-36a1-bc27-2e24b0c6ec77 | -4.90209 | -45.82839 | 2024-10-21 01:05:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| dd77f642-6e32-39eb-9d71-8236243abaa9 | -4.89658 | -48.2804 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 38459829-8bec-3322-a355-76d623491ea0 | -4.89511 | -48.26997 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d3a9c03-8670-35c5-a7f6-2b5b35f213cd | -4.89291 | -45.84512 | 2024-10-21 01:05:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1fb6f659-92f7-3454-99dd-b5396dc48b8a | -4.89074 | -45.8303 | 2024-10-21 01:05:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 03796737-fd8a-3406-8cea-cfac7823b1f0 | -4.87814 | -48.21906 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fad2d6d2-ac66-3576-bf97-7a7b67b54098 | -4.87667 | -48.20874 | 2024-10-21 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| a175e13e-78b5-34cd-ba54-1b00723a4656 | -4.85547 | -44.35007 | 2024-10-21 01:05:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 48cdd7d3-8eb4-357b-b6ff-0d3b410201d0 | -4.8525 | -44.33015 | 2024-10-21 01:05:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 6259ad97-0c98-381d-bdb1-8609933d2e50 | -4.84088 | -46.89811 | 2024-10-21 01:05:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f90d9c35-4711-3db9-b877-ed8ed791613e | -5.69083 | -46.41635 | 2024-10-21 01:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 83dd1694-af11-354a-bc83-ae7a34801bbd | -4.16194 | -43.35906 | 2024-10-21 01:05:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 83b4ee52-5637-3206-bde2-c2e3ba3d80fe | -4.15916 | -43.36498 | 2024-10-21 01:05:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 091bd395-fffe-3e74-92cd-f5a82404bbea | -7.74604 | -49.86046 | 2024-10-21 01:05:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e021f7b9-1344-3b87-bf56-0e496a2f1f37 | -7.74479 | -49.85157 | 2024-10-21 01:05:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ccf97ba5-18a7-30d7-8498-eee1c4f09f35 | -7.7372 | -49.86174 | 2024-10-21 01:05:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 5f0e65e0-fafe-3e25-9f05-45aaf8930053 | -7.73595 | -49.85285 | 2024-10-21 01:05:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1724d36b-75ce-3a9b-8330-86f38948c766 | -7.03573 | -50.24659 | 2024-10-21 01:05:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aa3b2d76-8cad-3e38-be88-daa7cfeda655 | -7.03449 | -50.23775 | 2024-10-21 01:05:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| edbf2d48-f52b-3296-b7cf-5b43dabfb768 | -6.22198 | -50.89248 | 2024-10-21 01:05:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1581a742-c58b-3f31-ae97-e31af144e3bc | -6.20184 | -50.87726 | 2024-10-21 01:05:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 35dc3afe-44a3-3c4c-9487-f5f5ebc2f78e | -6.18307 | -50.88582 | 2024-10-21 01:05:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| df8754a8-c17f-3147-8bee-33fdd5b05632 | -6.18184 | -50.87697 | 2024-10-21 01:05:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9e86b57f-022d-3a0d-9536-f787c131364f | -5.9127 | -51.06009 | 2024-10-21 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eedf3a91-6094-3076-b02b-089595869ea1 | -5.85099 | -51.08377 | 2024-10-21 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 92c320ba-2557-3533-8e4b-f532443c2e3b | -5.69478 | -46.443 | 2024-10-21 01:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 54402cac-ef52-3b92-ac8b-7283f4152252 | -5.69285 | -46.42998 | 2024-10-21 01:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 88068aff-b238-3400-8684-f19bf8a70d2d | -5.68215 | -46.4316 | 2024-10-21 01:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| e907282f-40f4-35a4-80f2-94fb3c81ab76 | -5.5943 | -50.16245 | 2024-10-21 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c74e5dde-9591-38d2-bfe1-d1d5a8f472a6 | -5.59305 | -50.15356 | 2024-10-21 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 392aba1e-f981-387b-9cae-12ced1ad4376 | -4.83906 | -46.88565 | 2024-10-21 01:05:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 5606fde4-2b38-383c-94be-15eeb9c018b7 | -10.8253 | -58.61017 | 2024-10-21 01:05:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |


[Clique aqui para ver as próximas entradas](README10.md)
