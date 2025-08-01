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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0838240-30d1-386a-a824-379a27ee5690 | -7.7253 | -45.1008 | 2025-08-01 02:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 09ec8c98-0d30-39b7-af84-4b25dfb2a632 | -6.7294 | -59.1723 | 2025-08-01 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 386.6 |
| a4a58933-51bb-3c34-84fe-4b2295f06651 | -8.3396 | -50.5652 | 2025-08-01 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f17bef78-0c87-33bd-a0ab-18c6d67e0595 | -6.7477 | -59.1909 | 2025-08-01 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4468f33e-d90b-3a6b-9935-24c72a459daa | -9.3989 | -45.4928 | 2025-08-01 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 1dda9fba-9d9a-3be9-b984-911a0105c9e3 | -6.5443 | -56.2113 | 2025-08-01 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6e1da681-c774-3b78-9220-2d6058197e05 | -6.526 | -56.1923 | 2025-08-01 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 54561e26-9130-3687-a4a2-8696205f2b61 | -23.5022 | -47.8407 | 2025-08-01 02:00:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.4 |
| cee5e46f-0f67-3b44-ad2d-57d212b349bc | -7.7444 | -45.0762 | 2025-08-01 02:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 182.8 |
| eb727529-33c9-319d-ad3f-6518ea433fd9 | -6.5258 | -56.2121 | 2025-08-01 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 86c4fd08-9236-36b0-addb-2cd05bfe1b65 | -9.5339 | -40.3531 | 2025-08-01 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 9fa89dcd-c962-3873-b0b2-3c8323b75763 | -23.5446 | -47.8293 | 2025-08-01 02:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.0 |
| e1413232-4c9c-3f46-8c25-dcdd4fcf0eb8 | -8.0513 | -43.1001 | 2025-08-01 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| c77ba8bd-a270-32a2-8c41-ecc6e4376502 | -6.748 | -59.1523 | 2025-08-01 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| d62da2dd-4b3e-3480-8bed-61ef990d3ad7 | -6.5074 | -56.213 | 2025-08-01 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 60c44f73-379b-31b5-9504-a22960e7a025 | -8.0321 | -43.1257 | 2025-08-01 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 77627c22-4fb2-3d66-bd4e-d4ba020e850a | -6.5445 | -56.1915 | 2025-08-01 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 0c1f3401-05d0-356e-8692-460a3205c5df | -23.5242 | -47.8109 | 2025-08-01 02:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.4 |
| 1e085a20-cd7d-33b9-ade3-b96de7d258a8 | -7.7255 | -45.078 | 2025-08-01 02:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 154.9 |
| b0c911ee-ffa8-3d86-ba93-57a0e276a637 | -7.7441 | -45.099 | 2025-08-01 02:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| c2b72977-900b-3a5a-9cd5-e94c38380dbf | -6.7295 | -59.153 | 2025-08-01 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 44aad173-aac7-3b6a-88f9-222ac75b7960 | -9.62134 | -63.42771 | 2025-08-01 02:04:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 58717bf1-646e-308a-bf47-f83f6452c0f1 | -23.5242 | -47.8109 | 2025-08-01 02:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.3 |
| d9ab90d4-e4f5-3048-9ea5-085849dc1d0a | -6.7477 | -59.1909 | 2025-08-01 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 02f2901b-475f-3d95-9f47-ce67945c5f32 | -6.748 | -59.1523 | 2025-08-01 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 1887e5dd-1f17-33e3-ab14-8d2a831e3d47 | -9.5343 | -40.3282 | 2025-08-01 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 442b6497-8237-367d-af22-9e55fd2dc963 | -8.0321 | -43.1257 | 2025-08-01 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| f7bf6f6b-7c0e-3439-a0ec-e4658e5a3e35 | -6.7295 | -59.153 | 2025-08-01 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 0c73d6c5-ad45-3e03-9c63-efb1f16edac7 | -6.5445 | -56.1915 | 2025-08-01 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9bbeffdf-0bdc-366c-b48a-4d7a1870667b | -6.7478 | -59.1716 | 2025-08-01 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 195.2 |
| f9aa2c77-9cb8-3e80-895b-54d1062d28b5 | -6.7293 | -59.1916 | 2025-08-01 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| ff07a9ca-46a3-370c-8c70-a3a01d636a6a | -23.5234 | -47.835 | 2025-08-01 02:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 300.6 |
| 681eaf47-9acc-3f94-a783-a6df14cc8ac6 | -6.7294 | -59.1723 | 2025-08-01 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 408.9 |
| 47bdff04-fce2-3b70-a786-4813ac7591a8 | -9.5339 | -40.3531 | 2025-08-01 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 122.0 |
| d0e64929-b014-3b60-9b92-e02acda856f2 | -23.5446 | -47.8293 | 2025-08-01 02:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.5 |
| 971c0b3b-6a85-35e2-bcd6-861546c2ab2d | -9.5152 | -40.331 | 2025-08-01 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.2 |
| b50d7355-95a2-335b-a5d5-761151594a53 | -9.5147 | -40.3558 | 2025-08-01 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 5d2675fa-06a6-3be8-bae9-8a68d8a1626d | -23.5022 | -47.8407 | 2025-08-01 02:10:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.7 |
| 7a9d3618-e5c3-3870-88ff-31835d238b51 | -7.7444 | -45.0762 | 2025-08-01 02:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 51a8c9f5-da91-3f81-82c1-d7832c4954b8 | -7.7255 | -45.078 | 2025-08-01 02:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 98c95f56-f180-32af-ba1a-fe74938a1551 | -6.748 | -59.1523 | 2025-08-01 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 8a1379e0-6a4a-39a0-b698-07ad59e98ab5 | -6.7293 | -59.1916 | 2025-08-01 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| c5a7a8b9-76b8-33d2-8606-eba6cbc73e63 | -6.7294 | -59.1723 | 2025-08-01 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 347.3 |
| 3bc3cf9c-af89-345c-a1f7-de9094f22717 | -6.7477 | -59.1909 | 2025-08-01 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 524869f0-c831-30c5-b7e6-78b461f5109d | -6.7295 | -59.153 | 2025-08-01 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 476ca6e0-24a0-31fb-aded-102afcab96d3 | -23.5242 | -47.8109 | 2025-08-01 02:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.6 |
| 0b51e722-8dbd-39ed-82e3-c43657eb81a9 | -8.0324 | -43.1022 | 2025-08-01 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 2864e8b5-a430-38e7-a512-d8bc4b8c0ef4 | -6.7478 | -59.1716 | 2025-08-01 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 191.9 |
| 78dff165-8372-3922-b30b-9490a83569d5 | -8.051 | -43.1237 | 2025-08-01 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 5724ad80-67fe-370d-8612-64350e0512b6 | -8.0321 | -43.1257 | 2025-08-01 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 2ddc3dc9-7e2f-31dc-8347-42ffd191fb5b | -23.5234 | -47.835 | 2025-08-01 02:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 289.6 |
| 7523db3b-5229-3191-81c9-568a7564b121 | -8.0513 | -43.1001 | 2025-08-01 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 5d522c21-28a9-32fd-b4c0-df7176711fca | -23.5022 | -47.8407 | 2025-08-01 02:20:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.2 |
| ffbb4ca5-2f8a-3bbe-a7c9-1a5720504dc0 | -8.0321 | -43.1257 | 2025-08-01 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| f9128ddc-69db-3322-b797-b10e6e38bfa9 | -6.7295 | -59.153 | 2025-08-01 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.8 |
| d0662032-f2b9-367c-9c48-762183e64c91 | -6.748 | -59.1523 | 2025-08-01 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 67877968-ab92-31f9-b179-2defa573e5a2 | -23.5022 | -47.8407 | 2025-08-01 02:30:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| c8d766d2-6829-3b35-b736-5f7f650eed22 | -6.7478 | -59.1716 | 2025-08-01 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 246.9 |
| aa8f7bfe-fb3c-3f4b-b8e7-bc298c966639 | -8.0513 | -43.1001 | 2025-08-01 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 0f48ede6-f00e-3f79-878f-df44ff31e36b | -8.051 | -43.1237 | 2025-08-01 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 4cfc35cf-a6be-35b4-aa8b-804b388965b4 | -8.0324 | -43.1022 | 2025-08-01 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 5f4d9f1d-d529-3f43-b5fb-f49ce0ea5220 | -6.7293 | -59.1916 | 2025-08-01 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 4f8b5c78-951e-3d7b-bff0-d92b30dad1e4 | -6.7477 | -59.1909 | 2025-08-01 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| cdd008a0-b656-391d-9081-ac2ca265698f | -23.5446 | -47.8293 | 2025-08-01 02:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| 737bf899-bcea-3055-9e9e-0a6e7a2b987b | -6.7294 | -59.1723 | 2025-08-01 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 274.0 |
| b929f890-4f12-31ae-a574-19a2ceccf0d4 | -9.3989 | -45.4928 | 2025-08-01 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 912dde66-2f91-33e5-852d-0b3d215d725f | -23.5242 | -47.8109 | 2025-08-01 02:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| 19f7efea-3845-3881-9aee-39b7f8592085 | -23.5234 | -47.835 | 2025-08-01 02:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 186.6 |
| ae35ec36-edaa-30cb-b80f-11cbc938dc4b | -6.7295 | -59.153 | 2025-08-01 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 5921ba27-4b2b-3cd3-b81f-b918498fc1b2 | -6.7293 | -59.1916 | 2025-08-01 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 86e197b6-218b-3641-9861-f64dada1af4c | -6.7478 | -59.1716 | 2025-08-01 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 187.6 |
| fa8814fc-c3f4-3ede-8917-2bb98efaaaa9 | -8.0324 | -43.1022 | 2025-08-01 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 0ffd6361-265f-3839-bc8d-be0180c58ae0 | -8.051 | -43.1237 | 2025-08-01 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 75cbc2ca-bb97-38a8-ba4f-ed63a71eab8f | -9.5147 | -40.3558 | 2025-08-01 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 116.1 |
| 7b82101e-3a87-3af8-881f-fd87cbfde7eb | -6.7477 | -59.1909 | 2025-08-01 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 2d5095ba-7aae-3b01-8827-14a26858408d | -6.748 | -59.1523 | 2025-08-01 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 3b819bc1-f503-331c-9690-ba49962eaccd | -6.7294 | -59.1723 | 2025-08-01 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 361.6 |
| 4fe7eb4a-6f95-3038-860f-5872f00aaaae | -9.5343 | -40.3282 | 2025-08-01 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.4 |
| f60418e9-812c-3a97-b986-66e0844bc93c | -23.5242 | -47.8109 | 2025-08-01 02:40:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.7 |
| 24761ff3-345d-3d87-88e5-c1f0ab2dcab6 | -9.5339 | -40.3531 | 2025-08-01 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 124.8 |
| aff7c392-cdf1-35d5-92e1-57cb386772e2 | -23.5234 | -47.835 | 2025-08-01 02:40:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 213.0 |
| 70822d71-a94c-3e75-a9ec-fe7f532c0cc8 | -9.5152 | -40.331 | 2025-08-01 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.5 |
| f026da90-4cd9-36ef-a420-0dff86ac83fc | -8.0321 | -43.1257 | 2025-08-01 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.5 |
| ecb56682-4c10-300b-a44a-19dcedccd7e1 | -8.0513 | -43.1001 | 2025-08-01 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 21ee24f6-0b67-3208-830d-c2cfc1a0448a | -9.363 | -40.3031 | 2025-08-01 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 8b287cf9-465e-3c3d-a180-8070d8104433 | -23.5234 | -47.835 | 2025-08-01 02:50:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 167.8 |
| 5b794f15-6fcd-33cc-a984-b9691eb8117e | -7.7253 | -45.1008 | 2025-08-01 02:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 094594b9-3bb0-33bc-8ed1-ad51277b6847 | -7.7255 | -45.078 | 2025-08-01 02:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| c0101b3d-073e-3d0e-81a7-444deb58e447 | -6.7293 | -59.1916 | 2025-08-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 0c5501cd-65ef-3893-83a6-098535b36e89 | -8.0324 | -43.1022 | 2025-08-01 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| 0a12a5cf-ad67-321c-bc20-84467477fe31 | -23.5022 | -47.8407 | 2025-08-01 02:50:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.9 |
| e577a4c1-7d7e-3bf5-ad56-0a30d02622e6 | -6.7294 | -59.1723 | 2025-08-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 308.8 |
| 0ca769bf-7811-3e7f-b8c4-56302edb3a40 | -6.7477 | -59.1909 | 2025-08-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 1b6eb9a6-fb98-3414-aee3-3c366867d0f9 | -6.7478 | -59.1716 | 2025-08-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 222.8 |
| b48a2312-dc56-30e9-a944-6b545a306a27 | -6.748 | -59.1523 | 2025-08-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| aa903922-957d-3831-9c74-2c832a85d9cb | -23.5242 | -47.8109 | 2025-08-01 02:50:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.2 |
| 96dda1ff-d4e3-38f1-955f-8558b56dea5d | -8.051 | -43.1237 | 2025-08-01 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 09048c55-47dd-36dc-9f6c-64df96d410b1 | -6.6143 | -59.9848 | 2025-08-01 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e4a34f40-bfa9-3a98-ab37-d8088dd5e46d | -6.6328 | -59.9841 | 2025-08-01 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 43b30919-36fb-34dd-8187-62b373f4ac74 | -9.3626 | -40.328 | 2025-08-01 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.6 |


[Clique aqui para ver as próximas entradas](README8.md)
