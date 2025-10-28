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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94f01275-0357-3709-914d-f871adab2f6f | -10.93233 | -50.26207 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3acebf56-35cd-3b67-a818-79b770c7b685 | -10.89329 | -48.39445 | 2025-10-28 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 046c5114-7256-3f4c-ae6a-670000b4034d | -9.26465 | -45.57033 | 2025-10-28 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6710ae5-eafd-3608-9e92-8cc6d9618c2f | -10.98287 | -50.35339 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c75fc59-51bd-3256-a43b-17f8246be5ad | -10.55969 | -49.79516 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bdb57b8-3159-3d16-80db-891e0182563e | -9.06197 | -46.94525 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43b66795-ab63-3968-b25f-b6f690983fa5 | -9.22525 | -48.60131 | 2025-10-28 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11e1a55f-628c-3cc7-ba66-9128ca7879d9 | -9.95769 | -47.08998 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83828b31-dcc9-3e02-98a7-ecd2cbfd3c75 | -12.6994 | -46.32398 | 2025-10-28 05:04:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e11a2e8e-3a85-3bc2-acad-df3c52a70876 | -7.85893 | -46.39922 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6d59a54-ebb4-38ef-9570-ccfb652c84b0 | -7.40505 | -47.7771 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 78832f05-8d9d-35b5-910f-433bb09cc240 | -10.56116 | -49.81899 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15d75c04-f152-389d-9e2e-0ee06c6f4a07 | -9.14107 | -51.29602 | 2025-10-28 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c028c4e6-1ab3-3fc1-a001-fb855770745e | -9.22172 | -46.36374 | 2025-10-28 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d452df82-02c6-3789-8928-b3a0c910f3a8 | -9.97184 | -47.16702 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee556dbb-c15a-39cf-a9be-6baa8e4fc910 | -9.54232 | -46.95992 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54e788a0-963e-331e-912f-cf2737b66528 | -6.63411 | -47.19925 | 2025-10-28 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad815e03-9b32-3e99-a10e-b3ef035b7818 | -10.56191 | -49.83617 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 14f65a2f-1061-39cb-bbb9-d729d5e3c0a3 | -9.46412 | -46.88094 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f9ff9b12-fe9e-347c-ba66-56de4d4b8575 | -7.27206 | -44.97151 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8f5b244-77fa-3040-a09b-1c71a50b4547 | -13.65444 | -47.6402 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62ec2572-7f06-31c2-b0c3-b4e7e88d15ff | -10.6877 | -48.02808 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8787eca-d59b-3c71-a113-c2db0e4fafba | -12.62982 | -45.08733 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 207d8a5f-c78f-3fd7-9d8e-e5499e516482 | -8.63973 | -45.28447 | 2025-10-28 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8bc7ab20-6a10-3dfc-ac8f-6c42890116e4 | -7.94379 | -45.49902 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a39fbf08-84b5-3235-a4d8-a08ebd648e04 | -10.3026 | -47.1707 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 250359e9-a88b-39c6-b62a-7e0d29aa9a7d | -10.36127 | -47.14303 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af2e817a-fed0-3ea7-9d7d-fb7e8ad36ef4 | -9.53886 | -46.94449 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35bdf7b9-42f7-31e3-a314-daa05f12c3a1 | -10.91986 | -50.25723 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 582d9b74-cadf-3afe-b092-1dd4d14e9e22 | -9.97809 | -47.16098 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71ca8e87-22a4-35bd-9eb5-1f39930dc046 | -8.1607 | -47.00912 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b695379-341d-378f-82fc-b0e02d1eff2a | -13.37382 | -47.40702 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d968f26-0ae0-3914-afaa-647045097b1f | -10.21891 | -49.89913 | 2025-10-28 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b79e7db7-e514-33a0-953a-3b9e4e5b5678 | -10.95177 | -50.25142 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 089be46f-cc81-3921-bffa-c023a4ef1d21 | -10.56214 | -49.77657 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 76636bbf-b885-34b9-9a5a-ac2c2805af63 | -7.94527 | -45.53318 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3bb68eb9-4d6a-3b3b-8dda-0c603724db9d | -10.64745 | -48.01652 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47ed2178-5443-3da8-b3de-da2399b26e65 | -7.32449 | -47.21719 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a8489fe2-2031-351e-9f33-aef5bf4dc948 | -7.6774 | -47.42375 | 2025-10-28 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4245ea37-c09f-3128-856a-f23da498f949 | -12.52853 | -47.53844 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3d792d9-2768-3c74-bcb2-6386e4acadfc | -12.54613 | -44.93456 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac1160a4-3cd7-339e-8303-18dea70690e8 | -13.63048 | -47.03034 | 2025-10-28 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ba77d702-7263-3816-831a-e2ad8a5724bc | -7.60713 | -46.47587 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ebdcb0d-0564-393c-90b6-70f79e5387b7 | -13.63413 | -47.62334 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9bc8ef3-c679-365a-83fd-6fab61146919 | -7.95005 | -45.54205 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 032dce63-160b-3cff-be2d-4597ceaabc92 | -7.94247 | -45.51206 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5d592c5-31ac-3193-b29c-b0f6fec4afff | -7.81189 | -46.45129 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 339802c9-7765-3e71-b95d-3979387d00e0 | -9.45998 | -46.86993 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bfe1c9f-deb9-328e-853f-56017debc698 | -12.52808 | -47.54206 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3650167b-5dcb-3f63-a3e1-1ca94612feb0 | -11.13895 | -44.94402 | 2025-10-28 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee5af6c8-aa27-38da-8759-b4c13ea9f20e | -4.97144 | -56.27786 | 2025-10-28 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44dbe90a-f4e5-3e6d-a08e-1c916c2b174c | -7.97233 | -46.73479 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee9b0279-c1be-3d11-bdea-c52b5112f8a4 | -9.96168 | -47.10128 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3921f606-4be1-3c6f-83fc-79ee4fd5c001 | -5.18368 | -60.30642 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 065fce59-6b2b-3259-9590-e50faf2cc7ea | -9.36932 | -49.2659 | 2025-10-28 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2825e692-a47a-3ad4-84e3-461a2e5027c1 | -7.00119 | -47.00087 | 2025-10-28 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2d761af-e641-3e46-91c5-23ae6cce117d | -7.10323 | -47.26743 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 715eb92a-5bde-32f8-8d4f-72f66751a1fd | -10.92183 | -50.27531 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9fd48ac-ad3a-3f5e-9a35-7d83af298f6e | -13.24342 | -47.97052 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb241ca7-4ecc-34a2-8d93-e0e008f21ff9 | -10.9256 | -50.27895 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f7004f7-597f-3d4c-a8f4-d430b97ae350 | -10.30889 | -47.16457 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41495a8f-d99d-3421-b750-2052ccf477ca | -7.94421 | -45.54127 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 19ef83e1-2fa6-3757-bf62-6987002fe802 | -9.99389 | -48.1032 | 2025-10-28 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a43510bd-1002-3270-bb24-743d3a951b62 | -9.13614 | -50.7013 | 2025-10-28 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b8237eb-bce3-3cd7-8191-01b29e218c8b | -13.22173 | -47.08863 | 2025-10-28 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7ec95fb4-0f15-35e7-9b11-8fd636456104 | -10.68969 | -48.01317 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31612858-94a1-3908-a1c2-ae4bae50864e | -8.16162 | -47.00221 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| add70700-a892-34b2-accb-2f4719761638 | -10.76134 | -49.7827 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90a9f4d6-aef8-3b07-a72d-3da5abb55eb5 | -12.52764 | -47.54568 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b682324d-1ed9-34e1-9ddb-e006e6c3614e | -7.83586 | -46.4041 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43331325-e645-3a00-9e0c-2c5cd4883716 | -7.97561 | -46.73106 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f486848-742f-31c6-8ff0-eaa8c45d186d | -10.28788 | -47.19999 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f3e473d-4f9a-3cb6-856b-c7e12afd3ffc | -7.71066 | -55.50116 | 2025-10-28 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83029ec2-edf0-32d1-9c0e-5ba13a6830f6 | -7.53529 | -46.76706 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df810cc4-6229-3eb0-a3d9-65c5cf171cad | -13.55848 | -47.15621 | 2025-10-28 05:04:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8794d15-4025-33b7-89f3-74fc9d779e88 | -7.44934 | -47.1645 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99406a91-d3ba-396d-a58d-8e5854ecad77 | -7.31543 | -47.20648 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0e9bf65-0d08-3d33-becf-b5c9499dcbb2 | -10.56125 | -49.80788 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 64583c6c-3458-3117-bebf-9e60f2f2dedb | -7.15567 | -47.00586 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51d37f50-78de-3baf-bf00-85fffa728971 | -10.35854 | -47.16379 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04aeeb69-e559-3f5f-b005-baf209caab92 | -14.66592 | -48.41453 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4414c47-bb79-3df0-abfc-d926aac66d94 | -15.15044 | -46.60094 | 2025-10-28 05:06:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c3c702a-410f-3467-bcbc-8f02b96a39da | -14.53018 | -47.99583 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f78d62e5-685e-31bc-8990-df0533603496 | -14.73163 | -47.36418 | 2025-10-28 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecc319b0-f0f5-36fa-8a82-0074be46445b | -13.92224 | -48.43347 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3d4c7cc-8daa-3cdd-bbe2-d31e74472ad2 | -14.54281 | -47.98231 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8606139f-4a45-3264-a256-77e54c739d27 | -13.73932 | -48.40772 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1636e0a-a18e-366c-99d7-7ffb66bf541d | -14.53367 | -47.98084 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f6020c3-d147-3518-b9d8-633cd5c1805e | -14.53938 | -47.97907 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a510589-0ad6-357f-9b3e-072c20eda280 | -13.74035 | -48.43486 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f477f10-e5c8-3bb4-94b4-b4d2a6322a05 | -14.4827 | -47.93153 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d8879b7-0e95-34b7-a0c0-e44c9808f5fa | -15.2015 | -47.21407 | 2025-10-28 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db71505e-c60e-35b6-a5fc-11e49d36a684 | -14.53211 | -47.99462 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9b5e155-b3c3-3d3b-8a5f-9d108797fce5 | -14.66668 | -48.40813 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 783f08f9-b427-3310-80c0-0e412fb448ad | -14.6663 | -48.41132 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fbbe2a8-cdba-3158-9c31-a6b164bd8425 | -14.76832 | -44.96379 | 2025-10-28 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d41e42b2-658f-3a41-9787-323bbd4f1bfd | -13.73584 | -48.42862 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5151eac-f58a-374a-bde6-08d4d3ffd9ca | -14.42945 | -47.85435 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71a0b52e-8528-3e82-926b-242d289b7089 | -14.53408 | -47.97727 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a293a23f-177d-3d97-b637-50c70f8008b6 | -14.42132 | -49.41995 | 2025-10-28 05:06:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README85.md)
