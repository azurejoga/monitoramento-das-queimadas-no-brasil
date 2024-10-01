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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee0b932e-2142-3bfa-85b5-f96ebebfb317 | -11.6554 | -65.018 | 2024-10-01 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| bf4e41ca-605a-3564-9a9f-5227f8456a1f | -12.0224 | -50.3034 | 2024-10-01 01:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 604f343f-fee2-3c92-b144-8d6b00546d57 | -12.022 | -50.3249 | 2024-10-01 01:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1e6e0c50-a0ae-3b22-b53a-e3e47d9c972a | -12.0033 | -50.3057 | 2024-10-01 01:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 3fe89449-e45b-3bf7-883e-304a06a7e13f | -12.0029 | -50.3272 | 2024-10-01 01:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 29ec47e8-8761-379f-9011-36afff1539a1 | -12.4748 | -53.1899 | 2024-10-01 01:06:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 150.3 |
| eca4f5ea-b369-329e-92e9-3688be2eb688 | -12.4745 | -53.2108 | 2024-10-01 01:06:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 857a1c7e-1033-3f50-a5b7-fe728375cecb | -12.6039 | -53.4879 | 2024-10-01 01:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 12ba0a7a-0f57-32d8-8583-0d36a1d2a052 | -12.4939 | -53.1879 | 2024-10-01 01:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 0fb94b76-b54d-3f60-b770-d2a711ad8de3 | -13.5768 | -51.1607 | 2024-10-01 01:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 603ce889-919c-337e-b42b-3d2089d0020d | -13.5765 | -51.1821 | 2024-10-01 01:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 3b21d771-e800-322e-a724-a358c05a938e | -14.7406 | -48.7498 | 2024-10-01 01:06:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 125.7 |
| b748984d-9d07-3001-9a9d-a962c7f786b8 | -14.7211 | -48.7529 | 2024-10-01 01:06:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9707ce92-bb42-31a0-ba3a-150f784d8c82 | -15.6372 | -57.447 | 2024-10-01 01:06:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| b402d40f-5977-3f61-84b6-5c70575e2aa6 | -15.6179 | -57.4491 | 2024-10-01 01:06:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| f330649f-f5b8-37b2-a158-cae8e6648a13 | -16.1859 | -58.4215 | 2024-10-01 01:06:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| 30236371-fa94-30b0-839e-013a7512a857 | -16.6459 | -55.1908 | 2024-10-01 01:06:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| aa861d59-10b9-3e18-9c62-0bb3da625d26 | -16.6455 | -55.2117 | 2024-10-01 01:06:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 4415c93a-895b-3b68-93ca-c706a91c4ea6 | -16.6263 | -55.1934 | 2024-10-01 01:06:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 127.0 |
| c107d523-2605-3117-b808-77562382a0eb | -16.6259 | -55.2142 | 2024-10-01 01:06:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 2e7de984-b25c-387d-91dd-657231cae3b1 | -16.5134 | -57.3305 | 2024-10-01 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| ae52390e-0e4e-3165-80de-f562553338c5 | -16.4939 | -57.3327 | 2024-10-01 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.2 |
| 1a225d69-40fa-3802-8c6a-e5059488b9ce | -16.4935 | -57.3531 | 2024-10-01 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 1bf9e247-31ed-3ac1-bff8-6f7db758f43b | -16.4743 | -57.3349 | 2024-10-01 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.8 |
| f943e0ae-e9ab-3cad-bd23-d572716fb647 | -16.474 | -57.3553 | 2024-10-01 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.9 |
| 997b9602-3548-3e84-84f8-a9ebd792032c | -16.8103 | -55.8762 | 2024-10-01 01:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| d3d87cdd-316b-31c0-ba1c-4cc958205291 | -16.9179 | -57.6926 | 2024-10-01 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.5 |
| e67467ef-66f3-3f2b-9056-bbf730fded54 | -16.8983 | -57.6949 | 2024-10-01 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.3 |
| bd4818f8-3cf5-36e5-9674-d1396540ef7c | -16.898 | -57.7153 | 2024-10-01 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 84ce1ee8-1951-350e-be85-f726b72f0f85 | -16.8787 | -57.6971 | 2024-10-01 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.7 |
| 5bc64113-f143-3358-9946-3b10c8d07af4 | -16.8784 | -57.7175 | 2024-10-01 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| a13df6f1-8f79-3ce5-942e-aee903ae6382 | -17.1195 | -56.1271 | 2024-10-01 01:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 017894d8-6f50-3d41-8568-9f68bfdc0265 | -17.1101 | -56.686 | 2024-10-01 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| a03cb86d-0f40-3672-87cf-822cf67abf0f | -17.1098 | -56.7066 | 2024-10-01 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 3a315b3f-0c94-3b31-92d3-02bd60cbd25d | -17.1095 | -56.7273 | 2024-10-01 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.1 |
| c4198379-7728-3576-b525-12af25b60c0d | -17.0905 | -56.6884 | 2024-10-01 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| ed1bf221-bf2a-3c8f-bdac-80901f1104c8 | -17.0902 | -56.709 | 2024-10-01 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 418f955f-4e20-3d74-9783-fbbe6457656d | -17.0898 | -56.7297 | 2024-10-01 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 3d093a0b-7475-3621-9945-90e8bc2dff83 | -18.543 | -43.4436 | 2024-10-01 01:06:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.3 |
| 3a4fc453-0afd-3e2e-96cd-ce2b110ebc72 | -18.5423 | -43.4683 | 2024-10-01 01:06:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.7 |
| 450a0f39-f60e-3aed-bc76-7f9c3f468b20 | -18.6011 | -53.0412 | 2024-10-01 01:06:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 62e048d1-d913-39e1-925d-7cbb2a8b5a0e | -18.6006 | -53.0628 | 2024-10-01 01:06:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4228ba3e-4b01-3c19-96b8-0158f202b600 | -18.9091 | -49.2129 | 2024-10-01 01:06:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.7 |
| e21ef8d8-6b8a-3bdc-9138-c80bfb0b379c | -18.9085 | -49.2356 | 2024-10-01 01:06:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.9 |
| 4c2da4c1-6486-3dc0-a64f-fdf757867d69 | -18.6977 | -57.3123 | 2024-10-01 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 6ff97586-d07a-36ce-9aeb-0c4dc065f3cf | -18.6973 | -57.333 | 2024-10-01 01:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.4 |
| b98b05e6-d1b2-3325-980b-3daf2f4ea78a | -19.1329 | -57.4628 | 2024-10-01 01:06:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 181.9 |
| b90873f9-1512-3d1c-8984-a8c1b7a7120c | -19.1325 | -57.4836 | 2024-10-01 01:06:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.4 |
| eb365940-d6f1-32f8-84fc-224cb46e67ee | -19.1129 | -57.4655 | 2024-10-01 01:06:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.4 |
| befcda92-bccc-3b9c-9b7c-5e776d05299d | -19.1125 | -57.4862 | 2024-10-01 01:06:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 8351085e-f8c4-39bf-8e0f-392d457e07dd | -20.5266 | -46.2783 | 2024-10-01 01:06:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| fed8fbd9-1944-37b4-bcd6-b3ef7c1d8935 | -20.5259 | -46.3023 | 2024-10-01 01:06:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 56.8 |
| cdde1ef8-4b79-325b-89f6-4c7705cb09fc | -21.5684 | -47.7933 | 2024-10-01 01:07:04 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 23181172-f1d6-3252-9a41-dfd22473091b | -21.5677 | -47.8169 | 2024-10-01 01:07:04 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 264.8 |
| 8989b6fc-4289-3fe0-a0fa-a92cabc1c55b | -21.567 | -47.8405 | 2024-10-01 01:07:04 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 142.8 |
| a93fc0d8-7f2c-35c9-9a75-483e95aa2668 | -21.5892 | -47.7882 | 2024-10-01 01:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 6f37709d-46fa-3341-8bb9-61bea845b67c | -21.5885 | -47.8118 | 2024-10-01 01:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 499.9 |
| 011e6739-3eae-3628-96ed-c5b9dc24a3e8 | -21.5878 | -47.8355 | 2024-10-01 01:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 323.0 |
| 6586c7cc-cd19-321e-8196-cdecb1d9fef3 | -21.7117 | -54.847 | 2024-10-01 01:07:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 26f1780a-ed84-33b3-8088-2e585254c892 | -21.6917 | -54.8288 | 2024-10-01 01:07:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 2067b2ca-699c-3ca0-8e55-8f8fa65ffdcd | -21.6912 | -54.8506 | 2024-10-01 01:07:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 5bd1b16b-ba13-3550-ad24-233f72a4c545 | -22.1242 | -48.5469 | 2024-10-01 01:07:07 | GOES-16 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 635194c9-35cc-3814-8591-c3cd15429c4f | -22.3713 | -49.3011 | 2024-10-01 01:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 179.1 |
| 8e592fc9-7ca8-3119-b419-5805dfe4d837 | -22.3707 | -49.3244 | 2024-10-01 01:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 251.0 |
| 0f5b4ee9-eec4-3e8d-a0d3-0186e581416f | -2.4048 | -50.3085 | 2024-10-01 01:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| a23e98ee-7547-3401-9902-a22810dac761 | -2.4047 | -50.3295 | 2024-10-01 01:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 365.7 |
| 7962946b-c171-339e-a402-4cd2bc0f9755 | -2.4046 | -50.3505 | 2024-10-01 01:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 8b0fb054-35cf-3e50-8a1d-99e128d16812 | -2.3863 | -50.3299 | 2024-10-01 01:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 6e415650-7070-3a48-b003-26db69cf6a03 | -3.0282 | -51.3345 | 2024-10-01 01:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| bd2f6e07-ae83-3d53-8791-a6405fd74a8d | -4.6987 | -49.8062 | 2024-10-01 01:15:32 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 88d49201-db2b-354f-903a-b7a95ec34980 | -4.7172 | -49.8053 | 2024-10-01 01:15:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c9ab2030-9bcb-3591-8d48-09af0b46bb66 | -5.7715 | -45.5574 | 2024-10-01 01:15:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| ce971c9a-126d-35d6-9219-f124d0a54d10 | -5.9788 | -45.3621 | 2024-10-01 01:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 2be194aa-09a6-385e-8ef2-cf3e20377f9f | -5.9786 | -45.3847 | 2024-10-01 01:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 736fbe9c-e9da-3d2d-94d1-cf94ca53e517 | -6.2524 | -44.132 | 2024-10-01 01:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 2057dbce-d80e-30be-976e-7f42e0af1caa | -6.6953 | -43.0474 | 2024-10-01 01:15:43 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 79eaa358-c63c-3365-acac-80af8128d10c | -6.9858 | -47.6201 | 2024-10-01 01:15:45 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| bf47b5fd-a7de-3cf9-8c79-6694347b1f6f | -6.9671 | -47.6215 | 2024-10-01 01:15:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 2275be5c-484a-3514-80e1-e64f51c54255 | -7.583 | -46.0407 | 2024-10-01 01:15:49 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 32c6adc5-858e-3cef-8117-6fa7dfd15f73 | -10.5743 | -48.0399 | 2024-10-01 01:16:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 4bced871-9aac-345f-85cf-783a12e642aa | -11.1249 | -45.6407 | 2024-10-01 01:16:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| b70928a0-0246-3b02-a549-eb0f4f288dd2 | -11.2584 | -45.6453 | 2024-10-01 01:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a1509b99-65b2-3d05-aa8e-07cbd5e46589 | -11.6744 | -64.9793 | 2024-10-01 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 0fc54342-343d-32b9-b1d3-6bc80847bfcf | -11.6743 | -64.9983 | 2024-10-01 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 142.5 |
| faf3e63e-7192-3a80-ae0e-d1fc281a11d0 | -11.6556 | -64.9802 | 2024-10-01 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 805b6bb5-37e6-337b-a53d-96973f5c31d6 | -11.6555 | -64.9991 | 2024-10-01 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 219.7 |
| 879cd3f2-7fa3-3e26-b754-48399e732825 | -12.0224 | -50.3034 | 2024-10-01 01:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 9c7c6075-f8bb-341b-889f-0c9b87afa0be | -12.022 | -50.3249 | 2024-10-01 01:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 2d572e4a-621b-3c6e-a33c-3a4c0623c527 | -12.0033 | -50.3057 | 2024-10-01 01:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 7531ad41-6082-3232-94a5-e96c0a244150 | -12.4748 | -53.1899 | 2024-10-01 01:16:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fd76e4de-5f22-3ca4-8b5d-b9f9fc55939c | -12.4942 | -53.167 | 2024-10-01 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 16549a81-083e-35dd-92e2-d88adb8b03c0 | -12.4939 | -53.1879 | 2024-10-01 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0376be7f-e603-3971-b1b5-eae67e51f8f0 | -13.5768 | -51.1607 | 2024-10-01 01:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| dbf06eda-3466-3bda-bc3f-03c3b7d6f6e2 | -13.5765 | -51.1821 | 2024-10-01 01:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 17048d3c-cdf3-301a-b4b7-c2cdfbcebaea | -14.7406 | -48.7498 | 2024-10-01 01:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| e35db7c2-0008-3937-9d6b-1c743328a3d9 | -14.7402 | -48.7721 | 2024-10-01 01:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 0ee22dba-0c5b-35a1-ac2e-9a754ea5882e | -14.7211 | -48.7529 | 2024-10-01 01:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 30e5200d-d660-35c3-a2e7-feb4f64c2443 | -15.6933 | -53.914 | 2024-10-01 01:16:34 | GOES-16 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3c612a15-c602-3755-91c1-ec96667023ae | -15.6372 | -57.447 | 2024-10-01 01:16:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 10fef2f7-9847-3405-a716-2f0f01fd93c6 | -15.6179 | -57.4491 | 2024-10-01 01:16:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |


[Clique aqui para ver as próximas entradas](README23.md)
