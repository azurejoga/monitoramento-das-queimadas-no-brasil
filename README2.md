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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 485cd36b-1508-3702-8a30-0cde5d8e22ee | -6.1979 | -48.0482 | 2025-06-25 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| b4669c55-42b6-36fe-8b9c-e45fba44ee47 | -6.1789 | -48.0929 | 2025-06-25 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 962f2d4c-1bde-3e8a-8cfd-88eef2be1227 | -6.1604 | -48.0724 | 2025-06-25 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 31f47bad-1263-311c-85c2-0aabdfe4a70f | -13.0408 | -48.825 | 2025-06-25 00:40:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 29da8750-c644-3611-9122-db0ce80c3146 | -6.1791 | -48.0712 | 2025-06-25 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 377.5 |
| 5386ec63-f67d-3c50-b18b-e25ea1b4ffc1 | -7.0174 | -44.5495 | 2025-06-25 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 7c280212-08d0-3648-a07c-f2ce080ff7fe | -7.0171 | -44.5725 | 2025-06-25 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 47d56dc5-3deb-33c5-9a23-80eb71fe3641 | -7.2028 | -43.0936 | 2025-06-25 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 221.0 |
| 37a47105-5843-3bef-b358-7bdccd9fd97c | -6.1977 | -48.0699 | 2025-06-25 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 37282dce-24cd-3988-9463-0c1f60aea841 | -7.0359 | -44.5708 | 2025-06-25 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 19df5b2e-9b8d-35e1-adfd-3328c7c27698 | -3.618 | -47.5352 | 2025-06-25 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| caee09fc-eb3b-3ba4-a36f-597f13fef884 | -6.1792 | -48.0494 | 2025-06-25 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 231.2 |
| 8a77243e-5497-3928-9738-a0c9344cc5d0 | -11.94821 | -47.02626 | 2025-06-25 00:41:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| beeb1fe7-eff0-3cfa-a3be-f5e9c366b49a | -12.5139 | -47.43904 | 2025-06-25 00:41:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7abcac7f-00e6-3106-95f3-2aea5ca98363 | -6.17696 | -48.05853 | 2025-06-25 00:41:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 294.6 |
| 28fb7781-986f-352f-a3bc-f207e1d22648 | -12.80445 | -48.73634 | 2025-06-25 00:41:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 52392fda-471c-30ea-b407-725216fa9522 | -11.18595 | -48.61538 | 2025-06-25 00:41:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a3e001b0-b6d3-3ded-b3a3-4b0c62c53d57 | -11.10402 | -44.52154 | 2025-06-25 00:41:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 74c7c060-8382-3c84-8b63-37128bf4d112 | -7.01273 | -44.55721 | 2025-06-25 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 81686b06-3d77-300d-bcae-ec4ac2598038 | -10.30483 | -57.13354 | 2025-06-25 00:41:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 9b9aa3cc-fea1-340b-9037-e8a1d508850d | -9.56944 | -49.11343 | 2025-06-25 00:41:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 80df583c-57be-3471-9ed6-a339ef185348 | -7.21253 | -43.10921 | 2025-06-25 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 1c6f29c8-7a7e-362c-bcfd-62de9cd2ad41 | -8.86679 | -47.27112 | 2025-06-25 00:41:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5a5bf9e2-b695-3dc5-967c-bdc3abbb245f | -7.19767 | -43.08538 | 2025-06-25 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 0b5056b6-5184-3396-8e8f-cb72fb784530 | -7.30608 | -45.77219 | 2025-06-25 00:41:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 460864b3-ecd8-3288-99ea-d13b5c835f3f | -6.18602 | -48.06086 | 2025-06-25 00:41:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 026f5cf5-fa45-333f-a39d-4d692060fff2 | -5.91731 | -43.47603 | 2025-06-25 00:41:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| dfcc4927-9f41-35b8-a816-6812b7c4d332 | -11.09026 | -46.95694 | 2025-06-25 00:41:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4b6b00c1-9738-3683-ae55-4fcd664a2252 | -7.21328 | -43.10257 | 2025-06-25 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 98cde011-2b37-325b-ada4-85c0a3797666 | -10.8331 | -54.00829 | 2025-06-25 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1979269e-f153-3459-9cd7-df20aaaa0e77 | -9.81704 | -48.38704 | 2025-06-25 00:41:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 47638fb1-1387-36e4-9646-b504975ae32e | -6.95717 | -42.81271 | 2025-06-25 00:41:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 1c746d8a-65b3-3e22-ad2d-cef9f5b8133c | -6.22947 | -43.36486 | 2025-06-25 00:41:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 1a9ce06c-db1a-36d8-9a51-15d3f0e4b3d5 | -6.95591 | -42.79862 | 2025-06-25 00:41:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 042b9ea4-c882-3fdb-9585-c0c2a2ed705d | -11.59032 | -44.64101 | 2025-06-25 00:41:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1a25899b-c1ca-39d2-a11a-085634977185 | -7.19994 | -43.11115 | 2025-06-25 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| 68a6b153-b310-36dc-b359-149636f39b33 | -11.78034 | -47.4017 | 2025-06-25 00:41:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 758cc9b3-6ca0-3989-8493-6078bee5a6f5 | -5.76358 | -43.40814 | 2025-06-25 00:41:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| d19c8f9e-3f40-3092-83aa-ae8c7de5debe | -11.93383 | -47.8374 | 2025-06-25 00:41:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 890ad29d-19d0-3782-9f2d-28609463cf90 | -11.58379 | -44.64796 | 2025-06-25 00:41:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 393848c1-ce1f-39e9-86bf-8e40ec022c6d | -7.70019 | -49.32797 | 2025-06-25 00:41:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0bef80d3-7af9-353f-be8d-5fca22260cc0 | -7.02624 | -44.57077 | 2025-06-25 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 404002bd-d8ed-3c96-8f0d-9bf6eccd3b5f | -10.59299 | -49.46566 | 2025-06-25 00:41:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2c5271c6-27e4-3c70-b6c0-c5890d46df91 | -8.71102 | -47.85867 | 2025-06-25 00:41:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf38735d-920e-3520-98ec-b47a985602b1 | -5.35851 | -45.11764 | 2025-06-25 00:41:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e018c52d-68d4-39a7-90ce-eab707d108fe | -9.57067 | -49.12234 | 2025-06-25 00:41:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4d234cf6-668c-3d98-864a-534095e6d609 | -11.57211 | -47.42629 | 2025-06-25 00:41:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8661f00b-38d6-374f-95c3-cc9d71db0d0c | -8.72 | -47.85736 | 2025-06-25 00:41:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fcdceb91-028f-3c83-9604-890b2397042f | -7.09722 | -49.16198 | 2025-06-25 00:41:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 58983933-b894-38c4-8b69-bc382d5e3e24 | -7.02393 | -44.55525 | 2025-06-25 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9e24595c-dccf-3392-8c28-d118ce57d211 | -6.21595 | -43.37263 | 2025-06-25 00:41:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 388e111d-3455-3fe9-9ac8-b0d8aba7cae3 | -6.2966 | -44.23583 | 2025-06-25 00:41:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| fb2ac611-e5c7-360e-a023-f189585c0e13 | -9.8082 | -48.38833 | 2025-06-25 00:41:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42c6470d-8eaa-3b5f-8e0b-af0c732d2e21 | -11.9422 | -48.42901 | 2025-06-25 00:41:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 44fd7139-a1f0-3099-8779-5258b0d54c7c | -10.94949 | -47.39309 | 2025-06-25 00:41:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 19ba6d89-2306-3962-8b7b-1ef8e6a29f29 | -8.47498 | -50.27476 | 2025-06-25 00:41:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 38ef3199-4137-3f3f-b9dd-559838e1b93b | -5.07388 | -43.72362 | 2025-06-25 00:41:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6a3a1e9d-4c45-3bfc-82e5-7a5625a67cb6 | -7.27948 | -47.06709 | 2025-06-25 00:41:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1367dba6-e1c3-3044-84f0-6467e7ead636 | -11.12019 | -46.97552 | 2025-06-25 00:41:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 64ff8d23-22fe-38f5-bac9-92cf21a03ce6 | -8.05502 | -43.10818 | 2025-06-25 00:41:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 6042df26-d9d7-3bd3-809c-4588bfafa251 | -5.82548 | -46.36336 | 2025-06-25 00:41:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c4fa01bc-05b3-3008-930d-c310850e6913 | -11.61339 | -46.49805 | 2025-06-25 00:41:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d6c305ce-c4f3-3e47-a042-756c66ba794a | -8.9813 | -49.86867 | 2025-06-25 00:41:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b9659d51-1458-3786-aa6c-d8dfec4c12cc | -11.58921 | -47.61076 | 2025-06-25 00:41:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3259da83-ef09-3e13-ac60-a633d2785863 | -10.00354 | -48.13106 | 2025-06-25 00:41:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 86c02108-42da-34c3-9971-2d014032a62a | -10.79815 | -48.54123 | 2025-06-25 00:41:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7da4d7af-9bfe-3755-bd02-d11fd4ecf324 | -6.29894 | -44.25122 | 2025-06-25 00:41:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 01d95913-a9c5-3c17-9ada-be1e766ef92b | -9.81829 | -48.396 | 2025-06-25 00:41:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 19f98373-5103-3298-aa8c-3684be47fc7b | -6.28499 | -44.23796 | 2025-06-25 00:41:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 73178001-080d-3deb-9793-1c4b203ae3a1 | -7.18812 | -43.10649 | 2025-06-25 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 3c83e97a-55bf-326a-95f3-c5b88e9a6135 | -10.8488 | -42.23777 | 2025-06-25 00:41:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| e1109f17-e35c-36b2-b66f-c4f688858f00 | -7.19706 | -43.09201 | 2025-06-25 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 191.3 |
| 23b2e14e-5eb9-3288-bac3-8451fe1748cc | -10.30639 | -57.13882 | 2025-06-25 00:41:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| e2a85847-96b3-363f-8056-3ba6f0e7b44d | -9.87826 | -49.56046 | 2025-06-25 00:41:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 78b7e33e-9f70-3919-96e6-d081246aa5db | -11.61482 | -46.50782 | 2025-06-25 00:41:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 92b677f3-cbf2-3e96-8b57-e2efc19848f9 | -8.42343 | -48.3061 | 2025-06-25 00:41:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a0fa6562-44f4-3a62-9b46-e2cac26fe841 | -10.6019 | -49.46441 | 2025-06-25 00:41:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| f5f43c41-890a-3b0b-8bca-04c1727187a0 | -7.09969 | -49.17966 | 2025-06-25 00:41:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a158cc5e-b013-35b7-a9ea-fff6199d0928 | -7.88498 | -47.88394 | 2025-06-25 00:41:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2fb5ce15-da2b-3049-b319-da4bb784d739 | -9.51687 | -56.12307 | 2025-06-25 00:41:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 5ad1039a-cca4-300e-b28c-b12a7fd6aa39 | -5.73663 | -43.49639 | 2025-06-25 00:41:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b07bf2c0-7978-3acf-a78b-68a80cf87230 | -6.2285 | -43.37076 | 2025-06-25 00:41:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 473bc35f-ac4a-35b0-bcf6-9cd0a11aedec | -10.79938 | -48.55016 | 2025-06-25 00:41:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ebe82c2-6fb3-3a7d-8fd7-7730103087af | -6.34574 | -43.79362 | 2025-06-25 00:41:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 72a9fe32-c959-3383-adc2-bc5472d5eaec | -7.43664 | -48.10248 | 2025-06-25 00:41:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| aaea5005-8767-3a49-baa8-e60b04a25bec | -6.18737 | -48.0703 | 2025-06-25 00:41:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 1261f10f-3c91-355c-9347-1da45c78a530 | -12.51261 | -47.42991 | 2025-06-25 00:41:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 28b0efd4-f76e-30ce-ba68-c4e55f23a7c8 | -11.58001 | -44.64267 | 2025-06-25 00:41:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 98975333-ba3f-37b9-8906-8a6fc5328db8 | -9.26234 | -47.64985 | 2025-06-25 00:41:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8e15cd51-9ab3-3068-a799-02f14fa24648 | -11.57342 | -47.4355 | 2025-06-25 00:41:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 658c7c00-a311-3a1c-acfd-30140ad3dbd4 | -7.01496 | -44.57209 | 2025-06-25 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 5e9ce41a-67fc-3781-b9b5-b0c34e8893c6 | -7.09845 | -49.17082 | 2025-06-25 00:41:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ec560100-2f98-3575-842b-e551c0ad08b8 | -5.76006 | -43.39555 | 2025-06-25 00:41:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 4e7995a5-b678-3727-8797-5a69cdd192c1 | -10.7229 | -48.85913 | 2025-06-25 00:41:00 | TERRA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2ca36656-ca15-3510-ad58-843fde4a05bd | -10.82552 | -54.04346 | 2025-06-25 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 903e762a-86c7-33db-8040-c39cb35b8643 | -10.60711 | -52.83831 | 2025-06-25 00:41:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 04c6e7c6-d00f-362c-b7f8-286dff9a5656 | -6.21691 | -43.3667 | 2025-06-25 00:41:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| b9d3e114-5c94-3c67-8aaf-030f4f7db031 | -10.87242 | -53.78224 | 2025-06-25 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b7c74767-926f-35ad-bf40-6bd320238cec | -11.11882 | -46.966 | 2025-06-25 00:41:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 59c19f39-f1a0-3870-911d-ce1ec83a40ff | -5.76057 | -43.38893 | 2025-06-25 00:41:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |


[Clique aqui para ver as próximas entradas](README3.md)
