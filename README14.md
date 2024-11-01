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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c867a2d5-6a88-3543-aec2-493e0ab8d92b | -6.87927 | -44.76705 | 2024-11-01 03:45:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcd81df7-3aae-3a00-8322-50e867649603 | -6.87512 | -44.75894 | 2024-11-01 03:45:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2211ae4-f07c-3906-9bc5-9c26433c98fb | -6.87448 | -44.7625 | 2024-11-01 03:45:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab30c852-9f2d-3b62-af31-3a94192f7ccb | -6.60825 | -47.39837 | 2024-11-01 03:45:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b86be3dc-5464-3614-933c-09a391363d32 | -6.60372 | -47.39123 | 2024-11-01 03:45:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7357f555-3aea-3a9f-9e6f-12c657a03374 | -6.60279 | -47.39173 | 2024-11-01 03:45:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e7b1e8b-1635-3f27-b45f-e2e571a9589d | -6.60275 | -47.39647 | 2024-11-01 03:45:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b5b81e3-b0ab-3b78-969b-10c4991b08e9 | -6.55355 | -47.51674 | 2024-11-01 03:45:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d724594-19e0-3057-9d65-f8347a71f60d | -6.55347 | -47.51756 | 2024-11-01 03:45:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1abf2c64-fe4a-3aa8-abcb-8b93de458948 | -6.53996 | -44.46341 | 2024-11-01 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2b04bc91-8fcd-349f-afdc-1d556425fa50 | -6.53937 | -44.4668 | 2024-11-01 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf1f713c-19f1-3500-83a3-f83a89767f61 | -6.53462 | -44.4624 | 2024-11-01 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f3551cd2-8398-37d2-813b-e161ab22c7d1 | -6.53404 | -44.46573 | 2024-11-01 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2743b52a-b952-326b-a827-1a5faf9613db | -6.53345 | -44.46906 | 2024-11-01 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 49909d68-5bfc-3e5b-9fa5-23dc969713de | -6.52872 | -44.4646 | 2024-11-01 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 057f2593-23e0-3bb5-a94d-d441d65f6509 | -6.52814 | -44.46789 | 2024-11-01 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec41817c-b413-376c-abcc-9a0c4a51817f | -6.054 | -45.79654 | 2024-11-01 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 30faee0a-1986-3255-b709-58f8e1a7fa50 | -6.05326 | -45.80071 | 2024-11-01 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c0824a56-fb5e-36a0-b151-e5881da09132 | -6.0525 | -45.80494 | 2024-11-01 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bdbbd98a-4dd8-348a-8c6b-d6d480c01473 | -6.05173 | -45.80928 | 2024-11-01 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3741851d-0d8d-34ce-90ab-062018869404 | -6.05095 | -45.8136 | 2024-11-01 03:45:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aac72362-da30-37d6-9a5b-b8314713d6c2 | -5.8677 | -44.47717 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84bd9912-a466-356a-b22f-e1b815badc69 | -5.86712 | -44.48052 | 2024-11-01 03:45:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8de3cedd-dfce-330c-97da-67f390accbd3 | -5.72855 | -44.52824 | 2024-11-01 03:45:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ccea550-66b5-3df1-b4f5-fc91f7dc61f3 | -5.59668 | -45.20848 | 2024-11-01 03:45:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| affb3c11-f1f6-3f11-baa2-92579615fc2e | -5.5947 | -45.20921 | 2024-11-01 03:45:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5ab7ccc3-9ebe-3850-a124-2f8da65085ee | -5.59099 | -45.20743 | 2024-11-01 03:45:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58594437-1b3a-368d-ac85-7dc7e1018b67 | -3.0539 | -49.4683 | 2024-11-01 03:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| e83dbaca-b3cf-393f-8041-0e9f275a0813 | -3.0538 | -49.4895 | 2024-11-01 03:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| d0efd0ef-1225-3263-8e38-6e05770fbe50 | -3.0354 | -49.4688 | 2024-11-01 03:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| a9937df3-da6b-37ed-9c48-c17dde7ac3f3 | -3.0353 | -49.4901 | 2024-11-01 03:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 373e2da2-ec0e-3e03-ad93-73615607d8d9 | -3.2417 | -53.3562 | 2024-11-01 03:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c5f6fd65-68e8-3e0b-b5b8-2136faca2512 | -3.2416 | -53.3764 | 2024-11-01 03:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 56ed3289-6723-313a-ad75-41402b7ff869 | -3.5631 | -47.3847 | 2024-11-01 03:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f52e985b-7a90-3b92-9e6c-599e8db1ab85 | -4.4056 | -43.4514 | 2024-11-01 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 413a137c-f323-37f1-ba46-df029f588262 | -4.4054 | -43.4746 | 2024-11-01 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 9c9ba3d6-d29c-34c0-a14f-4ff79a7db5ba | -4.3869 | -43.4525 | 2024-11-01 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| ca047f6c-f156-37c1-9a8e-a38d6e484f83 | -4.3867 | -43.4757 | 2024-11-01 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 4b59d6f7-d918-328b-925e-caf942fca608 | -6.1229 | -43.9578 | 2024-11-01 03:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 9c5d5464-09c3-3035-b426-1fea86abb385 | -6.1041 | -43.9593 | 2024-11-01 03:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 2e3fc9a0-4c22-359c-b57f-7245d349fa31 | -19.5063 | -56.7039 | 2024-11-01 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| e48c3723-e88d-3449-babc-0e30c6e70f5f | -19.5059 | -56.7249 | 2024-11-01 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 7f018d59-e639-3a18-b45b-94f0fe7fee9b | -20.66605 | -42.20297 | 2024-11-01 03:47:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a7aa3d2e-95e5-3e57-8720-786ad3222cda | -20.42385 | -47.59301 | 2024-11-01 03:47:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29182a35-e9d8-3d1f-91c7-32c08dfa24bf | -20.40763 | -42.15057 | 2024-11-01 03:47:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a7db095a-69d4-356a-960a-60bd2ab21d76 | -19.44621 | -48.62865 | 2024-11-01 03:47:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35a6d401-c109-3631-a046-7b2a7bdd3128 | -19.4408 | -48.62687 | 2024-11-01 03:47:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 992ef4b6-e539-3612-b73d-c93856601a0f | -23.72472 | -47.42606 | 2024-11-01 03:47:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e4fb0a3-c79e-3427-b8fd-34a439a6a515 | -23.72441 | -47.42409 | 2024-11-01 03:47:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cb63e10c-bee7-39fc-86ad-bc8db637f2f3 | -22.99881 | -49.80099 | 2024-11-01 03:47:00 | NOAA-21 | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f3566125-86da-30c7-a0a8-2bcaecb69fbc | -22.9982 | -49.79831 | 2024-11-01 03:47:00 | NOAA-21 | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| f7815358-c4e6-3e1a-8f1a-4ec61a8acbcb | -22.05748 | -52.78995 | 2024-11-01 03:47:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a882987-e2db-358c-bb43-88481d61816d | -22.0548 | -52.7879 | 2024-11-01 03:47:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ae102cec-7c7b-3d1a-8bbd-4724ae1a5268 | -22.05089 | -52.78811 | 2024-11-01 03:47:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8da824d7-e85d-3a97-a55a-622e0fc65b5f | -22.85697 | -42.98289 | 2024-11-01 03:49:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c29a1d53-4a9a-3453-83df-86f5e73ae74f | -28.58644 | -49.44148 | 2024-11-01 03:49:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7b14c5ef-a389-32c9-912b-99ee3a4b9388 | -3.0539 | -49.4683 | 2024-11-01 03:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| a30801f8-eb0d-35eb-844c-f805dbee72f8 | -3.0353 | -49.4901 | 2024-11-01 03:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 3b1c5132-b83f-3ef9-bf83-a1ca1d6e794a | -3.0354 | -49.4688 | 2024-11-01 03:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| e70adddf-5286-30ac-a769-b260fb94a524 | -3.0538 | -49.4895 | 2024-11-01 03:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 67864856-476e-36e6-b3e0-6ce3c1036641 | -3.5631 | -47.3847 | 2024-11-01 03:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| f6fdaeb4-461b-303d-8e60-853c0bc6fb46 | -4.3869 | -43.4525 | 2024-11-01 03:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 1d9a3957-71c0-37d5-8e50-3a2e868e32ea | -4.3867 | -43.4757 | 2024-11-01 03:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 4cfda4b7-3da2-33a9-8eab-e97000e054d5 | -4.4054 | -43.4746 | 2024-11-01 03:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 7b3095f7-b284-367d-8064-b66a228c7109 | -19.4859 | -56.7277 | 2024-11-01 03:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 56d3a5bc-3ef0-35db-90f0-a5617e334591 | -19.5059 | -56.7249 | 2024-11-01 03:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 8f15e2f0-da0f-3440-8e1a-2403125982e1 | -19.5063 | -56.7039 | 2024-11-01 03:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 36925c72-5cae-36eb-a84e-09677747eff6 | -19.526 | -56.7221 | 2024-11-01 03:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 42eae732-e7b3-33fe-aef1-3a1f8bd9b584 | -1.0564 | -47.63346 | 2024-11-01 04:04:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 618aba99-d603-3fc8-b30f-adc6353905dd | -1.04079 | -47.79005 | 2024-11-01 04:04:00 | NPP-375D | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 027c4a20-f518-3d56-85a2-d6059b11286e | 0.08741 | -49.86497 | 2024-11-01 04:04:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36ad2678-f1e4-3865-831b-c5a18c35e42c | -3.0353 | -49.4901 | 2024-11-01 04:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| a8fa45f0-54cb-3a8f-9e87-bc29ce701d71 | -3.0354 | -49.4688 | 2024-11-01 04:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c8646c56-6988-3ac5-b79c-53d02a9819bd | -3.0538 | -49.4895 | 2024-11-01 04:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| b1bc64b5-e2db-356e-95c0-596447aa11db | -3.0539 | -49.4683 | 2024-11-01 04:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| f5b2bdbf-b838-3d14-bb65-6f381be26678 | -3.5631 | -47.3847 | 2024-11-01 04:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c4e3efa2-b2e1-3893-ba35-4028d1ea5447 | -4.3867 | -43.4757 | 2024-11-01 04:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 0d5f1cc8-a916-35d5-b244-1d5ac6b89930 | -4.3869 | -43.4525 | 2024-11-01 04:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 137d2a8c-37c1-3cbb-93c7-80c446e47ff1 | -4.4054 | -43.4746 | 2024-11-01 04:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| e244a0fe-f868-3719-bf5a-86baca4d2416 | -5.62371 | -41.72259 | 2024-11-01 04:06:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea5d328c-46e3-3f15-bf58-c84973842489 | -5.59216 | -41.77109 | 2024-11-01 04:06:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9a1048f-67ac-3da7-8ded-11b6b77c8257 | -4.94379 | -42.57501 | 2024-11-01 04:06:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2278e03-0e85-3103-8abc-b40690718d6b | -6.28134 | -43.18871 | 2024-11-01 04:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21695b94-0702-3e72-8d73-2e9b8f071c7b | -4.64767 | -43.11794 | 2024-11-01 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f38b2d2c-bda6-3fda-b31d-3e56f40959b8 | -4.54931 | -43.09901 | 2024-11-01 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b93f5dca-327b-32a5-aec0-f51c42f2d6ba | -4.59106 | -42.79271 | 2024-11-01 04:06:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4af275a3-8fea-3fba-a1ba-721c3c965408 | -4.89198 | -43.37374 | 2024-11-01 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 555d0dc8-51b9-3b73-8b6c-ab08b709db54 | -3.88363 | -42.93412 | 2024-11-01 04:06:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8693c7bd-17a7-378a-9fef-e6488a6ff88e | -3.55765 | -42.70501 | 2024-11-01 04:06:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 204cc73a-0d04-3ad3-9964-85ba86410702 | -3.46017 | -43.18705 | 2024-11-01 04:06:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35b31fae-ce84-389e-859f-e1a6ff5860d3 | -3.29234 | -43.54118 | 2024-11-01 04:06:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bfaf6b4-d8c1-3c05-bae4-49b2925fb1b5 | -3.2917 | -43.5452 | 2024-11-01 04:06:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e69e6021-f010-3445-8d52-318f981b65c5 | -3.25142 | -43.38739 | 2024-11-01 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| baff198a-2e7d-3ffc-822a-c3705818eae3 | -7.22021 | -44.01865 | 2024-11-01 04:06:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2728a95-a44b-3646-9d05-320e72c19c59 | -6.85172 | -43.57329 | 2024-11-01 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e9cd253-6a95-332c-a047-c43102fe3c22 | -6.53745 | -43.95594 | 2024-11-01 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49ed5bd4-9a7c-3802-a819-cdf8efc0d5d0 | -6.5368 | -43.95992 | 2024-11-01 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 104c1285-1214-3c74-af0a-06d1614b9e76 | -6.5333 | -43.95929 | 2024-11-01 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 219d9c22-e99b-3693-8a88-c503ad71fcf0 | -5.56602 | -43.73843 | 2024-11-01 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4739fab9-07f9-3505-8199-f117f2a41b5b | -5.57396 | -43.57327 | 2024-11-01 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README15.md)
