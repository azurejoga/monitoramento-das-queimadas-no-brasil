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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e367e00-5453-3b06-8203-965893d946ca | -2.8769 | -50.76065 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad831e21-f0d1-3332-90a7-6442c8a7bfb0 | -2.87641 | -50.76373 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 10c15460-83b9-3f46-adbd-b3b902b82a81 | -2.87466 | -50.75703 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 676adb8b-82f2-37b6-91ef-94cfda997f83 | -2.87464 | -50.78851 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 950ba499-76f8-31eb-9de1-4bb2482a7c84 | -2.87415 | -50.7601 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8dac9532-3cf1-332b-bc48-b2caa489ce76 | -2.87413 | -50.79155 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4784e032-0a1a-3ba4-9158-61e6a51a56d1 | -2.87363 | -50.76317 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dde97585-39aa-3834-bea6-9be6508dd68e | -2.87362 | -50.79459 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b727a7f-5bf8-395e-a5fc-01c8495d0a67 | -2.87312 | -50.76623 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6418612d-d32a-33ad-a11a-d3e10a74aa1e | -2.87226 | -50.75673 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4a57fa5-9e35-312d-adf7-69d269770b00 | -2.87176 | -50.75981 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8732c90-c477-348b-8e40-92b169b23765 | -2.87127 | -50.76289 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bd2df1ce-a758-31ff-8f37-a2b285a7b6c2 | -2.87003 | -50.80349 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 746cc41e-f6ea-3377-b096-f01f1fc4799c | -2.86902 | -50.75924 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ae3daf9-8323-3cad-9d01-1810f524684c | -2.8685 | -50.76231 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b139db34-7f65-3b1c-9a31-28708c845f20 | -2.86848 | -50.79373 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bbcb695-2aab-3ec8-818a-45a156edb9e1 | -2.86799 | -50.76535 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 162e0579-5170-3cdc-8ddd-6fa3eb703fae | -2.86797 | -50.79675 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b1a68ec-4863-33fd-be37-372640c8c451 | -2.86746 | -50.79979 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e27cb24-6a5f-3c23-878c-4261a2e90cd6 | -2.86664 | -50.75893 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 641798c5-379b-3e4d-b27b-4b3ca1a6a13d | -2.86614 | -50.762 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b0b541a4-17ad-3e9e-84c9-2c811d26f884 | -2.86591 | -50.80899 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7133706-5e66-3af0-a827-dbf988d21524 | -2.86488 | -50.80263 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02e3f1c0-d388-3f6b-b567-63a5457bc39b | -2.86488 | -50.78376 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aabb695d-ff32-336f-a972-4b27bc736abd | -2.86439 | -50.8057 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cced493-2b43-371e-9542-3b0b56c55b57 | -2.86436 | -50.78685 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c83292ca-9c93-314e-ba07-28984e64f4de | -2.86389 | -50.75838 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 14668ccf-f780-3cd1-92f1-e26093027abc | -2.86368 | -50.77731 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0e5ef16-6a3e-35a4-bde5-ade981d049e7 | -2.86338 | -50.76143 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb46f91a-5e98-3f45-a130-f0edbc302a3b | -2.86318 | -50.78041 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14319b67-d7d4-3f65-875e-acbc05caad37 | -2.86286 | -50.76445 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0a1b9cd-7dde-3161-88df-c74f39024a32 | -2.86268 | -50.78351 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed6dae49-b282-3f75-988a-c1aec62f22a6 | -2.86235 | -50.76749 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81309440-222a-3c14-a12d-b66598f38d09 | -2.86218 | -50.7866 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 98550fea-7b9d-3721-b540-ffda0d6dae66 | -2.86184 | -50.77053 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c65c4696-34dc-39b5-ad0e-462f33f741be | -2.86151 | -50.75806 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e8201557-74e4-3c94-806e-e5859dfec50d | -2.86101 | -50.76112 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e5e7c24-44cf-3cf4-a1c0-b305ccff152b | -2.86052 | -50.76417 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7732eef1-f6a5-325b-b707-ed2ea5e1ffbb | -2.86027 | -50.7798 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65be27af-fdac-3756-9047-efc74a22ca17 | -2.86003 | -50.76722 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca036762-5972-349b-aa40-d8925942a906 | -2.85974 | -50.78289 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9332e00f-b044-3c04-8ef1-ff0ad30be94a | -2.85924 | -50.80483 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b45119c-ecb1-3437-89a9-b643bf28a107 | -2.85904 | -50.77333 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| afa0e1b5-6129-3e46-9460-42fea51a4d6a | -2.85874 | -50.80793 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02d875a3-cb80-341e-9d19-b2ab05856749 | -2.85804 | -50.77954 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d7cff28-22ff-3625-96fe-301ca8706a4a | -2.85704 | -50.78571 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0306d501-6d94-34ae-b73d-7b486926b457 | -2.85637 | -50.75721 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea5efeb7-ee8b-327a-a352-65d2adeac41e | -2.85538 | -50.76336 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8d2c8a02-88d0-3a4d-bb87-b7e549c98b99 | -2.85409 | -50.80397 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0452694-e198-3fa7-afc2-e894bd484947 | -2.8519 | -50.78484 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| afda9c67-4109-3080-9965-7e7d908c518c | -2.8514 | -50.78793 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22397cbb-48eb-3945-8c80-ee682943e9e4 | -2.85091 | -50.79096 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54019fb2-e858-3bde-ab34-56e7fec000ea | -2.84993 | -50.79704 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f5ea983-cd46-34a8-aa22-fa2d61f0a728 | -2.84894 | -50.80312 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13c18a18-76a4-39b2-b7c3-4c7ef43e8900 | -2.84776 | -50.77782 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ef33783-1d3b-362a-af95-15d43b3216d8 | -2.84726 | -50.78089 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 595057fd-382a-38b6-b59f-21dbf0d9ad28 | -2.84626 | -50.78707 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6dd738e-f1f8-3a4c-87ba-2e1cd6ec0638 | -2.84429 | -50.79924 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3581e81-03ad-3c30-b941-67e98e7cf271 | -2.84379 | -50.80228 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fa0cf38-8380-32af-af2d-d2036108355b | -2.84329 | -50.80534 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8047c92b-1582-3ae9-911b-a48b082fb00e | -2.84263 | -50.77694 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5381e166-a661-377b-a9ec-7d41756e66ab | -2.84112 | -50.78621 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e92870d-200d-3f1e-9e79-562a2d5b4312 | -2.84062 | -50.78925 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1491d392-be56-3e11-8acd-9e7c53c53f71 | -5.15944 | -37.96778 | 2024-10-01 04:10:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3a257a1a-64f2-3ca6-baf8-5f1d1efdc8a9 | -5.1042 | -37.66647 | 2024-10-01 04:10:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b8a4df6c-d116-3064-974a-664e76afe932 | -3.88848 | -41.03882 | 2024-10-01 04:10:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 936c2f96-e6f1-3890-9454-3fe7c4dc6477 | -3.88659 | -41.0393 | 2024-10-01 04:10:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 585c1c5d-7e85-3e7d-8fb1-2e4907295122 | -3.96541 | -41.50937 | 2024-10-01 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f3439a3f-5fb5-3606-ab2b-8ffd7408f7ef | -3.96147 | -41.49083 | 2024-10-01 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 66b87ef4-9a26-3add-b9f7-0e51085174d0 | -3.95759 | -41.49381 | 2024-10-01 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4cae4912-ae43-3765-b83d-84bcfd5db025 | -3.95378 | -41.5183 | 2024-10-01 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c06bbd66-380e-34fa-8b07-0dfdfb5ccdb0 | -3.95317 | -41.50029 | 2024-10-01 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1774397f-25bf-3802-ba87-7f5b9766ceca | -3.95099 | -41.51429 | 2024-10-01 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4a876200-65df-3720-8588-0b306941e35a | -3.95045 | -41.51778 | 2024-10-01 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 03f6939e-96f3-3fe0-97c0-da507cab8433 | -3.94991 | -41.52128 | 2024-10-01 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f229e5e7-a7e6-32dc-8789-8f7d2d267bad | -3.94766 | -41.51377 | 2024-10-01 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5e6755ce-4925-3ca8-a29d-94cb100b1bc3 | -3.94712 | -41.51727 | 2024-10-01 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c3e62723-3cac-342d-a822-faea990edf89 | -3.46795 | -43.35706 | 2024-10-01 04:10:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 85536864-cc00-33af-aa00-46db8fec65e0 | -3.46883 | -44.30184 | 2024-10-01 04:10:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8eccf2b-cd58-382c-9736-7c0ead9433f8 | -3.6052 | -44.79235 | 2024-10-01 04:10:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a7bee5f-1cac-3ea2-96da-52545fbde296 | -2.56441 | -45.7639 | 2024-10-01 04:10:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d72ff0e-37fc-301b-957b-e31bda7528b9 | -2.19971 | -46.27479 | 2024-10-01 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07b79521-208a-38a3-a7a4-2aac8ea5f2a2 | -1.80113 | -46.4496 | 2024-10-01 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 388cbce9-98ec-3f3b-9ee6-1cd551df6bd7 | -1.21476 | -46.73214 | 2024-10-01 04:10:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3028c651-eb43-3190-a3d1-aa5656ef6cf4 | -3.20984 | -46.04105 | 2024-10-01 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c883018-2e15-348b-b24a-01c1a3348912 | -1.16973 | -47.73355 | 2024-10-01 04:10:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 77d6677c-02b4-3a1d-a930-aa4a117e95c2 | -1.1691 | -47.73756 | 2024-10-01 04:10:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 685bd445-6a18-35d7-b8d9-1efa57c5c5ab | -1.16545 | -47.73286 | 2024-10-01 04:10:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| a96c1f3a-5fa7-3a98-8c7b-ee37507c457f | -1.16481 | -47.73689 | 2024-10-01 04:10:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 165b6006-6d0b-3136-9e9a-0cd03eebbe31 | -3.36527 | -50.37728 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eccbf0ab-a139-3635-aa64-0839b9ceafea | -3.36462 | -50.37526 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89a54f9a-2a6b-3b26-b65f-3727c32270bc | -3.36032 | -50.37642 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 620e251e-b15a-3def-9e0e-3fd8195d5e2c | -3.21367 | -50.45263 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be85b24c-49be-33fa-9cdd-06e6f6c7b756 | -3.09095 | -50.48019 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1b92b54-c7e6-3098-96e8-c0babf2cb64b | -3.09048 | -50.48304 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39e3bc96-4014-3b34-b3c6-925029905d2e | -3.08641 | -50.47647 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14457372-db17-3999-8637-fe215e4d6df5 | -3.08594 | -50.47933 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23de9075-2e36-3826-b3eb-33007b764bb5 | -3.08547 | -50.48219 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd55729a-de9c-384e-91bb-7955bc036edd | -3.06995 | -50.48255 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 724a4496-19d2-3788-81d6-5323908f4be3 | -3.06947 | -50.48544 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README66.md)
