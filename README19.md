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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df538855-fdf7-37b6-b13e-6c00bc6e367e | -2.85706 | -50.73457 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77a3868c-a1c0-31a5-8764-f2dba2432e27 | 1.73829 | -55.7021 | 2025-10-21 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f151d53-1d0f-3b88-b039-da6bf4aaf916 | -2.86626 | -50.73186 | 2025-10-21 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb38ae13-a4f9-36d3-bc87-e01b92526d75 | -3.32065 | -53.35011 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d283a86-b344-3a6e-a3b9-bb0a4c7b90e5 | -3.3333 | -53.24215 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40cd6a59-836e-39fc-8c97-dba35d0b82ac | -3.65941 | -52.11856 | 2025-10-21 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 396819e8-b821-3d4a-86d7-30f187d21c23 | -2.40937 | -57.65949 | 2025-10-21 05:14:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 960744f5-01ff-3201-85f9-936ce4847620 | -3.69439 | -52.59302 | 2025-10-21 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ff2d43a-3d5d-3289-a8e2-410b28e47272 | -3.58717 | -55.44564 | 2025-10-21 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7b65256-b347-3b05-88c6-ae6b743120aa | -3.21769 | -50.21817 | 2025-10-21 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b09150e6-82dd-3ff4-8f23-f8dee074d1ef | -8.84851 | -49.7054 | 2025-10-21 05:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f5724b3-b272-313a-b27f-2fd82467c89d | -3.66478 | -51.94897 | 2025-10-21 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fba7439-03dc-335a-9e1d-7182fc3f379a | -8.64235 | -63.04917 | 2025-10-21 05:14:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d276b8a-6624-3e41-80d2-1c03a34d82b3 | -4.35761 | -49.68782 | 2025-10-21 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fdb13c1c-cfb9-3c76-89ea-f00c5a62ded9 | -5.52731 | -50.05645 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43dd666c-fe19-3b6a-83ab-96a71517887d | -5.66669 | -49.79639 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a9bcd14-17bf-3a11-afe4-1c29922fe0a8 | -3.41279 | -52.60156 | 2025-10-21 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a387455-deca-3748-8f6a-a80db53e8b06 | -3.406 | -52.7197 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd9d1e56-e9a1-373a-afa6-58cdc0d14b77 | -3.61673 | -50.14737 | 2025-10-21 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4776b15-e8e5-36c1-9341-0b890a6f3612 | -3.40432 | -52.72142 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2833d4e0-cabd-36fc-be19-3ecbb4263187 | -2.8118 | -54.38302 | 2025-10-21 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 404ab313-fc83-33ff-b7ed-b8ee5ba76df7 | -3.32368 | -53.35487 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e94738ec-4829-3e91-8b52-35d8761cda39 | -3.11959 | -52.72253 | 2025-10-21 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb2eeeb0-aa35-3f2b-adf3-88467d5ea09d | -8.48933 | -49.53897 | 2025-10-21 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd34af4f-baf5-391d-b4bb-6fb243063b9c | -4.56703 | -49.65534 | 2025-10-21 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fb25425-1e67-3632-8155-37231851936c | -2.8124 | -54.37923 | 2025-10-21 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ad270f5-1690-3962-89df-677819b18450 | -8.29641 | -49.3068 | 2025-10-21 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0aeed5a-2fed-3e2e-a5a8-5421fa0d5a14 | -3.1138 | -51.20617 | 2025-10-21 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1d7d9af-cd54-3b79-89d2-2300ba9b4b18 | -3.81482 | -48.64817 | 2025-10-21 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3417c4c-7a45-3f90-9068-5c67b93fa4e2 | -6.57908 | -47.54086 | 2025-10-21 05:14:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aefde870-053f-3340-be1f-891e08f79aea | -3.50047 | -53.44545 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a89d526b-72eb-34eb-b477-d8d41a78e7d2 | -5.67174 | -49.79573 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76a48dfb-5384-33b4-951b-e949b6f56afc | -5.77796 | -53.45762 | 2025-10-21 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e9c5528-a20a-3eca-b785-ba80ee57665f | -5.532 | -50.05717 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dab4f2bd-f00f-30b5-b6c4-e6f89e0436b7 | -2.05884 | -56.83459 | 2025-10-21 05:14:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcb709ab-d5c3-3788-953b-961c6a8adf83 | -5.67147 | -49.79712 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6963d5df-4837-3921-a29f-3172dee72258 | -3.15863 | -51.35836 | 2025-10-21 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5734342d-c15b-36e5-adf2-7cdd9a0d6d7c | -4.57177 | -49.65613 | 2025-10-21 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c81d77c-d7d7-3b52-a0dc-c0aeae7a90b4 | -5.66742 | -49.79121 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76908003-7123-317c-acb0-fecb6904940d | -4.34562 | -56.06366 | 2025-10-21 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c98abc78-fb9e-39be-9927-f1179643cc4d | -8.71545 | -49.59793 | 2025-10-21 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6075433d-b385-30ab-9501-b29ee5fcceba | -4.66623 | -49.67852 | 2025-10-21 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 360e0864-3c2f-396d-a4b0-fc3f6875600e | -2.20369 | -56.90384 | 2025-10-21 05:14:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0be1e15e-df38-3b1a-92d2-1deaa3324400 | -5.53095 | -50.05417 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70e7a7ef-9f7b-36f4-ab10-1febf54abc9e | -2.41005 | -57.90076 | 2025-10-21 05:14:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f1ac270-14dd-388d-a444-21881b249ef4 | -8.14441 | -49.46923 | 2025-10-21 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2ff77fd-d717-3fbf-83a1-2dc2ab7a2dfa | -3.14467 | -50.24775 | 2025-10-21 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be645ea2-ff1b-30d1-aa3c-4ee0a9ea6414 | -8.14481 | -49.46639 | 2025-10-21 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86ee107f-9270-3fe0-b98a-d12b21b60965 | -3.337 | -53.24267 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4dafc70-fcdd-30c2-bb3b-170d5f8f5889 | -5.44652 | -50.04197 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e42b9c50-1c6d-34b0-8d25-af9be61ad9f3 | -5.22212 | -49.60614 | 2025-10-21 05:14:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a3a6523-e08d-366a-81ee-e8a8dfa1c984 | -5.45119 | -50.04272 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b4afcdb-9ecc-3a00-afb9-9113777e4140 | -9.48524 | -57.92427 | 2025-10-21 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fa168b18-d617-33ed-8617-2bac38aa2f30 | -8.88705 | -50.16792 | 2025-10-21 05:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52267282-6c36-3174-84c0-b8a9b914d8e1 | -2.50205 | -58.04778 | 2025-10-21 05:14:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d08a5710-5477-370a-8d32-65ed8d171f48 | -9.45349 | -49.85005 | 2025-10-21 05:14:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f8e2e00-d299-3570-ae94-7446f64d4a26 | -3.52084 | -52.8965 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 191d855e-2c47-3db0-abc9-fcba8a7034af | -8.49058 | -49.54171 | 2025-10-21 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d361d70-aa13-3519-afe1-d35821bc473e | -9.55398 | -57.35492 | 2025-10-21 05:14:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acd638d2-9e2a-31c2-abfa-6e097b3abc5f | -3.15285 | -54.98708 | 2025-10-21 05:14:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41585445-0317-317f-b70d-a3d2f0d07c5d | -2.3454 | -57.11779 | 2025-10-21 05:14:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa0ed60b-84fb-3086-9ce7-3606a3ab5324 | -8.84771 | -49.71124 | 2025-10-21 05:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75fec74a-e3d1-3975-9c1e-0b3ff2de4e7b | -2.80732 | -58.32236 | 2025-10-21 05:14:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8ef0e07-c557-3caf-9fbb-0c493367bf11 | -3.11437 | -51.20238 | 2025-10-21 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56cb1636-58bf-3727-968b-f7d69f233156 | -2.49865 | -58.04723 | 2025-10-21 05:14:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c00a43bc-9674-3a9c-a6ed-83ec8f731007 | -3.62671 | -55.2822 | 2025-10-21 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a477ce3-21ba-3bce-b64b-1228d85a4c6f | -3.23466 | -54.77641 | 2025-10-21 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb2ffbb3-660e-3bdc-bb97-1b6267b45f23 | -2.81587 | -54.37977 | 2025-10-21 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eab72ac-9d23-371e-9768-5d62c559136d | -4.48352 | -50.09161 | 2025-10-21 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89edad81-a22e-3b78-94e8-32f1ed774cde | -8.29601 | -49.30986 | 2025-10-21 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55daf9ab-1dee-354e-8cc4-917f7bc8e0e9 | -3.54321 | -55.41676 | 2025-10-21 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| defbdfdc-7341-319f-a19a-e581536aae37 | -5.29035 | -50.56845 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f038732b-2518-3408-b2ec-652349a56ac2 | -4.48282 | -50.09633 | 2025-10-21 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c35d724-aa84-3681-8789-eac0d246e198 | -3.10964 | -51.20549 | 2025-10-21 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f13a928-5333-3ace-b013-7dd1936b28ed | -2.70551 | -59.68706 | 2025-10-21 05:14:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 665d06c8-87e5-3b13-8e76-ad7aeee318bd | -5.66696 | -49.79502 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe3d5c0d-1969-3a5a-b56c-f3622028964c | -3.58323 | -55.44869 | 2025-10-21 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f5514a4-e594-3592-b3c9-4924e9c46404 | -9.45853 | -49.85075 | 2025-10-21 05:14:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50a49381-ccf9-3f28-85bd-b6f382e8446f | -8.29398 | -49.3094 | 2025-10-21 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 876d046c-034e-368d-90a2-02a9e9addfae | -5.26577 | -50.23324 | 2025-10-21 05:14:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eec04006-c24a-3ba8-958e-f138596dee12 | -3.66157 | -55.46064 | 2025-10-21 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5753c25-d53f-318b-84dc-4ed6406961e0 | -2.20588 | -56.88999 | 2025-10-21 05:14:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc940588-e359-3b7c-aef6-96ca958db9b4 | -3.11495 | -51.28343 | 2025-10-21 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd673679-302b-3a66-9dd0-03f74b193b4b | -9.55343 | -57.35846 | 2025-10-21 05:14:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a047e4a-36e5-37ec-bac5-80e5b805fcf3 | -2.65098 | -54.89221 | 2025-10-21 05:14:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a60b48f8-eb92-31e8-b7ab-8e23c3b124f1 | -5.44722 | -50.03707 | 2025-10-21 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9468ee90-69bc-3e5c-a7e6-7c19b982269d | -3.19565 | -53.07753 | 2025-10-21 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99312add-164a-3a52-bb80-a19a221490b1 | -4.55202 | -49.65838 | 2025-10-21 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 739290d5-333a-346f-98d6-40a23dbd38d3 | -3.81311 | -48.64995 | 2025-10-21 05:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c4fe2d6-b122-3f7c-bcda-157433976210 | -6.58477 | -47.54144 | 2025-10-21 05:14:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a23c460-0c0f-3641-b6c5-1e17f1f9ceff | -5.27038 | -50.23394 | 2025-10-21 05:14:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e3c3f73-de1e-3e5d-97d9-758d7148bdd0 | -3.58379 | -55.44511 | 2025-10-21 05:14:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10d5eb88-fdcb-3b18-88e3-4d1a3769ff81 | -3.2381 | -54.77695 | 2025-10-21 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9b313af-643b-358b-b8a2-9f7f432497fd | -3.66426 | -51.95247 | 2025-10-21 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2e23623-2653-3e8e-97b4-09d0ca1c6afa | -9.29078 | -57.54516 | 2025-10-21 05:14:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2cf78bc7-f7bf-36a1-b454-6fc8c3afb065 | -3.06549 | -51.52755 | 2025-10-21 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 928e93e8-894b-3a8b-857d-4bba378dc647 | -3.32919 | -50.22419 | 2025-10-21 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 735fbbce-828a-3043-ba6f-3f478dc64791 | -3.45721 | -51.64824 | 2025-10-21 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89184438-2a5b-34ee-bafe-2d0d65fbf442 | -8.6458 | -63.05345 | 2025-10-21 05:14:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad7744cf-cbd6-38e4-b8c2-d5a7594305e0 | -3.1102 | -51.2017 | 2025-10-21 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README20.md)
