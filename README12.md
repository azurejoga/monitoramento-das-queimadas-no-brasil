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
| 7207fdce-2223-39f5-a8b2-6d7fb3d25ba4 | -3.49668 | -48.03916 | 2026-06-09 05:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ada6c7cc-0696-30be-ab69-539933efac98 | -3.50132 | -48.03992 | 2026-06-09 05:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f521a70-943c-3c29-9b73-d95fa8c501ee | -10.03785 | -54.57904 | 2026-06-09 05:08:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 499efeae-3716-33f2-96fe-1febc7fbaf7b | -6.6434 | -43.92122 | 2026-06-09 05:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cdd5a83d-e655-30b3-8072-a77fceef900a | -9.31575 | -45.48847 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c9da643b-34df-3bf0-8629-e071e1f921c7 | -11.64939 | -52.86327 | 2026-06-09 05:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ece2b4ec-f37c-3794-85b8-a030486f54d1 | -5.80637 | -43.79343 | 2026-06-09 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c6393ac-ed44-3403-9f41-49adab6c7e6b | -10.85472 | -53.73835 | 2026-06-09 05:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d583997-2ba1-37cf-a561-8a3bc1d45659 | -11.54524 | -52.78361 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 813dc2d3-5dac-33aa-9299-7c879d6579e2 | -6.6419 | -43.91843 | 2026-06-09 05:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a4383603-b71f-3ee9-a570-a6c2f59eb98d | -10.38767 | -49.44948 | 2026-06-09 05:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2739515-711f-3a47-b213-d036ce1c5e3d | -11.5522 | -52.78115 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a193e1c7-4e48-357a-a21b-b5670a127197 | -10.64406 | -49.38593 | 2026-06-09 05:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| fa13c020-05e9-3f52-9d82-f398c62f0648 | -11.54838 | -52.78059 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4d81c99d-6ffb-38eb-b0ad-89239e2fbc80 | -11.54456 | -52.78001 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| aa55df25-07a8-3200-bab4-f06d6ec41f07 | -9.22169 | -48.56776 | 2026-06-09 05:08:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 389dabde-9d87-3d84-a18a-382274f3092e | -10.23131 | -47.42566 | 2026-06-09 05:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b672aade-3f3d-3355-adf0-12e269d15c41 | -9.89578 | -47.86023 | 2026-06-09 05:08:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 482be725-be57-3189-82d2-fdf41ed871e5 | -10.90627 | -49.35386 | 2026-06-09 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8ca5b78-fffc-3853-9ade-f204f85977d0 | -10.5746 | -57.32098 | 2026-06-09 05:08:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c4500e5-1d27-3ab4-b727-d5bb89a5487c | -11.64531 | -52.86049 | 2026-06-09 05:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51a8115c-27a6-3ad0-b0fd-d5a39f42cc74 | -11.55153 | -52.78592 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6f986d8-1a80-338d-8c2c-d2620f27e7cc | -9.29343 | -45.47221 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae62e5c2-26ad-3c67-84f5-229c48b0b45b | -10.90152 | -49.35324 | 2026-06-09 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6416bca-57d7-397d-85f5-20f1a75cdf90 | -5.80034 | -45.11413 | 2026-06-09 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ede0bac-8f25-3549-8dc4-8ef698db18d3 | -10.71429 | -56.24476 | 2026-06-09 05:08:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71c2c208-6782-361f-b337-36a36afe4d52 | -12.48376 | -46.26941 | 2026-06-09 05:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f61476fb-44c0-3614-981a-d505e78011e3 | -11.5439 | -52.78476 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1e7ea0f3-f923-3420-af53-cfc7f8737875 | -10.82759 | -56.6044 | 2026-06-09 05:08:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2460c417-5e92-34cf-939f-3c84e23bccb6 | -11.55739 | -52.78054 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 213fb3ee-50c1-34a1-9093-682e1e08276a | -11.05179 | -56.92764 | 2026-06-09 05:08:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1791490d-6824-3b80-bd7f-c8cd56a2a268 | -10.89204 | -49.35187 | 2026-06-09 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b49e137c-5391-3ab5-a854-cbe257d68f2b | -10.84862 | -53.75455 | 2026-06-09 05:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24d4a835-ff07-38b7-9dfb-859d76568899 | -5.80094 | -45.10989 | 2026-06-09 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f638b153-8a9d-340e-91b9-71f18a9dd7eb | -11.2676 | -53.97304 | 2026-06-09 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b123f1f-e3f8-37d2-a3c1-c80ce1ac46ad | -12.48414 | -46.26629 | 2026-06-09 05:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc5947b0-3478-38da-9ec9-e6ef9011e528 | -8.26267 | -54.96361 | 2026-06-09 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f697ea47-cede-38aa-80c1-eb6551e03f66 | -11.95795 | -48.52936 | 2026-06-09 05:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaa10cd8-3a8c-3805-b25f-1b37fd50d1b8 | -12.05052 | -49.76627 | 2026-06-09 05:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0481c94e-0324-3c6d-9eda-5413031b1f96 | -12.36318 | -47.89624 | 2026-06-09 05:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73e2faa0-fda1-34e6-97f2-b0f4ef52053f | -9.87605 | -55.93851 | 2026-06-09 05:08:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 724d7b01-a023-3660-8a35-8090fb474318 | -9.29887 | -45.47742 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74734ad9-277e-37c0-bdde-7ad0caded172 | -12.48335 | -46.27286 | 2026-06-09 05:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59921028-4b36-38cb-8416-b9269abb44e3 | -11.5532 | -52.80902 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32c13249-f38a-3a05-b706-286fae0b0851 | -10.92101 | -54.11492 | 2026-06-09 05:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80be4bf6-8366-3b70-80cd-b27738c64ee3 | -11.55268 | -52.80549 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb54dd6b-0775-3aeb-8fb4-a1a391d455c2 | -6.57263 | -47.9124 | 2026-06-09 05:08:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4085446-17bd-3fb8-9a78-70641876fd64 | -10.17533 | -51.66226 | 2026-06-09 05:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0c0b0b4-1380-301f-8d2f-3bc4764cc59a | -6.64408 | -43.91608 | 2026-06-09 05:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8c28723-e9e6-3295-947c-46773c4acc38 | -9.21674 | -47.33504 | 2026-06-09 05:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eed2f79b-5f10-3a1f-a41e-d7401cc1a1e1 | -9.30612 | -45.48505 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b5a9e8d6-eaf5-3ae5-83ed-b95214d45e6f | -11.95757 | -48.53239 | 2026-06-09 05:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8a578c9-10d3-363f-86ee-eb9995145058 | -8.97878 | -47.9813 | 2026-06-09 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b3fb2280-7880-356c-b1f7-2fec4fa8afa4 | -7.37624 | -49.855 | 2026-06-09 05:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d4c8044-e2af-3f5c-bf90-6b7a325397cc | -9.07643 | -50.59996 | 2026-06-09 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 97575e74-166c-3904-9213-e8e3857a394e | -12.05655 | -49.75689 | 2026-06-09 05:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f2b3d788-96e4-3c28-ac88-fda80788e9c6 | -9.31159 | -45.49026 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 131cca59-5e10-3971-973f-c2832873df24 | -12.05119 | -49.76126 | 2026-06-09 05:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7242dfc7-6a30-3ac4-9ad0-d77a6cfc2cbc | -11.26526 | -53.96431 | 2026-06-09 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9fc7135-7429-35ca-a998-6abf937146d6 | -9.30489 | -45.47808 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e7f8a7b5-99b3-3218-8ea3-6bda42653ef0 | -6.64832 | -43.91911 | 2026-06-09 05:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e10c2a6-7c1f-3fa1-b87b-2481efb7fa32 | -11.55602 | -52.78172 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0243c07a-a22c-3ade-a13d-ff66f90951e1 | -9.2241 | -48.56599 | 2026-06-09 05:08:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55c9d9c8-8450-3fec-acd1-22eb4690a123 | -10.25879 | -52.07991 | 2026-06-09 05:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a005b806-afb8-3ec3-960c-6c2d8c6d07c7 | -9.07219 | -50.59934 | 2026-06-09 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0fe1d709-14cf-3eb9-8f9f-ecc07ef0b9ac | -5.84131 | -43.48101 | 2026-06-09 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 658f6376-9504-35e3-ad83-3e263d2ec318 | -9.33847 | -47.91312 | 2026-06-09 05:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b255136-44d7-38f6-b18f-9d00af898490 | -11.54594 | -52.77885 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b39aa57c-f459-3fd3-bccd-fb4141780194 | -10.89467 | -51.16049 | 2026-06-09 05:08:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48697098-ede7-3917-b0c4-399bf6202a30 | -11.64558 | -52.86272 | 2026-06-09 05:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e32105c8-73e6-3073-af23-db68158cdc80 | -11.0551 | -56.92818 | 2026-06-09 05:08:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b518a7b5-8f82-3754-b799-d0e108b85973 | -8.71635 | -47.91794 | 2026-06-09 05:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2b0a1c8-414a-3142-9fc8-5fe267ef6b29 | -11.33259 | -51.39597 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f548f2c-d583-3497-8b95-aa9ae72bb6ee | -10.89678 | -49.35258 | 2026-06-09 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cef0fb0-cc10-34b8-9160-713cd1439afe | -5.84057 | -43.48634 | 2026-06-09 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 86182774-92e3-3466-bb84-016abac2746a | -10.57129 | -57.32044 | 2026-06-09 05:08:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c4e294b-7cae-34d9-bb91-c015a8740e1f | -12.36362 | -47.89274 | 2026-06-09 05:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49eeea51-c08c-3fed-b3b4-bfe3b4b7050a | -9.07532 | -50.60786 | 2026-06-09 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dceea539-3650-399d-b305-e10d85303f99 | -12.03839 | -47.80309 | 2026-06-09 05:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90da0df1-d6f3-310a-9ba8-43ee9bcd259d | -5.92785 | -43.47907 | 2026-06-09 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fd08e2b7-b5a3-3c69-9e12-44267cb76961 | -9.30122 | -45.4753 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 554712a7-bd49-33c5-82a1-a763bef6f7db | -9.29946 | -45.47289 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d17fbba8-7e2b-3fa0-b0ee-c6e4b06c67d5 | -6.85522 | -45.00843 | 2026-06-09 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 205e4ff1-0482-3bae-adae-ea2fc0746803 | -6.85582 | -45.00401 | 2026-06-09 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b29a78c1-1c92-34af-abe1-26cbed0c8649 | -9.21113 | -58.06813 | 2026-06-09 05:08:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b57b759-fa9b-3486-bc39-fb7c5de57f9d | -11.54771 | -52.78535 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b5195505-94a2-3c54-8a78-063650d4bce0 | -10.77175 | -54.09772 | 2026-06-09 05:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e282f2e-e953-3469-b16c-b58ade91b6c6 | -11.55287 | -52.78473 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6d39b94a-8a87-33e0-981d-e41ba7a8b9ba | -5.80155 | -45.10556 | 2026-06-09 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a977227-526e-3959-8957-acd540cf0673 | -11.26465 | -53.9684 | 2026-06-09 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 637aaa84-1314-3128-b404-412d0ce278b8 | -12.05588 | -49.76192 | 2026-06-09 05:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d708e4e0-c2ac-3f5c-bdd9-2809a4b25ddf | -8.74153 | -49.46914 | 2026-06-09 05:08:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f372395a-c767-3988-9310-c895bbfe0fbc | -11.33311 | -51.39214 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bf1a482-3f89-3487-8e6c-32f4a9aa642a | -10.92108 | -54.1138 | 2026-06-09 05:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a03fc709-c82f-306d-b72a-fd65bf3b19b9 | -9.31761 | -45.49097 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a56b664-a269-3feb-956f-19917bd6c44a | -9.31033 | -45.48326 | 2026-06-09 05:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f722d797-fa66-3166-913c-dfc4383931c0 | -11.26732 | -53.96785 | 2026-06-09 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2ab397f-dffa-33f8-a061-ca20b1805f18 | -9.07163 | -50.60331 | 2026-06-09 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 778eccaa-606d-3f8c-926e-dd6b18c85fcd | -8.97332 | -47.98344 | 2026-06-09 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bcf07cff-e9df-3c09-a546-4080c3959fc6 | -11.33207 | -51.39979 | 2026-06-09 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
