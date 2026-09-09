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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e800f3e8-f59e-3efa-9b74-4f67aec5e1b7 | -7.08113 | -59.82069 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4e0d300-e16e-3477-80e5-4c43f63fdd96 | -5.37207 | -56.02551 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 92028605-0e15-36b7-9f51-f97ac92a6151 | -8.42228 | -46.89482 | 2026-09-09 04:46:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9d0bd1e-0d7f-3f9b-87ed-9ca18949fc92 | -5.80436 | -53.80694 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 057ae902-6977-3cf6-b94d-61332e5536dd | -9.69825 | -43.45173 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a469fc24-e11a-355c-b270-5a750ed2d99d | -7.19541 | -43.62789 | 2026-09-09 04:46:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bef4f04f-2008-32e5-ba19-cd4fa37e77ab | -9.70433 | -43.4086 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c58ecd54-a6e1-3d6e-8859-dcfeb789bca7 | -10.73314 | -46.01169 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c42dee4d-dc3e-34cc-a235-aab16d7cd3b1 | -6.83679 | -51.49234 | 2026-09-09 04:46:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0266ad99-06ad-3af5-85c5-fc4303078b8b | -9.69572 | -43.4365 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 8f7ee7bb-ba4c-3305-a0a6-6c638c575aac | -6.86511 | -46.01769 | 2026-09-09 04:46:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fd99870-2734-397a-af34-dc1629ac4b23 | -5.21178 | -55.99226 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 758c91c5-05d7-3bb8-8396-4d5c756b25b0 | -10.7508 | -45.97306 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a30c0c82-4de3-36f7-94d8-08ed27eeb6ad | -6.24651 | -51.6732 | 2026-09-09 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 856d4a0a-a0fc-3729-8697-6ea3f91d0a1f | -9.70889 | -43.40652 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 58467a76-74a4-3f11-a301-15b76c1d54cd | -8.76024 | -62.41044 | 2026-09-09 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dac92ea-008b-3351-812f-bafd8e1363f4 | -5.81204 | -53.8083 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab0047c9-3d87-3497-89ed-4b58e1f633b1 | -9.70049 | -43.43443 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| dc891ecd-bea9-3941-91ab-8442c90bf1ff | -9.69759 | -43.4894 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 14620a53-35e5-3b5b-8f97-8d7f9c97ef6a | -12.95421 | -48.61149 | 2026-09-09 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 44624b3c-0dc7-3a21-bf54-1208d5c176b0 | -7.19167 | -43.6231 | 2026-09-09 04:46:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc907e8b-ca17-3212-9348-4404577fb88c | -9.76249 | -48.75359 | 2026-09-09 04:46:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b1f1bd9-f437-3234-8d7c-ac5b64c83a03 | -9.69816 | -43.48687 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f07e2f6c-2640-353c-9d81-ac3db109c867 | -5.81972 | -53.80961 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 600c93de-2d82-37a1-b571-e7e9a27237e1 | -6.79951 | -58.95153 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ae93da1-4526-3dbe-bd82-2419e53eea9d | -11.4353 | -45.15582 | 2026-09-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29f47a92-4bf4-3a45-80d4-270ad3603a6c | -5.3676 | -56.02473 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a0368c02-7f84-3007-add1-4b0aca64cc4f | -8.74206 | -62.40112 | 2026-09-09 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5900c294-b934-3a5b-b168-b1c7c0959ddd | -5.36579 | -56.02203 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1429b860-f5b3-3579-a0af-b6474c47d2e7 | -6.86206 | -46.01257 | 2026-09-09 04:46:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 128dcd4c-68d7-38bd-9ccd-92db3312ca4c | -6.78474 | -58.94163 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fc95019-8a0a-3f18-ac8a-d7e1a11cfd24 | -5.82977 | -53.79638 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53b44394-2429-3720-b34c-d8d8500efbf1 | -9.70892 | -43.40925 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5ca2e2fd-1c4e-3846-aa5b-13a4bc70771d | -11.43581 | -45.15208 | 2026-09-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 836b77d0-218e-3082-9538-6b5175e0f066 | -13.28827 | -61.78646 | 2026-09-09 04:49:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acf5addc-888f-36a6-a129-9f7d162593de | -13.28776 | -61.78253 | 2026-09-09 04:49:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 806c879e-7881-36ec-b1b7-7e6e3de66406 | -13.28695 | -61.78659 | 2026-09-09 04:49:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50cb0e5c-3396-3294-b1e4-d401c79e04de | -13.28615 | -61.79066 | 2026-09-09 04:49:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79c1e224-f8b3-3c05-8bff-102419979bf2 | -13.28744 | -61.79052 | 2026-09-09 04:49:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a55fa9e-cb55-3f07-98f7-76ef12df1633 | -13.27965 | -61.79347 | 2026-09-09 04:49:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b577392-4b6e-30c2-b5ca-dbc67ea1b593 | -14.67826 | -48.92065 | 2026-09-09 04:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 272db022-19a7-36f0-a15b-b1549d39cfe2 | -23.65762 | -50.38011 | 2026-09-09 04:49:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 2e401e8b-53fa-3f10-81e2-44a8db499881 | -13.28091 | -61.79333 | 2026-09-09 04:49:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 965d89a5-5630-3536-89e3-c936417c41a8 | -13.2891 | -61.7824 | 2026-09-09 04:49:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5227d212-2301-32ba-95f4-7c8bcf7b6b90 | -13.25993 | -61.68405 | 2026-09-09 04:49:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ab59373-5153-3d28-9a20-ee45b1968b30 | -28.94054 | -50.82753 | 2026-09-09 04:51:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c859f833-7aa6-3ae5-bbc7-5ee1c38d4332 | -29.10774 | -51.91053 | 2026-09-09 04:51:00 | NOAA-20 | DOUTOR RICARDO | RIO GRANDE DO SUL | Brasil | 4306759 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7726543b-db0b-3983-b590-f8df940ee711 | -2.93741 | -50.47044 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e464477a-b17d-3e69-8f98-02cf824ca5c1 | -2.94215 | -50.46842 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 92eab441-8f5c-3f14-95d2-b9ad9dc64915 | -2.89373 | -48.2799 | 2026-09-09 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 62f1fa0d-d2ac-3c6e-952f-04d034f3b561 | -1.19707 | -55.70757 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9f9cb91-9d58-3485-a94a-08c25de90429 | -1.19595 | -55.71503 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bb5176e5-2452-30cc-a96e-17a22c4c3c54 | -2.9435 | -50.45945 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 917f2584-5e49-356e-a04c-6fa2031908fc | -2.93677 | -50.47491 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1229c45d-2d21-3e4b-8768-d54501d8ed0b | -2.93614 | -50.47932 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3d3c3e50-d69d-3c98-8aab-fd03967a7d7b | -2.56154 | -54.74544 | 2026-09-09 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 06a1e4d3-1d64-3bfe-bb93-8db057a96c50 | -2.93543 | -50.47203 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d2d2adf2-6cb5-324a-99f5-44df5d1a3a2f | 2.38655 | -60.25611 | 2026-09-09 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f169046-b991-32ad-bf76-1315e29254bf | -3.24955 | -50.82417 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 49be3895-170d-36c8-ae48-26b1fd6dfc73 | -1.67042 | -55.6661 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| de11b4ab-59ab-3fa2-b592-be86c1f67ba0 | -3.54269 | -48.18136 | 2026-09-09 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d76d1faf-b1e3-39fb-aa3f-fa7f49d8572d | -3.2631 | -50.07948 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d5294877-3b98-36d8-9861-d94e9abebc70 | 2.64928 | -60.17627 | 2026-09-09 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6eb0f0c4-bbb5-3897-ad5c-97440d7fce71 | -1.2116 | -55.75116 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29f6cafd-dcab-38a9-a6f3-8a793697ecde | 2.66379 | -60.17744 | 2026-09-09 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4177b351-d00a-321b-bdb5-90d504480de9 | 1.17163 | -60.49579 | 2026-09-09 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffdb8237-0dfd-3972-bda4-1af8f2548f48 | -2.94346 | -50.47132 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e3658b18-64e8-33bf-9605-351534f7d207 | 1.67398 | -60.13948 | 2026-09-09 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ec3962a-ee10-356b-996f-01846cb18015 | -1.03506 | -53.73284 | 2026-09-09 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cab03742-708b-3529-9e8c-0e18218c34c6 | 0.30637 | -60.44525 | 2026-09-09 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1f2f442-388b-322f-b426-22d23cb94ecf | -1.56524 | -55.25072 | 2026-09-09 05:27:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c6869d5-be82-37c8-891c-50dd22769b1d | -1.03589 | -53.7275 | 2026-09-09 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 96c834a7-ba89-31f1-bd9d-2e974a41fa94 | -2.93869 | -50.46141 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 647e161e-1a3a-31e0-b872-ce6ea88798fb | -3.26239 | -50.08438 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7fab7e9e-947f-3035-972b-3c5dfb5895a1 | 0.31788 | -60.44994 | 2026-09-09 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c40d66bf-83a0-3ed5-9c92-f27c7d30a309 | -2.94218 | -50.48028 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e2d31955-3901-3389-87e1-f74c1c18b8bf | -2.93805 | -50.46593 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d983c42d-beed-344a-827d-62745b121431 | -1.31535 | -54.65323 | 2026-09-09 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b6b1c96-5675-3e72-8d38-115a9fe20392 | -2.12183 | -54.38863 | 2026-09-09 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 84bb7281-1c5d-33d0-b881-d4d1a83a0a68 | -2.94474 | -50.46237 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| caa64181-79f1-3713-b814-93be960ba16d | -1.19182 | -55.7144 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 863828eb-d21b-3288-919c-0d877157c592 | -2.94618 | -50.4828 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd3b22ff-24db-3dfa-a10b-4c8bcf362ba5 | -2.93476 | -50.47648 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6189a6c4-e57a-32ab-9dc6-7691811b7627 | -2.9441 | -50.46684 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 63ef2b2c-f655-34d6-9838-826501681b9a | -2.84422 | -53.9943 | 2026-09-09 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a0c2a08-f92c-3d61-aa39-730a604bb169 | -1.18804 | -55.72219 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bab2fc98-01e1-3d0f-bc54-04f6d0f3c577 | -1.20121 | -55.70815 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5703abc8-75fd-3a72-82f0-2c756ee5b2a2 | -1.61294 | -54.9145 | 2026-09-09 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6327398-f718-31fe-b482-e45387cffd05 | -3.26862 | -50.08528 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d68a10a4-8729-3b9b-ad3a-ee1f9d8977ff | 1.81833 | -50.95363 | 2026-09-09 05:27:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c220f91-cb1f-391b-91bf-4469468c948b | -2.93934 | -50.45686 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b1ae31ae-e877-3a21-bddf-89cfc3e692f9 | -1.1935 | -55.70314 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24e9d0b3-586a-3f8a-adeb-9665e0ba9415 | -1.31404 | -54.66171 | 2026-09-09 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a446c72-9ea2-3964-91a9-005f20e56e25 | -2.94539 | -50.45782 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e2e175af-565d-3cbd-a128-181e7951d0b4 | -2.56221 | -54.74092 | 2026-09-09 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9086e67-2a13-3ead-8d04-771474790e3d | 1.10338 | -60.51331 | 2026-09-09 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 453a5d27-717c-3f00-92f8-e6d6b27500f4 | -1.31911 | -54.65834 | 2026-09-09 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 70b1a551-211f-38db-8d86-1396510d2330 | -1.31469 | -54.65747 | 2026-09-09 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3f4df7e8-2de7-318a-b249-8ae8ced7e28d | -2.94282 | -50.46397 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 93f2a97f-3857-3d41-8f06-57e0a9f03c1f | -2.93745 | -50.45848 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README24.md)
