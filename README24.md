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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82a80ebd-cf45-3585-83fc-92b9cd606c77 | -17.97786 | -52.80041 | 2024-10-22 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eb5105e-2b62-3083-8249-3e7a7c0f468a | -17.83843 | -57.60319 | 2024-10-22 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cef97673-07eb-39e7-97c9-0ebc51493b1c | -17.83761 | -57.60703 | 2024-10-22 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cceeb993-072b-30b3-8ba6-ab0015ed845d | -17.83372 | -57.59827 | 2024-10-22 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 64afabc4-b24f-3d0e-b300-d39c28db2b49 | -17.79795 | -51.81296 | 2024-10-22 04:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 601cbd9d-61d5-3f5f-990e-8741e7609648 | -16.96486 | -52.02022 | 2024-10-22 04:21:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 799e4133-5892-34ee-a9a8-7646ae05b53c | -16.9639 | -52.02546 | 2024-10-22 04:21:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1432c67c-60aa-38d0-a59d-e138079b709b | -16.75135 | -50.76368 | 2024-10-22 04:21:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29a4b977-1128-3263-895a-6ed9a0bb9478 | -16.56508 | -52.41463 | 2024-10-22 04:21:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b407c8fb-aaf4-3d94-89f1-5fec8ba9feb8 | -16.56441 | -52.41825 | 2024-10-22 04:21:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0857df6-ae97-37d7-8e51-2a929d33e8da | -15.69513 | -50.46572 | 2024-10-22 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 774b7f0b-2a03-3de7-a7a7-5bcc460a8be8 | -17.77645 | -57.54613 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9f03a2ca-c2cf-37a0-887f-9a06f4d31db4 | -17.77097 | -57.54483 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 759db9fc-b2af-387a-84b7-d81a41cd67ec | -17.67513 | -57.40199 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f998ca2c-4a62-3797-a7e2-0c6d32f82741 | -17.67435 | -57.40569 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b81425b7-73a5-34bc-a742-bb17e1b8fbf8 | -17.66813 | -57.40812 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f7487b00-e05a-37e5-ad4f-4b01ee58c170 | -17.66805 | -57.43549 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fbd958ff-8fb6-393c-8572-3db06f99703e | -17.66726 | -57.43921 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cd50f163-7b3c-36f6-adf9-645e342db0f5 | -17.66269 | -57.40685 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d3442fd5-d7ee-3e24-ad4f-6d8de6415898 | -17.26051 | -57.30564 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 99da07f7-2da6-31ac-9f93-2f5801ca2da7 | -17.25973 | -57.30935 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d81967e3-9b53-3758-85bb-7cc1271c3958 | -17.25663 | -57.29691 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 354b7598-2096-3c3b-912a-83e3ceafe67e | -17.25585 | -57.30064 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 96edf169-4f83-387c-87f0-2a3582ebcc06 | -17.25506 | -57.30436 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b2211dce-26c0-3c6f-a2f9-89774786007b | -17.25428 | -57.30808 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 17fd627c-390e-301d-9586-a6d77c9660fe | -17.22564 | -57.28087 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 02611a9f-594c-3212-b3e6-c14720e6f39a | -17.22554 | -57.2819 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b0c2ae26-625a-3c2d-9f1a-c46bfd351ab7 | -17.22488 | -57.28458 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 92a7e3a3-2121-38cc-bc4c-8a39e8af1776 | -17.22475 | -57.2856 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 24b432ae-c506-37e6-a8ba-2c1c0eda4c25 | -17.22411 | -57.2883 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a44e2f05-70e8-37ce-9934-357bff2415fe | -17.22189 | -57.32695 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 533e0b31-5bd5-3743-b901-21a9ee8c20c9 | -17.22147 | -57.32786 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e255cc66-1775-37ce-89ac-9f1befa1a57c | -17.22112 | -57.3307 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2b8932a0-b647-3a55-8adf-9f19282b7a4b | -17.20557 | -57.51109 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ab8741a7-e87f-30e4-a47a-9b03fd085507 | -17.20475 | -57.51493 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f54ed965-4cb3-35b9-b270-a311c8323df1 | -17.19923 | -57.51364 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ce148aea-0e74-30d3-93f0-04c072687530 | -17.06276 | -57.48091 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d7b9cead-48b1-3607-b2e4-bf10b6a6d773 | -17.03502 | -57.45406 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 55f74f0f-7e60-38db-85d8-dcd989862f5d | -17.02869 | -57.45661 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 340dcb9f-f96a-37ba-bed1-e0974d5899d6 | -17.02384 | -57.47971 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fe0350f0-decf-35c1-b7d8-7920b198b5b5 | -17.01993 | -57.4707 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 877e36b4-fa81-3c08-b550-ec210227ddaa | -17.01974 | -57.33465 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a8035658-0474-30a8-8735-8987de012b75 | -17.01912 | -57.47455 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cd06382f-6087-397b-bbfa-ce612b57cb8c | -17.01894 | -57.33843 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| ab625265-a348-3bcf-898d-608c42c3aeb2 | -17.01814 | -57.3422 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 4d20898f-60a8-3b14-be0c-8146cab4f298 | -17.01734 | -57.34596 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 06e29b71-c7a4-3530-931a-2df9456692da | -17.01521 | -57.46555 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ba011c8f-bf03-3dcc-bbc6-6521093d262e | -17.01425 | -57.49772 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 95c0460e-0171-353b-9a99-7ffd98443972 | -17.01343 | -57.5016 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 3b30cb15-5b1b-3704-b721-7bf31f2f87da | -17.01266 | -57.34092 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 433e5028-106e-33b7-9c72-6f8e669e3d0e | -17.0118 | -57.50934 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 8fc723ad-dc62-341d-bcbe-3405fb3d92aa | -17.01099 | -57.51321 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 785cc8dc-198e-3a09-a4fa-f4d348e76bcc | -17.00935 | -57.52097 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| b01a23b6-7cfd-3a02-be07-61b628d6618a | -17.00853 | -57.52486 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 38107ed4-01a8-3cab-962a-ab5570c81e1a | -17.00772 | -57.52874 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 944db820-8f7a-3d9b-8994-184a309cda07 | -17.00398 | -57.49127 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8603e398-0db6-3f4a-85d9-40b9d27ac9de | -17.00317 | -57.49513 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d81398a2-7b37-31f0-9c16-898532762b64 | -17.00299 | -57.52356 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 1cac3231-9f88-3ac0-9bf8-02ec37cd961b | -17.00217 | -57.52745 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| ad63f14e-98a1-348e-bf78-e2b5101e7853 | -16.99908 | -57.5145 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e349e1bf-d55e-38a0-bd1f-8ee81282afac | -16.95716 | -57.53044 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| a66180b3-5f1d-36b2-9c54-cad986981fcf | -16.95554 | -57.53825 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1c1b9389-82bf-35c1-8580-86a78ec27801 | -16.95526 | -57.52877 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9d3b900f-b8c8-36fe-bb43-f8dbe3db8096 | -16.95443 | -57.53267 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 87e1b8a3-df87-3b39-b120-c49078a5009a | -16.9536 | -57.53656 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 57dd812d-f895-3c31-9a93-e30863f69348 | -16.9516 | -57.52913 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 289ab9ed-1eaa-3d36-a92d-0900d2a581f5 | -16.95079 | -57.53303 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 23460cd5-2787-3711-8dde-c68edbd96ea1 | -16.94998 | -57.53693 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 2a82d12a-fc6e-3832-8630-8f87bbf5df36 | -16.94971 | -57.52749 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 257db416-761c-3b25-abaa-e1aaf615ef42 | -16.94887 | -57.53139 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 321fd188-b0ce-3236-aedb-017fbdf27a02 | -16.94804 | -57.53527 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5c3ca00b-08f8-3677-be34-861c9ef59f19 | -16.94604 | -57.52784 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 01e77fb0-e45a-3524-8525-f0ed93352be2 | -16.94523 | -57.53174 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ee40a6f7-6e31-3de8-a9a5-65f1175245c4 | -16.94442 | -57.53563 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cb8456a7-aea0-3388-b4ad-5421c4f31e4c | -16.94248 | -57.53399 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| efca4df1-abb1-3d78-923d-81508b128322 | -16.93967 | -57.53044 | 2024-10-22 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6770594f-7120-3045-85c8-aa21fbd85ac5 | -16.09006 | -60.13179 | 2024-10-22 04:21:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e1d80f0-7dda-3b5c-988f-971888cdd947 | -16.08713 | -60.12552 | 2024-10-22 04:21:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a2c83b9-ffe2-3afc-b9cd-7bce10d5996c | -16.08584 | -60.13143 | 2024-10-22 04:21:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c36727c-702c-3375-86d1-4c2fc0134cee | -16.08483 | -60.12425 | 2024-10-22 04:21:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3d07af1-eca5-3822-822e-6a860cf63611 | -16.0835 | -60.13015 | 2024-10-22 04:21:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9e634ed-ebd0-3857-a08f-21b17c6b9392 | -16.08057 | -60.12388 | 2024-10-22 04:21:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f74afe03-48e7-37f7-9501-d8562e85e44d | -15.9504 | -56.65025 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3efbfe4c-e757-3cdb-852f-8c9fa202c430 | -15.94966 | -56.6538 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39f977f9-8d42-3825-9bf4-0d044de5a750 | -15.94849 | -56.64924 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 934cd7b9-ebe3-38ee-a7aa-ec7fdcdb48dd | -15.94777 | -56.65282 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21133e57-0205-3f5c-9db7-8c62940c20aa | -15.83221 | -56.64135 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f64e8811-f36a-3a9e-9678-31ea4a4d6274 | -15.83148 | -56.64488 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61037b79-c7ff-338b-9cd5-9d3934e80438 | -15.83047 | -56.64138 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 725c4415-9a50-381d-82ce-e6e2c4e6b0bb | -15.82976 | -56.64492 | 2024-10-22 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ab66a1d-b476-3208-9904-cc6011cac299 | -28.58565 | -49.44284 | 2024-10-22 04:23:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46ca3b2c-0764-37c1-af0b-669fa07e7c5a | -28.34169 | -49.25908 | 2024-10-22 04:23:00 | NOAA-20 | ORLEANS | SANTA CATARINA | Brasil | 4211702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 06808cc2-6e5d-3fb7-b025-02a759d22164 | -30.88437 | -52.4958 | 2024-10-22 04:25:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 349656fd-f495-3b4b-951e-508d9f0f7473 | -30.13133 | -51.31877 | 2024-10-22 04:25:00 | NOAA-20 | GUAÍBA | RIO GRANDE DO SUL | Brasil | 4309308 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 529b97d2-bdfd-3bc5-ae1c-9434682c7252 | -29.81368 | -51.17832 | 2024-10-22 04:25:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| c977623f-e926-340b-b137-a129af165d6d | -1.165 | -53.6571 | 2024-10-22 04:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 69da64fb-54ff-3800-b241-5960c867852c | -2.7773 | -49.3067 | 2024-10-22 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 02f76c5d-f49e-36bb-9f63-a5f356d99faa | -2.7773 | -49.3279 | 2024-10-22 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| b1767895-7ece-37e1-b57a-62caaaf4a7de | -2.7589 | -49.3072 | 2024-10-22 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 2af3229b-3727-3ef8-b7e6-88d5917331df | -2.7588 | -49.3285 | 2024-10-22 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 144.8 |


[Clique aqui para ver as próximas entradas](README25.md)
