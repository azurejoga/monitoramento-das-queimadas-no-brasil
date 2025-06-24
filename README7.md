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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25ba9385-cfce-3e49-8e6d-60bc7909c2b6 | -6.63824 | -47.85925 | 2025-06-24 04:02:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69b7da90-038c-332b-907b-ed0e6f9762fa | -5.7064 | -36.24033 | 2025-06-24 04:02:00 | NPP-375D | LAJES | RIO GRANDE DO NORTE | Brasil | 2406700 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e753798f-1404-333a-a36d-a585e38151be | -7.09354 | -44.37229 | 2025-06-24 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3408095b-abd7-3134-a8d4-714aa1cfd17c | -7.0553 | -43.92319 | 2025-06-24 04:02:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0266e1a7-93dc-3bd8-a358-dacef17ecea5 | -5.49015 | -42.14814 | 2025-06-24 04:02:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a7160dff-b392-36bc-a4ce-414932ed3de4 | -7.29571 | -38.9815 | 2025-06-24 04:02:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| df45e70e-0a29-3208-9f10-c6bc228c420a | -5.13022 | -45.03055 | 2025-06-24 04:02:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18ab3543-22cc-3df0-ae6f-a50f34d980cd | -7.06053 | -43.91484 | 2025-06-24 04:02:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d731c22-776d-37bd-8f4e-3fa62a28911f | -5.20809 | -43.31027 | 2025-06-24 04:02:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd76382c-9231-342e-9897-b881ba2f1000 | -4.53985 | -48.00724 | 2025-06-24 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 52c9ed06-c3ad-3103-bdcd-b5aa23f934ff | -7.2121 | -43.1023 | 2025-06-24 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 19187051-cc21-3821-b8ad-c4a6900f45be | -5.75812 | -43.39645 | 2025-06-24 04:02:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffe16cb8-174c-305b-bfe9-c96547fe67f6 | -6.25035 | -44.84179 | 2025-06-24 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4669445f-c9c9-33a3-a0ac-7d94421cc541 | -7.20134 | -43.10054 | 2025-06-24 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d95f3fe9-9c26-3e9c-a828-0da5947d122c | -7.13116 | -43.7512 | 2025-06-24 04:02:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa8931d6-2b9b-3188-bfc0-f89d1c455788 | -5.48666 | -42.14757 | 2025-06-24 04:02:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0876c554-a80e-30d3-8bb9-484270a21e28 | -7.32737 | -43.22469 | 2025-06-24 04:02:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ec271863-1d7c-3132-a1b1-86263df835e6 | -5.78182 | -43.60792 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1540ab2e-8cc8-3e8d-9500-01bc780e128d | -7.29173 | -43.21198 | 2025-06-24 04:02:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c1d9b983-ec2d-3cd9-ab41-b323674f30a6 | -6.25091 | -44.8384 | 2025-06-24 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a9d0ebb-6323-3432-8e07-6052c8a08c6f | -7.32873 | -43.21648 | 2025-06-24 04:02:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2750022-0c45-3dc8-a035-759be19df1b5 | -7.20918 | -43.09761 | 2025-06-24 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| fbb8113a-ae96-30bd-a672-e4a292c022db | -7.20785 | -43.10583 | 2025-06-24 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a7d17958-ebfe-3ea6-9b6f-1e899c2e0c76 | -6.94868 | -42.80771 | 2025-06-24 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6b48cdd9-07b8-32a9-9cd5-f0f3a2479321 | -5.78409 | -43.61747 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 015719e4-de6b-3d0f-a657-7bf9e8a6530c | -7.29669 | -43.20428 | 2025-06-24 04:02:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ba869937-673e-3b02-b734-c0fc444606ec | -7.52644 | -44.08978 | 2025-06-24 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6147ba3-bdf1-3b0d-acd4-2ad36f5625fd | -5.78858 | -43.61362 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fcae512-3e1b-35c9-9a06-5a47ba0e1560 | -5.49078 | -42.14427 | 2025-06-24 04:02:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d938dc24-9ae6-3c1f-aa82-7162b2789a05 | -7.09738 | -44.37297 | 2025-06-24 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ad96c04-53bb-3332-8d30-d05c61ca0b36 | -3.02207 | -49.42916 | 2025-06-24 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88362626-caa5-39b8-b933-575af2e678aa | -4.53935 | -48.01019 | 2025-06-24 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8ec0ff0d-25d6-370e-a379-df0359517137 | -5.78556 | -43.60854 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6660d47-74c1-3631-8594-95bdfef8e124 | -4.5347 | -48.0066 | 2025-06-24 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 738c0c99-7d0b-3e69-9445-9a852bdfd76f | -5.9799 | -43.76603 | 2025-06-24 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3ffbccb-1a2d-3fa3-bc3c-6707cf2004d2 | -4.54449 | -48.01093 | 2025-06-24 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b0f704d5-4e44-3694-9e8a-70b3cbd61ece | -7.54013 | -38.5522 | 2025-06-24 04:02:00 | NPP-375D | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8382c7c8-25f9-39ad-a35d-335a6f8be0bf | -7.01045 | -44.60708 | 2025-06-24 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2f757ff-2860-3ed1-b46c-db66d9df21de | -4.27886 | -48.18671 | 2025-06-24 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 021013e0-830a-3e2d-b910-4b7267425d3e | -6.95354 | -42.80034 | 2025-06-24 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a4e450a-d3aa-37e3-a8cf-1e1d5481eb50 | -7.00651 | -44.6066 | 2025-06-24 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ec744f5-562c-32ad-b194-26a009c450bf | -3.02783 | -49.43013 | 2025-06-24 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3ca7e09-9cbd-3164-b997-d507b34b4aa2 | -3.02717 | -49.43413 | 2025-06-24 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32341527-c459-381c-976a-4ff8ab8c2df8 | -4.27367 | -48.18579 | 2025-06-24 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff7cdd25-2389-3aef-a1fc-508f51ee13c5 | -7.20067 | -43.10465 | 2025-06-24 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 5d923bf2-3edd-3f05-8be2-d63e5bdac672 | -6.95026 | -42.80528 | 2025-06-24 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ea0b1773-d3ed-30b0-838a-6d966214d5d4 | -6.95222 | -42.80831 | 2025-06-24 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f09ed25a-0680-351d-87e7-22b20215176a | -5.78784 | -43.6181 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a306976-128e-3ced-9747-3c398acc7362 | -5.91571 | -43.47668 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 39996ad6-344f-36ca-9e97-fe424a0dc2d0 | -5.91942 | -43.4773 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2c6bf7d2-f46a-3360-bd2e-95c73c78e86b | -5.48728 | -42.1437 | 2025-06-24 04:02:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 02b8e14c-3b8a-3ca7-8c8a-9e1088a00962 | -5.78109 | -43.61234 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 249ad8d9-de02-3d7f-b1ed-129503b615ba | -6.33831 | -43.74874 | 2025-06-24 04:02:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55ae04af-5c08-3d8a-b6ae-bbfab9e5b391 | -5.48379 | -42.14313 | 2025-06-24 04:02:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ecf5fecb-fbea-30f2-a12c-c837bef5d68a | -7.32805 | -43.22059 | 2025-06-24 04:02:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 916b28fc-10c3-3cdf-9efb-36cb7c337a46 | -7.68675 | -40.15711 | 2025-06-24 04:02:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3bb845be-321b-3af0-8f5c-e0383b582134 | -7.05905 | -43.9238 | 2025-06-24 04:02:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a70f7172-6496-3fa9-8619-cc231898b90e | -6.16979 | -47.27488 | 2025-06-24 04:02:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d514db68-6db0-3e9a-9276-754b633efbf7 | -6.17451 | -47.27577 | 2025-06-24 04:02:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 607e3540-1d97-3f74-bcff-93da0faca565 | -5.75441 | -43.39585 | 2025-06-24 04:02:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79a29692-ca9e-364d-abcc-44c964c823b9 | -7.34126 | -45.32992 | 2025-06-24 04:02:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 301dd2ba-706b-30d9-a576-86f66d2a2c55 | -6.00625 | -43.74701 | 2025-06-24 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a81bd169-dd1a-3184-b2b5-0c65f4925a60 | -5.91789 | -43.46344 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91d76123-6c46-34a9-90bf-47e0b771ba9f | -4.66148 | -41.96097 | 2025-06-24 04:02:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9dc283a-f8d0-32c6-8b85-2a0f05672b63 | -5.91869 | -43.48174 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6eb84251-6cae-3e8f-b41c-e97e15f73c88 | -4.55672 | -38.46092 | 2025-06-24 04:02:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2140aa6a-d205-3618-a1ce-1544e5fdb4ad | -4.53886 | -48.01315 | 2025-06-24 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 395fa1d4-e337-33a0-b4dc-6556f91e2658 | -6.34279 | -43.74491 | 2025-06-24 04:02:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cae3fed9-6df6-3d33-a34d-1ece0e55222d | -7.0897 | -44.3716 | 2025-06-24 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c78f095c-59c7-313d-8731-2e89b90f2a6e | -5.07148 | -43.72724 | 2025-06-24 04:02:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afc7adb4-e2db-366c-ab7b-4bd3bcd8c396 | -5.76182 | -43.39705 | 2025-06-24 04:02:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 353a8821-fcb5-38a3-98e6-aea39f56e0f1 | -6.07829 | -37.94336 | 2025-06-24 04:02:00 | NPP-375D | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7025c42e-8dd6-3f43-9daa-e6b7ae730d14 | -7.34533 | -45.33057 | 2025-06-24 04:02:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2d3a76d-e5ef-3014-b747-9911c8e0b2e8 | -3.02141 | -49.43313 | 2025-06-24 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11ca80e0-dadd-335d-ba81-5ef989abb9d8 | -4.98024 | -37.40183 | 2025-06-24 04:02:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd84da85-5a02-393b-9555-9331794289e4 | -4.2742 | -48.18268 | 2025-06-24 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c03c995-cd93-3f0c-b10b-50cbb49ca732 | -8.55456 | -51.55971 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0886894d-96a7-3605-89a1-e12e21c24516 | -14.4344 | -48.92018 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 86078131-c772-3d83-a922-324a3a8ab72f | -13.55156 | -42.48986 | 2025-06-24 04:04:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ac078000-06b8-3a1c-9745-a4be627610d6 | -10.87231 | -49.5445 | 2025-06-24 04:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 058b62b7-55cd-3c33-b136-e0357aa4f191 | -8.57053 | -51.58131 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7240d05d-7ae0-3076-ba84-af05a86299ad | -14.51713 | -40.35896 | 2025-06-24 04:04:00 | NPP-375D | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 58021535-f888-31ed-aaa7-a0955850ea43 | -8.5791 | -51.56907 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c3aa153-ec5f-3098-88c9-15ea5605b6d2 | -14.4363 | -48.91332 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d424b641-f8bd-3181-9bcc-908f5e46ccf2 | -8.069 | -43.1133 | 2025-06-24 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2ff27a84-215d-3380-8871-5b76bed330dd | -11.27518 | -52.46901 | 2025-06-24 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dc8675b-2048-3dc0-a5cc-46885eb93112 | -12.75113 | -44.40941 | 2025-06-24 04:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f7ea5b44-f450-34e6-8b95-0b5122c8532c | -11.57249 | -47.43044 | 2025-06-24 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6472a56a-3b11-34f6-a067-7f68b019eea4 | -12.23 | -40.35646 | 2025-06-24 04:04:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 788c9cd8-a0ff-312f-a039-d470b6db33a0 | -9.16642 | -43.13528 | 2025-06-24 04:04:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d03a61e-a15f-3e02-8ce0-8aa9792f53b7 | -8.14395 | -47.13646 | 2025-06-24 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f472a37f-061c-3b22-b135-667ad9e7c263 | -8.06321 | -43.10407 | 2025-06-24 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 8e4ebcfb-a682-3da7-8532-ea01d0e6fd9c | -12.68527 | -44.40643 | 2025-06-24 04:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f41d0355-1f78-326c-8c4c-a8477b7c819e | -13.25917 | -41.32775 | 2025-06-24 04:04:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 395e6a36-ab0e-3085-af42-9932653e83a6 | -10.59454 | -49.46317 | 2025-06-24 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5eed08b-77e3-3cb2-b2df-d3e9983f6db1 | -13.64082 | -41.35695 | 2025-06-24 04:04:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d0e0e3be-18d7-3f68-9885-dfaa76c90c42 | -9.41895 | -48.42199 | 2025-06-24 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2def6112-e3c6-38e2-adcd-20768aa4d492 | -15.64652 | -41.25509 | 2025-06-24 04:04:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f8abacbc-2350-3aa6-9535-17a02e0a1d06 | -10.95145 | -47.39228 | 2025-06-24 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 308f8f1d-8d6b-3f5c-b0c9-b009cbc11b3a | -14.24539 | -43.75903 | 2025-06-24 04:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README8.md)
