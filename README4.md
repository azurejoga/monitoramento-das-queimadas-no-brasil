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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35c805a6-2717-3f78-bdb0-e269502742ce | -10.5961 | -53.956001 | 2026-10-04 00:09:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f05e1f6-361e-372b-bb94-0df61d49b958 | -5.5258 | -44.944599 | 2026-10-04 00:09:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1f49a2b-84b1-3c42-952c-c864c5b2618d | -4.8146 | -49.8703 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8cb3b4e-146d-311c-88e2-418c32711ccd | -4.5408 | -55.953602 | 2026-10-04 00:09:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 057fcec4-a394-32ae-b4e4-12651491fbdd | -4.2667 | -50.7309 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f998d65-bc0d-357f-92ad-bad844d43131 | -2.8199 | -54.108299 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99bec0ea-adc0-37c2-9753-e23e27eff72a | -3.1085 | -53.742901 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 549a8ec8-a0c8-3d4b-ae08-c56269aab74c | -4.4885 | -45.530701 | 2026-10-04 00:09:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5744fa14-f209-338a-be36-aeb6681deb25 | -3.0411 | -54.224499 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dca90e1-a0c5-3d04-95ba-1d0b8d2ddb94 | -1.012 | -48.786098 | 2026-10-04 00:09:00 | METOP-B | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3b1c929-99dc-37bf-b944-b34dde210a18 | -3.4661 | -50.106602 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 011350d6-199a-32a0-beaf-dc6a5a7c5ae2 | -2.4362 | -49.021099 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af7daf26-b219-3506-9792-45c74a45533b | -1.0995 | -54.097401 | 2026-10-04 00:09:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98e7f8c7-108f-3fcd-af8e-f78a7d554980 | -3.5143 | -54.597401 | 2026-10-04 00:09:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cf20fe1-3c3e-3f3d-b271-f43452a6a32b | -2.9198 | -54.0956 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b77e61e-9f29-38b1-8097-e540d0cbd34e | -4.133 | -54.145302 | 2026-10-04 00:09:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea3d8f27-8104-37d6-b62e-2755e3720c82 | -3.0016 | -53.862999 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7175e966-5cb1-332c-a222-dca0f5a536d3 | -3.5066 | -54.608898 | 2026-10-04 00:09:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 454ceb01-0903-3a89-8d02-57996e663c33 | -5.9909 | -53.630299 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8816ae47-27b4-306b-b3c1-c61235421755 | -3.3032 | -53.8325 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30d64b78-0033-3780-879b-9f8c9ac85442 | -2.9452 | -54.117199 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8714f9b3-7d44-3759-a78e-d12d3bdd96fe | -3.8772 | -49.691399 | 2026-10-04 00:09:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 586db437-2e7a-3a4c-a00e-bad383aa9cfc | -3.8642 | -55.809601 | 2026-10-04 00:09:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f70dcfb-22b4-3a2f-bf27-3ea499e4cfbc | -3.7018 | -50.648102 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81bce3a2-eed2-380a-ae5f-709a8dd9e60b | -2.9061 | -54.080399 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c27c9e3c-2042-392f-9afb-1975fa441ed5 | -4.4659 | -50.975498 | 2026-10-04 00:09:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62912475-9c74-37f5-8aa5-cfbf07a86517 | -2.955 | -54.115002 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba058573-b9fe-3ea9-979e-390abb4b2a6a | -2.961 | -54.0956 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d38774de-43bb-3219-9647-9b76465d5800 | -14.5771 | -52.868698 | 2026-10-04 00:09:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e2761c5-3b55-3b35-8a25-d653f7d3f017 | -2.9177 | -54.132301 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c15313a8-f3de-343b-a673-8eace88d24e7 | -2.6962 | -49.030701 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f279a7f-314e-34d4-807f-d5272592aaa1 | -4.2567 | -46.351002 | 2026-10-04 00:09:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a239932a-b0f7-38a2-948f-9efcc4fd835e | -3.2714 | -50.020901 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8660f2c-2e59-3fd4-9cf0-b22bde5868b0 | -2.8294 | -54.197201 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e27c06ef-4a78-3bf5-a083-c26b3cd1cfe9 | -6.0698 | -53.474499 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66685742-8ee7-3594-88a9-a3457cd18290 | -3.7761 | -51.390301 | 2026-10-04 00:09:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 595687c6-0616-3eeb-acc7-199f871cfcbe | -4.2579 | -50.783199 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c51bcf1e-9821-3db8-8bc6-b4945de412c8 | -5.5283 | -44.955101 | 2026-10-04 00:09:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15ffeadd-2dde-31f4-ada0-51785eb2e84a | -2.5866 | -51.873501 | 2026-10-04 00:09:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc1364a0-0623-3f87-b1f9-5d0aee8a8afa | -5.9622 | -55.336399 | 2026-10-04 00:09:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17cfd5fc-97bb-3215-9d33-766125db7fde | -3.1745 | -54.0853 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13b5eda5-1063-33c3-83df-e1febed785fc | -4.0156 | -44.828499 | 2026-10-04 00:09:00 | METOP-B | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3ec245f-927b-34e6-86fd-99679f6d51ab | -5.7354 | -45.134602 | 2026-10-04 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38aa2918-585f-3baf-a526-3398c6e0a507 | -3.1514 | -53.0597 | 2026-10-04 00:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67993d15-58a2-3f63-bfd6-411f7e49bfe2 | -5.9988 | -53.619301 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8227e166-7e44-3ca9-b674-49fae1aa0b4d | -3.1047 | -53.726299 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| add982a6-0679-37f5-8e4b-e889f72b35ad | -5.4857 | -49.2369 | 2026-10-04 00:09:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51acc199-9e6a-3afd-ad07-d9242f1f6d16 | -3.0791 | -49.536201 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06706f5f-3653-33eb-bfc0-b59b0fb2ad21 | -4.2035 | -53.442799 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e354da3-9d8f-3ddd-8c6f-90efe8e3bf64 | -2.9492 | -54.0891 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30409f86-105a-3b2a-99e7-c4fa904ec546 | -4.2863 | -49.7225 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5de64dfc-df49-37b9-9003-725dce1e990b | -3.1206 | -53.705399 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a17f5ed0-1885-3c48-91fa-b2a616f7734e | -1.4857 | -49.465401 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd71cfd5-8dbd-3254-b08c-b7bc9135eca1 | -6.2093 | -52.799599 | 2026-10-04 00:09:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95259eeb-5912-31b1-a4d7-bd3c8b1ea866 | -1.9278 | -54.349098 | 2026-10-04 00:09:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae564166-a0a7-33a9-8c1d-9ac63a660b37 | -0.4692 | -52.0345 | 2026-10-04 00:09:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d1a11a09-7bf0-3913-b757-453f8c016709 | -2.987 | -51.043499 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24be9ee1-d6e4-33a9-89af-8c58c5f2bd74 | -2.6826 | -54.414398 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cae39708-3df0-36c7-9051-d6a01513186f | -2.6898 | -54.631199 | 2026-10-04 00:09:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7efe341b-4f21-310f-bac5-aa6e4403ce0d | -2.9786 | -54.082699 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a06271d9-55f7-3ff1-8adb-9be2c2f854e4 | -1.4907 | -49.442101 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10525aee-de24-3055-b6be-acebab69aef5 | -2.8904 | -54.102001 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f87c52a3-a430-39fb-8f7c-cdff4a813591 | -2.8022 | -54.1213 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 918dc896-9368-391b-8828-4ec1cd9e8473 | -3.0909 | -51.0924 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bb54d31-40cc-3b1f-844d-aa1b0b791717 | -7.7465 | -49.205399 | 2026-10-04 00:09:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 60916913-a039-3f2f-85fa-250f0d67de3f | -2.0507 | -56.872299 | 2026-10-04 00:09:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd88124d-7ba9-3061-aff3-2880ffb9535a | -3.2761 | -53.803001 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fabc9731-9ec9-35c1-b8d3-79261d9ec4bb | -2.8297 | -54.106201 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd9b94a-9a01-398b-bbb9-98046cd6510e | -3.0549 | -54.147999 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a32cef7-7434-3c99-ba6b-f176872f27fa | -3.4615 | -50.086201 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b831400-7114-37e0-a766-ba27e46fc39d | -4.9171 | -45.689499 | 2026-10-04 00:09:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2c32ae03-3d45-3a0e-bffd-75e967e82e50 | -4.249 | -46.362202 | 2026-10-04 00:09:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4bf3aa9-1146-3db1-8b74-4e4af4cd5204 | -8.5349 | -50.0569 | 2026-10-04 00:09:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 936d1833-88c2-352f-b73c-1819cb517f0e | -6.1743 | -49.3643 | 2026-10-04 00:09:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0539b499-a8b5-3806-a131-26814a0d7a16 | -3.1872 | -57.8927 | 2026-10-04 00:09:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad2f4f52-e22b-378a-b44c-b399cb1d4886 | -1.0938 | -49.192299 | 2026-10-04 00:09:00 | METOP-B | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2af83dae-e151-36fa-b3f9-17dd9f0dfea0 | -3.0112 | -50.465401 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65290dc5-6ea1-3872-b3dc-72fc3ccfaffa | -6.0029 | -53.544201 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9587c7cf-b7ac-347d-8600-45c8e0a32717 | -4.5069 | -45.875 | 2026-10-04 00:09:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af8954c9-2e6b-3c33-a820-2ab52e33bacd | -4.9269 | -45.687199 | 2026-10-04 00:09:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b3a461ce-6438-3f20-ade4-3980dd7ffc28 | -5.0716 | -45.1604 | 2026-10-04 00:09:00 | METOP-B | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 890645b3-0ace-3daf-b1c2-da77f9a9f760 | -6.0659 | -53.457001 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9d15571-f681-34cb-8978-535598c433ca | -2.8845 | -54.121399 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fbeba1c-fb59-3351-bb03-bbf9f0d52078 | -2.8101 | -54.1105 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97822fd9-0f3d-3d8b-a2dc-2acacfb25136 | -3.18 | -50.528 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1828974-92cf-3bf1-baa3-5ebb8e442766 | -3.4697 | -50.077099 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd9171c0-1a50-3209-b1e8-3937a5ba5460 | -4.106 | -49.064301 | 2026-10-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9f0d4ac-e305-38ca-9634-7f0c23c10b0b | -4.1232 | -54.147499 | 2026-10-04 00:09:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 263ae8b3-c06f-3945-a5bf-9e64a18b7145 | -4.2682 | -50.737701 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99994d0e-48f6-3c98-b3a8-0feaac66c9cb | -9.0991 | -49.7701 | 2026-10-04 00:09:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b32fc14b-a275-3189-99b9-90f9f85fd0a2 | -6.1959 | -52.7855 | 2026-10-04 00:09:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0130151-24c4-315a-8a25-e39b68d42c50 | -2.8943 | -54.119301 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e5db753-3491-3e1c-8515-924b256e681a | -5.9971 | -53.517799 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2da4345e-fec0-333e-80cb-e7270884dfa2 | -3.0127 | -50.472198 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3edd0f7c-9a9c-3bc8-83ec-3fc69131c1bd | -3.1815 | -50.534801 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeae8fb2-d425-3003-aa2b-467cd94f65fc | -2.7945 | -54.0868 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1eb1501-9a0a-32e0-aa83-f05476795575 | -2.5902 | -51.843201 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb65841c-6aa0-3cd4-9e2c-cc870b2f6e92 | -2.2498 | -51.933201 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbaa55b4-b2e8-34d2-863b-2cb9b1c63fc7 | -4.813 | -49.271702 | 2026-10-04 00:09:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dcc335e-9afc-3605-b2eb-82d46c6b7aaa | -6.0186 | -53.5224 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
