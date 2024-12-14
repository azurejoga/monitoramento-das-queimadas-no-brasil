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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95268d6f-8679-3151-866d-b78582bcb164 | -1.69909 | -52.6127 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaef9f9f-8376-3f5e-801b-61ebb30020a9 | -2.37498 | -51.91573 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1afbc84-14cd-30cc-8abc-f9be9a3aca55 | -2.80722 | -52.81059 | 2024-12-14 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20b2afe0-08b4-3db0-86b9-258dcb044aaa | -2.37058 | -51.915 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e65392c5-e5b1-3d47-88a3-fc6e20ec3855 | -1.87822 | -53.21825 | 2024-12-14 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55ddcca6-9aa5-323f-88a2-5ebc5eb1caaf | -1.69966 | -52.60892 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63558a1b-9e5e-328e-af68-7cb12a7bee0c | 2.74358 | -60.3823 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 295bd749-bece-3d3d-a489-ed74efeedcd6 | 2.62544 | -60.41665 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6f78787-d9b2-3d43-9a61-4516cee2c010 | -1.92805 | -52.7279 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5d959b9-4dd1-3044-b147-2b62f3cf92e7 | -1.72433 | -52.55835 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c702b54b-1d2f-3688-b562-2b617dad6900 | 2.52958 | -60.64681 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91c582b1-b4c1-3d32-ac81-53c5ba47a157 | -2.6787 | -53.08058 | 2024-12-14 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fe482e0-1c00-3abb-b80c-6a957be2aa68 | -1.719 | -52.56532 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c564ff0d-444f-34f2-af66-927dae411927 | 2.39666 | -60.41416 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c0b3c02-c506-3260-a389-6e26e3d1dccd | 2.74293 | -60.3781 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0f59237-a9e4-307b-8c9b-d34c7f52302f | 2.73867 | -60.37447 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76b42f4f-79f4-364e-a3f1-57d7ed068799 | 2.58159 | -60.69196 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3ff5862-89ee-3dd3-a7bb-2f2bbdfc5bec | 1.30158 | -60.40713 | 2024-12-14 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f68a160-ffe8-3747-8f2b-1ae0a17338a2 | 2.74656 | -60.37756 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d588723a-0309-3bba-b726-73887edaf770 | 2.74423 | -60.3865 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19f952a6-a353-3234-ad66-c82ce157cf38 | 2.62182 | -60.41717 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc6e55d3-2b62-359d-ad2a-a3824d607b3a | 1.52661 | -60.67437 | 2024-12-14 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b292ece7-ac38-3363-9acc-606afd79702f | -2.58556 | -51.92242 | 2024-12-14 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8f524ef-dc5e-33d0-82d8-49ce1708d929 | -1.65935 | -52.7455 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ffa6e75-b7f0-3fbe-95b2-d9a5d8b05f49 | -1.71958 | -52.56151 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ac8e2753-9787-32a2-87bf-a56f1652e4fc | 2.74591 | -60.37337 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13a5169b-f965-390b-a16d-8f6cd1b7ca41 | -4.41967 | -45.80969 | 2024-12-14 05:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c6f2552-f883-3a88-91ea-73391933462a | -4.41126 | -45.83594 | 2024-12-14 05:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8479b8f7-087c-3a51-8953-f09c3b467648 | -3.96727 | -53.84219 | 2024-12-14 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ba76305-c090-3ec5-892a-6df85d76d90f | -4.08965 | -53.95896 | 2024-12-14 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e81ab4bd-4408-300c-ab25-e555fc78064e | -4.0895 | -53.96283 | 2024-12-14 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e543ab8-ada9-3399-a9b7-776892bd7050 | -4.41019 | -45.82749 | 2024-12-14 05:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 70cd7cc8-aa4e-3f73-b21a-20bbe15495af | -4.41217 | -45.82925 | 2024-12-14 05:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fd08a18f-9da3-3d9c-8963-8e1192adc70f | -4.40635 | -45.82124 | 2024-12-14 05:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0746ceb5-c0d3-31a5-8e31-bf887b1669cf | -6.96697 | -55.29131 | 2024-12-14 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c896fa49-dd28-3cb3-8cf6-53414ccdf4eb | -4.08891 | -53.96405 | 2024-12-14 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d784ef6-c1d2-39cd-ae0b-8ae46797082e | -4.41475 | -45.8104 | 2024-12-14 05:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65087a26-3883-3f37-92b4-593947463205 | -4.41319 | -45.82177 | 2024-12-14 05:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 939a0925-1fa3-3370-a47a-8cb998a91a1e | -3.43581 | -53.14451 | 2024-12-14 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9eb08f47-aeee-3ea7-99c8-b341de5f5a21 | -4.41204 | -45.81457 | 2024-12-14 05:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0aa17f62-d72a-3e57-8038-67fe15850592 | -2.96901 | -53.11641 | 2024-12-14 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd859e58-0796-3246-875a-76cb34fa420b | -4.08872 | -53.96792 | 2024-12-14 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53e03900-03bc-3b83-bb22-a513d301f26b | -4.41399 | -45.81595 | 2024-12-14 05:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a99d0127-ed40-3813-886f-1b2e4c438e55 | -4.40537 | -45.82844 | 2024-12-14 05:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d0fc8e9d-4874-3367-bc86-d2ec655e0a59 | -4.41701 | -45.82817 | 2024-12-14 05:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 962d80a1-3594-3588-b5c6-bfd2095ba523 | -4.41901 | -45.82983 | 2024-12-14 05:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 64da2c93-4d50-3fe8-b833-67321325e567 | -4.41802 | -45.82114 | 2024-12-14 05:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f17e6980-5bd4-3138-ae48-e33ae8b44793 | -6.48271 | -54.92539 | 2024-12-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3de2fad-9fed-311a-a7b0-2e05f66c0b1d | -3.21544 | -53.716 | 2024-12-14 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee5e00fb-f78b-30d5-b71b-f79ba3acdea3 | -4.40921 | -45.83429 | 2024-12-14 05:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e6b65e17-82dd-30b9-8bce-39a1110becd4 | -4.41602 | -45.83504 | 2024-12-14 05:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| a33319e4-cd17-3932-81f8-aed57d2f9853 | -4.42159 | -45.811 | 2024-12-14 05:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db1d9114-9d19-3c5b-b0fa-4066337049af | -7.83319 | -54.76782 | 2024-12-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 212fe3be-67bf-3350-a710-f95710e73202 | -4.41283 | -45.80906 | 2024-12-14 05:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76f45dfe-856c-336b-b785-3c4b8e9daef4 | -4.41123 | -45.82021 | 2024-12-14 05:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e6175ec8-257d-338f-8f4d-f9f36d9ab79f | -4.41807 | -45.83664 | 2024-12-14 05:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3b3c71e6-ee5f-3e40-8bc4-3b19d65568f5 | -4.41886 | -45.81529 | 2024-12-14 05:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98e3effe-70a8-3f91-baf2-16942da64ce6 | -12.56941 | -57.76055 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08a08041-e7f1-38d8-8581-0105fa72038e | -12.55166 | -57.70763 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f012dddd-cd54-3175-b35c-5b5af0bfe18e | -11.82673 | -57.8203 | 2024-12-14 05:20:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41447e53-88c5-3c50-989a-dc6c2b91d39b | -13.17919 | -53.28823 | 2024-12-14 05:20:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 90d397be-723f-3155-9dc8-1a28d5a7e28e | -12.55048 | -57.71582 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d25007c5-4297-3c3e-a68c-05aab1bf14ab | -9.72235 | -61.91504 | 2024-12-14 05:20:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a20e32b-a286-3e88-b99f-6e9e67b9f53a | -11.82614 | -57.82428 | 2024-12-14 05:20:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8490bfa-0d79-33d8-9ce8-54e1655c3673 | -9.30264 | -59.41686 | 2024-12-14 05:20:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 134464da-6243-33a2-85fb-881a3ea0487d | -12.56232 | -57.75948 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6b35e403-8c72-33ed-a7c8-23d770d3a501 | -12.56528 | -57.76411 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6eeb842a-bde7-329e-9206-1db76d69c220 | -12.45498 | -61.22193 | 2024-12-14 05:20:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b8835e6-6f6c-36dc-91d3-31f30be42421 | -12.55817 | -57.71284 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7df7503e-ce1d-3014-bff7-54c3beb86c4e | -13.17513 | -53.28242 | 2024-12-14 05:20:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 51fe5241-7cd4-3fb9-a2fa-e6dde8e81f86 | -11.11966 | -54.65393 | 2024-12-14 05:20:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 711ea268-e4d2-3a39-a7e5-556aeab20bbd | -13.42085 | -61.18124 | 2024-12-14 05:20:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a5f7587-4d58-397b-ae66-c34ce4719fad | -12.55462 | -57.71229 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0ed9564f-0d05-3dfa-adab-a08640d91253 | -12.55403 | -57.71638 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 3ca1a8d5-b356-3a40-8b99-29e728c7b77a | -12.16713 | -57.86493 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4171454-f031-3311-ac8b-df37af4feb7f | -13.06289 | -52.03408 | 2024-12-14 05:20:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69185851-3928-3e2d-a2e0-73f0b93fdced | -13.54454 | -55.38455 | 2024-12-14 05:20:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d4cb091-45b6-36c3-9a95-1f88af941b32 | -11.78608 | -55.13253 | 2024-12-14 05:20:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1336735e-6add-3d9e-a51e-7476f7b9901a | -11.83082 | -57.81687 | 2024-12-14 05:20:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f2054f1e-5dec-3555-82fe-b611889097d5 | -12.91277 | -55.04695 | 2024-12-14 05:20:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 681fb84b-e9e5-3d27-9099-e75cceda9baa | -12.55521 | -57.70818 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f1bbe50-feef-371d-88e5-8fed1d3e85fe | -12.52817 | -57.82084 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f5d9b55-0666-3e71-a314-145baabf6853 | -13.06505 | -52.03623 | 2024-12-14 05:20:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32f259ea-c69c-361c-8168-bd22d110591d | -13.48569 | -60.35053 | 2024-12-14 05:20:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86cc90b0-7777-37e1-92cb-5005c735b8ce | -11.82556 | -57.82825 | 2024-12-14 05:20:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5d9b916-6311-3578-8f3a-a3290bbfd4f7 | -13.17448 | -53.28759 | 2024-12-14 05:20:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b614bae2-0631-3ac9-9d91-ce1b927f0e92 | -11.82965 | -57.82482 | 2024-12-14 05:20:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 1a47749c-c39b-35fa-adff-6d3236d44166 | -12.55876 | -57.70873 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 322c4424-aba5-3ad2-b539-6db57fb6646f | -12.53865 | -57.72241 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 000bbe0a-240e-383c-a51a-c3a35d0016a0 | -9.50599 | -62.94457 | 2024-12-14 05:20:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7157365-3c6b-3fec-8fdd-a82fb0ec5fce | -9.93023 | -59.90932 | 2024-12-14 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6540a80d-2fcd-3211-8fc2-fec1ffb46e7c | -13.17042 | -53.28175 | 2024-12-14 05:20:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a81aa502-cd4b-35fe-9637-43579b2adbd6 | -13.54043 | -55.38395 | 2024-12-14 05:20:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de62040d-7099-3cde-8cb6-b06bf7f02920 | -11.83023 | -57.82085 | 2024-12-14 05:20:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e1199131-e7f1-3200-9aed-18cff5d8a79e | -12.99314 | -54.14985 | 2024-12-14 05:20:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cd689b4-82f3-3aa8-b149-a298350a79af | -12.54693 | -57.71527 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 13d3454f-83b1-3296-ab50-f169f3f1f73c | -12.5351 | -57.72189 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f886d29-6e56-36c9-9b64-288785de6d4c | -12.90861 | -55.04629 | 2024-12-14 05:20:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 862ddb1d-bbc5-39f4-8979-69464c06bdf0 | -9.73079 | -61.92795 | 2024-12-14 05:20:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a18828f4-d4f0-3c23-8ac4-770a49618ff5 | -12.55107 | -57.71174 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |


[Clique aqui para ver as próximas entradas](README12.md)
