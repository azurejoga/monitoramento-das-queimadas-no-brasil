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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39b566fb-b150-3df1-b474-40dab02a4b88 | -6.7294 | -59.1723 | 2025-08-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 199.2 |
| 9906cc84-59ef-3219-af0a-166169d64995 | -6.7293 | -59.1916 | 2025-08-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| a381a682-6ba2-36da-bf8b-bb332f3e7b55 | -8.0513 | -43.1001 | 2025-08-01 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| cfe68b5e-38b9-3f26-885d-1564c57f0611 | -8.0321 | -43.1257 | 2025-08-01 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 584504f2-1a44-3324-b03a-74e258e9f8ce | -6.7478 | -59.1716 | 2025-08-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 134a16fb-55a7-3ae8-9a7b-62e023ca777c | -6.6376 | -59.0988 | 2025-08-01 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| cdd53690-90d9-30cb-b520-a8508d2ce654 | -6.73952 | -59.18265 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 004814b7-f480-36ee-a165-d60083324e55 | -6.82727 | -59.27169 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 5651fe03-183f-3af6-938e-fab8eab339f3 | -6.82929 | -59.25744 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ea8d79cc-5422-349f-8c48-91bb48d9baef | -8.12396 | -65.43945 | 2025-08-01 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57b23280-0e13-3b36-8f4b-98fa2b263248 | -6.72772 | -59.18125 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a967fb94-0f3c-35fb-b4a6-9568051f586a | -6.62393 | -59.98409 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92403869-5ab7-3e3a-a0a4-b3e7930a8239 | -6.82555 | -59.25573 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 937a0b1b-7701-3f63-aafd-0689a2c43f96 | -7.07723 | -60.04417 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75f73f19-2134-3829-b254-fc5e5c2a63ba | -6.65043 | -59.09404 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ffa19db7-9fb8-39d8-95f8-fc46ac36f654 | -7.07204 | -60.04356 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe74edbe-1db3-33d8-afdb-bcb4f9620188 | -6.73419 | -59.17492 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 421910b2-1bca-3951-958e-d19adf695904 | -6.62526 | -59.97488 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bbee3008-7ff0-3c79-b64b-dc23c9d03be2 | -6.64444 | -59.09698 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 5e817cf2-4fed-382e-96fe-9ab831f3c4b5 | -9.45239 | -57.83774 | 2025-08-01 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 03633600-8c35-39bf-9d99-a6cf1213d6b0 | -6.74 | -59.17911 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9ff6f523-9828-35dd-9cc5-056b044c2fae | -7.32649 | -59.6257 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8acbfe6-ccb4-3386-b2af-11756f71eaf4 | -6.62064 | -59.98115 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 245bf83e-4d5c-3d73-971b-de654b444717 | -6.61963 | -59.97735 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 470bd4c0-e627-3050-bee1-47db4516f115 | -6.81838 | -59.25604 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6999d8ca-d855-3e10-b7aa-4ecd10f96c2d | -6.64328 | -59.10012 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 13ae8d36-e9d7-3ad8-8db9-bcf27a538202 | -7.32114 | -59.62496 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18b6222e-26c6-3a21-859d-a5024fdb15fb | -6.74048 | -59.17555 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c04d7d40-2eda-3193-b763-51d047f72488 | -7.32159 | -59.62163 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c735ba2-958c-3461-9892-04fe1de74bdf | -6.74268 | -59.15444 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fba5e535-460f-39eb-8f73-3a70de4383c3 | -6.72861 | -59.181 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 73085a37-7698-38ef-b801-f96623efbd73 | -6.83321 | -59.2689 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 631f12a5-f591-3328-aca9-e613d85d58a1 | -9.45867 | -57.84661 | 2025-08-01 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 33528892-fb1b-3adf-a8c2-da897a634876 | -6.74881 | -59.15519 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0a7b8cf7-7287-3d5d-92c8-7f7f9bc231d8 | -6.81642 | -59.26996 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 28b2724f-b667-3c2a-9059-b098d937159d | -6.73964 | -59.17575 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| ed89ac7f-be77-370e-aa3b-de6789c134db | -6.62305 | -59.99019 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd61ad48-a6cb-375f-9710-391fdc5d8219 | -6.74096 | -59.17199 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fc7d17d7-1e95-3e11-ae71-42bdf8eb070b | -6.83501 | -59.26795 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31d89cb8-eb71-3bd2-a77e-5184e9276f4e | -6.73646 | -59.16402 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f3108c59-6894-3438-a04f-924caa4519bc | -6.64494 | -59.09329 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d054a490-aa7f-33d5-becd-04253b828300 | -6.74115 | -59.16514 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c51f159a-8af3-3a0f-8868-a0a61749d96c | -6.64993 | -59.09772 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 26929fb7-4559-384a-8441-d48647ecddc2 | -6.73741 | -59.15689 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ecfaa2d-cd6e-379e-a364-a6646125ef70 | -7.32409 | -59.62014 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b14a437a-5e02-38ae-9026-d1989db290f6 | -6.74336 | -59.15419 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a37cad7b-b2e6-3127-b469-9c910a76fd77 | -6.74065 | -59.16866 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| e1e88724-4fda-3c1d-b1ee-faf93e26b3d0 | -6.73502 | -59.17468 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| ff14ef89-92eb-3522-92ef-e82e339609c0 | -6.62458 | -59.99092 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11d86000-2ebc-3cb8-af5e-06e64bf47212 | -6.62007 | -59.97429 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 10cd2000-4a59-3837-81bc-7d782495fedc | -6.82826 | -59.26466 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 01746e2b-09d3-360a-8b3e-81ed122a2c69 | -8.12028 | -65.4389 | 2025-08-01 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7b8a242-c31f-3d79-986c-86a5b5c67856 | -6.7466 | -59.1661 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 534eac34-006f-343d-a0fe-1e73fa8e2143 | -6.62667 | -59.97557 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| be5a51ee-4c76-37ca-9b26-1ec4eaba9d84 | -6.73721 | -59.1536 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1dd65dd3-dfce-3a0f-a171-0f76a01449a2 | -6.73519 | -59.16781 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 1e3abe1c-ae68-3aeb-8bc6-e727be9df28a | -6.6493 | -59.09717 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b106a51e-1471-38c6-b43a-550b91254b01 | -6.81148 | -59.26562 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 092ef70c-2942-330f-b384-99720af79b14 | -6.74217 | -59.15802 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 84773232-5ca1-37ce-8308-85c052561296 | -6.64394 | -59.10068 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| a5f4ff5d-c775-3cf4-8c50-ac2ec716cf12 | -6.73837 | -59.14975 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a5b2217-e18c-3e5c-9011-165d7168477c | -6.74812 | -59.1554 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 992fe371-5e67-3540-b4e6-46366bd1bc23 | -7.32203 | -59.61827 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cb70c25-3414-3132-85c9-35bce42652ba | -6.83052 | -59.26008 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 543a0f68-ee1c-3331-b040-467d6128e7a3 | -6.74191 | -59.16494 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 289368f4-d2a7-313a-b099-41d09710b337 | -6.82507 | -59.25935 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 1747fe22-33d8-30cd-8ff1-8d2b035f155c | -7.32695 | -59.62233 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37524dbd-1e9a-3b1c-ab64-cb2957b862c7 | -7.32456 | -59.6168 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b1c05ae-c5ae-3f4d-ac22-af6eda8875b8 | -6.82184 | -59.27084 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| d68cbe64-b0c3-330f-a837-c543dbe58199 | -9.45311 | -57.84093 | 2025-08-01 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4833b4b3-8a0c-3ab1-8c9a-18f5059d28b0 | -6.73454 | -59.17825 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| b5d46d6e-f756-35f5-9178-22aa5d9f2329 | -6.73097 | -59.16332 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| af1d4aac-2c99-386e-8782-1b252b7a0969 | -6.62437 | -59.98103 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f4226cd6-58d8-32bc-bf50-99ed898ed89e | -6.72872 | -59.17418 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 36904395-b5fe-3a60-a8fa-a66fb7a392ed | -6.73863 | -59.18285 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| cce9d8c6-24ef-36ab-9819-cec83b8deaa5 | -6.83422 | -59.26179 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 37f419df-609c-330b-b68c-7cc11be09afc | -6.7357 | -59.16428 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6959694c-ab02-3e7b-91bd-1b40397b82c0 | -6.81197 | -59.26214 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a3fd28b-3bb4-3427-aee6-5b8c187289a7 | -6.72971 | -59.16711 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d8332abe-b117-3f9d-bc07-43e733d786ac | -6.62481 | -59.97796 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b3b5fa67-04b5-36c2-b5b2-b10050ec8924 | -7.32849 | -59.62758 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea41323b-4012-3f36-85e5-fd164a022bf9 | -6.64486 | -59.08902 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2e406207-9f98-314d-977c-71aa95a65671 | -6.74166 | -59.16159 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3f846754-13e6-36a6-bda4-b103b42caa29 | -6.83371 | -59.26537 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 2b4d44af-4167-3b29-ab82-16d84d885432 | -6.82233 | -59.26735 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| fbf3dd36-fe49-302c-97eb-676f0095fe00 | -9.45928 | -57.84187 | 2025-08-01 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 931d50ab-cddf-34f4-9f6b-c324011a699f | -6.73003 | -59.17036 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| c05b5c67-533d-301f-bc9a-8b83ed58b333 | -6.64434 | -59.09273 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5fbe0d1d-00da-32c1-98bf-780db754bcd0 | -6.82877 | -59.26109 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 3fa4e184-d645-34f7-8fd4-cc670c331ca0 | -6.7461 | -59.16961 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e7141b33-d26e-301b-b89f-c5e299b1578a | -7.32362 | -59.62349 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed6ed49d-3fe1-33ad-94b8-58b0160ec5a1 | -6.82383 | -59.25677 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dbfd7906-f1f8-3204-b7b1-202b1e78b36e | -7.32897 | -59.6242 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6163154d-918d-3d85-9868-dec42bd6de5f | -6.82435 | -59.25311 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 277593a0-0bb2-3afc-8451-cb93441d6369 | -6.73318 | -59.18203 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4b7517ff-51cb-34f2-a1e6-f6a4b8c670b0 | -9.45856 | -57.8387 | 2025-08-01 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 68a5fe99-2188-3912-9419-4519aea10360 | -6.7355 | -59.17112 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 166f0fa1-fdac-3343-816c-1bb3503a2585 | -6.6219 | -59.97192 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a6ea0688-bb2f-3291-bd99-30d2758771d4 | -7.07679 | -60.04738 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7759fc31-d239-36e6-ac54-b6a3c2320214 | -6.7471 | -59.16259 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README26.md)
