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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d386ef7-2f8f-3bb2-b50d-6487650ebeab | -9.57492 | -64.70885 | 2024-10-20 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c4816de-04c3-33c8-9747-4a6f8bdf3f2e | -9.57011 | -64.70413 | 2024-10-20 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e561e9c4-46eb-33aa-8e68-4923a39ee0cc | -10.20323 | -64.84463 | 2024-10-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 686dd26a-050d-38e0-8ac7-b11092fa4b38 | -10.19842 | -64.83997 | 2024-10-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0813e45d-03e7-3c60-a128-b524e12542d4 | -10.19774 | -64.84361 | 2024-10-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8cf16baa-c25a-3eb8-8150-b51741793799 | -10.19705 | -64.84729 | 2024-10-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cf715a37-5bb8-354b-98af-4c8ea67aef79 | -18.29636 | -56.17213 | 2024-10-20 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4bb7fed2-824b-38e3-963c-1b0cebf0f0a2 | -18.29303 | -56.17157 | 2024-10-20 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8873f985-7a73-3e68-acba-de048dedc077 | -18.276 | -56.08606 | 2024-10-20 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6855f52d-269d-32b7-83a6-a0ea74c22bc9 | -18.27544 | -56.08973 | 2024-10-20 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d9ac6c2f-bdda-3ea9-bd28-f10d0ea67d81 | -18.27267 | -56.08551 | 2024-10-20 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 950e07f5-5e82-3541-aba7-ef912ba42ce2 | -18.27211 | -56.08917 | 2024-10-20 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e942a5ae-a1f8-300e-a406-5ac1d93a3549 | -18.18465 | -56.30333 | 2024-10-20 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4cfeed8c-0ee8-354a-b55e-7702df967560 | -19.58509 | -56.53209 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 90d5a93f-c510-30bc-9e25-035daa59769a | -19.55768 | -56.62188 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1946b889-7e41-3715-b608-4721c4238830 | -19.55712 | -56.62555 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 33819c01-44fa-364c-9ac7-d861694b5aa4 | -19.55655 | -56.62923 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5d5bae78-0358-32f0-aa1f-88e6965f52c3 | -19.55436 | -56.62131 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 74dd75ca-d889-3c04-93f9-5270c98bb42f | -19.5521 | -56.63601 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5829cd88-bf49-3d09-bede-29896122e27d | -19.5516 | -56.61707 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 59be892b-76a1-3211-96c2-f1e495c94874 | -19.55103 | -56.62074 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 73f4121f-1e1e-3de8-85d7-d0be71c02f4f | -19.54771 | -56.62017 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0a79ea8d-42e5-3299-bf33-0820ef90abcc | -19.54765 | -56.6428 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a40d3f3d-b846-3eb1-85ff-24371858a085 | -19.54715 | -56.62385 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7283182a-3c8d-364e-ac40-773ee73602e0 | -19.54659 | -56.62753 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9e72baf9-b768-338c-9113-beea4073505f | -19.54602 | -56.6312 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f2501bb0-822d-353f-8205-0b7e59c4431b | -19.54546 | -56.63488 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5cf75403-a04e-30f3-b2f7-71be85097670 | -19.54489 | -56.63855 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f19a7da9-e713-323a-aa8d-91ff140a9b80 | -19.54439 | -56.61961 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 72cb00d3-5681-370c-be3e-8e897de8aa46 | -19.54433 | -56.64223 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 59200f2f-4ad7-3ecc-9f1a-ddc6820dc645 | -19.54383 | -56.62328 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| da5305e0-f32e-39a8-b5ff-d209e87cbc9e | -19.54326 | -56.62696 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8dc04471-f50f-3558-bb3a-0f2366af7cc8 | -19.5427 | -56.63063 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8fa8f935-a6f2-3e79-8d7b-b8e590bcc05a | -19.54213 | -56.63431 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 958877f3-2a2e-37a8-82a4-359edbcd80c6 | -19.54157 | -56.63799 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7988c5a5-1ea2-3f3c-a91e-1886da6e0f78 | -19.54107 | -56.61904 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 002644d6-cf9c-37bd-979c-51cccbde3a8b | -19.54101 | -56.64166 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 46f834ef-8839-33cd-8d7d-1d0099b9db42 | -19.5405 | -56.62271 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d56cb3b3-e1cc-3c6d-b617-58f92eba7d79 | -19.53994 | -56.62639 | 2024-10-20 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 19986ef7-a34b-37cb-8f55-8212f49f1259 | -17.23813 | -57.31357 | 2024-10-20 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 372cd3e9-aa35-31ca-a9dd-75d311b65b4b | -17.23481 | -57.313 | 2024-10-20 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 85141631-d1d7-3431-8752-34d60afd198f | -17.20773 | -57.50234 | 2024-10-20 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 52766d79-36e5-315d-ba0f-9ec1c1991ac4 | -17.20714 | -57.50598 | 2024-10-20 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0e9c4ec0-4752-35d4-9d1e-ceddf28ee14d | -17.01662 | -57.46563 | 2024-10-20 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 241b3388-7e31-316b-b4a0-526149b84dd3 | -17.01329 | -57.46505 | 2024-10-20 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 790cbc05-e551-311d-953a-01a11dc7dfbd | -16.9984 | -57.51484 | 2024-10-20 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cd940245-ce73-38a8-a67c-aec2d7f8b406 | -16.99567 | -57.51062 | 2024-10-20 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6b01b624-e99a-370e-a103-8488a5f6df55 | -16.99508 | -57.51426 | 2024-10-20 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7c30b28d-e495-3805-a0a2-f8dd1ae5a9f2 | -16.99175 | -57.51368 | 2024-10-20 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 31f340a9-2d75-3b97-a9dd-209ca1977de1 | -16.95284 | -57.52564 | 2024-10-20 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 71429b52-94ba-33b8-a954-cc02e0087afd | -21.67308 | -57.84223 | 2024-10-20 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 0405bb96-04ed-3d2b-bd27-266422fbe79d | -21.67035 | -57.83793 | 2024-10-20 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 05a134f9-f630-3765-987c-3e462b721aba | -21.66977 | -57.84163 | 2024-10-20 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 18b98561-046b-3cd6-a572-5f7c44c492d1 | -29.86691 | -51.16718 | 2024-10-20 05:01:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| e6877205-e54c-3d9e-90da-82981bcaca08 | -29.86529 | -51.16682 | 2024-10-20 05:01:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| eb33a49e-b579-35c0-9a84-c7e79ea41af8 | -29.81185 | -51.17896 | 2024-10-20 05:01:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 62ff49e9-ca5e-33ce-83e5-25d3f3136d13 | -29.4213 | -53.99718 | 2024-10-20 05:01:00 | NOAA-20 | JÚLIO DE CASTILHOS | RIO GRANDE DO SUL | Brasil | 4311205 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 8043f42d-3372-3cfa-84ce-3d7961c9edbc | -2.2994 | -48.5722 | 2024-10-20 05:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 946adcc9-57d9-3976-a232-4237a0c57c77 | -2.7773 | -49.3067 | 2024-10-20 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b9ec5910-b709-3bac-8ce4-876abfe86700 | -3.0478 | -51.0226 | 2024-10-20 05:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 209fd822-c4dd-3ede-ba42-7cdbf0056fd5 | -3.3814 | -50.6579 | 2024-10-20 05:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 063f13af-c5ca-37f3-b2dd-d87d734896e9 | -4.1985 | -46.6318 | 2024-10-20 05:05:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| fe5d1a5f-df7e-3d00-a5f9-631f7798d735 | -2.7958 | -49.3062 | 2024-10-20 05:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| ae921acd-173d-3699-b1a8-9eea0a38f42d | -3.3814 | -50.6579 | 2024-10-20 05:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6fb4f698-d1c0-3788-9075-4d1b8ecdc185 | -5.91563 | -42.95665 | 2024-10-20 05:18:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 4bd60d56-942b-318c-80c6-f93d7b0ee6c1 | -5.54202 | -43.90018 | 2024-10-20 05:18:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a62ff335-610b-3cef-b153-4e875e78ccd0 | -5.54056 | -43.91014 | 2024-10-20 05:18:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 084023af-941a-3c4c-ad26-4e791f998c39 | -3.5171 | -43.61507 | 2024-10-20 05:18:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 20714443-405e-37de-a839-b09eb08993ec | -6.15564 | -44.42651 | 2024-10-20 05:18:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 921319af-f5d0-3e30-bfea-cf70737ee94c | -5.43825 | -46.34652 | 2024-10-20 05:18:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cde2192f-e41f-302c-a3d4-d60c8d2fd99f | -5.43692 | -46.35535 | 2024-10-20 05:18:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3044d1e3-48c4-3e9c-afaa-6ee1abf4d30d | -5.39945 | -46.90665 | 2024-10-20 05:18:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 80f59503-7ef7-3e9b-bdb3-cd2a5911f9a7 | -5.21623 | -46.09705 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 53afa683-319e-3768-9823-b7191c4c2089 | -5.21491 | -46.10587 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d20295ea-0057-3682-97e7-5b581685fc49 | -5.17645 | -46.18142 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51877109-c1e1-35ab-b92a-4368f92c0c48 | -5.15714 | -50.7154 | 2024-10-20 05:18:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 002492bb-d6a1-3425-aff5-2bd9eabcb036 | -5.13976 | -46.11525 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4fd63a90-1f24-37f7-bff4-932fad629fce | -5.1243 | -46.15807 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 323a0373-2d7c-3755-8aa4-e65647914868 | -4.99124 | -46.48572 | 2024-10-20 05:18:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b6402f4d-b308-3ef5-a463-f98516254fc1 | -4.97214 | -46.492 | 2024-10-20 05:18:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 345924b0-227f-3abb-be83-759fabdbc365 | -4.96834 | -45.9066 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be5c6c7a-4b28-3f78-a99a-d00d358633c9 | -4.91405 | -45.82984 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d9277c1a-4155-3252-a822-91a990c3dff5 | -4.90654 | -45.81974 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d9dc9428-0897-3283-ae6c-ead45e4f764b | -4.90522 | -45.82855 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| aa2d0b33-69af-353d-b5b4-61da311fa0e7 | -4.9039 | -45.83736 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4eac0f7e-5063-3af5-aa3b-2a7dda11fdf5 | -4.8977 | -45.81845 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0981e533-3456-3cc2-ab3e-12a63a8b237e | -4.89638 | -45.82726 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 51151514-9930-3300-8947-1240cd6fd45b | -4.89608 | -48.27753 | 2024-10-20 05:18:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 51075120-8994-3c54-b63f-7bf53ff1c42a | -4.87702 | -48.21179 | 2024-10-20 05:18:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 8ea4ad38-93c0-360e-8005-39f91d39446e | -4.86754 | -48.21039 | 2024-10-20 05:18:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d57a1114-3f79-324f-9aa4-376549791a2e | -4.86327 | -45.86742 | 2024-10-20 05:18:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c88b04c6-f7b9-3de7-8d04-f9d435d5139d | -4.70956 | -45.84153 | 2024-10-20 05:18:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1ea02a7b-5718-3ab0-9baa-91799502a35f | -4.70072 | -45.84024 | 2024-10-20 05:18:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6a20ac0a-d3d0-37ed-afa1-0b8de1e87ef8 | -4.57601 | -48.01734 | 2024-10-20 05:18:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 004b8784-bb3f-37b0-8110-2bbabfd13b5f | -4.42305 | -45.9695 | 2024-10-20 05:18:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05bc1f0c-0b96-3283-b683-f411e479709b | -4.39396 | -46.1636 | 2024-10-20 05:18:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e27266c0-64d4-3b77-bc54-3e3094ba80f9 | -4.39374 | -45.80327 | 2024-10-20 05:18:00 | AQUA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 145b4a72-7370-3298-b2a5-4f796f47ba02 | -4.38847 | -45.83847 | 2024-10-20 05:18:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe9e3d9b-988e-3b60-9005-5eb3d239ca20 | -4.3849 | -45.80198 | 2024-10-20 05:18:00 | AQUA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 8a6a3d4d-b32f-3679-b030-14509cc6b060 | -4.38094 | -45.82838 | 2024-10-20 05:18:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README55.md)
