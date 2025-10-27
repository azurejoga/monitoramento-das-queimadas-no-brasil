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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2dc19db-f06b-3269-8ef9-429684cded1d | -3.0148 | -41.6851 | 2025-10-27 13:10:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| a68f2ff6-8b38-37c7-832e-adcdcc3911bf | -13.2455 | -47.081 | 2025-10-27 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 73c00bbf-4b86-311b-aede-58f7be0a16ca | -13.0569 | -45.8599 | 2025-10-27 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 84c1bbfe-ea49-3d6f-93d7-0043341a9998 | -4.3879 | -43.3129 | 2025-10-27 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 168.2 |
| ae76c754-97f7-3756-8d8c-0d7edcdf5926 | -4.3877 | -43.3362 | 2025-10-27 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c0e233b9-a8de-37a2-9958-44e0e32dbded | -4.914 | -42.9764 | 2025-10-27 13:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| cb7397a8-294e-3729-800b-27c087ebf0d1 | -4.4431 | -43.4259 | 2025-10-27 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 726e5321-1e4f-3dd0-ac2b-9bcea611f53f | -14.781 | -44.9835 | 2025-10-27 13:20:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 216.7 |
| f3506f16-3831-3b65-874d-c637bb1a94f7 | -4.8557 | -43.2607 | 2025-10-27 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 1b211494-d0df-327c-9bb0-6b901b779888 | -6.4067 | -38.4547 | 2025-10-27 13:20:00 | GOES-19 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 79575529-9e75-3458-8a63-d578328400ea | -4.3877 | -43.3362 | 2025-10-27 13:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 8de43cf4-e9ba-3b0b-af06-851850926d11 | -3.5834 | -43.5877 | 2025-10-27 13:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d0de9bed-c46b-3b0f-b314-c5176b6d75d9 | -14.3599 | -51.5281 | 2025-10-27 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| c8c27622-1c81-3643-a5ad-5d369c5eb43a | -3.6254 | -42.7699 | 2025-10-27 13:20:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 20869a78-ff7b-3aa0-9650-e3baf7928878 | -11.9501 | -51.315 | 2025-10-27 13:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 03518587-4a2f-38af-a033-0ac995bf6b14 | -4.0915 | -42.9329 | 2025-10-27 13:20:00 | GOES-19 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ad748bdd-efb9-3cab-8baa-4c533712ee45 | -4.9138 | -42.9998 | 2025-10-27 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| acffde3f-5be5-3854-8977-046237f2257a | -4.4665 | -45.4589 | 2025-10-27 13:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 76530db2-371c-338e-a9ce-ffc4724f78dc | -3.0146 | -41.709 | 2025-10-27 13:20:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 7ad303fa-bc2b-31ab-aa22-2b1f260fd22a | -3.3448 | -42.877 | 2025-10-27 13:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 2371a35e-979b-3b25-b0d6-b32bcd522d0b | -4.9146 | -42.906 | 2025-10-27 13:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 430a8bc7-51c6-39ef-b1fb-2090a9502902 | -4.9333 | -42.9047 | 2025-10-27 13:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 2988945f-3ea9-3eef-92f3-b6b4a8a4b211 | -3.3447 | -42.9004 | 2025-10-27 13:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 96709f0a-e771-3f0a-b379-1eda7c6a79ac | -4.8744 | -43.2595 | 2025-10-27 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 4fa098d8-b1e3-3cdf-8891-8a6ed6d1e6ba | -4.3879 | -43.3129 | 2025-10-27 13:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 81a386b2-e15b-31df-8209-262bca9126b8 | -5.6619 | -41.1099 | 2025-10-27 13:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| c277297a-50c4-3ae7-a3c3-fac3a0eadf30 | -3.5833 | -43.6108 | 2025-10-27 13:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 193.0 |
| c341a5ed-3b63-34a8-a429-dd9f7fd729d1 | -14.7816 | -44.9599 | 2025-10-27 13:20:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 8593567f-7c03-3bba-bcb6-393d1e050fc2 | -14.3982 | -51.5443 | 2025-10-27 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 89848def-1351-3b01-899a-e69c4f25cb9a | -14.781 | -44.9835 | 2025-10-27 13:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 254.7 |
| 03d2b4d1-0e25-3caa-b894-2769c0d7e6ba | -6.6745 | -41.5027 | 2025-10-27 13:30:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 226.8 |
| 70ce241a-d4ea-3587-811e-245c00bd4810 | -5.6431 | -41.1114 | 2025-10-27 13:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 120.5 |
| b6c52c77-565f-37bd-a760-a4d610c1ffd8 | -3.3447 | -42.9004 | 2025-10-27 13:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 8795b012-47ac-3010-b989-b0834dd949a4 | -13.3772 | -44.3208 | 2025-10-27 13:30:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 3db46c67-b613-313b-8bb1-11a265c791a2 | -6.1923 | -42.6205 | 2025-10-27 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| c3150f9f-3bb4-3b54-902b-a701f02113c4 | -4.4665 | -45.4589 | 2025-10-27 13:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 2e5bb70b-54b8-3342-8846-3c3c31281583 | -4.3877 | -43.3362 | 2025-10-27 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| bfaace42-80d3-33af-af10-d6fc32799da6 | -4.8557 | -43.2607 | 2025-10-27 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ef883f7e-7160-397b-b950-ffb69a1c585f | -4.9138 | -42.9998 | 2025-10-27 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 38531480-672a-33d3-8b6c-f35290f28da4 | -3.0146 | -41.709 | 2025-10-27 13:30:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 0c77c35c-6fb5-3881-9920-881208c6a3d5 | -4.4431 | -43.4259 | 2025-10-27 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b283f2cd-4bb6-3497-8458-33b1cee9fed7 | -13.2589 | -54.3696 | 2025-10-27 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 43e4599d-1c97-37c9-b50b-b0742ca00ee9 | -3.6254 | -42.7699 | 2025-10-27 13:30:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 16a29e16-f5cd-3b00-a6c3-616e5a987ae3 | -4.3879 | -43.3129 | 2025-10-27 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 198.3 |
| 3a2b1d50-73c7-3e75-ab41-10bc626cc782 | -6.1735 | -42.6221 | 2025-10-27 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| d9d7e66c-7acd-39eb-868b-604b3b38282b | -4.9146 | -42.906 | 2025-10-27 13:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ea8d2d5b-fa59-3b5c-9f9b-efc58516bd68 | -4.4618 | -43.4248 | 2025-10-27 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 260af7f2-88a8-3a59-bace-e52c59e18882 | -3.5834 | -43.5877 | 2025-10-27 13:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 13e09fe0-0c38-3ecc-aa46-087a6cbecbc5 | -3.5833 | -43.6108 | 2025-10-27 13:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 248.9 |
| 8fa2c5b1-7e15-3052-abc4-d5b2004141ce | -5.6619 | -41.1099 | 2025-10-27 13:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 136.8 |
| 510703a2-9722-3387-8d7c-f070c3df28fa | -4.026 | -44.4167 | 2025-10-27 13:30:00 | GOES-19 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2a3c0f27-e179-3989-8904-ec2dc1ef8beb | -3.3448 | -42.877 | 2025-10-27 13:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| e0669923-ae00-3f19-9fd7-0ed87ea0c3cf | -5.7758 | -42.9842 | 2025-10-27 13:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| edc5bb26-d8b5-3200-b75c-0aa34bab1a5a | -4.8744 | -43.2595 | 2025-10-27 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 7b9270e7-1a72-3441-a35b-388221170338 | -4.388 | -43.2896 | 2025-10-27 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 05f1b7c8-5a54-3204-9c33-a138e4bd6d5c | -14.7816 | -44.9599 | 2025-10-27 13:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 723ecf08-b64e-3eb1-af90-5a8bf6d66c37 | -6.4067 | -38.4547 | 2025-10-27 13:30:00 | GOES-19 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 159.3 |
| 7db128dc-cece-3f27-a86a-001a9daefd2e | -4.3879 | -43.3129 | 2025-10-27 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 9ceeac9d-8035-3f50-a82f-d8add8c0eb8d | -5.7758 | -42.9842 | 2025-10-27 13:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 5f8010eb-8b29-3f41-9203-b1d1c7b0cf27 | -14.781 | -44.9835 | 2025-10-27 13:40:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 281.4 |
| 8e66b9c4-a96a-3f13-89b4-6e7c4f638f0a | -3.0146 | -41.709 | 2025-10-27 13:40:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 166b9877-bf7c-315a-b8b6-d10a8fbcd397 | -4.8744 | -43.2595 | 2025-10-27 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| e4b893a2-3d37-3e94-baf6-263955814d9e | -5.6431 | -41.1114 | 2025-10-27 13:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 164.8 |
| aafba599-49e3-3f89-a9c2-6ce3f411283a | -4.8951 | -43.001 | 2025-10-27 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 60f94bb1-374f-32f2-a1c2-d72e9de508d4 | -3.5834 | -43.5877 | 2025-10-27 13:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 1acd66aa-6feb-3cba-a8c3-ddfc732a712d | -4.9146 | -42.906 | 2025-10-27 13:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 60405479-c534-37b8-a347-215da8f4e302 | -3.6022 | -43.5636 | 2025-10-27 13:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 9e5ff759-d3b3-3bd2-a557-eff1099d4d1e | -4.4431 | -43.4259 | 2025-10-27 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 46026def-8623-31bf-807f-3fc429f66802 | -4.388 | -43.2896 | 2025-10-27 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5a8c7bbb-9f6f-3d30-a923-e0c2839175a7 | -3.3447 | -42.9004 | 2025-10-27 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| bd59af22-9e5a-3d24-82f7-a9809ec2c9f0 | -14.3982 | -51.5443 | 2025-10-27 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| a1144c85-0da3-326a-82bd-8f9c89de15bc | -4.4415 | -43.658 | 2025-10-27 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 5d9e7001-4420-3d0f-8e7e-3b6f1acde192 | -4.9138 | -42.9998 | 2025-10-27 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 726831e3-fb30-3aea-a590-8da4817901a8 | -5.6619 | -41.1099 | 2025-10-27 13:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 168.1 |
| 31b89043-0332-3b86-b3cb-c008b64f5c89 | -4.8557 | -43.2607 | 2025-10-27 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 3fc67e6d-c408-3cc4-8e2c-36820faba82d | -12.0866 | -46.3935 | 2025-10-27 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 0856cfa8-d940-346e-8467-612d05918621 | -3.6254 | -42.7699 | 2025-10-27 13:40:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| f77d6273-c374-3dfa-acd8-9c7b2d21ab31 | -12.0674 | -46.3962 | 2025-10-27 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| acda8420-aeb5-3a9e-9c53-342876506652 | -14.2491 | -48.1148 | 2025-10-27 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 2809bcf4-c117-3905-a6f4-79660eb00784 | -4.2457 | -42.2408 | 2025-10-27 13:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| d0387724-0550-317e-8c58-b879db738980 | -3.3261 | -42.8778 | 2025-10-27 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d36d6700-dde5-3b50-ab47-c76c9bb78d48 | -4.3877 | -43.3362 | 2025-10-27 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| a3cd3c61-a87c-3584-a9d8-2028b3d57f68 | -14.7816 | -44.9599 | 2025-10-27 13:40:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 125.8 |
| a4a7b4e8-6084-3a8a-984a-66e4f6711dc0 | -3.3448 | -42.877 | 2025-10-27 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 0ea3a32b-2ee9-3827-8f39-1c81b0078dc3 | -6.1923 | -42.6205 | 2025-10-27 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 492fa868-da4d-3c3f-9375-ff2b38a995f3 | -4.914 | -42.9764 | 2025-10-27 13:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2679f66b-58ae-3620-9316-f6265b85d32e | -6.4312 | -43.1411 | 2025-10-27 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a4138439-8f73-30f4-ae32-d48c5ba128a2 | -4.4602 | -43.6569 | 2025-10-27 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 42c6fea7-d191-356e-8e84-ff5cf5ed4366 | -14.3982 | -51.5443 | 2025-10-27 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 166f7177-9a67-3584-b13a-49e8263550fe | -4.8951 | -43.001 | 2025-10-27 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 6e70633c-aa6c-34e3-bec7-aa46a80478da | -3.3447 | -42.9004 | 2025-10-27 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 21ba065e-3498-3da9-82b0-60e07ce3b895 | -14.781 | -44.9835 | 2025-10-27 13:50:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 210.8 |
| f85ba652-8969-3b24-a85e-36ef7d4b85be | -3.7097 | -44.3181 | 2025-10-27 13:50:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| be806b93-2bad-32b9-a95d-cf1c6589ba3a | -4.4602 | -43.6569 | 2025-10-27 13:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 316576f3-b783-3e9c-b717-6f461235af1d | -5.6431 | -41.1114 | 2025-10-27 13:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 361.0 |
| d91534cd-127d-3115-96b1-15976393a5a9 | -6.1737 | -42.5985 | 2025-10-27 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| ebfb3741-f1a1-36c9-a151-ecd3742f719d | -4.3879 | -43.3129 | 2025-10-27 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 8e23fd93-b272-3d1e-a224-1e0c0fa43072 | -6.4312 | -43.1411 | 2025-10-27 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 14b70538-8d98-3999-b3ff-240921f4219f | -4.8558 | -43.2373 | 2025-10-27 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| c6aea446-9324-3062-bea1-1f4b64b18f31 | -6.5864 | -42.6804 | 2025-10-27 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |


[Clique aqui para ver as próximas entradas](README76.md)
