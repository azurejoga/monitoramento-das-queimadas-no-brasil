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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcbb2b10-9c46-3e2e-aa99-1eaee1375b53 | -3.10922 | -53.81001 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f76bb960-0e9d-35c3-bbe3-fdfdb254ea69 | -3.22199 | -54.0927 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdbd540b-3044-3db1-9583-1bf763cca491 | -1.65142 | -52.73992 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15931073-a0dc-38eb-833a-8ac21e109241 | -3.05379 | -54.03875 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9ae00da-dbe7-349a-bc98-f3d6cea77862 | -1.72498 | -52.47474 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37f321aa-4707-386f-be54-8f6508bc31b3 | -3.23014 | -53.39211 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 496644f7-ae75-3129-84b5-2f6ed5dcdb5a | -2.97791 | -53.89182 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72fed96a-7a46-3598-bca1-7b7ce2f64f25 | -3.10433 | -53.8133 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d92fbcc4-7cd7-370f-8704-cebd90452837 | -4.19841 | -50.68892 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 621a67ba-c701-31d4-bb76-b23ae053ce8c | -12.30285 | -56.69715 | 2024-11-29 05:22:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ceeb7a51-9c6e-3ff5-be0c-f05eabc54a28 | -2.88267 | -54.11668 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c7cf652-7157-367f-bae9-ad0c25169952 | -2.83204 | -49.84482 | 2024-11-29 05:22:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4055334e-2c3f-32a0-bcb2-cff402c4fac8 | -1.65595 | -52.74061 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e77a353a-6692-3911-9b0a-5ec84f2f0a25 | -4.78467 | -46.12012 | 2024-11-29 05:22:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 44625e2a-8543-3166-81b7-1463155c840f | -1.55892 | -55.26594 | 2024-11-29 05:22:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbd71759-69f8-3904-8892-585844c60fe3 | -3.50582 | -62.85066 | 2024-11-29 05:22:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03bd0ba9-1172-317e-b5ce-a2385ba0dd85 | -1.61863 | -53.87481 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 207a42ba-b3e8-3a2e-a24e-71e5116ae19f | -1.94874 | -52.97352 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b4baf3e-a848-30d5-b26d-a8a4eca4983d | -3.06037 | -51.30117 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e85bb439-1f62-3957-9bba-38c682100a42 | -2.66393 | -48.78657 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| c7b3b89b-2b7e-3814-9967-fae9092724ed | -2.76022 | -54.07048 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d566bb7-7c0e-3c71-b077-e655d38cb7ee | -3.9625 | -47.94557 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 086f9f24-b4f7-37dd-aa0d-055203fa7d34 | -4.1725 | -48.61607 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e06aa4cd-c23b-3bd2-9231-12d8835fbd68 | -2.79881 | -54.12719 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 631746b1-c2c5-3971-8de4-f4fa9b735ca9 | -1.57941 | -53.84582 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b229695-f983-3da1-83ae-0f083f09b57b | -3.32359 | -46.69714 | 2024-11-29 05:22:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22f92e17-6e5c-3983-8316-13f96af44b9f | -4.18861 | -50.68023 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e664ef8a-bc39-37c0-949a-64bee1f49b65 | -2.87439 | -46.83847 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec08a218-e2a0-3dd1-9321-ad0531ac5d21 | -1.6038 | -55.42218 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4877217-8a8f-3875-a7f0-32ca02f01246 | -4.0711 | -50.03518 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b351717-3a44-31a5-9658-030ad06f129d | -1.30385 | -55.74265 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f09ec070-e16c-3530-a5a0-0cfdd768c452 | -2.59373 | -53.97626 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27b530b2-b240-3b48-9175-9204ce5ab452 | -1.79873 | -52.75858 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5323643c-c241-3608-af2e-839f40883e0c | -3.9618 | -47.94464 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64ecdde7-1da4-3252-a68c-ce9bdb0b938d | -3.54371 | -50.19004 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c95e185c-48e3-3df5-a259-e8f48b1946a6 | -3.73962 | -50.79057 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9707d6b-27e3-3e5a-a567-e0a81b125c4e | -4.08112 | -62.94345 | 2024-11-29 05:22:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 618afb98-7b7e-3487-8450-61f6761217c7 | -2.66378 | -48.77843 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 25642a36-489b-3395-923e-ab1614f630cb | -2.66265 | -48.79534 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| a78a2806-3fff-38f1-b3f1-b0cbfd547432 | -3.11856 | -53.26649 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 336c4c00-0523-3b90-b1db-a932eec02e18 | -3.10649 | -53.25555 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd2323f6-a886-33bb-bc69-eed1847a90e6 | -1.88859 | -54.5423 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f7bcd3f-b67b-3bf9-ba76-ee9772cb8798 | -3.32278 | -54.1678 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c85cf17-b7d3-3f56-a839-2744a7fec0bf | -2.60157 | -53.98143 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b5853e1-33cd-3059-8bdf-6f9597535c70 | -2.73371 | -54.13279 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c0e8af2-557b-3724-a5a4-aae156c97937 | -2.77304 | -53.98525 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d4edcbd1-5c97-3d10-968e-5e9f67389bdb | -1.36164 | -54.65797 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3a552060-f709-3171-ba35-e77b2595180e | -3.36444 | -50.40685 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 380256db-18d7-3938-bfea-87d6b69fbd49 | -3.03023 | -48.50163 | 2024-11-29 05:22:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75796616-d8ae-3174-b04f-e066ac02e727 | -3.49747 | -50.45689 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4d305e2-cb4c-32cc-b1ed-4b18409810ae | -2.83108 | -54.08518 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4f46f8d-4f25-3736-bf9b-12b91d093d10 | -3.3152 | -53.75128 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daab5ba0-3fa0-339f-91ac-abf09713075a | -4.486 | -48.11718 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3755dbba-40f2-3edc-a2e4-03759b4d4714 | -3.25033 | -50.61774 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35d78889-f5ab-31ca-b3cf-a24605ea68f3 | -3.85619 | -50.15093 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0dfaaa7-156e-322f-8d14-16a3a65e63ec | -1.71513 | -52.63115 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 35538a60-f9b5-316a-bbc1-6e08fa242308 | -3.23851 | -53.92648 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ed7d593-fc29-3077-a6b2-46e6ad50b197 | -3.5957 | -50.36259 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 249d66d2-a1e4-316c-bd7d-44fb33f90c64 | -3.58449 | -50.51127 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 974396e5-a103-3ef0-a33e-a34170fcb250 | -3.54229 | -50.18856 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49811989-babb-353a-8c73-6a0e193d12cd | -3.09164 | -54.13042 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aec783a8-e8da-3310-91f9-daa15005ce18 | -3.11497 | -53.10625 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b26fa9bc-73dc-3196-a7b9-f13c688e38b0 | -2.36562 | -54.35867 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0d6e740-53e8-33a3-9364-ced21771c01a | -2.81054 | -54.02292 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4adb3253-657b-3717-8874-779cd5690f90 | -2.57685 | -53.97371 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 204a4cfc-5768-345b-846c-4600696aa905 | -4.47511 | -48.19493 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7933e374-f745-32df-8485-a6d7e53755a4 | -1.94215 | -52.97034 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a0d5239-a27b-32c5-9873-9606d3d64685 | -4.47958 | -48.11617 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 664ce7f3-bd3e-3a20-8a96-3a8b84ba934c | -3.92272 | -53.66807 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0785886c-c5c4-3227-a14f-7ae44bac3010 | -3.13988 | -55.00337 | 2024-11-29 05:22:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9d704ed-7d61-3412-b289-ff18eb98903e | -3.09573 | -53.81195 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a994a646-cda3-3975-813d-170750a13de7 | -3.04834 | -54.04597 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8eaa2455-92ad-3c87-9db3-1e9c7b628233 | -3.27256 | -53.30762 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5a638e8-25be-39da-ba32-abde866adfbd | -2.84796 | -54.03244 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0facb9d-abd8-35c8-bb0f-4253192f3750 | -2.84164 | -54.07498 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d0a4184-376b-3401-bc83-bfd4ed80044f | -8.13251 | -47.99233 | 2024-11-29 05:22:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 985439d7-cccd-3d0d-ad3c-4054734d23d3 | -1.69932 | -52.64289 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9701a4bf-ec7f-30b9-aff4-eb7f59d1f7f8 | -2.65777 | -48.77751 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cd455757-cdf4-32d8-9acd-84a217266a73 | -1.35265 | -55.00254 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd309748-7fbc-3b15-8488-ee53106505fd | -2.20487 | -52.04513 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b28138f6-4008-30f3-b8dc-9a0583d536fa | -3.29263 | -53.68625 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a4282ce-4bae-3eb2-89e0-daf204d15283 | -1.69374 | -52.44265 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e3a6e2d-6f5e-34a1-b8d6-8b492fdaae34 | -2.60579 | -53.98207 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3119924e-60d3-3bdf-8913-e83e3210fb7b | -2.42353 | -54.01732 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c80f065-7253-3a08-9a19-4d676fe4a730 | -1.78267 | -52.74215 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6c4709d-6467-37dd-a164-fdbcd174b118 | -3.05257 | -54.04659 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 938e2513-c009-353d-a96e-56d1d9fb25a8 | -2.7335 | -48.89598 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07280b8a-fbfb-39aa-ac63-49077117bcda | -4.41033 | -55.1131 | 2024-11-29 05:22:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db7850a6-9888-331a-8f08-546ee6f07878 | -4.18914 | -50.6767 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d817e31-8259-3d7b-8ff8-bb41ed8bf3c2 | -2.2597 | -53.46247 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4525c488-3333-3388-ba31-1ec8d2318871 | -1.69623 | -52.446 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6297cf9f-84be-3442-9505-a3584d61ba38 | -4.17407 | -48.6204 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b19c695-41c5-3a30-892e-2b1679e418ec | -1.67747 | -52.42556 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e70f7458-d668-3dd8-8c6d-2ccefefed17c | -3.30607 | -50.75905 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2ad14ef4-13dc-3113-ad57-3ee8ca5702f4 | -2.14051 | -54.90008 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 508325ed-295d-38bd-b189-172fb14e1ac3 | -2.30248 | -51.98591 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| edb0ac4e-3d1d-3cb9-97c8-f0120cdb7583 | -2.58563 | -51.91905 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6411e3d2-5a7c-3717-811a-71fa54dc704c | -4.51321 | -59.81613 | 2024-11-29 05:22:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4345980-7a94-31e5-9297-d91831e1d362 | -2.66847 | -48.78799 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 2692a763-367d-3912-ac9b-1eab3a3d87af | -3.05823 | -51.05622 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README93.md)
