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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57feab3e-5b27-3c72-b9d6-d5b0de7d16e2 | -5.71807 | -44.81539 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da0f5f47-a400-38af-b4cc-ce47e1a4e9fb | -5.71477 | -44.81487 | 2024-09-28 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ceb696a-c786-34da-b7fd-3e27aed21c56 | -5.66148 | -44.41858 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11088e33-3f0e-3eb4-807e-a3a1d41f661c | -5.5838 | -44.41294 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3c5693e-426b-3d39-9d9e-dd5da32e4284 | -5.5805 | -44.41242 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 029da1df-0bd5-360a-a6aa-2bdd862408dd | -5.57996 | -44.41586 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0536140-fcbd-3ac0-8fa7-9cd6248b21a1 | -5.55648 | -44.67298 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 81f416e1-e200-3285-936f-ba67e5a7d391 | -5.55594 | -44.67642 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc055274-e029-3d2d-b32c-f6444f0fb3be | -5.55318 | -44.67246 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7272d88d-1a33-356f-8d98-f9f53b9e3c1f | -5.55264 | -44.6759 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0c9dd4a-e37b-34c1-8af0-afd5c4b10e5d | -5.54988 | -44.67195 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 014ccc70-b86f-376a-9ad0-92938cf52f2f | -5.54934 | -44.67538 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd81854a-4702-347e-8264-f62fbfe93aea | -5.54658 | -44.67143 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60b766f7-4fb9-3715-958b-153ac2002727 | -5.54604 | -44.67487 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8c086ae-46c2-3112-8cef-7639a4e3db5b | -6.56224 | -43.65751 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9839f51e-439c-3f91-9554-e0a8b52ab848 | -6.51869 | -43.63279 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ffc98fc-7810-3b84-b41d-472a3ce86ad7 | -6.50591 | -43.62718 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2e3ae2c-f925-325b-8538-425831580b2d | -6.50536 | -43.63073 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5ef046e-f471-3565-870f-85f41ed52fd4 | -6.4588 | -43.64506 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae760530-20a1-377d-8701-bad7fd0e31ec | -6.45826 | -43.64858 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9becde74-5709-3107-9ec5-23cee593f33b | -6.3375 | -43.79104 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bb26520-dcc3-361a-9040-7f884b835976 | -6.33696 | -43.79454 | 2024-09-28 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7fc7315-59de-300d-bac1-3e2fe1b644fa | -6.29767 | -43.93826 | 2024-09-28 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aadd3696-afdf-3839-8e36-fd67954c8334 | -6.25214 | -43.72775 | 2024-09-28 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7bc6e0b-f599-3cfd-ab76-a44df04567e2 | -6.24082 | -43.64711 | 2024-09-28 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df256e0e-f148-3768-a456-8766ec0994fd | -6.47428 | -44.11565 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06f6dae7-b4e0-30e2-a447-6902ac3fcc04 | -6.46989 | -44.12209 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fbcce07-49b3-3f0d-bf16-6b08ebc8d6e4 | -7.04891 | -44.51131 | 2024-09-28 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 366e7bae-cae5-3e29-9c7d-e9bbae1d4e65 | -6.88179 | -44.38184 | 2024-09-28 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 777177b9-813d-31fa-b9e2-cdfdf2f84be3 | -6.79143 | -44.71759 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c318af76-2209-3c59-b845-71bb7bdcf4e9 | -6.7838 | -44.74465 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0685863-fe62-3253-addf-042f4cd84536 | -6.78326 | -44.7481 | 2024-09-28 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebf2ec36-85c8-3a5e-bb3d-72f0b3a3512d | -6.69454 | -44.5542 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9bbdaeb6-058d-3a06-b98b-98f30bddade1 | -6.64606 | -44.71256 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e254c039-4b30-3ad1-be28-f7225e7c0ee2 | -6.64276 | -44.71204 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e695c19-448c-3a08-983f-a7a1fc8a663d | -6.58267 | -44.63832 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb7876b4-affc-3d31-8239-aa3c794e8f44 | -6.58226 | -44.925 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63e7f450-1ada-3aa8-b069-01481a0a7124 | -6.56581 | -44.94361 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2900b312-dd10-397e-856e-3d72dea4ace4 | -6.56251 | -44.94309 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55407c80-2c88-33db-b8ff-42a08eb0ba1c | -6.55922 | -44.94257 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 940fcb50-a327-3fd1-b7d7-ef5dd55cb3b5 | -6.54038 | -44.28187 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c77d8f8-214c-3126-aff3-1e1150483613 | -6.53708 | -44.28136 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 227f10cb-de17-3c8e-b30f-3772c8d4f596 | -6.5167 | -44.43384 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d252b99d-a458-3465-9974-0999a9f10fb2 | -6.51616 | -44.43729 | 2024-09-28 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94e63024-a3d2-355a-a85a-c37529f2daa5 | -7.98229 | -43.91033 | 2024-09-28 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a7e296d-7143-3a6a-aaa9-5377fc2f51a0 | -7.08529 | -44.1229 | 2024-09-28 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c687fc3f-1dcf-3dfd-a87e-d046bd2fbae3 | -7.08475 | -44.12638 | 2024-09-28 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a935c7-e05f-345a-93e2-fd0482a98312 | -7.07597 | -44.1392 | 2024-09-28 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9711051a-3d43-330f-b0cf-54eceb93c1ad | -7.06658 | -44.13415 | 2024-09-28 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33f3e27a-0c02-323d-9d87-582bc7f5f0d6 | -7.06381 | -44.13015 | 2024-09-28 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fda0764-57c4-3249-adc6-78cccd35039f | -7.06023 | -44.044 | 2024-09-28 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 532984e5-bc8f-367e-b40f-6443d5500721 | -7.04994 | -43.93491 | 2024-09-28 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00e49dc8-8a4e-371b-b251-a84d74d6910e | -7.0494 | -43.9384 | 2024-09-28 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40b4f251-aa04-353f-95e8-bb63ee627088 | -7.04886 | -43.94191 | 2024-09-28 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b652ad2-6d33-3c27-b5f1-a3ada43cbd6d | -7.04723 | -43.95241 | 2024-09-28 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68e7bd3b-3dbb-31b9-bba2-857e0252deef | -7.04391 | -43.95189 | 2024-09-28 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93e5f065-a7a1-392d-b353-87d4dc195921 | -7.03047 | -43.8847 | 2024-09-28 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e3d829d-2aff-30ec-960a-b03c934d5c40 | -6.89048 | -43.86659 | 2024-09-28 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c62e381-f1ab-318e-a911-5eb9321ad46d | -6.88661 | -43.86958 | 2024-09-28 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d826559a-84b7-3491-b559-364706fad475 | -6.88607 | -43.87308 | 2024-09-28 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d1c9b4d-660b-3690-b52d-e271924980a4 | -6.63374 | -43.85508 | 2024-09-28 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a66129d-6474-3ef8-ac3c-509e40c87e7f | -6.63042 | -43.85455 | 2024-09-28 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5369d79d-c79a-39e4-b3df-abfdeb662d0c | -6.58735 | -44.17586 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 73afa41b-4757-3b24-90fe-9d1760b385c5 | -6.58682 | -44.17931 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b01c85be-712f-3159-a52a-5e32772b8aae | -6.58405 | -44.17535 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 750c86a7-8aab-3869-a03c-1989c90643ac | -6.58351 | -44.17881 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| eee9b17c-6c6a-316f-bd8f-aae3f8b52632 | -6.5802 | -44.17831 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ed671ea2-1993-33e2-bb4a-4106802724c8 | -6.57967 | -44.18177 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c28577df-7904-3dcf-b924-4d5bb4760a37 | -6.5769 | -44.1778 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3941d660-71cb-36cd-a7f0-3df537badd55 | -6.57413 | -44.17383 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 40708477-d066-3316-b87a-554c554261bc | -6.57359 | -44.1773 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 796b6834-b6c2-3efe-81b2-a5a46dcf87dd | -6.57083 | -44.17332 | 2024-09-28 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8da997b8-552c-3616-990d-fa2eed2a627f | -7.79447 | -44.66127 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c632443-3e02-3334-aaa6-6ddb8bab490a | -7.79393 | -44.66473 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9b9012de-5c27-342f-ae27-8aadf845eb9e | -7.79339 | -44.66819 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2332c923-4385-3d7e-bcad-798c0f505cb8 | -7.79117 | -44.66075 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1c481000-5521-351a-a76a-9df647c24f20 | -7.79063 | -44.66421 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d77fad88-e675-3003-9869-248ba1722d36 | -7.79009 | -44.66767 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9a86ab70-607a-322d-a124-d2ded529a6d8 | -7.78733 | -44.66369 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cc076b3-fd7a-34fa-a6f9-e1c3dc2380ef | -7.78679 | -44.66715 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ca4bf34-9f70-38c9-a199-3a3cec5accbe | -7.77998 | -44.66264 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c4e1a6f-86f6-320b-9aaa-110c78f86d51 | -7.7723 | -44.66851 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 7c63489c-2c27-356b-b466-8fec11dfc43e | -7.76954 | -44.66454 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 53c6c756-229f-3ea9-8b9f-9426809b8aca | -7.74638 | -44.63965 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 76409210-cabb-3491-93f4-1f83fa55890b | -7.74308 | -44.63913 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5c1aa0d-1e99-377e-ba9a-e7eb0b655158 | -7.58345 | -43.87007 | 2024-09-28 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5c7f3f53-f34b-364d-96d1-7255b29c96b6 | -7.57796 | -43.88363 | 2024-09-28 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da4b5da1-1dbe-3a72-9e49-dbbf1587478a | -7.57742 | -43.88715 | 2024-09-28 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27647da9-e70b-3492-801f-5cadde244595 | -7.57504 | -43.88327 | 2024-09-28 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 368be4fd-5107-31f9-b4ee-ca9a2b5444d7 | -7.5728 | -43.87571 | 2024-09-28 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f8d14ba-8962-3705-8c03-d82f1d78fa5e | -7.57225 | -43.87923 | 2024-09-28 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f1463f9-7ba3-3ef8-8119-1dba1475c634 | -7.38451 | -44.10209 | 2024-09-28 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 873c9c9c-ea38-331f-986d-704c678fad4a | -7.3669 | -44.65374 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b38d91d6-80e8-37e7-b5fb-42faeb40730e | -7.3636 | -44.65323 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32f7f24e-da44-36ae-a6b7-11d4c303086a | -7.35976 | -44.65615 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2132343a-ec20-3ed5-8dce-16eae07fe9c9 | -7.21622 | -44.08975 | 2024-09-28 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9365c289-0851-3c64-b7ac-fdd2c16cf71e | -7.89718 | -44.60997 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 310d2127-c8e1-377d-9e33-3bc95d110d76 | -7.89663 | -44.61344 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 917a5720-f387-3db4-be07-c5a87682ce16 | -7.89609 | -44.61691 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff054e87-9a59-3b85-a3f4-01d36c791b91 | -7.89555 | -44.62037 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README40.md)
