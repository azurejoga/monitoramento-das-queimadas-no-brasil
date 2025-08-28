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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12b1b9c2-82a5-300b-b4ba-f3b492bde4c9 | -9.00748 | -48.72636 | 2025-08-28 04:08:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fea6e7a3-84de-30bd-80e0-ac08d79d159f | -8.27833 | -45.17322 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.5 |
| d5e1a0e6-1189-31c3-ae7d-54d18cdf80f8 | -11.55819 | -46.341 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c85bf31-1d04-39e4-b699-054032369c31 | -14.24086 | -44.12029 | 2025-08-28 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 228e873c-b293-37cf-9476-e366c581e2c1 | -13.45636 | -46.98163 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 849cb56d-bfdc-3c45-ba21-b10d0756cd84 | -8.29108 | -45.1411 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dc254703-fd65-3174-b4c3-ac817517e11b | -13.39113 | -46.86107 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 012e29b6-5352-3065-9db2-0db7134a9372 | -13.51422 | -46.88015 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4960580e-cb40-34c8-93f7-2949236d0fd7 | -11.83278 | -46.79941 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b726d307-8e85-357b-838d-1b53dda64c52 | -8.85278 | -47.15669 | 2025-08-28 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5b99b50-bbd2-34e2-b0ea-ac1af72608f3 | -11.80278 | -46.79379 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ecec0f3c-8fd3-3824-acae-eb589ad634ef | -13.17968 | -45.28902 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 77e9bc3d-aa57-3ba6-b048-5f3d5462627b | -13.50805 | -46.85722 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64b2db3b-347c-320b-91e4-a2724aeb33ac | -13.44035 | -46.96351 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29b8da90-9958-3417-95a4-091af24364a6 | -7.75199 | -44.0515 | 2025-08-28 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47e87251-9fbb-3108-a52c-936412392fb2 | -9.51149 | -46.71045 | 2025-08-28 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6ec291a-bf2f-31f8-ac50-17b6cd19830a | -8.08913 | -45.00325 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51219fd5-1963-3aa1-a36b-41a91b34a143 | -11.32745 | -43.51725 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe2cacc0-7bd7-39d8-b7c8-e5fd4a1bc834 | -8.29979 | -45.15554 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b48f5841-046b-3218-90bd-e033c3e6f95a | -12.96088 | -44.57211 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 887055e4-3de4-3e38-a188-cf347211959b | -10.32656 | -46.7965 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff456fe9-84e4-356d-bc46-ef5e2c2e29b0 | -8.27473 | -45.1726 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 62588727-d96e-3f37-93c1-c2eb1cbcd2df | -8.2919 | -45.15847 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0081a69c-0dda-3d4c-b7c5-9d63d29249c1 | -7.7658 | -44.05368 | 2025-08-28 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de9159f8-a045-3c1b-9d96-02b781d0b9df | -11.57188 | -46.41629 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a26ad33c-9441-3274-a0a6-4ed74352319b | -11.24391 | -44.98143 | 2025-08-28 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b3c1079-5a89-3172-b2e9-98e4c067f155 | -13.43291 | -46.85234 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75d2c939-015a-3313-98d5-940faaa58eb4 | -11.65214 | -44.87163 | 2025-08-28 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24415a04-63a7-3bd3-bc77-761bf62712bf | -12.92835 | -46.33617 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0839c293-259c-3460-aa23-eeec6714e904 | -8.08761 | -44.99025 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94eb7985-d244-376e-a651-231e60954af8 | -13.08616 | -46.3165 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18e41712-a40a-3d58-aa62-58dc52188d25 | -14.23349 | -48.03047 | 2025-08-28 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d895e7dd-8f84-394c-9515-cabf734c312f | -12.4328 | -45.9609 | 2025-08-28 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 06dd9f83-47b8-3f4b-a9da-34c7d380f522 | -12.80251 | -48.14703 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f7cb34e-8b28-38f8-9448-587e9d6daa1f | -13.38587 | -51.754 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5f1859e-3e6b-37fb-8b0d-c6f46ff4f8e9 | -12.79121 | -48.16401 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 983ae74c-d2a1-3c70-8721-50068cb903ee | -13.62791 | -48.21453 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a78ea95-2fd0-3b48-bf52-92a7d9875e91 | -11.22999 | -55.06302 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8522ddf-e786-36a1-80eb-19ab4338d5eb | -11.57271 | -46.3891 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20e9aaca-fc76-3e02-9f3d-23d551545cdb | -13.50764 | -50.81224 | 2025-08-28 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42ed146b-94ff-3d6c-ab69-c9059d734e4b | -8.25171 | -45.17722 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 655abf19-fa4a-3b5b-9303-154907d2efad | -12.89351 | -48.10788 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bae66ed3-f491-3297-b8c4-fca9a9398e6b | -13.46957 | -46.99396 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a86532f0-3008-32b2-a790-9b46d5acaacd | -8.45026 | -43.65868 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d3efbc1-7858-3735-b7f8-15c393c3babd | -8.44106 | -41.44911 | 2025-08-28 04:08:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| bfe6da63-30bb-345e-ab90-f577ab49ceca | -7.94588 | -42.65071 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5245b26c-9f3e-3ee1-aa80-3230e6490031 | -13.39994 | -46.87638 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42c24d9d-9240-34f5-be2c-c92d33fd633b | -13.7329 | -51.90665 | 2025-08-28 04:08:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dfd94cf-ad05-39d0-8311-398732b658ea | -12.56038 | -44.81091 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dad0d6c9-dc4f-3270-b730-63e9584f835f | -11.64808 | -44.87484 | 2025-08-28 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bac40453-0a38-319f-9394-0aefd56f99e9 | -8.85937 | -47.19099 | 2025-08-28 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc7899fa-5e35-3bd0-9e76-fcb0378bfa8d | -12.81514 | -48.1459 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49b07f7a-df0c-3e2f-aa2a-974bc84ca00b | -13.83371 | -46.68415 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 110413a8-8d1c-3c86-8431-129ed6d29426 | -10.54231 | -46.69106 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07436aed-8339-30ff-b981-f5b61a709d08 | -8.28194 | -45.17382 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f16d9a36-f270-32e3-a95a-086fba7b8156 | -13.18032 | -45.28517 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 703c181c-edcc-347d-a3fe-605e39c0f357 | -8.46248 | -43.69076 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 950d936d-cd7e-3528-b69b-5d0ff2d57c65 | -13.63097 | -48.24337 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d962089e-906d-3031-bb7f-e2f123d9f99d | -9.44937 | -51.96301 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| eb089151-12e6-301b-b71a-1c7b64ae059d | -13.47425 | -46.85497 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75fc8c35-4584-31f1-8679-bc7021c8efd1 | -8.41043 | -47.37788 | 2025-08-28 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6249bcba-41bc-3e96-8ffd-ef0a02edb412 | -9.1901 | -44.43773 | 2025-08-28 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| becf6e5d-bf2b-3d21-913f-c0b081585cc0 | -12.90491 | -43.57278 | 2025-08-28 04:08:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 318b9820-9781-3993-8328-5a31e15f1070 | -7.9498 | -42.62616 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89165931-d611-3dea-8de5-a0ba1871be2a | -13.47618 | -47.00009 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a916deb-949b-352c-87dd-1186bd2e8b32 | -13.5179 | -46.88086 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c88478d5-d4a4-3be2-8256-8a221f3ce609 | -13.44106 | -46.84921 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03c8d509-e311-3419-a7d5-3a4400804c6e | -11.32462 | -43.535 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5104cbf-b760-3f27-897c-340dc8661a8e | -13.46662 | -46.98881 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e369dac-d30a-3dee-8acf-ff5980e06027 | -12.77935 | -48.9858 | 2025-08-28 04:08:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97131958-9323-30d2-9bac-bd4a8ca83bc4 | -11.74807 | -49.08466 | 2025-08-28 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed42c363-e44b-3593-bbc2-cf54edd63087 | -8.48577 | -43.67577 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f742306a-cf4d-3ed1-a3d0-0c229a485e17 | -8.27043 | -45.17613 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 037b725b-da20-3650-9ac2-5f6c57ba5d28 | -12.96425 | -44.57269 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dcb84f2-46e4-327c-ae3b-129e9d893f13 | -11.79447 | -46.79704 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 813c0309-6907-3594-972c-16523fbdc744 | -12.96028 | -44.57578 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2cba3486-01b1-3ff7-a870-60bc910a7357 | -13.42869 | -46.98678 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0918af1a-2d9e-3187-b72f-fdff8825da91 | -10.53988 | -46.70525 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99e0d69a-19ff-312c-980d-fe2cebbd89e7 | -13.08526 | -46.34338 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 17b3d03c-76f4-362d-88a6-6af2d0c09fe0 | -12.41192 | -46.48335 | 2025-08-28 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bc83e11-347e-350e-b522-6aaf83eeafb7 | -11.65558 | -44.87224 | 2025-08-28 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1724b1d5-5c5f-35a7-935a-4c424672eaeb | -13.37884 | -51.75657 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c5697f0-9c6a-3cfb-926b-9bd42fd1a393 | -8.29275 | -45.17565 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eebc0ca0-7954-3b52-af53-8297a8e96b5d | -8.72237 | -45.34185 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a1f7c98-0d46-38b1-a47f-9d7c9fcd0633 | -12.18122 | -47.18776 | 2025-08-28 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9170b2eb-bc8d-3fd8-9dfa-c208e69d1529 | -15.00607 | -41.90501 | 2025-08-28 04:08:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 44d803dd-3adc-3be3-a562-1b99bd79b182 | -13.45268 | -46.98077 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b749013-498e-3cf2-b41d-55fd6946cf6a | -13.59635 | -48.14941 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bce81713-60aa-3b29-93c6-553f605e8f57 | -12.7145 | -48.1712 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e1584b1-b1cf-3be0-88cc-8fc82badd321 | -9.6713 | -37.13788 | 2025-08-28 04:08:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 89ff46ad-bc79-3254-91d9-ea73fa491c8a | -11.21823 | -55.05491 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 39de3d8e-61f2-314c-aeef-b00e3d5bdbe7 | -13.42386 | -46.97046 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62f60cab-0b36-3353-a52a-427f160fb244 | -12.88359 | -48.1172 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51307339-efa3-3bd1-9ad2-b5f9e935a66f | -11.91942 | -46.70388 | 2025-08-28 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65799f05-122e-3b0b-a45d-e98b3f9e270b | -13.18096 | -45.28133 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37a244d2-7814-325d-9246-56a176f82115 | -13.17752 | -45.28073 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa7480f8-b525-308e-b49e-740abf187219 | -10.52545 | -46.69797 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 51cd75f8-0e26-328f-8741-48f40f235055 | -11.32851 | -43.532 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dd99ba2-4d78-3f93-b8f7-1df54281e739 | -13.51313 | -46.87213 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d023b9c0-2445-3d39-abbf-62d4c924503e | -13.60202 | -48.22136 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README38.md)
