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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32258007-3fbe-3782-abd9-3cccc66ec44f | 1.1507 | -50.7483 | 2026-10-06 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 85.5 |
| e51efdb6-a4ff-36e8-a286-16797eb7fb47 | -11.6951 | -43.655 | 2026-10-06 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| eb14d0ce-959e-335a-bda0-7ef85f2b05d7 | 3.0733 | -60.576 | 2026-10-06 14:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c1b0b2e4-c742-3181-a720-fdd5a49e2039 | -7.2079 | -44.3024 | 2026-10-06 14:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 16aea711-82b3-35da-8161-0f24575a4d91 | 1.7304 | -55.6259 | 2026-10-06 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 57a354fa-9635-3b49-a1ca-2a38bca61c3d | 1.7854 | -55.5856 | 2026-10-06 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 175.2 |
| c8bbb003-0910-396b-8328-f3aa19873bac | 1.7304 | -55.6061 | 2026-10-06 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c38d7bd9-8170-3560-9df5-57bf6e730f3a | -9.1613 | -68.2568 | 2026-10-06 14:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 68313254-4b7d-3ad8-8145-6f998d6eeab3 | 1.8038 | -55.5458 | 2026-10-06 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| d18a5efe-22ee-37a5-b8a2-3d3e581db7c3 | -11.21 | -46.2655 | 2026-10-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 695b2eeb-588b-3eec-ba42-814cedca4180 | -11.657 | -43.6373 | 2026-10-06 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 0ddd56df-1469-3147-bce6-303b9d030ea6 | 3.128 | -60.594 | 2026-10-06 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 196382f8-b23d-3e3c-b65c-ebfbdde217f1 | -11.7143 | -43.652 | 2026-10-06 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 4d7fd72d-6610-3f2d-bf81-024b5f20d25f | -11.3753 | -46.6497 | 2026-10-06 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 72486270-6639-3950-9751-66d13c03031c | -11.8311 | -43.5628 | 2026-10-06 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 2c43e09f-5689-3c4c-8fa8-2d25d9955585 | 0.4465 | -60.5442 | 2026-10-06 14:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 84.7 |
| e1fe1209-362c-3947-a4ff-30254984d073 | -6.8957 | -43.6368 | 2026-10-06 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 162.7 |
| c23d8a5f-ba36-3b45-aa61-40cd68b62f56 | -11.21 | -46.2655 | 2026-10-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 238.1 |
| 271f0efb-f52e-3daf-b310-6f6b6488a097 | -7.1778 | -42.0055 | 2026-10-06 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 08b776c8-3e5b-3ca7-b4f2-c97e103a394a | -7.8682 | -44.169 | 2026-10-06 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 270.5 |
| 80a906e7-0d4f-324c-8be1-40a5be03b7dc | -11.6946 | -43.6787 | 2026-10-06 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 1eb7520e-ab31-3ee6-bf59-e1fc1363cee7 | -7.4001 | -45.6072 | 2026-10-06 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 214.2 |
| 1b6c659c-d18d-3a8f-ac4f-0d5f27cd5e8e | 1.8038 | -55.5458 | 2026-10-06 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c01f99a6-4f07-3120-a8ab-492edff92044 | -11.6951 | -43.655 | 2026-10-06 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 244.0 |
| b9ad65a8-928a-3a50-885f-544e0c379619 | 1.9864 | -55.8789 | 2026-10-06 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| bd8a26fd-9592-3395-a69e-8ba6004ab9ab | -12.1948 | -44.6554 | 2026-10-06 14:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| ba8fc429-4c12-36ec-a007-2734d90d17fa | -11.6758 | -43.658 | 2026-10-06 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 26cc2de6-ce5b-3598-a64f-e9a848682bc8 | -10.9758 | -45.4324 | 2026-10-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 560.1 |
| 648ec090-f364-3304-903b-8cd26e30f35a | -11.8315 | -43.5391 | 2026-10-06 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 231.9 |
| 51f05253-d214-371d-a4d9-b6b6bc2d5f5a | 1.7855 | -55.5461 | 2026-10-06 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 57001f9f-89af-36b3-8198-ff79161850e9 | 3.1281 | -60.575 | 2026-10-06 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6175f9f5-d737-331f-add4-8cce451cb9f0 | -10.9755 | -45.4553 | 2026-10-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 6bd9cf8f-f29b-3426-986c-cdf470e8ed34 | -7.2079 | -44.3024 | 2026-10-06 14:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 296e76e8-49a0-3cce-b517-87e753c93d75 | -7.8684 | -44.1459 | 2026-10-06 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| c3dbe7bb-9a69-3ca8-b47c-ca7f33df25f3 | -9.0046 | -65.6988 | 2026-10-06 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| dc70603e-b8b7-3d57-8067-42e36406efc9 | -7.47 | -42.8078 | 2026-10-06 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| f9ecfd75-9c1d-353b-ae3b-f146da31c82e | -11.657 | -43.6373 | 2026-10-06 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 46e004a0-1fa6-34db-a350-fa85b6b47e0c | 3.0733 | -60.576 | 2026-10-06 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 67961ba8-0a33-390c-8013-ec548c53c5cf | -11.0485 | -45.6511 | 2026-10-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 3cf3430a-c7fe-32e0-a9e1-2b5721fde11d | 1.7854 | -55.5856 | 2026-10-06 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 193.7 |
| 61760f94-fa5e-30c4-9e6e-d6ce2f4946e4 | -9.8071 | -44.7804 | 2026-10-06 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| f67c15b1-1d84-308a-bcbe-b83be8a0bc53 | -9.0059 | -65.4186 | 2026-10-06 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 74ae2be1-b0ef-3837-b25f-a36a0682405f | -11.7335 | -43.649 | 2026-10-06 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 2239c7d8-7f16-359b-a116-0c2964e5f2ba | -10.9762 | -45.4094 | 2026-10-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.4 |
| b220ade9-8842-34ba-b1a7-778f39f02bef | -6.7068 | -45.5539 | 2026-10-06 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 9b10d00e-a55c-31eb-8f9c-f08dc4a306ad | 1.7854 | -55.5658 | 2026-10-06 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 172.8 |
| 1f2ee882-bb95-3eed-bfce-0517f45729aa | -9.1613 | -68.2568 | 2026-10-06 14:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b660c2f2-4f24-3911-abb0-5884bee4e417 | -11.8296 | -44.688 | 2026-10-06 14:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| d648b8f7-3b22-3c8a-a196-b35b5ed5663b | -7.2077 | -44.3255 | 2026-10-06 14:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| ff9f4a9a-40dc-3a01-9ce2-4af2d3fbba05 | 3.055 | -60.5952 | 2026-10-06 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a390a246-71be-3d14-a2c8-5f6706bc8682 | -9.7312 | -65.0944 | 2026-10-06 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 16835841-efc5-3b24-95ea-f4023cabfddc | -7.8496 | -44.1478 | 2026-10-06 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 191.6 |
| ac00021f-b125-3688-be77-0ff76134b418 | 1.7671 | -55.5859 | 2026-10-06 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 6608d27e-e0a1-34c3-ad03-47fd2f5c25ed | -11.1909 | -46.2681 | 2026-10-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ba3fb35f-79c1-377e-a051-f821f702f05f | -9.1334 | -65.9 | 2026-10-06 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 1b1718ba-b989-3afb-a73c-38f68bee0905 | -6.8952 | -43.6833 | 2026-10-06 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 50dc7fd0-5171-3748-aed0-0b6bd1bbb00d | -11.3562 | -46.6522 | 2026-10-06 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 7c6ad2dc-e4fb-3a20-8964-55b2957680c7 | 1.7304 | -55.6259 | 2026-10-06 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 997f2477-e6ed-33ab-99ef-bae39c849b1f | -11.0 | -45.47 | 2026-10-06 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca2010ba-d568-3f70-b76a-f399882bd523 | -7.86 | -44.16 | 2026-10-06 14:15:00 | MSG-03 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b2c81815-c1a7-376b-a931-5c5df7159774 | -14.34 | -41.27 | 2026-10-06 14:15:00 | MSG-03 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ab4e2969-eea2-3b30-ac58-7df678755a5c | -11.09 | -45.68 | 2026-10-06 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee3c02ac-5fd8-39f3-a8e9-b8e1af45b4d2 | -14.37 | -41.28 | 2026-10-06 14:15:00 | MSG-03 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fb97b68b-4df7-3167-983d-809ff7add082 | -9.42 | -45.86 | 2026-10-06 14:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c9d839f-6494-3edc-80d8-1fce2ea8035a | -10.99 | -45.42 | 2026-10-06 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1f630d6f-cfb1-3b37-a9b2-d9556f33e5a1 | -10.17 | -46.47 | 2026-10-06 14:15:00 | MSG-03 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac3dbd74-e190-3561-b92c-f400e5521084 | -10.2 | -46.47 | 2026-10-06 14:15:00 | MSG-03 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1bb5497-3764-3a8a-88ff-af0bf15de849 | -3.9697 | -41.5416 | 2026-10-06 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 143.4 |
| e3b80c07-aaad-30a4-a5fc-8b4b3d59d4a6 | -11.21 | -46.2655 | 2026-10-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 525.8 |
| e9313d76-255d-36c3-b8d4-333ed0c5d76c | -6.7228 | -44.0001 | 2026-10-06 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 30c36b18-76aa-32e5-b4ca-af3951456f95 | -7.2079 | -44.3024 | 2026-10-06 14:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8f8b02a9-eb78-3f57-a5bd-1d461b2e0765 | -9.0059 | -65.4186 | 2026-10-06 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 2cce002e-373a-397e-bd1e-106080ba4db3 | -9.8257 | -44.8011 | 2026-10-06 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 135.1 |
| b9a0e2b7-7a95-3961-a97c-9ee1dba617c1 | -9.0046 | -65.6988 | 2026-10-06 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e7d58724-4ec9-3e40-8a3e-dd252e0f9b62 | 1.7304 | -55.6259 | 2026-10-06 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 3cf7ec6a-ed7d-33cc-9ce8-095e18decf5b | 3.1281 | -60.575 | 2026-10-06 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f4522b17-e270-352e-9873-4b4dbcb1128c | 1.7854 | -55.5658 | 2026-10-06 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 77a8d70d-5a4b-3529-a40f-0d672ab233fd | -7.2077 | -44.3255 | 2026-10-06 14:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f42f7720-85b0-3d68-9f02-f8bc28bf8a44 | -6.8998 | -45.0167 | 2026-10-06 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| d6c66488-1c2c-3b32-b54c-3318dd9bfb1a | -7.8682 | -44.169 | 2026-10-06 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 221.2 |
| c9684e8a-525c-3fbe-9ba9-c7557d4db3e4 | -12.1948 | -44.6554 | 2026-10-06 14:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| e67e83c7-7049-3e99-96d2-fd9a90f12d29 | -9.7312 | -65.0944 | 2026-10-06 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 232b1bf4-0564-3802-93ad-6ba1d358aef1 | -9.043 | -65.4175 | 2026-10-06 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f07ded74-e198-3d32-831e-8528a692de38 | 3.128 | -60.594 | 2026-10-06 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 15558981-af3b-3f4e-8b75-d5f639bd036d | 0.4465 | -60.5442 | 2026-10-06 14:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 01528c58-1d07-39da-95b5-382a3b8b3343 | 3.0733 | -60.576 | 2026-10-06 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| aa78d953-5d1f-3edc-8e74-d2803b44e143 | -9.8261 | -44.7781 | 2026-10-06 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| a534d72a-33a0-3d86-b868-dbb76347100b | 1.7855 | -55.5461 | 2026-10-06 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 89328297-8774-3994-9d8e-6fc314ead601 | -9.1613 | -68.2568 | 2026-10-06 14:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d18ef028-f5e2-392c-bb3e-7453d088ae27 | -0.3952 | -52.0768 | 2026-10-06 14:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 115.8 |
| d39a7a45-3a38-3c65-b13a-030c541ff243 | 1.8038 | -55.5458 | 2026-10-06 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ff62a031-20e9-3446-b2eb-c2ebea69e743 | -9.1334 | -65.9 | 2026-10-06 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 23880042-868b-3b03-8f0c-0857fc662b0a | 1.7671 | -55.5859 | 2026-10-06 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| c550754d-3f5f-3295-acec-725e39eb00f6 | -10.9758 | -45.4324 | 2026-10-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 213.2 |
| 80d4c460-e778-3d04-a382-d443c466bb8c | -11.8315 | -43.5391 | 2026-10-06 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 262.0 |
| 5110bb7d-b664-35f0-ba52-7bd4e20c6646 | -9.8071 | -44.7804 | 2026-10-06 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| f7e49b5e-b95d-31fe-a724-b749023ef1a9 | -9.0244 | -65.4181 | 2026-10-06 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 81c4b7dc-c4b9-3c89-8ee1-195436f1fb77 | -10.9762 | -45.4094 | 2026-10-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 142d341e-52f1-39ba-9135-28d1f1c364bd | -11.0485 | -45.6511 | 2026-10-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 4ded9357-58d2-3ac0-9c86-62655d05af0a | -9.8067 | -44.8035 | 2026-10-06 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |


[Clique aqui para ver as próximas entradas](README84.md)
