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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c984ec8-b611-3ad1-8cb4-07adad6edfd6 | -3.07015 | -49.20103 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eab46b6-813b-3be7-82e0-c65b22eac36e | -1.84318 | -55.57609 | 2024-11-28 04:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 143e4e53-3875-3912-abf4-fdfd51774696 | -3.84633 | -51.17514 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9acdc71f-25d1-31f9-9205-61ad6b238bc8 | -3.62084 | -44.05124 | 2024-11-28 04:25:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c8e361f9-33ff-3f8e-b1ab-3caa61c5b0ea | -3.6883 | -50.23299 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c84ae8ad-975b-36c5-b1ee-ccc633a6d88d | -3.76783 | -46.51416 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 780a73c9-11c9-3717-ad8e-e078ae30fc9a | -2.60528 | -53.9809 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca810e3e-1ff6-33b7-8118-b5142acca48d | -1.49537 | -54.46591 | 2024-11-28 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8173cb47-0e30-31a5-8c84-b06691cb5fa8 | -3.38579 | -50.11669 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 72be32d1-ab3b-338c-b1fc-460e1f5ea3f5 | -3.88228 | -46.67236 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 390e34f4-211a-3c94-a70c-deda585bbeab | -3.00621 | -53.21529 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 121b7a99-8b84-3c57-b777-3fec505cf568 | -2.97464 | -51.57796 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07726550-8615-3e87-ac55-5ae3b519478a | -11.95719 | -49.52733 | 2024-11-28 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f80c877b-d516-37ee-986e-9067e58e210f | -2.01869 | -51.19442 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd9bb3f2-3531-3cbc-8108-0396b4f44165 | -3.51234 | -50.50526 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ddebcfb-70e4-3966-b936-e39c94fa25b0 | -4.77498 | -44.42477 | 2024-11-28 04:25:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91efcc9c-eac8-3f2b-8752-b55a6e5ed97c | -5.21199 | -41.28505 | 2024-11-28 04:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 31288093-75bb-38bc-ac6f-764e94d01f5e | -1.78188 | -52.74561 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ffad4a9-8363-36c1-b32e-95c5f65f59c2 | -3.83774 | -46.5036 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5bdad7a-b9d1-3a59-97eb-0224a3ea8f30 | -3.24413 | -50.77307 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7d73e3f9-c080-3b7e-99ba-c0e158b01dff | -3.50029 | -53.81265 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 20a6a3c3-cd06-3df9-8e20-947d4f8a9bca | -1.50127 | -54.46378 | 2024-11-28 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c01b2c9c-1d75-38ac-9f67-e259ccf905f9 | -4.036 | -46.53849 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 154511eb-2ba9-35df-a482-f0dda66d0606 | -3.51736 | -50.2225 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4347000-ae5b-377f-9c43-6fa7586f7ae4 | -3.9586 | -49.34909 | 2024-11-28 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ebe2b53-a367-3773-93c0-42299c69e468 | -3.92445 | -46.5139 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5c334ca-87a9-3f2a-b5f8-a7af4b71651b | -3.68447 | -54.20637 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06daf3e6-01ce-331a-91de-1c48cde47922 | -4.92809 | -45.42633 | 2024-11-28 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30f03fa6-523c-3bec-a45f-809d9416256b | -4.31714 | -48.08015 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6d3e576-a31e-34d7-8858-f3d5160d522b | -3.84107 | -46.50412 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5ee2985-da04-3396-bd93-686f38b6efc2 | -2.85252 | -46.8644 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67c5323c-b67d-3037-a02b-13d551a53ee7 | -3.2744 | -50.61106 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46f5358c-082d-32de-a535-ed43e952cae5 | -3.36458 | -46.65982 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2163f9a3-3977-3f21-9228-b754aebcc0a1 | -3.27028 | -50.55933 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96830f6d-639e-3652-8891-37f16ec2ce3c | -2.85771 | -46.81015 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 410721f7-0d1f-3919-84c2-516b1fb114ff | -3.83777 | -46.52507 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19889459-58f8-309f-ba32-0a4ac3c12ee3 | -4.10767 | -46.94716 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecf8c396-0ed2-3740-b116-64350733a906 | -3.27394 | -48.76604 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65ace400-2bad-3750-99ab-f2a776552eab | -2.9472 | -51.58199 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b4ad4c55-ed65-3e72-becb-dcccfafe33ad | -3.23212 | -54.22819 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21d014b9-3851-30da-9d93-a4fd29f1e655 | -3.31327 | -50.49762 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 719c71dc-4856-318c-80d3-e064cad6ab74 | -2.65575 | -48.50857 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e123b41c-9da6-31e1-9dd9-82faf377ba30 | -4.65818 | -49.52383 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f0580425-7cb7-398c-827d-5e398a463af4 | -3.7077 | -47.13003 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2042529-8459-3361-83b7-476eb782dcd0 | -3.69438 | -50.22233 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfcf71da-1b35-34c7-8fde-c0c0593fbd62 | -3.38811 | -50.32408 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f89c6e5d-11ce-37a2-afb3-6e0da69eae65 | -3.80645 | -52.35694 | 2024-11-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 36bbe6c6-5e7d-3a19-a775-1314db8e9291 | -2.69655 | -48.65549 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e3ab8a7-9f4f-333d-97c9-f1960c63a48a | -1.7822 | -52.74128 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a61d3a0-c407-33d7-9a86-d4346efb794d | -3.93651 | -46.71325 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56515ad5-1e87-30cf-bd8f-d4992acda4e5 | -4.44022 | -46.34548 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c7c51b7-c6b7-3ffe-84db-7637f95318ac | -17.62935 | -57.58408 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b036bf24-4cbf-36f3-8403-fcb6c656566d | -22.3308 | -47.40491 | 2024-11-28 04:27:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 579d13a2-d921-361b-92f0-d90b14bf9e3b | -20.1286 | -53.32199 | 2024-11-28 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04088bdc-7408-3105-b06f-42b833ecd79d | -20.76217 | -46.76932 | 2024-11-28 04:27:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4d925d04-7998-36e9-b74c-34a50c7425d1 | -19.52355 | -47.33183 | 2024-11-28 04:27:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc189353-cc4d-3242-8179-fee9233cc32b | -18.68827 | -48.9739 | 2024-11-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73610ff1-efe8-31b4-b76a-93f228cd2c32 | -21.50101 | -48.61639 | 2024-11-28 04:27:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d6f2281-2ceb-34dd-85fb-772be9eb39a0 | -19.52298 | -47.33571 | 2024-11-28 04:27:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b12f472-38be-3614-a94d-c68f097c8a62 | -21.13353 | -49.9841 | 2024-11-28 04:27:00 | NOAA-20 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c592bce8-ecb0-39f5-9608-f8a096d465ec | -23.46447 | -47.52136 | 2024-11-28 04:27:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 50e94d2f-53c6-312c-b703-f3e8709c6874 | -17.60148 | -53.74747 | 2024-11-28 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6c162e4-fc28-33ca-8b18-e46fab2a7362 | -16.9078 | -48.29017 | 2024-11-28 04:27:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c69b5d46-53d2-3264-9eea-909b3f8817ae | -16.07855 | -60.11344 | 2024-11-28 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac41a6bb-7578-3f13-9d44-bb8e56ef3fda | -17.64062 | -57.58023 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e028a0a9-4471-36fa-a3bc-465657926493 | -19.30408 | -45.53681 | 2024-11-28 04:27:00 | NOAA-20 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb0e38c1-b110-3621-9601-54810dbe6f2c | -21.29519 | -50.58295 | 2024-11-28 04:27:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| efcdcf7b-00f4-3df6-80f9-eda1a9e05ee1 | -22.46572 | -47.13672 | 2024-11-28 04:27:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b83686c-0106-3b34-bba8-c534eb43b264 | -20.59749 | -51.61034 | 2024-11-28 04:27:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8898cc32-3a25-3c6a-a2d9-46ede773d4fc | -21.12422 | -48.64719 | 2024-11-28 04:27:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5b6cb33f-fc07-3b8a-be4e-99efcaa8f6e3 | -23.71881 | -50.55864 | 2024-11-28 04:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 5d05ea40-4cbc-34cc-a809-fa0f87e45b9f | -20.79874 | -45.89898 | 2024-11-28 04:27:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac00eb4a-c9b0-3cc3-a921-ba324dd68d43 | -19.30343 | -45.54141 | 2024-11-28 04:27:00 | NOAA-20 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2383709-b903-34e4-90e8-242bdfb6f9b6 | -17.53944 | -57.4388 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7affeb13-e8ab-3dc0-a768-bf7c2ab5d92d | -17.5729 | -57.6033 | 2024-11-28 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7c870907-4d68-3b8d-b6d0-91266742d3f6 | -18.7726 | -55.85067 | 2024-11-28 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6d6b71c0-ca67-339a-8220-a9c36a523bd9 | -16.0747 | -60.10445 | 2024-11-28 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f725fb6-ca4d-3223-8088-c180ee3434c2 | -22.0582 | -49.73936 | 2024-11-28 04:27:00 | NOAA-20 | ÁLVARO DE CARVALHO | SÃO PAULO | Brasil | 3501400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e42708bf-d707-31d8-afe0-a3d125612928 | -19.33603 | -46.32549 | 2024-11-28 04:27:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcc8b1b4-2f04-344b-8cb5-76d94a415811 | -18.77434 | -55.84158 | 2024-11-28 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cd385280-82f5-30a3-84d6-e13c9cef1a53 | -23.7155 | -50.55802 | 2024-11-28 04:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 4a0bd635-4d8b-3c24-8874-8c860089dd59 | -19.9725 | -55.08989 | 2024-11-28 04:27:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35d3a7dc-9f31-390a-b708-a3240237e0dc | -19.20891 | -45.37742 | 2024-11-28 04:27:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5feee74-3a75-33f9-902e-a9fd34aeeea6 | -23.59427 | -47.44092 | 2024-11-28 04:27:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 783a0472-696f-3219-af32-5318cd398b37 | -18.77873 | -55.84254 | 2024-11-28 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c3073878-0b2a-3959-9fd8-3a125c68cfb4 | -21.17047 | -48.69654 | 2024-11-28 04:27:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1210b339-0860-3ac4-ad6d-346028068205 | -17.84954 | -46.00278 | 2024-11-28 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1125c84c-4f07-33eb-87fc-ea56eeff44b6 | -17.57459 | -57.60213 | 2024-11-28 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ae6ebe49-3663-3a2c-8256-ba4b226e8f0b | -18.76995 | -55.84063 | 2024-11-28 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d38dc456-8f34-3d7f-895d-d050a0abe170 | -18.67329 | -47.17212 | 2024-11-28 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 116e1e0a-967e-3b9d-802c-bbcce876b3dc | -22.05547 | -49.73505 | 2024-11-28 04:27:00 | NOAA-20 | ÁLVARO DE CARVALHO | SÃO PAULO | Brasil | 3501400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| daabd0f9-4598-3a47-8113-2e86830ec24d | -17.59756 | -53.74654 | 2024-11-28 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb382e9c-e312-3792-aad3-c6d8e764baea | -17.34858 | -50.52534 | 2024-11-28 04:27:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a31e84e-64dd-31c9-b603-314d0400ce2d | -17.57856 | -57.60136 | 2024-11-28 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5af4d339-6cdd-395a-bab8-21d19449d19a | -23.71218 | -50.5574 | 2024-11-28 04:27:00 | NOAA-20 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 40b7eb75-4dcc-3a64-b35e-c07dd30ede7b | -20.12774 | -53.32669 | 2024-11-28 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a2b041b-8059-328b-ada0-fb81ac1419eb | -20.72188 | -54.43459 | 2024-11-28 04:27:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0904fc15-843e-3bfc-9ea4-7d80bf582ee9 | -21.12411 | -47.85641 | 2024-11-28 04:27:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 52e83c9e-ddc2-3739-b976-cc81162ef2ac | -17.62435 | -57.58294 | 2024-11-28 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 229bd834-1c1f-3a09-89db-42aae0085e8c | -19.30265 | -45.53902 | 2024-11-28 04:27:00 | NOAA-20 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README71.md)
