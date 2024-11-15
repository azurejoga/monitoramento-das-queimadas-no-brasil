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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8efcb2d-4a5b-38c7-8b3f-6acbdf357581 | 0.44286 | -50.92404 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4e91bcb2-d754-3bd5-90c4-c3df1621c77f | 0.90825 | -50.14297 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fdf42fa-cb08-3297-8156-8f417f61eb5f | 1.06839 | -51.1211 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c79e546b-67bb-3b0f-9e74-ba2551ca8f75 | 0.12528 | -49.84663 | 2024-11-15 05:05:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7bc496db-435e-3b97-83d4-fa91fb8d369c | 0.4474 | -50.92688 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 33c51b7c-2842-324d-9e51-2d19a5b2abdf | 1.07457 | -51.13787 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1bf861d-df17-3369-987d-7d4025a70b7a | 0.84989 | -50.20665 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf638b5d-1170-3b57-865c-c0d1aba114fb | 1.59087 | -55.8855 | 2024-11-15 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a65dac08-403a-3fb3-bf56-d708d7742d99 | 1.0716 | -51.14089 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4babd73-d0d9-33e9-8f45-0a0f1c929b93 | 3.44979 | -51.50335 | 2024-11-15 05:05:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baf323be-f995-3a2a-a690-ff2f0e1372ab | 0.69787 | -51.44171 | 2024-11-15 05:05:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce6946cb-13f9-31b9-9377-9cee6d90bcac | 1.07861 | -51.13474 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1c81c31-bc00-3566-957c-c36df6e96b25 | 1.07422 | -59.23606 | 2024-11-15 05:05:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cec3ef0c-3ef8-33ff-b1b6-446a10c7288d | 1.07066 | -51.13849 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cf5b48e-43d5-3fdd-9b88-3b1edc664639 | 0.38309 | -50.88351 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b22bfecf-8764-3a94-8232-b8d7309105e7 | 1.30344 | -60.40625 | 2024-11-15 05:05:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 328c3d5b-f3f9-3607-a98e-47cebb8dda98 | 0.12162 | -49.85139 | 2024-11-15 05:05:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcfac252-d433-337b-b2d4-cc6bc3c7b376 | -4.24022 | -55.88046 | 2024-11-15 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f99e42bb-ae0d-3424-8501-a662198bbee0 | -1.09265 | -53.17779 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13c14142-8246-361d-9d55-468b270136ed | -3.65926 | -54.6619 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b762d691-b6a4-3cb8-90af-ea6f8e358c75 | -3.23433 | -54.16317 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 517f6112-4b20-30f5-918c-d8adf0270d4c | -2.38816 | -57.2893 | 2024-11-15 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66db098d-8fd4-30ae-a015-3b7aed67706e | -3.55034 | -54.57238 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbb4a944-8707-3598-808d-a608c833c700 | -2.23337 | -54.47906 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88191151-ef55-329d-b8f4-32557ad9390a | -1.55901 | -51.85883 | 2024-11-15 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30e2c79b-a98a-394f-9bef-7f3c308d0521 | 1.05938 | -60.59756 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c2208ae-ae50-3471-911f-1ee8d2847d1f | -1.98352 | -53.13791 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83a0733f-6294-3da2-a7be-13f9291e97cf | -3.55321 | -54.57666 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d979383-e086-3d49-9c9c-0aa162848899 | -3.34388 | -53.28928 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f5c117c-3731-379a-b535-57f94dfb68d8 | -2.84966 | -53.98029 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ae4f49fa-071b-3349-97bc-901232cb656a | -3.55301 | -54.66868 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f79be140-86f8-3618-a842-a9a5845a3e48 | -4.00085 | -56.10764 | 2024-11-15 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e342daa8-cb26-3588-a567-cd2b756e7e90 | 1.06098 | -60.60801 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e1d77ca-5a59-3bbf-9bda-0bc6a7aedd7d | -0.19295 | -51.53136 | 2024-11-15 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d91675fa-6550-37b5-b5af-a7e4e4399336 | -2.89778 | -53.05214 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f7b415f-5c1e-349d-a5b9-4b60a9f14031 | -0.1615 | -51.58107 | 2024-11-15 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d041986-c548-3f27-ad68-0150bfa1d085 | -2.83406 | -56.7896 | 2024-11-15 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0265239-e177-3400-80dd-0cfbf42c52ed | 1.05485 | -60.59473 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8770d9f8-1ca9-329e-87db-dd933ff9b3e6 | -3.45184 | -53.46648 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16e24719-79d9-3a63-b5c6-beef7cbaec6b | -3.55263 | -54.58042 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05b54ac7-ddbd-3817-9d4f-4b017d3dbbc1 | -3.27428 | -53.01488 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| acb4f274-4ce7-375e-953b-69ee4d118a21 | -3.54632 | -54.5756 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2634aa5b-9217-3d24-ad59-a5cb8707fb9d | -1.07268 | -54.10066 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3d3febe-f321-37fd-87a2-deda6e282ad8 | -3.08329 | -53.2575 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca252a96-5097-3449-b97f-0551c52f3935 | -4.29884 | -55.5932 | 2024-11-15 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0fb9716-1370-3363-b801-6c0329c74357 | -1.61242 | -52.51584 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c47b353-a8d3-3b9f-b71b-db8dd4a238e4 | -3.42961 | -53.9717 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5eb20ed-96c2-3987-92b0-83a7c81b3799 | -1.21256 | -53.56608 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3833bd7-67fc-34c2-9b8c-29d2b32fc519 | -3.53465 | -54.08826 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e46c565-edea-31ca-9856-e81f1f556aa2 | -2.38658 | -54.64201 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 02348587-e875-3fe0-8c58-8597b5a7f07f | -3.02421 | -54.4868 | 2024-11-15 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55c8d020-fb36-363c-be1e-ca80f64be8f9 | -1.41807 | -53.47859 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12c2f4ad-04b4-3500-bca4-90335fe828a7 | -4.00139 | -56.10418 | 2024-11-15 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 561c2280-d2ef-33c2-a7ec-ef698f26cffd | -1.63794 | -53.27074 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 169a241c-ab4b-3289-8cb6-726bedc18581 | -2.74608 | -54.0406 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 525d5c31-ef2a-340b-8834-7536f7e4cca1 | -3.70619 | -54.54183 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afd99240-597a-3259-9264-fb443a94e897 | -3.646 | -52.2743 | 2024-11-15 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 745c3a5d-8610-38b0-88a1-7857337a41de | -1.57445 | -53.8017 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b64730a6-327d-3e55-bb8f-6d02ae554ce1 | -4.05735 | -55.79088 | 2024-11-15 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| feb549ce-9657-34d6-9d37-58d0a4476382 | -1.35635 | -53.07974 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00e03ea4-d2c5-3008-a850-cf0b83a87dba | -1.60635 | -52.50579 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 447bba87-80db-3986-a170-99958c564483 | -2.46233 | -53.93199 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92152d31-6933-33d7-b37c-5074e12181e1 | -3.62854 | -52.31145 | 2024-11-15 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1b36184-ce4d-31f2-b6ea-bea5d2c59402 | -0.86367 | -52.58925 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2029c68-3d89-3488-9e0b-cac756b02f80 | -0.97481 | -53.71993 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d87b3ca-f260-3deb-9ed1-a4dd1ec446e9 | -3.00326 | -54.0827 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 008ce10e-33d7-3032-bbe1-1cc09e1eb32c | -3.24801 | -53.67074 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08a70ab9-29a7-3a31-afe2-3efcace53439 | -1.98237 | -53.13919 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7db2f94-10a7-3381-944d-cba356ba299a | -1.84485 | -53.68984 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba64232b-9f75-3e3c-926d-2b1aeb1b6f12 | -3.31325 | -52.86201 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da359dc0-5b34-3639-b176-02340de55486 | -2.33943 | -47.22042 | 2024-11-15 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 246116b4-e52f-37c6-927f-2b52e61e7183 | -2.34208 | -47.22015 | 2024-11-15 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36005bc9-1e77-3182-81af-2285ba0265b5 | -3.43021 | -53.96778 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 820efdf4-5e55-3aaa-9ce4-7d6489493a76 | -3.63171 | -52.30981 | 2024-11-15 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e641f6c0-9ebe-3eee-a194-2f996367bf67 | -1.47539 | -53.01171 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc94a272-ab85-35b1-8638-e67f4fdc7436 | 1.14161 | -60.59906 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3aa5c6be-2a42-3499-be2a-957b97ebb2c6 | -2.6306 | -54.38249 | 2024-11-15 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad874f5b-0f28-30b8-b63b-899d8a7bd5a9 | -2.97624 | -53.86175 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 329a87e5-96ee-341d-bdca-c0f96130e718 | -2.72176 | -53.1987 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bedee8c-c8aa-31b9-890c-9415445c79d7 | -0.15954 | -51.5831 | 2024-11-15 05:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a54dde2-b023-384b-9621-eab747421eae | -1.9061 | -45.45087 | 2024-11-15 05:08:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96158319-6bfd-367d-bb6c-90d36edf650b | -1.07347 | -54.09711 | 2024-11-15 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac184996-4789-3be1-8542-c5f0d0412e3a | -3.23552 | -54.15536 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9972a1fd-865d-33e7-9031-fb8b1582098f | -4.23912 | -55.88746 | 2024-11-15 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0515187-b348-3e3b-a609-6457eb6e5629 | -1.68099 | -52.55092 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9447cb6-876a-3f41-b70c-bab00a915472 | -3.2773 | -53.01986 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10fa3b5e-7894-3b3e-a63a-b9858e93a784 | -3.64527 | -52.27916 | 2024-11-15 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b95b35d-f3e9-37e7-8968-532d0346648a | -1.9517 | -53.33317 | 2024-11-15 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb043d91-76d3-37b1-b38d-cdb325276dc1 | -2.65193 | -57.10299 | 2024-11-15 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b73bcf8-be8a-313a-b213-7038a7ebad7f | -2.5863 | -47.47961 | 2024-11-15 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27824011-3726-3acb-ba0b-3abc1935c073 | -3.34024 | -53.28867 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad21b49b-3a2d-3cce-a326-2ee046ed928b | -3.55549 | -54.5847 | 2024-11-15 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e7d6a2c-5edd-3ae6-b0f0-bbbd68116377 | -3.22984 | -53.62195 | 2024-11-15 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7ae2b36-960e-3fbe-b493-49fe707743aa | -3.45121 | -53.47065 | 2024-11-15 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35e158de-f247-3a4d-b212-b47cbc44c3f1 | -1.28615 | -52.47124 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 390dbdb9-c0e0-3920-a348-4763961fd9d7 | 1.05644 | -60.60516 | 2024-11-15 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7deb915-021f-300b-a31c-835bed2c14e0 | -1.9799 | -53.13736 | 2024-11-15 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1939e5f0-c820-374c-9602-5bcad1257a20 | -1.38887 | -52.08393 | 2024-11-15 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ee225eb-369e-3d73-aa5a-0a552e23c8e1 | -2.83736 | -56.79012 | 2024-11-15 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ec950e2-04c7-3714-ad1f-5ca7a28671da | -8.27363 | -45.97075 | 2024-11-15 05:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README27.md)
