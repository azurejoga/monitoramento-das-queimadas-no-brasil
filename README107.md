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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d52207a8-3c22-3b20-8d3c-4e36f8502fc4 | -8.9031 | -45.82 | 2025-09-04 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| dfcdf27b-400a-3bca-b723-116998b0f38e | -6.1665 | -43.3273 | 2025-09-04 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| ec6bac58-ec8c-37d7-b709-de3c3aa49fc0 | -12.4593 | -48.0885 | 2025-09-04 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| c8f961d4-e7e3-3042-9422-447076bba35f | -15.4564 | -53.0183 | 2025-09-04 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| fcb958b5-49c4-3249-b2bc-ce5859bc9ddc | -6.8941 | -45.5609 | 2025-09-04 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a6d7c5d5-fb19-37e6-b05e-78dd3842c5ab | -7.6851 | -48.7386 | 2025-09-04 13:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 377.8 |
| aa661e4e-c90c-3007-bccf-5c4cfebcc193 | -5.8601 | -46.1116 | 2025-09-04 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 58943886-2378-3de7-b04d-5b1d1b4432c3 | -5.811 | -45.3065 | 2025-09-04 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 2cd61229-4f2f-3051-a2b5-46a8c1143665 | -12.4977 | -48.0832 | 2025-09-04 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d1ac3087-7c82-31b1-92bb-c6be66e889c1 | -9.9597 | -51.6454 | 2025-09-04 13:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 9a298dad-e288-3aae-b66f-9cd6ff3745e1 | -8.0389 | -44.082 | 2025-09-04 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 188.5 |
| feb98a8f-bc28-3012-9a0c-dea65aea22d2 | -6.2318 | -42.4278 | 2025-09-04 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 212.5 |
| 49fe882b-80d4-30cc-b249-c6d65049ab8b | -10.9867 | -45.9325 | 2025-09-04 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 682e4ce0-c52a-3613-9f24-0e70f41d6185 | -9.6913 | -49.0089 | 2025-09-04 13:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0f531ad0-3d1e-3e71-9abe-dc8bf1a7785a | -14.5852 | -53.0268 | 2025-09-04 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| d9036193-0b04-33fa-ac56-51d2684ba811 | -5.7927 | -45.2626 | 2025-09-04 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| c1882c1e-d018-364c-adde-8490cef99f4a | -8.0392 | -44.0588 | 2025-09-04 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| a2f562b1-906c-3047-a10c-020f05bdf6f4 | -11.0062 | -45.9072 | 2025-09-04 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 018ec03a-6f0b-391b-bb0f-d7b51d7bc64d | -7.912 | -45.2192 | 2025-09-04 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 6d2d9abb-95c5-3032-98e7-3269e57db83c | -4.9951 | -56.256 | 2025-09-04 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 9b86a1d9-e164-395c-933a-0c2fa1f8615b | -7.6854 | -48.717 | 2025-09-04 13:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 98.3 |
| c7e4658c-3cd8-30cb-a742-de13e263c426 | -12.5233 | -53.8071 | 2025-09-04 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 14f1222f-5e33-3710-bd12-0e92e850d434 | -7.953 | -44.9417 | 2025-09-04 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 4d9e0a50-d4be-3895-b935-28464810d9fe | -6.2127 | -42.4532 | 2025-09-04 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 133.8 |
| 7efc1ff9-3a89-3ff5-a3d4-7b8a771121f1 | -4.9049 | -41.7696 | 2025-09-04 13:50:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 154.3 |
| 2872f81d-e7e0-3372-8117-97ddb3e3a153 | -10.6577 | -51.5996 | 2025-09-04 13:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 475.2 |
| a2452ab8-462c-3294-b687-f51005a26403 | -6.7686 | -45.0051 | 2025-09-04 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| ebd9a8f8-9f6b-35f0-b830-a83fe5c078e9 | -5.7528 | -45.5587 | 2025-09-04 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 86a99f34-f6de-3ccb-adf2-433690b85724 | -5.774 | -45.2639 | 2025-09-04 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 439.3 |
| 37bfc33c-5a41-34b3-b185-e4b26ff2e77a | -5.7187 | -45.1773 | 2025-09-04 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 18e99841-c797-3fde-9e4d-b012951aad2b | -13.8453 | -47.9988 | 2025-09-04 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 4a9d74dc-8677-3545-b772-df06e86a4595 | -6.0232 | -46.6784 | 2025-09-04 13:50:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 23204609-cc69-35a6-bdd1-8d4d0f6994fc | -10.4655 | -50.412 | 2025-09-04 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 188b84af-69a5-3c7d-a583-1830bdae05ae | -15.737 | -53.635 | 2025-09-04 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 1c37b946-de0b-37ab-af78-efa92e01a105 | -11.5969 | -52.113 | 2025-09-04 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 187.4 |
| e3ae9fce-a25e-3165-9df8-d5e2f7e5ceaa | -8.02 | -44.084 | 2025-09-04 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| a1e48ec0-48bd-338d-bf7c-700c6213ea50 | -16.0474 | -47.835 | 2025-09-04 13:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c096d931-f7bc-36c9-8a3a-4112418a6b9f | -11.6599 | -54.5297 | 2025-09-04 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 6ed03e3a-c158-3997-8ae8-34fdc38c15e9 | -6.2249 | -45.0491 | 2025-09-04 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| de931185-84b7-3bd7-b339-7d58e47d6873 | -5.7 | -45.1786 | 2025-09-04 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 5b828006-c337-36d2-8a83-da30aabd33ff | -8.3641 | -48.3334 | 2025-09-04 13:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 669cd429-f7f5-38d0-942f-3673a4ec2174 | -11.5972 | -52.092 | 2025-09-04 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| a651b9bb-ca14-36ac-a0b8-1f2dd63ebe42 | -8.8842 | -45.822 | 2025-09-04 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 248557ed-9e92-3095-a3bf-e758394f2bcc | -5.8206 | -46.3595 | 2025-09-04 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| c9d01bb5-6480-3fd4-bcb9-b34d9e8b66c3 | -7.7036 | -48.7587 | 2025-09-04 13:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 123.0 |
| ed8c2de3-740f-3399-b1c1-506121343ed8 | -6.2062 | -45.0506 | 2025-09-04 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b44247e0-2be8-399c-beea-7ac8d3028a72 | -8.9028 | -45.8426 | 2025-09-04 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 85b4302e-2e9b-3789-a2cc-657ad349ab67 | -5.753 | -45.5362 | 2025-09-04 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 7e2d4d1f-a947-32b1-9c9d-011c2c848b49 | -5.6777 | -45.6089 | 2025-09-04 13:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 286dadde-c52f-3162-b07e-f3db3fc80db2 | -5.5401 | -46.4448 | 2025-09-04 13:50:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 8b8687e0-1657-3125-a211-a1c1e3666fcc | -4.8862 | -41.771 | 2025-09-04 13:50:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 141.4 |
| f52c2a6d-0220-3c96-8b3c-472d7789d916 | -13.8647 | -47.9958 | 2025-09-04 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 62496a54-5cb5-356b-8321-b64aeddfffbf | -9.4376 | -46.7947 | 2025-09-04 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 37db9af0-b757-34f3-ba4b-ed7c78464498 | -11.6601 | -54.5093 | 2025-09-04 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 109348d1-2e8e-3269-bc18-28e64f5c545c | -11.7385 | -47.7637 | 2025-09-04 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 63f83c99-358e-3109-bca7-e8e4c573f2a3 | -8.0796 | -45.3617 | 2025-09-04 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| cb6929cf-c6b5-35b5-8c19-04a15d3b131a | -10.1454 | -46.265 | 2025-09-04 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 57308b95-4c69-398e-8068-6577ff0c0300 | -6.6669 | -43.9587 | 2025-09-04 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a420fa31-bb63-3345-befb-dee90cf0b4cd | -9.7102 | -49.007 | 2025-09-04 13:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| a4952b9e-03d6-3c93-9a3a-8941490aede6 | -5.8801 | -45.9537 | 2025-09-04 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 06895fb7-ce7e-31aa-a568-d705283352fa | -14.3916 | -53.0722 | 2025-09-04 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a5deec0e-2059-3ca6-b9f4-71ac0255c2e3 | -15.5848 | -50.3129 | 2025-09-04 13:50:00 | GOES-19 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2ed04ac7-b56a-39e9-ad71-24ae2f479733 | -11.5782 | -52.094 | 2025-09-04 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 3e8fafef-a813-36a6-83f8-0dc2080c5b0c | -11.5779 | -52.115 | 2025-09-04 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 226.8 |
| 020e4cc4-1c81-3d66-ae9d-e373a24be102 | -7.7252 | -50.3174 | 2025-09-04 13:50:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d3469fd6-a690-30ef-90e2-207ba02eb323 | -7.7039 | -48.7371 | 2025-09-04 13:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 06735251-5aa9-39ed-b77a-aa9c9e4f51e5 | -8.0572 | -44.1264 | 2025-09-04 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a603acb3-b4b8-3ce3-aa5e-7576511b2fc5 | -12.4785 | -48.0859 | 2025-09-04 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| df1cca92-dca2-3141-8a4d-40845f615e64 | -5.8525 | -57.7722 | 2025-09-04 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 741dd2c2-f167-3cd3-97c8-73f670938163 | -8.0417 | -45.3882 | 2025-09-04 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c674bc8f-89e1-3572-ab1a-8a3f72730780 | -7.9117 | -45.242 | 2025-09-04 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 276.5 |
| 235ccad6-c50a-35cf-8852-41e56e5b4f59 | -5.5403 | -46.4226 | 2025-09-04 13:50:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7656cbc2-eaf1-3dc4-8955-0ba199d6344d | -17.0652 | -46.449 | 2025-09-04 13:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 171.8 |
| d3d66c4e-1108-3e0d-a833-c00bf6f325df | -6.2606 | -43.2961 | 2025-09-04 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| dd59a04e-0297-3f48-af87-5885cee5c8dd | -11.6525 | -52.212 | 2025-09-04 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| d6239dd3-d82f-3c6b-9e9c-22775d06cfb7 | -5.7341 | -45.56 | 2025-09-04 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 6519132c-4dcd-33e1-add6-5e7b3c06e397 | -6.2952 | -43.5961 | 2025-09-04 13:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e1306f0b-1486-3d32-a511-38d453a7d706 | -5.8896 | -57.7318 | 2025-09-04 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| baeab896-73e1-3596-af9b-286472a5aab7 | -6.213 | -42.4294 | 2025-09-04 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 0baf8d02-dd40-3e08-872a-870516c0b92b | -10.1457 | -46.2424 | 2025-09-04 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 265.9 |
| 371f2116-d0fc-31b7-840d-ad5c7bc0b065 | -6.0419 | -46.6771 | 2025-09-04 13:50:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 176.7 |
| a1b2e607-ba06-3127-8637-87daf4f49fcb | -6.8754 | -45.5625 | 2025-09-04 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 6e17cd06-9f25-36e3-b082-abbd2dbb3bcb | -16.5497 | -55.0991 | 2025-09-04 13:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 6256e0c4-e58a-324d-8e18-9159150cad40 | -12.4985 | -48.0388 | 2025-09-04 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| cdf02761-3bf3-3645-a03d-495896fabb24 | -8.0799 | -45.339 | 2025-09-04 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 154.8 |
| d25e33d2-a00d-3989-9873-eedc022788e7 | -6.2205 | -43.5558 | 2025-09-04 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 87fdfe8c-74bd-339a-8687-f8a15f8eb7a3 | -11.6231 | -46.6614 | 2025-09-04 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| e14bec26-320b-3353-8cab-7482d89128ed | -5.5403 | -46.4226 | 2025-09-04 14:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 585a8c5c-a646-3cea-8c99-2d33d876bf30 | -5.6992 | -45.2692 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| f9f4d406-7cc5-3888-b481-55d241145905 | -7.7409 | -48.7772 | 2025-09-04 14:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 106.8 |
| b931b2c5-6831-39c1-9b33-460100fb42e7 | -8.0799 | -45.339 | 2025-09-04 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 71b1aeb3-3de8-300c-8015-9afc298aede6 | -6.2249 | -45.0491 | 2025-09-04 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 172.3 |
| eadd283f-06d8-3c38-adf1-b8c27c7be3ec | -13.8651 | -47.9734 | 2025-09-04 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b87f77eb-2a96-3e1f-84b0-9efa998bd8e3 | -14.9865 | -50.0769 | 2025-09-04 14:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 497a6e71-d2fa-3002-b5fc-c7b7ce4c9818 | -7.7252 | -50.3174 | 2025-09-04 14:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 66a05a87-907d-3224-bf6b-000a59042384 | -8.9028 | -45.8426 | 2025-09-04 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| df9532d0-e740-3e0f-bafc-d84f9e25f5c2 | -5.7341 | -45.56 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 4cff00d0-2861-31cb-9291-b22bb426229b | -12.5233 | -53.8071 | 2025-09-04 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 700ce952-0884-31dc-b819-2a660c1f4aad | -10.4655 | -50.412 | 2025-09-04 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| b7b341a9-6c3d-30c6-aa8a-5b12e7515ae5 | -5.7189 | -45.1547 | 2025-09-04 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |


[Clique aqui para ver as próximas entradas](README108.md)
