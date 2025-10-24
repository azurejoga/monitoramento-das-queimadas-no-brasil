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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8df8223b-42f9-3c98-b090-d8f9715076e9 | -8.20619 | -46.98368 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 04b4773f-e8de-3c50-988b-c932e00c1cc8 | -2.95623 | -49.14707 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89a205e3-aa18-38a9-8827-047b1e07f829 | -7.55939 | -47.36688 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 93d437d8-e760-35a5-9856-96487e8104a4 | -3.15567 | -49.1752 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b45ae8a6-06af-3ca9-bc40-2963e26278cc | -2.86773 | -50.71907 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54701083-2fe6-3111-97ea-417aafedc131 | -7.64063 | -42.30103 | 2025-10-24 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f6e3322d-b052-3a14-9ed5-8289c5e3182c | -9.60132 | -46.90805 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7fbb3cff-6817-3c51-ac5c-49ada5957079 | -3.01704 | -49.44871 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b6602d6-64f7-34d3-b030-0c025408e834 | -10.04224 | -47.07986 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89b579f4-c9d6-3e25-9814-bd63124953ae | -9.236 | -51.83801 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f899df89-dcc9-3ce9-bb54-77ea130c76c8 | -7.62539 | -42.207 | 2025-10-24 04:38:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e12d34aa-b464-347b-a911-92237724e6e1 | -3.98697 | -49.90734 | 2025-10-24 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b303b4c8-12d5-3e88-a34a-0270c73c8e59 | -3.13594 | -50.6174 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e006f8b-8e93-3e79-9c00-6b592bd4d51f | -5.62611 | -42.59027 | 2025-10-24 04:38:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bfaa3e2d-7f51-39f2-a562-3cc0287b4710 | -9.01015 | -47.84084 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04fbbb7b-b96b-345b-a544-9578094d9c5d | -2.81696 | -49.14616 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1bf49c00-bb76-3ca6-9e9b-b0a63a6b9b6c | -4.03767 | -51.15981 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4958101e-32ce-35b2-83b1-eaec168b047d | -4.91437 | -47.32492 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27af0a55-9d79-31b2-b8e4-d32cf3736384 | -10.00055 | -48.09639 | 2025-10-24 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 445ac633-df64-36a7-8310-149077ea8c08 | -7.8247 | -45.37698 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5deae605-a598-3135-9327-27d421e85b9a | -7.97861 | -47.24084 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be4ca5cc-a6b8-3c14-b2bb-8c5c24539c57 | -6.94149 | -44.02482 | 2025-10-24 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 064cd84f-f778-3236-9595-63dd737c1468 | -2.81419 | -49.14218 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 9ac5f8e2-6d80-385b-86d2-bd965ef3bae4 | -2.96148 | -48.59704 | 2025-10-24 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f9063a9-672f-3c49-990d-d2797029e0e2 | -9.26357 | -45.35041 | 2025-10-24 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8a31ed1-815f-3cc0-8c43-d2917bf38cb8 | -4.76135 | -49.52813 | 2025-10-24 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69662386-401e-3f8c-90bc-d787ddb68a76 | -6.8855 | -43.61821 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45be17e5-6e5f-35b8-94ef-423d61662468 | -9.87552 | -44.89867 | 2025-10-24 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3661aec0-8355-304e-839f-9f836953e8cf | -10.87877 | -45.0823 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d740cde-937c-3fd9-b5bd-05948a7b6ac4 | -7.35756 | -45.02198 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c86405e-1f12-3f46-8f08-99991129123d | -2.95568 | -49.15053 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dbf680e-c5c2-31b0-acdd-47e1fc69fe2a | -7.24742 | -43.9769 | 2025-10-24 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcdf1511-966c-3688-a150-4fb4c8651ad9 | -4.18426 | -46.22861 | 2025-10-24 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ebf3cc96-fe2b-30f7-97c6-5e29064543dd | -7.46616 | -44.6089 | 2025-10-24 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d788ba80-7511-3eec-a0be-69416f20649f | -11.04507 | -45.40131 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7598821d-f462-3549-bd46-f7f02ef7cbcb | -3.21872 | -46.80647 | 2025-10-24 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7ca076f2-81b9-32d6-8c1b-5eedd7b63d14 | -6.08524 | -46.23366 | 2025-10-24 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba7f040a-94ad-323a-a972-6d61208d0864 | -10.42166 | -49.37088 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2561fda-3566-38cd-b5ac-165acb126c13 | -6.84398 | -41.55614 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90b3e3bd-203d-398e-b2b6-91170dc572d7 | -3.14206 | -49.51881 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb163c6f-232d-3bba-8f2d-3a719eb489ec | -7.29912 | -46.9588 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e748626d-8f9b-370d-a32a-286b8a255b65 | -2.87524 | -50.71638 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d613af4-2a91-3f37-95f4-56f2ac89ebd5 | -5.82146 | -40.8043 | 2025-10-24 04:38:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 101aecc5-6732-3722-901d-3e491cf9be8a | -2.80729 | -51.35232 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1ef32b1-7eb0-3ee6-a25c-788754e35c91 | -10.47013 | -49.10157 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60ba647d-22c2-3a6f-8f19-50cabe7e3b1f | -6.36802 | -41.74014 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8eb6ce13-405a-30f0-8363-0a1e675833c8 | -3.14838 | -50.16434 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f4b0644-df8c-31ef-b4b1-0dc30e44977a | -3.70084 | -47.65358 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd71264a-518e-343f-9b13-b793e479a9fd | -6.09606 | -47.00019 | 2025-10-24 04:38:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71acc694-84f0-3a57-a968-5b3523cff58f | -6.80852 | -45.44815 | 2025-10-24 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc7764e9-daeb-330b-9c06-0b5df366b11b | -5.25526 | -50.80723 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21a60af6-300c-3d09-9a32-79a3f30be2ae | -8.18931 | -49.89622 | 2025-10-24 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb387fa4-5a0a-3b26-8245-546c44156591 | -3.47722 | -50.08276 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82a29bed-4ba7-34d5-abf0-9e906f1b43a4 | -11.05811 | -45.39581 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3dca5f46-5a7c-33ae-b9a7-2bc36a3a97d2 | -6.98276 | -47.36348 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39fb6c7c-8731-39d3-aa68-c718b089303b | -7.9827 | -47.23746 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f809b62-db1a-3666-ac6a-6683f6ea91db | -10.04162 | -47.08405 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e466dc6-349a-364f-88e1-77ce31bdad2d | -8.3431 | -46.19972 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0175041c-74fb-32a0-a668-f3c2b3c60838 | -11.05512 | -45.38819 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce1335ee-dcb9-37de-a08c-c8b3cde4b4e7 | -8.11326 | -47.04794 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45fb1513-f054-3877-8d7d-e6dd452ff9c2 | -3.59079 | -47.5144 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f82f193-23ac-3f84-ab78-b66b7291e36f | -10.89028 | -46.06893 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd11aa6f-70f1-35df-82d0-cdff866c79c6 | -3.98566 | -50.52199 | 2025-10-24 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed2173d4-1794-33ee-ab74-376317e54cfe | -9.23662 | -51.83427 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 948cc58b-cdc0-3f67-b37c-203b229cc608 | -10.47068 | -49.098 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0dbdebba-cf17-322a-a117-7e66ac13e127 | -4.2876 | -40.70039 | 2025-10-24 04:38:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 4b66a55a-7d3e-36f1-809d-e1923f080b23 | -3.84111 | -52.14204 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef3d6e7e-945d-385e-8623-5c87e075d3f6 | -2.80479 | -49.13716 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf8337cb-9392-3bbf-8f31-ae2e12af6421 | -7.64171 | -42.16946 | 2025-10-24 04:38:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4a9a094b-f5cf-34ec-b052-31f2f5cfaf19 | -6.92195 | -44.01442 | 2025-10-24 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8f7b3595-0736-3f29-bf48-21800f437f02 | -9.59711 | -46.91161 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6cec7217-8613-311f-8306-d80f27acfa32 | -8.64909 | -44.78936 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f107544b-719b-3e84-a986-314a9800ecb2 | -6.96148 | -50.33258 | 2025-10-24 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9883e6e-fbdc-3ba0-aae2-40e0c7387341 | -6.60385 | -48.76792 | 2025-10-24 04:38:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 453e56f7-5993-3c28-86da-02da091df1d6 | -3.23996 | -47.25694 | 2025-10-24 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ce3182c-9bc4-3d3a-ae54-49edf71e4e5a | -10.86958 | -44.41684 | 2025-10-24 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c13a9f21-8aea-3dc3-ab8c-50dc9ff84bc0 | -8.31398 | -49.73156 | 2025-10-24 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f486431e-70b9-329a-919a-90a5953750e9 | -7.63558 | -42.20313 | 2025-10-24 04:38:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2710415d-6700-3a84-a102-3d1df83bc1b7 | -5.38315 | -41.55517 | 2025-10-24 04:38:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 89fa71cd-fd2b-3fb2-949b-a14420df2c8c | -5.54486 | -48.93441 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04d6ac6c-132f-3ca2-80b0-a03a72ca3f68 | -11.09668 | -41.61547 | 2025-10-24 04:38:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63380e1a-b0cd-3163-9cce-c6f1e98a5b06 | -9.64044 | -46.8926 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b5a0ca7-dbec-3c37-8e10-57e31d68aacd | -8.6521 | -44.79688 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4288692-e036-3bd4-81cc-c2ad98173ba9 | -4.87435 | -47.53664 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 04b1ae65-5e29-3713-9d95-440e2bad8c01 | -9.62238 | -46.89018 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c704a569-1dd1-3be2-9d56-35c9066d2b4a | -6.97506 | -45.28806 | 2025-10-24 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd3410c2-aa98-3ba5-8e9c-0cc429e53136 | -2.43988 | -51.91195 | 2025-10-24 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51ac2904-9fdd-320b-96cb-36adedade48e | -6.92966 | -44.0193 | 2025-10-24 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a36a50ef-17ce-3381-9fab-b9c7f8487327 | -10.8896 | -46.07374 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2e77225-17c8-3dfc-a7e2-c50d4ca201c6 | -8.61729 | -44.8105 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 28170de5-39ef-3ca2-8367-ac9a46fb2348 | -6.89341 | -43.62329 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e2f335b-c5ff-3299-bac3-48e79d7004de | -9.59833 | -46.9034 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 14ebc813-e7ec-368d-8ebd-0269ffb02c74 | -4.95213 | -43.70036 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4623f592-d025-37dc-a055-a85ca78c6f0c | -9.62301 | -46.88597 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3aedee56-163e-3030-8a87-fbac02f7ba5c | -5.45266 | -45.41521 | 2025-10-24 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 27500de3-0bc1-3daf-8e60-508f7354874d | -9.67368 | -45.44906 | 2025-10-24 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f39510be-803e-3414-b115-444dfe5498e2 | -6.81093 | -45.4577 | 2025-10-24 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6908150-2d9a-389c-9426-cceadbab962c | -6.44253 | -43.81765 | 2025-10-24 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cba15d9-10ca-3179-9bfe-89677beef0cd | -5.3824 | -41.55782 | 2025-10-24 04:38:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7e759a6-67a3-3080-b7c7-4477fbb330bb | -3.9286 | -47.69632 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README43.md)
