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

## Dados Diários - Página 192

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3deb46c0-9db7-3c2f-bdd8-4ceafcb54819 | -9.1039 | -50.9231 | 2024-10-04 13:25:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 5d586c73-7738-38dd-b6e3-13f9b35a6ac6 | -9.1041 | -50.902 | 2024-10-04 13:25:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 265.1 |
| 4c6d68a0-8367-3162-ae42-3d5b23b6d6cc | -9.5962 | -46.2618 | 2024-10-04 13:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| b29ded0d-7a37-31e1-b5b0-471caf5629f3 | -9.9735 | -46.353 | 2024-10-04 13:26:02 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f3d28792-f249-3658-950e-a6af5e47faa6 | -9.9822 | -42.0976 | 2024-10-04 13:26:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 97.3 |
| e7797e76-225d-3e2d-aaa0-8e1049573f0d | -10.2381 | -47.7038 | 2024-10-04 13:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 60d5edfc-ab4f-3055-a891-63a3e51ab748 | -10.2378 | -47.726 | 2024-10-04 13:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 5e7ac28d-2557-337b-90bc-581ac2df66a3 | -10.2764 | -47.6774 | 2024-10-04 13:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| d02cdc3e-5886-3792-8e95-707aa1413c97 | -10.2571 | -47.7017 | 2024-10-04 13:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 258.1 |
| 88baceca-8519-3e85-ae9d-8efc4320536a | -10.2574 | -47.6796 | 2024-10-04 13:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 591bf830-6757-3e9a-a3b3-a2804cc01307 | -10.7118 | -47.7149 | 2024-10-04 13:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 5001050c-d299-30d4-97f1-6fe6a10e9a7a | -10.7359 | -46.1465 | 2024-10-04 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 1d2c28ae-6799-3160-94a9-75926b86a96b | -10.7115 | -47.737 | 2024-10-04 13:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 562e0520-f5e9-3dec-afe9-f6d29db273de | -10.7309 | -47.7126 | 2024-10-04 13:26:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ff0bf8da-5b4d-36cc-8df0-3a2910fd39ad | -10.8216 | -45.5444 | 2024-10-04 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 5b65d2f2-1a90-3bad-8cd7-18592b8ac74f | -10.8992 | -46.6442 | 2024-10-04 13:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 7178160b-4b34-3f83-a69b-5dcb3b47d2c2 | -11.0349 | -46.4917 | 2024-10-04 13:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 320.0 |
| 00e058e6-0ad3-3374-86af-70a21992dc5c | -11.0345 | -46.5143 | 2024-10-04 13:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 240.6 |
| a4e16c9e-25e8-33c5-9a72-6267f47db10b | -10.9187 | -46.6192 | 2024-10-04 13:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 57b1b3e6-43e9-32df-92dc-eb93c6fb4398 | -10.9374 | -46.6393 | 2024-10-04 13:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| fa80a6ce-04b9-3a97-b449-c63adba1cd86 | -10.9377 | -46.6168 | 2024-10-04 13:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 2f1e8f1a-0ab2-3f71-9983-600a751647ed | -11.2779 | -43.4118 | 2024-10-04 13:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| cbb5156f-fa21-32a9-93dd-6875f7ffef3d | -11.1384 | -45.9804 | 2024-10-04 13:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 392.6 |
| b13d97a0-87b5-3a1c-9607-363f54198307 | -11.2369 | -46.9597 | 2024-10-04 13:26:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 544e0854-e913-3eed-a0bf-44594bb022ce | -11.2376 | -46.9148 | 2024-10-04 13:26:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 73b0fdf6-2e1d-3452-95f0-89c853a5ae98 | -11.2971 | -43.4088 | 2024-10-04 13:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 302.4 |
| 831a2bd4-3cc9-374a-bf16-39b714bca3c8 | -11.1388 | -45.9577 | 2024-10-04 13:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| d4397b53-9a7b-34d6-a26f-9b4cb8301185 | -11.2783 | -43.388 | 2024-10-04 13:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 9ef47ecd-b0a3-377e-9eec-05b0efc081cf | -11.2563 | -46.9348 | 2024-10-04 13:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| f61ee107-ce3b-3ffd-91a8-8feeb4a1e580 | -11.3853 | -47.2088 | 2024-10-04 13:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| c525ac5c-df0c-3bd6-b22c-27d92371a44a | -11.6804 | -47.8156 | 2024-10-04 13:26:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 87b3ea84-31be-3624-8354-c3379d4e98ea | -11.9105 | -50.1447 | 2024-10-04 13:26:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| bd18626f-9e4a-3af3-b3dd-1016955e2bcf | -11.7415 | -49.9925 | 2024-10-04 13:26:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 374e9164-0541-3e1e-b5a1-cf3f25675a97 | -11.7412 | -50.0141 | 2024-10-04 13:26:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| b87a66f0-b900-3187-aca7-ffd6d5840e1d | -11.9487 | -50.1402 | 2024-10-04 13:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 97b95158-72ec-36c3-8187-aab1b9581099 | -11.9296 | -50.1425 | 2024-10-04 13:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 32ed7b2b-6784-3046-a645-f31ef9d4ba33 | -12.1533 | -50.4595 | 2024-10-04 13:26:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| eb99a332-f484-36c6-9d01-27d3ed2f175d | -12.7815 | -50.5758 | 2024-10-04 13:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 5b86eab0-6503-30b1-8885-cb70815b3fa2 | -13.1163 | -51.1765 | 2024-10-04 13:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 93ec6738-1899-3422-a1ee-8d470230c116 | -13.1636 | -46.3231 | 2024-10-04 13:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 101.8 |
| c03f4975-5979-3d44-a8b3-43a62fe25c25 | -13.1443 | -46.3261 | 2024-10-04 13:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 602e876a-f58e-3dcb-84d4-946fd2c27ef7 | -13.1447 | -46.3033 | 2024-10-04 13:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 92348152-e458-3e55-9a2a-d923b15888ba | -13.1787 | -48.6295 | 2024-10-04 13:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 9c78ce00-355a-3970-88e2-98348e0d5cdd | -13.1791 | -48.6073 | 2024-10-04 13:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 7fbe795d-939d-3094-8f08-12cefa4505bc | -13.199 | -45.492 | 2024-10-04 13:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 67e020f0-a5b9-3496-987f-5304498981c3 | -13.1779 | -48.6737 | 2024-10-04 13:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 138.4 |
| d435d04f-2cc0-339f-9558-b09442a8f474 | -13.5626 | -47.6395 | 2024-10-04 13:26:22 | GOES-16 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| a83f8fcd-bef6-3903-be1a-6d2966e6243a | -13.5255 | -48.6018 | 2024-10-04 13:26:22 | GOES-16 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 06af5359-45b0-3377-86b1-cb6507a75a2f | -14.0378 | -45.1648 | 2024-10-04 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 7a768855-c8db-3d2b-b1d0-ed1d2454b147 | -14.0382 | -45.1414 | 2024-10-04 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 59e0cff8-aeda-365a-8896-bc3574c5f6f9 | -14.5163 | -49.3148 | 2024-10-04 13:26:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 934a330b-bf13-38d2-a57e-6cdd0cbbd185 | -14.5168 | -49.2927 | 2024-10-04 13:26:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| c0e46aeb-2091-3a7d-95a8-49ecf1f1e731 | -14.5362 | -49.2898 | 2024-10-04 13:26:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| be8e0044-8217-3f4d-a8ec-5f64f7377d58 | -14.7926 | -48.095 | 2024-10-04 13:26:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| cf8e76a8-a375-33be-a7f5-69e6d75f7a2d | -14.793 | -48.0725 | 2024-10-04 13:26:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 0b6dfd52-9b00-378c-8c8c-a904cb3278fd | -15.4247 | -47.6736 | 2024-10-04 13:26:32 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b550c0cc-b637-36a9-81ec-faa33af358b3 | -15.6304 | -47.2063 | 2024-10-04 13:26:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 627645c5-05c7-3034-a182-034b44f5419b | -16.9296 | -47.1455 | 2024-10-04 13:26:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 84.1 |
| f2b7a35f-ff6a-329a-8248-dbb249bcd7da | -16.843 | -57.4767 | 2024-10-04 13:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 66cf9c73-36c9-3c2f-97a7-c4b21af25c6f | -16.8055 | -57.3788 | 2024-10-04 13:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| e2c36f1b-c90c-3dfd-a483-4ea465d33a9a | -19.1134 | -48.2833 | 2024-10-04 13:26:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 123.2 |
| a8a09af0-271c-31c3-b038-1b18e30d1509 | -19.6122 | -46.2632 | 2024-10-04 13:26:54 | GOES-16 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 101.8 |
| aab95eb5-131a-3b5a-a03b-a61601be34a0 | -6.6529 | -45.3324 | 2024-10-04 13:35:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 0d8082f9-9d41-3b72-af32-9d32034acfe5 | -6.6531 | -45.3097 | 2024-10-04 13:35:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 8f1e2e35-fae0-3b84-9810-0c1670ab45fc | -6.929 | -47.6901 | 2024-10-04 13:35:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 95ad640f-d2a5-35e7-8398-5eddf8f8d2f1 | -6.9477 | -47.6887 | 2024-10-04 13:35:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| b72ffcc3-4eef-3810-b4d9-69a6300f39ae | -7.2565 | -45.0079 | 2024-10-04 13:35:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c8188429-7321-3f8e-92c7-980d61cd718a | -7.276 | -44.9378 | 2024-10-04 13:35:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| d7b9499e-b874-3a4a-812c-b2e871364517 | -7.3136 | -44.9343 | 2024-10-04 13:35:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 68fa45ba-24aa-3915-8ce0-f6f46bbb0638 | -7.8541 | -45.3384 | 2024-10-04 13:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 184.2 |
| c7f40ef8-d1fc-3b99-b232-8b0c56267279 | -8.2239 | -44.363 | 2024-10-04 13:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| f9968747-87cd-37f9-b331-2b550d23e160 | -8.1951 | -43.6703 | 2024-10-04 13:35:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 117e684a-1cba-310f-9fb3-fca2f8e7e79e | -8.2859 | -45.4317 | 2024-10-04 13:35:53 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 36a693c6-3d91-3d52-849a-4fa2a56f7753 | -8.6636 | -50.0501 | 2024-10-04 13:35:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 973804f6-c399-3239-93bb-729d76025d7a | -8.6451 | -50.0304 | 2024-10-04 13:35:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 40415eab-c908-3fcb-aa1c-f098ce41754a | -8.6448 | -50.0518 | 2024-10-04 13:35:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 81617b50-5394-381f-869e-b62875fa36b2 | -8.8362 | -45.1688 | 2024-10-04 13:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 3a75b63c-719e-3f33-8dd0-090fc40aed58 | -8.8359 | -45.1917 | 2024-10-04 13:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e97e7105-d7d3-35a6-a4c3-cd7d4ea90bb1 | -9.0853 | -50.9036 | 2024-10-04 13:35:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 102ebbfe-954d-3767-a5ef-3359c4368d28 | -9.1041 | -50.902 | 2024-10-04 13:35:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 185.9 |
| d4659a35-5942-350b-8da7-1a6887cd7ea5 | -9.8855 | -47.2124 | 2024-10-04 13:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| caee39ad-d8b3-318f-80ff-809bcaec475a | -9.9822 | -42.0976 | 2024-10-04 13:36:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 125.5 |
| 54e3f8ec-314d-3281-ab03-453d8d31f97d | -10.2381 | -47.7038 | 2024-10-04 13:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 3c272fb6-7d90-3eb7-9c6b-7bb299eac08f | -10.2378 | -47.726 | 2024-10-04 13:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| efe66186-2184-324f-91d2-ad937eaf869b | -10.2574 | -47.6796 | 2024-10-04 13:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 04d221dd-8db8-3594-a8ea-e37e75d1293d | -10.5933 | -48.0377 | 2024-10-04 13:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| e9d7619f-9154-353a-af37-fcd3a962daeb | -10.5929 | -48.0597 | 2024-10-04 13:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 0b147416-736f-38c9-8385-0bb38b9f078a | -10.7309 | -47.7126 | 2024-10-04 13:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 1d316d51-b872-3a1e-91fa-5852e032b3ed | -10.8018 | -45.5927 | 2024-10-04 13:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 61ea195d-dfd4-3964-a37f-c3cb2123edd6 | -10.9187 | -46.6192 | 2024-10-04 13:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| eca80064-77a1-353c-9690-c449076b9f20 | -10.9374 | -46.6393 | 2024-10-04 13:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 88f7a8a3-fe26-32b8-988c-f09bca2541d7 | -11.0349 | -46.4917 | 2024-10-04 13:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 8256bcf5-85ec-3c23-9bd5-f7cf1ff3f739 | -11.2369 | -46.9597 | 2024-10-04 13:36:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 8d4a99bd-aaa7-30fb-9183-e7e663502b9d | -11.2971 | -43.4088 | 2024-10-04 13:36:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 209.9 |
| b4305371-e0b9-32b9-9e96-523803fdc14d | -11.2783 | -43.388 | 2024-10-04 13:36:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| c315ec7c-2a52-3125-892e-7ba9d1de37cd | -11.3853 | -47.2088 | 2024-10-04 13:36:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| bd8a71e7-03b0-37bb-9b14-73d7b2546b0c | -11.3849 | -47.2312 | 2024-10-04 13:36:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 0d06cd7b-918e-34dc-9f6b-f9dca500ef2a | -11.6804 | -47.8156 | 2024-10-04 13:36:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 6b828505-765f-34c7-9478-4dae8a5844f6 | -11.9105 | -50.1447 | 2024-10-04 13:36:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 282bb61b-5191-318e-b896-ccc9355d502e | -11.9296 | -50.1425 | 2024-10-04 13:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |


[Clique aqui para ver as próximas entradas](README193.md)
