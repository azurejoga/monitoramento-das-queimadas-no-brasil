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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b258da26-843b-33af-be6f-63d20cf55fe7 | -3.99551 | -49.92717 | 2024-11-21 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 821f6826-f883-3205-a0bb-1165b00f80af | -6.12214 | -42.52621 | 2024-11-21 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 505004f2-f588-3c42-a972-c822177e1f13 | -2.94556 | -53.90001 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d7c38fc-54e9-32ef-bf1b-a412e4c42397 | -6.29713 | -45.33702 | 2024-11-21 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c38f000-afab-36a4-8f5b-14a6e3f59e90 | -4.12428 | -53.81697 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85373ad5-5174-36e3-9819-7192569b5cc7 | -2.9321 | -54.09282 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74429890-1d13-3238-b913-d29e069a2ee8 | -3.22756 | -53.61951 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f817a962-cafc-32aa-bcd2-43db815b006c | -4.05956 | -49.28374 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bad4a7ea-abf9-3a26-a291-240386cee1b9 | -2.54471 | -53.98536 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4d9fc42-2813-317d-a944-a2b303ba63c3 | -5.46152 | -46.47958 | 2024-11-21 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a905e80-8855-37dd-ad69-bb03b1091bd9 | -2.58145 | -54.22661 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3849e52b-dd11-3aea-ac47-46fda58fcee3 | -2.68708 | -51.80632 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae99c050-1a59-35a8-aee4-d01a940bf52e | -3.64585 | -51.45901 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b030309-db36-3adc-98c1-6fb9ffe58725 | -2.42139 | -53.66956 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff84326c-2a46-393e-9861-d305456187f5 | -3.09452 | -53.21185 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23fa6c8c-810c-31e7-bf36-061ccc003d56 | -3.32869 | -50.25314 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4030f53a-8fd2-3fcd-8c9c-49d000a2eb02 | -3.39637 | -50.10691 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 931f5155-2f1d-308a-9438-c6cc8875e071 | -3.10059 | -53.21631 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 71a15e40-f0e1-3009-80d4-5e4b1a6c0467 | -2.75957 | -52.11636 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7e3f416f-9be8-3466-a44e-c48df9ef87d7 | -3.50325 | -48.22256 | 2024-11-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d850841-4deb-39d3-bf92-068aa588c3fe | -2.78719 | -52.55149 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 695613ed-6587-3a92-8d4f-80bf892c2aa6 | -2.46339 | -53.94138 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 880115c9-0700-34d9-b1b9-bd822c4fce88 | -2.78152 | -51.7212 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9bbb466-810c-36ea-ab51-3ff7b615ad9d | -4.15259 | -42.02345 | 2024-11-21 04:55:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 0e442806-9b86-387a-8626-70a110ac9d70 | -2.76862 | -54.07397 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d27f5cd-49a4-3c26-a808-040195204d28 | -5.19457 | -47.74283 | 2024-11-21 04:55:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9ae39b5-7178-3dfd-84d2-47ef63a42331 | -3.35553 | -51.61341 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc5f8785-9cf2-3877-9b33-0e5b8dcaf21a | -4.06759 | -50.90192 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f50b9f4b-3322-3b97-9c2c-b2f9000a5af5 | -3.53688 | -50.5232 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af02a77b-67f5-3c53-adf5-5e41c5247aca | -3.20141 | -54.32399 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 909e50b1-3ed3-36ee-8b78-64839eec88c3 | -3.56306 | -51.49617 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da129ea4-b371-3859-abf7-2959012cc244 | -2.61845 | -51.80313 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f36daee-9191-3705-8814-3bf9803a2c18 | -3.29075 | -53.84464 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 308d5556-f748-3ecf-819b-a48a5cd870f2 | -6.12144 | -42.51334 | 2024-11-21 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 583b0538-8d4d-321b-8ca7-93d00feca3ce | -3.72706 | -52.3164 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92681531-3745-383a-9d96-1924ab0ca469 | -3.52198 | -53.80013 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fab5c887-b98f-3a36-b178-da3b8081f906 | -4.97745 | -48.4558 | 2024-11-21 04:55:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cf40191-fa03-3386-b302-ce8c0b071df4 | -3.03571 | -49.46682 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b0e1ee5c-9957-3616-a304-21d53c10ab2c | -2.54694 | -53.99279 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b68b48-10d6-3eee-8774-6a7372f7fc3a | -3.05308 | -54.40081 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5a9b75e-4b3e-3fac-b013-912719ee9cb4 | -2.74824 | -54.11707 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da9d1fc2-8eb4-3f5a-9ae6-64ef887c6833 | -3.01232 | -51.43308 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ae804bc3-4d64-382b-8fc5-51860e3e6011 | -3.3483 | -53.54372 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61cdf835-fd6c-3349-9d71-5b65155e579b | -2.98349 | -52.14009 | 2024-11-21 04:55:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba4601bd-e3c7-39dd-8dc0-2e9b8c9ad2fb | -3.28305 | -53.85049 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 733b32bb-82cb-3daa-a774-5078f3533c4c | -2.76682 | -52.11386 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 414650a1-f538-39ba-b33c-e5d2c273c4e3 | -3.29256 | -53.68281 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10d81a18-6086-3621-93b8-387b523563e9 | -3.39304 | -54.27214 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6741c4cf-8a19-3291-8e0c-28e4872090ea | -3.63847 | -52.14215 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6a9a432-d7f1-3c54-981f-6d0a1bd498b2 | -3.34154 | -53.3069 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba6674b9-c298-3229-8b94-87135bedfcb1 | -3.10861 | -53.70646 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e56ec653-459e-32a0-b769-f3b6fc3e75bc | -3.38064 | -54.7598 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebd2b59b-bbc5-3a57-9a47-22afbfe92893 | -3.01612 | -54.03472 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce2c51b7-b243-3dcf-a60d-c60a6e52fc1b | -3.42621 | -53.2849 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bc0d752-afb6-3e46-977e-f9387aa65de2 | 2.5247 | -50.96429 | 2024-11-21 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3775fd8-5c51-3f1a-987b-681f20b3b065 | -2.56961 | -54.00023 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f092601-b3b5-3802-9222-b8c821e50248 | -3.28926 | -53.6823 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1018ccd2-2f78-3921-a668-f78ef73f330c | -3.30414 | -50.3641 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 546aa8c3-d149-344f-99aa-96d347efd11e | -4.13417 | -47.73363 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 343eb57f-be20-327c-b846-0382aea802d4 | -2.84088 | -54.00396 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffaa0b6e-ec54-3136-9e81-45e40f1d5820 | -3.28582 | -53.85445 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 45ccc3b3-0990-3bc3-9c96-5c9ce1e24f7d | -3.10868 | -50.20068 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 414e3042-919a-3aee-b8f0-5d4f7137c2b5 | -4.76963 | -44.49352 | 2024-11-21 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79fe95c8-3347-39bd-b26d-0b9443e317fd | -3.51254 | -50.22705 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be9fc9b6-c5ad-3bfa-89dd-595a0eedce7f | -2.76916 | -54.07051 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2c08fe3-0b2a-3bd5-a818-e159816f28ef | -3.47188 | -54.54542 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e25bbdf-71e9-390a-9bc4-d7f79c793644 | -3.0992 | -51.28211 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b85e8bc6-f66e-393b-9fc4-080937a9839a | -4.62949 | -49.54901 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 625e8085-be97-37cb-9cb3-ba5e4716f9e0 | -3.80874 | -51.26662 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02e6b8db-9b40-315d-97d7-37374d94f01b | -4.63021 | -49.54431 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 276a9fde-ace3-328c-942b-b2f60e02e3e9 | -3.21658 | -53.83975 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 836c4b9a-05a1-3cea-984b-2711aa6d0fe0 | -2.91115 | -53.05965 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2782aca-11e7-3613-af03-15308e68e17c | -2.76802 | -54.05611 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7314877f-a86b-3a1d-a115-c4135260e669 | -3.23295 | -53.39165 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef48d738-9397-3e68-93e9-48e6fb49eb0e | -2.90784 | -53.05913 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8aaf266-3c7a-3793-b67c-3822d768e58c | -3.55388 | -51.51003 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae91d6ac-84df-301f-a2c7-cbd3830e4efe | -3.47132 | -54.54894 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8801d5ef-d88e-3476-873c-f15ae6b384b6 | -3.11906 | -53.70457 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ed0dc95-56c2-3b68-b890-85eca1bb628d | -4.39035 | -47.75799 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9cbacde9-2615-3ef0-a3c8-85f2c6fe95ab | -2.78347 | -54.04468 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99247ca8-0d63-3881-9716-9552034d65b3 | -3.88225 | -52.23755 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36fcd0e2-6a9c-32e7-a0ab-21521cb9a8a4 | -3.06447 | -51.36876 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 082371f9-5aea-3e11-92a0-19bbf9e0723f | -2.18988 | -56.07898 | 2024-11-21 04:55:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 525bb7eb-f973-3e83-b661-93f95c3fbc00 | -3.67539 | -45.24199 | 2024-11-21 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0a771ac-675e-3d7a-aa18-2084f4e42648 | -2.80167 | -54.01556 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a297d8ac-689b-3257-b621-49ea8dc58e0d | -2.7547 | -54.03275 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1722e8a5-a595-3437-8245-a73be9a83e22 | -3.88169 | -52.24113 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cf9511f-0942-3936-9ce1-8c5a3d0ce071 | -3.14789 | -54.66138 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d477a7a9-14e5-39d9-86e2-5a1266fdee14 | -3.41906 | -53.28732 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce25bdb3-e7c1-3525-b4c6-d16b1c7d9e91 | -3.28194 | -54.1158 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8c80aee-b0ff-3efa-966f-ebed9e1a6c56 | -3.46329 | -50.83199 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f70f0e9e-5b13-3186-9ef8-7a25a6bec546 | -3.64224 | -52.36104 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c1e5ef1-31f9-3eeb-b069-529a3677422d | -6.12015 | -42.52293 | 2024-11-21 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| bb418f25-c0fe-3731-a0d4-c08dffb9c467 | -3.41679 | -50.71124 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc27fe4e-ca88-366b-99ce-97d45815f514 | -3.26331 | -50.62821 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1894986e-bb3c-3d6b-a47b-6749fdaae98d | -3.38766 | -53.27181 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7010de76-07c5-38ef-9f6e-66227711758d | -2.57576 | -54.09023 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c7386fd-901a-33e4-ad61-f8a2adc1350d | -2.95009 | -52.57359 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3ca2b47-7d35-396b-b5c5-ba52ce948618 | -3.18532 | -54.31793 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c59d970e-976e-39cd-ae2e-b63ff7f207e2 | -3.23628 | -51.29837 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README75.md)
