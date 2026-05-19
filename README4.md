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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87080f25-6082-312f-b062-a7d59e318e4b | -11.02706 | -42.84859 | 2026-05-19 04:10:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f1b186cc-5e71-3cda-958d-36d9ac96a6e3 | -10.66677 | -49.69878 | 2026-05-19 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7b399176-322d-3ab7-bdbf-3ab36e426612 | -11.32135 | -47.41962 | 2026-05-19 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe8443d0-e597-390f-a1a9-210b0c5b192c | -18.73326 | -47.50861 | 2026-05-19 04:12:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc17f66a-89d3-3998-92d5-568d19514d6a | -17.96128 | -44.56945 | 2026-05-19 04:12:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f0fb8ec-a3a2-3e5e-9d3e-1b58c660335c | -17.96905 | -44.56335 | 2026-05-19 04:12:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed052d0d-2535-3e30-99ce-7acc662bb38e | -17.96574 | -44.56278 | 2026-05-19 04:12:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 224cc876-e884-3bb4-8451-a1ffbd19ed4c | -17.80328 | -46.71807 | 2026-05-19 04:12:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6123f688-f12f-31a3-aed3-7d123054a6b0 | -17.70341 | -46.2319 | 2026-05-19 04:12:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c60ae4d8-ccc3-31c3-9af9-992020becda4 | -17.70685 | -46.23252 | 2026-05-19 04:12:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56e0026c-2bec-31f7-b762-158c77a7e3fd | -10.13493 | -52.20131 | 2026-05-19 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e1932fe-076f-3027-8b49-5d2bf45b58c8 | -8.55241 | -45.98729 | 2026-05-19 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f218d4ad-4a9a-35fa-beeb-1a47bb33b361 | -10.4509 | -47.94415 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abea9d26-61dd-3209-bb43-25a4e3d58e50 | -8.71714 | -48.32444 | 2026-05-19 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2f444af9-5e0d-31ce-8480-2eaa02c24d6d | -9.29912 | -45.48017 | 2026-05-19 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40ab3c75-1365-375a-84a1-fb94e5551520 | -10.44698 | -47.9472 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6eac1f34-b185-3e6e-9d4b-3ecb815f55a6 | -10.45818 | -47.94164 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc44199a-6e22-3b0b-9b72-f615d90a8cdb | -8.71603 | -48.33144 | 2026-05-19 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7d748d74-4dbe-3703-841f-5d16b6c98fb9 | -10.4599 | -47.93782 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 596f579d-d9b3-3ce8-bd1f-9038647a7d0f | -8.70692 | -47.92044 | 2026-05-19 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa510295-4cc1-3e0b-b336-773590b56d42 | -7.96802 | -45.27489 | 2026-05-19 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29df8b7c-e69a-3c70-89dc-82789eea3efa | -8.72269 | -48.3325 | 2026-05-19 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffbb302b-2c4c-306b-b4ec-226eb5141bca | -9.93977 | -52.45701 | 2026-05-19 04:42:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81b428a1-3e2d-3a96-8fe4-a222715d7c61 | -10.4537 | -47.94827 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e78f7b1-4b98-35c9-9f05-7df5eadefa1a | -8.71659 | -48.32794 | 2026-05-19 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 48fd4f32-ad02-3ea1-a6e9-8fb306fdfa8b | -10.0982 | -48.01284 | 2026-05-19 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10e996ec-9860-3539-b007-27d671997e76 | -10.01444 | -49.3595 | 2026-05-19 04:42:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a9b87d2-96a5-3ac8-a1d6-bc769c4dceb4 | -8.72047 | -48.32497 | 2026-05-19 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4b6636e2-f4ab-3517-bb27-357cad4a9012 | -8.08241 | -44.11253 | 2026-05-19 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4d5c123-1259-3a16-aab7-1b54a2c392c4 | -8.73111 | -47.9746 | 2026-05-19 04:42:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98f44383-8c28-3250-b523-0a0f1ef04009 | -10.67404 | -42.15547 | 2026-05-19 04:42:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ccb719f6-907e-3e95-a429-c7480a0309ee | -9.3124 | -45.4908 | 2026-05-19 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da7bb27c-898b-3b3f-8e1e-41b8e6fce1a1 | -9.47401 | -46.07803 | 2026-05-19 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fdaf674-8980-33dc-81d9-de1c7dd7deb0 | -10.65233 | -42.31756 | 2026-05-19 04:42:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8465c156-0d3b-3568-a527-195e0a9d6ec3 | -10.65294 | -42.31301 | 2026-05-19 04:42:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb3241a4-acce-319b-8161-77c419498222 | -8.33066 | -45.35912 | 2026-05-19 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 586eb363-9015-3121-add1-6c0e5d6d06f4 | -8.07538 | -44.1065 | 2026-05-19 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33dcd425-5c89-317f-887a-f69fa43655f8 | -10.65355 | -42.30844 | 2026-05-19 04:42:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a802cced-b148-33dc-9f43-336fbc50f2ee | -8.70024 | -47.91938 | 2026-05-19 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd005ea1-b436-3b5a-8faa-6bb63d814299 | -10.45595 | -47.9339 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7f4a4140-8cb4-38cb-9667-408b8c0431b4 | -10.45203 | -47.93697 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c2bad27d-3d22-33e7-9caa-5320da9bcc9b | -8.07854 | -44.11194 | 2026-05-19 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d03dadd1-b1a1-3f18-ae98-88dda32749e7 | -10.57223 | -46.6729 | 2026-05-19 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7d047a90-5bf3-37f2-9bed-020e71d6203b | -11.01703 | -45.13537 | 2026-05-19 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 650dbf84-3fa4-3d4a-8abb-c5be9b3be194 | -8.73001 | -47.98162 | 2026-05-19 04:42:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 501d5d6e-6fe8-3c5c-b069-9f04e85009db | -9.30876 | -45.49026 | 2026-05-19 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28c10b33-0b40-3d4f-8569-a26bbcd17b2b | -8.72946 | -47.98513 | 2026-05-19 04:42:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b5ab1cf-9a50-3333-adfa-23f2bec6ada5 | -8.07638 | -44.12649 | 2026-05-19 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f292321-9f6d-39a4-bd08-16cb1dd05161 | -9.47756 | -46.07855 | 2026-05-19 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67c3fa3c-f933-362f-bc46-b0ca9c458f8c | -10.45482 | -47.9411 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f22e1951-1aec-3fbd-92b4-0bf6324a3306 | -8.07323 | -44.12106 | 2026-05-19 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f36bb649-8728-3760-acbc-8d83b707ef90 | -9.30576 | -45.48549 | 2026-05-19 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1a4183c-c575-341b-b375-4f2577b43b57 | -10.66932 | -49.70206 | 2026-05-19 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50a433f9-3cc6-3601-a49a-c81a471c3686 | -9.81667 | -48.51487 | 2026-05-19 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0247ae6b-5a22-354a-aa5e-55bd55c21dd4 | -9.29848 | -45.48442 | 2026-05-19 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76d4e943-1451-3316-944b-52958f6c3a77 | -10.40034 | -49.44048 | 2026-05-19 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64d698ae-896c-3ff5-b198-475c7c98f7ab | -10.40311 | -49.44456 | 2026-05-19 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e0b40e1-33d1-37d1-a36e-d58b314df83c | -10.45146 | -47.94056 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c880f9fa-fe58-333d-8ceb-a1458a10537e | -10.5734 | -46.6651 | 2026-05-19 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad51dbee-fe98-3a07-bc38-2196fccbb8df | -10.09485 | -48.01231 | 2026-05-19 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1746c3d4-4fdf-3ef1-a933-fe6f5e580fe3 | -9.89257 | -49.33617 | 2026-05-19 04:42:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a8661b1-db49-3626-ad75-60c9b880d7dd | -9.62023 | -40.3452 | 2026-05-19 04:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8b0527eb-b14b-30bd-908f-a80d29b08adc | -10.57281 | -46.66901 | 2026-05-19 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68b7a8ff-ff0c-353b-bd47-6814fa9d92ee | -8.70358 | -47.91991 | 2026-05-19 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ab433f1-b4ca-314b-9ece-c026da76aec2 | -8.71991 | -48.32847 | 2026-05-19 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c6c961b7-8f3b-3571-a8e8-05676f30ae55 | -9.61982 | -40.34819 | 2026-05-19 04:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d87c951-6c53-36a9-8a96-a7cc76bc38a4 | -7.9674 | -45.27907 | 2026-05-19 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9d31685-ddad-320f-a5df-7f69a836de16 | -10.45875 | -47.93804 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c74023cb-6044-3c42-9e6e-df45e8531754 | -8.70302 | -47.92343 | 2026-05-19 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40af47ec-bc67-3f9d-8b1a-00d343c30e37 | -8.72324 | -48.32901 | 2026-05-19 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9fb5637-0641-343b-958e-ecc090362130 | -8.72214 | -48.336 | 2026-05-19 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 799b4080-0a92-3b88-a34e-43c1d68e3000 | -11.02699 | -42.84768 | 2026-05-19 04:42:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d1b49189-5d1c-35fe-b2c7-09b7069fae79 | -10.39977 | -49.44401 | 2026-05-19 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2a7c28f-6b0d-3d00-924d-48118d664918 | -10.45034 | -47.94773 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0639228d-ec8e-3407-95bf-e6dcf9b305b7 | -9.29547 | -45.47964 | 2026-05-19 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0151bf85-93f1-38cd-b7e3-8c7bca19cc16 | -9.29247 | -45.47486 | 2026-05-19 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0976e003-a638-383c-b58a-0442ae7e0650 | -8.71936 | -48.33197 | 2026-05-19 04:42:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 030b73b4-4f51-3435-8fd7-f2fb954779a8 | -9.6174 | -40.34516 | 2026-05-19 04:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 51495959-3e9d-3cd3-8e42-5738769bb68d | -9.30512 | -45.48973 | 2026-05-19 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60ef5993-2d53-38a7-9312-237532877578 | -10.45935 | -47.94141 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 107e3c08-fc14-378d-80d6-38d5ff27bca2 | -11.27734 | -44.65012 | 2026-05-19 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96b32ad1-ff45-3da6-b569-c2b123358b64 | -8.08313 | -44.10767 | 2026-05-19 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9f12878-42df-368e-b981-b15a6b533d06 | -7.96865 | -45.27069 | 2026-05-19 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae952c7f-bdf1-3655-a37b-e37598e5f985 | -10.99284 | -43.723 | 2026-05-19 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c174e3d-e4d1-3569-9986-61cabf2baeb2 | -10.03895 | -44.15142 | 2026-05-19 04:42:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0978e294-4c33-3798-8599-5714f7c21531 | -8.0771 | -44.12165 | 2026-05-19 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8e88b88-417c-37bb-8664-4424b74ce45c | -10.66655 | -49.69797 | 2026-05-19 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 01abb0f9-618c-332a-a5a4-9a512deb756a | -7.72373 | -44.55684 | 2026-05-19 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3e1dd7c-30c3-30e3-a023-d3c7633a3a6e | -10.44643 | -47.95078 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 86a6797d-cf11-35db-9dd3-f79783ec29b4 | -8.73056 | -47.97811 | 2026-05-19 04:42:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f71b9776-728e-3a89-87cb-cc64160996eb | -10.45931 | -47.93444 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0249c8fd-1919-3e53-9909-f6641a4f04f9 | -10.66598 | -49.70151 | 2026-05-19 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 58718c62-189a-3502-9272-f2620c0da281 | -9.30212 | -45.48495 | 2026-05-19 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 883da001-0757-3395-94ec-6bc465ec6f72 | -10.45538 | -47.93751 | 2026-05-19 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7dabe66c-cf6e-3b41-b3b8-737c4970679b | -7.46058 | -49.51884 | 2026-05-19 04:42:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84f40d0a-fa46-3342-a0aa-02eae70d536b | -8.08024 | -44.12708 | 2026-05-19 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eab4373a-ff9a-3fcc-9ba9-4e7f2ed48973 | -12.05778 | -45.27503 | 2026-05-19 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9926a256-4f28-36eb-9013-7b5516ebd943 | -11.30685 | -47.41372 | 2026-05-19 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb865d07-2ff0-3aae-b807-f46cb8355ea8 | -11.95928 | -49.52467 | 2026-05-19 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2ff5abdd-fd8b-37dd-ad91-408f14dab7e1 | -14.1555 | -52.88287 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README5.md)
