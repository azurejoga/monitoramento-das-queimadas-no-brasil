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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1102b13e-3b64-3caa-bdae-8a1b8582651a | -10.97402 | -45.10878 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 367c9a05-3850-3bf9-8cba-343fc166c93a | -8.74077 | -45.22356 | 2025-09-11 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 1fa3935c-a4a1-3b5f-b054-04fd55637811 | -8.87775 | -49.55162 | 2025-09-11 11:57:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 72ba6b9f-3dc4-376b-a1da-8a45cbb6a61f | -11.77817 | -46.50738 | 2025-09-11 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 9dc82dea-0404-35ad-b712-33e7dfa6ecbd | -7.0837 | -45.19747 | 2025-09-11 11:57:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1314e5cc-c7a2-3977-ac6d-f855d4992a2d | -9.00778 | -46.08004 | 2025-09-11 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 284849c8-2041-3783-bfa7-b8b9164829cf | -8.18675 | -42.41748 | 2025-09-11 11:57:00 | TERRA_M-M | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| c87d9bec-56c0-3a2b-b46f-ffd2d826cbf3 | -11.98634 | -47.56599 | 2025-09-11 11:57:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 62d6ae76-e02c-311e-859e-93c275eb0d84 | -8.17405 | -46.10462 | 2025-09-11 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 6dda4f74-c66c-38d8-a4a4-f4af488a983e | -6.43329 | -44.49381 | 2025-09-11 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 2fdfa31b-e92c-3a54-a885-48211bd4aca4 | -11.71894 | -46.5044 | 2025-09-11 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 0c045256-da6c-379b-b577-f9994bc5d807 | -11.42278 | -43.56056 | 2025-09-11 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| f5cb7777-9852-35d1-b61e-bf93b9eb326d | -10.20265 | -46.83225 | 2025-09-11 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| af6db578-220a-3f29-8121-46983c7f7a84 | -11.39129 | -45.58581 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 93ce16f6-c360-346c-b6f0-cd34b9bb600c | -7.27489 | -44.62345 | 2025-09-11 11:57:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 25167a03-7191-308b-bef4-db1b199492e2 | -9.06996 | -47.07821 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 64e333db-e016-3d10-9a59-0a3a2cbf87fb | -8.16525 | -46.08942 | 2025-09-11 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4b0c129a-2f7f-3568-b8ab-b9bd8623bcb3 | -11.02133 | -45.06016 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 7fc7be20-fcfb-3937-bee8-4062924a05cc | -8.729 | -46.68061 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| a23094a3-4581-36f9-9333-f5fdb11c2741 | -8.75091 | -45.22503 | 2025-09-11 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 8232fa3f-0c90-3fb8-a383-6220c68a52d3 | -12.2441 | -46.75205 | 2025-09-11 11:57:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2f00851f-ca12-3440-9233-344891efb9a3 | -10.18664 | -46.20721 | 2025-09-11 11:57:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 224.9 |
| 4ea3fac5-be3e-3cb2-a60c-982e18018351 | -5.54964 | -43.04427 | 2025-09-11 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cc312702-7694-3d6b-9c57-a4bbe72ab385 | -6.66075 | -42.06535 | 2025-09-11 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| e05915cc-0ae8-3996-8cb3-446678d2b483 | -8.72661 | -46.69575 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 9f08d205-a7f7-3c4a-9a30-9d290e76db9f | -7.98396 | -43.66332 | 2025-09-11 11:57:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5eb5ef8e-a739-3dd6-8a80-cc94e2b56c7e | -8.08487 | -45.56043 | 2025-09-11 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 288e35ac-d326-30eb-962d-c2dcea2910d3 | -6.48424 | -41.74845 | 2025-09-11 11:57:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| f3ef9f02-c36b-36b8-9e7a-45c47dbe4205 | -7.22737 | -43.97986 | 2025-09-11 11:57:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1ed7d237-e13b-35ea-a994-52d039dcbd55 | -6.24802 | -43.48442 | 2025-09-11 11:57:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f3001af7-289f-3b67-b10b-9a4c3cff4c7f | -10.31958 | -48.80165 | 2025-09-11 11:57:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| d199d2e8-a156-3e7e-b26c-267419243be9 | -9.06705 | -45.70012 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 251291f2-a606-31a8-963e-fd343f06429a | -12.25498 | -42.15248 | 2025-09-11 11:57:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 80aec2a2-96ef-34dd-ba95-44775b7ee6ad | -11.63874 | -41.74697 | 2025-09-11 11:57:00 | TERRA_M-M | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 019fe5c8-b077-39ff-ac74-13a169f5c34a | -6.31479 | -43.42228 | 2025-09-11 11:57:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 5ff0fd25-7ffd-3f62-811e-1134a00d3412 | -5.57584 | -42.9288 | 2025-09-11 11:57:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 5f26a39c-3366-34ac-aedf-9436b9109d77 | -5.31287 | -43.63383 | 2025-09-11 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fcfb15d5-d7ba-3c3e-9002-255b57a61228 | -11.0993 | -51.32106 | 2025-09-11 11:57:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 6884ff4d-0004-325b-a371-bd42ff092509 | -7.90905 | -46.24942 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| ebbb03c1-029f-3db1-8bc9-805a0895d146 | -11.41654 | -43.54061 | 2025-09-11 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6e343a74-c296-3dac-afbe-f45e738239b3 | -7.90684 | -46.26381 | 2025-09-11 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| c9f969f2-b572-34cd-a163-b152ed7dc6fe | -11.99524 | -47.58334 | 2025-09-11 11:57:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| a5a09df4-ae99-3d77-ac49-79b7d7e6ff9e | -11.71688 | -46.51746 | 2025-09-11 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| fde8e15a-4bb2-3987-acdf-e41d70ce77a9 | -9.01728 | -49.52878 | 2025-09-11 11:57:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| dcd95e22-e479-3851-8bfd-98f7f265f0d2 | -6.31965 | -43.81631 | 2025-09-11 11:57:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 001dafdc-c1ce-3aea-bced-13450b402cf0 | -11.34195 | -46.48568 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| d7075f72-02ca-3889-8809-4b5fe0c25ed9 | -8.52494 | -45.69744 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 7d55ab90-3ec6-376b-8ee3-49945049d8c4 | -8.50989 | -45.6558 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 1e233787-814d-3979-9d2c-ffb439174b26 | -7.94159 | -37.73436 | 2025-09-11 11:57:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 6d6c15cf-c6a7-3748-851e-192242985967 | -11.36135 | -46.57059 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| afdc8213-c8db-35ac-a714-5d1d349f28c8 | -8.34589 | -45.40595 | 2025-09-11 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3ec1cbed-d759-384e-811b-59fe626b43f2 | -8.64555 | -45.72221 | 2025-09-11 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f6b24100-d6ec-36c5-8e78-0176ab35a10b | -11.38109 | -43.52932 | 2025-09-11 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b6cbc2b0-e11e-35b6-b403-d980158dea08 | -10.97068 | -45.11348 | 2025-09-11 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 315c5635-9a16-30d2-bb05-1f52d84c0f6c | -9.13662 | -47.0146 | 2025-09-11 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a5c66278-9a8b-36fe-aa9c-00aea439fe0f | -6.66595 | -43.96777 | 2025-09-11 11:57:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 320d673a-e699-38a3-8b8e-835a7a5b2c7e | -6.85766 | -47.86353 | 2025-09-11 11:57:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 251a0f3e-83c0-3284-99a0-d98fa2a1a9b7 | -9.13796 | -46.19048 | 2025-09-11 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c23f5da6-fe60-3102-bd39-334a74f80340 | -10.18874 | -46.19387 | 2025-09-11 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| c05b7c74-a1bc-37aa-a428-df3455ef1fae | -6.56754 | -44.21014 | 2025-09-11 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 97eb1372-ccef-363c-b15e-17a2cc713a4a | -6.66752 | -43.95725 | 2025-09-11 11:57:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 1f83a2fb-c4b9-3744-81a6-bb12bff124ab | -14.5128 | -53.9158 | 2025-09-11 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| b15180ef-cfef-3e98-b379-19c40d5c56aa | -11.4285 | -43.5544 | 2025-09-11 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 75bde94b-e793-3795-9ffa-5aae079fa615 | -10.1844 | -46.1927 | 2025-09-11 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 1c6d0db8-9623-314c-8678-2cfa93a27353 | -11.7211 | -46.5127 | 2025-09-11 12:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 99825f97-7556-3115-bf73-555cba97d0d5 | -11.374 | -45.5836 | 2025-09-11 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 432add45-08bf-3ff9-b43e-ce07e08c4a5e | -13.5089 | -51.7877 | 2025-09-11 12:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 6860f776-dc6e-3e91-a9d7-e8e0d9f134b5 | -11.3931 | -45.581 | 2025-09-11 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 0e1a9330-db1a-3317-bcf2-863474b97fb0 | -14.7525 | -46.2876 | 2025-09-11 12:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b85fd186-290f-3765-bab2-07ec5938ad8f | -15.1367 | -52.4466 | 2025-09-11 12:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e67b9b37-92af-318a-8811-514c358ca34c | -15.1565 | -52.4226 | 2025-09-11 12:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 1998ed73-42d4-31eb-8a70-206066ba7b23 | -15.1561 | -52.4439 | 2025-09-11 12:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 05aa8133-44c0-3ad8-ab04-1edb443003ef | -15.118 | -52.4066 | 2025-09-11 12:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| bfbcac2b-1cbf-3800-8d97-fb26be0ecadb | -12.6632 | -45.3008 | 2025-09-11 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| da2bef60-c3d1-31cf-adbb-470b6eadebc8 | -12.6825 | -45.2977 | 2025-09-11 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 92798849-1114-381a-8a7f-9ad0d6ebc7fe | -15.1176 | -52.4279 | 2025-09-11 12:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| eec33a0d-df7f-3e31-977c-2a137f5449eb | -9.0942 | -47.076 | 2025-09-11 12:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 81fb46cd-95a9-3e7b-92c4-f71b7a5d94d7 | -9.0579 | -46.9688 | 2025-09-11 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 2b7e5be7-b921-34f0-99a2-2ebfd8dcdaca | -15.6732 | -47.0389 | 2025-09-11 12:00:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 115.8 |
| fcb00818-9846-3f4c-9771-213d097d6928 | -19.2611 | -48.0221 | 2025-09-11 12:00:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 126.3 |
| ef870eeb-b210-3a26-8e79-91435038bad0 | -12.6829 | -45.2746 | 2025-09-11 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 94b6c334-6601-3b88-bd40-dc9ff0ed2945 | -9.039 | -46.9707 | 2025-09-11 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 362f036f-48a0-3b36-be33-2043d410d168 | -8.7547 | -47.1107 | 2025-09-11 12:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| a7b22fd4-379e-3902-8b83-ca361fd07877 | -8.8755 | -49.5613 | 2025-09-11 12:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| d1230f1e-6487-3054-9813-a4abed079216 | -8.7411 | -45.2248 | 2025-09-11 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 9a275585-7e0a-3e4a-b1d0-761c8feb82ca | -19.2617 | -47.999 | 2025-09-11 12:00:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 4c5fdc14-5c78-3989-ae54-377e816d2744 | -11.4093 | -43.5573 | 2025-09-11 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 19a5931a-d32e-395c-a822-225c38e8b82a | -13.2602 | -51.7548 | 2025-09-11 12:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.0 |
| bd0417ec-a04f-3db4-beec-dc286471a1d2 | -11.779 | -46.4821 | 2025-09-11 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 7eac00d9-ffd6-380b-b2b9-82f325d7c953 | -14.1492 | -45.4009 | 2025-09-11 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 65b96a39-bf60-358f-8e2c-4e819128ea52 | -10.184 | -46.2153 | 2025-09-11 12:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| c1c4c50d-09f3-3747-a8e6-c0a892a955e0 | -19.64724 | -40.20823 | 2025-09-11 12:00:00 | TERRA_M-T | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| bb20c0ce-8e6d-33ae-b79b-f98a599b8a89 | -20.16376 | -43.67558 | 2025-09-11 12:00:00 | TERRA_M-T | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 1d4aef80-ef29-3cf5-88e4-2424d4f9b7e0 | -19.66954 | -45.84606 | 2025-09-11 12:00:00 | TERRA_M-T | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 600916bc-08e6-307a-bc0d-d730e29d1356 | -14.4069 | -47.30845 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 0af14472-9a1b-39d5-b74b-b5b1a508dd9b | -19.04872 | -44.19901 | 2025-09-11 12:00:00 | TERRA_M-T | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2b7918c3-edcb-3f3a-9a32-e88dcd842f93 | -16.95301 | -45.8136 | 2025-09-11 12:00:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3ee77896-7acd-3af8-8a99-8c62a40af21c | -19.07712 | -43.8643 | 2025-09-11 12:00:00 | TERRA_M-T | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 51886268-fbfe-3155-a395-db8e17035774 | -18.00634 | -44.45288 | 2025-09-11 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b2b802be-0e6b-3ed8-98c0-57ef1933fa7e | -20.12787 | -47.6824 | 2025-09-11 12:00:00 | TERRA_M-T | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README135.md)
