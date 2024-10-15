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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f81a9cc-45d2-3202-b6fe-7ab55baa4d79 | -6.81682 | -44.46851 | 2024-10-15 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2331c722-9cf0-32a2-8dd9-8c0470b34777 | -6.8114 | -44.47071 | 2024-10-15 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a2ad636-fa4c-3d44-8187-01a1ddc940a3 | -6.58196 | -44.17996 | 2024-10-15 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13b34902-dfe6-3adf-9c2f-68a5dfa36b7a | -8.91537 | -45.06179 | 2024-10-15 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8c62e4ed-c4fe-38dc-b4a5-41ba3e798cef | -8.91039 | -45.06123 | 2024-10-15 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbbc4e5d-0bce-3ff1-a212-e50bc7a180a2 | -8.3373 | -44.92293 | 2024-10-15 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc6e751c-5c2b-39cb-88d2-35af71603b62 | -8.28576 | -44.85026 | 2024-10-15 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70017a35-aad2-334f-a424-9b1d67c8f35d | -8.13419 | -43.96117 | 2024-10-15 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8de1c402-3771-3d3b-b3f9-b77a9445559f | -8.13384 | -43.95875 | 2024-10-15 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 630781f5-7594-3f96-9e89-1dcd953de93d | -8.12849 | -43.96339 | 2024-10-15 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b1abcb1-b989-3549-9e97-3d33601dbe73 | -8.12816 | -43.961 | 2024-10-15 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80bf2400-a617-3a8b-a1bd-584c216cda48 | -8.12773 | -43.96431 | 2024-10-15 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2685748f-1e6a-3423-8aed-560453ce9162 | -8.02891 | -44.82642 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4702c4d0-cdaf-398b-a306-bd0704fce3e8 | -8.01069 | -44.81084 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c96665e1-4c2d-3788-bd40-38412002445c | -8.01025 | -44.80884 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dd83f436-4e07-38de-88cd-8d4a2c123e08 | -8.00651 | -44.80412 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 685dc04a-fdec-3726-b3a1-fef674e6c2f8 | -8.00572 | -44.81005 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f5d0e2e-25ca-3d1f-84f3-bf833ed7f659 | -8.0049 | -44.81622 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2c82ed8-580c-3c63-8d63-33ab871a01b2 | -8.00443 | -44.81407 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef5e51c5-7375-3bc2-9951-881f6be1dddc | -8.00075 | -44.80921 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b34c22fa-d633-3e49-9e86-4c95c36c588b | -7.99997 | -44.81514 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be1f6ec9-f250-3291-8986-84b20cfc0e30 | -7.99949 | -44.81311 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 467e53f5-e86c-3a0d-bc58-a59baeafdc29 | -10.74042 | -44.70568 | 2024-10-15 04:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26e30602-5e7d-3621-a71b-2030fb0b8777 | -10.74001 | -44.70887 | 2024-10-15 04:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f6fd4de-e209-37f8-8894-0e9adbc01a94 | -10.70584 | -44.97636 | 2024-10-15 04:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99c0ba26-9d0c-3a39-87a6-451bbc939b90 | -10.70544 | -44.97948 | 2024-10-15 04:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be607429-28ce-36f3-a9f2-a6a0fc5441c5 | -10.38958 | -44.82001 | 2024-10-15 04:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bbc3858-8faa-398f-9b95-8487973965ff | -10.38918 | -44.82315 | 2024-10-15 04:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a02fe1ca-8ab5-3ce2-901c-f7e2844c9ee1 | -10.38879 | -44.82623 | 2024-10-15 04:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ca3b44f-85ad-3334-8148-2a838e760b83 | -10.07061 | -45.04443 | 2024-10-15 04:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44f757d8-7a5c-3a24-8ce3-7bc1d5423624 | -10.06557 | -45.04369 | 2024-10-15 04:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80fc93b7-2048-3578-a1f0-1a9d81871e84 | -11.05844 | -45.36428 | 2024-10-15 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77470607-83f0-3f3b-95b4-51cc99f9aae8 | -11.05342 | -45.3637 | 2024-10-15 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19ac8874-b734-3139-8914-b5e3e85a032f | -11.05334 | -45.36584 | 2024-10-15 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcf729e3-6420-324a-94fd-047de2800d49 | -4.71888 | -46.1556 | 2024-10-15 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8963c971-9cfe-35c1-a682-f6e78dd49d0e | -4.71765 | -46.16406 | 2024-10-15 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66e1d912-5979-3cef-9c47-b7ec49506ae4 | -4.71333 | -46.16338 | 2024-10-15 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7981085-3d98-3764-8e24-2709c2189b5a | -4.7096 | -46.1587 | 2024-10-15 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e5660fbb-a3f6-3560-b46d-e3ed265ae9d0 | -4.70901 | -46.16281 | 2024-10-15 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cb7e2b3c-481c-3064-9e92-59678f7cd764 | -4.70751 | -46.15985 | 2024-10-15 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 05a8e64d-03f8-3260-9b61-24d7dc4f1b4d | -4.70688 | -46.16398 | 2024-10-15 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e8d9aa7a-24eb-3695-82c1-db74f9a44fa2 | -4.70468 | -46.16227 | 2024-10-15 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| abac3059-0c88-35e4-ad31-05aac068a535 | -4.70255 | -46.16341 | 2024-10-15 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a7ecbf36-ec20-3039-b315-0da57d4818d9 | -4.70035 | -46.16171 | 2024-10-15 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce30f8dd-009c-337a-b51a-3266dab6a60f | -4.68631 | -45.79405 | 2024-10-15 04:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 193e4d70-047d-3254-8d5c-d60f5802b72d | -5.4809 | -45.51642 | 2024-10-15 04:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93007552-61f1-39e8-8535-192c606ed766 | -5.29708 | -46.40152 | 2024-10-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 935bf841-4b74-3ea0-bf87-7c01e148a1cd | -5.29463 | -46.38868 | 2024-10-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b911d499-2e82-3c79-9edb-728801416ace | -5.29341 | -46.3968 | 2024-10-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef24765b-6927-3fba-9681-b2387f2dc6e6 | -5.2928 | -46.40089 | 2024-10-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f18a0cc-8a96-3562-b486-b56bdf7c8933 | -5.28117 | -46.39079 | 2024-10-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 508dacbf-6e41-3c76-ad4f-8df9a6779a38 | -5.27934 | -46.3736 | 2024-10-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 082c474e-3e39-33d0-bb7d-7a3500e57200 | -5.27871 | -46.37782 | 2024-10-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dde3e801-da79-3697-b968-2cb4a2371faf | -5.27681 | -46.36104 | 2024-10-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2adba0f9-3c6c-3863-8ed8-df9f7ccdbdf9 | -5.27504 | -46.37299 | 2024-10-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ccbc6681-4471-3ccb-b43c-b9c8d78df32c | -7.41247 | -46.15645 | 2024-10-15 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcd4bd7d-3048-3b2e-a834-a12491185ad5 | -7.21003 | -45.39273 | 2024-10-15 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd43bffb-6ab4-3804-8cc1-ae72f1767b3e | -6.96856 | -45.54868 | 2024-10-15 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef57d929-9858-338c-9630-907e92011392 | -6.87772 | -45.46455 | 2024-10-15 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d996761c-7379-31f7-8eb0-24a7e11d30d4 | -8.05493 | -46.63224 | 2024-10-15 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b6b9a73-9e93-3215-bab3-44bf467d50e0 | -8.05054 | -46.63154 | 2024-10-15 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08b4e1a7-b782-3a39-9359-e450087b7bd1 | -10.47142 | -47.49109 | 2024-10-15 04:49:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc3ff0e6-7de9-3db0-9762-f445c1924882 | -10.28636 | -47.20329 | 2024-10-15 04:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fee1da70-382b-3070-bda3-41af16d389b5 | -9.97844 | -47.25498 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b572ee33-1bfb-31f0-8d7d-633bdd12b6a0 | -9.97787 | -47.25914 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb37d456-c8f0-3e0d-9dc3-ffe56ea08e0a | -9.96544 | -47.25316 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b166a8a6-0067-321a-bdf7-9f20fcf58327 | -9.9611 | -47.25257 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d08d6572-23a9-36b8-9abf-64e90bede867 | -9.96053 | -47.25677 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 888a23eb-a3e7-3cce-96cd-4532d192f1c6 | -9.94603 | -47.33077 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a53858f7-d489-32ab-9797-e34f41ce8bfe | -9.92796 | -47.26918 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3d32b6c-7c02-3244-9aa7-3e36eb37666e | -9.9274 | -47.27338 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc681992-2097-3066-955e-f309c1e677ab | -9.92608 | -47.27045 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e515702d-bf9a-3e90-ac94-b67dd4618deb | -9.92548 | -47.27465 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 653b19c4-c2a2-3057-9510-a9f975277a15 | -9.91763 | -47.29894 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0766d5a-2e22-370b-a93c-2a9af5f9a88a | -9.91389 | -47.29424 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9220b99f-a7e7-3248-86d1-328f64d54bf5 | -9.91331 | -47.29836 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0349ad6-a4f6-3961-92b1-44107636a202 | -9.90957 | -47.29366 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dc442ed-7abe-330c-a3f5-7aef944fe2e1 | -9.71622 | -46.94505 | 2024-10-15 04:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e972ed6-7691-3ca9-bcf1-8b6d3c92d679 | -9.67119 | -46.91253 | 2024-10-15 04:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dc14621-2c1a-3240-814f-a6a64d6d2993 | -9.6706 | -46.9169 | 2024-10-15 04:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dddb272-6ba5-3ce6-add6-863b8aa1e1ad | -9.66679 | -46.91176 | 2024-10-15 04:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d58bcde1-15b7-3c80-80f0-58fc1a04d641 | -9.60574 | -46.63323 | 2024-10-15 04:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0db8c51f-ebfd-398d-944e-55f7134a3313 | -9.60513 | -46.63775 | 2024-10-15 04:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34c18c42-ec2d-3249-86ac-d13b0e2187b5 | -10.00531 | -47.2841 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ca86659e-a51d-3734-965a-7958f1d997e5 | -4.89345 | -47.64057 | 2024-10-15 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 35.9 |
| a7445ccc-79fd-386c-8b26-6ef28a5a1afa | -4.88951 | -47.6401 | 2024-10-15 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fc793658-96d8-3093-9a30-feabb201971a | -4.87473 | -47.10564 | 2024-10-15 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 514bfcc1-aea9-3ed5-8c47-b75af1439726 | -4.87419 | -47.10917 | 2024-10-15 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96e265d0-9891-36ee-985b-b094ae23e240 | -4.87123 | -47.10133 | 2024-10-15 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0a61ca5-7982-334b-8064-2fde7dd35e76 | -4.87013 | -47.10859 | 2024-10-15 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4c1b248-73a0-3b13-a76e-e66da3694901 | -4.86608 | -47.10791 | 2024-10-15 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28438c5f-be13-353d-a572-55ee8bc890cc | -4.72355 | -46.71839 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a315834e-ff61-3c8e-bb9e-fa1cab1ccc88 | -4.72206 | -46.71548 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28c76e12-a85b-3bac-9134-395e0f8c39de | -4.65131 | -46.81973 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 982394b8-9702-33ff-8fe8-cebd256fbe99 | -4.64776 | -46.81523 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80592c6e-7703-315f-8d21-771eb348c35f | -4.64721 | -46.819 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1165b181-74f2-30f9-aa36-171f2d4bbd81 | -4.64365 | -46.81452 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53be0db8-620f-334f-a519-9e404a395bfb | -4.63056 | -46.90274 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be87aafa-d951-3742-8a4c-0c302b7455ac | -4.54329 | -46.56112 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 007c1d52-1477-3bc5-ab54-000eecb65d9d | -4.54272 | -46.56499 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README58.md)
