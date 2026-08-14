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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af966cae-175d-3d93-b9f8-bd28d72129ac | -13.2804 | -54.2021 | 2026-08-14 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 3425676e-0d07-3bc7-a33d-81b5975e4be1 | -9.9706 | -53.9624 | 2026-08-14 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 21c70f9f-563f-39be-bd33-e232c5363fa7 | -10.6909 | -50.5165 | 2026-08-14 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| d1377dee-2f2a-3f82-bb4c-c9c5d9ebb471 | -6.6379 | -53.4177 | 2026-08-14 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 55e08444-50dc-32bc-b11a-596a9fb6f619 | -7.5851 | -61.228 | 2026-08-14 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 5918ca21-a54b-3ceb-9c14-e55f162d4477 | -9.9896 | -53.9404 | 2026-08-14 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 215.5 |
| f46b28ca-cbe1-3f40-b986-acd65a7b35e1 | -11.5074 | -54.6256 | 2026-08-14 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 592c6818-5061-34d3-bc8e-a85e30de0e3e | -14.0939 | -53.6321 | 2026-08-14 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| feaf8cb2-80b2-3d49-97a3-b4b0f254886d | -11.4885 | -54.6273 | 2026-08-14 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 8934cc87-2c8e-3444-afbd-6124a121e3be | -12.0458 | -50.0208 | 2026-08-14 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| b6a641b3-9bb1-326f-84ac-0936a1696291 | -9.9894 | -53.9608 | 2026-08-14 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 195.9 |
| df0f07c6-dd5c-3a93-9325-023f1f496b21 | -6.6379 | -53.4177 | 2026-08-14 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 9f30fe9a-b08d-3b94-b96b-1a33e77eeddd | -10.7099 | -50.5145 | 2026-08-14 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| c772c982-0900-31ad-b929-155a81062d71 | -8.7291 | -54.6049 | 2026-08-14 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| bc8b25a7-6757-3724-b385-b2a215f6d811 | -9.7584 | -60.7645 | 2026-08-14 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a0c110ef-dcc8-3b98-8d4e-983990bb4bdd | -7.5851 | -61.228 | 2026-08-14 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 59b41843-64e0-3d6a-935f-6e8e0f35e402 | -12.0454 | -50.0424 | 2026-08-14 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 69964e42-3a9d-3b8f-8584-73f44f15bb31 | -13.8227 | -53.7889 | 2026-08-14 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 2700db25-ccd7-361a-af9c-6c13c2f78b1f | -14.2945 | -51.9635 | 2026-08-14 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| cdf59e6f-e5c8-37e5-ac3e-0f010433af4b | -14.2752 | -51.966 | 2026-08-14 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 7c1bc8a7-2009-382a-a036-9b7f4d15f075 | -11.6013 | -54.6782 | 2026-08-14 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 3e4cc8b0-cc6a-32f2-bba6-d246b6a2b1ea | -9.9896 | -53.9404 | 2026-08-14 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 0199e5cf-0bc4-33be-a88a-6c90b65f6000 | -11.4885 | -54.6273 | 2026-08-14 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| f7edd26a-56ec-3adf-98d6-164eb33bb408 | -9.9706 | -53.9624 | 2026-08-14 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 91d12c3f-b63d-3fc0-9f1d-5ccd3d308a44 | -13.5899 | -46.2323 | 2026-08-14 14:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 7fe73fce-abfc-3114-ad50-e69dc070aaa5 | -13.2804 | -54.2021 | 2026-08-14 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 386.0 |
| 6a16e078-a047-35c7-8f10-c09b16e16cc2 | -6.9847 | -45.8685 | 2026-08-14 14:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 7e5d2c4a-064d-31dd-a43c-ed6833866f1b | -11.0635 | -50.9452 | 2026-08-14 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 71cada97-becc-30ac-bcfd-dacfe54fa1fc | -6.95 | -59.2984 | 2026-08-14 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 167.6 |
| ece0e5c2-5663-3f78-a7ce-f122c6729048 | -13.2798 | -54.2435 | 2026-08-14 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 81dd231e-5b34-3cc5-88d8-eb9adae46ed0 | -11.8467 | -51.8971 | 2026-08-14 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 58606773-ca77-3c82-96f7-be7350990a79 | -13.2801 | -54.2228 | 2026-08-14 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 332.3 |
| f792825e-51ef-3267-aac1-502ae557c75b | -11.6015 | -54.6577 | 2026-08-14 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 81123000-7e17-32b4-bbac-66efe84e494c | -15.1115 | -48.6682 | 2026-08-14 14:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c9fbb610-0896-3196-8c88-e507fd433898 | -7.0146 | -41.445 | 2026-08-14 14:40:00 | GOES-19 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| f4f03b09-c887-3028-b770-b65542b4c0d6 | -14.3492 | -53.3084 | 2026-08-14 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 864ee5a6-edb7-3502-b207-d91892768510 | -6.9685 | -59.2976 | 2026-08-14 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 177.8 |
| dcafebd1-fd2d-30a0-b99d-7fe5ca856a66 | -9.9708 | -53.9419 | 2026-08-14 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 148aae0b-615e-3b52-997f-0ffaa45ef8d8 | -13.8223 | -53.8098 | 2026-08-14 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 262973f7-d216-33e6-b37c-38ea596cde8a | -8.7104 | -54.6062 | 2026-08-14 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| f595f280-dd4f-3341-a7d6-c09b0b463420 | -6.9686 | -59.2783 | 2026-08-14 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 201.2 |
| 4ad1c7f3-b749-37ef-86d2-863d7bf9627e | -7.5852 | -61.2089 | 2026-08-14 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ad9bbccb-37b4-3d81-b5ca-5e2ed643d569 | -6.9502 | -59.2791 | 2026-08-14 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| be654ec5-c10c-340c-9e26-4d10f1fcd59a | -6.7871 | -58.764 | 2026-08-14 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 408d9395-d09e-3387-b37c-0db4f83e770b | -10.6909 | -50.5165 | 2026-08-14 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 9cf2036d-f35b-38b4-83e6-d47682313dee | -15.2091 | -52.7339 | 2026-08-14 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |


