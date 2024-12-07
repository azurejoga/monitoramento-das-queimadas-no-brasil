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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 294e608b-9d6f-38b8-9d58-9d9bac6c64eb | -6.45728 | -45.75321 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dce866bd-98d5-3b83-9444-a33a85bff0ee | -8.27817 | -48.02945 | 2024-12-07 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e20ee00-7f91-35ef-bec0-321b7d8ac82c | -10.75526 | -54.78513 | 2024-12-07 04:55:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01d4abd7-6442-3b82-8020-3aefba99dbe4 | -7.08623 | -45.21374 | 2024-12-07 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af25887a-dfe0-302b-94cf-b841ecb04fbe | 2.73906 | -60.38981 | 2024-12-07 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dba9e4a1-4876-33e6-a3b8-237d4af43e59 | -7.08667 | -45.21049 | 2024-12-07 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff591cfd-74e6-3836-8add-e3a0715318e6 | 2.73862 | -60.38684 | 2024-12-07 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82e2010b-09fe-357f-aaf6-05c5c51a486c | -10.76574 | -54.78322 | 2024-12-07 04:55:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8714d497-3df8-37a3-91e2-09b2edb83b03 | -7.30938 | -55.30904 | 2024-12-07 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca4cf797-a1b0-34ac-bf63-c4a57dca0a05 | -8.93676 | -44.25304 | 2024-12-07 04:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce324938-8a3d-3a2a-9aab-41d951ad610a | -5.34855 | -46.8653 | 2024-12-07 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85e9ae14-7880-3d42-bb9c-ac839d2d3171 | -8.27435 | -48.03194 | 2024-12-07 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ef1f27d-3776-37a7-9168-f65979b411d0 | 2.60424 | -60.17005 | 2024-12-07 04:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8774ec5b-afb2-35e3-a73f-01f21be7a948 | -11.48574 | -54.03657 | 2024-12-07 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c010bd91-9075-3c97-8028-141bfd9e753b | -9.10196 | -43.19923 | 2024-12-07 04:55:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d26342e0-d459-3eff-beca-ad06f41800de | 2.73994 | -60.39576 | 2024-12-07 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 676f6282-95a1-397f-af3f-7d20d9c15aff | -6.92637 | -47.88298 | 2024-12-07 04:55:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fd359a0-3420-34ee-96d1-908336667712 | -10.04039 | -50.57807 | 2024-12-07 04:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0650cb3-71cc-36a8-b19c-38c6f80955bf | -6.41111 | -46.18945 | 2024-12-07 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd41ae7b-d7a7-3202-8412-719a09fae871 | -8.99192 | -47.42703 | 2024-12-07 04:55:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| befb125d-98c0-337a-bb36-5c192c9cafb3 | 2.422 | -60.65147 | 2024-12-07 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0f8e505-a14c-3e7e-806e-cdaceda5055d | -7.17077 | -44.99379 | 2024-12-07 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e532940-80e4-3353-8f31-80eebdb99649 | -5.97748 | -46.07716 | 2024-12-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14020a7a-7d0d-35d1-8c68-c9e2f98849a5 | -12.28596 | -45.50254 | 2024-12-07 04:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 803b44a5-7158-3af3-bc92-b9f9933f3e67 | -6.45625 | -45.75256 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea961713-83a9-3845-a5c5-e31041d9c416 | 2.42153 | -60.64841 | 2024-12-07 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 532e048a-7a2b-3f0b-ab6a-3a4db4d49d8a | -11.15348 | -49.70246 | 2024-12-07 04:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2399e056-7cd5-36d2-880d-25ead7fd486e | 2.5116 | -60.99099 | 2024-12-07 04:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a81377e-d5da-3387-8b93-0a0aa8c69eb9 | -8.93201 | -44.24416 | 2024-12-07 04:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ac2432f-a19e-3def-8369-e95a518491fe | -6.00554 | -46.40311 | 2024-12-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4f2fdcb-9c7d-31d3-882e-ae1a52a3d248 | -12.49768 | -46.35222 | 2024-12-07 04:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6739006c-5094-303b-8af0-804064086d2c | -8.27815 | -48.03697 | 2024-12-07 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62b059fb-60d3-36cd-b80c-1889ce00cf61 | -10.53237 | -49.05524 | 2024-12-07 04:55:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab52d507-a833-3248-9288-63e7715f2d3d | -10.74854 | -49.51537 | 2024-12-07 04:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8539dcd-4bc0-3c43-a9da-e794657c6e91 | -7.17032 | -44.99707 | 2024-12-07 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba3803e4-c426-3d6c-95b1-58bb200505f1 | -12.48077 | -46.27864 | 2024-12-07 04:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93ff21df-abd7-3109-8e97-84bf9d51ff57 | -8.9315 | -44.2482 | 2024-12-07 04:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cfecb15-10dc-3471-8c28-e2e02766ebc2 | -12.28642 | -45.49876 | 2024-12-07 04:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8e35d88-2ba4-37a2-951a-7957357ca50e | -6.45666 | -45.74963 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a299b796-d509-30ce-bd0e-d1421a0d5b1b | -11.87107 | -47.71118 | 2024-12-07 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0ca16e9-1e32-3b41-8a2c-2cb5a3cab3ec | -10.75581 | -54.78163 | 2024-12-07 04:55:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02ace1f4-cb9b-3df1-afbe-8c1e03074650 | -11.4149 | -51.27439 | 2024-12-07 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29d1c53c-647e-3bbc-b2bd-ec3867281992 | 2.51735 | -60.99338 | 2024-12-07 04:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43cf3001-955b-3ce4-94f1-6437803aa8f7 | -10.03654 | -50.57752 | 2024-12-07 04:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5327f7f4-ba7f-3125-a214-09b4bf0cf62b | 2.74458 | -60.392 | 2024-12-07 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a90d2b22-9da3-3164-9aba-17771b19486a | -10.5281 | -49.05464 | 2024-12-07 04:55:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 766e8ecf-778e-3296-aabe-19b233caaa99 | -11.16056 | -43.57777 | 2024-12-07 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24b88bbe-fec3-3a67-943f-ba91a882d260 | -8.27498 | -48.02761 | 2024-12-07 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbec3de7-849a-3e24-980e-c848af1ec263 | -6.83919 | -44.38514 | 2024-12-07 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d073f30d-c610-3809-83e5-c3614451e0e5 | -12.4924 | -46.35151 | 2024-12-07 04:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d86837dd-4493-38ee-a41c-189dd1587b31 | -5.50898 | -45.4884 | 2024-12-07 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f16c48cf-28c1-3a14-a9ae-2ff6e6989de8 | 2.51638 | -60.9869 | 2024-12-07 04:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48133b1e-3d46-31e2-8cdf-00506d17c5ca | -12.29156 | -45.5031 | 2024-12-07 04:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd9cc0e0-8dcf-33a1-b3d0-0c6192aff8e0 | -12.46183 | -46.93945 | 2024-12-07 04:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78b1768e-85aa-39bd-94bb-8bfed8e20f5c | -7.08711 | -45.20722 | 2024-12-07 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90a59503-dc76-35e4-8599-731ec5ffbbf9 | -6.48905 | -44.68533 | 2024-12-07 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc07a518-ac29-3b2d-b0e7-891d75b9e6c1 | -6.93289 | -42.84417 | 2024-12-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3ff66a4e-b49b-3abf-be45-c1f97b331437 | -9.2202 | -50.69296 | 2024-12-07 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1be0b1c7-8188-3218-8304-92690d409c27 | -6.45585 | -45.7555 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89a0f460-4c3a-3e7b-9d42-7ddbeee9f2f2 | -10.53666 | -49.05581 | 2024-12-07 04:55:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00c80e3e-b85d-3fa4-a0df-c658fa8808b2 | -10.65956 | -44.50175 | 2024-12-07 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 78de4931-a04e-333d-a5c3-e76c08a3d4bb | 2.51208 | -60.99424 | 2024-12-07 04:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee584817-2ecc-3ca7-b50f-a042d23b86a8 | -5.76859 | -46.55372 | 2024-12-07 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 32b08ebe-1aba-3ce7-8733-52c10581597e | -5.58221 | -45.21515 | 2024-12-07 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 373b87bf-6df7-3966-be7f-a3a3b5668091 | -5.77334 | -46.55424 | 2024-12-07 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b62ef0e-73f0-3b7a-9137-74334708576b | 2.51783 | -60.99663 | 2024-12-07 04:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb33eb1e-0322-323e-afb2-0adce294e33c | 2.7395 | -60.39278 | 2024-12-07 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21011576-b632-3da0-a72d-8ded9e8480c1 | -11.16736 | -43.57376 | 2024-12-07 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6bf7c01-bf1e-3460-b420-715fc5b449c3 | -6.44759 | -45.74895 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d951b2c-fd55-31b7-938d-47b87f9dbcf0 | -6.45079 | -45.75487 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 330f2dff-58ca-3bdf-a256-3b9ff419b7b2 | -5.92192 | -48.03157 | 2024-12-07 04:55:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d90f2cfc-a54d-36bd-aaf3-27ce8fbd9ed6 | -5.58308 | -45.20895 | 2024-12-07 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6d52e04-bcaf-3f80-bdcb-864d864882ff | -6.4516 | -45.74896 | 2024-12-07 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e945daf-2705-33ea-9092-17851031baa6 | 2.51686 | -60.99014 | 2024-12-07 04:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52b8f0ac-5122-3934-9bf5-b25964e97d17 | -13.4384 | -49.65422 | 2024-12-07 04:57:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09f89b9b-1d4c-3b50-a142-7c0075fe68dc | -15.26393 | -53.57353 | 2024-12-07 04:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2df98922-f211-3d54-ab73-982ad88920ce | -12.65161 | -46.57888 | 2024-12-07 04:57:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47a400d0-6c45-3337-980d-463a704d37f3 | -16.0126 | -51.87842 | 2024-12-07 04:57:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08ce0626-9368-3086-aad6-7278a3daf20a | -12.67671 | -58.2364 | 2024-12-07 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dd61e39-4f77-37fd-a2a9-d5246aca90a3 | -15.08716 | -59.62569 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05d49570-5544-330c-a4b7-e573d1d2799d | -15.0987 | -59.64621 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe481cda-784f-34b9-bfc2-c4ac5cb1d072 | -16.19788 | -48.22374 | 2024-12-07 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8690b462-6e62-3757-9d30-0ec2f6e22723 | -12.65636 | -46.57676 | 2024-12-07 04:57:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee6c7354-ff61-35a8-b306-b497ca45daca | -15.26161 | -53.56496 | 2024-12-07 04:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cbedc32c-745c-34e5-bd95-6fc7efe3c67a | -15.08927 | -59.63525 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2aacd00b-5dcd-32b0-8a52-edeb4d8fa59a | -11.73503 | -54.3102 | 2024-12-07 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5d8cedb1-cd73-3beb-89a1-a7bc596cc651 | -15.15712 | -56.48151 | 2024-12-07 04:57:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dbd0353-4675-3bb7-8461-064aed89c526 | -12.68023 | -58.23703 | 2024-12-07 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91ade71f-b966-3a02-9071-f9529cb040f9 | -12.86441 | -51.93548 | 2024-12-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83627bdb-c7c6-313a-9657-6fea24ad00ea | -15.15456 | -56.47729 | 2024-12-07 04:57:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b364ca1-a274-3eb8-83cb-80477c24dd64 | -12.86008 | -51.9394 | 2024-12-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fda6828a-c067-310a-9e1e-84c5bc9d46ab | -17.56292 | -48.01089 | 2024-12-07 04:57:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4b1f92f-3a0f-3225-a4dc-2757072d3d9c | -12.68241 | -58.24578 | 2024-12-07 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82e514cf-7281-3695-baa8-534f893bc5c9 | -16.01191 | -51.88344 | 2024-12-07 04:57:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24cc081b-6640-3ffc-9008-407bb6e49256 | -12.67738 | -58.23236 | 2024-12-07 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a157ee57-a202-3ea3-bc31-54ede320d83f | -14.7691 | -50.5312 | 2024-12-07 04:57:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a0b2e88-b619-363a-9dbe-c1c841cfa1b2 | -12.65721 | -46.57634 | 2024-12-07 04:57:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75350dd6-9053-3f26-b99f-afeae8893fa9 | -12.54062 | -57.74292 | 2024-12-07 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5f66ee3-18cd-3a7a-b67e-98830c4ea608 | -15.25751 | -53.56849 | 2024-12-07 04:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b853689d-d690-3dcb-b35a-e87101a426cf | -12.65595 | -46.57995 | 2024-12-07 04:57:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README11.md)
