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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f5d799d-2a6e-3aaf-804f-407b431955e8 | -5.7521 | -49.25 | 2025-11-18 00:55:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d234362-6a39-383a-8781-bf3ba7d5b14b | -9.0866 | -44.331799 | 2025-11-18 00:55:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ff30ca2-6027-3920-9a75-22c3935087a5 | -6.6623 | -42.016899 | 2025-11-18 00:55:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 535f4562-aacc-38d8-be08-3d40d43048a0 | -9.0831 | -44.3176 | 2025-11-18 00:55:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 09487885-c742-39d7-a5e2-859a33f19915 | -4.1925 | -44.224499 | 2025-11-18 00:55:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91f3e044-4dc3-3014-8842-085cee595de9 | -10.6605 | -49.359001 | 2025-11-18 00:55:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b74db0f-999e-3944-a90f-feffbdee04ea | -4.9707 | -44.6805 | 2025-11-18 00:55:00 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cedb28d-527e-3b94-89f4-90fbf109176d | -9.3941 | -48.449902 | 2025-11-18 00:55:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 644bf6d2-b25d-34a0-ae96-3a067fa10348 | -5.9988 | -51.515301 | 2025-11-18 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 890beb17-2e79-3073-b1e6-aafb14584067 | -3.6655 | -50.212399 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e128f85-75bc-392a-bcea-be21731bba7d | -6.8346 | -46.294601 | 2025-11-18 00:55:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19cefac7-f0c4-33f5-8f08-1b91fb6a0d93 | -4.8691 | -49.0042 | 2025-11-18 00:55:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5bc4b1b-3191-3eb4-96a6-1b6603f3ce55 | -3.753 | -50.9468 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdeb1aed-7696-3c07-af86-d3498cf74268 | -3.1677 | -48.607498 | 2025-11-18 00:55:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca6029ab-45c7-3ed6-8fb4-20a831e23a2e | -4.6393 | -45.520802 | 2025-11-18 00:55:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a90d553-b471-3018-b000-5d3fba5d1f17 | -6.1179 | -42.9552 | 2025-11-18 00:55:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a2f12481-7a82-32d7-b64c-e7e332c16c16 | -7.616 | -42.579601 | 2025-11-18 00:55:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1aeda50d-90a1-383f-a9b1-dc292541be26 | -2.8296 | -45.429901 | 2025-11-18 00:55:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3772b547-c5b9-323e-b1a0-05e7ede19ada | -3.1238 | -45.7598 | 2025-11-18 00:55:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 95667e84-3310-3e9a-8aea-c0a01fb84114 | -10.794 | -47.644299 | 2025-11-18 00:55:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49760962-65a5-3c5b-8931-51b0195107fb | -6.2135 | -46.8853 | 2025-11-18 00:55:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4e84415-dcd9-35d2-b950-cbd1efc13697 | -2.8579 | -45.246799 | 2025-11-18 00:55:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e25f5814-aaee-3ad5-87c2-7ae711ee68d8 | -11.2101 | -49.414001 | 2025-11-18 00:55:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ffb23a9-b3a9-3c2d-ab33-5fd14f9c9e97 | -3.0817 | -51.256199 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d724df31-a5db-3fed-bcda-11169e3eadba | -8.4658 | -47.975201 | 2025-11-18 00:55:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7b4caaa-ad55-3d80-8093-f4f7383d2be6 | -2.8643 | -49.471802 | 2025-11-18 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfe2ef51-2fd5-383a-97b5-678af4c8b090 | 1.5182 | -55.970798 | 2025-11-18 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17a55d40-3612-3789-bdb1-9558713e9e32 | -2.5159 | -47.802799 | 2025-11-18 00:55:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9922b402-3e93-3d16-8d2b-85e2172f0953 | -3.2777 | -52.421902 | 2025-11-18 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dba02313-8010-38de-8575-a3201f8b2819 | -3.1466 | -45.080601 | 2025-11-18 00:55:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| edc77b38-7790-3cb3-94b8-e61f3ba5da8a | -3.7199 | -52.056999 | 2025-11-18 00:55:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6f2ae5d-37cc-32fe-94f9-9299905c99e1 | -2.2779 | -51.931301 | 2025-11-18 00:55:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4d4bada-b085-399d-a674-974364528d49 | -8.2918 | -43.9977 | 2025-11-18 00:55:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f7022159-e4aa-35ec-8c97-8893712dcafd | -0.9878 | -47.071899 | 2025-11-18 00:55:00 | METOP-C | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86908af5-e702-385f-a1ee-452de24173d9 | -6.9343 | -49.6717 | 2025-11-18 00:55:00 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf05382b-fcad-31a3-8fd0-c598ae236d4b | -6.9424 | -49.6619 | 2025-11-18 00:55:00 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6f01073-9212-3bc3-bcbb-ef73918e3696 | -4.5995 | -45.9547 | 2025-11-18 00:55:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5ee8bbf-1fac-31c9-b61f-f231f50a4f71 | -3.0569 | -45.392601 | 2025-11-18 00:55:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6324adef-2441-3f9b-9a75-83f36f52634c | -10.1595 | -48.1483 | 2025-11-18 00:55:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71f4982c-e2df-38cd-bbb8-63d5edbf53f4 | -3.9342 | -52.181599 | 2025-11-18 00:55:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1df6000d-ac56-33f9-9b0d-42fdecbd06d5 | -6.4163 | -47.431301 | 2025-11-18 00:55:00 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f1068ef-8556-33b4-97f7-7106c8845d26 | -3.3895 | -46.142502 | 2025-11-18 00:55:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a33f537b-f368-339e-83db-863dda76ad6c | -9.1575 | -50.133598 | 2025-11-18 00:55:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5808512-768a-30e2-a660-43c78da0231a | -10.3618 | -48.919899 | 2025-11-18 00:55:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fecd3b73-89cb-37d2-a9e6-e602399d5296 | -3.2499 | -43.041901 | 2025-11-18 00:55:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c89e24ae-c0e2-3a20-9a2a-949fd73e2c1d | -4.1634 | -44.2314 | 2025-11-18 00:55:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30de72c3-4d59-39d9-a016-345f062d4b83 | -3.325 | -51.505699 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e39dc7f-3dfe-342a-a261-83a20ca80372 | -9.3843 | -48.452202 | 2025-11-18 00:55:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e134f63-fcfe-34de-8917-000f827be04a | -3.1204 | -45.745701 | 2025-11-18 00:55:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30289e9b-c33f-3f7c-b602-988c35e8861c | -3.3266 | -51.512699 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2c21eb6-6aa9-369f-9a51-3312de308581 | -6.3035 | -43.785301 | 2025-11-18 00:55:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f1b3a8d-caaa-34cd-b203-3ca746f075f4 | -3.4615 | -46.056 | 2025-11-18 00:55:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c27e9ebe-e00b-3265-b489-0f4387954f53 | -9.3922 | -48.441898 | 2025-11-18 00:55:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d57413fa-28de-3116-86c8-2a4e01d83985 | -4.6416 | -47.949299 | 2025-11-18 00:55:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4914574-05dd-35a3-80f6-efe4ed093612 | -3.0702 | -45.4053 | 2025-11-18 00:55:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a44fa3d-5dcd-3f59-81b4-82ab77d2269b | -9.4058 | -48.455601 | 2025-11-18 00:55:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1b4a228-ac5a-3b7b-a7a2-de8bfcf5a94d | -4.1765 | -50.192101 | 2025-11-18 00:55:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 170d7f17-dfb8-39bb-bf73-ba7d711ccf6c | -6.4186 | -47.441101 | 2025-11-18 00:55:00 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9fda1e76-b7ed-336e-af57-e47f3dd69c72 | -3.1712 | -46.6092 | 2025-11-18 00:55:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4bb4b731-48c1-3d9a-bb26-78c04eaecde9 | -3.0604 | -45.407501 | 2025-11-18 00:55:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4e6fdab-c672-3f5a-a376-8bffeebe9377 | -2.4723 | -48.232601 | 2025-11-18 00:55:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7242739b-f657-38a0-8676-78877046d08a | -4.187 | -44.244099 | 2025-11-18 00:55:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 780b1b11-3b2b-3b56-99b1-fc99d5395c00 | -3.6637 | -50.2048 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a2efda-4f01-3e18-8bad-ccfff9a41944 | -3.1268 | -45.729301 | 2025-11-18 00:55:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60254229-106d-31bf-82fa-bd71765008b1 | -3.6567 | -51.782001 | 2025-11-18 00:55:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1178745-e345-3abb-b34c-9b2f9946d90a | -2.5183 | -47.813301 | 2025-11-18 00:55:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afbf1719-bce6-3fb8-ac19-faa1808042cd | -3.2507 | -50.692799 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f361ed01-2e38-3614-8962-99a8ec5bf151 | -3.4797 | -55.435902 | 2025-11-18 00:55:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 908bd9ec-ae1a-3e15-9d4a-64dff0bf7483 | -4.2307 | -46.348701 | 2025-11-18 00:55:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92909f69-0e1c-324a-b0ea-89bda6500311 | -2.47 | -48.222698 | 2025-11-18 00:55:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f78687d-a1c3-3825-84e4-e1d408c1ce77 | -3.6672 | -50.220001 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b336ea1-119b-3b63-9ab3-49ffe9efd103 | -4.1967 | -44.241798 | 2025-11-18 00:55:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03a682a8-fe7e-3dba-9eea-61e97573b5b2 | -4.0495 | -47.493301 | 2025-11-18 00:55:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d330aa9-ad8a-3a8a-8a8e-28657db872c4 | -3.6294 | -50.7691 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb246a19-432a-36da-95d7-1f183216f3d8 | -3.1436 | -51.480099 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aea9f62-ae79-35ed-9df4-ccde123c32fa | -4.2687 | -44.242699 | 2025-11-18 00:55:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb533a82-b711-37be-8576-8cd44a084c3a | -8.3015 | -43.9953 | 2025-11-18 00:55:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8e494cf2-7176-39cd-8915-0923c4812fd0 | -3.4712 | -46.053799 | 2025-11-18 00:55:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f4c50c5-18a2-389e-b96e-1791eb0160c1 | -3.2354 | -50.492802 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a341c7a5-d4b5-3aa2-93f4-48b67c1d1a72 | -4.1773 | -44.246399 | 2025-11-18 00:55:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60a209ac-8f06-339d-adab-76180f33ec50 | -3.7545 | -51.803501 | 2025-11-18 00:55:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf5a2a5-a9b6-3813-8607-1e26742aadab | -3.4761 | -55.420101 | 2025-11-18 00:55:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31ea5c6b-4a63-3760-8f9c-b8e7cad5bb6f | -8.4678 | -47.983799 | 2025-11-18 00:55:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19ebf5fe-05b7-336a-9998-4d0bdd75e4d7 | 1.52 | -55.963299 | 2025-11-18 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6dfe826-bf4c-31b3-928d-0c75faa0221f | -3.3402 | -44.390598 | 2025-11-18 00:55:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76085341-41af-33d1-bcb8-0a9852486d1f | -3.1504 | -45.096298 | 2025-11-18 00:55:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6cc35a9f-ff79-36c8-bdd3-44f0db021aae | -5.2207 | -49.580898 | 2025-11-18 00:55:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f770643b-1cb0-33fa-ba33-871277098b82 | -10.5875 | -49.001701 | 2025-11-18 00:55:00 | METOP-C | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f398516-0c26-3dda-8b6c-9a411d807648 | -3.6445 | -50.834599 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 939304d0-fed2-3d3e-851f-a1b8f9a6fdde | -6.4324 | -43.8078 | 2025-11-18 00:55:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd354f3-33f5-3756-951e-4555462734e3 | -4.137 | -52.1217 | 2025-11-18 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddfb2286-134a-3eda-8048-04753e3404ff | -3.0775 | -50.345699 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 681b7834-5585-3164-81f2-9768cb16bb89 | -3.6743 | -50.2505 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4f73b57-d0e8-3537-b2b0-c37b1dbae9c4 | -3.3458 | -44.370899 | 2025-11-18 00:55:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48337096-042c-347d-b907-5850f43e7745 | -11.2084 | -49.406799 | 2025-11-18 00:55:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 606254ac-68c3-3fff-8aea-000c1823e6d4 | -2.8163 | -45.417198 | 2025-11-18 00:55:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 34490969-b6b5-3c2a-9b39-d68f011e2216 | -3.4774 | -52.348499 | 2025-11-18 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a66eb7f4-8c2e-38ed-b3b1-e259efbf6f6c | -9.7176 | -48.903099 | 2025-11-18 00:55:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb1d0aaf-57bc-32c5-92c2-0e3ce030bc4a | -9.0999 | -44.343498 | 2025-11-18 00:55:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1091c5e-a913-3743-b211-1ebb3aa4b914 | -4.18 | -50.207199 | 2025-11-18 00:55:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
