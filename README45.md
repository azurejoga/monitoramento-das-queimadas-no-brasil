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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e914a282-c88c-389e-a40f-a5801d035ac2 | -10.53212 | -47.66816 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbde4f32-4049-3d80-abb1-ae85e2226d4d | -10.42222 | -47.51867 | 2024-10-24 04:34:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 590175f6-3a61-36b9-a6f2-020232d8eb8f | -10.41888 | -47.51815 | 2024-10-24 04:34:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd8b7db1-2d48-3ac7-8218-ffc7f25358a8 | -10.30799 | -47.95231 | 2024-10-24 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3ec7748-38f8-3427-a418-f6449398f496 | -9.99471 | -47.99997 | 2024-10-24 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36dcae7b-03c6-35cc-9295-bd5d6f777cbb | -9.9914 | -47.99945 | 2024-10-24 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d76e3517-76d2-3ac7-8ec6-59189372fc13 | -9.9301 | -47.86745 | 2024-10-24 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a685c40b-ebf4-3e3a-b647-51da06acf19f | -9.92286 | -47.84825 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfa2a100-fb6f-3851-9922-2ecd30c51f15 | -9.88911 | -47.80332 | 2024-10-24 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0f9313c9-9c9f-3cd3-b6a9-6f9bdc2ca89a | -9.71439 | -47.65622 | 2024-10-24 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87f53306-ccf6-3b3a-9c04-2638ac1a7f92 | -9.62775 | -47.90955 | 2024-10-24 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82e0a561-1d90-3203-a1cf-55a590b1ef17 | -9.60644 | -47.60683 | 2024-10-24 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 069b6e94-4517-3393-a18e-ccd97da9afd2 | -9.4802 | -47.76431 | 2024-10-24 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4732e2f5-8028-3802-8417-563a152fda4a | -10.25628 | -47.62483 | 2024-10-24 04:34:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfadfdeb-a7ce-3019-a6c0-b9e3ca8c7b0d | -10.23492 | -47.54504 | 2024-10-24 04:34:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36a5e5bc-ff5f-3bd1-aa2f-bed365b8c97c | -10.22645 | -47.48868 | 2024-10-24 04:34:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7eb82e6-cb7d-3710-9a05-b5230b96e0fc | -10.08584 | -47.71825 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d0657e37-1b38-333f-920f-69c1de6af5f6 | -10.08251 | -47.71772 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e9b048a-4794-3468-81bb-ba0d33549bec | -10.07918 | -47.71718 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3be1e335-a4a4-35cb-96db-995056d4c0ec | -10.07864 | -47.72074 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38e8cf11-9e15-3bd5-b797-013892b8925c | -10.02742 | -47.45745 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5553609d-9c3f-3eeb-b002-6da485af9f1a | -10.02407 | -47.45692 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a6a39ab-0f7a-357a-8e1c-08b05043beed | -10.02073 | -47.45639 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cb9d6ed-b1e9-3260-906a-8adb74545108 | -10.02017 | -47.45998 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7f05e689-32ba-39b3-9db6-9a51adff242a | -10.01793 | -47.45227 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6473075-214c-34da-8597-875c69737941 | -10.01738 | -47.45586 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1df898ad-e0c1-3bd4-a1c5-62ffc0b7b895 | -12.21392 | -48.07072 | 2024-10-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c248cb70-2b82-3500-8dab-815112d927e1 | -12.21168 | -48.06304 | 2024-10-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fee0cad-8770-3dec-ae07-64d544909eb1 | -12.20834 | -48.06253 | 2024-10-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43087ecb-d362-353d-9b9c-9da09e59aa5b | -12.07696 | -47.98629 | 2024-10-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 394763cc-fdc9-322f-83f8-281f781db468 | -12.07362 | -47.98576 | 2024-10-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e892a38b-87f6-3290-a35a-0bb6768939a7 | -12.05714 | -48.33801 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 65636e96-475d-397e-948b-ef2d38f01541 | -12.05437 | -48.33394 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95027c1f-f079-3ae2-8e9d-8e71a984b379 | -12.05382 | -48.33749 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a41120a9-74c4-391e-bb78-06257d338768 | -12.02917 | -47.90173 | 2024-10-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e44095bb-dd64-3383-8265-1d4336a63c9d | -12.01912 | -47.90016 | 2024-10-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9238728a-daeb-3536-b9d6-1bab859a55fa | -12.01048 | -48.26508 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 282aa6fe-325f-3c1f-a3c8-b1f70d926465 | -12.00994 | -48.26864 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f6888319-89fd-30dc-bcb2-a04487ec6560 | -12.00661 | -48.26812 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 67eb7e22-2c04-3b5e-b72e-215f577603b6 | -12.00329 | -48.26759 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e27ddac7-aad8-3e2a-a2cf-77d2f55d34cd | -11.99656 | -48.4662 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 823f8136-4aee-35c7-a31f-4fd5723e419a | -11.99325 | -48.46567 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76370712-e0e8-3612-b3d6-06de3e8a92a1 | -10.88002 | -49.14466 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a98eddc0-d7fb-3602-9962-cd3113edc770 | -10.87672 | -49.14413 | 2024-10-24 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce34300a-b250-3381-91e1-29c0611985c2 | -11.37395 | -48.46825 | 2024-10-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b0cdaa9-f537-3667-82f4-7614dbc52c9b | -11.25615 | -48.72187 | 2024-10-24 04:34:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7697c6e-de38-33de-b05e-ab1bd9c611b0 | -11.25339 | -48.71785 | 2024-10-24 04:34:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67ddad98-8eb9-3a48-a5ce-9bee338dde59 | -11.25284 | -48.72134 | 2024-10-24 04:34:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6f179ea-dbbb-3165-8dbf-78e947fa22cf | -11.23482 | -48.44555 | 2024-10-24 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a9d2af0-959c-36f7-b36f-7a9cae3867e5 | -11.15582 | -48.29634 | 2024-10-24 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7b1d1c4-f641-3a5a-9b01-1270a9ccaee9 | -11.12224 | -48.62173 | 2024-10-24 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d5cb2ae-d969-3d01-b90c-ba89bd091ff5 | -11.11893 | -48.6212 | 2024-10-24 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60011eb7-55a1-3c22-91a2-3517df46f559 | -11.08511 | -48.33579 | 2024-10-24 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52cbfb6d-2404-385b-9af6-baa030ba05ce | -11.02982 | -48.27639 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab0c8cee-132d-307f-9a60-eeeaf12ee920 | -11.02928 | -48.27991 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce85c4f2-1774-3fa0-8a50-af2f9c534ab7 | -11.02651 | -48.27587 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ccc192d5-816b-339a-8268-c131960c4e5e | -11.02597 | -48.27939 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 014c1ab7-dbc0-3ea9-838b-a97d606af1e1 | -11.02542 | -48.28292 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ee1184d-2c41-37fb-8dc7-8c2bd0b5f491 | -11.02374 | -48.27182 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fae2766f-2633-388e-8bab-6118bad9df93 | -11.0232 | -48.27534 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a91b58b1-ddd2-3b82-bdc6-eaec698f8945 | -11.02265 | -48.27887 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 77a3c368-d41d-30d6-8044-cfa1082da89e | -10.89794 | -48.66428 | 2024-10-24 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 827c952d-dfa1-3603-9b01-47f0da6e6c47 | -10.89464 | -48.66376 | 2024-10-24 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbcdd820-3055-3238-939e-a24c6ec92b09 | -10.9789 | -47.85505 | 2024-10-24 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caf53261-2f0b-37ab-b804-9d4156c7ed8d | -10.97557 | -47.85447 | 2024-10-24 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1ae59a6-922d-3325-a0af-b9c7be56ff2c | -10.97548 | -47.83635 | 2024-10-24 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c37dde7-6df8-3178-9b36-646b5b29822c | -10.95496 | -47.83658 | 2024-10-24 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 535c22ae-d646-398b-ae1b-89d68042c229 | -10.93822 | -47.81219 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3b30673f-1ee5-3fad-b33b-8bfca24022f2 | -10.93768 | -47.81574 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1cafa2b3-776f-300a-8c35-7c2dbf995c57 | -10.93698 | -48.04114 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbd3f276-6bb4-3cf6-adc3-82e37b463b99 | -10.93489 | -47.81168 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 919255d2-19d3-3aa2-8790-c126ccee75a8 | -10.93434 | -47.81524 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f2680b54-9c51-3d37-98fb-212a8cb3b12e | -10.93365 | -48.04064 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccaa9bad-42a0-316f-803a-072ce47e4fa8 | -10.931 | -47.81472 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d496583d-1ddb-3f41-8188-c4643efec57d | -10.93045 | -47.81832 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d2fac9d-bc03-3846-b4a2-c3a273de268e | -10.92822 | -47.81057 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 561f4440-d03e-30cd-a691-b659c16fd609 | -10.92767 | -47.81419 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1f05a8e-9ff2-32c4-8cd3-83e6db6f173b | -10.92712 | -47.81781 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c962051d-f07e-3f30-852e-c4a0bacd7fed | -10.92434 | -47.81366 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1ceac6ee-3f00-3ab2-8511-ec6b1ea737e6 | -10.91303 | -47.97583 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10fd3aa9-ca99-3860-94de-c8cd4fcf3eb9 | -10.91249 | -47.97935 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f861e5cf-8db9-3635-ad5c-9b56e7f968f5 | -10.90639 | -47.97474 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fb3ad5e-3ecb-35ba-83f5-a74b000963df | -10.90307 | -47.97419 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fdc28f7-c81c-34c2-b56c-939a3306b070 | -11.72773 | -48.35802 | 2024-10-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0fd954f-cdec-3410-b03c-df292a2ea269 | -11.72496 | -48.35396 | 2024-10-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 272f47b4-7a28-307d-9225-e4fc95b2c16f | -11.72441 | -48.35749 | 2024-10-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 588cf7be-3ea0-384a-8ce9-0110f76c1ab3 | -11.70631 | -48.43058 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edb70d27-8728-31a7-89f5-9e6ed3e15cac | -11.65883 | -48.80114 | 2024-10-24 04:34:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9542b3a9-2ffd-38dd-95f5-271af1eeb135 | -11.65828 | -48.80464 | 2024-10-24 04:34:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3542d62d-0016-3645-a25f-9eed37100f25 | -11.65553 | -48.80061 | 2024-10-24 04:34:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea4e55d6-fd9c-3cfc-94f7-302b533cc199 | -11.65498 | -48.80411 | 2024-10-24 04:34:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7618229e-18ab-301d-9127-ee190c14c22d | -11.64206 | -48.60427 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9006b17e-e8a0-381f-a81a-a029c16bd62d | -11.64203 | -48.58266 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8692d012-a511-373d-9737-2762d0103b42 | -11.64152 | -48.60778 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 107d3def-ffad-3308-916a-e756e44fc417 | -11.62425 | -48.38884 | 2024-10-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fff4fbf2-51db-36cd-be14-6bd66483d5bc | -11.62148 | -48.38478 | 2024-10-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46be1192-cbb4-310d-bc5a-2c122415e80f | -11.61817 | -48.38425 | 2024-10-24 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8888781a-11af-338c-8787-f365472af357 | -11.61675 | -48.56805 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bdacea6-14d0-3fdf-8679-a08a472091e0 | -11.61068 | -48.56348 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adeee0dd-650c-33c1-b899-9d68e4a0c2df | -11.6068 | -48.54485 | 2024-10-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README46.md)
