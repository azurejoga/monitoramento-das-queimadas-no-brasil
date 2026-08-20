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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f07b13e5-26cc-3559-808b-f5b7c1169cb9 | -7.64956 | -42.75528 | 2026-08-20 04:00:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6b2c2a3f-9f05-3b14-9101-b204b4e06aab | -7.02434 | -45.89157 | 2026-08-20 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eed89a10-74e3-3e36-a6f1-bf9f1fecf718 | -6.7796 | -42.8858 | 2026-08-20 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d3c32f64-e8d0-30de-8e86-ad84339b1734 | -2.64054 | -47.98925 | 2026-08-20 04:00:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e009432f-721d-37ea-b3fd-6f4a8be0b566 | -3.47007 | -47.70101 | 2026-08-20 04:00:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7114a09-0167-3239-a7e1-c51887f8a8b2 | -7.22022 | -43.30391 | 2026-08-20 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b5f1c95c-007d-3e50-9b03-068f342a9a34 | -7.01329 | -45.89303 | 2026-08-20 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f414fa90-94ab-376b-b42f-672566ccb3f4 | -3.96642 | -43.10849 | 2026-08-20 04:00:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5b8e064-7038-3f59-9ffd-049412b08f94 | -2.57133 | -47.24085 | 2026-08-20 04:00:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0b584b5-17ca-3714-8247-33bf53a53f56 | -4.9351 | -41.98385 | 2026-08-20 04:00:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8d13e9ff-3462-32f5-bcce-cb581cd7e0e0 | -2.80267 | -48.59449 | 2026-08-20 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2c59fdc-e882-3514-9594-d6da6ff469f4 | -7.59921 | -45.17295 | 2026-08-20 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 6a2bf37b-8868-30e3-a6fe-0a9ddd24a9fc | -4.12479 | -49.44861 | 2026-08-20 04:00:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c590a15e-7a60-3306-af12-d84005e7b04b | -7.96369 | -44.66417 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 78750978-1aab-3d8c-b9f5-b4aaec058b01 | -6.26606 | -43.27618 | 2026-08-20 04:00:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7c638a5b-2cc4-393a-a067-3d5fa3456926 | -4.05768 | -38.29215 | 2026-08-20 04:00:00 | NPP-375D | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4bced649-636d-3d76-8aae-0401320e684c | -6.42438 | -35.08381 | 2026-08-20 04:00:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c91333a9-ec9b-3f35-8feb-bdacc78a9208 | -6.17207 | -39.38335 | 2026-08-20 04:00:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 055ef24a-b846-3a53-b86a-78eb2b2f5541 | -3.97797 | -49.20075 | 2026-08-20 04:00:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03c5b978-b22b-33cd-bcc6-fa679fc5e09a | -7.182 | -43.1102 | 2026-08-20 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 490c9b62-348c-3ea9-bb93-acdde819db25 | -7.17762 | -43.08429 | 2026-08-20 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 00e8a5b8-7346-3d91-a4fb-940b37f1a90c | -4.05828 | -38.28844 | 2026-08-20 04:00:00 | NPP-375D | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ad922be0-9ba8-3c78-b934-b40095818019 | -7.95924 | -46.91619 | 2026-08-20 04:00:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 803ed475-6835-36d8-ad74-62bb266aa3ee | -8.35972 | -46.33598 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86c3ee74-12f2-3591-8144-34ee208c636e | -5.53942 | -42.27311 | 2026-08-20 04:00:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3e8f7cb2-a12a-381b-a24b-b3b21af9a7b3 | -7.7596 | -49.20867 | 2026-08-20 04:00:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72ef9c7e-c88c-33b9-9e8a-6e8b1adfd8f4 | -7.34659 | -45.83723 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5be1a0f0-c3b7-3f98-939e-58e77fd3109d | -6.26776 | -43.27359 | 2026-08-20 04:00:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ec5117b7-a7d9-3138-938e-06621bb71535 | -2.56435 | -47.24696 | 2026-08-20 04:00:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e2f9aa3-6ef6-3c2c-b70d-7fb12203c93c | -5.42603 | -43.43371 | 2026-08-20 04:00:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2eeffb58-bce9-39cf-ba46-e8a06e20b2f4 | -6.29027 | -43.64671 | 2026-08-20 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6ec948f-4a7b-3f10-bfda-391ab3d11241 | -5.21094 | -42.76283 | 2026-08-20 04:00:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 28b11e6e-8d02-339b-b18c-225b65f92309 | -2.57199 | -47.23891 | 2026-08-20 04:00:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 684cc78f-cdff-3a99-b1d4-6d034ba8fab0 | -9.40112 | -37.8119 | 2026-08-20 04:00:00 | NPP-375D | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0c586031-fcd7-3c82-bc27-9de5a4e2ccd9 | -6.24142 | -43.68603 | 2026-08-20 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a2d7173-bc71-367a-9402-2e59976deb3e | -8.36442 | -46.34 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27727735-12e6-3810-8dca-fcc47b107883 | -7.17332 | -43.08351 | 2026-08-20 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d0a43f2f-4168-3670-9d4a-3c4daae0226b | -9.38949 | -37.82078 | 2026-08-20 04:00:00 | NPP-375D | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0cb69b3e-4145-3cb1-9b88-bde5720374c6 | -6.34361 | -44.08121 | 2026-08-20 04:00:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 444d9f8f-2afa-3300-be12-aa2f62f97c9f | -7.35052 | -45.81549 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 531e7fc7-d3fe-3029-8e23-53950b5c2477 | -2.81031 | -48.58984 | 2026-08-20 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9cf73b0-28bb-3eaa-9317-c0b6bd497542 | -4.28304 | -46.51687 | 2026-08-20 04:00:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7eacbd17-95b0-329e-9675-cecf2089da08 | -2.57204 | -47.20059 | 2026-08-20 04:00:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e181bf0-f67b-3a4d-97be-54a4dc62aaa9 | -4.89989 | -46.83493 | 2026-08-20 04:00:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 042b89d1-edfc-3b54-8443-28bd021ba33b | -6.78101 | -42.87764 | 2026-08-20 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5818b29c-2978-36fe-9a3c-17831fd0e2c6 | -2.56976 | -47.24992 | 2026-08-20 04:00:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a6158139-86fe-37df-9b65-cc71c60100f2 | -2.64174 | -47.98805 | 2026-08-20 04:00:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 578d61ed-e0c3-39e7-b0db-bd891be0eb27 | -2.80932 | -48.59557 | 2026-08-20 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 199ae6b2-001d-3d40-b9c4-70c23178e805 | -7.35917 | -45.82673 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8fefdb6f-8a7d-3836-a132-e8e3e00d72c5 | -6.23686 | -43.68523 | 2026-08-20 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d87a1a91-8064-3dff-8133-3b5b07a1d6fe | -7.96969 | -44.66212 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 942eef21-b009-3a13-afcd-a3ee893de374 | -7.3494 | -45.82167 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d13081b1-7c7e-3df1-9947-bdf7881aa3b7 | -10.4537 | -37.14323 | 2026-08-20 04:00:00 | NPP-375D | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2cf4811c-b3a8-3124-817b-1c9d978b6a67 | -2.57778 | -47.20351 | 2026-08-20 04:00:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f806b5f-356d-3eb8-ae2b-a3ca0c5e72fd | -4.09327 | -42.50819 | 2026-08-20 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3c6e6a10-57d9-382d-a065-23c1b90c0b2d | -7.3431 | -45.82695 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd5b67fe-075e-3bad-a348-fbcbfb295161 | -4.90066 | -46.83062 | 2026-08-20 04:00:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a417b6e-36f0-3c7e-804e-9a74a12af9a8 | -7.49041 | -43.8199 | 2026-08-20 04:00:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a793531-611a-3e0f-85cc-20d28e9eac2b | -7.97403 | -44.6608 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3ca38786-4ac1-3910-842f-eb19a066a3f7 | -7.76486 | -49.2077 | 2026-08-20 04:00:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8967481a-9169-3883-9846-7a047188478a | -4.90108 | -46.82837 | 2026-08-20 04:00:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c37634e8-a4ab-365e-ac45-f54fc1a6d72e | -7.96928 | -44.66003 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 110f2f60-f496-3a5e-b4fb-8d91f4d8f988 | -5.8367 | -42.63379 | 2026-08-20 04:00:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| baa03a2b-49b1-3d0f-bb12-dac7048d72eb | -7.35288 | -45.83198 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5c5f383a-c82b-3e6f-aced-ab2c221e9e18 | -7.61212 | -45.15749 | 2026-08-20 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 47fb42b0-bb79-3eb7-a939-385ca251e907 | -7.01648 | -47.97655 | 2026-08-20 04:00:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 490458b0-9cf6-308d-b69a-d2940031780a | -8.94797 | -38.00057 | 2026-08-20 04:00:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 70369a9e-0364-394a-aa9e-49649f2d158c | -6.17909 | -39.38454 | 2026-08-20 04:00:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c917f214-c7d7-3f6f-aeec-e8fd11ee9ee8 | -7.96843 | -44.66497 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f0c72137-b0ab-3154-aa09-1e045c737458 | -5.23058 | -37.68633 | 2026-08-20 04:00:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b92e0a84-4607-351b-9d05-df8123935a7b | -6.26703 | -43.27797 | 2026-08-20 04:00:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 706146a6-1552-37f2-9479-bf3e97b72384 | -4.16547 | -38.44667 | 2026-08-20 04:00:00 | NPP-375D | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 18dcd2af-8398-3f97-a975-4a89f1a06da3 | -7.34367 | -45.82384 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb666236-ed54-3887-9c8c-9417151f9775 | -7.35401 | -45.82573 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ebc2f3b1-4998-386f-843d-884c5b907240 | -7.35231 | -45.83513 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2bec75d9-0334-3fac-a37e-3efa3b17620b | -7.12053 | -47.49652 | 2026-08-20 04:00:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb2d96f5-6886-304b-848f-b0f9c69bd56f | -7.75851 | -49.20638 | 2026-08-20 04:00:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6e3c440f-4beb-3be9-a657-f56451e12d95 | -4.90036 | -46.83261 | 2026-08-20 04:00:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a51ec83c-756e-33b5-90d5-ba6664905c1a | -4.09969 | -42.49637 | 2026-08-20 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cb2ed087-4735-32e1-a36f-381f78c2a20b | -7.59823 | -45.17849 | 2026-08-20 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b3cb1c02-477e-3bea-aa14-fbc19df17290 | -7.3586 | -45.82986 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a907c601-8130-35c8-80cb-6ab9494fdb68 | -3.68542 | -47.65413 | 2026-08-20 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e4b91e5-d7ef-3b47-983b-c7849a0fa479 | -5.54363 | -42.27369 | 2026-08-20 04:00:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0d477d3e-c710-3fa5-89e2-d2e94bba2c53 | -2.57161 | -47.20277 | 2026-08-20 04:00:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5e3e9a1-45a6-3910-aab1-405adaa5394f | -7.65056 | -42.77824 | 2026-08-20 04:00:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cf7c9a7c-e572-34f1-b48f-f2a08d3bf341 | -7.6042 | -45.17352 | 2026-08-20 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6951e9b2-9bdb-3819-9361-5f59fe6c90f4 | -6.13867 | -47.23092 | 2026-08-20 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 33dc7d52-4a41-33ae-8e60-931209d4a86e | -6.14448 | -47.23186 | 2026-08-20 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f1f4a6b6-3413-3c11-a9a1-98efd07b2fe5 | -6.29441 | -43.65047 | 2026-08-20 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2413a5b6-b4b1-37f5-aac8-e95bd8698c31 | -3.68629 | -47.64916 | 2026-08-20 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c9d5e98-91c8-346f-afdd-90a3ff2657b2 | -6.42381 | -35.08752 | 2026-08-20 04:00:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b897e517-ad67-39ef-a615-316fe1bd1ff8 | -3.97122 | -49.1995 | 2026-08-20 04:00:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ee978cf-5134-3dd7-90c7-645bb2c4c967 | -4.05485 | -38.28788 | 2026-08-20 04:00:00 | NPP-375D | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 98f74f76-0d1b-3fa2-b04f-33715848eaa5 | -2.64144 | -47.98391 | 2026-08-20 04:00:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c77a7ff-75aa-3517-a662-c8869b9dca49 | -7.12604 | -47.50373 | 2026-08-20 04:00:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9339556-df86-3d5d-ae96-02a7768f9a23 | -7.60519 | -45.16794 | 2026-08-20 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| aaf7695e-11cf-3c8d-8ae8-5c5e82987e18 | -7.35345 | -45.82885 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a549c9be-891d-37b4-8fa3-0e26d48379a5 | -6.78388 | -42.88654 | 2026-08-20 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ef1c04ba-eedc-3f41-8e30-55efa55f32e9 | -7.34884 | -45.82478 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9c24bdf3-96ad-37ac-b563-9924eca4a9eb | -7.63606 | -42.73318 | 2026-08-20 04:00:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
