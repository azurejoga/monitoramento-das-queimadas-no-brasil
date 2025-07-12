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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1b35ad4-30c2-3fd3-9546-59163888c500 | -10.84444 | -49.10835 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0e3e274c-7b93-3471-bbb7-d9b7419895e3 | -9.91168 | -47.82994 | 2025-07-12 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94b08af2-c3b3-34fe-9b47-8fba882999fc | -13.11917 | -47.3033 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aebbc3b3-aa72-38e6-b0d2-33dd286f4d4a | -10.90197 | -49.20663 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0631892d-2425-3846-8622-2a452ec06c88 | -7.9936 | -46.41622 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78e9700a-ca81-36a8-9f05-73d601373324 | -10.05263 | -59.11013 | 2025-07-12 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1423bc9-5cbd-3f3c-8134-f80707c2373d | -11.42519 | -46.40311 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d9a724b-ba54-3572-ba01-fbf5e367c4dc | -8.54932 | -48.26158 | 2025-07-12 04:40:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d4d713a-b41f-3476-9e0d-f5e6a099e513 | -9.33428 | -49.91633 | 2025-07-12 04:40:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df2a92b8-c136-39f5-a14c-1879e5a3cf32 | -7.7354 | -49.32853 | 2025-07-12 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25154d8d-523c-3917-bffb-93325b2a5033 | -6.65521 | -41.99663 | 2025-07-12 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e5752dca-a576-31b8-aef5-3dd552b0c492 | -11.27513 | -46.40593 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32687104-ca8d-3a4b-a8f1-6591865f4f66 | -8.92017 | -47.34612 | 2025-07-12 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98cf1f7e-c760-37f5-a96f-9daf462e29a9 | -7.19213 | -45.32883 | 2025-07-12 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e335ccae-2e5d-3e01-a574-e623c9edbebf | -9.27267 | -46.6167 | 2025-07-12 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dc1f1a7-7f61-31b2-8846-814881b17373 | -8.89497 | -47.27312 | 2025-07-12 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d014506d-4723-3ad2-a3aa-ab23618301ae | -7.44252 | -43.91835 | 2025-07-12 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57a6bcee-86ef-36e9-8047-87aee89e624a | -7.47627 | -47.52034 | 2025-07-12 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1a72163-1ad9-3cd7-b215-4bca71a27f9c | -9.50634 | -47.56463 | 2025-07-12 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94b42d3b-ea67-3d00-8538-a46961df8418 | -11.84173 | -47.51075 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| be37d722-a293-3120-a1a3-2593daff5520 | -11.10211 | -60.85222 | 2025-07-12 04:40:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6b496ef-cfb7-308c-948b-51f1d2976a25 | -11.84295 | -47.50217 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f014c2a-9f39-37fc-ae95-b1dffe48107f | -9.14927 | -48.99986 | 2025-07-12 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88ae4a17-100c-35fc-bf60-a84769c21904 | -10.86076 | -49.11462 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 810a65a5-adda-3b17-a101-ca21dc800787 | -13.1423 | -47.31253 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d0d163f-5a17-3eb0-89de-2119219d6bbc | -11.73134 | -47.47355 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 78a6f8cb-58ca-3c7b-acf0-88050618ec6d | -8.22941 | -47.55581 | 2025-07-12 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 228627f2-6083-36e0-bde4-acd969b80d43 | -7.93146 | -61.55605 | 2025-07-12 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ccbe654a-15f7-3f0a-8d05-7984acd90d7d | -6.08883 | -49.8971 | 2025-07-12 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 985bf668-5606-3bab-ba11-3e220fd53598 | -7.68802 | -44.3737 | 2025-07-12 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c26007e1-6b95-362f-9f41-e1b4535ae4c3 | -13.02651 | -46.66281 | 2025-07-12 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6657287e-ef13-3245-944d-bd70fc76faf6 | -11.86912 | -52.25592 | 2025-07-12 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c16cfa6d-6ecd-39a8-af54-a1f99e42a15f | -11.42902 | -46.38764 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69baaceb-ecf1-32b9-894f-fd858c6150fd | -10.05206 | -59.11322 | 2025-07-12 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0f19824-7409-310e-bf27-5ed6767546b9 | -11.83871 | -47.50593 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fee1944a-85ff-398c-8848-0cd12262de88 | -7.08656 | -49.6095 | 2025-07-12 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 007ee20f-331c-315c-b742-99f1a22bf10c | -8.52982 | -54.77295 | 2025-07-12 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84d182d2-1570-3f1d-8cb5-d4d7347bd02f | -12.60716 | -48.36841 | 2025-07-12 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f3026604-6666-3f44-91ba-6d0ac6861466 | -7.98193 | -46.419 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f61a78c-0085-328b-a95a-7e4c31764e26 | -11.73678 | -48.52866 | 2025-07-12 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2862f935-7842-3edd-9308-fcd80ad5e5bf | -5.84301 | -48.39544 | 2025-07-12 04:40:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 245e26a5-33e9-3e3d-890a-714675acf4ec | -8.4781 | -49.60578 | 2025-07-12 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e84052ce-0243-3bc9-bdc6-79ebf6108197 | -6.65593 | -41.99482 | 2025-07-12 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f7366c44-b007-3235-8050-43c6a3dd4263 | -11.42206 | -46.38141 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e2224a0-cfee-31a2-8c9b-27379bbfd71d | -14.78328 | -48.20704 | 2025-07-12 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b5f5f002-4e53-3d1d-a954-02597cbff142 | -16.71699 | -49.41602 | 2025-07-12 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc7e82c1-4fc8-3131-b119-46a417fa48a9 | -14.22965 | -49.78516 | 2025-07-12 04:42:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b801b72-dcae-3473-ad94-1b07db5aed56 | -12.58029 | -56.98277 | 2025-07-12 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 854db478-d18b-3201-a8b7-e860423994c4 | -17.917 | -45.56487 | 2025-07-12 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c2eac5d-02b0-31b9-bbfc-c4d8cd562ddb | -17.33308 | -44.89891 | 2025-07-12 04:42:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8230136f-51d7-30c2-9c1d-2506f0a86b98 | -15.02311 | -43.75515 | 2025-07-12 04:42:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9e66d19c-2763-3ffd-80a9-f470bc07df3e | -18.42473 | -54.56376 | 2025-07-12 04:42:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cca9cff3-2a06-3f22-adba-bf6bbdfba9a1 | -16.84008 | -48.52621 | 2025-07-12 04:42:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b2ede2d-846c-3a7d-9705-63bb1a20f5a6 | -15.06481 | -47.59908 | 2025-07-12 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01c5680e-7413-3151-94c3-a8e353e4f466 | -15.73547 | -48.28578 | 2025-07-12 04:42:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81ca2a80-816a-3ab0-ad8d-184371fe597a | -13.64635 | -53.93723 | 2025-07-12 04:42:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0969c2a-b647-3b2a-bb01-bb4e52074781 | -13.28945 | -49.15784 | 2025-07-12 04:42:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b514b4c6-e557-30cc-b599-54d0727c14bf | -15.68518 | -48.27017 | 2025-07-12 04:42:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52e209b2-d24e-3263-8187-6258c8f893cb | -13.22739 | -49.83399 | 2025-07-12 04:42:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdae12f9-2ca0-3604-a6b0-e9ada26dea98 | -17.94061 | -44.38852 | 2025-07-12 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf4217d3-9bef-3010-bd54-4b45aaf45352 | -11.88273 | -58.74162 | 2025-07-12 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9b88465-56f0-33b6-a7ba-a32256b3c167 | -17.9405 | -44.38876 | 2025-07-12 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbf7abec-5bd0-3483-bc8f-d396a8a55e63 | -15.06105 | -47.59853 | 2025-07-12 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8ce9948-121f-3891-9b1e-20aa2427786b | -13.37774 | -49.12848 | 2025-07-12 04:42:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48393161-44b2-3349-926e-57e781ce7b13 | -15.07978 | -48.94381 | 2025-07-12 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29ba1e15-e2b1-3ed1-a400-4fa9e5dbdd26 | -14.91003 | -51.05651 | 2025-07-12 04:42:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4175bf7c-26e0-34cf-8513-d6d9c0b398d6 | -14.75146 | -46.29971 | 2025-07-12 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79150083-59ff-376c-abdf-9494630a7600 | -11.88193 | -58.71901 | 2025-07-12 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1158ba9-89a5-34a0-b62d-c91c770cc889 | -13.65407 | -53.93763 | 2025-07-12 04:42:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7f82d0f-e68c-3148-adf0-448f33afab9c | -15.07893 | -48.94506 | 2025-07-12 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5befccfd-84c7-3863-9a98-3af70573c1af | -18.32298 | -47.63357 | 2025-07-12 04:42:00 | NOAA-21 | TRÊS RANCHOS | GOIÁS | Brasil | 5221304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e94479f4-992b-33f4-a6a1-7af0f593e56e | -11.8781 | -58.71279 | 2025-07-12 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73d64830-8eee-3961-86cf-2c71a7c35949 | -16.59082 | -47.61444 | 2025-07-12 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d27f714-d961-3d29-b96e-6ec2ac6dc614 | -13.91417 | -51.81439 | 2025-07-12 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88a2798a-6461-37df-9e96-458266fb9eab | -11.86362 | -58.71029 | 2025-07-12 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 733f334d-92f7-34db-b32c-439991f52b24 | -17.59599 | -52.49602 | 2025-07-12 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6adedb11-78da-3116-8a16-a9430175a19e | -13.65055 | -53.93704 | 2025-07-12 04:42:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c388eb48-b3d1-30a0-94f8-eab0436fae49 | -16.71349 | -49.41545 | 2025-07-12 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47774d19-2ceb-3d3e-8b37-a12079d6990f | -14.34937 | -54.46669 | 2025-07-12 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51ca6393-e254-3300-8f29-290a9c760292 | -13.66109 | -53.93884 | 2025-07-12 04:42:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd517ed8-e7ee-35ea-9c39-83d846e723c9 | -14.74909 | -50.55279 | 2025-07-12 04:42:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cee17939-764e-383f-a5df-b2b8f8171eb0 | -15.57063 | -47.85495 | 2025-07-12 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7fa08aa-23cb-384e-bcf4-60a7f2c2f68c | -19.16466 | -50.84695 | 2025-07-12 04:42:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6851f4f1-4f98-33b0-b1d5-c6c3c0f46989 | -13.64704 | -53.93647 | 2025-07-12 04:42:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b71b248b-a1e6-31a8-8cb5-ef89f8191e6f | -15.60622 | -46.516 | 2025-07-12 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7dee3a04-94bd-3001-a962-7f2db8456274 | -17.69056 | -54.01063 | 2025-07-12 04:42:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed8b2e31-4900-31e5-891b-172ac4fc79c4 | -15.1034 | -56.2327 | 2025-07-12 04:42:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d82caeb8-a5a5-3728-a80f-352d657e0511 | -18.42538 | -54.55981 | 2025-07-12 04:42:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5652cd43-a13a-3a55-bdd1-50f2adbcfa01 | -15.73328 | -49.34541 | 2025-07-12 04:42:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0edaf3af-9a39-36be-876d-f6abec77cf33 | -14.75096 | -46.30341 | 2025-07-12 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8961afeb-2f79-3c7c-9aa8-74e0fbb05517 | -18.42625 | -53.03035 | 2025-07-12 04:42:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6af7f8c-d677-395f-8775-75182f8d29e2 | -15.103 | -56.22966 | 2025-07-12 04:42:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ff176ec6-b151-32a4-8a34-d3756770a88a | -13.65758 | -53.93823 | 2025-07-12 04:42:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e278b2d-fead-3c28-b0b0-188ba7af7d09 | -12.58379 | -56.98758 | 2025-07-12 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc94e559-6e83-351f-b785-341dfe02da1d | -14.56801 | -48.14489 | 2025-07-12 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f68ad0a5-d853-3ad3-b8f1-901d0f1067b1 | -18.95282 | -54.32895 | 2025-07-12 04:44:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d79987c9-acc1-30c4-8b31-c25da9fa2e69 | -20.70832 | -56.66395 | 2025-07-12 04:44:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44cfc043-7ba1-386d-b7f7-4022b4bc549b | -19.0221 | -57.62108 | 2025-07-12 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 08c86122-7432-38ab-9e3b-151c37f5089f | -20.47702 | -53.67448 | 2025-07-12 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ac9c26f-1107-3705-afee-674cd659a8ec | -21.30944 | -52.79715 | 2025-07-12 04:44:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
