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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae242dc5-3bfd-3d9b-83bf-a34ac6a53444 | -11.1042 | -54.145 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 68a9e73e-1ca2-3f1f-b0f0-7b643692bf88 | -11.03322 | -49.5154 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78ad6adc-2b38-3c62-a23b-9be14c43572b | -10.68856 | -60.7471 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6eb670b0-6f48-311f-ad0e-0d3fb8b00172 | -8.39181 | -45.55491 | 2026-06-21 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| acd1fd1d-1050-3e0b-875d-4ba34f3b6254 | -11.0589 | -52.47041 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81088475-5134-3ecf-a3bc-8ee25a24d00d | -10.9285 | -56.85022 | 2026-06-21 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77bab5bb-daf7-35de-adbb-db33acbbb088 | -11.2746 | -58.31355 | 2026-06-21 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6ab1ca0-d8d2-3405-998b-76d64179f661 | -11.3059 | -54.72023 | 2026-06-21 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e53d52ea-f214-3211-882d-ba583f379770 | -13.51913 | -52.16344 | 2026-06-21 04:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfbe61f9-5a73-3678-bb89-d3fe740aaf1a | -8.81472 | -47.0652 | 2026-06-21 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78f59aae-c82c-39e2-9c78-f6324534a6f2 | -10.68627 | -60.75874 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71bab727-5946-30e1-9c83-43090fd125cb | -11.10712 | -54.15009 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 59283e9e-82c7-3ecf-bf55-669d8d783670 | -12.42245 | -54.17921 | 2026-06-21 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 80760a2e-6edd-37a8-993d-1b61f775fcd9 | -11.09612 | -54.14808 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 9926f012-bf7a-3465-90d5-bda0719982c9 | -8.35198 | -50.49731 | 2026-06-21 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2e4aa2c-2e0d-3429-b58c-7edc03993b63 | -11.6378 | -48.53156 | 2026-06-21 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 17a085bb-5568-3e9c-835d-abfc51d6f4cc | -13.85765 | -45.89262 | 2026-06-21 04:44:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe1bbefc-8b4c-31dc-acbd-24cab9e80ed2 | -11.09319 | -54.14304 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c584c48a-2b2b-32f4-9c2f-01bb48786b02 | -10.05619 | -48.09124 | 2026-06-21 04:44:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf20d65d-894f-3a41-bc92-1fcbd1b53a23 | -12.4227 | -54.18198 | 2026-06-21 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dffbdb8d-6186-31f9-aca7-381ea11f0ad7 | -8.35529 | -50.49817 | 2026-06-21 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a96e390a-1180-340b-822e-611bf68beed0 | -9.80469 | -48.91938 | 2026-06-21 04:44:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44a07326-5440-347a-b438-37d592989c66 | -11.06292 | -52.46723 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b4eb12e-4c60-330e-baef-ca890358824e | -10.83673 | -49.12348 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af87ac2f-e5b9-3e17-bb74-301455425072 | -8.1389 | -46.87964 | 2026-06-21 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3627572-79f2-3a74-9720-09a97aa6f4e6 | -11.09393 | -54.13867 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| df5f204a-de70-38a9-95fe-c4a965691b61 | -11.1587 | -48.80769 | 2026-06-21 04:44:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d31c37b-be2a-3472-920b-ffd97294cb70 | -11.09834 | -54.13493 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| b5c22e96-e387-3415-a51b-3461a5258e76 | -10.68138 | -60.75375 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 583a05ed-bfb1-3cdb-b8c8-aeaca3c40e67 | -8.46026 | -51.53593 | 2026-06-21 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75b4e92f-0f33-31e6-a3be-4f5fcdd4cd19 | -9.30841 | -47.62766 | 2026-06-21 04:44:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 706d17bf-d991-3224-8b3c-b05ee904dad5 | -11.946 | -43.96589 | 2026-06-21 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24c3b2c7-4d7a-358e-b768-ddab78fba072 | -10.05677 | -48.08737 | 2026-06-21 04:44:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a935fc51-826f-30bc-abc4-a14139cd0791 | -13.52436 | -52.16815 | 2026-06-21 04:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98027bf9-a955-335e-a9b0-c5b7c6f4b6e9 | -8.35805 | -50.50219 | 2026-06-21 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1462d87-867e-3dc9-8c24-b7f612281562 | -10.68836 | -47.70343 | 2026-06-21 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e83e140-037c-3181-abf9-4599f26d73d8 | -12.06567 | -48.42798 | 2026-06-21 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e844316-9e89-3778-8db0-5a81d9ee894b | -7.95921 | -47.43667 | 2026-06-21 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad1ee7fc-f5b0-3965-a29b-0390c6a14da9 | -12.42196 | -54.18622 | 2026-06-21 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebf423b1-eeb2-3f19-8165-eaef25779182 | -11.94661 | -43.96127 | 2026-06-21 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1ab8648-3b27-3c7c-b697-c20f041355c4 | -11.06975 | -52.46841 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3695c5fc-993a-373c-93a7-64351d01596a | -12.51742 | -48.30378 | 2026-06-21 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2aca1d6e-756a-3d87-b328-b06b6b4a3f41 | -8.0099 | -46.44884 | 2026-06-21 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 873acfe3-a7ac-35b0-87b4-3c87bfffaf94 | -11.54804 | -48.26472 | 2026-06-21 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5f4f28d-473a-3ab1-9b60-ea455ee7301a | -10.25591 | -49.60409 | 2026-06-21 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86066d57-6b6e-3336-ae53-ef2d9b0c4dfb | -11.11227 | -54.14194 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| bc4c95ad-bd47-35c7-96e7-3c0f8a4c8d01 | -10.83729 | -49.11984 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc358fcf-d455-347c-9d18-09e7c47bd228 | -11.1993 | -46.77734 | 2026-06-21 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56e13d90-9c1a-348d-bf4e-a63f1586ebce | -11.3051 | -54.72493 | 2026-06-21 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8617b3b3-fbd1-391e-9f40-3b00aae963e8 | -11.64601 | -52.87089 | 2026-06-21 04:44:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e65ad9e4-e338-30f1-b101-924f24c1913d | -12.51449 | -48.29925 | 2026-06-21 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af070679-10ad-35e4-bc2a-25090d5dacee | -10.6917 | -60.74765 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21c97d49-8ad1-38a5-99ca-b3890027d17b | -9.29227 | -48.66637 | 2026-06-21 04:44:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90c31a20-b092-3b37-becc-ff4ec01377a4 | -11.64182 | -48.52825 | 2026-06-21 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ffa902c2-84e0-36d0-aeeb-27a2bfbfde39 | -8.00624 | -46.44827 | 2026-06-21 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6ccf6ec-78d5-3f1e-be01-e74279cea4a3 | -26.61944 | -48.7689 | 2026-06-21 04:46:00 | NOAA-20 | SÃO JOÃO DO ITAPERIÚ | SANTA CATARINA | Brasil | 4216354 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d10757ae-07ad-3536-8466-f7c2510ae2d4 | -27.98265 | -54.68656 | 2026-06-21 04:46:00 | NOAA-20 | CÂNDIDO GODÓI | RIO GRANDE DO SUL | Brasil | 4304309 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3d3c50ee-d974-30ef-ba84-229e24546024 | -27.84944 | -53.96891 | 2026-06-21 04:46:00 | NOAA-20 | INHACORÁ | RIO GRANDE DO SUL | Brasil | 4310413 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f028c3da-f083-3786-98b7-c98b901b3acd | -24.94411 | -53.44604 | 2026-06-21 04:46:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 71870bab-4023-396f-afdb-2d603f462d39 | -15.81074 | -58.64917 | 2026-06-21 04:46:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f23a0708-d46a-3241-af89-d6165d92f718 | -21.35782 | -54.05188 | 2026-06-21 04:46:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 740684ae-9bcf-3f69-945e-35c93c33cbde | -16.0603 | -42.0908 | 2026-06-21 04:46:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| dc6c4d99-0ed5-3215-8667-41fc855acc98 | -17.61456 | -46.69727 | 2026-06-21 04:46:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0d2adca-5e48-3269-8547-d99b52237d62 | -16.06071 | -42.08727 | 2026-06-21 04:46:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f2589436-a5e0-3577-b257-e3f7c1ed6a6d | -14.32921 | -54.96999 | 2026-06-21 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80effec9-4f91-398f-891e-4b6de35cd457 | -18.77069 | -40.90459 | 2026-06-21 04:46:00 | NOAA-20 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2d8c1416-666e-34e3-ae6c-252e8e517b9b | -15.92353 | -46.88228 | 2026-06-21 04:46:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4abc005c-3595-3244-95b6-ddc450a81d3d | -21.46498 | -44.31848 | 2026-06-21 04:46:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5ab7b9ac-a4cf-34c6-815a-6919b12832a4 | -14.9121 | -51.9968 | 2026-06-21 04:46:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8f68440-8fa9-3739-bfda-eeb245670e45 | -15.22814 | -50.8553 | 2026-06-21 04:46:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2df4488e-7021-383f-8b80-1c596a9d7032 | -17.61407 | -46.70105 | 2026-06-21 04:46:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 462b3183-fedc-3f5f-a528-7683e0c19506 | -16.46313 | -53.07946 | 2026-06-21 04:46:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee163bc3-65e8-3340-b20e-1edc29f24424 | -16.93571 | -47.13147 | 2026-06-21 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e88e98c8-541c-3063-912a-2d812f196c65 | -14.91153 | -52.00038 | 2026-06-21 04:46:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9243695-ffc8-371b-bc01-d476fa1f2ba4 | -20.51898 | -48.75089 | 2026-06-21 04:46:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29edf0a9-0b34-33cd-beaf-cd5c40eddcd9 | -23.4563 | -46.74516 | 2026-06-21 04:49:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0560a270-fc72-378b-9b17-5d6572351e89 | -11.0979 | -54.1311 | 2026-06-21 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.1 |
| ee338bb8-12ef-3cb4-882b-8f8db558389c | -11.1165 | -54.1499 | 2026-06-21 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| c52dcb00-acab-314d-9291-759e528d2e14 | -11.1168 | -54.1294 | 2026-06-21 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 30437afd-89b1-388f-944e-7fbfa5384ac1 | -11.0976 | -54.1516 | 2026-06-21 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 174.9 |
| e5ad1f9a-cf1d-3bf7-aab4-e4f3bf3d95fc | -11.0979 | -54.1311 | 2026-06-21 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.8 |
| c8a49b32-5e44-30ae-bc87-66703de7402f | -11.1168 | -54.1294 | 2026-06-21 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 87f2b924-f3ea-3e36-95de-d1f8ea6cf862 | -11.1165 | -54.1499 | 2026-06-21 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 566ad4e6-0b73-3790-bcc5-de80924757c7 | -11.0976 | -54.1516 | 2026-06-21 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 183.1 |
| ccf33a17-58dc-30d5-93e4-f9815439ad6b | -11.0979 | -54.1311 | 2026-06-21 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 32c7a833-7bd0-3bdc-bd5a-b27a5a72cc44 | -11.0976 | -54.1516 | 2026-06-21 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 180.8 |
| 6f15c1a9-de52-379e-892e-d5cc6a9cf730 | -11.1168 | -54.1294 | 2026-06-21 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 7cd79818-3b23-3130-a69a-73249b3a71a3 | -11.1165 | -54.1499 | 2026-06-21 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 9906b72e-2dc2-39c1-987a-548913caa3d8 | -11.0976 | -54.1516 | 2026-06-21 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 183.7 |
| f82a9b65-a47b-3b40-acd5-b89992ba7f73 | -11.1165 | -54.1499 | 2026-06-21 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 00d09826-f021-3e3b-922a-4a7865e599ab | -11.1168 | -54.1294 | 2026-06-21 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 87477db9-d4c8-3d86-ad86-02f4ef33a9a1 | -11.0979 | -54.1311 | 2026-06-21 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 155.5 |
| ca018dfa-065a-30ff-9204-827ebbbf2608 | -4.35146 | -47.76539 | 2026-06-21 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 25ab55d8-315a-39ff-bfa8-fce81a81b215 | -3.85392 | -54.22221 | 2026-06-21 05:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f2d5d5b-8d69-3b48-8e58-5b3ae9af16ef | -8.4638 | -51.5349 | 2026-06-21 05:29:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df934736-94d6-3adf-85d7-7093279aa593 | -10.15582 | -51.64679 | 2026-06-21 05:29:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f73dc1a-537c-3d0a-a093-eeb78a097f1c | -8.35612 | -50.50012 | 2026-06-21 05:29:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e0e5fe66-2d32-32d7-acb8-61e48476b719 | -11.06937 | -52.46614 | 2026-06-21 05:29:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c29b2f6c-47cb-3668-9701-aa38cfd13ec7 | -11.06887 | -52.47035 | 2026-06-21 05:29:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51e7b2bc-f80d-383e-b3cd-5a212899eadb | -8.46111 | -51.53399 | 2026-06-21 05:29:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
