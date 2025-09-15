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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f167212f-80a6-3deb-ad79-8b7296abe22d | -8.91241 | -45.49751 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62b7213f-eb33-3616-be4c-975855f978dc | -8.11711 | -50.1675 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bf85507-3619-30da-9e60-14cce28f9da6 | -6.32696 | -43.34268 | 2025-09-15 04:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae16b8cd-5e3b-3451-ba99-03e0e66fd66c | -6.34017 | -43.16254 | 2025-09-15 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2bba986-c190-3bfc-a8b6-83ef200a6e92 | -10.79699 | -45.98598 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bd3a2e7-8fe4-34c6-a21e-865addecbe70 | -8.94037 | -45.7956 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3abf147c-4fa9-3ffa-b0d1-5afdfab2b7cd | -10.14852 | -46.14756 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be2ffe1d-a343-3ee6-be94-6ea52e423413 | -8.97502 | -46.21254 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8aca864-cb73-3f76-add6-300577e2c023 | -8.42991 | -45.73383 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f23da409-7568-3c27-bc94-1f4ae79f5e44 | -10.15505 | -45.30056 | 2025-09-15 04:49:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d4521ee-3f8d-3fad-a6f6-4e48c7c08229 | -9.09049 | -44.81245 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c615600-60cb-3335-ab0c-a387a6574849 | -7.05812 | -44.14012 | 2025-09-15 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7221ee01-3c60-3eff-9f41-f2d6b65029ad | -8.61795 | -45.73952 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19a1a393-4372-3c6b-837e-60bc639c7705 | -8.64361 | -46.3578 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84d26f75-c485-33a4-839b-d72ed6a2e149 | -7.8691 | -43.58546 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 396db8b3-11e6-329a-bed9-7104347ef6b6 | -3.64832 | -54.05238 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a48217e2-08fe-33a4-b025-9f50e359e4e0 | -8.95628 | -45.80571 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49a0a181-bee5-3bef-afb7-d46eb6660521 | -10.66407 | -46.23704 | 2025-09-15 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4013ed0d-6575-3d4c-99f9-fff9cd98e6c0 | -10.93322 | -45.48853 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2fe14e45-3cdf-3dd6-a2f0-6483d0db72f0 | -8.59871 | -46.35112 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 879c8200-27e5-3002-82a7-7db1159fa3d4 | -10.86384 | -45.46208 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 445960ea-ae0c-3089-a83d-59d6f4d187fd | -7.6406 | -49.72745 | 2025-09-15 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13132a3a-3264-34d0-a03c-79c11f1bd071 | -9.22265 | -44.5047 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1bb1d88-73ea-39d3-8180-39b203a7b8c4 | -8.6507 | -46.36632 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c71678f-9cbb-3e0d-8d70-c757a21fb525 | -7.29462 | -46.58145 | 2025-09-15 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a2ea5d0-e177-38fa-ac62-a409d8085242 | -8.11655 | -50.1711 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5deb0eb2-2553-300b-b7c3-043a60e1774e | -7.51951 | -44.36343 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99b3fc18-2810-3b75-b023-86f03a48b979 | -8.42045 | -47.22173 | 2025-09-15 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8c76039-1c24-3179-a303-21dd80389b45 | -7.98348 | -45.66976 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97b288bd-210b-3695-846c-51421b925cc2 | -8.81864 | -40.67052 | 2025-09-15 04:49:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 329a3901-01d5-3bd9-9a56-b45960eabdb6 | -9.0081 | -49.77115 | 2025-09-15 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f95591ba-4a1a-3548-95e0-ab629c6d4e48 | -6.42528 | -42.60268 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 43527336-53dd-3083-851e-a5e86c393fd7 | -7.88604 | -43.57151 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 6d21a1b0-d9e4-3266-8fe3-08f401ac89ff | -6.68673 | -45.51187 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d58050c7-29c6-357a-89fd-ed620ac8bb5e | -8.14202 | -43.67644 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d98bc911-9022-3232-9d3f-0dcaac882b7b | -6.64064 | -44.7468 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03fb93d1-9bb1-3184-bd48-c6fd37ac3a3f | -7.98034 | -45.66166 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4578dce7-8e3e-3bd5-b5a7-d1e87e349b06 | -8.08142 | -44.50439 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88edfc02-8b3e-3bd7-9864-82b80ea23fb9 | -7.87736 | -43.57664 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| a681c597-e12e-334f-8a08-c642198a492e | -6.89673 | -45.63377 | 2025-09-15 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1528eb18-d686-34a7-92d0-643a0cc6118d | -7.63496 | -49.74155 | 2025-09-15 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eaf06946-2ddc-32a9-81b5-a43c499a1cc7 | -10.65508 | -46.23955 | 2025-09-15 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba785c6a-de45-35cb-95ce-0b553bbe268a | -5.93442 | -44.86927 | 2025-09-15 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b734505-f7d7-38c0-a4e9-8a0454002e85 | -7.63552 | -49.73789 | 2025-09-15 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31b4f1df-1d7d-3d7f-99b8-0d1bc66c4411 | -5.7687 | -52.36618 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f0ba860-0997-3062-b349-e3c0866387e5 | -7.8015 | -46.11881 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ef80498-388a-3418-82c4-07cd5d7c41f4 | -9.23339 | -45.66513 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2ca20fc-7ff6-31e8-a7be-04bd70fce5ec | -8.97472 | -45.82302 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c92fd6ed-1962-3a47-b478-da8dba1c5b2a | -8.92413 | -54.44602 | 2025-09-15 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23c4d642-ae4a-31e9-8d70-317a868adbb3 | -4.18146 | -48.57381 | 2025-09-15 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8419a7b2-7e3f-324f-a900-5e7e42413a87 | -8.41203 | -47.22533 | 2025-09-15 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9597a60-fe20-3417-9a45-1c8a85e897cd | -3.85197 | -52.21242 | 2025-09-15 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a20366d-ca0e-3f09-9618-dcfcacb701d1 | -8.98063 | -45.81174 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3532fd24-81fb-31bf-8a30-161e8a684d91 | -6.41603 | -42.6104 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa7d7e72-d567-3c57-a293-7c9589a5cf01 | -10.74039 | -44.78736 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e8f5b36-494d-3660-949b-c12a41a91877 | -8.10753 | -50.16242 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2e0f045-f743-3b1d-8860-c3b51188b48f | -8.63386 | -45.68972 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e587a57b-3eb4-3ea1-b376-06979370d99d | -8.9615 | -45.79312 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 91e66cf2-b062-391f-b997-12cb2442851c | -9.23282 | -45.6692 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56be8efe-d8ea-30aa-a8de-783725d60caa | -7.87398 | -43.58619 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 0b855f0c-fee0-31d9-9f4a-5139f8519727 | -6.17783 | -41.19318 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5625c194-b9c6-3b75-91c6-006d3ed67c14 | -8.34406 | -44.72308 | 2025-09-15 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d08f269c-ad9a-3941-978c-528bf510eada | -8.96399 | -45.78269 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac08d73f-ef1f-3d2b-b27b-bfbfbd2ad33d | -5.18393 | -45.17358 | 2025-09-15 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff33060f-0c01-3fcc-9e13-7c6c472cda9e | -8.43621 | -55.63385 | 2025-09-15 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35d359ab-dbf0-32b1-a035-075eab69e2b7 | -8.78414 | -46.01612 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3de5f22-becd-3c27-9392-af6ae36dbfef | -7.69675 | -48.86088 | 2025-09-15 04:49:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b8a9274-12bd-303c-af8a-5aec1d7957ce | -7.89052 | -43.58956 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cddd9c4e-fa55-38d4-be75-db9d9fd5aa50 | -8.95972 | -45.78212 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02154c84-3c8a-3296-b498-c2912d72f3ad | -8.97091 | -46.21175 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ce12399-5b6b-394f-b512-8ec2b25ec8dd | -9.01998 | -47.02369 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 050656fb-205c-3eda-96e1-824c99a54d34 | -10.66778 | -46.24147 | 2025-09-15 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5fc35bcc-5443-39f6-b01c-e08564ddee10 | -7.79683 | -46.12208 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f6d8306-1e3d-3080-9480-11f70c0558c4 | -8.76743 | -46.07292 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 358ccf89-9f5a-3428-b032-29191dc67f21 | -7.8732 | -43.57056 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 91755061-0219-356c-afaa-292d53c760bd | -8.62221 | -45.7401 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fc91aac-4c01-38d3-ba09-5c218dd00d5e | -8.60792 | -46.34504 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d094bd7a-92b5-330a-bcdd-4d1a04d9f61f | -8.95726 | -46.03931 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6026d7c-bc4f-3a1a-a564-7ad3ada5c846 | -3.73561 | -55.94472 | 2025-09-15 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44ad8a0c-50db-36f8-9c3c-bdc4ad1d8f39 | -6.40659 | -42.62492 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 12d7dd32-eab5-3a28-9d1a-7e68b8420fa9 | -10.16992 | -45.3251 | 2025-09-15 04:49:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db544730-7461-3cdd-85ac-8229d8d460b7 | -7.88937 | -43.58297 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 521bb8d2-5f1a-33b2-a7ab-7ecd53e6e613 | -9.09131 | -44.80967 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e56474d-45a8-31e3-af5c-4403955ed604 | -10.90923 | -45.56245 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b237669f-3e4c-3117-83d0-6c38745fb579 | -6.9694 | -44.55375 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 57e850eb-304f-36ac-b955-0f7953178f54 | -6.34815 | -42.53754 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e45f201e-b696-370c-a04c-ba45b49e03e9 | -9.54954 | -45.98233 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5f9f2bf-3dc8-3813-97df-11879bbfb1a0 | -8.78802 | -46.04829 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd967fad-b1fa-3d5f-867d-fd98b28bb819 | -7.67832 | -44.49007 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0719c9fc-d2cb-3b13-9830-6efdefc365f5 | -8.42007 | -44.97007 | 2025-09-15 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ec23cc3-97b5-3b27-872d-dc987dee069d | -3.52846 | -52.8642 | 2025-09-15 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81eacd8c-7d19-3500-934d-219c26bd4cb1 | -9.12618 | -46.94682 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8243f1d9-16d5-3084-9589-e973bdd38895 | -7.50375 | -44.37523 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7249cd02-79b7-3105-a5a0-4af153dce327 | -5.74569 | -43.9277 | 2025-09-15 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d20f93a9-3cb2-3cc3-bd87-d951f95c981c | -7.88652 | -63.70834 | 2025-09-15 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4885d86c-d619-3407-8f02-01cddb29e27a | -9.23827 | -45.66172 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 562ec71f-9f49-385c-adf0-83214b5a7623 | -6.94008 | -44.40488 | 2025-09-15 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cb6ffb2-b427-3233-9c42-00034cc87fb9 | -6.407 | -42.62196 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ff9b9657-7f64-3181-bb3b-a7060df89027 | -6.9137 | -46.16256 | 2025-09-15 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65f4c22b-9d24-3747-b559-9e29fa7f2e20 | -8.50668 | -51.16231 | 2025-09-15 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README41.md)
