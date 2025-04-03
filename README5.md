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
| 2c991f0e-ab9a-3348-8583-68ec56b2661a | -16.30101 | -45.08952 | 2025-04-03 12:32:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c0d2c8e5-87b1-3133-97c0-2b3a88a0c07c | -12.90488 | -44.37135 | 2025-04-03 12:32:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| e690d316-a520-3b95-b32b-85f561156c95 | -13.7359 | -48.27137 | 2025-04-03 12:32:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7950c6e9-cc74-3d0c-9802-d9246f83bdcd | -16.76827 | -41.14096 | 2025-04-03 12:32:00 | TERRA_M-T | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| ea8acf83-3f87-3420-91e7-a206027c1166 | -14.68432 | -45.82934 | 2025-04-03 12:32:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6350ef6c-7ebd-38f6-8496-0b39065d3555 | -12.9033 | -44.38329 | 2025-04-03 12:32:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 70da5d38-e7ba-3d55-a410-3b2fa1364e2f | -14.6857 | -45.81894 | 2025-04-03 12:32:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| cecfe931-0d46-3515-b4ed-64ee980fd76c | -16.28932 | -45.10035 | 2025-04-03 12:32:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 93e1b39c-815a-3356-b643-c882bbaca2f4 | -11.75133 | -46.34408 | 2025-04-03 12:32:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5b0dabf3-c063-3fd9-93dd-b1bfa7d7e8e4 | -11.27039 | -44.5311 | 2025-04-03 12:32:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| a99747db-10a4-3ba3-8c3a-bfe5ff74dd37 | -13.03589 | -45.08413 | 2025-04-03 12:32:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| c465788c-08f2-36ee-a09b-4e6e187ee11d | -15.14371 | -43.92569 | 2025-04-03 12:32:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 72fd2df2-7a54-3fa9-9243-fc3865dc8064 | -12.75991 | -44.8419 | 2025-04-03 12:32:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 483f2821-da3a-3b3e-a4ff-c77a7216cfa5 | -20.15904 | -47.31992 | 2025-04-03 12:34:00 | TERRA_M-T | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 05a9799b-aeec-3ce8-92e8-d8a82c291aad | -20.17274 | -50.50605 | 2025-04-03 12:34:00 | TERRA_M-T | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 9d7598bf-28c3-36ad-a9ca-9d91e8d98b77 | -20.46543 | -44.78208 | 2025-04-03 12:34:00 | TERRA_M-T | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 9d82d21d-a385-37d7-af7d-a020fb286ea0 | -13.033 | -45.1027 | 2025-04-03 12:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 6eae5c2b-51ec-35c6-bcb3-48df00b337ab | -13.0335 | -45.0794 | 2025-04-03 12:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| fc8ad77d-1a70-3cbe-9ce8-325dbcd3a8b3 | -13.0524 | -45.0995 | 2025-04-03 12:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 62cdd33d-ccce-3f75-b450-eff94ed5e242 | -13.0528 | -45.0762 | 2025-04-03 12:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| e1ba0f51-9bcb-3b5e-bd2b-cba32acbfff9 | -13.0528 | -45.0762 | 2025-04-03 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 97e31e8a-6328-3d79-b871-45a469f06f0f | -13.0335 | -45.0794 | 2025-04-03 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 7db858c0-05b0-326f-8e21-752ca46abc9b | -13.0524 | -45.0995 | 2025-04-03 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 16334661-db20-303e-b5f5-302f40449048 | -13.033 | -45.1027 | 2025-04-03 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 2f3ef857-5fb6-3c07-97ed-1a5748819fea | -13.033 | -45.1027 | 2025-04-03 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| bcfa7390-5e39-3c7e-80e5-841c14d47ed9 | -13.0524 | -45.0995 | 2025-04-03 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| bee37123-e596-3f2e-95fd-3dc226ed53b7 | -13.0335 | -45.0794 | 2025-04-03 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 4fc16f09-bba2-3a06-97a8-6c09b89451a1 | -13.0528 | -45.0762 | 2025-04-03 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 7c06fddb-a177-3a13-aab2-542b94c942d2 | -13.0528 | -45.0762 | 2025-04-03 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 9e16f757-f501-3a92-85c0-28af023a7872 | -13.0335 | -45.0794 | 2025-04-03 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 3423efdd-ccbd-3327-bafc-4ee67e0950a9 | -13.0524 | -45.0995 | 2025-04-03 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 3348565e-b885-3f22-af8a-8625b44129a0 | -13.033 | -45.1027 | 2025-04-03 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| a9c61be1-1889-3089-92a6-5f89cb78a35b | -13.033 | -45.1027 | 2025-04-03 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 72dd4406-5cc4-3822-a6b3-29200fd511bd | -13.0528 | -45.0762 | 2025-04-03 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 3b7c2337-8eb6-3bec-bcc0-675348077859 | -13.0335 | -45.0794 | 2025-04-03 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 6f459d71-aba3-32a2-99a2-d82e225f43e0 | -13.033 | -45.1027 | 2025-04-03 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 08cd5ae6-8178-3833-8fca-0a39a75ced70 | -13.0335 | -45.0794 | 2025-04-03 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.3 |
| f67b21e2-fdd1-3e96-8ed2-e8240af0e291 | -13.0528 | -45.0762 | 2025-04-03 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 3770e01c-e4ca-38ee-9f11-ce3276239fb5 | -13.033 | -45.1027 | 2025-04-03 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 4ed334e9-6002-3b7b-b07e-d9c902abab22 | -13.0335 | -45.0794 | 2025-04-03 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 69f2a861-daa0-3297-823f-37e8e25fec0c | -13.0335 | -45.0794 | 2025-04-03 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 79aadea3-5fc5-3188-ad14-331a98a19836 | -13.033 | -45.1027 | 2025-04-03 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| f7a4dad4-77e8-3eb7-9c3e-989de400d98f | -13.033 | -45.1027 | 2025-04-03 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| bc64d4e8-8627-339d-b479-dc515e56a87b | -13.0335 | -45.0794 | 2025-04-03 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 2f424292-ec33-3656-aaef-85c1974fcfc7 | -13.033 | -45.1027 | 2025-04-03 14:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |


