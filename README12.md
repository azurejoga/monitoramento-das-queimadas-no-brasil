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
| 4bc05f31-f9f9-3a81-a80b-f6ad7f0ca2c1 | -7.69927 | -47.28572 | 2025-07-05 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adbbf16c-b2d1-3faa-a2c9-a4ee1802d30d | -7.9618 | -47.2277 | 2025-07-05 05:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89bea106-b5a9-3da8-8ab6-ebbd25327dd4 | -7.34936 | -49.63301 | 2025-07-05 05:10:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66acc73b-bf44-330e-bb85-d404f11987ae | -7.94649 | -44.85002 | 2025-07-05 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d03bdef8-e9ec-3356-8c01-379a97e37790 | -3.52268 | -48.43385 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 035350a2-ec09-3188-8b58-187d3b0e51fd | -6.80283 | -44.75617 | 2025-07-05 05:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fdca19c4-2dcd-37e7-bb24-feac27d44f6b | -7.18982 | -45.32878 | 2025-07-05 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bd0955f-cb1a-380d-aa40-962fe14ec00a | -3.52646 | -48.43293 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2a20dec-63c4-3dcd-8b77-30666b168e6c | -4.11014 | -47.95442 | 2025-07-05 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8cb0a88-dd17-33a7-aa4e-f7313447da94 | -7.94784 | -44.85257 | 2025-07-05 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 139da249-50c6-3e26-b5c8-c5121c0f7ef3 | -7.3444 | -49.63228 | 2025-07-05 05:10:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd28753e-9453-3ff3-95d4-5808ad43c46a | -5.06861 | -43.72649 | 2025-07-05 05:10:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b0e3841a-af10-3ef7-835b-c67ae82d5242 | -4.2797 | -48.19035 | 2025-07-05 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13de8268-11f5-3984-aa53-c3e62be2bfe6 | -8.01686 | -49.72237 | 2025-07-05 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f055466e-5391-39ae-be12-5e4057c9ddd2 | -4.27924 | -48.19356 | 2025-07-05 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60f754f4-9519-3de4-a94c-3d611cfc53cb | -5.99629 | -43.73434 | 2025-07-05 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d37df6f-934e-3903-bf8e-e5128d4c20fd | -7.94862 | -44.84603 | 2025-07-05 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 327e05f1-07ad-388b-82ed-11cab967fc6c | -6.01026 | -44.52784 | 2025-07-05 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c42b7a6a-b93c-316c-b42a-c14cf6eb1506 | -3.52561 | -48.43885 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fbd9281-c0e1-3f71-9220-2e27bc4452da | -5.04991 | -43.85925 | 2025-07-05 05:10:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e17043fc-a704-3540-bdad-ced9a00c8fc9 | -5.61298 | -45.17916 | 2025-07-05 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e0d8845-978d-3be8-aa21-d72a50cfe114 | -7.34775 | -49.63648 | 2025-07-05 05:10:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0401aaa4-2ba5-3b3b-a705-0c79d4692ab7 | -8.09366 | -45.39161 | 2025-07-05 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5769958-a0f8-36b9-95fa-c7d91f195ed6 | -4.39598 | -48.93812 | 2025-07-05 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5da6332-400d-3095-885f-32f148201a94 | -6.87838 | -48.16847 | 2025-07-05 05:10:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5520054e-1003-3b02-8e37-34c725f275d4 | -7.19055 | -45.32309 | 2025-07-05 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08a2f19f-1d7c-3386-9c5c-afd77af079b8 | -7.96716 | -47.23241 | 2025-07-05 05:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e987981-6f1c-3086-a0fb-310c0556b679 | -4.28494 | -48.19112 | 2025-07-05 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57b62d95-2754-38e5-b7eb-3beb677fb30e | -4.10719 | -47.93756 | 2025-07-05 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0063f393-7c0f-3501-b89c-62c0321ff800 | -5.87333 | -50.15013 | 2025-07-05 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98b70e8d-568f-3c94-9baf-0450f98da094 | -3.48958 | -48.44674 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7d83ce19-bf3d-34f5-8cef-7064d05bd555 | -4.11296 | -47.93516 | 2025-07-05 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 91d3f7a8-44f5-3a52-9fbb-1b8d101df25a | -5.72325 | -49.10918 | 2025-07-05 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ad47a54-85a0-3a08-89b9-4508f0d534b4 | -7.15674 | -44.31487 | 2025-07-05 05:10:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c73507c-f361-3816-8f47-9e361e711e6d | -5.87798 | -50.15099 | 2025-07-05 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5724acd6-b1cf-3774-93d0-95c22d381b23 | -5.72367 | -49.10623 | 2025-07-05 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8560c721-ec08-3f61-b36a-567648825d75 | -5.60679 | -45.17832 | 2025-07-05 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0de6e14-db54-3374-8dea-efce6acacbd9 | -4.11248 | -47.93845 | 2025-07-05 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a69802a-602f-361d-99b3-fab00317711b | -3.52224 | -48.43681 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 463833f5-d373-3b33-b7d6-88695242a384 | -5.61374 | -45.17376 | 2025-07-05 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74213541-7ca1-35ca-8548-6c4518488db6 | -6.01703 | -44.52882 | 2025-07-05 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad0a9834-5d00-3654-a7f6-fa8e489b506d | -7.2978 | -45.36372 | 2025-07-05 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 015526d2-916b-3499-8912-0ca5753f70e3 | -5.87588 | -50.15129 | 2025-07-05 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc4a713b-b5be-3ab5-b54b-137f10a26036 | -3.52686 | -48.44063 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fc0fff9-9e01-3159-b758-279cbd51fe85 | -5.99533 | -43.74141 | 2025-07-05 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 763959a1-a40b-3cc6-bbe0-4aa906bdcd75 | -6.79901 | -44.75461 | 2025-07-05 05:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca709fd7-78be-3847-b524-613fa06995c7 | -7.15598 | -44.32077 | 2025-07-05 05:10:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 380fe400-8c91-3a16-a7b0-292d26e54608 | -3.52774 | -48.43477 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0cc4b293-aa69-37cd-af4e-17437610d37c | -5.06656 | -43.73019 | 2025-07-05 05:10:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f437290c-a543-3d12-93a1-9f798cc9ebd3 | -4.11395 | -47.92839 | 2025-07-05 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e80636a-dc64-38a9-97b6-b2c48c16b533 | -5.06767 | -43.73317 | 2025-07-05 05:10:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6b4f6608-6ade-3e9e-a61d-f3c73c64abdd | -4.39556 | -48.94093 | 2025-07-05 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f8ae7d6-bb5f-31d5-addc-140d8f4d526c | -3.51762 | -48.43294 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ac3844c-a7b7-3200-bce8-24cb1193f98b | -5.72408 | -49.10328 | 2025-07-05 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b06c2570-9f74-38e5-8af5-aa3115f8b589 | -8.01743 | -49.71812 | 2025-07-05 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df06c3b3-ca94-3621-801f-eab0eaf5d3b2 | -7.30436 | -45.36454 | 2025-07-05 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13760b9f-599b-3b16-8496-4e63d65e097b | -4.11448 | -47.92478 | 2025-07-05 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c385860-e50e-3a81-b639-586890474c93 | -5.6065 | -45.17829 | 2025-07-05 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90ef6afd-5374-3bc8-8b25-612cc914ef4a | -4.00197 | -43.2355 | 2025-07-05 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 965dfd95-04b3-3652-86d2-0dc3eaf07fe4 | -8.09608 | -45.38692 | 2025-07-05 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d11a723f-b64c-3b48-b1cc-3c78bc693b1a | -3.48404 | -48.44915 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3337af5d-cb51-3596-bf33-6010dbc9f99b | -2.91316 | -48.24955 | 2025-07-05 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0c24238-9651-3ec4-a4ee-ff53e93dd774 | -3.5273 | -48.43773 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74687787-ba4d-3b8c-a128-c1d196f169d6 | -8.01246 | -49.71732 | 2025-07-05 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2017c1e-84e0-3221-9094-3edc27f05f6b | -3.52688 | -48.42996 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e81dd68-1653-3ab8-a772-e534c8fc3552 | -5.99964 | -43.74056 | 2025-07-05 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a8499413-3865-3047-8491-71474ccd6e2d | -4.11345 | -47.93181 | 2025-07-05 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| badbff4f-d0dd-37a8-b6f5-1c880e862513 | -7.02192 | -49.18456 | 2025-07-05 05:10:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2ef5bb8-ac59-3132-8e78-0e166109dcaf | -6.63253 | -56.27631 | 2025-07-05 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5d03cda-f71a-3771-b9e2-63d09974f3d2 | -3.48447 | -48.44621 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a52096a-5bae-3f04-b90e-c9cc7a60be1c | -3.86558 | -50.08503 | 2025-07-05 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 810b81b9-bba0-3f52-914b-c522d59cbcb2 | -5.72826 | -49.11001 | 2025-07-05 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e211c015-a928-3d2e-b8ec-fb223737b591 | -3.52603 | -48.43589 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 45102206-99db-34b3-8efc-7a9f50508a73 | -3.52819 | -48.4318 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 924e74a6-6c42-3aa7-a598-fda949b0eee2 | -5.72868 | -49.10704 | 2025-07-05 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7467f15f-f790-3f5b-aca0-6e2c30ab9f69 | -3.52179 | -48.43978 | 2025-07-05 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51fa0d90-f792-39c9-9975-e0ab60265266 | -8.09529 | -45.39308 | 2025-07-05 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b9edf5e-38ae-3372-abe9-c023a6386b86 | -4.13187 | -54.89842 | 2025-07-05 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2b6af74-5492-349c-b7f4-32f28d23c344 | -12.57898 | -56.97137 | 2025-07-05 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc7580d3-e619-3fe0-b801-6254792a08f7 | -10.36171 | -48.71804 | 2025-07-05 05:12:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3332c121-4474-362c-93df-3b02092c7c7e | -8.37989 | -51.07097 | 2025-07-05 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 58706bbe-acb8-3d56-a342-ae4a4e8f4827 | -10.10623 | -58.22252 | 2025-07-05 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e12e2e7-1b61-3efb-be3e-6a9a529a521a | -9.92121 | -59.90751 | 2025-07-05 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0629f6e-f216-3362-b2df-14f5d19f5c4a | -9.0031 | -47.44942 | 2025-07-05 05:12:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7988d5c3-9f48-3854-8510-f5d4f6dbc5c9 | -11.33324 | -51.44214 | 2025-07-05 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c83bb5e5-af47-3866-b818-8d79992c9670 | -11.05082 | -56.73883 | 2025-07-05 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dcd4770-2db0-3db8-8ad5-0dc0930295c6 | -7.89544 | -63.04009 | 2025-07-05 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e895165-9b11-304d-8a31-2e3f86492a0a | -10.63965 | -46.47063 | 2025-07-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebaed5c3-ba0c-3a8b-90c0-36ccc900d740 | -13.41431 | -47.84378 | 2025-07-05 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29af2646-7ae3-350a-8f70-158cfe778282 | -9.79052 | -64.76443 | 2025-07-05 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db3a13ec-01cd-3225-844e-e0b42dd3149a | -11.48007 | -60.65643 | 2025-07-05 05:12:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c587102-9bd8-3190-aecf-a608637cd742 | -9.57721 | -49.10355 | 2025-07-05 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7ebf511-9cea-3fc8-ae11-b7eff1426b6f | -7.89925 | -55.42044 | 2025-07-05 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 773442ea-b8dd-3d8e-99b1-2c240a3f5217 | -12.57842 | -56.97517 | 2025-07-05 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0791fec4-85c4-3072-ae45-750c6dee447b | -11.88002 | -58.73358 | 2025-07-05 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4466a4e7-b03c-34d8-b38e-3a44629c8b2b | -11.4546 | -45.112 | 2025-07-05 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bd8efa54-c7fc-342c-845b-8723149d5dc8 | -10.05573 | -59.36027 | 2025-07-05 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17687346-e8d8-3df0-b444-8c5b3cadcb94 | -11.05026 | -56.74256 | 2025-07-05 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0ec0551-eac5-30fc-96e9-bed9902d7908 | -7.90274 | -55.42098 | 2025-07-05 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4c21847-5db6-3b40-95ec-a32a9da0e709 | -9.70417 | -56.185 | 2025-07-05 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README13.md)
