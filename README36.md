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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08a8314b-c422-38ba-b094-d19c665ccef2 | -2.38851 | -46.55439 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c5551c96-ae70-3f3a-a4c6-a37bffb95927 | -3.2032 | -51.02325 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57b2f964-9348-3a1f-a5db-8ec3283364bb | -2.98226 | -50.3027 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e1af1c1-e99b-365b-b89c-e7fe6888e988 | -2.70433 | -48.64849 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 005de5ad-3175-379d-afd1-fd0ebfba057b | -2.58277 | -46.1145 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccad0bb2-5af4-31c1-847e-14367b2a5935 | -3.77842 | -51.40689 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b1e2c31-50b4-3879-8cd7-a285c0d90a5d | -2.95357 | -49.56771 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46fbe6b6-a896-3959-a3de-7301d3b392a9 | -1.48055 | -52.73586 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ddf54a8e-2484-360a-abc8-5f9adf255ee0 | -2.30612 | -48.54388 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1b088df-009f-3927-96a9-3de0d9505e2e | -2.84971 | -49.23469 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8457928-b1f8-33f4-923a-a0c9bbac1bae | -3.04348 | -49.53535 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd9b6422-8a27-349a-b37a-e7bc658a6d4a | -3.55709 | -47.38338 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1962d122-7260-35bd-bb48-7e67611d876c | -4.08173 | -48.31356 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b94eaff-9350-33ae-9cc6-82356300ffc7 | -4.44571 | -50.69368 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bbf2534-b657-35d1-9bb2-1b207bd6a370 | -3.6419 | -50.13717 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87d429fa-741a-31a1-9243-84700995715e | -4.45014 | -45.86911 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82f16e4d-6f66-3af0-9c03-a203653df646 | -3.85747 | -46.61934 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed74c8cc-748e-3aa6-93d5-6945c00cd6b1 | -2.49484 | -49.20024 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3f30bc1-2081-302f-9d90-ee64b8adc062 | -4.35405 | -46.52653 | 2024-11-06 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2513f6b-9a14-3fba-8ed1-da37f6505cc9 | -3.27009 | -50.33971 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3499315e-f224-35aa-ada4-455e8f4b7a6c | -2.46461 | -48.05446 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4956899-c92d-3c3d-a634-60155cf5e97c | -2.6791 | -51.82838 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a12d7261-bda2-305e-aae7-3b918a7ab341 | -2.79181 | -51.44077 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d5e40e9-f52c-3541-a7ff-80e7d0f575ab | -2.43794 | -49.17365 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c93c331-a236-3e9b-84fc-3eeef71c00f6 | -3.96739 | -48.13255 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6688b59-9bc9-3323-982c-404eae797806 | -4.02441 | -45.66894 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77f4a405-baff-30f1-998e-917d8fc9f106 | -4.2209 | -53.56548 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53fc8c32-e3dc-3790-8c37-b04286d2838d | -3.01197 | -54.09717 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 731d54b9-8a77-3902-80ad-edc89c438eac | -3.16192 | -50.20455 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a6ead059-25e8-3f4e-a218-c7b8b98e7813 | -2.6036 | -48.20667 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf3b9563-6da2-353b-bf79-c5347d1f2415 | -3.36817 | -49.76148 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c93cb30f-7a8b-3fed-ac12-d151782bb29e | -4.12881 | -43.5829 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| c80736fc-1345-3baa-a49b-6d5fc2625dd7 | -1.22783 | -51.95787 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5b9dbff-2716-36ae-8c87-7a3611b7071e | -2.96107 | -50.98738 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c18423a-0904-3deb-b4d5-53def28df6f7 | -2.43685 | -49.18056 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 928cf9ce-c913-3f3d-b919-d174644d62fd | -3.14428 | -51.20356 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 52cdc471-3387-3072-90a3-118aefc52fb1 | -2.45417 | -49.02775 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 744e19d7-b6fa-3996-bdf5-73d01886826a | -2.42576 | -50.51274 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a9c1149-21c1-3430-bace-3ac5ca0eb82f | -3.17822 | -46.61486 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30761f7a-902f-3172-922d-a28ccbeab29f | -3.07733 | -49.57992 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a04b64fd-13d8-378f-bedd-1209d4ad341f | -2.60847 | -54.53895 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8b58b94-f040-3186-9216-e9ffb845fd7b | -3.01466 | -53.423 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5da7fcf7-f87c-30e5-9938-aad9bbfc0b71 | -2.91951 | -48.3159 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 507edcb8-b82a-32de-892a-93b833eacee6 | -4.82443 | -48.56106 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 557a37f6-8432-3bc9-9d04-1227e9d63990 | -4.13346 | -43.57986 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6641a13c-cf63-306f-9e2b-ad259789da46 | -2.96048 | -50.99113 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c52e4c0-0046-3e4b-bf80-d5d623214c55 | -3.18607 | -50.58416 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73be68f5-5a50-35e4-8531-ebd12fab3d04 | -2.90299 | -49.13342 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89c1f04d-bb2e-360c-b16a-9c48b1bcf53e | -2.76464 | -54.07679 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13e2a3de-7183-3f61-bc8b-d9076403fdc1 | -1.08278 | -53.64835 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a50041b2-83b6-3277-a469-e5f575e56a5e | -3.24609 | -53.40722 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b69080c-dc2f-3aee-ab11-68c81d1feef0 | -3.08478 | -50.95876 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c13455c4-99cb-3d7d-b3d3-eadb8ea04720 | -4.23264 | -48.54262 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d754d83e-68fa-3bd7-8ae6-54d00d287b76 | -4.40593 | -45.85965 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da94770a-59f7-32da-a734-8a0c811da0ac | -4.29401 | -46.35073 | 2024-11-06 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 081b7d7b-a95b-3742-a6df-0968efac6ecf | -2.57964 | -51.33939 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41f45413-c784-3579-8313-a7c7ea14df5e | -2.50951 | -47.46305 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45c6cb60-cc7a-3c1c-b6f7-e69a924b8ad6 | -3.3618 | -49.49976 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b65ab9b-874f-3a36-9b9d-111bfe272402 | -3.4845 | -50.38072 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7232d02f-fc0d-3845-ba50-86ff327648a8 | -3.53421 | -40.91473 | 2024-11-06 04:36:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 672c11af-59b1-3bf9-adad-eddd5c31cc0e | -4.59588 | -44.04667 | 2024-11-06 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dafdcf09-0d2a-39b9-b19b-552d5c07b3d6 | -2.30385 | -46.7382 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e34de3ac-8af7-32c6-a396-cec0feb279ee | -3.96769 | -46.47071 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e459dc2-4c54-3929-bdd0-f15a034f77f2 | -3.17925 | -50.58307 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59b2f184-4875-3098-9b4f-74af0cddcdf7 | -3.68616 | -52.29936 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10f1616c-c656-3955-a51b-9c60b1fa970f | -3.14646 | -48.73177 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b140337d-37d7-3a37-a8d3-53df3931595e | -3.33433 | -50.08533 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cd3e9de-939b-380f-b63c-144f84862cf0 | -2.83525 | -52.91191 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 127c337c-952f-3fa5-bbe1-8f8afa60af0c | -3.53268 | -50.34732 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4361a7c1-9e39-3e07-b899-51a779efb34a | -4.18163 | -48.80269 | 2024-11-06 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab4b95c9-34cd-370c-8192-a4ea3760da12 | -2.8473 | -48.45256 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e5bb738-d00f-3234-8995-c157be9e8e3e | -2.71441 | -52.96356 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4764bc6c-739f-395d-9085-668615f1b948 | -3.44465 | -50.13186 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 548d2642-f211-3781-83d8-3ea08d085526 | -3.14767 | -51.3229 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ae47c55-488c-37ff-97fc-4959db066e20 | -3.2237 | -50.91783 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcc90f83-5d10-3797-a92d-163bd7d7fcff | -4.1372 | -49.71078 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39528e41-c8cd-384b-84f9-f673ca7870af | -2.42394 | -49.86345 | 2024-11-06 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26267fe1-86f1-3d1c-bedd-82dde0c8bb10 | -2.92304 | -51.04784 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f18d9720-7c1d-3731-bbc5-f6ed891a6c64 | -3.14733 | -51.18422 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c73e77d-80ff-30d2-95bc-8b010bd823aa | -4.12062 | -46.90876 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb3379fb-3159-37ff-9d6c-6347f9aaac98 | -1.35608 | -51.95293 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bf5ad9e-f231-3f2a-8546-5467dbfdabbc | -2.79435 | -51.35544 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2c00fb1-ff44-3f07-9cf4-8a39d6395e5d | -5.21368 | -46.72334 | 2024-11-06 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9054f901-da3b-3c1a-9c16-dadbbb9dddc8 | -0.96627 | -47.81332 | 2024-11-06 04:36:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5dd554b2-d3e5-37ca-bee4-1d6a3c722c55 | -2.31644 | -48.86541 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9d4ff87a-32e0-3255-8521-76ab5727c3bc | -3.80448 | -52.35646 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c488e82d-812b-336f-96db-ae80df369b09 | -3.2115 | -49.2248 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4a7f4ea-4f7f-3fa3-952f-fa94b9d5e1eb | -2.72701 | -51.71284 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| adf5b158-d1c7-3749-8aab-7a2668dc45ae | -2.89636 | -49.36961 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd94f4ab-fe9c-3157-aafa-3d64676e33bd | -2.22891 | -50.00481 | 2024-11-06 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ffa30c1-751b-3aa9-92a3-738b4d2ebdf2 | -2.39136 | -46.55865 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 483a8ff3-6684-33b8-a7a2-cf6cf868372f | -3.53211 | -50.35092 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5ac8bb65-b9a3-3799-a473-1c58d0daf7c8 | -3.42756 | -49.23372 | 2024-11-06 04:36:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21b52ee1-2290-3054-b9d4-a6f0977d5e73 | -2.36432 | -46.32872 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bbf60f8-32da-3be4-80f6-fcb0f521bb69 | -3.77781 | -51.4108 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c90a465e-92e7-3a16-b541-704ad70ba6b4 | -3.97079 | -48.15422 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a90eb947-e8d4-360c-9135-f8bf01213fb1 | -1.39339 | -52.18478 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3140e2a-5715-3765-8b06-e90fdbc27701 | -3.01779 | -53.42882 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b8fc2c58-ccce-30a9-87cc-7931e1ffc3ec | -2.89249 | -49.37256 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc9a4f62-e5c9-346e-a5fc-69270b8b5558 | -3.67765 | -50.16427 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README37.md)
