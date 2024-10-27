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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2798a8fc-2d64-3b26-8968-5cd1318a9d3b | -2.8329 | -49.2626 | 2024-10-27 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b30f2399-3034-3b6c-bf20-f58737c0765d | -2.833 | -49.2413 | 2024-10-27 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 6a9acd58-d461-36f7-a3a4-3fce6620c2da | -2.8501 | -45.0131 | 2024-10-27 00:45:21 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 9f2b4acb-ea0a-33af-bacf-4d57c6124625 | -2.8502 | -44.9905 | 2024-10-27 00:45:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 1b603a48-8447-37b8-843b-55a691340138 | -2.8422 | -51.8148 | 2024-10-27 00:45:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 91e09aa7-9814-31e8-b455-38762f21045e | -2.8687 | -45.0125 | 2024-10-27 00:45:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 183.5 |
| 5b076b9c-c065-3954-8d7f-a674f38341bf | -2.8688 | -44.9899 | 2024-10-27 00:45:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 231.8 |
| 1724666a-b46d-3104-9fa7-ef58d3fa1fb6 | -2.916 | -51.7716 | 2024-10-27 00:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 75a740d8-3326-35c6-84d5-0e07488605c6 | -2.9161 | -51.751 | 2024-10-27 00:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| c1816b31-1838-3784-b789-37a89bf4bd5b | -2.9214 | -50.295 | 2024-10-27 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c99bfda3-e138-3d00-b54d-b53dc1c5f586 | -2.9215 | -50.274 | 2024-10-27 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 11f1b823-0bb4-3f7d-8ad3-ecc5c9721675 | -2.9345 | -51.7711 | 2024-10-27 00:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| befdcbae-3ee6-325b-8396-039351dc2a91 | -2.9345 | -51.7505 | 2024-10-27 00:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| f428750e-6c7e-3995-8e80-08c1b01776ea | -2.9399 | -50.2735 | 2024-10-27 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4e601a58-f300-3112-b2c6-1a5892b25887 | -2.9669 | -53.0389 | 2024-10-27 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0784dfb3-ff52-3b00-a906-193ebcb8f69e | -3.0888 | -45.6568 | 2024-10-27 00:45:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 92.8 |
| b9244fee-15af-3aec-a6b0-9ac1c9ad9759 | -3.0889 | -45.6344 | 2024-10-27 00:45:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| cac9a299-f5e0-3e7a-b1a6-432a453e8f21 | -3.1106 | -44.9809 | 2024-10-27 00:45:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| ecdae787-7e8b-3ffc-b7fd-c2f1ac7d11d7 | -3.1292 | -44.9801 | 2024-10-27 00:45:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 426ac5f3-f454-3656-8326-3a2e3cf0b535 | -3.1242 | -50.3519 | 2024-10-27 00:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 3bc56aa8-6f1e-36cc-a06a-ac80c372e588 | -3.3256 | -50.7641 | 2024-10-27 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 98126a40-d2b1-37cd-9be8-4b8decc27c30 | -3.344 | -50.7635 | 2024-10-27 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d3706b52-ff08-3717-ac96-7594cb338535 | -3.3441 | -50.7426 | 2024-10-27 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 44e7d9cc-04fe-3f07-8f08-00e53c6ab901 | -3.4392 | -50.0896 | 2024-10-27 00:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 97b620bf-dccb-3896-a875-2092083bbe28 | -3.4762 | -54.5772 | 2024-10-27 00:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 82bc0726-e66f-3aa7-ac11-968b75616de7 | -3.4763 | -54.5572 | 2024-10-27 00:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 470e6eaa-49b1-3681-95fc-e1a2d944bc30 | -3.5202 | -52.7384 | 2024-10-27 00:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| a40c696c-4843-367c-8a59-6b05b303879b | -3.5626 | -51.4217 | 2024-10-27 00:45:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| d491fe73-65c4-3619-81f6-64a71af11ccf | -3.6798 | -54.2107 | 2024-10-27 00:45:26 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 86d94822-30e7-3ff2-8627-f9a89f082e6e | -3.7748 | -49.4856 | 2024-10-27 00:45:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8efc2325-b1b7-33d8-b1e8-8318e0c75323 | -3.8149 | -48.8874 | 2024-10-27 00:45:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 083b17d3-e394-38da-b23b-0a2e3cecdb35 | -4.254 | -63.153 | 2024-10-27 00:45:30 | GOES-16 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 3052bb61-f668-3f9c-9553-95944e0d9c7b | -4.3841 | -49.7571 | 2024-10-27 00:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| e919bafc-628c-3930-a9c3-900b8f7d18ed | -7.2264 | -46.0498 | 2024-10-27 00:45:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e3b1b53a-6787-397d-924e-8ce2d1319b5f | -7.2452 | -46.0482 | 2024-10-27 00:45:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| d0dd5cc6-2afc-3f6a-9a63-42c71249cc24 | -10.5424 | -45.1463 | 2024-10-27 00:46:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| aef820df-6738-34c5-8cac-dd643b719937 | -0.9815 | -53.7192 | 2024-10-27 00:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| d4bed873-106b-3425-b0d6-1b9e82aac5be | -0.9815 | -53.699 | 2024-10-27 00:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 213.7 |
| 465b2c60-5660-325d-a1f3-a04be6ae664f | -0.9815 | -53.6789 | 2024-10-27 00:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| de3f1781-4285-3753-a564-f89f0265ff39 | -0.9998 | -53.719 | 2024-10-27 00:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b775e935-ac7f-3267-bb64-1cf9598176fa | -0.9998 | -53.6989 | 2024-10-27 00:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 37e59c32-677c-3e00-bfa1-7ad609f6c452 | -0.9999 | -53.6788 | 2024-10-27 00:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 8077b4a6-71b2-32d4-adfc-50c4253b9fdf | -1.7874 | -46.4065 | 2024-10-27 00:55:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| a0adc8d7-0116-3742-97ea-197aa30892a1 | -1.7875 | -46.3844 | 2024-10-27 00:55:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 4deb8c26-0c8d-304c-aaaa-d65d0dc29918 | -1.8188 | -48.6256 | 2024-10-27 00:55:15 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4e0e8828-f98d-342e-8f18-950d51fccfb0 | -1.906 | -59.9839 | 2024-10-27 00:55:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 2f9a3f4e-c1ba-3069-a500-77086f76c6b5 | -1.9243 | -59.9837 | 2024-10-27 00:55:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| cb39701e-1c10-3c75-b197-aa454f02c463 | -2.4567 | -45.8567 | 2024-10-27 00:55:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ca93b930-e3b9-3ddd-87a4-6b6f415d29d0 | -2.4568 | -45.8344 | 2024-10-27 00:55:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6c61b7d7-54b6-3c05-973b-54e2c13e22e9 | -2.4598 | -50.412 | 2024-10-27 00:55:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f475b04d-47c7-33db-bef4-2df35ae92735 | -2.4753 | -45.8561 | 2024-10-27 00:55:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 176.6 |
| 932b58a0-fcce-3e94-8e4c-7797bb67887d | -2.4753 | -45.8338 | 2024-10-27 00:55:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 197.9 |
| b18eea7b-44a5-309f-805e-0fe5dabb8307 | -2.4786 | -50.2858 | 2024-10-27 00:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3dc7bda7-62dc-3318-8856-ed98fd754b1e | -2.486 | -48.0507 | 2024-10-27 00:55:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 4cf39007-fe0b-3e2d-860b-3d696ed963bf | -2.5045 | -48.0502 | 2024-10-27 00:55:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 2c99edb7-9dca-358b-ab7c-2eb14ef8c4dc | -2.6297 | -49.247 | 2024-10-27 00:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b0a0c25e-832b-3f8b-a8a5-02f19ca6d214 | -2.6321 | -54.2975 | 2024-10-27 00:55:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 80142687-c5a0-3091-98ea-25b856b738b0 | -2.6482 | -49.2465 | 2024-10-27 00:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 178b8ae5-decc-38b5-bc1f-8232c35403b4 | -2.6505 | -54.2971 | 2024-10-27 00:55:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 03599f47-a592-37a5-95ab-205a2737c568 | -2.7033 | -49.33 | 2024-10-27 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| d982c2cc-926a-32f2-8619-27c9098a4e1c | -2.7034 | -49.3088 | 2024-10-27 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| ebbe7f7f-d7b5-3118-8f2f-be9b150e3efe | -2.8145 | -49.2418 | 2024-10-27 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d8202d3c-e7e5-34ba-9691-8d0b280c08b1 | -2.8329 | -49.2626 | 2024-10-27 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 20c905f3-37ae-36b9-8648-c71c46c4d7e5 | -2.833 | -49.2413 | 2024-10-27 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 822e9195-1f72-3b86-b7ef-fabb0706e2a4 | -2.8501 | -45.0131 | 2024-10-27 00:55:21 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 5108c97b-118a-3002-ab1e-c8836c89af94 | -2.8502 | -44.9905 | 2024-10-27 00:55:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| dcd10ebf-7f97-32f8-84da-dde4c3483a59 | -2.8422 | -51.8148 | 2024-10-27 00:55:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a93ba217-55ab-3280-a788-edf3a3f7ba15 | -2.8515 | -49.2408 | 2024-10-27 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f987bfd3-e731-3394-b8c0-d7b738b14aea | -2.8687 | -45.0125 | 2024-10-27 00:55:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 28be0c89-5998-30bc-b882-15edd3279638 | -2.8688 | -44.9899 | 2024-10-27 00:55:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 88951b22-e9a8-36ed-be22-8ea1563048b9 | -2.916 | -51.7716 | 2024-10-27 00:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 55af2839-9a0c-3a8b-9e9c-a1aefb953924 | -2.9161 | -51.751 | 2024-10-27 00:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 0c6ce932-013d-32d1-9a7d-20d93133213f | -2.9214 | -50.295 | 2024-10-27 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b3cb483d-d07c-3b91-9a85-6590f667b954 | -2.9215 | -50.274 | 2024-10-27 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 1a049256-fb7d-3701-b079-5cd917e19970 | -2.9345 | -51.7711 | 2024-10-27 00:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 21747e6e-45a1-3469-bfee-3ebee460c140 | -2.9345 | -51.7505 | 2024-10-27 00:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| dee118d5-08f0-3465-9055-f853276734d3 | -2.9399 | -50.2735 | 2024-10-27 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 1f0fd762-9a88-3e80-9175-5245d8063360 | -2.9669 | -53.0389 | 2024-10-27 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 606726b2-fa04-365b-9a4e-2044d89ea64e | -3.0888 | -45.6568 | 2024-10-27 00:55:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3ea8ae45-a23c-3c65-9163-84ebf3f52260 | -3.1106 | -44.9809 | 2024-10-27 00:55:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 127.0 |
| adca0cb1-5dfd-31c8-b73c-dc5289c06c15 | -3.1292 | -44.9801 | 2024-10-27 00:55:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 280560d3-5c4e-32b1-95a2-e28a0fae13ef | -3.1242 | -50.3519 | 2024-10-27 00:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 71580971-156c-315b-b811-76a19c585e49 | -3.3256 | -50.7641 | 2024-10-27 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e2de3ce8-d081-35d9-877c-43715c2293d9 | -3.344 | -50.7635 | 2024-10-27 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 21770ad3-3f25-3ec7-9a6d-d2e404c1bfc3 | -3.3441 | -50.7426 | 2024-10-27 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| bbbec5ed-2641-378f-8cd9-a971c6625137 | -3.4392 | -50.0896 | 2024-10-27 00:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 30089e84-3513-386a-9d8e-b747d447dba4 | -3.4762 | -54.5772 | 2024-10-27 00:55:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| be96caa2-0ae5-3a6c-8a67-bdd067c78ae5 | -3.5202 | -52.7384 | 2024-10-27 00:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f7305f82-6bde-3a73-9527-aa2d583ef059 | -3.5626 | -51.4217 | 2024-10-27 00:55:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 95639e57-c458-320b-a766-0c43b1b6868e | -3.6615 | -54.2113 | 2024-10-27 00:55:26 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 8f2b35ae-8c4a-3d23-aa35-bbc54d381d0f | -3.6798 | -54.2107 | 2024-10-27 00:55:26 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 9da17379-7505-358c-98d4-928c34655d5b | -4.2799 | -45.5138 | 2024-10-27 00:55:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 32efd828-7c5b-3bad-ad0d-75c7a5e72de2 | -6.1674 | -47.2638 | 2024-10-27 00:55:40 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d97adf7f-7246-3a38-85b4-a91efb1812c4 | -6.8534 | -45.8794 | 2024-10-27 00:55:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 062981bb-0d1e-35be-baa9-879aede53e6b | -6.8719 | -45.9003 | 2024-10-27 00:55:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d42d2ab9-bddd-3aeb-878a-6fbb8ad00cc5 | -6.8722 | -45.8779 | 2024-10-27 00:55:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 9a0994c6-91cf-37f0-96d3-2d768907a157 | -7.2264 | -46.0498 | 2024-10-27 00:55:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 274e9145-51a9-3c14-8afd-1016250dd696 | -7.2452 | -46.0482 | 2024-10-27 00:55:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b16a5526-2b39-3192-b1a8-cda12f75f0f2 | -10.5424 | -45.1463 | 2024-10-27 00:56:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 613d74eb-1946-3f1f-a388-0d10c6a0145a | -13.3803 | -45.1149 | 2024-10-27 00:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |


[Clique aqui para ver as próximas entradas](README15.md)
