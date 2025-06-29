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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b473b937-8a94-3800-9315-5aded7a82e9c | -12.4831 | -58.465801 | 2025-06-29 01:30:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51c7d13d-1bd5-3e5b-90d5-711296fc13d6 | -10.3538 | -57.496498 | 2025-06-29 01:30:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1d76615-daac-301c-8758-83c7a94ebb16 | -11.0418 | -56.273701 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84b5e7f5-0f94-3a42-b439-500b84678ecf | -12.106 | -54.668701 | 2025-06-29 01:30:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0cefd8e9-b23d-380e-af9c-869b3f9eccc0 | -11.2729 | -52.761799 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d76d79c9-9091-3afe-8403-bfb9da0f9b7f | -11.2689 | -52.745998 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a604a001-35e6-38c9-946b-0621b026efcc | -11.5681 | -52.7845 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5aabb5d-dd7f-358b-9295-cc0c96e3aa92 | -9.2483 | -63.289501 | 2025-06-29 01:30:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0237aafc-46b5-3b32-b00c-92142a2a9abf | -11.0154 | -56.249802 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d277ff8-9f54-322e-8b58-e817e19455c3 | -11.0131 | -56.240299 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67c9317f-629c-363b-9f86-980ff5980f95 | -12.4963 | -58.478199 | 2025-06-29 01:30:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8ed5d73e-b41b-3647-863c-de1c7cc76008 | -10.8423 | -53.751301 | 2025-06-29 01:30:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3666732c-3be8-3321-a7f2-d99ace4975b1 | -9.4743 | -57.838402 | 2025-06-29 01:30:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30ab5aab-9c78-3a7c-8c4b-8face6d195f8 | -12.115 | -54.580299 | 2025-06-29 01:30:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed492360-93c1-3c5b-83d0-5ecc7697afe0 | -10.0471 | -59.355801 | 2025-06-29 01:30:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4574e864-92f1-3325-b202-80c116c0564e | -12.4929 | -58.463402 | 2025-06-29 01:30:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7aba094-56c6-359b-9e18-f1b4d927d566 | -12.6226 | -54.2104 | 2025-06-29 01:30:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51f2e345-71ad-3f97-b434-098970a61c82 | -11.53433 | -52.7598 | 2025-06-29 01:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| d9f42d7b-a3d8-3a3d-941c-19afa94e73b1 | -12.50245 | -58.34909 | 2025-06-29 01:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 21dc2caf-c879-327c-9b0e-35e08469c867 | -12.62625 | -54.217 | 2025-06-29 01:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| cc0c9784-5f7d-306c-ba9e-ceb5bc3c89c3 | -12.4769 | -58.47543 | 2025-06-29 01:39:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9af81af1-9cf3-3116-a402-3f0c5e447eae | -12.61292 | -57.88618 | 2025-06-29 01:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 89bc6a00-7596-34d8-bda2-767f30c840e6 | -12.61029 | -57.86987 | 2025-06-29 01:39:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e758a385-dbc3-3e32-a776-c78287fe912a | -10.83705 | -53.75236 | 2025-06-29 01:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 198ff517-8206-3545-8cf1-e33715e321fd | -12.48796 | -58.47936 | 2025-06-29 01:39:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 15807a7d-108d-33c1-80d3-de581c6fa316 | -10.83162 | -53.76042 | 2025-06-29 01:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 68928736-6c58-32fe-aec1-b23fd8cbd3b0 | -11.53421 | -52.76486 | 2025-06-29 01:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 34b90fbc-58dd-364e-9d20-35e2892364e1 | -12.48801 | -58.47365 | 2025-06-29 01:39:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 4f95ad65-9cb1-38ec-86f9-7f15005be75b | -12.47454 | -58.46622 | 2025-06-29 01:39:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c7248f25-50a1-34d9-ac66-7f027e3efc19 | -12.48566 | -58.46439 | 2025-06-29 01:39:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 01438fce-51f2-3430-bb48-eebe57570503 | -11.25713 | -52.75014 | 2025-06-29 01:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 62a5e724-4817-3c5a-b265-36240a3ec7d9 | -12.62154 | -54.21126 | 2025-06-29 01:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d670ae40-76e7-3492-b174-a5211f7cf16c | -11.25689 | -52.74297 | 2025-06-29 01:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 2a298433-9015-3ebb-9fd4-2549f2c367ad | -11.0354 | -56.2844 | 2025-06-29 01:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 1d94a66f-ef84-33b1-bee0-cb8dcd1deac1 | -10.9808 | -45.1335 | 2025-06-29 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 83717f34-753f-3b17-a086-34ee9b5bc928 | -22.4056 | -46.8205 | 2025-06-29 01:40:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 6e6bbf14-f306-3b29-8d4a-bca89cb0026f | -10.5579 | -52.0289 | 2025-06-29 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 1cd9de51-b426-38ec-bf07-563ec8104075 | -10.9811 | -45.1104 | 2025-06-29 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 199.1 |
| e5068be7-81e3-336e-8c31-778d2b4cce79 | -11.0168 | -56.2659 | 2025-06-29 01:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 110.1 |
| dc9e84c9-5eb2-31f9-b9bf-451878044b54 | -11.0166 | -56.2859 | 2025-06-29 01:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| bf0d75e9-eb85-3b7c-a9b1-8513f02fd8de | -10.9815 | -45.0874 | 2025-06-29 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 66937bc4-6343-3fd1-b008-98948f3c75fe | -10.5576 | -52.0499 | 2025-06-29 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 157.0 |
| bef75fad-b21d-3401-a5be-abfc22b39034 | -11.0356 | -56.2644 | 2025-06-29 01:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 0a439b4c-b6d4-36fb-ba44-04602c47202a | -17.4045 | -42.6186 | 2025-06-29 01:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e22780d5-af0b-3366-8334-7ad50c21bb62 | -10.962 | -45.113 | 2025-06-29 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 54c82cff-8f99-3416-9820-f4199c344d34 | -9.71658 | -56.19608 | 2025-06-29 01:41:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| e33c0f49-2d15-3bb0-bb42-f7fd66770ea1 | -9.08662 | -59.49908 | 2025-06-29 01:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| c6a23387-3ad4-359e-a95c-dfa7bf336b14 | -11.02525 | -56.28243 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 193.3 |
| ccdf61ec-f55b-34f6-9de2-4261085c71c4 | -10.04208 | -59.35743 | 2025-06-29 01:41:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8f8a7105-4cc0-3653-b5ab-0d90129da953 | -11.02845 | -56.25273 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 14ebb8b0-e56a-38fd-809e-ee52ca472f9e | -11.03232 | -56.27574 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 170.6 |
| c82d4ce0-6432-3121-859b-4012b20d046e | -9.24608 | -63.29004 | 2025-06-29 01:41:00 | TERRA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7d734484-d5a2-3231-98a7-75564ab40c09 | -11.02261 | -56.30088 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| d421ed94-74a8-3335-9c85-4d808d822ef1 | -11.03883 | -56.28017 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| cdb37387-1f46-3c9a-95b9-5b85844aae5d | -11.01873 | -56.27798 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 122.8 |
| cc188304-9a3d-3410-8da5-2b7fabe0b067 | -10.35564 | -57.5199 | 2025-06-29 01:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0335c37d-f103-31f6-a995-b55a97429d1d | -11.0148 | -56.25482 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 6b789122-f02f-3708-a278-5c1ef01c3d71 | -11.03512 | -56.25698 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 99639b75-fd76-3bd9-b93f-072963b8880d | -9.47335 | -57.84018 | 2025-06-29 01:41:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ec0069ea-1ff4-361c-912f-431eff62247d | -11.0178 | -56.23623 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 0eee0faf-5236-3fa7-b216-ae6065f48f85 | -11.01089 | -56.23172 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 472804c1-38ce-3cd1-bc16-500cdef74ef9 | -9.24735 | -63.29902 | 2025-06-29 01:41:00 | TERRA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3a2b325d-8dbb-3efb-8292-a41a65674db8 | -10.30587 | -57.12626 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 6c874190-63b5-353b-b3a9-37355e2e7e30 | -11.03619 | -56.29872 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| bca6840b-c854-37f3-8646-c00921e3f524 | -10.35264 | -57.50113 | 2025-06-29 01:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 0454c614-732a-3534-9632-ee1c74993bb7 | -9.08448 | -59.48507 | 2025-06-29 01:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 75efcf59-6e5e-3354-b75f-192b3f73d79f | -11.02154 | -56.25941 | 2025-06-29 01:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 289a17b0-97c8-3e87-b4e7-52714ad5e466 | -22.4056 | -46.8205 | 2025-06-29 01:50:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 66.9 |
| b0f37ae3-d82b-324b-affd-ceed3285a13e | -17.4045 | -42.6186 | 2025-06-29 01:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 299d9fd2-4e04-355f-a310-04ddbd4102d1 | -6.634 | -47.274 | 2025-06-29 01:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 53003663-cd83-3b29-b1d2-4bc284c138c1 | -10.5579 | -52.0289 | 2025-06-29 01:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 430ebde6-5140-3bf0-af8f-778a7a589b59 | -10.5576 | -52.0499 | 2025-06-29 01:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 165.0 |
| d494ed23-f574-3904-bf67-9a3a23a5d207 | -11.0356 | -56.2644 | 2025-06-29 01:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 6bc40114-944c-3718-8198-9b0727bb3eb4 | -11.0354 | -56.2844 | 2025-06-29 01:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| fbf83ac5-a525-37b0-9ca8-4f363a0b3002 | -11.0166 | -56.2859 | 2025-06-29 01:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c35354ef-3cdb-3f3b-b03f-4bf2a7cf33ec | -11.0168 | -56.2659 | 2025-06-29 01:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 644757f4-1314-3920-b38c-305c8f369745 | -17.4045 | -42.6186 | 2025-06-29 02:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 88.4 |
| d926ba0a-e77c-3f30-8dcd-d5bd49953b61 | -11.0166 | -56.2859 | 2025-06-29 02:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 211625e2-941e-3e8e-adc5-ba57bace21c8 | -10.9811 | -45.1104 | 2025-06-29 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 910633ef-2efd-351e-96e8-e71be73d34e5 | -10.5576 | -52.0499 | 2025-06-29 02:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 5f7b0b6a-f8fa-39ed-9983-2034f9cf1072 | -11.0356 | -56.2644 | 2025-06-29 02:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 305b1525-ead8-3948-9d63-4c6bb78b9cfb | -10.5579 | -52.0289 | 2025-06-29 02:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 47b9cad2-4dc5-3f04-82f6-611d32fada27 | -6.634 | -47.274 | 2025-06-29 02:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 6e06d7c9-6a15-39f3-8c41-fd3e4fec8679 | -11.0354 | -56.2844 | 2025-06-29 02:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b839e3a2-ad45-399f-877e-f786b19b01b9 | -11.0168 | -56.2659 | 2025-06-29 02:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 61b7afb8-099e-3640-8980-5f690a3fa4e5 | -10.962 | -45.113 | 2025-06-29 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.9 |
| a1996b71-7a37-34ed-879a-4464548f00ef | -10.5576 | -52.0499 | 2025-06-29 02:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 3b9b10f2-e16a-3514-823a-e822cef3fb84 | -10.9811 | -45.1104 | 2025-06-29 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 1b7e38e4-533d-32b6-be61-2e5c096d6ae1 | -17.4045 | -42.6186 | 2025-06-29 02:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 72.2 |
| aa483270-8a4b-36b4-ab1c-3b700794b29f | -10.5579 | -52.0289 | 2025-06-29 02:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| ea376ce4-92ed-3c1b-a18c-4ecbdffbd73c | -10.9815 | -45.0874 | 2025-06-29 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 1a7e8061-6c03-3084-beb9-61ad586541ce | -17.4045 | -42.6186 | 2025-06-29 02:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| be0039c4-9cdb-3a14-8ea1-c55c7c57e971 | -10.9808 | -45.1335 | 2025-06-29 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 968afa10-aa4f-36b3-bac0-73b3e68cf463 | -10.5579 | -52.0289 | 2025-06-29 02:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 810ca682-0085-37ab-969d-13252813e28c | -10.9815 | -45.0874 | 2025-06-29 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2d71672e-3eae-384c-b618-e5c8bc19770a | -10.962 | -45.113 | 2025-06-29 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 9b519133-d235-3394-8d24-3b7b70573b5a | -10.5576 | -52.0499 | 2025-06-29 02:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 1459624d-50c0-38f0-bf30-895d494a058e | -10.9811 | -45.1104 | 2025-06-29 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 40630252-f1fe-382e-ac58-426dd81fa3df | -10.5579 | -52.0289 | 2025-06-29 02:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 06cecfe5-29a4-3f13-8458-f88b4df35f1b | -10.9811 | -45.1104 | 2025-06-29 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |


[Clique aqui para ver as próximas entradas](README7.md)
