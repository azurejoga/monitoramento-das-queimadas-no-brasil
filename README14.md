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
| 10e813ae-917a-378b-abdc-70ddf6ecd722 | -6.91215 | -43.98111 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b573cb6f-375d-398b-a1ef-f28b7073dbdf | -4.54093 | -48.02301 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 3f6e6803-040c-3f65-a87c-bf53d15650d4 | -7.21973 | -43.08216 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 6f432f19-8eff-38aa-b7c5-fe27d3f27cee | -6.22818 | -44.52498 | 2025-06-28 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 385d6e43-9d4d-3e82-ae32-26cad6fc9659 | -8.3093 | -46.31026 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01fe2fd0-55ec-3ca3-93cd-7bc2cfc269fc | -9.43807 | -47.9604 | 2025-06-28 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bef83ac1-3b1a-3d75-9da8-20974abfe2e9 | -7.20377 | -43.08856 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d5a8286a-2b91-3426-a04a-a9d5cbe2c2f5 | -5.73929 | -43.05149 | 2025-06-28 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ffa4cd5b-a3a5-32b6-a1b1-8c5176554645 | -4.54154 | -48.01923 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 944932a0-98b9-36d6-9a8c-928327c9b797 | -6.91036 | -43.99282 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3c83993a-637e-3b12-9760-66c0609e7a1d | -8.42465 | -47.05342 | 2025-06-28 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c58b61f0-75b8-322a-bf6f-e39c40b475d3 | -6.90514 | -43.98004 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d48ca096-b6fe-3fb6-a06b-9cf1fda87a3e | -7.2167 | -43.07727 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 926cd57e-0fb9-3745-bd13-094a84e2af86 | -5.45908 | -43.07685 | 2025-06-28 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 23ee6271-e57d-3f7b-88c2-84043d45a415 | -9.97737 | -47.80402 | 2025-06-28 04:27:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7e172bc-3b7c-3281-b7b5-cd252a0ea5ff | -9.47495 | -47.32262 | 2025-06-28 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bbcd5ad-d641-3850-853e-2db2be187fba | -9.79257 | -48.55793 | 2025-06-28 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07454897-f6e6-3270-b992-ac70c9344718 | -7.70938 | -48.49937 | 2025-06-28 04:27:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41c70ea3-e405-3535-bc9c-262bdcb37523 | -8.03584 | -47.64718 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf5fac66-3cd0-32cc-8562-f7ec8ba6cefd | -6.54985 | -54.98449 | 2025-06-28 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0b32a66-c40f-3de3-aa66-8c6fafdbaa8b | -4.13022 | -43.06955 | 2025-06-28 04:27:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2129f892-ade2-348c-b38c-9f21963d0f8f | -9.09178 | -47.96645 | 2025-06-28 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 793aa428-2054-3ebf-8a7e-84825e049d52 | -9.7411 | -48.34015 | 2025-06-28 04:27:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 761d4670-39a5-3cb7-bc68-3a206987980d | -6.74349 | -47.22325 | 2025-06-28 04:27:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cdd9082-f4db-32b6-883b-8c7a433383aa | -5.24889 | -35.68358 | 2025-06-28 04:27:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fe641248-6358-35b2-b720-cc522f123936 | -7.22037 | -43.07783 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| a26edc25-4e38-36cf-ad3f-3346b224934e | -6.91386 | -43.99335 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc8944fc-ca8f-3959-9f95-793aeabcd7b1 | -8.30985 | -46.30677 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 776f34b4-6e9b-37fc-8ad4-5af605396540 | -7.54497 | -45.82756 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ea262cc1-d575-36ca-ba31-4bef1f6bc997 | -9.11127 | -49.48645 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5963cf45-13c7-347f-a13c-2dbf5720de96 | -8.0297 | -47.64256 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 477f3106-71b3-3729-a3f1-e45a4bc84164 | -7.20083 | -43.18426 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe116042-8df5-38ba-87d2-49406e47e342 | -9.97338 | -48.24438 | 2025-06-28 04:27:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 39d2a686-f059-3ea6-9f59-a270de11a9ff | -6.90335 | -43.99175 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7dc3c1f2-a08f-33c8-acc5-b890ed043935 | -8.73701 | -47.85048 | 2025-06-28 04:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68cb569d-5818-33d4-9c69-aee9dea9c625 | -9.11348 | -49.4949 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f12ce2fb-b2ba-3fa8-bcb6-c8b1e7cc1bff | -5.85523 | -46.95188 | 2025-06-28 04:27:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01d5b0a6-a634-30bb-8c79-3909bb3b9b92 | -6.91275 | -43.9772 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7663bdb7-6014-3e3e-a0c3-85c0f2b29d85 | -6.54469 | -54.98357 | 2025-06-28 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dd7b263-d422-3bb4-b9b7-23e3bea28026 | -6.23444 | -44.52976 | 2025-06-28 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95375273-31ec-3aa8-ad19-297298667714 | -7.18563 | -43.43493 | 2025-06-28 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e7b623f-4957-3f02-aa7f-c102e779bc7d | -7.18658 | -45.32606 | 2025-06-28 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c623fdc2-c10f-32ff-9291-425f15a19a51 | -8.00387 | -49.71551 | 2025-06-28 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fca5d760-2e26-312d-a028-01f1196d4db8 | -8.86946 | -50.16901 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 120aea46-ff1d-35bc-9402-aea095b049d4 | -6.90745 | -43.98838 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2857d66a-e18d-3713-b372-ac74172682aa | -7.26966 | -43.8563 | 2025-06-28 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65b2ea11-3ea6-366a-92bd-0378fc227199 | -9.15682 | -46.36157 | 2025-06-28 04:27:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 742ee55e-64ae-3b6d-a73c-6374fb20e17e | -8.04311 | -47.64471 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ea196e7-ae59-3108-b004-bc0ddf7d7415 | -9.11832 | -49.4876 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ee40212c-dafe-382a-8d22-aa591701272d | -9.87605 | -48.60519 | 2025-06-28 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 753bae6c-0bb3-3022-a69e-fa9a556ab715 | -8.37655 | -49.23378 | 2025-06-28 04:27:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37acbb85-4034-3a70-b990-4d08a9969ada | -9.87317 | -48.45121 | 2025-06-28 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b556e84-e69b-3690-bece-06c4e95edfc8 | -8.11764 | -49.99714 | 2025-06-28 04:27:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1585bb95-2ee7-3215-b6a9-f28f9f522448 | -7.11247 | -43.37362 | 2025-06-28 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5e7fd33c-874d-38ca-86fd-92eff13165b9 | -7.21047 | -44.89829 | 2025-06-28 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef7bfbca-ecf7-3cb1-94c5-adbf0cd7dd10 | -7.21606 | -43.08159 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 16246ea9-ceac-364b-8af3-82c051497236 | -8.07105 | -43.13419 | 2025-06-28 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f3433e54-e317-3836-8b7c-26e21fe727c9 | -6.06496 | -48.12611 | 2025-06-28 04:27:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a21bd80-032b-375e-886a-dd155ce3b1ea | -3.87449 | -54.22868 | 2025-06-28 04:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 39237d8a-6950-3b48-8c85-8f1987b93ab0 | -4.3737 | -48.07821 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ae124ec-2a88-3c52-ba89-69c88b693550 | -6.90693 | -43.96832 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83bbb8c2-7428-3adb-97fc-9ec90b885f7a | -4.5444 | -48.02356 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 60186ea0-b9dd-385d-9092-6c9d627b7bb6 | -8.85628 | -47.95452 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 793cea6f-2061-3d99-9473-16eabb974491 | -7.22276 | -43.08704 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 64d5b126-6f87-3b5d-9215-606b2fbeb122 | -7.88463 | -46.32185 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5760e615-b246-3b2b-9f51-39c12e7179e1 | -6.90626 | -43.99618 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e364624-7cf3-363c-b6ba-2a328b7f1e34 | -8.67755 | -48.80013 | 2025-06-28 04:27:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8bd1e7a-dad2-3164-a357-c62719088ca4 | -8.04254 | -47.64826 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67e9bc08-fd88-3294-b907-e5cff120747f | -6.06436 | -48.12983 | 2025-06-28 04:27:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ecf1a80-5d29-3351-99cb-4b8218337fe3 | -5.44037 | -46.56463 | 2025-06-28 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e09cbba-e1a4-3e48-879b-cb2e8daf9d46 | -6.94759 | -42.88658 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 62bd4a1d-a5c1-3a1c-9ae9-af475b929e87 | -9.11162 | -49.48698 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| db8cc12f-aaa9-3d13-ac29-e42689bc28f9 | -5.46267 | -43.07743 | 2025-06-28 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 540e635f-60b0-384a-b013-299b7bfa4ab0 | -8.03362 | -47.63956 | 2025-06-28 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1d6c321-58de-3433-9860-85768efb1be9 | -9.73833 | -48.33594 | 2025-06-28 04:27:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb2d0cf4-a81e-3962-bc9e-991119fabc20 | -9.11291 | -49.47908 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2db744e2-937b-3c9b-bacd-000c5387c1de | -7.54776 | -45.8316 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5b8be7e-01f4-3cf4-94e7-fe7c155d4f32 | -6.89813 | -43.97898 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64dd820d-0e7e-34fb-8b66-c68467068114 | -5.86618 | -46.48256 | 2025-06-28 04:27:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6e055bb-8e02-394d-8654-47892f623c38 | -8.00184 | -44.78753 | 2025-06-28 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e672b68-f664-3e4c-8124-066e3396432f | -7.55055 | -45.83564 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d8ad619-019b-3d87-bbf1-3fb90f94c25d | -8.85056 | -47.50599 | 2025-06-28 04:27:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8de7dbf1-9aec-3557-a96e-8a35774ddc9b | -6.71407 | -44.40463 | 2025-06-28 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ef89a42-4663-356f-aa8f-5ed0f5a3a9e1 | -9.11579 | -49.4836 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 80271890-bc8a-3eae-ba44-09241d654471 | -4.37494 | -48.07058 | 2025-06-28 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fff1ceb6-725b-391d-8884-35ddeb9d2069 | -9.1148 | -49.48703 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 896b8f28-6349-391d-99a8-c8d974c58465 | -9.11766 | -49.49154 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8bb0c4c9-aaef-30d6-83f7-5d8a5ff1f362 | -7.88408 | -46.32534 | 2025-06-28 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4dd6ac2-ddeb-343f-b656-4a226942a0e6 | -6.45037 | -44.57719 | 2025-06-28 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ab22442-690a-3df3-8484-ab98de7854d3 | -6.74015 | -47.22272 | 2025-06-28 04:27:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dfe7076-6dfb-367a-9698-c4176d714620 | -4.12668 | -43.069 | 2025-06-28 04:27:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e90bf11-7f11-38eb-9fa4-7a30d1f4e586 | -7.34156 | -45.31411 | 2025-06-28 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46b2a443-2ca3-3e60-825b-4f513dbe71c7 | -9.44142 | -47.96095 | 2025-06-28 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a77caa9-e7a5-3aa3-903e-039980728392 | -7.11184 | -43.37777 | 2025-06-28 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e22737f7-06a3-3ab5-9a6a-0800f0c6905f | -7.38968 | -44.5508 | 2025-06-28 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b8987d5-5a8a-3eec-a6fb-91ae21085376 | -6.91446 | -43.98945 | 2025-06-28 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 583c67ad-4dcc-3b09-a7f0-eb2c0a6f1b96 | -7.15338 | -43.37909 | 2025-06-28 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2711c172-9814-3ec0-9f08-b68bde6a3550 | -9.11701 | -49.49548 | 2025-06-28 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f499eea4-7878-3a49-89c3-7ed5d5f5cf93 | -9.08785 | -47.96947 | 2025-06-28 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 742d8441-d7ff-3c12-a392-a0d5ecb61317 | -6.95541 | -42.91006 | 2025-06-28 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README15.md)
