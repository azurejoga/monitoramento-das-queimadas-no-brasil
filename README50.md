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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18ddd6ec-4664-352b-ac2b-c1f2efcb29b7 | -6.66066 | -48.39017 | 2025-09-07 04:19:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aabe8611-6441-3375-9740-cbc167499ae9 | -10.76898 | -48.26719 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 773e4f28-5fb4-3e56-8dd1-6f1b09f6aaa4 | -6.35543 | -46.37074 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0706395-6847-377d-9b95-eaf5bb11395e | -7.81432 | -45.42495 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 258f3092-828c-3881-8b63-566a011bb06c | -10.73255 | -48.59485 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf573899-76b1-3965-b996-10b49c2795fa | -13.00962 | -45.22111 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd39f0b4-7d98-3742-99c1-0ebdf019df3b | -11.30619 | -46.53571 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0ba6e83-b46d-3c7a-91bf-3d854418b8b5 | -11.38433 | -43.54426 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a7512e9-f941-3e96-b8fe-16deef43c3ed | -11.61299 | -47.15934 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 330ff828-dbf4-318a-a9da-7ad23992fb33 | -10.60596 | -44.3336 | 2025-09-07 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6abec200-22d6-30b7-932f-1fc2a49a0f93 | -11.33609 | -50.31072 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c46b4e35-b9b9-38c7-9011-d1fc31297da1 | -6.20117 | -42.6291 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62269ee4-6b0c-3903-90b4-8059a6c836ea | -7.67635 | -50.30458 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b08135ae-0dca-3db1-803c-32954720dc5c | -12.54623 | -48.07728 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3edc33fe-2e89-3dc5-ab67-759ae81b9cd9 | -5.84317 | -44.09721 | 2025-09-07 04:19:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 085b47c0-d3af-3442-9239-ef39de0bc741 | -11.39933 | -43.56244 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d99d615-2763-3f00-940a-574b399686fb | -12.84834 | -47.99046 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fc1654f-83f6-3b8c-880a-284ff86054c5 | -8.45708 | -45.03296 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36ee56e7-a10e-3fa0-a228-07d345444b14 | -10.80941 | -47.73714 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c72d0f0f-e19a-3ce8-be52-5fd252488db3 | -12.81259 | -48.01632 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa7f1169-443c-3f8e-89de-3e752fe3946f | -9.70598 | -49.49028 | 2025-09-07 04:19:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93b7c6fe-2c2a-3b0a-af10-fc424ba1ab69 | -7.58271 | -49.28229 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 710b0a9b-743c-3fe7-8ac9-57775ebacebc | -7.71833 | -44.72019 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc9a74e2-1308-3395-a581-73a0973d519d | -6.12792 | -44.25264 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5cc4468-6e67-3a23-93d7-9229f2085619 | -11.20106 | -55.05667 | 2025-09-07 04:19:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdaffb0d-c233-386f-986f-9d24f831eb3c | -11.40207 | -43.62963 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4890988-eddd-3555-aa87-84a06522eb4b | -12.80171 | -48.01849 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b433e077-b98f-384b-9b6d-0fb6ef427d67 | -6.6022 | -43.99894 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7c28fedf-479a-3216-af7e-68e40f7e28ab | -7.06287 | -50.85892 | 2025-09-07 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c82ec3a-3a4a-399d-ad3b-d2172240b40e | -10.31455 | -46.46892 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cba0e2f-eeea-33ea-8cd3-fae146626f0b | -8.45294 | -47.32264 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19a7af74-058f-3bd6-ba16-3a9ddbde976e | -8.93383 | -48.65048 | 2025-09-07 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25d0695a-fe76-3f3a-8d04-54cebfc793e7 | -6.29725 | -51.4142 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 937e9204-f7d1-3d0e-b43f-0d78b1cfe3d8 | -8.86699 | -47.91057 | 2025-09-07 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94e5865e-23b6-3b1d-acc0-63a4a2a14eec | -6.4026 | -42.98123 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cdf8108-5f85-320a-a122-2b7695d2182d | -10.78377 | -48.26856 | 2025-09-07 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 673142e8-a697-3334-91ca-bf85331ca530 | -10.84047 | -55.10464 | 2025-09-07 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03e0bfd9-f9dd-372f-9282-70baaa1d4924 | -8.01803 | -45.44715 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b781cbd-f932-38cf-a360-8ef66035bd11 | -11.59322 | -47.16392 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58102eab-4952-38d0-aa95-462b8eccbc7d | -6.23696 | -43.27536 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 57ef4e39-4b76-3630-ad86-1daa8375e00b | -6.16322 | -44.24397 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e302b5e-4dcc-3e38-8a97-84725b26bb9d | -11.84008 | -47.5686 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e202187-7e2a-374f-a2f2-26be4ac801b7 | -6.85706 | -45.5904 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5482852f-19fb-39ea-a11d-e4b7fb1c66f3 | -10.72191 | -48.59287 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 578af0f2-2477-3362-af23-34d41e2128e1 | -8.68261 | -45.28281 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6ca08e2-8119-370c-ba61-8255a8186dac | -6.19381 | -43.37518 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3df771f-62bf-3500-8d18-3d4c55ae96d1 | -7.61068 | -44.6712 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97c47d4e-0f8b-332b-9375-21937c0b8b9a | -6.15198 | -43.17749 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 105f86a3-252b-369f-8359-5dce1fc31f6a | -10.05674 | -48.06226 | 2025-09-07 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12b7ecb6-6683-3a75-8db1-8f05a8e1f4ce | -7.25447 | -41.88886 | 2025-09-07 04:19:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 61998fca-dbc2-3bec-9138-babb6036b906 | -11.31884 | -46.56317 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 051bc93f-3392-3753-be28-76a40263a22b | -7.75373 | -48.82181 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 79226c79-9c6a-3a27-b001-00129cd08fb1 | -11.58044 | -47.76312 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48235f86-7d21-3d7b-87c5-799273f00841 | -11.39874 | -43.56631 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b127541-9e9a-33b5-84aa-32d61aa24542 | -11.9074 | -46.64191 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c9881ac-18e8-314b-bd88-5f7ee5d936b5 | -8.18463 | -44.84403 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f872712-2c6d-3b27-a156-5a6439ae20b1 | -8.04104 | -44.04585 | 2025-09-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc177332-0427-3472-abd2-87340250c15d | -5.98305 | -44.15854 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 534d7d03-2174-399e-bc53-130f139bcf90 | -12.87933 | -47.99591 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e943f6e-df9e-37ff-92a6-a7122eade329 | -6.21093 | -43.58919 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0536bf84-d84e-3bf3-94d7-31e0f0a0dd3b | -6.1882 | -43.36699 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9761c8a8-a4aa-3715-b3e8-0b00efde8329 | -7.75524 | -48.81284 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 2b48338b-5547-33d6-a051-22763e069c1f | -6.79947 | -50.84708 | 2025-09-07 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d581c89c-b962-378c-8e87-cbf23d1fe399 | -6.3884 | -43.00192 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9cb75d5-e4a8-3e85-ad26-0c3cd527493d | -11.58597 | -47.72924 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 190c7632-2034-3a3c-84fc-a07961367bb8 | -5.56919 | -45.63435 | 2025-09-07 04:19:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00319d69-f6da-3d6c-8651-98248435085c | -5.8987 | -51.93808 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d90926e0-3368-3b18-bd10-8ae029ea540e | -6.19701 | -43.59061 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89a8255a-1f1e-3d39-98f1-87f6107c64fe | -6.19981 | -43.59467 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff117c64-5b93-3156-90c1-a01f9c017deb | -5.94902 | -53.79643 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70427af1-9c48-30fe-8056-f1d084fa1059 | -11.83113 | -47.55942 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd53a82b-3347-3beb-9268-9d44ff861c9f | -11.40162 | -43.57072 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57606766-fbe5-3969-8f8e-3c96bfd74a72 | -11.56399 | -47.75647 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54701c22-bdbd-3abf-ab24-2a42ac970f0a | -6.1722 | -44.31635 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3850ef07-3ed3-3a8b-a3d9-2562ae2f684f | -13.33086 | -43.25063 | 2025-09-07 04:19:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 006fbfe7-23f5-3b81-84f9-e5dabbf3a7ac | -5.86651 | -51.95647 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c8033ce7-e0ef-3d8e-b942-db711ef8f024 | -6.37651 | -42.98885 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 204492a9-a5f4-32de-b9e5-939252b602ec | -7.67537 | -50.2606 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c81e4761-0b24-35a5-90cb-1f75000d5de8 | -10.43359 | -42.53646 | 2025-09-07 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5838a8eb-fe86-3544-9b8c-2862ea9a528e | -12.80512 | -48.01907 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 36d87041-1166-36ef-8ef6-b95bffb34e9d | -11.38951 | -43.55696 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b62f681e-9f41-3ade-876d-7030b421c5c0 | -7.6763 | -47.32872 | 2025-09-07 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91a2c6e1-4192-3d41-906c-37e4442acd5f | -6.65992 | -48.39465 | 2025-09-07 04:19:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2eea2e32-c7be-3167-8537-76d1a333a41b | -6.40204 | -42.9849 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78d5b0ad-0e8b-322d-9b4c-4b526a7051f8 | -7.68327 | -50.31358 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20b01353-5d79-35a1-863b-55cbee450937 | -11.40434 | -43.61426 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02ee5b6d-97dc-3111-b284-9a005b412488 | -7.68391 | -50.3097 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02689157-7a79-3d8c-9314-dac778ef1acb | -6.20165 | -43.36905 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 64482725-af8a-3910-a6f0-8b51a6d3e498 | -11.40139 | -43.5623 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d14bf94-fb20-3b66-a4bd-5cc7a0dc9739 | -6.70655 | -51.41827 | 2025-09-07 04:19:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c41932d3-b8fb-3462-ac68-e82f30a2dd63 | -10.33262 | -46.39911 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c53abe13-c3fb-3aba-b598-17029efb9598 | -6.14805 | -43.18053 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 23df54f4-58d9-318d-9f2f-0282ae65e48f | -11.20382 | -55.01223 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9abcf09e-3215-390c-b0fa-c57763ba4b25 | -11.21906 | -55.01295 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e55acce8-f98f-36d0-a65a-1bfdefd137b5 | -7.54372 | -45.35359 | 2025-09-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db9642dd-8f5e-3c9a-954c-6ca98aa7251e | -8.46417 | -45.69717 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 863cbaff-080b-35ff-a103-ec39881db6b3 | -11.10849 | -52.01549 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e981e044-7f81-3077-af68-829e01b1724a | -8.50295 | -45.06512 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d44acf5-84d7-31cb-9e6a-17728e76ca8e | -7.67405 | -50.2933 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b8f8119-a6ad-3ede-a720-391e77c20a80 | -5.89629 | -43.37006 | 2025-09-07 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README51.md)
