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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7baccd6-a706-314b-9814-71d861ae9c0e | -11.42357 | -43.4732 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1a5a191b-1d43-3c56-b9e4-1e6c482b5991 | -9.9619 | -50.13351 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0709117a-69b6-3b5c-a307-7c9172fe7440 | -12.31313 | -50.29829 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d642feb-76fb-3d39-9f2a-990704ff659d | -11.42812 | -43.43903 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c0d6cb2d-447d-3c13-8f9e-ee6e4567c7bf | -6.70349 | -45.6931 | 2026-09-29 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7752038-5d0e-30f3-a683-2f96cf5b8d51 | -10.20061 | -46.69704 | 2026-09-29 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68458ce4-a41d-3dd3-9c47-ea12483e2cfb | -11.36696 | -54.04484 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 320b2c84-4676-3a36-8873-eb6229129343 | -11.35149 | -54.04665 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87e0eb35-4d3a-3929-b406-0ba99a181517 | -6.70416 | -45.68863 | 2026-09-29 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5d1dd9d-677c-31a8-9d38-20e60f85b144 | -11.26615 | -43.53266 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d98d150-4bcc-378b-ac52-f7f7225eb5e3 | -12.69427 | -47.38063 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53ea23a0-723c-3994-bedb-ea9e7b6e73d8 | -12.66733 | -46.98029 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff5b888a-20f5-3157-bd0b-c4b3fe8a3c12 | -11.138 | -50.07365 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 824fed20-9fbd-38f8-b4fd-29967d7b528f | -12.04693 | -50.95197 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4ffba6a-7867-3079-bd0e-8e267c168417 | -12.39227 | -50.22336 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cec1a8c3-0544-3d45-a343-9992efaadb89 | -10.43492 | -49.37614 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad794a38-50f1-3528-b220-d847255fc308 | -12.00627 | -50.99245 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6f55e0f5-9d35-3998-ad31-22eb9fa3a3b4 | -12.73604 | -47.27452 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 199597e0-252e-3f45-846d-c68a90546335 | -12.06724 | -46.47012 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b37a15d-a2ee-3a7c-8494-aab92e0e95fa | -10.41388 | -53.82608 | 2026-09-29 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36dff8a2-1462-3723-bb9c-0f720912fb7e | -7.4821 | -45.81771 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bb5b49a-ad0b-30fd-8a4a-dfac60805531 | -12.76006 | -47.29152 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 129fceeb-09f6-3515-bf69-9b72598dd2e6 | -12.04861 | -50.94142 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7db65957-c3be-3b0c-bc25-79e89c1d9c42 | -8.64198 | -45.34371 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 019e2448-0d79-31d2-89a4-940d7b463342 | -12.0135 | -50.99002 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45fe4dfa-85fa-3c6e-a5b1-3ae44c4749a9 | -10.81753 | -48.74721 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 515b220f-4b61-3e88-a262-affe46946296 | -13.177 | -48.52821 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7f10c73-f35c-39db-a3d5-eda56689c52e | -7.8446 | -45.81282 | 2026-09-29 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cba6b7a2-e814-391a-9d51-bc4fa45aeda3 | -11.37875 | -54.04236 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e44ac16b-e152-3b3e-87c1-17e5cbe07739 | -9.77129 | -36.98109 | 2026-09-29 04:51:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 4c3bfb32-d4af-349d-8fc5-efcfc49e6e16 | -6.72354 | -45.58521 | 2026-09-29 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56942246-9926-3491-b38b-bd5d8ac6a6c6 | -12.00166 | -50.94107 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bee3c4e-ea15-30cb-bbb3-a79957c6633d | -9.1396 | -49.98397 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b7b41fb-9c41-319e-8953-86c24b4ff5ac | -11.44213 | -43.47572 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2952e2a7-2516-3d5a-bb9e-952cc4658a8b | -12.05415 | -50.22053 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaca322a-96e3-370f-b4de-05250d9a15ad | -11.34468 | -47.33677 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59bc4f7a-581c-3c8e-b5b8-31f6f0943715 | -10.13532 | -43.89986 | 2026-09-29 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6144e765-b2c4-33f4-8f04-0ca58a36d30f | -10.72217 | -53.99299 | 2026-09-29 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f4d98b0-8cf7-3fb9-8ad2-27f71d32fb6e | -12.70242 | -46.9769 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d288f76-5ddb-35d7-b55d-54222377344a | -13.47128 | -48.58213 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0940fd21-428b-3ff4-b0a9-0210851014ad | -10.70711 | -47.82111 | 2026-09-29 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22419280-9677-38fb-8edb-bb669eaaf745 | -11.42552 | -43.45856 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd249e23-9ad5-3434-a675-cc1b300fa83a | -11.43147 | -43.44944 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19f240e0-19a3-3227-9f99-bbc0a3404f71 | -7.33349 | -48.58921 | 2026-09-29 04:51:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11102a1f-2a99-33a6-a2fc-00180ee3bd5f | -7.99959 | -43.26086 | 2026-09-29 04:51:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4454750e-427c-33d2-a612-0ee5d61f0f3b | -6.31755 | -52.62346 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| de7b7672-8cc7-30fb-ba4a-caf81232f792 | -13.52458 | -46.89713 | 2026-09-29 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32c16fad-f4bf-38a1-a229-f4298028419d | -11.38942 | -43.45692 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a45e37f4-6d0c-3019-8670-ea9f59cd6a93 | -7.99511 | -43.26027 | 2026-09-29 04:51:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 22266af9-bdaa-36d0-870c-7f20eaba1d8e | -13.08559 | -47.39279 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32ef103d-4e97-39f0-b5e3-0dee84ab7752 | -11.43212 | -43.44455 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a29d5521-1490-3e81-ae89-bfcdf5bb1a08 | -9.1321 | -49.9715 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e65f1b0-a331-3a90-acd1-69bef5a1fbcd | -12.93954 | -46.66475 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d676f202-0346-3386-9551-f63850b3edb9 | -9.77199 | -36.97553 | 2026-09-29 04:51:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3042a931-016d-3181-8893-7dcb6d553144 | -11.8018 | -49.05614 | 2026-09-29 04:51:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d9543e5e-e64d-3f84-b220-494047af7eaa | -7.43124 | -46.87973 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e79d4004-c7c2-3c1d-95a4-f11a3411508f | -12.31598 | -50.14925 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cba5a6dc-c011-36da-894d-6ed94c77bf2f | -11.47436 | -49.7337 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71c665d4-98ef-3c77-a638-d6b2f04aa9e1 | -7.39387 | -46.42118 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e9dc86b-fef5-3dac-9f76-538fd1a1a1e7 | -8.05626 | -44.80993 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8ecace5-4c26-362f-a089-b515164e4e3b | -11.39621 | -43.42965 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aedcc6e8-60a2-3828-9d8e-bc0d4d09d060 | -12.05081 | -50.94904 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0d9d3c7-cd96-3318-a673-dbdfa26fe343 | -11.33582 | -54.11654 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70a378ee-5d62-37db-a30a-ca46d534fb24 | -9.95857 | -50.13297 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b040e41-6174-312a-80fe-305ee3020163 | -11.62698 | -41.83089 | 2026-09-29 04:51:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34e3c1ae-91f6-3ef0-a651-e693f08f65c7 | -11.39126 | -54.03555 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c04377e5-09b4-3154-a269-d136214fdb38 | -8.72998 | -44.92643 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9ac64945-7a13-3668-8167-de453ae5e92d | -11.18881 | -45.13118 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a0b8a92-64b3-32b5-ad52-47338927e48f | -11.36279 | -47.44121 | 2026-09-29 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee7258f2-6429-37bd-9a8a-bd146130c143 | -12.15548 | -50.39668 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03331dfb-c9e2-3b32-91f4-44e36c7f4220 | -12.00053 | -50.94808 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da334d03-5df9-3717-abd9-344408ad28b1 | -13.34119 | -46.81115 | 2026-09-29 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c0883e26-8f1e-382b-b7c9-faa87dd12630 | -9.16885 | -61.4035 | 2026-09-29 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4cf899c1-8375-39e3-a803-cc03c036319c | -11.17961 | -44.7942 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 414e5e35-623a-3372-8786-0af3182f86ea | -9.09159 | -49.88252 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cb4f7c0-ff80-37ef-919c-3114f3bbb850 | -7.24609 | -43.37497 | 2026-09-29 04:51:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 41aac605-c9bb-399d-b937-adc28db198aa | -10.43436 | -49.37971 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eca67894-162b-32b9-9a9a-fe37230afb89 | -6.16569 | -52.82397 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2730335b-06c7-37d8-a6e8-fccc12a8fc8c | -6.31687 | -52.62768 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1e265af4-e6f8-3c1a-8abb-6cf783324cc6 | -6.16287 | -52.92022 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 547c7aac-3a13-33fe-a1f6-be68d50d9537 | -13.20396 | -48.56382 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ece3510-9f4a-33ad-a56e-fe99f4c34401 | -9.78039 | -44.81627 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd337564-4569-363e-bcd4-8632bad755e4 | -12.05526 | -50.21342 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdc79203-1adf-3987-b5fa-49ae9ca535a3 | -12.6269 | -47.25999 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef51baa7-e9b9-3823-b609-2c9b04ab9b8c | -11.41482 | -43.43222 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12dc7224-d8ed-3c70-9905-9c983cfdd386 | -10.69968 | -44.42641 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 718416d4-41d9-370a-8db1-0e86270b509f | -12.00109 | -50.94461 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5897bc4b-3a03-3f17-a88d-3d90edaed96b | -12.77125 | -50.67421 | 2026-09-29 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4962e982-5509-3cd0-940c-f7af75de1bff | -13.37411 | -44.00686 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4c59319-2255-33ca-9522-807f3605df54 | -12.05025 | -50.95258 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab764b90-75a7-36e2-8135-9683d499503d | -14.12618 | -46.2851 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| a868f83d-0233-3549-b9a5-f7b1579b7b52 | -11.37139 | -54.04107 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e73bb03e-be82-3fd1-bcc2-bc655b1d0737 | -13.40852 | -51.34351 | 2026-09-29 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f116a0ea-0090-36d4-8784-01fd03082e2d | -7.67996 | -44.89281 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5c68f38-35eb-3286-8705-cca3b21faba1 | -10.7959 | -48.75145 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e038618-0748-3b78-b289-a97c7de2caeb | -13.54352 | -49.17558 | 2026-09-29 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc8ba8e0-8421-3dfa-8737-667f6dae48fd | -9.07273 | -49.87232 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bde9d440-b51a-3e30-b11c-0be7352da110 | -7.46156 | -45.80074 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e385b98-95e9-3a35-bc4a-a1ffe3b14a7e | -11.01 | -54.14315 | 2026-09-29 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04d66141-6ee7-31d4-9bc8-ede611bcf155 | -11.39271 | -54.03879 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
