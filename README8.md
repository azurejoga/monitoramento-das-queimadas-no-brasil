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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fd86952-93d3-3496-a495-f922bc698b3a | -2.066 | -45.35952 | 2025-12-05 04:29:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dd5c230-46a7-3952-a991-cd1f0a51db3f | -4.70233 | -44.56081 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f63ac0c-1bfa-374e-9d65-20beb52bd05a | -4.53424 | -44.22784 | 2025-12-05 04:29:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c9af9f8-7b55-39b1-99ed-c85bb7e88483 | -2.69312 | -51.64737 | 2025-12-05 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c30dbb1e-88cb-3bca-b786-8471e27589ec | -1.12364 | -53.44302 | 2025-12-05 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 85075767-810c-3276-b5d3-fa4baa5d3e6f | -1.69333 | -46.15535 | 2025-12-05 04:29:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d99135b8-2626-3216-a2c4-71e322ad8847 | -5.86989 | -35.38337 | 2025-12-05 04:29:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 806615da-cc96-3947-9cc1-7fde7e081ef4 | -6.00386 | -41.13845 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 1bea9662-e208-33e7-97f8-68de259f87c2 | -4.55237 | -43.71235 | 2025-12-05 04:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88644e15-f218-3217-a3ff-e07dc4e07298 | -4.70294 | -46.42648 | 2025-12-05 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e143e881-81af-3fcd-8654-f10aa6f7c995 | -5.17728 | -43.07579 | 2025-12-05 04:29:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e164e59-70de-3b34-a5e5-4f26f1a15c27 | -6.42285 | -44.78705 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f941b32e-d971-302f-ba0a-c8c0bc4bbe86 | -3.49805 | -39.9034 | 2025-12-05 04:29:00 | NPP-375D | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c288340f-5111-331a-b139-7c5b6b13f4b6 | -5.18087 | -43.07635 | 2025-12-05 04:29:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e4fb3816-1f15-3f91-990e-e4f860690988 | -5.62447 | -37.33176 | 2025-12-05 04:29:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 95f472bf-104f-3e0f-b7b0-d868f41cec36 | -3.34893 | -42.15054 | 2025-12-05 04:29:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 210e6128-d2a8-3f30-8480-38f086edcb87 | -1.67841 | -45.79657 | 2025-12-05 04:29:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3c8e025-983b-39e3-a271-6c42d4a46edf | -4.71126 | -44.45899 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 148c8b5f-e7e6-31a6-9785-60bb2bb2b5c9 | -7.05762 | -39.31212 | 2025-12-05 04:29:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8673c291-eb13-34db-9eed-fdde5aa1935f | -3.42569 | -39.26561 | 2025-12-05 04:29:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6f15c232-0fcb-3f1b-95cb-be0639fa4eaf | -1.41163 | -51.59949 | 2025-12-05 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99bf126c-5cba-3a4c-8cab-c34830d5812e | -1.46116 | -46.72261 | 2025-12-05 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81ddd822-bea0-30ed-b890-eaed5a801ed3 | -0.78027 | -49.16419 | 2025-12-05 04:29:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95723113-9b59-3435-ba2d-7c32c754357a | -4.70571 | -44.56134 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53f0ef1a-520e-33a1-a7d4-bc519af88d82 | -4.78965 | -44.56307 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0610825d-2695-399a-bb9a-03aa0ad209ac | -1.35558 | -46.42049 | 2025-12-05 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17551760-f96a-394d-8742-c88d64d34c7c | -6.00439 | -41.13495 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 429b92ac-efdf-3979-87d3-25410a1002a4 | -4.70965 | -44.55827 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 385051f1-18b6-3664-8ca2-3bc0b877cc0d | -3.97733 | -45.49385 | 2025-12-05 04:29:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5208ec9b-18e0-3ec7-99bd-f3a7a67a526b | -4.16445 | -39.25147 | 2025-12-05 04:29:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| df7a7d4f-5b8b-30ba-a6ad-7209b0bc14aa | -5.62443 | -37.33176 | 2025-12-05 04:29:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 03f7debc-3e06-3c85-b0ac-fffe5b7f6c7e | -5.35198 | -42.11232 | 2025-12-05 04:29:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24ab67fe-beb1-3d3e-a174-5d932a229acb | -4.53822 | -44.22472 | 2025-12-05 04:29:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef9841af-7fee-30bf-a5ac-a593de0c3e7c | -2.4426 | -47.1643 | 2025-12-05 04:29:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9ca4004-b610-38dc-9200-44a842391502 | -3.02525 | -41.13474 | 2025-12-05 04:29:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f6f82db-a009-391c-8478-e7657e6407bb | -4.50024 | -40.50661 | 2025-12-05 04:29:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cb6b0e23-a228-3b7f-a035-050eaf0ab969 | -2.06932 | -45.36004 | 2025-12-05 04:29:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fc2b8e1-12a3-3446-9b2f-7975d7976231 | -3.93506 | -45.24615 | 2025-12-05 04:29:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b38cf343-7fea-3b7e-b207-2c5fb179160b | -1.95773 | -52.72926 | 2025-12-05 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e706f6b-ec78-33fd-9b5a-3fc58e2922fc | -5.3471 | -43.28125 | 2025-12-05 04:29:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0acfe4ab-d50b-394a-8815-82fc9a94b8bb | -2.07425 | -45.5866 | 2025-12-05 04:29:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7fca503-bc9d-3852-a8f0-caa84cd0036d | -1.78769 | -54.0141 | 2025-12-05 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b137eac1-ef57-3751-9e8f-e2dbffb8cbec | -6.42002 | -44.78291 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba2c3b8c-9eda-310f-8e0e-1396a48d346b | -2.60657 | -47.01068 | 2025-12-05 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 185cec60-3055-3d29-aade-8c2ab163a9ff | -4.73609 | -44.43329 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1ab714d-e4cf-3979-bb55-b88d0f57021f | -2.56488 | -51.82911 | 2025-12-05 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5e7d2ff-477d-3ec8-975c-07e3fd432d3c | -6.00739 | -41.14268 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2019beda-66bc-3ba6-8859-0432b8797c77 | -4.53765 | -44.22837 | 2025-12-05 04:29:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 880dd793-bcbb-34f8-85be-42b89383a74f | -1.23835 | -46.73952 | 2025-12-05 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 311078fb-bee1-32cf-9e27-f38d46c4d600 | -4.72951 | -46.388 | 2025-12-05 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06f7b5a6-9904-39e1-a850-0d493065dd0b | -1.69278 | -46.15884 | 2025-12-05 04:29:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e2c9115-fffe-3eae-9b06-aa6ced912762 | -5.83836 | -43.26779 | 2025-12-05 04:29:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3881385-3fbf-38fb-aba2-4ac8551dbd25 | -5.18024 | -43.08043 | 2025-12-05 04:29:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9cb660e3-b48f-32e3-8aec-34f1890c82fe | -6.0109 | -41.14695 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 611b7a7d-041c-32cc-ba11-24409ecb0011 | -3.34827 | -42.15486 | 2025-12-05 04:29:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b7c3b60b-b520-3b53-83ef-702a4f87dc8e | -2.61053 | -47.00762 | 2025-12-05 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48ec29f0-29a6-36c8-8226-28fbcf5aa73f | -6.04307 | -41.8054 | 2025-12-05 04:29:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ae8c2ac6-cac7-37a3-8bde-850d5ec411d2 | -2.06878 | -45.36348 | 2025-12-05 04:29:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bce4fa2f-a2e5-3e37-afab-e717493fa43b | -3.16669 | -45.76541 | 2025-12-05 04:29:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fb86d90-2d87-3492-8bf1-3a196bf1541f | -4.70515 | -44.56493 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99d34a22-48ad-3c4e-bb4b-2f4e3a89a365 | -3.42125 | -39.26495 | 2025-12-05 04:29:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 91ba759b-8a3d-3552-9082-6e8a37c71c6e | -3.50801 | -44.51986 | 2025-12-05 04:29:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0aa4035c-bd79-35f5-b0e8-f93a41e3aff2 | -3.17418 | -45.65356 | 2025-12-05 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3422fddd-e293-321a-83ac-02406bd66e96 | -6.05003 | -39.43801 | 2025-12-05 04:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bfab9fbe-2421-3f5b-a001-9e813d859cbd | -1.23156 | -46.73845 | 2025-12-05 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 415e30a8-f22c-327a-ad2b-275b72ad9491 | -5.18383 | -43.08097 | 2025-12-05 04:29:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ddc96527-1924-3fb1-8e51-448dccda0524 | -2.59353 | -46.80985 | 2025-12-05 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d40384da-8629-3418-ad74-620d4bd35ecd | -2.06655 | -45.35608 | 2025-12-05 04:29:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61b67054-8e1c-333f-a71b-65aac3d4e2dc | -4.55177 | -43.71615 | 2025-12-05 04:29:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4db2d8ab-ab57-3d3d-a16d-d3f07dff7980 | -3.51137 | -44.52039 | 2025-12-05 04:29:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed26e584-e7c5-315e-8f88-1a2ad38b9c8e | -6.00792 | -41.13915 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6da82e72-d9b7-382d-91b6-9bff87b11279 | -5.61874 | -37.33427 | 2025-12-05 04:29:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| dc405c62-76c8-3ae8-bb4a-076bb79214dd | -2.50908 | -47.2494 | 2025-12-05 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d63567ab-f165-355c-9c88-8904210c366b | -5.19122 | -37.63694 | 2025-12-05 04:29:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cce50231-0dc5-36ac-9deb-4c992923daf7 | -6.00686 | -41.14621 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 657581e8-bb9e-3de9-95fc-0ad20f6d043b | -6.41889 | -44.79019 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 595cdc23-29b7-31d8-93f0-cfbb3a7297df | -0.7859 | -52.29347 | 2025-12-05 04:29:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48fdd75a-1ba4-31c5-8806-55dbfd5a2127 | -6.00633 | -41.14977 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 25a291cf-32c3-3ed3-b408-fd68710ec696 | -5.17665 | -43.07986 | 2025-12-05 04:29:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd95cf38-5660-32e1-9a45-4c5ba7f0e73f | -5.62399 | -37.335 | 2025-12-05 04:29:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 150672b6-7339-32e1-ab83-17d9957c5876 | -6.04325 | -41.8071 | 2025-12-05 04:29:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a8f716ea-c9dc-3719-8eac-fb49f950cd04 | -4.73228 | -46.39199 | 2025-12-05 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c6ffee5-10f6-30dd-82b1-c2fc6d282bfd | -2.63434 | -46.96695 | 2025-12-05 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e82f27a-f280-329d-b524-a8d84177db2f | -4.42163 | -45.31874 | 2025-12-05 04:29:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e9fe9be-1568-3bd5-912f-c485f230b47b | -7.05503 | -39.31377 | 2025-12-05 04:29:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 032bccdf-0a13-3464-ac24-f5a938df0f7f | -3.17364 | -45.65701 | 2025-12-05 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7d76051c-8684-3623-8ce1-d7b909f448ae | -4.50383 | -40.51091 | 2025-12-05 04:29:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e46011e5-0b48-3628-a0eb-c1ae8455061d | -5.17961 | -43.08449 | 2025-12-05 04:29:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95d772a3-ac13-3d4c-845b-5f202d2560c4 | -4.71521 | -44.45593 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 143a4f29-268e-3660-9f0a-a58c1013a17b | -6.00228 | -41.14907 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3947bbaf-97e2-3b2c-a0f0-6ce859d7fc78 | -2.60996 | -47.01122 | 2025-12-05 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28053314-4624-38c0-b011-e8f6d6420e95 | -5.99927 | -41.1414 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| cefeb43d-374f-3812-a00d-1f1df5bfeb4d | -6.42625 | -44.78756 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c70424b-2dcd-32c4-a34d-1f1e98f1fdb0 | -3.47158 | -43.87893 | 2025-12-05 04:29:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e9c8394-ccfd-3784-9797-319fa859a9f3 | -6.00281 | -41.14552 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 92201433-5974-364c-8a38-8e482521d458 | -6.41492 | -44.79334 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e507e2bf-e8e6-3780-87a9-3a87c97f3465 | -2.06269 | -45.359 | 2025-12-05 04:29:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba3ec3c0-5a6b-36df-8714-2a4d99252360 | -1.78875 | -54.00763 | 2025-12-05 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 725f956a-4b8b-3d21-a8da-f8287a6993b7 | -2.56559 | -51.82481 | 2025-12-05 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f4115a9-fe63-3199-a7ae-b66d19212fb3 | -1.67896 | -45.79311 | 2025-12-05 04:29:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README9.md)
