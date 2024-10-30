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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d25e9887-27b8-3c1d-bf7e-ca4ffcccc361 | -5.9788 | -45.3621 | 2024-10-30 03:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| fcd6c028-9068-37c2-9e13-68ef6acdad89 | -6.4232 | -42.1017 | 2024-10-30 03:25:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 133.9 |
| c0369b1d-84f7-3e90-a64a-4827eaf0a66a | -6.4235 | -42.0779 | 2024-10-30 03:25:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| c7b4a61c-3eca-36e6-8fcf-9209278ffe2d | -6.8408 | -59.0519 | 2024-10-30 03:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| cf396270-3cfe-3c17-a7ac-9faa5221f3fd | -6.8592 | -59.0511 | 2024-10-30 03:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6d975498-7f9c-3ddf-ba3c-34ab7f9f9cb4 | -10.7175 | -44.916 | 2024-10-30 03:26:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 0287d664-bacf-367b-98e4-dfac7a3c9717 | -19.5662 | -56.7164 | 2024-10-30 03:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 2f930019-4564-3bc9-9ff3-a1697dc71ec2 | -19.5862 | -56.7136 | 2024-10-30 03:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 129.6 |
| 26b9140c-398c-354c-b2db-e0aeee1fd1de | -19.6063 | -56.7108 | 2024-10-30 03:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 149.3 |
| 59a68411-e90d-381c-ac72-04da479db6d1 | -19.6264 | -56.7079 | 2024-10-30 03:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 71b9b0cc-c6d0-36c3-8789-768d8c86c587 | -9.81858 | -35.92533 | 2024-10-30 03:28:00 | NOAA-20 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 29da9b82-4e4e-3dee-b5cd-4c632a68cbb0 | -9.81498 | -35.92473 | 2024-10-30 03:28:00 | NOAA-20 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0a2fd03a-1173-33ae-be15-25087cc90c64 | -9.56328 | -37.80781 | 2024-10-30 03:28:00 | NOAA-20 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ea406ddc-9e37-3279-8850-20d76af27ab8 | -9.5452 | -35.69636 | 2024-10-30 03:28:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9373353b-b7f3-3782-b077-a7b9bfcb0c50 | -9.21106 | -36.5764 | 2024-10-30 03:28:00 | NOAA-20 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9187b600-1476-31e2-98c3-1bee1e0576c4 | -9.13238 | -40.92097 | 2024-10-30 03:28:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8cdd78b6-87b9-3c81-8b23-246b96573cb4 | -8.89771 | -44.22646 | 2024-10-30 03:28:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21fd253e-3558-3295-8dfe-6f4e21ac1391 | -8.74901 | -44.71763 | 2024-10-30 03:28:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05bf4cae-2bb6-30b6-a8dc-3d92823c90db | -8.7412 | -39.68449 | 2024-10-30 03:28:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b5dc3fa5-07af-39df-8b65-69a0de59898c | -8.53594 | -40.45108 | 2024-10-30 03:28:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fcbbde3d-93b1-3c26-a9a5-444d6801697f | -8.40989 | -39.96542 | 2024-10-30 03:28:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1f3f13d1-4090-3e51-97ef-ab2b700d14f0 | -8.38959 | -35.02879 | 2024-10-30 03:28:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bed67602-4754-3020-9e4a-4f4229f2bfbb | -8.25215 | -44.86512 | 2024-10-30 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 485783bf-4df1-32a2-8c54-838ae2d6c60f | -8.2196 | -35.66186 | 2024-10-30 03:28:00 | NOAA-20 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9e3fc688-ef51-34c9-a890-8f32e854963a | -8.04795 | -35.3642 | 2024-10-30 03:28:00 | NOAA-20 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5822e08f-389a-334b-a874-ee2abff74f5f | -7.92023 | -42.84107 | 2024-10-30 03:28:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2fba9167-0480-31b6-831a-8076e87cdeb9 | -7.91951 | -42.84492 | 2024-10-30 03:28:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e441b009-29e3-35b8-b749-31c79cedbe0c | -7.87057 | -35.47759 | 2024-10-30 03:28:00 | NOAA-20 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b7414972-9cb3-3f29-be57-2f211cbc593b | -7.76667 | -37.80849 | 2024-10-30 03:28:00 | NOAA-20 | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 847e9633-dd2c-36d0-9f40-773d7e82858f | -7.76254 | -37.80777 | 2024-10-30 03:28:00 | NOAA-20 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4235c72b-9077-38c6-90a1-b71631ae14d5 | -7.7619 | -37.81149 | 2024-10-30 03:28:00 | NOAA-20 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9125ef28-20ea-3909-9b63-48a8a226e6e6 | -7.56334 | -38.7533 | 2024-10-30 03:28:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c573adbd-ab30-3e2c-9657-2455be61e17c | -7.47404 | -34.84451 | 2024-10-30 03:28:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 75aad80c-4545-32ba-8272-8a98d33a288d | -7.34808 | -38.04663 | 2024-10-30 03:28:00 | NOAA-20 | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 79ed6289-6daf-3cb6-9df5-c455c7e00381 | -7.34385 | -38.04588 | 2024-10-30 03:28:00 | NOAA-20 | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| db30eff2-30b0-3d59-97b2-b6294f90dc3c | -7.32928 | -41.86356 | 2024-10-30 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 89997f2d-2036-386b-848d-75f5b64e6f9d | -7.32862 | -41.86727 | 2024-10-30 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 82a05ab9-6fc1-3db6-b28f-a209a4ea66aa | -7.32797 | -41.87098 | 2024-10-30 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d1ef2ea3-bce0-3dec-a692-f5157e6ec8a3 | -7.32598 | -41.88223 | 2024-10-30 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1bf6b630-7e66-32f9-b4ee-c23cd66ff209 | -7.32536 | -43.26038 | 2024-10-30 03:28:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 293b67d5-fe32-3358-8bfd-d060017fc6ce | -7.32454 | -43.265 | 2024-10-30 03:28:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c1e9a0c-64b1-3da1-a104-f9af8cb51073 | -7.32188 | -41.87342 | 2024-10-30 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f3c7cb32-d8f1-31a1-ba4e-27217d63f7c6 | -7.32122 | -41.87713 | 2024-10-30 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fdfdf357-5fda-3af8-b1cc-0c7dfd05cbec | -7.32055 | -41.88091 | 2024-10-30 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86189d8c-b092-3f62-b957-9f01a190f629 | -7.31588 | -42.18872 | 2024-10-30 03:28:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6485bcb1-1180-3e4c-9ddb-32f6c27ffd10 | -7.2799 | -39.44706 | 2024-10-30 03:28:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d9afacce-1363-38c7-a00a-c902893102ec | -7.27511 | -39.44701 | 2024-10-30 03:28:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e78428d0-12da-3fa7-aa24-d5a3ed646e67 | -7.04764 | -41.3779 | 2024-10-30 03:28:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 44d3a815-e805-3f25-bf17-9f8e1c28e10b | -7.04704 | -41.38129 | 2024-10-30 03:28:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2941daf1-f71a-3fdd-90dc-35b89c9996ae | -7.01775 | -34.88363 | 2024-10-30 03:28:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bd7101a5-7e7c-3fd0-a111-1b996e6eee54 | -7.01422 | -34.88308 | 2024-10-30 03:28:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a50244f5-c1dc-3401-9aa8-58c4a26bf489 | -6.989 | -41.34718 | 2024-10-30 03:28:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 428b27b0-7f13-341d-83fa-34beb49bf9a7 | -6.98841 | -41.35052 | 2024-10-30 03:28:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 868ec985-84d7-3bd7-aae7-b95315867189 | -6.98368 | -41.34621 | 2024-10-30 03:28:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0337fbc-36c7-3c22-94c7-f771d24fedcc | -6.9831 | -41.34952 | 2024-10-30 03:28:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6db708e9-a33e-35f9-b55a-0c5448ea63e4 | -6.98199 | -41.32466 | 2024-10-30 03:28:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e9537849-c744-301c-abf8-bcd1967074cc | -6.98137 | -41.32815 | 2024-10-30 03:28:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0bd24389-0510-38e8-ab5e-6d0c8b7aec24 | -6.98076 | -41.33163 | 2024-10-30 03:28:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 304e71b6-e7f8-376e-9c54-6b75e97ad828 | -6.98015 | -41.33512 | 2024-10-30 03:28:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2df5a3f8-d8ac-3a41-8343-e3a61471e538 | -6.97898 | -35.19309 | 2024-10-30 03:28:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e06e2460-e6ec-303e-b5c9-082f9b7ea5c9 | -6.97777 | -35.19126 | 2024-10-30 03:28:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d3af1a7-90e8-3f65-ab10-bf01f88f036b | -6.84336 | -42.81498 | 2024-10-30 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5541a3ff-ffe6-3e07-a91c-45749ddfdcbc | -6.8426 | -42.81921 | 2024-10-30 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f947b81f-c8fb-3cad-9d5e-ec88d68060fe | -6.84216 | -42.81287 | 2024-10-30 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4c98d5ad-eb29-3bfe-9d9a-13a45aa4875b | -6.84137 | -42.81709 | 2024-10-30 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4f84ab0e-fd6a-374a-9ced-2a2260a7bbc2 | -6.8406 | -42.82126 | 2024-10-30 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7f715af0-43f6-365f-80ae-5f48488861bc | -6.83824 | -42.80971 | 2024-10-30 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f2d992ee-3d22-3cc5-82ce-d30737962d52 | -6.83748 | -42.81399 | 2024-10-30 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3823a4c5-c960-371e-bc0e-96d3d42b1473 | -6.83674 | -42.81813 | 2024-10-30 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 09725293-fa25-3cc3-9ffa-e7bb7f677f57 | -6.72515 | -35.01071 | 2024-10-30 03:28:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 4aaeee0a-cd07-395f-b0d5-242c4d7f3693 | -6.72159 | -35.01013 | 2024-10-30 03:28:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 4c967631-1047-39dc-8d5c-1142daf6b187 | -6.71697 | -36.95605 | 2024-10-30 03:28:00 | NOAA-20 | OURO BRANCO | RIO GRANDE DO NORTE | Brasil | 2408508 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d6891489-0638-3dcd-9548-ecc189cf8215 | -6.71639 | -36.95947 | 2024-10-30 03:28:00 | NOAA-20 | OURO BRANCO | RIO GRANDE DO NORTE | Brasil | 2408508 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 369bbbff-2392-32b7-9328-a644f65615e4 | -6.71263 | -37.49812 | 2024-10-30 03:28:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d55724fe-0dea-3ee6-8ae2-d77871cbc89f | -6.70849 | -37.49757 | 2024-10-30 03:28:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4bdd32cb-f3e7-3a4f-9251-9824ddcb02f9 | -6.70653 | -37.49398 | 2024-10-30 03:28:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 46272b8f-30cb-30b0-ac72-2e47dcd04816 | -6.70589 | -37.49788 | 2024-10-30 03:28:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 87055e27-3f01-3323-8308-2b6d5e8af0f0 | -6.70433 | -37.49707 | 2024-10-30 03:28:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2b8edb28-025c-34bd-b490-9ff57f43c7fb | -6.63911 | -37.49191 | 2024-10-30 03:28:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d44c1452-7ed9-3dc5-8914-b6e2d647307f | -6.6379 | -42.83031 | 2024-10-30 03:28:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2b23a8a7-94a8-3d23-b41a-de769ec88fe9 | -6.63711 | -42.83483 | 2024-10-30 03:28:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 103fa219-8022-31d4-a956-a8ea0eed0076 | -6.63626 | -42.82792 | 2024-10-30 03:28:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e8bc50e0-4b63-327e-87d7-9796a6344f5e | -6.63545 | -42.83232 | 2024-10-30 03:28:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| dbb03a4a-94af-3874-8f4e-a162c8f2f89e | -6.6327 | -42.82535 | 2024-10-30 03:28:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9e8c9afd-a10e-3fee-9290-8d994f54f9cd | -6.63195 | -42.82958 | 2024-10-30 03:28:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d5f6353e-a01d-3b63-85cb-f9790097e297 | -6.63028 | -42.82734 | 2024-10-30 03:28:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e61c03f9-c590-3599-96aa-075f10d0feb6 | -6.53596 | -41.56834 | 2024-10-30 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0827b5fa-fad3-327d-9caf-f5c9b753825f | -6.53534 | -41.57197 | 2024-10-30 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aab260c3-57fe-367c-8d26-29ca1e5acc59 | -6.53235 | -41.56468 | 2024-10-30 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 99d67815-755b-3adf-a4c8-9787d4f35384 | -6.5317 | -41.56826 | 2024-10-30 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99513fd2-0fda-35a4-8117-70e5516d771f | -6.53116 | -41.56373 | 2024-10-30 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ca0657b5-0ce9-3b96-82ae-894bb2538dd3 | -6.53105 | -41.57187 | 2024-10-30 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0524bfaf-5be2-39f5-a917-85821378ec3e | -6.52572 | -41.56278 | 2024-10-30 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06bdb350-e152-3948-86d0-81dd02c01d29 | -6.4208 | -42.0968 | 2024-10-30 03:28:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 3265d12d-8a72-3bc8-9100-b1c0eb283c11 | -6.42005 | -42.10109 | 2024-10-30 03:28:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 79b28ba7-efc1-36cf-ae7f-848337f1b37c | -6.41931 | -42.1053 | 2024-10-30 03:28:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 8da62bc5-361f-3780-99eb-22eec24060f2 | -6.4191 | -36.02268 | 2024-10-30 03:28:00 | NOAA-20 | SÃO BENTO DO TRAIRÍ | RIO GRANDE DO NORTE | Brasil | 2411700 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a479091b-734d-3ac4-af14-29f02cda1c34 | -6.41653 | -39.80519 | 2024-10-30 03:28:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 794c6a01-8033-308f-9620-0412ea627ae6 | -6.41572 | -39.8018 | 2024-10-30 03:28:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3b3723dc-9660-337e-bdde-e8b08bb28bd9 | -6.41437 | -42.10032 | 2024-10-30 03:28:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |


[Clique aqui para ver as próximas entradas](README28.md)
