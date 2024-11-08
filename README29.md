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
| 31f7d37b-0975-3553-aa94-143aee3c396b | -1.32323 | -54.63976 | 2024-11-08 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ac49dcf-a96e-3669-9106-bd1bed937615 | -4.38214 | -47.22276 | 2024-11-08 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0fcdf9b1-7ef6-3672-bac2-01b2d2e69108 | -3.97545 | -48.39813 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df62c842-691c-3423-b511-e3a2db8a0799 | -3.50163 | -51.14241 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4d0ad60-0608-3a13-b0fc-f3a25aebe6fd | -9.7974 | -61.51015 | 2024-11-08 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62a79e7f-ac1f-37da-b314-aba3f288eeff | -2.61316 | -51.29984 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 062586f9-1c86-3d97-a383-86fab2530fd3 | -1.42349 | -52.27559 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3360cca4-1396-33dc-8e62-e33658e55016 | -2.85118 | -51.78104 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a4c385b-9f66-37b0-ac76-68dbcc914da3 | -4.73832 | -43.25032 | 2024-11-08 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d63cfdcf-01f2-390c-8d64-f0c2f641ad1e | -2.95757 | -53.86062 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c84b05bd-d416-3436-9c7a-cedc0c6f95c9 | -2.62217 | -51.74498 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0779601c-3606-3149-838e-c0c5d38e12b5 | -4.09336 | -48.51388 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d68e185-918f-3fbc-91c6-691d80dabf13 | -0.90044 | -51.76691 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a4510679-af1b-3fcc-a2d6-7faf667b2cdd | -1.19153 | -51.9954 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54d43af9-5a94-32be-8ece-aa869fc7d608 | -2.73281 | -51.73397 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01e60c77-fe31-38e8-af05-122f742bef91 | -3.01658 | -52.35492 | 2024-11-08 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b06085a5-aa84-3a64-9681-7bdb445ead52 | -2.02133 | -53.29846 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da741698-0e57-3b4d-b162-515dfb35d696 | -1.24337 | -51.77135 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67f32cd8-2aaf-3004-97b1-71b39b7532e6 | -1.98707 | -45.61462 | 2024-11-08 04:53:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00178daf-3987-31da-968b-f8e3e261c122 | -1.11605 | -53.17729 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ef5c205-f141-355e-9513-7c49b5ffda5f | -1.38596 | -47.50388 | 2024-11-08 04:53:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 674d407c-03c4-309b-9881-bf5e0c6b5fbc | -3.05238 | -51.14444 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cdb71f6-83e9-3892-aa9a-73ace0f25bd7 | -3.37352 | -50.22765 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beacd139-983e-3195-97a2-e74dd3693b0c | -4.38163 | -47.22625 | 2024-11-08 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c42de312-1cdd-32ad-9ea3-40f23d9a6141 | -1.73385 | -54.14523 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b95171e-c95d-3252-86d3-b87db90d6afb | -1.64643 | -47.82429 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26379969-6b52-3828-867b-b55633e96bcc | -3.39422 | -51.87621 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87cc7f7b-0902-39e7-9453-4e6b09e4a0ed | -2.97008 | -53.87003 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c29570a-395d-3ff4-8510-d9b3ea279d1a | -5.64141 | -44.24917 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c708c4ec-a27a-35e0-9f68-9dffbb882017 | -2.97529 | -53.27429 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 449d5e9d-7e27-35ef-b84a-9b98bea02ea5 | -4.33953 | -49.35342 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee652f06-ae9f-33ce-a1e5-bde73c200e1e | 0.03733 | -49.51808 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6cd8061-a3dd-33bd-989d-f16051065a29 | -3.52688 | -51.52725 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1c4e67e-ea1a-3457-8841-2511960d0d00 | -4.77483 | -45.7429 | 2024-11-08 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3078d166-f994-310c-b467-017d1cea4d09 | -1.16971 | -53.91003 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 76addcc2-af2f-36ee-b871-7fbcae97112b | -2.42904 | -48.60167 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1847ec13-2b17-3d48-8d6b-237aaaa1ce0a | -1.15248 | -52.00702 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 551517f6-5865-372f-a9ab-6e9944d99337 | -3.81995 | -46.45646 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f7283ab-40d0-362f-b374-b0f4a0b8d449 | -3.02477 | -48.09054 | 2024-11-08 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4f38ed9-082a-32ca-b51f-3e7a83f201d4 | -3.23808 | -53.39555 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82f70560-0100-38e9-9c9b-6fc444514f17 | -4.22909 | -46.90602 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11fcb1e7-7c1d-3586-9823-e0db23cdaf7f | -2.72951 | -51.73346 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cdcf6c0-def4-3c22-a9b9-91e561d15605 | -2.21107 | -53.67437 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 481c0b9a-8be5-3fcf-9c6a-bc1e52bf1476 | -4.08405 | -43.36299 | 2024-11-08 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eec68144-ef92-38de-94cb-8247a169cce4 | -1.06517 | -53.66215 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0747ea03-e59a-36e4-a0cd-666902559099 | -3.01317 | -53.44104 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 162981a3-42fd-3512-821a-38f3afde3d20 | -2.81027 | -53.9939 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d678f10-eee7-36a0-abb6-313073661cc1 | -1.53037 | -54.29023 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3994825-de4b-3c0a-8d92-76fc188e501b | -4.6802 | -46.40425 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f0ae8662-7387-31d7-b106-78f4be594c00 | -1.38666 | -52.20552 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e19bfe86-5b8c-31cf-88f5-b7f251df14f6 | -3.07366 | -50.57114 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 145e8009-8a54-3406-92c2-1f7a4ec30365 | -3.71037 | -41.68981 | 2024-11-08 04:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b40fc1b2-11a8-364a-a9f1-50118d820866 | -1.15686 | -52.00064 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63b204be-b625-3129-a25a-19cf3f384d7f | -1.23891 | -51.75662 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be5f12d3-a8ea-33ec-a153-6f830b6b6b3f | -3.03621 | -51.53156 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3c75a3d2-afee-398d-a798-f05af6e41c7c | -2.60736 | -51.75325 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21f905a7-848d-3911-b582-8522be38cfdc | -3.951 | -48.14605 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f107062d-929b-379b-b9ef-ce852d3ae1cd | -4.50871 | -45.67934 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80efc2c6-0f63-3b5f-89ff-5f8a7327ecad | -3.24088 | -53.39966 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0afa6133-1477-3507-97b2-4a226bc086ff | -3.30176 | -50.07703 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c652d577-e8d5-3342-8fe6-69882453810a | -1.15579 | -52.00752 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2b8a3287-b598-3703-8174-d58a0a246879 | -2.84349 | -51.34947 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d8729f9-f3fc-3d49-ac7b-072bac948d7a | -4.73253 | -43.25285 | 2024-11-08 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b5ccf11-674b-390c-89f7-2c8121133a47 | -1.63614 | -53.44345 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74ea2b69-83ab-35ac-920f-d0d408db7471 | -3.02629 | -51.53003 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 209f43f5-5cf4-3122-8109-8797721891d0 | -1.50913 | -52.16148 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d00cca1-2758-33b0-9058-409c5032c74f | -2.77951 | -52.87173 | 2024-11-08 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46ed561e-ca87-3460-b243-a9e99fda2ab3 | -1.14694 | -51.99912 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cb095e51-7e64-3fc0-8f1c-b728f1267618 | -2.22263 | -50.85865 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ece86b3e-04e7-3b81-bc0b-070efc217556 | -3.24455 | -50.44969 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 522f652f-f9ee-3d79-aa7e-fcac44145913 | -2.08294 | -46.17202 | 2024-11-08 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 427370b7-facc-34f0-a656-b68b27baa8a3 | -3.08705 | -53.27698 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12f005a3-29ce-300e-8729-e960ff23bb12 | -4.8876 | -45.42624 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d10f3b86-d58e-30c3-a135-2dfe1e9014c4 | -3.38146 | -50.22134 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0195c782-f94a-339b-8c39-a571bdb2d3ec | -3.02949 | -53.27172 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60b90f96-144c-357f-940f-46a88dcf42e3 | -2.79116 | -51.35906 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31838977-274c-3e8e-907a-6f794d26712b | -3.38714 | -50.22974 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4474919-2e97-3cd6-8784-8d5f0ea75082 | -3.97326 | -48.17765 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| d1c57f8e-d61a-3a94-b311-19a1a4ced15e | -3.30404 | -50.08495 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0bbfb0a8-ec8a-36be-9ef9-a6d91c23d5ce | -4.67856 | -46.40649 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 171629df-8061-3e32-983b-3a7d444305de | -1.75581 | -54.19627 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d3c08c3-f007-3f49-8dba-bb9f3225e727 | -5.37312 | -46.2646 | 2024-11-08 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdb5fd4f-d7ca-3fd0-aed6-c46e7f4f9990 | -2.2172 | -53.72441 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55c46399-8c16-39bc-b046-68749d185fc6 | -4.31595 | -49.22072 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9b0f923-e6ea-3b22-9e05-3ac642365e66 | -2.05567 | -53.30003 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27c06f12-2421-30d0-be1d-03dcc3a50801 | -3.54871 | -47.38052 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5c11ca7-30ff-3cbb-8cbe-cc60212a824d | -3.03741 | -48.03957 | 2024-11-08 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 509bf027-6916-3407-ac30-e67d9df18fc0 | -2.96652 | -53.91511 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7db0d39b-49ab-3fa6-9c15-295423675655 | -3.38033 | -50.22869 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6995d6ca-9e08-37f6-bf14-c5bef538ad60 | -1.13233 | -53.72605 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d7837cd-7cc0-3d3a-ab14-c8d01f3a9d6c | -2.91465 | -51.04496 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3612942-bb48-37ce-b8af-36466def7e59 | -1.38388 | -52.20156 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 297f0a9e-88f6-3851-8665-e4b7f20e32fc | -3.08726 | -53.8842 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd7bdab8-76a2-33b4-9d40-762134adc2a3 | -2.65067 | -49.24112 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4736d3ed-d855-3c8d-92c0-4478d9018e0c | -3.15127 | -51.69085 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc87292a-bf43-3773-bf2d-c368ca96686f | -2.07498 | -52.04526 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67d27682-9255-3bc4-8303-856cb85427f1 | -2.81077 | -52.95545 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c23e19ca-75ef-3167-b259-8f0a825d19a6 | -4.51636 | -45.6897 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 3ed07c2f-644a-308e-9d5f-f436cb36d177 | -3.80436 | -43.59638 | 2024-11-08 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ebe1334-0400-36fe-825d-7331e8be42e5 | -4.22474 | -48.6125 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README30.md)
