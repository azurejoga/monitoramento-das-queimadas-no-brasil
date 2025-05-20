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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 137ceeae-0b60-3254-8a96-1c85dd4449d2 | -20.22161 | -50.7529 | 2025-05-20 03:45:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c3d6b38e-c005-36bf-84d6-8fb36945f6a5 | -21.19767 | -48.48868 | 2025-05-20 03:45:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52960dae-6c4f-3b56-8be6-a3b15f2e7489 | -17.05926 | -45.03069 | 2025-05-20 03:45:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2d849cb-0f76-30dd-9a5d-5873843f958e | -19.1561 | -47.81931 | 2025-05-20 03:45:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f944e290-0051-38cd-ad71-34672964f180 | -21.21999 | -48.60598 | 2025-05-20 03:45:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| e5ad6fc7-bacf-3030-ac0e-f491e45712df | -19.53093 | -43.92139 | 2025-05-20 03:45:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1b1907a-fcb3-3a55-8787-237cec9fd945 | -19.1546 | -47.81764 | 2025-05-20 03:45:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc7de91f-a697-3069-afd5-2ea56fb81a6c | -19.15687 | -47.81561 | 2025-05-20 03:45:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 214ccb66-7038-3978-9c27-ccbfc4de05a8 | -21.21918 | -48.60966 | 2025-05-20 03:45:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 2d86466a-9ad7-3fd4-b3c3-8d0b372d0e76 | -15.89368 | -46.0084 | 2025-05-20 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 832f4d35-6770-3d4a-97a6-243af9054dc9 | -20.21661 | -50.75387 | 2025-05-20 03:45:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec469058-e772-3731-a445-655bddd959e1 | -22.67786 | -42.85488 | 2025-05-20 03:45:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| df3c034c-a654-3c82-82e6-f0eef64b069f | -21.21837 | -48.61337 | 2025-05-20 03:45:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| d9e42ed1-1477-3cac-90ad-2ef51be24649 | -19.72719 | -42.01664 | 2025-05-20 03:45:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 973cf7f7-1e63-30b1-b45a-d05f0c233127 | -19.16057 | -47.81565 | 2025-05-20 03:45:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 804ff603-2f48-307a-a1ee-614d752972bc | -15.27377 | -43.07485 | 2025-05-20 03:45:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 88166dd8-a29a-3075-adce-4a38591541c5 | -17.77737 | -42.80642 | 2025-05-20 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af71e3f9-c785-3769-8cf5-c5c600a22785 | -19.45364 | -45.30655 | 2025-05-20 03:45:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ea6bae0-0549-3d0f-a0de-bee009c9376f | -17.50272 | -46.73655 | 2025-05-20 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b5c690c8-f6e6-3af8-b404-cf323f6c6d7a | -17.50208 | -46.7397 | 2025-05-20 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7d10ab06-f25e-3681-beb6-d0f7427994ed | -17.50144 | -46.74286 | 2025-05-20 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fe2800a8-2de6-33aa-909d-f935bd3087b3 | -17.80065 | -44.34007 | 2025-05-20 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9306bb4-3f23-320c-b5fe-ce152f6c54d3 | -20.76294 | -46.77074 | 2025-05-20 03:45:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 257d15d4-5495-35d9-a4a4-e2ef188695e7 | -15.26958 | -43.07396 | 2025-05-20 03:45:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a0c35220-a730-38d5-96ee-a2771155c1dd | -19.15976 | -47.81942 | 2025-05-20 03:45:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1119b9c4-3620-3942-9bd1-e6e5e3f37621 | -15.27722 | -43.07977 | 2025-05-20 03:45:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 11.0 |
| c3b8ed7f-4284-3e1d-86eb-4ede5a59423d | -19.71815 | -40.35285 | 2025-05-20 03:45:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5f143da9-2825-348c-b688-35023c1b9256 | -20.34587 | -40.36182 | 2025-05-20 03:45:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 55997f64-c8f8-3885-882a-90b31e28d8df | -20.53852 | -47.30286 | 2025-05-20 03:45:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4196ebfa-963f-33d9-8457-c853f8da7ad1 | -16.66909 | -44.55397 | 2025-05-20 03:45:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 723d7ee4-e216-3751-b5e2-3b73480fb53c | -21.47022 | -41.58081 | 2025-05-20 03:45:00 | NOAA-20 | CARDOSO MOREIRA | RIO DE JANEIRO | Brasil | 3301157 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 43799446-c313-3e8d-b131-ad8e33fd5488 | -17.06025 | -45.02563 | 2025-05-20 03:45:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f13d1f8-7f67-3f8a-852f-0c6c493e21e0 | -20.22276 | -50.7554 | 2025-05-20 03:45:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aecc9369-8939-37ec-b881-08dc5a935b42 | -17.86388 | -43.76286 | 2025-05-20 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4fbda44-c014-3d72-8643-3fb003bad909 | -17.80413 | -44.34549 | 2025-05-20 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbca6b65-b67b-3c75-b46b-b564081df8f9 | -22.34305 | -41.78507 | 2025-05-20 03:45:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 72d9d685-dbd9-38c2-a934-2802fc543a26 | -20.34929 | -40.36248 | 2025-05-20 03:45:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fda00577-75af-3cea-99b0-8b935f10731d | -17.86463 | -43.75884 | 2025-05-20 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab165db5-2d3a-3b4e-a2de-4aab6723ba73 | -21.24463 | -49.26968 | 2025-05-20 03:45:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0ed27848-d81d-3855-99bd-1cbe96ecef61 | -22.7849 | -43.75496 | 2025-05-20 03:45:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f02141a6-af83-3e5c-85a3-d2f4ee469759 | -17.79981 | -44.34442 | 2025-05-20 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 201cd6cd-331d-37a7-881e-7d5a2496167d | -19.43704 | -44.34063 | 2025-05-20 03:45:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 976f98d4-c674-3f2b-9227-ce433c4184b7 | -17.67546 | -42.74537 | 2025-05-20 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57bbc738-2ce6-3261-80df-43bfc7a7406e | -17.50718 | -46.74085 | 2025-05-20 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 897ff93a-a9da-3ca3-a513-e44ece4a2536 | -21.24628 | -49.27021 | 2025-05-20 03:45:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d3551cc1-2c32-3944-a23f-4dfffa90b25b | -22.53837 | -48.81292 | 2025-05-20 03:47:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a886df82-6909-37df-9394-3cb5d80aecc9 | -22.53977 | -48.81366 | 2025-05-20 03:47:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bd888a4-e60a-3039-9b3e-9c07f3a769ce | -23.60495 | -49.00955 | 2025-05-20 03:47:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fd8904c-eb5a-3e16-baaf-9da54cb6d75d | -25.19264 | -49.32833 | 2025-05-20 03:47:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| be42ecb5-2c7d-3ff1-a4a6-82ec87d71555 | -25.19921 | -49.3233 | 2025-05-20 03:47:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 036a2380-3060-3d6a-958b-49b371120ee4 | -25.18747 | -49.32725 | 2025-05-20 03:47:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3cb1be39-564f-31e7-9fe3-f22686bb880b | -23.98161 | -48.91665 | 2025-05-20 03:47:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f69f934e-ed67-38a1-a077-f1d79c432829 | -23.98673 | -48.91794 | 2025-05-20 03:47:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95c976e9-6a6e-35f0-956d-779de989a204 | -23.61015 | -49.01084 | 2025-05-20 03:47:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9e2cdb4-8a01-3e46-89ab-ab2c8a98770d | -27.11532 | -50.57634 | 2025-05-20 03:47:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 61de02bb-ddc6-3fab-88ff-82eda31b31c3 | -23.33966 | -46.77464 | 2025-05-20 03:47:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 91f0067f-63c3-31e4-968a-f6efe1cc2d88 | -22.9019 | -43.75624 | 2025-05-20 03:47:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 44d5813b-78a0-3583-8d3f-e52f90071714 | -23.60414 | -49.01314 | 2025-05-20 03:47:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 347a07c7-7720-3b6d-a0d2-cbba75a10331 | -7.06805 | -44.93085 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7644d7b6-9a9c-3b6e-a0aa-a43e73e7ba32 | -6.23111 | -43.36139 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86d66be7-48ee-33bf-add6-22401bf32711 | -9.43666 | -40.37778 | 2025-05-20 04:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8491f31c-3f70-36fd-be46-9983946e0025 | -7.06985 | -44.9185 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2aedd3e6-c9cd-34f4-a4fe-dbb6a44db3ec | -7.07163 | -44.93146 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed062e75-321a-3e1d-85be-8f33bf1cf0ef | -6.20666 | -43.32991 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1243a2c6-3be0-3a9a-af48-be222a7efa7c | -7.06978 | -44.92866 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d58b58db-c4dd-3b4e-a349-5e54bd0468e9 | -6.20739 | -43.32501 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9078b54a-b6a5-35e5-8a8e-d8f5abe57b91 | -5.76491 | -43.48699 | 2025-05-20 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23189800-6cdd-3045-a12c-195ee6e4af02 | -6.5563 | -44.48884 | 2025-05-20 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d249e91e-b354-3a91-993a-5663afa55715 | -5.97894 | -43.76457 | 2025-05-20 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c5873f2-cc40-3eed-b38d-bc06942ae43e | -6.20594 | -43.33474 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8b9b9c4d-5b2b-3bbe-a4e0-e209d1709473 | -6.2304 | -43.36629 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07bde73b-778b-3038-9cf9-bb6a19f12857 | -7.60512 | -46.64022 | 2025-05-20 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e547d09d-908b-39cc-a404-26be3709d53d | -5.97962 | -43.75994 | 2025-05-20 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c033c8e3-02ac-375a-a87f-3d3cb23b2026 | -8.16348 | -46.49747 | 2025-05-20 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94ab4a96-154d-365d-bcc9-d013c20f322a | -6.96121 | -55.28024 | 2025-05-20 04:32:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58e47f00-1545-30b4-94c5-1f912a55c49f | -6.95655 | -55.27943 | 2025-05-20 04:32:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad0418f0-73a7-383c-8493-79107d298922 | -6.23182 | -43.35647 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 14e8f404-808a-3d4f-9ef5-b1abec3b9a80 | -4.25171 | -48.21179 | 2025-05-20 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8602df9b-3fe3-3203-ae80-9099cef0b707 | -6.22697 | -43.35325 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 52ca6c16-4556-3896-b36d-8a1f7a9d36ff | -6.31892 | -43.74324 | 2025-05-20 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4d64419-753f-34a8-bcc6-ee4d905f4634 | -7.06916 | -44.93274 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1df9532d-534b-3eb5-b063-f29de33f7c1e | -5.97139 | -43.76344 | 2025-05-20 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f7868cb1-9e6d-3451-af95-0374ef6f3b81 | -5.96829 | -43.75824 | 2025-05-20 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c60ffea5-95c0-3943-9381-2195dc375516 | -7.06808 | -44.9157 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54e08a35-2822-366f-9346-e67084d05978 | -5.76682 | -43.49383 | 2025-05-20 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af98765b-45eb-3055-b835-9040e893a625 | -6.23571 | -43.357 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 79c29acb-cc3f-3fcf-9657-605e1ffd8d64 | -6.83332 | -45.36708 | 2025-05-20 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ef89442-3de9-3c2b-a4e9-6ba1b15c3e33 | -8.16293 | -46.50113 | 2025-05-20 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d3bbc85-692c-3430-9e2d-7a9372effd04 | -5.75918 | -43.49259 | 2025-05-20 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf3b9401-8bd8-3cb7-b1c9-ad2dac15796e | -3.42239 | -43.16531 | 2025-05-20 04:32:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7cfe205-e221-3606-bfba-591ee089ef47 | -7.06386 | -44.91925 | 2025-05-20 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 944a2734-4c3c-3a72-8daa-4320d33d0086 | -6.3227 | -43.74392 | 2025-05-20 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70ce182e-7141-3396-8e43-092434985e8f | -6.29766 | -43.64939 | 2025-05-20 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab522e1b-a91d-334c-b040-af8b7b52d26f | -5.97585 | -43.75936 | 2025-05-20 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f79c66fe-8ee9-3f1c-ba05-9ec594b61949 | -6.235 | -43.36191 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0a4ecf40-7360-3678-acf3-b57264b0695e | -8.0748 | -47.12653 | 2025-05-20 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41950e9f-07da-3975-bf17-83156f82237e | -5.89065 | -45.54863 | 2025-05-20 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 894d19cf-ae95-3034-91ea-d196ff0f398a | -9.44254 | -40.37856 | 2025-05-20 04:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bb3be732-5620-35b7-a319-3f7c0e818141 | -6.66279 | -47.37295 | 2025-05-20 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c94a02c-06da-3e40-9a06-a3f9d286f695 | -5.78394 | -43.6165 | 2025-05-20 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
