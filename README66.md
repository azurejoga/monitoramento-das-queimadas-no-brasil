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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d111a5e3-d74c-3f7b-8c3a-f9de288eee54 | -2.75945 | -49.61096 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81851492-f77c-36ca-ad8d-cf404b18e8a5 | -2.748 | -49.49102 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da129806-4f0b-33e6-a8cc-0c813bd00c06 | -2.74744 | -49.49478 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f82f7704-7cb2-3590-a531-99e706f5bed7 | -2.74657 | -49.83164 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4199db6-8523-35c8-a1e3-fade29a5c5ff | -2.74203 | -49.55894 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0e51c5c6-ff30-3f0e-85fc-19dff90c593b | -2.73968 | -49.63042 | 2024-11-02 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0262c733-2d23-3d29-b4a1-b760a0cad32e | -3.48423 | -50.33445 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e28d7ceb-bfc9-34c1-a35c-7ae758d69179 | -3.47496 | -50.36941 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 65194683-85a1-38fe-a6e8-728f8be5984a | -3.4742 | -50.37451 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8607db58-a14e-31d9-8f65-ad49a3e2c087 | -3.47345 | -50.37957 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 925e2557-2157-3c9c-a24c-4dee763eca45 | -3.47177 | -50.3637 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f2bd32d-5e9e-38d7-be12-7c339a2a5596 | -3.47025 | -50.3739 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4baa23ee-0fa2-35d3-aaa1-3e1df0083c43 | -3.46705 | -50.36821 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d706409-d390-3489-a5a7-4fbce1240bf7 | -3.4631 | -50.36758 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eddeb753-f288-3434-bb04-4e87af6e56d3 | -3.46234 | -50.37269 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc08c80e-aecc-3ef3-bd6f-8a6455c7ce22 | -3.45668 | -50.35627 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8de83e84-c70f-3f1e-aca5-745a7b85f148 | -3.449 | -50.38088 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfbc40e7-4523-3892-819a-98410a8d7e92 | -3.44525 | -50.38319 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 110786a8-7246-3f47-8c0e-381fc13632ce | -3.44506 | -50.38022 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d07999c6-7d3d-3fb1-b283-441a90399976 | -3.43405 | -50.32445 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59409ab7-8a72-37de-a9c2-d108d59b3973 | -3.41682 | -50.38414 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8de3a26-b019-3251-9f8a-35969e33f18c | -3.39532 | -50.33933 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 587cdf90-d6b9-3170-ad7a-ee7ffb7cf500 | -3.39454 | -50.34449 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e53f4b9-11fd-3641-9e3e-d66ba2943b16 | -3.39058 | -50.34389 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 249e8cf8-44c3-3cbb-976e-fa7a7ebeabd2 | -3.37871 | -50.34205 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e7e41a1-d072-3aec-bc48-86531d1a3763 | -3.27546 | -50.33522 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c5498e8-5272-351c-b6a2-9aaf29d68b93 | -3.27151 | -50.33462 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 761693d0-be6c-3a2d-8ba2-037f8d6850d7 | -3.27074 | -50.33972 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c47c3854-a234-32d7-85d2-c5091ba8acce | -3.26998 | -50.34479 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5d828551-add5-39a3-bf20-ea31501ad23d | -3.26755 | -50.334 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a2a13d1c-b970-3c1e-9878-72e9f96af249 | -3.26679 | -50.3391 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| aea5d4a4-b719-3658-8f76-f1bfb16441f6 | -3.26603 | -50.34418 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7668b35b-2b7c-3d0c-ac6c-e2820836c637 | -3.26527 | -50.34924 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0b7046fd-822e-3bce-b2b6-8f4a758ba7d8 | -3.26284 | -50.33848 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5bd0faa-b53c-366e-9fa4-782802e24633 | -3.26208 | -50.34357 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d89480be-50ed-3110-93f8-b0dfbbe79524 | -3.25889 | -50.33788 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60d95370-4ec4-3ecc-acf3-a65a2e07e0f3 | -3.25813 | -50.34296 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 077d9166-4b58-3687-bd81-5d576c1b399c | -3.25738 | -50.34803 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b61ec07d-f517-3ea4-b215-2fd758caee37 | -3.25418 | -50.34235 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f5fd0e8-b240-368c-b5d8-3ea5efc23788 | -3.25343 | -50.34742 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49b5acc9-81ab-31c5-988b-eb4b8f456e54 | -3.25099 | -50.33667 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f724ca8e-04fb-3e46-9141-d8494d742b48 | -3.25024 | -50.34173 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8fe11d3-e8e6-3463-8bdf-f0994d56b7e2 | -3.24948 | -50.3468 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fbf398a-94a0-3518-bb76-77ea3573eae3 | -3.24704 | -50.33606 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c9f8f56-406d-3cb3-bdd0-b470e1053e4a | -3.24629 | -50.34112 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8437f527-c37d-35ea-826d-e97c61ca77f7 | -4.89954 | -50.50636 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c1a86f9-c4f4-3f44-97b2-da4029fcae9a | -4.48564 | -50.1258 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2fb4f6e-e034-3141-9e7e-56c042484ab1 | -4.15635 | -50.21286 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5c6b116-b700-3e3a-9bbc-35c3420bcb6d | -4.14883 | -50.75069 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ac4b704b-2bdb-30e5-aad2-d809f7ac331e | -4.14838 | -50.74897 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b76f5ce7-097c-3c7a-930c-5030d5c51388 | -4.14493 | -50.75009 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 747a60c5-e7dd-3d67-9652-1b648b179383 | -4.10014 | -50.75167 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a1376eb-f03c-38cd-8e3a-79d375b88325 | -2.16863 | -50.50904 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aec90a21-7a0b-39c9-8ccb-f91573977a04 | -4.0994 | -50.75658 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6404704c-4fc3-357b-98bf-31d6654ddf85 | -4.09625 | -50.75107 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| adf421e3-077d-39bd-a2e9-1ced23695d98 | -4.09552 | -50.75596 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40f26260-9256-3078-985c-a84e0bf9d617 | -3.91843 | -50.43802 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d83cc9b-ce0b-3e3d-b1a0-9166a5e9ac13 | -3.91447 | -50.43743 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36aa7e23-aaf4-30ea-8860-c6aba96eccfd | -3.89398 | -50.24493 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3c3ea35-02c5-38f8-a0b7-6eb97df83934 | -3.8666 | -50.48749 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a2c2cf3-d2b6-3603-954e-9f80d45e0482 | -3.86336 | -50.48572 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8c3b937-fadf-3fd7-bb15-88d06b714247 | -3.85535 | -50.43246 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a33b94e-e478-357f-8d63-90d869fb69fd | -3.84106 | -50.14771 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3397e647-2839-30c8-b21e-16777daa081b | -3.77012 | -50.37878 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70c47075-5561-361e-a15f-a78ef72fe693 | -3.7671 | -50.38044 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cf0bd05-68c6-3a60-9ed3-741ac618d89f | -3.70931 | -50.54722 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a76c1265-f3e6-3ee5-b9ae-b52f5b4f529b | -3.70857 | -50.55214 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4d4d2f2-62b0-3162-becc-0b797780d026 | -3.70287 | -50.15538 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b0d944c-f81e-3cf0-9446-3d318e7a3f8e | -3.69935 | -50.1513 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a1f8ad1-987f-3f0b-a6a5-f8cc308dc0c4 | -3.69884 | -50.15481 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 99a269dc-ce56-38be-9013-4d10499fe1f3 | -3.69533 | -50.15068 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fbf5ef7e-20cf-3a86-9a43-6b7525c35dca | -3.69481 | -50.15422 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30c7fee7-930f-3542-bc57-e046bc4b5f6f | -3.69471 | -50.59063 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff3d8b83-8492-3194-8c81-a2553faa61f1 | -3.69397 | -50.59556 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa124aa5-12d3-3c00-832e-9c18844a5131 | -3.62723 | -50.1839 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b367918-2910-3538-a729-cfecead3da65 | -3.62672 | -50.18735 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b96028b-d82a-3be9-bd51-1857f1992e15 | -3.62619 | -50.19084 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76df7d38-f3f7-3493-8e24-0431928df50e | -3.62426 | -50.17633 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd7515dc-c5b5-357f-8753-a7e117828955 | -3.62322 | -50.1833 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b9005b6-87d3-38a0-b9cf-f7cdb8e6058e | -3.6227 | -50.18677 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d39d3a58-1639-3b89-95f6-072e801529be | -5.04841 | -49.79962 | 2024-11-02 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15f8cb01-4d45-339d-9449-f7c4a5130312 | -4.80441 | -49.48375 | 2024-11-02 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1f24da5-fbd2-3600-a059-33b9b49a629f | -4.80381 | -49.48781 | 2024-11-02 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eea767f0-46ce-3d09-aa12-027796ff094e | -4.80012 | -49.48319 | 2024-11-02 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3165f3fb-5f5d-3e4c-a0e1-0b00e51a721c | -4.79953 | -49.48723 | 2024-11-02 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d31832fe-a07e-3bc1-a337-538756337ee9 | -4.71318 | -49.60611 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f5eea4cd-bf15-37c0-9cf9-e8c62f95e007 | -4.71258 | -49.61009 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| af017b75-a6ae-3445-b4ec-8e0a2219da67 | -4.70894 | -49.60548 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f5ab7d72-a3f5-316b-8c1d-66fbf626de4e | -4.70835 | -49.60946 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 5928fff8-845d-3078-b1d3-c16854eaa16e | -4.68048 | -49.41267 | 2024-11-02 05:04:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cff5d1cc-04b8-3ee7-9193-91ae4a11d44e | -4.67694 | -49.52772 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1c227f7-cccd-37b9-85f0-e0b4fa7e9a3c | -4.49464 | -49.7069 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f55287a-54e4-3e35-9b4e-261e5b11bc5d | -4.41295 | -49.67228 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 327e1a55-5747-3dfe-a25c-f4f415c3f421 | -4.40993 | -49.67024 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2336e2be-6728-3b12-8dd4-12050e742fb3 | -4.40938 | -49.67406 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dfc9ffc-5631-38be-8486-eac642f93ffc | -4.40875 | -49.67165 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d396d02b-8011-3d76-ae98-8186d2faad1c | -4.38593 | -49.41843 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fcd7c7cb-3c12-3bbe-9a46-34686a865b82 | -4.38166 | -49.41782 | 2024-11-02 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1a373d2-e9ae-3b4d-b13a-ae36be8f8873 | -4.37823 | -49.6748 | 2024-11-02 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1311fe85-cdbc-3c1f-8f7b-e1d19275dbd6 | -4.06279 | -49.26192 | 2024-11-02 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README67.md)
