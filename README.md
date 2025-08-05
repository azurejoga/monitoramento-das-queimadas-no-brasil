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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63ef6c42-629d-303b-b293-c05d41b994b1 | -13.0535 | -56.8947 | 2025-08-05 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 21f189cd-d54a-3997-8bf3-9e1271580152 | -6.9607 | -42.858 | 2025-08-05 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 7a632938-60c6-3ac5-842d-8f099ebb2594 | -13.0538 | -56.8746 | 2025-08-05 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ea1477bc-6b72-3a0d-8943-0fe2943ab3a6 | -7.994 | -43.1534 | 2025-08-05 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.7 |
| eac51a64-9612-3cfe-9ebc-7783f0f0267a | -14.308 | -54.7078 | 2025-08-05 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 2179f0f0-db2f-3693-93fd-45a2007c673c | -18.0619 | -51.3063 | 2025-08-05 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a0b4198b-d154-3fb2-903e-65b6579977c9 | -6.6672 | -49.7995 | 2025-08-05 00:00:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| dd15dc47-5296-3d00-b164-aef30501d2f6 | -8.0132 | -43.1278 | 2025-08-05 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| ead9af98-d966-3186-960e-e24498f1292e | -13.0726 | -56.893 | 2025-08-05 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 00664d97-79b0-39de-ac83-9b94c623b812 | -14.3083 | -54.6871 | 2025-08-05 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 5df6be55-0a5d-3bce-8c4a-744769884060 | -7.9943 | -43.1298 | 2025-08-05 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 92a6e29e-771d-32f0-b498-033eda0ebd85 | -8.9478 | -46.7354 | 2025-08-05 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e7781d71-01a1-393e-9bb3-111224230641 | -6.686 | -49.777 | 2025-08-05 00:00:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1334ea31-7bcd-308e-a132-dca6c6844844 | -13.0728 | -56.8729 | 2025-08-05 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| b9f2a9ba-d203-30bc-96bf-6b78d4723f51 | -6.6858 | -49.7983 | 2025-08-05 00:00:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 37b07e0a-2941-3074-bb57-23bc3650c84b | -8.0129 | -43.1513 | 2025-08-05 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| a4aadd27-a5d1-301f-a1f4-eba56c7e85a9 | -13.0916 | -56.8913 | 2025-08-05 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 822f6ad3-9b19-3dfd-9d79-d1dc1774e13a | -6.6673 | -49.7783 | 2025-08-05 00:00:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f251a6f2-0d97-3b5b-ae00-0062bac23cf1 | -6.6672 | -49.7995 | 2025-08-05 00:10:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 763c21a4-fa35-3686-879c-9a3727656818 | -8.0132 | -43.1278 | 2025-08-05 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| b085a20f-b782-33fa-82e0-19e828c29aff | -8.9478 | -46.7354 | 2025-08-05 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9835a477-1ab1-3177-98de-6ab1aba98588 | -6.686 | -49.777 | 2025-08-05 00:10:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 1cfd0ad7-9141-3d1a-b35a-bcb5b4ecebed | -18.0619 | -51.3063 | 2025-08-05 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| cc142d36-b6be-31f5-b174-f996b3dd7871 | -6.6858 | -49.7983 | 2025-08-05 00:10:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 87aec95d-210e-3613-8519-8e4ed4adee6e | -13.0723 | -56.9131 | 2025-08-05 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 720f8ecd-3c64-3e14-9ddc-d43e1a3e22a9 | -13.0342 | -56.9166 | 2025-08-05 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 01e7869b-42dc-31c1-9505-1f333f6464b3 | -13.0533 | -56.9149 | 2025-08-05 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 95271801-c2ee-3747-8be6-99b0b0f0c345 | -14.3083 | -54.6871 | 2025-08-05 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 1ff15f4b-b227-3200-bfe0-d6bfa55e4efc | -7.994 | -43.1534 | 2025-08-05 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| 06840a32-98ab-3ef5-807c-e56f8924929f | -7.9943 | -43.1298 | 2025-08-05 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| c09a54c6-0444-3a64-bd3f-8775685bea99 | -6.686 | -49.777 | 2025-08-05 00:20:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5891251b-860b-3cee-9cd7-9946181aa5fb | -8.9478 | -46.7354 | 2025-08-05 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| c0dbac08-f59d-38db-8972-9a8b260d10f6 | -15.6732 | -49.7947 | 2025-08-05 00:20:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| f148ba84-32c8-39a6-b087-6a361d05cb7f | -15.6728 | -49.8167 | 2025-08-05 00:20:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d02d6ae6-5038-3d32-8516-3808fcbc6058 | -7.994 | -43.1534 | 2025-08-05 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| b1d5b174-3da1-3ede-a91c-26bb0fae0cc3 | -3.1832 | -49.4642 | 2025-08-05 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 7429c92e-c4b0-32f2-bee7-1ad338519c10 | -7.9943 | -43.1298 | 2025-08-05 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| edd496c3-a626-3ad4-bb86-3abd2fee0979 | -3.1833 | -49.4429 | 2025-08-05 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 02834034-0130-3d00-8152-ebbd70acaeb8 | -6.6858 | -49.7983 | 2025-08-05 00:20:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 7ccdc1c2-3b6e-3a6b-9b82-f2553d639654 | -3.1649 | -49.4435 | 2025-08-05 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 99f6d774-08de-30d9-83be-c507f89932ff | -5.6131 | -45.334301 | 2025-08-05 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7fb9cf9-ad87-3497-a159-91141f3f6a4c | -9.559 | -40.342201 | 2025-08-05 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 75b12b52-d439-350a-aba9-f7466cc0c12b | -8.7259 | -46.435902 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cec24c64-ce11-3c27-8900-0bcbc5bb18f2 | -6.5742 | -44.216999 | 2025-08-05 00:28:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba995553-26c6-3d62-b044-2f0311f80a98 | -10.4809 | -44.388 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7e059a2b-4260-3eb6-9de3-3b3a26dfa703 | -9.4087 | -45.483299 | 2025-08-05 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0a1e3dca-2f73-3d5a-81ed-e310dde4ff5a | -7.9052 | -45.531101 | 2025-08-05 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac4a32f9-ac47-36ef-a5a9-4ff4479b03cc | -8.158 | -49.131599 | 2025-08-05 00:28:00 | METOP-C | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c08eb703-873e-3182-b29f-8684f6580ffe | -7.8651 | -46.727901 | 2025-08-05 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73a421fa-70fe-3732-a620-9118203ef444 | -8.0248 | -43.1245 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8cf1c344-33ef-361a-bcc4-6d1649eed0eb | -6.5573 | -44.0093 | 2025-08-05 00:28:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 968a0a73-36df-3a1e-b484-6d5a807ea125 | -3.0304 | -49.4324 | 2025-08-05 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7ad1f33-afc9-3ca7-84ee-fb09c018b2e9 | -7.5474 | -45.0439 | 2025-08-05 00:28:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f95a842c-09df-3e97-8af0-756b64ad2eaa | -11.7631 | -45.0079 | 2025-08-05 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0af7b784-f474-3370-9ac6-6946e8ab3521 | -10.486 | -44.364899 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 04ca37c2-87e1-3759-b36b-4dcb2685a8d8 | -10.5781 | -50.473301 | 2025-08-05 00:28:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c332e1ff-45bd-3132-bf81-8304db824fed | -3.7859 | -41.6805 | 2025-08-05 00:28:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1ae10d96-e683-3303-bbab-41754b351341 | -8.7439 | -46.424 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3485dcaf-42ae-3d57-b537-d78cf55c8ec3 | -7.7201 | -43.9053 | 2025-08-05 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0eb24ae0-c809-36dd-b729-ed8340b4451b | -8.2715 | -45.054798 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74e1377e-d38c-3279-a6bc-2537c37e77eb | -8.2632 | -45.0639 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c6f475da-2043-38c4-986b-3e7f45647600 | -10.455 | -44.3647 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c7cdc351-b2ef-34c3-b8e6-35e2ae693b74 | -14.0586 | -41.982601 | 2025-08-05 00:28:00 | METOP-C | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9f8953bd-1243-3291-8614-e96f258cddd8 | -10.4695 | -44.383202 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54eaf3a8-79ab-39f9-8286-8eaa3a1f1516 | -3.1893 | -49.453201 | 2025-08-05 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9733cd68-e108-3914-9139-14282f8387a6 | -5.72 | -49.098999 | 2025-08-05 00:28:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e03274-a49e-32a6-81fa-9e6d3589066a | -12.7233 | -47.7896 | 2025-08-05 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff5c0b05-2a6d-352d-bff7-744c02f708d8 | -8.7243 | -46.428398 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b230ccaa-8ad8-308b-9b57-449c8a59cc28 | -9.1905 | -48.8382 | 2025-08-05 00:28:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f34ab01-7ab7-3790-9335-40d5db6981ce | -10.571 | -50.488499 | 2025-08-05 00:28:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eaaf7947-5cb6-33d7-b67d-c7c737721936 | -6.7088 | -44.0844 | 2025-08-05 00:28:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87e38ac3-a534-303b-82a5-d4452885afaf | -10.4582 | -44.378502 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0d4ce52-4c0a-30f0-b67f-4ff216ef97be | -8.8603 | -47.602501 | 2025-08-05 00:28:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6133f5d0-2a2b-3483-9907-36e8efe4a068 | -8.2405 | -45.054501 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7c5d6fc2-17d6-366e-87e4-dd225cacc3e7 | -20.3773 | -42.1064 | 2025-08-05 00:28:00 | METOP-C | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 885b36f5-7e9f-3c8a-bf92-c87a17f5fb97 | -3.48 | -43.243099 | 2025-08-05 00:28:00 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd166123-95ff-3ffb-893d-35d9d6c68ef1 | -5.1413 | -36.3507 | 2025-08-05 00:28:00 | METOP-C | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 452a3853-8492-37ed-9811-bc23f9d8d790 | -7.5766 | -44.900101 | 2025-08-05 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 33f3c99e-04b7-3cd4-9488-6955de01de29 | -6.6801 | -49.777302 | 2025-08-05 00:28:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5175061-90c3-39d2-bc6e-1f12127872fc | -7.9987 | -43.1455 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9d7680e1-bff5-39ac-b3eb-cce4963d399c | -8.0266 | -43.176701 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7795fdd9-86fd-3ea4-85e3-cd22c091c05f | -7.915 | -45.5289 | 2025-08-05 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f4e5b34-5402-3e38-868e-5a22da9c78c0 | -11.7647 | -45.015099 | 2025-08-05 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72c39450-86dd-3408-afdf-cc16197dd46d | -8.0102 | -43.150398 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87d2fce2-7c31-37ba-9865-b2db59dfb045 | -10.4484 | -44.380798 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bb8d14a5-088d-302b-84bd-f91efab18415 | -12.6892 | -48.1147 | 2025-08-05 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffe7fb0e-67b6-341d-a077-5bd193ee5a6d | -8.0068 | -43.136101 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0c57ee98-0ee9-36f9-8931-6ba39cc9144a | -11.7592 | -47.5387 | 2025-08-05 00:28:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73d14d23-9933-30d7-8556-20c0166df1eb | -11.7925 | -45.001301 | 2025-08-05 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 63f3fad5-2f67-38da-92ab-859e94a47511 | -5.8211 | -46.976799 | 2025-08-05 00:28:00 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa1fa55b-7818-35ee-99d2-f5529e286e28 | -9.4118 | -45.497501 | 2025-08-05 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4a093028-4d77-346c-935b-fb375fb3c0d4 | -3.1853 | -49.435398 | 2025-08-05 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abe0e536-89a1-3a7d-bfdb-507cbba9fa15 | -5.4963 | -42.154701 | 2025-08-05 00:28:00 | METOP-C | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 97a62a47-263a-3bbf-964d-5eceb625e166 | -6.5726 | -44.209999 | 2025-08-05 00:28:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1fab92b4-3ce9-3bd1-b2c4-141060dbfaf6 | -6.5628 | -44.2122 | 2025-08-05 00:28:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97020f48-8611-3e33-a63a-7cb581f7c075 | -14.0603 | -41.989799 | 2025-08-05 00:28:00 | METOP-C | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| afb51c25-30a9-306d-a8a3-f778100ff443 | -9.327 | -44.8461 | 2025-08-05 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f8b6ce8b-fe23-3a99-9a3b-2d56de79f85c | -7.9939 | -43.169201 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 85848d67-ef2c-3a1d-945f-3a52feadb1f7 | -8.0004 | -43.152599 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 93fa9672-ad04-3b73-9889-a558cf397ac8 | -10.3508 | -44.908501 | 2025-08-05 00:28:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
