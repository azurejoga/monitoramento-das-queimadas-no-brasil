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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8164065e-c3e4-3522-b2e0-f25ff496f988 | -3.79387 | -52.28846 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa03cae1-4c57-3c70-be95-654cd4a05239 | -3.78025 | -52.37663 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3de9f035-e8a0-37aa-9c2c-763b8a7d3b30 | -3.76472 | -52.40671 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2585f4b9-305e-3b42-9d0e-5d155995caec | -3.73866 | -53.40809 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c15c59e-69dd-3030-9bae-df3463232f2b | -3.73753 | -53.73337 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5d20367-22ef-3458-8daf-2f01782f7790 | -3.72056 | -52.34397 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc5d43a0-2dd8-3408-bf51-363ae3e6bfd7 | -3.72002 | -52.34277 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47af0230-f709-3856-b5bf-15c26d84706f | -3.71942 | -52.34678 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 885bb94b-fd8a-31c4-a219-c009d3153116 | -3.71703 | -53.39009 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fff6dcd8-8f85-3a69-a37f-1e5ca82dd19f | -3.6144 | -53.51226 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ebd9d66-ce34-3d4f-884c-501a9d493684 | -3.611 | -53.51174 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fa0b030-b407-3524-a223-dfb5a5eea4bd | -4.21157 | -53.8684 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9191b743-e83a-3109-b39f-9e0421c7bab0 | -4.20876 | -53.86429 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ce605f5-d69a-36a6-85fc-174da499e7d8 | -4.20819 | -53.86791 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 696c4604-9d95-3aa1-90e9-62e847bf3c60 | -4.20538 | -53.86381 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c1163ad-d478-33b4-9209-f180766cb953 | -4.20481 | -53.86742 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 636dac7f-e9f0-303c-8e77-0e823dcafa66 | -4.20144 | -53.86691 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15c4c713-c504-3a2b-99fd-1fe147ca3ff8 | -4.11016 | -53.86765 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5805fd4e-e455-3c89-bb30-662aff71dd7c | 1.16723 | -52.80627 | 2024-10-29 05:01:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2e297fd8-11f0-3004-b094-ab02ed8863bc | -1.13971 | -54.10447 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 427925b6-87ad-39cc-abd7-7603c889c7fc | -1.13639 | -54.10396 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd71daca-f72d-3a8c-b3ef-676778f20a6d | -1.1309 | -54.11726 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f2d94a4-e7d8-37e1-9378-3d6afc9f2fdf | -1.121 | -54.13692 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac0bb1f9-3494-3a72-97e5-33e5a2f4929c | -1.11937 | -54.14727 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8723ee2a-bb73-3bb8-aa01-7b3d5488c8b9 | -1.11822 | -54.13297 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ca06359-90d5-3fc2-93a7-b8c339a9233d | -1.0914 | -54.21709 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fc49465-5085-3167-aeef-fba08c2c34aa | -1.08293 | -54.16282 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1af8cfb2-8218-3ed6-8e47-5f08aac139d2 | -2.26118 | -53.55136 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cd854ff-e17e-3373-b8b8-00915bbc5e8e | -2.26048 | -53.48942 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36e6de41-843d-31da-86d5-cbe67654f4fc | -2.21783 | -53.67516 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 690e5ae0-b47a-3b6d-8d23-da88f6edc338 | -2.21728 | -53.67868 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1204efd-9659-378d-bbfe-c36823dda6f8 | -2.21645 | -53.67145 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20ded7e5-72c2-3425-93bc-12a0b8d35efa | -2.2159 | -53.67497 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6504d807-3bfb-38a9-a029-40806ef4d67c | -2.21534 | -53.67849 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 813cfc7b-4194-3125-b8c9-77c1b5b0506f | -2.2131 | -53.67093 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 224fb033-ecc5-31f1-b935-f16cdb34bc18 | -2.20362 | -53.68751 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9517397f-bb9f-3b3c-a786-2364d21d7f76 | -2.19635 | -53.69 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d93bbb0e-3b77-381a-aa1d-ae45d6db15d0 | -2.1958 | -53.69352 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09fb65fb-7aa3-36da-be43-3185fb86a67b | -2.07506 | -53.55567 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf161619-aae8-36a2-999f-b6f738100864 | -1.87132 | -53.75837 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5da7dd3-4e45-3842-bba7-6a8164135b55 | -1.86798 | -53.75785 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23c7db4c-8043-3654-9eb5-56114c9f9c64 | -1.65605 | -53.40057 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56ce7968-8045-3a38-ada7-ff954d55e051 | -1.75262 | -54.4469 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 232f7c4c-49ed-3e26-8c87-b1ec7a821ea0 | -1.74931 | -54.44638 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23eba8d4-891d-309c-8e2f-9a34fea06278 | -1.71915 | -54.70276 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5e95904-f84a-3271-bc98-40f2e1d9d39b | -1.71584 | -54.5294 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 250e17cb-71d4-351c-959b-6e0a8389670c | -1.71253 | -54.52889 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c0588e8-5986-34c5-8604-8b5ce7960858 | -1.70921 | -54.52837 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8062e96-b9f3-39fd-9a05-ef0cccb5e4f9 | -1.60963 | -54.77388 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cac1ebc-3fdd-37c3-8582-4480f682ec05 | -1.60909 | -54.77733 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7701881-b053-34b4-a106-358400766b6c | -1.57037 | -54.59145 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9c68f6c-35b6-3462-bd78-e72087f5bd36 | -1.56549 | -54.44962 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cae0bc79-cfec-3bff-bfb5-065a329e7fa8 | -1.56217 | -54.4491 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bef09d76-bc18-3806-abd0-354358030a5b | -1.55885 | -54.44859 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1008766-04bc-3f8f-af2e-efb872ebf990 | -1.53042 | -54.71571 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a47bb2f4-6b06-3f5f-bbff-2edf82dcb0b9 | -1.50591 | -54.27101 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bf426b3-29ae-3b08-a76c-876ec5cf61dc | -1.4992 | -54.76739 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 147cf8ec-559b-39ab-a1a8-1a8bf01035e2 | -1.48768 | -54.27878 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bbc7ee5-d1c9-315c-8342-45d7f43dd3ad | -1.4849 | -54.27482 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf71d46b-3f1c-39e8-bd4c-0ef62b2ce950 | -1.48436 | -54.27827 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48fe2bcc-b28e-314f-ae96-2fb6a84642c2 | -1.45148 | -54.07861 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4858685e-6523-3bf4-8e3f-59a985fad450 | -1.44924 | -54.07116 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 926504e4-d942-3eb6-a029-a894b97db251 | -1.4487 | -54.07463 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 537086d1-e9e6-3738-9b92-4477f300234e | -1.43808 | -54.22875 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2321386b-48c8-3a41-937d-a34d1abc4465 | -1.43754 | -54.23219 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f33e1eba-1221-333e-ae60-a04a1162657b | -1.43699 | -54.23564 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4f6f050-51b9-3187-b80e-fe6042dbe5a5 | -1.4353 | -54.22478 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 159958ee-e895-300f-a3ae-fa02dc995180 | -1.43476 | -54.22824 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 029db87a-96c6-3c01-ad3d-86a5cd7ec985 | -1.43447 | -54.48931 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9a275dc-cf0f-3f6b-b05c-7e1935d91c75 | -1.43393 | -54.49275 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67564413-7b0f-3b0f-af1f-33d65a8b9a5a | -1.43367 | -54.23513 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 139f75dc-9d65-3d1d-8849-277fefd07cd6 | -1.43252 | -54.22081 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e99d9449-c842-37d3-80f0-fcf33fd4591f | -1.43198 | -54.22427 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1b1f4825-c4e2-3995-b32a-be09b23e7d14 | -1.43116 | -54.48879 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 151a3453-47fa-3d6c-b085-69eb8a680b9d | -1.42866 | -54.22376 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5d39ba75-2ecf-3faa-8dbc-f0b8eaa04d0c | -1.42588 | -54.2198 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20404ab4-5de9-3eb5-91d7-aad73e098c51 | -1.42534 | -54.22325 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9fd6c389-1b92-3b3a-ab2f-119d85ff7c84 | -1.42249 | -54.54385 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dafd51b9-3076-37e5-b4c7-6e2a58ba280d | -1.42202 | -54.22275 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09c145f3-9d6b-3438-8b66-63f0e423f044 | -1.42141 | -54.55074 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c84454cc-ed7b-3d6e-bc16-98b19c0a6281 | -1.41755 | -54.55367 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1b8dbb7-4ce9-3362-a832-54f1755cab31 | -1.417 | -54.55711 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d13e0a8-aa82-323f-afee-4065802aec8a | -1.41423 | -54.55315 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 28e648c2-b049-3cf4-a162-fb91e87106a8 | -1.41369 | -54.5566 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 296cc861-72c5-36ef-b7b2-3f7a63b6f383 | -1.39363 | -54.04091 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b98856b-166e-3f36-9e40-91d02e275d45 | -1.3903 | -54.0404 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf4d98e1-81d3-367a-9ee2-1ecd1a1bff81 | -1.38975 | -54.04387 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8dda8a3-8d8f-3a1f-af02-bdf4571be246 | -1.38643 | -54.04335 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 586e980a-8169-3db5-9fb9-f589fc109cef | -1.35032 | -54.61374 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09642d56-9c7c-34c2-bb52-67cc51369649 | -1.34754 | -54.60978 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d87de3c5-8356-34de-ae90-6e4920dcad29 | -1.347 | -54.61323 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 814d6efd-dc9a-3a38-b872-3317b29ce50c | -1.34646 | -54.61667 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04628e70-248e-3f6b-b9a3-96a1cfa34f15 | -1.34423 | -54.60927 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fb7b9f1-3509-356b-ad24-235606b89b96 | -1.34368 | -54.61271 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0077d73d-7071-3685-99a9-909093d63ffe | -1.34104 | -54.65109 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9932ca8c-5905-3d77-b712-294eab4c82c8 | -1.3405 | -54.65453 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4e889662-3125-3fe8-b557-dc967f3cee94 | -1.34037 | -54.61219 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae230eb1-3171-331b-bb56-b74bd851d2e4 | -1.33718 | -54.65401 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2789dac-8747-37ed-b1c0-80c782a6fe90 | -1.30886 | -54.21192 | 2024-10-29 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0769ea04-77ed-38f7-a2e8-b3dc7b7db631 | -1.29098 | -54.67103 | 2024-10-29 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README83.md)
