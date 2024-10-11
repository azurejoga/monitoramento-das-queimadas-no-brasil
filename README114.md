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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e0e04f9-6904-3c67-bdef-70ea43d84974 | -16.95908 | -57.4352 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ddc7f25b-8a8e-3f64-920a-cdb22fa165fe | -16.95867 | -57.4391 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 14ff634d-ab62-3b34-8497-b9b873c61120 | -16.95588 | -57.44059 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f7dd4d3b-4e86-3f89-abee-88908865f18c | -15.70636 | -59.34617 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c835aa37-9e27-35bd-8efa-2e891ed34e0a | -15.67761 | -59.33781 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4b26d64-35ab-3a3d-b5ac-07909f9e149c | -15.67576 | -59.33678 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 336d14b3-d883-3a69-b8bf-1f78d9bdfc0b | -15.67276 | -59.33691 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fca8a449-e645-3cf4-8784-d3e0a0d5bca9 | -15.66324 | -59.35778 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6977b47-98b9-35ed-9d58-0d2904f4c5c3 | -15.66259 | -59.36301 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 329a05e8-06b9-35cf-b522-7c8fa568dd52 | -15.65501 | -59.38425 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2879805-ec64-3e9a-aea8-a38bd98d1d88 | -15.64313 | -59.40043 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f22ca85-128c-35ae-a2ea-73fe5ac21f18 | -15.64247 | -59.40579 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f0a450c-8172-3148-a05a-6ee07ce63f54 | -15.63895 | -59.39427 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8108c8c-d8f3-3909-9623-52ca009c2f72 | -15.63831 | -59.39946 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 842d41cd-c98c-3607-89fc-440c9592b65d | -15.63772 | -59.44424 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a47bed9c-aaf3-3012-b327-f27692358fce | -15.63709 | -59.44935 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87279cad-fa49-3090-a97b-0923b49be1f4 | -15.6348 | -59.38788 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 810665a8-a0ce-3f93-80c3-71b7ba4043e6 | -15.63347 | -59.43878 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5c03597-242d-3946-b2e2-895f72f95ea9 | -15.6329 | -59.44345 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48d2bd96-afcd-33b8-87ad-34e9e4849690 | -15.63145 | -59.4152 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 38214e76-c2d2-352e-b880-d85dd96d2c8c | -15.63077 | -59.42068 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2a596e6-8056-3538-8f9c-411033efabb9 | -15.63004 | -59.42667 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6da17c68-178a-3579-ae06-a30b02670e76 | -15.62864 | -59.43807 | 2024-10-11 05:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0924eaf-8475-326d-945d-579c965b4791 | -13.74799 | -60.60215 | 2024-10-11 05:44:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3184d974-63a1-3931-a9f8-d1d154b8ffda | -13.74419 | -60.59729 | 2024-10-11 05:44:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca782092-3e1c-376d-bf1d-bf9215fc96f3 | -15.43621 | -60.01144 | 2024-10-11 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edecabc2-90f1-37b5-9c54-ac1965cda790 | -15.43156 | -60.01081 | 2024-10-11 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 674bc9f2-255a-3cb6-a728-94f3f387efaa | -15.38869 | -59.81633 | 2024-10-11 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 129e3478-86ae-326f-876a-3572ddfca00f | -15.3878 | -59.81504 | 2024-10-11 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d20b7a4a-620e-3a8f-9968-d937cff56d49 | -13.74363 | -60.60154 | 2024-10-11 05:44:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51c6b44f-350a-319e-8b0c-35d086aed295 | -13.73927 | -60.60093 | 2024-10-11 05:44:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf897fc4-0bc3-37e0-8f48-2561080b9d65 | -4.8363 | -50.78654 | 2024-10-11 05:53:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e1312a12-3317-39cd-99fd-9ab06464e366 | -4.83464 | -50.79829 | 2024-10-11 05:53:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 94f9cbe8-c5f8-3675-8057-4fb29834474e | -4.32154 | -48.63258 | 2024-10-11 05:53:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 3204c86b-5f29-36f6-88b5-f16dee4238a7 | -4.29784 | -48.62919 | 2024-10-11 05:53:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| da0ea1e9-2d8e-3c14-8fac-7c04576c0ca7 | -4.29233 | -48.62122 | 2024-10-11 05:53:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 187c5f12-adc1-3e95-941f-b8d0204d9228 | -4.1266 | -48.23811 | 2024-10-11 05:53:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 26e57076-a084-3483-8439-f50208f5f2f2 | -4.12411 | -48.25582 | 2024-10-11 05:53:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 723205d0-6a08-361d-8635-4a1cc90412b4 | -4.12168 | -48.27306 | 2024-10-11 05:53:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4ea5155b-01c5-3362-9c98-c057ec4be9f7 | -4.11441 | -48.23634 | 2024-10-11 05:53:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 346.0 |
| ed17404d-31f3-3672-a5c7-18977e902603 | -4.11191 | -48.25423 | 2024-10-11 05:53:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 232.6 |
| 9d745939-105e-3240-9121-636e706f8778 | -4.10952 | -48.27134 | 2024-10-11 05:53:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 26921f0b-e652-301f-bad0-f93671aaf569 | -4.10222 | -48.23457 | 2024-10-11 05:53:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 585f4d4c-8f49-3bf1-802c-01a97207c7d5 | -4.09973 | -48.25251 | 2024-10-11 05:53:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 005ddde0-eb8e-3bf2-b8a0-374365556b5c | -3.91677 | -48.33795 | 2024-10-11 05:53:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| f3a6ec9a-31b8-3b64-9b0a-8824f065af64 | -3.6961 | -50.11842 | 2024-10-11 05:53:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 913bbf05-b2b9-3e02-a548-e542f3ca4c52 | -3.69152 | -51.06808 | 2024-10-11 05:53:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d8bcb0d2-1a7f-3de5-a7cf-f35b3cd1569a | -3.68567 | -50.11694 | 2024-10-11 05:53:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5ec57bb2-8df2-3008-a574-1eb4a776fa5b | -3.33845 | -50.80749 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 25d74e35-1247-3754-8e9a-8dcc16d82110 | -3.3206 | -50.16696 | 2024-10-11 05:53:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 00b17a84-5026-36d9-9cf9-42b9aa752fcf | -3.31881 | -50.1792 | 2024-10-11 05:53:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| e72ede8e-c227-32c9-b6bf-4b16ace8a2f5 | -3.28781 | -50.94666 | 2024-10-11 05:53:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 6ef6cd28-081f-3729-9ed3-ae29c6376baa | -3.26961 | -49.09816 | 2024-10-11 05:53:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c6df88b9-b70b-3ede-a924-0bb0a4eaffa0 | -3.26105 | -54.18163 | 2024-10-11 05:53:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| fcc6ee72-4d90-3c73-8a10-309a46fbc2c2 | -3.25973 | -54.19042 | 2024-10-11 05:53:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5bc3c44d-7852-377c-ad7f-c6401147263f | -3.24139 | -50.84371 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| efb16172-3797-3ff0-b5b7-c679846c12f1 | -3.23975 | -50.85475 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d47952c3-7362-37c1-afdf-7c1022ca401b | -3.17298 | -51.30391 | 2024-10-11 05:53:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| eacf7301-7747-35ea-93c0-b944abd5a571 | -3.16834 | -50.4328 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 833938be-222f-3fea-9100-5d18afaf93d5 | -3.16662 | -50.44469 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| fbc18839-2364-36f0-b95a-01d4804b157c | -3.15823 | -50.43138 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 9ac6a28c-b931-36e2-92cd-b374c60079b9 | -3.15651 | -50.44328 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| d0cdc691-19f8-3b6c-b493-43adef3bfae6 | -3.1464 | -50.44185 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3d9d6ea2-5e3f-3052-9026-5f9424992a7e | -3.12507 | -53.73622 | 2024-10-11 05:53:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ff520b70-8bad-3078-99ac-c1480d1debee | -2.9898 | -52.90262 | 2024-10-11 05:53:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0198fc48-9323-30d7-81df-3281ba0d26d2 | -2.98847 | -52.9116 | 2024-10-11 05:53:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 55460272-0906-3f5d-ad3c-03650815d065 | -2.98088 | -52.90133 | 2024-10-11 05:53:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| d5b4f501-b2dc-3b0a-a117-aac69fe571c7 | -2.98033 | -51.35878 | 2024-10-11 05:53:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 0fb78b97-dce6-3ecb-b172-b6a812f28418 | -2.97954 | -52.91032 | 2024-10-11 05:53:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| efd8e23c-2c08-3823-88fb-7f8c7d078370 | -2.9788 | -51.36906 | 2024-10-11 05:53:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f38f4f9d-809c-3b2c-928b-4e0285f1fcf4 | -2.97195 | -52.90003 | 2024-10-11 05:53:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 08316165-beff-3642-85ee-1b2ff9052c9c | -2.97062 | -52.90903 | 2024-10-11 05:53:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 4526bea0-c1ac-3102-acf2-30e7b37c5c03 | -2.96303 | -52.89877 | 2024-10-11 05:53:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 036d1657-0a18-39fb-9d18-95f5ffbdf74c | -2.84006 | -49.52617 | 2024-10-11 05:53:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| af00ea76-704c-36c7-b25c-19cb3cb0c919 | -2.80977 | -48.70544 | 2024-10-11 05:53:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| df70599a-0961-3e5c-83a9-ef5d846eedba | -2.80955 | -51.00133 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9a724d99-77cd-3e14-bb5c-2636654ef4cd | -2.80798 | -51.01203 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 9c2a10fe-985d-3c15-8d75-dbf012e314a6 | -2.80643 | -51.02263 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ee9b82af-99ae-3796-ac11-d4e9e25eea2b | -2.8056 | -54.07555 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2eeebe2b-75d6-39e0-9687-839666c0b664 | -2.80428 | -54.08435 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7d814c9a-dd82-3725-9159-c250f2b85354 | -2.78619 | -52.47453 | 2024-10-11 05:53:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 93415584-51f3-35ad-895c-200f47672509 | -2.78482 | -52.48371 | 2024-10-11 05:53:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 5410eb21-51ec-3461-9009-a685a4c8a777 | -2.7788 | -49.23253 | 2024-10-11 05:53:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e9c170fb-bd5c-37ef-ba24-f0125917c314 | -2.74632 | -49.53463 | 2024-10-11 05:53:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| fb91ddad-f8be-3025-8c2e-54368d64e475 | -2.68464 | -53.33852 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0dca55c3-ea0a-3fca-a13a-b1a701149433 | -2.68332 | -53.34733 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e69794fc-6211-3a48-b9e8-88cd358ab667 | -2.67447 | -53.34605 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 7af9624d-40a7-3da0-8139-cb05ce699c59 | -2.67315 | -53.35485 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 43fd2dea-ba4a-3d34-af39-8430c5ad4138 | -2.66562 | -53.34476 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 3d7a3c9b-81a9-3df4-a404-f608ed54328c | -2.66431 | -53.35357 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 55bf7fa5-6ea4-37b1-9ad3-7f730278f3c0 | -2.65678 | -53.34348 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f92a75b1-7c87-34ac-828c-1843549c9f63 | -2.65546 | -53.35229 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b1075d45-6b57-3072-825c-ae05387e093b | -2.65171 | -51.70277 | 2024-10-11 05:53:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8a5d0a10-c839-3326-9301-ce74431c1aa8 | -2.25855 | -53.47639 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f9c931cb-8da8-302b-a5d2-04678e8a3d3f | -1.59504 | -53.34602 | 2024-10-11 05:53:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 919c11d6-f815-3dca-afab-959a285a7270 | -1.53345 | -55.41466 | 2024-10-11 05:53:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4bc6ea90-3486-318b-9d80-94251f1a2fa9 | -1.18037 | -53.39772 | 2024-10-11 05:53:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7b3e4f93-2b00-3217-bc7f-2835f04bb545 | -1.17154 | -53.39644 | 2024-10-11 05:53:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 559c8244-c958-3667-86ff-c7bb64af269c | -1.02885 | -53.72847 | 2024-10-11 05:53:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6eda9244-5105-35e8-aaab-62f6cf421d4e | -13.98545 | -45.79643 | 2024-10-11 05:55:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |


[Clique aqui para ver as próximas entradas](README115.md)
