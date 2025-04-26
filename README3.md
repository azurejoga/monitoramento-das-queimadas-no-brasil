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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e6f3929-2559-3a46-a2dc-0eb2fd8235de | -11.39598 | -52.94344 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 853e45da-8bb7-3942-a24d-40af9e1d6870 | -11.40011 | -52.95251 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 57f3b9b6-b2fc-3b33-80f6-93458d2f515f | -11.57763 | -37.96389 | 2025-04-26 04:10:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e575b91b-4dca-3e64-a378-87a535bb754e | -11.57833 | -37.95882 | 2025-04-26 04:10:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e567f75-db96-3ec3-9e72-04ee7fe10c6d | -17.59565 | -43.19923 | 2025-04-26 04:10:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70f63bac-d6f2-341e-9112-0266043d0c06 | -11.40499 | -52.95775 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5290e2d5-548a-3398-a619-27dcf55c5f82 | -17.27362 | -41.85968 | 2025-04-26 04:10:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eb707280-8a54-3040-a890-a7fd1b05ff0a | -11.39749 | -52.9357 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 21e0b5ad-5862-3620-b62e-615a96b0d0ec | -15.59922 | -41.79433 | 2025-04-26 04:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 9c5ef0a2-1592-31e9-b2a1-6117229c6fab | -12.56582 | -45.35851 | 2025-04-26 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c463d96b-01b9-3fba-b4d9-c0e842ff4130 | -11.57932 | -37.96267 | 2025-04-26 04:10:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6ab13c71-ee52-35af-bd56-1f9e087076af | -10.62583 | -40.51227 | 2025-04-26 04:10:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1727352e-8e0a-318e-815c-cd9e5c66eaa4 | -12.35287 | -41.28136 | 2025-04-26 04:10:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf525781-ee0f-36fb-9d0d-a3478534075e | -15.79034 | -41.27673 | 2025-04-26 04:10:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c564efa2-a2f1-3cc0-855c-a6791676b1de | -13.6683 | -43.7886 | 2025-04-26 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6d92db2-9e72-3b68-a193-99175e660905 | -11.96421 | -44.00565 | 2025-04-26 04:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c58c3a2a-0812-3ea0-99c4-b74404074120 | -16.6808 | -43.88285 | 2025-04-26 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9dc9d95-a96c-3424-bade-fc9c58c0d046 | -13.66106 | -43.79103 | 2025-04-26 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 442bc068-4a86-3f30-9389-7a4eaeb50f2c | -15.59579 | -41.79382 | 2025-04-26 04:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 95f38093-afa6-35fc-80e5-0ab938d8fbc1 | -13.94354 | -52.54279 | 2025-04-26 04:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5a25d38-e60c-3824-968d-29ff9f18081c | -13.94418 | -52.5396 | 2025-04-26 04:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e4f0e77-4569-3bdc-a856-503404885596 | -11.40576 | -52.95376 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4bb5eb8e-afef-3d5e-b437-6c943b704669 | -17.27182 | -41.8604 | 2025-04-26 04:10:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 83771dd8-01a6-319e-bb18-a9693339ab52 | -11.39934 | -52.9565 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e42febfb-a6f5-3a0d-80c4-9e35c39050ab | -11.39523 | -52.94733 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 25263a18-acdb-31d6-9997-eea275b35c55 | -15.5998 | -41.79049 | 2025-04-26 04:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f9f8e4d2-c88d-399c-840b-47ba4d235c1b | -13.6644 | -43.7916 | 2025-04-26 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 519ae098-8ac7-3c60-a558-797bc403e6a5 | -13.66383 | -43.79515 | 2025-04-26 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cd4bd1b-1e52-3f5f-8945-2498bb8cf2f1 | -14.19512 | -44.35794 | 2025-04-26 04:10:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc002221-f9e6-3cc3-bd09-1b79c0d7ab56 | -11.40653 | -52.94982 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b103827f-6c21-3097-a38f-45b75600b31a | -13.55225 | -43.68897 | 2025-04-26 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a5edd6b-564c-3f28-a8c8-c25e9ebed7d9 | -12.8747 | -43.77542 | 2025-04-26 04:10:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c90e933-46e5-384f-83c2-24130c64e582 | -11.40239 | -52.94079 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 16f5e135-3522-3c6b-b383-8b3b107db471 | -16.62242 | -43.36911 | 2025-04-26 04:10:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcd64f59-3aa3-35b8-b59e-cd76d0aeb5f2 | -14.19571 | -44.35431 | 2025-04-26 04:10:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5205442f-d81c-3a9c-b5a4-ca5ff2277821 | -17.56741 | -40.6697 | 2025-04-26 04:10:00 | NPP-375D | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6b144b1d-f589-3f5c-ade7-dc42d900179b | -11.40088 | -52.94856 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c307c24-277c-314c-8ff9-e0d47ecd7f89 | -12.87804 | -43.77597 | 2025-04-26 04:10:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 147580a5-e517-3086-8efc-d027e2b47e0a | -16.81553 | -41.22622 | 2025-04-26 04:10:00 | NPP-375D | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 709f95ab-1e2d-30f0-ba5d-ef4c0bffb9a4 | -13.66049 | -43.79459 | 2025-04-26 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea7105a7-b383-3a07-9cdd-b2d107c83f9a | -13.65716 | -43.79401 | 2025-04-26 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1feca08d-2437-3f78-9002-e2a5aece287b | -11.40164 | -52.94464 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ca22e8e-64d5-38aa-8cb9-92d16d764fdf | -15.0794 | -48.94529 | 2025-04-26 04:10:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97ae96d1-2763-39b7-8f79-32403ee69c41 | -11.39673 | -52.93958 | 2025-04-26 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 64b5d59b-7ed9-3fba-9a71-eeceba287bb0 | -23.3373 | -46.77428 | 2025-04-26 04:12:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e8c56e43-1a7a-3060-870f-8f455b02eb01 | -17.75352 | -42.89457 | 2025-04-26 04:12:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7e521d1-08de-388b-8554-a38eb0eef904 | -17.77672 | -42.81031 | 2025-04-26 04:12:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be0e9022-d169-3ea2-ab93-2efb8f72e4a8 | -26.33265 | -53.18902 | 2025-04-26 04:14:00 | NPP-375D | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a7fc01fa-4c12-3567-8966-3586ccc9bb99 | -29.81069 | -51.34422 | 2025-04-26 04:14:00 | NPP-375D | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 9e0131c6-b74a-3703-959d-9d7dfddf77d4 | -29.63478 | -51.30553 | 2025-04-26 04:14:00 | NPP-375D | SÃO SEBASTIÃO DO CAÍ | RIO GRANDE DO SUL | Brasil | 4319505 | 43 | 33 | nan | nan | nan | Pampa | 5.3 |
| dffa849e-99c0-3ba4-8779-6f828bcc5d2b | -29.80974 | -51.34921 | 2025-04-26 04:14:00 | NPP-375D | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 905785fb-8948-3889-a881-543a6baf655c | -23.59341 | -47.43739 | 2025-04-26 04:14:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 90a98960-e0d5-31ff-a385-fc3ea8889959 | -28.20165 | -48.70193 | 2025-04-26 04:14:00 | NPP-375D | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2413893a-22f5-3324-8b5a-461679702762 | -28.20267 | -48.70379 | 2025-04-26 04:14:00 | NPP-375D | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 298faebd-50de-35fb-bdb6-0d974d153618 | -29.58423 | -50.63041 | 2025-04-26 04:14:00 | NPP-375D | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 658a65c4-0a78-394b-977d-86e75253a656 | -28.20506 | -48.70267 | 2025-04-26 04:14:00 | NPP-375D | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ef97a7f3-b8e2-34af-8ac7-a7e2fa91d6c9 | -28.06071 | -48.66978 | 2025-04-26 04:14:00 | NPP-375D | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d3f48249-8826-3109-804c-b531a8a45646 | -11.3965 | -52.9269 | 2025-04-26 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 42c1706c-8a73-3b53-a0ba-aad4fb23e6f1 | -11.3963 | -52.9477 | 2025-04-26 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| a122a9c1-7e11-3ece-806f-2fbe34dffdf3 | -8.09146 | -43.11138 | 2025-04-26 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2a19c4fc-7b59-3eee-a0ed-d6a79c4ef008 | -8.09199 | -43.10776 | 2025-04-26 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9b88f992-9b31-3a36-ac0d-dc48ff3dd253 | -8.08743 | -43.1108 | 2025-04-26 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ee0aec22-69aa-3a2b-9b4e-5865c12ff080 | -7.17575 | -44.87142 | 2025-04-26 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b7146e5-6f3a-34ec-984d-04c84d1a02ae | -8.09602 | -43.10833 | 2025-04-26 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 543e0351-ae79-320b-b2c5-ebc4df75cef8 | -11.4152 | -52.9458 | 2025-04-26 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 5ce6792c-daf9-3587-a00f-eb04d0ae1399 | -11.3963 | -52.9477 | 2025-04-26 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 1e9a7e0d-930d-3402-bdb8-8187d4ec8475 | -11.3965 | -52.9269 | 2025-04-26 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| e7b8cf55-a0f7-3062-96d4-fe016e8af1fa | -11.39635 | -52.94867 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f6e8fff9-fa40-3461-a738-0f9bc90075e1 | -11.39296 | -52.94604 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ef166bb3-9df6-308c-9f3d-42bc92846c73 | -11.40427 | -52.94809 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a4d5e87-2037-3cb7-9693-b4a97df02e24 | -8.93979 | -44.23737 | 2025-04-26 04:32:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5cd06854-9b8e-3d03-b99e-5d3711846705 | -11.39791 | -52.93938 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d5e22ac3-06da-33b2-920a-97a0430b3e61 | -13.65792 | -43.79425 | 2025-04-26 04:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d6c28f2-c214-3c88-9909-4268de9acdd6 | -11.39887 | -52.95673 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7bbf07c5-b404-3f48-9ab7-43c43f7c76c0 | -11.40346 | -52.95274 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0e5a08b4-db97-3901-9146-198014084e7d | -11.39868 | -52.93474 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a251d24e-ba32-340a-b57e-a1d7adcb22c0 | -11.39834 | -52.93747 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| fffa60a1-2ba8-3c2a-ad73-527978dd18d3 | -11.39592 | -52.95138 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0a531a9d-e43c-3ffe-8b97-dd388cef8e13 | -11.40803 | -52.94879 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2f7149b8-77d1-393d-9c5c-737079a9a44f | -11.39969 | -52.95206 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5d4b67e3-0fd3-300a-9282-61c6a3e64033 | -8.94359 | -44.23795 | 2025-04-26 04:32:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20aba94e-338c-3d37-abc2-e7b95772f8b1 | -8.94739 | -44.23853 | 2025-04-26 04:32:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa1c84f6-17dd-3e73-b3d3-1331f087f99a | -8.17513 | -46.70531 | 2025-04-26 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c45bdf64-f4e4-3e9d-9c49-45f4c70a5798 | -11.40264 | -52.95742 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fe698975-394c-3ff4-b39c-cb962d9310c4 | -8.1785 | -46.70584 | 2025-04-26 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08e54a2e-bb0c-3ada-baa0-39028baae20d | -13.5521 | -43.68806 | 2025-04-26 04:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05a3a3e8-7cee-3172-9e1e-cfa1e43c9b7f | -11.40211 | -52.93815 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d7aece8-1c3f-3ca5-9806-7d17b25f8c41 | -11.39754 | -52.94209 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f7b7e427-a664-31df-ae57-f7fc8f52a99c | -11.39492 | -52.93405 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 331ee4ef-6843-3c73-8ebb-c271abac3234 | -11.4005 | -52.9474 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 578c6976-9afd-3759-9eb5-6f22745bf2f9 | -12.41243 | -44.89255 | 2025-04-26 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbb10ea7-dfa4-3712-a3ef-0969f83b6f23 | -11.39713 | -52.94401 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6be2b16f-a4e3-3553-a92f-ba6d5af5cd49 | -11.39377 | -52.94141 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| db6832f4-9a7b-394b-aa32-596d5077126b | -12.24689 | -51.45074 | 2025-04-26 04:32:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 388bca3f-459d-39f7-b653-f245b0783cdd | -15.07775 | -48.94535 | 2025-04-26 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d79363ce-f990-39d1-81e9-558d10aa9b3a | -11.40507 | -52.94345 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec9941a7-7b8b-36ee-b4a4-b297dc4b309b | -13.66848 | -43.78984 | 2025-04-26 04:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef09cc29-0e1f-3351-9fe3-119b9e242461 | -12.877 | -43.7747 | 2025-04-26 04:32:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcb4c2d9-946e-32fb-8317-4ff425f352d1 | -12.56534 | -45.35848 | 2025-04-26 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 420f58c1-fe1d-3c2c-8121-8a3c51f5c6f7 | -13.66685 | -43.79116 | 2025-04-26 04:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README4.md)
