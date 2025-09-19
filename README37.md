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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73094788-1398-3810-bdd5-a11fd0a85fa1 | -9.18112 | -45.32055 | 2025-09-19 05:44:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 138258ec-c6ae-3a9d-9857-215047ed86eb | -12.14745 | -44.95803 | 2025-09-19 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cbe5ec18-503a-3afb-bae9-698403a10c7e | -6.90863 | -44.76476 | 2025-09-19 05:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b5da0f58-13c0-3fb9-acd4-6b6d24a43e7d | -8.13717 | -46.78601 | 2025-09-19 05:44:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ac6e371d-6002-36f7-b3a7-0dbccfe8f759 | -8.05698 | -44.09278 | 2025-09-19 05:44:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9efd54d9-0481-3f7e-b05d-7286c5a4d574 | -8.01519 | -45.74095 | 2025-09-19 05:44:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cac26aac-b024-33a2-a3b5-fa592e90d38e | -6.91197 | -44.80326 | 2025-09-19 05:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cce98f8f-f8ae-34e8-8737-57ccd436c265 | -10.2956 | -50.2231 | 2025-09-19 05:44:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 07f5dce9-240c-302f-94cb-34f9d94001aa | -7.32587 | -44.57253 | 2025-09-19 05:44:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6986a0ba-2862-34a9-b69d-3736c5101379 | -6.82891 | -41.0348 | 2025-09-19 05:44:00 | AQUA_M-M | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 8a8371fe-0ca5-3869-8e2c-27d9ee26e57b | -12.10216 | -44.84114 | 2025-09-19 05:44:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5028b4b8-dc4d-36d5-a3ae-10d213fd4d61 | -11.08579 | -41.07053 | 2025-09-19 05:44:00 | AQUA_M-M | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 08d55a6c-435e-3c49-ac59-07ddedd736eb | -7.57516 | -45.47263 | 2025-09-19 05:44:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 147013b1-1a2e-3fac-80f7-a0e15ef54757 | -8.4852 | -44.72747 | 2025-09-19 05:44:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5779c679-831a-3f54-817c-8ec67111bee0 | -6.90723 | -44.77393 | 2025-09-19 05:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 3fa4ed14-12d0-34c0-9398-4162e773ded1 | -5.80308 | -43.64034 | 2025-09-19 05:44:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e2f15ba-c14c-3f8b-850e-fa5e5ce2d809 | -9.18256 | -45.31127 | 2025-09-19 05:44:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| ed43f4a1-28b4-35df-ac22-37be983d9b6f | -11.08739 | -41.05885 | 2025-09-19 05:44:00 | AQUA_M-M | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 754de334-46a4-3005-b5ef-4b9e75c5f088 | -9.51346 | -43.06143 | 2025-09-19 05:44:00 | AQUA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| b4002d40-73e6-3887-a128-43f27b417ed0 | -9.72411 | -45.92504 | 2025-09-19 05:44:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 95f3bbdf-cefa-3b20-8204-352006132b9d | -9.17213 | -45.31917 | 2025-09-19 05:44:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d48d96e6-1787-3d23-884d-ee3a1ae40329 | -12.09119 | -44.8419 | 2025-09-19 05:44:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d40cc8a9-5288-3aa3-b6ef-e00f4fac1c96 | -12.09794 | -44.79714 | 2025-09-19 05:44:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a54ebbeb-8ab0-31df-81cc-5c8b64927f13 | -6.93873 | -44.74791 | 2025-09-19 05:44:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7020d316-e4a1-3b1d-990d-2f9e36af25da | -7.32724 | -44.56351 | 2025-09-19 05:44:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 275c54e6-ab2b-3b29-a076-28e013210c9c | -7.28495 | -43.93084 | 2025-09-19 05:44:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2a2f4b4e-7549-3782-8852-116548fa4bbf | -5.91712 | -45.0821 | 2025-09-19 05:44:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e5049b2a-3b66-3aaa-b9b2-b7b5b49da335 | -21.28398 | -48.79515 | 2025-09-19 05:46:00 | AQUA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 40a8df11-6955-30d7-9e69-03092993da07 | -20.79376 | -47.23198 | 2025-09-19 05:46:00 | AQUA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b25bdff3-eec5-3c7a-b194-e46f80f897d7 | -22.34304 | -46.76402 | 2025-09-19 05:46:00 | AQUA_M-M | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 49438831-6173-3194-a887-df7bc70ecd40 | -20.21024 | -44.60646 | 2025-09-19 05:46:00 | AQUA_M-M | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| fccc6d49-28ce-3bfa-a893-9ff6331f0372 | -19.12031 | -46.62267 | 2025-09-19 05:46:00 | AQUA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 02182fa1-b8a3-3fab-a3f3-1d8de125f063 | -17.16038 | -44.78523 | 2025-09-19 05:46:00 | AQUA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 27605814-2165-3959-9246-608a78efb005 | -17.22793 | -45.95494 | 2025-09-19 05:46:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dc9c0ca7-34d3-3750-a625-c7b2862278ab | -17.09091 | -43.3384 | 2025-09-19 05:46:00 | AQUA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 734b1969-9053-36c4-85be-8019aa54ff0d | -20.42635 | -46.47902 | 2025-09-19 05:46:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4ae6a6f4-2fd4-3268-9696-b1026628c25b | -17.08294 | -43.32664 | 2025-09-19 05:46:00 | AQUA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 022bd2c8-96bd-3435-bf2e-301edbb83c4c | -22.33239 | -46.76527 | 2025-09-19 05:46:00 | AQUA_M-M | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 315fda2d-7761-32c5-9acd-bef4e23a9700 | -22.75333 | -51.39737 | 2025-09-19 05:46:00 | AQUA_M-M | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| f58b029a-bfac-3fd5-bc1b-f75bf4acf8cd | -21.12177 | -45.71853 | 2025-09-19 05:46:00 | AQUA_M-M | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.5 |
| cb1cb940-5be8-3824-b9b7-a1b294ccf8f6 | -21.28504 | -54.80482 | 2025-09-19 05:46:00 | AQUA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 21.9 |
| cbb51c2a-79e9-3eb2-abd3-ec01dc195ce6 | -24.14721 | -53.05045 | 2025-09-19 05:48:00 | AQUA_M-M | GOIOERÊ | PARANÁ | Brasil | 4108601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 25399e53-68b1-3a56-aa03-6790e7532330 | -9.41797 | -68.87268 | 2025-09-19 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80a735a0-3f54-3369-a20e-b76a7ecf6efd | -9.423 | -68.87339 | 2025-09-19 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ba15cd9-0b3a-3372-8441-897238b32a60 | -9.42255 | -68.87325 | 2025-09-19 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2161b320-20e3-338b-aa46-f0f97bd849db | -9.41752 | -68.87253 | 2025-09-19 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65888e43-bff6-390e-88ed-d9fa2d4da382 | -9.41758 | -68.87558 | 2025-09-19 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8558eab-2541-3bfb-bf8c-dcc7f4186874 | -21.2831 | -54.813 | 2025-09-19 06:40:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 88db2248-eec6-3817-8ca8-ff1df1c8046d | -10.2982 | -50.2158 | 2025-09-19 07:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2432b7e7-7ef9-361e-b26c-57e375e7398a | -10.2793 | -50.2177 | 2025-09-19 07:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 81518531-704f-3b8a-8e9c-eb7f8eb01631 | -10.2793 | -50.2177 | 2025-09-19 07:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 5734a1f2-7b6b-361a-947a-63fd2ffc8cbc | -9.46781 | -67.05472 | 2025-09-19 07:22:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d1d9ce43-c0b7-3812-80ae-1b44f7ff857d | -22.2048 | -52.3369 | 2025-09-19 07:40:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.9 |
| 86cb666b-4dc5-3cec-918f-466aa6a7a9b3 | -22.184 | -52.3412 | 2025-09-19 07:40:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 9e75bd20-4056-3843-a88b-4413cbc235b2 | -22.2048 | -52.3369 | 2025-09-19 07:50:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 140.7 |
| b01d9fe4-5952-3a15-9caf-2345422abc20 | -22.184 | -52.3412 | 2025-09-19 07:50:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 238.3 |
| 67a512be-86fa-312b-a3a1-d3ab51ba161d | -22.1835 | -52.3636 | 2025-09-19 07:50:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.1 |
| ca978d32-80b6-3043-b422-4d1a06c60a63 | -22.184 | -52.3412 | 2025-09-19 08:00:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| cd847320-0867-3e75-b2ec-6cbeb54f4152 | -22.184 | -52.3412 | 2025-09-19 08:10:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| c4ccc246-dc05-30f6-9d2d-1a255e935980 | -7.7148 | -44.392 | 2025-09-19 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 66429654-a2ed-3c4c-bbd7-d550478a2afc | -7.7148 | -44.392 | 2025-09-19 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 141.1 |
| fb04a341-c4fe-39f1-b322-669104b14665 | -7.7148 | -44.392 | 2025-09-19 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| eda3465a-5d5f-3409-baae-0a6f03e784f0 | -6.06 | -42.7025 | 2025-09-19 11:40:00 | GOES-19 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 43d3c788-bdb9-3476-86ec-31144e791c7a | -7.7148 | -44.392 | 2025-09-19 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| db78b573-c657-3506-9b93-d4facaca8314 | -9.0097 | -46.3264 | 2025-09-19 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 83e602a1-8ece-3d79-b884-d9d52338d5c9 | -9.0097 | -46.3264 | 2025-09-19 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 62a9fae0-9788-3add-87ac-dc90b3a410b2 | -7.7148 | -44.392 | 2025-09-19 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 673d1468-21d1-3c33-9572-e086e9571095 | -7.7148 | -44.392 | 2025-09-19 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e0ddc1cd-90d1-3469-8ecc-2a88633b5b8e | -7.1878 | -44.4193 | 2025-09-19 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 565ca452-884d-348a-92ff-5e570cf8f5f5 | -3.15856 | -43.26304 | 2025-09-19 12:14:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 2b65db4d-8963-3241-a5b3-16adeac289f9 | -3.16007 | -43.25253 | 2025-09-19 12:14:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d4211c64-01cc-3dec-9a61-ba01d9b027aa | -3.41423 | -42.98906 | 2025-09-19 12:14:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b3cdf85a-57a2-32f7-8946-ab9e6e16292e | -3.06477 | -42.41417 | 2025-09-19 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 956cc5af-e4b6-39c3-ade5-c61febbc9c1a | -3.41271 | -43.0 | 2025-09-19 12:14:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 33e722ab-b71f-3dee-b9f2-3ddfa679b676 | -3.42205 | -43.28517 | 2025-09-19 12:14:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f4ce78c0-abdb-3d3b-b448-8341cc8edab7 | -3.07489 | -42.41558 | 2025-09-19 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6058a216-384c-3400-9ac0-38ccc4da8ed7 | -7.71811 | -44.40611 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 4ade8f10-ec17-35a2-912e-2af8c93b44a1 | -7.63927 | -44.45161 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8055dca0-315d-38f8-9361-2b117f22c8c9 | -9.52027 | -48.14462 | 2025-09-19 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 70aa3f44-bdf6-3b39-8c67-8dfefd8a700e | -8.38183 | -44.68464 | 2025-09-19 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 25793e80-b75c-3c4a-b1b9-ae581c404261 | -8.61606 | -45.7073 | 2025-09-19 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6a9f8085-a983-34fc-b982-b8462a1fab4d | -6.04959 | -46.64052 | 2025-09-19 12:17:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dad9a39a-de97-3b11-9ac2-a2adb4984ebc | -9.72787 | -45.92369 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 04a75ab7-d901-30aa-a112-f1e5adb902eb | -5.9229 | -45.07365 | 2025-09-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c877f973-3651-3c4a-b146-2f6e06f2e351 | -10.02666 | -47.19761 | 2025-09-19 12:17:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 3b5179fe-4915-3525-bd57-9785476dd771 | -8.798 | -46.05151 | 2025-09-19 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4920ecb1-15df-3bfd-8887-37a2e36705bb | -5.79922 | -45.35929 | 2025-09-19 12:17:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 05010b77-0812-3769-ab16-5a271fc84d36 | -9.04373 | -44.8763 | 2025-09-19 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ef0d4115-886a-3ef5-baf1-43ae73b50814 | -8.03023 | -44.9537 | 2025-09-19 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 11a88124-057a-369c-8e09-ed3d5a864d48 | -9.00915 | -46.32147 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 7dc125bd-06e9-3238-8ecc-7d14edb86c89 | -9.78245 | -46.97144 | 2025-09-19 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| d541aac8-3b68-3528-96d2-13cf64a731ba | -7.99561 | -43.93509 | 2025-09-19 12:17:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3444f520-7d31-383d-ac2f-1234b7677abe | -6.33405 | -42.39262 | 2025-09-19 12:17:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 661255e9-74a7-39ee-9b90-78bda66bdf9c | -10.61084 | -46.45752 | 2025-09-19 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b8f513b5-a9bc-39f9-a468-e3c748d7250a | -7.30255 | -45.15647 | 2025-09-19 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3d11cd57-92f8-3bce-9851-1295399b9e66 | -8.48576 | -44.73667 | 2025-09-19 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a8398e50-967c-3421-be73-80f97d60fd21 | -7.56264 | -44.75206 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a3bfb5f8-20aa-3699-9666-0b77e487822a | -6.91529 | -44.77009 | 2025-09-19 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 4438b416-f054-3c1e-97d4-5ca71d26e85a | -6.90605 | -44.76885 | 2025-09-19 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d0364313-d4bd-3cb9-bb87-1e3c80d2db79 | -8.90672 | -46.12841 | 2025-09-19 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |


[Clique aqui para ver as próximas entradas](README38.md)
