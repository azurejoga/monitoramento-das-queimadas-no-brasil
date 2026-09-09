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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49d78aef-0b53-3c83-9cdc-ccfcb70aa50e | -3.8604 | -44.0585 | 2026-09-09 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| d792dc0c-96d3-3cdc-b3cb-a1f7aac1a193 | -6.8708 | -46.0126 | 2026-09-09 14:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 6316d50a-8a11-338c-8a38-fdae88dc0a4e | -3.2731 | -50.0741 | 2026-09-09 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 01aa4ddd-3067-3434-9da2-0080b0cc5d26 | -10.6995 | -46.038 | 2026-09-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 37b4d5af-8d05-3fc1-a9e6-60091a948682 | -3.2545 | -50.0957 | 2026-09-09 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 162.7 |
| be8dac44-a433-392b-9a49-080a95ab2763 | -9.7134 | -43.4428 | 2026-09-09 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| f8f0ae4d-ffea-3535-ae7e-09930be8b2bf | -9.7131 | -43.4664 | 2026-09-09 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 7f0bc23a-aa66-35c1-b10a-4cb8247a26aa | -10.2559 | -45.2292 | 2026-09-09 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 19b3a67d-ed41-3c1b-a851-f251e6d46f17 | -10.2372 | -45.2087 | 2026-09-09 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a76f9899-39c9-3cce-839a-d1c4b0177846 | -6.852 | -46.0141 | 2026-09-09 14:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 07285b2e-28cd-384c-b1f8-397219cbcd3b | -9.6947 | -43.4217 | 2026-09-09 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 562.7 |
| f3bcad35-659f-3508-9b8e-8599c3894cbe | -10.69 | -46.11 | 2026-09-09 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2e075b0-e969-39d0-8c10-bd8c2b36e353 | -6.8708 | -46.0126 | 2026-09-09 14:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 175.2 |
| c7692da4-250a-3e8e-9e9b-e36638e94696 | -9.7889 | -43.48 | 2026-09-09 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| b38d7add-3c50-3f5f-ac89-f7a032c6f564 | -9.7134 | -43.4428 | 2026-09-09 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 305.0 |
| 3322a0a2-3453-38a8-aeb2-2ec5acb99940 | -10.7387 | -45.9649 | 2026-09-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 5f93c66c-20c3-339c-a1a5-43c6d08c27da | -9.6951 | -43.3981 | 2026-09-09 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 275.4 |
| f8d3e7c8-e12d-3d69-89cd-14b991554401 | -9.6947 | -43.4217 | 2026-09-09 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 928.6 |
| 11a65165-1c91-394e-b990-addc7bb73ca9 | -3.2545 | -50.0957 | 2026-09-09 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a2c845c1-f72f-335d-bdf2-d877ef3aa745 | -13.6516 | -59.4734 | 2026-09-09 14:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 54a1eed4-258b-3183-8c43-2fc934a32995 | -10.7391 | -45.9422 | 2026-09-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 265.4 |
| 6ff76cf8-9890-3d44-8135-9584e795318e | -3.2731 | -50.0741 | 2026-09-09 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| da0be32e-26a0-31c6-b1cf-2fd4a90ec571 | -7.1386 | -42.129 | 2026-09-09 14:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 149.2 |
| 5f3bc87e-2c16-39fa-8eec-a5619670d7b7 | -10.6995 | -46.038 | 2026-09-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 82f81441-aba1-31b3-992c-5427ea7fbd9b | -9.7138 | -43.4192 | 2026-09-09 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 906.7 |
| 4aa99ef6-52fe-3e81-9055-d28126a31648 | -10.6999 | -46.0153 | 2026-09-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| f9dc52f8-0f63-355c-ba77-d23556192aed | -10.2372 | -45.2087 | 2026-09-09 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 4a1ac943-c864-38f5-a907-880bda9be185 | -3.8604 | -44.0585 | 2026-09-09 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 022eda0d-b7d6-39a1-b805-b06954b8c5b2 | -13.2917 | -61.109 | 2026-09-09 14:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 56075997-3541-337b-ad1b-26897765d84b | -10.2559 | -45.2292 | 2026-09-09 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 60a9ad95-084e-3df8-a17a-08ea49a32746 | -7.4693 | -46.1406 | 2026-09-09 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| b8047520-74f4-379b-b85d-7e21447f02ea | -9.7131 | -43.4664 | 2026-09-09 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 15e4ccfd-8cce-3377-9d47-bc8c8d5b3c78 | -10.7578 | -45.9624 | 2026-09-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 986b07f4-3e88-39eb-833e-a22d70eacacb | -7.1389 | -42.1051 | 2026-09-09 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 155.1 |
| 0963fe5a-509e-3d39-b7e6-b11d6299fd38 | -9.7889 | -43.48 | 2026-09-09 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 197.7 |
| eec74c04-0de8-3103-ad01-7a73ff9bd6cb | -10.7391 | -45.9422 | 2026-09-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 34fdc3d7-f89e-311d-9fe8-713051162327 | -10.6999 | -46.0153 | 2026-09-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| baeb0466-fcb1-3e57-97cc-fc0a61112ba1 | -6.8708 | -46.0126 | 2026-09-09 14:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 4fa68cde-2140-3036-bca4-f37b75b42c18 | -8.7253 | -62.4177 | 2026-09-09 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ac141145-fd08-3ae1-b8b7-eee62b0a7972 | -3.8604 | -44.0585 | 2026-09-09 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4f5c9f9f-7d46-3431-b18a-f6d603eebecf | -13.6514 | -59.4932 | 2026-09-09 14:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 87a0ad50-afde-3ce3-8583-6a26f2c7558d | -9.7698 | -43.4825 | 2026-09-09 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 207.9 |
| 6165d9da-20e2-30d4-9a3a-bae68284875f | -7.1386 | -42.129 | 2026-09-09 14:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 132.2 |
| 92c8910c-cd9d-3def-b613-8e297222e774 | -6.3307 | -43.8021 | 2026-09-09 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| bfe978d7-5611-369a-8b4b-e475ad809598 | -10.2372 | -45.2087 | 2026-09-09 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 2b538001-e2ab-39e9-b4b5-dae2574aa5ba | -9.7134 | -43.4428 | 2026-09-09 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 216.6 |
| 890c52fb-fac0-3ee7-b8d6-e6ae8a82ee8f | -13.2917 | -61.109 | 2026-09-09 14:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8253c725-b18d-38ec-b9e9-a63a1c09c2ae | -9.7131 | -43.4664 | 2026-09-09 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| eaa68fa1-5d00-317c-b93d-4772bc38379a | -9.7127 | -43.4899 | 2026-09-09 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 6a1a2ee9-772f-3090-8199-5095a48c28ac | -10.6995 | -46.038 | 2026-09-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| f4922fb9-92af-39f6-b685-b78db169800b | -10.701 | -45.9471 | 2026-09-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 57e8bcb2-721d-3c91-828f-0dfbfbf22317 | -9.7138 | -43.4192 | 2026-09-09 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 500.4 |
| b4987242-a640-355f-853c-325aeeeb6a04 | -9.7702 | -43.4589 | 2026-09-09 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| ba7b3a84-203a-3154-8e72-1be113ce7e44 | -10.7006 | -45.9698 | 2026-09-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| da80ce42-93d9-35fb-a530-fed5ef9a281f | -7.4693 | -46.1406 | 2026-09-09 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 63cc7d78-e155-325f-b3a7-1b79d17933f8 | -3.2546 | -50.0747 | 2026-09-09 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 25a658b3-cca0-313c-825b-d7d2724e6f89 | -13.6516 | -59.4734 | 2026-09-09 14:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 55345c09-6351-33fd-bf99-88136d0f7683 | -3.2545 | -50.0957 | 2026-09-09 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 5948b203-8421-37f6-a526-da728b7cf939 | -9.7131 | -43.4664 | 2026-09-09 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 59021dc4-6a5e-3adc-8283-72f63f156336 | -9.7889 | -43.48 | 2026-09-09 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 244.7 |
| 76044f68-c19f-3499-a175-7ab47d6eb39d | -10.7578 | -45.9624 | 2026-09-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| a56e5ba1-bcdf-36a6-98ef-0c7132b7307d | -9.7134 | -43.4428 | 2026-09-09 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 277.6 |
| 8a65d421-be5c-3c40-80a0-9b3ef4a45581 | -6.8708 | -46.0126 | 2026-09-09 14:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 79bf484b-1059-3c5a-8504-8090ea3fe062 | -9.7698 | -43.4825 | 2026-09-09 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 4eda2327-9f46-3ac7-b13e-0906da057657 | -10.7391 | -45.9422 | 2026-09-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 230.7 |
| 8f39cd91-596e-30c2-bd6c-049ef6e67cd7 | -13.3298 | -61.1064 | 2026-09-09 14:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 72b766da-df2e-3a77-be0e-3f6959fe5e6a | -8.6198 | -47.3672 | 2026-09-09 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5c160753-c335-3f4a-a3c5-6ef3831ca3b4 | -10.72 | -45.9446 | 2026-09-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| aca37c04-66b9-3d5d-a365-b517fd992128 | -7.4693 | -46.1406 | 2026-09-09 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| da37edaf-854d-397a-8a04-2ac1993754f6 | -9.7138 | -43.4192 | 2026-09-09 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 591.1 |
| e9892538-e167-321c-913c-65ad62045b7d | -10.7387 | -45.9649 | 2026-09-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| afa09fd2-f18e-3f48-9bd0-75094da24c76 | -9.7127 | -43.4899 | 2026-09-09 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 8389e8fd-c584-36a8-b80a-e11b01dd499c | -7.1386 | -42.129 | 2026-09-09 14:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 123.0 |
| 05f52f9f-ad55-3704-abc3-d09ba3f3a092 | -10.2372 | -45.2087 | 2026-09-09 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 01fb4cd6-27c4-3960-8f14-bdaf11485f81 | -10.2559 | -45.2292 | 2026-09-09 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 4002669f-5ef8-3919-a72c-a116a5c066f3 | -13.2917 | -61.109 | 2026-09-09 14:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0657269e-88fe-339a-9d89-034db0c85d24 | -10.7395 | -45.9194 | 2026-09-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| a6f50cc3-52aa-392b-a237-5f33174f393a | -10.7006 | -45.9698 | 2026-09-09 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 306.1 |
| e8827271-ce61-3381-8d88-ecec71ad25e4 | -10.7391 | -45.9422 | 2026-09-09 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 235.2 |
| db83108b-ca1d-3de9-8695-8079e3989021 | -10.701 | -45.9471 | 2026-09-09 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 2960e35c-8345-3651-bb3a-e8eeaeb0d54e | -10.7674 | -60.7666 | 2026-09-09 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 509760e8-e5af-3eb2-ac65-07ea1e913223 | -9.7698 | -43.4825 | 2026-09-09 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 239.1 |
| 79551856-56ae-3695-b418-26e89323064f | -10.2372 | -45.2087 | 2026-09-09 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5c174c2b-e939-3222-bc62-dbf199066ca8 | -9.7138 | -43.4192 | 2026-09-09 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 517.1 |
| 8b6069c6-0a74-3a0c-8293-1565104b6b54 | -6.3304 | -43.8253 | 2026-09-09 14:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 19640f83-ebe1-31c1-ba00-78883347f70c | -9.7131 | -43.4664 | 2026-09-09 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 240.3 |
| a0bdcc2d-b1eb-3ace-be85-dcb302ed7911 | -6.8708 | -46.0126 | 2026-09-09 14:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 13692ccc-e2bc-3f82-b869-31f3253c264c | -9.7702 | -43.4589 | 2026-09-09 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 2b873be3-6bc0-3163-81c0-1bbdeeaf39b8 | -7.6747 | -44.6028 | 2026-09-09 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 5f11282d-e0bd-340f-b7b5-5239cdb03ad9 | -9.7321 | -43.4639 | 2026-09-09 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| c509bad2-fe31-3664-a0b3-e2423b12a94a | -13.3298 | -61.1064 | 2026-09-09 14:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 32aa5b1b-302b-30e2-9a7e-18fdf0f6c4b3 | -8.7253 | -62.4177 | 2026-09-09 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 0d17dd93-5d3b-3924-b5c6-8a69f0fbe5dc | -10.7395 | -45.9194 | 2026-09-09 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 7f966371-af6c-391e-86f0-f64277347fa8 | -9.7134 | -43.4428 | 2026-09-09 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 274.4 |
| c751640c-a916-3e09-9d02-d17b78dac737 | -10.7578 | -45.9624 | 2026-09-09 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 56d01e0e-028e-382d-a57e-ac9ec652f9aa | -7.1386 | -42.129 | 2026-09-09 14:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 220.9 |
| c65375b8-c72f-3589-92a9-51d928d9fc8c | -10.72 | -45.9446 | 2026-09-09 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 5a92bc2a-503a-3abf-8082-e93783bd5599 | -11.333 | -45.7492 | 2026-09-09 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 2b4347fd-b1ea-3cea-a6e9-41423ba8bc85 | -13.2917 | -61.109 | 2026-09-09 14:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 41abcdfb-d2de-36df-a92b-4ec58684039f | -9.7889 | -43.48 | 2026-09-09 14:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 591.7 |


[Clique aqui para ver as próximas entradas](README33.md)
