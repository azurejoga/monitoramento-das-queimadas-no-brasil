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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff5ac38b-e6a6-3fa5-8320-7a7f9f44964b | -11.4972 | -44.99326 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 360dce9e-3c15-36d7-8cb0-02976e98d6cd | -8.62562 | -55.0008 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f179cf23-1e4f-377c-a943-7cc64173703c | -8.35269 | -46.83711 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c51aebfd-e347-3b89-b718-e20bb74b7898 | -15.3518 | -46.29429 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc71a0d1-2dd6-37cc-b5e8-2fc66ffb17eb | -14.56791 | -48.95166 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 539417bf-22ae-3eca-b84a-7241099429bf | -13.33119 | -47.79136 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c9a45da-fe6e-39d9-9245-91a0c1f5a16f | -13.31599 | -47.26282 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43e2c963-3412-3428-bf7d-9e65cad8c7a1 | -13.75883 | -48.05444 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b86e9fc7-12fc-3d86-9bdb-33c289460bb1 | -14.35447 | -46.10979 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 116da95c-810d-3482-9aab-6a65ed9e7c7c | -11.92684 | -46.37594 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be79a84a-de15-3789-a5f9-3419656ae255 | -8.83991 | -46.83823 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f198cc1a-692c-3762-a0d9-fb59241f1cbe | -12.78372 | -47.7224 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae9c4179-db6b-3376-b972-e5cef19951fe | -14.23745 | -46.09734 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 838163d3-8431-3333-bf07-2ec355fd423b | -10.64003 | -49.16048 | 2025-10-04 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e746836-fe4e-3ea3-93e8-84c5585d177b | -14.92656 | -48.33561 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35721a4f-9962-322d-b047-def13cb0bacc | -11.31524 | -47.84352 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05185d4e-2a3d-39d0-8b72-be8f829b521c | -13.34594 | -47.21387 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6863ecb0-b4d6-35ba-bbdf-90e36e9060dd | -9.91007 | -43.80293 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0cf5e95a-ef8c-3fab-8da5-e57a8f15764d | -13.99218 | -48.1825 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7cb0f6e-f57a-39c9-b586-a1eae9e7fa46 | -11.26291 | -47.79227 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a4fe7ed-09d0-3350-bfa4-069177c8a5e9 | -11.44872 | -49.71552 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce5d9fac-c056-3eff-b512-394a1bfa4df7 | -12.82907 | -43.80996 | 2025-10-04 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25f22206-0fad-3433-98cb-c2c139a86135 | -13.64326 | -48.6814 | 2025-10-04 04:14:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c0d2327-0c79-30d9-9712-29b7fa2c6a1a | -13.40778 | -43.69032 | 2025-10-04 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f50a5cc-9167-3aa8-b028-f5e9172092c2 | -8.09839 | -47.99689 | 2025-10-04 04:14:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bca293c5-594a-319b-8865-5e6c00f0e6f0 | -12.81735 | -46.86541 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d2fe3633-8669-3c33-acd8-53fbad7b2e91 | -9.66506 | -48.22752 | 2025-10-04 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08ee729e-1174-3dfa-8e25-6baf24554710 | -14.38464 | -48.47847 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d04dddd-89c1-3799-87c0-f3edd6a6c7fa | -12.29436 | -45.35968 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b6054d9-e528-3c9f-827f-96a86038f133 | -14.67875 | -45.17735 | 2025-10-04 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c789ccfc-fcc9-3e5f-80ae-c71dc7bb639f | -13.20614 | -47.82 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 653ea375-0ce0-39b3-b0c9-802c2b9879ec | -13.74254 | -47.93177 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0190650a-10d4-39bf-b43a-7b9da9e1ae82 | -7.72686 | -46.29339 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16295709-4776-3511-ac81-f4052628efb0 | -13.12911 | -47.83053 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f722ba81-10cf-3ff3-8875-51ad531bcc98 | -13.50938 | -47.27826 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7ad11f7-ddad-3518-9145-37efc24b5326 | -14.72647 | -48.08026 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4cd4e9df-b561-3f93-9cd7-41136e200dd1 | -11.49707 | -45.01522 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f697956-1289-3019-9c05-100ac7821269 | -12.36782 | -46.51202 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6db2a52e-0181-3698-8cea-00b9a81eba2e | -13.92818 | -48.16132 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c4e5903-f580-32c0-9c41-1c6694bf747e | -11.78667 | -46.8221 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 30cd324d-24f3-3631-af05-ce17f40febc1 | -13.74785 | -48.07485 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f03a8df-7963-3a7c-9418-a82ccba137d9 | -7.72551 | -46.30158 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e188e037-2113-32a0-b442-583fdf7cce1c | -11.91398 | -46.38935 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b964a974-7275-37cc-a72c-38f04a628c9a | -13.10955 | -47.90119 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2e82734a-27b5-3582-892b-932eedb60bb3 | -7.73489 | -46.31166 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 004aa204-35c2-3b5d-8fe2-1a794f01906f | -9.32796 | -45.75056 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 140464cd-ddf5-3bf9-b974-6a8507d3a4b8 | -12.70179 | -48.55238 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f1f332c6-d982-3844-966c-37132ff6e0d5 | -13.74712 | -48.07909 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31bc7770-1947-3990-b8ce-4cda4a59dfc8 | -11.82223 | -45.04377 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 112fee32-b464-3090-a2be-f4b65b5288f9 | -14.07674 | -44.25528 | 2025-10-04 04:14:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e4a9107-d6b5-33a1-a1d7-b37344466683 | -7.73874 | -46.26589 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab1d70cf-2216-36e5-aef9-213783f63bff | -11.91614 | -46.39766 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 826e3daa-59b6-31af-9447-832e6da0dbf3 | -10.33146 | -50.33381 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 93185eb8-7af9-3ad2-ac4b-855457b8ffa7 | -11.7984 | -45.02499 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cd2aaff-09c0-3266-a99d-bc82bc50d43c | -8.84389 | -46.76959 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a553e07a-8362-30e8-9879-cc366af7a5b0 | -13.16842 | -47.88478 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcaeafb4-92b0-3830-96d0-883824b24613 | -12.65286 | -46.9986 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 408a9888-a9df-35a8-95f9-f3b26746907b | -13.9936 | -48.19469 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d66756fe-9442-387d-bb99-23ac48f16ffb | -15.30944 | -46.27922 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b10cc870-ae18-37ba-80dc-f2cd84e30e83 | -11.11436 | -47.88195 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dae5966-db23-3eee-add5-a5af9d6b6e39 | -13.2621 | -47.23805 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f481cdf-1747-3e9d-a3a8-c8574a27bdb1 | -13.97894 | -48.1941 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3425a89b-c28b-3536-9872-3c706455c62b | -9.93272 | -50.23639 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7cf272c-a509-3864-940b-b3c849436a91 | -11.14183 | -48.11266 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 196a2e6f-0d2c-3397-8b99-e46bd36e479b | -12.23066 | -43.7725 | 2025-10-04 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07ecfc44-e821-3b4e-a69e-c12e1cc7f029 | -11.4652 | -45.1489 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b8d2c64-dab2-35cc-a496-5a64250e6745 | -11.11602 | -47.88039 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 188ee74d-f0fc-3de2-a81a-31e4dd6aae60 | -11.79783 | -45.02856 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 603ab563-e27f-3d16-ae77-a911ade124fa | -14.68157 | -48.27649 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27892b09-5948-309f-a392-e08ece6ba8e0 | -10.99212 | -46.67241 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dee7e41c-eb15-356f-a81e-ffc4a35bcfe8 | -7.7695 | -46.27989 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e71727f8-c15b-30d7-9a9c-f79d81f8bc94 | -11.54462 | -47.66052 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7de730c2-f078-3cbe-850d-47ffe7ef9572 | -14.32421 | -45.86129 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ca41ef2-0f3b-3b0c-a061-216de63d7449 | -9.37081 | -47.63231 | 2025-10-04 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bef80b52-cabe-34c5-821b-b33f3335444d | -10.9698 | -49.56758 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d495153-c9b1-3613-be77-b3e162ac959e | -10.32916 | -50.34689 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78df2120-4b8d-34fa-b9ca-99ba87d4b604 | -13.5164 | -47.27956 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 937d7c0e-8f54-32a0-881b-0bc1728211d1 | -9.34646 | -45.78878 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7081def6-d0d8-3004-b76f-0d94d192dc58 | -14.38371 | -48.47611 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 721f6f1e-c58c-3e3e-97bf-9e697a69eec7 | -10.84555 | -47.20171 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2cee363-07db-37d7-b1c1-13039254891e | -11.46187 | -45.14833 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e027344e-1fb3-336f-94dd-da58260dc879 | -13.68127 | -48.04633 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2308868-9d7f-3fc2-b78c-3ab4254ab969 | -9.90949 | -43.74204 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ee7e5330-460a-3c5c-bc1f-23d00fc52ae5 | -11.80202 | -48.91291 | 2025-10-04 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bb12f2d-a4ff-3128-a9ae-9b59a1b69c54 | -12.64569 | -46.97668 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f7fc31d-deae-3b82-9b3a-e454f347d0ff | -13.33902 | -47.6167 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15ebd94c-4cb3-3ade-aa82-fce2c08f04ee | -13.55093 | -48.2128 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2d22e44-4e31-3d29-a0dd-1286b2d578d7 | -12.19615 | -47.77854 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2750ed5a-80d9-37e4-aa2e-43d63e6ad470 | -11.12632 | -55.4589 | 2025-10-04 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68601486-cfbc-336d-88aa-a67a79a6180b | -8.20335 | -46.99475 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bb545b95-fa48-33a9-b431-d74640ea946b | -9.33141 | -45.75108 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 539c557c-6b17-3295-a000-9b7363894424 | -11.55876 | -46.99335 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e700d19-30ab-3aa5-9a31-5ad095badb7a | -13.26511 | -46.47718 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b87e1c8e-126b-3e13-926d-4a9583ef38c9 | -13.77735 | -47.81538 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4111fc39-7b56-3de8-a75d-c20b047e438b | -13.11818 | -47.93832 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 428940be-25b5-3b09-8fae-5d79c4583e8d | -11.7945 | -45.028 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 682f217c-4eb4-3055-88a0-4dfed0f3df6f | -11.47871 | -45.02311 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f2a8e3c2-1e4f-30fc-95f3-077b92d85f6f | -9.13231 | -43.28537 | 2025-10-04 04:14:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 03fb44ba-674d-3678-b2a6-e0dad37fc8c5 | -12.42063 | -44.07827 | 2025-10-04 04:14:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01b81598-e625-3d8e-b049-cd1fe5d9be4e | -8.62466 | -55.00575 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README89.md)
