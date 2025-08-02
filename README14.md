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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fab7092-a498-3dd6-9198-398fb4f5bea2 | -8.0513 | -43.1001 | 2025-08-02 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.4 |
| a1dab425-5683-39be-bb7d-83a0846f8a6d | -12.6784 | -44.5085 | 2025-08-02 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 7abeec5e-e2bc-3cfe-9aa6-f914779bb9ec | -12.6595 | -44.4882 | 2025-08-02 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 4fc8c8da-10a7-357c-bed2-84f1ff308c06 | -8.0324 | -43.1022 | 2025-08-02 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 9c7599c0-d1be-3a5a-ac9c-b0ffedadd1cf | -8.0321 | -43.1257 | 2025-08-02 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |
| 8d0e56ec-fd4a-36c0-ab52-e5a13658917b | -8.0324 | -43.1022 | 2025-08-02 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.5 |
| c471bb03-035d-393e-9f83-6b2275707094 | -12.6591 | -44.5117 | 2025-08-02 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ecbea795-79c9-3910-8a7a-77a18dcc9205 | -12.6595 | -44.4882 | 2025-08-02 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 807d51c7-481c-3c58-beb1-4f5ad70e7696 | -12.6784 | -44.5085 | 2025-08-02 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| ce57564f-fa7a-3fa8-ad13-c93e164738c1 | -12.6789 | -44.4851 | 2025-08-02 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 3e3ed777-d140-3049-aa03-9807f0577636 | -2.92092 | -48.67387 | 2025-08-02 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dad789f4-897f-33fc-a5c9-0550f6c5600a | -3.59608 | -41.65228 | 2025-08-02 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3bf7791e-2bed-3c6f-895a-087cb4459dbb | -2.90255 | -48.24973 | 2025-08-02 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8cff9853-c2bf-3eff-a1b0-be53e1ca985c | -3.51656 | -47.21519 | 2025-08-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a767458e-b4a5-3a1e-905b-d77ff8b98374 | -3.9947 | -43.23325 | 2025-08-02 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24aa9c32-9482-381b-943d-1f609957186c | -3.58062 | -47.51342 | 2025-08-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbe1dccc-b3ca-3fc1-842f-ba33c2efa550 | -3.99547 | -43.22808 | 2025-08-02 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e9efc70-f1e0-38f5-9463-ae94224dff94 | -3.58509 | -41.65395 | 2025-08-02 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3a939c0a-1b84-3d54-a4bc-6717845df0b5 | -3.51521 | -47.22117 | 2025-08-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 08977ddd-f404-3aff-bc0b-dbf09d861b0c | -3.51951 | -47.21747 | 2025-08-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f519221-edba-3d51-a871-d423a825ce16 | -3.43843 | -48.95626 | 2025-08-02 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d93a76aa-3792-3e75-9894-b01084615b7a | -3.52726 | -52.86718 | 2025-08-02 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 533f15d3-936a-3330-b5b6-f658d5ba6dae | -4.20882 | -46.43908 | 2025-08-02 04:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5251a987-f8b0-3c06-944e-f4f97d8e4ee3 | -3.77433 | -41.68174 | 2025-08-02 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8231f23a-c5e2-36cc-87a1-2906d6984f31 | -3.43505 | -48.95573 | 2025-08-02 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63119bc4-9c3f-3eca-9c36-dff1450aaa33 | -3.99616 | -43.23053 | 2025-08-02 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 554a1d0d-2176-36bd-9cbe-047a56e83e69 | -3.04276 | -49.44513 | 2025-08-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc712060-5f32-3926-973f-0bf5634f58bf | -3.5818 | -47.51527 | 2025-08-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 624687b8-14d1-3d02-855b-efef7f3132eb | -3.25175 | -43.26421 | 2025-08-02 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a7c32b1-c029-333c-9354-c102e61b6288 | -2.58555 | -51.92492 | 2025-08-02 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ba6acff-ea6f-36d6-b4d9-cdd30eaa5b5a | -3.77384 | -41.68502 | 2025-08-02 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 773f6cd9-5c6c-3b88-8fdb-cf0dbcd82295 | -3.77957 | -41.68265 | 2025-08-02 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d8ae87f9-dacb-3b3c-9bfe-5375362f8229 | -2.9901 | -49.32184 | 2025-08-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d6b06ba-93ae-352f-94ce-04c0d20547af | -3.59036 | -41.65472 | 2025-08-02 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2995ba64-8b81-3a2a-b24a-4a5f585121e0 | -2.906 | -48.25027 | 2025-08-02 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c437f43-1e45-31b2-87f3-7d9ce0d58ac2 | -4.02954 | -48.0626 | 2025-08-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf110287-c379-37e9-863a-270319b26add | -3.24879 | -52.85654 | 2025-08-02 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b560143f-81f2-3ac9-9382-b7ac46272079 | -3.79013 | -49.42747 | 2025-08-02 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3b1fba0-4ac1-365f-b068-4ddb6f3f8e36 | -2.60636 | -51.9467 | 2025-08-02 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02430716-d2e4-3a90-bcb2-5de03dac3511 | -3.91089 | -42.42131 | 2025-08-02 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f6d46a28-4942-38fc-8204-1eedc320c12f | -2.81177 | -49.20085 | 2025-08-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4156a27-3935-3d56-af83-bfba64c47d9d | -2.90587 | -48.29644 | 2025-08-02 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ff30c72-ef0f-39ec-aba2-398ebe1f2d04 | -1.29147 | -55.74786 | 2025-08-02 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3311b644-e110-3c25-ab40-0564f55894d4 | -3.53178 | -49.97398 | 2025-08-02 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17a8a62f-08dc-3e89-9530-3a44293134c0 | -3.24959 | -43.26263 | 2025-08-02 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7152fbc5-5451-397a-a327-129923e6fcba | -3.51587 | -47.21694 | 2025-08-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fe15d9f1-afad-347a-9577-a0da276b43b3 | -3.78678 | -49.42695 | 2025-08-02 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc950645-618f-3288-886a-c593ff808942 | -2.81059 | -49.00789 | 2025-08-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb63d497-a01d-35e3-91e0-5928c033af8f | -3.9109 | -42.42118 | 2025-08-02 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7dae65ef-7f18-3275-a3ed-e0c13afd3774 | -3.59052 | -41.65383 | 2025-08-02 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b5aa9219-61ab-3970-aebe-f51f74bcfaed | -2.98675 | -49.32133 | 2025-08-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15cbec8b-20ce-3efd-aaf9-d5615621bb78 | -2.81122 | -49.20438 | 2025-08-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acdbfe4e-dd3b-3e92-8058-01d8fcef226b | -3.59881 | -44.7968 | 2025-08-02 04:44:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 203e0f25-def0-35e6-977c-519a48829aba | -3.51593 | -47.2194 | 2025-08-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 32cd4b23-bcb0-3e0b-8a38-bc712df78312 | -2.58217 | -51.9244 | 2025-08-02 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4623a3d1-6da6-32d8-8b18-3a7632ac965e | -2.92432 | -48.67439 | 2025-08-02 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56ab6bfc-3a5f-37ad-b2ac-94e19d85f7ec | -3.58526 | -41.65307 | 2025-08-02 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 736f289c-1102-32f1-b810-a023cfedda5d | -3.73361 | -49.68154 | 2025-08-02 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d84f1c02-9b15-3b7c-8964-a926c95d5b17 | -4.02894 | -48.06651 | 2025-08-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b45aa6c4-6cc7-3420-9ea1-915b596b397b | -2.94279 | -40.09788 | 2025-08-02 04:44:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b76fa33c-fef2-35f1-91a7-1f65012cb610 | -3.59627 | -41.6514 | 2025-08-02 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14519adf-afc3-3679-9ce9-20b296513412 | -2.99678 | -49.32286 | 2025-08-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b79edab3-8108-3236-9db0-c432f0d44992 | -3.48474 | -51.188 | 2025-08-02 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f38a460-ced4-3146-b45c-d8370db81c79 | -3.59081 | -41.65151 | 2025-08-02 04:44:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8eb17576-645d-3bb8-a2b2-f93f26c32bca | -2.60298 | -51.94618 | 2025-08-02 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 847bdda5-e241-3f66-8464-d2b68ba0a3a9 | -2.81068 | -49.20792 | 2025-08-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68a41a72-666c-3342-934c-3805fb0b2b48 | -3.58359 | -47.51809 | 2025-08-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97a58cb9-1fbd-3340-8b8c-a8ae8f4d80db | -3.66473 | -50.95053 | 2025-08-02 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e1d393c-4cc6-344c-8c8c-6415ba040266 | -2.80877 | -49.00717 | 2025-08-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 480ea090-bdd6-3583-a6b3-5f60eea73e34 | -10.08143 | -46.77585 | 2025-08-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ed36042-7d8e-3f1b-bab4-28d352a36231 | -6.52677 | -42.81033 | 2025-08-02 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3778874b-1f88-372a-972e-a7b5d04bb862 | -6.73177 | -43.98629 | 2025-08-02 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df1275ce-7d29-3c9f-b714-a337c8507924 | -6.78852 | -42.98223 | 2025-08-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7c83a832-4949-34d6-9055-e46abe072b84 | -10.59421 | -45.26492 | 2025-08-02 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dbd2ee8f-e469-3baa-8577-e73eea06cc09 | -7.34987 | -44.66127 | 2025-08-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d3d8926-98ff-3a08-b38b-25726bbeac7e | -8.98747 | -45.68523 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39846970-4f4d-3cb5-9af0-fba2f976773e | -10.62341 | -45.29723 | 2025-08-02 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e355b769-b1d6-3671-a0b0-1036229221b4 | -8.04868 | -43.1069 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 055e193f-8f6f-3a38-83aa-b6242dbff04e | -11.9452 | -44.91796 | 2025-08-02 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5296e84f-c080-38f6-b60a-8c6b17b92b11 | -7.5821 | -44.80696 | 2025-08-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9da92320-d27c-3fcc-bd0a-c0068f5ccfc8 | -9.05508 | -45.06003 | 2025-08-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 205080de-e271-3f61-b2f4-3c7f6f45bf36 | -6.69883 | -43.07579 | 2025-08-02 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1b10dcec-c6ad-3932-95f6-2af390b99a64 | -7.74671 | -45.14181 | 2025-08-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb85623b-c2b9-3e4c-b22b-127f90ae241a | -7.72227 | -45.83859 | 2025-08-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72a87f11-d89d-36e6-994e-3c0cfd0c9357 | -10.58383 | -45.27306 | 2025-08-02 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acdf4fd2-540d-3fdb-b89b-9724c10e0d08 | -7.27354 | -43.39429 | 2025-08-02 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c2d1c6b-5470-364f-a655-7f78598ddf3f | -7.25876 | -43.39199 | 2025-08-02 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0cc9b3b6-eb8f-31c2-aaf8-472a06875bcb | -9.89616 | -46.6407 | 2025-08-02 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbe91201-1b75-3483-91d9-9a36ba423464 | -6.56962 | -43.91553 | 2025-08-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49d8adfd-8bd1-33e6-9b8c-2b228b83186f | -9.38983 | -45.50329 | 2025-08-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b5302163-8e8c-3203-873d-ad8d6b9fd2b0 | -8.02781 | -43.14661 | 2025-08-02 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1f034711-3481-3d09-80e4-2b835957c194 | -6.70828 | -44.35526 | 2025-08-02 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02f60053-80eb-30bc-b81f-770ab9beda3a | -11.95264 | -46.71222 | 2025-08-02 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cc4d9fa-5212-3dbf-a65f-6211c1019427 | -8.23076 | -49.93409 | 2025-08-02 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f0b3f9f-9a63-33d3-87ad-2e97d39ae477 | -11.07103 | -48.35788 | 2025-08-02 04:46:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00e570e3-462f-3e6c-8a11-4a440bf5d570 | -7.69168 | -45.11854 | 2025-08-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d0063d0-fca4-35f9-8f64-243daeb95134 | -8.44315 | -47.486 | 2025-08-02 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee703a0a-47b5-365d-b569-92970ce9437a | -9.05957 | -45.06088 | 2025-08-02 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6eee7068-1cce-3df6-a8e6-a7385565fe5c | -7.881 | -45.53818 | 2025-08-02 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 265b7d34-36be-331e-9da4-b5260b71414d | -11.6143 | -50.45346 | 2025-08-02 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README15.md)
