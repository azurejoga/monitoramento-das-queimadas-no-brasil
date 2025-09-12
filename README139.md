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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 807bde60-0c9c-3ca9-a534-2c9641436ed7 | -11.9904 | -51.1618 | 2025-09-12 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 247c9fe8-1b24-320a-a41b-ead4f64fe63f | -8.9368 | -46.132 | 2025-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 8695e8a6-d678-388b-a2bd-3ddd59314392 | -15.5822 | -54.7429 | 2025-09-12 14:40:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 239.5 |
| b54ab053-31bf-3375-90c3-42cbcd79e6e9 | -14.7397 | -59.6989 | 2025-09-12 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 98ba17cb-5fa9-3c84-8bab-0519727da66c | -12.8649 | -62.1268 | 2025-09-12 14:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 66f6e9ea-a39a-307e-ae9c-724a78942cd2 | -8.0963 | -45.5414 | 2025-09-12 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 71f9e9b2-4a8f-3287-b93f-23288ef0c9e6 | -8.096 | -45.5641 | 2025-09-12 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 1c870f14-99e7-38f6-9681-3e6b4b5e1561 | -9.3436 | -45.3853 | 2025-09-12 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 1f2caafa-56a9-3ff1-b22c-e945ef62ea9c | -9.7703 | -45.9937 | 2025-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| db69e1bc-b8b4-3edf-a92b-542a6d04a139 | -8.8765 | -51.1321 | 2025-09-12 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 7a76b7eb-d5ed-3f41-a7db-1ff7629355d6 | -10.9092 | -47.2247 | 2025-09-12 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e46f0d66-3329-3655-accb-8e0a5e05e2b8 | -6.1923 | -42.6205 | 2025-09-12 14:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 113.6 |
| 61a2dd36-b525-3c7e-b510-4fc61567bc75 | -9.5135 | -54.6494 | 2025-09-12 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| f30ce7fd-7a4c-32cb-85da-aab1763eeb5b | -9.0791 | -49.8211 | 2025-09-12 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 4393b6b7-dec7-3736-985b-84a31dd1b417 | -10.8972 | -45.58 | 2025-09-12 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 78e3f899-5955-3d7e-8581-031b0045f8e6 | -9.0748 | -47.1224 | 2025-09-12 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 312.2 |
| 0d53519b-96ef-32af-b455-67cfbf886763 | -10.4252 | -50.6078 | 2025-09-12 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e33f0207-1028-3665-ab32-d9d65ca9f310 | -7.542 | -44.6844 | 2025-09-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| e3970db4-c57d-3185-bf27-e6b5b13de06f | -9.0166 | -45.8077 | 2025-09-12 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 7a8ddf44-5fb0-397a-994c-c2cf7861d34e | -11.795 | -51.5229 | 2025-09-12 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| e3edc0a9-cd7a-3b02-a333-bd3795c369b2 | -9.9571 | -50.3353 | 2025-09-12 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 168.0 |
| c3f97128-c57a-35db-bf00-89a1aaa509d5 | -9.9568 | -50.3566 | 2025-09-12 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 34828e56-7317-3bc7-bf25-f45551eac1bd | -8.9371 | -46.1094 | 2025-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 30d61e28-929a-3fed-8d06-bf04362d4a67 | -8.8768 | -51.111 | 2025-09-12 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| c8506079-a465-3665-aca5-fa0bb58b842a | -9.1162 | -49.8604 | 2025-09-12 14:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| b9b37db8-ad4e-340d-b11a-645520cfab7c | -12.9289 | -54.7744 | 2025-09-12 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 070c4980-d246-3829-a38d-c278b2847839 | -6.2595 | -43.4129 | 2025-09-12 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 5251a507-a22e-33f2-bea8-7f0300587be8 | -9.057 | -47.0355 | 2025-09-12 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 44ee7ceb-92df-3152-8961-165f12bcb063 | -7.5232 | -44.6862 | 2025-09-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 60d8fa28-c5b2-3c2d-b7de-e27ff19aeee0 | -8.9938 | -46.1034 | 2025-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 188.8 |
| a1d7d127-5322-353c-b751-3891f2b21d7b | -9.3433 | -45.4082 | 2025-09-12 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| f1e39964-f09f-379d-a8e0-22a4b80fa84b | -6.8281 | -52.8143 | 2025-09-12 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 809ed38d-6337-3439-b017-73ef4adde0cb | -9.0373 | -47.1041 | 2025-09-12 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 9ee3550f-4f44-3633-94e3-05d128610a4b | -7.5641 | -44.4068 | 2025-09-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 139.2 |
| a377fcf6-0c73-389d-b548-ec5554441bcb | -10.0947 | -47.1441 | 2025-09-12 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| b771e050-dc59-33b3-872f-0beb1f3a5c25 | -5.9466 | -42.7825 | 2025-09-12 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| 1c1da4d5-b71a-3104-a9c7-cf7eea50e3d9 | -8.3727 | -47.589 | 2025-09-12 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 3a22daef-33bc-3a0d-9a70-fd62c2748b95 | -7.3212 | -49.6255 | 2025-09-12 14:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 586378a6-e9e8-39c3-ac0c-a9f24d3d6e1e | -9.72 | -46.8749 | 2025-09-12 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 21309744-59da-36db-bfcc-94e352d2f2bb | -7.4511 | -44.4177 | 2025-09-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| cf5e975e-566d-3411-8210-457ed904e265 | -9.5324 | -54.6277 | 2025-09-12 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 316.6 |
| b10ab03b-8a8e-32e5-8010-cb80030406e4 | -15.0453 | -48.0982 | 2025-09-12 14:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 1eca9b90-926b-35fe-bf90-2604c6be5744 | -14.1912 | -46.1782 | 2025-09-12 14:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 129.6 |
| b9e3318b-de01-3027-a7aa-ba966c12af98 | -9.0172 | -45.7624 | 2025-09-12 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| b684d792-3883-3a68-b256-9c4b2aae6a50 | -6.166 | -43.374 | 2025-09-12 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 4cf65ff8-4033-3bad-92de-88ca1258c60d | -10.1216 | -47.9154 | 2025-09-12 14:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| ead2c304-55e5-338d-97ee-af4b979fa9d7 | -6.199 | -45.8186 | 2025-09-12 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f181f41e-562f-3cd6-b753-2412df5b6153 | -9.0793 | -49.7997 | 2025-09-12 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 8fa9059b-39f1-3e46-83ce-6fe290e8ba94 | -8.9563 | -46.0849 | 2025-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 1ed6b4a7-4386-3583-8a5a-5a5f5b2bb8e2 | -10.9089 | -47.247 | 2025-09-12 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 6338060a-0b38-37d6-8b72-aa07f6e61e02 | -15.1058 | -47.9983 | 2025-09-12 14:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b059c10e-af50-33d4-bd1b-518d7fb6c7c4 | -11.5422 | -50.6161 | 2025-09-12 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 524.8 |
| 0e97d057-f82a-331f-be70-59178076fffd | -9.0759 | -47.0335 | 2025-09-12 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2bb66eaa-5707-32e9-b320-8c1f8f4c50c7 | -12.0849 | -47.6065 | 2025-09-12 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 0bfdf5e2-cb90-3dd5-9225-3e7ddac2236e | -7.3954 | -44.3539 | 2025-09-12 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1a428f54-7007-3fc7-b4bd-2d2b5afbc31c | -8.4705 | -47.2712 | 2025-09-12 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2aaa673a-e4b7-3a9c-a39c-4b9d55da35bd | -10.0717 | -46.116 | 2025-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 31531a55-2de3-3b1e-a09b-ef6e926f92e2 | -11.6626 | -46.5884 | 2025-09-12 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 227.1 |
| ebf73930-0d9a-32c8-a0f0-c4417b642de0 | -9.9004 | -51.8811 | 2025-09-12 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 115dbb80-b145-383a-812b-060c77ddeaee | -10.6979 | -48.6612 | 2025-09-12 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 9a45793e-73ab-37f6-9870-290063d1a96a | -11.5232 | -50.6182 | 2025-09-12 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 6ae4452d-5ff2-35f4-a15f-b0604b8aec3e | -8.4893 | -47.2694 | 2025-09-12 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0db7bad4-e7d3-36e6-ba82-38639527e621 | -17.9332 | -44.4413 | 2025-09-12 14:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 57d59d5d-7c8b-351b-ba71-7efc03694c4c | -10.4441 | -50.6059 | 2025-09-12 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |


