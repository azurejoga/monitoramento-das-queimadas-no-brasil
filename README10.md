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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb242d46-5ddc-3330-b53a-882919c77be1 | -8.75788 | -49.77008 | 2025-06-04 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab818014-2075-3b44-b3c6-253e28110885 | -11.53508 | -47.31401 | 2025-06-04 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 108f62da-b4d9-3de9-96e9-f19eda9bc30c | -10.61844 | -49.55663 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5588c03-0b06-3dcd-9b01-6944f49d90bf | -6.56191 | -44.4873 | 2025-06-04 04:51:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7773d5dd-3e2b-325c-bd51-c4c0d2052f91 | -9.25214 | -56.31549 | 2025-06-04 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4028ab33-29b6-3943-b96e-df59c3e82f20 | -7.89072 | -55.36555 | 2025-06-04 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ace0c60d-a6b5-3c35-acc2-08240f434990 | -7.01244 | -44.59783 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 26f356a7-eb92-3ab6-b88a-56f5c83e43c5 | -8.07647 | -43.11392 | 2025-06-04 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 65f5ed47-7f16-3436-b11f-aff751403f73 | -7.68592 | -44.57022 | 2025-06-04 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af64e384-0cd4-32a1-abf2-43df9f304ca6 | -11.89272 | -47.45801 | 2025-06-04 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0b841b7-ab6d-3506-b1a4-4c70dc9e357f | -10.26185 | -48.4577 | 2025-06-04 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3df6747d-c2f2-3175-8349-0235f14ad08f | -7.99928 | -50.6968 | 2025-06-04 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0378807-02b8-32ac-a125-2ec42e101ecd | -9.62475 | -62.8139 | 2025-06-04 04:51:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d187b25d-55a6-38e0-955f-36d89fcbd7b9 | -11.40362 | -52.94352 | 2025-06-04 04:51:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4186723b-1cc2-3dd7-b4ec-41f3f31b623d | -7.01284 | -44.59487 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3d095890-6d3b-3cfc-8cbc-fb29589f83fe | -6.86701 | -47.84621 | 2025-06-04 04:51:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bda3d80f-2572-3e51-9a48-2eb2f505f613 | -11.4064 | -52.94758 | 2025-06-04 04:51:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caf47c7d-df63-348a-8d15-1174ea2b0243 | -10.6924 | -57.64558 | 2025-06-04 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e59abe8-3fcb-37fb-84e9-6edb03eb689c | -7.22047 | -43.12455 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 795aebb3-34e7-3975-ac13-b90a81e3f6da | -12.27414 | -44.59298 | 2025-06-04 04:51:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1026b1d7-3ea1-359c-9c5b-f3c80d506b59 | -11.80595 | -48.28107 | 2025-06-04 04:51:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9893f045-fbc2-3e93-8656-32504a99bd65 | -8.91667 | -48.90562 | 2025-06-04 04:51:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2ec239e-c5d7-339e-ab91-d353aecf55b6 | -6.96359 | -42.90168 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 8a6aa11f-83bf-3af0-8724-96ec0fa7a9e4 | -9.25571 | -56.31606 | 2025-06-04 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96105712-3854-303b-b104-fbd432f1004d | -10.04085 | -48.78115 | 2025-06-04 04:51:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8e424b0-7e6a-3c8d-a517-be2ff11003fc | -8.55632 | -44.55666 | 2025-06-04 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57a58d51-c8c0-3658-ad1e-3d66faa61508 | -7.58416 | -45.8638 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b266e342-3c1d-3960-ac39-d5d190ca14c8 | -7.87534 | -45.98994 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ae52789-fc6a-3d1b-bee7-f0cfdf572c8f | -6.36987 | -43.68164 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78946603-acbe-35e9-baaf-08fb4e38e013 | -9.60071 | -63.25552 | 2025-06-04 04:51:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bfd4d7c-4242-39a9-bb61-7c1ed2aa09c4 | -5.76257 | -47.19403 | 2025-06-04 04:51:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7af93eb-b189-3130-a61d-c194d76c84dd | -11.25427 | -49.49213 | 2025-06-04 04:51:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 818d2a80-eb95-322e-bf0e-cea340888719 | -11.13843 | -53.92851 | 2025-06-04 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02c0ce62-8a69-3a57-aaec-40d735918dec | -9.35351 | -50.22682 | 2025-06-04 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fe2aa01-57a8-3295-aa58-5c2cf9d3641d | -6.21264 | -43.33527 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cde10446-d31f-366f-9737-066b23ced660 | -7.01862 | -44.58989 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a534cbbe-6d53-3bc4-9db0-70fa09f5597f | -11.84174 | -51.29393 | 2025-06-04 04:51:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98a61264-9cca-31b9-8a6f-82be6ba6bf2a | -11.89329 | -47.45364 | 2025-06-04 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c681363f-3881-3815-a99a-60f3d0872322 | -7.01366 | -44.58876 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7ea9b40a-78f0-3e27-bbe6-6bf8ab3b9ac7 | -8.68812 | -48.28966 | 2025-06-04 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83779591-c5fd-3577-ae72-12205360be9d | -7.48569 | -49.74521 | 2025-06-04 04:51:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 935b1f4d-da5f-3792-9a2f-c3a50eb6ba86 | -7.01782 | -44.59573 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 79f0a0d7-6a13-3cdd-b723-d33528efad47 | -11.84 | -51.28142 | 2025-06-04 04:51:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| afed4e96-22d9-3a7c-bfd8-00c831eaaa4c | -10.21165 | -54.30234 | 2025-06-04 04:51:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2daddb2-d172-3c51-bff5-4ae5ed36e70f | -10.34216 | -54.18662 | 2025-06-04 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7451474-5907-3272-94f1-7e0987f929a9 | -11.57445 | -47.62626 | 2025-06-04 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ec8f2b4-a80d-3aab-817a-e0f99cecce17 | -6.37468 | -43.68568 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c4d36bc-8805-3ff9-87c3-4dda1cf9c5af | -7.99582 | -50.69629 | 2025-06-04 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d6427fd-2a5f-3807-b416-416bc54d839f | -8.3658 | -45.06356 | 2025-06-04 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 747bc16b-2aa3-3502-abc4-3277f1c68197 | -8.89983 | -44.78092 | 2025-06-04 04:51:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| add1cae0-a5c1-3c6f-976e-e4ee85c25141 | -6.60351 | -43.89065 | 2025-06-04 04:51:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8ebe323-bda9-3c85-880c-af03d2f18583 | -8.96676 | -47.96811 | 2025-06-04 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f63f48fa-27dc-3b78-9205-0894509c91f6 | -8.84324 | -49.84875 | 2025-06-04 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7c1a999-9499-3faa-9ab0-aefbba98b331 | -7.87994 | -45.99062 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfb3f5b4-24c4-3dbd-9486-12be6eea8ab5 | -10.71058 | -48.77907 | 2025-06-04 04:51:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6825584e-3c93-3f2b-aaba-9af6e679e229 | -10.06911 | -55.54641 | 2025-06-04 04:51:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32dab18c-e510-346c-89bc-5277cf556971 | -6.6905 | -43.68413 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55ad6c88-11f7-3b65-91b7-b2b5421b84ad | -10.22409 | -47.56878 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cacbd965-36ce-32f7-9d57-75b61be72ef6 | -7.21998 | -43.12828 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6dccbca0-c495-3240-b6a1-f754d6ba9aa9 | -8.69211 | -48.29021 | 2025-06-04 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f562bd0a-1ae5-3896-ac5a-989b3c4056a0 | -7.14604 | -44.03947 | 2025-06-04 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5703d3b3-2add-3111-838b-c4981771f913 | -9.0458 | -47.02879 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2520026-7a83-3588-91ec-59402cfe77e2 | -10.87061 | -49.55062 | 2025-06-04 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31c2ee65-8c7d-3f9f-ba12-8f4d70276201 | -5.18328 | -48.07987 | 2025-06-04 04:51:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71cae47e-2560-3b81-ae27-113d63908fb7 | -6.86751 | -47.8427 | 2025-06-04 04:51:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4dbf00f-06c2-33c4-8dcc-bc262c25176d | -7.15125 | -44.0402 | 2025-06-04 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32c86e4d-3b79-3b5a-b077-0fc1aec9d472 | -10.12414 | -58.20325 | 2025-06-04 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9858738-3eb5-3fc7-b5a7-3f92e34123af | -8.31987 | -47.92467 | 2025-06-04 04:51:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a7f0835-0b9c-32dc-bb50-bf4e03c3bc62 | -7.90065 | -50.35983 | 2025-06-04 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e5323c95-1edd-3af8-8758-139ce3f5b0e1 | -7.01325 | -44.59182 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b0db5435-6346-3e79-8acc-d0d44fe0f8e9 | -7.21299 | -43.13842 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e6b54bba-1cda-3a65-b28b-878510d17132 | -7.20747 | -43.13752 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c9fba175-6ced-301d-b601-0fa49acf6c02 | -6.96868 | -42.90627 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 261a87ee-6f70-3639-9852-5bbae21c5ac3 | -8.75423 | -49.76952 | 2025-06-04 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4d929130-a742-3353-bc9c-6e0d43fe4070 | -12.31908 | -47.25892 | 2025-06-04 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 519c97ce-2386-315b-a32d-63898969592e | -7.20789 | -43.13575 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b89bcf8a-f83d-3ef9-b7c4-719b701ce0bb | -7.98449 | -47.21464 | 2025-06-04 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 387cda8f-b598-3289-8ea6-30afed904222 | -9.66614 | -48.71014 | 2025-06-04 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6bf00e8-c81a-3266-a912-94f445dbba79 | -7.01087 | -44.60939 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ce9634c2-910a-3fa8-8bc0-f11664864632 | -6.96307 | -42.90551 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 73f1ca8a-a7d6-3c54-8437-d111a7b9363d | -5.17299 | -46.10407 | 2025-06-04 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dc1e963-0b66-3d29-b2a1-63ee7a0cb1da | -10.49446 | -53.65284 | 2025-06-04 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4be867cc-4f8f-33e9-97b3-1d5ee1fa460e | -6.9692 | -42.90245 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| db27886f-5876-30a3-9fff-a80c03f4adbb | -9.40018 | -48.4352 | 2025-06-04 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cc346f3-7d15-35cd-a9a5-80c2f0751bf4 | -11.83824 | -51.2934 | 2025-06-04 04:51:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 777e0662-ccc1-3f3d-9432-ebff180484f2 | -7.11256 | -43.29901 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 17fbfd85-0322-361b-968a-d86f0afe2437 | -9.60001 | -63.25922 | 2025-06-04 04:51:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72cf8285-f1b2-39b6-a94a-a11829a245a2 | -6.29704 | -47.0113 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b404849a-2348-3b06-82d6-5efdebd43a0e | -6.24606 | -43.37209 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3a5f0565-724e-3a71-af9d-6b5e0cab1bdf | -6.36922 | -43.68252 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2d295a9-2476-32c3-92c0-7f50d06a4c04 | -7.98393 | -47.21856 | 2025-06-04 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fabea127-caac-335e-b43d-84f686217416 | -9.04638 | -47.02453 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ba3a01c-00ec-3d20-84f6-8d00ae1fb24a | -9.6657 | -48.71413 | 2025-06-04 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4937246a-4124-3c5c-9de8-c1d4e5f6d941 | -7.98171 | -47.23421 | 2025-06-04 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dc411ec-8ae7-3d7f-b9b7-5e26a1c9e98c | -8.00361 | -49.71157 | 2025-06-04 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b7e8596-c419-3f8a-a35d-ad854d38c489 | -11.90654 | -47.45551 | 2025-06-04 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c0a4da5-f941-3856-a4fc-dbd299347111 | -7.90464 | -50.36317 | 2025-06-04 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c9cf3670-830f-3700-b505-6d4f383ec4cf | -10.29683 | -57.14311 | 2025-06-04 04:51:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0172bc4-45c8-3d12-94f1-cedb449543cd | -8.97084 | -47.9687 | 2025-06-04 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8447d14b-c775-39cd-a0d0-015defe2994f | -10.22353 | -47.57278 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README11.md)
