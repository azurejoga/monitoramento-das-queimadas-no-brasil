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
| 21e70423-97e8-333a-bb82-6320e1adc63d | -21.13058 | -50.37117 | 2025-10-01 01:09:00 | TERRA_M-M | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| a99bca20-3b96-3aee-92d5-928e16aed5ef | -13.20589 | -50.90105 | 2025-10-01 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 91c1d328-b294-39d2-bdf0-ea6fdca4105f | -18.43041 | -53.16837 | 2025-10-01 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 004306d0-4c33-3fa5-b1aa-b96c15f9f95f | -14.98491 | -46.95295 | 2025-10-01 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 392ac4ab-7191-32f3-9314-03513c1453d2 | -18.70665 | -49.16453 | 2025-10-01 01:09:00 | TERRA_M-M | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e330a7e7-d8e8-3d4c-af29-83a6ea2c184d | -18.45369 | -51.42534 | 2025-10-01 01:09:00 | TERRA_M-M | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 28.6 |
| dbca602c-5323-3049-8b2d-321b1d1401cf | -17.41255 | -47.18505 | 2025-10-01 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 0ce0c8aa-08e6-3d4e-92fe-cbc1986ff678 | -21.05563 | -45.69489 | 2025-10-01 01:09:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 025b975f-85e4-3f37-90f4-c25510ebc27b | -20.60482 | -46.2122 | 2025-10-01 01:09:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a0009292-77c8-3d62-bfc2-f4e66fe97326 | -18.63408 | -50.71595 | 2025-10-01 01:09:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 3396ccca-7cfa-3892-ab1c-edc3b78cfec6 | -22.27882 | -46.73431 | 2025-10-01 01:09:00 | TERRA_M-M | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| d96c87fd-eacc-3ae2-a073-a6cccd4a4552 | -15.86158 | -59.32443 | 2025-10-01 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4d8a69bf-0829-3714-a765-6a2cbda06841 | -17.38284 | -47.14479 | 2025-10-01 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 171abffe-bfb8-3b80-b663-568a99ac9225 | -14.72196 | -48.15888 | 2025-10-01 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 11a638e8-a8ba-3521-9d65-fa4fa8da49a0 | -14.37722 | -54.95175 | 2025-10-01 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 26665be5-3d62-394f-b58c-cdf989981e14 | -14.35812 | -47.16156 | 2025-10-01 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 640811fc-5267-3c33-b98d-3312adbf7955 | -13.19999 | -50.94456 | 2025-10-01 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 2557f88e-5683-3c10-b473-b8d3a1b1a8ba | -15.92589 | -48.12576 | 2025-10-01 01:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 57.2 |
| d3c5c2cd-b69f-3f3c-9c11-0b41fdfcdbb7 | -16.0197 | -50.87316 | 2025-10-01 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 0a111a62-18e3-3552-bc0e-86e0eaffee94 | -15.99098 | -51.18086 | 2025-10-01 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 438e60f9-37e1-3078-9e99-1a012d59acc1 | -21.03859 | -45.65585 | 2025-10-01 01:09:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| c1842134-3e80-3620-8331-124f8c14fed9 | -15.29784 | -52.88903 | 2025-10-01 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 457f3921-81c6-3482-b88f-763c19d91406 | -13.32638 | -47.87102 | 2025-10-01 01:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 122.7 |
| d32df636-8a3b-3285-8a3e-ddef4b2ea91e | -18.45629 | -51.44074 | 2025-10-01 01:09:00 | TERRA_M-M | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 08e8a7f8-4bc8-3a2d-88ed-e279da909cf4 | -18.71556 | -49.15639 | 2025-10-01 01:09:00 | TERRA_M-M | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 24.0 |
| b5f30e04-9bea-34a1-91fe-47d5e18adeb4 | -20.62889 | -46.19933 | 2025-10-01 01:09:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 1242d93b-b912-37b8-a993-e4647800bba9 | -15.85666 | -54.03729 | 2025-10-01 01:09:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dff424f2-ff22-3692-a634-f37bcec798a8 | -15.25266 | -56.84717 | 2025-10-01 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5d6585fa-6532-36d3-b7f0-490d450978fc | -15.26138 | -56.7808 | 2025-10-01 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 62da127a-2630-39fb-862a-506d12b126ef | -14.86543 | -49.30597 | 2025-10-01 01:09:00 | TERRA_M-M | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 04959067-3831-3f62-ad59-700cf18b8e08 | -18.70634 | -49.18086 | 2025-10-01 01:09:00 | TERRA_M-M | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| faf6a6f4-3710-366d-9fb2-5646201a6eea | -15.84289 | -59.59293 | 2025-10-01 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c04b50a2-1231-3d97-837e-9aade63ca90c | -16.02266 | -50.89093 | 2025-10-01 01:09:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 28.8 |
| dbf9c2de-1cb2-398b-a264-0c6b7df70fcd | -20.59022 | -45.88527 | 2025-10-01 01:09:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 2c94c9b3-8182-311a-b4f9-a5ad812919fe | -14.49712 | -48.44641 | 2025-10-01 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| e9ca6bae-147d-32ed-ada5-fc18ff66a5c5 | -21.03223 | -45.66273 | 2025-10-01 01:09:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 54.5 |
| d70a39ba-67a2-3910-b24b-1f020549cad2 | -15.99386 | -51.19845 | 2025-10-01 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| c981b698-163f-38d6-9a06-093724bcdfc7 | -15.16847 | -49.12457 | 2025-10-01 01:09:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 27b7a1d4-d6b6-3b0b-8494-6305e4caea4b | -14.7175 | -48.15527 | 2025-10-01 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 59bbeaee-5043-3104-adfd-f064b9bd42e9 | -20.61367 | -46.20521 | 2025-10-01 01:09:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 830f831c-9671-3a75-9118-e613a282b60e | -14.71194 | -48.12543 | 2025-10-01 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 9e7b2573-6025-3815-9d12-0863568e2c55 | -14.35121 | -47.12378 | 2025-10-01 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 3226d011-52c6-3d63-b73d-5606c07f025a | -17.39904 | -47.14395 | 2025-10-01 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 137408e3-8ad3-3de0-9b55-443b91b3ef04 | -13.33966 | -47.89972 | 2025-10-01 01:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| e1a13bbf-e2bf-3374-aa9f-2b4e58849572 | -15.28031 | -56.78712 | 2025-10-01 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6798ec6a-22a0-31b8-afb2-975e353c7634 | -15.3004 | -56.787 | 2025-10-01 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 240d4ba6-6d0c-33b5-8c11-2d1238778d0f | -15.82742 | -56.21817 | 2025-10-01 01:09:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aee76c97-35ce-32da-a9ab-41fe882179e1 | -15.92853 | -48.13175 | 2025-10-01 01:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 2058c00c-4ea6-38f7-b564-8af3f6d48030 | -14.90395 | -48.14768 | 2025-10-01 01:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 7c691c3b-9304-3be6-8541-13e51f399aa3 | -15.9784 | -57.23371 | 2025-10-01 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 79c9f799-8917-3b87-b066-e7d7ae5af70c | -15.84797 | -59.59684 | 2025-10-01 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7738b759-29cc-3e9f-bc0a-33523fe3bf73 | -13.66925 | -48.05264 | 2025-10-01 01:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 5d1ea097-6ff9-3f75-87c3-09a8cb96f68e | -13.76878 | -47.96635 | 2025-10-01 01:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 44.7 |
| a9871d35-7eae-39df-ba4d-5b85695937d5 | -15.24756 | -56.81079 | 2025-10-01 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e54d1b21-8f15-38d4-826d-28b9d3bc56bc | -13.1853 | -50.93171 | 2025-10-01 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 845.3 |
| 3768c110-f3ab-38bf-a3e4-c562f2a5e5ca | -13.35953 | -48.10039 | 2025-10-01 01:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 9bfd29ae-5fa7-301e-9934-e4154d2cb808 | -21.13018 | -50.38197 | 2025-10-01 01:09:00 | TERRA_M-M | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| efdebaca-6c95-3db0-aa3e-8acb45d81301 | -15.8575 | -59.59552 | 2025-10-01 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2168477d-6062-3c64-9fb2-bc692aaef81d | -22.25865 | -46.70933 | 2025-10-01 01:09:00 | TERRA_M-M | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| 2a166eac-d164-3dfb-b830-7dfdf008b4b0 | -15.23902 | -48.73609 | 2025-10-01 01:09:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 2fd4a1f3-2e67-3c84-9cdf-fe685a5a2057 | -16.24594 | -50.94344 | 2025-10-01 01:09:00 | TERRA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 50.0 |
| b1a35e7d-7d1d-3590-9a75-bf61558a3953 | -13.18713 | -50.94686 | 2025-10-01 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2127.3 |
| 044aa7ac-b04f-3fa4-bdd3-618cc8143f44 | -13.33309 | -47.8635 | 2025-10-01 01:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 245.1 |
| 89354327-c6ca-3720-8edb-9af55debd85f | -13.36736 | -48.10566 | 2025-10-01 01:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a2d3a627-8d83-3f21-bd89-2f94fa4440b4 | -15.27148 | -56.78849 | 2025-10-01 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c9716e1a-4a60-322b-ad03-e43a18fe0993 | -17.3899 | -47.15108 | 2025-10-01 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d9dda6da-0c3b-39bf-9b30-996ec3940c77 | -15.98693 | -51.19433 | 2025-10-01 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 28d47325-7aa8-382a-a796-006239cf165f | -15.93404 | -48.16254 | 2025-10-01 01:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 041a539e-74c3-3df7-b761-635f5d6567c8 | -18.7105 | -49.18654 | 2025-10-01 01:09:00 | TERRA_M-M | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 41.3 |
| ff8cece2-06ef-3277-ab1f-389e617e77b7 | -15.16389 | -49.09835 | 2025-10-01 01:09:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 013f8b02-6596-3d02-9343-59e687957e10 | -22.2642 | -46.73758 | 2025-10-01 01:09:00 | TERRA_M-M | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 9e42e698-e31c-366b-82d7-e3c74afa58b2 | -20.59698 | -45.87791 | 2025-10-01 01:09:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 68.4 |
| dd6a0d6c-51ee-30a8-be88-7ea36fb09a2e | -14.8994 | -48.14296 | 2025-10-01 01:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 43.0 |
| c8504959-9135-3439-834e-9b8525ba6a13 | -15.16636 | -49.09154 | 2025-10-01 01:09:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 1d6ccafd-9904-305d-8a19-e23e8997c3f9 | -14.86223 | -49.3133 | 2025-10-01 01:09:00 | TERRA_M-M | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 30.4 |
| a2266593-a27e-3c37-a6bb-80085e96c56c | -16.24282 | -50.92528 | 2025-10-01 01:09:00 | TERRA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| f1b007d2-e17a-33b1-b2e3-9e91d68eceb4 | -16.19484 | -57.60107 | 2025-10-01 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 039397b0-baf0-3f00-9aca-d1ea58c5beec | -14.89853 | -48.11736 | 2025-10-01 01:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3ea731de-60bf-3a26-adc6-49f47b7c728a | -14.70129 | -48.13282 | 2025-10-01 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 59873592-706e-3955-811e-6f839e549642 | -15.84213 | -56.38602 | 2025-10-01 01:09:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9b3a9757-a635-3a90-a2b8-161ecf141cf6 | -13.77678 | -47.95884 | 2025-10-01 01:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 2a220f24-4dd2-3a35-b14d-32251c1b932e | -15.70831 | -59.48668 | 2025-10-01 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 166712e3-005e-3458-9ca7-7b327baa0bfe | -13.67537 | -48.08546 | 2025-10-01 01:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 36.8 |
| a0f5d177-910b-390b-b93e-9bf518461d1d | -22.57771 | -46.76508 | 2025-10-01 01:09:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.5 |
| 9177a8d8-3e05-3de7-a2a7-b7c77eb81486 | -16.0258 | -50.88419 | 2025-10-01 01:09:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3151e063-7358-3fdd-8b34-967da23ec7ce | -15.84343 | -56.39524 | 2025-10-01 01:09:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| da9b9731-564b-381c-b1f0-de80c5718fb1 | -22.58311 | -46.79287 | 2025-10-01 01:09:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| 8b63c057-f791-3833-9688-d17d3f010c35 | -16.05612 | -51.01736 | 2025-10-01 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c413604b-f4a8-30bc-98de-05ce5282c7aa | -13.28492 | -47.21613 | 2025-10-01 01:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 41.2 |
| da34552d-15a1-345d-aa7b-18b131e8ad84 | -13.70627 | -48.6535 | 2025-10-01 01:09:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 927ca692-e5a3-3819-837d-334bcdc8f6ab | -22.58388 | -46.78732 | 2025-10-01 01:09:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.6 |
| f86a1d00-a992-37c8-b6cc-50043090a201 | -13.1965 | -50.924 | 2025-10-01 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| cd38494c-026b-383c-8874-6e13cc5bea77 | -13.32717 | -47.83091 | 2025-10-01 01:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| fa6406db-bb67-36a8-a836-10bc5d9e81ba | -13.18866 | -50.95229 | 2025-10-01 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1353.2 |
| a2c652df-0f68-3ec3-b4b3-d1deb89b683f | -20.62028 | -46.20739 | 2025-10-01 01:09:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 9c565b0c-ceea-39a7-bd9a-bf0e2e62a686 | -16.0601 | -51.01001 | 2025-10-01 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ee407b99-c774-3e73-8d1c-ef54f693edbf | -18.71958 | -49.17857 | 2025-10-01 01:09:00 | TERRA_M-M | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 35.8 |
| c6f2760a-1402-3096-82aa-8427f38b8779 | -15.99884 | -51.19208 | 2025-10-01 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b82e4eef-cc1f-3b31-a118-ba22ced40d7b | -17.40604 | -47.15004 | 2025-10-01 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a6016635-2db9-3848-b6d2-754d4ee10a58 | -15.93155 | -48.15611 | 2025-10-01 01:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 46.8 |


[Clique aqui para ver as próximas entradas](README6.md)
