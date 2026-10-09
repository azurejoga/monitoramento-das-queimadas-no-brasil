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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c903e4b8-2bb8-37af-a707-c7c9231294c9 | -3.5688 | -54.678902 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71fac282-8f30-3c67-93db-88c8da31a269 | -2.7468 | -54.105701 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dccff81b-176d-3f44-82bf-f23ad00cd178 | -3.245 | -50.403 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bbe21b5-534a-3256-8365-dbb858251fbf | -7.2168 | -55.111 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0204074a-7e4a-360a-936b-5d9ca5f34d9e | -5.3837 | -45.947899 | 2026-10-09 00:28:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 554dbf2e-708e-359c-8003-10634856dfb3 | -13.5387 | -43.818501 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e72ca541-3588-3e81-a194-61ff129bd97f | -9.027 | -44.386799 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 040cd230-1eb8-3b6c-9913-b201021bda1c | -8.333 | -49.1343 | 2026-10-09 00:28:00 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1444f89-c340-3ee3-934c-0e8fbb989f75 | -16.8878 | -40.715599 | 2026-10-09 00:28:00 | METOP-C | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8772c25-9b78-3cf1-a4ce-0780ce7d257a | -3.3413 | -50.419601 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 653c4aa7-e2af-31a2-9f25-090f170bc80e | -15.9635 | -41.092701 | 2026-10-09 00:28:00 | METOP-C | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f4097e8d-b3c0-3587-a169-56811fa0fdc2 | -14.7841 | -42.903099 | 2026-10-09 00:28:00 | METOP-C | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| fec910cc-2e07-35cd-8e8a-62ebc2326f60 | -2.7726 | -54.084099 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b220d10-e483-3789-bcf8-7e0b7f51ced9 | -11.5803 | -43.691002 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b4a2978-f63d-36e4-8d48-b8f52596f286 | -5.2618 | -50.1432 | 2026-10-09 00:28:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32863bfe-a5ad-3161-8b9f-cbd1d43e3650 | -4.6106 | -42.402901 | 2026-10-09 00:28:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 05d10612-eb94-3762-bceb-9516dc1d9833 | -4.633 | -50.958599 | 2026-10-09 00:28:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 505e2935-fe5e-33c1-8a22-02690228c6bd | -14.0783 | -43.7883 | 2026-10-09 00:28:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fb3e0ab0-9608-357d-82ef-c15705c7c25d | -5.252 | -50.145401 | 2026-10-09 00:28:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b1b1204-631c-32f4-9899-52f3d2253903 | -13.5254 | -44.397499 | 2026-10-09 00:28:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3dc6c5ed-b456-3636-8e88-d7514f3a0ea8 | -10.4738 | -47.240601 | 2026-10-09 00:28:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77cab189-5920-3660-83b3-36bb49605520 | -13.1564 | -43.275398 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d02abd7f-f0ef-307c-9995-16468a3ccf31 | -7.4711 | -42.8493 | 2026-10-09 00:28:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2e4062be-319a-3931-a060-245e1ed12dc4 | -11.9899 | -43.497898 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ef62d83-145a-33ce-a91c-a065ca383f81 | -16.968201 | -41.230999 | 2026-10-09 00:28:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49e68807-d802-314f-8bc2-0a2857b004f2 | -7.7532 | -49.204102 | 2026-10-09 00:28:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| bf83e08f-e154-35d6-9a6c-e4e28d08a3da | -4.5501 | -47.035801 | 2026-10-09 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 647d2fa8-ca12-334b-b811-f99216f04536 | -4.9903 | -45.314499 | 2026-10-09 00:28:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5d4c4fb-bc4c-3df0-919c-a338898c4852 | -8.1665 | -48.610699 | 2026-10-09 00:28:00 | METOP-C | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a63e166f-64ee-39d7-8161-436adce12dde | -9.124 | -45.850101 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 665b7d6f-f71c-30b0-8fa8-c5b59a10808c | -5.1023 | -45.665901 | 2026-10-09 00:28:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6dabae9-51d3-3f68-8234-b5fb2f6f8429 | -3.563 | -54.698399 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 430970cd-34e1-3513-957f-cc5863972078 | -3.1032 | -53.964199 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55d1b19a-581e-39c2-bf8a-7e9c887d5a62 | -3.1786 | -49.247601 | 2026-10-09 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4784563-6c14-3c56-8f34-ec7e3249fb0e | -16.123199 | -43.761101 | 2026-10-09 00:28:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| abbb9089-3e11-3daa-975e-e74314c0dc5c | -0.9908 | -47.656601 | 2026-10-09 00:28:00 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30b1f3a0-727d-37f2-9abe-7fcc51af0905 | -4.7584 | -44.002701 | 2026-10-09 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a9c3f71-38c1-38bb-b28c-ae32ddca471d | -3.5358 | -54.6679 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7613dabe-7a81-37ae-85c6-dab4f5cb6d38 | -11.275 | -45.201401 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8bf1f84-939f-3470-9178-93b8d3f1bced | -11.8382 | -43.6008 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff12ef3a-9230-30b7-affe-82def34a534b | -2.9331 | -54.162399 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f48ddede-b21d-3ed1-a37b-7363fcf9182a | -7.2018 | -55.1362 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| add6c4fa-29f7-32db-9d87-116cd2a5ae41 | -15.1057 | -43.635601 | 2026-10-09 00:28:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 7ce6f488-e334-32e5-98db-dddba2e0e8e6 | -11.4111 | -47.5825 | 2026-10-09 00:28:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7bef81c-da57-363d-8b81-0bc087699099 | -6.9324 | -46.591 | 2026-10-09 00:28:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28fe4cc2-a7b7-351c-a07c-f1aadb9ffb38 | -7.2537 | -48.063301 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 129a2d50-51f9-3aa8-b606-0b19496a1bdc | -3.5493 | -54.6951 | 2026-10-09 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 87d6b1e3-2846-36cf-9af4-bacfa681be55 | -7.1995 | -55.1627 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 13ffa895-99d5-3e76-a84c-9e1fd6b7749b | -7.4095 | -44.7656 | 2026-10-09 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 24bdb889-766d-33b8-aa1a-d5df5f520811 | -1.1094 | -54.1601 | 2026-10-09 00:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 08ac4c17-a506-34ba-87a4-32eebf437f31 | -13.2018 | -54.3551 | 2026-10-09 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| bf17d049-4087-369d-81a6-9044facce282 | -3.2031 | -53.8621 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| de13c069-c794-38f9-ba7b-b5a41e377883 | -7.4442 | -63.5589 | 2026-10-09 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| bcac0f62-3dd3-355e-9da6-af96e02329ad | -6.4949 | -55.2995 | 2026-10-09 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| b8b34d1f-c129-3163-a91a-397b69e4f889 | -11.6562 | -43.6846 | 2026-10-09 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 773d0be3-a024-3de7-9790-87b9d5516a43 | -3.11 | -54.1862 | 2026-10-09 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| bd3c1a89-95e7-316a-8f14-fca4b9c95146 | -13.1827 | -54.3571 | 2026-10-09 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| c085a054-7aea-3b3f-8953-dc7276d83e86 | -13.1636 | -54.3591 | 2026-10-09 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| da39e4f6-af62-3d0d-8586-2c5cd4dc16e6 | -9.2781 | -47.4333 | 2026-10-09 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c140707d-1ef6-3a8c-9595-e4a810a693e7 | -6.7365 | -55.1474 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 1b0371e9-5074-3fbc-9b05-348c04251a11 | -12.2156 | -57.1087 | 2026-10-09 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 4998f471-dbfa-3d41-a693-69bf664fb13d | -6.021 | -40.9577 | 2026-10-09 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 6deac3ed-365c-323e-97d5-193690b43d95 | -13.1639 | -54.3385 | 2026-10-09 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 9bf38541-88f1-3d93-b4ed-0948435dcd8f | -6.8907 | -45.8988 | 2026-10-09 00:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 14eeefaf-0552-3b00-ab4f-ffde371b349c | -3.1284 | -54.1857 | 2026-10-09 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 2fe16181-86a9-3e5d-9180-0d6162a9cb34 | -4.6096 | -49.2156 | 2026-10-09 00:30:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 53bd2115-050c-3769-85c3-863b2f75c8a7 | -6.0019 | -40.9837 | 2026-10-09 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 213.6 |
| 322dec9c-064a-30ff-a60d-5794722aa99a | -14.8854 | -50.2883 | 2026-10-09 00:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8e7eb75a-abb0-3080-bec3-66d7d66b83fc | -9.2973 | -47.4092 | 2026-10-09 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 36c0afce-2f5c-3956-b553-b72b3e9b281a | -3.5676 | -54.6946 | 2026-10-09 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| e060a034-f8a5-35dd-9927-69538ce6d66a | -3.1285 | -54.1657 | 2026-10-09 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| dea5a709-849a-342e-9aa9-36a72b8376ff | -9.297 | -47.4313 | 2026-10-09 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 10fc5a96-8647-33da-abbb-27228292cbd1 | -3.5677 | -54.6746 | 2026-10-09 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| f4d27cf2-721b-316e-af9c-ad80f29cbefb | -2.7428 | -54.1146 | 2026-10-09 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| bae5e7ae-d0aa-3cb9-bb5e-217e86415faf | -7.2372 | -55.0805 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a24d612c-3cb9-3e23-9dcc-611c9f6b6f1d | -3.5493 | -54.6752 | 2026-10-09 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| f154a8f5-8c04-3293-9039-8992f2a57e32 | -6.0021 | -40.9594 | 2026-10-09 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 595.0 |
| 64fc5d01-8dcb-3778-8ac8-4778cf6afa84 | -3.0007 | -53.9075 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 2716326d-2f9f-38fb-b424-db1bd36b8c18 | -12.0058 | -43.464 | 2026-10-09 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| a54fb09a-d90e-319d-97dc-e4cd56998912 | -13.4922 | -44.3713 | 2026-10-09 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ae633dd2-59cd-3be9-9c7e-335f6bbd4d12 | -1.1277 | -54.16 | 2026-10-09 00:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 3aa62530-70fd-375c-bea3-31cd5b2ebc7c | -8.911 | -45.229 | 2026-10-09 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 90e70ce4-d6f5-3872-8b36-0c17dae106c4 | -3.3454 | -50.4288 | 2026-10-09 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 3f0e983c-7571-3f26-822e-c49ff175a3bd | -10.0253 | -48.036 | 2026-10-09 00:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2a7caad6-f850-3213-8953-e1c8a21fa9cd | -8.7423 | -45.1334 | 2026-10-09 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 74fc6c5e-631f-38b2-9b24-ea5e02acac44 | -3.0924 | -53.9656 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 718a1b01-5e6d-322f-8aed-920eba81bfac | -3.7346 | -59.4577 | 2026-10-09 00:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 68c00b68-7a44-3b7a-900e-12006edef683 | -8.742 | -45.1563 | 2026-10-09 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 5978ccae-74f3-38e0-b53e-3e34acfb88be | -11.8499 | -43.5835 | 2026-10-09 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| a5968994-a54f-3c6f-b824-0709fc29c0c0 | -3.1114 | -53.7839 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| cd415e62-a2be-323a-8af8-9b66515303fe | -5.7117 | -53.4862 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| b56f2785-91cc-3661-b2d8-57ad12f07281 | -13.2015 | -54.3757 | 2026-10-09 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 0d033bbf-58ff-3d39-994e-97faed1d021b | 4.4435 | -60.9657 | 2026-10-09 00:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 6007887f-a2a1-3c2b-9d6b-8e63fadd1cfa | -3.2945 | -54.0006 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 16e32e95-d2c9-3b28-9694-5b87359941cc | -11.6369 | -43.6876 | 2026-10-09 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 9a61018b-bd59-3c85-9273-41cbc7a4d395 | -8.8961 | -44.9336 | 2026-10-09 00:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| eccb7a01-05ab-3d69-8aaf-eacd615eb639 | -3.1114 | -53.8041 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 5857170f-9697-3114-8e84-ea02420884ff | -3.1101 | -54.1661 | 2026-10-09 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 148.5 |
| ffda9e16-5a30-35ce-a6c2-ad4557e4f8fe | -5.6932 | -53.487 | 2026-10-09 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 14b079f5-022c-3692-92f1-af8128313c00 | -3.1109 | -53.9249 | 2026-10-09 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |


[Clique aqui para ver as próximas entradas](README35.md)
