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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a4d7533-23fb-3748-8b8d-f6fd30ddce99 | -10.7614 | -46.9529 | 2026-05-30 02:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 1f4b4c1b-77e1-3406-bd8f-eb3510c806cd | -10.7607 | -46.9976 | 2026-05-30 02:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 712cf178-5bf7-32f6-bff2-7665c9edadf6 | -10.8375 | -46.9434 | 2026-05-30 02:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| fc6a0e0c-8224-3f33-a044-4d0388c03c44 | -10.761 | -46.9753 | 2026-05-30 02:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| a0474e5f-6fa6-3c9d-b3f5-f377cdbbd08c | -10.8379 | -46.921 | 2026-05-30 02:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c780fa84-27e8-31a5-9989-8a3793f6f285 | -10.7804 | -46.9505 | 2026-05-30 02:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 6465bc9c-47c1-3b42-b10b-92794ea2d1ad | -10.761 | -46.9753 | 2026-05-30 02:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 8550fb9c-b6c7-3f8d-b155-447d7746b7c3 | -10.8375 | -46.9434 | 2026-05-30 02:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| aaf7cacc-29b5-3fef-80ea-47c7cc76f3d5 | -10.7614 | -46.9529 | 2026-05-30 02:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 5011e80f-d922-35a4-91a3-b58fa4bbb5b3 | -10.8379 | -46.921 | 2026-05-30 02:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 82650057-3853-302f-878e-be4770503be5 | -10.7607 | -46.9976 | 2026-05-30 02:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 6cb2061b-4983-3108-ae96-c7b42e757892 | -10.7804 | -46.9505 | 2026-05-30 02:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| fc050478-9e97-3632-a789-0ce3e258163d | -10.8375 | -46.9434 | 2026-05-30 03:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6312cd28-ab79-3504-8657-3d769c3da58f | -10.8375 | -46.9434 | 2026-05-30 03:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c5341753-1195-3667-8902-6c7343a32458 | -10.7614 | -46.9529 | 2026-05-30 03:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 9af23744-4188-3d17-811a-5ea8bd771a92 | -7.33561 | -49.85019 | 2026-05-30 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72219466-0e9f-3b87-b152-6e42c47112d6 | -7.63738 | -47.30809 | 2026-05-30 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0497363d-f816-39f3-bccf-8abd2dc4d62e | -10.77469 | -46.96974 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2b674cf-8178-3a2b-a81b-4f737ca5ef32 | -9.15955 | -46.85011 | 2026-05-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ddbcd7ec-a211-3d7f-a428-d611d6cea6be | -10.7689 | -46.97735 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b51a3576-db07-3820-9e1d-3e5e8fbb6e8d | -9.83323 | -39.43001 | 2026-05-30 04:02:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8a6d6c7f-d824-3761-87ed-7649dd9a9758 | -9.16392 | -46.85094 | 2026-05-30 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 22149a12-3130-33b9-8d79-0e13910b6e69 | -10.80565 | -46.94505 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf863582-5cfd-3858-961b-99cc56cedab9 | -6.99648 | -42.87798 | 2026-05-30 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| f39c892f-11d7-3b7e-9f4c-abc7d1609469 | -10.77509 | -46.91798 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9798d97c-f806-3da6-9416-ca242b05fcea | -10.78209 | -46.92831 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9d9248e-7c82-3e27-b761-0f75d63882f6 | -10.63375 | -48.3237 | 2026-05-30 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 917d2b14-9168-3a20-8b90-5820e6598e17 | -10.76253 | -46.96337 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e53ce81a-897b-3e88-8132-db964f7dd9c7 | -8.03272 | -46.58458 | 2026-05-30 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a72511ca-f83f-3deb-845d-81b84eeb3e3c | -10.76126 | -46.94577 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fd4e3ef3-ebcd-3772-87c2-491386137064 | -9.40166 | -48.45449 | 2026-05-30 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 840c6d7e-1852-3fef-8c75-7179ae02fe74 | -10.77319 | -46.97813 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 24db6d71-9ee8-3a13-abe7-949eafe395da | -9.45457 | -51.82733 | 2026-05-30 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d95d465f-7fbe-37cc-a986-f2a4c84140fa | -10.98147 | -45.10073 | 2026-05-30 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ed431af-2fd5-3b29-900a-2c9a4b52f124 | -9.9237 | -48.00599 | 2026-05-30 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fb517da-36ef-3077-9949-d70ce6b94aeb | -9.80355 | -48.92638 | 2026-05-30 04:02:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0050fff-c3e4-3dc5-8a85-0dc903851c1e | -10.76835 | -46.95564 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b7c7e3d3-bd74-31f0-a7cb-70061d98a8b0 | -10.76051 | -46.94995 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1b2b68ae-20f7-305f-9eed-f0ecec4fba4a | -8.01953 | -46.58247 | 2026-05-30 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 243c1d74-db42-3a08-ac4f-87afed7cbcbb | -10.7812 | -46.95808 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5329ca52-e2ad-35b1-a3f6-d11196e704fe | -8.7276 | -47.82772 | 2026-05-30 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1877d891-9884-392e-8844-3a3f98e4ba75 | -10.81699 | -46.95604 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0590db1b-a7d0-348f-bb7b-8c49393dab7c | -9.39933 | -48.45595 | 2026-05-30 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ae9f5b5-1ab7-3117-af47-f0ed94f16aa2 | -10.79405 | -46.96057 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32c71a68-5a39-3976-9e07-4512f2bddbac | -7.63826 | -47.30319 | 2026-05-30 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e28735f8-5d63-334c-afca-b2512e7f2e28 | -10.84568 | -46.91829 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f0c2145-cd08-3107-b5db-1d5480f76d08 | -10.80417 | -46.95345 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35459058-5e3b-3baf-a567-d9c0d839bf55 | -10.76102 | -46.97177 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34cddb93-2ff4-362e-a8d5-44748490a8aa | -10.76555 | -46.94653 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bdc3269-e988-3a32-be51-31fbb165637d | -10.81584 | -46.88732 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2772a0d3-5cbb-3a8c-8388-8bca1d0ff295 | -10.8151 | -46.89149 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 06253179-4763-30b6-bfbb-b786172a5a78 | -9.26684 | -40.67438 | 2026-05-30 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a8d63767-c110-39b8-b8ab-9225ced809a5 | -8.02393 | -46.58318 | 2026-05-30 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 763b388f-fb98-3351-848e-f337f86f260d | -10.78284 | -46.9241 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce35e848-20dd-3699-8297-f9210e8e1ed2 | -10.84214 | -46.91331 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a216b5f-924a-3e68-91ca-c00258c11b11 | -6.75738 | -45.01345 | 2026-05-30 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8df7bb67-7e4b-3fc9-8154-1c7f3388ab62 | -10.84283 | -46.93469 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3331a85-4ea1-3889-9249-b6f67951f24b | -10.62705 | -48.32575 | 2026-05-30 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 05fe328f-b39c-3b75-a233-9ebc8f83f9e8 | -10.79331 | -46.96477 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d83046b2-cd24-3af0-b9fd-c392bede0ad7 | -10.73765 | -37.38182 | 2026-05-30 04:02:00 | NOAA-21 | ITABAIANA | SERGIPE | Brasil | 2802908 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2e889ca5-bd10-3452-a531-fa6fbd4b2acd | -10.76405 | -46.95488 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9bf477f-e69d-3fdc-ad2c-e5360d73e338 | -9.37435 | -50.54583 | 2026-05-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db7b1f85-696d-3b90-87e4-de45d47c694a | -9.36876 | -50.5448 | 2026-05-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00a12c33-e49c-398e-b2f5-8340ef7890cf | -5.28948 | -43.96106 | 2026-05-30 04:02:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47a1051f-f2ba-3c0d-9045-e037ba720fe0 | -10.76684 | -46.96405 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6d8348e1-b1ae-3a22-91c2-81cdce4b54e8 | -10.76027 | -46.97595 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5e53f62-c0cb-3d4e-a6ae-4189937772c9 | -6.99582 | -42.88202 | 2026-05-30 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d6e95d5e-fa55-3cac-86b9-e0c006a3332f | -10.78415 | -46.94154 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e700530-d120-3425-80ce-ae0a371fb773 | -10.76587 | -46.99428 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 210287a0-c521-3419-a8b8-7dbe39b4fdae | -10.76984 | -46.9473 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb3d6fb2-50bd-352d-ae3e-a9c0b53e4d39 | -10.7663 | -46.94237 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee22a52c-e80c-374d-b0ad-fabf6ba0159e | -10.78195 | -46.95391 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3399e500-a7c5-307e-8796-ed70510f531b | -5.95048 | -43.48635 | 2026-05-30 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2328bb9-596e-32fa-a342-8914a0662776 | -9.4443 | -40.52101 | 2026-05-30 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6dc29bce-f523-3edb-b077-967e13771e83 | -9.44851 | -51.82625 | 2026-05-30 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| faf4e28d-7e63-346a-9de2-3fa8caf38b85 | -10.62809 | -48.32796 | 2026-05-30 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ad7ad7ed-dae7-3496-9e95-ad6eb0d6c482 | -7.3343 | -49.85742 | 2026-05-30 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f04f1c9-df71-3f84-a557-ab26e6b41133 | -10.77693 | -46.95721 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ff679db-592d-30d4-815e-f92f6c84b19f | -7.33919 | -49.86197 | 2026-05-30 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7bd552cc-ee60-3901-92ee-dc11fbf70d6e | -7.84555 | -46.25548 | 2026-05-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ec22d2b-857d-370b-a687-883629907275 | -10.76813 | -46.98161 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a8b8cce-ba68-3ba6-ad7b-f789a17feb40 | -9.50202 | -40.3024 | 2026-05-30 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f4ed708d-2475-3597-b419-399bed29092e | -10.76853 | -46.92993 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bb8e98d-53cb-305a-b9ef-319c92fbda4b | -10.83857 | -46.90849 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 906a75bc-6be8-38e7-bda5-f224a099d067 | -10.84067 | -46.94712 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f3ee14e-dfbe-3cb6-90eb-e27c4e231de4 | -10.84212 | -46.93877 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9fc6f25-8298-3c35-89be-49733ba5b730 | -7.84054 | -46.2588 | 2026-05-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d39114e0-a319-30c8-aecf-ed4a0e74e8e8 | -7.63917 | -47.30607 | 2026-05-30 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6eaab266-c9ee-326a-a389-adcb544cf58c | -10.76201 | -46.94159 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 79d45095-e73c-3fa6-911c-19c31665a372 | -7.33496 | -49.85379 | 2026-05-30 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42368d41-22d8-33d0-b595-5b7c3660d18e | -10.62903 | -48.32283 | 2026-05-30 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b22aa881-02cc-359c-9092-6eb17ed72ccf | -9.16828 | -46.85181 | 2026-05-30 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1dead48b-a947-3f31-a899-53ae1cd63f7c | -8.40757 | -49.60965 | 2026-05-30 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 583883e2-8ae2-3b11-8948-ed5d38d9d7c4 | -9.50148 | -40.30588 | 2026-05-30 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 4aa0ac7c-14fe-3ef8-a7ad-b258e488bf0d | -9.92529 | -48.68658 | 2026-05-30 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c564c5e4-ca42-3eb9-a6e5-363db818ea04 | -8.72582 | -47.8379 | 2026-05-30 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9b94a8ab-65a8-3a28-aaea-1605bee3eaf0 | -5.29413 | -43.95689 | 2026-05-30 04:02:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55c90ef1-46b7-3487-a668-eb321d82f748 | -6.75334 | -45.01283 | 2026-05-30 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74ed6eae-2ef9-3d10-821f-98127f2f7e07 | -10.77767 | -46.95304 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7e042ca-1705-3fbe-b955-23136a81fbd8 | -10.76661 | -46.9901 | 2026-05-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README3.md)
