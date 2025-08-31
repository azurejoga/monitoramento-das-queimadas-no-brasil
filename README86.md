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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db4adcbf-378e-3040-9ae5-4e11712f3bde | -12.6298 | -48.1979 | 2025-08-31 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 331.8 |
| 4be7ddb9-75ec-36a3-9e8a-3d3133212f84 | -11.8373 | -46.4287 | 2025-08-31 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| f6fffdb6-6705-3f4d-9215-fb2eba5fa62b | -5.4824 | -44.3969 | 2025-08-31 12:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a31c5a79-a947-36fe-a33b-fcc97ef74f11 | -11.3509 | -43.6133 | 2025-08-31 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 4c8273fe-c7e9-38e0-afcd-c494ede9e8c5 | -11.3509 | -43.6133 | 2025-08-31 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 6b83d471-7108-3680-87e0-effdfeee0adb | -7.8541 | -46.9747 | 2025-08-31 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 253.7 |
| 9fff0233-9abf-3bc2-b6f0-67dd9629286c | -16.2221 | -52.6778 | 2025-08-31 12:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 1ed347d9-1ac0-38ae-806e-5ec976b5b573 | -11.3504 | -43.637 | 2025-08-31 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 59a41193-a407-30ca-a3d8-1f638b71be9f | -16.2417 | -52.675 | 2025-08-31 12:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 7cf27145-6435-34da-9397-ba62d1c446ae | -5.4824 | -44.3969 | 2025-08-31 12:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ac659e29-0989-3837-8f68-2969d47c1e6c | -4.7346 | -44.4457 | 2025-08-31 12:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 327.7 |
| bbd8751d-68f0-3552-9006-cad39084a9f9 | -16.2217 | -52.6992 | 2025-08-31 12:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 201.2 |
| a8efbbe2-540b-3f0c-94e0-c01c353a1593 | -11.3112 | -43.69 | 2025-08-31 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| e6e021fa-5c17-36b4-8c33-5089a96da6f7 | -11.0288 | -46.8745 | 2025-08-31 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 253a5808-07aa-3b6b-bf11-c7d4dca2abb7 | -9.6865 | -47.9409 | 2025-08-31 12:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 65eb83ca-42be-385b-9644-b0fec544c874 | -11.3312 | -43.6399 | 2025-08-31 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 34b2ec07-9b14-3da8-8920-5cad31d8d806 | -15.7102 | -48.9479 | 2025-08-31 12:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| ec5d587e-e37b-3f0b-bed9-eff499c46207 | -11.3304 | -43.6871 | 2025-08-31 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| c7d6faf0-6241-3c37-8d41-e33a64675a3f | -9.2642 | -47.0582 | 2025-08-31 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b830944c-6ea9-310f-9e7e-10254ea18b6b | -15.7098 | -48.9702 | 2025-08-31 12:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7028b71c-ca19-347e-88fa-4e4284d942be | -15.7107 | -48.9255 | 2025-08-31 12:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 0cb3d81c-218e-36de-9a90-6f979a79aeea | -11.8181 | -46.4314 | 2025-08-31 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 24a66b5a-1f19-36ab-89f2-48a5ffbe807b | -14.0508 | -44.5543 | 2025-08-31 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| d29c73ed-fd39-3f04-8e50-fae6ad0f15f5 | -11.3308 | -43.6635 | 2025-08-31 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 247.3 |
| 9c749fdd-d855-3f95-b3fe-6ee1f460f527 | -11.3701 | -43.6104 | 2025-08-31 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 9168d2e0-e1c9-3765-a348-50b96f4898ec | -12.6298 | -48.1979 | 2025-08-31 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 1cdd14c9-a241-386e-ba08-a11851def91b | -11.3705 | -43.5868 | 2025-08-31 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 04d6b6b4-e3d9-3dcd-9e9d-a4fcfa425864 | -7.8543 | -46.9525 | 2025-08-31 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 368.9 |
| 730eb44e-2fe9-355d-8608-f48041b2b228 | -5.8696 | -42.9768 | 2025-08-31 12:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| de303d22-253d-3d8f-976c-ab45cbb43b08 | -9.245 | -47.0824 | 2025-08-31 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 0d454469-77f2-3c62-a994-ceee0fcbfa82 | -12.6294 | -48.2201 | 2025-08-31 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| c7a1692a-2d0a-3be4-9e5c-7044d085762b | -7.1957 | -45.422 | 2025-08-31 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 7b995865-7a7a-3283-a840-5f18e1713397 | -7.8543 | -46.9525 | 2025-08-31 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 551.0 |
| a3923da6-fa9d-38a0-9d62-7d1315b2adf4 | -15.7107 | -48.9255 | 2025-08-31 12:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8f99786d-4ded-3aaf-9f23-b70604d4d44b | -8.294 | -46.3099 | 2025-08-31 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1f481ca9-75ff-34c5-94ad-394f3ba1acaf | -7.2142 | -45.443 | 2025-08-31 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 48680db9-c0e8-3cde-a09e-66c4abcb9512 | -14.8013 | -46.7371 | 2025-08-31 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 5266111a-2cf3-3579-b7db-0e7bb4792bb2 | -11.3705 | -43.5868 | 2025-08-31 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 3b97674f-166a-32a7-88d4-cf78e9d40dc3 | -7.8541 | -46.9747 | 2025-08-31 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 346.6 |
| 1dd3850f-4583-3ed3-8172-7aef0999d9db | -5.8696 | -42.9768 | 2025-08-31 12:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 155.7 |
| 9017752a-e4e8-3215-9abf-e08af9d73f6d | -14.8008 | -46.76 | 2025-08-31 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 92.8 |
| f7a9200e-884e-3e56-bf7d-0bb2b21fdaee | -7.1139 | -44.3111 | 2025-08-31 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| e466283a-a5a5-3536-96d6-e9207411a9cd | -12.3287 | -45.7201 | 2025-08-31 12:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8a4c9cde-0b07-3e9a-b33a-271d8cef3add | -7.2144 | -45.4203 | 2025-08-31 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 5cb83ba9-9796-318e-a0f2-b72d0f9a06c3 | -15.7098 | -48.9702 | 2025-08-31 12:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f1c6d456-3227-3930-b87e-95c3b66a5706 | -7.1954 | -45.4446 | 2025-08-31 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 8ae72d00-bf14-3151-84ab-939f23213f89 | -11.0288 | -46.8745 | 2025-08-31 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 769f7ab3-016c-33f7-92f0-96c5cedb311f | -15.7102 | -48.9479 | 2025-08-31 12:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 9a445fe9-956d-3c1c-839b-787f3f20d2fc | -7.0951 | -44.3128 | 2025-08-31 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 32c0ea4f-b739-3cbf-987a-75fb636e30fb | -9.245 | -47.0824 | 2025-08-31 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 90af38ac-f6e4-35cb-a589-ddb01018122d | -4.7346 | -44.4457 | 2025-08-31 12:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 308.7 |
| d048ceed-3f21-366c-b9aa-08b5a3547645 | -12.6298 | -48.1979 | 2025-08-31 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 24048728-bb73-364f-864e-d23fdd98cc5c | -12.6294 | -48.2201 | 2025-08-31 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 6faa00bb-51e0-307a-8319-e6c0b5daef54 | -14.8208 | -46.7337 | 2025-08-31 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ceb8a5bb-5da3-357a-bf90-70a7adf9ffaa | -11.9143 | -46.3953 | 2025-08-31 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 95aeecfd-67a0-3c49-9698-3dc1599ab9ba | -10.0434 | -48.0998 | 2025-08-31 12:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 8290b323-ac5a-3edb-b7e1-7bc988ca39d8 | -12.6486 | -48.2175 | 2025-08-31 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c06bd53f-b4c4-3013-88a3-522cc8e36b93 | -5.4824 | -44.3969 | 2025-08-31 12:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| c60d89f7-8284-3f0a-9473-9b1d339a169b | -14.2759 | -51.9234 | 2025-08-31 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 17a84659-15f9-39cf-802f-d7063fdabf00 | -11.0849 | -44.611 | 2025-08-31 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 45051fc2-932d-3252-b6b3-6c98c0fa631b | -14.2566 | -51.9259 | 2025-08-31 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 7fb561dc-c437-38f2-a8a2-df1e3e0b0c86 | -14.2763 | -51.902 | 2025-08-31 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 8f59494d-91d1-3811-99f1-a7cb4ad20cb3 | -11.3705 | -43.5868 | 2025-08-31 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 84f12716-8bb8-3ec4-92ec-7b52042c8061 | -11.8181 | -46.4314 | 2025-08-31 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| b04d1782-d9f0-3f71-8d17-76b5f6bf8e74 | -5.8696 | -42.9768 | 2025-08-31 12:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 196.4 |
| 40753697-06fe-360d-b226-3375e3708f4d | -8.294 | -46.3099 | 2025-08-31 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0386f9ce-d8e5-3530-852f-beb22f145e45 | -5.4824 | -44.3969 | 2025-08-31 12:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| ed6ca46c-77c1-3428-88ee-7e51cbfa5a1e | -7.0951 | -44.3128 | 2025-08-31 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c3854222-3755-39d5-9cfc-1fa0350b86ce | -9.245 | -47.0824 | 2025-08-31 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4a5f79da-1ec5-3c49-9717-7684fe6041c4 | -8.4872 | -47.4462 | 2025-08-31 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 222e2c71-58cb-3232-8c02-3d7ee6670f58 | -12.3924 | -46.4399 | 2025-08-31 12:50:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 08b5d14a-2044-3838-8000-030cfe3e4378 | -8.875 | -45.0961 | 2025-08-31 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4c94099a-1edf-38e9-bb91-86000a9e4d37 | -4.7346 | -44.4457 | 2025-08-31 12:50:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 242.0 |
| e9c7c443-f837-307b-81b5-afb694042669 | -7.1139 | -44.3111 | 2025-08-31 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3b1404f6-93eb-30ae-b46d-f81aeb7a3c8f | -9.2642 | -47.0582 | 2025-08-31 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 7f6546e7-b318-3430-9969-76ef24234ab9 | -11.9143 | -46.3953 | 2025-08-31 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 04462ad5-4aa0-3884-b104-bb9f5b3ad2f3 | -15.7102 | -48.9479 | 2025-08-31 12:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 05669a47-4a2f-3b6d-a45c-2a0de917b152 | -14.3532 | -51.9132 | 2025-08-31 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 63475bd5-216f-3656-8117-a8960266f1f3 | -11.0849 | -44.611 | 2025-08-31 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 6fb69aa2-a769-3597-bcf5-11955e1d9f20 | -11.8357 | -46.5194 | 2025-08-31 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 507703b8-1849-3148-aea1-5c62ee18a56d | -14.8208 | -46.7337 | 2025-08-31 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a0e7c4b0-13ea-3113-bff3-452803c6cab5 | -14.8013 | -46.7371 | 2025-08-31 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 38c03588-ea13-3325-956a-d62470c85ba1 | -12.3095 | -45.723 | 2025-08-31 12:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 184d9650-9afc-3953-9a87-b7fca7c112b7 | -12.3287 | -45.7201 | 2025-08-31 12:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 532fe081-4290-30f8-8f2f-81ce4013b961 | -7.8543 | -46.9525 | 2025-08-31 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 266.3 |
| a46f570a-dda2-34df-b5d6-0f56682644e6 | -13.3636 | -46.95 | 2025-08-31 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 77ba5c32-aa40-34f4-a844-9b02edc0cdee | -7.8541 | -46.9747 | 2025-08-31 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 268.6 |
| 3fcb3f5c-85c0-3137-8c73-3f0a38ad9016 | -13.3443 | -46.953 | 2025-08-31 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 2244c289-8080-306e-ad97-455959c41563 | -7.2144 | -45.4203 | 2025-08-31 12:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 124f1a4b-8777-3190-af7c-4d63e64ee0d9 | -15.7098 | -48.9702 | 2025-08-31 12:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 92c539d6-6860-3cb8-96c0-da41d969d352 | -6.5021 | -43.5553 | 2025-08-31 12:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| b8fe4285-4b67-3b1e-80c0-628715058a98 | -13.3439 | -46.9757 | 2025-08-31 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 477c0b57-cd96-3f1e-99df-f0f4ec312802 | -7.874 | -46.93501 | 2025-08-31 12:53:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 002c52e8-04f4-32cd-86be-ee8d7200f95a | -6.44643 | -45.62071 | 2025-08-31 12:53:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| c1beb0dc-7f4d-326c-b2c5-12dbfb6dbc01 | -7.85609 | -46.99169 | 2025-08-31 12:53:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a7d53c30-e986-342c-b9dc-0c261e588ed6 | -6.34177 | -58.18122 | 2025-08-31 12:53:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3c4f5bca-16ed-319b-b7f8-90ae3ca284ef | -7.87572 | -46.9621 | 2025-08-31 12:53:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 665d96f3-78f5-3b2b-871a-3f4ef409ce15 | -8.49428 | -47.45674 | 2025-08-31 12:53:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 679aa721-664f-3e11-95e4-5f505256e667 | -2.4134 | -49.35133 | 2025-08-31 12:53:00 | TERRA_M-T | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 19ba5e75-6280-37f1-912c-11faed3dea82 | -7.85825 | -46.93299 | 2025-08-31 12:53:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |


[Clique aqui para ver as próximas entradas](README87.md)
