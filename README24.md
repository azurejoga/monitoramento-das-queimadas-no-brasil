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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc0bcb26-3689-328a-9ef2-b94e6d58ac8f | -10.13918 | -46.19138 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d93110d1-167c-333f-9b30-77f547379486 | -13.82723 | -43.85746 | 2025-09-08 03:40:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d020f29-6d60-3f82-9296-b9b32920bc38 | -11.01817 | -45.93354 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13788f87-a568-382a-b28a-ab16794fb9f7 | -11.39134 | -43.54427 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 994f7cb3-1c29-3460-a60e-2c7c433b55b0 | -13.00629 | -45.21001 | 2025-09-08 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5a5f49f-114e-3350-bc81-7478cbce6eef | -14.60804 | -48.08739 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cf66928-aa2c-3db7-8f1e-80bc7bc5c3ca | -10.14184 | -46.19594 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ef838aae-76a4-3b15-b7ee-76b95ad86673 | -11.03297 | -45.95369 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5d92885b-4447-3ace-a48d-f78dff0ea55b | -9.71812 | -43.98503 | 2025-09-08 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a1748782-dc58-3ab8-b5c0-57035ac4c8b3 | -14.26281 | -44.94445 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53924ea0-052d-3e38-a4bd-cd873bcbf1a6 | -14.29111 | -44.87867 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c86f2fcb-b323-37d1-9ba9-3660dd4f4f8a | -9.72487 | -43.97916 | 2025-09-08 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d6098fe9-cf08-3518-9529-3dca61f566c0 | -10.28781 | -48.80629 | 2025-09-08 03:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9afed383-b4a0-3fe1-939d-5627416b0f74 | -9.72355 | -43.98641 | 2025-09-08 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b08ad510-52de-3fcf-b673-aa5cdd7a0132 | -9.20614 | -46.05457 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7d58917-7a65-3a01-a096-eef33783083a | -9.18345 | -46.07065 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 904abc8c-0402-35ea-8fdf-44495b3d1750 | -14.29446 | -44.87126 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf0cc441-34f2-3c5f-9ad3-fe52f84c2010 | -13.70303 | -46.87348 | 2025-09-08 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b62f7411-1068-333e-93bc-d29229ce32ee | -14.79036 | -48.14747 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6756c74f-fd7b-3b66-949d-fe1ad760c1cb | -15.01618 | -48.00143 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2bbfc72-4371-3c64-9518-007b76aabc9a | -11.38675 | -43.54011 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ffe87ba2-8dd0-327d-a22a-4009e338e928 | -12.60628 | -44.64525 | 2025-09-08 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b935a3d2-cd2f-383f-a29f-a9a5cf29b910 | -14.50552 | -48.8164 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65cda49c-d7ca-3e11-b400-22098588d3bc | -10.81377 | -47.74604 | 2025-09-08 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 767b0c72-8a91-3fcd-9c7b-0f8a4b9447b7 | -14.99262 | -48.01761 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45fa27c0-2d93-3b5a-966c-69c3121cda77 | -9.81939 | -47.77215 | 2025-09-08 03:40:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ac3926d-7ecd-3423-9b80-a8cebcdb0fd0 | -11.27698 | -46.44799 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 07331a76-f664-3ca4-8c75-bd4b844b70b9 | -15.00007 | -48.01411 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1c17872-9e05-3c8c-9924-c7dc6f53b0e8 | -16.08301 | -43.63361 | 2025-09-08 03:40:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 171fce1e-c228-3fcc-808e-8eacea386276 | -12.52415 | -45.26211 | 2025-09-08 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3296f988-a95a-353c-aba6-6ae6fb695f11 | -16.3572 | -43.64225 | 2025-09-08 03:40:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5fc254f6-1365-3005-bca4-e489b58afa5c | -11.40965 | -43.59036 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 284a350b-6477-3697-97de-f72cc67bc9de | -14.29177 | -44.87523 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71d1e1fc-06a4-342c-9af2-122110d9b485 | -11.03336 | -45.95258 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| af61d351-895e-3cd2-b36b-d61daf70ca8d | -13.6469 | -43.80865 | 2025-09-08 03:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0381cda9-ab76-34bc-abe1-84961dd5711c | -11.42568 | -43.64918 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5070fced-21b1-398b-8723-632eaacc04fd | -11.42383 | -43.65886 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f148bc9a-ecb3-3354-8a6b-add0895444f5 | -15.29614 | -43.37836 | 2025-09-08 03:40:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b539c9d3-bd75-3d50-b5f6-f1771f96c0d4 | -15.53525 | -48.18358 | 2025-09-08 03:40:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d90ae16b-0c10-3e7d-9864-e4d4ff8635c4 | -11.24416 | -47.56744 | 2025-09-08 03:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9165ee52-0535-3314-a6d8-9da284c03747 | -11.42629 | -43.64594 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 308844b2-b85f-3d64-8d7a-ab8628320b2f | -13.82535 | -46.25336 | 2025-09-08 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 771b9ddf-fd8c-397c-a107-3eea0ecec4b9 | -14.60014 | -48.09258 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bce2c065-55b6-3fd5-b662-a27090ee1cf0 | -11.28743 | -46.46078 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| de072f63-6baa-34ca-bcea-ba9c819caf0f | -14.60294 | -48.07973 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5e45973-0131-388c-a0b9-bc8c6f9e0c39 | -9.8817 | -46.53865 | 2025-09-08 03:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7fc88970-aa43-348a-97db-1e78dd4b8204 | -16.28415 | -45.68581 | 2025-09-08 03:40:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3114ff1c-6be7-3a71-9d86-659f52aa5534 | -13.73547 | -46.90206 | 2025-09-08 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b102ff79-1df0-305c-ae3d-8f3d0df08f05 | -8.8248 | -45.89485 | 2025-09-08 03:40:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fda80fc2-eb1a-3f40-95ad-4c84a31f8ad3 | -14.28842 | -44.8639 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38a4fe6c-8aa4-33ba-8945-8f0058fc9efd | -13.82714 | -46.24465 | 2025-09-08 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f738bc94-0b00-30d5-a946-71f1cef57777 | -9.33471 | -46.53418 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 670832b1-ed05-3999-b449-a42778ea062f | -11.83377 | -46.76503 | 2025-09-08 03:40:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fee1cb15-d0eb-35ee-a6d0-aadb6571eea4 | -11.28034 | -46.46385 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| c5351ca2-0959-3472-b4f4-bf8cdf6103cb | -11.28507 | -46.45946 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 46212c3c-5a23-3507-8221-7d42df4c0264 | -16.295 | -45.68819 | 2025-09-08 03:40:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e80c071c-35c2-376b-996e-007d2c7cbd95 | -14.73842 | -47.76763 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b1e89ee-524c-3e98-a157-6d9dbda00f3e | -14.60105 | -48.09158 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7133a3a-e849-3152-8227-4a0bfd1d3e9c | -13.35734 | -44.43172 | 2025-09-08 03:40:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f208263-e8ff-3681-809d-e51f35b5dd4e | -14.29378 | -44.86497 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bf761b6-0e9f-350e-a740-7b04fb289967 | -15.0876 | -48.13744 | 2025-09-08 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 90813883-8349-3a12-af33-0ac8d4b8208e | -10.29368 | -48.81438 | 2025-09-08 03:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cbe6ec4a-429f-3cd0-bd3c-40c37e8c87b2 | -12.80942 | -47.99517 | 2025-09-08 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1d30a9ce-d0e9-346f-9acd-a3fce2ee1de5 | -8.6982 | -45.31077 | 2025-09-08 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 2c0dbd20-94f9-378e-a2aa-07e31e47a1e9 | -10.14042 | -46.21766 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4427671d-529a-328c-b3e5-127a0f29c01f | -11.42293 | -43.63528 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 598d35e1-bd94-3e5e-932d-6ed59a89c32b | -13.03176 | -47.1271 | 2025-09-08 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f92847af-d628-3ba4-86af-54411c63527f | -15.12998 | -48.06752 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c329d53f-3a3d-3e5d-a6e7-90684a2f7868 | -14.60244 | -48.085 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 165ad269-3cf7-370c-8119-b7007e89d3f5 | -12.8385 | -47.98874 | 2025-09-08 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d7ce22b-57da-3531-b959-9fe2cd4a9471 | -15.38327 | -46.42577 | 2025-09-08 03:40:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0dd3d80-1ec0-3bea-8339-9de1be7c3d0a | -13.64178 | -43.80796 | 2025-09-08 03:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 61e1ee2c-7a47-3a9e-b299-abab3c96220a | -8.74577 | -46.68373 | 2025-09-08 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3469fce4-60e6-33f0-8c84-39eb7762f1b8 | -11.27988 | -46.45304 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b6381d8e-7966-3c96-9604-f3ec6882b1a8 | -13.03811 | -47.12816 | 2025-09-08 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9347acf5-d34c-33e3-be75-fe287de46e82 | -13.64746 | -43.80578 | 2025-09-08 03:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 266ac19d-0559-3ffc-8e7d-5075ed831245 | -9.20834 | -46.05704 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f291c04d-64f1-3905-878f-47aeae59ac26 | -14.30053 | -44.86882 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98ddf596-77bd-33de-a209-b7d6b6d0192c | -11.27792 | -46.46267 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 30fa6d5d-0bda-35d0-8261-78753112d44e | -14.59041 | -48.0751 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85d2ea30-47ab-3a71-95b6-73ab0595c55f | -16.34151 | -43.03615 | 2025-09-08 03:40:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc959511-d9f4-3092-9238-171dad2dc07b | -14.99151 | -48.02276 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3628b5fb-0f49-318c-a88f-3f5bdc2e8d87 | -9.19761 | -46.04514 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9de76982-7ce4-38db-962d-b5357fa35934 | -11.83165 | -46.76215 | 2025-09-08 03:40:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ce47621-b797-3bc5-920d-74efa102fdc0 | -15.08878 | -48.13212 | 2025-09-08 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f61623bb-168b-32ad-a081-2569f7ca21a8 | -15.16186 | -47.9833 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bdd71a9-0186-3366-894a-9882bb102d4d | -9.20511 | -46.04026 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2885a433-8189-3e8b-be90-c38771c0d1ad | -11.40614 | -43.58232 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d57336f-3acf-3a31-8295-cffa8b69bd26 | -9.20425 | -46.06456 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9630d982-dbfe-3ded-b099-ceab79d59821 | -13.00553 | -45.21385 | 2025-09-08 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a22e415-2be9-36a0-b31f-da7b4b46d84a | -15.18586 | -47.96495 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b518d002-3ad8-3bfa-9656-4128ea1ab330 | -13.81678 | -46.26513 | 2025-09-08 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d69f75f5-e2e3-36c4-b148-baf6d82d545f | -15.01508 | -48.00659 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad1a84fa-d42c-3cef-9bc0-9f2f9fb74410 | -15.18873 | -47.98238 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 110fa682-750b-3e9f-b33d-9e557f1a4898 | -10.77512 | -46.0148 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 898aa14d-9a27-3b74-a629-e1238c0a33f4 | -11.28206 | -46.47424 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 239665a4-d730-3ff8-b1e8-372254d51f5f | -11.03429 | -45.94785 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 54cb0622-04a9-3a83-99e9-373037106039 | -14.78276 | -48.11764 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ad032b0-e87f-3fab-951d-55157bc868df | -9.20284 | -46.0376 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 064ca88e-f21a-3126-83c2-55c6d2ce8760 | -9.20918 | -46.03857 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README25.md)
