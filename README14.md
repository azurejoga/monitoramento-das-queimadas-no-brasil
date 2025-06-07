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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3488a62-2b6b-3f02-b029-f5ed75351a25 | -10.49208 | -53.66613 | 2025-06-07 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f94ff3e-3a6b-30b3-b2ef-e44788e95856 | -9.5022 | -40.36972 | 2025-06-07 04:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0e28d888-c9e6-35ad-a8cd-c2ecfaf4493d | -5.64719 | -43.71358 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 576aa0b8-b3a8-3909-909c-6c01dc02507e | -6.20197 | -43.33659 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d76ce6b1-7d51-33a9-b227-3eedfbfdf0f6 | -6.21434 | -43.32382 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e24c679a-f0d6-3d7b-b866-390716b56319 | -7.86507 | -47.90418 | 2025-06-07 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85966762-7498-3730-aa95-6b7cb7ef4ecb | -11.45713 | -48.12754 | 2025-06-07 04:21:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2db99191-51d7-3952-b5d0-db68c1660aad | -10.88217 | -54.30577 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d75fc851-3de3-33a3-a029-21802dfc16d6 | -7.01336 | -44.61876 | 2025-06-07 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ac65350-560d-32f0-a874-9fb919b76dd4 | -12.53514 | -45.41668 | 2025-06-07 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34c7b4e1-c1ea-3d3d-9c04-1f7f92733c34 | -6.23921 | -48.55145 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dbaaed2-751b-3bf8-bb33-4420c2fe7769 | -7.18574 | -42.81695 | 2025-06-07 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 24c04ffa-3ce7-3110-80ab-9b2089f2dce5 | -6.21227 | -44.50299 | 2025-06-07 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4afd58d-899f-3a8b-ab34-5752ecb7130c | -6.23845 | -48.55608 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b483681e-44ba-3f61-8246-c226e5608163 | -9.33498 | -48.5187 | 2025-06-07 04:21:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41b6716b-9c01-3648-b583-0ba630550091 | -6.44807 | -45.72374 | 2025-06-07 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 601bdeeb-18e3-3e41-940b-79d85a925e2b | -9.49647 | -47.39517 | 2025-06-07 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6065da12-93ae-3c5b-ba5d-537b1e7c07b8 | -7.9026 | -50.36485 | 2025-06-07 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e67fda83-5d88-32d3-862d-1cfed8be8d29 | -8.72423 | -47.90265 | 2025-06-07 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be70432e-6368-31a6-9989-3534844485d5 | -7.20985 | -43.11224 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 888f64c2-e202-36f7-b228-81a78644cace | -9.07545 | -47.1466 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28e37e92-9222-3b0d-9897-d36f10329298 | -8.45561 | -46.48715 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3961b4d-d4e9-33a4-a293-09eb4ded7df6 | -7.95584 | -49.64806 | 2025-06-07 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e57cbd2d-95d7-3949-9474-7b34b7d7cc5c | -11.78774 | -47.39819 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 30a7ca40-8d86-3f97-9b52-3448b3bb8355 | -7.22012 | -43.11385 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1e39fe87-6775-3016-ac54-01db3fa36192 | -6.45143 | -45.72428 | 2025-06-07 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c135b1f2-d9a3-3ca9-8da8-80b48312bc84 | -7.72372 | -44.16302 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0721a506-12fe-326e-8570-d6a15ebcb9c7 | -11.78156 | -47.39338 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 149b69b0-9b0e-3b6f-82b3-9783d4d5a42b | -7.7282 | -44.17821 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 15099724-4463-326e-b2a7-2581f4140541 | -8.45446 | -46.49437 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bc921b1-125c-3167-b3be-ab71abef159c | -9.55421 | -47.77301 | 2025-06-07 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 661d9984-4c30-3af6-beff-43419facf6e0 | -6.21379 | -43.32742 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7db459ec-a932-352e-b561-a0af9b5b8abb | -7.90198 | -50.36852 | 2025-06-07 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 651ab02b-70db-31e0-9270-79dc951c9ab6 | -7.71871 | -44.1731 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10f4f130-a827-3fab-a9ca-5a945acd664d | -6.96029 | -42.89964 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 66b11296-3bf9-3815-9a01-b198a7c26f79 | -11.13798 | -53.94901 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 606747f3-cd31-31d5-a8fe-03684ac76768 | -10.49803 | -53.66143 | 2025-06-07 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a148676e-8217-327d-9eb8-e37683f8475a | -7.11331 | -46.55962 | 2025-06-07 04:21:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54caa55f-9309-3419-9ebb-ed51f2cd8a1d | -7.71257 | -44.16851 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fabeb1d-ca80-36d2-8b9d-fb8eebe77f17 | -5.63605 | -43.71903 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 90d9fbd9-becd-3342-8e83-dfa10c83d85e | -12.27305 | -44.60833 | 2025-06-07 04:21:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6165a45b-9ff9-3782-94d6-9d8a737e5a4d | -11.55266 | -47.61705 | 2025-06-07 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89e85ae2-5637-3758-81b6-77dba9509720 | -9.40178 | -48.43449 | 2025-06-07 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1680a794-3da9-3d95-9741-d0632d8257fc | -6.2422 | -48.55674 | 2025-06-07 04:21:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1c82f672-a086-3a22-9eb0-2f333847c71a | -9.07666 | -47.13916 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6e9f065d-11fb-3ff7-8770-1b68e16ad600 | -12.47416 | -46.34031 | 2025-06-07 04:21:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc2a2d34-460b-3621-b476-b6b21f63b71d | -11.77022 | -47.39899 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9622bf9-1d06-3c9b-a079-4cde165ac44c | -12.41751 | -43.81283 | 2025-06-07 04:21:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83b7567e-51cf-3ceb-9c7f-1af2529bed09 | -10.88106 | -54.31179 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97e1b38b-6836-3b91-b83e-7243e2f7ce75 | -10.49104 | -53.67167 | 2025-06-07 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fade92b9-c63e-30b5-a195-cdb1501726d6 | -10.87654 | -54.30779 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d5ec012-fd75-32da-bc75-a16e24c8a293 | -8.38345 | -45.0639 | 2025-06-07 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab1581da-2a3d-3c3d-8bd4-67be0d1972cc | -8.21193 | -48.98396 | 2025-06-07 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07983d0d-dd69-349a-adef-c99eeec5cc4e | -6.2104 | -43.32689 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73572529-5401-3cf8-86f6-ce222aaaa98e | -11.81256 | -44.26804 | 2025-06-07 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 128124fc-4aee-3971-af33-1a86cf2254a0 | -9.33137 | -48.5181 | 2025-06-07 04:21:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84e56d3e-0e6e-354f-8ae7-a43ba82bbc7a | -6.94938 | -42.90176 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b5644068-717e-39d0-8d6e-2609db948318 | -6.95855 | -42.91088 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 0e9cea4c-f900-3782-9af4-9eef79c76845 | -8.38012 | -45.06337 | 2025-06-07 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45d7028b-f58d-3708-b00a-602dcdbf67f5 | -10.49593 | -53.66591 | 2025-06-07 04:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| adfeed2b-3137-3820-9f76-21f08a9bb36e | -6.95685 | -42.89911 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f224f6a4-64bf-360d-9df2-0f5144622116 | -6.21096 | -43.3233 | 2025-06-07 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70711397-b4ce-3078-9b69-3acdbf5b502e | -11.77978 | -47.40438 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f311db14-b0a2-340c-8539-0e6f602af128 | -7.00726 | -44.61422 | 2025-06-07 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e9abce4-12c5-31e4-8dc2-24050f3ec385 | -7.94746 | -49.76205 | 2025-06-07 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74b3d161-b063-35fa-8dba-af7eabc388c3 | -7.02384 | -44.59544 | 2025-06-07 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51c4d87e-e1a5-32df-9bc2-b0f6dd902879 | -7.72206 | -44.17362 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 003cd7f0-c02a-36a7-8632-ce5bc314971a | -11.7736 | -47.39956 | 2025-06-07 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80c3d86c-7c6a-3fc3-bb58-4b25016c94c4 | -9.33236 | -48.51687 | 2025-06-07 04:21:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c04891cb-72ae-3ac6-abc1-2faf37049ce3 | -8.31732 | -47.92104 | 2025-06-07 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ecec572-b219-3681-a798-b58b48013c45 | -7.72427 | -44.15947 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 06a62823-af39-3a89-af81-99ee9f2e803a | -7.81983 | -46.57495 | 2025-06-07 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72ccfc18-6609-3895-8103-c70fe1d5a9b2 | -6.44864 | -45.7202 | 2025-06-07 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd497be9-81b0-3404-a626-bb7c64e1cf7e | -7.73656 | -44.16864 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ab8089d7-261e-3922-afb6-9a48c48f7650 | -5.63995 | -43.71604 | 2025-06-07 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 505f854a-476f-37e4-92f9-0fcd1725293d | -6.95283 | -42.9023 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 7fc7748a-78b6-3bfc-867d-22217d34a1e5 | -6.95627 | -42.90284 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| cf061ab8-e71c-3924-9654-13a173994b43 | -11.02513 | -45.23509 | 2025-06-07 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 86b59577-84ad-3533-b875-1c9409f3cc92 | -6.68529 | -43.6861 | 2025-06-07 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04c92579-7361-37d7-a8cc-628ae68e0556 | -8.1737 | -46.50523 | 2025-06-07 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dcb5d06-c2fe-3bdf-9864-e3eba1e49f85 | -9.5466 | -47.77572 | 2025-06-07 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79d68407-0b88-3c2b-a650-8601046be056 | -7.71592 | -44.16904 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c8f5a92-ada3-3a85-8a40-a54a7b2cc905 | -7.71647 | -44.1655 | 2025-06-07 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7741a0cc-ac65-3601-8565-31c0a836a502 | -6.95109 | -42.91354 | 2025-06-07 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d7081615-cc38-3778-899e-d135330b3f0a | -11.11813 | -54.66214 | 2025-06-07 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6803f5e-b2dc-30c2-b36b-754c71a110f1 | -10.29454 | -57.14009 | 2025-06-07 04:21:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9a807a2-4e23-32f0-9acd-71890e5739f6 | -9.12424 | -46.88889 | 2025-06-07 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ef5cdd7-84df-3ba5-b7e2-554aef8ae4a9 | -12.53625 | -45.40953 | 2025-06-07 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4af08e53-7aa1-3307-be73-ee0b84b70215 | -7.95466 | -49.64959 | 2025-06-07 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 902160fa-41f1-3cdb-a655-b1a0e0293ee4 | -11.33309 | -44.8531 | 2025-06-07 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44c60c12-b800-3d2a-b042-15ddf63925f5 | -9.62761 | -48.60257 | 2025-06-07 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d386a87a-7c94-33ad-844a-7fbfafc7debd | -9.33597 | -48.51747 | 2025-06-07 04:21:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7335d84-4b04-3f77-a45e-68cde042db72 | -9.88211 | -44.80093 | 2025-06-07 04:21:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0561e2ae-668b-33ca-9416-1b60546f37cc | -9.62399 | -48.60196 | 2025-06-07 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6e24e4f-9df3-312f-9592-535e9c99e1ee | -11.45664 | -48.12446 | 2025-06-07 04:21:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 585a690b-b60e-346c-a26f-088261b77f16 | -9.07142 | -47.14975 | 2025-06-07 04:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcc96203-72e8-31aa-b045-4f8e3dca35dc | -13.33823 | -45.48543 | 2025-06-07 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afe2bda3-8d23-38d7-861e-f604fe35bc41 | -17.34833 | -52.00815 | 2025-06-07 04:23:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bff40ce6-c39e-3a8f-a3c1-9f4fa5bd07cc | -12.32399 | -52.47043 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 540cf088-2168-3283-a3f6-effe47ab4a14 | -16.03711 | -43.72367 | 2025-06-07 04:23:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README15.md)
