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
| 851f4b61-5b2f-300a-828f-97f637de048a | -9.4749 | -64.3713 | 2026-10-08 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| eb5d0ee4-2466-3037-8b19-c2a8e8ccf525 | -3.6049 | -54.5736 | 2026-10-08 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| ecffbc2d-eae8-3dd3-9d32-86193883f4d9 | -17.1213 | -41.3421 | 2026-10-08 01:20:00 | GOES-19 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.9 |
| 1e8843f6-3bc3-3924-ad33-8716a97958f6 | -7.1964 | -45.354 | 2026-10-08 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 96747dd8-590a-3eb8-8e93-328aefb8222d | -6.1431 | -47.9214 | 2026-10-08 01:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 7f23c06d-1994-31d6-8b50-ee4bc1bbbb27 | -2.4987 | -56.1659 | 2026-10-08 01:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 1ba04b67-b0e1-307d-98bf-520311eb989f | -3.1633 | -54.7452 | 2026-10-08 01:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| b06e06d9-b2df-35a1-b069-6170ccdf8ab6 | -2.798 | -54.0933 | 2026-10-08 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 3a916418-6138-3fec-95a6-795ee0285ac3 | -3.1972 | -50.5592 | 2026-10-08 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 125753d5-1435-352b-8417-4d8dc1188bf5 | -9.4936 | -64.3518 | 2026-10-08 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.6 |
| a65ac96e-1ccb-3a6a-8e02-c289802aa5aa | -4.4507 | -47.9112 | 2026-10-08 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b054011f-c115-35b6-bb65-e9b7e6f06785 | -3.0913 | -54.287 | 2026-10-08 01:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 2ada2eea-7722-3def-8582-96009311f81b | -5.7117 | -53.4862 | 2026-10-08 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 203.1 |
| 6852171c-4ae3-3e15-b40b-fd82f22339eb | -3.073 | -54.2874 | 2026-10-08 01:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b6abbaa2-cb87-32ec-8689-87343de0c6da | -8.7225 | -45.204 | 2026-10-08 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 33f5de89-4cdd-30c1-b4db-f73d532a40e2 | 1.7488 | -55.5861 | 2026-10-08 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| bced107b-87f9-3337-a47e-b29c24f8817a | -8.3882 | -46.3006 | 2026-10-08 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4da8d3b4-6da5-3a46-a96c-7090ab77bacf | -5.7376 | -45.1533 | 2026-10-08 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 1ad65370-8ee1-3271-8983-8ddd4d5e3a2e | -4.3471 | -43.8021 | 2026-10-08 01:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| a95cd5c1-ebeb-3910-a61d-af7d3e82a4af | -3.1285 | -54.1657 | 2026-10-08 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 5e7bba1b-4b3f-3a6f-bb3c-b43415a74267 | -3.5865 | -54.5742 | 2026-10-08 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| dad8e150-569d-3fd3-a6ba-fbde60829b55 | -8.7231 | -45.1583 | 2026-10-08 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 231ba708-05a6-3a35-99a2-9ac80c9c2c26 | -2.7613 | -54.0941 | 2026-10-08 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d5f2c441-c843-35bf-827d-512cf6d569a4 | -3.1697 | -58.6437 | 2026-10-08 01:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 61a0493a-a53d-3df0-9b00-2e353e6e1bd1 | -2.7981 | -54.0732 | 2026-10-08 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 3acee0c7-0eb4-32c1-baad-9b6a72cc9ab4 | -8.7228 | -45.1812 | 2026-10-08 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 178.1 |
| fff47d01-c91f-3d09-840c-bdcfee08082a | -5.6934 | -53.4667 | 2026-10-08 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 7ea63a61-f35f-324b-9453-63688c2eb73b | -6.1689 | -39.4391 | 2026-10-08 01:20:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 92f9b503-d55a-3326-ba40-13f7113e748a | -2.4805 | -56.1072 | 2026-10-08 01:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5f5d35be-a0b5-36eb-bd2d-841021f284ea | -9.4935 | -64.3706 | 2026-10-08 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b5d9120e-9dfd-301b-b292-e286a5aadb7c | -2.4805 | -56.1269 | 2026-10-08 01:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 3cc8ad5f-ae68-3072-961b-7150677a7566 | -5.7189 | -45.1547 | 2026-10-08 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 317449a1-bf95-38f4-a947-c893909b27b3 | -3.1097 | -54.2865 | 2026-10-08 01:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e49db569-1b87-3d33-98fe-6bdd7b0a5c8a | -6.8952 | -43.6833 | 2026-10-08 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 7abb52eb-f3e7-33dd-b3e6-d5b1130cf95b | -2.4032 | -57.8848 | 2026-10-08 01:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e9837d9b-1c7c-358f-96db-ec722125a464 | -5.7116 | -53.5065 | 2026-10-08 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| f70d5340-e89d-3c76-b4dc-e8c2a50a10e3 | -2.4031 | -57.9041 | 2026-10-08 01:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 910b7267-e450-3ede-9305-74920f5c34a9 | -2.572 | -56.1842 | 2026-10-08 01:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 95eddf7d-a889-354d-bdc6-701708aa8a6a | -4.3473 | -43.779 | 2026-10-08 01:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| a2194cc0-66d8-36e7-9a62-88cdf1a6e314 | -3.478 | -59.597 | 2026-10-08 01:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| e52563bc-2add-3b74-8af5-9ed2aedafc40 | -2.7612 | -54.1142 | 2026-10-08 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 91016cd7-6a08-340a-bb51-9cf49d4fb415 | -6.2342 | -52.8685 | 2026-10-08 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| dd05ac48-1816-3656-86e1-25cc763aa6f2 | -3.478 | -59.5779 | 2026-10-08 01:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 0c312842-9046-3729-a3fd-1ea7697261f8 | -4.3658 | -43.8011 | 2026-10-08 01:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 0b113b60-eefe-31ba-b8e5-e3fda539d02e | -4.0628 | -59.8328 | 2026-10-08 01:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 21cf7f0c-123d-3c96-ac84-ba5c8f996c35 | -2.9448 | -54.1501 | 2026-10-08 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 59d8de06-d1a9-3d48-bedf-fe2526b22e02 | -3.5515 | -59.4807 | 2026-10-08 01:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 15c3dc09-3a15-378f-985c-d4efdbc18af6 | -6.2527 | -52.8675 | 2026-10-08 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 88f95c9c-bc02-307a-ae01-d5bdb61c9c2d | -2.499 | -56.0675 | 2026-10-08 01:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9038b3b8-f98a-358d-ba6d-9cbafec55d6a | -3.1114 | -53.7839 | 2026-10-08 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 84fa2743-6c13-3407-a3a6-a15a0aaf56a6 | -16.8642 | -40.5709 | 2026-10-08 01:20:00 | GOES-19 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.4 |
| dbd4ce75-8327-3bc3-8451-8fe2622f7818 | -8.742 | -45.1563 | 2026-10-08 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 5c6de1cb-8903-33fb-b8c0-76c95b48bf9a | -3.1697 | -58.6244 | 2026-10-08 01:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| dea90e65-f923-30cb-b204-9b5f7ec58643 | -2.7797 | -54.0736 | 2026-10-08 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 89e84a4b-4013-3b3d-8229-e91cca481812 | -4.2954 | -49.0807 | 2026-10-08 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| ad856340-3b70-315f-982e-c63a630eb985 | -2.7796 | -54.0937 | 2026-10-08 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| be96cd78-514d-32fc-a923-1bc6dca93c53 | -9.0591 | -65.9396 | 2026-10-08 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 8cd30570-0d88-3d0c-abbe-c4d87872051a | -3.1298 | -53.7834 | 2026-10-08 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d9f57948-817a-3a47-9fc1-3670f125894a | -10.434 | -47.2601 | 2026-10-08 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 86e61e35-89d2-331d-a397-95875d9dd38a | -8.7417 | -45.1791 | 2026-10-08 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| f7afa80b-a1f6-3074-b7fc-c58ec1fbdf4f | -6.3163 | -43.3614 | 2026-10-08 01:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| bb8c5b62-3ce0-3724-92f4-7b1490f5da93 | -9.475 | -64.3525 | 2026-10-08 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 66f6e726-6c8d-3035-9208-299b5f8c537d | -3.1879 | -58.6433 | 2026-10-08 01:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| c287ed91-deb7-304d-a62a-42d562cac859 | -4.2953 | -49.1021 | 2026-10-08 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| bb770fab-95a3-3dc8-996d-ed69b624cd3a | -16.8441 | -40.5761 | 2026-10-08 01:20:00 | GOES-19 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| e96809b3-52cb-3c25-9de5-6ec7d4284581 | -3.0374 | -53.9268 | 2026-10-08 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| df15c1b6-93c4-355c-87b0-a485ed920d01 | -2.5903 | -56.1642 | 2026-10-08 01:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 67f5412e-f407-34e3-a2a1-567e671cb19c | -3.0373 | -53.9469 | 2026-10-08 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| dfe154db-3a96-3e92-8df8-6a38a6d96839 | -2.4988 | -56.1266 | 2026-10-08 01:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b481d397-c7b2-3400-92d2-62ea3fd850b6 | -8.537 | -66.9764 | 2026-10-08 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 48737c53-13dc-305c-8c94-a101f933b57d | -3.0913 | -54.307 | 2026-10-08 01:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 9f473ff2-db1b-3322-8d29-30f4ebfe8112 | -2.572 | -56.1646 | 2026-10-08 01:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 8582b89d-1ef4-384e-958f-93f8d6840859 | -6.3351 | -43.3598 | 2026-10-08 01:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 083b75b4-413f-333d-9ab3-697be1f715ff | -3.11 | -54.1862 | 2026-10-08 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 99b65ead-2130-35b2-810b-0bb6f8fe98a7 | -6.3165 | -43.3381 | 2026-10-08 01:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 78779b3b-7cd1-301b-a846-935535d3d223 | -10.4337 | -47.2824 | 2026-10-08 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| bb1d98d0-4f16-35de-879e-72a0d6fd37f3 | -3.0729 | -54.3075 | 2026-10-08 01:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 45667cbd-a6ff-3898-9b7d-9fa695b24cac | -12.232 | -44.7194 | 2026-10-08 01:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 994a9ba9-8e2e-31ef-862f-e5fcc022f187 | -6.8764 | -43.685 | 2026-10-08 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c6e238d7-6a65-39c7-8d3c-9c3fd4d774fc | -5.6932 | -53.487 | 2026-10-08 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 305.2 |
| 52ebb5b8-01ff-31e1-9fac-3a232643936b | -3.2499 | -46.9589 | 2026-10-08 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 37135767-2e98-320f-b720-ed1b7cd2837d | -3.1115 | -53.7637 | 2026-10-08 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d268e68a-6d6f-3210-9def-efc7c5ce11ed | -6.6317 | -43.73 | 2026-10-08 01:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 0e7b34ed-b819-39db-a1b6-f17e88f541fe | -5.6931 | -53.5073 | 2026-10-08 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 61549440-fb74-3e0a-a26c-282096fa2fbf | -3.1101 | -54.1661 | 2026-10-08 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| c6ac84dc-7023-3671-b1e9-95b671f25f89 | -8.0895 | -55.311 | 2026-10-08 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 7ef8e77f-c99b-3283-9b87-113008713e53 | -6.15 | -39.4409 | 2026-10-08 01:20:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 58893d9b-2b91-356b-b666-9c6be6d0577f | -9.0592 | -65.9209 | 2026-10-08 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 74618658-22aa-33fe-ab47-4b31f63f93c5 | -3.328 | -50.1775 | 2026-10-08 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 35aa0b29-f343-3dc5-9f6d-fed8bf8c4578 | -3.8383 | -55.9774 | 2026-10-08 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| f9e72f41-6342-3188-a4c4-c3b3732535d2 | -2.9447 | -54.1702 | 2026-10-08 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 25fec273-30bd-38a9-95ed-ade5d5d982ab | -2.517 | -56.1656 | 2026-10-08 01:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| bb64c974-db40-3f4a-b20f-b95ab9a12e6a | -2.4988 | -56.1462 | 2026-10-08 01:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c84addf4-f9dc-34af-ab0c-603bedad39c0 | -6.2343 | -52.848 | 2026-10-08 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| a28c915b-cde8-31d6-935d-c4177c60b642 | -3.2157 | -50.5586 | 2026-10-08 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 38d5b492-6dd4-3e71-9abe-3aa6b2edae32 | -2.798 | -54.0933 | 2026-10-08 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| ca696527-f645-373b-b552-28881e4b1903 | -6.1431 | -47.9214 | 2026-10-08 01:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| d43af629-dbac-3dca-b0fa-fbf8638c922b | -3.1115 | -53.7637 | 2026-10-08 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 1fec3446-d95b-3ac7-938b-3fd847ef02db | -2.7796 | -54.0937 | 2026-10-08 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 4f290177-dd42-35ea-b4fc-7b64ac30da82 | -5.7376 | -45.1533 | 2026-10-08 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |


[Clique aqui para ver as próximas entradas](README46.md)
