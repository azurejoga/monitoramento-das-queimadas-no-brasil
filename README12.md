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
| a05b783e-afe4-325e-9a0a-c6234f8c8184 | -2.0885 | -52.1119 | 2024-10-18 00:56:19 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 938505af-9752-3166-a92f-6b0ea92ba60b | -2.0901 | -52.1189 | 2024-10-18 00:56:19 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6089aae0-73ad-39fa-a439-21aec80e715a | -1.1427 | -48.092499 | 2024-10-18 00:56:19 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43168a7e-a4c3-3ea8-baf0-c2d97cec6728 | -1.1446 | -48.100899 | 2024-10-18 00:56:19 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3a0cddb-1941-3a34-bddb-763addfc600a | -1.1466 | -48.109299 | 2024-10-18 00:56:19 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 195781c7-892c-3521-b461-ca2fb04488fa | -2.1488 | -53.639 | 2024-10-18 00:56:23 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b97239ab-4d62-3547-b093-f9dc9cb1d2f8 | -2.0854 | -53.406502 | 2024-10-18 00:56:24 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 405c2694-89ef-3244-a5ae-5f34801a3552 | -1.5993 | -52.587002 | 2024-10-18 00:56:28 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29e16f56-ea2b-309b-a5f4-e252658c0c5a | -1.3965 | -52.331501 | 2024-10-18 00:56:31 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fe4fd73-4565-3488-8133-e10db7f00f71 | -1.3981 | -52.338402 | 2024-10-18 00:56:31 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bde3a3e2-7c83-3f50-bfa8-2b328e149075 | -0.8724 | -52.609001 | 2024-10-18 00:56:40 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e938e069-5a49-3965-a89d-933c7bc44146 | -17.189 | -45.4644 | 2024-10-18 00:56:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 70.1 |
| ae2ebff7-0bf7-34d5-a9d5-115e86f834de | -17.0191 | -57.4768 | 2024-10-18 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 8485edae-0e01-393c-97c8-d0fe4af81b3d | -17.2177 | -57.3102 | 2024-10-18 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 65d079d5-6130-3dfd-9f23-398a4f1e1c9e | -17.2373 | -57.3079 | 2024-10-18 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 165.3 |
| 8123f0cb-0201-3a1d-a68b-892b4b704302 | -18.0632 | -57.3514 | 2024-10-18 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 68455f0e-8325-36f6-889c-e2148c638472 | -18.1798 | -56.3217 | 2024-10-18 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 5e1186e2-2fd1-376c-954e-81adef80ffa0 | -18.1989 | -56.3608 | 2024-10-18 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.3 |
| 0b751ec4-e315-3128-9598-6787de5aef0b | -18.1993 | -56.3399 | 2024-10-18 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.0 |
| 106eea1a-c900-3b22-88f0-844d152a344d | -18.1997 | -56.319 | 2024-10-18 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.0 |
| cdad1442-aa72-3202-9628-80daac27266b | -18.2537 | -56.6237 | 2024-10-18 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 172.9 |
| 911f3e1a-39ca-3d76-a85d-0b1a42500a1b | -18.254 | -56.6029 | 2024-10-18 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 6847c28f-48d1-3633-a21e-d909eeffcad9 | -18.2735 | -56.6211 | 2024-10-18 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 12067644-6fc6-35bd-a907-3c782457aeaa | 0.2586 | -51.0056 | 2024-10-18 00:56:53 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 996a78c4-cfca-38e8-8da9-6fdd120169a1 | -20.7917 | -50.6786 | 2024-10-18 00:57:01 | GOES-16 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| 890af283-3783-3795-a7bf-a8c97201df77 | -20.7911 | -50.7012 | 2024-10-18 00:57:01 | GOES-16 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| 2567497f-dde4-367a-86c6-efc899dfeeb6 | -21.9662 | -49.7186 | 2024-10-18 00:57:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.4 |
| d49b473a-5d64-39a0-a452-e37db4db7418 | 1.0114 | -52.219601 | 2024-10-18 00:57:09 | METOP-C | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1437322f-a1a3-3f0f-92ac-e8510f51d3ed | 1.1202 | -52.329899 | 2024-10-18 00:57:11 | METOP-C | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4215c5c5-e1d8-313c-bbde-5cdf92dd13d3 | -23.3701 | -47.3747 | 2024-10-18 00:57:14 | GOES-16 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.3 |
| 29e035f2-54c8-3745-9751-728f250ce3be | -1.619 | -47.0919 | 2024-10-18 01:05:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 82ef8ab6-7ac3-3a5a-808e-97c21cbf80e0 | -1.6191 | -47.07 | 2024-10-18 01:05:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ccb15baf-ea12-35d2-9e0f-45097803a15f | -2.5744 | -49.2273 | 2024-10-18 01:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 5d6c72fa-107a-3ba1-954e-b680027d416e | -2.6105 | -49.4811 | 2024-10-18 01:05:21 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 7cf42104-2067-3cb5-bbf8-ecea49b8ef4e | -2.7045 | -54.656 | 2024-10-18 01:05:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 4c2c2c49-0e10-371c-83f2-96dc6226fbde | -2.8795 | -51.6695 | 2024-10-18 01:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ef3ddf9b-9098-3741-a9f6-93cf09ade0e7 | -3.1382 | -51.497 | 2024-10-18 01:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 6e6c2ed4-c512-3836-a1ca-c8103d955d46 | -3.1566 | -51.4965 | 2024-10-18 01:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| c563232b-595b-3595-9e43-16aa718ce3a8 | -3.1567 | -51.4758 | 2024-10-18 01:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a1cf6280-2f61-3697-bdb7-408048f072ac | -3.7007 | -45.9223 | 2024-10-18 01:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 7562de33-6303-35ad-a83b-7be5c701fdc4 | -3.7009 | -45.9 | 2024-10-18 01:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 112.3 |
| afd24105-acc1-3512-a906-ede3e8ff1315 | -3.7291 | -51.3331 | 2024-10-18 01:05:27 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 955e2518-774b-37c9-8cd4-3259a5880852 | -3.8733 | -52.0715 | 2024-10-18 01:05:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4ceeef6d-8a29-36bd-b38e-57c322762d92 | -4.4072 | -45.9773 | 2024-10-18 01:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 244a0842-75de-3534-b464-926b8dba006a | -4.426 | -45.954 | 2024-10-18 01:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 00d0dde0-5d83-3abe-9f95-ea77e53f9d9c | -4.4258 | -45.9763 | 2024-10-18 01:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 238.2 |
| f0c2e828-1323-32fa-b9f9-fa7271764990 | -4.4979 | -61.116 | 2024-10-18 01:05:32 | GOES-16 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 9814ee4d-b963-3d63-9c4c-fafb140d5959 | -4.5614 | -48.0141 | 2024-10-18 01:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| dddae452-da11-372a-8337-4995f2a1ec4b | -4.5162 | -61.1156 | 2024-10-18 01:05:32 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| fc7919f2-7a70-3ae7-b0a5-cf4eb753cbf6 | -4.8917 | -45.928 | 2024-10-18 01:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 3ac786c5-c084-3d08-90b6-13b2dc3bd145 | -6.6703 | -70.1174 | 2024-10-18 01:05:44 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 57b8f74d-523c-33b8-82eb-a77959634319 | -6.6886 | -70.1171 | 2024-10-18 01:05:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 0b9130db-fd31-39bc-8183-15e78243b5b2 | -11.4859 | -65.1198 | 2024-10-18 01:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 481202f4-4295-3939-891a-8582c62a4bd8 | -12.5045 | -55.205 | 2024-10-18 01:06:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4d366c35-59f9-325d-80cb-603bd9f65ccc | -12.5048 | -55.1846 | 2024-10-18 01:06:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 4c68e083-a2aa-3e6c-86e1-2587ba24e18f | -12.4964 | -63.2258 | 2024-10-18 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7e55f532-9943-3fb9-8198-824cf7d8522d | -12.4966 | -63.2066 | 2024-10-18 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 98.8 |
| c9613f16-2216-3816-931d-213ebabaae88 | -12.5155 | -63.2055 | 2024-10-18 01:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 03ec8dad-374c-3216-9c1d-82f6191183da | -17.0191 | -57.4768 | 2024-10-18 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 61b3f032-1831-3827-9c3c-6bf53c8c3aa5 | -17.237 | -57.3284 | 2024-10-18 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 60563612-3d43-3b8a-b5cb-fae40f8a40af | -17.2177 | -57.3102 | 2024-10-18 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| b979cccd-0b7d-357f-bd81-233322f9c332 | -17.2373 | -57.3079 | 2024-10-18 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 179.8 |
| 81f1583b-69f0-38d0-ac6c-de9318f8f218 | -17.8246 | -57.4631 | 2024-10-18 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 7faaf527-617a-3e95-9095-70d73927a862 | -17.8052 | -57.4449 | 2024-10-18 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 4282dfe7-9769-32a7-a96d-6459fc668a36 | -17.8049 | -57.4655 | 2024-10-18 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 155.7 |
| cafb7423-4f6d-3694-8d2e-6acd79185f42 | -17.8045 | -57.4861 | 2024-10-18 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 206abff4-5d25-371b-959c-1f3a9595490c | -17.7855 | -57.4473 | 2024-10-18 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.6 |
| 6e2802c6-ad87-3149-ae2f-2182219e0be8 | -17.7851 | -57.4679 | 2024-10-18 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| a677d5e0-e5d7-3853-b488-1c12f9843d59 | -18.1798 | -56.3217 | 2024-10-18 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 1ef11493-b100-3935-8901-c31e5311a31a | -18.1993 | -56.3399 | 2024-10-18 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.4 |
| add8e74d-289f-3d0d-8ffa-37fcc89f66c5 | -18.1997 | -56.319 | 2024-10-18 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 4ec756d1-dd4f-3886-85e1-ff612e7b8963 | -18.2537 | -56.6237 | 2024-10-18 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 187.6 |
| 6a3dfd3f-4fa6-322b-8f4c-fec7bdadd815 | -18.254 | -56.6029 | 2024-10-18 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 83359c2b-3326-39bc-80d6-16aa111edd0d | -18.2735 | -56.6211 | 2024-10-18 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.3 |
| 40db4443-f05b-3b98-97b3-b603038eb1ed | -19.6005 | -57.0253 | 2024-10-18 01:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 250.2 |
| 222b51eb-7c14-3b9c-9f54-043634fe4ef5 | -19.6009 | -57.0044 | 2024-10-18 01:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 333.1 |
| 58141d96-25cc-34d6-8549-44082f9cd96f | -19.6013 | -56.9834 | 2024-10-18 01:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 196.1 |
| 4254aeb5-ca15-3088-b2d7-30686c36d483 | -19.6206 | -57.0225 | 2024-10-18 01:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.5 |
| b7cea5a5-3bd9-30db-9983-3190ef63a864 | -19.621 | -57.0016 | 2024-10-18 01:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 206.9 |
| de192b84-1507-30db-8ef2-42ecace7da0a | -19.6213 | -56.9806 | 2024-10-18 01:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 123.8 |
| 6542f182-6a77-3c44-b39b-a3d3b2c7f0f5 | -21.9662 | -49.7186 | 2024-10-18 01:07:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.6 |
| f35ed64f-5849-3412-a20b-8550459341e4 | -1.619 | -47.0919 | 2024-10-18 01:15:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 2a2befa9-c47a-32cc-838a-6a57eece83ee | -1.6191 | -47.07 | 2024-10-18 01:15:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 46487a2b-8470-3efa-ae69-518233fa4efc | -2.7229 | -54.6556 | 2024-10-18 01:15:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e1a03594-a330-32c3-9593-6d1f412c6de1 | -2.8795 | -51.6695 | 2024-10-18 01:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| f42cd4ec-a6c2-346e-a192-fd657722bf4b | -3.1382 | -51.497 | 2024-10-18 01:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 2ea1415d-6b3b-352e-b781-f301685b080b | -3.1383 | -51.4763 | 2024-10-18 01:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 87c060fc-0ae1-3b56-a8cd-eae498e5304b | -3.1566 | -51.4965 | 2024-10-18 01:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 6fb277bb-1579-38a1-9cad-60ef56ffe120 | -3.7009 | -45.9 | 2024-10-18 01:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 97.7 |
| af583257-e6ad-310b-9418-097c7a2dfc3e | -3.8733 | -52.0715 | 2024-10-18 01:15:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 599429d0-cf62-38f4-a1f7-3236ad564b6e | -4.4072 | -45.9773 | 2024-10-18 01:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 104.5 |
| f624b3d1-a0ca-3280-a7fc-e61d37c7cae0 | -4.4258 | -45.9763 | 2024-10-18 01:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 171.0 |
| 7772d696-e568-3726-8486-ac5ba2fea506 | -4.426 | -45.954 | 2024-10-18 01:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 92.1 |
| a7668294-483b-3579-ba48-1e30edd97f67 | -4.4979 | -61.116 | 2024-10-18 01:15:32 | GOES-16 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 48be8ce0-430a-3a94-ba2c-6b01f66970cf | -4.5162 | -61.1156 | 2024-10-18 01:15:32 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f61ffa14-a298-3d59-b30a-3ba51cffea09 | -6.6703 | -70.1174 | 2024-10-18 01:15:44 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f1cf6107-9520-3408-812d-3b05bddb3d3b | -6.6886 | -70.1171 | 2024-10-18 01:15:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7ffed3ad-dea8-3b99-9ae9-9f1cb5ea619a | -11.4859 | -65.1198 | 2024-10-18 01:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 9ab256f3-239d-3352-ad34-d1843062f9cb | -12.5155 | -63.2055 | 2024-10-18 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f9e1f572-b6e4-378c-94ec-d40d3d09faca | -12.4966 | -63.2066 | 2024-10-18 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |


[Clique aqui para ver as próximas entradas](README13.md)
