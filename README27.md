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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb4d89d8-2367-3b7a-9cf5-189ef9ede26e | -23.19984 | -46.8641 | 2026-08-29 04:00:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1c13a2c1-5ac7-3a78-bd46-ff82a8cb45e8 | -20.98352 | -46.80145 | 2026-08-29 04:00:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69290381-21a3-30f2-8245-d304cb375fcf | -23.32265 | -46.77119 | 2026-08-29 04:00:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6cf922fa-25c3-314f-b1ff-96a338de3590 | -21.52949 | -48.62378 | 2026-08-29 04:00:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b50ac1bb-1b64-3f42-8ed0-0d2ae78cc7d2 | -23.15853 | -49.23648 | 2026-08-29 04:00:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cfa4ac8-cbfc-3721-93ce-6bca64fd8738 | -27.56523 | -48.66267 | 2026-08-29 04:02:00 | NOAA-21 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 901c69ce-1e82-38a1-a3ad-d363e5baff47 | -28.17347 | -55.26898 | 2026-08-29 04:02:00 | NOAA-21 | SÃO NICOLAU | RIO GRANDE DO SUL | Brasil | 4319208 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 15eaec1c-67e9-35fa-9770-4eaca30a5d5f | -28.17244 | -55.27321 | 2026-08-29 04:02:00 | NOAA-21 | SÃO NICOLAU | RIO GRANDE DO SUL | Brasil | 4319208 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 7138dd91-a63b-3adb-8484-7e61cb83651d | -25.49177 | -50.48457 | 2026-08-29 04:02:00 | NOAA-21 | FERNANDES PINHEIRO | PARANÁ | Brasil | 4107736 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8d587b9d-e010-34d7-9777-5e893694a086 | -5.8895 | -57.7513 | 2026-08-29 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 47ec8f7b-3621-3fa2-8136-3644d9cded15 | -6.7699 | -55.6644 | 2026-08-29 04:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| d152c597-518a-3652-8151-a941d2a3d5bc | -6.7884 | -55.6635 | 2026-08-29 04:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 42059cac-136f-3f09-bc02-ecc2baf4a83c | -10.4794 | -64.5012 | 2026-08-29 04:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7d8391a7-2e2c-36ee-ba53-73aef9cfeb03 | -7.4952 | -55.3062 | 2026-08-29 04:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 34a54569-6b56-3915-bf5d-2ad36a525014 | -7.5137 | -55.3051 | 2026-08-29 04:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 82b5903e-a5d6-3e89-a285-05205062501a | -5.8894 | -57.7708 | 2026-08-29 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 614df1da-93e4-3f44-b8c7-5c0d9f96fc7e | -5.9819 | -57.6892 | 2026-08-29 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 877df951-3e99-38ae-943c-7adf6fa27b9b | -10.4795 | -64.4824 | 2026-08-29 04:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 6c51f403-c43f-3dc5-a7c3-83c49680e6da | -7.5139 | -55.2851 | 2026-08-29 04:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 568c0356-7a8e-3fbf-b624-4724d00269d6 | -7.4952 | -55.3062 | 2026-08-29 04:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 03c40c1c-d5c6-3855-b1ed-91f3d3062264 | -11.0443 | -57.2222 | 2026-08-29 04:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 296a269c-701c-315d-9ad7-f08d5df3ae44 | -7.5137 | -55.3051 | 2026-08-29 04:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 81f5b03a-84c6-33c9-b2c1-744a60b7c07c | -10.4795 | -64.4824 | 2026-08-29 04:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e5c7fdda-f088-39cc-aec1-b70861fffc9e | -6.7884 | -55.6635 | 2026-08-29 04:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| c22f22cc-ef16-34b2-881a-4d367d98540a | -6.77 | -55.6445 | 2026-08-29 04:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 289addd1-923c-37a0-991b-5eb603ee7efc | -10.4794 | -64.5012 | 2026-08-29 04:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 964218a0-e08e-3ffd-b004-f636beafd580 | -6.6317 | -43.73 | 2026-08-29 04:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 3f933daa-d0a2-38d1-bf59-c342cc7de7c6 | -5.8895 | -57.7513 | 2026-08-29 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 9d5f5e71-a2dd-3f09-ad11-3d6451839eb5 | -6.7699 | -55.6644 | 2026-08-29 04:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 92fc5e50-a4e7-393d-bf9d-dc16188db11c | -5.8894 | -57.7708 | 2026-08-29 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3ba1a6f8-52e9-3e23-8c1f-4fae3a0ac801 | -1.86699 | -47.98092 | 2026-08-29 04:29:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea132b43-326e-3620-8b1b-57cf48cdc91a | -2.99102 | -48.95459 | 2026-08-29 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87ec9f3a-7305-39c1-accf-b212d421d4bf | -2.59656 | -49.3369 | 2026-08-29 04:29:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff2c0fb7-e46b-3da2-a669-f006389a784d | -2.72394 | -47.04797 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 440f87e4-40f7-3368-b2e6-1752f25f7a3c | -2.71807 | -47.03852 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4cae624b-85a1-33dd-abe2-77e1b83aa76f | -3.59967 | -43.00739 | 2026-08-29 04:29:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11f815ee-5303-3a45-ac9d-875f5304c60b | -2.71672 | -47.04684 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dfa9d4f-4941-39d0-8cbc-e1ff81f246f0 | -2.72033 | -47.0474 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eada91f3-ea5d-374e-b8a6-fde120c7b190 | -3.59631 | -43.00686 | 2026-08-29 04:29:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c422531-763d-3159-81b7-eef18e5a6d6f | -3.35356 | -44.2258 | 2026-08-29 04:29:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e291255-b7f0-33de-bafb-8292ed990bf0 | -1.59185 | -47.35683 | 2026-08-29 04:29:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d039265-6493-3843-ae13-c2fa61623879 | 2.519 | -50.8548 | 2026-08-29 04:29:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5210e487-75d5-387c-a872-695c42be55ff | -2.71739 | -47.04268 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4b25c71-ace7-3946-9685-6ba3767168e2 | -2.72101 | -47.04325 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ceb4af94-5830-3810-a758-a6f2b737c75e | -2.89629 | -48.27692 | 2026-08-29 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 370605cf-6fbf-3786-b4f6-2369ef7f3a8c | 2.23971 | -50.7638 | 2026-08-29 04:29:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bb9dd321-e5c2-3a8e-a73a-205b6a95a4eb | -2.50245 | -48.13554 | 2026-08-29 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0778e6b3-dd9b-3ad0-a2cb-a1e1825dcebf | -3.92261 | -43.12963 | 2026-08-29 04:29:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e76ba71e-6f6e-300d-8dc2-5a495e8fcd11 | -2.98756 | -48.95043 | 2026-08-29 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9038f1b7-9749-3b59-be47-e0157877149d | -2.99046 | -48.95808 | 2026-08-29 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 857eb8e8-936f-30e1-8b0e-11bdc7d5084f | -2.72168 | -47.03909 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7209564-17bd-37ff-bdf7-776480feafd6 | -3.69667 | -39.59127 | 2026-08-29 04:29:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 95ef97d5-61d5-3002-920c-2da7e80dd56c | -3.69823 | -39.58103 | 2026-08-29 04:29:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc253c8b-b08b-3868-8f8f-62bbc8fa7e39 | 2.51813 | -50.84913 | 2026-08-29 04:29:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 37275abf-945a-3304-9be6-1c2deb901234 | -2.02243 | -52.10805 | 2026-08-29 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22c88e88-6106-3905-a139-5d69ff710253 | -3.74036 | -44.3896 | 2026-08-29 04:29:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 134b692a-d9c5-3d69-96a6-40ca72cff795 | -3.97293 | -41.51968 | 2026-08-29 04:29:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e70328fe-f432-3240-973a-137e7e53257f | -2.72462 | -47.04383 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12331f99-a826-379f-8fcd-937baa78bc96 | -2.72447 | -48.80099 | 2026-08-29 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69cbe147-573d-3d40-b21d-d3534f9a6e9f | -2.99448 | -48.95876 | 2026-08-29 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80dc48f3-9368-3ed0-b17f-ee2bc7317ae2 | -2.987 | -48.95392 | 2026-08-29 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60e737b7-b862-380b-9253-c8a49bbd32ce | -1.20291 | -47.75879 | 2026-08-29 04:29:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 698127ee-d9f8-35e1-8276-a0d5f8a42cd9 | -2.72327 | -47.05212 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4995ff94-e941-3c3f-b0da-48e6c70c0eae | -2.72047 | -48.80034 | 2026-08-29 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 957ba79e-b10f-37b4-a151-79ddf989c4de | -2.02194 | -52.11102 | 2026-08-29 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b8e8034-92c2-3b38-b825-df4801b625ab | -2.72201 | -48.79995 | 2026-08-29 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0dc4c655-718f-35c9-b942-fb281de60b56 | 2.524 | -50.85404 | 2026-08-29 04:29:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 170dce6f-7f8d-390c-bec6-2d60301798fa | -1.59558 | -47.35743 | 2026-08-29 04:29:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2c0c39b9-18dc-384a-a1a0-cfcee524355f | -3.35688 | -44.22632 | 2026-08-29 04:29:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 175a6be1-4331-3097-b1e8-481050429c0e | -3.69352 | -39.58548 | 2026-08-29 04:29:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b391580-ff6a-301f-b8c8-d8b44dea445b | -2.7226 | -47.05627 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 462fdfff-abe0-3eba-8b32-20db2e5d2379 | -2.72235 | -47.03493 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44f04265-5833-3402-835e-842546f36aaa | -3.97356 | -41.51571 | 2026-08-29 04:29:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4c995a0c-29d2-36e5-94cc-364f3e209b11 | -1.03496 | -47.55614 | 2026-08-29 04:29:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92064e99-1d09-3b2f-a005-68f6eb5db41b | -2.72529 | -47.03967 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d221d8e-1c02-37a1-b189-2d6d7f60b936 | -2.71898 | -47.0557 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94f9feb1-780f-3ba7-93de-609bffbf763d | 2.16072 | -50.91456 | 2026-08-29 04:29:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 294db81b-69c0-3519-9119-96a435a3d196 | -2.89705 | -48.27216 | 2026-08-29 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0099348a-b695-3c03-8412-b0f8b1efbaf2 | -2.95256 | -43.25189 | 2026-08-29 04:29:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 012f7404-8b51-3cb8-bceb-86dbeee80466 | -2.49859 | -48.13496 | 2026-08-29 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 64e5d254-37fa-3fac-9816-d0af7f2f3081 | -2.71966 | -47.05156 | 2026-08-29 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 642fcc42-7437-3fe8-812d-4dad0991d893 | -10.4794 | -64.5012 | 2026-08-29 04:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 2fd8924f-9fd0-324e-8d20-2966e813fece | -6.77 | -55.6445 | 2026-08-29 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| ec47dc95-23b8-3222-9a25-114a4dd0f6cf | -7.5137 | -55.3051 | 2026-08-29 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 101f4e35-03dd-30e1-9d7e-114f55e07502 | -7.5139 | -55.2851 | 2026-08-29 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 01c323ce-1014-350e-aa7f-a729d371feb8 | -7.4953 | -55.2862 | 2026-08-29 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 3ee9b2b3-9101-3a88-9626-caf3f3d57b92 | -5.8895 | -57.7513 | 2026-08-29 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 706918ba-7772-3641-bec1-b8676167ee06 | -6.7884 | -55.6635 | 2026-08-29 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 30d4b426-37e4-3e21-a331-9fb0f060d70a | -6.6317 | -43.73 | 2026-08-29 04:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 4287e643-8215-32a7-85d5-a2c44ed5210c | -7.4952 | -55.3062 | 2026-08-29 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| b994422a-ced7-33c0-8da7-f8b85466be1e | -6.7699 | -55.6644 | 2026-08-29 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 2e548387-a3ae-3f53-893e-83d8289f2206 | -5.8894 | -57.7708 | 2026-08-29 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 534ba5a6-aab6-376a-953b-3f322ca37e8a | -10.4795 | -64.4824 | 2026-08-29 04:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 36b9822d-7c7e-3cdb-909a-2c374a426d79 | -7.09538 | -42.83553 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 848c9a5c-bcc3-3198-9937-25e9924d8041 | -5.88242 | -57.7682 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fa2f789a-c717-33ee-acbd-e15ae7d5b31d | -4.97099 | -49.62208 | 2026-08-29 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc12c52a-2a3b-38d7-b407-2b19683d5681 | -6.63454 | -43.73832 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0e0f40e3-83e2-3e85-934b-0d71734548f3 | -7.51155 | -55.31264 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 3f20f7d8-96ba-3aee-b2ea-e7d78f3527a6 | -11.16293 | -45.05439 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 967f952c-2dea-360d-aaf8-b1d420020cbc | -3.95649 | -44.02788 | 2026-08-29 04:32:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
