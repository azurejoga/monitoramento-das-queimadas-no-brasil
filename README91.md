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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad805cf9-33a6-3436-8ac6-d348c4395fb1 | -12.1736 | -50.82483 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fafbc42-e79e-3170-a781-e8c99c138673 | -12.1736 | -50.80325 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 471c632c-4e80-383a-9f06-21dbd6a6b71a | -12.17305 | -50.82833 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6075102-f67e-321d-8ce6-471961a64d65 | -12.17085 | -50.82078 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfb42980-6cf5-3a62-8802-7376394e2697 | -12.1703 | -50.80271 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5aa0d5cb-dd78-3f96-9857-1b8b7b36d539 | -12.16919 | -50.83131 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62aab229-d17f-3461-bc0b-ce55f3195ae5 | -12.16755 | -50.82025 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cafba360-1cf8-390a-adb7-02f0e65017bd | -12.167 | -50.80217 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3f1c6ad-b4e1-3b3f-9f77-1fa774694d38 | -13.17151 | -50.64515 | 2024-09-27 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ac7ace2-5d4a-3155-b404-f43eaa54240d | -13.04279 | -49.87086 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b33f7e16-5e31-3183-aa2e-f53bff9f7e4e | -12.47544 | -50.42038 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65361dec-c7eb-3bc1-b689-29973d7fd18a | -12.4749 | -50.4239 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eeb67200-6bf7-3ea7-beaf-7895a8170d7e | -12.47214 | -50.41986 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a30952cc-68b6-3c19-bb42-6988dd25cbce | -12.82735 | -51.12712 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a4fddf8-8270-3050-9a2a-b4e485ea0488 | -12.81744 | -51.1255 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d555aee-87f4-3344-b2ee-39fac251bf7f | -12.81414 | -51.12496 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7356ca73-990d-320e-b78a-ba35fad8338a | -12.53948 | -50.63972 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d5eb2cd-65a9-3254-8e9d-a82e83aee49e | -12.53673 | -50.63568 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c8b4893-be06-3f18-8536-88b0a6e51418 | -12.53287 | -50.63865 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfe826da-efe1-3d91-b121-ec9fd1dce2cd | -12.34687 | -50.50071 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 840f2f57-60d3-3c1f-be8c-e85c8142abab | -12.34357 | -50.50017 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0361ef46-393d-3d02-9391-537eb39e70a6 | -12.30833 | -50.5089 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c876372-dd59-3383-93ee-aab7314edf9a | -12.30448 | -50.51188 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcf25914-4bc8-3227-adaa-9dd613de9266 | -12.30118 | -50.51135 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e5cd0f2-383c-3f7c-90dc-6c3cd2ac4d32 | -12.29904 | -50.65495 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 681c7a6a-bc3c-3b10-8a3d-f21ee8366d3c | -12.27805 | -50.50762 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eccdd071-ea34-3c17-9e3c-dfd67793d86b | -12.27537 | -50.63314 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 619671d4-5d13-3233-a35a-780c7b356cb2 | -12.27256 | -50.52113 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 158d0339-d43c-309d-b6e5-bb70b42bfde8 | -12.27207 | -50.63261 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad421a31-adfa-361f-adbe-1b40c5e4c68a | -12.27201 | -50.52465 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bede974-3be1-326d-948d-f8d30175345b | -12.27152 | -50.63612 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e83abb0b-8098-3f84-bc1e-4d938d2457ba | -12.23409 | -50.85309 | 2024-09-27 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e574cf57-fa8e-337c-8f8c-6b8683677680 | -6.35806 | -50.70916 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0cc6342-2aa5-39dd-994a-e30cc36695b2 | -6.33736 | -50.70961 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d223cbda-1508-3810-90d6-a94c72bae747 | -6.33401 | -50.70909 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4c9fa25-01fc-31bb-b056-3958f2f4533c | -6.3109 | -50.70929 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffc32058-bb2d-3599-aee3-bfc888d90db4 | -6.30451 | -50.81476 | 2024-09-27 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef16b420-d64e-3fc2-a5a7-d65154664d52 | -6.28752 | -50.87847 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c57010e7-90f6-39ab-b7cc-9dcfc44ceec0 | -6.28415 | -50.87793 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afb3957c-bb54-3b06-b84a-74e4851fbc89 | -6.28079 | -50.87738 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58a32e1b-20a9-3d25-b44f-6babcb2682ad | -6.28021 | -50.88098 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e49e2648-deff-3e16-8f76-d5e310dd9814 | -6.27907 | -50.88821 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b334b39-fcb5-342d-bc93-9791a1b8331d | -6.27799 | -50.87325 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a307f4e3-f697-3646-966d-6e50d77b5c1d | -6.27627 | -50.88405 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8b97186-091d-3f94-80d0-7550c7a5857a | -6.2752 | -50.8691 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8ce37ee-b554-3246-bbf4-8949d3dedd51 | -6.27183 | -50.86855 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34d84c8b-1f4a-3d86-a86d-518b3eb76a67 | -6.26272 | -50.90409 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d6dfb08-92cd-30c0-a551-8810208b8e0f | -6.24933 | -50.87976 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c3fdeae-5d80-39a1-a7f4-62dd92bdcbd2 | -6.24653 | -50.87563 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 328ba265-7e61-32ae-b798-0de2e96d0b3d | -6.24037 | -50.87097 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24a2771f-b870-32ce-9445-3916f464ded0 | -6.23758 | -50.86682 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d23c5ac9-763b-3ac8-ae9d-f2872e97947d | -5.78055 | -51.04308 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 001a48a7-a2ec-339c-819e-f0bf54e4f65e | -5.77778 | -51.03869 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8cccd207-2a35-3681-82b2-412d6aa49449 | -5.77716 | -51.04249 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ea0010a-5ab5-39e5-a414-b57659a1241e | -5.77439 | -51.03812 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef09c48f-f293-37aa-869d-ae6984178239 | -5.77378 | -51.04191 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3868e355-e790-3e52-8590-489127295f7a | -5.77274 | -51.02668 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6831278b-793b-38eb-8e4a-18735456a461 | -5.76934 | -51.02618 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a789304f-f389-3989-995c-2e23bcdf5091 | -5.76594 | -51.02571 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80d0b40b-382a-3071-92c9-735f7391376e | -5.76253 | -51.02523 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ca6839a-fa8b-39dd-adac-450d3fbaa234 | -5.75912 | -51.02479 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0946fbda-36ba-3ceb-b886-f635a37f0354 | -5.75854 | -51.02839 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 719dbf38-fe3c-37bd-a879-c9cd657dc5bd | -5.75796 | -51.03202 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 300e05d6-0962-3ebd-89d0-45bbc25d6d92 | -5.74062 | -51.07468 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f878a7c1-453c-37c0-8807-04ede4f9086b | -5.73662 | -51.07788 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45ac5e79-0dab-3f41-ba74-f0f86dbf8f4f | -5.73503 | -51.06617 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7458e44f-fc3f-32ea-9bb9-cae054df3b4c | -5.73442 | -51.0699 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e50e8b14-2d18-3f4d-9db0-7a9b43208ed8 | -5.72824 | -51.06502 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9e640ea-fc6b-32a1-862e-a86ddc358357 | -5.72764 | -51.06873 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43a3b060-2397-3b4e-b471-672c5f5528b6 | -5.52445 | -50.53632 | 2024-09-27 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31c1bc5b-8abe-3b62-9a4e-884abfe0838d | -6.21996 | -50.91207 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82bb9c26-232b-31bf-8a8e-e2df9fb8ac44 | -6.21659 | -50.91153 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb44032c-7467-386f-828b-87ccba8d0e41 | -6.21322 | -50.91098 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 884fda88-6d7d-33a4-becf-4322a1e1104a | -6.20985 | -50.91046 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 857b3260-cc55-32d1-8713-a10b2321659b | -6.20647 | -50.90995 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a9bde43-1b45-34d1-8bfa-46487be0730a | -6.20589 | -50.91357 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7030707b-9d67-39d9-bf85-748b80e504c5 | -6.20251 | -50.91306 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 85cb5cc9-0e51-3882-b085-4c1c78b961a1 | -6.19913 | -50.91253 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4ddb0656-2a07-34de-9727-f3571f5d5c20 | -6.19855 | -50.91614 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05cb9498-c4bb-3bc9-bc93-50390bfa3181 | -6.19797 | -50.91974 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f2c712d-01fb-3975-b2b4-fef3dfac5ee1 | -6.19576 | -50.91201 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e334645-25f4-3d2f-831f-076882711c29 | -6.19297 | -50.90785 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bee3533e-1cbf-3e62-bae3-7b483e5654cd | -6.18902 | -50.91093 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fa69235-9517-3527-affb-36e96cdcef3e | -6.18565 | -50.91039 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b70800a-f76e-3303-a1d1-4de8f342fffc | -6.18412 | -50.90957 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b41d06c9-2032-3c81-86c4-cf56d7cf4eee | -6.18355 | -50.91318 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fe51c4d-0e65-3b9c-9e31-141a29889cb5 | -6.18018 | -50.91264 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fed64df-d748-3011-8d83-228116dd638e | -6.17961 | -50.91625 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f79acee-1d27-3a7e-9d00-97c2ebf812ac | -6.17731 | -50.93079 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 229c0cd6-3756-3d20-932c-259f19fc63de | -6.17623 | -50.91574 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 989f54a6-427a-3b88-964b-da1bc01d0727 | -6.17566 | -50.91936 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13539278-1f65-3096-be78-0efe02dae27e | -6.1582 | -50.92034 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54dbd364-dc96-3009-8860-61b11cd455bd | -6.15483 | -50.9198 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 615953ae-3bf8-3ea2-b326-ace941e69c6c | -6.15146 | -50.91924 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ec618e5-7186-3685-a410-fa85d7df898f | -6.13392 | -50.94241 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52199ff8-4aa0-3556-8065-928dac88044f | -6.13334 | -50.94604 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b9160d7-10f9-38b9-aee1-b059cea1e4cf | -6.13276 | -50.94965 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7de24fb4-c521-3185-8132-035b05a8fcd0 | -6.13219 | -50.95326 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11b43866-2153-31cb-b90d-819794af4da9 | -6.13161 | -50.95689 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 131a6f01-9044-3d97-b816-02b2d4d2d261 | -6.13103 | -50.96051 | 2024-09-27 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README92.md)
