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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdd2d458-1534-31c7-a859-dff52accb075 | -4.6613 | -49.52505 | 2024-11-28 03:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9cc4a79-555f-3d7e-b2e9-50176aabcec3 | -4.17827 | -44.26973 | 2024-11-28 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40fe5aac-61d4-35ff-ab00-d198131423aa | -2.83406 | -51.84388 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e063406b-b52d-3830-9354-333a6ffeeafb | -6.37018 | -45.69516 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 83553670-b059-3b43-bcb5-53043864579a | -5.95204 | -39.66432 | 2024-11-28 03:59:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 13.9 |
| b00a8120-dcef-3598-a23a-87a833042519 | -3.22375 | -48.81927 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 389f49b1-7768-3a91-9957-fefd7889e431 | -6.23447 | -42.98818 | 2024-11-28 03:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cf03550-7eb0-34fc-abc9-ad5f731593cd | -6.16386 | -42.62366 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 84c6c77c-477c-3dbd-b606-11f680753358 | -4.14333 | -43.84604 | 2024-11-28 03:59:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cca1caaf-bbd0-3387-80b6-580b484a9a9d | -4.17852 | -48.45077 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2c4eb08-b6f2-3392-8f84-044f8fd7776a | -1.03787 | -51.73916 | 2024-11-28 03:59:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b64141ce-6082-394d-bc6c-46938f6eccac | -6.50059 | -39.59785 | 2024-11-28 03:59:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f85bf4c-c7a0-3d46-987f-dbb40cc077fe | -4.77609 | -44.42604 | 2024-11-28 03:59:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8e59356-452f-368c-9619-e97448db0ee6 | -4.17532 | -48.45383 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b8190f4-cc38-3234-923d-4867605b1ac7 | -3.59744 | -52.54494 | 2024-11-28 03:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3a3076b-a203-3314-8db5-43ad784f16d7 | -3.49233 | -44.60436 | 2024-11-28 03:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c1f9284-fed3-3e19-a1fb-8b2fe61a0c41 | -3.17907 | -50.28209 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf11b49c-47b1-3c8e-a612-7925ba2af7b1 | -4.92797 | -45.42628 | 2024-11-28 03:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93e49c1f-76f7-3d0c-b788-785d5dcba505 | -3.62371 | -44.04677 | 2024-11-28 03:59:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 013d507c-f0ee-3b27-b839-72bd078c48da | -4.00221 | -47.91735 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9a7ab0a-221b-3c20-8c63-2f8217620249 | -3.77785 | -46.69143 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca07ec4d-9c94-30a1-9080-fcbe5cd34c12 | -2.85262 | -46.83786 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af661063-a267-3614-a6d7-8b6b6d844fc2 | -4.13698 | -44.83412 | 2024-11-28 03:59:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 997ddab0-4ba5-31f2-824b-573459cbf8dd | -4.35104 | -48.6851 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 654d6bc0-9d10-3744-846e-b149a7a081d6 | -6.1233 | -46.58792 | 2024-11-28 03:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 913cafb4-7b40-34c1-8cc7-a6ad64a9050c | -2.69977 | -51.68635 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7279e4b4-0734-352e-b4d0-7a1aaa28acc4 | -6.83295 | -44.39165 | 2024-11-28 03:59:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9e862928-8340-30ea-a117-15113258d3ef | -6.00985 | -38.66053 | 2024-11-28 03:59:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eee29294-2f30-368e-abd1-47e6170eb0ba | -3.77305 | -46.69085 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e6122eb-582e-38ee-ae79-2e6c0fb1c7d9 | -4.06229 | -48.96052 | 2024-11-28 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db818cc1-46a2-340d-8d4f-fd2e1eb1867a | -2.72974 | -48.90218 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0230151b-e6c0-3c7d-84c7-e510bc69ce4e | -6.56416 | -44.62849 | 2024-11-28 03:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 688b9a59-75f0-3f92-a257-4a078239ddce | -1.63605 | -52.46247 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c9f7099-bb16-3f59-b3fb-203ecea7864b | -3.3772 | -50.1167 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14b2ba37-64dc-38ba-aac3-3e2ca5e54e74 | -4.05277 | -46.68486 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3588949-66e9-332d-bffb-0ebf2c91962e | -3.73895 | -51.83563 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bbd4d29-5ece-3bbf-a8f3-482964f03087 | -1.64453 | -52.73268 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 08efbff9-e7e8-3621-8ae9-a0dc9aa9c973 | -4.18228 | -44.2704 | 2024-11-28 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae68b8fa-fd79-361a-ba9f-ef8fc85cebc1 | -3.7101 | -47.12765 | 2024-11-28 03:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 349c41d2-0d5b-3af1-aebd-7513d78e5f5d | -3.69047 | -50.22698 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8396c946-4a49-3d85-8cad-08548aed1938 | -6.86686 | -44.75956 | 2024-11-28 03:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a77bba37-7f07-35e6-9630-d436b25673f6 | -4.51697 | -45.80828 | 2024-11-28 03:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11b1b2b7-3157-3182-b7a5-85427feca0fc | -4.35047 | -48.68847 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ba10c38-00b2-378c-99cc-5c907410e45c | -4.09414 | -43.92464 | 2024-11-28 03:59:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dea77cf5-9d9f-3b29-a969-2484d1ffe277 | -5.21731 | -41.28592 | 2024-11-28 03:59:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2abab1aa-04ce-356f-b511-fc0fb4219cf6 | -1.32671 | -51.95443 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8fcf298f-d49a-305a-b310-c99bd7ab1b1e | -6.11868 | -46.58948 | 2024-11-28 03:59:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46a26427-ca37-3a5a-b62b-5d7463c431a3 | -4.01538 | -46.52955 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1d3e66c-6274-34a7-babd-d7fd4823bcd7 | -5.96701 | -42.7058 | 2024-11-28 03:59:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c44a737-2454-36a7-8f6e-31e5c2b183e3 | -2.63632 | -51.77282 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5854f85b-0ea7-3dd7-9f67-30be0f589d64 | -2.85386 | -46.8604 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb5ba3b4-5f93-3d77-a2e4-252e08b8b18b | -4.67376 | -44.61644 | 2024-11-28 03:59:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b909e46-6e03-3d17-9836-7c38f67607d5 | -6.86837 | -44.7633 | 2024-11-28 03:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c8bc3bc-353a-3940-9b4b-964ac2e8fee2 | -4.05748 | -46.68701 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| caf2b224-076e-38f1-9960-6f823262aa34 | -3.70649 | -43.42716 | 2024-11-28 03:59:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 91ee4e80-e511-38a3-9a1e-9cdfe5fe2634 | -4.20313 | -46.55071 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3458be5c-4ce6-3a24-a71e-67b4f72a0c6d | -3.04884 | -48.5163 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e66d97c-ebec-3437-baea-e29e97dcc0b3 | -5.21889 | -44.90741 | 2024-11-28 03:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ce2acba2-38b8-32e5-b4d0-bec94240bdbb | -4.17585 | -48.45063 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a56f519-e172-381b-ad7b-2cca50040784 | -6.249 | -37.20876 | 2024-11-28 03:59:00 | NPP-375D | SÃO FERNANDO | RIO GRANDE DO NORTE | Brasil | 2411809 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8e1e9230-e3c5-3ecd-b68a-41a84156e0e9 | -4.00573 | -44.28167 | 2024-11-28 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c782805-3224-3507-8287-b7d73eb9fec1 | -3.38323 | -50.11772 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21d9ba4e-80a7-3240-9070-ca5a8258e3ba | -4.51805 | -45.80893 | 2024-11-28 03:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54ca2e9b-b0fa-3300-90c6-b6867f2ff660 | -2.47565 | -47.04128 | 2024-11-28 03:59:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22453c47-c335-3a14-ac98-19cafcf89d5c | -3.95089 | -41.49175 | 2024-11-28 03:59:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cea44694-623e-3a03-9be0-0037e165fb79 | -3.19258 | -50.82689 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fd6f5db-8cd2-3e3f-ad77-d80a5878f94a | -5.223 | -44.90815 | 2024-11-28 03:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 23f1a9d7-6402-37fc-bf70-be8f8186001d | -4.99124 | -42.66914 | 2024-11-28 03:59:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cbd9dd3-e27a-390a-8093-3e058c23d5ae | -2.87166 | -46.87432 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f144e235-e4c5-3c3a-a765-30f6a5929c9c | -2.86185 | -46.87283 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 070c96f2-e65f-3f3f-8b15-293d09733398 | -3.41083 | -50.24741 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 811b16bb-10a0-38b9-bae5-94e3932f48b8 | -3.80037 | -44.46809 | 2024-11-28 03:59:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbfc34ff-ccb8-32a7-8352-55441a0e032d | -1.88061 | -50.59969 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee7cbdd6-8505-399e-9ba3-fd10f8eadca8 | -7.69351 | -42.97778 | 2024-11-28 03:59:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 41c6b4cc-9685-33f2-bb77-2413872fda5d | -2.7388 | -46.11753 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce4fcef5-c218-36ce-91d0-d7a28638c363 | -6.75669 | -35.09612 | 2024-11-28 03:59:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 5ec3791c-3874-3d58-b098-c4ead45f6be4 | -3.2447 | -50.76812 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f3abff7-3151-363c-8b63-295562db5829 | -2.98731 | -51.4472 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1cbcd145-377e-3d72-bf45-9a4d9618488e | -4.05084 | -50.86585 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19431ccd-125d-3e65-b47a-7601fa78b02e | -4.97686 | -49.63389 | 2024-11-28 03:59:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66739447-94d2-309d-ad26-319e4988ca95 | -2.86946 | -46.85733 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c59f2243-f873-39e9-b091-5af684ff56e1 | -3.60307 | -52.54659 | 2024-11-28 03:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ad1cf0b-0465-3753-8d95-bdeb9abe48c0 | -2.12247 | -46.41138 | 2024-11-28 03:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94c7b672-bbc3-3998-8271-0bf04630e8b3 | -5.98084 | -45.35998 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| eef1f9ef-851a-333a-b7fb-00720b1f70ad | -4.37911 | -45.97403 | 2024-11-28 03:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 040d4f6c-c338-3d53-a731-7bdc6b716f08 | -3.6977 | -51.37292 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d619f948-e154-3618-9ffb-cd1dbb0e6c80 | -3.3328 | -50.07656 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56b3246b-06d6-3ff8-b477-d40d80b3b203 | -1.6693 | -52.48254 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f807a92-d6c2-32d4-8bd5-576a4d69a87d | -3.59855 | -52.53845 | 2024-11-28 03:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbdd7b7a-8213-3741-a92f-6cdac7cdd686 | -4.01735 | -46.99382 | 2024-11-28 03:59:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93d00aa6-9b27-3035-8487-64b2c2f35270 | -2.04316 | -46.65392 | 2024-11-28 03:59:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78ffa6d2-2adc-3b69-822a-0f301093a241 | -4.66441 | -45.04274 | 2024-11-28 03:59:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfd4255a-389b-3120-a15f-2d4192a0b4ae | -4.51056 | -45.79909 | 2024-11-28 03:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50cc6f88-b8d5-3d44-ac2f-2c9adac9d0f6 | -6.3579 | -47.06406 | 2024-11-28 03:59:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46692e50-8427-3057-a86b-e941faf90b80 | -5.9809 | -39.04573 | 2024-11-28 03:59:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 202327e7-156b-3a9f-84b6-47fd88a4c87d | -3.94893 | -46.69047 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 200657b1-ff94-355c-8ef0-5e902f03e7ae | -4.09445 | -44.85827 | 2024-11-28 03:59:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6285a845-c5f4-3bc8-8d92-8c7a6ff7f92d | -3.99704 | -47.91655 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26beebf5-14ae-363c-8661-d2c91c406684 | -3.98111 | -46.64716 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c6949e0-faf0-3680-8d0b-cb24dbef45be | -3.20174 | -46.59685 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.8 |


[Clique aqui para ver as próximas entradas](README35.md)
