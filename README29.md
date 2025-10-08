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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bd0f35c-f966-39b4-a111-a8c2dda7d8a2 | -20.2695 | -43.26533 | 2025-10-08 03:51:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aa26c1d4-255f-3f9e-b6c2-52649c5bc03f | -21.31354 | -44.44895 | 2025-10-08 03:51:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e5b8f152-934f-37e7-8132-2c29b608a513 | -19.72164 | -43.90981 | 2025-10-08 03:51:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 398cb390-9f95-339b-a77e-2ea620072ff5 | -20.12782 | -44.42116 | 2025-10-08 03:51:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| d878a27d-9243-30da-96cb-097aecd69f9b | -17.15212 | -43.46319 | 2025-10-08 03:51:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6095b5b5-6148-3622-af1e-9d1d9c3a08c5 | -22.22657 | -49.72803 | 2025-10-08 03:51:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a7fc51a1-a6ae-3fbe-985c-625415315b2a | -18.04967 | -44.45675 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a562e0f9-be09-3a40-9c17-dd9e4ef433a1 | -17.36181 | -45.08776 | 2025-10-08 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b30c95ce-7a8a-3729-84ae-6aaacb33e22c | -18.07199 | -44.4683 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8aae9f2f-388c-309c-b0ff-07600e0a0045 | -18.29993 | -45.4416 | 2025-10-08 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d41d8b18-2b1c-3118-9d47-d9b5507059c2 | -16.05583 | -50.98256 | 2025-10-08 03:51:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5dea55e1-71c8-354e-abf4-d127dcede27f | -19.51525 | -44.07636 | 2025-10-08 03:51:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cfbda019-ef7a-3448-bd88-d1b46419ff7c | -17.57645 | -42.14781 | 2025-10-08 03:51:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 30868ff4-98f6-3bd6-851d-3a895ac25dd2 | -17.2752 | -42.6511 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 465ebdb4-0519-3d98-be33-9ce9028afd95 | -19.09831 | -43.73087 | 2025-10-08 03:51:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d963403e-fddb-3ae4-a367-341b5a3640a0 | -18.0283 | -44.96135 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 17cb758a-2209-3cb2-8fc2-b870f7550e76 | -19.58019 | -44.73719 | 2025-10-08 03:51:00 | NOAA-21 | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5edd451c-a5d9-37fb-8b01-a527a260bcc4 | -16.33806 | -47.05516 | 2025-10-08 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d33dc65b-a92a-3a4a-bdd0-443a34f1d608 | -19.71976 | -43.91177 | 2025-10-08 03:51:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81e267ec-ad0e-3352-9c82-23452e5a34c2 | -16.71744 | -47.5992 | 2025-10-08 03:51:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4c384cdb-4353-3a8b-8269-1ce7f93c29ca | -17.27446 | -42.65536 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2fbdbd4d-7dd0-3346-9f81-18e8186165f7 | -22.22722 | -49.72499 | 2025-10-08 03:51:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8e5c0742-26e7-3b03-bab7-395cf6b3bf14 | -18.01334 | -44.97382 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d93099fc-430d-3594-a19a-cd19286860a2 | -18.54075 | -45.07544 | 2025-10-08 03:51:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93265d44-cfe1-30bf-920b-49e97c8c5c5f | -21.23974 | -45.78957 | 2025-10-08 03:51:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 55db7a82-7345-3d13-8055-5f82b36e22f6 | -20.12491 | -44.41557 | 2025-10-08 03:51:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 540fb5e9-a6dc-3380-9b17-1e7f40c08b48 | -15.37046 | -47.30231 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f575ca1f-c6f2-3848-a9ca-d0bde79ef427 | -18.0191 | -44.29264 | 2025-10-08 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6e01469-75d9-3dce-a19c-aa88383d108d | -20.39023 | -43.07092 | 2025-10-08 03:51:00 | NOAA-21 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e88b5c45-d930-370c-9c64-eb4302e55e90 | -17.73275 | -44.37565 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 99722f4e-7b57-393d-a491-e8903e8f9ccf | -17.85741 | -42.29152 | 2025-10-08 03:51:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 36fd7bd6-0358-3df8-917f-e1e049d61da8 | -20.19071 | -43.92497 | 2025-10-08 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 70c6d887-45d4-33c0-89ad-85542f065ca3 | -22.11598 | -44.99295 | 2025-10-08 03:51:00 | NOAA-21 | POUSO ALTO | MINAS GERAIS | Brasil | 3152600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5ecd03ce-fd43-3463-9c3c-8fb1f5e09c3b | -15.99679 | -50.96136 | 2025-10-08 03:51:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 181bd71d-2535-3ff2-8b58-5524a4f47f96 | -18.00277 | -44.98664 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37f15c7b-3518-35a1-acd9-b2b140f057a4 | -18.02399 | -44.30785 | 2025-10-08 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34cf41bf-920e-3ad4-968c-a02fec16bf74 | -15.99784 | -50.95645 | 2025-10-08 03:51:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d859a9b2-4c00-3ae0-9261-9ddfb53c9d50 | -15.37196 | -47.32502 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84463f37-6169-3f25-9d80-45d02378f046 | -18.07215 | -44.44492 | 2025-10-08 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f3967aa-b121-3ca4-9530-64fbff8a4db0 | -21.16187 | -45.62783 | 2025-10-08 03:51:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb9d547c-5dca-3b69-aadc-15d8b14619d8 | -19.51899 | -44.07718 | 2025-10-08 03:51:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b4f492d-015e-34b8-ad58-f91576f21be9 | -15.99576 | -50.96611 | 2025-10-08 03:51:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c6a9d65-5256-39dd-9341-545661ef8923 | -17.55357 | -46.06632 | 2025-10-08 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6850a3a8-a02f-383a-8660-0a428b7e87c2 | -16.10988 | -43.87105 | 2025-10-08 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c1ee0ef-0eb2-398d-a24b-05b951fa88e1 | -17.45699 | -43.3938 | 2025-10-08 03:51:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 892d21a0-a4c4-3723-acfe-6d8cef12ddd3 | -17.28243 | -42.65233 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 76ed3ed5-defb-3688-be02-2cd992eb929f | -15.4004 | -48.01775 | 2025-10-08 03:51:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 407c6cae-bfcf-35bc-9e85-cb6cd3e6ff3c | -22.39423 | -50.0134 | 2025-10-08 03:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4e2b72b6-333f-3ace-9b5b-9fd63ff264b9 | -15.38427 | -46.27937 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2765a9e6-20fa-3fdf-9b64-1aa75f46dadf | -16.18657 | -42.97524 | 2025-10-08 03:51:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15713aef-8e84-3b3b-8c75-49e480263884 | -19.30762 | -43.1684 | 2025-10-08 03:51:00 | NOAA-21 | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c7c47fc0-0161-3261-819c-bdd37d2c8f3e | -15.39081 | -47.30796 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5af0d9d7-0ff6-39e0-bb07-b6fee01fa24c | -15.37106 | -47.30381 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7911dca2-6969-3472-84b9-1e02afb0848e | -16.01116 | -51.04438 | 2025-10-08 03:51:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e66502f-3ad2-3d64-9114-92023bc2af5c | -15.39727 | -48.00645 | 2025-10-08 03:51:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a889e3d5-4060-3685-9894-f7360d5e782a | -20.08621 | -44.32918 | 2025-10-08 03:51:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 531fb707-649b-357a-84d9-8776d3f5af8b | -15.33502 | -52.79205 | 2025-10-08 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b824fe9b-ce34-3435-95b9-a6fc10da3fee | -15.37141 | -47.29738 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 327b8d31-aaf2-3da1-9208-095116cc550f | -19.72144 | -43.90231 | 2025-10-08 03:51:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72ff272b-4bfd-388e-b409-21dedd2fc4b5 | -15.8031 | -46.24819 | 2025-10-08 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 013f5f28-71c4-38dc-8eec-b1eb49d600f0 | -18.06425 | -44.46609 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 8b9d996e-2a41-3b24-a388-74fb75cf2d83 | -19.4703 | -43.89159 | 2025-10-08 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e29cc5a1-f8c9-39e1-b5d0-13bfe5bcf89c | -17.971 | -44.97626 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83fcd76b-5432-3e6d-9ec3-0b951341ecf8 | -18.01523 | -44.2918 | 2025-10-08 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c241ce14-bd1e-3a4f-99cd-c00be5c7b6d8 | -18.40725 | -45.20258 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 980e4dc5-62d5-3a82-a88d-9c0ee6dce3b4 | -18.40392 | -45.19781 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f18d791e-74cd-3c3d-bd07-d48f62b13eff | -15.40177 | -48.01093 | 2025-10-08 03:51:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6cf5a97-4e4b-3558-a933-18c1dc106ab1 | -16.13936 | -48.23887 | 2025-10-08 03:51:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc42f7e1-cb01-37f2-8640-bc16a66c9f76 | -20.50228 | -45.95252 | 2025-10-08 03:51:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8ba9159-8446-36e5-93fb-fd0d08fa975c | -19.15731 | -43.31981 | 2025-10-08 03:51:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 2fc3f470-03ce-3a29-83d6-6204e34a4f38 | -20.19396 | -43.94937 | 2025-10-08 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| aea00a65-ebea-3c67-bf9f-4f7fdfc1aecd | -18.02784 | -44.31081 | 2025-10-08 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ee55575-0fa6-301b-aa43-e33639a1d193 | -19.71603 | -43.91113 | 2025-10-08 03:51:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bca8f6b2-4db2-35f7-a572-92e8a6dae7c0 | -18.42281 | -45.20999 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7707518-c610-3a2c-9492-fcacb3c34034 | -15.35441 | -47.33218 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19537d0a-2e7e-3bac-b49c-1d960f3bc398 | -16.18368 | -51.75143 | 2025-10-08 03:51:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dcab592-ffd3-3f8f-a697-c90c9ee6ee1e | -16.2915 | -47.09307 | 2025-10-08 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87dcbb1b-b413-3dfb-9cdb-ef431d17a643 | -17.03761 | -43.4492 | 2025-10-08 03:51:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 485837b7-9c51-35a7-bd93-94149806622a | -17.51335 | -44.9982 | 2025-10-08 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce85e7cf-802e-3680-b60f-02636b47f196 | -20.3202 | -40.36693 | 2025-10-08 03:51:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 52501156-b0d3-31e2-be4b-0e5a48fd062b | -18.34997 | -42.3882 | 2025-10-08 03:51:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 29039b9e-bf01-3f5d-9c08-3382474c587b | -20.20786 | -43.95715 | 2025-10-08 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 29e89d7d-0265-3dd4-b176-dae7c0f4995c | -16.06162 | -50.98546 | 2025-10-08 03:51:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c19416b4-16a5-3559-aec3-febac05e7e49 | -17.28603 | -42.65297 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b4192643-c2b2-3259-960b-30b2f964869d | -17.97504 | -44.97722 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 92212432-902e-34ec-92de-125d2460fd25 | -18.00239 | -44.98725 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c230559a-b8e7-34f2-b903-46cd7ab8bad5 | -19.51062 | -44.08038 | 2025-10-08 03:51:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7ab15e3f-d58e-327a-8c8c-391b5b5177bc | -21.09441 | -44.20837 | 2025-10-08 03:51:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 946527e0-3653-3730-8784-46d51d8a160d | -20.59519 | -45.15673 | 2025-10-08 03:51:00 | NOAA-21 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9db961a0-e805-358f-a4a8-85e00144e597 | -15.06628 | -49.48676 | 2025-10-08 03:51:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 33c60fc4-ebab-32aa-b34b-78c340014755 | -18.07801 | -44.45754 | 2025-10-08 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93845f66-ee93-3cf1-bfc8-f0402ad11bf7 | -16.13047 | -47.91288 | 2025-10-08 03:51:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4103e3d-7e78-3399-9631-9b0d2090bae1 | -17.56759 | -46.06432 | 2025-10-08 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d658997-f5fc-30f6-82bd-c061d4109629 | -21.53146 | -45.43494 | 2025-10-08 03:51:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f90ab9f7-4836-3f48-8290-ac3766d4588f | -22.30363 | -49.926 | 2025-10-08 03:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 50486ec4-396e-3764-b1c2-72156350380c | -17.84056 | -44.3392 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54fea60d-339a-3568-b791-300906347659 | -18.63165 | -39.78931 | 2025-10-08 03:51:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f2e31a76-e1dd-319b-a051-31e56c5fb5f0 | -15.37961 | -47.30817 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9711bf1d-5529-3116-bc01-c3daac86e3b7 | -17.45782 | -43.38915 | 2025-10-08 03:51:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebeadbc4-f7ff-36ba-856f-fbba6f9e50c7 | -17.28678 | -42.64867 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README30.md)
