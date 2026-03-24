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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ce1a7fa-987d-3917-9bce-2b1b7b561716 | -21.04149 | -48.79493 | 2026-03-24 05:01:00 | NOAA-21 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1cac2b01-9790-3d4e-95d7-256aa23ebf0d | -20.67585 | -48.79641 | 2026-03-24 05:01:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 511f88ef-07ad-3c2b-ae11-94755126e047 | -21.11784 | -47.46415 | 2026-03-24 05:01:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a313c516-fb0c-3dda-be08-a6054ebdd556 | -19.22937 | -44.75214 | 2026-03-24 05:01:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 00581993-a33d-3fde-830d-b4987a2509fb | -16.58148 | -57.80637 | 2026-03-24 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cbb344d1-5b3e-35d7-82ec-91a34fb42ece | -20.67638 | -48.79727 | 2026-03-24 05:01:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e7a99d46-09c4-37a7-9de8-fd9c284594a9 | -20.6809 | -48.79697 | 2026-03-24 05:01:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 15489dcc-6af7-3ee3-b501-cb4b5f332756 | -16.4399 | -54.93007 | 2026-03-24 05:01:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e10a5b0b-266e-3626-8121-d52e8b12d668 | -16.42919 | -54.93215 | 2026-03-24 05:01:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df63946c-6bdf-3d5b-8ea8-47986edd5344 | -16.58483 | -57.80695 | 2026-03-24 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a14a5bd6-df13-3137-8b39-8291c52bfaa1 | -21.04181 | -48.79184 | 2026-03-24 05:01:00 | NOAA-21 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6d3f5965-fbb5-3832-8bb1-22973d1976ec | -16.84624 | -50.66966 | 2026-03-24 05:01:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dadb4dd3-381d-3993-a240-2ceb6e63c549 | -16.57813 | -57.80579 | 2026-03-24 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 39943807-0c7b-3288-9183-23f75bad2467 | -18.03636 | -54.57276 | 2026-03-24 05:01:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17913998-4f85-39b9-986f-1bca667f0bdd | -16.58208 | -57.80267 | 2026-03-24 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 93b0fc08-b3b7-387d-87a7-89017290fb17 | -18.0329 | -54.57219 | 2026-03-24 05:01:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fbc4648-df1e-31f8-b9b7-ca6dd458450d | -21.11772 | -47.46189 | 2026-03-24 05:01:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de713ec0-2ddd-345c-adb5-01ffaf98a9b9 | -16.43934 | -54.9338 | 2026-03-24 05:01:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| dabf94ea-9ec2-3929-abd4-7a05da671663 | -20.68143 | -48.79784 | 2026-03-24 05:01:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2035779b-269b-3eaa-9d48-950214ed16b8 | -16.57873 | -57.80209 | 2026-03-24 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 80c32e99-c564-3b56-877a-862166d45211 | -21.11738 | -47.46561 | 2026-03-24 05:01:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4acb90df-1623-391b-afb1-ec236370db5b | -19.48737 | -52.70781 | 2026-03-24 05:01:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dffd68f4-d93d-3bf1-ac4d-e125609858e4 | -21.23105 | -56.92752 | 2026-03-24 05:04:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b40d0368-28d0-3d5d-986a-43a9d22b3ca8 | -21.23048 | -56.93123 | 2026-03-24 05:04:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1185c590-295c-3f34-9aa5-f2a861f993f3 | -21.63101 | -49.02902 | 2026-03-24 05:04:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af4905c1-fb40-3fd6-a1bd-1cb1ebcb57e1 | -21.54558 | -54.27176 | 2026-03-24 05:04:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c3ef5da-720d-3e70-b103-ecc1921ba8b9 | -23.61077 | -48.25869 | 2026-03-24 05:04:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63aff956-649e-3891-8cba-ce29c838d9d9 | -22.44062 | -46.91059 | 2026-03-24 05:04:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0218f03-e3cf-300e-ac50-1dfd321cfee5 | -23.60537 | -48.25791 | 2026-03-24 05:04:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4c1ce701-c2ae-35dc-b492-0683957e62bc | -23.6086 | -48.25999 | 2026-03-24 05:04:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 47ebac2b-fa91-367e-ade3-ad1423bc3b98 | -23.60896 | -48.25627 | 2026-03-24 05:04:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1fc5102-5616-33e5-ae13-3bcf5f468d0b | -21.63071 | -49.03201 | 2026-03-24 05:04:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a8d0d90-b0d5-38d9-89a7-01946321c2bf | -21.71726 | -47.2522 | 2026-03-24 05:04:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f9fcb230-f774-3128-a6c2-8cf05488fa84 | -21.54497 | -54.27632 | 2026-03-24 05:04:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7634da71-65bb-3f43-b307-204b9d1fe9c8 | 4.23969 | -59.91279 | 2026-03-24 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c00f4a53-b57b-3b3c-ba7a-1c778d036eea | 4.64479 | -60.23372 | 2026-03-24 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 344da643-ea4a-311e-9b8a-76ecd1a70de0 | 4.80591 | -60.62815 | 2026-03-24 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4cbcf598-aa88-32d0-a55f-b8a0618eda60 | 4.64652 | -60.23261 | 2026-03-24 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 351f4c68-aa7b-39b7-9779-f1f23d989abc | 1.84 | -60.42051 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 365a6d19-6601-39a2-810f-9aeb30488b8b | 0.57955 | -59.90079 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb7ca1ae-f150-3152-89b4-53f780ad666e | 1.13704 | -60.08523 | 2026-03-24 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc0a9e13-0344-3082-9265-6a25ec5bf33b | 3.44627 | -60.1543 | 2026-03-24 05:27:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ea75228-1071-3aff-9510-0a999800b460 | 3.84546 | -60.07101 | 2026-03-24 05:27:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1e4cf75-3351-3b33-a216-2c292b816389 | 1.80029 | -60.47935 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f4f2ca5-87d9-3000-ba31-6950aba36e0f | 0.9458 | -60.4644 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16ce8e96-b2ca-3a50-876b-2a4b588c6722 | 0.57732 | -59.90833 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c445ff3-887b-3c44-a51b-fb6dcdbf2d09 | 0.77436 | -59.8707 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af61a68c-a0a1-37fe-867c-cd53b9501c61 | 1.08349 | -60.65223 | 2026-03-24 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f116aa0b-bc7f-3e5d-a4d8-bc9c3a50c0c6 | 0.67105 | -59.81486 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acf908bd-9f9e-3849-a01c-d76946b6d0db | 3.34949 | -60.13865 | 2026-03-24 05:27:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34aff9bf-3ea8-3b3e-939d-902faa918cb1 | 0.58067 | -59.90781 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18d4ae6e-6805-3539-a3ed-c13dbff6e2a7 | 0.73562 | -59.60505 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef075c00-5491-3824-823e-cb9ef7d2e3a2 | 0.94107 | -60.32454 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 763c50f2-728f-3fca-ac42-ec90fa503a7e | 0.9817 | -59.38504 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acaefc4f-c31e-36a5-b3dd-746df0af94d1 | 3.45027 | -60.15746 | 2026-03-24 05:27:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 370da85a-4125-308a-ad8c-1e7e77e6347b | 0.9878 | -59.38054 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f439ca67-5970-3524-9a1d-889769833af2 | 4.01249 | -59.71195 | 2026-03-24 05:27:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47483a34-8630-3977-9128-9a5c1d7a754b | 1.83659 | -60.42104 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2751d49e-5309-3ef5-b736-5efb95f139bd | 0.78104 | -59.86966 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1709ddf4-c656-33dd-a799-129ffce3b577 | 3.59979 | -60.13113 | 2026-03-24 05:27:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3ffc8fc-a966-3c23-9428-671c365b00ff | 1.79237 | -60.51832 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5e4177c-f2b5-3614-bd51-2e0adee3a0cd | 3.35348 | -60.14182 | 2026-03-24 05:27:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0bfdf2c-cb20-35da-8234-dc45d2c8650e | 0.74005 | -59.61147 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54de2832-d9f4-3851-a8fc-60b95d5ac6d0 | 0.65896 | -59.65976 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bd3bb7c-1467-3288-94e5-471636a6de26 | 0.77007 | -60.54673 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5a77737-a042-3c89-b573-8db471e706dc | 0.98503 | -59.38452 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34a72be5-58be-32c8-9343-bd90cd6a41d2 | 0.98725 | -59.37709 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed42725c-d540-325e-a725-e5d0cb1a4180 | 0.77491 | -59.87421 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc9e39d5-09fa-31e7-ba08-a28fc679a653 | 3.35633 | -60.1376 | 2026-03-24 05:27:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc9e2edd-bc98-3c98-bf98-56bc66f77fac | 0.57488 | -60.52875 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a53b5a0a-e310-332d-b3ff-b78818a6c00c | 3.84488 | -60.06732 | 2026-03-24 05:27:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4195416-381e-3224-b0b7-7b87198f8c82 | 1.83942 | -60.41685 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9700505a-48e3-3298-903d-3b2c026d830b | 0.78049 | -59.86615 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06a14ce7-0afe-3969-a1c5-1b0a9dfd589c | 0.98448 | -59.38106 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4ba24bd-6fa5-30cb-95cc-dcdde8c5a54c | 0.77714 | -59.86667 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe333677-eb18-3501-9f16-f68be923a5a6 | 3.98622 | -60.03477 | 2026-03-24 05:27:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b710f03-9ffe-35fa-9be0-16050d2baa6b | 2.03546 | -61.10913 | 2026-03-24 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 27217710-08c6-3d58-b054-cf6be903e8f9 | 0.69617 | -60.0811 | 2026-03-24 05:27:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf406327-1db6-334c-9281-00e2f04e653f | 0.77157 | -59.87474 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b5cd4b2-f83b-3b1e-9f1d-9368649ca683 | 0.14441 | -60.41066 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5f8baf9-7952-3f8f-a699-555c840d6a33 | 0.94535 | -60.17714 | 2026-03-24 05:27:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67e4e874-0c58-342b-a453-956d8e905b88 | 0.64197 | -59.99917 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c12fa8e-d1a7-36b2-ae86-04507aed20f7 | 0.63018 | -60.05519 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bda0b066-2077-332c-93e0-9084def8cc96 | 2.64649 | -61.29812 | 2026-03-24 05:27:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a892532c-b747-35eb-8fe9-81604aa02fa5 | 0.14385 | -60.40709 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c09d318b-891b-3b0c-b70d-7c0496950877 | 4.16459 | -60.81704 | 2026-03-24 05:27:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e0a7a7c-b281-357c-be98-eda24ae5a8ec | 0.98393 | -59.37761 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d6f1f8d-b228-38e7-9427-2b46e6049639 | 0.9606 | -60.22958 | 2026-03-24 05:27:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84bac46d-b0b8-32da-968f-b001a7fd06d6 | 4.16812 | -60.81648 | 2026-03-24 05:27:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84b3c6a7-9ea7-34c3-93f9-42201090d7e3 | 0.98835 | -59.384 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4cfb661-ccdc-3672-8758-78b6b93be74d | -0.97137 | -53.18023 | 2026-03-24 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca3d60c3-d553-350c-a29c-d9ff2afe0dd2 | 0.7777 | -59.87017 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a6231ec-cf27-3ab3-88ea-b3e3b09ff03c | 1.879 | -60.42628 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f4fe2f5-ccc2-3d0f-a49d-a515c7736440 | 1.844 | -60.42365 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d93882c9-515e-3ae8-8963-b181333b6035 | 0.92998 | -60.49655 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b422c1c-5b24-33c5-842d-41e5788c4d37 | 1.84284 | -60.41632 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a6e6dc5-e72a-3b59-882e-e69fe077def8 | 0.73617 | -59.60852 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 308ac163-a53c-3762-b316-6f6fd3c64dd7 | 0.72214 | -60.28832 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98114d62-4f2d-30f6-8a5b-ba9e89c78272 | 1.84342 | -60.41998 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34b73db7-4f2e-365c-b568-76b6eebe6ec7 | 0.70737 | -60.0866 | 2026-03-24 05:27:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README5.md)
