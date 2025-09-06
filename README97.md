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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5e089f3-b844-38a3-865c-ab966cb33a5c | -6.2296 | -42.641 | 2025-09-06 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 874ed24b-45bd-3ff0-a34a-3e21e00a668a | -5.5508 | -45.1438 | 2025-09-06 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a3526e90-24d9-3a46-acb2-8d9011e15d09 | -6.2205 | -43.5558 | 2025-09-06 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| bf19338f-3010-33d0-a0dd-08d6af7a97bd | -6.267 | -53.4582 | 2025-09-06 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 4a69fefa-dae9-3150-978d-32db40b3d117 | -9.0951 | -47.0093 | 2025-09-06 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 6b1cb47f-845c-3dcb-b9f1-d0a3b5d852ee | -9.3753 | -62.3518 | 2025-09-06 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 76f8a720-9c0d-3818-be27-272417bae2ee | -6.1945 | -53.2381 | 2025-09-06 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| dbde9c89-e89c-3f8d-b837-227d97f6cb80 | -13.0353 | -48.0521 | 2025-09-06 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 70ffc68b-7591-327f-b0b6-10e2709ddc59 | -6.8841 | -44.7215 | 2025-09-06 14:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| d961e8c3-e413-3f77-8223-3fb5d6cf4425 | -6.2857 | -53.4369 | 2025-09-06 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f69f5bb6-c589-3223-aeb1-e2b2d4a6243b | -13.3178 | -51.7477 | 2025-09-06 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 22a1e0b7-8336-36bd-ae3d-677d5784c9f1 | -10.1453 | -55.1674 | 2025-09-06 14:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 258b3fc8-aeb8-3fae-9d4d-28b07a3cb58f | -10.7372 | -48.5693 | 2025-09-06 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| b9f56388-d04f-3113-8aef-e84ebad75d24 | -5.7183 | -45.2226 | 2025-09-06 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 64c11213-89ee-3755-9d86-6d8a8ac07b74 | -8.099 | -45.3144 | 2025-09-06 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 25023b99-bc4f-3521-9de6-d13cf1f4f74a | -3.3442 | -42.994 | 2025-09-06 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 0d3aac00-57a5-3031-a10f-691f40eb26c1 | -15.3258 | -52.7182 | 2025-09-06 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 4e38ff6b-40e0-3121-9be3-09dd66bfc498 | -6.4021 | -46.0944 | 2025-09-06 14:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 592e7ab6-7e44-3696-b9a7-a49b8829e9a5 | -16.3345 | -52.9387 | 2025-09-06 14:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 148.7 |
| c9e24114-069c-36c5-849f-602ebd06c07c | -11.2295 | -46.2403 | 2025-09-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 278374bb-9e11-33ee-b036-7cdb7fcca0eb | -13.0157 | -48.0771 | 2025-09-06 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1510acd3-fa87-361a-9a52-50ebbfacc79c | -9.4497 | -62.3485 | 2025-09-06 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e55aa4f9-f01b-3539-ae5c-06b01a4b61fc | -13.8602 | -46.2566 | 2025-09-06 14:30:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 28a4af3b-5d06-37a2-ad94-451ac4687a69 | -6.5141 | -42.4028 | 2025-09-06 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 317cbbe6-e457-3495-a9c1-effa6c3e6e83 | -11.2651 | -46.3938 | 2025-09-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| bd588f2f-413d-392b-96e0-aca05dd05ee4 | -8.0988 | -45.3371 | 2025-09-06 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| e26a093c-f77a-3117-b9ee-ec21a5476c18 | -8.4511 | -47.3173 | 2025-09-06 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 89483102-c8cd-3958-ba20-1fe523c7f90a | -6.8466 | -52.8132 | 2025-09-06 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| cca4afe6-2147-385c-83d7-f045e771dd7d | -11.3567 | -50.3161 | 2025-09-06 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| b496cd94-fb46-3f87-8d6c-7bcb1b2c3328 | -6.7419 | -51.975 | 2025-09-06 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 471.7 |
| e7cb52ed-dac3-345e-96c3-1411f2d418ab | -11.0055 | -45.9527 | 2025-09-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 1e2f0920-49c3-31be-9885-4ca952c391fc | -8.4829 | -62.6927 | 2025-09-06 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.2 |
| aee10ed0-ed9c-355a-bb1e-9ed20d186ec8 | -13.0041 | -54.8487 | 2025-09-06 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c9225a4e-e0e1-342f-ad00-ed7493de5c3d | -6.7421 | -51.9543 | 2025-09-06 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 7fc134d3-34c1-3522-8549-759cf2f7d7f6 | -6.1944 | -53.2585 | 2025-09-06 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 188.1 |
| 90308974-b8bc-33c5-92ce-fb3322731c72 | -15.3067 | -52.6995 | 2025-09-06 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 226.1 |
| cf5d22ad-37f6-3cb8-b6a7-af3a53480823 | -15.7186 | -53.5743 | 2025-09-06 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 276.1 |
| 2baf6a9e-9ac8-3807-90dd-265eee31da4e | -9.0596 | -62.3466 | 2025-09-06 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 8ceef607-2bcc-3fd2-93a3-e9c8fdecd68e | -15.5363 | -49.8165 | 2025-09-06 14:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 553969a3-b1b4-355b-a155-913630a87916 | -8.0223 | -45.4354 | 2025-09-06 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 423a5445-fe78-3e68-9e2a-30da9d9bee2f | -5.7298 | -43.9189 | 2025-09-06 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 165.2 |
| da84efff-262e-36ce-bdb5-506dbd853b53 | -15.719 | -53.5532 | 2025-09-06 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ede94a04-6b21-375e-bf65-6f78b8b929d5 | -9.4495 | -62.3675 | 2025-09-06 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| be0d12a2-5f29-3e53-9b15-63f4c71691fa | -14.4364 | -48.4421 | 2025-09-06 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 194.0 |
| e101046b-0b35-3b79-8ebb-041262b1b95a | -15.7377 | -53.5928 | 2025-09-06 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d0dd695f-c507-3a1e-a7c1-d48e43a987b0 | -5.5882 | -45.1412 | 2025-09-06 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 8975b092-202c-3a64-9db7-a74b4b3e1501 | -5.8485 | -45.3038 | 2025-09-06 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 882db9da-223b-32cb-8903-2970f691abe1 | -6.8844 | -44.6987 | 2025-09-06 14:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 025b5653-6133-34e2-8e1b-98ab49f525b6 | -11.0245 | -45.9502 | 2025-09-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.4 |
| c0d2e8fb-0531-31ea-b9a9-9bfeaf370dcd | -6.2299 | -42.6173 | 2025-09-06 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 702b266b-efdf-3d83-8996-3a05f4f60dfe | -7.7068 | -50.2977 | 2025-09-06 14:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 80931721-221f-30d6-a7ed-fa12181051a7 | -8.4831 | -62.6549 | 2025-09-06 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| e1d0bacd-b58c-3991-a0de-160f19ff2eb4 | -5.7923 | -45.3078 | 2025-09-06 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3eb72488-1fed-3c12-b5d3-6d933e8abcb4 | -11.2302 | -46.1949 | 2025-09-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| d920f75e-5347-33a7-937b-733f0f266983 | -11.319 | -50.2989 | 2025-09-06 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 70a8c79a-e57e-3707-81c2-4db77f3d0c9f | -13.8006 | -52.7454 | 2025-09-06 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 9630ec05-9374-30c2-b18f-4b645d891c58 | -6.8465 | -52.8337 | 2025-09-06 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| d5568fb7-b80a-3024-b1a8-74c750fdb8a3 | -10.1453 | -55.1674 | 2025-09-06 14:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 7065a481-e925-31cb-b729-e371fb939e79 | -10.8947 | -50.8356 | 2025-09-06 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 136.7 |
| b8bd0252-f6a2-3ce7-910f-d69b08d375e5 | -11.2302 | -46.1949 | 2025-09-06 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 209.8 |
| 165fba9c-33dc-3611-9f91-e97147959f33 | -7.3838 | -50.9116 | 2025-09-06 14:40:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b44b282d-7348-3480-bb70-6c33b4c99fd8 | -11.0055 | -45.9527 | 2025-09-06 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| defd2137-5c1c-3f23-aa54-10e32fc65e68 | -7.7068 | -50.2977 | 2025-09-06 14:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 13c1a285-2337-33d3-a3a0-07ae832f5ee4 | -10.7872 | -47.7501 | 2025-09-06 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 022195f9-de09-3d94-948c-90d6a1b6b6dc | -16.307 | -58.1055 | 2025-09-06 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 7b727c17-2182-3f85-b8f3-6cc0b04c0070 | -6.1945 | -53.2381 | 2025-09-06 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 4fd1c6c7-38bd-382d-9a80-183bc718a89e | -5.8877 | -45.0972 | 2025-09-06 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| abc336bd-5e00-319b-998c-c117894a0b5b | -11.0245 | -45.9502 | 2025-09-06 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 265.9 |
| 61324e20-3919-3c4a-bbab-3864c3c8fc17 | -12.967 | -54.7705 | 2025-09-06 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 69d5b78f-fd75-3780-a268-08841fb52ee9 | -6.4021 | -46.0944 | 2025-09-06 14:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| a2769b44-92c5-33f2-b53a-ae7a6de9ddc7 | -5.641 | -45.5214 | 2025-09-06 14:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| f034c609-9ec2-32ed-a6fe-5522fc646325 | -8.099 | -45.3144 | 2025-09-06 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| dd55e692-2be5-33a1-90c7-96b2cdc810da | -6.9942 | -44.9629 | 2025-09-06 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| c2025739-95d4-304c-9e7f-c951601788bd | -9.4497 | -62.3485 | 2025-09-06 14:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3f622b46-32e6-399b-8086-b066c1c22835 | -6.8844 | -44.6987 | 2025-09-06 14:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 232.5 |
| 2ed2443f-e910-399c-84bd-0b86d9ee7953 | -15.3258 | -52.7182 | 2025-09-06 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 6e1806ec-8b8a-3822-82dd-2f5e6dc4afa1 | -20.2016 | -44.872 | 2025-09-06 14:40:00 | GOES-19 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 103.3 |
| ac2daa2d-3c63-351c-91c6-2bdd87013f66 | -6.2108 | -42.6426 | 2025-09-06 14:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| b0987c9d-6a06-3150-ac74-5418fd92cb6d | -9.4621 | -60.5297 | 2025-09-06 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| b2647e13-88ff-31ae-96ac-0995ad7635d7 | -5.4579 | -42.8911 | 2025-09-06 14:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 8fa69939-431c-3ed3-aade-569eb5cb87d8 | -5.73 | -43.8958 | 2025-09-06 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 7698c9ee-8e1e-3472-b775-55679cd8bc67 | -15.7182 | -53.5954 | 2025-09-06 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 89ac9425-5ed6-369d-ab02-2025983af093 | -10.5937 | -44.331 | 2025-09-06 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 690d20e4-badc-3ad4-8a21-9651030db6b8 | -9.0596 | -62.3466 | 2025-09-06 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 152.5 |
| c48b4b75-e4fb-33fb-a7f3-020cca8507e9 | -6.8095 | -52.8154 | 2025-09-06 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 6f04618a-12de-3c27-ba82-c65a62a20adf | -13.0047 | -54.8076 | 2025-09-06 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 39c1f473-f4ef-3dc8-9beb-ed16b95ec4c3 | -9.0781 | -62.3458 | 2025-09-06 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 83.6 |
| db74b197-118f-38b7-a99a-18ca864bc2c3 | -12.9477 | -54.793 | 2025-09-06 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 2683e641-6a48-31eb-9a45-94aa4c0bf61b | -14.4698 | -56.7981 | 2025-09-06 14:40:00 | GOES-19 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 8052d9a2-7cd1-3f4d-a9fd-418bae45e90f | -5.5884 | -45.1185 | 2025-09-06 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 45d77117-57c4-39d8-9243-4c1c0f7cccf1 | -7.0129 | -44.9613 | 2025-09-06 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 278.5 |
| b6ecd98d-7d60-3989-b775-59cbc1cb59c3 | -10.3324 | -46.445 | 2025-09-06 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 192.6 |
| c8337b83-5b19-343b-95e7-2e0705282bc8 | -15.3067 | -52.6995 | 2025-09-06 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 53e11ccf-9701-36a6-aaf8-64f96f0c6c2b | -6.5065 | -44.9813 | 2025-09-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| aa0978c7-fe1d-3a99-a389-e9ede3ec511b | -9.3753 | -62.3518 | 2025-09-06 14:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 138.6 |
| f0fa01b5-7735-3a4a-b723-de56f682ebf0 | -13.0353 | -48.0521 | 2025-09-06 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| eccd5397-0dce-3af5-b838-23f5356dfed0 | -15.7186 | -53.5743 | 2025-09-06 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 225.5 |
| 41b3cd29-03f3-3150-9125-57a6acde3062 | -4.4568 | -44.1413 | 2025-09-06 14:40:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 623.9 |
| 398eb606-d437-3ac5-bd25-c6c04a1b8032 | -6.7419 | -51.975 | 2025-09-06 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 9c30398b-fa75-3c45-bcf0-618b3ebfb3d2 | -6.8466 | -52.8132 | 2025-09-06 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |


[Clique aqui para ver as próximas entradas](README98.md)
