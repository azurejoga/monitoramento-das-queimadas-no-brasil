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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a286363-ed80-33cf-b427-2f11e52e705c | -5.90926 | -51.05519 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc560115-9b0e-3c50-8122-d00a45e5ffef | -5.90808 | -51.0625 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 794e5769-1e4a-3416-8700-68c4a6f8954a | -5.85114 | -51.08764 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 066c0cfc-e6d4-3171-a299-22c7fbf0c1f5 | -5.84775 | -51.08709 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b4bc070-3a73-39da-bdbe-4753be1fd9c5 | -5.5772 | -51.04807 | 2024-10-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eaa63ab-3763-306b-9160-839755ba5afe | -5.50926 | -50.58892 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| af37b635-274f-343e-b28d-0c994636de4d | -5.50646 | -50.58482 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 014b5fc6-b26f-32b8-af11-6d889e442e9b | -5.5059 | -50.58839 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e598039-4151-3994-b107-a67e424d6de9 | -5.50424 | -50.57714 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd0c3c1b-22c2-3ca3-b18e-eea34994f975 | -5.50367 | -50.58071 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04d908cd-72b2-3648-99d9-501c4d689d1a | -5.5031 | -50.58429 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0bf3485-d237-33c5-a15e-b08598ba47a3 | -5.50254 | -50.58786 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5f11c18-8f29-30ad-8250-bdb60b836f68 | -5.50197 | -50.59144 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f056138c-da27-317a-bd26-ac6eb9affee3 | -5.50088 | -50.57661 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d4e9ffc-157a-3c17-af17-4bd474cb4358 | -5.50031 | -50.58018 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ccc3fd7-796c-3029-94a6-933db7e3be48 | -5.49974 | -50.58376 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75085e1e-8a7f-3d25-ae13-c52bc4e63953 | -5.49918 | -50.58733 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f2d0ef1-43a7-3494-bd65-3b9037b4b533 | -5.49752 | -50.57608 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e1bae7a-3d88-3894-8059-d00f260d5474 | -5.49695 | -50.57966 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05513e81-332c-399b-ad66-c09064d70967 | -5.49639 | -50.58323 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a86e4636-21ae-37e7-a5ec-7195cbef2fba | -5.49582 | -50.5868 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4329ae2c-edca-37d4-a804-6d7507d4cd25 | -5.49246 | -50.58627 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d0bd294-29de-3853-bb8c-f89686136570 | -5.49189 | -50.58984 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f430c44e-feb8-3b57-a921-594f23fd4d6c | -5.4891 | -50.58573 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fde776d-21fc-35a5-a494-bba9b292053e | -5.47799 | -50.54734 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f47b2bb5-15a2-3388-893c-5fee6a31ceb9 | -5.47578 | -50.53967 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c901da5c-0428-37cb-86be-d29947cbd901 | -5.47521 | -50.54324 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4201dd94-97d8-318a-b825-0ab3eb904554 | -5.47464 | -50.54681 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0cacf059-d1b8-3d3b-9456-912fdbd1cc3c | -5.47299 | -50.53556 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2d013182-ffc9-3632-8592-fa213a8be357 | -5.47242 | -50.53914 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 13b83895-bc5a-3eba-bd3e-ed427da76d15 | -5.46374 | -51.01173 | 2024-10-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b445bbf-1755-38a1-b79f-aa60564c797d | -5.38845 | -50.643 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32e0dc0b-71bc-39e3-ab46-b6647030ab71 | -5.16661 | -50.71454 | 2024-10-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1f8bd44-a971-3844-91f4-2afa8dae2c91 | -5.16603 | -50.7182 | 2024-10-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95c478ed-a8c4-3fc0-b7b5-a6cae4403407 | -5.16322 | -50.71409 | 2024-10-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baddcdc6-3816-383d-a1eb-57d5850b9497 | -5.16264 | -50.71774 | 2024-10-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c737a411-ba50-3c1e-a734-001f4d236d33 | -6.49134 | -49.81379 | 2024-10-21 04:38:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d1a64bd-3e39-3e60-a300-b96a0172a833 | -6.48804 | -49.81328 | 2024-10-21 04:38:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 996ff77a-fc7c-3c36-94ac-a0309dd9ddd6 | -6.45573 | -49.97506 | 2024-10-21 04:38:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d23c22ef-f753-3d32-8635-1f2dd6291d64 | -5.9558 | -50.1706 | 2024-10-21 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8312b59-a5df-345f-b160-5983a93e41b6 | -5.82491 | -49.9674 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f4da93b-024f-391a-8c60-54d965b14c39 | -5.59418 | -50.15646 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cae3f74-d5fd-3541-81c4-3c846a98357c | -5.59362 | -50.15995 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9aa9bbd-beba-3279-8e55-3bfe487e43a4 | -5.5683 | -49.56842 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9024f719-e4fa-37cc-855c-ea16c46f60bb | -5.5464 | -50.15969 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66295408-bff0-3e39-b139-ac6954777385 | -5.53975 | -50.15864 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df716389-dd4a-324f-b549-7f2df3db6504 | -5.45074 | -49.56049 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38ea22bc-f447-3119-81dc-9fdb27233079 | -5.45019 | -49.56394 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bcc789f-5ce4-3ad7-82c5-872a3f838c2b | -5.44743 | -49.55996 | 2024-10-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 182c96a4-6ebf-38bf-bb67-d66aa6b575b9 | -5.22984 | -50.07678 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e55f39f-3858-3eda-9fdd-9d5027c218a2 | -5.22925 | -49.93002 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd0d926a-29d3-3fdc-8a8b-2bb720bd30c4 | -5.2287 | -49.93349 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 048d387f-ed82-3614-900c-7e95d5334461 | -5.22706 | -50.07276 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb5de739-b725-31df-9141-2a8cb44c9221 | -5.22651 | -50.07626 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e78be5f1-25f5-3392-890a-7c8a582cdf83 | -5.2254 | -49.99727 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bdd82d1-63fb-3b6e-965f-be286fdc32c7 | -5.22484 | -50.00077 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8852f85-9fdd-3ab0-af54-80f564b2293f | -5.22152 | -50.00024 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f71e3300-e0fb-3cad-b1c2-b05ba1b75e68 | -5.22097 | -50.00373 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 434f23a3-40d8-3c53-b277-1636817f10a7 | -5.18437 | -50.0624 | 2024-10-21 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac0a7137-777a-34f6-80c3-c58467e4e9d8 | -5.01317 | -50.84404 | 2024-10-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1acc9c24-f4d6-34c0-9088-b9246cf259ca | -5.01259 | -50.84768 | 2024-10-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c048c260-f41a-369b-8083-064d08f2cb85 | -5.0092 | -50.84715 | 2024-10-21 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a187801c-71bf-3683-8535-642b603418f2 | -7.45023 | -50.13332 | 2024-10-21 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b8107e7-398a-3f0c-8d55-67c533477a90 | -7.03203 | -50.24149 | 2024-10-21 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f73de27-5839-3faa-ab2a-8449c7b1b2f6 | -7.02871 | -50.24096 | 2024-10-21 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aefcf9f-ddf2-3e95-964b-2b0146a0bdf2 | -6.81639 | -50.86807 | 2024-10-21 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85dd319f-bae6-3cf8-9f7c-6a069e1f34b1 | -5.54231 | -51.22069 | 2024-10-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccd7e8dd-07d3-37e8-aba9-ae5e5b4087cf | -5.54171 | -51.22441 | 2024-10-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa5d1b27-c1b0-34ad-a9d6-e7196b2b60e6 | -6.32099 | -51.87112 | 2024-10-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba5445d1-df47-3aa8-a0f2-bd9e29c101f1 | -5.9126 | -51.25172 | 2024-10-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b83dbf14-c55b-3fb4-a5ac-5c37d9efb315 | -4.26948 | -53.72429 | 2024-10-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e06f7578-9648-3e74-a452-5eaede972e0d | -4.30411 | -55.41455 | 2024-10-21 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d231cf7e-5c5b-3bf1-96de-7fbcebc3cc42 | -4.30291 | -55.41578 | 2024-10-21 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa00ef67-e75e-3cd0-ba46-cd302b833d5c | -11.29773 | -56.91351 | 2024-10-21 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1d41c6f-4336-3449-b0b0-60c051a785d4 | -4.76705 | -56.06582 | 2024-10-21 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcdc1484-d688-3790-90f1-41ad9ed06c3e | -4.73164 | -56.07943 | 2024-10-21 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8402c07-74be-38ee-96ad-01c82721e2ce | -4.73159 | -56.08279 | 2024-10-21 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d10b004-50a9-3ed3-8c78-22984fa80d16 | -10.83197 | -58.60535 | 2024-10-21 04:38:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 122a9f07-6de2-3d0d-8646-7de70daf74fc | -10.83089 | -58.61115 | 2024-10-21 04:38:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31b3e3b1-d025-3e90-8b7e-3a02f8ea9d03 | -10.82806 | -58.59892 | 2024-10-21 04:38:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7cce032-727f-390d-bac2-93fb7b66da90 | -10.82598 | -58.61018 | 2024-10-21 04:38:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34b2ae63-dd0b-366f-aca8-1aae65fff07e | -18.29441 | -56.16984 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 63daf453-d75e-3d96-9f62-124a33b6ccb7 | -17.70309 | -54.34661 | 2024-10-21 04:40:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e99e1983-9c16-35e5-9a89-2331796b1d9a | -18.28987 | -56.1738 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 06fa1bb0-9af6-383d-8ada-95c9636ce557 | -17.02835 | -56.0024 | 2024-10-21 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fc402e34-c2bb-30de-b855-26ad74f59454 | -16.92079 | -56.4353 | 2024-10-21 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 85619bea-ebe2-3b41-b379-8f9094fee137 | -18.29881 | -56.17301 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f3d59643-459a-3aeb-a616-baf351221786 | -18.29813 | -56.17057 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9a8ebb18-fbbe-3097-8a10-04f1424f8be7 | -18.29796 | -56.17769 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 39866da2-d9a4-39ab-842d-1e9ac737f746 | -18.29763 | -56.15827 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 58a2c42d-2674-33b9-9864-b6c5bbf47e3a | -18.29731 | -56.17525 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 429e34b3-d2fe-3e6e-87c7-7bcd0b5f40a3 | -18.29678 | -56.16294 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2b8d73b3-fda4-3c82-a965-524f819b7c3e | -18.29649 | -56.17995 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ea95349d-1510-3aea-a5fa-5acff64a05be | -18.29605 | -56.16048 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3d523443-8d8a-3ea3-97ba-abd3d67b386b | -18.29594 | -56.16761 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9fb119f0-5444-3775-86f2-6ddd74d9237c | -18.29523 | -56.16516 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c037f93f-4296-33a6-b0f1-d246a40a6883 | -18.29509 | -56.17229 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6a914255-bc3d-35ee-8364-e194b27024b1 | -18.29424 | -56.17696 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| e687abbb-1d5b-385a-9d8a-ba6fd71ef87b | -18.29359 | -56.17453 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 32b0cc81-ae6c-3574-b5ae-5fd4cb0d68bd | -18.29339 | -56.18164 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |


[Clique aqui para ver as próximas entradas](README49.md)
