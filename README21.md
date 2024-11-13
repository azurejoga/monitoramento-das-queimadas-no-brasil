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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5daefaff-8242-364c-8cec-e8e2a962b3ac | -4.69431 | -46.38962 | 2024-11-13 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 232ad7f5-b794-370c-9c50-9af683f0fba3 | -4.4107 | -49.7268 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 337ee0d1-a965-37e8-9fac-d2d9ef8a7b1d | -5.36026 | -43.52955 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1c72e84-86e5-3411-ab95-982f899a5793 | -10.55522 | -47.59076 | 2024-11-13 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26f3ead6-5aad-3b8d-bb1e-10653d83dc22 | -5.37165 | -43.72433 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b434807-a99c-33f7-a79f-2d1073c367cb | -6.82473 | -46.77948 | 2024-11-13 04:06:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3892a5c3-a4d4-3614-b98f-6946bb574020 | -10.55459 | -47.59436 | 2024-11-13 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc97d1e4-3095-3e62-89b8-16d6a4175ca8 | -4.3289 | -48.61509 | 2024-11-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aaa629b4-eabc-3b04-9614-9e1c28e5173c | -3.65872 | -54.65781 | 2024-11-13 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91009590-006d-3b2a-8263-9d1e4d685de3 | -3.76142 | -54.65875 | 2024-11-13 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13507939-b143-3155-9149-b73300d51b2b | -4.65787 | -47.42734 | 2024-11-13 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f262d935-afc8-3b66-9139-12560177b13e | -4.82598 | -44.50879 | 2024-11-13 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f461a15-6ab9-3ee7-8075-342c0fe894c1 | -6.55462 | -35.2798 | 2024-11-13 04:06:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a67c3fac-2d98-392b-aa41-d0f6f902caf9 | -5.35334 | -43.52845 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b60bf20-be60-35f0-be70-9e3647fe9b95 | -3.70602 | -51.84308 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc23f1d1-db7a-3b32-9153-3ac75cd213d1 | -3.76406 | -54.66171 | 2024-11-13 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bb414fb7-6b4e-3e86-aa87-346505e58882 | -3.85887 | -51.91413 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af0bd66c-ff39-3a74-a3e0-a4d18f37dbd4 | -5.0743 | -45.51932 | 2024-11-13 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f828cdc-b15e-3dd1-8369-3a7acc1793f9 | -4.772 | -45.57844 | 2024-11-13 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1723cdac-2f42-31c6-b330-d34e01ddce69 | -5.88052 | -48.00015 | 2024-11-13 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75b2254c-c35e-3944-9bf2-64a7a342daac | -5.21574 | -44.67076 | 2024-11-13 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b75cdcc-6c48-31c5-b16c-e37ff7265648 | -4.5974 | -46.94932 | 2024-11-13 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 159d1d3e-38bd-36b0-9f34-d24d9717e8f8 | -4.08581 | -49.14368 | 2024-11-13 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5349cfb0-cccb-3ae1-8311-e9bb329755de | -4.65645 | -47.43593 | 2024-11-13 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6f269f8c-002d-3ed4-ae90-1f8dc57e6770 | -4.11062 | -51.11016 | 2024-11-13 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77acfe8e-83bf-3fea-a9b8-c99e522577ba | -3.70678 | -51.83855 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8db1b7df-930d-3276-9920-e5e24a9a6ad9 | -4.40857 | -49.64415 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ad20588-fe92-3f90-8722-af8578bec18f | -5.00739 | -43.67252 | 2024-11-13 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 872f7bdf-f413-3551-bb75-e698457bd62e | -5.97302 | -39.32457 | 2024-11-13 04:06:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74f1057d-4b38-3112-85ef-fcf5b4d829c4 | -5.9014 | -46.23552 | 2024-11-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 534a25a3-5405-31d1-91a2-d3f4b7bad3dc | -5.49685 | -42.89721 | 2024-11-13 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a69cc604-9de9-325c-9fcc-18fecd019dcf | -3.72645 | -51.33278 | 2024-11-13 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24f21904-ccf9-3cde-88f2-ed9654723d5c | -4.11405 | -54.23785 | 2024-11-13 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6776d9b3-0bad-34b5-9a75-329871d12fa4 | -6.74942 | -35.33113 | 2024-11-13 04:06:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f4c877f9-3d60-32d6-9ace-65e90ac1c3c4 | -4.81482 | -44.48525 | 2024-11-13 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29368842-b71b-3df0-be12-0d3ae996433f | -4.47074 | -49.6343 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16ba5c20-7151-388d-ac2a-7f120124fd18 | -3.65744 | -54.6652 | 2024-11-13 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2819c63d-f46d-37e3-b8c2-ec703c1c4734 | -7.5491 | -47.58388 | 2024-11-13 04:06:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b594618c-ae4f-38a4-b30f-47b6f0beb81f | -3.25232 | -54.5328 | 2024-11-13 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d10e33ad-573c-3659-ba7d-61f07c7206c1 | -5.25147 | -49.79305 | 2024-11-13 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 171f3e05-997e-3cba-a350-cd7bbc8c92b0 | -5.41376 | -43.32918 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e52a5f6a-14d6-33e6-a90b-793f2bb9a986 | -3.79448 | -52.10067 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f664b5a-8a38-31d9-8031-697364736314 | -3.75842 | -54.65214 | 2024-11-13 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 52526791-25e8-30e2-b9e7-661225a76659 | -3.81521 | -51.26846 | 2024-11-13 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 87980fb0-1eed-3c39-8440-9e8cb8489e80 | -3.98118 | -49.94542 | 2024-11-13 04:06:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d59a0535-6f53-3b60-8234-fb229dacc2d9 | -3.87909 | -51.17282 | 2024-11-13 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16a2f2f2-95d4-3978-928b-6294c31f293e | -4.56441 | -49.38747 | 2024-11-13 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c869f025-5136-3ea0-8c54-44c0884213ff | -5.92395 | -42.96795 | 2024-11-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe936f45-5bbe-3a0f-b277-c48c02ba3eaf | -5.08188 | -45.98925 | 2024-11-13 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff50976d-f318-3848-8355-38f30876ba3a | -4.59804 | -46.94549 | 2024-11-13 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58942232-bcbf-373a-966c-1cfed6df8cdb | -4.33583 | -50.4248 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9ce38707-c4f7-35f9-96f9-827c9a3d0c31 | -4.77122 | -45.5831 | 2024-11-13 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecbe5444-b964-340e-bbcd-c6d23eb4e28b | -4.76039 | -45.44745 | 2024-11-13 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c45a3fe5-8910-3025-ac76-8236463ad505 | -5.01235 | -44.09156 | 2024-11-13 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3f1775e-9806-3def-869b-ea827a8aceb5 | -4.38919 | -47.2812 | 2024-11-13 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78ae4b76-1b7e-3159-9c7a-de3d778fe84c | -7.45902 | -35.14626 | 2024-11-13 04:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 579dd058-b5dd-3378-b30a-bdd62d546891 | -4.56392 | -49.39039 | 2024-11-13 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d49aef61-0d77-3668-88cc-122f46c976a8 | -4.41269 | -48.84974 | 2024-11-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b4621747-be7a-3498-8e1a-7bb1f55bbfae | -5.35965 | -43.53334 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fd47b68-a12d-3b0d-aef7-f99690de7b1e | -3.72715 | -51.32871 | 2024-11-13 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 004916fb-3cc8-3aed-83a5-c150eb18ba02 | -4.32984 | -50.42725 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 15e05719-160e-3403-887b-6be416e168dd | -4.11132 | -51.10609 | 2024-11-13 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed2ba599-385d-356a-b6c7-99a6dde45889 | -6.13024 | -38.8928 | 2024-11-13 04:06:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fb8380de-4026-33d1-b8c1-c2fd276121d4 | -4.92542 | -44.65726 | 2024-11-13 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 56818dca-6342-3716-8900-ea4c8b89c2c0 | -5.07458 | -44.26691 | 2024-11-13 04:06:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a68d8b4-a065-3009-8a04-37e4aadea3de | -4.4128 | -49.72551 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be077e0e-02c4-30fd-8058-3c2a471d2fec | -4.41173 | -49.73169 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb68589a-7f98-32a7-8ef1-fafe474a4d36 | -3.56801 | -53.01273 | 2024-11-13 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 085b838c-6021-3e72-a164-a557c5875f6f | -6.18143 | -41.81748 | 2024-11-13 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 69144c3f-051c-3669-84b2-db7371890ad8 | -8.38466 | -44.47975 | 2024-11-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4bfd202-17f7-3397-b9cc-ceac151f3d63 | -4.56488 | -49.38463 | 2024-11-13 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ec73b095-41d6-375d-8e15-dadb3b93e348 | -5.41093 | -43.32488 | 2024-11-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 209ef98b-a688-3913-ae21-e52090098273 | -4.31411 | -50.81828 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e547024-abcc-3113-a80f-09ab84e5d1f9 | -4.41228 | -49.72852 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8e669c0-b887-30f4-a59b-efbf892a7265 | -3.13955 | -54.48785 | 2024-11-13 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d46de94a-c0ae-36a2-8278-605888764bd3 | -3.76837 | -54.66074 | 2024-11-13 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e83dd316-18a1-3944-88e2-1326e5bb15b6 | -3.52424 | -54.48508 | 2024-11-13 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c82fc82-d452-3e51-98b8-4b31da81faf8 | -4.16115 | -50.74911 | 2024-11-13 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ed93990-f263-3f20-8f7e-f2e61727601c | -4.41019 | -49.7299 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72f67322-0352-3225-8e47-635bb1326088 | -4.6125 | -46.96363 | 2024-11-13 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b901911-e508-3e13-a4c6-0004cefacf7b | -4.37028 | -48.08413 | 2024-11-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a06db28-20da-3774-827e-6fbba8c1ffb7 | -3.25821 | -54.54074 | 2024-11-13 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d433c0dd-1c6a-3052-a9f3-741ed396c5ff | -4.24569 | -50.25698 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2ce884d-9946-389e-9aae-bf245b1b96d7 | -3.81596 | -51.26419 | 2024-11-13 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ea2b834-3422-3130-90a8-79be4a733289 | -3.87839 | -51.17689 | 2024-11-13 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c31b46fb-711a-3ff3-8497-43e96fa87fa8 | -4.5173 | -48.92937 | 2024-11-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d780f2bf-d0ca-32d0-b8f8-4a8654451f93 | -3.8581 | -51.91859 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a59fd913-78bf-38fc-9304-ea1980061ba5 | -4.69491 | -46.38593 | 2024-11-13 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 84f56f9d-059e-3f9f-8e6c-e600b3b3e978 | -3.52304 | -54.49191 | 2024-11-13 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5fdbd45-4c6c-3658-a0d9-3b651a6c15ea | -4.92556 | -44.6598 | 2024-11-13 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 91e2f7cc-a76d-3447-9b2e-99c13cde086a | -6.75004 | -35.32686 | 2024-11-13 04:06:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3ccfdfcf-8646-3805-9d83-e5a6e23506ea | -4.29735 | -48.10036 | 2024-11-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e756b89-2f58-3a6c-9d4e-edc5478b1714 | -3.80058 | -52.10158 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfe67b4d-f4ec-31c0-be4c-94a8373f75b9 | -4.77722 | -50.5577 | 2024-11-13 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9dc4c55-1ed2-3296-b425-b024d0a10d33 | -3.80161 | -52.10048 | 2024-11-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e47c42a8-aa4f-3434-aee7-77f9bf8babcc | -3.9711 | -50.94039 | 2024-11-13 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8486eea-4559-3893-974c-ef216b2561c6 | -5.05143 | -44.48075 | 2024-11-13 04:06:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ebec9399-f70e-3c0e-b95f-9f911018e52c | -3.97672 | -50.94142 | 2024-11-13 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7270000f-263d-3fbc-b43f-eb084439127f | -4.77503 | -45.57773 | 2024-11-13 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06274fba-827b-3583-8241-ca30f74a0a79 | -5.79765 | -46.47966 | 2024-11-13 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README22.md)
