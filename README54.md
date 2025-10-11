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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdedc761-7968-345c-85e4-ff1fdf67cd5a | -8.5024 | -46.1995 | 2025-10-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| c55ba468-3cc2-3990-ba17-02d23018d1b8 | -10.0747 | -45.9121 | 2025-10-11 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 378.1 |
| 03bf8f49-12eb-344a-9907-1dd0210a9846 | -7.7675 | -44.7084 | 2025-10-11 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| ada7c1f0-eeb7-31fb-b892-44daaca5f56b | -18.0601 | -57.5371 | 2025-10-11 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 90248f6c-a23b-39dc-b3fb-65d6fdc70b7f | -9.6974 | -45.7986 | 2025-10-11 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 941faf9a-ebae-3e3a-b703-41b07ddea67f | -10.1898 | -44.5934 | 2025-10-11 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| a4be6c2b-bfaa-3487-bf33-d3f0ac24fb0d | -8.4835 | -46.2014 | 2025-10-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 9adc2e0d-e5d7-3f27-8e52-7faf8f1fc052 | -10.1524 | -44.552 | 2025-10-11 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| dad44411-a943-3d9e-a216-6a90977e908f | -10.9041 | -47.5588 | 2025-10-11 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| b8ff8b23-4a66-3cf7-87e6-50e3b78f6ac1 | -9.6974 | -45.7986 | 2025-10-11 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| b8580ca4-92b5-3aa2-8e13-3b211ff4050f | -18.0601 | -57.5371 | 2025-10-11 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 3ae502bc-6bca-3622-8aef-9609d14dd692 | -10.5274 | -47.3601 | 2025-10-11 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| e64df9aa-2c35-392e-9e09-ebd254d0c19c | -10.5657 | -47.3333 | 2025-10-11 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| aaaa3e8c-c813-32cd-be90-18e2f3776a27 | -10.1898 | -44.5934 | 2025-10-11 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| a418c31c-1fff-353c-bcec-20823f051d7d | -7.5243 | -44.5944 | 2025-10-11 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 7126408a-a5a5-354b-a02c-d28499509ea9 | -10.0747 | -45.9121 | 2025-10-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| d37a4260-fc09-33e4-9f8a-7721d47854ee | -18.0195 | -57.6038 | 2025-10-11 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.7 |
| e1183959-8843-3540-b194-b9ff3a28b114 | -8.5055 | -45.9519 | 2025-10-11 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 86cc6f3e-d8dc-3424-b660-e9336773b808 | -9.3944 | -45.8109 | 2025-10-11 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| a224898f-b6aa-374c-ab9e-5e365d88fe54 | -10.5277 | -47.3379 | 2025-10-11 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| f715eb13-0d21-380f-a75d-ef0c980fc407 | -8.9833 | -45.4714 | 2025-10-11 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 228.6 |
| 39ab91f1-b870-3f2d-a85f-f7e38ca7a602 | -10.5467 | -47.3356 | 2025-10-11 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d19a5fc0-5394-3c38-8823-f457e28a3b1f | -10.5844 | -47.3533 | 2025-10-11 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 318.7 |
| 959f849b-c5b4-39e1-b124-aaeb2551019d | -12.7299 | -45.8422 | 2025-10-11 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| af5a982b-d21c-325b-9971-947992a1fd29 | -9.1024 | -45.0477 | 2025-10-11 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| cc7539c1-f91c-3bac-8d80-323d5b138ab2 | -7.5277 | -44.2952 | 2025-10-11 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| edf147d7-91eb-3a1d-9963-3cddd3902032 | -9.0022 | -45.4693 | 2025-10-11 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 85ce6586-5b35-3d86-9ec4-5e62ce90def1 | -10.0545 | -67.5484 | 2025-10-11 14:30:00 | GOES-19 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 0e6fd6ac-ee4b-39ca-8915-dcffd6f15990 | -10.5087 | -47.3401 | 2025-10-11 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 87d90083-fb82-310f-bf6e-65b90f9a7bd4 | -12.9921 | -45.2252 | 2025-10-11 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| a59a737c-eb1a-3e7e-bc76-c0c7bb38960c | -12.5541 | -48.1419 | 2025-10-11 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 04c0223f-b9f5-3738-8b49-31c014a9e047 | -18.3806 | -56.1696 | 2025-10-11 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 8510c765-00c6-3795-8bb7-674a81b8343b | -15.1833 | -56.7436 | 2025-10-11 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| e193ac10-a6f2-33e0-96b1-f71da4bb4f08 | -10.0937 | -45.9098 | 2025-10-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| c3e5af10-3c59-3793-85d5-e4f3b6d37a36 | -9.414 | -45.7634 | 2025-10-11 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 6ca5aff9-81d7-3aff-83fe-c0ac986b19de | -9.5562 | -66.7442 | 2025-10-11 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a4061d90-6669-39ae-8da9-e93be77f60bb | -12.0118 | -45.2161 | 2025-10-11 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f417385e-5f76-3757-8414-e1cc5d3a8600 | -18.0803 | -57.5141 | 2025-10-11 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.3 |
| 503caa3f-6868-3156-bdbb-2aae1dc69778 | -7.5466 | -44.2933 | 2025-10-11 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| ad23dcf7-b303-3e2e-b0ea-a5d7e6fc897d | -9.4674 | -46.006 | 2025-10-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d67cbe1b-45b5-3dae-9a0b-2dac86e40ffc | -9.4374 | -45.4428 | 2025-10-11 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0bfca16f-3952-3d45-aaf0-fe12a6f4ed44 | -9.18 | -68.1824 | 2025-10-11 14:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c34b5069-b733-3cca-a0d1-2bd589b5054d | -10.5661 | -47.3111 | 2025-10-11 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 34d84437-0557-3855-b20a-19d8dad26ec5 | -18.0598 | -57.5577 | 2025-10-11 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 4d79e5e7-160c-3e80-8ab9-09575b31cc27 | -8.2266 | -44.1548 | 2025-10-11 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 2c953294-ad8c-3b12-ac88-8b19b3568255 | -11.6268 | -48.7911 | 2025-10-11 14:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 1222b1af-2df3-3707-90c5-df9b5308f8c5 | -8.5016 | -46.2669 | 2025-10-11 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 66a6585d-e1ad-346d-bdcb-0b2bda359496 | -8.226 | -44.2012 | 2025-10-11 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f189b04b-3acc-3c1e-b69c-e5ba776b7614 | -9.2747 | -47.6983 | 2025-10-11 14:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 13540f70-4b9b-32ea-b901-e560eddd49a8 | -8.208 | -44.1337 | 2025-10-11 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| f08c53e6-4690-3321-9f1a-8da9d20d1088 | -9.0838 | -45.0269 | 2025-10-11 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f67499d7-db45-3eb7-bc39-4b811697702a | -10.1524 | -44.552 | 2025-10-11 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 964f0819-57f7-37b8-a3fb-9d65ee8477c6 | -10.1714 | -44.5496 | 2025-10-11 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| ab36de8f-5a22-3717-9e89-d30d89faee5d | -15.1836 | -56.7232 | 2025-10-11 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f591b528-0972-3a0a-b67d-bd5fe6808853 | -18.0803 | -57.5141 | 2025-10-11 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 48e7d3e2-0188-3d55-b215-3f60655fee72 | -9.3944 | -45.8109 | 2025-10-11 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| e02d45bb-e36e-3346-82c5-12f1f6d662fa | -10.8729 | -47.1177 | 2025-10-11 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 90e12e65-8387-3da7-92b6-39fe77f71b3e | -10.1898 | -44.5934 | 2025-10-11 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e7156a9d-353d-3a3a-be3f-cecdacb9f7a2 | -18.0601 | -57.5371 | 2025-10-11 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 36725cb1-59b7-3762-9a69-3b72c23aa18d | -7.5277 | -44.2952 | 2025-10-11 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 12bf52f1-077b-3c75-8fb3-8d7fab6dc26d | -7.4669 | -43.0674 | 2025-10-11 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 91d4a7c0-73d4-33e9-b06b-fb12d1307a24 | -9.3947 | -45.7882 | 2025-10-11 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 34f7a422-1ff7-3df1-b374-a763d83440b1 | -9.4674 | -46.006 | 2025-10-11 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 7a3ae9fc-395e-3425-8459-20c3d2d2c12a | -7.7924 | -44.1998 | 2025-10-11 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 37194ec8-dbe0-3c90-af7c-7daa85643860 | -15.1833 | -56.7436 | 2025-10-11 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 3679ab8a-8ceb-3030-99d9-29f55cb66821 | -18.0598 | -57.5577 | 2025-10-11 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.4 |
| d8631adc-7a03-3477-8f4a-d33669e46c21 | -8.226 | -44.2012 | 2025-10-11 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f779e577-0850-35ad-9082-72c49046efef | -8.1324 | -47.2589 | 2025-10-11 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| af7fb2bc-7f47-3346-8c3c-2c35f6cef91d | -7.8687 | -44.1227 | 2025-10-11 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 1e7c9c39-f26c-36d0-a69c-2c0442822aaa | -17.285 | -58.018 | 2025-10-11 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.4 |
| 63a9ee55-2534-3701-83e1-a97ee333ed72 | -7.5431 | -44.5926 | 2025-10-11 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| c9f247d7-5213-377b-b2da-16c837168eaf | -11.6268 | -48.7911 | 2025-10-11 14:40:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c1f3d161-ec02-3406-a029-fd9be59fb59d | -17.2837 | -58.0997 | 2025-10-11 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| cbad0bec-c64e-3298-abd4-0aa9c73079f6 | -7.3423 | -44.059 | 2025-10-11 14:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 679f8039-16ac-3e46-8469-4360b97694bd | -7.5243 | -44.5944 | 2025-10-11 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 1a3803d8-08c9-3cac-9454-832859ba771b | -9.5562 | -66.7442 | 2025-10-11 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |


