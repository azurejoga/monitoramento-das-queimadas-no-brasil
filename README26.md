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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8761b1d7-4a06-32cc-983a-7758a7391019 | -11.89952 | -46.42955 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9987b956-cd1b-3284-8f71-bc20a2bd307b | -13.98643 | -44.53854 | 2025-08-31 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d70a2874-d709-38c6-a99a-fbbf45981f49 | -14.63393 | -48.06065 | 2025-08-31 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b491a1a3-a702-3d91-94c9-7da75fb97299 | -11.79865 | -46.45356 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32241786-ade0-3ed6-a8b5-f5d02dc9eab6 | -11.86 | -46.45789 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12a8e809-c8d2-3f03-a485-920e50a9c038 | -11.88717 | -46.34771 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 16f9c9ce-89a7-3b22-8128-cf5579679b4f | -14.63448 | -48.06195 | 2025-08-31 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4e78638-8480-3de9-bd9d-63a0ccd591c8 | -11.82577 | -46.44058 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31fdb9f4-4fb0-3313-af70-8e925d934171 | -11.8287 | -46.5189 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0bceeea0-f9df-341b-9ca2-aab9cd270168 | -13.37267 | -46.95908 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 155b83a2-6140-3e4d-b14b-9fa111ea2eda | -14.23036 | -48.07535 | 2025-08-31 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41670921-5013-3ff3-820f-f9a39277e92e | -15.94954 | -41.40547 | 2025-08-31 04:04:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 655f5970-bd2c-33d4-ad83-3efa976650cb | -13.68745 | -46.88749 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb701997-0ef0-3197-9362-c047457c24c1 | -15.9501 | -41.40186 | 2025-08-31 04:04:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 53217dc7-4140-39b8-8111-c7f11948b090 | -13.49031 | -46.95681 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 60c96f7d-4fde-3de2-a064-21a2e49841cc | -14.0406 | -44.56055 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82b42118-4394-3128-aaae-bc87a4d3709f | -15.94733 | -41.39766 | 2025-08-31 04:04:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 68e58435-0d54-37f1-83bb-b9d615f00769 | -14.54299 | -51.98205 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ee094dc-0b5d-3ea9-9966-c52d0ae3565f | -14.34152 | -51.87668 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2452383-3e05-3a42-8b44-018a797fb71e | -16.65092 | -43.18698 | 2025-08-31 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13f21131-c198-3737-84cf-d0b4ca1444b0 | -11.79887 | -46.47584 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf3e5fa3-7e60-39b6-9977-f793dd06c1f5 | -13.40238 | -46.83802 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c87ea0b-dd33-34ee-9271-a8be8c1f97db | -11.81439 | -46.4347 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 63019ef9-c87f-30a4-a3bc-d79a447175c8 | -10.95452 | -50.84412 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a92aeea7-daa5-3d70-9499-cc54db8ab7e9 | -11.80267 | -46.45424 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea16e70a-1be6-30f5-a667-3f31d3cc96d9 | -16.22768 | -52.68566 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d77efa2-005f-3b27-9f6f-63d21f37d3ef | -14.83643 | -46.73948 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f17b38a1-a48c-33fd-ae6e-0bf4759d65cf | -13.3279 | -46.86041 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80fcc462-06d9-3e25-ad70-f3bc09df8822 | -11.8264 | -46.43696 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa3aa439-14f2-39ad-883c-f7404578ee2f | -11.90862 | -46.40148 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e45c77ef-2a1f-365c-a5a5-077bfd51eb73 | -10.96319 | -50.85305 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 97ca1ce0-bb6e-37f6-96fc-0474050c60d5 | -16.22108 | -52.69735 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| d1d4213f-ce7a-3d4e-81d8-1859e4d87b50 | -16.49656 | -43.65528 | 2025-08-31 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6fd4c78-fef3-344d-8b17-d9ed9f4cec37 | -11.91214 | -46.68951 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 38896310-198d-36c3-bf63-6f212e1c239e | -13.50446 | -46.97107 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4ae77f1-52e9-3dda-a351-13046e1c9178 | -14.03222 | -44.56745 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cba26578-4560-3853-ad0c-d72bc8625f51 | -13.35895 | -46.94235 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8dfdefcb-8826-34bb-a80e-7821ddbd6c4c | -13.50036 | -46.97071 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da2171f1-55f6-362e-abd4-f3b62e91e212 | -11.82148 | -46.53653 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9f90992-d3e4-32ca-8cc6-76c81ff3f9f2 | -14.28183 | -51.88795 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6fd87c2e-d279-3748-9fcc-5cc0505c015d | -15.71704 | -42.59689 | 2025-08-31 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eab4bd04-2534-32e4-b0f7-e174aa5fdb23 | -12.3125 | -45.72297 | 2025-08-31 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e00cb1e7-41f9-36f8-bb16-db342030dcd8 | -10.96333 | -50.85694 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6685a0d2-2fb4-36d4-a042-a0dfdb62817a | -11.87654 | -46.7247 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82153fc8-1354-3b3c-9b08-82d7b32e5bce | -13.35507 | -46.96409 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c91d4cf-9b21-38ff-afb9-17a2905c596e | -11.91894 | -46.69868 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc2e7af8-5851-3d23-908a-60233f96a0b0 | -12.39719 | -46.47583 | 2025-08-31 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91772568-ac36-3350-9479-e37fe0fa5d3e | -13.67109 | -46.93243 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49e67be3-20a7-321d-8de0-61ee27e0f775 | -13.51427 | -46.98646 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d69034ff-b334-3c87-bdd5-5b6cf83ae468 | -11.81839 | -46.43543 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 176b3ddb-898b-3821-ac11-64692b8edbac | -13.3043 | -46.9177 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 606f5228-6dfd-3b39-94ba-7b4e3ae83ff3 | -13.54107 | -46.9569 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e87c0650-5965-3f66-baf1-b3381e2f9991 | -12.41554 | -46.46463 | 2025-08-31 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbdf1f7a-9fc7-3b32-b46c-4dfcec25aae0 | -14.83555 | -46.74449 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1117e52e-dc54-3c35-adf0-aac4a35bcc17 | -14.34027 | -51.88075 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18e677f5-000f-3e58-bd2c-fb197f418b56 | -15.77662 | -45.3801 | 2025-08-31 04:04:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ed90a72-f54b-31a7-bfc3-b5245fffc718 | -11.559 | -47.61925 | 2025-08-31 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 26afa570-1611-3f2a-81ae-d1282ab849b4 | -17.86146 | -44.30853 | 2025-08-31 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edf8c8b2-2ae1-343d-9921-df74e4d9a8ae | -11.82551 | -46.53727 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da2030c1-67df-3a81-8f9b-1ccecbb9dcfd | -13.30366 | -46.92135 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab49798a-99b5-39b1-a715-302b41263f07 | -16.99847 | -49.32783 | 2025-08-31 04:04:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 622cae33-fd08-3d8d-8fb3-71c52583d8d7 | -13.46807 | -46.9414 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d01eecd-19f1-3c0e-95f9-a98e159d20e4 | -11.83041 | -46.43768 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe32a883-d595-3baf-a77a-88d6c231c205 | -10.96808 | -50.86156 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b89d7de8-900d-3fdb-a2c5-50d34b4aa3e8 | -15.22045 | -56.0646 | 2025-08-31 04:04:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 05066cdf-22ab-33ca-9eb4-3b6e49ae5357 | -13.34277 | -46.93952 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f595e223-41ef-3460-bb83-ec41203eefb6 | -14.22184 | -42.79852 | 2025-08-31 04:04:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9e740e98-f865-3616-839c-a192bc85ebec | -13.51506 | -46.98195 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6d01020-5479-3b89-b097-4490627531a4 | -12.63205 | -48.20421 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 274a16f5-7c20-3c9a-ba5d-59c501cb6020 | -17.15204 | -46.07876 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4a0e629-2396-3843-9d8a-f6b5ae797a59 | -16.22357 | -52.68522 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2c5eb9fa-60d3-3d38-8fb8-2527f6f90cc9 | -14.22606 | -48.07467 | 2025-08-31 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d81e900-c869-3dba-b9fe-6e89dd14d850 | -12.09752 | -44.72686 | 2025-08-31 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| b67c2178-8462-3e68-8b5f-89ac7e67fcb8 | -14.83167 | -46.74361 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ad1dfc4-01e0-3dc4-9376-4b1ed17c8c14 | -12.10114 | -44.7275 | 2025-08-31 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 8d122ca5-962a-3a47-9e6e-8fc5fffb4e66 | -14.54332 | -51.98044 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba217986-8d50-3b7a-9ad5-5f89c19801f7 | -14.03992 | -44.5646 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1b0cc1dc-e763-33e8-8049-b8a705553797 | -15.68082 | -43.2303 | 2025-08-31 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 21206513-e166-3168-bb6b-6c35e5f6981e | -13.68914 | -46.87799 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a406466-7618-394a-9c8d-4d1a724e4cc8 | -17.47733 | -47.00276 | 2025-08-31 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe0d45c0-df82-3469-8c1e-6e046ea41f26 | -12.81653 | -48.08532 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c265ccfb-7405-3ea8-81aa-8e12ca9feb41 | -15.21503 | -56.05659 | 2025-08-31 04:04:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7bec1318-37f9-3b0b-933e-8ee5aef2502a | -14.03776 | -44.55588 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9471b53-cc7e-3b9c-8699-dd2c443b0ba2 | -13.6868 | -46.89109 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 122c1e91-4eaf-3679-8892-3d8ed22083c2 | -13.34902 | -46.97456 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dd74db6-8695-34cf-9495-08b75f16cc2e | -11.82615 | -46.5336 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a5b6e8c-9478-3483-92bb-0933775bd23f | -13.33082 | -46.86093 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8d72483e-6d30-3c7c-a117-ede5a7b6569d | -13.33741 | -46.94609 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32493c63-7151-3af7-b41c-5f0963a7d170 | -12.0968 | -44.73111 | 2025-08-31 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ea05e53-fc03-309e-aa8b-1514847a461b | -10.96739 | -50.86516 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55f6a8bd-ce89-36ce-8053-e30ec4255b32 | -13.35767 | -46.94952 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02984803-29e3-3468-8069-f4c20b96a38c | -11.91553 | -46.69413 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42ba98a3-35ab-36fe-83fa-9264cd819f0e | -16.32945 | -51.59908 | 2025-08-31 04:04:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ae08774-a4e2-36b2-bbd8-2af4b5c8ff0e | -11.77934 | -47.39627 | 2025-08-31 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ad534576-6b39-30b7-b80d-55e203958a6d | -11.90414 | -46.42678 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 11f3f14e-ae33-3609-9b34-91b645348048 | -13.57619 | -46.92345 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 216e2c8a-5e82-3a90-a69f-f9aa6f8937da | -11.88321 | -46.71069 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 849ffbcb-4103-38d1-946b-4cae4467416c | -13.35165 | -46.95988 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c85030d-7749-3326-aa18-68fcee9c90aa | -11.84366 | -51.49004 | 2025-08-31 04:04:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| caf01d6b-972e-3227-9d59-b70639e06200 | -11.90609 | -46.70012 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README27.md)
