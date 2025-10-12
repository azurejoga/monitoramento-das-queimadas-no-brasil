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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee431f80-5717-3228-b8e7-b8cb68f1f5d1 | -8.43451 | -45.66619 | 2025-10-12 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c053dcd9-e89b-3778-8ad1-d1753107018d | -7.05299 | -45.26144 | 2025-10-12 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0bd40012-861f-3534-b533-ee7ebd939425 | -5.0417 | -45.11734 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f9588379-217c-3e7c-bbd8-198fcaab30b9 | -4.41323 | -43.12309 | 2025-10-12 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 27dafa70-2294-37d7-a4f4-8dcc8655d4aa | -6.51076 | -44.13471 | 2025-10-12 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 0df82a5a-837f-3181-8ab0-1d59b9f681d1 | -5.37362 | -45.04621 | 2025-10-12 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5b3cf345-5f9d-3e73-9230-2102292ffab8 | -7.21295 | -45.49141 | 2025-10-12 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 81255dc5-8d41-3816-8e35-38bd249bc1b0 | -9.88388 | -45.90987 | 2025-10-12 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fe6feea8-7ba3-31af-9b39-40bb66894485 | -10.1701 | -44.54409 | 2025-10-12 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 746f21f0-306a-3d73-840d-9d71558470e3 | -7.35864 | -44.80302 | 2025-10-12 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8397c116-a54c-392d-8dc6-a155a6c8ee14 | -4.80038 | -44.43102 | 2025-10-12 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c1cdc895-f757-34a4-927c-f0f2b59aa7d3 | -5.59398 | -45.84561 | 2025-10-12 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 4974eda6-5307-3a4a-9efa-cdadbbe7c64e | -7.67622 | -42.3983 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 978f68ef-19e1-39f1-9f9a-13a21282fb7e | -5.65611 | -44.48847 | 2025-10-12 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 730b93d2-00be-3545-bcf0-645ac808a231 | -3.87439 | -42.5121 | 2025-10-12 00:13:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 35.1 |
| f4e21d19-cf76-3111-8e33-444cf042d41b | -7.35479 | -43.85036 | 2025-10-12 00:13:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 88d655f1-02f6-394a-a4a5-47212d53269d | -4.82172 | -43.13823 | 2025-10-12 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 2443a709-a13d-3eb1-a27e-ebea04bb6cc3 | -6.59725 | -44.56337 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9acb96eb-64ec-36dd-aac6-e22969b6ba7b | -4.20092 | -46.4358 | 2025-10-12 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 24eb21a8-4f9f-3a63-bfe4-852f27a27dc5 | -4.42567 | -43.46706 | 2025-10-12 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d1cdac67-00ca-3ac1-9334-a5dbf4dddd96 | -6.89727 | -45.47007 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c49d52d9-f070-3a10-95e0-010129fe61f4 | -7.66698 | -42.39959 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 35722aa9-b628-34df-85b8-01f48a6a1409 | -7.68272 | -42.57538 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| fb2ed42b-6bb0-3234-adf3-c0c67ddd204c | -6.5727 | -44.71062 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d679b3fd-0032-3e4d-a774-62b6cea01267 | -7.52173 | -46.54134 | 2025-10-12 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| a5590234-d25c-31d6-ad12-eb7ee1da1130 | -6.08284 | -44.30757 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3b5970e8-4c5e-3466-b151-ae518963605e | -6.16943 | -44.67273 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8c1cadd1-3e0c-3343-91b9-45d641dfc11b | -8.52252 | -45.4322 | 2025-10-12 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f52666fd-ffc0-3572-acf0-b8ff5d8a8209 | -3.61377 | -42.75889 | 2025-10-12 00:13:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f1f97ac6-e2d9-3f54-bbcc-846efb24a71c | -3.8759 | -42.52258 | 2025-10-12 00:13:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 5fbbd9b3-3ac8-3e5d-81d6-fb9d7dc7e92a | -4.61758 | -45.77636 | 2025-10-12 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 29cd6a15-03d9-36a6-96a0-7a6b79e1a9ff | -5.73972 | -40.76697 | 2025-10-12 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| b44f0e6f-3593-378a-bbcb-aa52826107de | -3.13964 | -44.42229 | 2025-10-12 00:16:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2e0443bc-d1ff-37ac-b1a9-b541d1b52fac | -3.40409 | -52.18434 | 2025-10-12 00:16:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| c87ff2ab-e2eb-3b71-9144-f73dd0bb3100 | -3.19903 | -52.22391 | 2025-10-12 00:16:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 13261ad3-f5fb-355f-9b90-eeacd318138e | -3.41535 | -52.20003 | 2025-10-12 00:16:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 2badbfe9-3607-31b3-81dd-fc6150b9611d | -3.74281 | -44.39147 | 2025-10-12 00:16:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0f2241c8-9c52-36d2-9031-35c9d79c0069 | -2.71702 | -48.35893 | 2025-10-12 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 47bf4848-7446-3024-bd55-bf951d833c17 | -3.60816 | -42.75506 | 2025-10-12 00:16:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 602d33e4-d42b-3ece-95f8-7cd8987d46a4 | -3.42291 | -44.14348 | 2025-10-12 00:16:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ec548471-7bd4-3b52-9052-b2c1e2a8bff4 | -2.54769 | -47.80405 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 416b4d0d-508b-3c2b-942b-929fa109a319 | -3.60508 | -51.34345 | 2025-10-12 00:16:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9a2756b8-c5a2-36d6-a65d-0f9f0b2f7c6b | -3.29747 | -43.5088 | 2025-10-12 00:16:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8b13c0a2-76c7-314f-b0b8-1cdbcc4a0e0c | -3.51277 | -45.84966 | 2025-10-12 00:16:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 77d38dcb-9b7e-31ec-b4db-1c1fa4284df5 | -3.54385 | -48.93497 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 558f16b4-470b-308f-bf2f-ec28e3dbcd1b | -4.01291 | -47.35307 | 2025-10-12 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| e57c41c3-27cf-3b6a-9d1a-d51b93e95754 | -2.54627 | -47.79387 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a7f55fae-7dd4-357a-bc13-cae07f59e65e | -3.67683 | -49.18864 | 2025-10-12 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a78cdab6-9ff9-3b1e-b730-6154c92c8a1a | -2.44592 | -49.3634 | 2025-10-12 00:16:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 88b0bd55-0945-3748-8772-978a48514cb7 | -3.27278 | -50.04095 | 2025-10-12 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9260ffb0-237d-36a2-8db4-c3418344adfa | -3.76738 | -43.90292 | 2025-10-12 00:16:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bd621fc5-c52a-39e2-a8ff-8d9a7759f19f | -3.53006 | -48.91164 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| ffa3326f-00c7-3f01-a092-e2faaf40d882 | -3.14088 | -44.43124 | 2025-10-12 00:16:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6fc500ef-d437-3892-8651-4a43237bd5fa | -0.90827 | -47.5504 | 2025-10-12 00:16:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2a122e68-ec2b-3486-919e-673679d3f845 | -3.41748 | -52.18221 | 2025-10-12 00:16:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 98d8e598-6d62-343a-abfe-c1f7a12c5449 | -3.14977 | -44.42998 | 2025-10-12 00:16:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 76610c70-3636-3436-8c0b-8a0b48d736b3 | -3.42165 | -44.13441 | 2025-10-12 00:16:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 00d01336-ca09-3580-82c2-61d9a66908d8 | -4.01155 | -47.34307 | 2025-10-12 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a805ea76-264b-3c0d-a822-a28941484ed0 | -3.75381 | -44.39272 | 2025-10-12 00:16:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb25b8a9-ea48-363f-86de-9f67bddeb9cd | -3.14853 | -44.42104 | 2025-10-12 00:16:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bebaf5ce-b4e7-3e2f-809e-c027a65e431b | -4.46146 | -50.0962 | 2025-10-12 00:16:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| e265d681-b458-3648-97b7-b802faa9c8b2 | -3.29613 | -43.49927 | 2025-10-12 00:16:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5a88bdd8-95a4-3706-abb1-0627657bcf56 | -3.41248 | -52.17766 | 2025-10-12 00:16:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 7853ff4c-2c2b-3bbb-9e85-1c9e68eb904d | -3.50726 | -49.05466 | 2025-10-12 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 12308b86-accf-3d5b-b0e6-510b5e02ac9c | -3.53842 | -48.91729 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| c09a5a9a-f9e6-3bdf-907e-a7532bb83d6f | -2.43714 | -49.37768 | 2025-10-12 00:16:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 646d8d27-8180-34e7-ad7d-0717c3bea716 | -3.43818 | -52.64635 | 2025-10-12 00:16:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 5717e1e1-3e34-38e2-8221-5f1a826931e0 | -2.75015 | -45.3416 | 2025-10-12 00:16:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d4bc158a-018b-3cda-84f5-a0c09c1153d7 | -3.60673 | -42.74479 | 2025-10-12 00:16:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d4a80459-4efc-33e5-a67d-4a77c647d38a | -3.21712 | -50.22325 | 2025-10-12 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| acedb41c-7a3f-3d58-b8e7-714cff2135a3 | -3.67855 | -49.20171 | 2025-10-12 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 91237fab-7b80-354a-8dcd-6bcce685b493 | -2.52872 | -47.80656 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f14aad21-deed-393f-b9de-1bf25814cec4 | -2.26812 | -47.85032 | 2025-10-12 00:16:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5c4ebf69-f37a-3388-9bd0-bb6b217617d6 | -3.51399 | -45.85854 | 2025-10-12 00:16:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d8dc2df4-9a40-3271-9849-b92ba1c14c5e | -2.75896 | -45.34037 | 2025-10-12 00:16:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 4730f261-ffc7-3449-9c08-5742669e51a8 | -2.5382 | -47.80529 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 216.1 |
| 9e0187f2-84b7-3be7-843f-244fadac22a6 | -2.44767 | -49.37622 | 2025-10-12 00:16:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c1d92d86-0ccc-3820-a1f0-dc68b0c8dda4 | -3.21508 | -50.20819 | 2025-10-12 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e31d460d-19bb-3acd-be97-e16bee211666 | -2.29768 | -47.99326 | 2025-10-12 00:16:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fa245a5e-0950-388a-87b1-212f88e1d4b6 | -2.26953 | -47.8605 | 2025-10-12 00:16:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2be77118-8a62-3aa2-8d5c-89a5a0cf46c2 | -2.53679 | -47.79507 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 093db5df-9aa5-341c-b1d3-6fe70265c377 | -2.45644 | -49.36197 | 2025-10-12 00:16:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 37820aca-112d-3ce8-9901-2e521f45fba9 | -2.43541 | -49.36486 | 2025-10-12 00:16:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 47dea2b0-5bde-331f-8ff6-e1cc4d5cca07 | -0.89908 | -47.55169 | 2025-10-12 00:16:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 6bffd9f4-8b72-3104-b77b-866ab2e335ee | -3.53177 | -48.924 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 118324e9-7871-3188-af1c-b10f5c1ebd59 | -3.3534 | -42.16466 | 2025-10-12 00:16:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 13.4 |
| de03adcd-ee82-3be8-97be-8183f1551207 | -3.60322 | -43.8481 | 2025-10-12 00:16:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6cf4a1ee-b843-3785-8986-701954d1dcc3 | -3.54213 | -48.92261 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| ad77137f-71d0-3920-a7a0-880847e6a991 | -3.65904 | -52.50895 | 2025-10-12 00:16:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f4bfd1ae-b990-3c3a-9f33-beece00554f3 | -2.53961 | -47.81549 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| bd9ffdea-7832-3cf5-86d2-7278ae3ff137 | -3.82958 | -45.27765 | 2025-10-12 00:16:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 856dbbda-39f2-3406-b8e3-0a336ffbbc49 | -3.54006 | -48.9297 | 2025-10-12 00:16:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 5da45544-b87b-3da8-8e12-20cd4089bd0e | -2.99519 | -48.74504 | 2025-10-12 00:16:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| b763410e-4058-364a-837e-0eff69cb03cd | -3.20195 | -52.24578 | 2025-10-12 00:16:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 1ed3adb6-280d-3961-8609-bb457346febd | -2.9936 | -48.73321 | 2025-10-12 00:16:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f3524f7a-f89d-3fd9-8647-68df90c61094 | -4.22643 | -50.63311 | 2025-10-12 00:16:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 79d64e4b-3ea6-31dc-8d51-8877ba7a4b91 | 1.90174 | -55.76096 | 2025-10-12 00:18:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 88100c08-59e7-3390-94cc-ab06a7d9a886 | 1.90703 | -55.72627 | 2025-10-12 00:18:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b46f36f1-6808-3749-ab6f-fbb85ed442b4 | 1.91111 | -55.75689 | 2025-10-12 00:18:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 70f8473f-fe88-3556-865a-0f6724acb14a | -9.5173 | -46.4952 | 2025-10-12 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |


[Clique aqui para ver as próximas entradas](README6.md)
