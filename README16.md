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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31757311-8518-3de5-9ba6-6745c3d031fe | -12.38061 | -63.86917 | 2024-10-25 02:04:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 73d8a298-a94e-345e-aed5-1a8af0ebb66a | -12.37929 | -63.85996 | 2024-10-25 02:04:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 925c49c4-d640-3e71-8044-b4e6ad8c8a36 | -12.37035 | -63.86131 | 2024-10-25 02:04:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ca933801-2807-333d-ac5e-b568e2f1f7c4 | -12.05556 | -63.14668 | 2024-10-25 02:04:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a04c4247-2b90-360e-a1d6-f5976eb85714 | -12.05416 | -63.13696 | 2024-10-25 02:04:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 28004c5d-fb8a-35f9-9ede-177f29be7000 | -12.04639 | -63.1481 | 2024-10-25 02:04:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 29.6 |
| e6b5dc7e-d6e2-319d-8b72-7a1831b97ace | -12.04499 | -63.13838 | 2024-10-25 02:04:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f84561c3-7936-38f1-9d4f-c7cca2556cef | -12.008 | -63.52192 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a401d171-0ee6-3c38-810e-0b35899a170c | -12.00665 | -63.5125 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bfde5694-1972-3b72-a2b3-59fdc3635808 | -11.99993 | -63.91362 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 97edd48b-8ba1-393c-89db-38baa7a26ce0 | -11.9986 | -63.9044 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 7b88eefb-c3c0-3aa8-b2fe-d607b31de497 | -11.99098 | -63.91497 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d61ae04a-638c-307b-8821-fe3bfc75a47b | -11.98966 | -63.90575 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 6133d665-ce3a-38b9-8dde-b7be2c003dc9 | -11.98833 | -63.89654 | 2024-10-25 02:04:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| be348855-e75d-3871-8f67-5dd442a1095b | -11.98508 | -63.17748 | 2024-10-25 02:04:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fc8987bf-b510-3fb1-9479-b0c82207521d | -11.86343 | -63.2874 | 2024-10-25 02:04:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 05831cbd-08b4-371a-9110-ed4a9eee7d1b | -1.0445 | -47.6237 | 2024-10-25 02:05:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 906b52e9-6b9b-3d88-bbcc-f6011543aceb | -1.0446 | -47.602 | 2024-10-25 02:05:11 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 34639047-f737-3491-86e0-26f5131369be | -1.1925 | -47.6002 | 2024-10-25 02:05:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 847421eb-5427-3761-ad90-df64f2e7edd6 | -1.211 | -47.5999 | 2024-10-25 02:05:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 5417f254-0b18-3d53-a944-003885a6bf15 | -1.9669 | -56.4493 | 2024-10-25 02:05:16 | GOES-16 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 9fd6ec1f-7c1a-3d52-ae54-e6c3836133b0 | -2.6297 | -49.247 | 2024-10-25 02:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| c2bed5e4-4b9f-3aed-bbb5-011ed392c51a | -2.796 | -49.2424 | 2024-10-25 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 61d69b47-0c5e-3dbc-bb69-e9f49fb0a0b0 | -2.8144 | -49.2631 | 2024-10-25 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 72b461d3-05c0-3076-be59-344f6d7a712f | -2.8145 | -49.2418 | 2024-10-25 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 7efb48ba-ae4b-3264-938e-51cf7bdeeb96 | -2.9578 | -50.4198 | 2024-10-25 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c80678e9-71e1-3d7f-8ef2-e8965b7f3c26 | -3.1949 | -46.807 | 2024-10-25 02:05:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ec6e2e5c-a5d0-3f9f-9369-e6b67b98d2e9 | -3.2135 | -46.8063 | 2024-10-25 02:05:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 037611e1-f603-3567-bd00-eee3b8721233 | -3.2136 | -46.7843 | 2024-10-25 02:05:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9ea961ad-f636-3ba5-bc01-3ed0bb6ed348 | -3.9581 | -46.422 | 2024-10-25 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 1079e905-e6b7-365b-adaf-4253669aa221 | -4.2429 | -48.5474 | 2024-10-25 02:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 4ac0bf7e-4935-39da-b8ae-004bd7f1a111 | -4.5231 | -48.2108 | 2024-10-25 02:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| fb4c2ff9-a5cd-3804-90f9-35f147be5fe0 | -4.58 | -48.0132 | 2024-10-25 02:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 8f536d4a-7fbe-3680-abbe-ce43e9f4effa | -5.9786 | -45.3847 | 2024-10-25 02:05:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 6831ffb1-3d80-33af-9ae1-6c00c2070538 | -5.9788 | -45.3621 | 2024-10-25 02:05:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| c1bfcb8d-c50b-348f-becd-0da54c595cc3 | -6.5219 | -60.0457 | 2024-10-25 02:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 9921f630-1adc-3e8d-b861-2d99f3189263 | -6.522 | -60.0266 | 2024-10-25 02:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ee19cad2-12f2-337a-8b59-d3b6648f6ff4 | -8.52031 | -64.01829 | 2024-10-25 02:06:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2da10870-d411-3a42-a071-90a01dcc5ae9 | -8.47869 | -66.14356 | 2024-10-25 02:06:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e34b7124-57fc-3a91-8556-486d93549dc2 | -7.49863 | -63.63821 | 2024-10-25 02:06:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 191a6840-c73f-34f2-9672-2fb178165e1f | -7.27631 | -64.66653 | 2024-10-25 02:06:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f5c24860-23ca-3196-af48-3708ba97c56e | -7.275 | -64.65729 | 2024-10-25 02:06:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 6e4cc97c-9f8a-34ac-97fc-140b4ce5a7c1 | -7.2737 | -64.64803 | 2024-10-25 02:06:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9bb13d58-4f01-31f7-83d5-20093a093bb7 | -6.52949 | -62.94714 | 2024-10-25 02:06:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8a125354-8a11-3c82-8494-e1badb6ea212 | -6.52686 | -60.04835 | 2024-10-25 02:06:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a28e572e-0eed-30d8-b076-ace17d916942 | -6.52451 | -60.05429 | 2024-10-25 02:06:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 00306068-eb6f-382c-922f-f62d16808d42 | -6.52394 | -60.02979 | 2024-10-25 02:06:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1d0def4d-2a75-3180-a19c-bd3b56492b77 | -6.52174 | -60.03576 | 2024-10-25 02:06:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| b9b3258c-9d87-3d99-baa9-ae0da4427de9 | -4.52262 | -61.13813 | 2024-10-25 02:06:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 64602882-9100-3b9a-a1ad-f62494235f14 | -0.77428 | -62.88645 | 2024-10-25 02:06:00 | TERRA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2d545221-53ac-3d7b-b4e8-f3bb7a62f3f0 | -11.9822 | -63.9213 | 2024-10-25 02:06:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a1e4987e-c2d7-394b-a958-92ec9f5be8c8 | -11.9824 | -63.9022 | 2024-10-25 02:06:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 239de169-d4bb-35fa-82cb-f4d15894f7e0 | -12.0011 | -63.9203 | 2024-10-25 02:06:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.1 |
| f34188c8-f72f-3cf5-a625-a50fa315c42b | -12.0012 | -63.9013 | 2024-10-25 02:06:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 145.1 |
| e247718b-0aba-3e1d-a40b-f9ba93093e8e | -12.0013 | -63.8822 | 2024-10-25 02:06:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 46500004-83c4-37ba-a166-23042b7c4cde | -12.0444 | -63.1547 | 2024-10-25 02:06:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fce54a74-624d-3c61-a664-4323fdf0de73 | -12.0445 | -63.1356 | 2024-10-25 02:06:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2d20225c-9631-3529-badd-6017ffcb2ad0 | -12.0632 | -63.1537 | 2024-10-25 02:06:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 51ebf6a2-4c3c-3cdf-ba1c-c1839fb0f736 | -12.0634 | -63.1346 | 2024-10-25 02:06:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 98ec0c01-cac2-3b57-b9d0-31430e93a8a7 | -12.3782 | -63.8821 | 2024-10-25 02:06:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 9d97d077-8dbd-32f2-9cb7-052ac1a343c2 | -12.4589 | -63.1895 | 2024-10-25 02:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e10b57a4-a5a6-3520-9769-eeaee881c99a | -12.4591 | -63.1704 | 2024-10-25 02:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| affba4be-a274-3702-9542-384b3726b3e6 | -12.478 | -63.1693 | 2024-10-25 02:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 294209ee-9e45-3699-afea-f4f4e14e771d | -12.5356 | -63.051 | 2024-10-25 02:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| be43a3ff-0ee7-3223-9993-50b69f055bf2 | -16.94 | -57.5268 | 2024-10-25 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 9116004e-e20f-368c-8fec-891f88b28a88 | -16.9596 | -57.5245 | 2024-10-25 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.5 |
| d5763a15-1eb9-3e0f-a4fc-bb5434f976f5 | -16.9792 | -57.5223 | 2024-10-25 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.9 |
| 413cb29e-37c9-391f-8f1d-ec6b25611531 | -17.0184 | -57.5178 | 2024-10-25 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| e608625c-1c6c-3e47-94b2-ca65ee3ef271 | -17.0381 | -57.5155 | 2024-10-25 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 7798dcef-7243-3e20-9835-52059afb8dbc | -17.039 | -57.454 | 2024-10-25 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 6015dbc9-df4b-34e7-b4aa-d9df81fb8d82 | -17.0583 | -57.4722 | 2024-10-25 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 865c410d-c80e-33f2-a30c-c59eabf3f744 | -17.0586 | -57.4517 | 2024-10-25 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 2e7aab93-2de3-3394-8a9f-153d2b6f86e7 | -17.0786 | -57.429 | 2024-10-25 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 5448760b-e7fd-35e4-a42b-a78b8ad33ff8 | -17.0789 | -57.4085 | 2024-10-25 02:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 781d363f-f36f-3343-b6de-f673aa518ed1 | -17.2537 | -57.5108 | 2024-10-25 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 197bfb35-0c24-30aa-bf49-eb1195f656f1 | -17.8239 | -57.5043 | 2024-10-25 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 92064d8b-3025-36ab-b52c-c6ca5f835831 | -17.8042 | -57.5067 | 2024-10-25 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| e024d1c1-8496-319d-bad4-177056e2cb9b | -17.8038 | -57.5273 | 2024-10-25 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 4ecb0085-a080-3ca2-9203-87fd784b80a7 | -17.7671 | -57.3673 | 2024-10-25 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| f9d0f113-9405-320b-a2dd-1ee4a4b56d95 | -17.7453 | -57.4933 | 2024-10-25 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 5acfcecf-21cc-345d-a9d6-3299275fc3b8 | -17.9268 | -57.2447 | 2024-10-25 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 8b33a1bc-40f2-3910-8281-114acfd03f31 | -17.9272 | -57.224 | 2024-10-25 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 23a4f1c0-478b-376e-baa8-fff3b4ff9937 | -17.9473 | -57.2009 | 2024-10-25 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 917b8fa0-f655-3228-9b5d-589d689749ac | -18.0254 | -57.253 | 2024-10-25 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| a86da18b-e946-3740-ab22-26d74b7123e8 | -18.0434 | -57.3539 | 2024-10-25 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| 986bda27-9b3a-3089-9431-51ee09be539d | -18.0441 | -57.3126 | 2024-10-25 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.0 |
| ef342833-c9d8-39ea-8ca4-c560c3288009 | -18.0639 | -57.3101 | 2024-10-25 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 3d6ae591-971f-3a1c-91da-05de777eb970 | -18.0844 | -57.2663 | 2024-10-25 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.8 |
| e4a1365b-0330-3056-ac40-e289e14e00db | -18.0431 | -57.3745 | 2024-10-25 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 293f4c18-7245-3c05-b733-9fe211e7a074 | -19.6075 | -56.6478 | 2024-10-25 02:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| f7db4eaa-09ab-3dc3-be1e-a64b7a65df04 | -19.6268 | -56.6869 | 2024-10-25 02:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 86cc5616-0697-33df-a2a7-ef0781c1b864 | -19.6272 | -56.6659 | 2024-10-25 02:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.6 |
| 3afc0177-ce6b-30d1-98be-6cc977b61106 | -19.6276 | -56.6449 | 2024-10-25 02:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 6634d4c1-e030-3824-b0e9-659799e75c65 | -19.6473 | -56.6631 | 2024-10-25 02:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| f5e32a26-8efc-3eb2-a3bc-4b0dcb3ff95d | -1.0445 | -47.6237 | 2024-10-25 02:15:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b7eb6cfc-3e8f-3c3c-9d5c-a3330a5a38f8 | -1.0446 | -47.602 | 2024-10-25 02:15:11 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 94b25421-6ecc-38cf-a04f-87e67481bff6 | -1.1834 | -53.6569 | 2024-10-25 02:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 79214ab5-4c6c-303c-95d5-a4877de1732b | -1.1925 | -47.6002 | 2024-10-25 02:15:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 0f20fe76-7798-3f08-b53c-c38e610fa604 | -1.211 | -47.5999 | 2024-10-25 02:15:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| dcbeec9a-3a5c-3933-9616-d6bf9cab7932 | -2.6297 | -49.247 | 2024-10-25 02:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |


[Clique aqui para ver as próximas entradas](README17.md)
