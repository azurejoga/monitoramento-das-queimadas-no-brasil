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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85afd628-1f1a-3854-ad81-5570cc434e64 | -10.15297 | -44.52812 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2da4d006-8f80-348b-a672-bad93a920b36 | -12.4805 | -47.03025 | 2025-10-18 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1e2b7bc-e165-3f26-90a9-a70d7c7152ee | -14.91748 | -46.71727 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01bc6985-9cb0-30e7-9fd7-f7984efe11f2 | -13.22498 | -43.97741 | 2025-10-18 04:51:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fac3475-f8a8-3920-8d2f-410de8259441 | -14.90441 | -52.3898 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bd3bf1f-b2e0-3fa3-abe6-826c379dce77 | -10.5348 | -49.55196 | 2025-10-18 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 354315c8-cdda-3d33-9e47-61deb09dd1c5 | -10.88223 | -47.46372 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6f97502-6aa5-3c93-b470-c0585e92a257 | -12.74678 | -48.63106 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85c31089-e3f5-3b18-b445-0ad778e2903b | -11.00332 | -47.89855 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44ede4a8-ec65-3915-805d-7d3fbb6157b4 | -13.92527 | -45.59751 | 2025-10-18 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 843ebd73-11fd-3f74-93fb-089fc9c0325a | -11.37495 | -45.27526 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0db1fe4-89e9-394b-8f3a-cc7fd2685436 | -10.71897 | -48.1487 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be9e5b72-37d2-321e-bb5a-796c400236c8 | -11.36648 | -45.2622 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3828823-05b5-36e5-a8c1-bc5c790f8523 | -12.45969 | -45.47824 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9b73c6e-b9c3-34a3-988e-3cc64bc4b170 | -14.42695 | -48.06086 | 2025-10-18 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbf9169a-c395-3f2c-8bd3-f3b66b9bf3ea | -10.61836 | -42.30479 | 2025-10-18 04:51:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4d3ab514-074d-3abe-ae7c-2b683e1e3fa2 | -10.95998 | -45.45243 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d18c4105-3564-37d8-ab49-228ddc8627a9 | -13.51668 | -48.00816 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d5ac3a0-c380-3492-b7a3-6b143912fd0e | -13.04125 | -48.18829 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7517d90a-d2c3-3dfa-825b-da2e3d6c409e | -10.24829 | -44.04827 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12e131e7-5731-3734-851b-ce088b77a630 | -12.57214 | -43.76797 | 2025-10-18 04:51:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61c18ba3-0eeb-3beb-b8fd-06dde866bbfa | -13.27231 | -46.44085 | 2025-10-18 04:51:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f137cce-0295-3fdd-b5f4-7f4275c21a94 | -9.81657 | -47.75182 | 2025-10-18 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ef6f7e8-167c-35b6-8a8a-a0e88a86ae8b | -10.61781 | -42.30931 | 2025-10-18 04:51:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a50733ea-9bb6-38c9-aa60-d8df9bc4194f | -9.89048 | -47.64972 | 2025-10-18 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e34239c5-5783-3b5b-9b99-9c855713738f | -10.53292 | -43.3707 | 2025-10-18 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c74a4fe-d91d-3686-b8fe-76a9967e6922 | -10.43021 | -45.01731 | 2025-10-18 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81250baf-009e-3769-b761-0fd08e8e7b53 | -12.9102 | -48.58705 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15efe042-1481-3775-a62c-9aa784e86ad4 | -11.00282 | -47.90214 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9980a9ac-4303-3e5a-bc79-e29e37228232 | -11.75261 | -61.07213 | 2025-10-18 04:51:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f85c5927-c824-3223-bfc7-9c9457f87994 | -10.81241 | -54.61253 | 2025-10-18 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb0794c1-2714-3b88-85f3-655ba47bc31a | -13.07882 | -43.06479 | 2025-10-18 04:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 04252517-e627-3804-a4d1-f9e600f6e040 | -11.73027 | -59.31817 | 2025-10-18 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04cb3e67-e12c-3bb2-84c3-8b429749f8ac | -7.49668 | -63.51674 | 2025-10-18 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d79eac7c-cf9c-3799-ac71-968190b25064 | -14.14462 | -44.24603 | 2025-10-18 04:51:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7dad4fee-f41b-3b08-91ea-56b79be22509 | -13.70217 | -47.71732 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 490522c1-a9fa-3cba-8e10-abce07ce4805 | -10.91265 | -47.86797 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0e811394-d692-3556-a4ac-df14945281b8 | -12.24341 | -49.37026 | 2025-10-18 04:51:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cb701a8-e7d7-3d32-baa7-af1e66cad985 | -12.46043 | -45.47231 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9d01472-1720-305f-bdc8-2dd1a379c584 | -10.98082 | -44.3299 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92066361-ef9c-387c-9688-d7130d9d18b3 | -12.46582 | -45.46997 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3cc22562-f28e-332d-9fc9-2925fb65b19f | -17.8469 | -42.62538 | 2025-10-18 04:51:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b51e6250-df93-396b-a976-16bf58f234c8 | -10.9817 | -44.32324 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bfa6c61-c650-3f63-9c6f-b6ec049c9816 | -8.63046 | -54.71418 | 2025-10-18 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30da44fd-e2dd-320b-9500-3ad4ed5e07a8 | -10.22839 | -44.07539 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89b57dbb-4197-363b-8273-c03239d86692 | -10.49151 | -43.42729 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a73189c-7a2f-375c-abfe-e09e621a558d | -13.4658 | -47.40727 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e0ce7de-fe63-39d0-8ac2-0b42f8663b96 | -10.48919 | -43.44567 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6572cb41-5700-3d18-ac66-64d516ebc78a | -10.41834 | -44.91285 | 2025-10-18 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 062855ad-6029-3fe6-98c8-2cfceebfeeba | -10.15254 | -44.53135 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37a1297b-32ec-3040-9914-94fafb9b5c55 | -11.58518 | -44.05463 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f98adfb0-0515-3f99-bdda-8e8269e85031 | -10.69406 | -44.56036 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8e92788-e4be-3562-a7ce-391bf10ed525 | -11.48648 | -44.16666 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8154ee36-d133-3b20-847b-92b6968b6316 | -13.70161 | -47.72161 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 054e7a13-01f6-3b4e-b4fd-349c41a11e6d | -13.48619 | -48.11493 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79e268f8-8ce5-34ea-bc43-48d1d0c961b4 | -11.40151 | -44.27834 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64f10b41-1c3d-3ff7-b0f8-990e8759999b | -12.60453 | -52.83626 | 2025-10-18 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c7f71ceb-5524-34b2-b3df-e104e0743877 | -14.12758 | -44.7139 | 2025-10-18 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc072410-1a50-3fcf-91dd-9c1ea5020c8b | -13.47611 | -48.12527 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e77843ba-15e5-369f-9655-c6b8241b498c | -15.08715 | -44.00723 | 2025-10-18 04:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e98c245e-0031-3dc1-8f5c-8067fffa4678 | -10.40765 | -58.02055 | 2025-10-18 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e58156c7-13bd-3146-8f40-8a7c0a19318d | -10.98187 | -47.93059 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3478203a-c046-3ea8-a8ee-4b6172e83a4a | -16.18673 | -46.9578 | 2025-10-18 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69e4ed37-2ad2-3445-90b1-f3414e82cb10 | -13.00439 | -43.85312 | 2025-10-18 04:51:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72382ecb-1d0e-3a5e-9341-76c866229233 | -13.44237 | -47.98862 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8344a773-71f1-3f81-a174-96fa022500d3 | -11.73096 | -59.32038 | 2025-10-18 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1108f91-654c-3a07-b87a-12a89c1ebd2b | -9.29472 | -64.22826 | 2025-10-18 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ad88a20-dd81-36fa-bf01-c3ebe53cce02 | -11.20288 | -47.83001 | 2025-10-18 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 048c52f6-cf62-3f96-b312-448366403c0a | -10.91314 | -47.8645 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68bcf34a-216d-3cf6-818e-be30fd5404e3 | -13.04072 | -48.1893 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d60877cb-ecce-3bd6-90dd-f04bf848bd56 | -12.15382 | -45.08779 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b890fcf7-006b-3333-9f6e-cfc29af5c174 | -15.97323 | -56.44467 | 2025-10-18 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ea8a1ab4-89f5-3879-a347-bd160729b67e | -10.28349 | -44.05503 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a90dee6a-2f4f-3734-b091-5ae0ccf39180 | -13.41279 | -47.98119 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d555937b-9d41-3106-a871-aa4924f955e6 | -10.46626 | -55.59034 | 2025-10-18 04:51:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c800dc5-8ea5-3c14-a31d-2b23b0f9b1bf | -13.73013 | -48.1203 | 2025-10-18 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dfa42fb-e3c8-36fa-8c76-08aa0167eb6a | -15.717 | -56.84444 | 2025-10-18 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d1ffdf6-f490-357c-bbc9-28aa20545266 | -13.76815 | -48.22492 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50528626-4b53-35ca-b210-6c19cee2f6c5 | -10.59104 | -48.00034 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 258a16cb-573f-3913-a60d-4c9d699741f2 | -10.49059 | -43.4346 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ccee0bf2-d863-3542-9843-528d68bc1273 | -11.51521 | -44.07034 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48ffdcc2-b385-31c8-9516-7938caa2b5ef | -10.23907 | -44.03545 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39dc7fa6-791a-398a-b357-e6566bf2bf7c | -10.53558 | -44.50716 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e70168f-fd45-33d4-85a5-3f1b7896ee1e | -10.6181 | -47.38318 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4db355e5-ca14-3307-a25b-a4b99141ff85 | -13.42573 | -47.98238 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf1975e0-792b-37c1-ab35-08c9b37fe76f | -10.69571 | -44.54769 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8be81e5c-ff71-3fe3-89a7-c537c0ef2af5 | -13.04383 | -48.19777 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc7960d7-8987-38b3-b7e7-65f587776aea | -10.71139 | -44.54947 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f9198c5-003e-3ef9-a8b3-ed8fcab68913 | -11.37034 | -45.27156 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d88216f4-326c-3200-a79e-8928efa4f99e | -11.45879 | -44.2124 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f938f7b0-3868-34f7-823b-e335dda63f99 | -13.72637 | -48.11583 | 2025-10-18 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb2dc676-85ab-3be6-bf8e-a30869cff128 | -10.8049 | -44.01737 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77ec5620-3b4e-3dc0-903c-3f08ba20e949 | -12.49255 | -45.50055 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ae8945d-483c-30dc-ae84-049292ca640b | -10.43725 | -49.47947 | 2025-10-18 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69251563-ddfc-3414-9cce-9f7831027bf4 | -10.3663 | -48.66742 | 2025-10-18 04:51:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01975765-f00b-3a9a-b8c4-fb1c06d676ec | -10.18338 | -44.53724 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 028ac87b-c57e-3c48-955e-8ef60664c84c | -9.22475 | -61.83258 | 2025-10-18 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cde488a2-58a6-3521-b866-272210a4e67f | -10.52995 | -44.5097 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 811dac9b-159e-341f-8e8d-94e99c800ef8 | -10.69488 | -44.55404 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4717a82d-545c-3ae9-8817-5f23c6b90b33 | -10.48591 | -43.42653 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README80.md)
