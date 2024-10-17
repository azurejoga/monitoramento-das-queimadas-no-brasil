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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c50859d4-fe36-335f-9e01-d773845944d3 | -3.92372 | -42.44011 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fa05530a-62a1-33db-a95a-50c5cf07139e | -3.92318 | -42.40472 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 4ac5cbe4-dfcb-3ec2-9566-e19ae210581b | -3.92276 | -42.41788 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 51908f00-4bd4-3c85-8a6b-1e27f2de592e | -3.92217 | -42.41045 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 1ea7041a-4348-3f04-83a2-0b67f892caef | -3.92178 | -42.42361 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e3d7e439-10cf-3db2-8008-b5082ca27b4b | -3.92115 | -42.41616 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 3909173c-1346-399d-90b2-9d5b17a035f0 | -3.9208 | -42.42933 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ba8e2fe9-228a-34cf-9215-2f89dc45b183 | -3.92014 | -42.42187 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 9a18615d-2332-3dab-85e2-f58f656368ae | -3.91983 | -42.43505 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 470d0f89-7a24-391b-9dc4-3824d799c7c8 | -3.91913 | -42.42757 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d1e22103-0742-3773-8e92-99df11ec8196 | -3.91908 | -42.39955 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 26b35170-9ff4-3827-bb9e-515c9819c4d6 | -3.91885 | -42.44079 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e2fe6509-cb86-30bc-8d58-759e2a09d963 | -3.91811 | -42.43329 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9f1bc486-1fcf-307d-80fc-166bb2b6be51 | -3.91759 | -42.39791 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| d39b428d-26de-31b9-91f5-0592579e291b | -3.91712 | -42.41103 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 0e36cff4-cf25-3554-bd98-a4049d3fd382 | -3.91709 | -42.43901 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4b988ccd-40d9-3198-8f69-4a5d95196b7e | -3.91657 | -42.40365 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 4635a0d5-6546-35be-b2a1-985d82373692 | -3.91614 | -42.41674 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 6306d566-f4e2-32a9-87b8-e5b022d0dcb9 | -3.91555 | -42.40937 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 82005877-d52e-3d97-9dbd-02247a563770 | -3.91517 | -42.42243 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 77881ba2-9ae6-39e4-9825-3b12ea8a984c | -3.91454 | -42.41507 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 7e39f6c2-17fe-3191-a881-e9362adba458 | -3.91419 | -42.42815 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 48f80821-8a61-30b0-878b-f199b7e024c1 | -3.91353 | -42.42072 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| b6269825-3410-372b-81da-730901acfa9a | -3.91321 | -42.43393 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 274abbeb-e061-3fcc-8c5e-2b82b33b79a2 | -3.91251 | -42.42643 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c57e50a7-03b6-3381-834b-b087a84de9bd | -3.91222 | -42.43973 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cd5c0083-fac0-3bf0-bfd3-0a85fca0b7ef | -3.91149 | -42.43219 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bc0341ad-ca13-3312-845f-127fe594ee37 | -3.91149 | -42.40422 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| aba0a310-d203-330f-bf11-dc2ea5549a94 | -3.91051 | -42.40992 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 713639e7-c72f-3e89-a478-9f69fd02d2fc | -3.91046 | -42.43798 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 901466f3-1f00-3f41-9d69-52f97f61369a | -3.90996 | -42.40259 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 716c0896-2c80-35b5-8ab5-4b10ac4951ed | -3.90953 | -42.41562 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 3a07053e-489e-3a91-aa71-63fea11f2ede | -3.90894 | -42.40828 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| e43f59bd-6099-3a9a-ad49-c730029c8f7e | -3.90856 | -42.42133 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 3565feb8-b32d-371f-b7bd-d8418d3a70af | -3.90792 | -42.41397 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| a2ab1da3-5357-3008-944a-ea3f70d6f241 | -3.90757 | -42.42705 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 36263544-b60e-385a-9d94-934de2e130da | -3.90691 | -42.41966 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 698becde-b1af-3efb-b29f-1a86ff3550a0 | -3.90658 | -42.43285 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b50743d6-bf09-379d-929d-5fe4fca63545 | -3.90589 | -42.42537 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f256f9a3-35dd-3e6f-9648-958c8d6bca66 | -3.90558 | -42.43868 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f51f26e5-8df1-3cca-ab86-f4a602d5f3d6 | -3.90486 | -42.43112 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a9cbf7e0-6357-312e-860f-e67679e6a2c5 | -3.90382 | -42.43695 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a31ceaaf-4772-34cb-8c0b-a0e28e900069 | -3.89995 | -42.4318 | 2024-10-17 03:23:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6b335c6d-0ebd-3710-99ba-0f8e7a9e9f48 | -4.48092 | -42.87207 | 2024-10-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cc30be5-54de-365c-8db3-3af2fc05f896 | -4.47778 | -42.87394 | 2024-10-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96cd3e23-5268-37cf-91df-c039627d8a1d | -4.47419 | -42.87092 | 2024-10-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e562a88-6762-3280-ba86-4e61b6802fbd | -4.47528 | -42.8649 | 2024-10-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0d85c30-ff5f-38c2-94f2-9fbe5e62fdbf | -5.96539 | -43.37257 | 2024-10-17 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d69cd3b2-a3b9-366b-97a1-ffa1aba7d321 | -5.96428 | -43.37848 | 2024-10-17 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2a271081-bd5c-3d55-874b-3a45cd861d19 | -5.95859 | -43.3715 | 2024-10-17 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 13.2 |
| de27dd29-60f8-3b37-9c1c-6eb67c362e7a | -5.9495 | -43.38254 | 2024-10-17 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5e39c1fe-8c81-374b-b929-f882190fd3d5 | -5.96436 | -43.36811 | 2024-10-17 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 13.2 |
| dd91d817-901a-39f5-acfa-eae4436d752a | -5.9633 | -43.37391 | 2024-10-17 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 6f20a97c-38d6-3bcf-b942-2095ab4865b6 | -6.21448 | -43.28274 | 2024-10-17 03:23:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0c36523e-7286-3944-8711-3c188153a124 | -5.21285 | -43.19201 | 2024-10-17 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1585d66-dbc7-3afc-a87a-dc48cad083e1 | -5.95651 | -43.3728 | 2024-10-17 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 7b8601c2-8a41-3387-9640-b8e8d1f4ad11 | -5.96647 | -43.36687 | 2024-10-17 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ef23bd26-d6fc-3022-a3b1-5251fc643272 | -5.95747 | -43.37745 | 2024-10-17 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 13.2 |
| d9bbeb05-1d95-3cf5-ac3b-21d2cfd0abf6 | -5.94831 | -43.38878 | 2024-10-17 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 81c9c300-c922-37a1-8398-8a5c6c067e29 | -5.21964 | -43.19317 | 2024-10-17 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 308d555e-da47-3d30-9647-8870eee8078c | -6.21036 | -43.28279 | 2024-10-17 03:23:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 062a3a83-1c52-368a-ad45-aacfae985e9f | -6.68817 | -43.55 | 2024-10-17 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 19127a0a-9bb0-3599-8bd9-1e96c6cd6f0f | -6.46261 | -43.20751 | 2024-10-17 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 32b4d21d-73d1-38fa-be6a-38d6cfcf1e1e | -6.72859 | -43.55837 | 2024-10-17 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| df023f2d-e561-301e-8140-71f6748bfba9 | -6.72743 | -43.56453 | 2024-10-17 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| eff6044c-a44f-35b8-8512-ca6b8d9868f7 | -6.72069 | -43.56316 | 2024-10-17 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 58cc9109-5efa-3adb-bdd3-18c663e6388b | -6.68635 | -43.54887 | 2024-10-17 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6c33b08f-98b8-36b6-8457-703bbf6cc274 | -7.06438 | -42.63315 | 2024-10-17 03:23:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 72ea6eac-645b-3ae3-9d07-d5b0add42bcf | -7.74723 | -42.77974 | 2024-10-17 03:23:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2c6510fc-ab9e-395f-91ad-b1dd30a78fad | -7.18796 | -42.65196 | 2024-10-17 03:23:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8845f4b5-6642-37a4-9e46-8901ff6ae8cc | -7.07177 | -42.62901 | 2024-10-17 03:23:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5957a84c-26cb-373f-aadc-9272048a6e54 | -6.71888 | -43.56227 | 2024-10-17 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2759b5a2-b6c7-3da6-a3e9-29a31a6d3fe2 | -6.68145 | -43.54853 | 2024-10-17 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e769ee71-0974-309e-a463-55e50fc07b94 | -6.467 | -43.20399 | 2024-10-17 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7b54d442-dcef-3e35-824d-e96a504a417a | -6.46589 | -43.20987 | 2024-10-17 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b4c68b99-e99e-3e46-bb8e-6cb9977c8320 | -5.0209 | -43.66211 | 2024-10-17 03:23:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 75cd8bf4-4947-3548-82cb-104ac082330e | -4.12714 | -43.09308 | 2024-10-17 03:23:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8c045d91-dca4-3039-a9ac-7d86929b0dfb | -8.18679 | -44.10765 | 2024-10-17 03:23:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0dc24a8d-43a2-3de0-98d1-a3a526df9044 | -10.696 | -37.04894 | 2024-10-17 03:25:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 114868cc-3361-3899-9f98-ea40d1c2f38b | -12.2096 | -37.77383 | 2024-10-17 03:25:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6f8ff9ac-ecdd-3489-be88-b70f0c64ac40 | -12.20886 | -37.7779 | 2024-10-17 03:25:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2cfb4dd8-872c-3feb-b5a2-965a93b5e516 | -3.5086 | -51.1122 | 2024-10-17 03:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2495c0cf-c761-350a-b9da-b4264ba9d951 | -3.7007 | -45.9223 | 2024-10-17 03:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 413f70e2-5775-33aa-ab14-c0f4aa7c5825 | -3.7009 | -45.9 | 2024-10-17 03:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 6c1c44c6-8dd0-33d2-8399-a390f1d79818 | -3.9078 | -42.4256 | 2024-10-17 03:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 135.1 |
| d01ca886-c0f0-3b07-aa18-0e737db9092c | -3.908 | -42.402 | 2024-10-17 03:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 210.9 |
| dade0927-b060-3b2b-883d-c6be9a8263a2 | -3.9265 | -42.4246 | 2024-10-17 03:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 124.5 |
| 9dca4b71-eb76-3287-b280-d8f08cfd1124 | -3.9267 | -42.401 | 2024-10-17 03:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 189.6 |
| f6739e5c-c5f5-36f9-8022-78f8c350d997 | -5.5716 | -44.8927 | 2024-10-17 03:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 7b19e7af-56d1-31d2-a866-3e43827b7ba3 | -5.5718 | -44.87 | 2024-10-17 03:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 20b8532a-88f7-3515-a733-6a607e84d8d8 | -7.8727 | -45.3593 | 2024-10-17 03:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| c23ebd54-0861-36b4-8411-7761f5c215c9 | -10.129 | -56.7722 | 2024-10-17 03:26:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 3155b591-f503-3b6d-89ac-d9fe6a0bb05b | -17.1667 | -56.8232 | 2024-10-17 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 64a5e715-0ecc-323a-a16a-8305f2178e7e | -17.8638 | -57.4789 | 2024-10-17 03:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| c46a6e3e-847b-35de-a16d-1d22250a5cdf | -17.8049 | -57.4655 | 2024-10-17 03:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 250b0ceb-3089-3eb7-a270-87e3164b0648 | -17.8052 | -57.4449 | 2024-10-17 03:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| e2d1babe-b966-315b-babc-31e1d67447f8 | -17.8246 | -57.4631 | 2024-10-17 03:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 468daf2a-4d84-3354-875a-8277621a5a69 | -17.8444 | -57.4607 | 2024-10-17 03:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 94dcf7ed-c250-3e25-9ec6-f561670f6206 | -17.8641 | -57.4583 | 2024-10-17 03:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 231a4b6a-fcd4-35ee-b34d-63a5aae843a2 | -18.59674 | -41.11915 | 2024-10-17 03:28:00 | NOAA-21 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README18.md)
