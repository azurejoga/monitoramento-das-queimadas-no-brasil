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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a16d5bb-7364-331e-9837-afa20e61bd1a | -12.59297 | -53.12675 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2600eedd-796b-3293-a600-d878dbb4ba0a | -12.59015 | -53.12225 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fafec24c-7abf-3e99-b880-c6f9f26ee99d | -12.5895 | -53.12615 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9760967-58af-3fe3-ab14-b0a295a0afa8 | -12.58885 | -53.13005 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cbc2551-5826-33ce-a253-bc490356db61 | -12.58603 | -53.12556 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 643f6334-4d9b-3638-aadf-83a06418c11b | -12.5791 | -53.12437 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cfd10541-14e1-3309-bab5-521c18375c87 | -12.57563 | -53.12378 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1963bfca-9b01-3faa-8f27-75cec9a1d31b | -12.57216 | -53.12318 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bd06d02-f05b-3dc6-99d3-a2f1d3ea471d | -12.57151 | -53.12708 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18012cac-6dea-3dd7-8fe4-cfa886b92e5b | -12.57021 | -53.13484 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f8856b4-be04-3c2f-ae62-e52bed550d4a | -12.56262 | -53.13755 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccfce44c-6403-3279-9a2e-7c5fae01c0dd | -12.55156 | -53.13965 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00886bee-2e21-361b-9eb8-8c782372a89c | -12.54982 | -53.14027 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 798fa2e2-cbe2-326a-8d05-d991bf6879d3 | -12.49799 | -53.15138 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26dd3ea3-6463-3645-b66b-0a1ac7309c08 | -12.49517 | -53.14687 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4638a14-7b93-3624-bd04-1fd3df494eb9 | -12.49234 | -53.14238 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d724ed9e-56c5-3d7c-b16a-8b71dcb753e6 | -12.4917 | -53.14627 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 509241db-eae6-31a3-a593-14c50e9c42bb | -12.48887 | -53.14178 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6234f8d2-7306-3397-a09c-114b97f45401 | -12.48822 | -53.14566 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 127d0e03-6f15-3db2-8bc3-331ff40efa50 | -12.4854 | -53.14119 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a97ec9dd-6be7-32e7-8ca5-6646e328de49 | -12.47975 | -53.13221 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de8a0ba3-817f-3bc7-b959-fbe5334ad3ec | -12.4791 | -53.13612 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08e4ba36-5474-341a-9cd4-ced6cdd670e1 | -6.40599 | -53.68055 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5abaaee-37dd-3775-bf18-ea01e3f510c3 | -6.15039 | -53.4225 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0f34027-85cb-3cb2-a355-df0e42be4cd2 | -6.14661 | -53.42177 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d4ef159-54db-3ef7-92fd-54309d53fecb | -5.90613 | -53.44404 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e806004-28bb-3441-a822-57d3fe9b9ed9 | -5.90535 | -53.44874 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0691ccba-ed96-3af9-8cc9-9ff7049646e0 | -5.90384 | -53.4342 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8099b39b-457a-3c41-85e4-7a97cc866b63 | -5.90309 | -53.4387 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5c4628f-72b8-3fc3-866f-808bc401e80d | -5.90232 | -53.44336 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ae56e4b-dd2d-36f2-934e-5ed693570585 | -5.90153 | -53.44812 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 96bbfed9-d2d7-36a0-bf6a-d2977dd7f0ff | -5.89927 | -53.4381 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59af411c-a6c0-3cd0-86c7-fb139aaf3c56 | -5.89849 | -53.44284 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d8c6909-d9ad-312a-9246-06a99f580d8c | -9.46258 | -53.60488 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70f7e523-99a4-3eb5-95d2-2fa65f21ce77 | -9.45891 | -53.60426 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c23669c-0ad8-3414-a854-51dc59009da0 | -8.92541 | -54.75135 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab76c705-0164-3c84-9097-44b3a3c62e5d | -8.90702 | -54.45831 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a9d6908-bc1c-3085-8e04-4fa32328c901 | -8.90313 | -54.45766 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f53f45f-69aa-3cf4-b6f7-59f89f8a19eb | -9.6676 | -54.32114 | 2024-10-05 04:38:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8864ce5f-5243-3938-888e-d4308645689e | -9.66679 | -54.32585 | 2024-10-05 04:38:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af5aff9c-eece-3063-b360-e186e1c5198d | -9.66458 | -54.31583 | 2024-10-05 04:38:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 899ca00f-271c-3b7c-923d-600da4a4758b | -9.66379 | -54.32047 | 2024-10-05 04:38:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64321d4c-a928-3a99-81d9-0b3b120b4efb | -9.66299 | -54.32514 | 2024-10-05 04:38:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c3b4efb-bbdc-3bfc-ab4b-c25648a4af4d | -10.58536 | -54.93307 | 2024-10-05 04:38:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e7249c8-0c08-3955-a89d-c263114e7f94 | -10.39401 | -54.80355 | 2024-10-05 04:38:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0ededbb-435a-343d-9097-baa53039068e | -10.39318 | -54.80848 | 2024-10-05 04:38:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4abca2f0-d762-3f6e-80ca-174f6172f406 | -10.39013 | -54.80286 | 2024-10-05 04:38:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| add0cd41-f480-31cd-8076-0fd3dd9b996c | -10.3893 | -54.80779 | 2024-10-05 04:38:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 247a1bca-a62c-3282-aba7-0c13e6c9dbf9 | -10.34038 | -55.19146 | 2024-10-05 04:38:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78019872-6036-36f7-9cdc-37130c289f3d | -10.33699 | -55.18729 | 2024-10-05 04:38:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0502229d-ded2-3d39-a667-5a01636e81b1 | -10.38665 | -53.79702 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1f952a5-2ec5-3097-8fc7-1a2161da098a | -10.38373 | -53.79202 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87aafcf1-ebe1-36b3-aa57-150143379af4 | -10.38299 | -53.79637 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c6b0f05-182f-39b4-80ff-eef5508f325d | -10.34292 | -53.76847 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4685c041-e376-3084-bd7b-46521e67b14f | -10.33925 | -53.76784 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35a6eaf2-e27a-3c9b-99d5-5da8fc8d50fa | -10.33559 | -53.76722 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2688601a-ae28-3f54-8c86-ca8c57278026 | -9.66077 | -53.58574 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e13d73df-ca13-316a-baf6-0889db3f4c38 | -9.65784 | -53.58078 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17e2327c-106d-3029-b6a0-64571d76f8c3 | -9.65637 | -53.58946 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9d7e18f-988d-31fb-80ff-d61f4364424d | -9.65422 | -53.58273 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3a509f5-43c8-397a-ba9c-062e4f93d55d | -9.65419 | -53.58017 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85389a9a-c110-39c4-aa5b-1c3f7fb43c81 | -9.65056 | -53.5821 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b79e79e1-b830-3460-b98c-3c90e2d24b7b | -9.65053 | -53.57954 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21d11ec5-dd73-36e7-9641-16aea10e2d58 | -9.64968 | -53.54165 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12016949-6d77-37c1-b439-037548edfc6b | -9.64897 | -53.54598 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f411568e-cc9a-38dc-84e6-dbc9c424afb0 | -9.64613 | -53.58324 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bb072ac-ddff-306c-821f-5712be8d6aa1 | -9.63959 | -53.58018 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2342e5bb-15bc-3f49-8116-fe210c3f29a6 | -9.63665 | -53.57519 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2486282c-fe93-3b18-900b-228cb51000a7 | -9.63299 | -53.57457 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41d7bba0-3bea-37dc-b692-d6bb2d7e5e31 | -9.63227 | -53.57893 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 702ae27d-92e1-3e98-bfaa-57bf27692b91 | -9.63018 | -53.61441 | 2024-10-05 04:38:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7256cf34-7bf9-3de3-b0f7-50a2e4a5192d | -9.62717 | -53.58705 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c51e07e0-3794-3f1b-8d62-c6150117d7bc | -9.62652 | -53.61377 | 2024-10-05 04:38:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| faf8cdfa-8c53-3622-aee0-8533c3e82c05 | -11.38986 | -54.36034 | 2024-10-05 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e1ce40d-63b3-3bd2-b06e-21706560b373 | -11.38614 | -54.35966 | 2024-10-05 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29bc30d7-5bc9-3039-812b-4731b27da74c | -11.38536 | -54.36419 | 2024-10-05 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa23641f-7e7c-3f23-a07f-edaecd5fdfb1 | -11.38241 | -54.359 | 2024-10-05 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1f3c3b1-449e-34f1-8017-e7535783d64b | -11.38163 | -54.36351 | 2024-10-05 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e80d53e-f5de-3005-9191-91dc18f7457d | -11.35872 | -55.2122 | 2024-10-05 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90608244-4dba-362a-9795-0532edd982d7 | -11.31553 | -55.20786 | 2024-10-05 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b594685-2306-314f-a662-7dd3a70ee1b4 | -11.20966 | -54.97958 | 2024-10-05 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f8b38a0-1358-31bf-8317-fdce211b80f0 | -11.11269 | -54.22883 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b455640a-e73f-317b-a5ba-fc8540204ad9 | -11.11192 | -54.23337 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03aa685e-a9eb-3eac-9bec-ef061df1fee2 | -11.10898 | -54.22818 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c65cd6f0-39ac-3fe4-943d-feed99e9bf5a | -11.10821 | -54.23272 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 407fef0a-51bb-3e4b-82b6-da5c8792ccc6 | -11.10743 | -54.23727 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| db534980-7cf4-31f0-a3a4-439b9fd862d1 | -11.10603 | -54.223 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 61cc57d5-d345-35f1-8a2a-414854aa24b7 | -11.10526 | -54.22753 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e53f4ea9-3be7-3517-a6fe-1dab4056c716 | -11.10449 | -54.23207 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 62897762-a7ec-34ba-9315-019265fb841e | -11.10371 | -54.23662 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9af0fa61-507b-3602-b155-ae73a49fc729 | -11.10231 | -54.22238 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6ce2db2f-1c6f-33c7-a0de-d1c2a61dc8b2 | -11.10154 | -54.22691 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5e9f4420-73de-3b50-bb45-127f9c34c2b7 | -11.09704 | -54.23085 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05bcc394-4243-32fd-ab20-5a775c3f11fb | -11.09627 | -54.23537 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44c067f2-b1c5-3298-9f0e-019dc56443b7 | -11.08325 | -54.78362 | 2024-10-05 04:38:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 468f50ac-fa41-3530-9653-79b83eac9b73 | -11.08166 | -54.78077 | 2024-10-05 04:38:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 96846c38-ceec-3a6b-8e52-b798186c55d2 | -11.08108 | -54.77339 | 2024-10-05 04:38:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ca374e7-7a6b-3b18-a324-1d6df33d9da9 | -11.08085 | -54.78559 | 2024-10-05 04:38:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9308353f-5651-3faf-92ad-023700c44876 | -11.08024 | -54.77819 | 2024-10-05 04:38:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7e79576-0b41-394b-a807-ec2c7e309810 | -11.0794 | -54.78299 | 2024-10-05 04:38:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README111.md)
