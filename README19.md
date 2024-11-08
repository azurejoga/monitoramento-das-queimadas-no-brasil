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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fa28ee0-70a1-3c77-afd1-39234ecedbc2 | -3.5631 | -47.3847 | 2024-11-08 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 6e32c2fa-b5f4-340d-8d85-245e0375fb84 | -4.5022 | -45.6815 | 2024-11-08 04:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| b42ca16c-963c-395b-a8c6-c9d4117723ef | -4.5209 | -45.6804 | 2024-11-08 04:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 172.1 |
| 07bb372d-4c38-318b-994a-03ec5739aad6 | -2.8016 | -52.9414 | 2024-11-08 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| b3b8029b-8b1f-383a-b841-9d4eedb9d429 | -3.5446 | -47.3855 | 2024-11-08 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 5a07d299-691b-3e57-988a-89936d6d2f95 | -3.3833 | -50.2177 | 2024-11-08 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 0a6252b5-3397-3486-b940-f5ab09f4f354 | -2.8016 | -52.9617 | 2024-11-08 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 5fff618a-3233-3a3c-949a-70f726448daf | -3.5447 | -47.3636 | 2024-11-08 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 4b441186-5c13-3abb-a3b2-4b1c03e4dfdf | -3.8072 | -43.5999 | 2024-11-08 04:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 6821073c-9bb5-3dee-98c9-839a00c023b5 | -3.3832 | -50.2387 | 2024-11-08 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 899011f3-276e-348d-bf51-d8fcd0f4e6a3 | -4.5207 | -45.7029 | 2024-11-08 04:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 2b92daf0-99fb-34d6-be7f-8d92dbbb76d6 | -3.5631 | -47.3847 | 2024-11-08 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 34cbda6a-99bc-326a-b4c3-abc088998b4c | -3.9669 | -48.1716 | 2024-11-08 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 662513ec-75a9-3e09-8d68-f05b923266fa | -2.82 | -52.9613 | 2024-11-08 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| a320c2c6-760d-304e-a319-b6faefad13d1 | -2.82 | -52.9409 | 2024-11-08 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ac39af19-0ad8-3ec1-b507-320ece744837 | -3.967 | -48.15 | 2024-11-08 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a5e255b2-15f0-36e8-aa51-a734cb4d0e6f | -3.5631 | -47.3847 | 2024-11-08 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 61bf1992-fdfb-3669-bbfc-1b18bc31dbd3 | -2.82 | -52.9409 | 2024-11-08 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| df8ce08f-e3d9-31d8-b91e-0d94cf82ef05 | -3.9669 | -48.1716 | 2024-11-08 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 7a444a5d-28f8-3754-9c4f-71d9581d2870 | -2.8016 | -52.9617 | 2024-11-08 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1e614d12-1ee0-358a-8db2-ca5b3605f70e | -4.5209 | -45.6804 | 2024-11-08 04:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 5177403e-0c72-3566-9d67-fcf17c63f1dc | -3.5447 | -47.3636 | 2024-11-08 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| b339a73c-c9c5-3364-aec8-5e1de3251a63 | -2.82 | -52.9613 | 2024-11-08 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 88e28343-c720-3d1f-a99b-a2a664cc528b | -2.8016 | -52.9414 | 2024-11-08 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 62fb8655-1564-3c24-8997-3d57b5e12a44 | -3.967 | -48.15 | 2024-11-08 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 7adec1a7-ffce-36ab-a2dd-724122693f29 | -3.5446 | -47.3855 | 2024-11-08 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 90503575-acd0-3f9c-ab21-7e26de5f7c4c | -4.5209 | -45.6804 | 2024-11-08 04:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 122.7 |
| ae5d5c90-a857-30a9-9378-c35bd972caa5 | -2.8016 | -52.9617 | 2024-11-08 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 1f0d429b-ec9f-385c-b4dc-f135b45c650a | -3.5632 | -47.3629 | 2024-11-08 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 0d6e40f6-1e58-30a1-9525-3c839a54f444 | -2.82 | -52.9409 | 2024-11-08 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 15dd4a66-11ae-336a-9bb2-998cce838810 | -2.82 | -52.9613 | 2024-11-08 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 799f633e-ae0d-35b4-9696-6d4de88d74cd | -4.6835 | -46.4074 | 2024-11-08 04:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7ad3802b-2758-38bc-906c-1f2117f4f0f7 | -3.9669 | -48.1716 | 2024-11-08 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 147cb11f-bc91-389c-b6e6-2cf06683ddd3 | -4.5022 | -45.6815 | 2024-11-08 04:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ac1cac8e-c5ad-37e8-b19d-ac1d6734abb7 | -3.5446 | -47.3855 | 2024-11-08 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 9957b7f6-fb69-354a-97b1-edcafc18fa96 | -3.967 | -48.15 | 2024-11-08 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 30de4117-76ab-338f-809a-153f6c99b915 | -2.8016 | -52.9414 | 2024-11-08 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| c280e850-1ca0-36d4-9477-ad98cbda9d9c | -3.5631 | -47.3847 | 2024-11-08 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| e14a5431-8697-3ded-9e79-542ac7b05840 | 1.53415 | -56.05871 | 2024-11-08 04:50:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0168f020-cc2f-3d97-aa80-a696d8ea0957 | 2.4679 | -50.82883 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3aea2906-9ec8-3978-94c7-79f9c5a6457e | 1.66409 | -51.00067 | 2024-11-08 04:50:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a60697a5-ef17-3135-bf47-1f762fa700fa | 2.52234 | -50.93976 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c112b43-b61b-390c-bed8-0a0f4b3d4099 | 3.37349 | -51.29054 | 2024-11-08 04:50:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b49d4b9f-8706-3af7-b064-26f7186702a2 | 1.77679 | -50.43501 | 2024-11-08 04:50:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f0deeb0-88ea-312c-b5ec-7945384848b2 | 3.36686 | -51.29156 | 2024-11-08 04:50:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57209ad1-6402-36a7-a259-b33b4399b568 | 1.5406 | -56.04686 | 2024-11-08 04:50:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe28cd12-a3f5-3b5c-ba92-cc722135c49f | 1.79001 | -50.43297 | 2024-11-08 04:50:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 535b7f90-bb91-3931-b14b-ea0ae7ec4b7e | 2.46897 | -50.83568 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7318f78e-768d-32d2-8824-79305229ceac | 1.79054 | -50.43641 | 2024-11-08 04:50:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c92a121c-0541-3fb5-b493-5e187406a852 | 2.42585 | -50.77567 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ec070ad-4eaa-36f6-a2c0-17c68eab238b | 3.75677 | -51.61407 | 2024-11-08 04:50:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20be0f17-f81e-3743-911d-69e40cb1aaaf | 1.60083 | -55.92129 | 2024-11-08 04:50:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f86c7221-6da7-30a1-8666-9353adb14edb | 2.47173 | -50.83175 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a95dbeb9-3f9e-36c4-9c74-a3ac6e360449 | 1.54465 | -56.04623 | 2024-11-08 04:50:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c76e185-52ee-32b9-a917-fcc82c43da99 | 2.46567 | -50.83619 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f88c8159-23c0-32de-814e-7d4cfc529dee | 3.37403 | -51.29401 | 2024-11-08 04:50:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f075efa1-bd3b-36af-8804-daa1ebb5b45d | 1.52659 | -56.06348 | 2024-11-08 04:50:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e1354aa-ff96-3202-be93-ba44d97c9dfe | 2.50183 | -50.98154 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2bb8d2ff-cf3e-36c7-922c-80166297d740 | 1.52255 | -56.06412 | 2024-11-08 04:50:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a76b85d-353d-33ad-85d3-72fbc5ac5964 | 3.37018 | -51.29105 | 2024-11-08 04:50:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bad1c0e-0fbe-3260-9537-df6f652741c6 | 3.5207 | -51.23179 | 2024-11-08 04:50:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b83b9c0f-12fd-311e-951a-e07800d0b205 | 2.51851 | -50.93684 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9102e137-5b23-3f5b-8b6a-1f63e810f4a1 | 2.51334 | -50.99031 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 307f969f-70e0-3a25-8d8d-7be3a3b75e56 | 1.66355 | -50.99724 | 2024-11-08 04:50:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abe2ef4d-d2ff-3c6f-bcfb-fa189a991f6d | 0.69513 | -51.43989 | 2024-11-08 04:50:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27230d44-ddcc-300a-ab5c-f9ebf8febf07 | 2.49533 | -50.96146 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4470b3bb-5a3f-3444-aa00-da31733267e1 | 2.47226 | -50.83517 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2c662be3-a36d-3a8b-b42c-f1fcc594ce80 | 0.45856 | -50.27211 | 2024-11-08 04:50:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ce85c18-6de7-3367-bd0b-71ab0b2897c3 | 2.52288 | -50.94319 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1bddeb0-747a-385e-a35f-f25ff1823737 | 1.78617 | -50.43004 | 2024-11-08 04:50:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5902e5a-d724-3d11-b532-3954cbb84923 | 0.50035 | -51.67396 | 2024-11-08 04:50:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52956ef0-ced8-3629-bd1c-7227e6a2512f | 3.7518 | -51.604 | 2024-11-08 04:50:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab99839f-eaa8-3ee7-a95d-d28ad2400731 | 3.75514 | -51.60349 | 2024-11-08 04:50:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff9b5033-6e15-38c8-99e7-fc56c94ea3d6 | 2.68929 | -51.04733 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b88ee7ef-2321-3fef-a194-9d3b223047df | 1.60431 | -55.91716 | 2024-11-08 04:50:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0828f781-ccdd-32e6-a953-fb5290351f34 | 1.1309 | -52.38388 | 2024-11-08 04:50:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd6c4703-465b-3a91-82c2-48d5647ede6a | 1.01002 | -52.21774 | 2024-11-08 04:50:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12a4c34c-6b07-3693-9cd5-8e611c821783 | 2.51521 | -50.93735 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 507d87b2-fa9b-319c-b3a9-bb6088d2587c | 1.53765 | -56.05456 | 2024-11-08 04:50:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7581dabb-2a7c-3d15-8fd0-a16cd01fbff6 | 2.51387 | -50.99374 | 2024-11-08 04:50:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 260ebf4b-8bdd-36d5-a541-eafbeac691ac | 0.69567 | -51.44332 | 2024-11-08 04:50:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b92a421d-bacf-3598-9699-d0644ee0cd12 | 1.7801 | -50.43449 | 2024-11-08 04:50:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0424f756-8b38-3ad7-9499-f5eba852ac8e | 1.52309 | -56.06768 | 2024-11-08 04:50:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c944ab71-3e65-38b0-8636-3bc865924ad9 | 1.53656 | -56.04747 | 2024-11-08 04:50:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4653ee55-f0fb-3497-b609-5b6f400eec3e | 1.59735 | -55.92543 | 2024-11-08 04:50:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27b39553-f811-3803-aa1d-99902d7b3693 | 3.75343 | -51.61458 | 2024-11-08 04:50:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3fce49b-810f-330f-8b31-bfa95b13fd33 | -2.80465 | -52.95093 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a1f8bef8-f8fd-3475-bdf7-825e1d984a7e | -3.05241 | -53.27889 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bf20795-abb5-34ac-97d4-51fe35102a1c | -2.25936 | -53.72336 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 185aa056-9962-342b-8cce-fbc9aecb62eb | -5.64113 | -44.24634 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b693c435-073e-34f2-8843-785452c19d36 | -2.08159 | -52.04628 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2213ae3a-1d55-37c4-8860-352139a14b27 | -1.82911 | -53.69187 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e812accb-006a-3711-bd54-9fd4b2dd4e30 | -5.64074 | -44.2492 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ea739e3-84c4-3737-9b47-d544d131064f | -2.96099 | -53.86111 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99fc1821-b4d3-3aa5-9e39-400c9d742d2d | -2.91852 | -51.04198 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04c24d8d-f905-365a-812a-fb8d15357e41 | -0.03546 | -50.79221 | 2024-11-08 04:53:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f114cae6-b361-37ab-b22f-c9dec74019c1 | -3.15522 | -54.47454 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e05d62be-e64e-393d-884c-a04c88e53c62 | -2.61593 | -51.3038 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 349527df-e614-380c-91f3-a7997a92f8be | -1.23481 | -51.95996 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 018f82c0-cbc5-3297-b72e-7fb1ec419343 | -1.08159 | -53.64518 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README20.md)
