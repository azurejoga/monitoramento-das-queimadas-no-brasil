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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 880c605d-da26-32b5-a415-af33c1fffb47 | -17.83922 | -50.50626 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 91a2488c-c6ad-38ec-9dd4-e6bc78efb363 | -16.71854 | -49.29616 | 2026-08-31 16:28:00 | NPP-375 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93c7c4cf-5061-3d7c-9a3c-dfef6238d41d | -18.55342 | -46.32956 | 2026-08-31 16:28:00 | NPP-375 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 53decf66-d674-3ee6-9fa7-e7f6e146a3f9 | -18.26854 | -52.69424 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| a1779067-a09a-302c-b0c7-85f693987c46 | -18.18971 | -43.9739 | 2026-08-31 16:28:00 | NPP-375 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4e0f9c0d-e87a-38f0-9ff6-ad61dabda294 | -19.84935 | -47.93808 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 05d41896-4229-3455-8746-7ff80e9b22c0 | -17.72465 | -44.26186 | 2026-08-31 16:28:00 | NPP-375 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ad27de32-3b95-337d-81a5-677b3288eb5f | -20.82362 | -44.84154 | 2026-08-31 16:28:00 | NPP-375 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| eb49531f-d2f9-300c-b7da-3f9946e00d4a | -15.57546 | -42.71204 | 2026-08-31 16:28:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5f7ee3c1-2387-372d-bd2b-8404bcbf5c03 | -17.18373 | -48.74357 | 2026-08-31 16:28:00 | NPP-375 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b4613d72-1e63-38ee-884f-1c5e496e2929 | -18.48422 | -43.97131 | 2026-08-31 16:28:00 | NPP-375 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9c4fc4da-0107-36d5-a70b-8ca5424e8ef4 | -18.41218 | -47.96231 | 2026-08-31 16:28:00 | NPP-375 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 5c3dd911-cf5d-3906-a180-581b90c29d0f | -18.6607 | -46.84871 | 2026-08-31 16:28:00 | NPP-375 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 543991fe-3e42-35aa-806d-c198f9aa82ff | -14.99306 | -48.13596 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 92f1b906-83a0-33b9-9070-530f1d249a9c | -14.31771 | -40.83327 | 2026-08-31 16:28:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0d1a774b-13d7-3910-adbb-0215d70001e6 | -15.19615 | -46.2495 | 2026-08-31 16:28:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3b32af35-99a3-39ce-93dd-80d209e8db24 | -19.42195 | -46.89446 | 2026-08-31 16:28:00 | NPP-375 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 174043ee-5e6c-34b9-9bdd-bb9b4e7eef5f | -17.88604 | -52.10606 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 47.8 |
| aeb87058-76a6-3b20-9fc4-28970c39f872 | -15.99526 | -48.04714 | 2026-08-31 16:28:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 1ecb9b0f-7ad9-36ef-bd6c-9d753767c6a9 | -15.02362 | -48.1799 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f153bc6e-75bd-3143-b36c-0580937f51e8 | -16.99345 | -40.93523 | 2026-08-31 16:28:00 | NPP-375 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| c5d91f1f-7a8f-3ad5-acf7-4c4c4e2b4bb3 | -15.11251 | -48.15529 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d327a638-49d1-3e6c-adb1-132c35279526 | -17.84667 | -48.75385 | 2026-08-31 16:28:00 | NPP-375 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9902e49f-25f6-3457-bc1c-8a18cae46e2b | -20.38163 | -46.51016 | 2026-08-31 16:28:00 | NPP-375 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 895c9269-8bcb-3fc2-93cf-086c7807a4a2 | -17.30121 | -46.95803 | 2026-08-31 16:28:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0deaeb93-a9c3-39c1-bf48-e95ec9a1144a | -19.85802 | -47.92521 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2ecab5ec-80a9-3dbb-970d-335cc74ee9c0 | -18.26267 | -40.54928 | 2026-08-31 16:28:00 | NPP-375 | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 1e8a1d03-9a2a-31e6-9ff9-1d940d062322 | -16.89246 | -40.22329 | 2026-08-31 16:28:00 | NPP-375 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 2e016898-9173-3c7a-9b75-b5dedfdd2fa9 | -15.61048 | -41.522 | 2026-08-31 16:28:00 | NPP-375 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| c51b5cc9-d729-3481-b97b-3d70813f444b | -17.86541 | -52.09149 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 219.1 |
| 56af034e-4b99-3402-ab8d-83974e8f22e6 | -16.44131 | -51.40943 | 2026-08-31 16:28:00 | NPP-375 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 045ddc6e-ac7c-3cc7-8e5d-de402914b87e | -16.51932 | -47.73219 | 2026-08-31 16:28:00 | NPP-375 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ecda14ad-4022-399a-9ef4-cd178f655050 | -15.98985 | -48.04227 | 2026-08-31 16:28:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6aec7f29-25ca-3036-95ff-be0f029ad266 | -14.63907 | -41.10624 | 2026-08-31 16:28:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3cdf7cf8-fd35-3589-a1a0-23ad967342f8 | -17.85027 | -50.50072 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| f3b387c9-c45e-39cd-8a11-c5a698ef0f52 | -17.87516 | -52.19127 | 2026-08-31 16:28:00 | NPP-375 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1846a424-95fa-3b0c-a6fc-5536ce0a6860 | -15.52097 | -39.92118 | 2026-08-31 16:28:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| a77a70fe-a1b6-3974-9844-5c600a6b5e48 | -17.87414 | -52.18072 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b51353a1-d2d4-3e4c-aab8-302673cc4742 | -15.6611 | -45.91076 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 632d3ec2-df09-307f-9b62-d08be5e2eb5a | -20.24666 | -40.75073 | 2026-08-31 16:28:00 | NPP-375 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 0ca68326-185a-360d-95f2-97dbc074a7a4 | -15.189 | -48.98088 | 2026-08-31 16:28:00 | NPP-375 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fb5c4b42-ac3a-32de-9f81-15a49068dd4f | -17.8519 | -50.5168 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 6c0f6c36-496d-34c7-b11a-1c315d45c554 | -17.86715 | -52.08859 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 288.4 |
| 2afd5e27-7eae-3e45-a5dc-a6adee583a89 | -14.98769 | -48.13139 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 95.0 |
| bd099ad1-7762-365b-a372-816984cb7739 | -17.13466 | -44.77066 | 2026-08-31 16:28:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bf83912-b89e-3734-acb3-92e93b50e75e | -19.85337 | -47.92474 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| ac36a8d6-1a29-379d-a142-3c09d5f339b3 | -17.721 | -46.85213 | 2026-08-31 16:28:00 | NPP-375 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b4117ef-91ab-3bfc-95b2-276c0e21c8be | -14.52605 | -41.67705 | 2026-08-31 16:28:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5f783f5c-6d92-396b-8116-ded48e22b497 | -17.86194 | -44.25504 | 2026-08-31 16:28:00 | NPP-375 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d3196985-61b7-30dc-999a-d1ec94812757 | -19.3736 | -43.44732 | 2026-08-31 16:28:00 | NPP-375 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d02eae9e-673b-318a-98ec-23fb2fee542b | -17.31718 | -39.24621 | 2026-08-31 16:28:00 | NPP-375 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e9122089-c6fd-3306-8fba-90963c48488b | -16.48334 | -42.30218 | 2026-08-31 16:28:00 | NPP-375 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 4487e824-3d80-3b51-8b12-67755df8b6a0 | -15.7447 | -40.42336 | 2026-08-31 16:28:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 760da5a1-5b72-33fa-9d72-264952852411 | -17.18975 | -54.31622 | 2026-08-31 16:28:00 | NPP-375 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2d5e20e8-7df6-3482-bfc1-6ba88dba699a | -18.26553 | -52.73542 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eb59511d-f552-397d-b5b4-6aaffd9922fc | -18.58483 | -40.13847 | 2026-08-31 16:28:00 | NPP-375 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c56ea7bb-13b1-338f-8633-3ac65e7df712 | -15.68294 | -48.22748 | 2026-08-31 16:28:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 52.7 |
| cb83d6ae-b8ba-3f1a-9e64-f19c04abd603 | -14.95591 | -41.39668 | 2026-08-31 16:28:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| efde3433-ed89-305a-952f-ed8397af8ee1 | -14.98949 | -48.13512 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 3eab4164-5d76-346e-86ab-36ec1811c877 | -18.88773 | -48.24286 | 2026-08-31 16:28:00 | NPP-375 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9b0248d4-6c05-386c-a1e7-46a1fa674a02 | -18.83088 | -44.24846 | 2026-08-31 16:28:00 | NPP-375 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4e4992f2-2aeb-3d1a-8779-d02dbd552ae8 | -17.88277 | -52.11939 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 8e15c204-5121-37d6-8cbe-11301d5f874a | -17.10362 | -42.01805 | 2026-08-31 16:28:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| b8da1ac6-e940-39d6-9c49-54a2b2969067 | -17.45222 | -52.41553 | 2026-08-31 16:28:00 | NPP-375 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c09c9ba7-5772-386f-b7c0-7ea5b2ebec7e | -17.71708 | -49.22551 | 2026-08-31 16:28:00 | NPP-375 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fed184fa-9b19-3e12-ba99-932bfb6d5d98 | -16.78848 | -49.26052 | 2026-08-31 16:28:00 | NPP-375 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 155d504a-5fe1-392d-a785-dbece45c50c0 | -18.26451 | -52.72382 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 467de258-e3da-3031-b796-eddbf5be7650 | -17.86763 | -52.09377 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 288.4 |
| e0fd3a50-e384-34cc-92a8-4a0e89ac5e42 | -16.55918 | -52.51476 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 396d27dc-f627-3376-84e4-77087de77c6e | -19.76901 | -47.89344 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c42372ac-0ed6-3bef-b943-f2ec66d246ff | -17.88228 | -52.11404 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 76f1cc1b-f831-365d-9d07-12a9997e738d | -18.21685 | -43.97499 | 2026-08-31 16:28:00 | NPP-375 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0ba54912-8174-3c37-9302-969a3f04a17e | -17.88501 | -52.09565 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 279.8 |
| 484c4848-e4ce-301b-bb60-c1f7e3c97b78 | -17.87228 | -52.09625 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 246.0 |
| 7d12b066-0062-36f7-8529-ae0f5b56ef65 | -14.98362 | -48.13718 | 2026-08-31 16:28:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a13161c8-a322-30b2-8efb-7bb5af5f6421 | -15.67806 | -45.94393 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ce423e44-9ebd-3f80-a951-e3403485df91 | -19.83873 | -47.93327 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 5ffd6e67-081e-3221-8c26-4f5edf2cc42e | -17.84385 | -48.75246 | 2026-08-31 16:28:00 | NPP-375 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c649e22-e9fd-34f7-9716-818e4b0c4ee6 | -17.84954 | -52.1059 | 2026-08-31 16:28:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| b576844f-92a0-37fc-b99c-cfabcb813742 | -15.61154 | -41.51785 | 2026-08-31 16:28:00 | NPP-375 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 22065011-0023-3455-8b14-9b54adb11616 | -14.95893 | -40.45921 | 2026-08-31 16:28:00 | NPP-375 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| c2113331-92cb-382a-b3b4-fe36d82c7310 | -16.88259 | -43.70904 | 2026-08-31 16:28:00 | NPP-375 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 802f6009-7267-3e47-8778-557342e6aa2e | -18.3131 | -45.68546 | 2026-08-31 16:28:00 | NPP-375 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f6655739-4849-3f9b-8b70-93932ac20857 | -17.72552 | -46.85167 | 2026-08-31 16:28:00 | NPP-375 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 247a2d0b-3d0f-3f8c-836b-d80b85a3185d | -17.71217 | -49.2295 | 2026-08-31 16:28:00 | NPP-375 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4f229def-4044-346f-9fcc-ec9ef70f223f | -19.85834 | -47.9241 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| bd217e22-3cee-3808-b295-695d17ece6f8 | -15.67245 | -45.93327 | 2026-08-31 16:28:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28439fbe-fb81-3400-b753-e30b6a23e600 | -20.29251 | -47.8342 | 2026-08-31 16:28:00 | NPP-375 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 2a8a200c-ede5-3ea3-93b6-dfd11438a0e5 | -18.68897 | -48.2271 | 2026-08-31 16:28:00 | NPP-375 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| c4ad27b1-f273-3ec2-861a-338bba359db5 | -16.57894 | -52.51839 | 2026-08-31 16:28:00 | NPP-375 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 49.6 |
| ff49912b-3dd0-31b9-9567-ea441469e43b | -17.85681 | -50.50795 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 283.8 |
| cdc20368-6e78-3ec7-975e-981c4fc479c7 | -18.27462 | -52.68783 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d42d900d-22dd-329f-a258-1ce58633c81b | -16.8586 | -49.59822 | 2026-08-31 16:28:00 | NPP-375 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a45c5c2b-afb2-3649-b53b-0a50b9be3655 | -19.85866 | -47.93101 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d249612e-2003-34bf-964f-5e0a649e320a | -16.00007 | -43.55461 | 2026-08-31 16:28:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9cd5ceed-4578-357d-ac93-feca29a2b501 | -15.99589 | -48.05239 | 2026-08-31 16:28:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c30fc057-1856-3278-8316-02d9228b53ed | -17.75662 | -45.39841 | 2026-08-31 16:28:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a64bea1d-db0f-3e11-b93b-6bd1f377162f | -16.29979 | -44.97699 | 2026-08-31 16:28:00 | NPP-375 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b9899f97-4a07-3327-925d-e63071a0fb4b | -20.10012 | -41.9576 | 2026-08-31 16:28:00 | NPP-375 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1279234c-64d7-3ef4-bb4a-c580b5842692 | -18.26957 | -52.70579 | 2026-08-31 16:28:00 | NPP-375 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |


[Clique aqui para ver as próximas entradas](README108.md)
