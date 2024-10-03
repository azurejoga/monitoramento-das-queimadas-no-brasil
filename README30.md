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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfe18d94-d418-3324-8945-3f0c8d536f37 | -9.1713 | -48.761299 | 2024-10-03 01:05:09 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| eeb01417-304a-395c-9f3d-f09f34ae130c | -10.4132 | -54.222698 | 2024-10-03 01:05:09 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c76fd76b-3713-3236-8c40-7dafdf87a279 | -10.4034 | -54.224899 | 2024-10-03 01:05:09 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4b0cc8b-c57c-381a-8047-16cfbe354ddf | -7.6944 | -42.986198 | 2024-10-03 01:05:10 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7131c66a-c309-3f0a-b855-8f92badfcb6a | -9.1376 | -48.9669 | 2024-10-03 01:05:10 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8c9be0c-fd5f-305e-8d26-980c794c3be9 | -8.4311 | -46.299301 | 2024-10-03 01:05:11 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b0090e1-f29f-33f8-bb21-543cecd2adaf | -9.7653 | -51.928902 | 2024-10-03 01:05:11 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7229f7a-537b-331a-b7ff-71489c98a116 | -8.4214 | -46.301701 | 2024-10-03 01:05:11 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14039d95-035b-3b46-a74c-e76d40627795 | -10.017 | -53.409401 | 2024-10-03 01:05:12 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7f337c0-06fa-39c2-bf68-fd651cbdfd8e | -10.0186 | -53.416599 | 2024-10-03 01:05:12 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6398cad-612f-3065-bead-f5926e044357 | -7.7476 | -44.0481 | 2024-10-03 01:05:13 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1cbe3a6-bc40-3c05-bf6c-46305de39020 | -7.7527 | -44.027699 | 2024-10-03 01:05:13 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57bac519-1f05-35b0-ae04-e8fa0c2a1708 | -7.743 | -44.030201 | 2024-10-03 01:05:13 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f26697a-7030-3b25-8042-b0a57a04612d | -8.8516 | -48.936798 | 2024-10-03 01:05:15 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b37eb3e0-629a-38eb-b4a4-d988309f6c3f | -9.0286 | -49.816898 | 2024-10-03 01:05:15 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44f7a937-7907-3f6d-abf9-1d6f1d9a2187 | -9.2893 | -51.068298 | 2024-10-03 01:05:16 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5d66cf0-9df0-3fd3-812e-4641483f3450 | -9.7572 | -53.1679 | 2024-10-03 01:05:16 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d4a0c48-3d11-3917-ad8d-6830de0c618e | -9.4624 | -52.092499 | 2024-10-03 01:05:17 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12df6ff6-060c-3655-bcfb-08392b22788d | -9.464 | -52.0994 | 2024-10-03 01:05:17 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e1ffa73-c4ca-35d2-b7e1-ded2603f6856 | -11.2453 | -60.582802 | 2024-10-03 01:05:17 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 161b684d-ab91-3fca-906e-ed9ac041d77e | -11.2491 | -60.601898 | 2024-10-03 01:05:17 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f52cc259-945b-3f97-8e6d-16b989e85515 | -11.2356 | -60.584702 | 2024-10-03 01:05:17 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c514aaa1-a4ae-3ff4-a1ea-8156c2d799db | -9.6117 | -53.207901 | 2024-10-03 01:05:18 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b0b648-aec3-3eb5-8a7e-83ffe74e2a0c | -9.6329 | -53.5783 | 2024-10-03 01:05:19 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14d7fadd-a23b-303a-925c-a55845e60f60 | -10.7013 | -58.547798 | 2024-10-03 01:05:19 | METOP-C | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6849904d-a7ea-324c-8f70-990a5b9423c1 | -8.7523 | -49.783501 | 2024-10-03 01:05:19 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd2c2cd-d394-3ae0-8c70-05203fcf0511 | -10.6915 | -58.549801 | 2024-10-03 01:05:19 | METOP-C | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1a4c4fb-8dc7-35ac-97ec-2ff6600f433f | -10.6943 | -58.563301 | 2024-10-03 01:05:19 | METOP-C | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40745bb2-f259-36d4-b9c7-8f8417f28f9e | -9.1139 | -51.515598 | 2024-10-03 01:05:20 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42811cd4-126a-3930-ab1d-c185ca78cffa | -9.1155 | -51.522598 | 2024-10-03 01:05:20 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c7775ac-5175-30b8-a8ae-a7c6259a2741 | -4.4701 | -42.878201 | 2024-10-03 01:05:22 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fd0e461-0595-30ac-a51d-6fbd74c184f6 | -4.4762 | -42.9025 | 2024-10-03 01:05:22 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63734e86-d6fe-3ade-9b71-62ade5aef923 | -4.4605 | -42.880501 | 2024-10-03 01:05:22 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d70c6437-53e7-374b-a235-ac585ca5b680 | -4.4666 | -42.9048 | 2024-10-03 01:05:22 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55f17da5-0ec2-3f2e-8ae9-789f41fb9dea | -10.168 | -57.264599 | 2024-10-03 01:05:24 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 578fb560-8c24-30fd-bd93-a764ca650129 | -10.1703 | -57.275501 | 2024-10-03 01:05:24 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c345359f-6e31-36b7-954b-553da8dbd3e7 | -10.1727 | -57.286499 | 2024-10-03 01:05:24 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbfd3ae1-4c59-392a-92a1-498220fed284 | -10.1606 | -57.277599 | 2024-10-03 01:05:24 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4853e0b-9bac-3bbe-b523-217f9c68b5b7 | -3.404 | -42.2858 | 2024-10-03 01:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 4a08ba0e-367b-3156-b3c5-9170683e4345 | -3.4042 | -42.2621 | 2024-10-03 01:05:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e4950940-4c13-3d3d-a288-d00aa52e41da | -6.871 | -43.5877 | 2024-10-03 01:05:25 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d8f5b6d-0ea1-3f4e-8231-4d8e721710db | -6.876 | -43.607601 | 2024-10-03 01:05:25 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 70831262-e958-3fbb-9c3f-d2e9cd0997a0 | -6.8809 | -43.6273 | 2024-10-03 01:05:25 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9e6a1e1f-d981-352a-b97d-cd24bf21c155 | -6.8663 | -43.610001 | 2024-10-03 01:05:26 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e6c9fd04-6cc4-3d82-b419-62a1decfe9b2 | -8.258 | -49.700401 | 2024-10-03 01:05:27 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 782f2eb8-931a-3484-8f97-9d8cd5f0981b | -8.9672 | -52.815701 | 2024-10-03 01:05:27 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 728c6eff-3466-3890-b265-994891f5294d | -9.0666 | -53.256001 | 2024-10-03 01:05:27 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 274c368e-b1c0-3683-b978-ec72f1910bd1 | -9.0682 | -53.263 | 2024-10-03 01:05:27 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2740b7da-a886-3820-ac30-787da6e627db | -8.9527 | -52.7971 | 2024-10-03 01:05:27 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ecfe997-a019-396d-9015-1115205c9312 | -8.9543 | -52.804001 | 2024-10-03 01:05:27 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d64b96f-7bea-3145-a2fc-ee781f3e3143 | -8.2398 | -49.7547 | 2024-10-03 01:05:28 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd8e845-c901-3a8c-b3ea-ceb79c16db17 | -8.2416 | -49.7626 | 2024-10-03 01:05:28 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a923cb51-f411-3228-b033-cf8917744133 | -8.2435 | -49.7705 | 2024-10-03 01:05:28 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 839972cf-6fb5-334e-bb0a-018bf8044da6 | -8.5232 | -50.967602 | 2024-10-03 01:05:28 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46f5c342-ba4e-3cec-b3cd-fd7fde007937 | -8.5248 | -50.9748 | 2024-10-03 01:05:28 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b53be3a7-b26d-398f-a817-8fb64bd65379 | -8.5265 | -50.981998 | 2024-10-03 01:05:28 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72d10a75-b996-3135-8dd6-226f0504912c | -8.2318 | -49.7649 | 2024-10-03 01:05:28 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b130cf1c-584d-3fe9-a109-f5648eb0263f | -4.0949 | -48.4894 | 2024-10-03 01:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 00bde969-60da-387d-a904-c124709938be | -4.095 | -48.4679 | 2024-10-03 01:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 24692bef-3e01-3c4a-b6de-0fef18131e62 | -4.1134 | -48.4886 | 2024-10-03 01:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 48861f0e-23c1-342e-bf58-ee763c5c5e7d | -8.401 | -50.752602 | 2024-10-03 01:05:29 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0005a489-0f52-339f-b433-1c480989a3ea | -8.4026 | -50.7598 | 2024-10-03 01:05:29 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4a9d23b-d065-31c4-a2f9-bf9ef2e0e758 | -8.0816 | -49.521599 | 2024-10-03 01:05:29 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff09843-cb3a-32c0-abe8-56caa8a08f04 | -8.0835 | -49.529701 | 2024-10-03 01:05:29 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c91d94a8-c1f9-3ef3-9051-0f0b9b589094 | -5.2234 | -47.955399 | 2024-10-03 01:05:30 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88852f9a-4db2-3267-8c7d-ec08d3428854 | -5.2136 | -47.9576 | 2024-10-03 01:05:30 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6d17f9e-de31-30d7-8a37-f3a054e7f4e1 | -4.4657 | -42.8877 | 2024-10-03 01:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 6036a433-ab99-3969-a93e-7e088037277a | -4.4844 | -42.8866 | 2024-10-03 01:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2f887fef-1440-394e-8430-7e6f569df32f | -4.5373 | -43.3273 | 2024-10-03 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 0b0837a1-f6d5-3ceb-aa5e-d165d5de2d81 | -4.5375 | -43.304 | 2024-10-03 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 158.9 |
| d40b11d3-393a-3e7b-b70c-de3dda26056d | -6.9944 | -45.487598 | 2024-10-03 01:05:31 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b3ccb34-e7ae-3aed-972d-33797687679d | -6.9981 | -45.5023 | 2024-10-03 01:05:31 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b07429d8-d779-3e7d-8d70-845a0d69a10f | -8.2841 | -50.871201 | 2024-10-03 01:05:31 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb4b2ff-a020-3f89-bca5-8fbe6938c61e | -8.2858 | -50.878502 | 2024-10-03 01:05:31 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e6d3af1-f39c-3777-8c6f-72669d6166e8 | -8.184 | -50.4855 | 2024-10-03 01:05:31 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba133ada-5b77-3518-884c-9ccd955e22e3 | -8.1742 | -50.487801 | 2024-10-03 01:05:31 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3225d35-f269-3094-85b6-75607ebd44fd | -8.1759 | -50.495201 | 2024-10-03 01:05:31 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6a68e59-364f-33aa-9991-f98111627c35 | -8.4524 | -62.644798 | 2024-10-03 01:05:31 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fbf4260f-6f4f-3492-a77a-a1618d2536c1 | -4.6723 | -45.8773 | 2024-10-03 01:05:31 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e31e70a9-217d-3043-8479-ca403eaf8a52 | -4.6759 | -45.8923 | 2024-10-03 01:05:31 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cfc2c92e-73ce-3faf-a271-7d53af3a5f5e | -8.1676 | -61.360298 | 2024-10-03 01:05:31 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1238fb01-9177-3f33-a56f-7b587a66ee0c | -4.58 | -48.0132 | 2024-10-03 01:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 1c3a9294-e0d3-3771-b770-289216cd46a0 | -10.38 | -61.2048 | 2024-10-03 01:05:33 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f241c80d-8fb7-38b2-a6f3-21fd6abc6c7f | -6.6363 | -54.944 | 2024-10-03 01:05:33 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0479ee10-de58-3b6c-a18f-f0323cd7f36e | -6.638 | -54.9515 | 2024-10-03 01:05:33 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a102fcc1-3019-304a-bc58-0243aa3e7ba6 | -6.6397 | -54.959 | 2024-10-03 01:05:33 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 075226e7-20ce-32ea-8576-2b130999ad2f | -4.9264 | -43.79 | 2024-10-03 01:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| cbffe077-7c9f-3c7b-9796-506f89e75138 | -4.9265 | -43.7669 | 2024-10-03 01:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 1d3e6d60-8739-3155-b2aa-21ea06e4a790 | -7.4183 | -47.8638 | 2024-10-03 01:05:34 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 933a0f84-342a-3a5e-8cc4-45d92a7830fe | -10.3703 | -61.206699 | 2024-10-03 01:05:34 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47e03ead-f641-399d-ab4c-47af3ef73858 | -7.4086 | -47.866199 | 2024-10-03 01:05:34 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa2f527e-34d3-3ef4-a205-4ad53e85d85a | -10.8845 | -63.887299 | 2024-10-03 01:05:34 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 70d246ac-2e69-3ddc-a5ec-2eb4b9ece45a | -7.1414 | -46.930901 | 2024-10-03 01:05:34 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d90807be-ee19-30ca-8ab9-ee2009a43276 | -7.1442 | -46.9426 | 2024-10-03 01:05:34 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8c0331b-8f48-3e6f-be2a-443251e0b038 | -5.2441 | -43.8151 | 2024-10-03 01:05:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 2c47a709-3bf7-3953-8ed3-b7a5a51241b6 | -5.2443 | -43.792 | 2024-10-03 01:05:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 159.9 |
| eca95360-a8c0-36ec-af4c-54f06e04cb1e | -7.1316 | -46.933201 | 2024-10-03 01:05:35 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| caf7260d-ec6a-3fdc-80bf-1a97be6f0dfc | -7.7965 | -50.064499 | 2024-10-03 01:05:36 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7403849d-664a-3995-bc78-a59d139c7427 | -7.7347 | -49.889599 | 2024-10-03 01:05:36 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfd80a03-d221-3c27-aea3-beedb535f4e7 | -7.7366 | -49.8974 | 2024-10-03 01:05:36 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README31.md)
