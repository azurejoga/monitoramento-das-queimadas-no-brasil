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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c6a8575-7f49-3105-b378-608d850561f3 | -7.70023 | -47.2844 | 2025-07-17 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d92e1fe3-f321-39c0-99ea-00c5b6391b50 | -6.85132 | -44.76799 | 2025-07-17 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1780f04-6029-3b0f-827a-57e6c282510d | -9.27694 | -50.25962 | 2025-07-17 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dab60661-e568-3be4-b68c-ab75c80fe0f1 | -6.18852 | -45.87389 | 2025-07-17 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7513da9a-f564-3d22-be9c-b0e959d9ac75 | -7.19184 | -43.11952 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 52c98982-4ee2-313d-8543-c089b6887be5 | -6.33847 | -43.74892 | 2025-07-17 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04de8bdb-495b-3f68-88bb-c540274502a7 | -7.18185 | -43.59717 | 2025-07-17 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd6c9172-2f8e-32f1-a177-11de2ca8ba95 | -11.5048 | -48.95988 | 2025-07-17 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 87544515-88df-3b7a-aa73-75a10fa97b43 | -10.32188 | -49.91231 | 2025-07-17 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 293573f0-8bc1-3adb-8353-99a910cab45f | -11.46089 | -48.15699 | 2025-07-17 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14b7901a-aabe-3ee5-b1cc-3ff7f06a50e6 | -7.88512 | -55.36945 | 2025-07-17 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a4e11ab-3a79-30b0-a41e-367c8cdd43df | -7.88587 | -55.36497 | 2025-07-17 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dd0ed69-2bb0-3c58-bba6-d8e48a34ca6e | -9.31085 | -44.84694 | 2025-07-17 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d96ba74a-7ad7-3997-beb2-a24df9588d2c | -7.88438 | -55.37396 | 2025-07-17 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b1e7cba-7fc8-3bea-ad3c-19a053ca23f2 | -6.29331 | -43.40986 | 2025-07-17 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06595b5d-01e7-3475-8f7d-bc3b5eb2e786 | -11.23892 | -49.49423 | 2025-07-17 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebdd59cf-bf03-3561-b442-556b2b93cb4f | -8.54253 | -47.84913 | 2025-07-17 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d98da22e-c2f6-33aa-bc95-de0102bdda43 | -10.96739 | -49.25254 | 2025-07-17 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d18d4c03-ee7b-3211-a539-562504dcd3f5 | -5.66797 | -43.71534 | 2025-07-17 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| a03b5b31-d502-3e8c-9a1c-d0d91f82215a | -4.45214 | -48.99304 | 2025-07-17 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de780b0d-9632-3b8d-88cc-379efd4d95ed | -9.70166 | -48.90967 | 2025-07-17 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21697d8e-7b19-3119-89d2-5d1b7d7faf4d | -6.5732 | -43.47726 | 2025-07-17 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e474d049-a3e7-321d-8100-a6cfd9cad0d8 | -11.1087 | -48.88129 | 2025-07-17 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1359b594-40e0-3f5e-9fbf-7c7e7e3dd0f2 | -9.13435 | -40.54626 | 2025-07-17 04:46:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 480d5aa4-fc8d-395e-bbe0-e35d19813bc6 | -9.49601 | -40.39452 | 2025-07-17 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| aba50390-1078-33f3-badc-59e537025af1 | -11.35926 | -48.72764 | 2025-07-17 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00b760e6-7f10-3b50-a0ea-aaa520ea1f66 | -10.62305 | -47.4711 | 2025-07-17 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab28ae7f-e071-3b3f-8c2a-7fc4a9bcb220 | -5.65856 | -43.71396 | 2025-07-17 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 085076ee-ed84-314f-a204-3c491f52c9e9 | -5.51647 | -41.33018 | 2025-07-17 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 203b871c-4e82-3cec-bb5d-e13d21be54d9 | -11.52793 | -48.95459 | 2025-07-17 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9e6fc297-167f-34ca-8193-77a210a3cacf | -4.7984 | -48.56447 | 2025-07-17 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b258fa1-61c6-3db0-82a4-dcbeacfc3464 | -11.94429 | -48.42914 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebcfbbdf-0fb5-3f82-b2d5-be9e762868c2 | -7.94648 | -43.86504 | 2025-07-17 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eb7175fc-4bc4-3c8d-a228-8ce84b10940e | -11.94631 | -48.41513 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a806e7c-c298-3592-ab6c-8c036f1ed8d9 | -8.01411 | -51.02159 | 2025-07-17 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8d9ff4c1-1f8f-3c50-8f1e-700d9f99f529 | -8.53879 | -47.84859 | 2025-07-17 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8692a7eb-5ee2-39ba-9274-ce323f78a75c | -10.96782 | -46.48029 | 2025-07-17 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 6c1a9e71-d7e4-35af-a74c-5759628bac01 | -7.94094 | -43.86478 | 2025-07-17 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e2601341-b0ff-3b11-a35a-f8d649467602 | -11.15476 | -49.69847 | 2025-07-17 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6a562c2-7ffe-31ce-8dc3-cc22ad0eaa3f | -11.23832 | -49.49827 | 2025-07-17 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b816c19b-e89f-3655-a810-63c90ae1a871 | -10.963 | -49.25098 | 2025-07-17 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b6b9535-12df-34cf-8193-83743cc8b183 | -6.84404 | -42.7481 | 2025-07-17 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ea461be3-999e-3afb-9cae-494a008724d7 | -8.87696 | -50.15393 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d17955b3-876a-373f-8692-af636d3114df | -7.23301 | -43.50067 | 2025-07-17 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 847e4fd5-1832-3507-909d-c364385dcb70 | -8.35878 | -51.07933 | 2025-07-17 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbe87c6e-6d1c-3c27-a657-a9d46b9ee801 | -7.35051 | -44.20235 | 2025-07-17 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 91a3ad47-2b1f-325b-9d69-25ea101f92e4 | -4.36838 | -55.77076 | 2025-07-17 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 729af270-cd4c-3d6c-a723-51e41d54540c | -7.21142 | -43.1636 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0adb253c-ae5a-32b7-9530-e27e76438ce0 | -8.37996 | -46.87986 | 2025-07-17 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f08762e0-b20f-3935-8865-6b24a6d74b50 | -10.80941 | -50.46879 | 2025-07-17 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dd3f2932-1827-3769-b6ce-402178d9067f | -11.94564 | -48.4198 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4530c403-05d4-30c5-b795-1519335b09c3 | -10.24325 | -59.27787 | 2025-07-17 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b342d3e-8669-3a3c-8a41-c37f4e33c1eb | -11.94496 | -48.42448 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ffd0b53-fd4e-3863-90b4-2678fb341e28 | -12.02967 | -47.77703 | 2025-07-17 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f14ab8d5-59a5-3f82-b588-6085671a1ed3 | -5.53116 | -43.88387 | 2025-07-17 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9a727175-9746-3c19-a311-bb05202de171 | -10.05227 | -59.10533 | 2025-07-17 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66a55af3-5864-30c7-b3e8-5b5dea23df7d | -8.74976 | -46.59953 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d9cd1ff-0799-3507-a424-f563619ff41c | -12.03334 | -47.77885 | 2025-07-17 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef5bdf19-9f73-3483-94b2-9323a96945e2 | -6.4551 | -45.34233 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcbff327-b857-3e76-956f-f9d1744b561e | -8.05763 | -50.09688 | 2025-07-17 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9198922-b962-3a1d-84af-6eaf6182894a | -7.19264 | -43.11492 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7ac1447b-4f2f-3f15-85d1-d6414c19a2eb | -7.30753 | -44.30458 | 2025-07-17 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39d9f486-e4e2-3c68-b750-e28b39b31853 | -10.05687 | -59.10612 | 2025-07-17 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c278afdc-4bbe-3a9b-b09b-69e8a8f54330 | -8.14805 | -47.63605 | 2025-07-17 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f2c83ed-5fa9-350e-9e46-3de0ad6f215b | -7.19181 | -43.12076 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8567032e-3aa5-3b6f-83c4-324f869fc3a2 | -7.59488 | -46.33383 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e89376f-63cf-3b51-aaaf-9d119633b978 | -9.71238 | -61.29209 | 2025-07-17 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7018f8fb-017b-32bb-917f-706936dd550c | -9.16318 | -49.67168 | 2025-07-17 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54a27bf9-1f2c-3275-936d-8f0c0026b51e | -6.71423 | -44.3273 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| cac6ccde-68dd-3138-b6e0-47a789fb88e7 | -9.15973 | -49.67115 | 2025-07-17 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98530079-6c68-3fff-ba7a-5d1c2070dbf8 | -11.85338 | -46.75329 | 2025-07-17 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c0926b0-310f-3406-b017-99df3c45e29b | -7.59426 | -46.33437 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca1c9f2c-4a97-3423-bfc5-5cb456942dbf | -11.10506 | -48.88072 | 2025-07-17 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 94905210-eb8c-340d-a8b5-0702ae1f500b | -9.41595 | -48.41686 | 2025-07-17 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 936c6bd4-a85b-3403-9f93-005d39f2a4cd | -6.14349 | -47.31308 | 2025-07-17 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d317b078-0235-355c-a72e-31e5f66c7676 | -11.94807 | -48.4297 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f74bf4fc-0971-3509-962c-3cb5572ac7a4 | -11.46023 | -48.16177 | 2025-07-17 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 507199c0-a42f-3cbc-bcf8-ac26f74b7ddc | -7.46444 | -44.71901 | 2025-07-17 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6c67d92-319a-37cc-8d3d-ae82904ff82d | -7.18682 | -43.1188 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 45b1f2fe-92b7-3801-9040-7c89178f2dcb | -9.31544 | -44.8476 | 2025-07-17 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da678c88-5e87-3f51-a4f8-48286303bafd | -8.03998 | -49.88543 | 2025-07-17 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4eee3cb0-4bff-3622-8ca4-6cd93845f9af | -7.34917 | -44.19952 | 2025-07-17 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 743a31c3-bae6-3a62-b6e9-94f46b345561 | -6.73122 | -44.33948 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7c8b014-34b8-3dc4-a621-e4513678d8a1 | -5.7923 | -45.08812 | 2025-07-17 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e1274c2-c11d-3f9e-acbc-36e060eb432d | -5.45008 | -42.62624 | 2025-07-17 04:46:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 29e4a529-6dfc-3c28-9637-a1b35eb0d6a0 | -6.72731 | -44.33406 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5c23a534-b1ea-3be3-8182-a0f740d99c7a | -12.47854 | -44.503 | 2025-07-17 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0edfdcd4-792a-334c-8608-d967a335ea50 | -6.71031 | -44.32184 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| edeb0433-0b9c-3672-9b36-ea51b561eb51 | -6.99418 | -43.75172 | 2025-07-17 04:46:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb42df25-cd89-30d9-8396-30fd7b5ea24e | -11.23772 | -49.50232 | 2025-07-17 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fa48be3-e085-3ab7-82bf-8d0ac2f3787a | -5.51698 | -41.32646 | 2025-07-17 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7217070f-c738-33ef-afc2-21492f7862b1 | -6.97388 | -42.81222 | 2025-07-17 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a998cd77-1d61-3ae0-a559-4b132a43a009 | -6.62365 | -45.70787 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52e86eef-6b00-3e1e-b8b3-3e6bf164f743 | -10.96835 | -46.47639 | 2025-07-17 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 68214cf9-f506-3550-bd89-a43829625cf8 | -8.75018 | -46.60221 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6799d6a-4c70-3b2b-ba17-5adb6dfc491d | -10.32917 | -49.90478 | 2025-07-17 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca121e66-6fc2-3377-818d-f82b0bb40d0f | -5.66722 | -43.72051 | 2025-07-17 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e47a01b9-1cee-3cbf-a477-f8f5fe838294 | -5.59619 | -45.79862 | 2025-07-17 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8788a71-994b-3cad-9a0c-0450c5cfcc4f | -8.70942 | -50.05357 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e83bb519-2841-3d6a-b89f-c8b64379ac3a | -11.94638 | -48.41692 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README22.md)
