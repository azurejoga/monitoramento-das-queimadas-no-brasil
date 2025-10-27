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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b246d82-0201-3ebd-adc1-78c879f2f2ac | -8.65073 | -47.23846 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdd08260-574e-3726-aea5-6d066fa918ff | -3.15072 | -50.45619 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb5aa4a7-f9b3-39b0-b8eb-5528b148300b | -7.2505 | -44.96102 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90020dcb-da17-32d5-8064-0635bb262651 | -7.88478 | -47.24547 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c9e2084-8064-30ae-80d7-1321ec8b92ce | -8.14895 | -47.03038 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e3b7198-360b-3c7a-a20a-351dc8cadfd7 | -6.37901 | -44.26365 | 2025-10-27 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9c3cf71-aaa0-3d1e-b76c-cf8f883d4453 | -8.65976 | -47.11654 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45694c1e-1e47-3060-83bf-3cbd560bfd8d | -4.07241 | -44.37442 | 2025-10-27 04:32:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53e6d240-70c1-3119-99c8-c879396226ed | -7.82948 | -46.43024 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 44f2ccf2-fe33-3c4e-9727-7f658a694374 | -8.03329 | -45.14513 | 2025-10-27 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7376f5b6-3678-3bad-bb18-e43fad30bc91 | -9.45877 | -47.73297 | 2025-10-27 04:32:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ead6341a-b273-3c8b-8b5b-ce12f2b9787f | -7.85433 | -46.4488 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2891e54d-2654-3bb1-bd5f-bf222e7cad49 | -7.54075 | -46.25165 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49883664-4534-3a4f-8e27-4e259f603222 | -7.85625 | -45.38655 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03effcc3-9cae-3e1f-b336-186ce28e8738 | -5.71696 | -49.31553 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3a2b641-ef23-3224-b0ef-5593af65d719 | -6.88989 | -43.57631 | 2025-10-27 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d595ed8e-aadc-3cfc-916f-2f065c38a1b7 | -6.87502 | -45.16655 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0aaa7354-101e-3c4d-bfa6-340d7e17c2ef | -4.73258 | -41.48388 | 2025-10-27 04:32:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4f82ff51-546e-3310-adc1-96fa29eba7ba | -7.85603 | -46.46028 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 036e3753-053e-31b0-9cd9-b2733b0a29ff | -8.31684 | -46.82244 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c21f406f-3b5a-3a68-8c69-5a30c092f6e8 | -2.89769 | -42.83708 | 2025-10-27 04:32:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dbcc942-41d8-36ae-ba61-1b22d36fc017 | -7.00106 | -46.99983 | 2025-10-27 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0c50584-d2ca-350e-a804-9506d3974baa | -8.30904 | -46.18092 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7a9b5ef-9c39-3673-9097-215079d6a442 | -8.23432 | -46.91992 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fe9070a-ca03-34af-8978-799117ea92d4 | -5.76649 | -45.55738 | 2025-10-27 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12acb60e-fb1b-3176-8ef1-dbaac421fae8 | -7.83736 | -46.42395 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed8b9598-2c0a-3cfc-82bf-95561f916364 | -7.59824 | -45.68468 | 2025-10-27 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb2a3799-712a-3466-a5ed-1add4b3170ed | -3.74011 | -52.43024 | 2025-10-27 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bba207e-2532-3e92-9930-167523ab5242 | -7.86893 | -46.42125 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 804d74df-adce-33fe-bc30-62ee8d30abb9 | -9.13546 | -45.86021 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2da0dc87-a304-3a83-824a-381bfce985fa | -4.63748 | -49.53777 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0595a62-1428-333c-bf74-07ddb7fd0164 | -9.8245 | -44.22997 | 2025-10-27 04:32:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dd48f80-3e4e-3a90-a901-bad78d9e78c5 | -3.22824 | -48.76879 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0920fecf-97b8-35db-887d-bcd8b592f077 | -4.44844 | -45.45557 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| df019682-b61b-38a5-b4a2-1c9769f08ee6 | -8.83636 | -45.41457 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66e4c9cc-a0d0-3c35-ad61-7ab20d36603f | -3.57428 | -49.02159 | 2025-10-27 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8e5a0bd-75ad-393b-973d-17b4dfb7fd91 | -7.82726 | -46.44483 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 25298053-505b-3acf-8ec6-a9d1a85305f7 | -9.04138 | -47.61718 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 341e3a94-e6eb-3200-a496-9eb14db95194 | -2.35495 | -48.28922 | 2025-10-27 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f944c99c-1ede-3641-8521-021c4d1db711 | -8.52491 | -50.07468 | 2025-10-27 04:32:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 541ab6e7-20fa-3f5e-9e1d-6e07325907e2 | -9.46263 | -47.72998 | 2025-10-27 04:32:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 86f2c9b2-0739-31ff-a521-6bab3a95e7a4 | -8.23043 | -46.92296 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60543c54-0393-3b67-b6c7-c1fa048c9d58 | -7.78924 | -45.37365 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acc7348e-16a7-3f3a-813f-efffd8428bec | -4.65865 | -46.39924 | 2025-10-27 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c41d679-3bea-3c2d-97e4-c23eaff65aa1 | -3.09798 | -49.4539 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f9ab508-36d4-3bd3-8acc-7c98ae911a72 | -8.14507 | -47.03344 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc574faa-149c-3a82-a8d6-867a84762956 | -3.08144 | -51.27079 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d836f19-5f9a-35cd-996d-53a5c9c9e848 | -9.2203 | -45.60854 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2dd88c34-1142-3128-b835-f06dc226a20a | -3.34398 | -49.84386 | 2025-10-27 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7236eeba-94c3-3b95-a647-693e6991eaee | -3.17817 | -52.49559 | 2025-10-27 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36b809ca-b5af-35ce-b2a8-4a2125749f1d | -3.11737 | -51.21179 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d082b52-6b6d-3a43-9526-013983f21758 | -1.37976 | -55.34932 | 2025-10-27 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8354cfd5-a1ff-3c81-8183-834e098aa5ce | -8.10437 | -47.05642 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf9160d9-08cb-3cfa-88b3-a49046ac814b | -5.75767 | -53.39704 | 2025-10-27 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34819c78-234c-3a5d-9589-1330eb66ca7e | -6.89613 | -45.16974 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75667f6d-4061-3e5e-a665-bdb2e11159ba | -8.96183 | -47.18528 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8474f878-8cfc-3fbc-bdba-1f53377163fc | -7.83342 | -46.42708 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58b99bdd-e569-3984-bd51-9f1ffdf621be | -5.82499 | -40.82019 | 2025-10-27 04:32:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e5d5c1f-5ef8-347c-8b43-3748f9dac386 | -7.8469 | -46.40678 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d01e15d0-c8ad-3fa1-8987-38b18d62b1e1 | -5.21582 | -46.22583 | 2025-10-27 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c740672e-e63b-3f60-8596-d4d3eba283ab | -7.15671 | -43.73428 | 2025-10-27 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d882a90-3e3c-32be-a701-c0df659a7b36 | -2.77548 | -54.57275 | 2025-10-27 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8a4bc6e-3d68-3c6a-a2d6-b0db76b8325d | -10.01743 | -47.17153 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3537e1d9-556a-3388-b697-20617e29a648 | -5.43115 | -40.87787 | 2025-10-27 04:32:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a03d0585-70a5-36e9-b01d-ffb29d3336e0 | -3.09726 | -54.61792 | 2025-10-27 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d45a8c84-5d24-3ac2-95bc-fc4fb66f98fd | -7.4385 | -41.87072 | 2025-10-27 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ad27bc38-4c14-3b92-aa29-20026ed1d50f | -2.90276 | -53.12981 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 015de617-c855-3c24-ab31-8eee805b19a3 | -6.49033 | -43.63149 | 2025-10-27 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 293b3686-69cc-3f40-ad83-0d08ffc0e57a | -2.63602 | -47.29908 | 2025-10-27 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6bc1bb75-20c9-35a1-8b63-40234449c4c1 | -7.85104 | -46.49289 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce518a64-81fb-358c-aa99-91c3e2cd7d07 | -3.24314 | -50.65127 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fe6e85cc-7882-3d4a-8e90-1565cf97bb1b | -4.31951 | -48.08886 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37ce2130-0aaf-3c05-bac4-fc67c3ed42b1 | -5.64772 | -41.0915 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b6fa6903-809a-3d61-b26e-51fb0f5cf7ac | -5.66002 | -48.45876 | 2025-10-27 04:32:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6665cc6d-a39c-330a-ab64-3c5a30ef7c08 | -7.12937 | -39.43199 | 2025-10-27 04:32:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4f653cbb-6010-378f-a8cd-18990b849a67 | -4.83457 | -45.34252 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2991b55-e90d-3807-92e2-8086f6c79e23 | -9.13606 | -45.85624 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4e08919-7ff3-318f-be2a-1a98e2026278 | -3.15079 | -50.33569 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f60bb2c1-9483-3427-8ab3-19456ff5adf3 | -6.67109 | -41.50941 | 2025-10-27 04:32:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f1387bc-8eed-35fe-a242-4f05d2479a89 | -6.90514 | -46.14138 | 2025-10-27 04:32:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a36a5d4e-2067-3987-b771-9d44970957a6 | -6.44237 | -42.3442 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4473168b-e0f5-34ce-a4f4-16b269ab82a6 | -7.13127 | -47.05992 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef164fb6-1f50-3e4d-abed-afa9c71064e0 | -4.45909 | -43.43439 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8f40e3e-5801-3686-8012-8d18a02f6285 | -3.76157 | -47.61073 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a9915ef-1420-3682-9c35-eb2211bf8994 | -7.83857 | -46.4614 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e72c77ce-6054-3098-8442-c0438a816e64 | -4.63688 | -49.54155 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52dc52ba-be3e-3f8d-8f80-d7b53415d500 | -3.25379 | -50.04479 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8ab5fd1-5ff7-3d49-9fa2-9e49bf7a110e | -3.15608 | -50.33094 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 19a13f67-9ae2-3a43-bf66-3ed22f8d9fc0 | -7.8514 | -46.39994 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4414f050-ee1a-3837-8c7a-6179b9d25830 | -7.83526 | -46.48309 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 0ea03d12-b1ed-3e2b-ae0f-a88624d7d716 | -2.32603 | -48.58419 | 2025-10-27 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d4fd4bd-0694-3d13-bbea-28b62895e7f8 | -5.47561 | -37.85277 | 2025-10-27 04:32:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 51390179-7d25-39f6-b6c7-674b33be227f | -5.52009 | -41.71597 | 2025-10-27 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b1ae1a0a-4640-39b0-905a-aa23f9717215 | -7.82836 | -46.43758 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dac241c1-d5a3-3ca4-a977-114a25a66594 | -3.83826 | -50.1984 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eaa08cac-2176-34f1-9246-64991e1ac1f6 | -6.23422 | -42.5498 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e7b79be4-a6c3-3fd7-a3f5-ead353bf4222 | -4.83115 | -45.34201 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 286fbac1-a56c-307a-8ae2-87a588b328c7 | -7.22904 | -44.33728 | 2025-10-27 04:32:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5346038b-3573-3170-a951-3e732225fc5f | -5.46718 | -47.4366 | 2025-10-27 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb0f3d7a-a207-3e37-9e27-1b009c1f306e | -7.03757 | -43.93771 | 2025-10-27 04:32:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README44.md)
