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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7179ac63-5c67-33f9-a994-904c491d9c40 | -15.0153 | -49.5904 | 2026-09-28 18:10:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| c874fe5a-56df-3b6b-a68f-fb3d6e412047 | -10.2065 | -50.0113 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 8c93c643-9a0b-33c5-a573-06c005144c53 | -10.6869 | -44.4576 | 2026-09-28 18:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 67dd7da3-cbeb-3136-8783-3c266a85e15f | -12.6267 | -47.2851 | 2026-09-28 18:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 7d5a6bf7-a71a-3b4a-af22-2d7739ea4677 | -10.6873 | -44.4343 | 2026-09-28 18:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 1527c3dd-10b2-3f9d-ac13-676815307570 | -9.0437 | -49.6317 | 2026-09-28 18:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 152.6 |
| a4c4e7b6-6a93-3026-9cc8-f2e357839acd | -10.1286 | -50.1902 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 91132096-2012-36ec-b2e9-10fd4b5723b8 | -11.6408 | -43.4744 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 4367a185-c19d-3645-81c0-dd6262d8d8ad | -10.9254 | -43.8876 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 81d935a6-399d-3191-b435-c6cc20737a79 | -11.2758 | -43.5303 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 5404e5bd-329b-3944-8b01-e221b5b4b0dd | -8.2293 | -45.4375 | 2026-09-28 18:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 47dd15db-9434-3d27-a593-b3f9566ff1e0 | -12.6447 | -47.3497 | 2026-09-28 18:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 908224cf-fccb-37e9-b818-9e3d62d719a2 | -11.1962 | -44.8037 | 2026-09-28 18:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |
| ca3afc4f-2012-3ad2-9f67-dad9c3d00dee | -10.7115 | -60.7312 | 2026-09-28 18:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| e63ffe6a-1604-3157-bf97-5cd19f32e9a2 | -10.7916 | -48.7377 | 2026-09-28 18:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 587ad765-20f4-373e-b961-49a9506c9e7d | -12.588 | -51.9617 | 2026-09-28 18:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| fde7881e-fa63-3dbc-ac6e-fc1f97845d4c | -6.8057 | -45.0474 | 2026-09-28 18:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a35107a0-7979-3d35-8cea-f96441d52de9 | -11.8641 | -47.1004 | 2026-09-28 18:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 81e99a61-2466-3904-b42b-379752501050 | -15.454 | -41.4403 | 2026-09-28 18:10:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.4 |
| a29d0cda-c00e-32f8-bcdb-3e79835a1a05 | -15.3998 | -47.9261 | 2026-09-28 18:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c4faea61-db36-3ab0-95b3-36d6de04da87 | -12.8513 | -50.9957 | 2026-09-28 18:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 920ac94f-32c2-3af1-b38a-f23b3325f612 | -12.9457 | -51.0695 | 2026-09-28 18:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 9fa4950a-1a05-3682-b5a3-7b46de68eb0d | -11.3927 | -43.418 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 273.9 |
| 3e01f36b-190d-3826-8c64-fe6088ef0705 | -15.4003 | -47.9035 | 2026-09-28 18:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 1d347b09-3ff7-32a1-916c-6dd3f6a4c872 | -11.3735 | -43.4209 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 8a84ce8a-6701-3e92-a362-b2c9da085933 | -10.0148 | -50.2443 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5797a9cf-cd8e-34f7-a484-bef99361b478 | -9.9781 | -50.1626 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 4add2826-7041-37f5-8943-bea129d01395 | -14.0915 | -46.3096 | 2026-09-28 18:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 172.9 |
| ec86cbf9-41d8-3649-9f5c-08f088561308 | -11.6592 | -43.5188 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 0b212f72-4bac-3489-a074-bbab9acfa4ad | -10.207 | -49.9684 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 673e8f4c-a48a-34da-aed6-a607a90a3370 | -11.983 | -57.6066 | 2026-09-28 18:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 119.6 |
| ae1ce65e-98e9-3650-b1f0-2b97367d274b | -9.7684 | -44.8312 | 2026-09-28 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| a1fb03f1-9f87-3c9c-a8d0-571aa756d498 | -10.8001 | -57.2007 | 2026-09-28 18:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 174.5 |
| f5d00faf-ff83-3308-91ac-f83660ccff6a | -9.4813 | -46.3646 | 2026-09-28 18:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 843c08f7-6de5-34c2-b352-827de93ca92d | -10.8373 | -61.3988 | 2026-09-28 18:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 9e370c85-8d39-35cf-8a84-142017d8dd4b | -10.5957 | -50.569 | 2026-09-28 18:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a9fb8d27-03d6-33b7-becb-b6bcf914ca16 | -11.6096 | -44.1382 | 2026-09-28 18:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 309.6 |
| 9c7eb2c9-3f26-3ab5-a4a3-7c6b5478947f | -7.7038 | -54.7521 | 2026-09-28 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 410c2b58-4a6d-3db9-9b10-bfc1e81ff7bc | -9.1337 | -49.9656 | 2026-09-28 18:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 66b83436-640d-393d-adf2-8482997d1b32 | -10.9637 | -43.8821 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.3 |
| fad064ca-aeab-38cf-953d-ec64038d4793 | -11.3436 | -54.1086 | 2026-09-28 18:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| bd87e06f-7389-3456-8889-bb690e584cfa | -10.8191 | -57.1795 | 2026-09-28 18:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 338.5 |
| 71f57c5a-ef00-3543-a97c-02b30f849dc9 | -11.3739 | -43.3972 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| f5c45be5-d880-351b-9f3d-92791719e4c3 | -10.2257 | -49.9879 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 4dafe474-110a-36ed-ae45-a954d67a3b5c | -11.1331 | -50.0409 | 2026-09-28 18:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| d7499d7e-23c2-393d-ad86-3fc8a518713e | -9.1525 | -49.9639 | 2026-09-28 18:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| a1e6f34a-ba91-3758-b4c5-c7055731aa53 | -11.373 | -43.4446 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| f35f47e5-e2ea-3e27-b12b-bdda625ae264 | -12.6271 | -47.2626 | 2026-09-28 18:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| c8971de3-1f21-3355-8d0b-8f2cdec4a3ab | -8.1871 | -54.7824 | 2026-09-28 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 74b41785-14db-3a89-a84b-ab7a483abbcf | -11.2753 | -43.5539 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| a5dbdbd0-dd12-3e48-8c56-1881fb613cea | -12.1075 | -45.2248 | 2026-09-28 18:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 609f0071-f304-38f8-8079-c3c2d07601d8 | -11.1966 | -44.7805 | 2026-09-28 18:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| d62c1123-a6dd-3aed-b7e6-d4fe563338b8 | -15.112 | -53.8838 | 2026-09-28 18:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| f49a61f1-88b7-3c4f-b5b6-fbecc2a2bc7d | -8.3608 | -45.4695 | 2026-09-28 18:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 9b1fc00c-1aad-36cb-bfda-b31c8a20b534 | -11.6989 | -44.4984 | 2026-09-28 18:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 9435fbbe-9d1a-3255-89b2-d4f02713af1d | -13.3641 | -44.0166 | 2026-09-28 18:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| b7016b50-eba9-30b5-bb43-83937da28c4c | -11.6986 | -43.4654 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 1dea9636-ecd8-36df-9708-f93d08aa5ccc | -11.6784 | -43.5158 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 577282df-ab4c-31c4-bbb0-1bc7d3d3eb76 | -12.1391 | -57.1751 | 2026-09-28 18:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 5eb230ab-a13e-38ae-8b5f-83b4ac83553b | -11.0991 | -51.1111 | 2026-09-28 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 3851a884-795a-31c9-89d3-479ee551ea37 | -10.9538 | -50.6592 | 2026-09-28 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| d1c45a35-6158-3a5f-9a07-94ceab6e722a | -10.2067 | -49.9898 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 7d20faf7-93d9-356a-ba46-5cc0b713cd60 | -10.9258 | -43.8641 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 03937746-19b4-34ab-84fd-e639d4b337a8 | -13.9103 | -42.1126 | 2026-09-28 18:10:00 | GOES-19 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 21e91152-fa70-3554-b1c2-6e890e81367a | -10.2827 | -49.9606 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| aa1d57ed-9b40-3e69-9342-1ad9b8db547e | -11.6404 | -43.4981 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 501.2 |
| f1f5dca2-a53d-38dc-8a74-4884984625d4 | -10.8375 | -57.2178 | 2026-09-28 18:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 5bdc864a-7fc2-3790-b668-905410d132b9 | -6.3137 | -43.6178 | 2026-09-28 18:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 295a8738-5312-3d25-945b-fc954dbefe52 | -10.824 | -60.7246 | 2026-09-28 18:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 175.4 |
| efdc77f9-66bf-35c6-8160-1442942905d6 | -11.1775 | -44.7832 | 2026-09-28 18:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 353.5 |
| afb4cb47-e8c1-3338-a57b-7a287ecfa9fb | -10.8052 | -60.7257 | 2026-09-28 18:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 141.1 |
| e6c7ab4a-66d8-3d19-8f8c-6bda3ae89749 | -13.3272 | -43.9285 | 2026-09-28 18:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 186.1 |
| e201ff78-310d-30af-bc51-bf601c8125ee | -15.0984 | -54.7189 | 2026-09-28 18:10:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 188549dc-8bd9-388d-aeb0-feb77d325ef7 | -11.6213 | -46.7742 | 2026-09-28 18:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| eb261d23-3984-3428-851e-cfa66d84bde6 | -12.1359 | -50.3543 | 2026-09-28 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| f94aa278-bbfa-3e2c-8959-7208dddb000d | -12.1202 | -57.1767 | 2026-09-28 18:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 4a55c6ae-45ae-3931-84ca-c05d424cd6a7 | -9.1813 | -60.7747 | 2026-09-28 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 32fed127-1a69-35e1-a668-0460b9171b5c | -9.9784 | -50.1412 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 4445604c-090f-3bc6-bd5f-462bdcc3ae51 | -7.3175 | -44.591 | 2026-09-28 18:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4a202540-d402-3ea2-a616-62a49d0d8ce5 | -5.7388 | -45.0172 | 2026-09-28 18:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 3a4ee206-1715-3e38-ba69-2a32861f82c9 | -10.9441 | -43.9084 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 77a822aa-0071-382a-b830-2b118dabbe95 | -11.6985 | -44.5217 | 2026-09-28 18:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 2f059e19-931b-3830-974d-03806926117e | -14.111 | -46.3063 | 2026-09-28 18:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| b94677f6-2eda-3516-8280-da0fa0ad0e0e | -11.9039 | -47.0053 | 2026-09-28 18:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 3d9207b3-04c7-30db-b205-3444ec574a1f | -10.8532 | -54.0916 | 2026-09-28 18:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 46b5358b-562e-37fc-af0a-a142732c3d36 | -10.9449 | -43.8614 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 3d2af7a0-45b6-31f2-b24e-e7be55ca2fe0 | -12.6071 | -51.9595 | 2026-09-28 18:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 8b5c4fda-83de-3858-9286-fdf3d5878725 | -7.5057 | -44.5733 | 2026-09-28 18:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 23ff356a-147e-3334-8572-c7aedd635adc | -10.9445 | -43.8849 | 2026-09-28 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 372.2 |
| bd343449-f2a9-3314-a2cd-9bd32186310a | -9.9393 | -50.2518 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 3d28f183-2fb9-353a-b4a0-5d14563ec42c | -10.9536 | -50.6805 | 2026-09-28 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 23b5b318-f667-3c8f-b213-b3e5757c5339 | -7.6852 | -54.7532 | 2026-09-28 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 34fb2d9c-9b0a-3dff-abe9-04c8a4e3aa3f | -11.6793 | -44.5246 | 2026-09-28 18:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 185.8 |
| fd823c86-8fef-309f-b597-d22e45aa3b0c | -10.1098 | -50.1921 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 64c9547a-fa97-3028-8313-9ddc68b3f6fd | -10.8187 | -57.2192 | 2026-09-28 18:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 356.4 |
| bfad5e41-7707-382b-9159-0fd60ae18408 | -9.9396 | -50.2304 | 2026-09-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| e8de54cd-1dd4-3ec5-8b76-d001d5134c99 | -9.4535 | -41.8088 | 2026-09-28 18:10:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 329.8 |
| 44172eb1-0f16-3388-8335-b12a2d0efd55 | -20.7 | -57.89 | 2026-09-28 18:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0cc50f30-480d-304d-83b8-a4f88517321a | -11.89 | -50.87 | 2026-09-28 18:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e6f503a-f334-3b37-a3dc-b87cea0740a6 | -9.79 | -48.18 | 2026-09-28 18:15:00 | MSG-03 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README173.md)
