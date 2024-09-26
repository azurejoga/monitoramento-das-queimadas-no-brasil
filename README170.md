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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3c6dd6c-6b78-3e09-a4ec-547ae61ca446 | -17.09939 | -56.14113 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| eb34a917-1277-3371-ab15-0da3f5ae6050 | -17.09907 | -56.18128 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 45.8 |
| 8f50a2cd-1899-3e48-8eaf-ba160d0b38c2 | -17.099 | -56.07342 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ad658276-c830-3019-a3a1-c024448f1840 | -17.09881 | -56.14717 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 8dbd712f-c64c-330c-9a38-fa10477d735d | -17.09854 | -56.18731 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| 72b682de-89bb-375b-9de6-c794be67b7e1 | -17.09843 | -56.07953 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ed055855-e09d-3ebb-ac3e-7af4a8cf313b | -17.09824 | -56.15322 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 7a0f5503-9467-332e-8db9-ca74bba7e672 | -17.098 | -56.19335 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| ae8f6c21-584d-3dbb-8039-f0ba58815608 | -17.09766 | -56.15934 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 324b06cb-7131-3a1a-b595-1fbf0e69437f | -17.09708 | -56.16544 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 9dc44fb3-beb3-3efd-9025-34522b01af31 | -17.09651 | -56.17146 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 137.7 |
| 7ca71f2c-c395-3cfb-96b6-08315ad8bf6a | -17.09594 | -56.17748 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 137.7 |
| 18a692a5-02b1-3d47-ad32-ca91cdac371e | -17.09537 | -56.18352 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 8aa04044-4d96-3405-9343-0ef544387d9d | -17.0948 | -56.18954 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 0bf84299-d93a-3f35-98b6-5c435ea05b12 | -17.09422 | -56.19556 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| b339ac2f-0f28-33c7-a0ee-8800916e7d95 | -17.09342 | -56.06053 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7747b7c7-8d67-3f91-988d-42d7a67a8363 | -17.09326 | -56.13438 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e9007cd2-2dc6-3462-899b-0e233341e4eb | -17.09285 | -56.06663 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 73f41e4f-ac02-3aa0-8f1e-5d30707476f9 | -17.09269 | -56.14044 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 330aab0a-4612-3654-a1cd-a97b82ff29c3 | -17.09212 | -56.14652 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 0936677d-14c2-332b-b43c-716600f29ea8 | -17.09155 | -56.1526 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| be004fcb-ce83-333e-9995-cbfbd88fa2e2 | -17.09097 | -56.15872 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 4246ccd7-4a28-3d91-874c-b7603983e71c | -17.08983 | -56.17078 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 137.7 |
| cb2bc04c-2750-30cb-b08e-e8a970cdf75e | -17.08926 | -56.17676 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 137.7 |
| 1907d891-a848-3a1b-9cbc-993e6e731fba | -17.08869 | -56.18282 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 5e1d7ca4-26c3-3423-856a-815021213f9e | -17.08812 | -56.18891 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 845a4668-ee09-3f6e-acb0-bfe4cdea09ab | -17.08755 | -56.19489 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| 91513df7-4073-34d5-a261-e60678329b39 | -17.08698 | -56.20092 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| 23b7d687-3eb3-3630-b803-64faba67f6c7 | -17.08669 | -56.05986 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e28f847a-706f-3c3e-aea6-e860646bb10b | -17.08599 | -56.1398 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1cfc4690-44f5-3af5-806c-5705f5cc8883 | -17.08542 | -56.14586 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| abb55e2c-ca9a-34c1-95bf-6786992e724c | -17.08485 | -56.15197 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| be630144-ace0-3332-b22e-550d4385b8d6 | -17.08428 | -56.15805 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 75aacde1-0bf2-3b33-b327-bb2c6cb5169e | -17.08371 | -56.1641 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 2532c7ee-af02-3e63-b5fe-4d14dea277b1 | -17.08315 | -56.17008 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 6ef759be-becc-3ff0-9417-21c375db4f54 | -17.08258 | -56.17607 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 2d3b2e28-2d33-3245-bba0-cf70458f0c7f | -17.08201 | -56.18211 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| d2d6e97c-b731-3006-a6d1-f266cb625096 | -17.08144 | -56.18821 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| 076be1f4-a2ed-340f-8355-0e8032585cf0 | -17.08088 | -56.19421 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| b33ecd5c-034c-311e-a287-1d922f4e29cd | -17.08031 | -56.20026 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| d3ac9816-e5b3-3f86-9c63-ed454d8975d4 | -17.07974 | -56.20631 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.7 |
| ce2e5c68-ff3a-3dcf-9d12-c537e4b0ba31 | -17.07816 | -56.15126 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9116c0cb-e4ae-3aa1-95c1-a2e01950ffc2 | -17.07759 | -56.15733 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| a5aa0e51-ce3e-3f18-bff0-c07c97e4819f | -17.07703 | -56.16338 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 7a18727e-796a-30d0-852e-8dce9ca0e60c | -17.07647 | -56.16941 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| e24a6f59-dfa2-3cb3-95be-85409ee20ebe | -17.0759 | -56.17539 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 675a0b82-356f-34c3-b280-a2e011cc3308 | -17.07534 | -56.18142 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| 53ef763f-f741-3360-9292-a5bfe50e3392 | -17.07476 | -56.18753 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| 1038d585-ba2a-3970-b0ce-5515bcf8a057 | -17.0742 | -56.19354 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| d29345f3-013d-3f6e-80ca-7c4302ed3f74 | -17.07363 | -56.19959 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| 78793565-2454-3e24-9b56-b6d786f251f4 | -17.07034 | -56.16269 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 942477a3-8879-3f4e-b002-f8fd2958ad99 | -17.06978 | -56.16874 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 9d230730-f7e0-36d2-bee6-a3cdd113d79f | -17.06922 | -56.17473 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 7a81569d-eaeb-3141-a3ee-7c14ac92ed55 | -17.06866 | -56.18073 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 1e816080-397f-330c-adbc-56216e08c6d7 | -17.06809 | -56.18684 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 2e40caeb-43b0-3357-a159-132c3f48bdc8 | -17.06753 | -56.19288 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| f7b465ca-2e96-3d7d-bb6e-04ff3ccae733 | -17.06696 | -56.19893 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| fdf85c54-4f34-3d50-8e66-111c7d5d7b60 | -17.0631 | -56.16808 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| bb969298-ecce-3331-85a7-898637e4d442 | -17.06254 | -56.17409 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| b7611a8e-5d1e-3aab-8109-de58567bd9be | -17.06198 | -56.18006 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 1870d447-bea4-3f9c-8585-6f1a61b32e2c | -17.06142 | -56.18615 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 7e042dd4-fa98-389c-a700-b52b075abf04 | -17.06085 | -56.19221 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 51c485ea-07d2-3caf-bb5f-ea6f1af4d432 | -17.06029 | -56.19827 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 89de47e0-9666-380e-a280-6cdb2e9939a0 | -17.05474 | -56.18543 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 7e4df241-ce2f-31bb-8c9d-c70fc0b746d8 | -17.05418 | -56.19149 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 37941735-ba90-3b13-8bdc-f55ab19eb1aa | -17.05362 | -56.19757 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4818130f-94fb-3a31-a397-aac01ba15e86 | -17.04751 | -56.19083 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e2d7f0a2-f494-3913-a81c-4f91c107c3c0 | -17.04639 | -56.20291 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 76951a38-fa2e-33a0-a819-579f983e256d | -17.04083 | -56.19016 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| f89b7466-9cae-34c5-aa09-bfcf3166ba0d | -17.04028 | -56.19622 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| e5435b4f-d83d-33d3-96d0-b61e7d1dee45 | -17.03704 | -56.18776 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 25.8 |
| 025e9507-a1e0-35f6-a998-cc30f0f203ea | -17.03645 | -56.19383 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 432b9e4a-11b5-3e84-b9cf-0c015bfd976b | -17.03472 | -56.18336 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 018c6611-c1b0-305b-b227-e8ff6f245767 | -17.03416 | -56.18946 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 17d9c43f-4780-356e-9a4f-9029a184aa78 | -17.03361 | -56.19555 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 0f9486a5-1215-3499-8785-41c221a36aa2 | -17.03037 | -56.18707 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 0d3b8cf4-fc62-309b-a981-58bc2ab7a6fc | -17.02978 | -56.19317 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 266b333e-6527-3e92-a01e-4854900caf47 | -17.02749 | -56.18873 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 822f726e-76bb-3517-9274-e412bc817376 | -17.01972 | -56.20015 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| df656962-c7f2-3967-9c7e-c5df93df75a3 | -17.01918 | -56.20618 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f94e9428-3c5e-3dd7-8082-f54132697266 | -17.01586 | -56.1978 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0c5b2e76-6011-3eb6-8ddb-f3068305dac9 | -17.01527 | -56.20387 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 2aa8580a-1247-35ff-a71d-ed04e2421691 | -17.01361 | -56.19337 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3397d9f5-ab10-3da2-b365-4537e09ae4c1 | -17.01306 | -56.19945 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3c21cc16-77f9-372c-8bb0-19fc0942dac7 | -16.946 | -56.11722 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 8209b9e6-2b4f-3983-a241-76db96919ef0 | -16.94252 | -56.1173 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 2dd26fa4-21b6-3fb2-9d36-b961ed7799e2 | -16.76828 | -55.95549 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 07f42c94-c2b9-371f-9074-8e767dfab450 | -15.85084 | -57.42073 | 2024-09-26 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5dafd7cb-48cd-37de-9ebe-5b2f60a3a6af | -15.84506 | -57.41672 | 2024-09-26 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b01b8340-28c9-33d3-8b05-10dc748a5228 | -15.8447 | -57.42024 | 2024-09-26 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 205ac920-f9ee-317e-a08f-3a978f98a95a | -15.83899 | -57.41546 | 2024-09-26 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48df34cf-b438-3128-beba-ab50cd8e6476 | -15.83864 | -57.41898 | 2024-09-26 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b4ec4be-14aa-3c6f-8934-31f2f2d6cc64 | -19.14726 | -57.48155 | 2024-09-26 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 00c83b35-6ad9-3d4d-b2c7-1fa6008d3ada | -19.14094 | -57.48093 | 2024-09-26 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 412b8ac7-ebcb-39db-9c96-8076228727f9 | -19.11976 | -57.50411 | 2024-09-26 05:50:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 95288a5b-f651-385e-9de1-32f4db9e47ea | -19.11943 | -57.50776 | 2024-09-26 05:50:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 53b884bd-dd9e-3d1f-abc8-d3d4b4ebbb8a | -20.00514 | -55.49012 | 2024-09-26 05:50:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a124d1c7-d119-3e29-be98-fc5285979ef2 | -20.00455 | -55.49754 | 2024-09-26 05:50:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cded462-31d6-3927-a9f6-aef9cac905a5 | -19.98971 | -55.50348 | 2024-09-26 05:50:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d2a7977-1591-344c-adde-d600bda4c977 | -19.98927 | -55.50909 | 2024-09-26 05:50:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README171.md)
