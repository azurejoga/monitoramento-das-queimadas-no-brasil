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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd775642-8d3d-32ec-bacb-6f88f01e70ae | -12.7001 | -54.71456 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 2b13b7f2-ca79-3049-85af-72217f083dce | -14.43773 | -43.20681 | 2025-09-14 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ca1d81b-efdc-30dc-9388-9cc6d7965c7a | -16.54477 | -49.20795 | 2025-09-14 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ba6deed-10bc-3adf-973a-a14847bc60db | -12.67378 | -54.66872 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 65c71839-bedb-3976-8120-7ee88d1056de | -18.14405 | -49.1875 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d786f4ba-99ad-3dca-aaaf-426240f5ee5e | -12.68472 | -54.69344 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ef30ec3b-fbb5-3c7a-9888-db1a8be9f5df | -17.43489 | -49.22068 | 2025-09-14 04:42:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5ade539-c576-3af5-8d1d-d44e042d4e20 | -16.1413 | -49.94921 | 2025-09-14 04:42:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53defcdb-4c69-31ab-a2f5-32ac7dc2f871 | -15.7765 | -52.22577 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1796bff-acd3-3332-ad1b-25d607ad65e4 | -16.33499 | -51.52767 | 2025-09-14 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e3cd1e5-506d-383a-945f-90c04e55c3a9 | -14.16583 | -46.15691 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f40fcee-48eb-358b-b1eb-87ef4f1a519f | -16.33335 | -51.51638 | 2025-09-14 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 239eecbc-373d-3b69-b752-59bf8767cec1 | -18.61753 | -50.39746 | 2025-09-14 04:42:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e00bf0fc-5f81-3405-957e-8fc79270b9ad | -12.91299 | -54.74431 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b54df93a-e406-3a64-8670-621acd8f90d3 | -15.58474 | -47.12608 | 2025-09-14 04:42:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38a6fb0e-f0da-35b0-9348-c6a1feb9ff27 | -19.64384 | -45.37795 | 2025-09-14 04:42:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd202a5f-d5f0-376b-809b-2c527f00a32d | -14.63707 | -52.02747 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dddd454-6470-3c42-9c37-7c0c58a8dc5b | -15.1926 | -52.47031 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae3226d9-9243-35bd-ac35-7171d6e77f91 | -15.80034 | -52.204 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b6ce0ead-090b-34e1-96e7-b8409c356aec | -17.31958 | -46.08833 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74f1ba83-cd84-3799-abc4-30d0999a48c8 | -14.76711 | -60.22006 | 2025-09-14 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ecfb071-5f14-33f7-944b-1f5298735416 | -15.64817 | -47.04393 | 2025-09-14 04:42:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c372be4-b721-3fa4-a046-01e26a0eecc5 | -12.66338 | -54.68509 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 0f9f243f-dc55-3ef4-a643-e8000984e4c7 | -16.55827 | -49.21411 | 2025-09-14 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d1b0f67-6ff1-3b95-8044-924cb64c50b7 | -14.82219 | -48.76744 | 2025-09-14 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc704712-8a4a-3b99-883d-6553e29914c4 | -13.26261 | -51.68198 | 2025-09-14 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfaa7f62-1831-3fc4-900d-5416ab1f2211 | -14.39655 | -52.90843 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca2af6bc-16e6-30ee-89b8-54beefc7b70d | -14.21848 | -46.31496 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 822155ba-fd28-3b4b-9dda-bcecf2b4ee3a | -14.1525 | -46.25845 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aab8655e-c5b7-3a30-a3ad-1ef2e6ae9391 | -15.09909 | -52.502 | 2025-09-14 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c378e62-73a3-310e-aec2-c18fbc833edf | -14.15698 | -46.25547 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 02a5daea-5286-39f3-a681-b677b62e9f49 | -18.35783 | -45.02038 | 2025-09-14 04:42:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1588bc67-41b1-3dea-a015-9e7898a468d3 | -16.09347 | -49.98525 | 2025-09-14 04:42:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ae6cd75-7ff5-31b2-b12d-68cafde0a3a5 | -18.46806 | -46.93817 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 748d22eb-ca7a-33a6-80c9-9dc1f6a6c895 | -15.29496 | -53.77482 | 2025-09-14 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7084567-ed2e-3d19-bb07-bfa3f649bed6 | -14.40725 | -52.90649 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c233fe54-868d-3137-8dd6-37fe821f6479 | -16.36164 | -51.77064 | 2025-09-14 04:42:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48b4d4f9-993b-3526-8b09-a445b5290806 | -15.16251 | -52.46846 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 137a5e8a-a6a4-374a-8146-427212b134a6 | -14.17827 | -54.05227 | 2025-09-14 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6993c9c1-b618-3940-a622-35277607c6bd | -16.48714 | -55.12464 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 412995b7-d77f-30ca-853e-7f824032f5df | -12.69566 | -54.71833 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b1faa446-6f79-3c0b-b54d-e82dfcfc58ce | -12.70161 | -54.70562 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 302cf7f3-bec3-3aee-93ee-d6eeaa952ed1 | -14.16712 | -51.87917 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c6642f7-d228-352f-9107-25b4bee5f20a | -17.17315 | -49.38313 | 2025-09-14 04:42:00 | NOAA-21 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58410630-5fb1-3bbb-89af-23ec8502e0b3 | -13.88857 | -48.29568 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d23c4bc4-ee57-35fc-ba2f-58caa08be2db | -12.67302 | -54.67315 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ead62bd-2490-33ee-8494-f20c919a5582 | -18.1482 | -49.18399 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5fae631a-a33a-3b25-8260-b54a6b5cfc57 | -13.58712 | -51.67405 | 2025-09-14 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80542a84-844d-3ae4-b7f7-42e5e984b30e | -15.755 | -49.78887 | 2025-09-14 04:42:00 | NOAA-21 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 469016b6-1a1d-3ff3-8f02-6477d1bcdb1e | -15.60372 | -47.94555 | 2025-09-14 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a79ea7e-1c67-3b16-a891-405a75295f8c | -16.48785 | -55.12041 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 53bd50ab-a4f1-3cf5-b97a-e4feeaf45459 | -17.36716 | -52.90059 | 2025-09-14 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fcf27159-9db5-3ea3-ba45-220b67cb4478 | -18.98391 | -48.59454 | 2025-09-14 04:42:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 383f7cdd-7a52-3d16-a691-8a12604e2c90 | -17.3158 | -46.0841 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7054b0ef-52e5-35e4-bc85-3bd88121740c | -17.31244 | -46.11108 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9e1cffd-989b-3d47-9994-fadc46bc49c6 | -19.09585 | -44.4934 | 2025-09-14 04:42:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a51724d8-5b30-30e5-a489-a0dee8056b21 | -16.65466 | -49.7673 | 2025-09-14 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cdd23e0-ea61-31fe-ab34-e7a317ce52e3 | -12.66046 | -54.68003 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 74cef177-ffc9-329c-b5e5-97b74f5cea63 | -16.56658 | -55.10299 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ef56fedd-82f7-38c2-9a52-3bace1e2abac | -15.40807 | -52.9738 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a66c809-e4de-3533-92ae-de6ce1f8eb15 | -15.77432 | -52.21808 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f6947e5-8610-3570-a70c-afb45a6e8230 | -12.67291 | -54.6959 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ded4854c-4264-3544-9479-da5e0afc5932 | -15.6917 | -49.91157 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3bb89b5a-2f0f-351c-9dd3-e06cf93e79b9 | -18.53434 | -44.94 | 2025-09-14 04:42:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e52e1a0-ef3a-3adf-9347-0ed7f0595759 | -14.46665 | -47.313 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bec3bf75-2bd1-3e4f-835a-4ab9ebab27de | -15.78424 | -52.21975 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4406f47-88b5-3057-a093-2c2276ee12ec | -14.6159 | -52.07506 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7e9fc24-36dd-3fad-b446-80377eb2ebca | -19.71551 | -45.44236 | 2025-09-14 04:42:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8c02044-3daa-3881-94eb-56a2f9addade | -18.47263 | -46.93388 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eef057db-5b97-3754-a982-d4d8b8799ba9 | -12.69133 | -54.69916 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 41bda4ba-5b2f-3ad4-8e54-055873be0beb | -17.83696 | -50.42004 | 2025-09-14 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5e1400e-b01b-3125-9992-849823276537 | -14.63669 | -52.11531 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e7f00e2-c7a9-3f0a-98ee-6fdd6c99a2c8 | -18.06938 | -50.74803 | 2025-09-14 04:42:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 377ca3a3-0cbc-3517-be5c-4d74312549b6 | -16.36495 | -51.77119 | 2025-09-14 04:42:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9417dc4d-883e-3383-8be7-9e539ff4013a | -13.92904 | -48.29301 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0f8bc641-842e-3455-b286-4cfaeea6cd73 | -15.93524 | -49.96852 | 2025-09-14 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83a75245-c63e-37a5-9628-2aa902d2f4e5 | -17.38689 | -52.92648 | 2025-09-14 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3c4c11b-a2ff-3986-8d62-dc453f2116ed | -18.00985 | -46.95546 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44697f82-4a61-352a-ab4e-d034e8efd3ed | -16.71571 | -54.95415 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32539107-ec5a-30fe-a026-ead80f1bf772 | -12.69426 | -54.70426 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f9a81277-bc7b-32f6-ba7c-c9bf36a88508 | -14.63337 | -52.11475 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e69eee82-5675-35a1-9db0-789260dab4e5 | -15.80422 | -52.20095 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fb2d4e4-03a7-36c8-9651-c107595eddf8 | -12.69122 | -54.7221 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 673aa881-88b1-3e4e-b3bb-ca01a997dfa1 | -16.715 | -54.95836 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d54df670-9516-345a-a07c-8b03190c09d7 | -18.0125 | -46.9668 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3bac00fe-3d04-3085-bbd4-69e9b355a21a | -14.19778 | -46.16441 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6151ecb1-e75c-3343-b6ea-91162e83ed3d | -12.69794 | -54.70494 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6954427d-a533-30f8-b983-b046686ccaec | -16.83546 | -40.84949 | 2025-09-14 04:42:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 2d4aa99e-2e2a-3c89-ba9a-db297bb817e9 | -17.25846 | -49.2681 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dcf48a7b-120b-38e5-9c8b-e19330b686d8 | -15.12639 | -52.48085 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9b37f09d-2ee2-331e-91de-d9ac0453d1f2 | -15.8671 | -51.84527 | 2025-09-14 04:42:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f387f7f9-05aa-32c1-8484-f97866156478 | -18.15418 | -49.19337 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| de7e409b-a38b-3988-9f25-e16e5641a185 | -14.1973 | -46.16798 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e10e3121-d709-3b71-83a8-654f68c6448d | -18.91517 | -48.01043 | 2025-09-14 04:42:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b50fc61f-89f6-3dbd-80fb-f3f0af3d8004 | -15.63736 | -44.37841 | 2025-09-14 04:42:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d12fd1ef-fbfe-3244-984f-f5f42c0f2d1f | -15.65237 | -47.03721 | 2025-09-14 04:42:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d75e0b70-c981-3212-b1ff-b018f88366df | -17.96725 | -46.93385 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd972070-83aa-3f25-a67e-6578948e46a2 | -19.72707 | -45.86832 | 2025-09-14 04:42:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c26906ed-9903-3ba3-8775-0d4e116deec0 | -14.36418 | -52.93711 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02348971-11cf-3799-a0bf-3ea39a0b27cd | -15.43006 | -58.77534 | 2025-09-14 04:42:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README48.md)
