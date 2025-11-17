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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d86ca6eb-974c-3cec-962c-7e934c4d1dab | -5.5878 | -45.1865 | 2025-11-17 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| bdb6b88f-e618-3d6c-aa5f-d436cef65601 | -9.9758 | -44.9204 | 2025-11-17 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 34d6e9d6-914e-31c3-92ee-239fff344277 | -9.9775 | -44.8052 | 2025-11-17 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 2974f037-6f02-3334-8686-7c60ef6bdb0f | -10.0917 | -44.7907 | 2025-11-17 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 11c14453-bf8f-313e-917e-ebaee230a329 | -3.3415 | -43.4829 | 2025-11-17 13:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4275ac57-eb0a-3a97-8252-4e1e8c17a7d7 | -5.7616 | -42.4906 | 2025-11-17 13:50:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| bfc6695a-c1b7-39ed-8109-eb1973c28354 | -6.6875 | -42.0296 | 2025-11-17 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 49.5 |
| c9727c82-e8cb-380a-a62b-dde5527f3e20 | -7.442 | -45.2184 | 2025-11-17 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| af56ded3-d06a-34f8-84a8-f47702f3848e | -3.5833 | -43.6108 | 2025-11-17 13:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 90407491-8a41-3dec-9de4-dc2c2ae5d2e1 | -8.3202 | -44.2142 | 2025-11-17 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| add382a3-58d1-38e1-81c7-f8119c2ce222 | -8.3016 | -44.1931 | 2025-11-17 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 14a3fcee-7f34-391b-a9f5-2b517dbe7462 | -9.4645 | -44.868 | 2025-11-17 13:50:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| d4fdfb6a-9932-3b10-8676-192d7be7b86d | -12.4154 | -43.1826 | 2025-11-17 14:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| c6cf8a01-f46e-3cf2-9a0c-bf8c8c6ae8f0 | -9.9567 | -44.9228 | 2025-11-17 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 00d4bd7c-0d15-3078-a788-7fbfa01b5123 | -4.2531 | -46.8277 | 2025-11-17 14:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 46120413-7e7f-3384-b0f4-bf6055761ee4 | -7.3695 | -43.3352 | 2025-11-17 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e976b043-98c1-3753-8b47-a6593e46a307 | -3.3909 | -44.72 | 2025-11-17 14:00:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e106f434-9639-3d7a-9209-e33b4d6248ca | -11.6947 | -44.7314 | 2025-11-17 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 9a6fb9d3-525d-3cdc-a3c0-00d48ede02db | -9.0217 | -45.4217 | 2025-11-17 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 1691514f-91f5-39c0-ba97-5a4b74262f63 | -3.7293 | -44.1568 | 2025-11-17 14:00:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| f09b7f0c-18d8-323e-8a25-d2aa660dfb6d | -10.0917 | -44.7907 | 2025-11-17 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 7340c415-16dc-31c8-8783-2ca2a29d3161 | -3.5833 | -43.6108 | 2025-11-17 14:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9cc00c05-8dad-344e-91b2-775261a8b2ca | -8.0573 | -45.6583 | 2025-11-17 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| bcd2fffc-05e5-3c50-9306-7f78918ad62e | -3.3601 | -43.5053 | 2025-11-17 14:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c67a6028-7cdc-3d78-bf64-90f8089120cf | -2.4201 | -45.7015 | 2025-11-17 14:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 53032121-8ba6-31cb-b6c1-1f59221773ab | -3.3602 | -43.4821 | 2025-11-17 14:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 41d45d62-9305-3413-b7a9-6508e5aec9c4 | -4.1027 | -47.1206 | 2025-11-17 14:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| dc435064-16a4-348c-a1b6-287379fc207a | -4.2486 | -44.5876 | 2025-11-17 14:00:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3fe4947a-1d9d-3907-8400-bfdf57cd396b | -3.2304 | -43.3486 | 2025-11-17 14:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b469b331-1999-3e95-bf08-8a501d1da429 | -9.04 | -45.4651 | 2025-11-17 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 131.9 |
| d7f748de-9089-3c56-a5ab-df55ed3269d3 | -3.9959 | -43.2651 | 2025-11-17 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e1c31b64-4f78-30ad-bdee-880044639d67 | -3.2116 | -43.3726 | 2025-11-17 14:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| e2ea9f10-c5d5-30bc-847f-1c01552cce4b | -5.5878 | -45.1865 | 2025-11-17 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 11c22945-10ae-3d37-851f-6a21cb7e2ad4 | -3.4281 | -44.7412 | 2025-11-17 14:00:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1a30c0e9-2d43-3283-a9a4-bc130a865270 | -4.3434 | -44.354 | 2025-11-17 14:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| d9d59fa1-62f5-3cf0-8962-d05a10559286 | -3.9554 | -43.7773 | 2025-11-17 14:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 4f5b7929-18b8-3492-b2f1-c7bd5862670b | -3.2117 | -43.3494 | 2025-11-17 14:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| c060aff2-e6cf-3541-97ed-a4b3f0f289cc | -9.6236 | -44.3644 | 2025-11-17 14:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 30b56fb6-917c-3661-b9ad-e9a9eef8ce11 | -8.3049 | -43.9377 | 2025-11-17 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 45580625-a9e4-3382-8dbe-7f12284fe5a5 | -11.7996 | -45.2935 | 2025-11-17 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 0e77ff69-1b61-3802-bedc-31ad8d3555e9 | -11.4136 | -43.32 | 2025-11-17 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 4e084d6e-b9e2-3e0c-9d36-d14779aefe8c | -9.157 | -48.0615 | 2025-11-17 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 13d0c871-2f2f-3705-bcdf-8cc90335d791 | -3.9895 | -44.2813 | 2025-11-17 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 37e40ed1-f326-34c3-955c-3faa689c9139 | -11.2045 | -46.6047 | 2025-11-17 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 52443c9a-a540-317f-8541-9a288f5a1ebb | -9.9779 | -44.7821 | 2025-11-17 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 248.5 |
| 04cc8db4-e682-36fd-8f60-6efceac86675 | -3.9894 | -44.3042 | 2025-11-17 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 6314faf2-438f-3371-ab46-d596c22e8330 | -12.3961 | -43.1858 | 2025-11-17 14:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a8e083c6-511b-31da-970c-ef40ff052326 | -11.676 | -44.711 | 2025-11-17 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 200.6 |
| e85355e0-4b24-3dc4-a558-e7ce6366d370 | -10.1111 | -44.7652 | 2025-11-17 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| fb134e15-9aa2-31b7-9a2f-d56190319492 | -3.3414 | -43.5061 | 2025-11-17 14:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6c3e3b8d-ef9e-3132-90c7-01391f34fa68 | -9.0214 | -45.4445 | 2025-11-17 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 376ef151-d049-3919-b539-a8c647986409 | -5.7614 | -42.5142 | 2025-11-17 14:00:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 259f06c2-8d97-327b-84c9-e2f12ac2ef14 | -7.442 | -45.2184 | 2025-11-17 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 15083b55-7041-314b-88fa-6b4b8a5c3270 | -10.6464 | -44.6022 | 2025-11-17 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 78b28f27-7f10-344b-9f5f-a4220b9a7f86 | -8.3046 | -43.961 | 2025-11-17 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 207.6 |
| d032169e-9e81-3fc4-b3ff-22c6f271525e | -10.092 | -44.7676 | 2025-11-17 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 152.8 |
| dd2a07f1-828c-3d24-b0bd-7b87f428322b | -7.7135 | -42.9478 | 2025-11-17 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 234ce0fa-3df1-367e-9e04-493806d7ea77 | -9.0327 | -46.0091 | 2025-11-17 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e880d0cc-715a-3b19-8473-709725dec544 | -6.7013 | -40.7962 | 2025-11-17 14:00:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 127.6 |
| 91fcef52-df69-3de7-9543-924284952208 | -12.4347 | -43.1793 | 2025-11-17 14:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 6a5d2a38-9bb8-3e86-87ad-ca8abfa03a91 | -3.4598 | -42.3304 | 2025-11-17 14:00:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 749e15cf-3933-36af-b8e7-253443d6b3ba | -9.9775 | -44.8052 | 2025-11-17 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 0a6bdaae-a6cc-3b37-960f-bbd0f26b848a | -7.094 | -42.7272 | 2025-11-17 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 541693b4-e018-3aa6-940e-09dd5b73c66c | -6.1789 | -48.0929 | 2025-11-17 14:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a2d61f8f-0a5e-3a2a-99a6-07b40b3efe29 | -5.7596 | -42.7033 | 2025-11-17 14:00:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 73f7264a-75ea-3adf-a45e-46c33ace7906 | -3.8102 | -40.1418 | 2025-11-17 14:00:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 131.2 |
| 35c48966-7fde-329b-b8eb-3770b9e3e082 | -1.3376 | -49.1459 | 2025-11-17 14:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b2ade6d5-0490-3b0b-b88c-1ee6c1da4dd6 | -3.6701 | -44.7303 | 2025-11-17 14:00:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 65bec08e-2ae8-3c12-889d-743f71a9c8f7 | -11.6755 | -44.7342 | 2025-11-17 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 8a62c72b-0bed-3fa5-ab90-6a82f706dee9 | -3.9709 | -44.2823 | 2025-11-17 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8e2b5058-5a53-3ff2-9392-887f3a26a715 | -9.0022 | -45.4693 | 2025-11-17 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| ce334314-df40-3d14-b067-9878146a24ff | -7.6237 | -42.5788 | 2025-11-17 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 860f6f58-458d-3a4f-999b-dff9bac3bad8 | -9.0211 | -45.4672 | 2025-11-17 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 321.9 |
| 28e4d2f5-aaa3-3fb8-9488-b0a6bec165a1 | -6.1791 | -48.0712 | 2025-11-17 14:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1c77d61c-c651-36a2-a3d5-6844427d8b0f | -10.3939 | -44.9129 | 2025-11-17 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| c24a63f1-5483-357d-8d71-6fa37e177d75 | -4.107 | -46.3928 | 2025-11-17 14:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c8d65e9b-7dfb-3f6a-8263-82d042179f91 | -7.9714 | -50.0013 | 2025-11-17 14:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 233e7de3-a6aa-36c3-964a-4fdbe53854f8 | -9.6232 | -44.3876 | 2025-11-17 14:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| cd026f38-f216-3750-92a2-f22fca0a47ae | -9.9972 | -44.7566 | 2025-11-17 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 3287a10a-faca-353e-b666-e7d685826682 | -9.9758 | -44.9204 | 2025-11-17 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 910d8b0e-6e49-32d9-903d-95b81a40c788 | -10.0917 | -44.7907 | 2025-11-17 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 30f9d418-521a-3948-bf2d-10fb8f47160f | -12.7189 | -45.4074 | 2025-11-17 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| e9ac362e-4651-32de-84f4-e812ee73a326 | -1.1899 | -49.1904 | 2025-11-17 14:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| bb7f3427-8534-37ab-8508-97d23635285e | -10.7889 | -47.6392 | 2025-11-17 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 5e89f768-669e-3800-8695-4d3ffad5d562 | -9.6236 | -44.3644 | 2025-11-17 14:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| f48b7a1a-4279-30f1-8f80-c51445df5d19 | -8.6814 | -45.4587 | 2025-11-17 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| da7b6688-63e1-3430-aebd-b7a6e7b8d26d | -4.2695 | -44.2436 | 2025-11-17 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 06311822-96d8-3ee5-afe5-6d40a3773c21 | -8.9833 | -45.4714 | 2025-11-17 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| d11ca737-256d-375f-8500-2f3da59e2f3e | -4.2486 | -44.5876 | 2025-11-17 14:10:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 68c808ce-5db1-32e3-a784-cd6588322e08 | -8.3049 | -43.9377 | 2025-11-17 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 228.7 |
| 8cc784f5-dada-32f8-8419-1c1dea39dba1 | -11.676 | -44.711 | 2025-11-17 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 268.0 |
| 07bfdaba-c27d-362e-b98c-024915ecbc9f | -9.9972 | -44.7566 | 2025-11-17 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 53dc24d1-9a87-36d8-aacd-7edaea74ad46 | -10.092 | -44.7676 | 2025-11-17 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 87a98e7b-4e0f-3b08-810d-931780ab5e63 | -8.3046 | -43.961 | 2025-11-17 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 210.3 |
| fa0c1040-f96f-3754-96df-d7ff636a7d4c | -13.2938 | -43.6737 | 2025-11-17 14:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| a7d2c9e1-c73d-3239-a835-d501e817ea28 | -3.6515 | -44.7312 | 2025-11-17 14:10:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 4daa472c-d7bd-3bcd-a7de-80c1050a4df5 | -8.0573 | -45.6583 | 2025-11-17 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| d16c872f-5f7d-31b8-8d88-7c0e469f5c82 | -8.1212 | -43.5382 | 2025-11-17 14:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8f23a8af-e0e5-3854-a0c7-8e5627607692 | -8.9836 | -45.4486 | 2025-11-17 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 302e7f20-fecd-3fc9-ae4e-49e6ce8cb709 | -3.3841 | -46.0694 | 2025-11-17 14:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |


[Clique aqui para ver as próximas entradas](README56.md)
