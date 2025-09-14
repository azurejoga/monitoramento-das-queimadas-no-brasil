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
| 30d6ce04-47b0-3666-97c1-7b8c8d6d1f9e | -10.34645 | -50.49335 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2dff73f4-5697-3ad7-91d6-990636d6686b | -9.75233 | -46.90398 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f61cd2cb-e11e-3981-b19d-8bdd15823247 | -7.52667 | -47.635 | 2025-09-14 04:40:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01bcc454-149f-3b64-9957-d623109b5b43 | -7.30867 | -43.94295 | 2025-09-14 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 09096b82-aae6-3226-ac9a-1d5a567deb03 | -10.97266 | -49.56731 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8ef948d7-9140-34f5-9819-e5afc054f7a6 | -12.78378 | -48.04045 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44015b1c-762c-378c-af38-83f8a54661a0 | -13.9376 | -44.82296 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8f6b7255-6354-3348-9129-84e7d898588f | -11.47496 | -50.76166 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59ea730c-2a86-385f-a14d-7d395c562beb | -11.46065 | -50.76654 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf7baad5-8623-3905-b75d-c7c16afba1ca | -10.89998 | -47.21532 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 211482b6-8f5a-3f62-b1e8-2babbb826653 | -9.63005 | -40.61142 | 2025-09-14 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.2 |
| a6a3b513-6fb7-361b-ba96-1386e3796e8f | -10.75365 | -44.78502 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2f79bcb-20e5-3efc-97e8-cee7f41999d0 | -12.09215 | -51.38022 | 2025-09-14 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 185bf464-aa54-35e8-8b7a-38ff338ae097 | -7.02346 | -46.00929 | 2025-09-14 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37c585d9-748a-31cc-aca6-09698bdac8fb | -11.46394 | -50.74555 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92a5f7f5-e338-3a6a-a981-8613a67956ac | -10.34808 | -50.48291 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c30d8d75-44e7-3b9d-8373-76fceab4cac8 | -11.4722 | -50.75763 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b885c9bd-4d70-376c-9468-02926f894409 | -12.57987 | -44.87358 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfc1eefa-09e2-3a9c-9f03-bba1de96b138 | -7.22358 | -49.31675 | 2025-09-14 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba6cf6ed-05d0-3610-93d6-74bf58ecabb3 | -6.88239 | -45.63365 | 2025-09-14 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d82051e3-6046-3f68-a5be-af74fd6fa116 | -8.18867 | -45.57506 | 2025-09-14 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe157e98-a53a-364c-8631-b644c8a6cb2e | -10.60129 | -44.32682 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c07812fd-7a5e-3700-aaba-c293f7cb692e | -6.80707 | -51.3741 | 2025-09-14 04:40:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1bb53d75-500d-3ad5-868d-f9534fc98f47 | -9.12189 | -44.83548 | 2025-09-14 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f35ade5f-1db6-3325-8371-3f465673b7ed | -13.28535 | -43.78691 | 2025-09-14 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0688cec-8002-3793-9dcd-6a0f5824ba2a | -11.48101 | -50.76622 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e6ce454a-f683-3c1c-8dda-787e0bbac12d | -13.00761 | -47.99301 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b43033f-af86-370f-9951-64aea2f83031 | -13.5402 | -43.00637 | 2025-09-14 04:40:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e29fa033-90c5-313b-b104-f6fd76a6b3c3 | -7.31346 | -43.93978 | 2025-09-14 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66528342-3ba2-3ed1-913e-194654d999c0 | -11.44069 | -43.55872 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7a13fec-100b-3659-856f-db329b62a2a2 | -7.72941 | -45.31945 | 2025-09-14 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d23649cc-bfb7-3a0a-bcc4-d616fcd4200f | -11.46284 | -50.75255 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12654f29-8ea7-3c85-a622-5c0cf1bfb072 | -7.73791 | -45.3158 | 2025-09-14 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 057cdd14-13a6-34e8-89eb-a05f3dd808dc | -12.97014 | -48.04978 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f7d212a1-34ea-3a06-a6d4-db9a99ba5957 | -13.93816 | -44.81854 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2eb50ed-b623-3e40-aaff-481bec7c4590 | -6.99573 | -44.5489 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75e1ba5e-02a1-3c85-96a6-4eb0e4242902 | -9.72058 | -46.86526 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d7362b5-3b15-3871-9de5-698ba1c8e3cc | -9.02006 | -47.048 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d63a62d-a81e-345a-97e0-8b70610f2ee4 | -7.27183 | -48.6762 | 2025-09-14 04:40:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ec5a765-4728-339c-80b9-39422bd73631 | -12.56908 | -45.65114 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b2128ef-b2dd-3040-bc02-439ee81fd15f | -11.44967 | -50.79345 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 268f8178-7a86-3f47-ba4b-bf31d93685e7 | -10.67797 | -46.2519 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93eda41c-d542-3770-81ac-ae9bc752a722 | -11.78418 | -46.65317 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4a0b34cf-6bdf-3693-9e23-f0b8a83ab83e | -9.02671 | -47.02806 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32be77ee-6884-3978-93a8-52c103c71ea8 | -12.78561 | -48.00293 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 27ba183a-6139-3cd4-9c04-0388308a10f4 | -10.73987 | -46.4375 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b357e43a-6fc0-3d46-8ef1-80d084e4b741 | -13.12432 | -47.12772 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21e1b70d-258d-3444-8a4c-a45085013d0c | -11.49479 | -50.78636 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2c2f489-002d-38fb-ac24-c6a6102657c2 | -11.99615 | -46.65783 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acbdb41a-fe1d-3e53-b33a-534a2d471768 | -12.1226 | -44.84002 | 2025-09-14 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2c366b4a-88c6-3e64-8fe0-bb0e03063f30 | -11.46782 | -50.78561 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61047f5e-6609-37d8-8bb8-b590f0fdb96a | -12.5645 | -45.65421 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d5aac56-a5a0-3cd9-95df-89ce9768d215 | -10.41234 | -48.60579 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b6869d93-6257-3fb4-8965-31dc7712a780 | -11.78039 | -46.65256 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0f50ce10-a7f5-3f7b-b309-bcb3eb562feb | -11.44028 | -50.74534 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a8f13c33-2898-3509-8fe6-b03b04f788c3 | -11.48267 | -50.77724 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e07b7ff-abda-3599-aca1-b5dde3a16546 | -8.94261 | -46.05042 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f50c4932-e3f2-30ba-a09c-977bba0e7744 | -11.55143 | -48.27728 | 2025-09-14 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c48f2b6-0c28-335b-9bd1-cf32abc1cf2e | -12.91292 | -46.5476 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54044279-31cb-3a9d-b069-987206c316fc | -11.21412 | -47.67159 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3f8eeae-e7b2-3435-8cb4-51f06104402c | -9.80236 | -47.8756 | 2025-09-14 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d417972b-ee49-363b-a95d-77176af92e9b | -11.47884 | -50.80172 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 572453e7-9d8c-3011-bf65-d9cfa908a533 | -13.0022 | -47.9799 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa368fee-bb54-331b-8af9-095f96ebd5c5 | -12.97475 | -47.99255 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82211375-4647-303a-bf13-2beef51b531a | -11.45296 | -50.77247 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83d91583-821e-3ac4-87a8-ebf904026c2e | -12.09158 | -44.87655 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 474d50e9-e77c-32fe-b63d-390d52abb49e | -13.94472 | -44.83729 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7579753a-27b3-36a1-94fd-c43048346710 | -11.63329 | -46.92474 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b66e53b7-faf7-3a7b-a46a-b1ea38f73e84 | -11.55433 | -48.28176 | 2025-09-14 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e738683-ffed-30d1-802e-fadfc4f58dd9 | -11.06295 | -43.23554 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 87bc87c0-d418-3502-9821-fa149b385eac | -11.48651 | -50.75276 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| bf1d910d-167e-3615-b0d8-31bbf83c5d16 | -11.49535 | -50.80438 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76c873bf-42b5-3ca6-b83a-9966106a5fe5 | -12.96837 | -48.03674 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23b3e2bb-4e81-37be-9244-a761712ab82a | -12.82435 | -47.95275 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7a3891b-3432-38bd-bb16-abf1ff447f7f | -11.47663 | -50.7942 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9db025d-9db8-3362-8c2a-c23c152c8c97 | -12.95407 | -48.03463 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9e6557c-b793-3eb7-9e1b-87f50bebc9bb | -12.78618 | -47.99903 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b2d05954-7769-35d4-bd26-48b1f326dd2a | -12.46852 | -53.84425 | 2025-09-14 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95d48872-d42b-36dd-b6c8-51497cab8d6b | -8.95261 | -46.11414 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9925511-d818-3dda-81cc-4515562f9b4d | -8.10797 | -50.16603 | 2025-09-14 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee166834-442b-3f8f-9f65-5b85830fcf2c | -11.38632 | -47.3394 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 333dfcd0-c6b8-3ced-9bc2-4a2e450db1d7 | -9.12755 | -46.95502 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f34c05a-9eca-3789-bb4e-5dd66f4fbfe1 | -12.10223 | -44.86197 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60f4cad2-19d9-3684-9ce9-1a6897fa439c | -11.47828 | -50.78371 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05848e00-6f12-331f-98b8-cf9dbe4147a5 | -10.40497 | -48.60838 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e21495f8-199f-36a6-a124-7689a3705dae | -12.08733 | -44.87583 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f321bdf-1ae4-3e7e-9402-08d97d9cd50f | -10.97499 | -49.5969 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f59ff4f2-f95c-3c10-bc85-31338c4b7172 | -10.79285 | -45.98539 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37bd1ca1-01b5-306c-9c19-ad397778d487 | -7.87779 | -49.5052 | 2025-09-14 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c417789-74c2-3f24-9e25-381b662eba20 | -11.37902 | -47.33852 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d7e8a58-99d7-3e4d-a425-d75b224ea85a | -7.51011 | -44.67525 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1586740e-643a-3188-b865-0eb82558b68c | -12.81841 | -47.15525 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0848809a-4242-3830-a3ed-a42ab5c758c5 | -10.53434 | -49.78853 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01c256c2-42c1-32c0-bb0b-44c13abd1750 | -11.47494 | -50.74014 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0b9d3511-9d52-31e1-8337-991477038a33 | -6.56587 | -50.88041 | 2025-09-14 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d7703a9-eb99-3178-92ea-2259eef88ef4 | -11.48541 | -50.75975 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| aad7e3bc-68c5-3f20-8bdb-92a3c75632e1 | -11.47003 | -50.79314 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50366df5-ae71-32af-8f38-250a4c13f96e | -11.45131 | -50.78296 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9aeafd8-8386-3c7e-a904-957ec4cae7fe | -11.46984 | -48.70632 | 2025-09-14 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e43bf390-568d-3ff5-bb1c-08a3066e4e2a | -8.11348 | -50.17401 | 2025-09-14 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README37.md)
