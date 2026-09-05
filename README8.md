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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 471ca615-4a87-3039-bf88-6377461c3e29 | -10.8051 | -60.745 | 2026-09-05 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 83cc5b3f-3ad7-3cef-80d8-e2964e095fd4 | -6.6698 | -59.9443 | 2026-09-05 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 204.1 |
| 4f32d4ca-e18f-34b2-9f88-3353df01ce0d | -10.7863 | -60.7461 | 2026-09-05 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b8e2cdb4-8bd9-3c79-82ea-11220eb98752 | -13.4264 | -43.8163 | 2026-09-05 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 51bacc27-64e7-376e-9585-6930334298c6 | -9.5343 | -40.3282 | 2026-09-05 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 2e7d5920-7de6-3fa3-b815-82b2a1911735 | -6.6513 | -59.9642 | 2026-09-05 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 2c87a2aa-22b0-3618-8193-9e7005583330 | -4.6853 | -55.6343 | 2026-09-05 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 0fab557d-d39b-319b-9357-c721d2b3b68f | -6.6699 | -59.9251 | 2026-09-05 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| dcd0244f-e1d0-3595-8cf2-847c1f2bec44 | -5.6565 | -60.2475 | 2026-09-05 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4ae5685f-d665-3c17-94cb-f4fb3d96ee49 | -9.5534 | -40.3254 | 2026-09-05 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 347.5 |
| a49126b2-284d-39c5-a2f8-622f856c00fb | -10.7676 | -60.7472 | 2026-09-05 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 74404fee-1715-3c36-9469-db40c7ba879f | -13.4458 | -43.8128 | 2026-09-05 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 282fd906-97d8-31c8-88a2-2d0e9d0c4182 | -9.5725 | -40.3227 | 2026-09-05 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 151.4 |
| 433b1d18-16f1-3421-952b-0d16ea5e48e2 | -13.4453 | -43.8366 | 2026-09-05 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 1ecb0738-d3e2-3c81-91db-54c2f53b02b6 | -6.6697 | -59.9635 | 2026-09-05 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 122.4 |
| c33576ea-e23e-3fc1-b76f-a3e0c32d8a62 | -10.7677 | -60.7279 | 2026-09-05 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| dc55b60e-bb8a-3cfd-804b-5cea395fee30 | -6.6515 | -59.9258 | 2026-09-05 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8f4b9008-7f57-3ae3-b1c6-7d7314198764 | -17.1078 | -56.8304 | 2026-09-05 01:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| d9037451-f8b7-3aec-a501-b1e5c5c95c37 | -6.0244 | -60.1781 | 2026-09-05 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 951eea02-fc54-325d-8ef8-fa7524415d50 | -9.553 | -40.3503 | 2026-09-05 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 2fbb7006-b3ad-3ae4-b324-aa429178aed0 | -15.0773 | -52.5183 | 2026-09-05 02:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c6329946-4e74-3475-899d-217ed5f8b98f | -10.7676 | -60.7472 | 2026-09-05 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f4a282df-d2f1-3846-96df-3c8d2e57b9d8 | -5.3646 | -56.0249 | 2026-09-05 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e061c8a8-c57f-3556-adca-3978a9a277d3 | -4.6669 | -55.635 | 2026-09-05 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 7ada3e26-95cd-36f5-9055-37abc4e17372 | -9.5725 | -40.3227 | 2026-09-05 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 185.4 |
| d7be1401-89eb-3766-bc68-d07711fb786f | -13.4458 | -43.8128 | 2026-09-05 02:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3e8150be-03da-345a-b59d-49e129415d4a | -13.4259 | -43.8401 | 2026-09-05 02:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 12f3d266-85e0-3774-90b6-ef062edd88ac | -10.7677 | -60.7279 | 2026-09-05 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 208.1 |
| 5d042e13-613a-3182-81aa-747194445927 | -10.7865 | -60.7268 | 2026-09-05 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 9ece3cf4-6f2c-3685-b20b-9639b44572ed | -5.346 | -56.0454 | 2026-09-05 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 88cc5106-a503-362f-b78f-51be6398ba47 | -4.6853 | -55.6343 | 2026-09-05 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| c7619f85-bec5-3ca8-9b4d-5047e12205d9 | -13.4453 | -43.8366 | 2026-09-05 02:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| e058fae7-0665-3ffc-be49-c00c8e62d774 | -17.1078 | -56.8304 | 2026-09-05 02:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 172cac48-af6c-3a51-8460-402bd132e484 | -5.3277 | -56.0263 | 2026-09-05 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 8d832c3e-1736-380e-b29f-a0ec1c3fe27a | -5.3462 | -56.0256 | 2026-09-05 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 8569e35a-31dc-3cd7-a2ce-f23d950eb2cc | -5.7756 | -45.0826 | 2026-09-05 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 183c6753-12cd-3482-a39a-effd043ef7a2 | -5.3094 | -56.0073 | 2026-09-05 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 223b05da-b17d-3c18-b3ac-1386899dc9fa | -5.6566 | -60.2284 | 2026-09-05 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7722cbed-5e01-3e79-9805-899930abd4a3 | -9.0798 | -65.4723 | 2026-09-05 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| cb214234-47d0-38e5-b7ac-3ebdf806723e | -5.6565 | -60.2475 | 2026-09-05 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f5baf283-ea3f-3be2-b417-9f92baf8324b | -9.5534 | -40.3254 | 2026-09-05 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 215.7 |
| e9153d99-dad4-30a4-be34-0f33a3ad4418 | -10.7863 | -60.7461 | 2026-09-05 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| bc6fe4dd-5f2b-3260-acc6-55987d82a341 | -13.4264 | -43.8163 | 2026-09-05 02:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 056cd23d-fd87-302b-bdce-6ae6bebbe101 | -5.7758 | -45.0599 | 2026-09-05 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 74f05046-c512-358c-a478-b45a43964c97 | -10.7676 | -60.7472 | 2026-09-05 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7179dfb3-9595-363a-8a3f-4883bba6bedf | -5.6382 | -60.2289 | 2026-09-05 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 0a2884ba-7975-3053-ae27-7725277ea850 | -17.1078 | -56.8304 | 2026-09-05 02:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 21480e22-04e5-3271-9e20-94c43ad13f97 | -13.4458 | -43.8128 | 2026-09-05 02:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 720d22fa-9c21-39c7-adbd-10b82baa7193 | -6.0244 | -60.1781 | 2026-09-05 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5d94e4ca-97f7-37f5-93f3-f423ba2b3d42 | -5.3093 | -56.0271 | 2026-09-05 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 17bb3075-36ea-3315-b4bc-29d8762b8bb8 | -5.1618 | -56.0525 | 2026-09-05 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 184b5ba8-507e-3462-8175-04d646a59496 | -10.7865 | -60.7268 | 2026-09-05 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 10c9f7f6-d825-3d06-a92c-0343a3b733b8 | -9.5725 | -40.3227 | 2026-09-05 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 9302f8dd-6d48-3a66-9058-6fb8fdd813ea | -6.6698 | -59.9443 | 2026-09-05 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 247.4 |
| 071deea0-d18b-3256-8496-41ac2c4bf37b | -10.7677 | -60.7279 | 2026-09-05 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 06fdd0c1-eefc-368d-8aa6-adfefa1b65fe | -15.0773 | -52.5183 | 2026-09-05 02:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| b5e09a79-9541-31fe-a94f-c123ff7d884f | -6.6699 | -59.9251 | 2026-09-05 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 44f42589-def2-393e-af59-2d6c591d9c34 | -13.4453 | -43.8366 | 2026-09-05 02:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| f28d430e-b052-37ca-a554-4bdf896a5ac2 | -6.6514 | -59.945 | 2026-09-05 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 178.2 |
| 512a9901-4f5e-3394-ae11-bcd2113e2ddf | -5.1802 | -56.0518 | 2026-09-05 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 699dbbef-2385-3b72-b37d-819a9ec1be8e | -5.6566 | -60.2284 | 2026-09-05 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 566bd5f6-28bb-3c08-9bfe-74f512f31df6 | -9.5538 | -40.3005 | 2026-09-05 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 09ac5c2e-3761-3ee5-9c4f-1bb93d008b50 | -13.4259 | -43.8401 | 2026-09-05 02:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 86fc7b75-7e9e-365c-9c6c-cb4fd30174c0 | -4.6669 | -55.635 | 2026-09-05 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 9dcb6b39-4d17-3eaf-a28d-e14b7ca6b086 | -5.3277 | -56.0263 | 2026-09-05 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 13010118-9002-350d-b46b-4c3bd8f88d80 | -5.346 | -56.0454 | 2026-09-05 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 3ce06075-4cb5-34f0-bb01-b15a5a7d55b5 | -10.7863 | -60.7461 | 2026-09-05 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 660b7fcc-0fb7-32e7-8783-a82d4c258c19 | -5.8402 | -60.2607 | 2026-09-05 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 18bf8844-de29-38be-ab95-8350de1f6ec6 | -6.6515 | -59.9258 | 2026-09-05 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| cb437edf-ac25-3eba-8296-c01d6ac25e77 | -9.5534 | -40.3254 | 2026-09-05 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 301.4 |
| 4bdf6d92-fac4-38e3-84ee-06918d21d6ae | -5.6565 | -60.2475 | 2026-09-05 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 32e7a090-74ad-3cab-8d56-a99b7649997b | -4.6853 | -55.6343 | 2026-09-05 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 7e46c46b-b4d9-3401-8570-c0d11d7c5ab3 | -5.7756 | -45.0826 | 2026-09-05 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 39a40e5e-23dd-30ee-a655-90be1082f786 | -6.6697 | -59.9635 | 2026-09-05 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 959a2cda-e483-39ff-9dd2-eabe973c0b17 | -6.6513 | -59.9642 | 2026-09-05 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.1 |
| ffc6ee64-9f5c-3622-ae82-00dca4c97e98 | -13.4264 | -43.8163 | 2026-09-05 02:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 15389ecc-1be7-30ba-bbae-a8ad140ece76 | -9.553 | -40.3503 | 2026-09-05 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 9cdc4103-a46f-347b-9534-86964d146102 | -5.3462 | -56.0256 | 2026-09-05 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 1f722b67-1336-3998-a5c3-d37adad40601 | -6.5963 | -59.9087 | 2026-09-05 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 55d5502f-e6d0-39a7-afab-fee346b1c305 | -6.6698 | -59.9443 | 2026-09-05 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 25a94cac-13a0-384e-b21f-843065db67ea | -6.6699 | -59.9251 | 2026-09-05 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| be8b77ce-8f54-32ac-a27a-fbce859c44d8 | -6.0244 | -60.1781 | 2026-09-05 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ed283939-d898-3ba2-880d-ba91cdb6c581 | -5.346 | -56.0454 | 2026-09-05 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| f1cceff1-3a6d-3011-91ad-9927cb5e0f45 | -6.6515 | -59.9258 | 2026-09-05 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 9903a5f2-3dcd-3b2e-8c27-dcf81f18d8ba | -5.6565 | -60.2475 | 2026-09-05 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c7f84686-33cb-3a8d-8d6f-48fd21e6a1fb | -4.6853 | -55.6343 | 2026-09-05 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1d121878-0356-3792-ac32-325dedc16983 | -5.3276 | -56.0461 | 2026-09-05 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 96899ebd-ac41-30d3-a7f9-674447cd5fbf | -4.6669 | -55.635 | 2026-09-05 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7f232820-b532-3871-8627-fa4ed26ab690 | -5.8402 | -60.2607 | 2026-09-05 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 18b21d00-55b1-3d0d-88f4-af9e0741abbd | -9.5534 | -40.3254 | 2026-09-05 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.2 |
| f66d7cc0-a2e6-3039-b343-fe57a2ce9c71 | -17.1078 | -56.8304 | 2026-09-05 02:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| f7e11165-e77b-3407-a1b2-c178e46df268 | -10.7865 | -60.7268 | 2026-09-05 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| fda5d6ee-37d4-33e4-ae14-7aac485b98e6 | -10.7677 | -60.7279 | 2026-09-05 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b5c59852-a526-30df-9bf9-502d986f4f47 | -5.6566 | -60.2284 | 2026-09-05 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 695e00ad-a6a4-3570-adc1-461b26651fed | -5.9197 | -47.8927 | 2026-09-05 02:20:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b19c8101-95ec-3c45-bf33-58cdffa5bab3 | -13.4264 | -43.8163 | 2026-09-05 02:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 2c86e3b9-8a0d-3972-b559-c0cd5efd2db8 | -6.6513 | -59.9642 | 2026-09-05 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 7364d9eb-23bc-3f09-894a-9fbfa0d38fec | -13.4458 | -43.8128 | 2026-09-05 02:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 8e68788b-3c6c-3617-b2cc-59aa53049945 | -5.3094 | -56.0073 | 2026-09-05 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a8b6759b-1a58-385b-8d28-0af4d4f31237 | -5.1802 | -56.0518 | 2026-09-05 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |


[Clique aqui para ver as próximas entradas](README9.md)
