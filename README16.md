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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84dbd55b-976c-3ecf-b6d5-570374ba08b2 | -12.4608 | -46.9045 | 2025-07-14 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| ae40e345-4b3a-3704-bd87-3cec64658234 | -12.4121 | -45.3628 | 2025-07-14 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| e4755f88-9425-38f0-9e7d-6ea48e76e1c1 | -6.4846 | -45.3007 | 2025-07-14 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 32d03349-3f66-3520-b565-606aded68263 | -10.3857 | -46.6855 | 2025-07-14 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f04ab489-ec12-39b4-b07a-abc5129d3509 | -7.6325 | -56.7691 | 2025-07-14 13:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 144.7 |
| e6a8770c-a27a-37f8-8a51-fb2947f62514 | -12.4608 | -46.9045 | 2025-07-14 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 98d066ff-9227-3226-b058-74c4819d40c8 | -12.4121 | -45.3628 | 2025-07-14 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 266.9 |
| 4bec9221-3c01-3c64-afd7-21c630dac0d8 | -11.712 | -47.0538 | 2025-07-14 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 15c71ddd-0779-3c81-adae-8438a2864000 | -6.4848 | -45.2781 | 2025-07-14 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 9d105da5-0ae1-3c8d-b765-30f0d650bdad | -8.4509 | -45.7996 | 2025-07-14 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 3af519ef-7267-3576-b38b-8d886480cff0 | -7.0262 | -43.741 | 2025-07-14 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 088ab475-7f8e-3b24-bc4d-6177daafa776 | -10.3857 | -46.6855 | 2025-07-14 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c4b5e8cd-3738-31ff-ac26-fbba3c25c59a | -11.0256 | -47.0762 | 2025-07-14 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 144.2 |
| f61539e7-c3f9-3cb3-b1fc-dffc0862e1d9 | -12.4121 | -45.3628 | 2025-07-14 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 314.9 |
| 134a783b-585b-3c83-bef5-a6ae2ab67ead | -11.0253 | -47.0986 | 2025-07-14 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 68fbffba-c6b8-3e6d-bc86-489123b5824a | -8.432 | -45.8016 | 2025-07-14 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 156.9 |
| a017e80d-fceb-3927-96a3-52ccf21dd317 | -11.712 | -47.0538 | 2025-07-14 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a4414cd9-e7b8-3a58-b405-04d43dd5f27e | -12.4608 | -46.9045 | 2025-07-14 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 3fb8f9f2-d769-3975-8d42-1a298cc2243d | -7.6325 | -56.7691 | 2025-07-14 13:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 09f888d5-a9fa-3d8c-a1c0-b7eb1d3331ef | -10.3857 | -46.6855 | 2025-07-14 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 092e7a0c-193c-30c1-97fd-22ab243cfa4f | -11.712 | -47.0538 | 2025-07-14 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| d70114a0-6b19-3510-b83c-c8b34bb5d306 | -6.4846 | -45.3007 | 2025-07-14 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 158.4 |
| fe52e079-35d2-37af-895f-f11f43328311 | -7.1665 | -42.9796 | 2025-07-14 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 4dfe75ef-b82c-36a6-b4f7-f0a1c0ef5013 | -11.0253 | -47.0986 | 2025-07-14 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b5ad9a12-dee3-3363-bdc0-e840d5a12f85 | -12.4608 | -46.9045 | 2025-07-14 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 192bfe09-ab2c-3c75-b743-150fe9d4c714 | -11.7124 | -47.0313 | 2025-07-14 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 88ff85fb-7514-3ef5-bd1c-29f0940745f5 | -12.4121 | -45.3628 | 2025-07-14 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 233.2 |
| 4b565ee0-0a1b-3a5c-81ab-9418eced4fc0 | -7.6325 | -56.7691 | 2025-07-14 13:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| e595141c-70b8-3759-94fa-1688a774d07f | -6.4659 | -45.3022 | 2025-07-14 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 24523ff9-51c0-38db-b370-252c076de8ae | -11.0256 | -47.0762 | 2025-07-14 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 7e64a8de-c0cb-3c4d-b323-57b97fe4a4bd | -7.6325 | -56.7691 | 2025-07-14 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 4b2fab65-d82d-3cb7-9baa-e8cc24397b66 | -11.7124 | -47.0313 | 2025-07-14 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 215f65df-8de2-399c-ae21-156de1309cb5 | -6.4846 | -45.3007 | 2025-07-14 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| b3096936-5a33-3bfa-81bc-8fc41688c7fb | -12.4121 | -45.3628 | 2025-07-14 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 228.5 |
| 1165a64b-8588-369b-8400-5273d573f966 | -11.712 | -47.0538 | 2025-07-14 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 150.2 |
| ed56f527-969e-3c6f-bdc2-b0dadab48bec | -6.4659 | -45.3022 | 2025-07-14 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| abe157c1-671f-362d-8f67-5d253e8a3975 | -6.4661 | -45.2796 | 2025-07-14 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3e265c26-d16e-3af6-8fe8-36c5613924e1 | -7.2861 | -44.0412 | 2025-07-14 13:50:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4fb3d263-81e0-3551-bf1a-adf23f8149c5 | -6.4846 | -45.3007 | 2025-07-14 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 195.8 |
| 27735cb6-96c5-339b-b99b-cf2fd41ee1c3 | -6.4848 | -45.2781 | 2025-07-14 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| d6d05f8c-0159-3056-86a8-83b0662f9961 | -6.4659 | -45.3022 | 2025-07-14 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 66fb0ab1-4151-3c5e-b1e0-09fb8bb051db | -7.1665 | -42.9796 | 2025-07-14 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| f17eb766-00e2-384a-a056-0f3985b88414 | -12.4121 | -45.3628 | 2025-07-14 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 3eda4811-00f9-3943-a090-d59b850127ae | -12.4608 | -46.9045 | 2025-07-14 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a52f8623-4257-3910-b72c-0a0e87dfc764 | -11.0447 | -47.0738 | 2025-07-14 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 5020e672-af3c-35a7-a0bf-549d10654b05 | -7.1665 | -42.9796 | 2025-07-14 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| dcafa92e-055e-300c-8f74-91a8dcb803dc | -12.4121 | -45.3628 | 2025-07-14 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| e6ee815a-0118-3ff7-a43d-46308aabc953 | -7.6325 | -56.7691 | 2025-07-14 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| fabaabe6-9926-3de1-9a7d-e1dd8b87d50a | -7.6325 | -56.7691 | 2025-07-14 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 79f6df6d-51fd-349f-8d1d-54bd2526c5ff | -6.4659 | -45.3022 | 2025-07-14 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 2f465c97-cc1f-391a-bba5-11efd32a9d4d | -12.4121 | -45.3628 | 2025-07-14 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 9a45a890-6398-321a-ae9a-026cc2997e52 | -11.0447 | -47.0738 | 2025-07-14 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 39a295da-38b3-3bcd-863b-268d828331b0 | -11.0253 | -47.0986 | 2025-07-14 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 383e9173-fe06-379d-850b-b0b24927a3d9 | -7.2863 | -44.0181 | 2025-07-14 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| fb429ed1-f0a7-38db-9602-26f955c2509f | -6.4659 | -45.3022 | 2025-07-14 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 449.9 |
| a5276ce6-27af-3f0f-b92b-a1e09e8a92dc | -11.0256 | -47.0762 | 2025-07-14 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 355a4796-e076-3ca9-9496-3d00d848a096 | -7.3049 | -44.0394 | 2025-07-14 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 151.4 |
| c284f532-65ab-325b-b1c0-029e486d7c2f | -10.3857 | -46.6855 | 2025-07-14 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 6e604e28-09db-3578-b288-11de05ebb601 | -3.581 | -47.5149 | 2025-07-14 14:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 8726085d-5843-32e9-a427-216ce42aa05c | -7.2861 | -44.0412 | 2025-07-14 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 194.7 |
| dad1ae85-447e-3652-8558-556f518ddaf4 | -7.1665 | -42.9796 | 2025-07-14 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 701d9abc-5b16-35a6-9fed-2cf68d986c5f | -6.4846 | -45.3007 | 2025-07-14 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 53a9c156-b147-3f01-86c1-7470b41dd52a | -11.0447 | -47.0738 | 2025-07-14 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 9dba70ed-31ab-30a0-9227-f3fcf51ecae9 | -7.2863 | -44.0181 | 2025-07-14 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 57a226c3-7062-346e-a602-3856e1a7ed00 | -6.4659 | -45.3022 | 2025-07-14 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 225.2 |
| fc611d28-7daf-311a-b205-4dccb60a9e72 | -11.0447 | -47.0738 | 2025-07-14 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 5db1bd93-20f2-3585-bdcc-e082aab38d88 | -6.4652 | -45.3701 | 2025-07-14 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 0caa7739-8782-3922-a75a-9d3721d3a4c0 | -7.2861 | -44.0412 | 2025-07-14 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 269.3 |
| 8d438902-6567-3f4c-bb88-697d35f09856 | -3.581 | -47.5149 | 2025-07-14 14:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 0adbf3fd-38ac-36d3-b0c6-185fd6237702 | -2.5427 | -47.7025 | 2025-07-14 14:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 55cc8ab9-c7d9-31d6-897d-238b1485ae92 | -11.0256 | -47.0762 | 2025-07-14 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 2d798398-ffe1-3d81-a5b9-68e811000f6f | -7.6325 | -56.7691 | 2025-07-14 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| dc427ecc-9127-3072-8bf7-2b089e562efa | -7.3049 | -44.0394 | 2025-07-14 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 154.6 |
| a0669c54-12b7-34b8-96c2-7965046e1790 | -10.3857 | -46.6855 | 2025-07-14 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |


