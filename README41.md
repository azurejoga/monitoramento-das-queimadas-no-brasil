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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51303447-b4ac-36d9-a955-204025409b15 | -3.09341 | -53.71725 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5870b2a4-60f0-3c72-9004-d99c9d7038e3 | -2.67561 | -46.09702 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd9e7baa-8c35-3903-9a5b-aba23274c18d | -2.01527 | -51.19226 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9155a96a-2a8c-3b19-914d-952babec2f67 | -3.72543 | -49.2103 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fe33471-e2b1-3be5-8d40-fd436e1ca1fd | -2.46143 | -46.54887 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 514afc23-71ad-3ea3-a45b-c2c71c561611 | -1.33656 | -51.96852 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a88bcb0b-7edf-3db1-8811-d6a5e01d975f | -3.27191 | -50.62902 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b36c30da-a397-3f35-8bc1-8c6b5fb63edb | -1.09502 | -53.39238 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eda10df9-8912-3440-b3df-ba32c3b2f518 | -2.93631 | -48.51319 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97e60cc2-3612-306e-9b92-944a4de75289 | -2.66136 | -48.79383 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a9fa2e0-977a-32ec-90a8-db47031a8cd0 | -3.995 | -47.91303 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 795959f3-c513-3f97-b5d0-c46cd530157e | -2.98692 | -53.35677 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35641c1d-91a5-3c15-90a4-1cb23b66758b | -2.41299 | -46.50324 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26891727-58f4-3083-9e37-5120fceb7472 | -2.61739 | -46.56474 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ce8b0d5-60eb-3051-af7a-6e724a4787ed | -2.59104 | -47.02953 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39a563cc-e9ad-304b-aa8c-89eba0d6e6c1 | -2.97721 | -53.89382 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c8b7363-bc91-3906-b4ae-e799c5713478 | -2.25163 | -48.45567 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc4dc52c-ddbb-33f5-9712-4e24f3a7bbb1 | -3.22988 | -48.74595 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b17e48f-87c1-34d3-8b72-522cdae4db67 | -2.82753 | -54.1 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 622271b0-bf9f-3e78-98dd-d26c772fe959 | -3.48453 | -53.80977 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 5231a3ca-022b-3def-b676-fa75fbba9ff4 | -2.46139 | -46.57212 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6234678b-fd5d-303d-be01-b2564bfd2a74 | -3.97859 | -46.74133 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22b37ec0-4252-341b-a30d-ef52e3b95b47 | -2.02439 | -52.07561 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f58d2b6-6368-37cd-9a41-cc70a8d0cf5a | -4.13296 | -42.151 | 2024-11-30 04:40:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f6ce674a-ebf0-3e18-aaa9-8ba38b3a173b | -3.38438 | -50.10875 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f798aea0-2e51-3eb0-aa9e-283d78645fab | -2.86906 | -49.13954 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0edf93e-0701-3ad3-8258-32d1b156909e | -3.82603 | -46.55264 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2f7d3576-c920-3b76-9b31-4478dfc5c18e | -3.68251 | -50.22409 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 882df46c-4cb5-3be3-bc62-d73b1b6a61c2 | -1.23932 | -51.79886 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 569c48b0-c9ac-31c8-8c9f-fbd471ba0d76 | -2.83988 | -48.4766 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 44c325e9-376c-3c1a-b85e-d23bf93ec6d5 | -3.81501 | -46.68118 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 459e2a2f-14c3-38ae-8e6c-f0626a9c1d73 | -2.87953 | -53.98683 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e59460b-a4c5-3c20-80c4-d80819db1032 | -8.83864 | -44.78521 | 2024-11-30 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f26032db-adee-31b4-9c41-54c614a76eb8 | -4.70378 | -42.38351 | 2024-11-30 04:40:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 53695c96-7100-3c3f-9b48-b6f48f72966d | -2.67084 | -46.10447 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8786c08-7c0f-3a9d-b28b-e5ace14df3ec | -2.61811 | -51.80905 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1889d5a1-c444-326d-9a0e-fe885451a44e | -2.67397 | -46.60371 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a48a7f7-b566-3fbc-8dd4-47386a6ab325 | -3.56576 | -50.2313 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f50c8c1-7fb3-3087-8977-8f33c8c4ab62 | -5.23087 | -46.1208 | 2024-11-30 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dcac9b6-ad88-3148-ac89-9332744e40ce | -3.15413 | -50.1454 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed0cb9b6-fe6e-3c9b-9466-bcf23fc615b2 | -2.80799 | -48.61612 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2c97e75-cd03-3f4e-a40b-268531f4597a | -1.83232 | -47.21443 | 2024-11-30 04:40:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecd7db3e-a738-366a-857c-0966d128c526 | -2.98521 | -53.35925 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e20fb35-1e10-3291-be4b-468732ab16d7 | -2.56716 | -46.56874 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f7db359-f7f7-3971-bf07-fba3b682be40 | -3.33724 | -53.20876 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b6034354-b7d8-3d67-b343-0ba452076863 | -3.04263 | -54.08574 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ed50077-3524-3547-a365-39dcead498e1 | -2.69955 | -48.59227 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87423ddf-1a73-3699-8f87-a66389fd1364 | -2.83865 | -49.7689 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f28338c-97ef-3c50-bbb5-2bf039ac2e71 | -2.74532 | -46.11465 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f0e91a1b-9a94-3da7-bd95-349888f5b6fc | -3.14998 | -53.83791 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5271e001-613a-3eb2-b527-94e3c4ee3f9f | -3.73973 | -49.94545 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e722319-8147-3fc0-8315-f114cded5c09 | -4.86944 | -41.29522 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f660b24d-a755-318c-847a-01de1ff76223 | -2.67792 | -46.10551 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3154152d-055c-32d3-b56d-2d0810060607 | -2.78352 | -54.21739 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa49c35c-d2e0-3a5e-ba7a-288b99b38b95 | -3.93452 | -46.50808 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 440f93e4-18a1-3c94-8435-950567ae7711 | -2.62748 | -51.77313 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| df7a126f-f8bb-3a75-a754-929992e6b42c | -3.51219 | -50.31008 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75819d62-8ba5-3e5e-a995-5397be73fe54 | -2.81872 | -46.84817 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0094ccd1-3bb2-3230-9003-adf78b2293f7 | -3.49728 | -53.80635 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b527d78-1b16-3b81-9685-34df257e2128 | -1.58563 | -53.855 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cbc26f96-2fc7-3bec-8587-7d0977e692e5 | -2.71554 | -48.59825 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b1f929a-13cd-3feb-a961-6817b53cfb17 | -1.24077 | -51.62451 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef23d8fa-ca9e-38e3-8a27-995027bbb900 | -1.88824 | -48.64841 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 78f4354b-9f64-3409-b173-675973e73053 | -3.79806 | -49.59613 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01a8d791-0ca5-3d41-ba95-c26d4b638658 | -3.79391 | -46.69083 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31543bad-e57a-3d68-9912-78baaf8ef5b6 | -3.28262 | -50.64927 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f80e9dd5-ff34-30b1-9474-870fdafb8ea1 | -3.26805 | -50.56538 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a551df93-703a-3cdb-9556-314ec3b6d8c6 | -2.01237 | -51.18785 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba83b1cb-f533-38d0-a5a6-9093b140f3b2 | -0.96509 | -51.7114 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ab9e392c-d141-3902-854c-484c69c2c638 | -4.6793 | -46.3744 | 2024-11-30 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f4d9db80-c705-3899-9a1b-bfaae8120b3a | -2.35045 | -53.92581 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74940f12-3a48-3632-add6-429a0a9ae436 | -1.20008 | -53.89052 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9b166ba-51d3-399a-8b7e-d300bbac1073 | -2.92794 | -52.68895 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7bd58222-f8b4-34d8-99a6-d1e40db6d4d9 | -2.47869 | -50.36561 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c2d4423-3ee0-3a8e-8b5d-520b59640bb9 | -3.6104 | -49.98975 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aab7924e-2b19-34f8-9926-17d781acb561 | -3.04358 | -48.52274 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbf166fd-02f0-3fdd-ab9a-890352fa0192 | -2.78131 | -51.7183 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70516dd5-4e89-3cc0-a672-fc27111769b6 | -2.95794 | -49.37548 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39645558-9ba2-30d4-9d28-893e651792da | -2.53273 | -54.03891 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 605ab12d-6fd2-32f7-937a-8c6cceb09a81 | -3.06354 | -51.30669 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddc54c76-dd50-32ef-bc55-8e6ee27c50bd | -3.03357 | -48.50003 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faacf493-5b40-30f9-8765-1dced0e9795b | -2.19164 | -50.5784 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75fe6ad0-813a-3f31-8695-52e72761bef0 | -2.96521 | -48.0426 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| faba43d7-154b-3ed8-8a66-f7d23c59462b | -2.44399 | -50.42328 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6908240-e0f6-3947-8d6c-32895406a3fa | -1.10366 | -52.22835 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 416e9ca1-f6e9-33d4-81c8-f86f60a04b18 | -1.65785 | -52.49849 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1bf2c41c-d707-3c7b-9218-eb78c62602a2 | -2.72288 | -52.97883 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e3d6cf6-4db4-3c3b-8ab8-c2148db3f3ff | -1.26095 | -51.58979 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1fea6b0-fbc6-39dd-a394-89fe2754030a | -3.1756 | -54.32077 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f899112-1622-3f40-b802-96e08ece85d8 | -2.7829 | -49.21429 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9517fb00-5389-3a3d-b63b-b4700e84f197 | -1.70821 | -52.44638 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 22606d78-8024-3f67-a3e1-d130527c6f12 | -3.56245 | -46.33744 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09865696-8b1b-3aad-b50a-8f3df86d647c | -2.80487 | -51.5914 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dea471c6-779a-3f72-9645-bdc7f8410833 | -1.39598 | -53.62719 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5332e7ef-8292-34c0-9b60-4737989c68cf | -2.83769 | -52.91356 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb95db24-b7b2-3f3f-9389-e6482c4555fa | -2.67456 | -46.59992 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9021a9b-2fc4-3fa2-8171-29bc6a98e4f7 | -1.25037 | -52.18142 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5afec79-6ef9-39f3-b5aa-e4ec97c0e796 | -3.0919 | -51.40925 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8d1c3297-7c62-3403-a0ae-23149d708b8b | -4.08956 | -47.02124 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3e872eb-7466-3448-9225-1c0321aae02f | -2.60522 | -47.02793 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README42.md)
