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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98eeb971-aac4-3671-b479-de43c197cfb9 | -2.48754 | -56.09417 | 2026-10-03 05:16:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e489d6a1-72b9-3b10-9731-a6fa45457813 | -4.44947 | -47.92679 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 05006fe7-9a92-31a2-ab00-43613b47534d | -1.26676 | -54.55431 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15fbf783-86e4-3cbe-b1a9-7d958646574d | -1.21896 | -54.53993 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3a6b4409-567b-3309-b3d8-cac75acff695 | -3.16006 | -54.07566 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d5d337a-821e-36ed-91bf-9601cb23ceda | -1.27231 | -54.56224 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7858f4a-7fc6-33d2-bb61-e53d79a009af | -3.10828 | -50.29514 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20eeff6a-b734-38dc-ac04-abaa61d2d105 | -4.68718 | -55.79273 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da25f623-c41d-310a-b37d-bd57041f6afa | -4.43038 | -55.74514 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3401df47-3473-36ea-b797-b8b13e31c7aa | -2.90072 | -54.08578 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60b171c4-496e-32e5-8822-84ca79faf60b | -3.18934 | -54.09869 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| decc6977-76b4-31fa-9059-ba006dd9e6ce | -3.14133 | -53.73574 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41b35c29-41a8-3571-8dd3-9cb6a10d196e | -3.074 | -51.27706 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f4e78c8-5bff-35dc-ae7a-d73e7ef7cd85 | -2.89856 | -54.14283 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eac3c6f4-d23f-3471-9292-3abf27a300d9 | -4.79303 | -55.72076 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc6c0e7a-16aa-305a-ae47-16f7a16cb122 | -3.12279 | -53.74381 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dc6d9529-6520-334a-9a97-92198112ad7a | -1.65692 | -55.21115 | 2026-10-03 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c5a3b00-f5ce-37df-9860-4598ca9d8e39 | -6.34076 | -43.36332 | 2026-10-03 05:16:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbaa1a2b-a879-38c3-bcbe-e056bbb46cb2 | -3.10431 | -50.29456 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71af333a-ab99-34b5-b946-be95c560def8 | -4.39859 | -49.9644 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b43408e-25d1-3ca8-9b97-f7fc60cbf63c | -4.04208 | -54.22373 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 375c0546-d07a-37e6-a363-cdc2d134c1d7 | -2.25506 | -51.93141 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43c95021-ebf8-3a0d-954c-a97d1b4385d1 | -6.20102 | -53.26853 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 871f4b21-f147-35bb-a337-e6b333ccc182 | -5.89189 | -55.48976 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7f1fb95f-a7ab-3836-84d3-ea4e2f074502 | -5.22096 | -46.02402 | 2026-10-03 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea705e1b-ecfc-34b4-b30a-980f68e8f8b9 | -2.57344 | -54.74259 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b686ce19-2596-3735-994d-b28474e4f261 | -5.86754 | -50.15758 | 2026-10-03 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0539d6f3-9343-37a5-a54b-f1e7f4e27b99 | -1.35494 | -55.92426 | 2026-10-03 05:16:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88e73300-f165-34ec-b818-71ca9cd355d6 | -3.07841 | -51.27323 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a77ea182-a6c4-34aa-b425-dff759333e64 | -1.27286 | -54.5588 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acc7f3bb-1c81-3f10-8fbe-7bae53c5baa4 | -3.05753 | -54.16026 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 483c91c2-6b31-3069-a90f-a3d321cf3abf | -3.00008 | -54.23027 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9692c623-1abe-3bce-86a2-23d5a4cd9532 | -3.58317 | -54.36811 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48093082-09cf-3d4c-8d4b-9e27872b6ad1 | -2.15085 | -59.22626 | 2026-10-03 05:16:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad784966-5d9b-3c14-891d-f44703827732 | -5.25223 | -55.92144 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16299eba-5d72-39e9-b788-1328996f78ab | -2.89295 | -54.11329 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f976e1a-ed41-3ff3-a733-dab9befa28ac | -4.45947 | -47.92439 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12501fe4-a16e-3dd7-94b5-432f0568ab4c | -3.88129 | -49.68786 | 2026-10-03 05:16:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66c81967-1326-330a-8f46-27ef1acde751 | -3.28925 | -53.83582 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7bfc1cd-d5b0-37ca-9041-4cfe4904b579 | -6.74168 | -44.14234 | 2026-10-03 05:16:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 84674c5b-afbf-39d6-8f26-153458a6de67 | -2.54477 | -57.40611 | 2026-10-03 05:16:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97287c1e-040c-3b61-a096-898e5283608d | -2.3391 | -51.94302 | 2026-10-03 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 467ad8a0-3e13-3f75-8782-a097fff95a61 | -2.91528 | -54.14544 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dcfc49d-d778-3f49-88c0-9bf7ab481e4d | -1.26621 | -54.55775 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9931bfd4-913a-3f37-8418-d087a5bea17e | -4.36426 | -47.77836 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04b7e75c-56d2-3401-960a-7c7db3c8e20e | -6.31672 | -43.3425 | 2026-10-03 05:16:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66e15743-60aa-3287-8a0f-d3af8840d56d | -4.26884 | -50.74124 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12fae5db-ad63-3547-8d26-e14116a1a94e | -3.0203 | -53.88448 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fec40bd5-6c6d-359c-a368-a382222373dc | -3.6437 | -55.50308 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83434f47-0a25-394f-bcc6-ed1b7c21b973 | -5.89244 | -55.48629 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e7e3edf7-53af-329b-b168-c6a581af3181 | -3.71793 | -53.39523 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb8ab19d-1d8e-3af3-9013-ab8921da2f3c | -2.22708 | -51.92293 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fc3bd40-8db1-3697-b32b-ad87659a2464 | -3.27695 | -54.0007 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2e994566-18cb-3457-81a2-acd71a255872 | -2.3381 | -57.98827 | 2026-10-03 05:16:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2777bc4b-7028-3bef-a681-428b73e66c87 | -3.01639 | -53.88749 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77e64d83-2f43-31f6-9e55-211b72a12bc5 | -3.1787 | -54.07904 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d15490ff-6d8a-37c1-b1a2-f00d3002c14a | -3.21542 | -50.91196 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58385fb9-e881-3b5e-8b5b-4b16fe1ab391 | -2.93034 | -54.15854 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e248b6ea-8a7e-3f9f-88f1-43f1bd68d532 | -1.22338 | -54.53355 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53a59ff6-ddcb-3f30-a19f-865675144b5e | -4.11692 | -55.01413 | 2026-10-03 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1008bb77-860e-3535-95e9-27a6b19bbec8 | -1.27618 | -54.55931 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d459a14-363e-3a34-81a0-312efbca19bf | -3.22475 | -54.30857 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3ea6cc6-a46f-39b5-805a-64512a8c6297 | -2.89793 | -54.08176 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50c10901-6633-3688-bb12-a2cece2b36e7 | -3.58183 | -55.55381 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bec916d8-92bc-32d2-938a-57730f610474 | -3.29374 | -53.85107 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bab494ee-a0a4-3cc7-b5fc-dcd5e532ed19 | -2.91025 | -54.13391 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 686ffcc6-0687-35ac-ad95-e3a3612eb5d9 | -2.99953 | -54.23377 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 027e3b8f-6e9c-3476-bb66-3feac65c2154 | -1.25956 | -54.55671 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6150a72e-0ed6-3a03-88b5-663430377920 | -6.6134 | -44.71783 | 2026-10-03 05:16:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd54b1b3-97d1-3589-9633-9177925271f5 | -4.35947 | -47.77765 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 7a4906bc-bb4a-3689-ab93-8c330ecf4005 | -3.17594 | -54.09664 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b3ef219-5ed0-325e-bcca-aaabccb76020 | -2.97368 | -54.09357 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34ef150d-51aa-32d4-868b-5a71fa9a7d07 | -4.27203 | -50.7467 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29d49797-e073-39fb-a2fa-1f87ee176626 | -2.88288 | -54.09017 | 2026-10-03 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25ef8992-4b57-3b57-b8b4-7197bd835be2 | -3.76408 | -55.53268 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 749a24f2-48c8-3c31-b472-c5d6ca557c5c | -3.06521 | -49.36199 | 2026-10-03 05:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9c455ce-bb96-3069-b798-33aacfa9199b | -1.26179 | -54.56413 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e4360c9-8e42-3049-bb20-708b3bd61627 | -3.17235 | -54.08479 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f7ac47f-4983-31f6-a15d-0ca6f81dce2f | -4.4521 | -54.90365 | 2026-10-03 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2cd389b-6a15-3fba-a5d1-68ab7125769d | -5.88596 | -57.67682 | 2026-10-03 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c91c4f4c-8a23-32f7-94a4-cbc3cc4425ee | -3.61152 | -55.51223 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b671e5cf-fb13-3f7b-8c80-dd2fc1e67fa2 | -1.45306 | -54.64373 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b79f9890-25ce-3480-9466-b5f2058bb565 | -7.4597 | -54.99059 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cda243c-e9a5-34e4-83bd-8549eae54abe | -3.07574 | -54.37038 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 250ba334-8e3e-3d27-b7ea-683318a98447 | -2.85161 | -51.28933 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d4f8054-dd24-398d-90c7-9cfc3dcbc840 | -6.01236 | -53.53369 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 975c5832-2436-3362-9ede-3525013037ad | -5.88579 | -55.48524 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7192e685-e5a7-3f22-b617-ad9e125d95fb | -4.40575 | -49.97293 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69481257-ef5c-389f-8bde-79ca1aaedc57 | -5.98872 | -55.37351 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a552a583-62a0-3e1c-8c05-567defeefca0 | -4.41099 | -49.96622 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca7bffa8-8c9b-3e66-9228-4cd3ce369cb9 | -3.00801 | -50.47366 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 802218fb-647d-3064-9d41-4c7dd967f95c | -3.64315 | -55.50654 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cecc176-8c37-3f01-a404-da200ed6ff51 | -3.17291 | -54.08127 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d349bd20-954f-3529-8dc7-38cd44e03137 | -5.21115 | -56.07212 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9162640-7536-3e0e-ba83-784b796cdcad | -3.27015 | -50.08599 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a710682e-3e8c-37ab-83db-da063e0a1313 | -6.21629 | -53.26269 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ef98826-1195-3655-8c1c-0d3ae67d0003 | -2.29154 | -48.7594 | 2026-10-03 05:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 464fdfb4-38d9-34ea-9fb9-1575990408ef | -3.68048 | -54.18593 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bb3da45-7dbe-35aa-b84d-8035f9dac5a9 | -5.72352 | -43.28361 | 2026-10-03 05:16:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d170c388-12a5-330c-864c-5e2340fee679 | -5.95774 | -43.64937 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README34.md)
