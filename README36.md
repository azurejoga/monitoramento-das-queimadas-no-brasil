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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dec57cb7-056b-3716-aa6a-99eb5d7e625c | -13.29332 | -46.92773 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9aae4343-a288-3a6f-9fd1-552a67313624 | -5.74904 | -50.21091 | 2025-09-02 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d6dfa78-27ce-3707-8256-4fb7c8cea029 | -7.57852 | -45.2151 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e894190-d90b-335b-9ea4-d6cff17aa63c | -8.85641 | -50.58813 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8794cf36-d24a-3e75-ba11-aed0d543da1f | -11.61664 | -46.84373 | 2025-09-02 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39f2a054-de2a-310f-98f8-39b5eb33e91b | -6.04254 | -52.1802 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ccaf864-1590-3633-a928-9c36fe1f5924 | -11.66109 | -52.21724 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 6cbda15c-2a77-3f6c-8185-60ff41e54907 | -11.86319 | -46.71091 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56eeafd5-0064-31d7-b8a9-75db15fb72ae | -7.09175 | -45.34071 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95675f21-1ec9-312d-9e6f-e892befb9f5b | -9.27979 | -48.55929 | 2025-09-02 04:14:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5801b13-f7f2-3a3f-bd68-74cec4c0caea | -13.69495 | -46.88011 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8aabdd73-d5f8-3c05-b0a9-d90d519f4f8e | -6.81633 | -52.81905 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d94569cb-4485-3596-b79f-5d8e416e2ed9 | -8.85661 | -45.72559 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89d428a7-3064-30f1-ac06-140de9674966 | -12.77867 | -47.65965 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bece9bb2-f8c2-3d0d-a2a1-2d68def26cb3 | -11.38035 | -43.61458 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05c34e50-d485-37d6-a211-b35e9baed914 | -12.61266 | -48.19273 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b898330d-cdea-32d6-b61b-012cbb016588 | -10.44631 | -54.77251 | 2025-09-02 04:14:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ecfade9b-6178-3a16-b485-e88b3a78b1e5 | -9.61094 | -47.83758 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1abc759-3cff-3034-bb7e-579ad3d1b2ca | -8.70793 | -50.43859 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aa9ef0d-26d8-3448-a52d-745ea537e6fc | -10.26252 | -47.52364 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b75e9298-a1eb-3b6c-bca1-1e3ead4c68c6 | -13.53757 | -46.9811 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e735b067-45d6-3283-88fd-69acdb2528be | -13.72454 | -46.9311 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc80654a-7714-3c95-b580-393b8d270610 | -9.7165 | -48.95013 | 2025-09-02 04:14:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d15a405-4892-3569-8045-16675beb80d8 | -7.87099 | -47.97096 | 2025-09-02 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d11664a-2866-3cc0-b6e4-bbcd34142f24 | -9.74282 | -48.96566 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 501057ec-6c50-3b50-8bd9-5696dd9bead2 | -7.56926 | -45.22895 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7838e7b-6fba-32fc-a97d-adc2ec59072a | -11.5426 | -44.84788 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1344d782-7da1-30e5-be3c-38fdaec1abc5 | -6.99816 | -43.21568 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e311ee2e-490b-3b79-9d00-e2bc3dd70d36 | -13.27848 | -46.88922 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83b3b7a0-fe29-3127-8f79-a0f27d6d5d5a | -8.84311 | -45.80873 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73aa5a65-9103-3989-afd6-50a9b0bed468 | -11.67674 | -52.15878 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d2f6da1b-baf0-3e21-9834-a690777e8d7c | -6.78943 | -52.80854 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd885569-d54b-305b-a9ae-ad019b75a55c | -11.66409 | -52.2008 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| e605e691-0b2b-37f8-beed-89cf4669e65c | -9.4457 | -46.77647 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74427d24-917e-31e0-a7e1-6d159b8952ab | -12.61223 | -48.18069 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b97ceb2-a0fb-38ad-8695-b79d2262f782 | -8.35913 | -52.53189 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d7f2235-569a-3351-b6a0-01212a256993 | -14.0481 | -44.59504 | 2025-09-02 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4f31479-b002-3e40-b116-69a4317e35b4 | -11.05755 | -45.39287 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 43baca83-ada3-3dda-8667-7425c4148323 | -11.94706 | -45.77255 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33da19a5-1c46-3677-8360-70ef7c79d5ee | -11.64863 | -52.20353 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 3fa877d6-6c81-32bf-b11a-181d2fd2be8d | -13.51514 | -47.00914 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b44e40d7-9e94-391f-b32c-b53e43b8eeb0 | -13.40047 | -47.0661 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa54546e-8990-32df-a014-7504b453ea57 | -10.05423 | -48.13086 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a7d4034b-d1d5-3f1b-91dc-84f142028b23 | -9.64875 | -47.79918 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a3fc02f6-aef3-3efa-b201-0c005b575366 | -10.58285 | -44.85776 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6ebb2ae-236a-343f-81e5-e21ba33d698a | -6.7833 | -52.81138 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6d04659-e2f1-377d-bb96-e0707039d29c | -11.42649 | -55.18744 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4919d5f1-371b-33bd-b6a6-a4c287f0f91c | -6.62056 | -43.73492 | 2025-09-02 04:14:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be269b15-b375-31ef-b20f-1d6c2845d77b | -12.61733 | -48.19555 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aef0498e-1e99-32e5-a1d9-052983725a64 | -9.71589 | -48.95368 | 2025-09-02 04:14:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d06fb210-099d-3654-90cf-ebca1dda1894 | -12.7611 | -44.70369 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4217ed64-4f6f-3f83-8a26-37e1af3d8e96 | -13.28987 | -46.92712 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3472d9a-b8d7-3ab1-990b-77c1a5647e87 | -8.43536 | -47.35061 | 2025-09-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f923dfe1-a614-3ccc-9f4e-f8eb25d53561 | -10.29109 | -47.51068 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cc710f1-ac58-3549-ae12-bd0cd2e39830 | -7.4685 | -44.80878 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a97b8c9-9155-31c5-8296-9fa3ac9a0ada | -7.5558 | -45.70216 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1de8295d-a418-3a37-a8fe-d56c35124497 | -9.73357 | -48.97136 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 363681d2-8ddd-31ef-9fc9-393b106f744d | -11.35662 | -43.67954 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2cb05f9-2216-3510-b736-d5c0aeb5b61e | -11.6673 | -52.20293 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| f4b76f51-0018-3975-85d6-9186569ee453 | -9.07253 | -46.57875 | 2025-09-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad21d9ff-6d1e-379a-bd4f-6f3fcc7c5c6d | -10.32775 | -47.82472 | 2025-09-02 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14150615-2d62-36e3-b195-9365afb8b095 | -10.05687 | -48.09257 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 2b33d69e-9e1d-3d74-9122-c6864e77c404 | -6.82395 | -52.83928 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 955d0e70-3cec-3a88-8008-b19195013d29 | -12.79938 | -48.07034 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fde97094-8a4b-3545-9e1e-dbedb509302b | -12.99587 | -48.10602 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0047cacc-8650-3fac-9f33-00add29f1078 | -11.0609 | -45.39343 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 87488e3e-e931-3c8d-be11-f62ad0fe028f | -11.31068 | -55.21696 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd18658a-5011-3d7d-a4f2-de50a05272d5 | -10.03418 | -48.06564 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6cc86dd-6b12-3619-b88d-6e331acb88d3 | -11.09433 | -44.63369 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 632c0073-073f-3054-93ba-3ef10e0dd12d | -11.37032 | -43.54765 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b4e86f3-102b-3a2b-94e1-061fb75e2634 | -9.73417 | -48.96781 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f658902-c9b9-3762-9858-c0ae7114f3ce | -6.97902 | -44.34187 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ada91a74-bb0e-3016-adf5-6dab73de182c | -8.0011 | -44.0482 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f59bf08-6717-3f53-9e99-5dbed4087e6f | -9.44926 | -46.77708 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3065d894-fe43-35cd-a171-8f6f3b21e953 | -13.28211 | -46.90985 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c504e34-f880-36c5-bc7b-677bfcf85c67 | -6.9259 | -45.56418 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9755431a-4214-378f-b91f-8d591d7902bf | -12.56119 | -44.78645 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99c64e41-084a-33fb-b44f-681a7bcc72f7 | -7.49791 | -45.34374 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84ac2587-1fd3-31d3-947f-6ef4b91aa5ae | -6.78203 | -52.81859 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 693342ab-d2db-3c51-8867-96013845de35 | -13.53563 | -46.99279 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70c7d1cb-9477-347c-9b76-2d6230a27f19 | -12.59294 | -48.20512 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b517a40f-09a3-324a-b757-2aea8e4566dd | -11.39214 | -46.86423 | 2025-09-02 04:14:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00c1420f-9103-3ad2-9ea0-42facf23cafa | -11.65159 | -57.36159 | 2025-09-02 04:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2e59d962-a483-34e9-9788-3820e64bd5a1 | -12.61439 | -48.19044 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 4b7364fd-c052-3786-9a3d-981eb969531e | -7.19423 | -43.26474 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5648fba0-b0f5-3de0-8fa2-d16ee4ebf3d0 | -6.94207 | -44.65802 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84061946-88f9-3924-ba33-f520b687bb5f | -11.67274 | -52.2081 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 816942bf-3f1a-3788-9bc0-0060d683afae | -12.92927 | -48.10055 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63dc4447-6666-3cbe-87b3-9ba48518545b | -11.92319 | -46.45274 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dabb05f-2a5a-32e6-8bfe-d5ef8a7cb12f | -10.03877 | -48.0616 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4021619-336d-3bcd-9196-e1c99a26913a | -12.85946 | -48.04746 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f06673fe-6f2e-31cd-a421-a8f2606d1716 | -13.36545 | -46.32516 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eeb616f6-cc57-37ca-9ed2-58be0c19ef03 | -6.98683 | -44.33594 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33f3fe6a-d0f6-3b27-8aec-a33f0cc9d3ec | -8.8727 | -45.77874 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5bee277-2875-3b4e-8f67-17ee4c52a509 | -11.34001 | -43.67691 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e49e46a-e0b4-3c7a-bc73-655e67952df4 | -6.83331 | -52.8187 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93f1ef49-ca37-3643-b8a3-da577c639bbb | -11.67648 | -52.15471 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6dc571d6-07cc-3b60-8b93-6ce69cf2af8a | -12.97762 | -48.10286 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f6d6c73a-206d-38ff-8399-b213e2f58340 | -6.82242 | -52.81657 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01a23959-062f-3fdd-96b6-bda1f4e770ed | -11.93649 | -50.61429 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README37.md)
