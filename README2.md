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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e90ede51-84c9-3b58-bbe4-cd08a7c8d670 | -6.99958 | -35.15941 | 2025-12-24 03:34:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 64bff83e-7619-34b7-aee6-b81bf27615b9 | -3.20304 | -41.85284 | 2025-12-24 03:34:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b150b6d5-83a7-3437-b459-7655d4678092 | -6.996 | -35.15883 | 2025-12-24 03:34:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| bdee9fb5-0943-3269-9001-3321af3aa4ee | -12.2795 | -43.52941 | 2025-12-24 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9c7205a-e0d1-33fa-af90-6381c29d9d6a | -11.83206 | -43.78868 | 2025-12-24 03:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98f89f0a-d81a-33eb-91b1-0a20bf6ed4fe | -10.71516 | -44.1558 | 2025-12-24 03:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a591fc74-554e-3f2f-926e-e9c5179a4567 | -10.70926 | -44.1543 | 2025-12-24 03:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00e51bc4-dadc-3b79-9c1f-66c56cf38c22 | -12.28076 | -43.53421 | 2025-12-24 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0354294-bbff-3a14-b154-800320bbef5d | -11.8484 | -43.79618 | 2025-12-24 03:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c19372ab-cd51-31c3-8d55-0d5fbe6893e6 | -10.27465 | -36.28577 | 2025-12-24 03:36:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0a5d7ded-2d07-3981-bd05-6312f5b5eed0 | -12.28506 | -43.53058 | 2025-12-24 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f5b1509-0404-316b-a291-fd1b84399299 | -12.28222 | -43.52662 | 2025-12-24 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d03fc303-acf4-3d4a-a27e-609f83123304 | -11.84427 | -43.787 | 2025-12-24 03:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d85102b5-4e84-38cc-a813-687b838a4ea7 | -11.84268 | -43.79506 | 2025-12-24 03:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3b9d071-4a8d-3753-8cf1-77316f3e97c6 | -12.27874 | -43.5332 | 2025-12-24 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21ec4ef1-4d21-352f-a5ae-f67ff284de82 | -12.28149 | -43.53042 | 2025-12-24 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acea50ba-ea9a-38e3-97a5-e9aae8cc9574 | -11.83776 | -43.78988 | 2025-12-24 03:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30f67b0a-b36a-344d-a635-dcfd0c51e652 | -12.28706 | -43.53161 | 2025-12-24 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a994a5cc-8fcd-3b35-9949-864ea92c177f | -11.84347 | -43.79103 | 2025-12-24 03:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c4c600f-cab2-3048-8fec-d4606f57e1be | -12.28633 | -43.5354 | 2025-12-24 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f0e0ca1-7b43-3794-b35d-0af096f032df | -12.28582 | -43.52679 | 2025-12-24 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 174d2009-b52b-3772-8105-bc679a3d9283 | -12.28431 | -43.53437 | 2025-12-24 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58021ef5-8ac3-3bd1-acec-ce36be59d38e | -16.30409 | -45.09898 | 2025-12-24 03:38:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b9e71fb-d245-3cab-9924-a080c715ec05 | -18.82253 | -43.16372 | 2025-12-24 03:38:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ddd01528-d23d-309b-b21a-e6da633048e1 | -17.58274 | -46.67038 | 2025-12-24 03:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d5b1778c-9a8d-3d7a-84d7-1d4486879489 | -19.68725 | -41.47666 | 2025-12-24 03:38:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f6b42e69-3e31-3143-911f-d460bbced643 | -20.95827 | -47.18435 | 2025-12-24 03:38:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89e54aaa-519d-33d8-b229-3d905d6b848a | -20.91518 | -48.66527 | 2025-12-24 03:38:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9b3a791c-8088-3174-8381-0897ed489fff | -15.92001 | -43.72398 | 2025-12-24 03:38:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f44f1fcf-b181-32e0-8514-e308663cc007 | -18.8215 | -43.16882 | 2025-12-24 03:38:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 651d0357-dca1-3d82-aaeb-65f8d7c7794b | -19.683 | -41.47568 | 2025-12-24 03:38:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5f49a4b7-464f-3687-8f9f-9d799af04658 | -20.91375 | -48.67121 | 2025-12-24 03:38:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2f7fdeae-ef30-38cc-9aab-146b9e443361 | -14.88271 | -43.55831 | 2025-12-24 03:38:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e67a6d4-6254-3874-bcc5-a2f7be0fa7dc | -16.58748 | -45.87872 | 2025-12-24 03:38:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd1e87a8-55b8-3964-b6dd-c7f0665a959a | -16.30321 | -45.10312 | 2025-12-24 03:38:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4115abd-48fd-3f9d-baf2-b2c08b33b89c | -17.57661 | -46.66899 | 2025-12-24 03:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb79291c-af88-3c39-a6f5-0ccd5209e32d | -21.49504 | -42.65153 | 2025-12-24 03:38:00 | NPP-375D | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e2282cc5-6c7f-3d14-b8f0-e13bf50ff6aa | -16.18587 | -43.7245 | 2025-12-24 03:38:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e9e3df3-6d28-3752-81c2-ea30f1836438 | -15.91474 | -43.72281 | 2025-12-24 03:38:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b383d3d-8414-3237-9287-f20ddacca593 | -3.5386 | -41.6367 | 2025-12-24 03:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| e81e3b3d-ab02-332e-9007-885a4ee2c9c1 | -22.98724 | -48.63082 | 2025-12-24 03:40:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf7ec586-c565-3ba5-a4c6-5ae4d88950db | -20.99968 | -48.76233 | 2025-12-24 03:40:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 70894fd2-856a-3924-82c6-77158722bb68 | -22.98848 | -48.62574 | 2025-12-24 03:40:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 840ae6cd-e6c6-391e-a53c-8aacfcf3acfe | -25.51355 | -49.46534 | 2025-12-24 03:40:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 67dc678f-f3a6-3063-92b6-e9187a74a9e2 | -23.48058 | -45.35912 | 2025-12-24 03:40:00 | NPP-375D | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f840d605-b447-31d4-802c-e0fc543e0217 | -22.93987 | -42.92722 | 2025-12-24 03:40:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bddb29b3-8c1a-3b5c-8724-3f6b37895a30 | -20.99325 | -48.76067 | 2025-12-24 03:40:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6a1bd961-3067-3b88-aed8-9dabcbeba34f | -25.51222 | -49.47063 | 2025-12-24 03:40:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 226f49fa-a59e-39cd-9b51-664ce894bdd5 | -3.20322 | -41.85115 | 2025-12-24 03:53:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66664db0-2a27-3751-a2e2-a00865891068 | -3.54691 | -41.62384 | 2025-12-24 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| a13d29b6-3551-3c77-bd9d-2f1d28878d85 | -4.57398 | -38.12168 | 2025-12-24 03:53:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0974937a-16bc-3acd-a93a-bd6ee9d0eda2 | -4.57453 | -38.11823 | 2025-12-24 03:53:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 98887703-ece8-328a-bda0-8467897c47dd | -4.57729 | -38.1222 | 2025-12-24 03:53:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 049a6419-a9ff-3aae-bf05-94479ff7e7a5 | -3.55065 | -41.62444 | 2025-12-24 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 2cb0c9f0-6240-33b5-a69f-200630dbbe94 | -3.54318 | -41.62325 | 2025-12-24 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 7a0a06d9-fff4-3751-8ee5-40fd903d3606 | -3.55438 | -41.62504 | 2025-12-24 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 2cdcf7bc-52d1-3e92-9998-5d223e9fd1b8 | -3.55365 | -41.6295 | 2025-12-24 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| eebe2a64-3af7-31aa-b869-6bb6a7062c8c | -3.54245 | -41.62771 | 2025-12-24 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| c1965251-3abc-39c6-a28b-0af7f3586b19 | -3.54992 | -41.6289 | 2025-12-24 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 6dd9703b-bb1f-3cd7-903c-ab659dc759ec | -3.54618 | -41.6283 | 2025-12-24 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 5f3b2611-db9d-32e2-8c0b-9753229344b1 | -6.99746 | -35.15704 | 2025-12-24 03:55:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 4429666a-429b-375b-b98d-4d7c9fbaac5c | -10.71056 | -44.15606 | 2025-12-24 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daa19bb7-93b8-31bc-8029-80548d99a20f | -6.9981 | -35.1528 | 2025-12-24 03:55:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 8f1bde63-e495-36cc-bdba-10d87b72ab07 | -8.7472 | -37.17817 | 2025-12-24 03:55:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2f32d93-1fdd-30c2-9d65-fd57aa5c2037 | -6.36555 | -37.44187 | 2025-12-24 03:55:00 | NOAA-20 | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d583cc27-1566-38c3-ad0f-b9e25920b0dd | -7.00112 | -35.1576 | 2025-12-24 03:55:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d7897ae3-a43b-3e44-9bac-d347e3dfce62 | -7.11903 | -39.06082 | 2025-12-24 03:55:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fa4c7de4-2fec-3cad-aa48-de79b2a1512b | -7.82531 | -42.94175 | 2025-12-24 03:55:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 292fa922-1fae-36b5-a8d2-3ae0cab7f639 | -10.71468 | -44.15403 | 2025-12-24 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc9e6766-7a65-3536-ba16-462e0c54bbd1 | -11.76507 | -40.4138 | 2025-12-24 03:55:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6ce36247-6d51-3d90-8a31-c2e5de9342df | -11.83636 | -39.16891 | 2025-12-24 03:55:00 | NOAA-20 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 86e125d1-e0d4-3612-8c57-f1831c9ed37f | -10.71078 | -44.15324 | 2025-12-24 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87b7621b-8c84-3f58-900c-4cc794a64d56 | -8.054 | -36.14987 | 2025-12-24 03:55:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f89a7737-f1b3-30d2-8c26-9f8c1e40a28d | -7.00707 | -35.24188 | 2025-12-24 03:55:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 917344ea-e7ae-3872-8ba1-9a99e4a15023 | -10.51769 | -40.32993 | 2025-12-24 03:55:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1af19f97-3355-3b10-8034-6e2da8454b6a | -7.49259 | -37.59217 | 2025-12-24 03:55:00 | NOAA-20 | ÁGUA BRANCA | PARAÍBA | Brasil | 2500106 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5fe4ae6c-444d-3f1a-bcd5-bec4efec578f | -7.00342 | -35.24132 | 2025-12-24 03:55:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7249044b-0d25-3f0d-bddb-56f0dcb82d78 | -6.01373 | -39.91581 | 2025-12-24 03:55:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 88e6d20d-eff2-3543-a390-129c0da068cd | -5.23335 | -37.68766 | 2025-12-24 03:55:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67ced8b0-f22a-3a24-adda-04d0a9e996c1 | -8.05753 | -36.15042 | 2025-12-24 03:55:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ea55bad0-e78f-3ada-8bf6-c33d0d385f84 | -18.89034 | -39.93009 | 2025-12-24 03:57:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 98a2480b-a76b-3ce7-8d3d-0b9b7eab9068 | -13.37391 | -43.20022 | 2025-12-24 03:57:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 98f9ee1b-637f-363c-a2aa-66758bf04508 | -17.10203 | -44.64856 | 2025-12-24 03:57:00 | NOAA-20 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c7d9765-6694-3d0d-9923-648f40775133 | -17.57763 | -46.67039 | 2025-12-24 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac3d25e7-51b9-3e39-8487-3f9ec3ff2062 | -16.18449 | -43.72568 | 2025-12-24 03:57:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ee8369f-e06b-3a24-a432-35b6fb9e81d6 | -17.58173 | -46.67119 | 2025-12-24 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0812d3a8-8e8e-37c4-8968-91ac7cfdbd88 | -16.1965 | -47.60257 | 2025-12-24 03:57:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fda5aab5-029e-3aa4-a5cd-432347bb890b | -11.83134 | -43.79367 | 2025-12-24 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf4e51fa-b8a2-312d-9526-5680494cc57a | -11.83968 | -43.79035 | 2025-12-24 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f69f6c3f-95cc-3802-b117-775fed069bc0 | -12.59947 | -48.76833 | 2025-12-24 03:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d54e84b-1f0c-3faa-89d1-2c9799923628 | -12.28073 | -43.53065 | 2025-12-24 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31f320ec-cdd4-3a9c-b37b-8d2caa55f917 | -15.91937 | -43.72312 | 2025-12-24 03:57:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b255750a-c7a3-30bf-9842-26c0ffa0fae7 | -11.8095 | -43.78491 | 2025-12-24 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfd594c7-c72c-3159-bc4c-ca2046923000 | -12.28366 | -43.53579 | 2025-12-24 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bff82fb-37ce-3487-96eb-211354e09e52 | -15.91864 | -43.72731 | 2025-12-24 03:57:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f89c2a80-3d58-318a-8d5f-42fdbea88b43 | -18.82216 | -43.16494 | 2025-12-24 03:57:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 66eb2fd8-0d6e-30e0-967d-45024dbe7599 | -16.5175 | -43.54026 | 2025-12-24 03:57:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8dc6074-0d1a-3cea-92bb-f282342d68e6 | -12.07178 | -43.72709 | 2025-12-24 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df038318-b2bf-3f47-8acc-f2446829fb0c | -12.59886 | -48.77148 | 2025-12-24 03:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c172d97-d47e-3fa0-a41f-89649a62f278 | -19.54847 | -40.23287 | 2025-12-24 03:57:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |


[Clique aqui para ver as próximas entradas](README3.md)
