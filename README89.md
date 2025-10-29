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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3637dc24-1f69-3827-8963-4ccd295addaa | -13.9332 | -48.4528 | 2025-10-29 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 76a41af5-1c04-3b4f-a7f7-ac2638541017 | -9.2465 | -46.9712 | 2025-10-29 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 249374f1-1974-34fd-adbe-055a9876c59d | -7.7654 | -46.5162 | 2025-10-29 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| dfe0160e-6df5-306c-8f8f-3db92b9c39f6 | -3.7262 | -41.555 | 2025-10-29 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| a09e3298-a7a6-35b9-94f7-45587d3658ab | -7.361 | -42.4637 | 2025-10-29 14:30:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| cff625c4-643a-3cf5-87c7-a4f93f89daac | -9.4553 | -46.8819 | 2025-10-29 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 7dfa4613-7382-38a8-8c01-0e0197933ebc | -7.9936 | -46.2716 | 2025-10-29 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 998b2777-bb4d-39de-aacf-f727b7d1e5a4 | -13.6632 | -48.4488 | 2025-10-29 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| c11d5ce2-704f-31d6-9c15-d606cb91f115 | -7.5928 | -43.5699 | 2025-10-29 14:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| f2d4bdcc-98f7-3a61-9658-6f1619f54a6a | -7.3421 | -42.4656 | 2025-10-29 14:30:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 252.4 |
| b6d89a20-d2e5-3d93-bcde-61e39483ef69 | -10.3027 | -47.1644 | 2025-10-29 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5393280e-c528-334b-9a72-a6badf792462 | -8.0401 | -42.51 | 2025-10-29 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 148.2 |
| 144b6423-1ffb-301b-8516-4b13c02f9a44 | -7.4108 | -44.651 | 2025-10-29 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| cddb6ce2-84e8-3d0f-8878-abd7ac41fa59 | -7.3418 | -42.4894 | 2025-10-29 14:30:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 295.1 |
| 110cbed9-12cd-3ed6-873c-f474f4b64e2f | -9.8997 | -44.9299 | 2025-10-29 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 5b2a63be-ea99-371b-9b8c-05714c6c0f2f | -9.4742 | -46.8798 | 2025-10-29 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0a3f2830-7b60-3c8d-a143-84926e48a29c | -13.6632 | -48.4488 | 2025-10-29 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6ce9edf8-7895-33b8-b91e-58425800244d | -10.2071 | -45.9412 | 2025-10-29 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 43983be6-e9aa-3a6e-8f94-0c371231156b | -9.4926 | -46.9224 | 2025-10-29 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 9a3d9db4-b66c-369d-8810-27ae9981eb0e | 1.602 | -55.7065 | 2025-10-29 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 54ac8659-982d-37e6-9f26-558e54305a44 | -12.4723 | -44.2141 | 2025-10-29 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3d519044-f0ca-3571-a212-8a400b7a5c11 | -4.1016 | -44.2526 | 2025-10-29 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 7505d25e-8452-3a53-bf16-459f44a876ff | -11.1043 | -45.7347 | 2025-10-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| e16a7b11-24dc-3ee8-a94d-16b6f284e72e | -11.0564 | -47.54 | 2025-10-29 14:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 0307d0b5-ebf4-37c6-a521-6107a8560f8b | -11.3036 | -47.5534 | 2025-10-29 14:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 24b8aa44-d674-3453-9713-b9ab83421921 | -13.5686 | -47.3242 | 2025-10-29 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 694f5b96-8b58-32ea-b8fd-cfcc7c10642b | -13.9332 | -48.4528 | 2025-10-29 14:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 44f8e71f-50c3-35f9-9112-fee0ca2a2a73 | -9.4739 | -46.9021 | 2025-10-29 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 6449613b-c8f7-322a-a6e6-5356e27f421d | -14.2059 | -48.3445 | 2025-10-29 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d235d311-c00c-3dee-ad5a-a8b81a338be6 | -11.4413 | -46.121 | 2025-10-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 24eb8c06-6d7e-395f-bd78-4da2eb83c377 | -7.3421 | -42.4656 | 2025-10-29 14:40:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 208.9 |
| f106563c-439e-3ac5-92eb-cafb7e24928c | -14.4566 | -51.515 | 2025-10-29 14:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 92200a52-33c7-3042-b7db-73be9097ac08 | -9.4913 | -47.0115 | 2025-10-29 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| e212ebcb-25c1-3202-945a-a9038b299709 | -14.8981 | -46.7659 | 2025-10-29 14:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| cb20fd1f-43ec-3d2d-98d8-ec0f8b6fa4f7 | -7.9936 | -46.2716 | 2025-10-29 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 467ff525-7942-34fb-93cd-b1bbe6762ae0 | -7.8035 | -46.4681 | 2025-10-29 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| f42f162f-c55b-32b1-a920-f5094c5668fa | -10.3041 | -44.5785 | 2025-10-29 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e7e05908-b667-3449-a035-6d01bb19d914 | -9.455 | -46.9042 | 2025-10-29 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 22b13fa9-2ff7-3158-ae3a-03177e05885d | -10.2663 | -44.5603 | 2025-10-29 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| b70daec5-379c-385c-88b9-114058e8f2d0 | -7.7819 | -46.715 | 2025-10-29 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 796b077c-7e7f-33db-827a-1abf5935de8f | -9.4556 | -46.8596 | 2025-10-29 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 99253341-fa1c-3cf9-a039-ed3cb375eaa2 | -8.7622 | -46.509 | 2025-10-29 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 9ef1d1cd-21f6-3bc3-a7bb-e70e0372db10 | -12.1464 | -45.1958 | 2025-10-29 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ba2242d1-e319-333f-a3e6-a47492af3d7f | -9.8814 | -44.8862 | 2025-10-29 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| fb0b696e-7258-3310-8bb9-9b3f0f1f2852 | -7.6114 | -43.5914 | 2025-10-29 14:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| eece69d1-8ad3-33c2-a63e-981e408ad66b | -7.8878 | -45.6747 | 2025-10-29 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 94b74c4a-bb21-3fd7-b818-1e471cd2baf9 | -9.1612 | -46.2876 | 2025-10-29 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ca5ede26-5d08-3aaa-aa14-e3ce082324da | -13.9337 | -48.4305 | 2025-10-29 14:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 5751a943-f9cd-3def-9479-198f4304d56c | -7.804 | -46.4234 | 2025-10-29 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 4dbba9e3-49a7-3ed7-b2f9-95cd8b11265b | -11.3032 | -47.5756 | 2025-10-29 14:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 7c3c136f-ca72-3e38-af27-c5eeaae3d9d7 | 1.5837 | -55.7264 | 2025-10-29 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 21aa4278-ba76-3d82-9a9f-652202923f4b | -9.6518 | -46.3454 | 2025-10-29 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1b99092a-4986-3795-adc0-7f7522528e9e | -12.146 | -45.219 | 2025-10-29 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f455ce1f-1c9f-33ec-8620-9808438eb113 | -14.2055 | -48.3668 | 2025-10-29 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 70accdce-d35e-38fe-8905-8770c15093c7 | -7.7654 | -46.5162 | 2025-10-29 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 66794b88-74b7-3e02-895a-3077eefb3785 | -13.5682 | -47.3468 | 2025-10-29 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 123.3 |
| dcddc4c5-431c-322c-a072-8c7e1095881e | -9.8624 | -44.8886 | 2025-10-29 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| b4452b71-3392-35e8-94c8-8b6a8a61c223 | -12.1272 | -45.1987 | 2025-10-29 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 61dd6706-d911-3276-87ad-19e75381734a | -12.7426 | -45.1726 | 2025-10-29 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 693243af-85a9-3330-99a5-6c22f4dbb9b8 | -9.5106 | -46.9872 | 2025-10-29 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 05234a94-8775-37b6-b10d-4b6813912ae4 | -14.6114 | -48.4145 | 2025-10-29 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| ed2bbd7c-021c-3365-b80e-879056f29787 | -7.7847 | -46.4698 | 2025-10-29 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| a1719b69-47c0-3b49-9693-ef8742373f95 | -11.2845 | -47.5558 | 2025-10-29 14:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f551d0ac-41ae-3df9-ad53-aa8449a5afb8 | -13.7255 | -51.4621 | 2025-10-29 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 13282a2e-c4b5-31e1-9e9d-fc831b583280 | -13.2478 | -47.9991 | 2025-10-29 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 221b6da4-482b-3ff4-9fad-d307cffb5e4c | -3.7075 | -41.556 | 2025-10-29 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 155.0 |
| 463c5d9f-3374-375f-ae00-bab6098c7f0b | -7.7844 | -46.4921 | 2025-10-29 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| d15a4e95-ec61-3e03-889e-6d29f5e9ee32 | -9.1606 | -46.3326 | 2025-10-29 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| fa681293-5954-30ee-bb37-a56574a329bf | -7.2943 | -44.9817 | 2025-10-29 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 71a3be50-a4f5-34d1-9aa4-e2a35f8d7db1 | -10.9224 | -47.6009 | 2025-10-29 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 869134d9-9302-3dfd-bad8-46496f208b9e | -7.0693 | -44.9563 | 2025-10-29 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| cc9762ec-30a4-34b6-a622-b8cd574f880d | -7.5928 | -43.5699 | 2025-10-29 14:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 0e0dd12a-75b7-373c-af55-78745f233c91 | -7.3054 | -45.6833 | 2025-10-29 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 22ec3e68-ccb5-3727-84bd-76c50ebddf28 | -6.1464 | -41.5755 | 2025-10-29 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| a1933c11-41cb-3242-9b9b-af3417da3654 | -10.7892 | -47.617 | 2025-10-29 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| abb9d41c-776d-3f7c-a3a4-9480094c323c | -6.6414 | -44.6051 | 2025-10-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 1e810c03-0e84-36d6-be05-1ca34fd3578c | -10.2068 | -45.9639 | 2025-10-29 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8a37292a-7736-3a2b-841b-aca00c5ed988 | -7.3232 | -42.4675 | 2025-10-29 14:40:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 128.4 |
| 7ad133f1-99dd-3ea4-9797-b18a03391d96 | -9.5109 | -46.9649 | 2025-10-29 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 59c99d63-1b62-3741-a5aa-e7d80cb67bd8 | -10.2261 | -45.9389 | 2025-10-29 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 332.2 |
| 4640eccd-84af-30dc-af8a-c096e480bdd5 | -10.6506 | -48.009 | 2025-10-29 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| b3b36edd-cdce-3c3b-b229-b79bc690ebdc | -9.9004 | -44.8839 | 2025-10-29 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |


