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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59bd3c42-a930-3f15-945e-86571c3b2e09 | -15.6594 | -55.9742 | 2024-10-25 03:56:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 5739c3dc-4fd9-3241-9e03-44e5114150e2 | -17.0586 | -57.4517 | 2024-10-25 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 8629d231-e87b-3120-9d61-71db818bc819 | -17.0381 | -57.5155 | 2024-10-25 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| 60d93554-d26b-3fc6-b23d-81e71b6a2a87 | -16.9792 | -57.5223 | 2024-10-25 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.3 |
| be19b8a3-cb7f-3ae8-84b7-89bf7fa3e0db | -16.9596 | -57.5245 | 2024-10-25 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.9 |
| d0d94076-9ada-364b-8418-ab60407311b4 | -16.94 | -57.5268 | 2024-10-25 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 7b5ea370-2808-3df3-9b44-10fc55bf148d | -17.2537 | -57.5108 | 2024-10-25 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| a472629e-cc30-35b9-a94c-e7f8ad3cabe1 | -17.2386 | -57.2256 | 2024-10-25 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 84455c36-81f3-3edf-899d-9fdb15a71c93 | -17.219 | -57.228 | 2024-10-25 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| e0fcedd7-bcf0-36cc-a63a-343c91b481b7 | -17.2186 | -57.2485 | 2024-10-25 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 07f96d7d-88e0-3a77-a9df-eadfcc0cccc9 | -18.3199 | -56.2404 | 2024-10-25 03:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 10fb9fa3-9e32-335d-becb-e87e255b9b7b | -1.1834 | -53.6569 | 2024-10-25 04:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| c81a80c7-0c8c-3540-8082-cdd4cde584a2 | -1.1834 | -53.6771 | 2024-10-25 04:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| e9fe5bf7-4e1c-3ddc-b7f6-18595db9a398 | -1.6062 | -53.3087 | 2024-10-25 04:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ba7bd29a-0388-3422-a0b0-d04e65a60c79 | -3.2135 | -46.8063 | 2024-10-25 04:05:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 0c46a4b1-29d8-3d7b-a1f7-5a9b5278d910 | -3.1949 | -46.807 | 2024-10-25 04:05:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 5198401a-9b13-3c21-8f95-e483f63235e4 | -3.9581 | -46.422 | 2024-10-25 04:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 132f89d5-4864-3bb6-9257-2ec900560491 | -4.2429 | -48.5474 | 2024-10-25 04:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 348fdc8d-7e15-39ac-8b0a-810bc6976081 | -12.0012 | -63.9013 | 2024-10-25 04:06:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 79325fd6-5453-336f-bc0d-48344b5d8691 | -12.478 | -63.1693 | 2024-10-25 04:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3306e77d-a831-386b-bd54-e0ca2215e258 | -12.4591 | -63.1704 | 2024-10-25 04:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c4ad2798-1ec5-333f-9740-8c903626b23c | -12.3782 | -63.8821 | 2024-10-25 04:06:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 2d94a0a7-1205-367e-9797-14532ecdea04 | -15.6788 | -55.972 | 2024-10-25 04:06:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 05c4369f-a93e-387d-ba27-1bdfd8511c1c | -17.0586 | -57.4517 | 2024-10-25 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 99bdc756-b265-392f-96f7-73bb660f115f | -17.039 | -57.454 | 2024-10-25 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 90966b53-7ac8-31b0-888e-992b8cf2b6c0 | -17.0381 | -57.5155 | 2024-10-25 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| ed00ee36-92d7-3c11-896d-22a9ad170992 | -16.9792 | -57.5223 | 2024-10-25 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| 009b5342-090d-3235-a811-676ff6752d6c | -16.9596 | -57.5245 | 2024-10-25 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.8 |
| 58abc619-1fa0-35be-a757-ed66bc3a7350 | -17.2537 | -57.5108 | 2024-10-25 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 361bbefd-c51f-3fc0-b0b2-d83d43df80ed | -17.2386 | -57.2256 | 2024-10-25 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.6 |
| 0680ac81-b1f2-3bae-b7a6-2e8d92827162 | -17.2186 | -57.2485 | 2024-10-25 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| cddbc54e-2914-3cfc-95ce-d65bba0e30f3 | -17.2147 | -57.4949 | 2024-10-25 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 7802a54e-3a38-3c3f-9e02-d55a4ac4a682 | -17.7671 | -57.3673 | 2024-10-25 04:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 9ef15188-ef41-3e0d-8147-f82b57f96082 | -17.8628 | -57.5407 | 2024-10-25 04:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 03f9dbb8-1949-30aa-a51f-ef9b1444bb5d | -18.3199 | -56.2404 | 2024-10-25 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| f977aea1-4350-3ddf-8576-3c8d356b3c9b | 2.63414 | -50.88401 | 2024-10-25 04:12:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 151d0c50-3f3f-3e4b-8768-51c26cc11cc1 | 1.80219 | -50.46185 | 2024-10-25 04:12:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8b9016e-c088-364d-ab83-0f2616b38b99 | 1.78221 | -50.47523 | 2024-10-25 04:12:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb66ce24-c1c8-316f-bfd1-c15eb017070c | 1.7817 | -50.47182 | 2024-10-25 04:12:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b4e4913-4a4c-3dec-ab97-4a9f6606c64a | 0.13768 | -51.0723 | 2024-10-25 04:12:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c837e2c-ea70-3a6b-853f-b1e820dc2538 | 0.13663 | -51.07411 | 2024-10-25 04:12:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8780615a-2a39-3ec7-a4ea-8cbd5b7cad54 | 0.13221 | -51.07313 | 2024-10-25 04:12:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19ee00ae-760a-32c6-956b-f8434cef1983 | 0.13117 | -51.07495 | 2024-10-25 04:12:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 537a5421-f8a0-332f-be34-72cfb43e6a01 | 0.00795 | -51.22163 | 2024-10-25 04:12:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 30167a54-d847-3176-a5a3-e2dac3f1a18d | 0.00243 | -51.2224 | 2024-10-25 04:12:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 44557fbd-dd12-38f4-ad2b-dc4251c319e8 | 3.49316 | -51.25758 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36462f6e-13de-37a2-8356-d445b796cf89 | 3.493 | -51.25676 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffaa8db5-c925-36a9-a1b3-9f257694cd0d | 3.49257 | -51.25348 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c55fa285-f8a9-3570-b07f-b38a5801dabb | 3.49238 | -51.25266 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce79dbdb-7571-3253-bc36-fdeb153667f4 | 3.48617 | -51.25021 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31072b7e-2482-37b4-87f3-38c30434e049 | 3.48595 | -51.24938 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cdba779-37bf-3eb1-9b7a-e6863bd5b259 | 3.46975 | -51.26005 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ea1a5a6-64b6-383b-9fd3-e7fcb5d806ee | 3.46515 | -51.26904 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9105a451-59ee-3e4b-9f01-8d1bfa84b497 | 3.46454 | -51.26495 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06f21d82-01d3-3daa-be50-f44003c37022 | 3.46393 | -51.26085 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 224fc110-8c5e-3616-bc06-70a6fe2bb0cf | 3.42163 | -51.29631 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 363b4f8d-feb7-38ae-81b0-326ad81591cc | 3.41581 | -51.29713 | 2024-10-25 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6f44dce-b0e0-3ccb-af51-b87f72b5ebb4 | 1.01025 | -52.21599 | 2024-10-25 04:12:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c339e58-cfcf-375e-940a-0ecb47ad2506 | -5.5652 | -35.5289 | 2024-10-25 04:14:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b3886db4-ad0c-3b9a-a73b-93d755037623 | -7.77118 | -34.83606 | 2024-10-25 04:14:00 | NOAA-21 | ILHA DE ITAMARACÁ | PERNAMBUCO | Brasil | 2607604 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b3227f13-5af1-36a3-97ac-09eebd6961bd | -8.61919 | -35.08998 | 2024-10-25 04:14:00 | NOAA-21 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 91b424d5-6ddd-37b2-b824-12b414061f73 | -8.6141 | -35.08926 | 2024-10-25 04:14:00 | NOAA-21 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 89818524-e3d3-36fe-96c8-fd24b08e1e75 | -8.61371 | -35.09225 | 2024-10-25 04:14:00 | NOAA-21 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c8bbd338-a25e-3d49-a42b-1f6a1675a09c | -8.11581 | -37.59926 | 2024-10-25 04:14:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3666a7f9-382e-39a4-96d3-b98780757a7e | -5.17767 | -37.98689 | 2024-10-25 04:14:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 99f40949-75e9-35a4-944c-3c1f141c13a5 | -5.17714 | -37.98295 | 2024-10-25 04:14:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| efa498ae-9318-373a-84e4-bd37d44d65ae | -5.17639 | -37.98808 | 2024-10-25 04:14:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fa3a6cff-e48a-3a41-9d63-b9f4eab1dcfb | -5.15312 | -37.74271 | 2024-10-25 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 87856ab8-b352-39f4-96f6-0292bda2aa2a | -5.14962 | -37.73854 | 2024-10-25 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.8 |
| afbf9ad6-6041-353e-ab57-566e15804ebf | -5.14909 | -37.7421 | 2024-10-25 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 87f4e488-0c56-31d8-a1d8-17507bd61b88 | -5.95752 | -38.62885 | 2024-10-25 04:14:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1aae3327-0a85-32ed-a298-e0b56b95c55c | -7.21723 | -38.98668 | 2024-10-25 04:14:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8919ac9a-bb6c-37b6-878f-b6a8d60771b0 | -7.06733 | -38.90578 | 2024-10-25 04:14:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b6213e05-45e0-394d-a3bf-ab07b70cbed0 | -9.38217 | -38.3023 | 2024-10-25 04:14:00 | NOAA-21 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a3c92280-892e-375e-bae6-dff7d6b53882 | -5.53725 | -39.1717 | 2024-10-25 04:14:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d100cb95-f5f9-3739-8596-23bbbc246d35 | -7.34113 | -39.3281 | 2024-10-25 04:14:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| efa9ffd5-d2f3-3fd6-886d-ed6b2e22a587 | -7.32921 | -39.33067 | 2024-10-25 04:14:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 03983bab-415c-361e-8ea5-b34fb74069a2 | -7.32853 | -39.3352 | 2024-10-25 04:14:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e461acc6-5f89-3f8a-afb8-49b61a542c23 | -7.32546 | -39.33003 | 2024-10-25 04:14:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9da857d4-3e73-3870-9e74-cb5b9c4ad72c | -7.32478 | -39.33457 | 2024-10-25 04:14:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aecbcbeb-97c1-3870-92d6-85ad4e4b7b2e | -9.24118 | -40.93959 | 2024-10-25 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f0cde815-0984-3cfc-881f-f98991cdce20 | -9.01117 | -40.70811 | 2024-10-25 04:14:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 75bb888b-fc2c-395f-a4b1-00dbd17dff18 | -8.80064 | -39.77499 | 2024-10-25 04:14:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 74f0305c-a237-3e5d-8550-e91c5d91a43c | -8.39435 | -39.83486 | 2024-10-25 04:14:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d434f467-93ba-37bd-ab81-ddd6da372b6d | -3.21391 | -40.70168 | 2024-10-25 04:14:00 | NOAA-21 | MARTINÓPOLE | CEARÁ | Brasil | 2307908 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5326db6d-b0f4-3e58-aa87-48447c872381 | -3.06369 | -40.0425 | 2024-10-25 04:14:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f7a13daa-ad3f-322e-a908-bc79e75b1f4b | -3.06023 | -40.04196 | 2024-10-25 04:14:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 09a692d8-be68-3e08-b477-c4823322ac01 | -4.4331 | -40.92512 | 2024-10-25 04:14:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 23ba0fbd-0e68-3b0b-8ee4-dde5a006d6cd | -4.32912 | -40.55101 | 2024-10-25 04:14:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 45250586-4135-354a-9e5e-dcfad5cc3cf6 | -3.89562 | -41.03978 | 2024-10-25 04:14:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d133c4a1-9d00-380b-a765-0ec3d7890e13 | -3.89226 | -41.03925 | 2024-10-25 04:14:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 7a9db289-d833-3341-a2eb-2590493f40dd | -5.05598 | -40.88761 | 2024-10-25 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d6c35539-215c-34a5-8f1e-966d96d80ae5 | -5.60975 | -41.73916 | 2024-10-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8ca41c8b-4e78-37bd-b974-b485295634b7 | -5.60641 | -41.73866 | 2024-10-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e0637935-fc4c-3fa9-9853-c9f1b9b24641 | -7.41763 | -41.79461 | 2024-10-25 04:14:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 047841a9-ab51-3ca7-9faa-076ff4ee5421 | -7.09765 | -41.13971 | 2024-10-25 04:14:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a1e961d-81ed-3f48-ba59-82d4a017450c | -7.09708 | -41.14347 | 2024-10-25 04:14:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5f4c575a-20b8-30a1-96c9-89299b93225f | -7.003 | -41.30083 | 2024-10-25 04:14:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d37a3f7e-670a-3b4b-8896-1a5feb454e64 | -6.99959 | -41.3003 | 2024-10-25 04:14:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cbc06a31-70c8-3ada-a7e4-62b10a9dbba6 | -6.96441 | -41.32503 | 2024-10-25 04:14:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
