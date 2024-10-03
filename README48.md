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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ba8aab9-2b3a-3bfd-8791-6560b62ad2ff | -11.74128 | -64.08405 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2f66f728-5271-3bd3-83cf-fb3c8c1ecb26 | -11.73631 | -64.1134 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 35b82201-c292-3e5e-ba8b-05dcae1ab467 | -11.73227 | -64.0854 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 301f83e4-0244-3063-9af8-d6957863a0eb | -11.73092 | -64.07609 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 94e53806-362b-3cd2-a44f-847225e2a921 | -11.73001 | -64.13341 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bbe6ab9d-f169-313c-b8d9-658fb3b4c866 | -11.72347 | -64.28262 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f054a7f7-c979-3a99-95e4-2bbadea928fb | -11.72215 | -64.27338 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 17e8924b-3806-35a4-896c-d5201ea374c7 | -11.72101 | -64.13478 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 035187f2-af26-3da3-bef2-9091343dabde | -11.72056 | -64.06812 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| eab6712e-f5de-31bd-bd86-f4760589857a | -11.71131 | -64.13269 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2d5c2457-84c1-3177-a2eb-716862c6e69d | -11.70882 | -64.05074 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 42bbba99-bddd-338a-b612-7d9e466332eb | -11.6813 | -64.05148 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3c2771e9-968c-3d35-9504-cd4ccf30dac1 | -11.67997 | -64.04215 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 12b7e967-8b4c-37fa-81c8-a8f5a335ce20 | -11.6746 | -64.00473 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4788315f-f86d-3681-8a41-af9dfe28633a | -11.67327 | -63.99545 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 271bcf91-010e-3d00-9680-64b009d9c1d3 | -11.67229 | -64.05289 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c5237917-30c7-35d3-8e79-ec5ee3b86422 | -11.67189 | -63.98581 | 2024-10-03 02:06:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9e270aee-8f9e-3f63-9ba0-49603fe0fd78 | -12.44523 | -64.04238 | 2024-10-03 02:06:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7d17e06c-b500-31ab-b55d-6392d7ea2078 | -9.494 | -68.4895 | 2024-10-03 02:06:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 6311ecac-c904-3c54-b464-1be1c0c20b0f | -10.1802 | -57.2848 | 2024-10-03 02:06:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| dbbbe90b-0fd2-30a6-ad94-6efe581dd287 | -10.8942 | -63.8971 | 2024-10-03 02:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 31eb8539-1595-3486-bdaf-c5a6f8c20211 | -11.2566 | -60.5825 | 2024-10-03 02:06:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a152660c-e93f-34dd-b76c-9ccc232a5e40 | -11.2565 | -60.6019 | 2024-10-03 02:06:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 43787b28-d3bd-3eea-8e95-525a317c07fd | -11.6742 | -65.0172 | 2024-10-03 02:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c49c202c-d42e-3bb8-aa8d-78a24dc8e4e2 | -12.4038 | -63.0009 | 2024-10-03 02:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| bcf72b3a-bf83-38d8-9aeb-004009f6d309 | -12.6486 | -63.1022 | 2024-10-03 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 29032ee1-28b1-360c-875a-f394a8ca398d | -12.6484 | -63.1214 | 2024-10-03 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 97.3 |
| fe32b7da-d756-3398-a179-09f2efb82829 | -12.8999 | -62.4527 | 2024-10-03 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 9863e4ba-6a23-3cab-8d29-80fdc29b110f | -12.8998 | -62.472 | 2024-10-03 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 59c571e0-e98a-3b3d-8e19-45020926be7c | -12.8996 | -62.4913 | 2024-10-03 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 97.5 |
| c3db7582-e21c-3682-a23e-e2e798f32534 | -12.881 | -62.4538 | 2024-10-03 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 65e40019-c55f-39be-827b-108412b922f7 | -12.8808 | -62.4731 | 2024-10-03 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| da157b71-2ecf-3575-baa1-01c8421f71bd | -12.8049 | -62.497 | 2024-10-03 02:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 7589935a-e2e4-3350-92f1-71625c928fcf | -12.9187 | -62.4708 | 2024-10-03 02:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 84fb7918-caa9-3700-a823-11d24e9e9c3b | -12.9741 | -62.6409 | 2024-10-03 02:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| edbd0666-deb5-3735-91d4-95d9d2c89dea | -14.6929 | -45.4432 | 2024-10-03 02:06:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 132abb40-87b6-3288-bfc4-90b1d1d0f1b1 | -15.65 | -47.2027 | 2024-10-03 02:06:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 8528ccdd-5f09-3682-bcd7-786cb363e191 | -15.6697 | -47.1992 | 2024-10-03 02:06:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 3038a0af-086e-3c9a-a910-27b581ad2832 | -16.7793 | -57.8102 | 2024-10-03 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| bee7f6d6-ae4e-3ad5-8464-617bfbb73d54 | -16.779 | -57.8306 | 2024-10-03 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| 3ebe83b8-0f2a-3736-9c93-7e881314716e | -16.7606 | -57.7512 | 2024-10-03 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 2d8704b7-9156-38cb-8fa9-268cfa897145 | -16.7597 | -57.8124 | 2024-10-03 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 1c8ba119-c95d-3e55-9703-2a6ca84e62fd | -16.7594 | -57.8328 | 2024-10-03 02:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| fdd6696e-8268-3dab-85b1-fb62d1ebf0f6 | -16.6688 | -57.374 | 2024-10-03 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 96bebf7d-cad1-311d-b3f7-a0e544b65f4f | -16.9179 | -57.6926 | 2024-10-03 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| e8be7ebb-c2bc-3dc4-90b0-34d75e26fc37 | -16.9176 | -57.7131 | 2024-10-03 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| effde1d1-65f4-3fea-b377-45478daaa97d | -16.8986 | -57.6744 | 2024-10-03 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.5 |
| 084e9a0e-bdbb-301b-a239-c966370d8615 | -16.8983 | -57.6949 | 2024-10-03 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| fadac9a0-2af2-34b4-b65e-16d48f8dd6d5 | -16.8787 | -57.6971 | 2024-10-03 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 593a2d05-4687-3ab8-b3c1-6f9c0d6f37c7 | -16.7985 | -57.8284 | 2024-10-03 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 1e217d31-c8a4-3cb9-b1ba-ca285689f617 | -17.197 | -57.3741 | 2024-10-03 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 807b47b6-a41a-3cca-817a-cf65d5d18b60 | -18.6977 | -57.3123 | 2024-10-03 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.5 |
| 5990cc4e-f1e1-3b0f-8a73-0fd8856dad27 | -19.0344 | -43.1944 | 2024-10-03 02:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.5 |
| 94ee3234-436a-39b3-82c7-feb0bb298238 | -19.2954 | -42.6032 | 2024-10-03 02:06:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 08aa2daf-0ece-37be-af85-8a0da6860182 | -19.3159 | -42.5976 | 2024-10-03 02:06:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 168.3 |
| 695edd75-0e34-337a-8130-2a188967e435 | -19.8803 | -42.1132 | 2024-10-03 02:06:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| 1e3624eb-9aa5-3aa5-9e2c-20241cdd29dd | -19.8812 | -42.0877 | 2024-10-03 02:06:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.5 |
| fc399cbc-09eb-3231-bdbb-eede8c1fa15c | -20.6352 | -46.7497 | 2024-10-03 02:07:00 | GOES-16 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b6cac3eb-cad5-3603-8677-af14d1ccccdc | -20.6558 | -46.7447 | 2024-10-03 02:07:00 | GOES-16 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 94b89dcd-a5cb-31ac-a112-a30d0f343298 | -21.346 | -55.6626 | 2024-10-03 02:07:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 83.9 |
| e69ba24d-d0d1-3c46-b64a-d6f48a775c38 | -22.3495 | -47.9515 | 2024-10-03 02:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b50010e3-be58-3ff5-b7a8-50d49aa9d298 | -22.3502 | -47.9278 | 2024-10-03 02:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 8f46f9ea-8a89-3ea7-b7d0-3e1fb99981f0 | -22.3704 | -47.9462 | 2024-10-03 02:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e6cd818e-fa77-3372-95f7-93ce7102c11f | -22.3711 | -47.9225 | 2024-10-03 02:07:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 8828994d-da4e-3909-afe6-ef485131dce3 | -22.446 | -46.8576 | 2024-10-03 02:07:09 | GOES-16 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0bba0c6f-806a-3147-a908-a7e209d7d897 | -11.6659 | -64.97593 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c73a23be-300e-35fd-875e-b1dca69bc449 | -11.66338 | -65.02225 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| c54dad16-992c-3ab6-8bd6-85a09ab77ffc | -11.65988 | -65.20303 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 848f7326-00c3-30f0-aea0-9cbb7727375f | -11.65863 | -65.19405 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 47bdb209-565a-31b0-bea5-ed630ca1606f | -11.65704 | -64.97724 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| aec3d6c7-0715-301c-9fb9-29ff9ae21e64 | -11.65368 | -65.0296 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e59d62db-67f1-37a2-9ea9-0aa30bf8dc0b | -11.65241 | -65.02061 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e6baa3e8-b7be-3823-b081-a5010216f78a | -11.65103 | -65.20433 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59e849e9-4d80-3b7c-a9bf-84b5f26f10cf | -11.64737 | -64.9846 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 70d60152-c697-37b5-9807-81ea7c10cade | -11.63851 | -64.98591 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 25d97ae3-07ea-3ea5-b1c2-8338756a06a0 | -8.78729 | -68.80016 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| bfcb378a-8a22-326b-a7df-213173d74f14 | -8.78325 | -68.84554 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5fc4c27b-307c-3d66-9c00-d7c90d7621df | -8.18179 | -70.08818 | 2024-10-03 02:09:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3a6a5d8f-de44-357c-920a-b336561ba8c8 | -9.50145 | -68.95793 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1aca12dd-5a74-3ef8-a67a-cad56f30cef0 | -9.66861 | -69.06478 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 650d716a-0d1f-314b-bb3d-0741d28b8b5d | -10.72094 | -69.31368 | 2024-10-03 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c561c64f-1d85-3716-b04a-cda8d17811b0 | -10.66979 | -69.30138 | 2024-10-03 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 20a28adf-87d4-383a-8fc2-429cea95c56a | -10.66737 | -69.3079 | 2024-10-03 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3178e75f-f6dd-3215-8fc1-ac7ca1aa0093 | -10.56007 | -69.24564 | 2024-10-03 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a4332217-980a-3da0-8aa7-cf169259ba4e | -10.54813 | -69.23463 | 2024-10-03 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ef1908b2-ec28-35a3-8baa-34da51db39ad | -10.54037 | -69.337 | 2024-10-03 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 95072085-6b42-30ca-a3a2-b241f3f002f0 | -10.53874 | -69.32442 | 2024-10-03 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ac19956a-dbdb-3429-85a0-c04113d6e00d | -10.5172 | -69.23869 | 2024-10-03 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 24095a01-3621-3fdf-bdac-2f17142074c5 | -10.5156 | -69.2263 | 2024-10-03 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0c9b8f9b-80f1-35bb-b9b0-8d3066b949b2 | -10.50771 | -69.16485 | 2024-10-03 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 77c4c6e7-b220-30f4-866f-f4a365c447d4 | -10.50267 | -69.45792 | 2024-10-03 02:09:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6e164e2a-6a89-3928-b2bd-44ca7e43f688 | -10.49539 | -69.45221 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| eadea5a7-5ea3-3dac-baba-90bb5f471eb0 | -10.16586 | -69.36048 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 11dfa1ed-f5b7-3834-815e-d9f4008e6c47 | -7.52674 | -70.40597 | 2024-10-03 02:09:00 | TERRA_M-M | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7cd020bd-a784-3768-8c44-025ae380cf9f | -8.87844 | -70.8548 | 2024-10-03 02:09:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1667ed48-2a98-3669-b07b-94601ae40082 | -7.93122 | -71.48451 | 2024-10-03 02:09:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 646ba82c-6eef-3130-b72f-04367e18f1d7 | -7.92903 | -71.46803 | 2024-10-03 02:09:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4c1f3142-6bff-305b-b5aa-e25693506131 | -7.92637 | -71.47946 | 2024-10-03 02:09:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3a556751-3225-39a9-838d-a1336b1bc658 | -7.42992 | -72.73768 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ae7234c9-ae24-3b0a-9925-ba29a9b280be | -7.42841 | -72.73126 | 2024-10-03 02:09:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |


[Clique aqui para ver as próximas entradas](README49.md)
