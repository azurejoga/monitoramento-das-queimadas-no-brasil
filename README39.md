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
| ffc43ded-622b-3d51-9fca-37fd5ec4afc2 | -5.97377 | -55.38182 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5b7049c-409b-3ad3-83eb-662e9e67a371 | -6.73531 | -44.14183 | 2026-10-03 05:16:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdf45be1-241f-3048-886f-b2871c15b1d6 | -6.07472 | -57.80371 | 2026-10-03 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7902aee-b94b-38ba-8a70-0a3c5639136d | -5.6139 | -44.37652 | 2026-10-03 05:16:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21b47a9e-a350-35fa-977f-eb029e69e76f | -3.54128 | -55.52961 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 712bfbc6-1023-3949-8058-7403ac11e3a2 | -2.15546 | -47.7466 | 2026-10-03 05:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7d84418-110c-32da-b5b4-8a3f32f61bc2 | -3.70254 | -50.97449 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90e4a198-00b1-37af-bc6a-3de68ac25c0a | -3.11886 | -53.74685 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eefb6808-3450-388e-a48f-d53645518f45 | -5.09788 | -56.25548 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 306345c1-31b6-3bb4-b520-3292aa81112d | -2.97065 | -53.26691 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d807562-9fb6-3516-957b-65a6cf27e962 | -2.96534 | -54.10303 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b126e1e6-1382-38d6-a51a-ead360b693d8 | -1.76697 | -55.02954 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b673713-c001-3ae4-97e5-d2d580296b5f | -1.26953 | -54.55827 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee337d87-bf1d-3871-8663-8a70cb9a9939 | -2.8604 | -49.62807 | 2026-10-03 05:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05638df7-a011-31ae-86af-26976b15c409 | -4.42767 | -54.84969 | 2026-10-03 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62d79498-0a50-3044-8b2b-676f2b199547 | -3.14302 | -53.74696 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbad7079-791d-3eb3-9058-c6d8233747e0 | -3.81778 | -52.20866 | 2026-10-03 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4430500-656f-3777-90b1-27f774a021ff | -3.71472 | -50.65909 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1b5af08-6da9-3fd8-9caa-2b120f9b2695 | -5.2981 | -45.79842 | 2026-10-03 05:16:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1f484ea-3cf1-32bf-81bf-98ce766b23b5 | -6.05354 | -57.70373 | 2026-10-03 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db51f43b-46b1-365d-bcbf-49f15686f8f3 | -2.86452 | -49.62872 | 2026-10-03 05:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4dc7d93a-04fd-3ebe-896b-66e724f68df5 | -6.40256 | -55.23546 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e56f2810-7fd1-3351-9a90-f68dd02a35f1 | -5.13955 | -45.57668 | 2026-10-03 05:16:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c418440e-de1f-37c7-8426-0cc5e22a60fe | -2.97407 | -53.26742 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2224c4d6-b216-344a-8b19-ea55887184f6 | -4.30289 | -54.80176 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f889288f-aaad-3020-a710-48df40d7a462 | -3.55645 | -53.2689 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb02fb81-7588-3210-9ab7-99bfb39cc687 | -3.12786 | -53.75555 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 021cee7b-e081-3fcd-b509-539f1ed4c402 | -2.93423 | -54.15557 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90a05cdc-a4db-3c9b-b3ef-3d4515666d75 | -2.15342 | -53.66305 | 2026-10-03 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8e3a95e-52ff-3f45-8f13-bdfbbdf30581 | -4.14444 | -53.94546 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b60fa2c0-7ca2-3c33-bfb5-f2786b189ae7 | -3.17984 | -54.09364 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e12ebc8-4431-31c7-9c2c-34d8e8c8e489 | -4.42394 | -55.74767 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c346943a-a228-34cf-ba23-f79e5b09fc6d | -10.9923 | -59.13417 | 2026-10-03 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7d8f50a4-e18f-33bd-be36-79790f5ada45 | -9.48363 | -67.1589 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fd239d9-481a-3b11-823f-3e6085471add | -10.87076 | -57.11178 | 2026-10-03 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 920d4097-2ba4-3e66-bb49-02ae30256150 | -15.23777 | -43.26603 | 2026-10-03 05:18:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 13.3 |
| b00f71e0-ee64-398f-9c63-8d855bc8b2c3 | -10.98881 | -59.13358 | 2026-10-03 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 94c6287d-f940-3f2a-a5ee-4a11f018b081 | -12.86134 | -44.71333 | 2026-10-03 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a226efe-2af5-32f7-b90c-4c465c5bc9d9 | -9.62759 | -65.73852 | 2026-10-03 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1c10ce8-c88a-354f-a9a7-8505fb1ccfc2 | -9.48713 | -67.15932 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90673e8f-88e1-39d3-b0bc-6a5d28e00ae3 | -15.23705 | -43.27396 | 2026-10-03 05:18:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 13.3 |
| fe7287cb-9ab7-3caf-b889-98229fb952d3 | -9.8832 | -65.14214 | 2026-10-03 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4281b1a-0d17-3dba-841b-3c34d9fe1290 | -11.04701 | -62.56996 | 2026-10-03 05:18:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 331bb68d-27f7-3c46-bcc8-a3b6a8a9c25c | -10.13947 | -61.74101 | 2026-10-03 05:18:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6c74605-929e-3844-9b43-284a411a9e9a | -13.50332 | -61.13243 | 2026-10-03 05:18:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8165c252-c337-3712-a700-5a981845384e | -9.54001 | -68.52698 | 2026-10-03 05:18:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea2c7203-a9b5-304e-bad5-9b15040aae3c | -12.85064 | -44.68921 | 2026-10-03 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15639272-731c-3ae2-9120-ae567436e3a6 | -10.87465 | -57.1088 | 2026-10-03 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 742d1f76-421c-398c-917c-865a6c88b7a9 | -15.24451 | -43.26958 | 2026-10-03 05:18:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d529b24e-74f6-3053-9346-ed964b7a82d1 | -10.84437 | -62.78 | 2026-10-03 05:18:00 | NPP-375D | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b545006-daba-3801-a28f-be114c5677ec | -9.62165 | -65.74071 | 2026-10-03 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0282ce9-e4bf-3460-871d-581d6f734147 | -15.23643 | -43.27648 | 2026-10-03 05:18:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 3ea6d8b5-7322-3438-a23d-463dcfc5515e | -9.37957 | -65.47036 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f97d2d50-fbac-3e2a-b3f5-54c02103eb3b | -13.50213 | -61.13359 | 2026-10-03 05:18:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07218928-a005-3461-856f-2c020d82de7d | -12.951 | -57.11406 | 2026-10-03 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 79d83316-f9a9-3556-ad1d-52905b34cd01 | -9.54637 | -68.52831 | 2026-10-03 05:18:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c0d5d2f-5c21-3911-8615-f34d000b9a2c | -10.1401 | -61.73732 | 2026-10-03 05:18:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 713c6322-547c-3151-b8aa-84c4e2ef7c17 | -9.62225 | -65.73742 | 2026-10-03 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae332b7c-c7b8-3d43-a611-2994f4f429d9 | -12.13232 | -61.15685 | 2026-10-03 05:18:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aca51761-de85-38cf-9d90-d07379b380cb | -15.23718 | -43.26872 | 2026-10-03 05:18:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.8 |
| f4c21faa-a83b-38aa-a0a1-f903851aad96 | -12.14589 | -61.16906 | 2026-10-03 05:18:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e51e6c05-c857-3aa8-9a83-81e6e27cf941 | -12.85474 | -44.71266 | 2026-10-03 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 58ca3700-d2eb-3c86-be0d-655ed8930374 | -9.93162 | -63.97911 | 2026-10-03 05:18:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a90010e7-07ad-3a02-9b4b-a1fe6ca3f9f8 | -9.9086 | -65.03444 | 2026-10-03 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea997dee-5d07-3bbf-a7e6-7e6e0484a0fb | -12.1389 | -63.17235 | 2026-10-03 05:18:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf7822fe-1e95-33af-be63-2f3faec3e9b9 | -10.84867 | -62.78077 | 2026-10-03 05:18:00 | NPP-375D | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 119a623b-6596-3927-919f-17a017fdc1b3 | -10.87019 | -57.11531 | 2026-10-03 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 285450b2-91a1-36a8-aec0-466b34418dd5 | -9.54739 | -68.52316 | 2026-10-03 05:18:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efdc4746-b793-368c-aee4-349000fea9dc | -9.90804 | -65.03744 | 2026-10-03 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b965fa0e-f5a4-317e-a8a8-f2d20a3413e3 | -12.85224 | -44.68945 | 2026-10-03 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e9e98da-0a4a-3f32-a3c2-7e86ad7300f0 | -10.87521 | -57.10527 | 2026-10-03 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5c65deb-373f-33f6-a221-719c76f35ec6 | -15.24377 | -43.27725 | 2026-10-03 05:18:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 18.1 |
| f2cb66bf-1821-3435-afc8-ffa0c98a608d | -10.98946 | -59.1297 | 2026-10-03 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6d69ccf6-ee7a-3f5b-8f94-fdad31c059cc | -9.3743 | -65.46933 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62ec35e8-b15d-34a3-a1bd-05d1c7410a74 | -10.9958 | -59.13478 | 2026-10-03 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e7972423-0808-313b-90b6-825c1c63a8f1 | -9.48443 | -67.15459 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b3f6c24-c28b-3047-8104-c32f4abba160 | -12.12852 | -61.15614 | 2026-10-03 05:18:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 670985a3-0bbb-3eda-97bc-0da0101a1c12 | -10.99294 | -59.13031 | 2026-10-03 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5dece2de-6327-3307-8ec1-30566b04d0d6 | -10.99166 | -59.13807 | 2026-10-03 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0c52fd25-78b0-38c1-aea2-a92ee2ac0694 | -9.31066 | -65.77651 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf502b21-5798-3176-9fb2-043f3d3b3c02 | -12.14507 | -61.17379 | 2026-10-03 05:18:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60486385-d6d0-3289-a62e-729803cb6b26 | -12.13815 | -63.17651 | 2026-10-03 05:18:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fb45447d-50c4-30ce-b60e-709fb8cf558e | -10.9599 | -60.91084 | 2026-10-03 05:18:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93ed97f8-26c1-3a5c-9b89-0a748f4fa84b | -10.87353 | -57.11584 | 2026-10-03 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bbb2e13-81f9-3da9-8a38-edeaea495469 | -12.13384 | -63.1757 | 2026-10-03 05:18:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d26ebd2-88d5-3868-9aea-08c0ecb0e308 | -15.23795 | -43.2607 | 2026-10-03 05:18:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 12ce28b8-9d51-3b04-98dc-874b6557ce0e | -9.48129 | -67.15805 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96bc6f8f-0c10-30aa-b083-28adeb4f09ab | -15.24439 | -43.27478 | 2026-10-03 05:18:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 401d79bc-f8a1-3259-8b03-52faa6f50a28 | -9.3113 | -65.77312 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6abf4aeb-e2b0-3ee1-a01b-e888ee73dd1d | -11.03853 | -62.56856 | 2026-10-03 05:18:00 | NPP-375D | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0a1b4b5-912e-3885-8ac5-3c4126416205 | -9.88377 | -65.13911 | 2026-10-03 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 159499ae-5534-3b8e-8a96-44a0d8123630 | -9.88888 | -65.14011 | 2026-10-03 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18dc6031-460a-3239-bcbb-760264bd861a | -12.13459 | -63.17153 | 2026-10-03 05:18:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4a6292a-4af2-3c6e-8bf2-1e282723f66f | -12.05833 | -58.04086 | 2026-10-03 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c980f5e-f5ee-320e-b696-4ab609dcdb88 | -15.23636 | -43.28157 | 2026-10-03 05:18:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 17.6 |
| f6bfa752-6850-3817-bad7-7d70c1a35f6d | -9.55968 | -62.72907 | 2026-10-03 05:18:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 168458d8-9469-34e9-b405-bcd7dd810a7c | -8.3509 | -62.8377 | 2026-10-03 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f85f8e18-9f6f-3205-bcdf-57b19e7f7db8 | -9.17032 | -59.69443 | 2026-10-03 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc34968d-81b8-3663-9c85-3ace47f01069 | -8.70487 | -66.73384 | 2026-10-03 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc1c0345-97ea-3cd4-ab0f-85bd809e0827 | -9.15258 | -57.54643 | 2026-10-03 05:18:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README40.md)
