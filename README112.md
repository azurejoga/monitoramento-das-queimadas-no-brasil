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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7eab34cd-dd96-35ba-8c18-49f7e2562ee9 | -10.91302 | -48.31903 | 2026-09-20 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 2747e3b8-31ec-3677-b29d-754660a551b6 | -10.85374 | -50.17225 | 2026-09-20 12:06:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| de38590f-d711-3fe8-a0fc-1bbde194a8c9 | -11.12872 | -54.02008 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| da8be55b-568b-3a67-af4b-31cad50eec7e | -10.87359 | -50.17486 | 2026-09-20 12:06:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 5ac27d19-554a-3965-8bf1-b3af9f4b7851 | -10.2682 | -50.2752 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 9a314772-6e54-30ed-8603-051862ca20db | -12.7711 | -46.2299 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 72418db1-c9a3-3f86-b5cd-753e531d6255 | -14.66897 | -46.7134 | 2026-09-20 12:06:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 34.3 |
| a63e0bdf-56c3-3b8b-9450-d330b2ba0482 | -11.37263 | -51.42659 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 252.1 |
| 88590aec-0806-393c-9b0d-0c686f2c79d6 | -11.22173 | -54.07696 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 27d965bf-1196-35b2-878f-d8d9b3c40c88 | -10.38815 | -48.99886 | 2026-09-20 12:06:00 | TERRA_M-T | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d241f96e-579d-3358-bda0-d85f80b69185 | -12.76957 | -52.85842 | 2026-09-20 12:06:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0ca2fe65-21e7-358b-91a6-3c450f64971c | -12.76269 | -46.1791 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| ef1975c2-b81d-3303-85ec-ebaf7a13e767 | -12.17016 | -47.04012 | 2026-09-20 12:06:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 88ce1a31-067e-3731-927c-6484c8f85104 | -11.01788 | -48.30743 | 2026-09-20 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 5862c9cc-ef3f-3a60-bdb8-69306918f086 | -11.92649 | -49.78354 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| c380a4c9-676e-308c-b44c-2b0802c75b91 | -12.52627 | -50.03155 | 2026-09-20 12:06:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ac405352-b341-3ed7-9a6a-4c192f02ab7b | -12.77386 | -46.20547 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 419.7 |
| e2c36c03-70e9-3d47-b8c4-c0b8612919d3 | -11.01565 | -48.31414 | 2026-09-20 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 20412e59-a90e-3ed0-ab6a-d903f37089cd | -10.33438 | -50.24462 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 815a7b0c-79ee-3e9e-9734-8a609fe93076 | -16.40649 | -54.70956 | 2026-09-20 12:06:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a6b03245-18c1-3f0e-8dc8-68cc5f6a6a82 | -10.31913 | -50.2085 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 91a7646a-65a5-344c-91df-a3e10fa9beef | -19.19668 | -46.8448 | 2026-09-20 12:08:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 7eecb93c-9404-3456-8ff8-8cbc71c2882d | -19.195 | -46.83798 | 2026-09-20 12:08:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 8d045b52-5257-360e-812d-e3fa224f0c26 | -18.79281 | -46.48554 | 2026-09-20 12:08:00 | TERRA_M-T | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| b05f4997-c8d7-36e1-9685-3f1cad6930c5 | -18.79285 | -46.48016 | 2026-09-20 12:08:00 | TERRA_M-T | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 86752ffc-b6f3-3aae-a6c9-62c06805e40b | -11.379 | -51.42 | 2026-09-20 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 280.3 |
| c7f5c12e-cccb-3a57-8d0b-1baa28b797a8 | -7.1742 | -47.4736 | 2026-09-20 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 32cc2cd6-1075-3076-984b-d3352aad820d | -10.8656 | -50.1989 | 2026-09-20 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 4019b3fd-9a84-3aa6-a7ea-1a16cea6a3a6 | -11.3793 | -51.3989 | 2026-09-20 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f5d3e500-f5a3-3e7b-8ecb-9d6557255698 | -12.7621 | -46.18 | 2026-09-20 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 309.0 |
| d5ad7e50-1f50-3762-a05f-409a82d3aa1b | -10.8469 | -50.1795 | 2026-09-20 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| d459c93e-5cde-3d50-86c8-e2668d6ac455 | -11.118 | -54.0268 | 2026-09-20 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.0 |
| f62f01ee-0a9e-341a-ab43-7d5bb5d453e0 | -12.642 | -50.9359 | 2026-09-20 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 293.2 |
| 2e6e756d-996d-3421-ab64-77722977b99b | -10.2787 | -50.2605 | 2026-09-20 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 98db609a-4c89-30f9-bf70-d6bd3ee1c025 | -11.4537 | -45.3892 | 2026-09-20 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| db771864-b29b-3f9c-86eb-18be1706d7f7 | -14.6661 | -46.6919 | 2026-09-20 12:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 241d5ea6-d42d-3d19-9f33-07242c930c2c | -12.152 | -47.0383 | 2026-09-20 12:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| eb18871c-b629-3f14-a6dc-3cf151b8eebb | -14.6665 | -46.669 | 2026-09-20 12:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 4856eae7-24c3-33d1-affc-95e5f05944fe | -7.174 | -47.4956 | 2026-09-20 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| cb1c9162-0309-3c81-a99c-fe12e9cae238 | -7.5522 | -45.435 | 2026-09-20 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 47bbd24a-e39d-3a2e-9993-68e86b9aa593 | -7.5337 | -45.4141 | 2026-09-20 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 437.1 |
| 0e04f714-016b-30c8-adc6-4da5faffcaf2 | -12.7616 | -46.2029 | 2026-09-20 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1249.5 |
| 2cc72ef7-b461-33d3-8132-71765b4fb5fa | -8.3965 | -45.6244 | 2026-09-20 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| e53de10e-67e8-392b-a59a-850ed2778402 | -12.2344 | -50.1488 | 2026-09-20 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b217cf96-6133-3328-b359-5e802a83bda6 | -9.8316 | -48.3854 | 2026-09-20 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 108f47b0-adb2-3c8c-a1ed-4f0f322cd9fb | -7.5334 | -45.4367 | 2026-09-20 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 372.6 |
| 18c8b30e-f5e0-3b24-b9f9-879521e61d7e | -10.473 | -51.2808 | 2026-09-20 12:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 0d081b68-e511-3d71-b0a2-bb36c3dd33eb | -11.398 | -51.418 | 2026-09-20 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 6cc6db35-0c75-3ece-856e-9b8799a0df35 | -14.1458 | -45.5638 | 2026-09-20 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 8dc9a463-cb48-3d87-ba7e-9b5c873d8d7f | -11.3787 | -51.4412 | 2026-09-20 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 9d8c1e14-568d-3ee6-9b51-85bd66522e3b | -11.1183 | -54.0062 | 2026-09-20 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 4761098a-0c6a-3b25-ac02-c9c40c67247d | -9.8313 | -48.4073 | 2026-09-20 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| be08186b-f1e6-3eb9-ab52-572fbdbd8f2c | -11.0991 | -54.0285 | 2026-09-20 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 6f421a0e-afc1-3549-9ab2-f101f306afd0 | -11.6609 | -43.4239 | 2026-09-20 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a2e5effc-35c7-33c6-991f-0d2c960deb09 | -10.3914 | -48.9133 | 2026-09-20 12:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8c064b2f-6d18-3706-b49e-718566455872 | -12.1328 | -47.041 | 2026-09-20 12:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 48f55379-b943-3edf-ab1c-96bead5c8f78 | -12.6423 | -50.9144 | 2026-09-20 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 6dc357bc-6f9e-3995-a3ca-99e54c80db47 | -10.8659 | -50.1775 | 2026-09-20 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 207.5 |
| e126280a-fe81-3cdc-b9da-0cdd0654772f | -12.6615 | -50.9121 | 2026-09-20 12:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 94714d3a-0a8d-3c5f-b0cb-f538cad45b87 | -7.5525 | -45.4123 | 2026-09-20 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| cae1c940-073a-3f13-ac3e-7e9fce7f42f5 | -12.2341 | -50.1703 | 2026-09-20 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 7d59ad61-2c4d-3fa2-9860-11875cc81679 | -14.67 | -46.71 | 2026-09-20 12:15:00 | MSG-03 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6ead7731-5c24-3767-a5ac-4ce4f5716c85 | -14.67 | -46.66 | 2026-09-20 12:15:00 | MSG-03 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ca8a0b83-b6b9-3260-87a5-19a4d12e9670 | -11.3787 | -51.4412 | 2026-09-20 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 9439dfeb-323f-30b2-ac55-0730d4e599f8 | -12.7616 | -46.2029 | 2026-09-20 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1178.0 |
| 687a3c7e-14bd-319d-9e37-3e3a7989cbad | -11.4537 | -45.3892 | 2026-09-20 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 127a0c53-e673-370b-b313-3937592ede7d | -7.1742 | -47.4736 | 2026-09-20 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 9146fb21-2121-36fe-aa23-f8d4cf548cef | -10.8469 | -50.1795 | 2026-09-20 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| f6712d71-01cb-3bde-8e95-f10c20f9a1f0 | -7.5334 | -45.4367 | 2026-09-20 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 544.3 |
| 216e4d8c-6c97-3a78-9554-120985de7ea7 | -10.8656 | -50.1989 | 2026-09-20 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 5225b0f9-013b-3f57-b709-1161e264d7e0 | -9.26 | -45.9616 | 2026-09-20 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5518bdc6-b504-3d5d-af0a-e822e3f550bd | -12.1711 | -47.0356 | 2026-09-20 12:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| e73ec27b-4d57-3a2a-952c-20ee914607c5 | -9.8502 | -48.4053 | 2026-09-20 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 15a8e335-95b7-331b-a545-4c8ab1d0c9d1 | -17.5795 | -44.9765 | 2026-09-20 12:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 94dfd565-4804-3282-880a-2fd71193551b | -7.5337 | -45.4141 | 2026-09-20 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 433.7 |
| e3afa095-bf8c-3cd5-9e6a-8213c9430606 | -10.41 | -48.933 | 2026-09-20 12:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 7989756c-f13c-39c2-b05d-5e87dad16878 | -12.152 | -47.0383 | 2026-09-20 12:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 23e745fe-6599-32d4-b9c9-c36c4994648f | -10.3914 | -48.9133 | 2026-09-20 12:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7bde8295-d7d5-3a95-9c3c-33bdd56137f5 | -10.8659 | -50.1775 | 2026-09-20 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 243.3 |
| e87e51dc-7d73-359f-ab3a-6d1c1f9b3587 | -11.6609 | -43.4239 | 2026-09-20 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| dfe5fbd0-6343-3c62-9be9-0460591b7187 | -11.4924 | -45.3608 | 2026-09-20 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 36f8c4a5-9646-3ddc-b00d-0a96f91af989 | -12.7621 | -46.18 | 2026-09-20 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1201.6 |
| e59e45f7-4326-393a-9749-6c99642d6244 | -12.7423 | -46.2058 | 2026-09-20 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| a6bb521c-642b-38a4-8fc2-1b51a5724187 | -11.379 | -51.42 | 2026-09-20 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 337.0 |
| bb5d152b-3680-314d-a374-48053a55b299 | -10.6 | -50.2486 | 2026-09-20 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 779bc54c-eca5-34d5-b9e9-a87cef126bca | -10.2787 | -50.2605 | 2026-09-20 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 4cc84fb7-02f9-39f7-9240-f014df888fbb | -11.2118 | -54.0797 | 2026-09-20 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d476f18f-56fd-350f-a1cb-9aac13e9eca4 | -11.0991 | -54.0285 | 2026-09-20 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 018b7356-5469-30cc-a76b-4026fa5a8e9d | -12.1328 | -47.041 | 2026-09-20 12:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1d47bc32-d5d4-3b42-9542-a7a190a81636 | -11.118 | -54.0268 | 2026-09-20 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 84eea5b8-6d23-3ace-9204-743d2ee54d2d | -14.6856 | -46.6886 | 2026-09-20 12:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 296.4 |
| c340b07d-93b1-3792-babf-193b2eb76928 | -9.8397 | -46.4361 | 2026-09-20 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| a5006e23-54b2-3ecf-ace2-34019def65e1 | -11.3793 | -51.3989 | 2026-09-20 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| bb8d71ef-0f09-3605-9c71-e46a2628be2c | -8.1376 | -46.8155 | 2026-09-20 12:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 2976a9d4-d21e-3c07-8ef8-27018c635fc9 | -12.7428 | -46.183 | 2026-09-20 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 264.3 |
| 04f9e0f0-0a92-31d8-9028-6cefa5685c29 | -11.1183 | -54.0062 | 2026-09-20 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| abd4a2df-0bfc-3cdc-8566-c6d766cb16dd | -7.5522 | -45.435 | 2026-09-20 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 98b3bd66-61e9-3c14-902b-9d2cb822a472 | -14.6661 | -46.6919 | 2026-09-20 12:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 11a2d802-577c-3c92-83a5-f21ac934dfa6 | -14.6851 | -46.7115 | 2026-09-20 12:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 85330a16-404f-3ec9-a0af-6340a8215242 | -12.6423 | -50.9144 | 2026-09-20 12:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |


[Clique aqui para ver as próximas entradas](README113.md)
