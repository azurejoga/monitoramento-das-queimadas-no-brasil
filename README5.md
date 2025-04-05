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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c0176c7-aea0-3f34-8692-43ac7b36f3f7 | -20.58052 | -56.04079 | 2025-04-05 05:21:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9040f345-b044-35dd-bf8a-f68fc3fde59a | -20.58804 | -56.0504 | 2025-04-05 05:21:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a822673-fcb0-3742-acca-c611291686b2 | -15.13429 | -51.43132 | 2025-04-05 05:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe6c3949-68e4-3c4b-a35a-182b42801bd8 | -20.83136 | -47.75303 | 2025-04-05 05:21:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 39b2489f-6f73-3842-8fc8-ae54cbf127ba | -20.58156 | -56.03226 | 2025-04-05 05:21:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ec43df7-9563-38da-beea-936752804c93 | -20.57572 | -56.04452 | 2025-04-05 05:21:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56de1745-61c8-3a86-b7bc-5e13ed7767d3 | -20.84122 | -47.75805 | 2025-04-05 05:21:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 8c3b8d30-95c8-365b-9f0f-ab699a061e83 | -20.58532 | -56.03705 | 2025-04-05 05:21:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2293329-f353-33f3-8c38-55e4dc095bd0 | -20.58908 | -56.04189 | 2025-04-05 05:21:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5921b499-5152-3be3-a1f8-c1ead329b950 | -20.83849 | -47.75417 | 2025-04-05 05:21:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 89cb1c50-55e6-3b7b-99b9-c70d4fe55132 | -20.838 | -47.76093 | 2025-04-05 05:21:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 37.9 |
| bdd10619-e469-32b3-a67f-8d535c704bd1 | -20.56824 | -55.08683 | 2025-04-05 05:21:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9041b3f-5a5c-39d1-bca1-a78499ab2565 | -20.5848 | -56.04132 | 2025-04-05 05:21:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6baa9b5e-a21c-3613-a59e-393e53568c0a | -20.83088 | -47.75965 | 2025-04-05 05:21:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 8165eb2b-e7fc-3d4d-9974-7ce203562f4b | -20.83409 | -47.75699 | 2025-04-05 05:21:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 25.4 |
| c1f97846-90a9-3723-98c1-7753139e7743 | -21.25349 | -56.02213 | 2025-04-05 05:21:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9457072d-7b28-38a3-8cc9-ec0960042bf0 | -20.83364 | -47.7636 | 2025-04-05 05:21:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 078c7057-74e2-389a-a6c0-8939484d2ba6 | -20.83751 | -47.76757 | 2025-04-05 05:21:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 37.9 |
| c3d63745-be62-3706-82a9-914fb9a7b476 | -30.46436 | -56.38943 | 2025-04-05 05:25:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| e4f131a8-e3d0-3946-8d57-80c3838a8405 | -20.8306 | -47.7603 | 2025-04-05 05:40:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 52f5e421-2b6f-3dd3-8a4c-5a2f36ac8b3f | -20.8512 | -47.7554 | 2025-04-05 05:40:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f9def70c-bb2c-3835-8836-148d6c2a3568 | -13.44087 | -41.77284 | 2025-04-05 05:40:00 | AQUA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| df45decd-0d62-336f-82cd-e0ee1fc6a2c1 | -13.44329 | -41.75353 | 2025-04-05 05:40:00 | AQUA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| e028a287-77f1-3e2e-8cad-0a311338ad5a | -8.1031 | -43.12368 | 2025-04-05 05:40:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 3fdc1c3a-c261-35d5-9314-2c7d5fe9bfc4 | -13.03357 | -45.01211 | 2025-04-05 05:40:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1f7e8165-b186-348d-95dc-d88263c399c9 | -20.83466 | -47.75765 | 2025-04-05 05:42:00 | AQUA_M-M | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 155.6 |
| f932b5a1-3a83-31c1-92b9-3eeb043fd12e | -20.82537 | -47.75616 | 2025-04-05 05:42:00 | AQUA_M-M | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8a00ced1-8284-30c7-b7ba-001ee3892ce9 | -20.83323 | -47.76796 | 2025-04-05 05:42:00 | AQUA_M-M | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c1aca94f-b77c-3fbb-b864-f14c4769e707 | -20.83609 | -47.74727 | 2025-04-05 05:42:00 | AQUA_M-M | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5b0540df-a91d-3068-acb0-3fdfe5942dd6 | -20.8268 | -47.7458 | 2025-04-05 05:42:00 | AQUA_M-M | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| de624a33-ba18-375b-91ff-b97b56eb8b6d | -20.57488 | -56.04122 | 2025-04-05 05:46:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8caaa46e-2b25-3e9e-a6de-fc3fe0fba8ef | -20.58774 | -56.04223 | 2025-04-05 05:46:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20ecef68-35ca-359e-8a50-2b66335a3587 | -20.57993 | -56.04129 | 2025-04-05 05:46:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7f7edd4-09fe-3d92-89b7-1022037c49ae | -20.58636 | -56.04173 | 2025-04-05 05:46:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c430a14d-5f8b-3584-a6b5-a8cd0c4337a9 | -20.58131 | -56.04175 | 2025-04-05 05:46:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daa7cb4f-747d-39da-961c-45ae3fc301fe | -20.8512 | -47.7554 | 2025-04-05 05:50:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 84c5d871-7edc-3e44-be9c-805288473a7e | -20.8306 | -47.7603 | 2025-04-05 05:50:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 189f5b79-e27d-3bd2-91f7-8bd702bcf2c9 | -20.8306 | -47.7603 | 2025-04-05 06:00:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 106.3 |
| b02a98e3-e02f-3989-9e33-484946412442 | -20.8512 | -47.7554 | 2025-04-05 06:00:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5be0240a-9032-3c9a-893f-f44294b5ddc0 | -20.8512 | -47.7554 | 2025-04-05 06:10:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 68.4 |
| f7c19ac7-133a-3f70-9336-86ed3082242f | -20.8306 | -47.7603 | 2025-04-05 06:10:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 739c3e61-9460-3bd8-9daf-68d049c67a02 | -20.8512 | -47.7554 | 2025-04-05 06:20:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 019bfeea-37a4-36b5-9eb6-0cfbcb17915a | -20.8306 | -47.7603 | 2025-04-05 06:20:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 1500f8e0-d18f-36e6-b132-772ed5acf0a9 | -20.8512 | -47.7554 | 2025-04-05 06:30:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 7f64c297-4526-3c7b-8c59-770953be0008 | -20.8306 | -47.7603 | 2025-04-05 06:30:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 6763b8d2-831e-3028-ad70-9f986a5e89e3 | -20.8512 | -47.7554 | 2025-04-05 06:40:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1b13c6a9-0197-35b1-91bb-afcd290f6778 | -20.8306 | -47.7603 | 2025-04-05 06:40:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 75.0 |
| cd045be1-a7d4-37b6-aea7-21b076cbc6b2 | -20.8512 | -47.7554 | 2025-04-05 06:50:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 80.0 |
| f4ed8e89-86a6-35b1-b674-2452000239a5 | -20.8306 | -47.7603 | 2025-04-05 06:50:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 6b8dd4ad-83ca-3136-bb53-5f0660fd7220 | -20.8512 | -47.7554 | 2025-04-05 07:00:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 02deeac1-f34d-39a0-8e4b-553603bc5033 | -20.8306 | -47.7603 | 2025-04-05 07:00:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 72.7 |
| c4567d49-1559-3177-b7f7-322db30f4cbd | -20.8306 | -47.7603 | 2025-04-05 07:10:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 85.0 |
| f5bdf3e6-8ec3-34ad-af99-783d14fef22c | -20.8512 | -47.7554 | 2025-04-05 07:10:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 60.9 |
| a6a09d58-bebe-35fa-bc43-b7aaef4b35ff | -20.8306 | -47.7603 | 2025-04-05 07:20:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 46e49ba9-0cc1-3ead-8909-9a409c3e1729 | -20.8306 | -47.7603 | 2025-04-05 07:30:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 321f5af1-ee8b-303a-af18-05cb4561b4cf | -20.8512 | -47.7554 | 2025-04-05 07:30:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 855e5548-e743-3c78-9a34-d5a3760352e1 | -13.1851 | -45.2168 | 2025-04-05 11:40:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 55fb93d3-e453-3409-9810-7c22f975d50a | -13.1851 | -45.2168 | 2025-04-05 11:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 202.3 |
| b8763866-b80e-3e48-9aaa-51099e1b69b7 | -13.1847 | -45.2401 | 2025-04-05 11:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 7bbb3562-a03a-3d36-9226-9bcf6a89a8d6 | -13.1658 | -45.22 | 2025-04-05 11:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| df75e35a-1adc-3976-b7f6-e053ea06eae3 | -13.1653 | -45.2433 | 2025-04-05 12:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 2d242420-91de-3ccf-8028-2b29efc00413 | -13.1658 | -45.22 | 2025-04-05 12:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 268.6 |
| 350c17ad-261a-3990-9116-4c4891ebb9f6 | -13.1851 | -45.2168 | 2025-04-05 12:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 473.8 |
| 0249dd13-6698-38a4-a322-96b88f59ab9f | -13.1847 | -45.2401 | 2025-04-05 12:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 5453ed9a-6ca9-365c-8b62-7c644d83858e | -13.1851 | -45.2168 | 2025-04-05 12:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 437.9 |
| 6588fab1-2799-326f-8c9b-5a5ee6a93a7b | -13.1658 | -45.22 | 2025-04-05 12:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 767.7 |
| 23062551-2c0f-395d-a49b-bf85037d24dc | -13.1653 | -45.2433 | 2025-04-05 12:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 250.4 |
| 687422f3-e852-31c0-bf4d-ffee98ca8624 | -13.1847 | -45.2401 | 2025-04-05 12:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 171.1 |
| affcbed2-e45d-39d9-b6dd-8aa0f3a4d263 | -13.1653 | -45.2433 | 2025-04-05 12:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 299.3 |
| f6182de4-afda-3a44-a241-b2ee72e90409 | -13.1658 | -45.22 | 2025-04-05 12:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 548.2 |
| cc0fd8a1-b33d-394f-9a93-7776547968d5 | -13.1847 | -45.2401 | 2025-04-05 12:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 296.0 |
| 6e122bc5-4a57-38e1-a227-f52d2e057a26 | -13.1851 | -45.2168 | 2025-04-05 12:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 746.6 |
| 835bac33-54f2-3889-8a24-e61cfd26f2dd | -13.1847 | -45.2401 | 2025-04-05 12:30:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 66647471-4dec-3732-a074-6ee6d806c398 | -13.1653 | -45.2433 | 2025-04-05 12:30:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 233.5 |
| edc4947f-4db1-3951-b68c-408c8393165f | -13.1851 | -45.2168 | 2025-04-05 12:30:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 371.2 |
| 64220927-35f5-3127-9bcf-0653af665301 | -13.1658 | -45.22 | 2025-04-05 12:30:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 563.0 |
| 78e367b7-8934-3624-b6d1-98598967534a | -13.1653 | -45.2433 | 2025-04-05 12:40:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 174.0 |
| d14eeaa4-e583-3302-870b-c5d43be03106 | -13.1851 | -45.2168 | 2025-04-05 12:40:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 310.5 |
| 04cbef47-aaf8-34d9-8a32-5edf428c771d | -13.1847 | -45.2401 | 2025-04-05 12:40:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 41a6244e-8c40-39e5-9c8f-e051e18388f0 | -13.1658 | -45.22 | 2025-04-05 12:40:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 292.9 |
| b826230d-47d1-3597-9b4c-e3ef2a9cb1cc | -13.1653 | -45.2433 | 2025-04-05 12:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 946a9ab3-454d-3f36-8a9f-1b0b0604791d | -13.1658 | -45.22 | 2025-04-05 12:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 6aa8df85-3dcc-3dcb-9b25-bcb5c55b081a | -13.1847 | -45.2401 | 2025-04-05 12:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 9a14bd57-59e3-3eb3-9454-6b31dfce958d | -13.1851 | -45.2168 | 2025-04-05 12:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 272.6 |
| 2804245d-80b5-36ea-ba68-d61962ecb0c2 | -13.1658 | -45.22 | 2025-04-05 13:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 3ad3a75b-2e59-38eb-bb6c-30980ec09195 | -13.1851 | -45.2168 | 2025-04-05 13:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 7b65744e-a43f-32a2-ab36-e0eccd9776ea | -13.1847 | -45.2401 | 2025-04-05 13:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 1cdbd16d-3e42-3c3d-8057-22e33d7490a0 | -13.1658 | -45.22 | 2025-04-05 13:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 46157de6-3a48-3556-8464-f6f831d9ca37 | -13.1847 | -45.2401 | 2025-04-05 13:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| cd191c1e-fc57-35b7-ba84-0c98362c1cf7 | -13.1851 | -45.2168 | 2025-04-05 13:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| ae6b0fbb-cad5-34a8-952b-46d6f9016dde | -13.1658 | -45.22 | 2025-04-05 13:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 35a0d8b4-5fba-3d7f-8a29-e4eef0dbfc2f | -13.1851 | -45.2168 | 2025-04-05 13:30:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |


