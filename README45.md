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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a57318b-4059-3c02-89da-7ced38a35e8a | -1.19724 | -51.97821 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4b495dc-bba6-3d12-a4b0-f0a2af6d4ec0 | -4.94183 | -50.64605 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 554d7fe7-0551-39c5-af78-531eb06e1d03 | -0.93267 | -51.72 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0764b29e-5899-3617-b698-b87e9e4dd61b | -1.54666 | -51.28281 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 067a9b56-8193-3dc7-bf81-b7ac4b5a11f3 | -2.84481 | -53.97059 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71bfe5d4-1468-39f0-b2df-156cfb72fbfa | -4.95618 | -49.85471 | 2024-11-20 04:50:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d51af82-2461-3b32-92a5-9612dd7a7198 | -2.29097 | -46.37341 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e368f24a-f48e-3f36-8fee-08be2ffac01a | -2.41345 | -49.1443 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89675438-d949-360c-a338-1008c89390f6 | -3.03228 | -49.45481 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 358fc29b-6dc6-3b21-830c-0bac9472d74b | -5.24784 | -42.64301 | 2024-11-20 04:50:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39c2772f-6439-317b-921d-3a8a69822192 | -3.51052 | -51.01798 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24f8b676-a577-330a-84f4-6bb5e6eb96f7 | -2.68697 | -51.71199 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ce175fc-eb99-3978-8797-3a885864e4d4 | -3.05194 | -54.4136 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 798c60c8-86bb-36eb-bebd-ccd9ace60ef7 | -2.21097 | -53.70718 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5e9c156-cd5a-3ce4-8d34-5b35fc81e243 | -5.51239 | -46.44193 | 2024-11-20 04:50:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a44e160-12e1-3fe0-8b6c-3ce95fee4e30 | -2.68944 | -51.80419 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3948c30-4281-3898-b83e-2a468ea43435 | -2.81695 | -54.02601 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17a601f2-96e8-3b55-a10d-ec0447cd9125 | -2.56031 | -47.2828 | 2024-11-20 04:50:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7f6d565-a1a5-39e6-9eb5-52a0958429c1 | -1.72741 | -52.69444 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 866b32b1-9e9f-3905-824b-e52abaa87dbc | -3.07086 | -49.20448 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d5215c0-a558-35aa-946f-7dfe6ffb6bf6 | -2.269 | -49.14305 | 2024-11-20 04:50:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 874ac37e-47d8-3fd7-9647-367dc0bdb1ca | -8.31824 | -45.11267 | 2024-11-20 04:50:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1d49697-5f2c-35e5-8ef4-062020fd7c3d | -2.297 | -49.05628 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98241163-a9e1-32aa-a060-1f7f90417951 | -1.32649 | -52.40329 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 620a40f8-6d65-3fe1-9a8b-add443e0237e | -4.01218 | -49.93126 | 2024-11-20 04:50:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a388079-ca4c-30a5-8d0e-8c70f2329c1a | -1.44979 | -52.66619 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b22d116-033d-375d-8598-656c60b539fd | -5.37696 | -50.47293 | 2024-11-20 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7bf4697-8a22-315c-ac72-dab8c55e96da | -3.56171 | -51.12244 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b7a5cef-11f4-37bb-85f6-8ff3d21244d9 | -2.00284 | -46.60141 | 2024-11-20 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5afc013a-8ad5-3f29-9759-bbcd0c0fffb4 | -2.03329 | -45.79709 | 2024-11-20 04:50:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2ff7cb7-41a3-31f4-af4c-0331c7fe6b07 | -6.63506 | -47.34811 | 2024-11-20 04:50:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3ed8a2f-573d-3676-bb33-4ed33780d9af | -3.10799 | -53.70481 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a478561-0b43-3d58-8769-49704a353009 | -3.76148 | -45.08542 | 2024-11-20 04:50:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3b12409-5b97-3f27-8f26-28a49974a5ba | -2.91555 | -53.06921 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 09102a14-ccbd-3e00-8ff6-890a6c03dd86 | -2.35694 | -48.60609 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e1396af-38b1-31ab-b9b2-2d39f152c97d | -3.24378 | -48.44235 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a32005e1-aba0-3ba2-b317-6b27dd3b97ea | -1.54192 | -51.18331 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6dcaa32-0d5f-355b-ba0c-232f583cf4d2 | -2.73444 | -54.11614 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31dece2e-5db8-3f5e-b4de-2d974ed891d5 | -2.36116 | -48.60258 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59002133-dc68-3bae-a149-937ecbf66fb8 | -1.73372 | -52.7941 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 759cad0b-282a-3e1c-87cf-73d629d6d55e | -3.91755 | -54.01339 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55d01c5f-307d-3447-99a5-6fac4ebcf3c8 | -2.3111 | -47.89553 | 2024-11-20 04:50:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ab6cf9b-13aa-38ef-ac3f-40f4c27727a0 | -2.759 | -54.05244 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f58ce38d-2565-3c45-b400-d03c5c20efba | -2.47564 | -45.86362 | 2024-11-20 04:50:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaca11eb-e012-3ce5-827d-bb944bc1e05b | -2.21162 | -50.64536 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2597fa5-2ef7-3e7f-b266-3c9c394a552f | -1.5067 | -52.09078 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba7e760f-693f-3d32-b28c-eed5f8d35195 | -1.39275 | -52.09047 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f419fb50-97f5-3e92-b6d5-ce819e20363e | -2.74875 | -45.70263 | 2024-11-20 04:50:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f12574d6-35e1-3414-a1c7-4245e2bb066d | -2.69168 | -46.08036 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21d1965e-80d3-3f06-9745-c1b9353025ef | -4.38364 | -50.42021 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b3c4b3f-191f-3fe4-9b29-17d93215148e | -3.76017 | -52.14169 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d5c133b-e8be-3027-9dc4-b9e0f66e17dd | -3.05394 | -45.13298 | 2024-11-20 04:50:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddf4c66b-1c61-31d9-a77e-1f746d4cfffa | -5.69329 | -45.84591 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f0b569e-28d4-3ac3-807d-eab830e6d70a | -5.46822 | -43.94625 | 2024-11-20 04:50:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c9864056-75a4-3fc4-afa6-e44a4a4029ea | -2.75303 | -54.06735 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b71c7204-e757-3b73-8d14-58a77832c025 | -2.66412 | -46.23437 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a83f4aa5-b01a-33c8-b021-542398ad47de | -1.52481 | -55.48996 | 2024-11-20 04:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 351c3cda-7108-35be-b980-8804d1bc9092 | -2.13593 | -48.56659 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 50dc8274-7b6f-31f0-bffe-a41ebbe9b18f | -3.50976 | -50.22518 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5986cba3-53c8-38b1-abd7-1410041676b7 | -2.08724 | -48.94624 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74d3a4c9-fdf2-3bbc-b0d8-00f02f2d7d8a | -2.8415 | -54.01335 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be52dee2-c673-33ec-ae15-67a4a5c8a44b | -1.39536 | -51.59784 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38a35992-7991-37d5-89bf-379340ce2f97 | -2.05839 | -53.43028 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d816695-f13c-37cc-b0c6-dc88e2197b2d | -0.93302 | -51.63157 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 201405d1-14e1-3266-b503-6cdd1e65b955 | -1.39863 | -52.17717 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d327f8d-cae0-3fca-a8b6-5bc627c07d84 | -1.34689 | -51.43517 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afa4d14a-f8de-39dc-b629-69d6df897874 | -2.65383 | -46.54924 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a99e6055-c64b-3c1f-8fd0-b2d41b2596e5 | -4.8865 | -45.7548 | 2024-11-20 04:50:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b27bfc1-6d45-3a77-8dcf-4ffe5917aa4e | -1.3079 | -52.25986 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a21bf97-41b4-3ae7-828a-37d952496efa | -1.61504 | -52.41598 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5925b86b-d1aa-3c9c-abb0-1729ebfabb22 | -2.97137 | -49.28949 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f81f9f7-505b-3d2d-92fb-ea0b0084461b | -2.37342 | -49.83366 | 2024-11-20 04:50:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59e72939-426b-37d6-97ee-873ea3d37b2f | -5.4511 | -49.68421 | 2024-11-20 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10de3860-10e4-33f4-aca0-1f7d27b78476 | -2.2254 | -53.5704 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58bd3158-e3f6-3e10-b263-2b0e5635db55 | -1.61169 | -52.41546 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94bb09a4-1a14-35ef-bb23-217a36367982 | -0.94929 | -51.72259 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c2825c3-f1cc-349f-91ea-93a2c4af7805 | -2.56608 | -53.99543 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e265b8b-01c7-3e5b-90d3-2cfd7d529896 | -3.00626 | -51.01466 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 796309e5-30f1-387a-a431-81d09f07b121 | -1.05777 | -53.09175 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36d686af-6cd7-33e0-92fb-865dc7915e1c | -2.74275 | -51.83022 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 25d8ad4f-059e-3f42-991b-7858f885715f | -1.21159 | -51.75674 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c1c4851-b336-3127-8ec7-2e38daa21485 | -2.14466 | -50.64543 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d50e7b89-bf0d-394a-ab1c-117796a754d9 | -1.62977 | -52.62847 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c822b04c-b1bd-3085-b2d7-9749e02d4e29 | -1.93179 | -54.06057 | 2024-11-20 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 495be85a-fa8c-34c1-a0c1-e142b8130ab6 | -1.54698 | -52.26876 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b760193-f8e2-3e69-903b-789eab155807 | -3.29391 | -53.85247 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b61c71e0-15cd-3990-89d0-beb876441168 | -0.81563 | -51.60633 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c267f608-5501-333f-a7a3-380ac543be7f | -9.18011 | -44.72181 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11110a8f-4506-3606-823d-533d303fcac1 | -9.17344 | -44.72122 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e070c805-bd15-3dac-bf39-911c4ca83e9b | -2.82282 | -51.79678 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d4bf93c-74f8-3d00-8922-64f324bbf37c | -2.69374 | -46.23494 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 851890f5-85b3-383a-af67-006f282d3837 | -3.88314 | -52.2393 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8659c5dc-afdc-302e-bfd9-ba79bb8fc0a4 | -3.18564 | -54.32088 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 670d8fb2-7862-32cd-9ea2-84bcc9c027ae | -1.1117 | -52.34848 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86d7f69b-b19d-321f-b244-827aa17765b2 | -2.88447 | -41.76324 | 2024-11-20 04:50:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1456c33-c3ea-3c74-9622-b53c54baeb5e | -1.44783 | -54.50536 | 2024-11-20 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66727432-cbb7-38a2-8a01-ef3ed476b66e | -7.21185 | -54.99791 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2c38cd5-ad60-3461-9d52-e465d56b9836 | -2.16702 | -48.92149 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a9abb81-12b0-30df-a91e-b8a590347508 | -3.68372 | -52.36734 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce3ee7c2-ac67-37bf-b775-15bf962b654d | -3.03865 | -49.45964 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README46.md)
