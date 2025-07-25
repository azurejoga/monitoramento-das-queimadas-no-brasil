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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 162817e7-5380-3b27-9dcb-87cc7e3cc41c | -7.9259 | -44.0706 | 2025-07-25 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 3d9ecea9-be14-3e25-b096-beb086ee784f | -7.9256 | -44.0937 | 2025-07-25 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| a02bc8be-25c2-3e4e-8148-24b18812d675 | -8.8305 | -45.6015 | 2025-07-25 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| dd8e7d35-dfce-342f-8751-dac516050fdb | -7.2597 | -43.0645 | 2025-07-25 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| d0a78cda-01fa-327f-aede-b9668edada19 | -8.0886 | -43.1431 | 2025-07-25 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| b208a744-6c62-3ba3-903a-7aa1215a6059 | -11.9518 | -58.7574 | 2025-07-25 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f87de1f4-509c-303b-93b2-5d06ae0344b3 | -6.961 | -44.5546 | 2025-07-25 02:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a816f6c4-969e-340b-8ebe-5a9c46a3f172 | -7.2597 | -43.0645 | 2025-07-25 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| ce2499f6-04cc-3fdb-8d71-9dce831d9fe1 | -7.9256 | -44.0937 | 2025-07-25 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 6e6534e0-4903-35f8-88aa-e457753b06cb | -7.9068 | -44.0957 | 2025-07-25 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ac8d4c43-c6db-37ae-be61-ba7089242e5b | -11.458 | -45.1357 | 2025-07-25 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 97c8befd-cf7e-3690-97bb-bbc50d508293 | -8.0886 | -43.1431 | 2025-07-25 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| fdcf818b-7a90-302d-a7c8-5529aa3ecb95 | -11.4584 | -45.1126 | 2025-07-25 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 3a858ce3-5a2b-37f5-ab0d-d8f914f06924 | -6.9422 | -44.5562 | 2025-07-25 02:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| cd46932e-75e4-3e96-b3fa-6db1250a62bf | -7.9068 | -44.0957 | 2025-07-25 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 8d8c9ac6-c455-3701-bbe1-bdc9e59479ab | -7.2597 | -43.0645 | 2025-07-25 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 8b4d3e20-3de1-32e4-b0b4-56f7f0314d09 | -6.9422 | -44.5562 | 2025-07-25 02:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b1a5ebb7-75d9-3d65-ac9e-efd07f02e2cc | -11.4584 | -45.1126 | 2025-07-25 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| d5d38ce1-0a7d-3fa4-b1ec-4b09cc2c8c7d | -7.9256 | -44.0937 | 2025-07-25 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 74fed552-a3f7-3455-8a35-2963f66a1f4b | -8.0886 | -43.1431 | 2025-07-25 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 0765f05a-3840-3321-8b5f-758c79ec6eed | -7.9256 | -44.0937 | 2025-07-25 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 134098cb-2b0e-3b97-9ddd-f1066b35b680 | -7.2597 | -43.0645 | 2025-07-25 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 542b5306-d151-3478-8a02-83f7d68d5784 | -11.4584 | -45.1126 | 2025-07-25 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ce4d19f3-b581-3982-8e63-25022b6385d2 | -11.458 | -45.1357 | 2025-07-25 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| f3ac43b2-352d-307c-a757-fa920b9bdfc0 | -6.961 | -44.5546 | 2025-07-25 02:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 16e499ee-0b95-3ef1-86c5-934c6bc68f65 | -6.9422 | -44.5562 | 2025-07-25 02:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a9bc1a1a-da88-36a4-8fe0-930206b65192 | -7.9256 | -44.0937 | 2025-07-25 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 746f1d43-40ce-3c1e-b3f4-b8f8370250b1 | -11.458 | -45.1357 | 2025-07-25 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0f0f919e-50a0-30cf-bd84-754b08bbd5e1 | -11.4584 | -45.1126 | 2025-07-25 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 89924232-b1f5-3cd1-8a2b-7d32a468e01d | -7.9068 | -44.0957 | 2025-07-25 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 9716132a-84f9-3c3b-a892-97e99b5c3c80 | -6.9422 | -44.5562 | 2025-07-25 02:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 3585be15-67ce-35d6-a631-03fabfc891ae | -7.2597 | -43.0645 | 2025-07-25 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 4b2a3dbc-98b7-3d1a-9435-f260dd7b11f4 | -7.2597 | -43.0645 | 2025-07-25 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 6e258be0-3adb-39c9-b5ab-aefcc8e16c2c | -7.9256 | -44.0937 | 2025-07-25 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b10977fd-c20a-308c-8181-1cb61d4ba6f6 | -11.4584 | -45.1126 | 2025-07-25 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| d1cf3815-6b41-36b3-b81b-a9d7d776350a | -6.961 | -44.5546 | 2025-07-25 02:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| daaa9292-b05a-36f0-95e7-933c60fe921e | -6.9422 | -44.5562 | 2025-07-25 02:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| fa021955-8636-3a7e-936c-9a41e3336342 | -11.4584 | -45.1126 | 2025-07-25 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| a42e6980-7118-3c3d-a939-f008493e64b9 | -6.9422 | -44.5562 | 2025-07-25 03:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 7a853b4e-627b-3434-9b07-9c5202bf9a8b | -7.2597 | -43.0645 | 2025-07-25 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| fc698f22-bf58-3be9-adcb-3e5b896bc551 | -8.0886 | -43.1431 | 2025-07-25 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 28abea33-91f0-3f72-aa2f-b6ab8999d56a | -6.961 | -44.5546 | 2025-07-25 03:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 116771e4-b186-3871-9524-d1be7cbd8440 | -7.9068 | -44.0957 | 2025-07-25 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 5f71d1e0-731b-3bab-a1b0-5c7f3dca6708 | -7.9256 | -44.0937 | 2025-07-25 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 973a115b-aec6-3e2c-9fe6-93017ce46764 | -11.458 | -45.1357 | 2025-07-25 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 90b2a641-bc8b-38a5-93e5-e357cde65ee8 | -16.69607 | -41.01632 | 2025-07-25 03:06:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f72be712-bc40-3d7c-8fba-3f4adda4248e | -16.68961 | -41.01492 | 2025-07-25 03:06:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9a4bee6c-01ec-30a9-a60c-c9162d132abc | -7.9068 | -44.0957 | 2025-07-25 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3bf88777-9c48-3aa9-a4d2-909bd5379856 | -7.9256 | -44.0937 | 2025-07-25 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e8badee7-d58f-37a8-b04f-40badf53fa4f | -11.4584 | -45.1126 | 2025-07-25 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| d880a6fb-df7d-3cdb-b447-edbf81109d5a | -11.458 | -45.1357 | 2025-07-25 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| fffc2952-9880-3fca-b49d-aed31e3ec780 | -7.2597 | -43.0645 | 2025-07-25 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 916490cd-83fc-336e-a8c2-93effbf1bd0c | -6.9422 | -44.5562 | 2025-07-25 03:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ee0340c9-13a0-34c5-a46d-683803f3229f | -7.2597 | -43.0645 | 2025-07-25 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 8491f649-d6a9-3671-a337-2a5aae59c4e9 | -11.458 | -45.1357 | 2025-07-25 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5b5756bf-c6fd-3154-863b-5dba05db835f | -11.4584 | -45.1126 | 2025-07-25 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 8309e8dc-19da-3027-8a07-05f1ca81f727 | -7.9256 | -44.0937 | 2025-07-25 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4f4bb8c2-ad23-32fe-ae57-13b2c9f6532a | -11.458 | -45.1357 | 2025-07-25 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 3b79722f-55dc-3d5f-b543-f854cb46c3b5 | -7.2597 | -43.0645 | 2025-07-25 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| af2d8434-0b17-3dcf-b25d-11dfb8ac6818 | -11.4584 | -45.1126 | 2025-07-25 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| ca0af2f1-e7ca-38a1-8d15-0a251e710c94 | -7.9256 | -44.0937 | 2025-07-25 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 7634c0e3-b1fd-36fe-9e1c-1b9975a81723 | -6.961 | -44.5546 | 2025-07-25 03:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 7995eda7-abaa-3b06-a3ba-f3f5a3823878 | -11.4584 | -45.1126 | 2025-07-25 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 5f6861d7-f950-3dde-8ab8-c1094cb2336c | -6.961 | -44.5546 | 2025-07-25 03:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| d9d34186-3c53-3463-b6e1-2a92a207cf4d | -7.9256 | -44.0937 | 2025-07-25 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e74f3da0-cb0b-3ca2-816b-c0185fa68c04 | -11.458 | -45.1357 | 2025-07-25 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b820221a-1191-3e11-8980-3e37dcedf479 | -7.2597 | -43.0645 | 2025-07-25 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 5599c6c2-e731-3fe0-8a26-fb7442ac13ab | -11.4584 | -45.1126 | 2025-07-25 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 223d3ad0-537d-3e69-b7d3-04516f35097c | -11.458 | -45.1357 | 2025-07-25 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| cd78220d-3587-3223-93cd-03fffc98fa25 | -7.2597 | -43.0645 | 2025-07-25 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 49d4e3d7-f67a-30c9-be61-fd147f9d0ebd | -3.39442 | -46.90476 | 2025-07-25 03:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c38a44d-28e5-3c42-a86d-b62aa0975b24 | -4.29591 | -48.05782 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0addc25f-6f9f-36e4-8d79-f73e4f438f6f | -3.74469 | -49.04868 | 2025-07-25 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0421914a-ff1b-3be0-ad6a-6e64020c661c | -3.47579 | -42.85355 | 2025-07-25 03:53:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00c34a02-867d-3e81-b260-29ab96df7dcc | -3.04283 | -47.38765 | 2025-07-25 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bcff5028-2c9a-3803-9473-620da43739f6 | -4.29526 | -48.0617 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3eb21d5d-2a9e-3163-acf2-a48e98dbd3f7 | -4.31218 | -47.98281 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40c34473-8c44-3b0c-8f19-f097a318fdb9 | -4.83369 | -45.30385 | 2025-07-25 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d40aece7-38a3-388b-9c9d-c68a0862aed8 | -2.99274 | -49.32025 | 2025-07-25 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d617ded0-7de4-3551-96ce-741f9cb36a5f | -4.77744 | -45.33673 | 2025-07-25 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f86fc5e0-ceb6-3c2b-8528-4fd55f65a9ef | -5.48077 | -42.15309 | 2025-07-25 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4b01e2ac-4bb2-3675-935a-9cfd7e0ae471 | -2.91495 | -48.24889 | 2025-07-25 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 807bdf66-3cb1-3bf8-b065-f8cbb16924b7 | -4.78068 | -45.33487 | 2025-07-25 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 96ce5f52-3af6-3aed-bd09-e2741c36cb69 | -3.05508 | -47.38208 | 2025-07-25 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38b4dfd3-1575-3ff2-94d1-87a2a42cd8d3 | -4.29332 | -48.05724 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f4785ac-0fe5-3eba-a5f2-58cd31e495e9 | -3.32646 | -48.7169 | 2025-07-25 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f914080-fbf1-3540-8f5d-f9bfdcbcc92f | -2.90911 | -48.24797 | 2025-07-25 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a4059d0c-8958-3b70-a9fe-fe0f2c1e9304 | -3.05572 | -47.37832 | 2025-07-25 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0dd4c1d-c7a7-3ed2-bdb6-edc5d23eb5f9 | -3.32266 | -48.71959 | 2025-07-25 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ab980dc6-1ad7-3c85-ba07-aa96eea135e6 | -2.90769 | -48.25639 | 2025-07-25 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2e8a2e9-2bb1-3935-8894-34901575cb57 | -3.31976 | -48.72029 | 2025-07-25 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fa65dac-6c8a-356a-95ce-ce418de3e480 | -3.74548 | -49.04408 | 2025-07-25 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6661cd6e-756e-3a8e-a8a0-80376392f7ae | -3.39972 | -46.90564 | 2025-07-25 03:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3ff4588-0623-3cc8-8454-a8a2c3cf8b48 | -2.86095 | -46.77322 | 2025-07-25 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72246383-ba2f-3f22-9f30-aef76c33d5df | -4.31776 | -47.98394 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb04262f-07ae-3c47-8458-3992fa378da8 | -2.91354 | -48.25726 | 2025-07-25 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 473fcdec-f138-3a91-b029-ded676d688bd | -3.04895 | -47.38491 | 2025-07-25 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 32af97e5-31a2-3f8a-b919-864d12907170 | -3.04047 | -40.81546 | 2025-07-25 03:53:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 94f0c511-949c-38ce-880e-ba548657d2d9 | -3.05022 | -47.37741 | 2025-07-25 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9a18191b-85a5-3f10-8420-525d3bc40efa | -3.32342 | -48.71521 | 2025-07-25 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README6.md)
