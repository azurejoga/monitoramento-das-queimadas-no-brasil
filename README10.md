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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e58378ff-eb45-3999-9e4c-67886160fd10 | -3.4975 | -53.8137 | 2024-11-30 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| d96fa0d3-696a-3fa4-84c2-f980a38e25c6 | -6.086 | -48.0557 | 2024-11-30 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 946c8434-ec5a-3850-883f-71fad4e95c69 | -6.0676 | -48.0352 | 2024-11-30 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| bfa5e3f2-e592-3fd3-b08d-ccbb086f7566 | -3.6758 | -47.1176 | 2024-11-30 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 7dc63db2-1ed8-363a-a975-67acc7f99ea0 | -17.6651 | -57.585 | 2024-11-30 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 49552aa1-a3b9-365e-a017-976f8f579d8e | -1.6419 | -53.8731 | 2024-11-30 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| bc126f44-0812-3ce3-9c3c-e34cda5d886e | -2.5216 | -48.4591 | 2024-11-30 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| ece1fe55-193f-3a5a-bc3a-9b5aa81683a7 | -1.2739 | -54.5587 | 2024-11-30 01:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b745603a-407c-3a7f-886d-5dda5c5d2eea | -17.6654 | -57.5645 | 2024-11-30 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 244a7cc2-116d-3094-bdf7-b1e0e81a463b | -3.4976 | -53.7935 | 2024-11-30 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1e2bed11-6af5-3053-953a-48c786acdebe | -3.9886 | -41.5165 | 2024-11-30 01:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 4e598563-fc7c-308f-ad52-63b6afcf4e87 | -2.0347 | -50.7765 | 2024-11-30 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| e7032bd2-9d3e-3bfd-b427-e309f3d5ede0 | -3.6757 | -47.1395 | 2024-11-30 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| fdb6454f-f2e5-3e7b-8262-7743b9c6c392 | -6.9156 | -43.5418 | 2024-11-30 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 354.4 |
| 72ca059a-da12-3117-a65e-a4e15e86d54a | -6.8965 | -43.5669 | 2024-11-30 01:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a20ed8e0-6cb7-367a-ad7b-68a019545cdc | -4.8901 | -41.2902 | 2024-11-30 01:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 583.1 |
| 7082f431-b2d3-3ca9-9559-3c6a09828d12 | -4.8715 | -41.2674 | 2024-11-30 01:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 193.2 |
| 7d507e5b-8840-3060-b881-eb84472bdfbf | -3.148 | -53.8434 | 2024-11-30 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e2c0b7a2-b685-310e-8420-72ea4236d8ec | -4.8715 | -41.2674 | 2024-11-30 02:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 206.3 |
| a0dc9a38-bd97-3782-8e47-b691c9cda288 | -6.0862 | -48.0339 | 2024-11-30 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 461a2e66-fcc5-3e22-930b-465198ff2659 | -2.0347 | -50.7765 | 2024-11-30 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| c07bb092-da90-3123-87e7-864cf3f7b865 | -1.6938 | -46.7833 | 2024-11-30 02:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 5613d018-b277-318a-bc63-d86f35a9ab0b | -1.0022 | -51.7235 | 2024-11-30 02:00:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 63334dbb-778d-32a7-86b3-641d30c2b4e7 | -3.4791 | -53.8142 | 2024-11-30 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 4cb6c5ec-336c-3cf3-83f3-b1f401842c3a | -3.259 | -53.6388 | 2024-11-30 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| c7b6009d-09d1-3374-9bf7-7a18635453ec | -4.8711 | -41.3157 | 2024-11-30 02:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 343.3 |
| 514c6e7c-e064-32b9-9d77-9c7e9cb673ae | -3.6758 | -47.1176 | 2024-11-30 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 0c78c818-6313-3d23-a6b4-5d9ff2b10776 | -4.8523 | -41.317 | 2024-11-30 02:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 33256105-f47f-3ece-a5dc-1bd2b4f850d5 | -4.8903 | -41.266 | 2024-11-30 02:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| c4c7c04b-a16d-38d2-84ff-5ef24fded6da | -4.8899 | -41.3143 | 2024-11-30 02:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 224.9 |
| 3101b985-cc48-3399-bf88-01f445daf2b4 | -6.8965 | -43.5669 | 2024-11-30 02:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| b0ea1769-cbd7-309c-af01-a8ba607d201c | -1.6419 | -53.8731 | 2024-11-30 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 9160d700-e86e-3654-9136-8eaaeca7c974 | -6.8967 | -43.5436 | 2024-11-30 02:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 0092e119-2435-328d-a039-348f00443328 | -2.0348 | -50.7556 | 2024-11-30 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d20b31a5-a6aa-34ab-9484-3a2c6b4bca08 | -3.4975 | -53.8137 | 2024-11-30 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| a76ccb7e-dba5-3c16-bb19-911568535ac7 | -3.2591 | -53.6186 | 2024-11-30 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a89271fd-8dbd-31fe-8b64-212a4c5c7090 | -4.8525 | -41.2928 | 2024-11-30 02:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| fa41026b-32d7-3f0f-a302-306dad4c7c79 | -3.6757 | -47.1395 | 2024-11-30 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 0d9234bc-207f-360c-a5c7-b249458962a4 | -6.086 | -48.0557 | 2024-11-30 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| b9d177a3-0a19-3009-ac8d-75fd437eb920 | -3.9699 | -41.5176 | 2024-11-30 02:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| b6dfccc2-ad75-3204-8012-1e071c5b4979 | -6.0674 | -48.0569 | 2024-11-30 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| fc2cbb53-f8ff-3af1-a9c6-5b879c6164fd | -1.2739 | -54.5587 | 2024-11-30 02:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 408d00d9-caca-31ab-8e8a-a347482af476 | -2.0163 | -50.7768 | 2024-11-30 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| ac7cf027-add0-3cea-816b-f452c2c6f0a4 | -4.8901 | -41.2902 | 2024-11-30 02:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 446.4 |
| b618cc35-8ed5-3e0e-8123-f5f8c4eb8581 | -3.2406 | -53.6393 | 2024-11-30 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 558c0d0f-84b6-3d92-8d48-8b9b08f9f3b7 | -4.6237 | -47.0069 | 2024-11-30 02:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| c6a5c652-b941-35e1-bb2c-fa283d1604e1 | -4.8713 | -41.2915 | 2024-11-30 02:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 683.4 |
| d24aa32a-48b1-3edc-a5f8-0bf2a268c141 | -6.9156 | -43.5418 | 2024-11-30 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 381.6 |
| 1606c0f2-9a56-3810-8367-4ca767ef2dc7 | -3.9886 | -41.5165 | 2024-11-30 02:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 81242e71-58f3-3af2-ab50-337a109cd759 | -3.4976 | -53.7935 | 2024-11-30 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| dc7b3896-cdb3-35ab-a6c3-c29149a8569f | -6.0676 | -48.0352 | 2024-11-30 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 42e171a5-8608-33f4-afd2-8735c83ec460 | -6.9153 | -43.5652 | 2024-11-30 02:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 214.2 |
| c206a506-bf5a-397d-9abd-58d2feff6d27 | -6.9344 | -43.5401 | 2024-11-30 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 3c4a144c-93f9-36e0-8575-365ddf89bb54 | -6.93 | -43.56 | 2024-11-30 02:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c358f3d5-34fa-31ac-9202-06125fcac885 | -6.92 | -43.52 | 2024-11-30 02:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 90eefe62-c018-30d8-8e07-c7443856cea7 | -4.88 | -41.32 | 2024-11-30 02:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 48b4541a-1b6f-336b-8616-5ec95542b0c3 | -4.88 | -41.28 | 2024-11-30 02:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 40eddddc-9016-3aeb-a283-efa711be8084 | -4.85 | -41.32 | 2024-11-30 02:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 11b2c21a-47c4-3a86-9a46-a17761662493 | -4.85 | -41.27 | 2024-11-30 02:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 85135b8f-c997-3245-aafd-d46d91b5a54c | -6.9 | -43.56 | 2024-11-30 02:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| edaf9d52-c262-3ba3-8a35-9ae1a29d29fa | -2.0348 | -50.7556 | 2024-11-30 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4e791588-1124-3cc7-a157-ed80f0925b94 | -4.8525 | -41.2928 | 2024-11-30 02:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 16e4cd23-56c4-3f7a-877a-ce4e9bb56e86 | -6.0674 | -48.0569 | 2024-11-30 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| e736d61b-9efc-3eac-b884-706cda1ed2a9 | -6.086 | -48.0557 | 2024-11-30 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| be60bbd9-3b0a-3c22-b0a5-6ade6a6ea0e5 | -4.8711 | -41.3157 | 2024-11-30 02:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 223.6 |
| db447f93-ba65-3c5f-a0c5-83285789b9ad | -1.6938 | -46.7833 | 2024-11-30 02:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 650d1192-c202-3316-ae4f-7ac685c8bc05 | -6.9156 | -43.5418 | 2024-11-30 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 411.6 |
| 59d8b641-3529-3826-9d28-dcf5141e045b | -6.9153 | -43.5652 | 2024-11-30 02:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 189.0 |
| f116be20-3db4-3669-b2c3-06d962277390 | -6.0676 | -48.0352 | 2024-11-30 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 1d69634d-e083-3134-842e-eb08bbb562c8 | -3.9699 | -41.5176 | 2024-11-30 02:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 55a6ad2f-20bf-327c-ad98-6b9b7b6cf328 | -7.4987 | -34.9017 | 2024-11-30 02:10:00 | GOES-16 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 44.7 |
| d3c5e294-77bf-320a-98d9-8b0519ef750b | -6.0862 | -48.0339 | 2024-11-30 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| bed2fd19-d544-3736-9aec-e3f9985aa8f4 | -2.0163 | -50.7768 | 2024-11-30 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 8dd1337c-ab15-3147-91c2-d6a0b4a627e9 | -3.259 | -53.6388 | 2024-11-30 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| c0cf3207-112e-3cbd-9abe-6339c3b1f2f0 | -4.8715 | -41.2674 | 2024-11-30 02:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 208.5 |
| e1ab417b-169e-3357-a935-23bfc4e8e0a6 | -3.4791 | -53.8142 | 2024-11-30 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 4cc63a4d-8148-32d4-b563-289669050ee5 | -3.2591 | -53.6186 | 2024-11-30 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0b982b06-3bb7-3bbf-bd01-e02630258b4b | -1.6419 | -53.8731 | 2024-11-30 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ef997374-de6a-36e2-b69b-dd5494377f01 | -4.8713 | -41.2915 | 2024-11-30 02:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 528.1 |
| b5e45bc1-27c0-362f-af2c-5f2936f90689 | -4.8901 | -41.2902 | 2024-11-30 02:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 323.8 |
| 4843316b-a791-3a51-a3cc-c938ea65f43c | 1.1805 | -55.9671 | 2024-11-30 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e0848c4d-1466-3601-8907-45c23473994f | -7.4991 | -34.8741 | 2024-11-30 02:10:00 | GOES-16 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| 6ee2aca1-a540-3f7b-b5ef-ae067d60fb38 | -3.6758 | -47.1176 | 2024-11-30 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| f9a464dc-4127-394c-9922-3dd7a4dcbc1d | -6.9344 | -43.5401 | 2024-11-30 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 077f88f2-b558-3c53-9e7a-a520082219d8 | -4.8903 | -41.266 | 2024-11-30 02:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 2f3d745e-2be7-3d52-a483-702f528b8eff | -3.4976 | -53.7935 | 2024-11-30 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 3f6c1a81-7b6a-3697-bc83-72d563239069 | -2.0164 | -50.756 | 2024-11-30 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b08cb377-9735-3072-a0c8-a10083d59ccd | -3.2406 | -53.6393 | 2024-11-30 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 16f5c213-0a84-324a-b656-027f4e5d23e3 | -4.8899 | -41.3143 | 2024-11-30 02:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 135.4 |
| d432ea49-a8b9-37e4-8250-7ac203e1a0be | -3.9886 | -41.5165 | 2024-11-30 02:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 4537685f-7db4-3525-869d-d4b14df069dd | -3.6757 | -47.1395 | 2024-11-30 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 7523e919-3305-3393-b6ea-f7ae5e9cc3ba | -1.2739 | -54.5587 | 2024-11-30 02:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8e7ebf84-fb33-31da-96f2-131136cb870e | -1.0733 | -53.6378 | 2024-11-30 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 11774fb6-5fe4-31c6-ac7d-c296454adc07 | -2.0347 | -50.7765 | 2024-11-30 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 69e2cac5-6072-391e-b8bb-67fcc15ebcbd | -3.4975 | -53.8137 | 2024-11-30 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 593a17c6-e4eb-36a9-9e48-6ff5b813a39a | -6.8967 | -43.5436 | 2024-11-30 02:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 0c496a93-453a-353a-9269-1b794c0879ec | -4.8711 | -41.3157 | 2024-11-30 02:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 219.2 |
| 0ee72409-c38d-391d-8fef-09d2aaae1eb6 | -6.0674 | -48.0569 | 2024-11-30 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 3760865c-8f6c-35ad-8dab-48d87160b45b | -2.0164 | -50.756 | 2024-11-30 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b4c2cb51-bf99-3188-a7d4-9945591cbd5d | -1.2739 | -54.5587 | 2024-11-30 02:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |


[Clique aqui para ver as próximas entradas](README11.md)
