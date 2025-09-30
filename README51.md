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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd20ae3d-894b-3d15-9916-51dbbd4a4e1c | -5.73177 | -43.97065 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c480b93f-9585-3fe5-9854-d9e24a9df7cb | -6.15413 | -43.89758 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c08f8685-4aab-3946-8a9b-27ecc7580586 | -5.4983 | -42.74094 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5126eb6f-6ffd-3e82-a830-a9c1b7f5f571 | -6.94923 | -45.39375 | 2025-09-30 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 410d0ddd-0fb8-32cc-a033-339b261992a6 | -2.74012 | -48.67349 | 2025-09-30 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4d66355-d1de-396a-855f-58568e1d638f | -2.58146 | -48.40328 | 2025-09-30 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8af5280c-cf5d-31f9-ba09-b03623f69564 | -2.07641 | -56.87269 | 2025-09-30 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43ddf597-c68c-3905-a86a-9c0fc92c10ee | -6.41237 | -43.75682 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9cfe76b-158d-3c60-b370-001414ed26e0 | -4.48109 | -47.67461 | 2025-09-30 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebd0e31a-768b-341c-bc10-2a3652093108 | -5.09252 | -47.48344 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1540044c-a5d0-3b62-a12d-be8730846a84 | -7.17432 | -41.70663 | 2025-09-30 04:38:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01eaa2f5-bfbb-38dd-ba6a-1a27bbf59565 | -5.74321 | -42.68441 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3c0a9492-5f69-3655-a0f8-7586992b89bd | -3.10834 | -47.01193 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e4f87b0e-fd0c-3a02-b15b-6291272eafd8 | -5.24086 | -43.74465 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6141bef8-38c1-35d9-bd3d-bf6cf7535c50 | -4.15407 | -46.78431 | 2025-09-30 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37102877-263f-308f-981a-6ba34f2bacb4 | -6.52774 | -43.82448 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2947249b-b0d5-3ced-a268-c55a5c5b9884 | -1.28887 | -54.1844 | 2025-09-30 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 561d64c4-865c-3be2-be66-2c1b5a3542ff | -6.25363 | -43.6576 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 063f5fb4-ec72-33fb-b65a-543c81882768 | -3.08313 | -47.76303 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99f8f847-d2ac-3239-bff4-23ea8f29861a | -5.35394 | -45.96774 | 2025-09-30 04:38:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a774d9a-648d-3512-9ff3-132309c756ff | -3.50479 | -52.46983 | 2025-09-30 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e4dde2e-9bbb-3881-a164-e0cdc39cee01 | -4.96214 | -47.60131 | 2025-09-30 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 693fd135-801d-3e99-b982-662dc6bb866b | -6.25838 | -43.65466 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 045c860e-e4e5-37f2-908a-53e35359ba13 | -5.33016 | -43.72992 | 2025-09-30 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42e3acc8-dab6-335b-aecc-b9698cd8de67 | -5.7131 | -42.87262 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 14a04816-7e4e-321a-b192-b17b8d271781 | -6.10661 | -42.66388 | 2025-09-30 04:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0cc5007d-38d8-3137-80cd-bd0283862d8c | -5.66555 | -45.29846 | 2025-09-30 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7bad61aa-b7cc-373d-a270-4c220d6a6e4a | -4.64365 | -50.6764 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f828c24a-99ab-3eb4-a71b-b2266a56dad5 | -6.7366 | -45.62748 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f6a9a3a-072a-3500-9279-a1db5b36105c | -1.29431 | -54.17756 | 2025-09-30 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a0f28ea-85e6-3895-a19c-c704ae920b7a | -5.16835 | -43.71805 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ede847a-bd27-3c65-96e7-6209ea828d5f | -6.14608 | -44.7209 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ca25073-2094-3544-990c-fd2658605a92 | -5.51436 | -42.72495 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7c9e921c-7639-31b6-a3df-bc5d992d7884 | -5.58032 | -48.96928 | 2025-09-30 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05823232-3da4-33fc-a923-319697a5d079 | -6.30662 | -43.43786 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30ecca4b-ad06-38c8-9c5d-5fe0b1648681 | -6.76608 | -44.58758 | 2025-09-30 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63b87c3c-cd20-3f55-b384-9daef311a0b6 | -6.49578 | -44.2662 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a488a70b-d4a6-3360-a76b-d06bcb470351 | -5.52079 | -43.87632 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| c05a453c-3a40-3572-acce-805fb5eeaf40 | -5.37471 | -42.84529 | 2025-09-30 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b4b48f37-66c6-3afb-96ae-e828a2d6df00 | -6.50568 | -45.22231 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ddbf29ad-b63e-30e8-ba9e-f429c180df0c | -6.55285 | -47.27343 | 2025-09-30 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 898d8db5-924b-353d-bb91-21bd68f124d6 | -3.89074 | -52.07953 | 2025-09-30 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 500331f7-159a-338d-99ba-8e819dd13de5 | -6.50639 | -45.21749 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ad24af76-b924-3891-96ff-380e90e84a8b | -5.91376 | -43.70275 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95b5a3f8-ed72-37b5-8eba-5f6273f089cd | -7.36195 | -42.12599 | 2025-09-30 04:38:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a426090b-456b-3987-b348-dce6285a0ec0 | -4.67323 | -45.69199 | 2025-09-30 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 126ef568-aeac-3402-95ec-cafe6ded5d5b | -2.73802 | -48.55745 | 2025-09-30 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0a413dce-ce75-33a7-8f65-5d0ddb5fb9a9 | -6.88787 | -44.52163 | 2025-09-30 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43355722-7149-34d6-8910-c39b111b9a27 | -5.74786 | -42.66953 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7bff02f4-908e-3bf2-a16c-c8d8f4485292 | -4.74928 | -43.71166 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a95dfce-9d0f-3b79-a2b3-518616d02acc | -5.60965 | -45.8134 | 2025-09-30 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0eb36722-5471-3813-a5e5-354750cb744f | -4.90151 | -43.46908 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 80a69199-c445-3998-95a3-a3538407fa3a | -5.7736 | -43.83134 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e591d68-dac5-3a65-8ee1-7552fd099783 | -5.50208 | -42.74621 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b08e1586-e8eb-3f4f-9416-4fbe187ae8b6 | -7.29659 | -42.86584 | 2025-09-30 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d8f10f1d-b2fb-312c-a876-1ff081ccd8f5 | -5.7092 | -42.68232 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f9316b3-9805-3966-ac2e-e9d162d973dd | -6.81965 | -44.47248 | 2025-09-30 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3a7f728-f98c-3fd0-90fb-ccaa75891d31 | -6.68817 | -42.80007 | 2025-09-30 04:38:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c3776aea-d9fa-398b-943d-0175329334b3 | -7.01674 | -44.46284 | 2025-09-30 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48a1a259-d4f8-379e-a822-f18058a4f2a0 | -4.97598 | -45.29748 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2851a58-7109-340b-b7a9-28b7b20e39cb | -5.32705 | -45.23094 | 2025-09-30 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1342d516-3e79-3d75-be54-d1feab5f9b9a | -6.47098 | -44.00815 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c9b8a12-1350-38f9-ab61-adb1eaa2a729 | -4.07457 | -48.03835 | 2025-09-30 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d1190ac-5c0c-3ed8-b813-154c90c5d0d1 | -6.51791 | -45.21932 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 739cc240-6ac1-399e-a76c-261d0e1cb3db | -6.56511 | -43.41881 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 9.9 |
| d2c617cb-a8a1-3642-8f9e-6451708b3509 | -4.39642 | -44.3945 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e092a21f-2ec2-3aa7-b60b-5af21f39f59c | -6.42962 | -43.0803 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e46d1e12-73e5-386b-9d94-06fd9430f390 | -0.39683 | -51.77941 | 2025-09-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3578d6e-2ad6-3e5c-87d8-cfa120317610 | -6.20848 | -44.20984 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b6a803b-32df-3048-8edf-76daeff8fef3 | -6.88836 | -44.51814 | 2025-09-30 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7e2b514-4ee6-373a-aee5-57604ef133e8 | -5.81783 | -42.8638 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f2045d8b-852b-3e87-a135-a2d7952d7bf6 | -5.04328 | -42.89445 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d72ff2e1-224b-35b0-a964-67f205993947 | -6.86461 | -45.6246 | 2025-09-30 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68b063f8-9b66-3f37-a270-e70f44c5a3dc | -5.72674 | -45.51047 | 2025-09-30 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1654d25-d4f5-3df4-b994-ea4564c312b7 | -4.29063 | -48.26844 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 716d9985-c3fc-3f98-8829-de9a9aac12ba | -4.39957 | -44.07794 | 2025-09-30 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3b4ce7b1-71f9-331f-94ba-315a0d132902 | -5.87451 | -47.02534 | 2025-09-30 04:38:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0e20356-3431-3d27-b987-51887e36cab1 | -7.01477 | -44.47665 | 2025-09-30 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1f1ca24-16d5-3ddb-828c-4de46dde4be3 | -6.65868 | -41.39448 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f6df2291-70fe-3a25-83a1-1758541a268c | -5.97933 | -42.56518 | 2025-09-30 04:38:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3edebde9-69f6-3145-be91-1d20404beeb0 | -6.05371 | -43.60453 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 820fb1aa-9e12-34c5-96ba-bf7f66c65953 | -5.04747 | -45.31499 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fe1d1e45-ed4f-325d-9a04-ec78d8aeffd8 | -6.47044 | -44.01186 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d31c3da9-8232-3b81-b84d-a43dbdb9de52 | -7.02411 | -44.7807 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38b46a90-e882-310f-b0a1-5a97f6d4cfac | -6.50445 | -44.26398 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e248e76-4e73-39d2-a57b-35275f1e9c94 | -5.90835 | -43.71629 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c33b3fd-6713-36ce-8f32-7f2ed3b001da | -4.29449 | -48.26547 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a1339d2-a1d0-3346-becd-286beaabae51 | -4.06958 | -49.50965 | 2025-09-30 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a8c8542-d94f-3c29-807e-83b374282827 | -5.75483 | -42.66716 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a76459b7-9604-3058-b23e-a81aaf327110 | -6.70661 | -44.56343 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 74f99c6e-2be7-3d49-a9b7-3741c865c143 | -2.44258 | -47.32907 | 2025-09-30 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a593337-9bf5-36c0-9fa3-f059cf43bbf4 | -3.84667 | -52.28264 | 2025-09-30 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d87e84c0-dee2-317e-84d9-353cbfb0c0a0 | -5.31432 | -44.78639 | 2025-09-30 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d604dab-a9ac-3110-b56f-6c982d9d3426 | -5.27059 | -42.87902 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0c64b20a-a364-3044-befc-7a6b7566032b | -5.37802 | -48.91312 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f60c4b5-c465-3d6b-865e-6c3b748de55c | -3.09421 | -47.01347 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e932f2c1-bfd1-3cf5-a8d2-64b1ed48726e | -3.85764 | -48.97262 | 2025-09-30 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2d7df43b-b7e2-3fdd-98a9-75888dbf39fe | -1.95279 | -48.11499 | 2025-09-30 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2756910-51c4-3b19-901a-9a1a033d1816 | -6.86838 | -45.62518 | 2025-09-30 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11356a73-4408-320e-b663-e87f35eaea64 | -4.30426 | -48.07077 | 2025-09-30 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README52.md)
