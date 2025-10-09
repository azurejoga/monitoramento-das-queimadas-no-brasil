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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a35f66d-bb59-39cc-9cdd-4c51e01a9905 | -11.76166 | -45.14785 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 970da88b-1b28-3d74-b565-bce31efda232 | -13.76686 | -45.80712 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e7ed909-a0bb-3141-8f25-e65d983d05cb | -8.2011 | -43.34836 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| cf3f509d-f921-3bbd-9127-1d9cf6df647d | -14.40301 | -46.01638 | 2025-10-09 04:19:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 419901b8-e8bf-3ceb-bc29-4cf20cad6d48 | -7.75274 | -44.03184 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16bad565-bb1e-3c00-87fb-c8b6d8357f6e | -7.80453 | -44.20139 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c878a5a-7aba-31e7-b1a5-84f2131df334 | -7.66763 | -43.96771 | 2025-10-09 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7b8c43a-faa7-3d2c-9100-2a4cdf9ef1d2 | -10.35264 | -50.2162 | 2025-10-09 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b175900-d8c8-3085-9611-80f1a64abc77 | -7.77492 | -44.04253 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff73be3d-4fd8-349f-962b-e9d6600fd288 | -8.37515 | -47.75839 | 2025-10-09 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71c45edd-db49-37d1-8ee0-11cf062da794 | -11.87353 | -44.9288 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1e495ed-9484-3416-bff5-daea8db08dd5 | -14.38757 | -46.00652 | 2025-10-09 04:19:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e60133e-8a1a-3d60-8eb1-be580edcb1b5 | -12.2447 | -43.77753 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ef2f120-1d94-3ead-9c23-d260c880ed31 | -7.76129 | -42.38403 | 2025-10-09 04:19:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f6bd071b-619c-30f9-b005-6905744ac0f6 | -11.87555 | -45.50513 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5f1f012-7c07-3f1f-bcae-880bf0f100ea | -10.0314 | -42.31392 | 2025-10-09 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| ff152a43-284c-3a9b-ac48-ccf98e68f59d | -7.43205 | -44.56317 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1b9fb57-1ae2-337a-8567-1ea2f0f3230b | -7.6775 | -47.4161 | 2025-10-09 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 455ec11d-02c7-31a5-b62a-71df45d321d3 | -0.90215 | -47.54949 | 2025-10-09 04:19:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b7784983-bbd7-3727-8d11-9ec434a5a5b6 | -2.70393 | -48.33594 | 2025-10-09 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b4fe8f6-582e-373e-a575-7ae241837754 | -10.862 | -44.62368 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5a244af2-3215-3cca-90fa-b53cfcee6bd4 | -2.37894 | -47.71592 | 2025-10-09 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb9679c2-baba-3c3d-9775-2b6406c54534 | -8.09393 | -44.82408 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f67594f-b347-3df2-8a9f-89f09cfaeb57 | -12.26568 | -47.89325 | 2025-10-09 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bfcc3a93-70dc-3b81-9206-27727fd718d6 | -8.51952 | -46.18432 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f07762b-c896-33d1-b1f6-ece0f15f7431 | -8.63415 | -45.14498 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 510e2f20-fbc8-3270-890e-f7c76a89071f | -7.76162 | -44.04041 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4af12cd9-23d2-3ec1-a909-bbeaeef06a28 | -3.8588 | -41.53448 | 2025-10-09 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3cb14289-701f-3048-8799-05bfe09bfb3b | -3.36235 | -43.37691 | 2025-10-09 04:19:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8021c2a7-663b-368e-81b8-430fb4da7459 | -14.39419 | -46.00761 | 2025-10-09 04:19:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fb9de20-65d8-3f37-87e3-1310225a0e41 | -8.15431 | -43.33039 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 944a4215-1c75-39d7-b333-81131e906968 | -11.67043 | -43.89941 | 2025-10-09 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d6e5c71-e165-3c07-ac86-b8d4dada8bbe | -8.67122 | -43.91079 | 2025-10-09 04:19:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4af85ad-2f99-3eec-86d2-bfbd8f91c30e | -8.1768 | -43.32591 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 18621f86-4d29-381b-8353-3e97f3d70928 | -8.19262 | -43.33583 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 1c5e487e-513e-3e3a-898b-20665bc95c32 | -11.31699 | -44.88451 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94ea9a92-56ec-3c56-99ea-42375754aa0a | -13.78946 | -45.87992 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0200b45-6763-30c0-bc94-8677d3f4d5e5 | -13.70631 | -44.64013 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a4b5643-7853-3eb3-9df5-c66c128ae663 | -13.14034 | -50.00136 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3105fa96-b6bc-3d7e-b711-9653b2167750 | -8.53618 | -46.20898 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a33c7c8-8fe6-360b-978e-d7b87ee91530 | -8.62864 | -45.13699 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1153285f-695b-3280-8de6-f296d0f59076 | -7.86719 | -44.12517 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd5b6181-8c7a-3477-83f8-45b9f1a69c60 | -11.78157 | -45.15104 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b2b0f22-77c9-3687-9e62-2df5827059e6 | -7.71182 | -42.38052 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd511ce0-3394-37e0-9252-e56050d55016 | -14.69474 | -46.08237 | 2025-10-09 04:19:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c5e5769-cfaf-389d-b71b-ac34b4ca77f6 | -9.19257 | -47.85786 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c8d1184-a840-3ad7-a69d-1c6b89cc5016 | -7.81249 | -46.71624 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e6227a4-6a7a-321b-8d6c-8cfd9e06d1ae | -12.25447 | -47.87585 | 2025-10-09 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8b542aef-e2c2-32f0-9087-e1183f9b628d | -2.38349 | -47.71191 | 2025-10-09 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6dd67b60-13f6-3151-a78d-6415f52dd461 | -15.05629 | -42.33027 | 2025-10-09 04:19:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 14250546-ea01-394c-a337-d97defd3c4c2 | -11.13961 | -47.74374 | 2025-10-09 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98a41633-cd15-3f7f-bb5e-8f3a01645555 | -11.13617 | -47.74318 | 2025-10-09 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 587b2a58-b415-365b-b51b-9a478ef15032 | -3.59381 | -41.61312 | 2025-10-09 04:19:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3a15bf84-b128-3c47-9c76-48d91caab92f | -13.77624 | -45.83413 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b48f54a2-4521-33ef-b6b7-7d0999bc6fea | -13.13128 | -43.9082 | 2025-10-09 04:19:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e3e0f3b3-c6ca-36ed-80a1-d4d00ec109ee | -7.90938 | -43.17301 | 2025-10-09 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b64d0f46-7c51-3bc1-880c-3aa8f5be4e35 | -10.3478 | -50.22063 | 2025-10-09 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6dcb785-2dfd-3698-8fd4-677b4bfd87df | -13.79777 | -45.82671 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92a7c830-7c74-323c-89d4-f038702faf6d | -11.86839 | -45.52917 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04f8e5f5-4cca-34f9-aa2a-2e314bed77f3 | -7.25122 | -47.80105 | 2025-10-09 04:19:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d905fc63-61be-3a1e-8b25-72b6892f0647 | -7.55175 | -44.29754 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2d1a3a8-3234-3632-b1f3-11796e16e255 | -7.79906 | -42.61381 | 2025-10-09 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a38a0a58-2174-32c3-b541-09b275730db4 | -7.78083 | -44.24416 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec1df1d4-c8ff-37ac-aa15-7b0893504f45 | -10.73683 | -50.06691 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 43da1fd8-6583-388a-831b-46ab0bc9c439 | -8.73522 | -41.66423 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 69176152-1280-3849-a45f-77195dba9f59 | -3.56543 | -43.51091 | 2025-10-09 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e2a8b69-b112-3e31-87a7-43f9f599bcce | -14.4138 | -43.98157 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e1c1774-6876-3cf5-9f32-f321b04d2a72 | -9.61443 | -40.32935 | 2025-10-09 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 344d7979-592a-3b97-840f-8f01f3b46c00 | -13.00118 | -44.05327 | 2025-10-09 04:19:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 626269ed-f7da-3635-bb13-434344650fcf | -7.76274 | -42.38377 | 2025-10-09 04:19:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 38ab6c06-71ca-3a7e-8c35-78c0e08266de | -7.67155 | -42.57521 | 2025-10-09 04:19:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a0c74e48-cde2-38b8-9840-ea447ead8a9c | -10.52657 | -50.02498 | 2025-10-09 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9640bbdf-75f3-3780-860c-bb7874806d9e | -13.61463 | -44.43909 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a12e45d-1d83-32ce-b4ee-b63feeb0ec19 | -14.25686 | -45.86536 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a0a8d1a-6b65-344e-b9c2-bf6221faa56a | -3.47613 | -43.94814 | 2025-10-09 04:19:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac37697c-3e23-393c-baec-0601fa3647f8 | -7.73735 | -42.40035 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 111abea6-0931-37ec-bdb6-35d989123e0b | -7.32855 | -44.7877 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c2fed54-ad4f-36f7-8120-4d573abc5eff | -7.54457 | -44.29998 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f3fe7a5-a36b-34a1-adc2-df27244e5274 | -7.73208 | -42.41147 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1e559f40-a801-3d0e-aae1-8e6351ef2f01 | -1.96316 | -47.30962 | 2025-10-09 04:19:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8f6a6200-4e9a-3516-b6c5-11fa1f1d4331 | -7.31651 | -44.86387 | 2025-10-09 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7e5d2f3-fee0-3f04-814f-3b076093dc7d | -13.79666 | -45.83381 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 415fdbf9-1514-3ca9-a62c-89fcedc83126 | -7.78477 | -48.04146 | 2025-10-09 04:19:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4377e393-f36e-3908-b92b-3e6c7c1f169f | -8.19488 | -43.34368 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 89cf7ac3-642d-3327-acf8-0c2a04cc0248 | -7.75606 | -44.03236 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| df759971-4b93-3837-959c-8ae95c2a5306 | -7.67097 | -42.57906 | 2025-10-09 04:19:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9bab7272-98e0-351e-9e74-b3b373cdf4d0 | -11.87004 | -45.51864 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7898a282-5fc1-3b48-90b7-488e7df11517 | -14.2563 | -45.86892 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c769a45-7cb0-3437-aa1a-9efb54982e6a | -10.84697 | -49.94157 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2b7415c-354b-3f9f-bf61-667f6eff32f2 | -10.82255 | -42.81956 | 2025-10-09 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09dc711a-1fee-330f-8973-69e71136678a | -7.68041 | -42.39944 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 256ca592-a433-3327-baca-ddc1d55ea71d | -10.85083 | -49.94225 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 712bc9f4-1589-3591-acea-36ea341e7cdf | -8.78108 | -48.00071 | 2025-10-09 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d48d390-fdab-31d3-a599-9758ffbae282 | -11.66528 | -44.25447 | 2025-10-09 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7903949-15b1-36c2-8f7b-a4d49f36662c | -7.56113 | -44.3026 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d094a6c4-1a56-3c3a-8de6-db7f6c88626a | -7.43259 | -44.55971 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5789ee1f-b8b6-3ec2-991a-dd3a95445bdf | -7.70378 | -44.66988 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8550221-cc3d-3131-bd13-47128781a72e | -9.183 | -47.84983 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83b22839-09fb-350c-9f22-a40d2632c571 | -8.43491 | -47.63704 | 2025-10-09 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eba9f4da-827c-3013-94fc-10e33210027a | -10.72921 | -44.55979 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README38.md)
