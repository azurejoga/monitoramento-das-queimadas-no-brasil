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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e93558b-420a-39bc-8162-f12d01dc4dc6 | -2.90464 | -54.13741 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b448640c-1a65-33d7-ab00-a4f7d6655fde | -6.21458 | -52.80005 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fae7dec9-ecdf-391b-aef5-0ef91d01f190 | -3.12557 | -53.72117 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ac1efd5-4510-31dc-a3d7-f2546ed75c1e | -2.47425 | -48.03783 | 2026-10-05 04:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3b03ce0-3070-3b35-8076-47f016583649 | -4.44106 | -54.9635 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b5778c2-82d1-3efd-8c4d-1405c46eb0f3 | -2.97562 | -54.091 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29e55d28-9d4b-3537-8ce5-8d35160ead08 | -8.67601 | -54.55962 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dbcb4d86-68ad-3b1a-9813-51539aef0697 | -3.27327 | -50.39955 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f1ee78a7-2501-37d1-8369-d69cf3ec7e34 | -3.12276 | -53.717 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39139127-3efb-36f5-8b21-71eb982eb49b | -6.06061 | -53.46849 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6ba6c5d-4352-3b32-96c0-10251a22e2b0 | -3.13062 | -53.73317 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7bae656-6058-3574-a71b-7605c940f280 | -2.88274 | -54.14165 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e41e6847-614f-3442-9650-f60055ae151e | -8.2764 | -47.91933 | 2026-10-05 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 052ed1b6-d858-3450-b7fd-ec822f158849 | -3.04928 | -54.22161 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36de3a23-c2f3-3e6a-b7f2-749364241198 | -2.88335 | -54.13788 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d86f6b19-cad1-34cb-85d5-dfd2f57a3b10 | -3.21752 | -53.87055 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e3d9654-6694-3767-b1b8-db5264bfd70d | -3.91281 | -49.7033 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5490d8d6-43c6-3514-bf6b-595fe8c623a6 | -3.2795 | -53.83497 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ca9a7ef-ad5d-350b-81c7-1a40b4a620a7 | -5.99769 | -53.52263 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ef0caa8-e468-3f0a-b736-d674a70c8212 | -6.2102 | -52.82769 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 52c9460e-9071-36b9-a9de-af2ab16bcf8d | -2.57676 | -56.15495 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 785ccd13-7c20-3631-ad8e-c80666d261cc | -9.8121 | -44.80185 | 2026-10-05 04:57:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a08f169f-2ddb-3897-9c78-448e3fa23ebb | -2.96929 | -48.92435 | 2026-10-05 04:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7d34c39-7457-31a5-9412-b8ef169ced0f | -1.61841 | -55.14042 | 2026-10-05 04:57:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe80f255-3667-320e-9dd3-f2d1a3c283cf | -3.1278 | -53.72899 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae158ddb-3fb2-300e-bd0f-fa344028130c | -7.43926 | -63.56381 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86dd084b-82fd-3193-bcb4-4be21601f10a | -2.79515 | -54.09772 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7caf0320-a868-3744-b859-d93ace1e0b8b | -3.22434 | -53.87161 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a8cef466-e0e0-37a6-9a56-4994cf598cc8 | -1.2054 | -55.86175 | 2026-10-05 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9df7298a-c3af-3eaa-8f2a-e085a8bfbfe8 | -3.11811 | -53.74612 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ac59963-0af5-3d55-8a34-fefefbb79673 | -6.00325 | -53.50914 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6eaa597c-8539-3089-bb22-cbf10e475f5f | -2.91818 | -54.09722 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79b1be7b-0ffe-3dad-8499-385758ecd2eb | -3.87782 | -55.80657 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 689d1152-23c8-3ffd-998e-0dc22c268c94 | -3.1119 | -53.7414 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66af6dc7-42f4-319e-9b3c-2f62a35cac38 | -2.69966 | -49.03661 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8a151d6-e866-36dd-8047-20a055ed6203 | -8.54247 | -54.58588 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 221d769a-709d-3d48-9fd6-2df340b1307b | -3.32716 | -53.38845 | 2026-10-05 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd74ca1e-6027-3b13-827c-7f17f0ff031f | -4.57329 | -54.95188 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d87c8020-8a18-34be-857a-1fbe5f6fe50d | -7.21671 | -55.19008 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8514f7c9-04ce-34e6-a37b-44fea9b6f0a6 | -3.04583 | -54.22106 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45b57ba4-c559-3b2c-9e6a-95274a6dd082 | -7.46721 | -55.00962 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d1f528d-4927-36a8-8c5c-f3031ba6dfe1 | -2.82719 | -54.11824 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fb64d59-9b51-374f-9d22-0cde4f4599af | -6.08886 | -53.4837 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bb296ad-8842-3e2d-be15-7478e06355e6 | -2.77264 | -57.65434 | 2026-10-05 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0bd2031-2aea-30f2-b4c0-f42806acac15 | -2.9926 | -51.04622 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f044d95c-07c1-30d1-aa74-dd89a485e0f4 | -2.58665 | -51.85118 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfe4ffdf-248d-39db-a75c-7f2811dbaa2e | -3.12334 | -53.71336 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3af821a0-d7b1-380d-9463-0982bb3184e9 | -3.85038 | -50.31437 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 835b965d-dd75-3395-b416-0fd3152000c6 | -4.05769 | -54.31564 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e50f3b49-2089-3f4d-8537-c0e6c63677cf | -4.22952 | -49.97061 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6fcd98a4-7222-3333-8003-989ee2149796 | -3.28802 | -50.30458 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70fbe20a-f71f-33c9-be97-b5bdcdc6bf0f | -2.89791 | -56.6716 | 2026-10-05 04:57:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81100c42-1888-3896-85c2-759de5111b58 | -3.02021 | -54.18218 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc2d44ff-d870-3e5a-8127-d3115ee77523 | -6.09218 | -53.48423 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bbfd0d6-ed4d-37e3-859b-014dbd27e2d2 | -5.95898 | -55.34631 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de10ca76-adf5-3651-96ee-26205832bd71 | -2.61579 | -51.21612 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d23ee252-0b59-34a4-b44c-2125409ddd35 | -6.3326 | -55.32071 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 171b963e-c8fe-3991-a7b5-e3bc3165a48d | -3.10686 | -53.7294 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a67b939-295f-37f5-83b6-1c9ca0718b97 | -8.67438 | -54.54832 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8dc6dacb-a366-3f86-b521-251bb25e51d2 | -3.88081 | -55.81155 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 63736afa-b2ac-3aa7-8aa9-9405a7c9297a | -2.92472 | -54.14446 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 200ffaad-9724-3b0e-8d95-2956161b8633 | -3.00315 | -54.2221 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed457bc2-1b47-3d58-820d-e8d877de7c7a | -3.86974 | -55.80972 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3afdb2d-ec70-351c-8800-ed7908dca284 | -3.11762 | -53.72737 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a27ffd4a-9aac-3852-a34d-67fad01d2c76 | -4.60029 | -49.62946 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c2b21e0-6ea4-3edb-809c-6f03b33f8649 | -2.85411 | -51.29934 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9ac5dbbb-75af-337d-88e6-ad929fc852d0 | -3.28572 | -53.83968 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cbedca9-3046-396c-a1d1-1053114edf4d | -3.57407 | -55.41621 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24f6e7ef-613a-3b95-91e8-ab32408c29bf | -3.31856 | -53.85238 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23f6df56-e1d7-3283-9063-c0ecfcf413bc | -6.20135 | -52.79795 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 000c6e85-0162-3c8d-be02-1b26dedafced | -3.59228 | -54.31348 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fc81d38a-9613-30a9-88dd-37700f59f0d0 | -2.79272 | -54.11276 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04445772-aec8-34a3-96a3-d986af832f08 | -4.10875 | -49.08075 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8a3da8e-dfee-339e-84bd-93b612a5fefa | -6.22228 | -52.79419 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7087999f-1af4-32ea-83e5-e91b6fc12cdf | -3.70893 | -50.65891 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03bd343a-5f9b-3fa2-9c1d-fce17d449e72 | -3.57339 | -55.42039 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 481181ac-3f10-3851-a876-d91f5ffad728 | -3.53796 | -55.52277 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0442d2b1-ca34-3ddc-8def-128f97148113 | -3.37322 | -54.10319 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2cf2136-17fd-3095-86fd-2a481ad8d2b3 | -6.2194 | -52.68398 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c8c3aa4-22af-3d31-983a-13595aead8de | -3.06983 | -54.15927 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 98119e2f-3c6b-309c-a9f6-7713d41e871e | -7.44505 | -63.56488 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 306c1ed1-7848-3553-ba2d-686def4aabc6 | -3.30836 | -53.85076 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdfc883e-0f43-3b90-9fc0-ab82703c3ca0 | -6.2052 | -52.79502 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24f524b4-00bf-3784-99e0-3ed0e5bc2b23 | -6.89519 | -43.67572 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae3d015b-3b04-3be5-8fd9-3e214167b9e1 | -2.94315 | -54.1397 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c384c49e-303e-3423-819e-6b0a3ec4887d | -2.9168 | -54.12777 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 24ee710d-2261-35b7-8ada-f7c59f80b12e | -6.41398 | -54.95113 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57d86170-fbbd-3418-a100-2bebfcd19ae8 | -2.96172 | -54.11189 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f75b06c2-1d10-33f7-9de7-ef4ff0e6ed3f | -7.22017 | -55.19061 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00df2114-4216-369c-8b47-8b2f868e2b22 | -3.52072 | -54.62762 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 384f647a-fc64-3b4b-9732-26d8a65ca3d7 | -3.10435 | -59.74134 | 2026-10-05 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45c2ba8a-5f13-328d-971a-665d97907520 | -7.43771 | -63.57204 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fb82158-7caa-321c-821a-22329328194d | -3.46855 | -54.59549 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| c0a13177-f6c9-3b91-bd08-891f6b2c5c53 | -2.53565 | -56.43056 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10e1fb30-7fcd-304d-b871-e6f167a327a3 | -3.07659 | -54.18342 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 578cba28-7260-30d2-ad5b-8458ba634079 | -3.9257 | -49.71274 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ee027818-5b56-3420-b3bf-767dd56ce183 | -2.90302 | -54.12557 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e636b34-dc35-3e95-923d-09ad69eac561 | -4.28359 | -50.27651 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab3a178a-6c24-3e32-ab79-053be84ceb5d | -6.21239 | -52.81387 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b15e2c18-5369-3de5-9f1a-8d152b2f3021 | -3.79186 | -50.80033 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README37.md)
