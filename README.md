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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d4fbaeb-d04e-398c-84c0-9ca08814a442 | -5.656 | -45.9692 | 2025-10-10 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 64de3212-65eb-3273-8e35-e71f11cee81b | -11.2006 | -48.0531 | 2025-10-10 00:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| e7c664fa-eade-3836-a7f9-abd7990d2435 | -15.8288 | -43.7555 | 2025-10-10 00:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 92.0 |
| c270c8d4-6ea9-34ab-9345-1a85c4f975a0 | -5.4752 | -43.054 | 2025-10-10 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| bb7037a6-970b-3553-8e13-77e6dfe94459 | -13.3102 | -47.7446 | 2025-10-10 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| b959f7d1-a234-36d2-a2a5-21f0bbb061b0 | -6.5851 | -44.6098 | 2025-10-10 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 126fa487-4170-3a85-bd19-85f2486fd13e | -5.4935 | -43.0995 | 2025-10-10 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 4b54cac7-4d30-371d-8a3f-6fc7066c7536 | -5.475 | -43.0774 | 2025-10-10 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 175.5 |
| c4e913b5-9422-3011-a450-0c2442e568ca | -5.494 | -43.0526 | 2025-10-10 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 23e4c8fc-5e3b-37c2-82d7-067576280a05 | -4.2397 | -45.986 | 2025-10-10 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 0f3f6567-8f41-3f54-9578-d63bcc1baaa3 | -5.4937 | -43.0761 | 2025-10-10 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 280.0 |
| 9eb8e749-4d5d-3ede-8472-dea02240e63e | -3.3366 | -44.4263 | 2025-10-10 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 72a262f1-f663-3cf0-a922-e8d4606b5e45 | -3.7937 | -49.4211 | 2025-10-10 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| f809441d-86c2-3e83-a71a-f05759d7fb58 | -13.387 | -47.7555 | 2025-10-10 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 11c11d79-fee6-3a14-add8-71bfd74926a5 | -8.8435 | -46.0519 | 2025-10-10 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| e70e8040-d87d-3fbd-99d7-69ca973817d3 | -3.7466 | -44.3849 | 2025-10-10 00:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 8c4aacc7-428c-3ef2-95ee-61f701529828 | -7.7755 | -44.0396 | 2025-10-10 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 2aa1a768-0c82-3162-b29f-d35b7785d57d | -7.3966 | -45.9227 | 2025-10-10 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| fa478b75-e660-321c-ac45-aa157ab432f0 | -7.4154 | -45.9211 | 2025-10-10 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 53d00f7d-967a-3577-ba23-79e2d72a53a6 | -8.8432 | -46.0744 | 2025-10-10 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 8607aedb-ac3f-3e45-860b-5c836d6c768e | -15.8282 | -43.7796 | 2025-10-10 00:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 55ab0722-3431-3316-b8da-2404bd677b7d | -6.5849 | -44.6327 | 2025-10-10 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 16722ba5-0496-35f7-9e40-1dd108fdad14 | -13.3295 | -47.7417 | 2025-10-10 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| bb16c14d-3b1e-3e1d-b9d5-80897ffe840a | -7.7752 | -44.0628 | 2025-10-10 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| b7bc717a-ce43-368d-9774-033d068c3f5c | -3.3367 | -44.4034 | 2025-10-10 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| deebda03-240e-3bfc-aabb-d0a8564151a7 | -8.6044 | -41.4105 | 2025-10-10 00:00:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 7f03236d-64e8-363a-a7ef-0eb054a20fa9 | -4.5011 | -45.8606 | 2025-10-10 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| de7fcaf7-800b-3e33-9397-079214cbf17a | -8.5218 | -46.1526 | 2025-10-10 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 8fc29492-4a12-393b-95e7-997fc27307e6 | -6.8108 | -42.8014 | 2025-10-10 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| ac41aa03-d4e0-35e1-abb7-f308fe4c1661 | -5.9345 | -44.0649 | 2025-10-10 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 96942526-0d78-3831-8a8a-135c4ad2a766 | -13.058 | -43.8571 | 2025-10-10 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 89434d42-de3c-328f-84e5-3512502b12cb | -15.9189 | -43.3022 | 2025-10-10 00:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 08ed686d-7a67-3ab1-a2ef-63891cb7ee87 | -8.5029 | -46.1545 | 2025-10-10 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| a0550d2f-dd1b-3c5e-ad33-1ebc7f8e9513 | -3.7936 | -49.4424 | 2025-10-10 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 038e74b0-18c7-3aac-b7f7-49983f41a7f8 | -11.2197 | -48.0508 | 2025-10-10 00:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 8aab699a-9096-3ccb-9589-1cbb9e2df251 | -3.5371 | -48.9195 | 2025-10-10 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| a680b669-6ca5-3de7-acd0-28a8ad1c9113 | -8.5184 | -66.9954 | 2025-10-10 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| bc992166-3f1a-3bfe-8321-0919f56c70a9 | -3.0013 | -48.7453 | 2025-10-10 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b51a1600-76a0-346c-9bd3-73e188cfdc22 | -15.9195 | -43.2779 | 2025-10-10 00:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 193.2 |
| e26cf714-1f1a-3429-a4c9-920bbe0630d7 | -5.6373 | -45.9705 | 2025-10-10 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| b7fe015d-46aa-374f-945a-0022cc900af5 | -13.0584 | -43.8333 | 2025-10-10 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 25de3d06-5a1a-3292-bbc2-6b7e1efe0e09 | -8.5027 | -46.177 | 2025-10-10 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 27efea97-3d0a-3e12-a452-1a5212bc3d8e | -11.6349 | -55.0216 | 2025-10-10 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 11c337be-b7be-3ecf-a200-d353ce2f6cef | -17.9026 | -57.5153 | 2025-10-10 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| dde4cb2c-d3e2-386c-b665-063c911ad1cb | -17.9175 | -45.0194 | 2025-10-10 00:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 208.9 |
| bed35528-bf82-3b29-906f-4adb580b3515 | -3.7466 | -44.3849 | 2025-10-10 00:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 79e21af7-d5b8-355b-b38f-80411f17b8e6 | -8.5218 | -46.1526 | 2025-10-10 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| a3276ba1-4c69-3ac2-9d0f-7f8e597fa4de | -11.6162 | -55.0029 | 2025-10-10 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 337f25e4-20eb-37c9-b3f0-2b22a22a302b | -5.4752 | -43.054 | 2025-10-10 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| df2bd478-2e31-33d9-8c1c-bb5e881cf195 | -3.7937 | -49.4211 | 2025-10-10 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| b677e143-de0f-3729-80f5-08835b257f41 | -8.8432 | -46.0744 | 2025-10-10 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 8aa1baa7-b8dd-3d3d-bd88-960d4b596a4f | -13.058 | -43.8571 | 2025-10-10 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e0b7fdc8-5fdf-3b55-bf29-8b58ad4a671e | -8.6044 | -41.4105 | 2025-10-10 00:10:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 79da2118-2da6-3d64-aad9-5e230d0eac33 | -3.7936 | -49.4424 | 2025-10-10 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1cd9a90e-86c0-3cd3-96c6-807a015daa8b | -13.387 | -47.7555 | 2025-10-10 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 0866dbbe-3c12-3d0e-98b6-be2ff56f228e | -13.0584 | -43.8333 | 2025-10-10 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 2e5a820e-877b-3eba-9faf-5bd1baf13580 | -17.9376 | -45.0148 | 2025-10-10 00:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 445.9 |
| 767b94fa-4046-3252-9074-83391cd0a1f8 | -13.4277 | -47.6375 | 2025-10-10 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 5b37feb0-2cf5-3f3b-bce5-15aa2dd02b45 | -13.0778 | -43.83 | 2025-10-10 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1875d7c2-025e-3ee1-826e-b5c185ffb858 | -11.616 | -55.0233 | 2025-10-10 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 07a4b3c0-00fd-3250-9ad2-ea52f2dc43ab | -11.6351 | -55.0012 | 2025-10-10 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 520799e8-e302-3140-bb5f-c73dd719ea26 | -3.3367 | -44.4034 | 2025-10-10 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 288fdedf-61db-30f6-950e-030e3d1d11d7 | -7.4154 | -45.9211 | 2025-10-10 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 3988a441-2d67-3ce3-be30-907678022e5a | -3.5371 | -48.9195 | 2025-10-10 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2959abdb-22a4-3ec2-93fb-90f4535a24ee | -8.8624 | -46.0499 | 2025-10-10 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9aa422f8-29b3-333d-9747-17ee3e80e02a | -8.5027 | -46.177 | 2025-10-10 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 06641c9a-e090-3aee-9333-63297e934708 | -5.475 | -43.0774 | 2025-10-10 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 01312e79-2b89-3991-b1f6-c1c2b67fc5fa | -13.3102 | -47.7446 | 2025-10-10 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e884e4e8-0a34-39eb-aa7f-26533dc75fea | -15.9189 | -43.3022 | 2025-10-10 00:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 252.0 |
| 89973e81-da5f-38f8-8b81-bb967b9abbfb | -13.3874 | -47.7331 | 2025-10-10 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| dc914e88-5441-33c0-951e-f482a959b2f8 | -17.9382 | -44.9909 | 2025-10-10 00:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 89afde98-412a-3759-8fe6-1ea482e6520d | -17.9577 | -45.0103 | 2025-10-10 00:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 61836a08-05cc-34a7-aa48-2d89538d47da | -15.9195 | -43.2779 | 2025-10-10 00:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 229.2 |
| 2ac1cc6c-d46a-31a5-9aaa-ae2c9d6babf7 | -17.9168 | -45.0434 | 2025-10-10 00:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 91.0 |
| c5d50eb5-1c89-3dd6-b1d0-00124fa2fa1e | -5.4937 | -43.0761 | 2025-10-10 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 8a6e5107-374b-373f-9a88-b88ba4771a83 | -3.3366 | -44.4263 | 2025-10-10 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 539b4ce2-8592-3507-b679-2d1843425bf5 | -5.6373 | -45.9705 | 2025-10-10 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 8a101ed6-cf30-3e38-9e28-875b8a77fdb8 | -8.5029 | -46.1545 | 2025-10-10 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 24121861-127b-3b10-98d3-cc41ac384a26 | -8.8435 | -46.0519 | 2025-10-10 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 2b7c56ef-f0ef-3ba5-b5d8-e114a782dda3 | -8.5184 | -66.9954 | 2025-10-10 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 909ccab3-a4eb-3878-9233-c3bb0b9a018d | -7.3966 | -45.9227 | 2025-10-10 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 2291334e-168c-3922-9958-69fe561d9c93 | -6.8108 | -42.8014 | 2025-10-10 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 25c132ef-ee9e-3b3c-853a-07a24e5eb58b | -5.494 | -43.0526 | 2025-10-10 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 86eacbeb-66fd-38b0-9ca2-f0a0ff6d5137 | -17.9369 | -45.0388 | 2025-10-10 00:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 185.8 |
| de74e123-b790-31b5-8b3f-eec2151837dd | -6.5851 | -44.6098 | 2025-10-10 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 3e4c6c79-f1bf-3896-96d6-bb945aa90bc2 | -5.656 | -45.9692 | 2025-10-10 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 8019384e-7267-3398-9f92-8ec91bee2222 | -6.5849 | -44.6327 | 2025-10-10 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 971572c6-20dc-3241-9c94-8c1b1ab41d67 | -3.7937 | -49.4211 | 2025-10-10 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| ed0063be-d6a7-3539-ba7b-3f1ce1924531 | -17.9029 | -57.4947 | 2025-10-10 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 43866723-0548-38cb-917e-6007a93ef4b7 | -4.6505 | -43.1805 | 2025-10-10 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| b0592559-4db8-3185-91d5-a433a4c478c7 | -13.0584 | -43.8333 | 2025-10-10 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 05768641-1497-3376-bb9d-b083fd6fa692 | -15.9189 | -43.3022 | 2025-10-10 00:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 228.1 |
| 827d3a9f-7cb0-3d74-a9da-178dc36172e8 | -3.3366 | -44.4263 | 2025-10-10 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| caa68706-6246-30be-956e-bcf136c05ef7 | -7.7755 | -44.0396 | 2025-10-10 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2ec23036-d912-3d48-ab1a-53d1a1af26ce | -17.9026 | -57.5153 | 2025-10-10 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 39e23d44-c77d-33df-8e0f-6e7e3124de37 | -6.5851 | -44.6098 | 2025-10-10 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 7b103697-1382-3e7d-9088-24f1b6602a67 | -15.9195 | -43.2779 | 2025-10-10 00:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 269.6 |
| b2ee38e6-62e2-394a-8610-8b1b84cb3b63 | -5.5125 | -43.0747 | 2025-10-10 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 622716d2-a91d-38bb-a175-2bf048a9b6a7 | -7.3966 | -45.9227 | 2025-10-10 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 8044a2f7-39d5-352a-93f0-6d612b4bd3d7 | -5.475 | -43.0774 | 2025-10-10 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |


[Clique aqui para ver as próximas entradas](README2.md)
