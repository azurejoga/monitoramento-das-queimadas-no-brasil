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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bfa5f82-7756-3428-8608-33f4b1712a32 | -6.1606 | -48.0507 | 2025-07-07 04:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 70efe5b6-278b-3fd5-bf1d-5f360dd7f332 | -6.1792 | -48.0494 | 2025-07-07 04:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 099413b0-afe0-3f1d-b9b3-e9a6ae88d82d | -6.1604 | -48.0724 | 2025-07-07 04:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 5413912d-52f8-3dd6-a19c-6c6aa13b4a20 | -6.1791 | -48.0712 | 2025-07-07 04:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 6302124c-1fb2-3298-a50f-8c81632c47e5 | -7.6938 | -44.578 | 2025-07-07 04:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| d84b6b44-9177-331d-9c07-43b6edf8a424 | -6.1606 | -48.0507 | 2025-07-07 04:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| d9db8ba2-7663-3f3a-973a-59e2de5fe3a5 | -6.1792 | -48.0494 | 2025-07-07 04:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 633d2e8f-4801-3c87-a487-9d194a0752e0 | -7.6938 | -44.578 | 2025-07-07 04:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 31ff0729-20a3-3c56-8583-67bdff8feb99 | -6.1791 | -48.0712 | 2025-07-07 04:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 5991bf1e-592f-377b-bd4a-734d1046cb47 | -6.1792 | -48.0494 | 2025-07-07 04:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4bc6b171-4785-3207-982a-901364d11d7d | -6.1604 | -48.0724 | 2025-07-07 04:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 3d31c6e4-c9bc-34d8-ac3b-d66676bb4e3e | -6.1606 | -48.0507 | 2025-07-07 04:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5270f87b-6115-391d-8ba4-711ed76f46f4 | -6.1722 | -48.05371 | 2025-07-07 04:32:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 5e4088eb-4aff-33b0-b21d-ee82b2971df4 | -5.41168 | -49.08013 | 2025-07-07 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ca60a39-523a-34af-a62c-6c06cab0a70f | -6.17496 | -48.05767 | 2025-07-07 04:32:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 0aefc101-4e54-3b50-acc7-d2d5ed599b23 | -5.60179 | -45.17454 | 2025-07-07 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aea6ec13-7b3d-3cfc-8412-360adce42eec | -5.22471 | -46.02824 | 2025-07-07 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 104aea29-1fa8-3af2-8920-644487bb9063 | -3.9282 | -43.16517 | 2025-07-07 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9be2506-2f22-3267-a12c-58c322e4b6e6 | -2.91232 | -48.24871 | 2025-07-07 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b24d7f1-b737-3040-a87a-13b24f429e33 | -6.16835 | -48.05664 | 2025-07-07 04:32:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 53f52f95-a87e-3faf-8237-2ce651ecc022 | -6.76079 | -43.06746 | 2025-07-07 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84e0b92e-f8da-3472-95f0-ee6832383e4c | -5.56587 | -45.22134 | 2025-07-07 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3fb95c9c-ecc5-36f0-9c2c-5ef1f752bdb7 | -3.92436 | -43.16459 | 2025-07-07 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e8d19dc-ad93-3035-88f6-eb219054ccb5 | -4.82629 | -45.19841 | 2025-07-07 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef1a1ffe-f3d9-3e0a-ac5d-d91890cf74c5 | -5.04443 | -42.73619 | 2025-07-07 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71f06cd3-8346-3aa9-892a-c62f53c933e5 | -7.31307 | -43.87624 | 2025-07-07 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e527a163-3205-3b92-a528-69407abc8f84 | 0.6922 | -51.46117 | 2025-07-07 04:32:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4b05f1b-06ec-3c2c-885b-420e9b9b850c | -5.71643 | -42.23076 | 2025-07-07 04:32:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 32382b73-7546-3045-82e5-e2b5916feef4 | -6.87501 | -42.79779 | 2025-07-07 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b676af19-81a0-3f6d-9d30-ba8722d4f3df | -4.82569 | -45.20226 | 2025-07-07 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cd6fbc6-30c4-359d-8039-2c21f1607d12 | -5.71565 | -42.22717 | 2025-07-07 04:32:00 | NOAA-21 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0a6f258b-f939-3d87-b0f6-ea538ec1ba64 | -4.81786 | -44.35336 | 2025-07-07 04:32:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66bde087-f075-3f1e-80a1-4634ea76b138 | -6.6919 | -43.14694 | 2025-07-07 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8ab7729-5e89-3df7-9c24-fe6f6f058c8a | -3.92052 | -43.16399 | 2025-07-07 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b42b8c00-3b0b-3905-8db6-61c7032ab5a3 | -4.10907 | -48.21154 | 2025-07-07 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1257231-ecd6-31e1-b4e9-4fb96f5cadc5 | -5.56647 | -45.21742 | 2025-07-07 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 31aa2094-e548-3678-a8d5-c11fdd8886c1 | -7.31517 | -43.8748 | 2025-07-07 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd3f79a7-c7ff-35dd-a9fc-c2dd4eaaf2bd | -6.64105 | -43.17227 | 2025-07-07 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d63cb8a4-9af0-3cd6-9dd9-3e421f73a034 | -4.28611 | -48.18998 | 2025-07-07 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8f72f77-0f2a-35a2-bb1b-527b4a7fb9fa | -7.09728 | -44.16732 | 2025-07-07 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68b264fd-0470-37ad-975f-ebebd6ca5402 | -6.16781 | -48.06009 | 2025-07-07 04:32:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ac1471da-5fd3-342e-bfe4-9144cf38fbce | -6.6959 | -43.1475 | 2025-07-07 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3d98749-8a45-301f-ad06-df39b3db5093 | -5.705 | -42.24117 | 2025-07-07 04:32:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fd77fdbe-4e5e-32fe-bf9b-b454d01a5aa3 | -5.55585 | -41.26608 | 2025-07-07 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9748a57e-d06f-3894-b638-1902b5f35598 | -6.70779 | -47.80238 | 2025-07-07 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5ff49418-e1f9-3fdf-b26a-3492dc560883 | -6.16889 | -48.0532 | 2025-07-07 04:32:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| aca33e14-67c7-366f-adbd-441bc3a6de66 | -7.09466 | -43.21326 | 2025-07-07 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 78ebbd4c-2bc7-3b6c-bea5-768af9ef50f3 | -2.63481 | -47.30533 | 2025-07-07 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6cbf958-ca7e-3023-b7c1-6d8dd0b8a0a3 | -6.69239 | -43.14346 | 2025-07-07 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df0b6071-8153-362b-b97c-fd7036a9cd3a | -7.0562 | -43.84122 | 2025-07-07 04:32:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52e56356-50f0-3b3c-9c37-589a6a6706a1 | -4.2828 | -48.18946 | 2025-07-07 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a1b6099-a3b0-3dc8-8d1d-ab4fbe9dcc63 | -6.17166 | -48.05716 | 2025-07-07 04:32:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| d4b5611e-61fc-3716-8a9d-52e96e21defa | -6.71056 | -47.80635 | 2025-07-07 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 365c9dce-9489-3784-9331-504309aba524 | -6.26497 | -45.2698 | 2025-07-07 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61a9320b-0104-31dc-9fe8-b0e4ca96588c | -5.14197 | -48.88824 | 2025-07-07 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46d84e88-b31b-3a7d-8a86-48e1a677779d | -6.16505 | -48.05613 | 2025-07-07 04:32:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 9cc72fcb-fcd5-3fea-9090-fe0aa0e0d4ee | -4.73039 | -47.21937 | 2025-07-07 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fad22ac-140f-3329-898e-b0f8e5aaf89d | -6.94054 | -43.03653 | 2025-07-07 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce4075b4-a698-3fd0-a5f1-fde99d4f7d39 | -3.92748 | -43.16991 | 2025-07-07 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38116cc7-8509-32ba-8a70-a7e5ebe93c6a | -6.98669 | -44.2873 | 2025-07-07 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7487c2ce-9c65-33df-9dc1-54672f797a79 | -5.60591 | -45.17114 | 2025-07-07 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ea716e3-abbf-36f0-ad19-26fac4142aa1 | -6.64156 | -43.16883 | 2025-07-07 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b3534a4-0b51-3e9e-985c-0085cd64e91f | -6.87858 | -42.80209 | 2025-07-07 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4c5143b5-a690-374e-a33d-d8951adc04f1 | -6.10553 | -49.38059 | 2025-07-07 04:32:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f585589-3031-35f5-b446-9db34d4b22f0 | -4.01174 | -47.96591 | 2025-07-07 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee503fd7-1cb0-373a-9103-72443d2c39f9 | -3.8633 | -50.08286 | 2025-07-07 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ebee81c-f19f-3ec5-b157-c1cad7352824 | -4.82977 | -45.19894 | 2025-07-07 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1dbc4f2-6622-3a5e-825a-da6d5262ea54 | -6.71109 | -47.80289 | 2025-07-07 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 8ba965c5-733e-3cc6-bf81-adc419460197 | -7.09416 | -43.21677 | 2025-07-07 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e176c306-68c7-3805-8528-bea40da22c9d | -4.82918 | -45.20281 | 2025-07-07 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e6c5b22-c1e3-3085-b5c4-a4a45c9832b9 | -3.35743 | -49.79474 | 2025-07-07 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9324b65-59bf-3b43-8a4d-33cb8387690c | -6.6994 | -43.15149 | 2025-07-07 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4ce7178c-2024-36b9-9a79-4e62ae845c17 | -4.82149 | -44.35392 | 2025-07-07 04:32:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f276df81-df3f-3893-982e-67a6781a167b | -4.44108 | -47.984 | 2025-07-07 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dfc9fb9-a2ad-3903-888b-4b2dc027ff97 | -6.70725 | -47.80583 | 2025-07-07 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| be17c1aa-77cb-32cd-bfbc-b59e22e94db3 | -6.68839 | -43.1429 | 2025-07-07 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69f658c1-d848-3e35-a6db-addd06cddfed | -6.95412 | -42.70695 | 2025-07-07 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6a4264e-aa61-39a1-9aae-95df0490c644 | -6.56986 | -43.03312 | 2025-07-07 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eaafb337-2fcc-3821-b87b-a30efde5f2cc | -6.17442 | -48.06112 | 2025-07-07 04:32:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 2b8eb187-1cbc-36a7-8e22-f711f92807b6 | -4.24898 | -48.20897 | 2025-07-07 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f308b6e-0d9b-3984-bc3b-4c98cefde7f0 | -5.70973 | -42.23812 | 2025-07-07 04:32:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| abb82cc5-33db-39ab-92fc-dc59c834c932 | -4.81727 | -47.31745 | 2025-07-07 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0c8e44d-7004-37db-b573-7820a986adee | -5.7086 | -42.24571 | 2025-07-07 04:32:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| af3a0ac3-f2c9-32fd-8b43-6bad93dc0e56 | -2.63811 | -47.30584 | 2025-07-07 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2da4838c-d3df-346e-b133-0c683d9913fb | -5.87456 | -50.14647 | 2025-07-07 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03a680b6-4251-3fbc-a2a1-9b04226cec9b | -6.28694 | -43.61919 | 2025-07-07 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14ec5340-ac4c-38de-ba8b-1dca292df622 | -4.0368 | -48.06528 | 2025-07-07 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d23f512-6fea-3b81-9b29-1e9badc85dde | -6.92332 | -42.7827 | 2025-07-07 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6d82b0e6-9f67-3f3c-95fb-412fea1fe494 | -2.18884 | -46.56734 | 2025-07-07 04:32:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e69f8b5-76c8-3722-849e-61eb12fe1fdd | -6.95465 | -42.70316 | 2025-07-07 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 82473e65-b890-384a-b02f-640d3dc76529 | -6.87092 | -42.79712 | 2025-07-07 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a118026b-0b14-3514-b494-0bcb18908146 | -6.75678 | -43.06681 | 2025-07-07 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7496c679-3d93-32f6-8df3-7c178e3b002f | -6.17112 | -48.0606 | 2025-07-07 04:32:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 79c45dfc-599f-3053-ad8a-9a88389576ce | -7.16594 | -44.0691 | 2025-07-07 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30743d8a-6b99-38f3-965a-6d8c2d151975 | -6.94907 | -43.23162 | 2025-07-07 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 86839aef-b7a5-318f-9809-150f38a31941 | -5.41738 | -47.57059 | 2025-07-07 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb9e9f7c-b963-3e82-a9de-987d3886ce5f | -6.86331 | -44.07294 | 2025-07-07 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 894e3e06-5d71-3457-8466-997affcc0710 | -13.07401 | -48.89576 | 2025-07-07 04:34:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2e48925-d23c-39a8-bd7b-0fa14958ea0b | -8.06489 | -43.11507 | 2025-07-07 04:34:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 289c0794-bde9-317e-a765-ad20a5177ef8 | -9.79933 | -53.2332 | 2025-07-07 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
