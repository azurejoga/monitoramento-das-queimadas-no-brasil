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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53241989-dba0-3aa1-af3c-68622455e42c | -3.46581 | -50.60355 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 68a9d5e6-94f8-37eb-8776-840123b1e8f9 | -3.43293 | -50.16528 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 26f42089-6fff-3af5-91de-3fd176d3bb0f | -3.43166 | -50.15619 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e09d521f-005c-36e7-b995-b1ec0c77ff5f | -3.31515 | -50.17869 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| fe2a5d78-9b0b-3ff8-9ccd-0da6c58004ae | -3.3139 | -50.16959 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 96abbefb-2838-3b8b-968a-e3d22666f516 | -3.26667 | -50.16362 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 06ec96fe-697a-3f78-a666-c2224c90970c | -3.16763 | -50.44519 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a90cc4ee-75de-331e-98b2-47cd29063b26 | -3.16637 | -50.43602 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6653fdcb-7ce0-32a8-91c0-4e4d034b4c7d | -3.15986 | -50.45566 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ab819ece-8b25-391b-94ba-4cfbc5df3af2 | -3.15859 | -50.44643 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 50306a8b-e956-32c2-9dd5-517c463b98cf | -3.15733 | -50.43725 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 81bb01e3-4835-3e36-abf1-7e0d0c42e0ea | -3.14955 | -50.44769 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| da768eb1-cf30-3165-9dcc-bf5ec46949f3 | -3.14829 | -50.43848 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 939ea9cb-301f-369e-bae6-af13422c066f | -3.14051 | -50.44895 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3c2a8398-8ef4-37a7-924c-63e2774de37c | -3.13925 | -50.43972 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 46fb3702-a149-32ac-b9f5-067f5e272994 | -3.13799 | -50.4305 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 822a97ff-4c97-3fa9-9d57-02ffded84fab | -3.13674 | -50.42134 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0f624bef-f576-3d26-aafe-f3d1796ab15c | -3.65325 | -49.63087 | 2024-10-11 00:56:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 20134026-3d7a-364e-adae-f9e8dd8ac5ab | -3.33097 | -49.15758 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 88f91b1b-2b6c-32f4-8489-c94790df8773 | -3.32975 | -49.1488 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a5100930-6b10-3e50-99c8-99283e2945b4 | -3.32852 | -49.14001 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fb89bbf7-cd73-302a-aebd-65e7318ccbc2 | -3.29464 | -49.10593 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dde31e6d-16e9-3138-8c49-93020d258c26 | -3.28459 | -49.09839 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4e0f9816-f84a-3f42-b965-a864ba77483c | -3.27577 | -49.09964 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 96713416-6f5b-3796-af8f-59e700ee72b6 | -3.26695 | -49.10089 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 0f471c24-8561-3452-b0db-1979a72de4f4 | -3.0553 | -49.37329 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bfa5f9a0-9c6e-363d-a37c-1128ac830f90 | -3.05408 | -49.3645 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f4181158-2ff9-3317-a08a-0383a5ff5cca | -3.02799 | -49.56579 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1e10be75-c75d-3be3-9fcf-4ed68198ba12 | -3.02677 | -49.55696 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 577f416e-7909-34ac-8be4-bcdcb4029bc1 | -2.96208 | -49.36539 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| df57e18d-acb7-3780-a167-440ce3fd5e8b | -2.9577 | -49.20476 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 86077ca7-13a8-3e10-bddf-457d82b45934 | -2.84818 | -49.87123 | 2024-10-11 00:56:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2c6c1ce3-b2ab-35ab-976e-7840de417fb6 | -2.83785 | -49.52385 | 2024-10-11 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 70a588df-6565-3075-9b7b-0dcb5feebf59 | -2.83024 | -49.53391 | 2024-10-11 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 14d94906-4400-35c1-9cff-aace50532ce7 | -2.82901 | -49.5251 | 2024-10-11 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 5c87a419-3017-36b9-8d18-1d4b8048c463 | -2.77979 | -49.25107 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 0f6ff1cd-732a-3238-8b33-b5c2808f3a28 | -2.77857 | -49.24229 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4f52b0cc-d244-3cff-8f9e-2c58c768753f | -2.77734 | -49.23351 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 25edb2ae-fddd-334b-a4d4-26598d25c59b | -2.72816 | -49.54251 | 2024-10-11 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0396342-e77f-3619-988a-3cb2fd128e6a | -2.60073 | -48.95124 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 652f0e5a-0602-322e-9648-45f27995027c | -2.57127 | -49.07789 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| a9552fcc-e507-321d-942e-e54abcb8ee9e | -2.50043 | -49.15057 | 2024-10-11 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ff20eb42-8888-3910-ba1f-72d5ec184260 | -2.90302 | -50.39706 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 407342b2-79d7-3e8e-98ab-f8c89cf8e360 | -4.84561 | -50.91799 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 36fdc7c6-e7c9-3986-9aea-a2594a0b9f53 | -4.83844 | -50.79769 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 09c8c95a-9cbf-3cc4-8876-4eddbd4416b3 | -4.82913 | -50.79896 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| e1760acd-7de5-3707-9baa-2a23c229f097 | -4.82776 | -50.78911 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 32c5ccd1-3587-3e88-bc09-87f350e8df84 | -4.43448 | -50.54251 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ffae3063-e8fe-386a-857e-838a98ca1ffe | -4.34682 | -50.516 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 90ec252a-ed5b-3bec-9fc6-2d28794d7401 | -4.34553 | -50.50645 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 6db0e3d6-b9fb-3f9c-b370-fae4988fa5b3 | -3.69386 | -50.11975 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4fbc7b0a-de03-33f7-a88e-f519ad27d6fe | -3.68489 | -50.12101 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 66b8aff0-9934-3cd6-a419-080779c614e0 | -3.68363 | -50.11192 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b60ee69c-ca40-3667-b38d-9a6096068608 | -4.95302 | -49.76534 | 2024-10-11 00:56:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6da97a8a-4637-32ef-9a8c-0e39efd38658 | -4.84144 | -49.88882 | 2024-10-11 00:56:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0357b588-41b1-3b9c-b2cf-bfcd48947e0d | -3.91137 | -49.69386 | 2024-10-11 00:56:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a8fa9c91-2a30-3cf8-8c88-8d608282cd51 | -6.29651 | -50.82682 | 2024-10-11 00:56:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 230ddd36-fa3d-3c97-b2de-de7f2dbc3b56 | -6.20451 | -50.89812 | 2024-10-11 00:56:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b022f0b0-b1ed-327e-afa2-815a1dc5e8d7 | -6.176 | -50.90215 | 2024-10-11 00:56:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8bb542c5-e074-3658-b337-7ccbece76c0b | -6.10066 | -51.09838 | 2024-10-11 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9a630efd-0024-3443-996e-1c5ebd17cd4a | -5.55002 | -50.42588 | 2024-10-11 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6ab09d1e-da20-32d8-8848-fa386ddcb0f5 | -5.53432 | -50.99097 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ef1d325d-c308-351b-be9b-c231c74d53cf | -5.46933 | -51.04828 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a9b6e97b-a04c-3830-85e7-9c74ed56795f | -5.34168 | -50.99852 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 74224e26-b214-3e83-b1a6-faabae882742 | -5.28725 | -50.99166 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| e1a1c9f3-9ccc-3f10-93cc-9e8b93419391 | -5.28307 | -50.96106 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1afc6ae9-133b-3156-acfd-bc43acaff94a | -6.00029 | -49.67486 | 2024-10-11 00:56:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9144f82b-3870-3f00-aa8d-7ad2bfc80da8 | -5.55451 | -49.58253 | 2024-10-11 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 413851d1-1101-3b7a-8246-cc966e7b1b57 | -5.44207 | -49.56778 | 2024-10-11 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2729c4b9-be9e-3e88-9547-0338d0d69575 | -6.92054 | -50.7503 | 2024-10-11 00:56:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1b297b29-0624-31ee-9278-ad489fa9aa17 | -7.68098 | -50.25008 | 2024-10-11 00:56:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| bbdd8cdd-6f73-3693-9494-aa1e7305aba8 | -9.384 | -50.75264 | 2024-10-11 00:56:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e4646a86-f085-30b8-bc67-dd02a2f9724e | -9.18485 | -51.49889 | 2024-10-11 00:56:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5aa1b16f-5f13-3b1a-9a51-52e79cacb404 | -9.108 | -51.29363 | 2024-10-11 00:56:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d5616bf9-df6c-3ab1-8552-59841083f861 | -9.09786 | -51.29498 | 2024-10-11 00:56:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8b31e166-4125-3de9-bb4b-459a5ff10a7e | -8.89832 | -50.7807 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 20017165-6316-319d-ad13-51cafdaee5a7 | -8.58486 | -50.41764 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a902349a-dc5c-3dd0-9dae-0f30ac3fc250 | -8.56666 | -50.53316 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| bd669c77-3ac7-3705-a21c-8ab0c46d8a2f | -8.48963 | -50.24841 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6e1a6206-8313-3e2f-8722-efc63b8087ed | -9.6288 | -51.76489 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| f89d8473-99e2-3be3-a86c-132c3396a3d4 | -9.49604 | -50.98479 | 2024-10-11 00:56:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2758e866-2c04-31bf-a39e-a0b4fe13a2b1 | -10.44836 | -51.88805 | 2024-10-11 00:56:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| df72b858-f11d-3f1f-8f05-621b1663405c | -10.42023 | -50.7182 | 2024-10-11 00:56:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3d117325-a3cb-3049-87ce-88d90cbb6278 | -3.53794 | -50.85538 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bb6e9154-c7bb-3116-ad27-bd2e4f15677a | -3.50757 | -51.36998 | 2024-10-11 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a793f5fb-cac0-3a99-ae95-fbc8718cf772 | -3.49316 | -50.8028 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 28f02949-c869-3b56-9de1-a34763bed35b | -3.44656 | -51.59448 | 2024-10-11 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 15425760-b4cc-3985-a937-a018916936ca | -3.33769 | -50.80754 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| aab62cce-617e-37cc-860b-f23841d58f7f | -3.28525 | -50.95835 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 124126b9-fb96-363f-a4e2-d0b72781ceee | -3.2839 | -50.94867 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| a34e86df-3415-3a17-8c15-520339e2b54e | -3.27467 | -50.94998 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6cd72e70-0f16-3d95-b14d-3c796285badb | -3.23372 | -50.85759 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a7c0b440-13fe-374a-9ea7-b2cd02e80a4a | -3.23239 | -50.84799 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 5197216a-49aa-38f5-b2bf-ef73a1f73b8a | -3.21235 | -51.51257 | 2024-10-11 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5cf1fec1-2fd1-385a-b6fb-7c959a23c498 | -3.16589 | -51.31203 | 2024-10-11 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 07b1400e-8f10-3350-b6f5-0050fe8521c8 | -2.97379 | -51.36742 | 2024-10-11 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 9c0beca7-6721-38bc-8f26-a19243ff05f2 | -2.9724 | -51.35743 | 2024-10-11 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 346af0d9-5bd2-307c-a19b-34d560f7c215 | -2.80445 | -51.0163 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 37e11f49-62b8-363b-a97a-ddc66c975395 | -2.80311 | -51.00666 | 2024-10-11 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 493cbecf-fecb-3f58-ab66-83e4aeee0a14 | -4.65719 | -50.95624 | 2024-10-11 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README19.md)
