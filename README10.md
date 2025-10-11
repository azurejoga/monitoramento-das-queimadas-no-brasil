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
| 689eda4f-c83e-3945-8224-a53741906af2 | -7.80499 | -42.41623 | 2025-10-11 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd1821e1-f22a-3e94-8538-9b7de0e683ad | -10.14771 | -44.60823 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4dca116f-ae76-30a9-b6fb-a69f93ec2aad | -11.88245 | -45.49081 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fb019e7-6f6a-3455-9f0b-67730a2757d4 | -13.38958 | -44.25053 | 2025-10-11 03:42:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6d6f47a-3a99-3af9-803c-4256b6d18194 | -10.17176 | -44.54674 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 418dc10a-7eeb-3a64-8a2b-2847cd76585d | -11.77795 | -46.38295 | 2025-10-11 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0238f11-6ed6-3f73-9afb-4700c5bb2725 | -11.76775 | -46.37577 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fb632d1-4211-3aae-9c9e-cda12b06c36e | -11.75974 | -46.36935 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9432f52c-99f8-3a5d-8452-2107d7f547ee | -8.04801 | -44.11708 | 2025-10-11 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30345ce7-a9ad-3349-86b1-43308d61d83d | -8.2025 | -43.32778 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 02e6ca34-f4dc-3616-99f8-da6e1868d5f0 | -11.76241 | -46.37335 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fae98a3-78b0-3182-9195-557d17e0b96d | -8.17909 | -43.31791 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0b3e61f-c8df-3c99-b1cc-a8363a42829c | -12.92636 | -45.04864 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54dc9d00-5406-3404-b447-1717216209ec | -7.45542 | -46.8639 | 2025-10-11 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f9a27a2e-6557-3302-a729-1c1cafd6d3c1 | -9.10973 | -45.04672 | 2025-10-11 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8d42b722-518f-31e7-b0ac-b77fe759cbbf | -7.65707 | -42.59038 | 2025-10-11 03:42:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 956c3c30-5cbe-3e15-92a9-ddd965b18539 | -12.99524 | -45.22765 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3ea1b99-1adc-31b9-b000-1bb0a9272d48 | -10.87897 | -44.18954 | 2025-10-11 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb708131-3584-3ab3-9b77-6ab46d6740bf | -7.77468 | -42.2646 | 2025-10-11 03:42:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 59c1db5c-fed6-35e3-88b6-b95b6c2cd971 | -11.7697 | -46.37804 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4af116a9-314f-3fe8-9a7b-bf6f533f3db6 | -7.46256 | -46.86013 | 2025-10-11 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d22aba43-138b-391a-899f-e3460581a831 | -7.4139 | -42.97289 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0cd9c398-f9d3-3373-9cc2-9286b992c41b | -11.74207 | -46.401 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8e17bb17-aaea-345b-b1ef-9b7c4cca4d19 | -9.82175 | -45.94278 | 2025-10-11 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a2a8e50-9f38-35dc-9cd0-902be39efecf | -12.7192 | -45.86179 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18c299e1-4666-3605-9f4f-df313f504dfe | -10.15223 | -44.55405 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30e7a53a-42b9-34e1-9232-58bb20f52f29 | -7.6652 | -42.57127 | 2025-10-11 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1d5984ba-f23c-30cb-9c54-625c24500fec | -9.82244 | -45.93921 | 2025-10-11 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d279312a-249f-3033-a961-077baa9e5295 | -12.98956 | -45.22971 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f967e13-51ae-385e-9426-5c8cc0741a49 | -7.67457 | -42.57278 | 2025-10-11 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5af51f93-eac9-3d69-b808-4f006489262c | -7.65969 | -42.57525 | 2025-10-11 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b73efcd4-9952-3efc-8b3a-1bec5ae5ae2c | -10.14862 | -44.55717 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ddbf368-b8c1-36fb-8404-e2cf8a64b1dd | -7.67842 | -42.57842 | 2025-10-11 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bcfe7f0b-b6b7-3175-8717-109a82156732 | -7.864 | -44.48254 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b84315ea-2a0b-3214-99e3-78d939b4bf33 | -10.57165 | -44.51157 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7832c0b-8ffd-3ee6-a761-7d964cd68179 | -7.86341 | -44.48587 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4d84684-c6bf-3d3d-834b-677c6b9114b0 | -11.74132 | -46.40488 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 70b801fc-f29a-3c6f-aef5-baf549276e9a | -12.75835 | -45.88766 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1e4145c-e7f3-32f1-ac46-d68e79e48f37 | -11.89183 | -45.49899 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56635c1b-6c83-3a55-8f85-9e9fc3bdc16a | -11.05406 | -40.93741 | 2025-10-11 03:42:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec95975e-ec33-3d60-abc2-8fae228a5b7d | -7.29909 | -45.56345 | 2025-10-11 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f47c666-9ec0-3ab7-a0a7-1f108f7aea2a | -13.20483 | -42.34344 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 09841a06-7e00-3300-b58f-fc0493a827f2 | -13.20902 | -42.34423 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| eabc2e93-6c4e-3933-b597-1e488e97c3f9 | -7.79824 | -42.40028 | 2025-10-11 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6efaf12c-f406-3650-bc65-df22de0128ea | -11.87646 | -45.49352 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d4d42e9-d18c-30c8-9b0f-cdca03b78d2e | -7.86384 | -44.45299 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48d722a7-4f64-3c76-b43a-c16b337465bf | -7.06787 | -45.21949 | 2025-10-11 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f933d703-5a65-3475-a0a2-639cb4e08c0d | -10.42831 | -44.99514 | 2025-10-11 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f035afb3-e307-3a04-b3d4-b2dbe0f5e020 | -11.73902 | -46.40319 | 2025-10-11 03:42:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9a75865-8a37-3b05-9933-7c8bdd2c0321 | -12.18359 | -48.80755 | 2025-10-11 03:42:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 524d2c32-5c8a-3051-8bce-1a3e91cec8b5 | -7.74959 | -44.2178 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31a4a0c4-8444-38b2-b464-e881bc713335 | -10.4277 | -44.9984 | 2025-10-11 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e15fb3ae-8ccd-32b4-90bd-ec1db4c74582 | -9.10452 | -45.03178 | 2025-10-11 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94bd64ad-306b-35fc-913f-98e72a2c4b38 | -7.40706 | -45.92273 | 2025-10-11 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4399b3a6-6a13-3b8f-abf2-87013d8adabc | -13.20412 | -42.34736 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 181dd95b-f71f-3cb4-bede-3fd64a051118 | -9.10556 | -45.03925 | 2025-10-11 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ade2f72-a75f-3d25-a26a-27a1fb30abef | -7.43098 | -42.98138 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7b3172b0-ba9b-3f1a-8d21-36ae3ad8d470 | -13.21668 | -42.34974 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| fa1ad81c-a6dd-3e52-8630-9d186e420a41 | -13.48562 | -42.01773 | 2025-10-11 03:42:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c708843f-0673-3e37-b321-f2d086de64a8 | -10.19818 | -44.60394 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 420c1d01-9fd0-30cd-b10f-e04bb5b89c1f | -9.33504 | -46.10737 | 2025-10-11 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5292e775-a578-332b-9571-04f81d7cae19 | -13.00031 | -45.2287 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48dcaf31-6816-3a77-b8b0-540fe9adece2 | -8.01867 | -44.46579 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d823e24-3136-39c4-891d-0af85a1641b4 | -8.2045 | -43.34515 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e8067360-dc0c-3a77-a51f-ff8546117bff | -7.34255 | -43.86047 | 2025-10-11 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 238f1b10-8719-3949-9973-1b7b2b9cce45 | -7.65884 | -42.58013 | 2025-10-11 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c33343c8-3d77-390d-819c-f1f0219374ec | -7.41212 | -45.92085 | 2025-10-11 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5523ba9f-895a-3e41-9bd3-17897eef4252 | -13.2125 | -42.34893 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 165e24c7-80d9-3678-8010-5b259d3b070b | -8.04747 | -44.12012 | 2025-10-11 03:42:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dacb6c00-57cd-3c33-baf2-6c84ad973753 | -7.77807 | -42.9682 | 2025-10-11 03:42:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6b451b94-48a9-31f0-bba1-78bf41a3fbe9 | -7.53031 | -44.29519 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 593e51d3-726c-39ca-86d5-20d70d10e936 | -9.32858 | -46.11005 | 2025-10-11 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 76b22868-9a07-3021-ab04-90b230b96c6c | -10.17231 | -44.54382 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e256c59-75b3-3e03-9d46-f48cf608d37f | -13.22228 | -42.34269 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 3943c22f-5c00-399b-a532-78b0d8bd2885 | -8.01754 | -44.46569 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c51d677-cec5-3aee-be3f-9a0243ef7f4c | -8.20368 | -43.33508 | 2025-10-11 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 21071897-3ce5-30fa-934e-cd04e2ff11d7 | -11.75929 | -43.32169 | 2025-10-11 03:42:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 336b12cb-27e8-3c89-b7fa-614dbbb9107d | -7.67148 | -43.99346 | 2025-10-11 03:42:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df467058-acef-35c3-895a-268b9a408d9f | -7.33685 | -43.86279 | 2025-10-11 03:42:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 109d14d1-4ba0-3e8d-ba51-20f7533482c6 | -7.85452 | -44.47441 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f5f5f8be-700c-3a27-bc06-3213eeeacceb | -12.91463 | -45.05535 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d4a9aec-312a-34e4-93f7-7b85bff84c70 | -8.38664 | -42.26614 | 2025-10-11 03:42:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e48465a0-7540-3cdc-96d3-9054052b03a9 | -8.68044 | -40.41945 | 2025-10-11 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e29c7530-43c2-3f99-affd-11a9f62e3238 | -10.17684 | -44.54789 | 2025-10-11 03:42:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cac3e851-213f-32ba-bef7-2c7b35b2e209 | -9.32838 | -46.10624 | 2025-10-11 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b2c7748-163d-359b-8c24-058630d89d3c | -9.15926 | -41.05935 | 2025-10-11 03:42:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 364c0fe8-d780-3f3b-800b-8969792c32bf | -9.10491 | -45.04269 | 2025-10-11 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e27d239-1b97-39e9-8a29-efd1f89a522b | -9.32767 | -46.1101 | 2025-10-11 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3d2706f8-de95-35e2-9c2a-1c2a7b4412eb | -7.85213 | -44.48772 | 2025-10-11 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 96ce70eb-53eb-3c0b-b6cb-63cffbe8beb4 | -13.21179 | -42.35285 | 2025-10-11 03:42:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7aee340c-68cd-39ad-95ea-47389da8bc0f | -7.46297 | -46.8672 | 2025-10-11 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6573e864-8432-318c-855b-2c62f97e0958 | -7.79786 | -42.42995 | 2025-10-11 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cacf7686-a544-3f24-a56d-f15a0a5c1c4e | -11.75563 | -46.36049 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a033e844-275c-37e2-b6d8-9dec29a29093 | -7.40547 | -45.92401 | 2025-10-11 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0761dfea-33a6-38e0-b912-ac588eeff47c | -7.80582 | -42.41142 | 2025-10-11 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5bd33fae-18db-3c50-b042-477536b88da7 | -7.42356 | -42.97453 | 2025-10-11 03:42:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d8617cf8-610e-3911-9762-89c038672404 | -9.81585 | -45.52401 | 2025-10-11 03:42:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bce247c5-48c5-3933-a3c2-f6fcc9d10d20 | -12.44977 | -45.0793 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0e75b0f-bda6-301b-b4f5-26a14094777e | -11.75166 | -43.3899 | 2025-10-11 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f70dfb28-8315-3507-a151-5b2a4a5e49e9 | -12.71986 | -45.85847 | 2025-10-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README11.md)
