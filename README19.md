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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fccdfbd9-d58d-324a-ba64-b865706c7233 | -8.00982 | -46.78465 | 2025-06-19 05:10:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcb4e0d6-fa22-339d-99aa-0743bca93f6f | -2.5347 | -53.95875 | 2025-06-19 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a1b068f-a9f4-327e-84b3-bf142649c182 | -8.75455 | -46.94167 | 2025-06-19 05:10:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06568e52-06ff-3ae0-a526-be598ba7885e | -8.21957 | -47.61549 | 2025-06-19 05:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 089f9467-c171-3f03-95d0-0e21d54b5e7c | -8.72518 | -48.00254 | 2025-06-19 05:10:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c11bb1e-a346-3fa5-a108-749564434a3c | -4.55718 | -48.00423 | 2025-06-19 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b54657e-6563-3965-8de7-de0098643a31 | -8.12725 | -46.08347 | 2025-06-19 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bec79fdc-4500-3ded-8703-22ba6dbeac06 | -4.55142 | -48.00667 | 2025-06-19 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c93c0b2-ad37-3a7e-b477-fbeb96c9e765 | -7.2854 | -49.99005 | 2025-06-19 05:10:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25f01b2e-d130-3e94-b120-2eb73e0fb35f | -6.1618 | -47.26921 | 2025-06-19 05:10:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86f8262b-3908-3199-b3ed-e263cebc08dc | -7.28535 | -49.99456 | 2025-06-19 05:10:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd431d93-97f4-34ad-81ae-c791d575dfef | -6.71888 | -51.45407 | 2025-06-19 05:10:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a49ef8f4-fe25-32df-b256-eb30639c3816 | -6.29716 | -44.23821 | 2025-06-19 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a716285-0027-3244-a9ce-6738ce75404f | -8.75198 | -46.94572 | 2025-06-19 05:10:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b8049d5-7387-3170-9d62-8fd4c3285fe7 | -2.91818 | -48.23751 | 2025-06-19 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2defb4d7-da1c-3f6f-b0db-97c69293f92c | -6.15609 | -47.26842 | 2025-06-19 05:10:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ca74346-bfe0-3f94-8963-cd71436e9c86 | -8.72006 | -47.99797 | 2025-06-19 05:10:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 568e61da-a9c2-341d-9d11-8162fd28037b | -7.14913 | -44.0676 | 2025-06-19 05:10:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 186b7ae8-7a2a-3065-a306-3c02c1d9457d | -8.72381 | -47.99495 | 2025-06-19 05:10:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 820b719c-ab7f-39f8-bd3e-e297a35b725c | -6.29801 | -44.23176 | 2025-06-19 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f90e057-15c2-3a34-9a32-c14f30b1efa0 | -8.75255 | -46.94142 | 2025-06-19 05:10:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 011b4d78-2e71-36b9-a938-13b74df11e3c | -3.32446 | -48.7171 | 2025-06-19 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2830af6c-26f3-38f6-82cb-3d5757b7aed1 | -3.00702 | -46.72331 | 2025-06-19 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d64be31-9bac-3ee7-9bfe-dfaba7b09578 | -8.748 | -46.94504 | 2025-06-19 05:10:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aaefec4d-dd35-3481-8d3c-dbb683a56d84 | -2.92371 | -48.23534 | 2025-06-19 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c58b0e9-e64f-3a30-a10a-21e765bfc4f5 | -8.72569 | -47.99873 | 2025-06-19 05:10:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b92edfd-b957-33bc-961a-62caf25ca33a | -7.36464 | -47.04291 | 2025-06-19 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67872534-3ee1-3456-ae3e-2a7920da7dcd | -7.15697 | -44.06225 | 2025-06-19 05:10:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9ecf1f24-bccf-3c12-875b-f3c719e2d9ee | -3.16583 | -52.447 | 2025-06-19 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4846d99b-0885-322d-9929-45b9fb03fb8e | -6.15951 | -47.26942 | 2025-06-19 05:10:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1d6d02f-9b08-3468-84b2-32e242380c9c | -8.132 | -49.5851 | 2025-06-19 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94b76e7c-2e03-30f5-a5b9-58411669beb2 | -4.28432 | -48.18534 | 2025-06-19 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 298a9af6-e415-3ac3-819b-2c12dbbd6ddc | -6.29101 | -44.23158 | 2025-06-19 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da7cbc0d-c927-3bbc-aa0c-191a3831e00b | -4.77476 | -47.57265 | 2025-06-19 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1618765d-1327-3306-95c4-5e0bfd32e36e | -2.91309 | -48.23671 | 2025-06-19 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8a343be-dc47-314b-8d81-d048d6bf3d38 | -8.21437 | -47.61058 | 2025-06-19 05:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40f20076-b358-3bc1-96c8-8f7319862f5a | -2.91353 | -48.23367 | 2025-06-19 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 857a5a9d-e593-3b86-adb4-b4d39adee093 | -4.77529 | -47.56895 | 2025-06-19 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e1220ff-dc28-3302-98dc-6a998bcb3eb8 | -7.91443 | -47.55786 | 2025-06-19 05:10:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cb6e9f1-3898-31f0-83b8-f0aeab2e3a62 | -8.12654 | -46.08892 | 2025-06-19 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 316d8831-dd52-39b3-a668-a1f197ee0a59 | -2.58558 | -51.92412 | 2025-06-19 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faf6cd74-fa4e-38b7-a74f-636298941404 | -7.15329 | -44.06733 | 2025-06-19 05:12:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 31a219c7-f898-3c2f-b160-5a7e07a7e1e1 | -6.66312 | -42.47297 | 2025-06-19 05:12:00 | AQUA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5019ffbd-949c-3820-a892-42e341183ebd | -7.23123 | -43.09181 | 2025-06-19 05:12:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 48236d17-4cae-3ce2-87c2-2c8606aa510a | -6.6809 | -43.21667 | 2025-06-19 05:12:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 8796867c-c484-3d7b-adfd-9785c8903bec | -8.07291 | -43.10078 | 2025-06-19 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.5 |
| 79a218f0-f1ff-31bc-a9d0-af86f2e45cdc | -6.68342 | -43.20087 | 2025-06-19 05:12:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 12.2 |
| a8c4191e-0bda-3f75-ae3e-dd8273383ce6 | -7.23363 | -43.07694 | 2025-06-19 05:12:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.7 |
| 2c767479-4e78-3435-9f26-8ed1fe008f80 | -8.06185 | -43.09894 | 2025-06-19 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| fd1ed614-58a3-3e4f-b162-c9044b0b3063 | -8.07059 | -43.11518 | 2025-06-19 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 3e7ec86e-42ea-37d4-a4fb-c60a8c4f9165 | -7.24486 | -43.07869 | 2025-06-19 05:12:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| e2e528de-d1e6-3c0f-9fb3-dbf52595de81 | -8.12533 | -43.13105 | 2025-06-19 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| e703f3ba-c521-32fc-b7a0-019cbb3419d4 | -12.4985 | -55.74179 | 2025-06-19 05:12:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54d2c558-aa6d-349c-8506-e1429c344368 | -9.71498 | -64.53989 | 2025-06-19 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f40ad56-b93e-32f6-ae6c-757886bd2879 | -10.65694 | -49.4509 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15f126c7-1738-35e2-817b-f0a80b2358be | -12.21221 | -61.82961 | 2025-06-19 05:12:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ad7b9f3-a441-3dd2-a8a6-ec3e84f9599a | -12.42733 | -54.86646 | 2025-06-19 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35253df7-fca3-3ff3-900b-4f824dc42540 | -10.72775 | -49.56605 | 2025-06-19 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61d2a55b-963a-3d08-aec0-1e7c45e11dd5 | -10.16021 | -48.98635 | 2025-06-19 05:12:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52003534-1054-3cf6-9986-d8baa5d188d0 | -12.58194 | -56.97907 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e38396ac-a3bf-3b9e-afa5-41093b30d6cb | -14.22312 | -45.51313 | 2025-06-19 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad1c2d94-515e-3707-bb45-d477b9cb0760 | -10.50699 | -53.57819 | 2025-06-19 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7c5b38fa-0e35-38d0-a078-901f57d81d74 | -9.46235 | -57.85122 | 2025-06-19 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b2396a3-e1bb-39c4-abab-b2f0c18b581f | -9.00288 | -61.52435 | 2025-06-19 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 373639e0-cbcd-3811-89db-9bc1d9050bad | -9.33784 | -57.84261 | 2025-06-19 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d438c72-013b-3925-8978-37837eaef4b1 | -14.07343 | -53.39523 | 2025-06-19 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 625c3f09-b328-36c5-a16e-e8a9d8535b08 | -11.94874 | -58.74777 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 321eba60-ff72-39f0-813f-4876d1da6b44 | -11.95644 | -58.74182 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5dd015d7-173a-3d3f-8175-eafa46014634 | -11.14607 | -53.93214 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04ec88e2-3f98-3b6c-84f0-d624ff5dccee | -10.09255 | -52.73803 | 2025-06-19 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e646d0a6-757e-32cd-bbb7-60e04752cd41 | -9.79312 | -47.18734 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bfc8cb95-9a31-37bb-8f1e-9162ad12e8c1 | -11.13364 | -53.93534 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4385e91b-c4bc-32d6-a79c-ea426387347e | -14.21698 | -45.51805 | 2025-06-19 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1db9580-65da-3a70-a5b4-706691355289 | -9.33454 | -57.84209 | 2025-06-19 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf9d616d-eaa9-3fa8-b398-a21e99af703f | -10.08589 | -60.49614 | 2025-06-19 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8825289-d729-3772-85b1-b01e50619312 | -9.89869 | -48.02251 | 2025-06-19 05:12:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9f1961f-4592-3f26-a845-05516326ed85 | -11.64593 | -54.13721 | 2025-06-19 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b017db1f-8ab5-3bb0-8bf9-605cd9b5584d | -11.5672 | -47.43174 | 2025-06-19 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45fc20d5-cd31-3e88-85a9-85f3b604c7bd | -11.84188 | -57.85793 | 2025-06-19 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfd1cdc2-cfe4-3f51-9cc8-2278255dc7dd | -10.8574 | -53.76273 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c6da61b-dd66-3a85-b1be-958e71569334 | -12.97181 | -54.68248 | 2025-06-19 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad8bcd08-b4c3-3f41-8c85-81a9f188856d | -11.95589 | -58.74532 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 748f3701-bd63-3243-b302-e1edb110c7eb | -10.86134 | -53.76328 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d48b55f-77d0-38d9-9aa6-7f0a9aa0a05b | -12.48252 | -58.4667 | 2025-06-19 05:12:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f280f71-c2ce-354c-93de-3fcdcbb9d295 | -10.08526 | -60.49994 | 2025-06-19 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bd8df7b-660b-3737-bbce-ef64c24bcbd0 | -12.48913 | -58.46777 | 2025-06-19 05:12:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e05122c-f715-3e9a-8a00-342c8b59c9a5 | -13.58123 | -59.20879 | 2025-06-19 05:12:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df50b6b1-80e4-3e67-a025-ccec27b35de2 | -12.52665 | -57.21149 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb0237f3-c30c-396f-bde2-a392f692d432 | -12.42667 | -54.8711 | 2025-06-19 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d3dfd1e-65fa-325a-9d95-f3fcb76541da | -11.87425 | -54.67876 | 2025-06-19 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c92121d2-d3bb-3f4f-9dca-ad15d738322a | -11.95149 | -58.7518 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b5c508a-7f84-3a70-8208-539119b1be40 | -7.93019 | -61.5578 | 2025-06-19 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d2c1f2c-32bc-38a3-8d0f-39835129af8b | -8.30967 | -55.10023 | 2025-06-19 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da9bbdac-31b9-3f52-83de-bb84fa3a4d5e | -11.95259 | -58.74479 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3dced47d-0038-3a50-ac95-fe122e78cacf | -9.3351 | -47.83583 | 2025-06-19 05:12:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a88ff488-6843-3b75-bb3a-a95db141318b | -11.84238 | -62.83445 | 2025-06-19 05:12:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10155774-18c2-3a46-84bd-48269184fc1f | -11.7744 | -54.37003 | 2025-06-19 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16961e80-ac22-30ee-a23f-1b395a624e05 | -13.28943 | -57.07405 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efa0df0e-5a6c-318a-8eba-3acd49b65b3a | -10.86109 | -53.7664 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87f20910-1534-3a3f-8017-3f51cbaba76a | -14.21626 | -45.52494 | 2025-06-19 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README20.md)
