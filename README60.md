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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70f7c42c-1aa6-385b-8f3f-feca2e5267d4 | -5.43958 | -60.17093 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b460a5d-207d-36b3-a2d7-d22fa690750b | -6.44033 | -53.39309 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c68ad3fb-666e-33c6-be53-0d1d44161ade | -6.68998 | -58.85992 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38a065fd-3c2d-38ab-94f0-e9455a2eb214 | -5.87688 | -53.62709 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13d2ac93-edd4-3bb6-aa3c-19b654a26e9f | -5.87469 | -57.7604 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cfc29ece-43fe-36e4-a063-38cac7eebe06 | -7.64305 | -45.24454 | 2025-08-23 05:18:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65399f91-93e7-3253-bd0b-d6764b2fb852 | -5.80072 | -59.22083 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a50995c5-6fe5-34bb-8467-7661ef0cbc14 | -7.18406 | -48.42765 | 2025-08-23 05:18:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea0aac3d-854a-3319-9a0c-98112b80e295 | -5.75525 | -57.60049 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f90fef0a-e87d-30e2-a660-aa155504751e | -7.18348 | -48.43192 | 2025-08-23 05:18:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 141f51b8-7aed-32e2-b3ff-bf36fb76afe0 | -5.888 | -53.63607 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d265801-e1e3-336e-b8e6-8ff47938067b | -5.88078 | -57.74328 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dabb6ffb-57ee-3d85-aaea-286b6b510b1d | -6.27453 | -52.8294 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f548173-ee9d-3bda-89a7-60056c11af02 | -5.79795 | -59.21682 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 884cef66-688c-3c3e-aef4-7d230f56564e | -5.88193 | -57.75794 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4962e9e5-9cc2-38a4-a94e-91e3a4f09dee | -6.57412 | -59.86917 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e08fee4f-28d1-3899-a7fb-6da15a1b2e5c | -7.63877 | -46.28477 | 2025-08-23 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c605289-7021-3319-adaa-72d036e634b5 | -6.05917 | -53.8792 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc5b5c38-2744-3443-99b9-0138330921ec | -6.31022 | -59.88511 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88b910a0-46e7-3e45-90a9-653cb2e5abe0 | -6.00782 | -53.32157 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c42db0cb-825a-3448-80a5-5b7587386576 | -3.13405 | -58.04437 | 2025-08-23 05:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07707c1d-bd7a-3eb1-b552-f8030a5fe0db | -6.72672 | -51.9805 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7c9fbd6b-6a79-36d6-8c9b-71172f0cd628 | -6.47764 | -55.88428 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71cd609c-2898-30d9-aeed-bcb85e39f186 | -6.2538 | -53.68186 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20c1002c-b053-3912-bd86-9d8d2bbc9143 | -5.44181 | -60.17875 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a418306-a47a-3848-9349-559268cd4ebf | -6.61863 | -60.01096 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f26519ec-503e-3bb8-8433-c712c33df4b5 | -5.88084 | -57.76497 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d141385-6d21-3f43-a827-cbe203c11d68 | -5.88852 | -53.63257 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b01ede7c-3cb9-3296-a44f-14b4c2efc32c | -5.80017 | -59.22432 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74ee53e7-239a-3e95-a9c4-40aabd8327f6 | -5.80794 | -59.2184 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a6e6648-0771-3870-9bbf-b27547d1b4a2 | -6.28543 | -52.82514 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29671ad9-e03f-3a3a-9957-f92c36d794f1 | -6.28112 | -52.82448 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b79f4ce9-7e52-3e98-abd2-b3da9c820c12 | -6.05516 | -53.8786 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 812bad0a-8e9e-33f8-bc85-659fe13c50cd | -6.58305 | -59.87785 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e58ff3b7-7025-3c08-a43c-db923352e2f0 | -5.79684 | -59.22379 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c46a22d-af2e-3e09-b0ea-de5b4c0dd79a | -6.62772 | -58.54735 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da956813-57cd-3e45-90d9-69a9802a5b8a | -5.32466 | -55.94329 | 2025-08-23 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70fe1ba9-347a-315f-a4f6-333aef164930 | -3.65818 | -54.75921 | 2025-08-23 05:18:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce2304cd-8279-33dc-98ca-3a0b26d837b7 | -7.63955 | -46.27905 | 2025-08-23 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 083da710-5f36-331e-a10d-ca788203eb94 | -5.87524 | -57.75688 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 251dd8e6-4b6b-3cd2-a4f0-0a8b1cdfa028 | -6.46113 | -53.39612 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e18bf84e-e2c5-3d82-adfa-a8fe8030bf66 | -6.30965 | -59.88867 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d76954c-d0bd-34a5-9186-8c5ffc550db2 | -6.27681 | -52.8238 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e0f7b76-9a63-3dd0-b527-8223801675bb | -5.7363 | -59.88574 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c0e2170-e695-3268-873b-565e2e671aa9 | -5.22944 | -56.02235 | 2025-08-23 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a19f8a8c-268d-3bf5-bec7-842f898de4ec | -4.34767 | -46.47327 | 2025-08-23 05:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 24b1f0fc-726f-3d35-a35c-e8e6c5050697 | -2.29479 | -47.99269 | 2025-08-23 05:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0eb6c29-2c97-34a3-8766-83b220cd7a3a | -2.25815 | -47.85344 | 2025-08-23 05:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4f65513c-5949-38dc-a654-476b2ae3a997 | -2.70799 | -48.21221 | 2025-08-23 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7dd6a4b-08c5-30f4-91c7-b417940241d8 | -2.92877 | -53.69635 | 2025-08-23 05:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afa481c7-753a-312c-83b6-9cfec56e18d6 | -2.92902 | -53.6982 | 2025-08-23 05:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f6ac895-b527-342a-a8a2-a8854629bf39 | -2.25874 | -47.84952 | 2025-08-23 05:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daac1082-2c0b-3368-b34e-30d7e2ba072b | -2.4438 | -47.32847 | 2025-08-23 05:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1898d0e-ff51-3b63-a9b8-233cd8d74949 | -3.43355 | -49.04024 | 2025-08-23 05:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 89a3f335-713e-340a-ab20-d0b9c82f9464 | -2.55748 | -47.71203 | 2025-08-23 05:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 671b166b-a881-3a36-8e94-c79340e69074 | -4.07648 | -48.03881 | 2025-08-23 05:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b860bea-338b-3b69-88b8-fe1fcf2dfef8 | -2.93362 | -53.69397 | 2025-08-23 05:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 598f6e91-bb38-3cb6-be4a-bb56dad81203 | -4.22949 | -47.21254 | 2025-08-23 05:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 485d637b-bc48-39c6-81a0-91b9b78e9aea | -4.33995 | -46.47095 | 2025-08-23 05:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d0158a1e-93ec-3b1e-afbb-b1388271d5c3 | -4.30967 | -48.09783 | 2025-08-23 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c172222-a5a2-34ea-a123-042059f4e7ec | -2.93289 | -53.69879 | 2025-08-23 05:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46da9ab9-4483-364d-9e7e-6f885b8b3b24 | -3.37265 | -52.79682 | 2025-08-23 05:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edfc053a-14b5-3250-9fca-ec7c3ec7e5bf | -3.43305 | -49.04364 | 2025-08-23 05:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d7a29b23-1e06-33eb-ad93-ae7b5cb72415 | -4.34842 | -46.46798 | 2025-08-23 05:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b45c4528-d660-34c5-8f65-cc3fe6290c30 | -2.5511 | -47.71523 | 2025-08-23 05:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4929df14-1d1b-32a2-9942-72bdde4af138 | -2.44316 | -47.33268 | 2025-08-23 05:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 024220e6-b346-3419-86e0-957dcc7a5a86 | -3.43891 | -49.04105 | 2025-08-23 05:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d98f5b2e-e3b4-33eb-8e2c-987c9ae2db94 | -2.55168 | -47.71123 | 2025-08-23 05:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af0b736d-720b-3b77-af56-072ca37f9420 | -4.34076 | -46.46545 | 2025-08-23 05:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69c966bc-6986-3217-b3b0-8086e4ab83ea | -4.31033 | -48.09626 | 2025-08-23 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8485ff6-bcb9-3868-b95a-855bf87af2d0 | -2.97084 | -54.65671 | 2025-08-23 05:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 401a93f9-d61d-3e5f-b018-849301fa3be4 | -1.51153 | -54.69135 | 2025-08-23 05:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef12bf78-7a6b-3d82-a10e-76e957b6445f | -4.12434 | -48.11623 | 2025-08-23 05:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 752141ad-4883-33bc-b52c-665b6e3ab4a8 | -1.5614 | -54.53802 | 2025-08-23 05:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a8404dc-2ab4-35aa-9da8-366bfabb65a0 | -3.28177 | -48.80842 | 2025-08-23 05:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12fe4451-0e6d-3c8a-82b3-807d095994d8 | -2.91796 | -48.31016 | 2025-08-23 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d2767c3-c489-3840-a55e-704953d122bf | -2.93217 | -53.70362 | 2025-08-23 05:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24ba29a9-f967-37f0-8524-5a41adbe0e9f | -3.04721 | -47.01746 | 2025-08-23 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 532fcb15-5648-3217-a01a-aa83d66126dc | -3.43841 | -49.04445 | 2025-08-23 05:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 08a14e73-698c-3cbf-818a-3f3663489a87 | -2.92975 | -53.69337 | 2025-08-23 05:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba4f7f95-0c80-3c05-bd04-740cb49b788c | -2.55216 | -47.70934 | 2025-08-23 05:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4566c2cc-3d1d-3d37-9d8b-69536369e1b7 | -4.31612 | -48.09708 | 2025-08-23 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86c68e58-9edd-3c0c-b5c4-60f5c5096a67 | -1.7006 | -55.18999 | 2025-08-23 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a02eb80-85db-3b2d-b4f9-f535775d9ccd | -1.55777 | -54.53747 | 2025-08-23 05:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ce520f6-ff7d-320a-b6b2-e1e07b46f1d6 | -1.55644 | -54.54591 | 2025-08-23 05:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c475aa70-5421-3577-8835-5881b01108f3 | -2.96718 | -54.65612 | 2025-08-23 05:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71b9f63f-e21e-3bfd-bbcc-112a0dc5b4a3 | -3.51813 | -47.20903 | 2025-08-23 05:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a400821a-4b1a-3b9e-ac0b-ff146d230226 | -1.4624 | -54.11811 | 2025-08-23 05:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb217013-8be2-3e64-a677-aa116035f5a4 | -1.46174 | -54.12246 | 2025-08-23 05:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be912302-c55a-3554-bf9f-31f690690426 | -1.55711 | -54.54169 | 2025-08-23 05:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed419ac0-ce27-37e2-aef7-b684a216d7cb | -4.30398 | -48.09945 | 2025-08-23 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 162c11e7-ee47-3ee9-83fc-b5411fa9bbba | -4.07265 | -49.45663 | 2025-08-23 05:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0691b51-5613-3dc8-9b59-3943b5f4929c | -4.34127 | -46.47224 | 2025-08-23 05:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ce010976-765d-30d0-bb06-025404cb56f2 | -4.2242 | -47.20873 | 2025-08-23 05:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75ac3bd6-5299-3913-8c38-90434d199f4c | -4.07593 | -48.04273 | 2025-08-23 05:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4336c54a-85df-34b2-9327-f46fd342ac8b | -4.12376 | -48.12026 | 2025-08-23 05:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 093edf3b-1ae4-391a-95a1-ee13a1ea585e | -4.31555 | -48.1011 | 2025-08-23 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ed692b4-090e-3bf4-861e-76a91985ded0 | -4.22337 | -47.21172 | 2025-08-23 05:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c4d3d38-8852-33b2-9d72-e66b4f488671 | -2.70295 | -48.20753 | 2025-08-23 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 179ec177-52ef-3575-9763-2bc6292e9d55 | -2.55734 | -47.71406 | 2025-08-23 05:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README61.md)
