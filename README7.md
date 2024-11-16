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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fc88812-5f86-34d5-870e-032f02cd72e1 | -2.5794 | -54.418201 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e001426-4e2a-3dc5-b81f-6a12b14b16db | -1.9946 | -46.583599 | 2024-11-16 00:47:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e650112-50ed-30f5-8a54-82f15b5dd5db | -3.69 | -50.114601 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fde0244-9b90-3d32-a262-4bd1cfcbc38e | -0.6459 | -49.394299 | 2024-11-16 00:47:00 | METOP-C | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf1d96c-ed84-3602-bcb0-52540d5d68d8 | -5.9535 | -44.465199 | 2024-11-16 00:47:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 838dcd75-4252-341b-b45f-57728e4b1025 | -2.6063 | -54.5368 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc6d8a86-51ba-3729-9110-78105f4725c3 | -3.7354 | -45.6633 | 2024-11-16 00:47:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c68b1e3-3ec9-3533-a085-7a7c82dd82f9 | -1.58 | -50.450199 | 2024-11-16 00:47:00 | METOP-C | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0931e8e-aaca-378f-a8e2-ea7a7bb190b7 | -2.1526 | -53.718201 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e103e409-3a8d-36d1-bc8b-99f5e52534d0 | -1.2306 | -47.462399 | 2024-11-16 00:47:00 | METOP-C | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d59f457-5d93-3caf-8582-ee71e6c72982 | -1.2098 | -53.560299 | 2024-11-16 00:47:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8161fc8-2dd5-3ae4-9530-c886d856c821 | -2.6044 | -54.528301 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4afd0e3f-5324-377f-b427-6b0ddd62c2fd | -4.0006 | -44.352798 | 2024-11-16 00:47:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51cc7155-8c3a-36e0-a628-951b11a6c9e1 | -3.5395 | -51.483101 | 2024-11-16 00:47:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae679927-9faf-37d1-ba73-ef30997c4494 | -1.1722 | -47.076599 | 2024-11-16 00:47:00 | METOP-C | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae09981d-135b-3f84-81b1-ba4c498fc3d7 | -4.2233 | -50.6847 | 2024-11-16 00:47:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe2aa1bc-d023-378d-a380-6d8e8da9df96 | -3.5851 | -53.723701 | 2024-11-16 00:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c69eed07-7b25-38ee-930b-ea460253d477 | -3.3702 | -45.424999 | 2024-11-16 00:47:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db74f3c1-e768-35e9-8029-1d5aed3b1930 | -4.3749 | -48.568401 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 195045e4-afa7-3f0e-aad5-54bd91d2e22e | -3.7145 | -51.843201 | 2024-11-16 00:47:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4cea177-d289-388c-9051-20d7b3c55d00 | -3.9408 | -46.710098 | 2024-11-16 00:47:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96f76d7d-7121-3931-93f1-995aec71c5d5 | -3.3661 | -54.166 | 2024-11-16 00:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eaddc7e-47c2-3bf1-858f-ced2eaa43c10 | -4.3009 | -48.072601 | 2024-11-16 00:47:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a19158ba-8b7c-3c9b-b8ae-d2f05f9fe5ca | 0.1608 | -51.134899 | 2024-11-16 00:47:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 30180b93-50da-3569-9c42-98abba02bbaf | -3.0712 | -48.019501 | 2024-11-16 00:47:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dd5045c-607d-325a-bfff-32395c43105f | -2.4583 | -53.930302 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cc8548c-b9e7-3a8c-ac95-0754148f82df | -3.4929 | -47.218498 | 2024-11-16 00:47:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9d64f2e-75fb-30d9-bc2d-c35c540a0dd4 | -4.1373 | -49.369099 | 2024-11-16 00:47:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd744790-187c-35ea-bd67-b188394f4e28 | -3.7621 | -50.787998 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0260367-0b32-3471-87fc-13aab72706c2 | -2.1533 | -46.557899 | 2024-11-16 00:47:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfb81c60-4e03-3852-a101-8478ce940a8f | -2.9537 | -54.798801 | 2024-11-16 00:47:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c9c9332-caa2-3af9-b0a3-2191b2e40369 | -2.7671 | -48.575699 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24f5cd12-2218-3b21-a2c5-81ab5cbf15d0 | -1.2343 | -53.712898 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf3c9f1-d091-3c7e-834d-beec9c62ed33 | -3.6162 | -53.997898 | 2024-11-16 00:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bbc37ee-caca-3313-b044-2891fb9abd6e | -0.0206 | -51.251999 | 2024-11-16 00:47:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5ef88804-044e-3407-8361-83663bb5ef86 | -3.2627 | -54.528 | 2024-11-16 00:47:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cba6151-216f-3268-8428-0f1fe3a06131 | -3.3028 | -43.841999 | 2024-11-16 00:47:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f88b09f-fd1c-3d46-8b9f-9baa4cf355cb | -0.8307 | -52.310299 | 2024-11-16 00:47:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 06ba0839-5ea1-3c94-aae0-b9132561dcd9 | -4.2145 | -47.2169 | 2024-11-16 00:47:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d88c3723-3a77-309f-837f-1b50cb9f87bd | -2.6405 | -48.474602 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2431406-3f90-31a0-81f9-891ded95490e | -10.8356 | -44.458 | 2024-11-16 00:47:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98f1b6e7-f819-3d10-92b4-971c058c7991 | -3.5633 | -50.2369 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51e7ad5b-041b-3b34-8a38-5478e3410d10 | -17.556601 | -57.5051 | 2024-11-16 00:47:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 000bba97-6eb9-38eb-9ef9-caeb03fa2431 | -3.5649 | -50.243698 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34970587-5c9c-3a7e-8969-3bd10482b966 | -3.9683 | -45.820202 | 2024-11-16 00:47:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64a32d82-229a-3062-95cf-ad6b864acd4a | -5.7865 | -48.159302 | 2024-11-16 00:47:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 75695391-fd59-3014-911e-510debaf463d | -3.3125 | -43.839802 | 2024-11-16 00:47:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65f16fc0-cd12-3947-9108-7966d077ef24 | -4.3635 | -45.618099 | 2024-11-16 00:47:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 61400e69-8f8e-3243-b9a7-d0f157137212 | -3.5665 | -50.250599 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09d4eb98-8403-3c60-b2ea-3b2626ecf872 | -2.1459 | -46.569901 | 2024-11-16 00:47:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd06be88-1b55-3e6e-a2e0-bdd31da3a69f | -3.2939 | -53.846699 | 2024-11-16 00:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35a147cf-9624-3319-9dd5-7d03e042da28 | -5.7181 | -44.815201 | 2024-11-16 00:47:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d5fcbea-0e79-38bc-9479-71c17a8ce426 | -4.3767 | -48.088001 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1881174f-e898-3f8f-91c0-ff273a777386 | -2.9322 | -45.619999 | 2024-11-16 00:47:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f45c6144-2563-3c44-98f8-319b92b38800 | -3.5254 | -50.790798 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12ad1a68-ad0c-3794-bd34-edead68b308d | -3.5006 | -47.2075 | 2024-11-16 00:47:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74972066-d6a0-327c-9df1-9096c98c3ba8 | -1.8743 | -54.486099 | 2024-11-16 00:47:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f4298f5-aca1-3720-a3a6-bba98919f6e8 | -2.5123 | -47.478802 | 2024-11-16 00:47:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43aaea89-3c94-3a48-a5a0-78f19bd33106 | 0.7979 | -50.741199 | 2024-11-16 00:47:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 088a6683-808f-30e1-93cf-d1bc29a5276b | -4.2738 | -50.680599 | 2024-11-16 00:47:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b79ba44-1574-36b9-9868-862c6e4f109e | -2.6637 | -46.846802 | 2024-11-16 00:47:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c56b24d-a42d-36f7-b1b3-9e526bbd203d | -2.1556 | -46.567699 | 2024-11-16 00:47:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b4d40cf-1e86-3b46-983f-81747502de93 | -1.2326 | -53.705299 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44417f51-a408-39fc-9702-5029ac281de5 | -4.2217 | -50.677799 | 2024-11-16 00:47:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96673f72-1b57-369f-abe3-f72b9c302f7d | -3.5426 | -51.496799 | 2024-11-16 00:47:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 701aed4a-5906-3137-9afd-ffd318a82728 | 0.4267 | -50.9203 | 2024-11-16 00:47:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f6fdd0a3-2925-3222-8927-91d1e82ef903 | -6.4387 | -47.857899 | 2024-11-16 00:47:00 | METOP-C | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a27d54b1-fdb7-3736-911e-27681acbc4c4 | -5.933 | -43.783699 | 2024-11-16 00:47:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54095e4e-46a2-3221-a706-8df2fc4b0513 | -3.917 | -45.864799 | 2024-11-16 00:47:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c1eecce-f2fd-3272-8bb7-8e20ebeae3ce | -2.1491 | -53.702702 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e864a31e-7ec6-3822-ae14-4b54a6920a8f | -3.1205 | -45.895 | 2024-11-16 00:47:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fdbe5a4f-e314-3cf7-9f72-3f5d2bb46ef0 | -5.912 | -46.233101 | 2024-11-16 00:47:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ffa6c36-a31e-3b7a-8297-8f105c742554 | -3.7912 | -50.106201 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa8ee861-72f4-357c-b703-2b291b826d38 | -2.6563 | -46.198799 | 2024-11-16 00:47:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81a9ebc9-60e0-3488-9f26-d6c2e1e5014c | -19.769699 | -55.413399 | 2024-11-16 00:47:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 44d6c9f8-3a1b-3c03-80e5-ae8dabd852bb | -4.2315 | -50.675598 | 2024-11-16 00:47:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a1f878c-9594-3fa3-804a-db0ce8efb386 | -3.2418 | -53.526402 | 2024-11-16 00:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce4b2078-1fee-35bd-9224-be1cadb6aed5 | -4.3733 | -45.615799 | 2024-11-16 00:47:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb5f4064-5198-3b1a-bc94-eb2aa34aa4ce | -4.9914 | -44.320499 | 2024-11-16 00:47:00 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee82793b-cda7-3a48-926a-3576179b674d | -3.4257 | -46.097198 | 2024-11-16 00:47:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca46df2-364e-3eef-8df4-298c57ee599b | -2.8164 | -46.662399 | 2024-11-16 00:47:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 962a07e2-3507-3cad-b3ab-d8fd47c9735e | -3.9976 | -44.339901 | 2024-11-16 00:47:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1e04464-7725-34c3-b799-28f17b3c1e4a | -2.1641 | -48.911598 | 2024-11-16 00:47:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddbadac6-5e7d-3ca4-8323-201cbf29b2e1 | -1.689 | -54.2603 | 2024-11-16 00:47:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50c29e16-43fb-30b2-b1c1-3ff012a78125 | -3.618 | -53.641201 | 2024-11-16 00:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00adc093-1373-3453-bbe0-20a03f9013dd | -4.0073 | -44.337601 | 2024-11-16 00:47:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8515e55-b429-32eb-a63f-67c3678e1d36 | -3.1275 | -54.5214 | 2024-11-16 00:47:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4563f213-a933-3930-843d-34dca6261a77 | -2.7751 | -48.5658 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e754f826-a7e8-3ffb-befb-063b078e525f | -3.2487 | -51.5191 | 2024-11-16 00:47:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba335ce0-419e-39c9-a53e-c381e2b45271 | -2.6658 | -49.118698 | 2024-11-16 00:47:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7343e3ff-e165-3c04-b450-bf7940e579f4 | -2.0283 | -46.374802 | 2024-11-16 00:47:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a48bc3a-dd95-3644-895d-e8fc25fd20cf | -2.1124 | -46.5149 | 2024-11-16 00:47:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1eedf44-6643-36a6-a8ef-0f8b7cf2626e | -0.2586 | -48.518101 | 2024-11-16 00:47:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac0b3349-e986-3aa2-833a-7c10b32e7d84 | -3.3799 | -45.422699 | 2024-11-16 00:47:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9354e04b-6e66-379e-883a-71d63fdb6001 | -4.5321 | -43.567001 | 2024-11-16 00:47:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cb9bc73-a2aa-3f76-8620-d6fea363296b | -0.0971 | -51.270699 | 2024-11-16 00:47:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b1adac28-4cb9-30d6-8cbd-d2ec31a5d10d | -3.0324 | -47.985901 | 2024-11-16 00:47:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cae6545-2ce6-3742-beab-7ff7e469f7d4 | -2.7786 | -48.5811 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57ebdb04-1b14-3625-ba26-4ecc00594bbe | -2.4575 | -53.972301 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfef4d6a-5820-33e6-a53c-5c2ff7de01d8 | -2.9736 | -47.999199 | 2024-11-16 00:47:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
