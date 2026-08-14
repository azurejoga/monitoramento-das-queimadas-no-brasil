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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b043767-1235-3290-96e3-326d38e0dc9b | -10.7099 | -50.5145 | 2026-08-14 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f674ce99-183a-3dee-ab6c-76d57ca8e199 | -11.4681 | -44.5558 | 2026-08-14 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 2e3a87e9-b643-3bc3-9a58-ad8610d4fde5 | -2.52884 | -57.88984 | 2026-08-14 12:34:00 | TERRA_M-T | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d1716d35-a122-3340-a84a-469503415cdd | -2.5301 | -57.88107 | 2026-08-14 12:34:00 | TERRA_M-T | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 4ff986bc-f315-3b8c-a1d5-f5c78a033310 | -11.4873 | -44.553 | 2026-08-14 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 26363c7a-e514-3724-bb5a-596ec509b7c2 | -11.4677 | -44.5791 | 2026-08-14 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 8db1010c-564e-344b-a0e6-a7c7f75dc091 | -11.4869 | -44.5763 | 2026-08-14 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| a83c1500-d5af-3e35-b08f-2b4306317159 | -10.7099 | -50.5145 | 2026-08-14 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 57bf4645-bb02-378c-9105-ce08b27b6864 | -11.4681 | -44.5558 | 2026-08-14 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 148b5215-dd14-3736-aca6-b8ed42e57a5f | -10.7099 | -50.5145 | 2026-08-14 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 811fcc48-d707-3558-ab76-f1b5b750c9fd | -14.0939 | -53.6321 | 2026-08-14 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 2440a282-fa97-3c36-82bc-b4b2ee6e5cfa | -11.4681 | -44.5558 | 2026-08-14 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 166a62d8-0a08-3d11-8c73-3bc00717a72d | -11.4869 | -44.5763 | 2026-08-14 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 13b6b8e8-2f38-3b17-bdcd-9639b9dd84e5 | -11.4873 | -44.553 | 2026-08-14 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| b19ee962-2bab-3d03-bc9e-a9450cb70e68 | -11.4677 | -44.5791 | 2026-08-14 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 84023549-4004-3850-a04b-3fc386b7dfe0 | -14.0936 | -53.653 | 2026-08-14 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 46871d97-441e-3f82-8455-497fc351dbd5 | -11.4677 | -44.5791 | 2026-08-14 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 3a67da5b-d686-3b98-aa5b-22dd5af2a0d7 | -11.4681 | -44.5558 | 2026-08-14 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 392daf1c-cf35-3f52-92f3-5ec734432fd9 | -11.4873 | -44.553 | 2026-08-14 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 3a0df735-b5b5-3c5f-9793-f7155be22f48 | -14.0939 | -53.6321 | 2026-08-14 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 156.4 |
| c1f8e976-8082-3d4a-bd26-4fefe84bf9e2 | -13.2798 | -54.2435 | 2026-08-14 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 766601d3-9468-3bba-a0a0-86bcd93498da | -11.4869 | -44.5763 | 2026-08-14 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 1199a09b-09a7-33a8-b6b5-ff14736b7ae8 | -11.7128 | -47.0088 | 2026-08-14 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3822ea08-09b3-3833-82bd-a22b891ad3ee | -10.7099 | -50.5145 | 2026-08-14 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e37f25fa-2868-3204-8c73-0ccc30201c57 | -13.2801 | -54.2228 | 2026-08-14 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 72ef93e9-f6f5-3dba-9e4e-db3d221e8512 | -12.029 | -46.4017 | 2026-08-14 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 46304e76-fdeb-3d52-9392-ab3f944167a0 | -10.7099 | -50.5145 | 2026-08-14 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 86fb6c4b-2647-3d3b-9448-d60f17b74768 | -11.4869 | -44.5763 | 2026-08-14 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 82a1c160-80bb-309e-839a-7189696fb93f | -9.9896 | -53.9404 | 2026-08-14 13:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| da578f7f-5e49-3b13-94f0-2b85e11efad3 | -12.0099 | -46.4044 | 2026-08-14 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| faa4565d-844c-3d0e-8e64-3b8bdc711f46 | -11.4677 | -44.5791 | 2026-08-14 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 7e8d7fa1-f5cf-374f-aacc-87583852296d | -11.4873 | -44.553 | 2026-08-14 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 80e64fcf-4b38-32d5-9c54-3a56a528e3d5 | -9.9894 | -53.9608 | 2026-08-14 13:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 56a2de8f-a571-3958-920b-82018c7b6d86 | -11.9737 | -47.3986 | 2026-08-14 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 6e9e47dc-4770-300e-adf0-06f0e1f48849 | -11.7128 | -47.0088 | 2026-08-14 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| ff7c7029-f2f8-3997-9b76-9da700bb2c44 | -9.9894 | -53.9608 | 2026-08-14 13:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 1b4f4ac7-0760-388a-85d6-3412f6bed9f2 | -14.0939 | -53.6321 | 2026-08-14 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| bf290d06-e3c9-3725-aff9-c32ace56456a | -11.4869 | -44.5763 | 2026-08-14 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 53e89aa7-2ae2-3ee6-a9c2-cac143c7952d | -6.9685 | -59.2976 | 2026-08-14 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 17d4f5f8-2516-3fdd-8bed-97d1cd37e15f | -11.4873 | -44.553 | 2026-08-14 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 59cf379b-fd89-3cce-8ee4-b940dba068aa | -10.7099 | -50.5145 | 2026-08-14 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| bb9577d1-898e-3399-9ad1-fa89eee12508 | -9.9896 | -53.9404 | 2026-08-14 13:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 633347ea-4166-3751-928b-9b7d61491378 | -11.4677 | -44.5791 | 2026-08-14 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 205.4 |
| b86acfd0-597f-3a3f-8783-4b292e8bc2d4 | -13.8227 | -53.7889 | 2026-08-14 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a96353f9-c7be-3322-a61a-175972b2b13b | -6.9686 | -59.2783 | 2026-08-14 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 1905862f-eecd-3e84-9441-8054b38543f9 | -9.9706 | -53.9624 | 2026-08-14 13:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| f826a879-3852-365e-b219-0540fa8009ac | -10.7099 | -50.5145 | 2026-08-14 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 8db70f25-b764-3dff-947f-6bb860ad7b22 | -11.4873 | -44.553 | 2026-08-14 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 786c5a4f-e2f3-3a84-92ac-c28e7e0a8bac | -9.9894 | -53.9608 | 2026-08-14 13:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 86c43272-49d0-317f-b0f9-efeaee5bde06 | -11.4869 | -44.5763 | 2026-08-14 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 5867711a-be0c-3ae4-b058-84a514bebbb2 | -11.0635 | -50.9452 | 2026-08-14 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 31ddfcef-b5cf-3d16-96e0-5e120b43e97c | -6.9685 | -59.2976 | 2026-08-14 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 85ac6234-03b0-3f76-b8e9-f7880ce69a7e | -6.95 | -59.2984 | 2026-08-14 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 72921a56-0710-361a-88b0-e8b40452d6ac | -6.9686 | -59.2783 | 2026-08-14 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 6a689784-0868-345e-9a8e-728a1a01862b | -11.4677 | -44.5791 | 2026-08-14 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 96f9f72b-9048-3bae-8995-f1dc4a7d6c1c | -6.2571 | -47.6738 | 2026-08-14 13:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 95f504df-ace0-393f-90e0-a5f997ad9102 | -10.7099 | -50.5145 | 2026-08-14 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 78c660cd-55f0-3f5c-948e-664e1a364433 | -6.95 | -59.2984 | 2026-08-14 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 1b67faa1-6185-38a3-be77-3df09f8e98f5 | -6.7871 | -58.764 | 2026-08-14 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 56c214dd-201f-31da-acc2-9277f5942af9 | -9.9894 | -53.9608 | 2026-08-14 13:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 45846a4c-695d-34b0-bfcc-abc3b55fb873 | -11.4869 | -44.5763 | 2026-08-14 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 3f6ec5fa-c365-3725-b15a-12ec37af5442 | -11.0635 | -50.9452 | 2026-08-14 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| de2920d0-568f-37a5-bf11-ab468bc79f65 | -9.9896 | -53.9404 | 2026-08-14 13:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 2067f085-c1e7-3002-a579-39345b3d4864 | -13.2804 | -54.2021 | 2026-08-14 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| ddd3cd60-a999-3dc8-9c93-84a059ce0086 | -14.0939 | -53.6321 | 2026-08-14 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 957825cd-0f2e-310a-9540-6fa6fa758f7f | -6.9686 | -59.2783 | 2026-08-14 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| fcd7c880-1a83-3ef8-a2d6-95cf71762ea6 | -11.4677 | -44.5791 | 2026-08-14 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 8f8553d9-b4b0-391e-8a54-1f95d07e6b67 | -11.9369 | -47.3143 | 2026-08-14 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 8443772f-d32b-3664-9024-bea3c06eb3b0 | -11.4873 | -44.553 | 2026-08-14 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| d44b21bb-2937-38cb-94f0-26801390de05 | -6.9685 | -59.2976 | 2026-08-14 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 91b1933f-ef98-3548-a905-43cd692615b9 | -6.9502 | -59.2791 | 2026-08-14 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 68903959-a8c4-3750-8026-8cd5c2d162d0 | -10.6909 | -50.5165 | 2026-08-14 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4aeb86e5-efdc-3477-8fb3-d7a5895b4562 | -9.9894 | -53.9608 | 2026-08-14 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 7b7c95d4-dce4-3e1d-8b8b-45cb4ffeefea | -9.9706 | -53.9624 | 2026-08-14 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 53d85ec3-d8a9-3e83-83d1-67fbb3270dad | -6.9685 | -59.2976 | 2026-08-14 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 56948085-63fb-390d-9739-60090c61334d | -6.95 | -59.2984 | 2026-08-14 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 5e8ab79c-5011-36ec-a5ec-dfce0bfc98ae | -11.4677 | -44.5791 | 2026-08-14 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 93365990-5cd4-33a1-b5fb-b7b111a97785 | -13.2804 | -54.2021 | 2026-08-14 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 4779bb06-4bd6-3c82-9416-58eef0f83f56 | -13.8227 | -53.7889 | 2026-08-14 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 600ecba9-b9e1-3f1e-8b9c-d776778377f9 | -14.2945 | -51.9635 | 2026-08-14 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 9494dfe2-c567-3182-8e3b-45567a0ed2e3 | -11.4873 | -44.553 | 2026-08-14 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c43ce792-b8ab-3d16-ba1c-041d11f40304 | -9.9896 | -53.9404 | 2026-08-14 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 27a418d4-a1ce-3663-8c08-3fc6559dddda | -11.9369 | -47.3143 | 2026-08-14 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 610dcb92-4e8d-3fde-aee6-7a4c7859023f | -10.7099 | -50.5145 | 2026-08-14 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 2c9eae88-d637-3ed9-97db-2d9d7d97cd6e | -9.9708 | -53.9419 | 2026-08-14 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 333893b3-c66a-3488-87a2-b8a332a78451 | -6.9686 | -59.2783 | 2026-08-14 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 60ec8482-fd92-3353-a58a-a448fdca1ab9 | -11.9737 | -47.3986 | 2026-08-14 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 21ce133e-e9a4-312d-9dec-a4728e226c3d | -11.9741 | -47.3762 | 2026-08-14 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 60bb860b-a584-3c43-b3f5-a87e3903e931 | -11.956 | -47.3117 | 2026-08-14 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| a666621d-8365-3087-aa41-bb6aa0422b2a | -6.7871 | -58.764 | 2026-08-14 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8ef10d5b-9cfc-364d-a327-6ef583a9244b | -11.0635 | -50.9452 | 2026-08-14 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 215.3 |
| 4b04d88a-cc00-3efa-b4d0-df9ec99707ef | -13.8227 | -53.7889 | 2026-08-14 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 76fb5c18-ad22-354a-b6ba-80bc7732f3b4 | -6.9686 | -59.2783 | 2026-08-14 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.6 |
| a98c6614-9bca-32d9-9537-f969f1378ee4 | -6.9502 | -59.2791 | 2026-08-14 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 3f16be7e-65fc-3d53-ad4c-7426e4bf1b8c | -6.7871 | -58.764 | 2026-08-14 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 008686aa-f426-3e52-ac4b-1dba04a1b8d6 | -14.2945 | -51.9635 | 2026-08-14 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 956f575a-8e2f-35ac-b7d5-6c7b90f5801d | -6.95 | -59.2984 | 2026-08-14 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 181.7 |
| d1cc3dd6-4df3-34bd-9475-5ea1a36a0778 | -11.956 | -47.3117 | 2026-08-14 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 6cca2893-1324-3ec7-8b70-6554fb502bf7 | -9.9706 | -53.9624 | 2026-08-14 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 0b7aced8-1b87-33ae-b182-4b00e616d4d6 | -11.7128 | -47.0088 | 2026-08-14 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |


[Clique aqui para ver as próximas entradas](README39.md)
