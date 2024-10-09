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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b3b35c3-bb9d-3602-b8d6-e3ea78032e3e | -16.92697 | -57.70008 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f6cb17a7-8a84-36cd-97fb-539a00f10bb7 | -16.92581 | -57.50092 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| c8130951-d192-398b-a42b-edd9360d2901 | -16.92414 | -57.68352 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9e06eda8-704d-3ff0-9341-fcf151949fc4 | -17.15464 | -56.82228 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 38118d48-fd09-3339-ac00-ba2836b17af5 | -17.15371 | -56.82666 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 315fecf9-6a15-31b8-acd2-2251b4e91469 | -17.15366 | -57.42166 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 6fdbf15a-0b22-3698-936b-cf4c8a96f9f1 | -17.15292 | -56.82286 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1a320979-f271-3942-8e02-0ac69bd9300f | -17.15277 | -56.83105 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| c855c836-0b7d-3e17-8f95-cbfd11cdb6fb | -17.15196 | -56.82724 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 4e60ea98-3d01-39eb-83d3-99cfd49af46b | -17.15184 | -56.83543 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7c0564d8-ca1d-3b34-85ae-b379664ff900 | -17.151 | -56.8316 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| a1de7525-aef0-3ecb-b43c-6c2dbc569813 | -17.15091 | -56.83984 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 28209cce-62bd-39da-ae48-8f7bb7075108 | -17.15003 | -56.83598 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 6c6fff00-a6aa-31b1-9008-65812e0f1e02 | -17.14997 | -56.84426 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a9565a94-3259-3d42-b44e-468e018a7fd6 | -17.14907 | -56.84037 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 69a876e8-64d5-3d77-81ee-d821b7a5ad0f | -17.14881 | -56.82092 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4d2dea89-d417-374d-b511-4b3f83cc1730 | -17.1481 | -56.84477 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f5e8c2ab-b22d-3bd3-a114-dc5e52ad33b8 | -17.14787 | -56.82532 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 16b2c095-d5d2-3fbb-8559-5843f24e7f56 | -17.14507 | -56.83848 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d22f6925-a58a-3d95-99e9-dbdc25bdc310 | -17.14412 | -56.84291 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4b5b167d-593b-3835-8734-15b3f265c758 | -17.14318 | -56.84733 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c284c7cc-2809-3059-8d8b-a2f5a4d0048d | -17.14224 | -56.85175 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b90e14ab-872a-3a14-ac9a-6e97354585a9 | -17.14128 | -56.84783 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8def5768-2de0-3696-afc5-4006d9495a87 | -17.14031 | -56.85224 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 149a335e-4293-31b6-9e75-00cfc783dc2d | -17.13734 | -56.84596 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a837fda8-cc4d-3b7d-a78a-b431a4db46e6 | -17.13639 | -56.85039 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8af8d21b-8a6b-3000-b9ff-d0f2e4c742c5 | -16.84774 | -56.70401 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| faebb71f-327d-306c-b0d1-0445df85d0a4 | -16.84733 | -56.70012 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9fbe8052-7399-334a-a9e3-ebc28dec20f6 | -16.84638 | -56.70447 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| e656310c-1300-3b23-8c90-8c231c3df2fe | -16.84549 | -56.73647 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bef44333-393e-3428-9a00-c116c6de5859 | -16.84191 | -56.70267 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| d2402ab0-2e01-3930-8f37-52e2355f9330 | -16.84122 | -56.73475 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ed8d26b1-bae4-36e6-bdaa-b86ed1356ab4 | -16.8406 | -56.73079 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 17a9599d-5620-31bf-909f-874af00a6b41 | -16.84055 | -56.70317 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 3908069e-057e-3c77-bc64-3acacc614160 | -16.84028 | -56.73915 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| fcb543db-06c9-37f8-a521-454d15be2bee | -16.83964 | -56.73517 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5b5ad6f5-4c0c-32e1-9dc5-73ccfcfde0b7 | -16.83868 | -56.73956 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c381008e-b815-367f-9d66-eefe30090775 | -16.77495 | -56.70117 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 49d23f64-b377-3084-b5ec-11f389d29e6a | -16.774 | -56.70555 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c6237504-2d6f-390c-83d4-b4d6dda37cef | -16.76912 | -56.69984 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 04ba2331-a91d-37c7-8a67-32a885e06320 | -16.76539 | -56.69591 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1f83eebf-7c45-3fa5-8391-d5800d493365 | -16.76446 | -56.70034 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 1657432f-bb77-3800-9e23-87f02fa0cce7 | -16.76424 | -56.6941 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 35a56f6b-9e84-3f39-907b-884c2b882854 | -16.76328 | -56.69849 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 12fa552d-701b-3d1c-b045-a61c57eb9da1 | -16.76167 | -56.7136 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| f034b4a6-889c-3f2a-afee-3f39d21c4267 | -16.76041 | -56.71173 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 7736e00a-5de7-30b9-8591-9844481205e3 | -16.75955 | -56.69458 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7d4c73fb-1f20-35b1-8d0f-1a58dd98b817 | -16.75945 | -56.71611 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1fd6b9f4-06ee-3fe9-b6af-cd967e400b8e | -16.75648 | -56.70161 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7175fc87-8927-305e-8325-73a01deb2768 | -16.75361 | -56.71479 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 530eeaba-ab5f-3211-bb62-ea1371ee1dd9 | -16.75278 | -56.6977 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6a564217-1ac9-3378-89a8-f19120ead732 | -16.75185 | -56.7021 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 46ca3e06-7888-3a6d-9938-97a0b33ddb88 | -16.7516 | -56.69592 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e6135185-6ada-35f3-8003-446b61fc3db7 | -16.75092 | -56.70649 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 74899e6e-ed63-349e-8223-2905be672ce6 | -16.75064 | -56.7003 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1cd52b52-f28c-3b2d-90f1-9f83747e8b32 | -16.74969 | -56.70468 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 9aca77f5-6d3d-3ca8-a0a6-f57007a3ba8b | -16.74681 | -56.71786 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a8fa9bd4-d3eb-3e0c-a3fc-d6eac8f80a8d | -16.7448 | -56.69899 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 20d7819f-d2e0-3d31-aa96-904046acb76f | -16.7411 | -56.69505 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 485a72f3-1364-3194-be39-d185e3e0eadb | -16.74017 | -56.69945 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3eb4f443-ea18-348b-afeb-d685da2ed974 | -16.73896 | -56.69768 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 293beca5-6e15-3a3f-a0c3-5432c2f7fa51 | -17.15262 | -57.42648 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 945d5664-fd3b-3479-934f-14849dade581 | -17.15159 | -57.4313 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| b218e722-8c8e-39b0-a18d-ae486d1e187b | -17.15055 | -57.43613 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 73105e84-9665-359c-bb75-71e79ca273b5 | -17.14951 | -57.44096 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.5 |
| 077d6215-e36e-3efe-9ba0-2f7b1d18f3d3 | -17.14847 | -57.4458 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.5 |
| e4730106-c1f7-37da-8fb1-90b00633fc94 | -17.14743 | -57.45065 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 819398b1-f58a-3643-a740-d0838b29af44 | -16.96402 | -56.80357 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 76c7d888-fea9-3b32-8236-f8c00e2f6737 | -17.14451 | -57.43468 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 776bdad2-eaaf-342a-95a1-b5ded5237a89 | -17.14347 | -57.43952 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.5 |
| 90ce601b-3677-36fe-af30-3a7ba36154e8 | -17.14242 | -57.44437 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.5 |
| 6338555a-359a-35d9-8e53-7560764a9829 | -17.14138 | -57.44921 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| dffa33bf-e4b0-3a5b-9514-434d87e5b6d0 | -17.14033 | -57.45406 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 81ab4c6f-ac59-3de3-83a4-bfaa96547405 | -17.13846 | -57.43327 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e6dd8dbc-9e92-3898-b524-cf9d4ecf3992 | -17.13741 | -57.43811 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 452c9270-81c3-34e4-a3be-fb245332cf50 | -17.13637 | -57.44294 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 7eab276a-8552-32dd-a0e1-08b8753872ac | -17.02267 | -56.84488 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7a3fd26c-1050-3b4d-b037-c9f003603299 | -17.0168 | -56.84355 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bc5183e7-4afe-368f-8f5a-bd89cb3f9e6a | -16.96498 | -56.79914 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8240f0a1-6e30-3cc3-9680-1cccd8cba489 | -16.96305 | -56.80798 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5db766a0-6630-3567-a2b1-2410cc98febb | -16.96209 | -56.81239 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6f153f85-333c-3896-afb4-d08c37b59604 | -16.95968 | -56.80426 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d9c56372-f88d-3f6f-aef0-4787c150035e | -16.95757 | -56.78522 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 09f00195-73f9-3ce6-aa30-a5b9b7848d82 | -16.95663 | -56.78963 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 88aa23a2-c793-34eb-83d9-51d556a09ecd | -16.95617 | -56.78326 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d8f9e0b7-c9cd-3d63-a5a2-465b36df0223 | -16.95522 | -56.78765 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| cceec86f-94e1-34b9-b9f3-5552e01d4143 | -16.95322 | -56.76874 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7cf60216-297e-39b2-b352-ff7debad488f | -16.95266 | -56.77947 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b2e18786-4a1e-39e5-be4b-d6f5ac4b7729 | -16.95173 | -56.78387 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8d82baa2-6197-3b0b-bf0a-deb6bb2bc3ec | -16.9513 | -56.77753 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c1006f8b-2cb3-3229-a415-c3dd27461594 | -16.95079 | -56.78828 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 927392f2-fc5f-368e-9f45-7dc952b5dcd3 | -16.95033 | -56.78191 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 20848dc1-8341-3f9f-a3a7-ea2efd50b0c3 | -16.94937 | -56.78632 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 27afcc25-7e4b-3f1e-a90e-9d1a36e35947 | -16.94841 | -56.79073 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a57ea2dd-3808-3a3f-a297-aa3606d249e8 | -16.94682 | -56.7781 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d138b6ec-c18c-37d0-bb57-505e7d2b302f | -16.94546 | -56.77617 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 69b80907-1472-328f-b4f3-aa31b458ba53 | -16.94495 | -56.78693 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 632fa309-1a16-38fd-8d0c-14ce6908d35c | -16.9445 | -56.78057 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 02378a9e-0913-31f8-992b-445be49df483 | -16.94004 | -56.78115 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 526ffcae-5a17-3d6e-8aa0-c68bdbe1d639 | -16.93865 | -56.77924 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |


[Clique aqui para ver as próximas entradas](README108.md)
