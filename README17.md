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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13de01ae-c5df-3878-89ba-ee36e0ba2677 | -13.18474 | -51.44308 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eda481f0-5dca-3721-82d9-b1f17e44bf41 | -12.7251 | -48.4026 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8064b9d8-850c-3c7a-80c9-9360f859eab2 | -17.71665 | -43.49516 | 2026-08-23 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d9f4773-472e-3faa-a306-c00ba8266741 | -13.67012 | -51.8565 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52b3dd50-59fb-3f62-95f8-e24fdff4a1d6 | -14.38721 | -51.78835 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 277f5bd9-897a-3d88-b966-ecd790f5de94 | -12.24138 | -43.12377 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 73706a51-c224-3dbf-8382-06949cbb34ef | -8.53507 | -54.84719 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a87f8ae8-a751-33a3-8356-13534007923b | -12.37032 | -46.45178 | 2026-08-23 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03457050-dfa8-3419-b767-4b8bf34f6f40 | -11.28022 | -50.74012 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8245296-8e64-3562-98a7-2a1e4fa7ea9c | -12.72922 | -48.40302 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c8554bf-840d-3197-a88f-9009c6b76030 | -10.27106 | -50.37983 | 2026-08-23 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f565c0c5-4c84-30ce-81df-75142c0985d5 | -11.16255 | -54.01126 | 2026-08-23 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1356190-5337-3569-b713-92ca8b30ac13 | -17.91603 | -44.38272 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f68983b-13a1-34b0-9f6d-da0efde95d3c | -17.21198 | -47.52481 | 2026-08-23 04:10:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a85371f6-9112-3c72-b6c7-a92df71cfa8d | -16.87541 | -48.98377 | 2026-08-23 04:10:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77e70acb-fe0b-38f4-8572-3a2b73b73582 | -11.62006 | -50.56016 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4320de1f-2417-3e33-bdc5-d360330944df | -12.23751 | -43.12676 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c1fa14ad-5e4b-3b6c-99ef-143a488bdcd3 | -10.30723 | -48.21262 | 2026-08-23 04:10:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 816d34b3-3846-3134-ba6e-8d8b643b0414 | -14.13841 | -48.05187 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 135755f6-cd40-3d21-8c59-0e44f252c5cb | -17.40472 | -48.11478 | 2026-08-23 04:10:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc09d9f2-fde6-3a23-a1ce-0cb6d4100e1f | -10.83431 | -50.96702 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d68b3996-920f-3f31-8692-cb74324eacc8 | -13.18792 | -51.42603 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f2186195-bf09-39ab-b382-511f8c50ca66 | -8.53726 | -54.83565 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f09a273-ed38-33f6-aeb7-bd4f1fbf46dd | -15.31643 | -53.80021 | 2026-08-23 04:10:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3402931-0496-3aaa-b969-f3e8bcaa7214 | -13.18588 | -51.4447 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15db980f-7a0e-3c24-9643-32003892fc76 | -12.21906 | -43.15577 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f1593304-3b14-32a7-b918-f824353db2bb | -17.25579 | -44.87996 | 2026-08-23 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2efb02b2-6f37-31e5-bf8f-14de5d53a43c | -12.73505 | -48.39372 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 010ac856-4030-3523-8be2-cb9917deed8a | -12.06733 | -50.59939 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd5701d2-5f6d-3900-a4fd-71173141f3f1 | -10.69207 | -47.71964 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e86cb77-54e5-3570-8d8f-9ba5e80a98ed | -11.16166 | -54.01584 | 2026-08-23 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d65672aa-b98b-3908-bac4-7ae1581fc0ab | -11.94497 | -45.5039 | 2026-08-23 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23ee5361-a37f-3e1b-87f0-6d589008fc48 | -12.22732 | -43.14629 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 52f66c43-d28a-37c6-9e86-b47b78ec42d1 | -10.69548 | -47.72393 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48d30030-a9d1-32e6-86d2-82d7a3b00c9f | -14.38832 | -51.7826 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48a0cf9e-9821-3c51-b280-c9ac4abf9685 | -16.71512 | -49.13091 | 2026-08-23 04:10:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70f61fbe-d152-377e-b6dd-e3240dc68348 | -10.38357 | -50.41319 | 2026-08-23 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5bf4433d-4d98-32c0-8759-ce94084fc73c | -13.25883 | -51.60024 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a68b8dde-1775-381c-a062-aca2f499ea81 | -11.43522 | -44.53386 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e522d8dc-e8a2-38d1-b4e2-ea7fc175c501 | -11.14721 | -46.19867 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 370889ff-d77a-3e1a-bada-b859354ca7a1 | -13.66624 | -51.84968 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf958584-2b9c-3ed2-91af-b9621876ea4a | -12.74462 | -48.4109 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0efad1cd-7126-38fe-8701-1a88b9339006 | -12.74847 | -48.3889 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d381918-bf71-3a7b-a84e-e8bffcff4738 | -17.89087 | -43.19244 | 2026-08-23 04:10:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ae809c8-9b4d-39cc-81a3-3d13425af4c3 | -16.11574 | -43.63166 | 2026-08-23 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b951e21a-6136-3b15-bd95-f66c44fb1a4a | -15.51764 | -49.83194 | 2026-08-23 04:10:00 | NOAA-21 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 349fce3b-f7f4-3132-971d-5a1ffe7a699b | -12.24744 | -43.12836 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 67b1110e-a0f8-3c95-9eec-4208b0a551ca | -13.69072 | -51.85771 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a230290-a28e-3c3a-a6e4-a569446e5aa6 | -13.20887 | -51.4315 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c67c0c8-2fe0-36b6-b250-ec09e13a8b37 | -13.43457 | -43.85989 | 2026-08-23 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bd57d370-5eb9-3634-a83a-91f7273bec88 | -8.54249 | -54.83241 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fd8e148-ab95-31e8-8fe3-487929625fd5 | -12.73915 | -48.39424 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5e99505f-f2ee-3771-a89f-f26d8903ea61 | -12.84374 | -48.4659 | 2026-08-23 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3b8c743b-a33e-3af1-8d13-d8d3f2baac21 | -13.88427 | -54.00647 | 2026-08-23 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6bc8d37-0d58-3985-8eee-7bfb56dde266 | -12.23034 | -43.17247 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db663820-a2fb-3770-a7d0-b824728626c9 | -11.85046 | -51.67551 | 2026-08-23 04:10:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bbf4005-9b05-38ef-85b4-d1efcf676005 | -13.1661 | -51.43355 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e5a8c58a-6907-3f9f-949a-fda99059fb3a | -15.96434 | -47.49987 | 2026-08-23 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35dd34f4-0cfb-369b-a594-09253ae91277 | -8.54025 | -54.84381 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bce6480-afde-3e9e-b2f9-8488f813129d | -12.83673 | -48.48187 | 2026-08-23 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da14acb2-f2d0-36c3-b045-1f097324b6ce | -11.58208 | -46.94047 | 2026-08-23 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cae88e50-283d-3618-bba8-784e7fc6e8b4 | -15.24338 | -52.86045 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b717324-fce0-31e5-a0b7-60adbcd3423e | -12.22347 | -43.17094 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8346061e-4fb9-3841-8d91-8792db4b10d1 | -15.31572 | -46.06861 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3687537-e76f-34a7-a6fb-ebd131e2eedb | -14.97048 | -52.67426 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e568db61-dd1a-38f2-aea2-6267a59e1609 | -12.8478 | -48.46672 | 2026-08-23 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f1062a3a-247a-3f77-bc0d-5abdd2526c38 | -12.73971 | -48.39104 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e74c0170-cf04-36ee-b864-f867226fabe6 | -11.05429 | -49.50639 | 2026-08-23 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20dd746a-8902-34e5-9538-57aed5df4f8c | -12.2899 | -43.16045 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f58dc408-adaf-38f5-ab5a-86a28ff623db | -12.28824 | -43.17101 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b738f6b-a7b4-37ad-8302-b8eddc10da81 | -8.53616 | -54.8414 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8ee4c6e-512e-35a8-b76b-57987cc7e30b | -15.76338 | -49.96915 | 2026-08-23 04:10:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03931d86-02a8-3ca8-81c5-73702e0092c8 | -13.37974 | -41.32655 | 2026-08-23 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8d1a8309-3cc1-366f-b310-21f7aef54413 | -17.37416 | -42.63399 | 2026-08-23 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77a5c14f-ee5e-387f-ad80-e0671df61f0a | -13.10121 | -43.3432 | 2026-08-23 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4af0a7c-0028-3c84-a332-583bb63f75ed | -13.21544 | -51.45044 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e7aaada-dd56-375a-a027-c6ec6a70a31e | -12.74381 | -48.39156 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a78ea5c8-696d-3b6a-939b-2341a080af92 | -10.68767 | -44.18402 | 2026-08-23 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0262e37-d9e2-363f-9ef8-f07faaab48e3 | -13.09017 | -43.34864 | 2026-08-23 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cca7df9f-8fd8-3a14-8b15-00fa89260183 | -13.03291 | -42.00134 | 2026-08-23 04:10:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ca621fc6-f7c1-3caf-9340-5abc380cab21 | -9.43099 | -51.61443 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4bb7824e-40e8-3573-845c-9e7fb61b3194 | -16.40302 | -51.85201 | 2026-08-23 04:10:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1ff61d0-6a08-345b-8ef7-e0d36c64ec70 | -11.14357 | -46.19796 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b6d30f6-eb50-3500-91c1-cd5e4d035c55 | -16.60542 | -42.45972 | 2026-08-23 04:10:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2c7a209-08d7-381f-96c6-a29c8ddc256d | -12.22678 | -43.17147 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3a7e0861-5f8e-3ab4-a380-c9d8ef430cc2 | -12.5619 | -47.9279 | 2026-08-23 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c93117c-69e6-3bd2-b664-ce9204c0a9c5 | -17.86167 | -44.25084 | 2026-08-23 04:10:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b02a643-3637-34b0-becd-a770961531b6 | -11.85102 | -51.67247 | 2026-08-23 04:10:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94f861b9-bfbd-388e-9785-cc03cfb54b36 | -11.43242 | -44.52957 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5997b9e2-153a-34f8-8248-99abfbdc1924 | -12.25184 | -43.18676 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cb81a8f3-7c4b-3fd6-85e8-7a3a6066c654 | -13.43182 | -43.85579 | 2026-08-23 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4d11862-092d-3c33-8d04-18463f32ae3e | -8.54137 | -54.8381 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6693621c-e755-3980-83cd-cb2224d5be42 | -12.28328 | -43.18103 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| deef211e-8663-3460-858e-b584b998e5fd | -12.27391 | -43.13262 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 332c3052-16e3-3b21-b96f-ed310e5ea498 | -16.06512 | -50.42977 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a40e22b4-d0ef-34e6-b36e-84f0f13bbcb4 | -10.27491 | -50.38612 | 2026-08-23 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e1513b3-3e04-3b1c-96e4-5b85a7ca5dce | -12.73289 | -46.4621 | 2026-08-23 04:10:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c53a344-5805-383d-8c5d-58eca013d065 | -13.44518 | -43.83603 | 2026-08-23 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aeefce0c-ad61-3811-beef-20815820bf11 | -10.38841 | -50.41409 | 2026-08-23 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4c0a4b0-a039-3c87-a64b-8f1b88cf63d6 | -11.44082 | -44.54242 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
