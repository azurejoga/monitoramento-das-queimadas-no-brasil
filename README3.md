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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0cac025-19ac-3942-b683-354139889e97 | -17.87145 | -45.67487 | 2025-01-21 04:16:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e1fe04f-965c-31ff-abd6-c85306568c99 | -23.63141 | -46.42531 | 2025-01-21 04:16:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7e7e70ef-a87a-38ee-a8d8-1b0221265ae4 | -19.43698 | -44.34032 | 2025-01-21 04:16:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9c313ef-c695-3e54-a98a-cdd87065f9f2 | -27.0818 | -50.51051 | 2025-01-21 04:18:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2da9a1fa-397f-359f-97f5-2f2535000e1c | -29.86386 | -51.165 | 2025-01-21 04:18:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| efc798c0-2799-3c4c-bfe6-a6e2937db5a3 | -29.77809 | -51.1745 | 2025-01-21 04:18:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| ee721033-b51c-3429-bc23-f42528ed4fc6 | -6.8108 | -34.9387 | 2025-01-21 04:20:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| 8d3f9102-73d6-3f22-9067-fc5263efbd33 | -7.81731 | -35.15284 | 2025-01-21 04:42:00 | AQUA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 42ff20f7-a32c-3a0d-a919-9c162e8d12a0 | 0.89411 | -60.09159 | 2025-01-21 05:01:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53414424-6b94-3171-bae7-ee0fc8164d03 | 0.76448 | -60.0116 | 2025-01-21 05:01:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf7c3334-f2ff-3dee-bc44-fdb77ed7a2d0 | 1.0109 | -60.57795 | 2025-01-21 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99e87829-bdb1-322f-9365-e625f7222636 | 0.6269 | -59.74175 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdfe35c6-0a4b-3dda-b437-63293b009091 | 3.21969 | -59.90038 | 2025-01-21 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4a89d09-d9ca-3c3b-a35e-5a7d223897e9 | 2.16943 | -61.81842 | 2025-01-21 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0761a068-db47-3fbc-a820-cb852df7d54e | 0.70598 | -59.69062 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7d2c5d8-920d-38ec-b67f-05d65d2f30da | 3.59057 | -60.46704 | 2025-01-21 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 689d79b1-d981-3b70-a71d-2a77ce63c16f | 1.00646 | -60.57861 | 2025-01-21 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bac7d9b3-8fb5-312a-9e45-2820e5476d21 | 1.01014 | -60.57962 | 2025-01-21 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f486865-f3de-3175-9253-1eecc7a91748 | 3.73715 | -59.98954 | 2025-01-21 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb326bec-4146-3b65-a32e-fd0ee84f735e | 1.0116 | -60.58235 | 2025-01-21 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f323aae-92fb-34c9-80e0-8226f05c3fa8 | 3.60302 | -61.41818 | 2025-01-21 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89afc541-7deb-3989-af93-d008101b4e9c | 1.10265 | -59.70151 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a936afe-3a79-3226-b917-a63f5697aa98 | 1.3549 | -60.02482 | 2025-01-21 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6a1afa2-41a0-3bfc-be47-7b327ded6e89 | 0.86444 | -59.68288 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb06ed7a-db19-324e-a8b5-fb0747b61ec0 | 3.83731 | -59.93539 | 2025-01-21 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2773a632-e822-3100-8ba1-6587d199dc2e | 3.6071 | -61.41201 | 2025-01-21 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f3a76c3-b709-3299-9051-78295c313d95 | -2.12047 | -48.76052 | 2025-01-21 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c57b9d51-f041-3cad-82cd-2e068afc8d59 | 1.01287 | -59.51721 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13f7dc24-d481-3a48-8ef2-179cc1b54b04 | 0.80744 | -59.89676 | 2025-01-21 05:01:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c587f2b-aa80-3b0d-a6f7-e3a7ad52071b | 0.75467 | -59.64841 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0b9e2efb-e056-304e-ac48-c240da638c29 | 0.74863 | -59.64997 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bd2736c3-b113-33a5-b6fe-00dc5ad082a5 | 3.59093 | -60.46912 | 2025-01-21 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df9281df-25a0-3ce8-85d1-731605a90f40 | 2.18026 | -61.80986 | 2025-01-21 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea8486c7-34c6-3649-91f8-53a61342ef22 | 1.35669 | -60.02468 | 2025-01-21 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bef2ae05-aa2b-3e19-9ede-79b2063b5cf9 | 1.00715 | -60.58301 | 2025-01-21 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe398c9c-3bc6-3193-9c7d-aeec0729961f | 1.0057 | -60.58028 | 2025-01-21 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 759c428a-3546-3e4b-b92a-956a3698c6bb | 2.15666 | -61.01116 | 2025-01-21 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 511900fe-b989-3513-98c4-fc3e76633931 | 3.42458 | -61.11301 | 2025-01-21 05:01:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df8a632b-43ff-3b30-af7d-b5bd96c05bd4 | -1.78735 | -48.43705 | 2025-01-21 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b960648d-3262-3603-bb9b-8541db7e7b94 | 0.75053 | -59.64908 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ff30a680-0095-3c28-bb18-efcb0b62e8c1 | 0.78878 | -59.52503 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41e68675-a42b-330b-b0e0-69de09868493 | 1.08467 | -59.70366 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fc53d41-f16c-31b0-81b2-71b5b123de03 | 4.51709 | -61.05046 | 2025-01-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff41e92c-d1ce-324b-93ed-6b2eedf83ee1 | 3.82267 | -60.19668 | 2025-01-21 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5072855-d210-3d18-9856-6701fca481fc | 3.22408 | -59.89974 | 2025-01-21 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a128590-559d-32a2-ba50-6606ab88b27a | 2.17845 | -61.81157 | 2025-01-21 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc328333-5970-36bc-891b-e6fecf75fdcb | 2.82568 | -60.8786 | 2025-01-21 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85cf9c7f-6e6d-32fd-bdf7-d1c47758fecd | 2.65161 | -60.49971 | 2025-01-21 05:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09cebad9-1cc5-3a63-8ff9-f025fd2a6118 | 1.12498 | -59.40572 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2e3b9dd-c66d-31aa-bac7-16dcd9731961 | 2.15528 | -61.01382 | 2025-01-21 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd0f99a5-7cd1-37f8-9016-6a8698077fb3 | 0.70539 | -59.68678 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2c8d52b-4012-30ba-bd12-1af32e797692 | 2.83108 | -60.88282 | 2025-01-21 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32d8fd9f-6144-3d4f-9650-22636c4e3e33 | 1.01228 | -59.51343 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0972b108-a558-3726-9345-0fdaf570b615 | 3.24527 | -60.54495 | 2025-01-21 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f4ea451-934f-3bcd-89bc-75fa753a9770 | 0.86465 | -59.6172 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d5539d8-9e23-3825-bde5-fe46c23d06b2 | 4.33561 | -60.20174 | 2025-01-21 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39613e25-0dbe-3bdd-b0da-48f3c58150f5 | 2.15994 | -61.01311 | 2025-01-21 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b22cc7dc-a160-303a-9ec7-fe819516e4ef | 1.13519 | -59.5523 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bfcbf83-a6ef-379a-8214-e7dc77acb0f7 | 2.1712 | -61.81677 | 2025-01-21 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 56df2e2c-5a73-389b-a8a7-d354ff7199df | 0.8201 | -59.95141 | 2025-01-21 05:01:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a69fc80-4c49-3632-8804-64fc94c2d20f | 3.73334 | -59.9946 | 2025-01-21 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b803f96-d146-3d79-998b-40505719a8a5 | 1.15722 | -59.8895 | 2025-01-21 05:01:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc62fa4d-9478-3344-9fd8-4ca78a90d622 | 2.82641 | -60.8835 | 2025-01-21 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5fa1a84-7c85-3fc7-9518-e67a6b52543a | 0.75277 | -59.6493 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 33efd8ff-2d5c-395f-94fe-126de305e643 | 3.9177 | -60.83511 | 2025-01-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1bd49a49-02d1-3764-8804-01bfb9bf940c | 2.17202 | -61.82229 | 2025-01-21 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9f326974-dc7c-383d-93df-0b499118239e | 4.02438 | -60.8269 | 2025-01-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16e8b6a7-944a-31d2-88d5-0d2d096d82cd | 1.1429 | -59.54733 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea9fbc09-adc3-3878-a359-45888c59d1c3 | 1.00709 | -59.47998 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f63ad96-9520-31b6-bc10-7a46fea1022c | 1.12555 | -59.40937 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 624b79cb-3c90-31d2-99a3-512f6bd469a1 | 0.90273 | -60.4351 | 2025-01-21 05:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1efdff90-dd5e-3089-aded-36d140b7b37a | 0.75408 | -59.64469 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9e7cb73b-9de5-371c-8fd7-5c459a18a485 | 2.62355 | -61.45866 | 2025-01-21 05:01:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38e24681-78b7-3c22-be0a-cb244e95e331 | 0.74627 | -60.03478 | 2025-01-21 05:01:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e8498b8-27f5-3d1f-8532-ae8938c22709 | 1.13875 | -59.54792 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59ab548d-6a18-3b4e-b3e7-51e6535a841c | 3.22033 | -59.90464 | 2025-01-21 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 457a1a20-2b02-33e2-aaba-11083a4b87d9 | 4.01966 | -60.82769 | 2025-01-21 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32acaeb5-7567-3779-a1a7-1deba1181cde | 1.92612 | -60.49319 | 2025-01-21 05:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f545bef7-2873-3d0b-beae-23edb6ac9dc1 | 2.82495 | -60.8737 | 2025-01-21 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f4b92ee-e7c7-3b30-8be4-7f6be1f73b8f | 0.9264 | -60.32717 | 2025-01-21 05:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1af7a8fb-95eb-336a-871b-6db2a588f29a | 3.60104 | -61.42122 | 2025-01-21 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0f038f6-c9e1-3b55-a85e-f7f2532f7683 | 3.91513 | -59.76159 | 2025-01-21 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9823180b-0588-3cce-8a21-b6661befcb21 | 0.86249 | -59.68739 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5093e708-7e50-3e33-bb44-48b655893d6f | 0.678 | -59.70252 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83c32bbe-fb10-380d-886e-ae472759eff1 | 3.17499 | -60.45011 | 2025-01-21 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edba26fa-5f71-3971-acab-7c58051f3fde | 1.08587 | -59.70391 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5730295-d590-359c-acae-a4d359559537 | 3.60517 | -61.41504 | 2025-01-21 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e88d4e75-f530-384f-be4b-6ef7a630a38c | 0.75221 | -59.64556 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3471307a-23c6-3876-b0c7-e5bc88c2ff88 | 0.86192 | -59.68362 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 223cc6fe-7441-3abf-823f-ff38d4fb7e22 | 0.86504 | -59.68665 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4d391ef-e972-3749-bf99-a279005896b7 | 2.17029 | -61.82396 | 2025-01-21 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d86d66db-ca02-3ad9-8539-145bb57376c1 | 1.1346 | -59.54855 | 2025-01-21 05:01:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6980c774-ea28-31ff-9977-48f0fad9bec7 | -4.55289 | -50.18495 | 2025-01-21 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdb904ea-097c-38bf-aff3-3ca9355ac684 | -2.47164 | -49.12415 | 2025-01-21 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d07d340-d809-3d92-a79f-39019a5e1540 | -2.66111 | -48.79333 | 2025-01-21 05:03:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f123642-dbce-3bdd-81a6-03a15b834b5a | -4.54886 | -50.18409 | 2025-01-21 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7468d0e-0d99-357d-a6e4-636fc99340e3 | -2.47104 | -49.12808 | 2025-01-21 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 538578c2-53b4-3b21-899a-75d64c7c4dd4 | -5.01018 | -56.17542 | 2025-01-21 05:03:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c878aa65-7df9-3cd5-ae46-5fd62172a43e | -12.17611 | -45.82542 | 2025-01-21 05:05:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b910fde8-a9fa-31eb-a730-fc80300fa2c3 | -12.1756 | -45.83006 | 2025-01-21 05:05:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README4.md)
