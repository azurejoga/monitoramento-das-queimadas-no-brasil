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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d719b786-edee-3dc4-b4ab-4eff41c2b0f8 | -8.93489 | -44.24788 | 2024-12-07 04:10:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a60abcc0-00e1-35ef-8d0a-f78153998e41 | -8.27825 | -48.02552 | 2024-12-07 04:10:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91b01384-8a86-3c32-875f-f534048f1005 | -11.46242 | -43.24682 | 2024-12-07 04:10:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d01c8ec2-52b7-38fa-bd9a-1c104669b74b | -12.23653 | -52.45745 | 2024-12-07 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b3897c3-13ce-3c56-a8a6-a20a3c79658d | -12.28668 | -45.49475 | 2024-12-07 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c033c141-568d-3179-83be-92328fa2a405 | -12.85336 | -51.94096 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b726b96d-f699-3eec-8efe-1f4a82e78e9a | -12.4123 | -49.68225 | 2024-12-07 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27b2cf9e-7e8e-3535-9889-f0e18dee090f | -8.93831 | -44.24842 | 2024-12-07 04:10:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6d8cd36d-ed42-391a-890a-c4bb21718cd3 | -12.86292 | -51.946 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fb9c77e-a64e-363b-9848-637291d7a256 | -12.23587 | -52.46083 | 2024-12-07 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0d2b1b8-1e33-36e1-a975-80602ed5aa46 | -13.619 | -44.08666 | 2024-12-07 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24667146-c190-352b-9d6a-ad410b962ae6 | -12.27815 | -49.49556 | 2024-12-07 04:10:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 505d0946-3f4c-3686-be80-e43b146b891f | -12.65702 | -46.57533 | 2024-12-07 04:10:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ccfb8d8-037f-3632-acee-3cfb7b8bc965 | -11.00634 | -44.34008 | 2024-12-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3d5334e-4672-38c8-8e62-e2e7afd35cfe | -11.73615 | -54.30964 | 2024-12-07 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c52bf2ab-74af-37aa-9fcb-44e1c5dbddaa | -10.98195 | -44.73154 | 2024-12-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 426cb0ce-09e4-36d0-aa6a-88e74ec6146b | -12.40456 | -46.60101 | 2024-12-07 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc90c983-f833-345a-8063-33c0937c0fbe | -12.86025 | -51.94274 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7805c18f-5abf-310c-9d69-c48dea015405 | -11.11089 | -43.34088 | 2024-12-07 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fe744ff1-141c-3642-af57-0bf32df18887 | -10.66167 | -44.49519 | 2024-12-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 19c714b4-f9b9-32d1-8b10-05b948006962 | -9.10284 | -43.19608 | 2024-12-07 04:10:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 564203ef-b399-3590-9217-619df7c85b21 | -8.27687 | -48.03348 | 2024-12-07 04:10:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 714ea3fa-e996-3bd8-a9e2-5170a78513ed | -10.84877 | -44.4049 | 2024-12-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ecccaaeb-f19d-320b-91c4-6ca93580f114 | -14.81882 | -40.45985 | 2024-12-07 04:10:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7a96d659-146b-33fb-bf01-e3a71a3646f7 | -10.03733 | -50.5797 | 2024-12-07 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d417fd20-9d85-3ca8-9b0e-cdcd43837610 | -12.53603 | -49.27193 | 2024-12-07 04:10:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0694839-b8bc-3bb5-9ae8-35df11a7a00c | -12.85396 | -51.9379 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4b9b20f-6c61-3712-985d-8c3ceb871d92 | -12.28603 | -45.49866 | 2024-12-07 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 503baec0-5250-3099-a05f-131c714d41c6 | -11.06609 | -45.38225 | 2024-12-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e162c5a3-c0ef-3018-a23b-9e22b1fd4240 | -12.86527 | -51.93393 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a1c35aa-cdea-3f71-9794-1e214717f6e1 | -12.91543 | -49.68207 | 2024-12-07 04:10:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3875b2c6-77ee-3f2f-ac53-b51e5b8df494 | -8.93892 | -44.24468 | 2024-12-07 04:10:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 88148715-9a89-37fc-a12d-62910b70539a | -10.66507 | -44.49575 | 2024-12-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa37dde4-e00e-3648-8c91-6cd70807e27a | -13.43814 | -49.65163 | 2024-12-07 04:10:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adf4fa7b-88f8-3db1-bcfa-da2d414c24cc | -8.94173 | -44.24897 | 2024-12-07 04:10:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 678ff8b2-f61c-335d-a2fc-45afdc2ce866 | -12.53529 | -49.27605 | 2024-12-07 04:10:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22b99ce3-38e2-3ecc-abe8-e0cc8474bab3 | -8.9355 | -44.24414 | 2024-12-07 04:10:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8603b3e0-efbe-3788-a363-545080d32f9e | -11.06324 | -45.37768 | 2024-12-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 559fc844-79ec-3d78-8ccf-cc590b390dd5 | -11.99478 | -47.16819 | 2024-12-07 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8ddc42d-bb49-3a0f-9025-fda5d31ee903 | -12.46155 | -46.93544 | 2024-12-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96ab4dac-4d60-3b76-9154-3a3aef750358 | -12.28538 | -45.50256 | 2024-12-07 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5641ecc-ecc2-3d52-867f-e9babbecc46e | -7.08619 | -45.20658 | 2024-12-07 04:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76cb04eb-8752-384f-a0c0-9c9648ec12f5 | -12.8641 | -51.93991 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e02ee76-c903-34be-9abe-d7fb5365e57e | -8.28111 | -48.03416 | 2024-12-07 04:10:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e441caa1-6950-3736-a054-904a644eddc2 | -11.41357 | -51.27556 | 2024-12-07 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71dfed9f-9b9f-3775-b93d-adbbc4622b24 | -12.92652 | -48.63435 | 2024-12-07 04:10:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e336899e-0e01-3dd7-b93f-cb219543caf2 | -12.86469 | -51.93689 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58f11165-db1a-387f-aabb-a11700250ef6 | -7.0915 | -45.20245 | 2024-12-07 04:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 120b94e5-a2bc-3f1b-aab2-e4aa60aa0114 | -9.19245 | -44.35021 | 2024-12-07 04:10:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ce075f9-8934-36c5-9c34-8a1acfb92190 | -12.28885 | -45.50317 | 2024-12-07 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 86882240-30f4-3b34-8d5d-7b360446ddf1 | -11.4265 | -37.71677 | 2024-12-07 04:10:00 | NOAA-21 | CRISTINÁPOLIS | SERGIPE | Brasil | 2801702 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c3afe76e-17c3-3c4b-9691-ec0e01d7db35 | -12.49561 | -46.35122 | 2024-12-07 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dce5557e-8800-39c1-87a0-80bb347b0d62 | -13.40973 | -41.33132 | 2024-12-07 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| dd7de256-f478-3946-a069-ce4ab2e51177 | -12.85844 | -51.94194 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0df9e9b-4f2d-3f42-bb47-b80dced8a239 | -8.03151 | -47.68853 | 2024-12-07 04:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83d74ba7-6695-3986-989b-92b642d8ea39 | -11.73363 | -54.31379 | 2024-12-07 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df167c59-7a37-3d65-95e5-004ca4d731b2 | -12.40441 | -46.6025 | 2024-12-07 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 207e12f4-c8c1-34d8-9d98-8d1547cdc84d | -9.37197 | -43.27932 | 2024-12-07 04:10:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d8bf5c5-d88e-31df-bd17-7a6490fcb185 | -7.16887 | -43.50168 | 2024-12-07 04:10:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39a743d1-7c18-3a1a-838a-9d24fcf566aa | -11.05975 | -45.37708 | 2024-12-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d17b665c-713a-3f02-9770-74de8327cbb7 | -11.06389 | -45.37373 | 2024-12-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 839da76d-8bc6-3d88-b235-bb06f4281d0e | -12.4629 | -46.93896 | 2024-12-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b0c767b-8b60-30f1-8067-ecaccca19a64 | -12.63856 | -47.54415 | 2024-12-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f60dbff4-c099-37c7-bc23-68cf5e33637a | -10.6357 | -47.46451 | 2024-12-07 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16ee85b8-7a21-3124-9b89-d19dcbb527c0 | -12.20308 | -47.15725 | 2024-12-07 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86554991-ab4d-329a-bf01-b4d2f7c23ffe | -8.29338 | -42.76405 | 2024-12-07 04:10:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e25591d-3ca8-37f1-875d-c8968182e539 | -12.54384 | -49.27771 | 2024-12-07 04:10:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d6bb918-fb9b-396c-ab69-4b28c53721cc | -11.20563 | -53.82482 | 2024-12-07 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5789908f-4e72-3c06-a461-e57e6128e11d | -11.20445 | -53.82034 | 2024-12-07 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9e4fbbc-90da-347f-a3f0-2dc3eabc517e | -13.30324 | -43.69553 | 2024-12-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fe50606-16b5-34cc-809b-d19301a7cd3c | -12.85181 | -51.93165 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9cf0ed3-f6f8-3204-80ac-b9a53d5c629e | -7.17334 | -44.9973 | 2024-12-07 04:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc9ac894-d4d4-3496-99bf-23526628793c | -8.93208 | -44.24359 | 2024-12-07 04:10:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 603e9ebb-5830-3421-8803-a00e1dfdcdd2 | -13.41316 | -41.33182 | 2024-12-07 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 779e17ae-3a2c-3c44-aa08-9e53c37414bc | -12.40789 | -49.68144 | 2024-12-07 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c06e3b3-7f0d-31fe-8262-a52f788e275c | -12.86195 | -51.93367 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 28ad4c47-b861-3b8b-b50f-4cd2f595da3e | -6.7537 | -46.51997 | 2024-12-07 04:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e00a0672-4aa2-345f-a447-4abb09ae47ba | -13.40917 | -41.33511 | 2024-12-07 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4ef28450-b9df-3413-aa38-652480ef2066 | -14.10764 | -43.18207 | 2024-12-07 04:10:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 63cf07d4-4d86-36d5-ba42-5810747410d1 | -12.49992 | -46.34758 | 2024-12-07 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9c4164c-0a46-3a10-9359-e192e27faf9a | -11.36791 | -43.80002 | 2024-12-07 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d49c8d9f-82a6-39fb-a8dc-96b780e4422d | -10.49178 | -47.38781 | 2024-12-07 04:10:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 026bc4b3-8c0d-356c-8605-449caf170042 | -12.53957 | -49.27687 | 2024-12-07 04:10:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dc8b4d9-921f-36db-ad96-a90da6bbf74b | -12.86139 | -51.93666 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 883733df-9b13-3568-90bd-8b56448ef5fe | -11.0626 | -45.38165 | 2024-12-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 851bb36c-48de-32b7-ada4-4ea6defd88c6 | -13.41029 | -41.32752 | 2024-12-07 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 8fbc58e2-c0f9-33a8-8d63-c8e1213fa5de | -12.86351 | -51.94294 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5657e0a-8141-39b9-9aaf-0c958e015c6f | -12.48186 | -46.27935 | 2024-12-07 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a817b25-03e2-384a-943b-325cbc94c847 | -13.02686 | -42.01014 | 2024-12-07 04:10:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 146b999f-ca55-333c-9175-c929a2fa18f0 | -8.90637 | -35.23296 | 2024-12-07 04:10:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 11b8deed-ce33-3c7a-8fe3-18aafcec4428 | -12.2895 | -45.49926 | 2024-12-07 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6169a822-0ed3-39fa-8c64-55cb11153de1 | -12.69694 | -46.76184 | 2024-12-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a021640-5ca7-38ca-89ec-0d4548ed31f2 | -7.08551 | -45.21082 | 2024-12-07 04:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c94779f-0942-3075-802a-c83585bd95bb | -7.08647 | -45.2103 | 2024-12-07 04:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 551e55e7-31b9-3022-b0e6-5d44e83bfd62 | -10.5435 | -44.68352 | 2024-12-07 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a1ac72b-b94e-3168-83a2-29ae5bae4d61 | -14.88871 | -41.50926 | 2024-12-07 04:10:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3b49f3e5-8c40-32e4-9942-343f94a01368 | -11.16238 | -43.57339 | 2024-12-07 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 059afd9b-c744-315f-8de2-e2bb769d7bca | -9.22245 | -50.69223 | 2024-12-07 04:10:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0fdffe3-1ebd-3be2-a02d-d4fbb837c25f | -12.85124 | -51.93467 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc855ddf-0fda-3a76-9fd5-0c283391c5e1 | -10.63963 | -47.46521 | 2024-12-07 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README6.md)
