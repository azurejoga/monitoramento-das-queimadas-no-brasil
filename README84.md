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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5fb01db-26fb-3fdb-8763-9aae57da642b | -6.35729 | -58.28362 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84524167-b7d6-3b99-8ea8-36f0640e12f9 | -2.97567 | -54.76505 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18683ca8-cd3a-33fa-bc8f-dc6c1a513468 | -10.2889 | -50.21238 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87f6ec2a-af24-3893-b1d8-c683b77e0207 | -8.15927 | -54.82578 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79ecefd8-901f-3929-9e29-2b9e125da3db | -6.45863 | -59.97979 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0b087d1-53d8-397e-a914-a6bfb1f1a96d | -2.97051 | -54.77168 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58c7338a-2f3a-3b07-84b3-4d0d8754649b | -8.22874 | -62.84541 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b00b21b-506e-36fa-a18c-db6e2a419b6c | -6.89316 | -63.04287 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be82dc55-00b1-3116-b740-e37ccc1cab5f | 4.35575 | -60.73818 | 2026-09-20 05:23:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6fe9efa-5ac4-3481-b5f4-a24ba431d1d6 | -3.08267 | -61.1859 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c3296fa-d22e-3c40-bcfd-b2dc16abb67c | -3.3176 | -59.44494 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8604c5fe-7433-377c-8d97-e3df92218b01 | -8.07857 | -55.34053 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a040e1c-2c29-3d1c-ae97-e8f6374d5568 | -6.44867 | -59.97825 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d17ab0be-415c-3de1-9854-5beb4708d5b3 | -6.43925 | -59.97321 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3857f03-2f43-3205-ba9f-4d105bd969f3 | -2.91781 | -57.79863 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7773dcb7-c7f3-3b90-87fd-65dcfa9a9ea4 | -3.12682 | -61.25439 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20cadf73-47f6-3e27-9d9f-f09533e9fdcb | -3.44782 | -58.23089 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 76c514a4-9db3-3867-a7fa-ee4e859fc244 | -8.85183 | -62.35762 | 2026-09-20 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49a5c44c-2308-30cb-94b0-896dd0b51c2f | -10.27522 | -50.27335 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09727eb1-5462-3405-a8b9-85b9b96bd104 | -3.0364 | -51.37309 | 2026-09-20 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f57e1b19-e4bf-3bce-88c0-c6bd7818aaa0 | -8.22196 | -62.84433 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bdac70b-3deb-3ef7-a61c-e23201eb410f | -1.22899 | -55.73087 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b520bff-83f3-3d9c-a72f-6f7566198430 | -4.26306 | -48.63918 | 2026-09-20 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e7494d0-3ee9-3957-9a41-a8b8919ae09c | -3.39619 | -54.06451 | 2026-09-20 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d48efd7f-9e1b-31ef-9ddf-6d3214f8c200 | -2.85201 | -57.63377 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbef57aa-753e-32cd-9328-7b8ee46f0ee8 | -3.17303 | -58.57865 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b891ff2-2ffc-3170-ac4b-2fa3f762b2d6 | -8.30319 | -50.81869 | 2026-09-20 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8106aa7b-f94e-3e51-9b1e-f9d1752453a7 | -10.39008 | -51.87874 | 2026-09-20 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a672d0f4-5fbb-3b13-8c96-b3c3d3d4f27c | -3.12933 | -61.25459 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd67cee4-43b1-33ff-b967-03bd2b9c0ea6 | -6.29809 | -59.96226 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92207eba-6413-3d13-aacf-8a3bf7b68866 | -3.463 | -58.94629 | 2026-09-20 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be7bfeca-3006-374e-897b-d3e7e559c62c | -2.88274 | -57.82398 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc6f8972-033b-3422-b1dc-7ece0f276d1a | -7.57707 | -57.68381 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0efbd1a9-2f11-3ad3-baa1-66b29add1997 | -8.18262 | -54.75481 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4eea1f4f-1eec-3785-93e9-5c5e35563d55 | -2.88455 | -57.78968 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 57fa10a2-04f2-3b17-9b9b-d964c4082ce2 | -1.32017 | -49.27645 | 2026-09-20 05:23:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6532c3e5-7705-3425-b87b-7faaaf2cb918 | -3.44839 | -58.22723 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 776cbd81-1c3e-30f4-b32a-02dde9f57876 | -3.12627 | -61.25794 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 019b9e25-8e39-3fbb-b9d9-d435de5295cc | -9.5802 | -55.10769 | 2026-09-20 05:23:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff62c905-420b-388e-b249-95d70ed7d26b | -2.88962 | -57.82503 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fa4d19e-351a-3a34-ab0d-1a8e9fd0e201 | -3.33676 | -59.80057 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0a6c3e9-e983-3c3f-99b2-b2d86c42a251 | -3.33524 | -59.83199 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f86234d0-1bbc-3735-a7b9-927364cb7f1a | -8.29735 | -50.81847 | 2026-09-20 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 884b5c40-ebc6-3be9-b622-65842a0e72ff | -2.89708 | -57.82233 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c12cc9c6-def9-3fee-afb3-93f202c86582 | -9.93679 | -53.98576 | 2026-09-20 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35a1b264-e4d0-390b-9d7c-de8aee068fd0 | -1.2229 | -55.72073 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 796f3850-e26e-31cd-9473-97394be36901 | -6.44589 | -59.97425 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a88203bb-eceb-3ea4-8d99-79cbec0a1be1 | -8.42072 | -54.72342 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1892b1fc-a18a-32ff-a17c-37c8a261569c | -10.2758 | -50.26862 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d24ff54-7434-3fc2-9168-be921a1360d9 | -10.31549 | -50.24984 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65d8ebda-6a96-3571-90b9-cb7b85508673 | -10.31916 | -50.2212 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c391580b-796d-3582-abde-5a08f375ee06 | -3.4005 | -54.0651 | 2026-09-20 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87c9970b-6390-3172-986a-8cc03af38b67 | -3.13433 | -52.71439 | 2026-09-20 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d2d38b6-5256-3958-b389-cc8e4abd74a3 | -7.88249 | -62.54752 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91b5c025-e435-3663-ae31-371272737e77 | -2.81196 | -57.62461 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0798b158-c110-3893-bde6-55cf583924f3 | -2.82477 | -50.46366 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a69a92ff-07d3-3003-ac37-1f982b903fa5 | -3.19461 | -60.42933 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87dfdf87-1732-3ce1-8cc0-558fcd62445f | -6.29404 | -59.92233 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 32e84611-efb4-3416-81e0-2950d9eaa1ee | -9.17914 | -59.42037 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 452739d3-3670-349a-b58b-77eab9603364 | -2.98162 | -54.78085 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9bdd34f-26be-3e37-80a1-902f6706d06e | -1.18719 | -55.67868 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a54d2698-d37e-3e4f-b442-016177d0effc | -2.90518 | -57.78899 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b583fd3b-c2c7-3d5b-850b-54c4eb3a8998 | -3.17568 | -61.20012 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55197f5d-245b-320e-9334-a9c7c0d78a5f | -8.17564 | -54.74048 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8cb15936-bf94-33c6-a109-e7bbdfcd0cf2 | -3.31372 | -57.87309 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6ee6bce-c4f8-32bb-9383-503a330734f1 | -10.77872 | -50.8767 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f8796631-9b27-3907-a746-d1ea97677264 | -9.68709 | -54.33383 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe18c81b-daf3-35e3-ba47-06bc45efe6dd | -3.28053 | -57.7675 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92fd761a-ca24-3e31-93a7-a74459142f61 | -6.14941 | -62.62199 | 2026-09-20 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c06de37-4994-35e8-aecc-e7cfc9c7e979 | -2.45891 | -49.21874 | 2026-09-20 05:23:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 66455c8b-2f47-3166-8a09-516b583bd570 | -8.17875 | -62.80379 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c938ea32-d0f4-3ab7-b633-5f568bc11f9d | -8.17581 | -54.77144 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2884e5b6-9e4f-3093-9f5d-e6e72d7ae458 | -9.67538 | -54.32418 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2adbec18-84e8-36d3-8bf0-695aa0118262 | -3.02399 | -51.19656 | 2026-09-20 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b65e2ac8-06b1-3bea-a904-94a35fed5775 | -8.76547 | -48.66005 | 2026-09-20 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 34f9dd33-ef6a-324d-9cef-ad01fa437c8d | -3.08614 | -51.28617 | 2026-09-20 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86431f28-db2a-3779-b88d-7a92cb298636 | -3.25037 | -60.1809 | 2026-09-20 05:23:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da3dc396-8108-3cbd-bc3b-6fde07385865 | -3.59197 | -47.3545 | 2026-09-20 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c5f6b3e1-e9ab-37ef-aa95-5b5eb625940b | -8.22255 | -62.84066 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2caf0d9d-6bae-3eed-91d3-c4cc3f779589 | -3.19848 | -61.12057 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3f05b3d-3d8e-31e5-b2d4-cc6f10c8a293 | -7.04753 | -62.95848 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20aaccf3-4948-34f6-acca-a491eacc2ec8 | -3.34929 | -59.85518 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f015d77-179e-341a-ab56-f8690b3802fe | -2.82096 | -54.71346 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fe9326b-d662-34f0-b14d-a2b1b17fa59a | -11.09159 | -48.30336 | 2026-09-20 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f333a086-4bee-3832-bd1d-d16a78a6e5ff | -3.44147 | -58.02165 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a998ea66-796a-325f-b061-873b30c4b6ee | -10.78569 | -50.86873 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 461cc006-8dc4-35ac-acee-d38b69cafe12 | -6.35031 | -58.30629 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78dcd478-f780-3554-9b0a-3b681426e2d5 | -9.2641 | -48.21105 | 2026-09-20 05:23:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3aeb1c11-da46-3a48-a80d-a1ee3b46d434 | -2.97701 | -54.78379 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da1530cd-559e-37f7-92f6-10d0a3d71cb4 | -8.23921 | -61.36892 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d5319d5-5148-3163-adc0-ace5191a2498 | -3.36143 | -59.86408 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 131c1448-6a5a-33d2-97a6-d9374cc9c788 | -8.23812 | -61.37585 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaf4b56c-9d42-3927-aab6-42c56219a77f | -9.58081 | -55.10337 | 2026-09-20 05:23:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 919a570a-aa1b-369b-ad9d-22b01d9dfd3d | -3.89505 | -49.06828 | 2026-09-20 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6d51e7a8-444c-3c0f-8116-e0aff8a35148 | -2.54615 | -54.65702 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4663cadb-4959-349a-b0e0-53ea5667cbe4 | -3.44957 | -58.39922 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9592610-6640-3df2-afa9-6ffe4ade9c03 | -3.36307 | -50.4453 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79a2aa32-1cf8-37f6-9085-789ed76f764b | -3.45066 | -58.21254 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87e21008-57da-3a4f-aca0-d3c18bbcf0d0 | -8.6136 | -54.59241 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 663e274d-1fe1-3dbd-a14c-06f67c9b1532 | -8.76356 | -48.6755 | 2026-09-20 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 12.1 |


[Clique aqui para ver as próximas entradas](README85.md)
