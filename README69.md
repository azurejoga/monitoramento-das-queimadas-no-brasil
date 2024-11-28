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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a3038d0-fb1b-3a98-8348-56a4386e1ea4 | -4.31653 | -48.08397 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f37f19bd-2951-3077-939e-cc17d2a0cd8e | -2.23499 | -55.90245 | 2024-11-28 04:25:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58c276e7-cbd5-3cea-a964-8ff33e12328f | -2.52707 | -50.1072 | 2024-11-28 04:25:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ee87219-358e-3d51-a9cf-6113325ae184 | -4.10544 | -46.93957 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83909fe3-890d-3848-b9d9-152093e3c692 | -3.62565 | -42.40343 | 2024-11-28 04:25:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad76d4b1-a3a9-3ea8-86ce-503d07c26013 | -2.95701 | -48.61709 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1db6fa76-8d48-348f-bc13-9c64fd9a6b86 | -3.32557 | -46.62476 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a3b6ddd-82ad-3098-a50f-27a9dfa66799 | -3.34364 | -50.52016 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aed0f646-74b5-3578-83ac-97da796d5b13 | -3.55176 | -43.18295 | 2024-11-28 04:25:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0da60bda-d2cf-3b72-a0d0-cf0f8164615b | -3.07839 | -50.2531 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f1fa87b-5dec-38b2-bdc1-da6a6553695f | -4.74082 | -46.50728 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 891a9370-176e-3ec9-af56-3c5be49959b2 | -1.78668 | -52.74641 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58ab6113-b80f-3836-af7e-3dd451f22870 | -2.86826 | -48.56133 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb6d1a82-1325-3907-8b67-c85aa68ae3fe | -2.60063 | -53.97697 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0f37197-5b92-3701-a304-9427e2dedb7e | -2.79779 | -53.04565 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a251c795-558c-3811-9505-375f3b3a7512 | -3.37517 | -46.65788 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae4664aa-aa86-372c-9532-d795103c2492 | -3.10316 | -54.97883 | 2024-11-28 04:25:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cba34e07-34e5-341c-8518-1b97c928ccaf | -4.22114 | -50.8922 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26deeadf-5c83-3c43-9134-7b0c4c851e51 | -3.24467 | -50.14574 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a71f12c-57b6-316d-a22e-17f945864783 | -3.43864 | -54.5403 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bad25d7b-8a8a-38cf-8e38-a00d155128a5 | -4.25273 | -48.07029 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86206939-1c58-3ebc-9901-8c5a006ed613 | -3.96469 | -46.90251 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a13cda6-6678-30f2-b4fe-24f5bdfe7e2e | -3.24628 | -53.64151 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c1236c88-d530-34ac-9c8f-4eef9e92cb1e | -4.05809 | -46.82671 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9b6dbe0-4471-374d-b157-71d4aa0c63d1 | -3.38104 | -50.12109 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 202a0817-2715-3642-a7d3-157306470370 | -2.64526 | -48.48139 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a445fa4-0114-3049-a163-465231398b59 | -2.23249 | -53.68926 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17846850-7eed-3201-9cef-e320d0023b0f | -3.54303 | -44.94436 | 2024-11-28 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d43892f6-6755-329b-9f3f-447a3b961a72 | -2.53354 | -50.09258 | 2024-11-28 04:25:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65137dda-efb8-3b3b-8369-24574abac088 | -9.07882 | -49.57638 | 2024-11-28 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb18b956-e156-38b1-a549-4115de6e8753 | -3.11285 | -53.76208 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef03a1fd-1950-31ae-8657-7838293f4522 | -2.87109 | -46.85627 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35645c3d-e02d-30d3-9c11-fa78b9be7126 | -2.62007 | -51.76107 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5af7ce47-0ab4-3ed9-a228-15031de4a49a | -3.50902 | -45.22552 | 2024-11-28 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ff04d26-5b0c-350d-9475-171118bbcfb1 | -4.34238 | -45.86726 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccdfa612-d75d-32c4-97fd-c57f3d325ff2 | -4.30896 | -48.08669 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90922a1f-cef0-3533-8c64-3154716d7586 | -2.74808 | -48.65937 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ead52f03-2ede-3ffb-827b-89f09d4c3ddd | -2.69618 | -51.98476 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd555409-9c61-3b24-914f-396112cba96c | -2.97872 | -53.35604 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6b23df8-dcec-3b70-aca0-ae5760299e2f | -2.72264 | -47.69983 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fecf0513-5dcb-384e-8b56-19d10db1d567 | -3.81618 | -46.59697 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d123f9d7-a786-33f9-80d0-90dc915f0fbc | -3.0978 | -53.25501 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fad6a0fa-4029-37f9-9d76-533f0c10a9db | -4.36251 | -48.70219 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9350a33-bfdd-3463-b2b4-ebadb38a2271 | -3.46067 | -44.92804 | 2024-11-28 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b1c36b0-c487-3237-8d67-689e6c533c60 | -4.20892 | -50.89024 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0ff8755-7160-3b78-bef7-138cf21b0ffd | -3.05148 | -48.51955 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9431b471-f20d-32e5-a292-2fc36420d3a5 | -3.97188 | -46.96566 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c44ac043-21c1-3350-9402-86e47bdb2c4e | -2.32173 | -51.96886 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da42675f-a89c-3d82-8128-23c57d45ca8d | -3.86949 | -46.66674 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7012720-8daa-3460-8079-3b0237f0815d | -2.97139 | -48.00308 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7620c469-f2b4-379a-87e3-6b37f381e08c | -3.18048 | -48.43855 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54fdf725-7d2d-3c63-8c6c-aeb4417af0bd | -3.56852 | -52.28168 | 2024-11-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c77d3a8f-676e-3008-862e-8f81b7c081b7 | -4.11052 | -46.10932 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d23dce19-f4de-3168-8725-2123f53bb482 | -3.52475 | -52.15374 | 2024-11-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b264963-4468-3451-a309-6f3253370644 | -3.81174 | -47.46773 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fdea5d0-7507-3c5d-8a66-6c2ab7b11618 | -4.17174 | -48.6279 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d415285-bf60-3ec7-8ddc-6df602d77634 | -3.38187 | -50.11608 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 73e4a4aa-a262-3866-ad5b-c10b87c7a0e8 | -2.83307 | -51.83749 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8ab49433-420e-3199-b046-bddc7d4c9cc9 | -2.87852 | -51.58621 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37fa0c9b-c55e-33ec-838c-ca1662bd4cf9 | -3.34824 | -50.51731 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6c9f66f-d8c9-3a86-94e5-8cd541e6599f | -1.83783 | -55.57118 | 2024-11-28 04:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb949187-687d-3cf2-a8fd-7a3ab26eeec6 | -2.63564 | -51.77708 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 08080195-926a-3035-9fec-946cc7e4f4de | -9.31461 | -46.19185 | 2024-11-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c9bd372-2886-38ea-872c-c8e06763424f | -3.70806 | -51.80948 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f8c7984-61f8-378d-b755-e1de43ff081f | -3.04429 | -48.51841 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38a7c570-75de-34eb-b25b-08923f518b1d | -2.18312 | -52.1329 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf475be0-2942-30d0-9fb5-a522d0c35ccc | -5.44404 | -43.24916 | 2024-11-28 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b43ed156-d4c6-3072-aa3c-275195576e27 | -2.59649 | -53.96996 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a003d066-52c5-316d-a67f-3cb4f0a51153 | -4.37675 | -49.7556 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0edf3eed-abb0-3747-9734-af1e72c6feb7 | -3.82835 | -46.54149 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08459a93-15c5-36af-9fe8-084f0d8320e3 | -2.7974 | -51.8104 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7d5bc61-4063-3901-898f-d9870fc56355 | -3.92934 | -48.15156 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36814dda-adbd-393c-8953-c5c38e927e1f | -3.08612 | -51.02742 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71bffb38-ff78-3410-9b11-7dfd89bef691 | -4.04969 | -50.86911 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1072ef77-78ad-31dd-88f9-dcd9b6b6639d | -3.27676 | -50.6482 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14f35095-6df8-3016-b2ab-9ecd368adf96 | -4.22289 | -50.88135 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df5088e6-c953-35d4-86be-1f852472a6dd | -4.09674 | -46.11066 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1c1bd33-8332-3d0f-b2dc-fed08163549a | -3.29035 | -45.51514 | 2024-11-28 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d5edf21d-ab40-30bb-bbe9-3b010bb1b996 | -3.80338 | -46.59146 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b77a9bc3-1acc-34c9-b37b-5c1e5a97ce59 | -3.41246 | -50.24957 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e242c385-f2a4-32d7-8d86-34ec7796a912 | -3.5388 | -50.18999 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8743408c-8881-3cd4-9f39-fc34cfee48b4 | -3.08436 | -49.20786 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08ae1921-f71e-38fd-b434-f45ff76b556d | -2.86663 | -46.84086 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f38e0ef4-1ae8-3318-9c83-7f9619ee9be4 | -2.81171 | -46.82884 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 621f31ab-d78a-36d4-b305-2e3281b65822 | -3.3684 | -50.8307 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2048e1e0-c8b5-33c6-97d3-4a536833a763 | -3.93594 | -46.71678 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae0b7c3c-a318-3ab8-a6d4-8f4855e5322d | -3.93875 | -46.69918 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f854391-a345-3cb8-9a61-ba48feafe87a | -1.78134 | -52.74649 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5201462-1300-36f0-b21d-a3bf0beadc59 | -3.71173 | -51.81443 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f5e0551-ac97-3e24-b75a-99a4d13371eb | -3.82191 | -44.4431 | 2024-11-28 04:25:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8acc3368-3c48-3ce0-963e-aa20aa2f0efc | -2.87105 | -46.87829 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcfa2d46-6c31-3fb2-ac6e-eac947c6f6cb | -3.47606 | -54.67508 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8ca027c-1d7d-336c-8bd9-fba8338cf48c | -4.05029 | -50.86546 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edd44449-b2f3-32a5-be0c-78d9bf877eee | -3.88506 | -46.67641 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57621362-2d31-3b4f-9fba-c73e76cc13a9 | -2.80498 | -51.59258 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bd3b9675-8023-3176-b6b8-c7b584a75cd4 | -2.71025 | -48.5931 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dcaa4a43-224d-3c04-8ded-8f697dd289ad | -3.30954 | -53.75568 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b31c410-4d12-364f-a9ef-5d18850c67c3 | -3.71954 | -49.9641 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91356567-4e53-3a56-b773-3dc8db7fe4ae | -3.57193 | -53.02325 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f0ae4129-b0fd-330e-9637-82a51ddfe0c8 | -3.7128 | -47.11975 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README70.md)
