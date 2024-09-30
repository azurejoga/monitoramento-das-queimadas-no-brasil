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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e00c3a2-bf86-37fb-896d-013303bcb4f8 | -19.4324 | -45.8479 | 2024-09-30 00:24:14 | METOP-C | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2f253e84-83e4-352d-8537-044e47e4ddba | -19.434601 | -45.8596 | 2024-09-30 00:24:14 | METOP-C | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| df74a9eb-7828-3134-8113-118879865eaf | -19.4368 | -45.8713 | 2024-09-30 00:24:14 | METOP-C | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bf55ae72-6e3c-3eda-81f5-d1f786165c51 | -19.424801 | -45.861599 | 2024-09-30 00:24:14 | METOP-C | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1ab7003a-b4db-3121-ab68-89870bbc0c1d | -19.427 | -45.873299 | 2024-09-30 00:24:14 | METOP-C | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e7a6a181-9ff2-3b65-86ab-e95d7412d5ff | -19.4293 | -45.885101 | 2024-09-30 00:24:14 | METOP-C | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 63c2b8e6-c8c4-35df-ad47-6711c2d3941f | -18.948 | -43.501801 | 2024-09-30 00:24:15 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 008e34cc-4044-3201-93b3-648c67431676 | -18.9498 | -43.510399 | 2024-09-30 00:24:15 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b9be7fb-c214-311f-a162-04d9360cb715 | -18.9678 | -45.440102 | 2024-09-30 00:24:21 | METOP-C | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bfb33b96-012f-3117-8b99-663391e582c8 | -18.969999 | -45.451 | 2024-09-30 00:24:21 | METOP-C | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ff7db630-87ad-3c2b-bab2-4a37b5ceb832 | -18.9963 | -47.137901 | 2024-09-30 00:24:25 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 640e455e-2a29-3e78-aa41-6409c8e3549c | -17.726999 | -43.3862 | 2024-09-30 00:24:34 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| abc1cbbd-317f-3d8d-9cdf-2634c8aece45 | -17.728701 | -43.394402 | 2024-09-30 00:24:34 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5abb17cb-be38-3e9a-a578-913003d1eff6 | -17.7304 | -43.402599 | 2024-09-30 00:24:34 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e87e95b0-6ccb-3bfb-85c6-7d9d84a28125 | -17.6285 | -46.654301 | 2024-09-30 00:24:46 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 44d158e1-9d3b-314f-9d9b-8606135bd1b7 | -17.626101 | -46.641998 | 2024-09-30 00:24:46 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7fb93382-6ac9-3841-904a-152ead5aca47 | -16.894199 | -45.303799 | 2024-09-30 00:24:54 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| aa81289e-d088-3cba-8b6a-43ef65916889 | -16.8962 | -45.313801 | 2024-09-30 00:24:54 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c0b1dc0e-4616-3054-b978-e6b69a0aba6e | -16.898199 | -45.3237 | 2024-09-30 00:24:54 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| de53bbd7-251b-374b-9242-dea8555a6a39 | -16.882401 | -45.295898 | 2024-09-30 00:24:54 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d3ce9fe9-e2fd-3ba0-884d-42c289e837f6 | -15.8826 | -45.047798 | 2024-09-30 00:25:10 | METOP-C | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 48734bd2-25bb-359e-ad34-e195871b74b1 | -16.094801 | -50.327801 | 2024-09-30 00:25:23 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3c2ca1a0-bf07-33c5-a609-bbd36dbea0a1 | -16.0693 | -50.353699 | 2024-09-30 00:25:24 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ada8eafa-7c23-386e-b6d5-a78df98a7edb | -15.325 | -47.489101 | 2024-09-30 00:25:27 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7867c25c-5d1e-3e29-96c0-8cf8daedc2a3 | -13.7477 | -42.591702 | 2024-09-30 00:25:36 | METOP-C | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e143f124-29ae-3818-8b1b-b772d3fcf2b0 | -13.7493 | -42.598801 | 2024-09-30 00:25:36 | METOP-C | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 29b8e89a-bee4-3e6b-a9d2-dc00c1fde83f | -13.3588 | -42.046902 | 2024-09-30 00:25:40 | METOP-C | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e27745f4-3077-3fb7-9970-6b5d9b2af6be | -13.3604 | -42.054001 | 2024-09-30 00:25:40 | METOP-C | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dabd4fe4-1a2c-34ff-a0d2-7e5c52ef6af0 | -14.7538 | -48.716801 | 2024-09-30 00:25:40 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7a4c1592-8266-3c80-98aa-f44b4be79520 | -14.7567 | -48.731998 | 2024-09-30 00:25:40 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0468ef93-47aa-35ed-b0ba-0052aee649a8 | -14.7597 | -48.7472 | 2024-09-30 00:25:40 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| af536032-9cb4-3b2e-8df8-5a765a104861 | -14.747 | -48.733898 | 2024-09-30 00:25:40 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7585ee2e-e610-3be1-b29e-cc67398d9820 | -14.179 | -46.443901 | 2024-09-30 00:25:42 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1c366567-a26f-30f0-bcd8-d942ce36faff | -14.1692 | -46.445999 | 2024-09-30 00:25:42 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce730fa-31bf-3ab8-aca1-b4b0515cb7d7 | -13.432 | -44.013302 | 2024-09-30 00:25:46 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d68ed7c9-b1f6-3506-a281-924638d2889c | -13.4337 | -44.021099 | 2024-09-30 00:25:46 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f91c17ee-e3f5-3435-b661-0c82e7e67f89 | -12.8094 | -41.303299 | 2024-09-30 00:25:46 | METOP-C | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 51a792b1-c6c5-303f-9dea-83922a511764 | -12.7282 | -43.4706 | 2024-09-30 00:25:56 | METOP-C | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8459078-f09f-3563-af13-708c2b7506cb | -12.7299 | -43.478001 | 2024-09-30 00:25:56 | METOP-C | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 627f2df7-88c4-3ae3-9fa3-88efcbdd34ca | -12.7201 | -43.480099 | 2024-09-30 00:25:56 | METOP-C | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb2faa3e-3201-3be9-9d97-0c7007bf8aef | -12.7217 | -43.487499 | 2024-09-30 00:25:56 | METOP-C | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e534d82-25df-3510-95d2-fee7724bcdcf | -12.7233 | -43.4949 | 2024-09-30 00:25:56 | METOP-C | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d68f88c-b2a5-3a7f-b9bc-28d4d163034d | -13.2511 | -46.348 | 2024-09-30 00:25:57 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f4bed38a-726a-39a6-b58d-23c06196811d | -13.2016 | -46.305901 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e21fee0-1b5a-3357-ae51-46319240f98b | -13.2037 | -46.316002 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b0d7216-7430-3ecc-8481-dc32a51f6483 | -13.1918 | -46.307999 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 30c5edca-d541-3fc5-843c-9987bf1ee8e6 | -13.1939 | -46.3181 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 54d836fd-fd41-3f6b-bab1-ee5ae19659b5 | -13.196 | -46.328201 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a9602e13-aa4a-3ea2-b0c7-ba754ddab447 | -13.198 | -46.3382 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 24c4af16-ae47-3d61-8a80-b219b856bc8b | -13.1841 | -46.320099 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 893361af-f8a8-3c55-b7b4-2465d0b950b7 | -13.1862 | -46.3302 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 90ede0f1-d087-3d4e-842d-bc3ed3b2a79a | -13.1882 | -46.340199 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 97539c51-fa19-39a8-b8b3-90330633a4dc | -13.1903 | -46.3503 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 801ed51c-9926-3c99-8506-4007d0e3cd7b | -13.1764 | -46.332298 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 31d83737-e9e5-397c-9acd-f7b1507a9adb | -13.1784 | -46.3423 | 2024-09-30 00:25:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1cebc71c-0222-3f64-8f9f-b237d306c2ba | -12.8102 | -44.841 | 2024-09-30 00:25:59 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a91558b-a56b-3c4a-837f-6d7d3d2ecd8c | -13.48 | -48.576599 | 2024-09-30 00:26:01 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4c8d0dcb-014d-3986-bdd8-0327036a7f31 | -12.7223 | -46.407501 | 2024-09-30 00:26:06 | METOP-C | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 576dd405-4043-3037-bb4e-a1c39f61f1c0 | -12.7244 | -46.4175 | 2024-09-30 00:26:06 | METOP-C | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd188207-0f4f-306c-afba-7e53b9e620df | -13.1679 | -48.537498 | 2024-09-30 00:26:06 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68770d2b-9efb-332f-8d82-141878830548 | -13.1706 | -48.551498 | 2024-09-30 00:26:06 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d49862cf-892a-3ead-b6dc-355844a23190 | -13.0369 | -48.593102 | 2024-09-30 00:26:08 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e120f0e0-bcc0-33ff-ad0a-5b0ae58535d8 | -13.0271 | -48.5951 | 2024-09-30 00:26:08 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b986dfa-5f9e-3a50-a680-f1f5b3ce2d6f | -11.7801 | -45.437099 | 2024-09-30 00:26:18 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| faf1ec43-f226-3828-97ad-56bc5053405d | -11.7819 | -45.445702 | 2024-09-30 00:26:18 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59dd9d36-7761-3e50-b362-e6e5852b99bc | -11.6028 | -44.805901 | 2024-09-30 00:26:19 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e43c81e9-ae56-357f-a0fb-23eb0e878f15 | -11.6045 | -44.8139 | 2024-09-30 00:26:19 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4062ee54-55ce-3ab8-9807-ea70f4ac2220 | -11.9846 | -47.2761 | 2024-09-30 00:26:21 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f9585a4-142a-3812-a1be-d262a673119d | -11.9869 | -47.287102 | 2024-09-30 00:26:21 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 897ebaa6-0b29-3a03-8340-b6a065e325f8 | -11.9748 | -47.278198 | 2024-09-30 00:26:21 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64e6d3b9-2467-39e6-bb1e-7952b88426f9 | -11.9771 | -47.2892 | 2024-09-30 00:26:21 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93454aa0-59f5-3f7f-8c50-a553ef51f8a8 | -11.9794 | -47.300301 | 2024-09-30 00:26:21 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7d71faf-33de-3c95-81ef-67eb26349bfb | -11.9674 | -47.291199 | 2024-09-30 00:26:21 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 103a6635-188f-3957-be18-2c6febdc1d86 | -11.9697 | -47.302299 | 2024-09-30 00:26:21 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4983d003-97b9-375d-8053-d6afac9258b6 | -11.8575 | -47.3027 | 2024-09-30 00:26:23 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b70cbbc3-1b9d-3abe-8498-67e308476162 | -11.794 | -47.585999 | 2024-09-30 00:26:25 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43b27eb6-ba0b-390d-b11a-5c57bf9a5b6d | -11.7963 | -47.5975 | 2024-09-30 00:26:25 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd8ddffd-bf10-3a04-b5a0-2b1622a02101 | -11.7843 | -47.588001 | 2024-09-30 00:26:25 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb1b9669-90e7-3c1b-9224-804df77fe8bf | -11.7866 | -47.599499 | 2024-09-30 00:26:25 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09d4c936-6dcf-38aa-aba4-d5a1584ff647 | -11.7745 | -47.590099 | 2024-09-30 00:26:25 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9a4ade8-68b3-3f7e-ab61-1bb5ea11a4de | -11.7768 | -47.601601 | 2024-09-30 00:26:25 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a370199b-cffc-3034-adbe-97546fb66e9a | -11.767 | -47.6036 | 2024-09-30 00:26:26 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0969ccc-097a-3c82-8fb9-25fd5094ca2e | -11.2406 | -45.644501 | 2024-09-30 00:26:27 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f48e8521-8427-39b1-b310-f0866bbe0a1c | -11.2425 | -45.653198 | 2024-09-30 00:26:27 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 796a017d-b548-348f-b4f1-c687729d2a86 | -11.2444 | -45.6619 | 2024-09-30 00:26:27 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f93102ca-cfdb-310b-97e8-961864a1022f | -11.2075 | -45.633499 | 2024-09-30 00:26:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6083308b-6b02-3ece-8279-90e17c03a529 | -11.2112 | -45.650902 | 2024-09-30 00:26:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0213bc80-f142-34d8-83ae-d5065152dcb8 | -11.1846 | -45.5751 | 2024-09-30 00:26:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1f9a0d4-9873-3009-ac10-192dc6272cfb | -11.1865 | -45.583698 | 2024-09-30 00:26:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a8aa58c-aa3a-3f27-8546-baff4eb6a8d2 | -11.207 | -45.6791 | 2024-09-30 00:26:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cde05867-f220-3f5c-a765-2d04edc9011b | -11.1838 | -45.665901 | 2024-09-30 00:26:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b98862f-0d65-332b-a71e-758dfd9ee630 | -11.1856 | -45.674702 | 2024-09-30 00:26:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b297a8f-f9e5-3959-9aff-061a76042fef | -11.1875 | -45.683399 | 2024-09-30 00:26:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 758d87fc-656a-3118-bbf0-2c161f51ba53 | -11.1894 | -45.692101 | 2024-09-30 00:26:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4bd2d65-c063-382a-802e-4be734bfecfc | -11.1913 | -45.700802 | 2024-09-30 00:26:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b009f655-ce10-34ae-abaf-817bd58afc6c | -11.1931 | -45.709599 | 2024-09-30 00:26:28 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 86f5aba3-fae6-3f39-91c4-0d13d8e4812a | -12.2151 | -50.6287 | 2024-09-30 00:26:28 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f791338-b5bc-39c9-bc95-f74a6cde3a90 | -12.2188 | -50.6474 | 2024-09-30 00:26:28 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09e4b9e0-b7a4-3a3d-9bbc-7b3f1740135a | -11.1609 | -45.607399 | 2024-09-30 00:26:29 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68c6dc57-7fe3-345d-a765-818202ed8a42 | -11.1628 | -45.616001 | 2024-09-30 00:26:29 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
