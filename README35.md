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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 600b9abc-1e69-37bd-84f6-7c5ce1f230f3 | -12.08238 | -47.56728 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e3a1b4ed-25e2-385a-bdcb-7cab519f6295 | -11.67331 | -46.50772 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1de702a5-6449-3481-8e0f-57773599beaa | -11.45957 | -50.79504 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66abe678-0862-3683-8237-55a043a1f869 | -7.87995 | -49.49133 | 2025-09-14 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb738855-2508-3e85-bbd6-f9ae1e0c7ea4 | -7.57362 | -44.38161 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18fdb25a-b565-3422-a9f4-7b48f43370e3 | -12.93257 | -47.95428 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f11909c-e67d-3770-974a-70c8d1e693e6 | -11.83594 | -50.49683 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dc6e5d8b-3d23-3d24-8179-cbd00207da68 | -11.72164 | -46.9035 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0eb8500-72ff-30bb-95d1-86591c129e81 | -13.94865 | -44.80663 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffc62e03-5806-3bf2-863c-598abc0cb2df | -10.6802 | -46.25391 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6fca875-4c2d-3107-85f0-330f0c9fdba3 | -11.47552 | -50.77968 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71e16519-0173-30d4-a1af-4f7f2c104baa | -10.73607 | -46.437 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5292a7ff-6beb-32f0-8875-6adba95aab20 | -11.47937 | -50.77671 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ff4b915-0d10-3568-b803-171f8cc6a248 | -11.459 | -50.75552 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a5b5b8d4-a65c-3aaf-ad3e-fc5f70e8838e | -7.37822 | -44.3535 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aef6f98a-5b69-3761-90cf-dec342d9b29a | -10.91534 | -45.5657 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5898dfe-006a-3e83-96db-b624fba3abcf | -11.49258 | -50.77883 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64350b70-81bc-3d99-ae57-a8a3fd14a59f | -11.44799 | -50.76092 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0debedb-039a-3183-935f-a38b83b543bf | -12.81072 | -47.95618 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49ff58ab-fb23-306d-a637-1c0f2570030f | -10.41007 | -48.5977 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd608fcd-d672-3183-8cb0-5302b4dbb385 | -11.88998 | -50.54144 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3cc29207-4613-3677-8d4c-886c5c1b4bd4 | -11.39823 | -43.5225 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f883bcf-6b7b-3354-9ae4-b20a84af09bb | -11.37114 | -47.34156 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c4e9ffb-9c35-3e03-94bd-2fd678810118 | -12.14052 | -47.58281 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4fb9dc48-35a8-3937-8bfb-846e8349e87a | -11.46342 | -50.79208 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32bbc0df-50c6-3e58-8959-d476363619b2 | -10.53103 | -49.78801 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d51a070-b453-3613-9f7a-5e07f445e8f1 | -6.80368 | -51.37357 | 2025-09-14 04:40:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bbd2578-f3bd-3bca-bfb9-b18147ceb239 | -12.06926 | -45.63066 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2c649198-b12b-33c7-8355-73cc5508dd4d | -6.50978 | -52.2316 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02fc5898-1b17-37b3-af1c-47ad7e65e278 | -10.21178 | -46.75014 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25ff923c-0c73-32b2-aa48-4c1cdc77977a | -13.93704 | -44.82734 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 23587b41-f0ec-3d01-9aa7-177fe28b8fdb | -11.36387 | -47.34047 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7156ddf7-65e1-34dc-a441-659ec9c72b06 | -9.10397 | -44.81413 | 2025-09-14 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37f8d007-ec4d-323e-9f5e-7e26cfcdae90 | -9.06166 | -47.02759 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a35bef48-d38f-3457-9413-7b39606aa93b | -7.70019 | -44.68493 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ed4a296-186f-3adf-9828-3c8b0298dd62 | -11.23862 | -47.6294 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4387c386-aae6-382f-8e6a-750a099191d6 | -11.31491 | -50.82867 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d167d7cf-0e82-39d5-8ea3-d3da263e54a6 | -11.89378 | -50.54193 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d29603e1-44bb-398b-b6c3-27d08311d53e | -10.13423 | -47.18552 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37afd1e0-7c83-3eec-984d-db85a3168c55 | -12.77016 | -48.00873 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ff435ee2-dd9a-324e-a60e-ef275ad98099 | -12.74636 | -48.02195 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 43714ad4-e43f-33bb-a40a-0ab258cb3eb7 | -12.78974 | -47.99969 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 354c83a1-008d-32f1-84a3-ea68b1f11b39 | -9.52107 | -54.62502 | 2025-09-14 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5a7c5d9-d158-3069-a67f-d7fadb6b5484 | -9.62868 | -40.62229 | 2025-09-14 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 40.0 |
| c37d2518-a06c-3848-9707-0e640f0bd80d | -7.6107 | -49.60538 | 2025-09-14 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3e9176e-7455-3de4-9fd3-841e4ad22e9a | -8.94176 | -46.18775 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75962295-081e-3041-ac55-a5b461bf70ec | -11.50029 | -50.79441 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18964876-e19e-3123-ae4a-9e26bbdfc689 | -10.7068 | -48.67697 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2206800-d886-3d9f-80d5-3d419bdaf775 | -11.45572 | -50.79801 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d12960ee-de96-3bff-a522-f6a49a40e2c1 | -8.17784 | -46.77407 | 2025-09-14 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11835438-3de4-3037-89f6-46aedbb75b3c | -10.36129 | -50.48501 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 198fcf76-a6fd-31f5-a34a-c8075e7df6fc | -13.53524 | -43.00574 | 2025-09-14 04:40:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b73937c3-2533-3e11-b861-48a9476dcde0 | -13.93811 | -44.85384 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 7f491b9a-6ebc-3411-a3ce-7a24dfd2b41b | -11.49532 | -50.76134 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dff762fd-9e75-379b-a4ef-a7263b7839cb | -7.43565 | -49.57029 | 2025-09-14 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94e9d128-08e3-3317-8179-a11b87fc6b75 | -11.8737 | -46.75822 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eec05be-f5a7-3f61-8a0f-a15fcbdee6c9 | -12.7303 | -48.03219 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd7c404c-6047-3cb2-8828-6cb377d365da | -13.53455 | -43.01139 | 2025-09-14 04:40:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 07d29408-18d9-3953-abda-94be71a35fcc | -9.1179 | -46.9453 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 055fd981-a842-34e4-99ab-7c2710eab3e3 | -10.94116 | -47.23905 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de911bab-0233-345f-bac2-c61141100618 | -8.76894 | -46.04696 | 2025-09-14 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4b4667b-80f4-3b9d-9035-5233bccdf39a | -12.12631 | -44.84492 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 932d33e2-0db6-3f1a-b331-40baf532cd16 | -11.4579 | -50.76251 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61fdcee9-def9-31ae-9d4b-fb149e5334b9 | -12.78675 | -48.04512 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e540cb5b-3ddc-3f93-926f-2b7ea267aa31 | -11.13255 | -45.31571 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c512d7e4-9473-315d-9b54-fce28d836b10 | -11.25128 | -44.776 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 8be2727e-5a92-30fc-915f-c22ebb0de484 | -10.35523 | -50.48047 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6b8ef0ba-5cfa-3b2e-b9e0-836231c35e32 | -12.12526 | -44.8202 | 2025-09-14 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53066e2c-ed16-3e6a-80f8-415fc9f7d2d1 | -12.78674 | -47.99518 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c277b065-c180-3c92-8f37-e86b15441c59 | -10.66253 | -48.66982 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7720dc51-b1a7-37e6-8606-0a3ac1020b4f | -8.96089 | -44.44783 | 2025-09-14 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20aa8f42-c722-3668-83a0-19a956bd40c9 | -10.3734 | -50.49408 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07e58577-44a6-38e3-a42c-1d0567dcf250 | -7.3884 | -49.98052 | 2025-09-14 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c652af9f-f773-3e50-b796-7f7f9514ca7f | -12.7843 | -47.98688 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e2698be-a6c4-3d62-bc5a-63bb42b928d2 | -11.44801 | -50.78243 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73b4d9fd-974b-32ee-b8c1-a0feae8e4cdf | -12.72971 | -48.0363 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2828701f-d9c2-3eda-b89c-3b6081155669 | -12.4859 | -48.22347 | 2025-09-14 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d319e85-1d5d-3da4-a283-3f987138debd | -10.89931 | -45.46484 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6324a8e7-2a03-3d18-a1b6-95fac0dcf2ac | -11.47882 | -50.78021 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 567d7e5a-45b9-34f2-81b2-822e8b1c1376 | -6.67828 | -50.90206 | 2025-09-14 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ceb46eb-058e-3738-957a-5a4624e80a93 | -9.8565 | -46.47187 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7c0b4988-205e-3a5f-b09c-620c27defe29 | -11.46642 | -48.7058 | 2025-09-14 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 38b0f1df-46f7-3ef4-85ab-bdd347bb59d7 | -11.85741 | -50.48947 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e05dfe2c-dd69-3a1f-86df-2c3b5755ec15 | -12.80718 | -47.95535 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 731170bc-6d9f-321f-92a9-2c1aca4b9161 | -6.66109 | -43.51083 | 2025-09-14 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44dd7131-2bac-3268-8a15-5647425110ee | -7.52264 | -47.63827 | 2025-09-14 04:40:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66244daf-0200-312f-93c4-1d75059a1b28 | -8.94707 | -46.04646 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e3245e4-c912-3940-962d-530433a00aeb | -10.76735 | -44.77929 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d78413aa-289a-3a7c-a5cb-f5c89eac3fcb | -12.78905 | -47.97937 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3765d062-0b83-3080-9eab-ef66c124a1bf | -10.92618 | -47.1885 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8090eec2-ee62-3814-86f0-4ef88e59b9b5 | -5.76726 | -52.3541 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dd34f00-9d8d-3441-a6d3-b5d1f122f8de | -10.92132 | -45.5818 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6e0b190-0a47-386a-b079-e78dfb1f6292 | -11.44532 | -43.55936 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2e9b579-d32e-3023-ae6a-ce944fce0df1 | -11.39791 | -47.33641 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51dcfd46-fb0a-3097-aeb0-a6bfe7bcac78 | -11.46781 | -50.7641 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbd648f0-7430-3fbc-aa34-9fdf91d21665 | -8.17361 | -46.77766 | 2025-09-14 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1cd81ebe-5c80-3a85-b6a0-0bb11f90baf7 | -11.47605 | -50.75467 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 026e827e-5193-37b8-a0fc-25cea9a818b9 | -13.94416 | -44.84158 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 271.1 |
| 284d2e52-2d7e-351b-a57e-04197d4ef258 | -5.77082 | -52.35467 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dc0615c-9291-3701-84f7-1bee18f0d6a2 | -11.49864 | -50.78339 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README36.md)
