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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acd6858e-ec1b-38c5-823c-416091528633 | -6.01341 | -46.69328 | 2025-09-06 03:49:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5695854b-8eb8-3f7e-8b0b-60e6208377e6 | -6.80615 | -45.65302 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8531984d-5892-3ab1-96e9-a4d678026af8 | -7.33324 | -43.94455 | 2025-09-06 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c238ce37-c662-3704-a07f-cb7fa6d7ceff | -7.20848 | -46.19951 | 2025-09-06 03:49:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c068a91-fc2c-3075-a9e0-0a7118bde445 | -8.63903 | -45.74757 | 2025-09-06 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8d295c2-1fa4-31ea-8a31-8c7fe503801b | -9.7042 | -49.48777 | 2025-09-06 03:49:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 93d84069-cd9d-3560-af04-d5c84e2b69cd | -8.36667 | -48.27172 | 2025-09-06 03:49:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6eaeb911-b6e7-314c-98bc-cf3b1da9ce37 | -12.89709 | -48.88752 | 2025-09-06 03:49:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53700770-211d-35a9-8a24-9383a194dc40 | -13.59017 | -43.3565 | 2025-09-06 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ed93808e-9716-32e4-a75a-570e1c0e85de | -10.59895 | -44.32771 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c049392-9cb7-3d5c-b289-ccaa854e1817 | -10.03683 | -48.12955 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a3e47361-bf78-3afc-b424-2f37a5c21d5f | -12.72708 | -45.09742 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae3618ba-f4e1-3389-9ea8-2cd80ff2b9c6 | -6.01966 | -46.69038 | 2025-09-06 03:49:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6b7e543-8447-36c4-9bac-3e0dbb848cf5 | -10.31539 | -46.40832 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35f9b812-493a-36d3-8ac8-8b4ef395ef1a | -6.53807 | -49.50216 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 70a3bec3-604c-37c0-bdd5-f1f182e95145 | -7.41837 | -44.946 | 2025-09-06 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d869901-b883-39a7-9b45-179f00c7b429 | -12.68481 | -45.05199 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7aa3b39d-03f5-334d-a6e1-4ddb22c4574c | -8.75108 | -44.22972 | 2025-09-06 03:49:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3018eb74-7964-3864-adf6-6e3c7d895441 | -7.76491 | -50.7398 | 2025-09-06 03:49:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1da1abe1-1f84-31da-803e-7c01dcc321e8 | -8.43884 | -47.32232 | 2025-09-06 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a2fba6b-7d57-3c55-b3e7-ab151fb7e14c | -9.78425 | -46.91167 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecd05edc-b5f5-3a7d-9b40-c65fc40145a0 | -6.45542 | -44.67604 | 2025-09-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| feddc1b4-0518-3ed7-acbc-68bc3601e936 | -7.21618 | -43.99308 | 2025-09-06 03:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40fa89a7-789f-3084-a326-d21a2ecc2d97 | -12.00993 | -47.77808 | 2025-09-06 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0a14eaf9-7bdd-3d9f-bb6a-9060a1448729 | -11.9306 | -46.66578 | 2025-09-06 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66600b37-5bdd-3c4c-8a90-8acff6ab3d44 | -6.01901 | -46.69406 | 2025-09-06 03:49:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c603832-dd3c-3776-938b-41ba19774346 | -7.04917 | -44.35323 | 2025-09-06 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 559f7945-2b8a-374d-a656-1871677363be | -8.77936 | -49.63823 | 2025-09-06 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a36f32e5-421a-3d8d-9805-83631127cb18 | -13.06178 | -47.10822 | 2025-09-06 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bc5ec3e-ab67-3253-b26d-adeeb98d46f3 | -11.39827 | -43.62132 | 2025-09-06 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2664bc2-46fb-3fc0-85ed-0bdec441bf57 | -11.93504 | -46.66971 | 2025-09-06 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a746662-8a39-3a2f-a05d-73223de7d002 | -12.00926 | -47.78154 | 2025-09-06 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c0b630e-8cd8-381b-aeb7-4a5800c5a0a7 | -6.3995 | -46.09446 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7196d488-085d-37fc-ab97-d77f4e23cec1 | -7.98099 | -44.50956 | 2025-09-06 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b06fba59-bdc0-3153-a009-f9df53f64a32 | -7.0091 | -44.95134 | 2025-09-06 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b33a0f1-4eeb-359f-a6f1-93908274f28e | -8.10006 | -45.32655 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| efad3ea2-18e3-3ce5-bdbb-8d0d3d11d648 | -6.99689 | -45.64816 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24b8806e-6d68-3ab1-ba57-b64f6d3083b4 | -8.87873 | -47.25401 | 2025-09-06 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9721cd37-5065-368a-b1cd-84aacc2f9424 | -11.13716 | -46.34966 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 471942ba-4ea6-32af-b50d-b8a483d20f0a | -8.3483 | -46.95169 | 2025-09-06 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6600411-f96b-3db7-962d-31166562188c | -8.02074 | -45.42852 | 2025-09-06 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 779fa941-0f3a-31b1-80ee-76dbf2f3fc5e | -12.89599 | -48.88391 | 2025-09-06 03:49:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d32f0152-794e-3eda-9395-aea88199c2fd | -9.05735 | -50.45377 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 69f02138-61ca-350a-8fc5-48aa54305040 | -10.77154 | -48.2743 | 2025-09-06 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4460c8ef-a5d0-37f0-a709-3717bef7719d | -6.54356 | -49.51852 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a71b2470-20a3-341a-881d-ec4ad0a8deab | -8.8779 | -47.91947 | 2025-09-06 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddf21fbc-9e73-3ff7-92c6-c7f77e9a2de2 | -9.87809 | -46.54607 | 2025-09-06 03:49:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb77420e-d8c5-33c9-8fc7-b38c73ab9f88 | -7.3037 | -43.72871 | 2025-09-06 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4fb5df75-aabb-3e6c-a330-830ab4b5e8cf | -5.72776 | -49.28561 | 2025-09-06 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e82f81c1-9449-3f6b-9f6a-52a3375b2860 | -8.08652 | -45.31743 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d91374f4-7749-3f2b-97bc-8200cc824ce6 | -7.9907 | -45.47572 | 2025-09-06 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c37368fc-580f-39cc-ab08-f7c0c29d60e2 | -10.97196 | -46.81778 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d830789e-205e-3287-98a8-a3000aa76781 | -6.87351 | -45.55423 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 75b4dc74-8176-34e6-b47f-058dcd3171ce | -6.01276 | -46.69698 | 2025-09-06 03:49:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a153f6cd-d3df-3b6c-880c-150544be0048 | -9.17072 | -40.5685 | 2025-09-06 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 60cb856e-aa54-3beb-9c36-ff2ef02f9cdc | -9.68087 | -51.08976 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5214665a-8ca3-3a5d-8d72-7b7a92340bcc | -8.44289 | -45.03342 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e49cc50a-a16a-3921-bf35-4eebbf1b4cfe | -13.66633 | -46.95415 | 2025-09-06 03:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cd25cfcb-1153-3e9a-a4f4-f7c369661391 | -7.17153 | -44.00246 | 2025-09-06 03:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b06e94fa-6195-3361-bc78-846d1626ae1d | -13.28433 | -46.81189 | 2025-09-06 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b2a53c1-3778-3ab6-b28f-7e49befc387d | -7.80331 | -45.4256 | 2025-09-06 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4755fa1-938c-3708-ad86-0252b2798e98 | -9.17657 | -46.02863 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2721206d-2239-3bf6-91a8-a21bf0d492dd | -9.70322 | -49.49281 | 2025-09-06 03:49:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| e6be0cc7-c65a-3a1f-b14a-794b8b130367 | -7.76374 | -50.74589 | 2025-09-06 03:49:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc198d35-70d9-30df-b58a-6b3bcba90629 | -12.53099 | -48.06172 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6465a323-bb86-3c34-aaa6-d0e3e058b69c | -12.01529 | -47.77923 | 2025-09-06 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 635b7474-8dff-3276-8aa1-d222f63c3093 | -8.69537 | -45.28022 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46bd31ed-917f-3614-947b-d3d649d9a5fe | -7.35175 | -44.32174 | 2025-09-06 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5d338b9-e8f7-3155-b813-a5d7cd63af23 | -6.64665 | -43.41679 | 2025-09-06 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55c8227c-df64-3eb7-9c11-792219dff648 | -13.2893 | -46.8127 | 2025-09-06 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bbca0c4-ad54-31c4-be52-cbefc4f2ece9 | -7.34812 | -44.32277 | 2025-09-06 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8206fb6a-f1a7-331e-bb26-7269a96d3d45 | -10.03614 | -48.13328 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0bc06ffa-36e7-3cb3-bf00-eae42d243e4f | -11.3836 | -43.54531 | 2025-09-06 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 519875d4-e53d-38da-9d0e-f27633f0bff1 | -7.34147 | -43.95078 | 2025-09-06 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 523799c1-e495-3556-ab80-84d6918f19ab | -6.98849 | -45.42768 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4aab8fb3-6388-3157-9dad-843e99f75947 | -7.33776 | -43.94532 | 2025-09-06 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae1fbc5a-598a-36ad-b0b4-77083ef55b9d | -12.01057 | -47.7747 | 2025-09-06 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eee70321-6bf4-3e27-8fe8-bac3751df093 | -9.82616 | -46.53835 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6bbc52d-79b1-323a-bb06-9d7cd62261b4 | -7.32662 | -48.50361 | 2025-09-06 03:49:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2430d07-a810-325a-954b-4c10a9b43c09 | -12.56009 | -41.30623 | 2025-09-06 03:49:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4689b8df-894d-3bf5-9f4d-91adad8a0677 | -12.98624 | -48.04789 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fb78af4-389e-30ce-91ee-5c295cc2a796 | -13.66049 | -46.9578 | 2025-09-06 03:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb846d09-16b5-321a-aefe-6aa79af9471f | -8.77298 | -49.63698 | 2025-09-06 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aceeea98-df1f-3b11-9103-167bd9d6cc90 | -6.64224 | -43.41601 | 2025-09-06 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30ad99bf-96d5-319c-9666-c379c1ce03ca | -7.23474 | -43.86037 | 2025-09-06 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 57177207-810e-390d-a189-06f4d2a7d065 | -9.68409 | -51.1097 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 786319eb-77ba-356c-84e9-86233a23a04f | -10.08728 | -48.09071 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8173ac6c-492d-3d1f-b9c8-d3a1beb7c6ca | -9.69094 | -51.11227 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acf98803-677e-365a-8283-5f5baf5a527a | -6.54002 | -49.5006 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d2ea92f-a421-363b-909b-52c3c27a4948 | -9.82726 | -46.53241 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80532e75-5d23-346e-a93a-1df913d8e778 | -6.53701 | -49.50774 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 98d7acc6-f00b-373c-b058-ebfa777a9e36 | -6.59452 | -44.55605 | 2025-09-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 118a994d-a59d-3cc0-948d-090bc90f365d | -7.96497 | -44.94855 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 507d8166-1a69-3bb5-9491-cf215b38dbfd | -6.59067 | -44.54991 | 2025-09-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ee65d3a8-2173-3a31-b589-ac93121e71aa | -6.91552 | -43.81351 | 2025-09-06 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e34aa449-62d9-3a02-8cc2-f707815bffdc | -13.97991 | -42.58691 | 2025-09-06 03:49:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4dcb073f-c917-36fc-b31a-8a549f33cb0f | -12.9322 | -48.02621 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8335dcd2-a8cf-3271-8811-359f31cb6b8a | -12.5405 | -48.07101 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d3d9b60-3a56-3717-95bf-af51b3e1a951 | -11.62966 | -47.80112 | 2025-09-06 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d680ee50-8beb-3608-809b-98b22935b465 | -12.69007 | -44.97408 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README25.md)
