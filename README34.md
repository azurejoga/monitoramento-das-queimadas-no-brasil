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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e1f13ff-5a81-3531-8600-6a05e128f1b4 | -6.5302 | -58.5227 | 2026-09-09 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 92b10126-882c-3659-ab97-6af6ee7544ca | -10.7006 | -45.9698 | 2026-09-09 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 340.4 |
| 341bd65a-565d-3a7c-85d0-09ca71b279fa | -10.2559 | -45.2292 | 2026-09-09 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 281.2 |
| 076221dd-28d9-302f-8750-907d4ddda25b | -2.0585 | -56.4284 | 2026-09-09 15:50:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ad5bea03-f0ba-3fc9-84d5-ddbdb87e3a04 | -1.4935 | -54.8155 | 2026-09-09 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5296033c-cca8-3017-bb00-ff11a1c948e7 | -9.371 | -66.6752 | 2026-09-09 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 130.5 |
| a4391512-b5e9-3eb3-9c36-feba98696217 | -12.0379 | -64.0327 | 2026-09-09 15:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 06a7d753-8fc7-3d2c-84cb-3007ab0b0b74 | -10.2563 | -45.2062 | 2026-09-09 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 8595948d-db19-323e-9181-2f7434e21e02 | -10.7578 | -45.9624 | 2026-09-09 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 4f9d48aa-7a02-397e-afad-4681b43020ed | -3.0254 | -57.8738 | 2026-09-09 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d446df70-8ec7-3579-84a0-8b1a29ed0c60 | -9.0722 | -60.434 | 2026-09-09 15:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 34c96743-6e7b-38dd-a6ab-062df887463c | -10.2372 | -45.2087 | 2026-09-09 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 93606f3c-db9a-38eb-ae25-84c05e97b186 | -10.7395 | -45.9194 | 2026-09-09 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 5f5461a8-3709-38dc-9fe3-b2b763eabc12 | -9.3525 | -66.6757 | 2026-09-09 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6214166e-dd06-3249-ac98-0180e29bd532 | -9.3711 | -66.6566 | 2026-09-09 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 3561e1a2-9467-305c-a471-3b516cc0f77b | -10.6816 | -45.9723 | 2026-09-09 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 0fd50e45-7e15-38bd-a547-28a6a5fc4ad4 | -10.7204 | -45.9219 | 2026-09-09 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| a46cd373-95ea-364e-8295-47386ca092ae | -8.9783 | -60.5733 | 2026-09-09 16:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6c389844-76f8-3f6b-a318-8597299f16e3 | -6.7648 | -59.4408 | 2026-09-09 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| f55a8713-665e-361c-ad10-3c4c1d3da13f | -9.3525 | -66.6757 | 2026-09-09 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 886e0757-1844-346a-8c5e-735686f9d5bc | -9.371 | -66.6752 | 2026-09-09 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 3f3afa51-313f-30c4-b5d1-6e0ff9404727 | -10.7387 | -45.9649 | 2026-09-09 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| b50cc5ae-d273-3ab8-83db-f63a6ffd51b3 | -6.9701 | -59.0272 | 2026-09-09 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| e7217a97-27d1-38e8-8ec3-45930b329be6 | -10.2563 | -45.2062 | 2026-09-09 16:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 4a3ef6fa-7cf3-35b2-aa1e-e9e7b0886b90 | -3.0254 | -57.8738 | 2026-09-09 16:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b50f3e59-6f1d-3e7a-9995-a2deee0e99aa | -6.7123 | -58.9412 | 2026-09-09 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 688d922a-d520-3919-8123-53d0936fd69a | -2.0585 | -56.4284 | 2026-09-09 16:00:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| fa65db55-f391-37a4-9f39-1cae57fcd36f | -10.7006 | -45.9698 | 2026-09-09 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 355.6 |
| d7692332-47e8-3554-b7c7-cae3dbeaf6ae | -2.0586 | -56.4088 | 2026-09-09 16:00:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 94ebc006-4081-3633-8fae-4ba215580819 | -13.2725 | -61.1299 | 2026-09-09 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 397ba344-af41-30b1-9f8a-b26e91fdb0fd | -13.2727 | -61.1104 | 2026-09-09 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 488f66f4-d5ca-3291-ac05-516c23540bfc | -10.7391 | -45.9422 | 2026-09-09 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 255.1 |
| 79fe0dd8-972c-3cc8-aa81-2702e1d7ddce | -2.1179 | -54.3874 | 2026-09-09 16:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 8e9982c3-7831-3fc6-8ee3-1943119d75e6 | -10.7395 | -45.9194 | 2026-09-09 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 75237d2e-5104-33e7-875d-0d35daa9ab6e | -12.0379 | -64.0327 | 2026-09-09 16:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 19443ddb-5dd4-33b7-822e-61e88ea328e3 | -13.2723 | -61.1493 | 2026-09-09 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 3f937746-140b-373f-8e5f-6f64bb11954c | -10.7208 | -45.8992 | 2026-09-09 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.9 |
| 07fceeec-c848-39a5-b38f-e1f8bcf562f0 | -8.6198 | -47.3672 | 2026-09-09 16:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 37c05b86-227c-3b5b-99a8-7c3ea0e5f99c | -10.7578 | -45.9624 | 2026-09-09 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 78d4da82-56cf-39a8-9f56-cee00e324429 | -9.7698 | -43.4825 | 2026-09-09 16:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 4427b808-9088-3d0e-950c-39ca00572bf8 | -10.7193 | -45.9901 | 2026-09-09 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 26098561-065f-3c50-b7ab-00598f45c145 | -3.0254 | -57.8738 | 2026-09-09 16:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| ca6cb554-0c25-3f78-b0a3-55361d483d02 | -13.2094 | -61.7755 | 2026-09-09 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 088a4600-44c0-3230-8475-e74bf4895acc | -2.0585 | -56.4284 | 2026-09-09 16:10:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 6b713dc8-4a18-352c-9562-e463d340b935 | -13.2476 | -61.7536 | 2026-09-09 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e732aac8-10ba-394f-9da8-4934741bc744 | -2.1179 | -54.3874 | 2026-09-09 16:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3d4febd1-fff6-3982-b33c-b90dc2affa7e | -9.3711 | -66.6566 | 2026-09-09 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| d6a130b6-4ff3-3144-adfd-541fc5f967b4 | -10.2563 | -45.2062 | 2026-09-09 16:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| e8293e49-4e29-354d-91fa-3a29975e140a | -10.7003 | -45.9925 | 2026-09-09 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 625.1 |
| 3e6ba057-d991-39d2-baf8-3e55827c1430 | -10.7006 | -45.9698 | 2026-09-09 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 513.4 |
| f0d4e048-138c-3b2e-9547-cd3deb4695a3 | -10.7391 | -45.9422 | 2026-09-09 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| b37aa889-40a9-3c3d-bf06-d3b880454aae | -10.7395 | -45.9194 | 2026-09-09 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| fd169407-e07a-3ec5-be32-4539223c4a0f | -13.2092 | -61.795 | 2026-09-09 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 14959e8c-e3e7-33ae-b086-a9500aed8b4f | -2.0934 | -49.5359 | 2026-09-09 16:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f76f6b99-aab5-3ff7-8eee-5732d4143020 | -8.9783 | -60.5733 | 2026-09-09 16:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6daf99f5-2b95-39ed-a35b-5bd7a4663f3e | -9.371 | -66.6752 | 2026-09-09 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 5ea4e437-e650-399f-b1f9-25b949663b95 | -6.7861 | -58.9382 | 2026-09-09 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 876defa6-8841-3672-acb7-6d5a83f102cc | -10.701 | -45.9471 | 2026-09-09 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 90aa7a86-df00-30cb-a189-001e98dbe3e5 | -12.0379 | -64.0327 | 2026-09-09 16:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 8ccc1a27-1e04-3814-a552-2567a3899467 | -6.9701 | -59.0272 | 2026-09-09 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| f760ca75-7f62-326b-9322-b230261e3a8f | -10.2559 | -45.2292 | 2026-09-09 16:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 273.9 |
| 53774c30-54a7-3009-b62e-fe876ed11d33 | -2.0586 | -56.4088 | 2026-09-09 16:10:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 429a7af0-132c-3396-93df-9b848b1ffe33 | -10.69 | -46.01 | 2026-09-09 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc186347-f913-3ac0-8bf4-55e177d53c11 | -3.0254 | -57.8738 | 2026-09-09 16:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 8ce5e0bc-f929-3096-9981-006b1e76fc39 | -6.7123 | -58.9412 | 2026-09-09 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 0e4e76f3-5186-3f38-85cb-900074fefe85 | -2.0585 | -56.4284 | 2026-09-09 16:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 15b10fe0-5df8-3641-8cb9-11216202c08b | -9.3711 | -66.6566 | 2026-09-09 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ae9a5c15-8289-3ff2-afe3-dfff4a93e8e4 | -10.6816 | -45.9723 | 2026-09-09 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 677.6 |
| d1477c42-9eb4-3001-b886-a1f468a70269 | -2.0586 | -56.4088 | 2026-09-09 16:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 538eb371-c4fd-351a-b37d-9dd43251d906 | -10.701 | -45.9471 | 2026-09-09 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 5beaa626-bb74-3e9b-9b52-7c4ff3f32681 | -9.371 | -66.6752 | 2026-09-09 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| f419c9b4-3f10-3fd9-b471-412303916d58 | -10.7395 | -45.9194 | 2026-09-09 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 2cebc01c-0de4-3926-83b0-4d292f36d506 | -10.7006 | -45.9698 | 2026-09-09 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 629.9 |
| 9a69100e-2630-38fc-9ca7-1ab6fe92832b | -10.7391 | -45.9422 | 2026-09-09 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 139225af-db17-3277-9130-fa20b2423ae7 | -2.1179 | -54.3874 | 2026-09-09 16:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2e606d23-958b-31f9-855f-b2f213422409 | -10.2563 | -45.2062 | 2026-09-09 16:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 3d234238-2e36-3f5c-aedd-ba88a8596bc5 | -10.7006 | -45.9698 | 2026-09-09 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 47878900-74ea-3c61-a86b-8be66fbdf7cd | -12.5198 | -62.6679 | 2026-09-09 16:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 0c26f049-12f2-3a52-9991-dbf366b9c6b7 | -10.7391 | -45.9422 | 2026-09-09 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 677.7 |
| b15ff30e-d057-3e03-bef3-41f74cdc1301 | -6.7123 | -58.9412 | 2026-09-09 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 2c92872d-2b2f-399c-a276-595e2a008da3 | -10.7578 | -45.9624 | 2026-09-09 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 402.5 |
| 81a06852-baa6-3b4e-9d43-7b51f7b9b3b4 | -10.7395 | -45.9194 | 2026-09-09 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 5a379c0b-4c48-3f1c-bd3d-fb134bd70a11 | -2.0586 | -56.4088 | 2026-09-09 16:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 109eb23e-4deb-3ffa-ba75-88d145933b30 | -10.7387 | -45.9649 | 2026-09-09 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 309.1 |
| 27738487-abe4-3fa7-a475-d261a3c95027 | -2.0934 | -49.5359 | 2026-09-09 16:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| dcc3518d-b027-33cf-ae5e-949e8c73c4d7 | -2.0585 | -56.4284 | 2026-09-09 16:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 7bddda1e-5e3f-3d46-8b18-0f335f26cff3 | -10.7003 | -45.9925 | 2026-09-09 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 2094a7e0-d3e7-3fe8-83c1-fd957d2c54fd | -10.7395 | -45.9194 | 2026-09-09 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 124360ee-9c0c-3d4f-aebb-8a9f4b94dd35 | -12.5198 | -62.6679 | 2026-09-09 16:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 29109f51-cf84-3b2f-ad78-276747374cbc | -10.7391 | -45.9422 | 2026-09-09 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 4bccd665-56b7-378b-8738-d1f04c86e950 | -2.0585 | -56.4284 | 2026-09-09 16:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 91733177-ae72-39ab-b69e-573dd3c89efd | -6.8386 | -59.4379 | 2026-09-09 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 7bce4902-fe26-35c2-abae-6374a30a2855 | -10.7006 | -45.9698 | 2026-09-09 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| f0febd64-14fe-3d8e-830e-71cbdccf5fb1 | -2.0586 | -56.4088 | 2026-09-09 16:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 05ebe715-70f5-3dad-89e9-b3ff66326d09 | -10.2563 | -45.2062 | 2026-09-09 16:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| c50e5f81-d41e-3e29-8d49-3a3f313dc02b | -10.6999 | -46.0153 | 2026-09-09 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| cc19c0b2-2547-33a9-bbc5-55137e575909 | -2.0585 | -56.4284 | 2026-09-09 16:50:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0f1b26f1-0171-3a7d-ba3a-7203e9a2e45b | -10.6995 | -46.038 | 2026-09-09 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| bea857a2-d950-3eea-a46a-13e7cd0ba873 | -10.7006 | -45.9698 | 2026-09-09 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 394.7 |
| 8abb7c6e-f678-33af-92c7-fefcfb6ebe8d | -10.7391 | -45.9422 | 2026-09-09 16:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |


[Clique aqui para ver as próximas entradas](README35.md)
