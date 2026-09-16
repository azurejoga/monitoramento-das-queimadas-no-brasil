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
| 7475021f-b5ba-33cf-a8bc-a916a4bfa6ad | -15.28717 | -42.80745 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3ab52e5-9dd0-336d-afa8-d99ad674e622 | -10.59589 | -47.74832 | 2026-09-16 03:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce8a7079-f9e8-3177-a241-c7edc61c0f78 | -16.00152 | -38.94323 | 2026-09-16 03:55:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5351ddc5-6d9c-3f82-a74f-1cc10a7f0ced | -9.76266 | -46.57375 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b116c918-7333-391f-84a1-4266a8cd9157 | -15.2784 | -42.80866 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e71ace8-ca96-3799-990d-807231961285 | -9.78467 | -46.48713 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5eac690e-0747-3234-a21d-d68cf55f21ca | -9.56988 | -46.58705 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09335b83-b0a4-3c14-bc27-b514ec0c020b | -10.75868 | -44.81873 | 2026-09-16 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cfa1615-3955-394d-981c-e257a73c56aa | -12.68173 | -38.32248 | 2026-09-16 03:55:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6bb111ef-7033-3aea-a338-d63122410230 | -10.77521 | -46.21035 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22175215-ad44-3f91-af68-f54405fad823 | -14.85976 | -49.97022 | 2026-09-16 03:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 50e4da55-334e-3b9a-84e1-7d1a3e26ffa9 | -12.71482 | -45.61915 | 2026-09-16 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e50213fa-1738-398f-843e-f6171b563aeb | -12.47367 | -41.41986 | 2026-09-16 03:55:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b53778fd-ba0b-3631-9741-0e274f5085b9 | -11.24626 | -43.47935 | 2026-09-16 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b27ef159-27e1-3d64-bd04-51d5f4057efa | -10.41145 | -48.65746 | 2026-09-16 03:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 446c048e-1bdb-3e8a-b6bd-8b0436367b93 | -11.54493 | -46.86585 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a44e5508-725f-35ac-b1f1-7bcc2f910c64 | -11.88913 | -43.82469 | 2026-09-16 03:55:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ad663cb0-3b8a-3a0e-85dd-6b1a1be612e4 | -12.83045 | -39.76495 | 2026-09-16 03:55:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b2da0b3-9ead-3477-a3fd-69de0c824a95 | -10.7562 | -44.81923 | 2026-09-16 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 711d7b6f-2719-308f-8b99-d611ee8f1ccb | -9.3466 | -50.17628 | 2026-09-16 03:55:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42055925-133c-3b8e-a950-df9fd74adb4f | -15.56228 | -42.37588 | 2026-09-16 03:55:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| db520671-71ef-3dc5-8732-19c0efb7ff41 | -12.56237 | -47.10286 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e4e146b-465a-3697-bb55-e9c825c9d923 | -12.54404 | -47.10521 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6fd73fe-d597-34e1-a197-60366c6c3103 | -9.11122 | -45.72861 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5dd8710d-628a-3e76-9aed-028885d8f409 | -18.23155 | -41.25038 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 297ad005-997c-3ceb-90e3-9c6c7d72cd53 | -18.22127 | -41.24637 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 224dd912-7f77-33f7-aaa0-b1c6ca8ee8c4 | -17.03556 | -41.281 | 2026-09-16 03:57:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e404727b-36ff-3fd0-971e-2e07d98bfbf1 | -18.64813 | -47.2878 | 2026-09-16 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c118de5-b019-3c63-9688-20b3a6f9bba9 | -18.22641 | -41.23829 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4761d335-730d-39d2-b2d6-68fd86a24329 | -17.04126 | -41.29165 | 2026-09-16 03:57:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 1d294a8c-f7ab-31aa-bda9-b5bf683db114 | -18.22491 | -41.24694 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f47e0831-f849-3705-a94d-8e7a4258182c | -18.22661 | -41.23614 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f0bb50e-98e2-35f9-8a78-c0c5fc508aec | -17.03923 | -41.28175 | 2026-09-16 03:57:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5631573d-166d-3ff4-8f05-02e2f713abf2 | -18.11091 | -51.6935 | 2026-09-16 03:57:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1378bc8c-a696-3734-bcb0-105b00e8ccd5 | -21.06751 | -48.56131 | 2026-09-16 03:57:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 63ba1558-1801-3eb4-9875-c12fe968f3ee | -18.11762 | -51.6953 | 2026-09-16 03:57:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae0141fc-aec9-3e2e-8c92-edf9cdbb40fd | -18.23023 | -41.2368 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| be6dc74b-dfe6-348c-a42e-95bb3485262a | -18.22855 | -41.2475 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 358edf30-9fec-3e9b-afdf-b8c3d793c436 | -18.22948 | -41.24102 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 68210b5d-9980-39ab-bf3a-47dbb1b70165 | -18.22507 | -41.24473 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 585ebae0-4a96-3795-8f22-c71eb9e1e646 | -17.03759 | -41.29089 | 2026-09-16 03:57:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 2418e842-e391-3a69-bd28-d59ffad7fae6 | -18.23292 | -41.24383 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 8500de51-be83-3228-8b66-97e7d90edf10 | -18.23004 | -41.23892 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 881a16f2-fa61-3937-9732-d132324da3d3 | -17.68223 | -40.13352 | 2026-09-16 03:57:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b5b2074b-c4e9-36fd-ad86-59f7538bbe02 | -18.22566 | -41.24258 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bcff2372-f3c9-312c-ae14-b0d6670a1e8a | -18.2293 | -41.24315 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f7987e21-f0d5-379b-b167-a489c2e898ed | -18.22278 | -41.23768 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f7747f46-2f2a-3424-82b2-66a5f1fa315a | -18.22584 | -41.24042 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 1d3e039e-4a3d-3170-97b3-afc8ceda0781 | -17.47129 | -39.41632 | 2026-09-16 03:57:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0b8d04fc-ce3e-305c-8f4c-32b5cd72e041 | -17.03841 | -41.28632 | 2026-09-16 03:57:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| d65d5ea0-95de-3b1e-8134-7695915eea71 | -18.22872 | -41.24528 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| a69b7140-8020-3fe7-bd74-ccb879ce0956 | -17.04004 | -41.27723 | 2026-09-16 03:57:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2cb78775-6bb5-39be-adfe-33687aa12617 | -18.22414 | -41.25138 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c55618c0-d21e-301e-b6e7-bca47e4e2acb | -21.06828 | -48.55779 | 2026-09-16 03:57:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 517813b6-8ecd-3c50-abbd-28c8b089fa1d | -18.22202 | -41.24202 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 00b8040d-c253-3708-adf5-dcf002c501ea | -18.6474 | -47.29125 | 2026-09-16 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6678aa9-7736-36f4-9c62-216bade43a10 | -17.03636 | -41.2765 | 2026-09-16 03:57:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c5f7a842-3bc0-399f-baf6-464bac739398 | -17.04207 | -41.2871 | 2026-09-16 03:57:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 611249df-94f2-3aa8-baee-d52174f172bc | -18.23217 | -41.24817 | 2026-09-16 03:57:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 3b9b9044-27f3-3c41-ac6a-371d9653963e | -18.65254 | -47.29258 | 2026-09-16 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fafb23df-525a-36cc-9854-c5503deb6ed5 | -6.344 | -62.6904 | 2026-09-16 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 47c2a238-8d8a-3f7d-a677-85ee3b6dcf86 | -6.3256 | -62.6909 | 2026-09-16 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f5fb6643-4e56-3341-ae64-3f1f85042821 | -6.3623 | -62.6898 | 2026-09-16 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a99918a5-a374-350c-8537-a19f6696140b | -6.3439 | -62.7092 | 2026-09-16 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 948e0798-8e49-3963-bbf7-7ad9b2ef15b0 | -6.3257 | -62.6721 | 2026-09-16 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| fc48daf7-3dfa-3030-8950-b057c9602b5f | -6.3439 | -62.7092 | 2026-09-16 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| d1cb8bba-296c-3c67-9eac-930d8564f4f1 | -6.3256 | -62.6909 | 2026-09-16 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 84b944ab-9c8f-335c-a596-386198f8cc48 | -6.344 | -62.6904 | 2026-09-16 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| e0162441-7f9c-3e07-9c34-600429914161 | -2.10482 | -52.04852 | 2026-09-16 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46c0a47e-fc17-314a-9505-79254946cc1c | 1.177 | -50.95629 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f47421f0-924a-3dc9-beac-98f0eadf76e3 | 1.19083 | -50.93757 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a27757b-c3a7-36cc-b49b-419feddf8b9b | -2.10324 | -52.058 | 2026-09-16 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 15e2bd63-85e3-306f-800e-6d292dc05ba8 | 1.1763 | -50.96281 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c3e45244-0d54-3a3b-95cf-b3701a573ce3 | 1.1802 | -50.94837 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| daf8e059-bfb7-3b48-a939-2b6801022bd7 | -3.87966 | -38.49898 | 2026-09-16 04:12:00 | NOAA-20 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 837f169b-bd2f-35c6-927e-22b0cdfd6e49 | 1.92798 | -50.83184 | 2026-09-16 04:12:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 514d13ca-bfce-3304-8915-d2fa4fe0388e | -1.79062 | -47.83582 | 2026-09-16 04:12:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 339abf78-3af6-3855-b5d6-872a7f7e7d7c | 1.92657 | -50.82285 | 2026-09-16 04:12:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a26f6ae-5ac6-3152-9d51-e39fc14e9742 | 1.2463 | -50.88583 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c48e84d-d166-3816-ba24-4da4a8f913a8 | -2.25612 | -47.00705 | 2026-09-16 04:12:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33ebaf7b-496b-304e-8fda-f1bfd0da9ee2 | 1.18634 | -50.9364 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 962c537a-bd15-3ad1-b5d8-70448ec641d1 | -0.98069 | -47.50291 | 2026-09-16 04:12:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 766d6625-1cdb-3588-8671-9d4018d95843 | -1.21097 | -47.89149 | 2026-09-16 04:12:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b96e8f2a-8b26-344f-9eb6-b76832abbf5b | 1.17835 | -50.96529 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c8fb0ee1-6a3f-333f-8b1e-9cbbd8d6f04b | 1.92841 | -50.82363 | 2026-09-16 04:12:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 482c4459-5ed3-3b1c-8ec0-d50505f47824 | -3.15013 | -40.1605 | 2026-09-16 04:12:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d861b370-5bec-364b-8925-d25b6c82a019 | 1.18166 | -50.94628 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0ada0915-a29d-3bb3-be6b-7ff61204c693 | 1.25161 | -50.88045 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e32c1219-1a3f-3d1d-9ef6-17cc1c2e9a23 | -2.09789 | -52.05219 | 2026-09-16 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2595484c-e3be-3e7d-ba80-a82c04e61ba3 | 1.92727 | -50.82734 | 2026-09-16 04:12:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c02d344b-e77b-3dd2-81d4-60b5092af602 | 1.18701 | -50.94086 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7404e256-cacf-39c8-b038-2c3704f2a624 | 1.18092 | -50.9529 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5247f384-c415-3dd0-ada8-88264561c99e | -2.90313 | -40.3918 | 2026-09-16 04:12:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8e65cde0-068c-33c4-9245-c0ec5fbb5063 | 1.18163 | -50.95742 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d3c9335c-8ec9-38a9-900f-4f4d86886cbb | -4.14914 | -40.78312 | 2026-09-16 04:12:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c37cbf6-7063-31e2-9ee5-a57c14a8a205 | -2.09709 | -52.05696 | 2026-09-16 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ece2983-16b4-350f-b767-d62dad580a83 | -2.81288 | -48.65413 | 2026-09-16 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6be0437f-5173-32ea-8bb7-8d644e2e4fe5 | -2.6086 | -47.74934 | 2026-09-16 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0397244-3220-3c9a-951e-7695159a4a60 | 1.17768 | -50.9608 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ce82c3fd-4bdd-37aa-8c8b-514e8b094300 | 1.18235 | -50.95082 | 2026-09-16 04:12:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README20.md)
