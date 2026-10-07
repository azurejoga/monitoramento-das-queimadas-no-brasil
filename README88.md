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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83f1b65d-9e2d-330e-818a-af2eacecb5fd | -3.28279 | -54.04443 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e501f5e7-6afd-3b8b-b870-f0e0ed232c2b | -4.45589 | -54.96624 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f86e228f-496c-3967-9306-bc08bb58749c | -6.15245 | -51.74136 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84f661aa-2904-3e8a-ab76-97fa739d6502 | -3.58764 | -58.53442 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f588739-b16e-3e1b-ad1a-800d9da2fb59 | -2.76841 | -54.09097 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ecf95b6a-484c-32d1-b74f-e42a26af525b | -1.09654 | -54.12046 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa6f1574-ff2c-374e-bf4f-5202b6efd8fc | -5.68147 | -53.48534 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a185bc59-c539-3dbd-b326-c6d4b86122cd | -2.9101 | -54.09887 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c95d5b4-ae4d-3220-8d1a-d55595963398 | -3.54035 | -54.64259 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a513820-e017-31be-bc09-616cef2ae54c | -3.88936 | -55.82723 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a8c2543-1706-3c7c-a85c-2527d5c275a0 | -0.42543 | -52.06125 | 2026-10-07 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8078402b-df03-30b8-a6d5-ebd795ff4b35 | -3.43118 | -49.25019 | 2026-10-07 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32c095bb-3363-35a3-a420-ef1abef73985 | -3.4804 | -50.08928 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 97f431f4-4602-323d-bb7a-83a2ad5989e7 | -3.66101 | -60.61945 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5be4cb3-8bc9-34c9-a41a-03103922e212 | -3.02045 | -54.13362 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fcc31058-dffc-3ea2-b976-d1ecfeb98f33 | -6.88008 | -43.69018 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 57dd6a57-b5fa-3da1-8bda-cfbeb24421a2 | -2.93693 | -54.16764 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ff1fee6-ca43-3211-b6bf-c6df3649ccdc | -3.06605 | -54.25539 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5af6cb9d-e779-39f9-abbb-979b69cda36d | -2.99068 | -54.03898 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f87e6aff-2ef2-3735-86fc-5aacf0e7a0d6 | -2.9336 | -54.16713 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67efa72c-c470-3bc1-99ba-9231a99dc136 | -3.92008 | -53.46755 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 100ba100-bbce-3ef7-ac55-cafdec467886 | -3.10898 | -53.76254 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd972f1a-d2a8-3f50-b536-35825fa42350 | -2.04933 | -56.88543 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f47794b4-8aa5-3c98-8ed5-b1137d454ab7 | -4.26613 | -54.87611 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e25e8e05-bcb8-3039-8f22-f38ea5884cc1 | -3.72825 | -54.65736 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f43fdc7d-daa0-3f8b-8b43-dc9b131c84bb | -2.10714 | -52.06436 | 2026-10-07 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f0e07df-e3e9-325e-9205-459cb4cdfd43 | -4.1561 | -54.02852 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ee475c3-42e6-3a22-9a03-d2631137f741 | -3.85245 | -55.97678 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 3e2c72bc-b1e2-3fca-8126-d873a6a08305 | -6.40458 | -52.7204 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1809cc5d-d544-3694-82a0-4ab36f6752eb | -3.50957 | -54.64153 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59318384-0f0f-386b-80e5-77b889b1d285 | -1.29758 | -54.55687 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ba6fb22-dfb8-3726-96e9-ec10ba310622 | -2.9842 | -50.48747 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e20acb91-5053-3dcc-8d66-4dd1b9716857 | -2.91234 | -54.10641 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 150b49b3-993a-3376-8548-7843a453dbfd | -3.08127 | -54.17891 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1544c50-d971-372b-a1b1-3c79e55187f5 | -3.80979 | -51.034 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d573e5f0-bcb9-36ad-9d45-6c196feab336 | -3.35601 | -50.474 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65846b8f-e615-3119-86ae-3d6e82ca1bab | -3.00208 | -54.12001 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 51063431-e522-3b5f-8466-a73f514ea2cd | -3.35652 | -50.47062 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 764af5e3-5741-36ba-98a2-b8d7dedb3f37 | -2.94321 | -53.2267 | 2026-10-07 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb97baea-e3ea-3791-8ced-1457d457d3fc | -3.53899 | -59.47909 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96f77925-279b-31d9-bd74-e2c28f5a8325 | -3.19865 | -53.95135 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6d3c2fb-e2ed-3334-8b1f-ef0ae25fc49a | -3.05114 | -54.26377 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab71abb1-4d7a-35c9-8993-b0a3e3d8be0d | -3.60104 | -54.35975 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 978d071c-d0a8-39b4-8ffc-3fdc3605bdde | -3.50546 | -51.68708 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20dd3836-ffc9-324c-ba14-289800c9d189 | -4.37042 | -54.75027 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f5e48e10-ee7b-3516-8fc6-d464f6d8976f | -7.24833 | -45.2627 | 2026-10-07 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b92f8026-426e-3ecc-af8e-676408eaa8a3 | -3.52397 | -54.33015 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f65679e-92da-34cd-8ec3-c189f783517d | -3.06732 | -54.15878 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a44f09bf-0bbe-3688-b782-b439b40f1c5f | -3.85029 | -55.9906 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5d410c0-fdae-3653-bad3-391e9ab8d663 | -3.54555 | -54.49778 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a05b927b-ae9a-3be6-b4de-473d181edf62 | -3.46924 | -50.08003 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5b497cea-d7c0-3772-943d-06bdf52d00f1 | -2.57296 | -56.1499 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0616038d-517b-3dfd-8cba-f75e875299bf | -3.04664 | -53.94265 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f856efd-cf84-3d74-8ce0-d73b17f9ad3d | -7.18397 | -52.61651 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cde4b75c-ca60-3ac2-b0aa-3e418fe3db06 | -3.29713 | -54.05732 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 578ef05d-e8d4-3da7-a1f0-f2fbd1552997 | -1.71928 | -49.82926 | 2026-10-07 05:04:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eb27df1-defa-3b41-b4c0-f906335927c8 | -3.24387 | -53.87483 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a6d17f8-bb72-37b3-874b-e7be32d4782a | -1.47787 | -54.51096 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 228c23d1-4f28-35c5-83a4-e677ed6131cf | -3.50072 | -54.63306 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e93c5a5-623e-3e5a-b010-c5f7e16133ef | -2.99344 | -51.04964 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 019588b1-24a3-3cfb-a94d-8215d5acbf69 | -2.91901 | -54.10744 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cab48f8-0ebe-34e4-b49f-4b7751ecb49e | -3.52335 | -54.64013 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6faa207d-0e07-3098-b9ae-3c35c314ddaa | -8.71619 | -45.19178 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 88661bb6-79db-3a05-9fdc-086e28476cd8 | -4.04595 | -50.98525 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b7c7f7f-3df7-3c40-831d-d82d8a9b2050 | -3.16711 | -54.08771 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95e99c57-0e82-363f-a477-0abdaea63006 | -3.09786 | -54.15985 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed830361-e4bb-3022-9464-5a0a6897a650 | -3.27271 | -54.02116 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 301fe0c2-0fc1-3be5-b06d-145194accea8 | -3.18236 | -50.56152 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 791ba4d0-2ca5-32c5-8dd5-70a0461625b6 | -2.87251 | -54.14336 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0b38a9c-c56d-3d59-a108-08ff29e9b1da | -3.05598 | -54.2324 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4569996c-cd4c-3d32-b740-46b601c5ee04 | -2.93359 | -53.94728 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1cda689-9361-358d-9ef4-869103c9b5d7 | -3.54506 | -59.46576 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1a8a394-d119-3d38-a220-5e0e90bfedd7 | -0.04733 | -53.25325 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f18610a9-f706-3c5d-a625-9401cdf7df51 | -3.51626 | -54.66384 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f0b0d45d-2b54-3c14-95c5-846b35af79c4 | -4.13972 | -54.92029 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 9f88df89-255e-3de6-9d59-fed9688f44e8 | -3.04324 | -53.92032 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9023fd7-6110-399d-9aad-d72ba49ade90 | -3.07154 | -54.24194 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea0b9a4f-da68-315e-9c16-ee20a05c2878 | -2.04875 | -56.88909 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3760a529-c91e-3c1c-9261-c8e4e9b85dde | -3.62783 | -55.27977 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5da01d2d-af55-31b3-9786-784f111cae5c | -1.46028 | -54.64511 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9b619a5-0602-36b4-9804-b38f8ef21a23 | -3.73238 | -51.21132 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91dbade2-6ce2-3ddf-b596-4030556b2976 | -4.1408 | -54.91339 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56ae966e-5f67-3978-a3db-448805627c1c | -3.02849 | -54.52015 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a557962-da1b-30bb-93ec-8dc710fd0af2 | -2.49225 | -56.101 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69013355-b889-3eb7-894a-d8f24457e209 | -4.27525 | -55.71266 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b634498-782d-3a9a-bd18-5711dc748799 | -4.44835 | -55.01456 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b6c87f1-4306-3e2b-a77d-5303df3a4d47 | -3.13261 | -53.71084 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27a18ba9-d280-3b06-bce6-44e4f54e4ffb | -3.29727 | -54.0394 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 540d525b-9fb0-3f06-b19c-622b97fa98bf | -3.04819 | -53.88834 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc782c91-82fc-3c12-8b6a-8a1a2a474dcd | -5.01657 | -49.93994 | 2026-10-07 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e639a865-201d-3548-98cc-5629c0952c9e | -7.27249 | -46.15214 | 2026-10-07 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cd5764cf-a0dd-30e6-9c12-3cedf2e66d4a | -3.72857 | -51.21072 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16b95755-422f-3457-8df6-16662abfb10b | -3.17284 | -50.43925 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70dd6472-706a-3a1d-ae65-f3a1f4a73b5c | -3.09111 | -54.29147 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 865063ea-6d7f-389e-9e2e-90fca2b1ba93 | -7.18746 | -55.1188 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaedb89f-815b-3174-80bf-6ade8d8fc2fb | -3.98773 | -56.2219 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85238cdb-f679-3df0-b75c-798300bda334 | -7.8747 | -44.19552 | 2026-10-07 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5b03c107-6498-383b-ad33-7d66e0408366 | -5.67743 | -53.48863 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70d7b8bb-658a-3e79-a701-5a47d07c67b5 | -2.03347 | -57.0536 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e6aa2e4-8949-3dda-9171-af9ae9fb9fba | -5.23365 | -50.90868 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README89.md)
