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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da8defc4-c1ce-3903-adea-36b764912866 | -2.36257 | -46.80696 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b05684d6-fef4-3c73-8256-df545d432e8f | -2.25316 | -48.22293 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19d69a16-2708-3cc4-b35f-5bc4fa716f4e | -2.19611 | -49.52328 | 2024-11-09 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f154db5-77e3-3371-8c9a-f19c2b7d27ae | -2.5792 | -49.13913 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2fec6512-5d67-3966-ba23-4add1c716787 | -2.12079 | -46.37059 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 834a2d39-b101-33dd-8e1e-1a961981ada9 | -2.24745 | -46.49614 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bea5ee1-a407-384a-a08d-f5cfdccc569b | -2.51159 | -46.30705 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2d9c5e2-c426-3a48-b6bb-9ff928e504d1 | -2.65992 | -48.64667 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e25fa64-0ab1-3ee3-ad6b-4329f9428e1c | -2.07131 | -48.51177 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e755754a-fcfb-3759-85df-2303e405e744 | -1.17211 | -54.1579 | 2024-11-09 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa37402e-9e5c-33de-8ced-dada7c08f18c | -2.91228 | -46.81506 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb73ed10-174e-39d5-ba64-a35ae8bed363 | -1.18684 | -51.99245 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 951f5a7c-3bbd-36c0-9d03-987fd650b009 | -2.22026 | -48.38829 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 140ffc48-bf0c-374c-b7f2-9d447e0fca6d | -1.15051 | -53.66447 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| cff49394-10f2-3548-a18c-657219659f60 | -2.09728 | -48.89894 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f80ecd25-9009-3a33-80d9-8aef262b5f5b | -1.04579 | -52.45932 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed0a2d66-5d7c-35bc-b091-a2a106100951 | -3.13734 | -45.95417 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bb25e6f-962e-315b-a4c5-78c932a3049e | -1.87929 | -50.9725 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5a0cc2a-4b95-353e-b3c6-d1a7954acf9b | -2.21569 | -46.41702 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81a8b959-b3a1-3a55-8d14-b9429899331d | -2.29452 | -46.50058 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0e90cd6-7f78-3a53-bfb0-9c59e110b22a | -2.28953 | -48.55249 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5526d0f5-f270-37d0-9d46-6ba4039d1bba | -2.51411 | -46.37843 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 139c527b-40db-318e-b8cf-1c59ff4995ff | -1.22851 | -51.76026 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3da5ae12-f8db-3c06-8cbf-1ca0e4f29dd5 | -2.1941 | -46.77324 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66723234-5568-3ae4-9c8c-0445850d00e5 | -1.51501 | -52.18491 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1866bd0a-4b01-3ba7-84c5-2ed643e071ba | -2.23271 | -49.28983 | 2024-11-09 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0016897c-4fa8-313d-9f9d-8994ad396ec4 | -2.52646 | -46.29859 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d122391-612b-36b2-b1f6-bbbfd0bb12f7 | -2.54402 | -47.12654 | 2024-11-09 04:31:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12deb8a4-0b01-3cb2-bb54-52669ef634a5 | -2.6333 | -46.79241 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c97ce455-5c30-32c4-821c-62220422785f | -2.56445 | -46.53496 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e71f5b78-d80a-3160-9b7b-e05e3bba6123 | -1.14592 | -53.66019 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f53352fc-d91c-3c92-add2-4e86b8b85696 | -2.39933 | -46.78801 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 984ab01b-ef6b-3594-b7cc-1976d94617e7 | -2.68208 | -46.78658 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52077800-a649-3f48-a9bf-a70ceb70f2c6 | -2.42698 | -46.30471 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0634c4d4-e8e7-30b4-8138-ec3e1e4daa8e | -1.15052 | -53.66062 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b11f1539-8a53-30af-bf3a-fbd0b9e09dde | -2.29346 | -48.54943 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4878ed58-4301-34f3-a1d8-c560e5adc9c3 | -2.20349 | -48.36388 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 164fa1c5-b366-313f-a1b7-65fdcf79e197 | -2.50868 | -47.35293 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90e6ab4f-ab5a-3773-9d45-13404b74fa60 | -2.30945 | -50.66181 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7003662-39e9-348a-bf02-82154a5c01e7 | -1.32298 | -54.64076 | 2024-11-09 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d4de3325-062a-3efc-9484-e6e687c42cb6 | -2.61002 | -48.33635 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 929828e5-af18-3fa1-a61c-eb6c968965f4 | -2.22418 | -48.38526 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70e1b954-38c9-38f3-8393-3505d6a71ceb | -1.98787 | -48.11656 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85e0ed36-3df1-392e-8325-d7d8241260fb | -2.10662 | -50.66508 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9c951b8-4200-3654-98c8-43acf11da225 | -2.81252 | -46.64795 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81a6ab4d-e61e-3490-a62d-13d562f14d84 | -2.50856 | -47.46196 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01768d32-ace2-38ce-bbca-caebdffdea3a | -2.38943 | -46.78649 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef8cc7cf-041d-3eac-89e1-9da65318b30c | -2.66331 | -46.73014 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae49dd0d-70b2-3bce-b6ec-a306e9b6b841 | -2.68368 | -46.77626 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e2cff41-8876-37b2-98ba-beca9872141c | 0.84688 | -50.16888 | 2024-11-09 04:31:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d01f54c0-a50e-3c15-bbd7-78808b663b7c | -2.57633 | -46.17424 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 829c3d87-cc5b-3d2e-8261-e8f102d481b5 | -1.5939 | -52.18579 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b075ab9-de46-3117-b178-6fa18a021251 | 1.08314 | -51.30397 | 2024-11-09 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6a2b13b-567c-3557-8939-9f7a444f344d | -2.08618 | -46.52783 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8958ff6f-475d-3e56-b79c-8fef33c5cc54 | -2.47013 | -46.87981 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1de2351c-0bfb-3ef3-80bc-6764cb296a28 | -2.65139 | -49.23834 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00244dba-b5f5-3565-9334-c5ccba886af1 | -2.01764 | -48.01333 | 2024-11-09 04:31:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e042a98-baf8-3f07-a6cb-02ce550f9518 | -2.17113 | -46.44201 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a49a4c3-24bb-3752-804f-8d3ea4373d17 | -2.8423 | -46.65253 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13309731-c243-3dc4-912b-b5c221b3b1b7 | -2.44914 | -46.31523 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 504df03d-22c7-398c-a83c-3b91d0333b65 | -2.21016 | -46.8003 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f91f16fa-a28e-3771-acb1-72409ba16498 | 3.35565 | -51.27322 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a7f301d-48d8-369e-884c-deec014cb336 | -1.16966 | -54.15428 | 2024-11-09 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfc4d782-e5f2-300e-beb1-1bcf40ec2ced | -2.23 | -46.54288 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 808ca160-d805-38a1-ae89-fdef212e853e | -2.28448 | -46.71758 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83067987-388e-3e6f-9a67-2748bf919474 | -2.70303 | -46.67351 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c99f0d8-ee96-336d-9911-a065c06197da | -3.5481 | -43.57075 | 2024-11-09 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e120aa7-faab-3bdb-a4ac-07ffa981f5d3 | -3.09405 | -45.88535 | 2024-11-09 04:31:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0960701a-5235-3881-bb4c-d47c89d9d51c | -2.28674 | -46.85503 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dadf925b-6929-3f7b-9b45-80850c5fdda5 | -2.18626 | -46.86688 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02b7fe0f-9ce2-3815-b6ea-7d09dc884a7b | -2.13924 | -48.38683 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56fe4390-64f8-3582-a021-3499e04bc023 | -2.81428 | -48.46626 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca171f56-ddf4-39e2-96b5-098f71db2c5c | -3.12057 | -45.9516 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 138e9423-ecd2-36a4-b325-d555ed6549e8 | -2.13596 | -46.69045 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25bc5411-ef53-392e-b078-3db0d30c1bb1 | -2.30941 | -46.01098 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 003be144-0729-34e8-9c33-b649504b2019 | -1.68672 | -51.91837 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a0124d4-95f7-35bc-bd1a-f09f04038a75 | -1.69475 | -51.91963 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f09f2c1-937a-3cf0-a9e0-70278b90926c | -2.56776 | -46.53547 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f70572b7-cbb1-366a-97b1-daa02ba19103 | -2.2966 | -46.18084 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a04b861-74b1-3af0-96a0-edd77620fdfb | -2.57578 | -49.13861 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f96d7e8-d96d-3b30-b514-eabfd301292b | -2.08755 | -46.34424 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0633177-66d3-3370-8714-e8eac19bc4f7 | -2.19672 | -49.51941 | 2024-11-09 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59bf0b53-9228-31da-af84-7854ca7a3fa6 | -2.31046 | -46.7462 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| beb7bb01-3f23-3f56-938a-ac4e8b6b7425 | -1.73515 | -46.0943 | 2024-11-09 04:31:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e88b6b2-0dcf-32cf-97f2-a4c9b11e8986 | -2.1761 | -48.32701 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55ff6a4a-7f17-337f-8baa-3bf05089dbe9 | -2.83666 | -46.62338 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2053f46-046a-351c-bc31-b6ef07e17811 | -2.51821 | -46.30799 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 487f2fba-56cf-3594-b9ce-68861b59dff6 | -2.28335 | -48.54787 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 598aa02a-84dd-3801-bc57-42da79640c40 | -2.30707 | -46.72457 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c111479-30a9-38fc-9c83-9e3b4caf0677 | -2.29853 | -48.5392 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c6ea354-2d64-37b8-95d4-ebafa6f8a47e | -2.29623 | -49.10759 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d150a181-9fef-3416-bf59-5072a4113fd0 | -0.91265 | -51.66018 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89556f79-6521-3fd5-9c81-1c485b1d1577 | -2.02764 | -48.01487 | 2024-11-09 04:31:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95f5dc97-f9c7-38a3-af4d-42dd83c2215e | -1.05462 | -51.7463 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32cc592f-e0f6-32af-a6f0-7cb9a6bbba04 | -2.09488 | -49.52019 | 2024-11-09 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53c19a2a-9be6-3154-aba8-566494badecf | -2.27201 | -50.68284 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c239b8b-01af-3cf0-8792-2992080c81c8 | -2.54293 | -47.52361 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ef3c09c-8e50-3dc8-ac39-418199d2051a | -2.15078 | -46.68217 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4398b8c7-27aa-3acd-a68c-64f8ef3839b1 | 0.04428 | -49.52022 | 2024-11-09 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b5e9dd3-ef52-38fd-b73c-026c64031c28 | -1.10608 | -46.50857 | 2024-11-09 04:31:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README35.md)
