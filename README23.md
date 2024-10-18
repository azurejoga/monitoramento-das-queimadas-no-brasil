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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a761e08-f449-32fe-8b4a-16a3512005fa | -23.13675 | -45.54609 | 2024-10-18 03:34:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5d2c6ab1-a719-3e15-aa36-d1bd179aa900 | -23.13597 | -45.5496 | 2024-10-18 03:34:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3cea22df-00da-39d3-822a-a91c2b16f781 | -23.13153 | -45.54487 | 2024-10-18 03:34:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 430cf643-5a36-387b-96d8-c6831c84df87 | -23.13074 | -45.54841 | 2024-10-18 03:34:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ecc5a206-c5fc-3914-ae3d-7a42bdcd02c1 | -23.12996 | -45.55194 | 2024-10-18 03:34:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9da9ab3f-4c29-3e0e-9e3e-0f66808d20ab | -23.36589 | -47.37283 | 2024-10-18 03:34:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 36b86f9a-f8cf-303e-bb75-50db7fbce9f7 | -23.3648 | -47.37744 | 2024-10-18 03:34:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 33782206-558b-3b2d-bfa1-d931bec0f29d | -22.97829 | -49.52093 | 2024-10-18 03:34:00 | NPP-375D | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| d936b287-b535-3a93-9384-860033dfd072 | -22.97677 | -49.52703 | 2024-10-18 03:34:00 | NPP-375D | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 91983cd0-f503-390c-9c90-227da4ee2776 | -22.97182 | -49.51894 | 2024-10-18 03:34:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 51af94e3-3ff1-3fed-adb1-457a666a7747 | -22.9703 | -49.52498 | 2024-10-18 03:34:00 | NPP-375D | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| a55185a7-b3e6-35b9-8e6a-d35fbe655f03 | -2.4459 | -48.975 | 2024-10-18 03:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ffceda5a-f3d4-31e4-a3d0-6ffb24d755af | -2.4644 | -48.9745 | 2024-10-18 03:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c3b737e2-d95e-3252-b5cd-f96dec1ac8e9 | -3.7009 | -45.9 | 2024-10-18 03:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 7bf5eccf-c273-3a2a-943c-0e9f69ceb2dc | -3.9267 | -42.401 | 2024-10-18 03:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 158.0 |
| e4ff21c1-658c-304c-a2ea-428e76346257 | -3.9265 | -42.4246 | 2024-10-18 03:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 88800055-6f8a-3f61-8df0-7ebaacb1de69 | -3.908 | -42.402 | 2024-10-18 03:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 151.0 |
| 14554f74-94af-3368-b627-c935d9a5898c | -4.4258 | -45.9763 | 2024-10-18 03:35:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 91ecee54-4ac9-3c08-bf44-51954951b1e4 | -5.5716 | -44.8927 | 2024-10-18 03:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2e2e4135-20df-380d-9de8-34c770937495 | -9.962 | -67.4394 | 2024-10-18 03:36:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b07e2209-1986-3f1d-b2f1-7b93ccc3a29e | -9.9619 | -67.458 | 2024-10-18 03:36:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 48.3 |
| d3de33ff-e741-3065-9f18-d7fee3267eaa | -12.5155 | -63.2055 | 2024-10-18 03:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 5bdb414a-c2f2-3802-88a9-7f5867d14cfd | -12.4966 | -63.2066 | 2024-10-18 03:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 087c4b66-d9c9-3290-a4d8-356e966670e6 | -17.2373 | -57.3079 | 2024-10-18 03:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 8d7b0f49-337f-3bad-9241-133d82e57494 | -17.2177 | -57.3102 | 2024-10-18 03:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 86c1dad0-5bae-36a3-ae68-2746239e1f53 | -18.0632 | -57.3514 | 2024-10-18 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 457a560e-d683-3a97-b757-8586fd05c844 | -18.0629 | -57.3721 | 2024-10-18 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.8 |
| cffeaa9e-db49-3265-bc24-79595030ebec | -17.9036 | -57.4534 | 2024-10-18 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 2f839f2c-6957-3619-a97c-662ba3859639 | -17.9234 | -57.451 | 2024-10-18 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 87e82e36-158e-3c62-aae2-0073a5550454 | -18.1993 | -56.3399 | 2024-10-18 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 03dc9f96-c25c-32a3-a75a-27f2c2c78783 | -18.1989 | -56.3608 | 2024-10-18 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 2576aa62-0371-366b-a0fe-71217e52d731 | -18.1798 | -56.3217 | 2024-10-18 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 14578d85-9fa2-3249-ad37-1b747d48ae10 | -18.1795 | -56.3425 | 2024-10-18 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| af75e370-c45b-39b4-b541-783522fe5b4d | -2.4644 | -48.9745 | 2024-10-18 03:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 06947a80-a07d-3163-9906-2de24b93e022 | -2.4459 | -48.975 | 2024-10-18 03:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| cd6d96b9-a97b-3c11-a305-ac5a70fbbfc5 | -3.7009 | -45.9 | 2024-10-18 03:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 16a3304c-45ba-3731-938b-28ec20078f11 | -3.9267 | -42.401 | 2024-10-18 03:45:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 5c1b9f48-f632-3371-8261-d5781666c913 | -4.4258 | -45.9763 | 2024-10-18 03:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| f9bfac44-883e-3302-8fcd-5d8e6b94d0bf | -4.58 | -48.0132 | 2024-10-18 03:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2216f0ab-4f94-31ac-a844-5bf677a1a6cb | -5.5716 | -44.8927 | 2024-10-18 03:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 6364a5cf-465b-3790-bb0a-a8fa0869e4b6 | -9.962 | -67.4394 | 2024-10-18 03:46:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 185072f5-1c40-334c-881f-93fe5f606e89 | -9.9619 | -67.458 | 2024-10-18 03:46:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 3f5b108e-d328-3be5-84b0-631cf1bf40fc | -12.5048 | -55.1846 | 2024-10-18 03:46:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 97aab4c5-0475-3ac7-83fd-bfea977b1e54 | -12.4966 | -63.2066 | 2024-10-18 03:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b2c1b0a1-47ff-3cce-91a7-d721089e0ed1 | -12.5147 | -63.3014 | 2024-10-18 03:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 77f99c0d-6501-3377-8609-6a2588dee861 | -12.5149 | -63.2822 | 2024-10-18 03:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0b04bbfe-e87a-3bfd-acd1-443b91f69ceb | -12.5155 | -63.2055 | 2024-10-18 03:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e3c90818-c8dc-3df1-b809-544e5d3e019c | -12.5338 | -63.2812 | 2024-10-18 03:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3f4f161c-7dda-376c-9e62-df431acd947b | -12.5336 | -63.3003 | 2024-10-18 03:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 93c6eb22-b54b-3248-a23e-133f56d48e60 | -17.2177 | -57.3102 | 2024-10-18 03:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 889ac4fd-560b-34e4-a045-cebfe80ad538 | -17.2373 | -57.3079 | 2024-10-18 03:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.7 |
| 7fd4dfe1-c8a6-3ebc-92f7-32eef3c0273d | -17.9036 | -57.4534 | 2024-10-18 03:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 4a5c78f2-c718-3d4d-816b-eec600a11cf1 | -17.9234 | -57.451 | 2024-10-18 03:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| 4566dba0-4709-39d5-ae26-ee560863455f | -18.0632 | -57.3514 | 2024-10-18 03:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 85a7235c-30c6-3236-9664-93bc98ef4118 | -18.1795 | -56.3425 | 2024-10-18 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 4b4e2592-2211-3398-8257-47bb9a0acb1b | -18.1798 | -56.3217 | 2024-10-18 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.7 |
| d92b3fd1-d529-3bd3-aa9e-1cb87c5e76c4 | -18.1989 | -56.3608 | 2024-10-18 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| dc99d323-c5be-330b-a4ad-a82bdbbe5e23 | -18.1993 | -56.3399 | 2024-10-18 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 6471c590-0b4a-3b9e-b532-c135fe0f8f9b | -18.1997 | -56.319 | 2024-10-18 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.0 |
| ce098466-7a39-3066-94cf-f83beaf8381f | -19.5804 | -57.0281 | 2024-10-18 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.4 |
| d993c28b-f208-33cf-9fe4-3a67dd4b7766 | -19.6005 | -57.0253 | 2024-10-18 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.1 |
| 9085dbce-3a95-3190-bc27-aff5b28586dc | -19.6009 | -57.0044 | 2024-10-18 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.6 |
| a0ca2a55-4234-317d-a567-73a6b3aec349 | -19.6202 | -57.0435 | 2024-10-18 03:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.4 |
| b2f6f55a-c9dc-34ff-929b-029b7041d60e | -19.6206 | -57.0225 | 2024-10-18 03:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 380.3 |
| b1cb6f1c-09d5-35c4-8021-eba04b11ddc5 | -19.621 | -57.0016 | 2024-10-18 03:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 198.9 |
| 5759be76-beb7-3c78-b7be-dc6585d23cd6 | -3.53401 | -43.61569 | 2024-10-18 03:51:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ca5676ca-a4ff-357e-8037-396339d1da70 | -4.48158 | -42.88557 | 2024-10-18 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 868a8b9b-6c1f-3bf9-a4c1-93575614c849 | -4.36148 | -43.85535 | 2024-10-18 03:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03c605b1-5b99-39d0-a5d5-2fbffb3c7a2d | -7.63484 | -34.8587 | 2024-10-18 03:51:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b065e011-a593-3443-bd24-0811ef903e7d | -7.31264 | -38.12774 | 2024-10-18 03:51:00 | NOAA-20 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0460ab46-80bc-3009-9e9d-13ed30f1bf49 | -7.30933 | -38.12722 | 2024-10-18 03:51:00 | NOAA-20 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| adcd4ec1-c58c-364e-9bbd-a4e175c36baa | -7.28314 | -34.88418 | 2024-10-18 03:51:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ac85df35-c520-3963-887e-15133c8b7a50 | -7.00115 | -38.76997 | 2024-10-18 03:51:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 351ff086-6d8b-3210-9208-b7a5b47617c6 | -7.0006 | -38.77343 | 2024-10-18 03:51:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ba06db22-5bd7-3d00-bacf-46c190cbab03 | -6.75354 | -39.26165 | 2024-10-18 03:51:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c01b7ff1-d1af-321f-a7c0-205ffdc0f6c8 | -6.75187 | -39.18607 | 2024-10-18 03:51:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 8f462acf-0eeb-39f9-ae49-5b212dafe1b5 | -6.69566 | -37.48881 | 2024-10-18 03:51:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c93db359-d1dd-39c8-9d11-7b213d52b0fe | -6.57114 | -35.12236 | 2024-10-18 03:51:00 | NOAA-20 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 54c9c164-b97e-33c6-b0d6-a24638717935 | -6.57051 | -35.12658 | 2024-10-18 03:51:00 | NOAA-20 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 11b9686e-beee-3600-b88b-fd2cb06b26d3 | -6.54323 | -43.03741 | 2024-10-18 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 765ddf2a-774c-34c9-9781-f1b090724b10 | -6.5424 | -43.04242 | 2024-10-18 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8965f6ca-ffe6-3556-a9eb-2a536005ce79 | -6.54015 | -35.15644 | 2024-10-18 03:51:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 9f4c7eb6-e9ab-34e0-8799-8e795ff8309f | -6.53952 | -35.16066 | 2024-10-18 03:51:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| e172cf0c-4226-3122-8223-aca04087973f | -6.53929 | -43.03679 | 2024-10-18 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b53b976-9f46-3a2a-8c3e-fb89ae34528d | -6.53847 | -43.0418 | 2024-10-18 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c050b3ca-b848-3a76-a17d-52d67345fd20 | -6.53716 | -35.15164 | 2024-10-18 03:51:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9c134b5c-9f36-3ae0-bdf5-c4b0d01ec65d | -6.53653 | -35.15587 | 2024-10-18 03:51:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 54d647b3-aaed-3d8f-b980-41fb6d3f36ac | -6.53591 | -35.1601 | 2024-10-18 03:51:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 5305781a-09f0-3caa-840f-002e0bff8be1 | -6.40526 | -39.73975 | 2024-10-18 03:51:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 514d6bf1-84cc-3cff-9289-81a2d0f68451 | -6.40499 | -35.33704 | 2024-10-18 03:51:00 | NOAA-20 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 431c3bf5-f280-3491-bbf2-2c380c627841 | -6.33695 | -39.31446 | 2024-10-18 03:51:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 59c1fd1d-195e-3758-a609-73e8fce8b55c | -6.19194 | -42.72663 | 2024-10-18 03:51:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d0f4e9c0-a895-3f29-9adc-93ff83bf5d8e | -6.18957 | -42.72333 | 2024-10-18 03:51:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 374334cb-2c66-33a7-b49b-89f951994dc0 | -6.18807 | -42.72598 | 2024-10-18 03:51:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ddc786e5-fb61-3cf4-a2b1-5db29d675578 | -6.18451 | -43.41356 | 2024-10-18 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57eff4d1-4602-3d61-b338-ecdc4edb1e77 | -6.18046 | -43.41295 | 2024-10-18 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97df2b15-c2c9-3697-b226-084f229e615f | -6.09138 | -43.93005 | 2024-10-18 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 460f169e-8420-360d-a673-6506ca7cc22c | -6.0891 | -35.11658 | 2024-10-18 03:51:00 | NOAA-20 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c0952116-24ed-30a4-a0f3-a1f487118ff8 | -6.08719 | -43.92933 | 2024-10-18 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1c1b874-3b47-38f0-b639-adb5cad3d5df | -5.96186 | -43.3724 | 2024-10-18 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README24.md)
