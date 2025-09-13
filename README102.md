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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6732fbb2-0a12-3af0-88af-8b0491054c98 | -9.73688 | -65.0093 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b9cbaf1-cd1f-3051-9443-a73f1e28bc27 | -10.78968 | -50.53866 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e24b047d-33b8-37ae-9996-db77a44702c0 | -9.25901 | -57.06778 | 2025-09-13 05:25:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17040f5d-4cd7-3594-8313-65375e1a1efc | -9.05589 | -47.03018 | 2025-09-13 05:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a240c05-5f12-38dc-8557-a7883ccbe079 | -11.09465 | -51.43475 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0132920d-c55a-3f92-8a30-27ca1a8ad325 | -9.7971 | -61.51477 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c9c4c7a-6c74-37df-8c23-041221d5e81c | -11.21706 | -54.99236 | 2025-09-13 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9e32046-f34a-3241-905b-cecb6af014f2 | -10.76727 | -50.5221 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d274d7db-9d7c-3fcb-b7bd-f26380108747 | -11.87911 | -50.57973 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d3614e0d-0ade-3a0b-8ad2-ee39063c8704 | -9.24387 | -51.25712 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 6270c1d8-8686-3f41-9ff0-50b889402c7f | -10.39884 | -60.81102 | 2025-09-13 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 071e9398-ce35-3d94-976a-5e630d799c85 | -10.35464 | -50.50876 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 783e8447-d34d-3e71-a2f0-415343fa3afa | -10.93389 | -56.20965 | 2025-09-13 05:25:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 848f1a7c-5aba-33d6-8c0a-ef3730c69714 | -11.11864 | -51.33294 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 96883666-7291-3550-9ca2-b55f3e5dd429 | -10.02048 | -50.38934 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2249db51-d15b-3429-aadf-a25974f68789 | -9.26357 | -59.40122 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 93beb601-698a-399e-874e-ae458bba31df | -11.56885 | -50.57573 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 53ce98c6-5301-34d9-a865-29f51a028375 | 0.67773 | -50.66556 | 2025-09-13 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 66d94df0-d71f-3f1c-bca5-fe460dd50d54 | -8.27275 | -64.03893 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1588615f-50a3-33eb-8410-bbd14be1d4a9 | -11.40158 | -50.73653 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c332cdf-523a-3baa-a1e0-7ec08ed8dffb | -9.74088 | -51.01105 | 2025-09-13 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ff38cbd-dda4-343b-b5c1-002bd7b8b8c4 | -9.20023 | -60.62569 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f5cc35ac-c918-3496-b802-5c8532bd95e0 | -11.58873 | -50.56428 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 743e5598-cb2d-3e95-90e3-7d1d6f840ff7 | -12.00417 | -47.76569 | 2025-09-13 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 34de66f6-61b5-3183-b04a-bb623859cf92 | -9.26188 | -59.41239 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b6ea2a9-4a10-362f-914f-f980d3d0a4cd | -9.23677 | -51.26772 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fce76f09-fe7f-3e96-8770-fa6c485c77a9 | -11.81402 | -50.54898 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6ffc2a77-f5c3-31cc-98fd-8e4722d8a15d | -11.10559 | -51.4402 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| bc40bb73-7abb-39bc-914a-3ee11677ecaf | -10.27264 | -57.79824 | 2025-09-13 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 342d20ee-cace-330c-a6ae-46b44449f339 | -7.85691 | -61.16798 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5684e3db-a6f4-3abc-8905-0ddf7b493a59 | -11.22996 | -54.99858 | 2025-09-13 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e37fda5-5795-3261-82c5-d0589b18bf99 | -9.82231 | -54.54052 | 2025-09-13 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 438e3e68-ac8f-3191-95e6-3d28c30aa81b | -11.82013 | -50.54974 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 32066053-f47e-32f6-a9f7-ca419acfe1f8 | -9.24999 | -51.25415 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12bc727f-9f09-3bda-b9b1-7723b8a70495 | -11.09311 | -51.43215 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 58459f8f-ac9e-3d08-bae7-bdda761e26f9 | -9.52564 | -54.63189 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| ad06863b-93ee-3f75-9baa-39b2d6dfa79d | -7.90542 | -55.26657 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1598a848-f37a-3a02-9ab3-c658fb3e558e | -11.42451 | -50.7485 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0fddd9c-1590-3d9f-add9-a5366745b82e | -9.80819 | -61.50938 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40581d5f-651a-3c10-a5aa-29fa61295c0a | -9.73457 | -51.01444 | 2025-09-13 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 263ae6d6-5c3b-3bbc-b2c7-86fba6b4097a | -10.09468 | -59.1652 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d390ebde-c58e-3dc0-84a4-74e1e64629e6 | -9.70139 | -47.53434 | 2025-09-13 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e70c4ef4-2879-3cd0-96a9-59caa9fcaee6 | -9.9056 | -57.06032 | 2025-09-13 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58e478aa-398e-3d98-9a01-54edf9c94b61 | -8.27636 | -64.03954 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b135e4c6-4d69-3bf4-b9ae-4099dea5ea5a | -11.8863 | -50.57122 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 73b0e2ec-31be-3cb9-9c96-1480764518c0 | -9.55555 | -66.73097 | 2025-09-13 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 217ac0e0-755e-36c6-b181-b214e259ca17 | -10.39829 | -60.81454 | 2025-09-13 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6c88f93-ead7-3ff3-945d-e020d6be3c2a | -11.86246 | -50.56353 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 78e4ad87-0db6-3828-b6b1-543c4c8f2e14 | -9.4931 | -55.97091 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60d6d3a8-6e33-3614-9f50-9e62d5d4e88f | -11.41305 | -50.74252 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 61dc31b5-93f4-31f5-82cd-39745e0caddf | -9.21865 | -59.37966 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecbd6ebf-1616-313c-9f0a-e732ba3c97d4 | -11.11942 | -50.69785 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eda61f75-ae96-381c-aab0-4d862fb78da5 | -11.19136 | -51.41097 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 5cff1efe-e13f-3f52-bc07-3e9655b9a4fc | -11.18232 | -51.43023 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebcbacea-6ae7-30a2-ab0c-bb0b68e257fa | -11.58817 | -50.56888 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| e6887088-ecf2-3b38-a4ad-7198683ae893 | -9.96469 | -50.29493 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 373d0a75-0782-30fa-944c-311214e4a9b7 | -9.48582 | -55.99241 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a271b46-8560-3524-985a-edf07d6d63cc | -9.21807 | -59.38339 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fdff1eb-73e9-3eb0-9d7c-b5eb7ce32e04 | -9.49709 | -50.89256 | 2025-09-13 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f005b8d5-a70f-3704-8576-9b04dcb11323 | -9.23797 | -51.21391 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b985bfc3-5455-360a-947e-b198f7c7e26f | -9.91576 | -63.18607 | 2025-09-13 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f27fbb2f-a833-3a9d-924f-9fdae18c80a7 | -9.91326 | -60.21357 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0895a653-32c9-3c37-a5af-f164b188c4b3 | -7.86634 | -61.17307 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96fff191-8cff-3053-8134-f0485c354fc0 | -9.9686 | -50.30116 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 11787197-451c-320c-8777-74f548db730f | -11.11782 | -51.33049 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 006fdb09-a393-3a29-aebe-7e9482638d4a | -10.20202 | -58.22893 | 2025-09-13 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0548bf66-b381-3cf2-b480-181adf10e5c4 | -11.39452 | -50.47586 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7394167-21e2-3b5d-b8e9-70eb9f19c5e6 | -11.38342 | -47.32175 | 2025-09-13 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c346d0fd-bf0b-3f56-8b35-00d32209c934 | -10.70138 | -54.44178 | 2025-09-13 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acb7b00b-73d0-3c7b-a40c-a3628c56fef5 | -11.14991 | -50.69729 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 3d968be5-f37e-3a0d-8782-cfee2a2b3e7b | -9.03848 | -65.40376 | 2025-09-13 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ea26f00-f747-3d37-89b5-b6bbff178432 | -11.88075 | -50.56585 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b244f86e-1959-372f-b635-f81af94c7857 | -9.24314 | -51.21836 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33bdd03f-b840-31f4-931a-025c42a14946 | -9.13992 | -60.53694 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69c204c3-9616-3e6a-9177-3aa8377946a7 | -9.95282 | -51.69412 | 2025-09-13 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a44d9cb-9f5a-3782-b303-28947163b82c | -9.24628 | -51.23854 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2fa3de1-53d5-3c7b-9c5b-55e123f9c915 | -10.70601 | -54.44246 | 2025-09-13 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8661aa62-a68c-3dbf-9854-c819f8fd1df8 | -10.38138 | -50.48963 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 049d12da-0cca-378e-856b-ae7a74acf5da | -10.40606 | -60.80856 | 2025-09-13 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba43668e-5e9d-3719-a9df-ecd5c93eb232 | 0.69656 | -50.65359 | 2025-09-13 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dad20dc-dd14-33cb-9fd4-fdbc6fe9a6ec | -11.19056 | -51.41117 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 4b33ba68-3587-3545-8f7d-9e7073bbcef8 | -11.10617 | -51.33942 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd98da87-24ee-3f58-9cd4-0db9b8a88993 | -9.95971 | -50.38586 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a60aeb50-36e7-3d4d-b961-3fc02c484e68 | -9.55653 | -66.73029 | 2025-09-13 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bee23dd7-0066-350c-8694-9fe8847598a4 | -11.39509 | -50.47122 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 167b2bcb-0bef-35be-8abb-92df6eb8105d | -9.6982 | -47.53286 | 2025-09-13 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea5a7382-8208-3659-aea1-ad73e98d580e | -11.88575 | -50.57586 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e90e61e0-e548-3df0-a7eb-677510e4bbca | -9.96037 | -57.72138 | 2025-09-13 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 284ced96-5138-3e57-b188-0c5593f26a5e | -9.8093 | -61.52393 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 899af674-ad3d-3c61-9568-585e9e56a845 | -11.18383 | -51.41835 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 76b0f36f-17cb-3df3-b06e-1fd9e95a42de | -9.23775 | -51.26009 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 31b08037-2bdb-395e-995b-135962962c7b | -9.26131 | -59.4161 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61a8999b-2b04-35d1-a12e-26bc16f19d2b | -11.85582 | -50.56739 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5acdb646-62f1-3521-ab95-9cbdbf2a73f6 | -9.9713 | -50.29117 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a074703e-3a51-3a98-97ba-cf1af195669a | -4.28291 | -56.33193 | 2025-09-13 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93fe655f-5503-3ce5-a9d9-ddaf06cf1211 | -11.56277 | -50.57497 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55f258ef-d5fa-3fc0-9438-8276d522bf89 | -8.26994 | -64.05561 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bec97dfb-ab34-36a3-ae9e-95b645fb19a4 | -11.18527 | -55.09257 | 2025-09-13 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bb27fde-0f3b-3ae6-a61d-962c33112572 | -10.45972 | -50.61026 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c59bf733-1416-3e5a-b0e3-6867fdd153e0 | -9.50185 | -55.96836 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README103.md)
