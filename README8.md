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
| 76c3c4d1-d76f-3b6e-a20d-7ce0e945e41b | -6.4441 | -54.948101 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35db5902-d3d5-3525-b43a-34eb1a2af68d | -6.8687 | -59.011799 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d822c07-15ce-390e-892c-02a3a297e508 | -7.3792 | -55.1633 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1a3e249-516b-331c-984c-5251b36bcb41 | -11.1062 | -44.424702 | 2026-08-25 00:32:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13c25a06-b569-3364-a922-f0a270e3912a | -4.0409 | -48.933201 | 2026-08-25 00:32:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 321f5796-8f63-3a17-ae0e-a49d60dbcc6f | -6.5895 | -52.449799 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1ba6ab-5bdf-3cc2-8080-0892cb0180b5 | -9.4744 | -56.890999 | 2026-08-25 00:32:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 310cce51-a0a9-3ed6-9e50-20dcb453b27f | -8.5763 | -55.263901 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aaa2b34-ee87-3ff5-8e81-547b9b1bbbd5 | -6.6979 | -52.075699 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef7861fe-f5ad-37ba-ab92-e9594511b25c | -6.9568 | -52.787399 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aaf9e1b-f8c6-3383-961a-31372ce604f5 | -6.1836 | -57.7243 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecddc08f-8eeb-3ffc-8cb0-bd64042cb2b7 | -12.76 | -44.252899 | 2026-08-25 00:32:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e61f3f19-b95a-3e14-a688-09d9ee2a854b | -12.7183 | -46.452801 | 2026-08-25 00:32:00 | METOP-B | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 933d408e-cb09-3b2d-9e35-2aaa08716c76 | -14.8647 | -52.6367 | 2026-08-25 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7afb979-b8fa-3e41-876b-d3cd87f9e181 | -6.8077 | -59.671001 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3de9d277-de54-39c6-b38a-0f8f28596530 | -5.9455 | -53.583199 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebfda878-4b21-3f5e-936c-15cae2c94d19 | -6.3432 | -54.732101 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d8bb136-73a1-3e69-8b2a-bcae2a5559cb | -10.5233 | -50.763599 | 2026-08-25 00:32:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9fd108a-6a32-33d6-9f66-e06bdda99043 | -7.5475 | -61.3627 | 2026-08-25 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 6bafcf0f-99e5-3c63-8460-3e7f1f96f59c | -10.3723 | -45.0767 | 2026-08-25 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 146c7897-b1da-354b-9ae3-22826a09d417 | -11.4494 | -44.5353 | 2026-08-25 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 87622080-99cc-3ea0-a8b4-2a1d00b05fd4 | -12.799 | -44.2544 | 2026-08-25 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| f52b28bb-3945-34d2-83ff-3ba66e3ff936 | -11.4306 | -44.5148 | 2026-08-25 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e37ba36a-d25d-30d4-92e2-4c34925a29e3 | -7.4286 | -43.1182 | 2026-08-25 00:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 178.2 |
| 8949b82a-d124-34e6-b40a-d4494b296920 | -7.2474 | -45.846 | 2026-08-25 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| a17d9a05-f490-3e35-a270-e0f4683d57a7 | -10.3918 | -45.0512 | 2026-08-25 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| f3af4e31-2a9e-3778-bfec-7d7a1af5c4b2 | -7.2659 | -45.8668 | 2026-08-25 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ad9cf60c-c959-3047-82ee-4a34a9a972d1 | -3.5221 | -48.1896 | 2026-08-25 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 83240e51-7063-3fc9-9c79-c11ffc8ebf9d | -7.2856 | -44.0875 | 2026-08-25 00:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| ee5ba69e-9b24-3546-9b20-9d0413b00462 | -16.3946 | -49.9191 | 2026-08-25 00:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 34d1f3f9-e834-3a23-bc3a-99af94274af8 | -6.6227 | -58.4801 | 2026-08-25 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 2dd97029-544c-3afb-a2c9-855593675b26 | -7.0058 | -59.2382 | 2026-08-25 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.6 |
| c3bb2e54-b77f-3fc1-a4b0-19c45d954f01 | -8.0695 | -44.6552 | 2026-08-25 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 51329385-f3d2-3c9f-9f37-cf6674b09ff9 | -11.4302 | -44.5382 | 2026-08-25 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 85f246a7-83e1-3b16-9a64-7e51a55b9a46 | -6.6409 | -58.5181 | 2026-08-25 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 5e959244-f5bc-38c4-a67e-31162fdccd00 | -4.0552 | -48.963 | 2026-08-25 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 736624a4-c516-3c15-bbfa-660e144558a0 | -6.1743 | -53.4834 | 2026-08-25 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f31fbd32-2c8c-3c8a-a8cc-9aced361b9ee | -12.7224 | -48.3842 | 2026-08-25 00:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 19ec1b91-2824-32cb-a0b2-80fa5880d4fb | -7.2858 | -44.0644 | 2026-08-25 00:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e5ce7526-421f-3d0b-982f-2e8edfde72ae | -7.0057 | -59.2575 | 2026-08-25 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 98fb6413-5e03-30e2-9451-f8b205185838 | -3.5407 | -48.1673 | 2026-08-25 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 25e14838-1645-384d-a655-70a5f30a9c21 | -3.5406 | -48.1889 | 2026-08-25 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 140f0e3f-5d06-32a7-aef6-930c64bc7367 | -11.4498 | -44.512 | 2026-08-25 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| e9fa375a-8095-314d-84f9-0b774a1d71fe | 2.58 | -60.6973 | 2026-08-25 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 7629f97b-da96-3e79-8c78-7d4472b774c4 | -6.6226 | -58.4995 | 2026-08-25 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 143.7 |
| c97f1617-b5aa-3686-8c29-948b1a43bf77 | -11.1447 | -44.4632 | 2026-08-25 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 74f95c20-2dde-380f-8a12-3e70aeee2ed5 | -7.2901 | -45.3683 | 2026-08-25 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 894981db-5bf7-3ec9-81ff-9788e41e477f | -7.2713 | -45.37 | 2026-08-25 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a875d555-9140-36af-a043-f41c91f3c7e6 | -10.3536 | -45.0561 | 2026-08-25 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9fd7f3c8-c98f-3b23-9f10-74b6e361fa4f | -7.2661 | -45.8443 | 2026-08-25 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 243.0 |
| 75d781f7-ddb3-346c-8e2d-317a4723ad23 | -12.7792 | -44.2812 | 2026-08-25 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| a80d85e4-f14a-3ebe-ae32-78c8767a1e57 | -6.8008 | -59.5934 | 2026-08-25 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| fd693390-353e-3e20-a2fa-1f189466697d | -6.6411 | -58.4793 | 2026-08-25 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 192abade-6b60-32cb-8354-3cb979d8cb73 | -11.1443 | -44.4865 | 2026-08-25 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d4527108-0fdf-3b17-a094-6eaa786906ff | -10.3731 | -45.0306 | 2026-08-25 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| e25df6bf-e801-3241-8c80-cf05731e2caa | -6.641 | -58.4987 | 2026-08-25 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 317.5 |
| c3d250ec-49ef-362a-b5bb-ebae2c8d1e68 | 2.5983 | -60.697 | 2026-08-25 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 67d7273b-edb1-3e46-a21c-308fc5850700 | -12.7797 | -44.2576 | 2026-08-25 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 5bf99ac0-3eb7-364b-abd6-ba32db55be3d | -7.2471 | -45.8685 | 2026-08-25 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 89fa74fa-7b03-3d73-9a16-f9dc96b7f7c2 | -10.3727 | -45.0537 | 2026-08-25 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 545.5 |
| 643abca8-b43c-346d-8a3e-46144407db0f | -7.4474 | -43.1163 | 2026-08-25 00:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| 0b18d325-0453-35d9-b8f7-64108505f8c4 | -7.4289 | -43.0947 | 2026-08-25 00:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| be0ee7b7-5777-3220-9d8a-a71ff67ea8ff | -23.02617 | -52.66331 | 2026-08-25 00:43:00 | TERRA_M-M | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 37817e91-cf35-3ee5-a5eb-c9af1e316703 | -17.60003 | -50.90725 | 2026-08-25 00:45:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 43.1 |
| d6fc5bc1-f4c9-31ef-8bbd-ca3bcb7bb0d6 | -15.2383 | -52.81065 | 2026-08-25 00:45:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 664c4d52-e723-324a-a151-95ca1e71879a | -17.31483 | -54.92518 | 2026-08-25 00:45:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a5bec4a6-2870-3fa1-afb3-14a7a06ef105 | -16.3932 | -49.92406 | 2026-08-25 00:45:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 7d5c9662-47f6-36b9-bd5e-f6a3b48c6d57 | -16.37966 | -49.93349 | 2026-08-25 00:45:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 3f08bf90-93da-301a-8312-9e95d9ae6b81 | -16.37841 | -49.9273 | 2026-08-25 00:45:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 8e842273-25ab-387a-8fc7-01cac16ce152 | -16.49642 | -54.67229 | 2026-08-25 00:45:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8e813b6b-1e4f-3f26-bdcb-65cfd1227a4c | -8.53692 | -55.30664 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 31a1c815-2177-3a37-b13b-13330cbe9a57 | -11.16128 | -54.0117 | 2026-08-25 00:48:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 22df16b3-4336-3679-964e-7b6680fed3d5 | -13.87182 | -54.04553 | 2026-08-25 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2e9685ca-db7d-37f0-8adc-634dcce05f5a | -7.49681 | -55.36157 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 9105dcb4-e278-34dd-b73f-5bd87a336b28 | -9.06311 | -65.39213 | 2026-08-25 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e2cb9efb-0603-3c8e-b134-c5e39f16df76 | -9.67907 | -55.0927 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 3f8eff75-af16-350f-8712-cf21c2115662 | -10.93696 | -51.06138 | 2026-08-25 00:48:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 40782c5c-44c5-3683-8f4f-6bca03660f67 | -8.57824 | -55.27777 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| bfe0bbc1-7acc-3f4d-a35c-90af23f2180b | -7.49922 | -55.37716 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| bdfa5a38-edcd-330b-91c3-b77f3832c6bc | -10.92679 | -51.09398 | 2026-08-25 00:48:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| e7a9ad26-9157-3a55-860d-234d6dc78546 | -9.4749 | -56.91016 | 2026-08-25 00:48:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| eb29bbc8-f587-30e2-a44a-d3b0ad2be643 | -9.48479 | -56.90856 | 2026-08-25 00:48:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 463d94d1-8ebd-3b7e-a79a-6fb44a343777 | -14.31868 | -52.98003 | 2026-08-25 00:48:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| bb99aeb3-e38f-37ab-90ca-27441ef78524 | -8.61007 | -54.74021 | 2026-08-25 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| ba0d9898-5017-3fa7-975d-e2cc1324ee9b | -8.60151 | -54.7301 | 2026-08-25 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c573af63-b524-31b4-8101-e9299366b969 | -14.92239 | -52.65443 | 2026-08-25 00:48:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8296edbc-f2a7-3e05-963a-8d3b845ddcf4 | -10.47537 | -50.44052 | 2026-08-25 00:48:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e609ccbf-19aa-3220-80a5-1bc32f562cfd | -10.91165 | -51.0967 | 2026-08-25 00:48:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |
| bd313e01-859c-36f7-8bdb-3f8d4ba71a36 | -8.54826 | -55.30481 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 79095493-19e1-36c7-9378-5157ae6218a3 | -8.59557 | -54.72529 | 2026-08-25 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 8c553f00-2ff5-31d1-8525-66e4db0ff413 | -8.57199 | -54.855 | 2026-08-25 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 1da4a6b3-9d3c-3c1c-a249-2ae20952099e | -9.06504 | -65.40806 | 2026-08-25 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| c0190326-0a21-372d-9cda-419ef4acd036 | -8.57451 | -54.87146 | 2026-08-25 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 40450cda-9e7d-3cfb-bf39-fc929d571ff2 | -10.94931 | -51.05376 | 2026-08-25 00:48:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e51ae161-88dc-34dd-8e03-461c83eb22c3 | -8.57998 | -55.28399 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ab18296e-f04d-3931-9387-e157f341b903 | -8.62193 | -54.73838 | 2026-08-25 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| e1dd2593-0aaa-3f44-a914-c391ea74cbbc | -7.5019 | -55.38338 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| bb13274d-80e5-3309-976a-b2820b23385f | -9.16848 | -58.32937 | 2026-08-25 00:48:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b6220c40-f91c-3c83-bdf4-17166ba786e6 | -7.4996 | -55.3677 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| a1be51bf-d0c3-3e11-a721-3c19263cafb3 | -9.15053 | -59.57171 | 2026-08-25 00:48:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README9.md)
