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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63cad891-e762-302f-8d4b-b58be406ebda | -13.3392 | -45.2377 | 2025-08-15 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 607.8 |
| c265ea26-6d18-30ed-a3e2-4d38885a018e | -6.8673 | -42.7961 | 2025-08-15 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 388.9 |
| 5cc309ec-13a6-30d7-9eec-c215c652a3f3 | -6.4165 | -44.6008 | 2025-08-15 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 43953743-0608-3842-901b-03861b04d157 | -8.6694 | -62.4579 | 2025-08-15 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 81c6258a-884d-3b01-ab62-08f4fa9aeeba | -7.5292 | -61.3254 | 2025-08-15 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 23034f8c-4304-3988-9768-f02f1a05b860 | -9.1069 | -44.7261 | 2025-08-15 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 5ccc2e9f-9667-3df6-bb2a-9424aceb869c | -7.5291 | -61.3444 | 2025-08-15 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9a1c05c2-9f03-33fd-818b-59352f13078d | -12.6461 | -45.1879 | 2025-08-15 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| d3557aae-c9ba-37c6-9675-95609d44d21b | -6.8671 | -42.8197 | 2025-08-15 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 238.5 |
| e09758c7-d015-360d-b636-73dfc51b2192 | -16.3741 | -50.9089 | 2025-08-15 14:00:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d82bc70e-1b52-3a17-b99f-e130c27aea6a | -8.6695 | -62.4389 | 2025-08-15 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d1af3104-c376-31e1-a48b-bdcb943ebc22 | -7.3894 | -44.8817 | 2025-08-15 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 449.3 |
| 61a89a0a-9419-30a8-91ba-17c245fefddf | -7.9333 | -61.7471 | 2025-08-15 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d754fca2-8945-3f93-990b-f1a673a06ef6 | -13.3392 | -45.2377 | 2025-08-15 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 576.5 |
| 1771006b-6498-3285-800c-22eeeac20141 | -13.3397 | -45.2145 | 2025-08-15 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1357.7 |
| b500c144-3a33-3a2c-a14a-9e4751e8518b | -13.8743 | -45.5643 | 2025-08-15 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 95a0186e-ddda-32ee-87fc-a029ac47e68e | -7.3896 | -44.8589 | 2025-08-15 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 5d886113-633e-358d-8f72-1f0ab4ec87cf | -14.5631 | -52.0557 | 2025-08-15 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| c8e9b12f-ba10-30cc-b279-ddf0a9322585 | -12.4973 | -47.0118 | 2025-08-15 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| c3de3ee4-8463-396f-bf38-122458f0dbda | -6.8673 | -42.7961 | 2025-08-15 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 328.4 |
| 1abfeef6-2a6f-3c6e-8e5c-20774d0b7403 | -7.4085 | -44.8571 | 2025-08-15 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 526.4 |
| 82b22402-3f11-3bb9-b76d-2c3b8d34f6d8 | -9.4994 | -60.5278 | 2025-08-15 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1af836ca-f11c-37cc-b417-fe21eb2e966e | -7.5292 | -61.3254 | 2025-08-15 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| aa44e281-ec16-3744-86dd-1c6bd46a3662 | -14.5634 | -52.0344 | 2025-08-15 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 087f8a22-229b-37d4-bfd1-916e7a545f31 | -12.6461 | -45.1879 | 2025-08-15 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 9e4ccf8d-1709-37ff-88bf-00b905c26681 | -12.5938 | -46.9753 | 2025-08-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 720e5cb2-d0fd-3639-95f1-20d633af41a4 | -12.4973 | -47.0118 | 2025-08-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| f4f12101-4ccd-3668-9efb-bd5dd4f190f5 | -7.3894 | -44.8817 | 2025-08-15 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 249.5 |
| f9709ce7-ff10-35fc-b35c-e32ab0565735 | -13.4759 | -56.6537 | 2025-08-15 14:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| ddbccc0d-2698-309f-97bf-63d9bcf76aeb | -12.5947 | -46.9301 | 2025-08-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 62c5487c-120f-36fb-9693-026c02393116 | -8.6694 | -62.4579 | 2025-08-15 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 4e67d2cf-5471-3d65-903c-c91878351ea4 | -13.3392 | -45.2377 | 2025-08-15 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 377.9 |
| 6ff00c90-a20d-3cc9-944f-4055afdb69ff | -6.4165 | -44.6008 | 2025-08-15 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| b60b2381-15b7-38aa-8ea8-dfb94df526ea | -16.3741 | -50.9089 | 2025-08-15 14:10:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 3c93b017-a74e-3a61-8468-2d97bd938cf7 | -6.8673 | -42.7961 | 2025-08-15 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 268.4 |
| d1b872d4-906a-3c02-b6c6-01ce5422dc9a | -6.8671 | -42.8197 | 2025-08-15 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 200.7 |
| 6827e70e-6d6a-3f56-8776-d8b07522b8cd | -13.1262 | -57.1695 | 2025-08-15 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 93ff2769-7b94-33fe-a444-4f765251cd87 | -13.3397 | -45.2145 | 2025-08-15 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 937.1 |
| 8ec208a6-9fdc-315d-b040-d4e2b9466e3d | -14.5631 | -52.0557 | 2025-08-15 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 126.9 |
| aad5ad80-5125-3802-87b2-b6e523c997e5 | -9.91 | -60.448 | 2025-08-15 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| bed10627-b4dd-31b6-b066-bf43e908f56c | -8.6695 | -62.4389 | 2025-08-15 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b48ed7a7-7e40-354e-8abb-c18c25285a34 | -10.0514 | -59.1208 | 2025-08-15 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a090ee7f-ef5a-3dd1-a8b5-90f15af15031 | -7.5291 | -61.3444 | 2025-08-15 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9f9d843a-1b9f-3d1f-b9b1-42ce959eacfc | -7.3896 | -44.8589 | 2025-08-15 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 23d262b5-61c6-3132-b149-aafbb5ad2efd | -9.9102 | -60.4287 | 2025-08-15 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 87df098a-60a0-39f2-a73a-18bbb2679a1c | -12.5942 | -46.9527 | 2025-08-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 201.3 |
| efe7be28-fc8b-312c-b4cb-15c824b043f7 | -9.4992 | -60.547 | 2025-08-15 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 5b15f951-832c-3d80-98d0-790d656ed645 | -12.5165 | -47.009 | 2025-08-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 44347ab6-af1f-38ac-b785-ba9f14e4dd25 | -12.575 | -46.9555 | 2025-08-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 49e31773-5239-35ac-aad0-f960c7df02e3 | -7.4085 | -44.8571 | 2025-08-15 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 709.6 |
| 38aa49b0-71ef-3dca-b658-7e23546076e5 | -6.4353 | -44.5993 | 2025-08-15 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 639ce383-77ac-3bf8-b565-a713de3d4348 | -9.8915 | -60.4297 | 2025-08-15 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 0ddd93b6-afa1-33ab-a7df-e5c1defacd74 | -7.0201 | -44.2966 | 2025-08-15 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| fa94414d-7c1c-30cf-96c5-266dbb530d32 | -13.1262 | -57.1695 | 2025-08-15 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 4eb73f1a-a32b-345b-8dff-a1b274e826d8 | -13.3392 | -45.2377 | 2025-08-15 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 311.0 |
| 03013a9e-8f5d-3060-8902-3f2e85255c5b | -7.3896 | -44.8589 | 2025-08-15 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 185.3 |
| a81fd5d0-75bb-369b-a157-a558e89e8daa | -13.4568 | -56.6555 | 2025-08-15 14:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8951392e-e157-38bf-8d9d-20fd3c6f7b39 | -13.4759 | -56.6537 | 2025-08-15 14:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1107b78f-e02d-3bae-811e-602dd1c93f1c | -12.5165 | -47.009 | 2025-08-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| c425c348-aa5f-394e-b3d2-01e0e589e920 | -12.5942 | -46.9527 | 2025-08-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 259.7 |
| c0760b5a-c20c-3fc4-af32-86fa7f7789ed | -9.4994 | -60.5278 | 2025-08-15 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4fd84940-b1cb-3a9a-9650-b4015cca387b | -12.5934 | -46.9978 | 2025-08-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 088101ff-b3f3-339d-99e8-c34d721a4ac7 | -9.8914 | -60.449 | 2025-08-15 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d1c59aea-cd6b-3e24-8f45-a4445e25d39d | -12.5947 | -46.9301 | 2025-08-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 383d59ca-2f08-337b-b9b9-feeaa5b3912a | -7.4085 | -44.8571 | 2025-08-15 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 764.5 |
| 92f38505-ed79-315d-9b9e-f6594023328d | -12.4973 | -47.0118 | 2025-08-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 617d868c-238c-3896-9081-b5c5b2b8a7fa | -9.518 | -60.5268 | 2025-08-15 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c6303459-b2d7-3d71-9d8f-066a705ba056 | -13.4757 | -56.6739 | 2025-08-15 14:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 0dd50d0d-364f-36dc-b46b-caba125d4279 | -9.8915 | -60.4297 | 2025-08-15 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 7271fc65-4f05-31d8-a2bb-5a1ef59f46c8 | -6.4165 | -44.6008 | 2025-08-15 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 012a89f6-3b06-3a96-abd6-b7c2cf213ab5 | -6.8671 | -42.8197 | 2025-08-15 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 164.1 |
| 9fc43d37-4595-3978-bffe-130e0c92c5ab | -12.575 | -46.9555 | 2025-08-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| bb553f10-b84e-3a1a-94d2-c4a05013091a | -11.9296 | -43.4288 | 2025-08-15 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 5e5d19c3-0ab2-3426-9ff0-349d58063633 | -6.8673 | -42.7961 | 2025-08-15 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 229.1 |
| 34dff5f1-0b82-33b9-a50c-cdef61f2c27c | -16.3741 | -50.9089 | 2025-08-15 14:20:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 93ae55db-64cf-30e2-88fa-1eaee3744feb | -7.3116 | -60.628 | 2025-08-15 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d71ae2ad-677b-3a14-9c65-3e66957cb40e | -13.1265 | -57.1494 | 2025-08-15 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 22ffd9e9-34b3-3851-850f-6450005babcd | -12.5746 | -46.9781 | 2025-08-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a01aea75-aff7-3b44-b934-cb7d513eddd8 | -8.6694 | -62.4579 | 2025-08-15 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 39ee9bcb-7b95-35e3-8107-48d9626fcbb8 | -7.2931 | -60.6287 | 2025-08-15 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 1c2893d4-bafe-3724-bff8-d9a381adc435 | -14.5634 | -52.0344 | 2025-08-15 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 50dab1aa-b1a4-3550-a594-e6d6fdf89bd3 | -10.0514 | -59.1208 | 2025-08-15 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 74b55634-6c05-3116-b35e-20d67590e09d | -8.6695 | -62.4389 | 2025-08-15 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4b81b358-4621-32ff-84cb-d31fe89060a8 | -14.5631 | -52.0557 | 2025-08-15 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 5b3644b0-5e88-317d-985c-75c1b545b561 | -7.5291 | -61.3444 | 2025-08-15 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 17f15d34-8f38-343d-8d52-c50af6d370c4 | -7.5292 | -61.3254 | 2025-08-15 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 3ed8314f-770f-39e7-8b7e-98376985b16e | -12.6461 | -45.1879 | 2025-08-15 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 4fc233e0-d8d1-3dbf-97fb-1636601b3a0a | -13.3397 | -45.2145 | 2025-08-15 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 626.6 |
| 16adfb67-637a-3cbc-a39a-f862593e9422 | -7.3894 | -44.8817 | 2025-08-15 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 361.6 |
| 58a6f561-16fe-3f0a-8bf7-f6c1575aa6df | -12.5938 | -46.9753 | 2025-08-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 409.6 |
| 31cdb6a2-b9b3-3a44-9120-ab4fc8f011bb | -12.5942 | -46.9527 | 2025-08-15 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 305.6 |
| b7627554-931c-35fd-818b-aca7a913ae6a | -9.4992 | -60.547 | 2025-08-15 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ac87f30f-2fe5-3f95-8577-1b3e4a919757 | -7.3894 | -44.8817 | 2025-08-15 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 297.7 |
| 487fd5f0-0bd1-387b-b0ca-89a236c6c74e | -13.4566 | -56.6757 | 2025-08-15 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| be56c1d4-5e7a-32cb-80d4-53489b739909 | -6.8673 | -42.7961 | 2025-08-15 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 265.1 |
| 8eb08c96-5e44-39cb-a310-7110a0fc4bef | -7.3116 | -60.628 | 2025-08-15 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 17393f68-2b6b-36f2-915c-5d93afbf302d | -8.5689 | -63.9155 | 2025-08-15 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 135.1 |
| e6ff63bf-5b8d-3345-8198-7cc9a06e2a53 | -6.8671 | -42.8197 | 2025-08-15 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 151.3 |
| b5a5efaa-5fe3-3bee-aaf9-95f014585e5c | -7.6104 | -63.4972 | 2025-08-15 14:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 4fb9efd0-b5ec-3dde-a4d5-8cf0ccdabe67 | -13.1265 | -57.1494 | 2025-08-15 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 141.5 |


[Clique aqui para ver as próximas entradas](README78.md)
