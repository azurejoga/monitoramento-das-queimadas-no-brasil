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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1c4bbfa-1ae5-39cc-b3aa-fcc6e2dca506 | -11.0901 | -54.7852 | 2025-05-21 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 42599cb8-04d7-3537-a7ef-9b25f5794b86 | -6.2226 | -43.3459 | 2025-05-21 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 1cef49ee-67e4-3413-a849-a8da8f57987d | -11.0712 | -54.7868 | 2025-05-21 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 251b0b4f-9b15-361c-ba52-49a68568a190 | -12.2946 | -52.4785 | 2025-05-21 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| a796c363-3a70-3307-889a-ea53653cbd92 | -12.2943 | -52.4995 | 2025-05-21 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a625f780-f9d7-35b7-8c29-2679d9f005d2 | -20.9601 | -56.5967 | 2025-05-21 01:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 65.1 |
| bbad1ec6-5e9f-3496-ab43-34c22c97c41c | -11.7988 | -44.2733 | 2025-05-21 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 27d2cb5f-fc6a-35c7-ba13-19e6d62c90b6 | -11.0903 | -54.7648 | 2025-05-21 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d1581f21-20e0-3bc6-854e-a91ef898b18a | -6.2224 | -43.3693 | 2025-05-21 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ba2b55ce-0d44-3a9c-baae-47cf5c2808f9 | -6.2411 | -43.3677 | 2025-05-21 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 4af26c48-8aa6-364f-91d5-a88a6c345449 | -11.0901 | -54.7852 | 2025-05-21 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 45be7111-e1b3-3d88-91b2-e42c797da169 | -11.0712 | -54.7868 | 2025-05-21 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 31e70b6d-307d-394e-bfff-6f80e1933e3a | -12.2943 | -52.4995 | 2025-05-21 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 41f85fa5-8a2d-3af8-90f0-d8af04b6194e | -6.2224 | -43.3693 | 2025-05-21 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6a1129fc-c492-3e68-9a29-4492e3a72e0c | -11.0714 | -54.7664 | 2025-05-21 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 19a9cd10-9b9d-31d5-967d-bd04cc74ae10 | -6.2414 | -43.3444 | 2025-05-21 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 96cfe18e-49e7-3fc5-991a-0d4b1383906c | -6.2226 | -43.3459 | 2025-05-21 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 2b0897f3-1912-3dd7-bac9-591bef8d292f | -12.2946 | -52.4785 | 2025-05-21 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| ee77da2f-8947-3980-aa54-d37d2bd3047c | -11.0903 | -54.7648 | 2025-05-21 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 9d1bab41-0a14-3d09-8406-f397d8f695b5 | -12.424 | -43.7274 | 2025-05-21 02:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| ac0fba8e-a627-375c-adc1-f974112b63b3 | -11.0901 | -54.7852 | 2025-05-21 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 967bd60b-1039-3ae3-9a7f-17e1616686d8 | -15.1943 | -49.3862 | 2025-05-21 02:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 9a85d85b-ef2d-3074-a0ea-e2daee8aad14 | -12.2946 | -52.4785 | 2025-05-21 02:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 6863c993-79b9-34fd-98f6-ff19ac0c0dd9 | -11.0712 | -54.7868 | 2025-05-21 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f88d0b7d-b4e8-34e7-8d96-a3acda29cfa1 | -11.0903 | -54.7648 | 2025-05-21 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 35b6e107-efe5-3ebc-baab-5694257245ab | -6.2411 | -43.3677 | 2025-05-21 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| df6c0087-7ae6-3c9e-ba1e-3d9377496025 | -6.2226 | -43.3459 | 2025-05-21 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 00adff29-e5c6-3b89-bf18-530a1ba3b308 | -9.0291 | -47.7452 | 2025-05-21 02:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 4d739634-da56-360d-a43c-c1b451a37673 | -12.2943 | -52.4995 | 2025-05-21 02:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2379ab08-063c-34c7-b0e8-084831f7d324 | -6.2414 | -43.3444 | 2025-05-21 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2e54ba22-03e6-30a4-b895-9b58ab4fdde9 | -15.1939 | -49.4083 | 2025-05-21 02:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b4cc6d48-9c7f-3c6d-8ddf-be1a22df706e | -11.0714 | -54.7664 | 2025-05-21 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 49aea502-3cdd-3aa5-a585-0a7abe02dee6 | -6.2224 | -43.3693 | 2025-05-21 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 9a818b5c-daf5-3332-a560-ca05471cac26 | -12.2946 | -52.4785 | 2025-05-21 02:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| ffba2a77-acde-3306-bf47-a63350ed0456 | -11.0903 | -54.7648 | 2025-05-21 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 079df412-0582-373d-8c2b-6e617a37e881 | -12.2943 | -52.4995 | 2025-05-21 02:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 92968082-badd-3b4b-bf97-f5e863e62982 | -11.0714 | -54.7664 | 2025-05-21 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 8f59dafd-0382-3124-8303-f8d9b4733192 | -11.0901 | -54.7852 | 2025-05-21 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b7e2e3bc-3976-3b77-b574-b8c9ee6c8864 | -6.2226 | -43.3459 | 2025-05-21 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| d09f2cdc-47ce-3506-a1d9-982c0acee53a | -11.0712 | -54.7868 | 2025-05-21 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 37a42896-0148-3134-8ea4-6a224e7865db | -11.0712 | -54.7868 | 2025-05-21 02:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 3da67592-a5f3-3290-8052-12cd494d662b | -11.0903 | -54.7648 | 2025-05-21 02:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f772dc88-fd14-32b7-b5b0-a7827d708444 | -12.2943 | -52.4995 | 2025-05-21 02:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 21f20ddd-271e-3610-a876-ace25310bd7c | -11.0901 | -54.7852 | 2025-05-21 02:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e34ba680-2476-3f36-93bf-ac91e0043087 | -12.2946 | -52.4785 | 2025-05-21 02:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 39d3cdc9-b386-384e-9548-84510fe3bf4f | -11.0714 | -54.7664 | 2025-05-21 02:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 48ab93bd-22db-38b9-b766-77f5e045c252 | -11.0712 | -54.7868 | 2025-05-21 02:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 97e8e4cd-7bd0-3ab1-8792-886d31af95b4 | -15.1939 | -49.4083 | 2025-05-21 02:40:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 40.6 |
| fd339223-ea7b-3195-ad70-c2c6d20a4a1f | -12.2943 | -52.4995 | 2025-05-21 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8dfb52a3-cc4a-3ef5-b916-f73e320a13eb | -11.0901 | -54.7852 | 2025-05-21 02:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 62f832bf-a247-3489-8d41-7fa10d735868 | -11.818 | -44.2703 | 2025-05-21 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 0faaed2d-ca71-3ed0-a449-d9c0419d7112 | -9.0291 | -47.7452 | 2025-05-21 02:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| a1334649-1fda-375f-93b5-b2002e6aeb54 | -12.2946 | -52.4785 | 2025-05-21 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 578eef88-260c-344e-914d-f9f43a597930 | -12.2943 | -52.4995 | 2025-05-21 02:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 8d0b9883-e5fb-3cf7-9bce-10daa19900b0 | -11.0901 | -54.7852 | 2025-05-21 02:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| fa0a11c2-88fd-3e3a-8593-02b23239a950 | -15.2134 | -49.4052 | 2025-05-21 02:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| d5987c93-8dba-3f4a-b2f7-cab65cbb8124 | -11.0712 | -54.7868 | 2025-05-21 02:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 59cc0161-79fd-30e4-b34f-7eb306fb0f6d | -12.2946 | -52.4785 | 2025-05-21 02:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 090d38e6-2a9b-39ed-b54f-a57fd528741b | -15.1939 | -49.4083 | 2025-05-21 02:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 101.0 |
| eaed994c-e633-3ebc-9409-3aeff3ef45f8 | -11.0714 | -54.7664 | 2025-05-21 02:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a8b83ce8-cc0e-3efe-80ad-c9f53358218d | -12.2943 | -52.4995 | 2025-05-21 03:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| e913b948-2e21-3614-a5a6-d5fbf1483166 | -11.0903 | -54.7648 | 2025-05-21 03:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| c5d9d7d3-1c4e-37ba-8ea7-bf943e986c5a | -12.2946 | -52.4785 | 2025-05-21 03:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| d2a7dd27-c423-31ba-927a-4c9da504049a | -11.0712 | -54.7868 | 2025-05-21 03:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 91ffbe81-db9a-3288-a9bd-093350133e9e | -11.0901 | -54.7852 | 2025-05-21 03:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 61c7a922-1bfa-3a2b-a852-b69fd0147eff | -11.0903 | -54.7648 | 2025-05-21 03:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| e28692cf-db27-31f4-9643-082571199609 | -11.0901 | -54.7852 | 2025-05-21 03:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c76dae91-80e0-391f-893d-a67bdfc6c138 | -12.2946 | -52.4785 | 2025-05-21 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 3396e988-4791-33d1-ae9c-41710fa3544d | -11.0712 | -54.7868 | 2025-05-21 03:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 521ee74c-eeb6-3bb1-ae46-a30662f466bf | -12.2943 | -52.4995 | 2025-05-21 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 4ce3772e-4f30-38b0-a4fd-85eb79b15021 | -12.2946 | -52.4785 | 2025-05-21 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 060672a3-8830-39fa-a950-df727082d151 | -11.0712 | -54.7868 | 2025-05-21 03:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 1b2c72e9-c372-3123-a96d-08b91f95d722 | -11.0901 | -54.7852 | 2025-05-21 03:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| e8ec388a-69a8-3dc1-8fa0-f3e477bfb4af | -11.0714 | -54.7664 | 2025-05-21 03:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| b069e3af-3dc3-3fc3-b9d8-f1427d8bfcbc | -12.2943 | -52.4995 | 2025-05-21 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f9415da8-dea1-3d15-9b57-b4a1db2c60a1 | -12.4297 | -43.72981 | 2025-05-21 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f5856c60-b2af-3d71-9956-ec2556d22bc4 | -14.15482 | -45.48215 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96c8ff8b-d098-3952-8ba9-a8ce627c8e29 | -11.8131 | -44.28055 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1672b53f-0448-3527-8da8-e9a4e1642de8 | -17.75612 | -42.89637 | 2025-05-21 03:23:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a43212ed-568b-3394-b2b4-de06ca025ee4 | -12.43388 | -43.72702 | 2025-05-21 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 47bb5339-b087-3265-a9d8-e63522a56aed | -11.78625 | -44.28403 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3bf1ef9c-c76b-3b21-9177-3c68b29403af | -14.15083 | -45.46834 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35ef36a0-423f-3259-a8aa-05ee613ca5a9 | -14.15616 | -45.47601 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19b5d4da-6f30-36cd-9d7d-75dad10820a7 | -11.80155 | -44.27546 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8b325c50-44ca-3189-b640-edc89a1ee4e7 | -14.15751 | -45.46986 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b2894b6-578d-3e17-bd7a-77f1d444dba3 | -11.78588 | -44.28078 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2b9b6aac-cc65-3e7f-99c7-f98fe95322f0 | -14.15274 | -45.47966 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 177ea161-fa3c-3b85-9d24-045e93c9db09 | -12.42768 | -43.7256 | 2025-05-21 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e18b89b6-c835-36a1-9676-c803f0f68a0c | -12.86979 | -43.18108 | 2025-05-21 03:23:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aeb6fbb3-ccf6-3452-ada9-332760951068 | -14.04837 | -45.50793 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 658a7b36-c78b-3319-a7e6-e94c0d84b3f1 | -14.16817 | -45.48523 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd13d8e5-d4e8-386e-aee3-46294d663890 | -14.04706 | -45.51391 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| acac811f-f2ac-3d20-b006-507c10032ea7 | -14.16284 | -45.47754 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 701a747d-f92c-33ae-9d06-cc0b97c752bb | -11.81192 | -44.28622 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27e2ca1d-1530-3263-8147-79fdb09198b2 | -14.15404 | -45.47351 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8fb20d0d-823e-3c30-ad9d-6ec7794df7b7 | -16.04299 | -43.80723 | 2025-05-21 03:23:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4de522e0-3230-3950-a97b-a11d2b1d72d3 | -12.43072 | -43.72472 | 2025-05-21 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eeee6d53-0d31-3c67-a20a-440d8d1e2a74 | -11.7847 | -44.28642 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 30449101-7332-3860-8c23-e92e222b4bc0 | -14.16952 | -45.47905 | 2025-05-21 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cacb5d9d-32f2-3bbc-950b-4ccbe6c7b6fe | -11.81342 | -44.28391 | 2025-05-21 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README6.md)
