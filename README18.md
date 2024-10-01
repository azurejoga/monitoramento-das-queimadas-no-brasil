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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1222ae0-6484-3afc-a861-a44d49578b9e | -12.7583 | -53.9939 | 2024-10-01 00:51:46 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43f57a1e-88c5-3132-a9ec-13cf3df25f5b | -12.5653 | -53.1413 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2b345a5-d3b8-3c4a-b81f-9a58997fa54c | -12.5539 | -53.136002 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af491686-e8a6-3552-96fa-3acd11aa5625 | -12.5555 | -53.143398 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68d63b2c-68c6-3038-a589-c4d2726576de | -12.7404 | -54.0061 | 2024-10-01 00:51:47 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5ebe1c2-b095-3b19-bc7e-31e40f05277a | -12.5409 | -53.123501 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55dec32a-a37d-3d61-aefc-098ae8c2f919 | -12.5425 | -53.130798 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50f61058-1d86-304e-8600-35e54343e176 | -12.7289 | -54.000301 | 2024-10-01 00:51:47 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7e41ac4-80c3-3f5e-a156-d68666b6bd08 | -12.6051 | -53.468899 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9950800-041e-377b-b9b8-9cec05725c6c | -12.6067 | -53.476501 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de642ccc-fe20-3118-b529-abcc4c0c517e | -12.6084 | -53.484001 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6b6c0c5-c838-32d5-a9c8-0c26abc2e5a9 | -10.9896 | -46.4557 | 2024-10-01 00:51:47 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c380646-0534-3bec-9d11-2f37bcb97e70 | -10.9923 | -46.466801 | 2024-10-01 00:51:47 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ca9ac6e-2680-3460-a677-126701961eb5 | -12.5953 | -53.471001 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43e31cd5-105f-3cad-82a8-6928e47103a0 | -12.5969 | -53.4786 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b278dec0-da01-3db6-856b-f830d97e7084 | -12.5986 | -53.486099 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a086599-b56e-316d-9afb-7a1bd9f7df25 | -12.7262 | -54.084202 | 2024-10-01 00:51:47 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf489d55-05c4-39d5-ae3f-34a11d5257ff | -12.7279 | -54.092201 | 2024-10-01 00:51:47 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78b0e2c0-5f2d-3a19-90ea-7759f7e21d7d | -12.5115 | -53.130001 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0422bc64-d040-32ff-beb0-2713c38b5ac1 | -12.5131 | -53.137299 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9814b8c-2949-3b4c-8e26-594b954df2f9 | -12.5871 | -53.480801 | 2024-10-01 00:51:47 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecfec18f-57c9-3138-8979-85ce49d134fe | -12.7181 | -54.094299 | 2024-10-01 00:51:47 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51b44aaf-1e3c-3d40-8f43-6943f7527b93 | -12.7198 | -54.102299 | 2024-10-01 00:51:47 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8bb56c4f-9350-3d02-8259-c26aeb2d5580 | -12.5017 | -53.132198 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83dfc462-defc-3fdf-8cdd-d1ec42f22d1c | -12.5033 | -53.1395 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea42c3a8-61e4-3d7e-b5f7-3a992106f732 | -12.5049 | -53.1469 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05c083db-67f2-30fe-9872-422ef86cb8f7 | -12.5065 | -53.154301 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 046f736e-c58d-3686-8d48-8dcf6673d210 | -12.5773 | -53.482899 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e617dc87-e83a-3aa6-b5f3-2bb2cc0c9631 | -12.579 | -53.490501 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ffec273e-120a-35df-a66e-135cf0b4733c | -12.6897 | -54.0089 | 2024-10-01 00:51:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6fe7059b-358b-3f55-9320-1fbf463e755d | -12.7049 | -54.080399 | 2024-10-01 00:51:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f95953a6-f8bb-3b24-b80e-b650009a413b | -12.7066 | -54.088402 | 2024-10-01 00:51:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd22c32b-62ac-334c-8c95-ef08cc88cef9 | -12.4935 | -53.141701 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3470f23-e3da-3e63-bf8b-0eaf12f977f7 | -12.4951 | -53.149101 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1eba74dd-7428-3ec9-baa6-0a0302ff3459 | -12.4967 | -53.156502 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3ba51c1-df22-3216-b8ee-dd5900a19e73 | -12.4983 | -53.163898 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17de7182-0ccf-344b-ac78-d5bad1288298 | -12.6816 | -54.018902 | 2024-10-01 00:51:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd91456b-d174-3f5c-85e9-3a7a034adaa2 | -12.4885 | -53.166 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c81d536-b347-3c7f-9bad-4dc394ad8303 | -12.4901 | -53.173401 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70041723-f03d-35c4-8f67-52595086fd2a | -12.4917 | -53.180801 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82adeba2-36d0-3d59-b894-dbb476b8c93d | -12.6786 | -54.052898 | 2024-10-01 00:51:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97c84116-09a0-3c55-b3bf-8e92032ff807 | -12.6803 | -54.060799 | 2024-10-01 00:51:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97c2a284-12b6-371b-b7cd-5fe65ca2f8d3 | -12.6819 | -54.068802 | 2024-10-01 00:51:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 961b773c-1378-30ca-abc7-7ceb6b6e1f22 | -12.6836 | -54.076698 | 2024-10-01 00:51:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2029367b-a186-3c59-b631-e665288e85db | -12.5447 | -53.4743 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e83745a-f085-3aa7-a086-d82361dc30ae | -12.6671 | -54.047001 | 2024-10-01 00:51:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0f385e2-9a52-350d-ba7f-4677ff2c9a7b | -12.6688 | -54.055 | 2024-10-01 00:51:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66b066cd-5f73-35c3-af36-a462e8e6f976 | -12.6705 | -54.062901 | 2024-10-01 00:51:48 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 576698e1-514e-315c-a785-838b400d9a61 | -12.4657 | -53.155602 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bfe14525-37c4-3445-9b41-08abaa0758c3 | -12.4673 | -53.162998 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec9669b1-914d-356f-9479-60de22f7b858 | -12.4705 | -53.177799 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96840835-aaf2-3bec-b334-ba070ff1e10c | -12.4721 | -53.1852 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 612811cd-dbd5-30e1-8be0-5ebcbbadd883 | -12.5317 | -53.461399 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67811200-1165-39ac-9dc5-1f269fb2015d | -12.5333 | -53.468899 | 2024-10-01 00:51:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b68c2641-ff01-34fa-a087-c42f407adb68 | -11.7212 | -49.997002 | 2024-10-01 00:51:49 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e236221a-0890-3473-877e-628fea176c26 | -10.6871 | -46.145401 | 2024-10-01 00:51:51 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06994b74-4081-324e-a379-2137f85a39cf | -10.6899 | -46.157101 | 2024-10-01 00:51:51 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a63f25a1-3d7c-3b29-913a-61cde50aa6f9 | -10.6745 | -46.1362 | 2024-10-01 00:51:51 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c71d4996-2f19-3c8b-8ca1-2f4701bf1662 | -10.6773 | -46.1479 | 2024-10-01 00:51:51 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 767d3bde-d79f-378e-88a8-a05eb8c009f8 | -10.7683 | -46.522499 | 2024-10-01 00:51:51 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64abdf31-da8b-3008-8547-d419a34b88b7 | -12.3076 | -54.0924 | 2024-10-01 00:51:54 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16b17cc6-bb5e-3f6c-84e5-f55b6cca5386 | -12.3093 | -54.1003 | 2024-10-01 00:51:54 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5564ead1-8e46-38c9-83da-9a89e28556b0 | -12.3109 | -54.1082 | 2024-10-01 00:51:54 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29e9e922-c8d2-3d19-a3dd-35ba15aba069 | -12.2611 | -53.970901 | 2024-10-01 00:51:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa87e61b-8727-3a74-8e4f-16521b02fc47 | -12.2628 | -53.978699 | 2024-10-01 00:51:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65c0e11b-702a-3593-a109-cf73f421191c | -12.2645 | -53.9865 | 2024-10-01 00:51:54 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 73078785-a968-3027-8a41-c43869e6571e | -11.1511 | -49.715401 | 2024-10-01 00:51:57 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b831373-6ac2-355d-9036-8ef03515f48b | -11.0982 | -49.575802 | 2024-10-01 00:51:57 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f651d16d-3a91-3013-acba-63476eb562dc | -11.0999 | -49.5835 | 2024-10-01 00:51:57 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b705968f-6617-3812-bd37-05ed0643238b | -11.1017 | -49.591099 | 2024-10-01 00:51:57 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26f01081-ff8f-3240-8a54-a6e5f06f39dc | -11.1035 | -49.598701 | 2024-10-01 00:51:57 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4bb050f-75c5-38f8-bf6e-099ad0abc0c1 | -11.0884 | -49.578098 | 2024-10-01 00:51:58 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07b71c54-f782-34ba-9aa2-71f0eda733f9 | -10.7792 | -48.737 | 2024-10-01 00:51:59 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29ae64c6-6092-3809-a921-b06068c4dccb | -10.7812 | -48.7453 | 2024-10-01 00:51:59 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70b9ad8b-2b42-3aeb-b63e-95a2395fc24b | -10.7676 | -48.730999 | 2024-10-01 00:52:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 189d9784-6224-334b-b8c1-e5af761820dd | -10.7695 | -48.7393 | 2024-10-01 00:52:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f49d48cb-af82-384e-ac5d-7636936c71fc | -10.7715 | -48.747601 | 2024-10-01 00:52:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8478e64b-ee2f-378e-b3e0-f859bbf037fc | -10.7597 | -48.7416 | 2024-10-01 00:52:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cac868a7-59ae-3206-a84a-a6dbf6fcc524 | -10.7617 | -48.75 | 2024-10-01 00:52:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15081599-e46f-34cf-8b97-98a259eaf343 | -10.5686 | -48.0173 | 2024-10-01 00:52:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 247cd3f5-30dc-306d-b700-d2c9be530338 | -10.5707 | -48.026402 | 2024-10-01 00:52:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7739dbef-f8a9-3dc1-97b5-ec69dddabd27 | -10.5729 | -48.0355 | 2024-10-01 00:52:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf209db0-8fbc-35dc-9e92-fb91ef976c5c | -10.744 | -48.763 | 2024-10-01 00:52:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 621de13a-f24c-3c9d-828f-dd368dd2f08c | -10.5566 | -48.010601 | 2024-10-01 00:52:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f77ea3b7-ad7c-3ecf-b519-928f4062f35b | -10.5588 | -48.019699 | 2024-10-01 00:52:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3572439-e896-31c0-9d32-3f5d11c96c21 | -10.5609 | -48.028801 | 2024-10-01 00:52:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e83c2aa5-91a8-3404-b98c-fd05f4de9f61 | -10.5631 | -48.037899 | 2024-10-01 00:52:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ca63bdc-53c5-3ff5-8bc5-d395562cbf23 | 2.11365 | -50.67775 | 2024-10-01 00:52:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ab22320d-04e6-3f16-ad75-62a2eaa7bb89 | -11.0018 | -50.188702 | 2024-10-01 00:52:01 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 109d96b9-81ff-3fb4-8df9-9a69e227b83a | -10.982 | -50.146999 | 2024-10-01 00:52:01 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| deb102cf-be49-381f-9724-02d44bf0085c | -10.9836 | -50.154301 | 2024-10-01 00:52:01 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a2313b0-2654-370c-8111-5ba98e8c289a | -11.0957 | -50.645802 | 2024-10-01 00:52:01 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f27abd9a-a1b7-363f-b99a-d06eb51261f6 | -10.9421 | -50.063301 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73321b4b-4bbc-3376-b6e6-0cc4212efe55 | -10.9438 | -50.070702 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61474055-cdfb-39d6-b0c9-b49480d9afdc | -10.9455 | -50.078098 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e67648d-e1a0-3117-a3b2-0490c0e0d336 | -10.9323 | -50.065601 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 220eae7f-88f8-3fed-bb1a-49015b308d99 | -10.934 | -50.073002 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9175e8cb-5302-3ad9-a050-fce0d368c9be | -10.9357 | -50.080399 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84844cfe-174e-3fa5-9c2f-6d109799ba36 | -10.9242 | -50.075298 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08340bdf-4731-347a-9c7d-0bfd574975bf | -10.9259 | -50.082699 | 2024-10-01 00:52:02 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README19.md)
