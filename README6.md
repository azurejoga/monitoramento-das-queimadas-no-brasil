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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddfaacab-422d-3c6f-a8e0-38412e9f775b | -3.54 | -48.204102 | 2026-09-08 01:08:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5065d01-c11c-307f-8f4a-336ae556acb0 | -2.9768 | -49.273102 | 2026-09-08 01:08:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7df262ad-2993-3825-831e-38bd8da58589 | -3.8943 | -55.815701 | 2026-09-08 01:08:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19d9d3aa-dcaf-3e78-b424-8ea4074be28d | -3.2358 | -47.244499 | 2026-09-08 01:08:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c5d520f-eeda-3b9a-a1f6-a2d06f6be485 | -3.5594 | -48.199501 | 2026-09-08 01:08:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5921a36-c2c3-356a-8eaa-ff29b6997105 | -5.9869 | -57.708801 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60a92bdb-7fc0-3e0a-a2a4-554df77fefeb | -5.1637 | -55.952099 | 2026-09-08 01:08:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78cf05b5-eef2-3242-bf8d-3469aabae486 | -6.7695 | -58.948502 | 2026-09-08 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18bb994c-f7dd-3480-a61e-beef8d9b38db | -6.7615 | -58.958599 | 2026-09-08 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6668ad0d-29b2-35c6-8558-7574a0975e03 | -5.9919 | -57.685398 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a827d000-28a9-3970-8324-ce57951fcd03 | -6.6413 | -59.434799 | 2026-09-08 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba50ce2f-8ca5-36d0-817e-cb843432bcdf | -3.8959 | -55.822701 | 2026-09-08 01:08:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95915180-0db6-31ec-9c2c-214483d59a0d | -4.351 | -47.578499 | 2026-09-08 01:08:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76c31e5e-2fc6-3f9c-b52d-012b53c79566 | -13.2358 | -61.721298 | 2026-09-08 01:08:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b5bf9df4-f867-3b73-bcbd-47021ec83cf7 | -6.0584 | -57.797298 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8284757-295e-3bfd-9a9a-ecd7f5539cdb | -5.3639 | -56.0154 | 2026-09-08 01:08:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0241703-241a-3a76-85a8-732a6bacb455 | -7.3737 | -47.0214 | 2026-09-08 01:08:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c04e799f-7da0-341f-bb3a-3315e0c19a6d | -15.8402 | -56.6064 | 2026-09-08 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa660a3f-7ee8-31c5-b4be-e712b50943e7 | -5.1652 | -55.9589 | 2026-09-08 01:08:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70aaa55c-0e18-357a-9768-aa0c98bd347c | -1.1943 | -55.7365 | 2026-09-08 01:08:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27e06806-dd90-3936-b736-a7176cc1871e | -5.9967 | -57.706699 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd1bd8cc-dca5-35ea-ae67-86296488b9f5 | -1.1893 | -55.714802 | 2026-09-08 01:08:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92bd831c-d9d4-3577-a7ee-abfa6a4cf18a | -9.6993 | -43.413502 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b4528565-4cc8-32b6-a7ee-f33eba6d5483 | -1.2074 | -55.748798 | 2026-09-08 01:08:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3805e33-6c2c-3e0b-a3c7-1065b55fa729 | -13.4352 | -43.821201 | 2026-09-08 01:08:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 191bbc20-1dbf-32c8-a56f-6520cf7c7a64 | -4.0367 | -50.872799 | 2026-09-08 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a38c1216-0490-3a79-9768-148b9fa499e8 | -6.7909 | -58.952099 | 2026-09-08 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a266b49-407e-3403-918e-428e8493dbdf | -13.4281 | -43.7957 | 2026-09-08 01:08:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3993050d-c721-3a8f-ad41-6740e49a32bc | -5.3654 | -56.022301 | 2026-09-08 01:08:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f4635bb-21e8-301a-a01c-4c00aa207090 | -3.3351 | -53.4044 | 2026-09-08 01:08:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| facb7c21-7f09-3cd5-89a0-78429c8701ef | -6.7731 | -58.964401 | 2026-09-08 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 052a1cea-2718-317d-9c82-c37853f69f06 | -8.5287 | -63.828899 | 2026-09-08 01:08:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 991d8232-f266-35f3-8566-b4ce5e2158fe | -10.7223 | -51.816898 | 2026-09-08 01:08:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52782759-d712-3f96-b3d5-54908499415d | -4.0709 | -55.775902 | 2026-09-08 01:08:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 401cc627-657a-3304-9f15-3d3a220b9d01 | -13.2233 | -61.709099 | 2026-09-08 01:08:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 48f14caf-0e38-3ced-9816-d0415ae5360f | -3.4188 | -59.2402 | 2026-09-08 01:08:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 263431bc-8ea7-3e55-9bbb-acad01835e20 | -3.5503 | -48.1619 | 2026-09-08 01:08:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2552f6c1-fac1-38ee-bad9-65eb73ba5e67 | -3.5355 | -48.185398 | 2026-09-08 01:08:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64ffc284-7425-312c-88b7-f465d9606160 | -1.5956 | -60.144798 | 2026-09-08 01:08:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7cc23b4f-d84a-3532-80d8-33be69f51b1a | -6.8007 | -58.950001 | 2026-09-08 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e5247b8-e5f2-3ef7-8fcb-40aaf79b1f9e | 2.0962 | -55.951698 | 2026-09-08 01:08:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff69aa4-253e-37e2-a205-5997af5fdda2 | -9.6982 | -43.447601 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4968b0ea-73ab-3004-9e3e-8e913695bffe | -1.2058 | -55.741501 | 2026-09-08 01:08:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b09fde67-4f3a-3d7a-b86f-d9c4e11532ec | -4.3414 | -47.580799 | 2026-09-08 01:08:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a0c0f4a-fe1d-38b1-8fcf-04d4692bff05 | -6.5079 | -58.2845 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2d607b3-7cfc-364f-9e85-1343a25e68a1 | -5.9951 | -57.6996 | 2026-09-08 01:08:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8deb369-40c2-30b3-b6a7-b24d017f368a | -13.2163 | -61.725201 | 2026-09-08 01:08:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 53b7e6a3-7a62-3907-93dc-e55c63836cae | -3.8861 | -55.824902 | 2026-09-08 01:08:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0161fa20-8609-3c26-8c2e-4e947fdaa2c9 | -9.7173 | -43.442299 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db92d532-27ff-3749-bdba-7a578f442937 | -21.9781 | -56.0453 | 2026-09-08 01:08:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 14dc36b8-8ef2-3bbd-b068-70d2d3e75520 | -9.7554 | -43.431801 | 2026-09-08 01:08:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3ee9f2d-d50a-3381-838c-5fc9b8ab46eb | -6.6315 | -59.437 | 2026-09-08 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b428be74-f676-3d8b-b552-8aaab6940b50 | -13.2099 | -61.7173 | 2026-09-08 01:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| a5936128-18c8-3b02-b5b2-16b07570e027 | -3.5591 | -48.1882 | 2026-09-08 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 193.4 |
| ad114159-d49c-38d9-b68d-c4e91dbe25b9 | -3.5407 | -48.1673 | 2026-09-08 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 156.8 |
| dc424035-f252-3685-87df-5a1858af4646 | -9.4769 | -40.3365 | 2026-09-08 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 113.2 |
| bfb7d8f1-80dc-32b3-9483-cc0317f30462 | -3.5406 | -48.1889 | 2026-09-08 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 345.2 |
| 19bd1400-a234-3013-b1df-42ed0620268f | -3.5592 | -48.1666 | 2026-09-08 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 58b9be04-d6cf-3ea6-9b32-db4fd0cbb813 | -9.4765 | -40.3613 | 2026-09-08 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 05799971-21e4-3e22-92f4-ac9c1f2c60d3 | -9.7138 | -43.4192 | 2026-09-08 01:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 20956fea-2f27-362a-bf52-ae7d3771e11c | -13.2479 | -61.7148 | 2026-09-08 01:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 6da3cbc2-1c8c-33c8-80ed-d082e2340d5f | -13.2289 | -61.7161 | 2026-09-08 01:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 56e8e0cf-15c7-3791-92c9-22804d37b171 | -8.5322 | -63.8604 | 2026-09-08 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 191f5882-6255-35d9-906b-7a72256d3941 | -9.71 | -43.42 | 2026-09-08 01:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f862fd39-3ef1-3a4d-9132-81bc7b7af355 | -9.72 | -43.46 | 2026-09-08 01:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3820d62f-e6c9-34f5-9dc0-6042b7c0124c | -3.56 | -48.15 | 2026-09-08 01:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 796491ef-2a00-35af-bc03-fe298a03bd83 | -3.53 | -48.15 | 2026-09-08 01:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd015a4-1325-3bb0-b513-e74bbe229bb3 | -3.5407 | -48.1673 | 2026-09-08 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 08ac1884-edbd-36fe-b0f5-7b2987ec3f0d | -13.2289 | -61.7161 | 2026-09-08 01:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b24fec0f-8145-305f-95db-b92c6a0fd954 | -13.2479 | -61.7148 | 2026-09-08 01:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 150b4cd8-bdd6-31a1-a845-95c554f9b247 | -3.5591 | -48.1882 | 2026-09-08 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 282.5 |
| 9c72c59a-81c3-3447-ae06-4da60e3f00a6 | -8.5323 | -63.8416 | 2026-09-08 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| d82d1854-376b-31ea-9d73-33d262a87df9 | -8.5322 | -63.8604 | 2026-09-08 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 481c398a-ea6c-3dd6-8cf1-a77e0644ad42 | -3.5406 | -48.1889 | 2026-09-08 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 236.6 |
| 911b2c39-3952-30cc-b470-4f4380b10c7e | -9.7508 | -43.485 | 2026-09-08 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| bbea1725-328a-3e34-a07b-ec66137e7dd9 | -13.2099 | -61.7173 | 2026-09-08 01:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 38.2 |
| c8b29482-6d1c-34c4-99c5-b12ecfdfbe6d | -9.7317 | -43.4874 | 2026-09-08 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 6d2a87f3-fdf7-3f6e-a878-4f7c21764a21 | -3.5592 | -48.1666 | 2026-09-08 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 96250b57-90c8-3f9e-9919-7645be5f9e86 | -9.7314 | -43.511 | 2026-09-08 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e5145f13-43d1-337f-a8df-f318d89073b7 | -9.7131 | -43.4664 | 2026-09-08 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| ba05fcfe-74ec-30ff-8f85-87a7e8d53ffb | -9.7134 | -43.4428 | 2026-09-08 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 7bb536fc-3bce-3a6b-9768-c8c2d84f13f0 | -9.7504 | -43.5085 | 2026-09-08 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 3482d55a-c725-3d7a-b9ef-00d61f93ab42 | -9.7138 | -43.4192 | 2026-09-08 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 9e452e3c-2bac-3afe-add2-4fc7b27e7aed | -3.5592 | -48.1666 | 2026-09-08 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| c3b78084-348c-376a-8c0f-10aac579a1b4 | -9.7317 | -43.4874 | 2026-09-08 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c81b8b90-75a6-3b77-b34d-3fb3bf0a50dd | -9.7134 | -43.4428 | 2026-09-08 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 0c6001bf-2052-3f88-8dfc-6226d7b9d6e6 | -9.7314 | -43.511 | 2026-09-08 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 28a83a69-02f4-313c-bb33-c7a38d2b5cda | -9.7131 | -43.4664 | 2026-09-08 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 22662d69-457e-319f-aef6-17338026551f | -3.5407 | -48.1673 | 2026-09-08 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 31633eb1-007c-3afd-b025-25b74cec9ba7 | -13.2289 | -61.7161 | 2026-09-08 01:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| b13b37a2-5ad3-3e6e-9d20-f8d4928ef249 | -3.5591 | -48.1882 | 2026-09-08 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 265.6 |
| e7731c02-e05a-3ec1-8aeb-94c6c5caaa0e | -8.5322 | -63.8604 | 2026-09-08 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1841b6b7-dc6a-3f76-9f20-6ad21747f779 | -3.5406 | -48.1889 | 2026-09-08 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 224.9 |
| 10ab8cc0-1541-376e-aec2-f14a7d9201ad | -9.4769 | -40.3365 | 2026-09-08 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.1 |
| d4890e4a-8605-38e6-940f-bb9176421803 | -9.7138 | -43.4192 | 2026-09-08 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 056b4d1b-f333-3e20-b9a4-9a527ad0eabe | -9.7504 | -43.5085 | 2026-09-08 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| e4e6bd37-12ba-3bff-96d1-4e31de58e8e3 | -9.7508 | -43.485 | 2026-09-08 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| b0285eb0-1f11-3255-8235-eabaa02a2000 | -8.5323 | -63.8416 | 2026-09-08 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 052111d2-5660-3cfd-a54c-197459799110 | -9.7138 | -43.4192 | 2026-09-08 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 94.6 |
| bba112b5-bbe0-3d0a-96bb-8dbf94fadd61 | -9.7698 | -43.4825 | 2026-09-08 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |


[Clique aqui para ver as próximas entradas](README7.md)
