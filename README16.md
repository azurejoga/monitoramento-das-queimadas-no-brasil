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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6726d2d6-362f-37d2-80d6-a3137acab3f3 | -18.2624 | -55.989799 | 2024-10-26 01:26:45 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f06618aa-3390-3932-b170-1eca29ae0c82 | -18.264 | -55.997002 | 2024-10-26 01:26:45 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6b73dc77-5d19-3205-a46e-30104434df78 | -18.265699 | -56.0042 | 2024-10-26 01:26:45 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bb456489-1aa4-3f2d-a999-d0a112f338fd | -18.2673 | -56.011398 | 2024-10-26 01:26:45 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dd1c87e0-a8ae-3569-92dc-8b8046f3aeea | -18.2542 | -55.999401 | 2024-10-26 01:26:45 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9165770c-66ed-34e3-9284-6b7b6194ff77 | -18.255899 | -56.006599 | 2024-10-26 01:26:45 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aec1b80e-6379-3e38-a53a-85deb96c5e00 | -18.2575 | -56.013802 | 2024-10-26 01:26:45 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 30dbed37-adb8-359d-87ad-0653cad50a13 | -18.0629 | -57.3721 | 2024-10-26 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.2 |
| b66e409b-0aea-3f56-8bf3-748b78685224 | -18.065 | -57.2481 | 2024-10-26 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.7 |
| c0b30bdd-a9a7-3a1f-8431-c1b76dc4735b | -18.0653 | -57.2274 | 2024-10-26 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| a06cb4ed-6aa3-3e1d-b750-283fd9ef7c3d | -18.0827 | -57.3696 | 2024-10-26 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.1 |
| f71594dc-2742-32c7-8a55-8dd720ac3dd8 | -18.0847 | -57.2456 | 2024-10-26 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.2 |
| 7bef5773-4b72-3ae9-ad1d-12027700ede1 | -18.0851 | -57.2249 | 2024-10-26 01:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| a5083d45-72b5-3a7b-b44f-86fabc3afbab | -18.245 | -56.0002 | 2024-10-26 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.7 |
| 73edc87d-302f-31cd-91b2-a3eb7c94a322 | -18.2645 | -56.0184 | 2024-10-26 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.0 |
| fabfe8fe-e920-3bf3-b83c-54d49768344f | -18.2649 | -55.9975 | 2024-10-26 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 721fa5aa-6971-32bd-85bd-7e67cfa8b5c1 | -18.214199 | -56.606998 | 2024-10-26 01:26:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 224ed468-92e7-38d3-bf0f-beac02458b7a | -18.212299 | -56.645302 | 2024-10-26 01:26:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0175427f-78aa-359f-aacf-3cb903c83ee0 | -18.202499 | -56.647701 | 2024-10-26 01:26:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8f5157d7-d0c4-3c84-96f5-ef5d95ffe85b | -16.172899 | -48.7663 | 2024-10-26 01:26:50 | METOP-C | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 550df8f0-0348-3cb4-9edb-7da5648ca40f | -18.099701 | -57.258801 | 2024-10-26 01:26:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 90373c56-c135-346c-a7bd-72bb905aabe6 | -18.083599 | -57.231899 | 2024-10-26 01:26:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bcaa3b9f-39a3-35b9-9b7a-178ac8d68e58 | -18.070601 | -57.219601 | 2024-10-26 01:26:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 91303866-4f00-3e6f-a981-c8dad1fdca5d | -18.072201 | -57.226898 | 2024-10-26 01:26:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 18b82292-72fe-3699-9ead-872f1b4974e1 | -18.073799 | -57.2342 | 2024-10-26 01:26:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e57b0d30-6cd3-3dd3-88e1-6b0f6fcc701b | -18.075399 | -57.241501 | 2024-10-26 01:26:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 16c952d2-41bc-3da3-be65-c49d10b676d4 | -18.060801 | -57.221901 | 2024-10-26 01:26:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| be79d090-69d6-394a-9f85-91e0eccc3073 | -18.062401 | -57.229198 | 2024-10-26 01:26:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8db5bdb8-cc56-312e-ad0d-037ec37b5563 | -18.063999 | -57.2365 | 2024-10-26 01:26:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6f2383f5-f3cb-3260-aae3-c4aeb2b09f11 | -18.042801 | -57.233799 | 2024-10-26 01:26:53 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1a789836-9085-3bf7-8ef6-8c068b84798e | -18.044399 | -57.2411 | 2024-10-26 01:26:53 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7d6be77c-3f81-3c45-8288-935580934e42 | -18.069799 | -57.3582 | 2024-10-26 01:26:53 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1ea7c8e2-d561-3262-9e76-bd68c6eab58e | -18.0714 | -57.365501 | 2024-10-26 01:26:53 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 831466e5-1cc7-3fae-a2e8-8daeba095aa1 | -18.073 | -57.372799 | 2024-10-26 01:26:53 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 59c9ab0c-f0fc-35d7-94b9-88c74b13f066 | -18.060101 | -57.360401 | 2024-10-26 01:26:53 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1c1bdea6-36b5-34f0-906e-fb3f8488c080 | -18.061701 | -57.367699 | 2024-10-26 01:26:53 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 896c1f14-d4b4-38a7-b59c-a3f96ea6030f | -18.063299 | -57.375099 | 2024-10-26 01:26:53 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fae4254a-8a16-3d2c-b4c5-db45df6abca2 | -18.022699 | -57.330601 | 2024-10-26 01:26:53 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3415af29-b4db-3336-a2d0-29b7fa0698c0 | -18.0243 | -57.337898 | 2024-10-26 01:26:53 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 277e2604-11a2-32d8-97c4-93ddfc0ce236 | -19.5067 | -56.6829 | 2024-10-26 01:26:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.0 |
| da966bf0-34ad-3d76-b835-5f9c73bbe7b1 | -19.5264 | -56.7011 | 2024-10-26 01:26:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.2 |
| d83bd19e-d917-3509-8e5f-47f6cb0331f8 | -19.5465 | -56.6983 | 2024-10-26 01:26:54 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 72af4dd1-e229-323b-8a87-f462f76c8993 | -19.6256 | -56.7499 | 2024-10-26 01:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 47.6 |
| 62706c9f-c954-3704-b2c5-08d92a2ab284 | -17.932199 | -57.529202 | 2024-10-26 01:26:55 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1397f213-7a03-3405-b69d-3162e2048833 | -17.933701 | -57.536499 | 2024-10-26 01:26:55 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 255b2438-069c-3cb2-a1c3-69c7c6d29c78 | -17.935301 | -57.5439 | 2024-10-26 01:26:55 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 905f5689-e978-33f9-a3bd-f7e46e94a2a7 | -17.936899 | -57.5513 | 2024-10-26 01:26:55 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7720574f-1352-38df-9c0f-5d73f4a2b5fd | -17.938499 | -57.558701 | 2024-10-26 01:26:55 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 85580fb6-4656-388e-8cc7-48d08eee2015 | -17.9401 | -57.566002 | 2024-10-26 01:26:55 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fe8fe5c9-3989-3a7f-b0e3-d9fc0810609d | -17.050699 | -53.436501 | 2024-10-26 01:26:55 | METOP-C | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 068df99f-9870-32cb-a98b-19af3032f4fb | -17.0527 | -53.445 | 2024-10-26 01:26:55 | METOP-C | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f90a9956-02c5-3e9f-a914-580739063212 | -17.054701 | -53.4534 | 2024-10-26 01:26:55 | METOP-C | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b49e262-ad19-3f12-980e-34fda298467a | -17.0567 | -53.4618 | 2024-10-26 01:26:55 | METOP-C | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e30bc3e0-6e55-391c-875d-284efb579b4e | -17.042999 | -53.447498 | 2024-10-26 01:26:55 | METOP-C | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 598a7430-c976-34c0-a311-bdaa0e4ca00d | -17.045 | -53.455898 | 2024-10-26 01:26:55 | METOP-C | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 72c1972a-6989-3e46-b0e1-0e9d0c9c6d98 | -17.047001 | -53.464298 | 2024-10-26 01:26:55 | METOP-C | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7251af4-388b-30a2-af06-89b10a34878c | -17.9224 | -57.531502 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dfc61404-4e5c-3939-a1f0-3ce0ff0fd1e3 | -17.923901 | -57.538799 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 851e715f-3f38-346c-9571-39b9c0eef620 | -17.925501 | -57.5462 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 73cb924f-b80d-3838-a569-99c2f849b2ad | -17.927099 | -57.5536 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3cf93b00-2c96-382c-a3f5-9322f6720da0 | -17.928699 | -57.561001 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d589b5f6-8503-3afa-bf47-a1cb8bf199dc | -17.9303 | -57.568298 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b0dfef12-6ec3-3e5d-a9e4-c9877573eaee | -17.910999 | -57.526402 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0528e85d-3bac-30d6-8299-561b28831b33 | -17.9126 | -57.533798 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b204f3d0-cc45-3416-9a66-edb5f0e4a495 | -17.917299 | -57.555901 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dde5d307-1b0d-3d03-9753-6b969e873609 | -17.9189 | -57.563202 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 70305b02-0ae0-3e8f-ad1e-49dfb8c3f37f | -17.8899 | -57.523499 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 73cb056b-3d81-3238-a044-badea1db2526 | -17.8962 | -57.553001 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8cf94b0e-29d1-369f-b3bc-fc4dd3bc9f57 | -17.8978 | -57.560398 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1cbde603-95ce-3794-938a-ef097fbdde26 | -17.8769 | -57.511101 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9f9853f5-1eb4-37d5-87da-da534b666ed1 | -17.8785 | -57.518501 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ff6c3ea4-3e6a-3b5b-963e-2ae76bc67319 | -17.8864 | -57.555302 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6dc2fcf5-8776-3ca4-b79a-067f6320c217 | -17.888 | -57.562698 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aa569f05-9fd6-3ddf-a660-c179ef35d9e2 | -17.889601 | -57.57 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 42af2ea4-f6b2-3ab4-9798-1a0638c58da8 | -17.8671 | -57.513302 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 07ec3eb4-1e58-312d-b201-121ee122b583 | -17.8687 | -57.520699 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d976b98b-e9ba-33a8-89b4-50c70073c510 | -17.8703 | -57.528 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a399f1ee-0d49-389e-aac6-9316cd3468d2 | -17.8766 | -57.557499 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 564bf249-0513-3ecd-84c1-46f3364a8948 | -17.878201 | -57.564899 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7cd5f1df-39ab-34a5-87f0-3b3c71af88d6 | -17.879801 | -57.572201 | 2024-10-26 01:26:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 09cf925b-d57d-318e-96ce-1b7cf4374645 | -17.8248 | -57.507702 | 2024-10-26 01:26:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a29e45c6-5152-3908-8638-baf5acab1b38 | -17.8605 | -57.5303 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eed895ab-7323-3cfa-969a-4efdbf96f76c | -17.868401 | -57.5672 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cd3e2e96-026a-3ac7-93b2-78d83462dad6 | -17.870001 | -57.574501 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f06eec05-7c35-3690-b257-d03cb1b7a791 | -17.871599 | -57.581902 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 96a7a9fa-27f5-3d01-ad20-d65f57aed226 | -17.858601 | -57.5695 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f2677a1e-aaba-3630-95c2-1aa99c85483c | -17.860201 | -57.576801 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 60256710-94c0-3888-8c08-f58edcbe9f65 | -17.842501 | -57.542301 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0fce8091-9b81-3f34-adbe-e477bd3d62ed | -17.844101 | -57.549702 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 043d8459-6c09-344e-90c5-e34dc39fb4ac | -17.8456 | -57.556999 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b20402eb-9048-336c-9a94-00b7e3fa439c | -17.8552 | -57.601299 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 604b6984-e399-3ff1-8ebb-24d4bf78ae8b | -17.8568 | -57.6087 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 98b8b185-6acf-3a70-84de-2306c16a49b8 | -17.8328 | -57.544498 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 49b83fc4-546d-301c-825c-3b3f6dbe3fe8 | -17.8344 | -57.551899 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 18f3c023-3150-391a-a635-f8c987bd9fc0 | -17.845501 | -57.6035 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b4e5cbfb-4b84-3459-9d0b-b295db0efcc3 | -17.847099 | -57.610901 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1ad6f51f-c5ac-33de-aa26-1eb7467b0144 | -17.8246 | -57.554199 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4c01383e-54f5-3c4b-a7fe-c35e7fe1c8b6 | -17.826099 | -57.561501 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 916edd26-484e-39dc-9576-839f98cec3b7 | -17.835699 | -57.605801 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b4bab4c3-2690-37aa-a442-4b3148c7f0cd | -17.8195 | -57.578602 | 2024-10-26 01:26:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README17.md)
