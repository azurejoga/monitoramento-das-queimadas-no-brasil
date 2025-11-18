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
| c95a876a-ec7b-3677-ab62-eb65af9ddb51 | -7.8564 | -46.868401 | 2025-11-18 00:11:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2cd3046-2ffb-31c2-82a9-a6b8c5a81cde | -10.8462 | -44.856701 | 2025-11-18 00:11:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 779381a4-4d15-35f3-ba8d-ff7184cb4feb | -12.7343 | -45.3839 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d58729eb-ebaf-3c92-a35b-f1822aa6e76a | -3.0668 | -45.411201 | 2025-11-18 00:11:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2207f8d0-16ca-3a76-86af-04eee69c2bac | -2.8087 | -45.141201 | 2025-11-18 00:11:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0051819e-b5ff-30fa-8066-c131564c01c3 | -4.0997 | -45.6022 | 2025-11-18 00:11:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ced046d-fec3-36fc-ae6e-a8e8403dbc58 | -5.324 | -43.748199 | 2025-11-18 00:11:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b419d97a-8c29-3b14-b362-24ea56ccbbdd | -4.2278 | -46.3339 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8190cad6-647b-3387-9088-24b5e4501b78 | -5.4519 | -40.973999 | 2025-11-18 00:11:00 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e21c96b9-3ed6-3730-ad33-150a0f3bee6c | -3.1662 | -46.600899 | 2025-11-18 00:11:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e046fad-82e0-37aa-98ab-45a77da2b05f | -6.2969 | -43.767399 | 2025-11-18 00:11:00 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24805da3-8b09-3e92-90f6-5718ef7b73ff | -6.122 | -42.945801 | 2025-11-18 00:11:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 305306b2-58a4-370b-aaf4-f0dca87a6461 | -3.3304 | -51.492901 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92391614-5bc0-372e-bac8-10e67a045e0b | -7.919 | -46.022301 | 2025-11-18 00:11:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7aa84bf8-9e2b-3f3b-8f17-8efb7a1c2627 | -13.5277 | -43.011002 | 2025-11-18 00:11:00 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 88993385-93ed-30c2-8467-007e4146fc71 | -11.2552 | -44.532501 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02a2057d-e368-3627-97f7-e58a51dbbcdb | -4.1813 | -44.229599 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c128d5d-a45c-363b-9589-5f935be55ae7 | -4.1936 | -44.237999 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b134a01-eca1-356b-b69d-53b2e94e3028 | -4.6369 | -45.652901 | 2025-11-18 00:11:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e170b22-5305-3715-a63c-729f28cc27b8 | -4.0105 | -44.247002 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccaf3518-0b0c-3c93-a177-f132edef7600 | -6.8457 | -43.129398 | 2025-11-18 00:11:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 35e2ca1e-0899-3622-ad76-9d67de246b89 | -7.1448 | -44.914299 | 2025-11-18 00:11:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b543217b-0094-3128-a308-fed0837a6edb | -7.4042 | -42.750999 | 2025-11-18 00:11:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d2e5d5f7-e8a2-3467-ba90-77f2f8e23805 | -4.9693 | -49.763302 | 2025-11-18 00:11:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0329ab07-9c0d-3afd-97f6-b98d1819d495 | -2.49 | -49.323898 | 2025-11-18 00:11:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f92f970-0f59-3f77-820f-78ca91422c6b | -3.1521 | -51.478001 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b9309e3-3403-307b-a7b0-9248058401d8 | -3.6586 | -50.207401 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02a27d54-2237-380e-8c7c-5abf56c7a4dc | -6.8361 | -46.289299 | 2025-11-18 00:11:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42f8f5df-a37d-3564-b0d5-a4ebec322430 | -12.7441 | -45.381599 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b2e52ee-f231-3679-96d6-536e1720828a | -6.6777 | -43.765598 | 2025-11-18 00:11:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56ca15e6-3a4c-3b63-82a3-fb452ada3fd6 | -2.6838 | -49.043098 | 2025-11-18 00:11:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1267ce3-426e-356f-9b6f-cfdbccb4c9dd | -2.5604 | -45.268902 | 2025-11-18 00:11:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff1fef4-7eda-3ae8-9989-f72bb67bdd39 | -4.7742 | -44.6064 | 2025-11-18 00:11:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8fbde3c-36c7-35a5-b1d4-a230ba3a694e | -5.7479 | -49.242401 | 2025-11-18 00:11:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea34601e-7c43-3efb-8507-37f48976f3ee | -5.997 | -47.9785 | 2025-11-18 00:11:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b747a16a-96b7-3f87-90ea-e91339cf6059 | -4.638 | -45.5247 | 2025-11-18 00:11:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6861814-e28f-3941-9439-02379b2e3015 | -6.1053 | -42.962299 | 2025-11-18 00:11:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a9226224-45ed-3052-bf6c-f484a633aefd | -4.1691 | -44.221401 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ca2466f-cd47-3f71-8e9a-0607c87559f0 | -7.9478 | -46.816898 | 2025-11-18 00:11:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57ab353f-17f6-34f9-a8fc-ed323a832c8e | -10.8383 | -44.8671 | 2025-11-18 00:11:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67c83693-a610-3e25-ad1b-42272c9135ac | -1.8095 | -54.698101 | 2025-11-18 00:11:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 769f413b-8914-3d3e-8df9-a63c4fbaa2f9 | -6.8406 | -46.264099 | 2025-11-18 00:11:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88258699-2197-3a8c-8b5b-7d343c0ba658 | -10.882 | -44.613602 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e7bcaa7-0a8d-34b1-921f-d4a75d673c0f | -8.213 | -48.298199 | 2025-11-18 00:11:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e7595c5-5ec0-3437-8930-3f2ab9caa7f7 | -10.3407 | -49.6269 | 2025-11-18 00:11:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72dfe9a1-c8ab-3306-97ec-731547ddc00e | -8.1896 | -45.014999 | 2025-11-18 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a91afd22-0a7a-3fd7-9284-a446d2c76df8 | -4.963 | -44.665298 | 2025-11-18 00:11:00 | METOP-B | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa81345d-1e1b-3ff3-aaea-e4085bdbcaa6 | -9.388 | -48.439098 | 2025-11-18 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ddbe573-8505-36f5-b542-2fa15347cda4 | -4.6373 | -49.569901 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee5c624d-d379-3e0e-9200-ca2876d0c2d6 | -3.4045 | -50.1768 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db7d2b10-550b-393b-a0c4-277e9b9769bd | -3.2452 | -43.0448 | 2025-11-18 00:11:00 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8be50667-40c8-30cb-91ec-6708e58e31d4 | -4.6948 | -46.3032 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64d82ea9-413f-372f-bb2e-9fa2c9133eb0 | -10.748 | -45.1427 | 2025-11-18 00:11:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 730d5b24-c65d-34bf-b596-4e7886c20ba7 | -3.4912 | -52.347301 | 2025-11-18 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46ced6d5-e3bf-33d9-a862-81636d2e977b | -5.0779 | -49.833599 | 2025-11-18 00:11:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b11bf2e1-d447-3075-b2ad-7904d85d7bca | -8.1097 | -43.5438 | 2025-11-18 00:11:00 | METOP-B | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49bf9abc-e03c-31ed-972f-fdbd9134ac1e | -2.9145 | -47.839901 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c7e19d6-9ce8-39b8-87b3-9489e53ac4c7 | -8.2815 | -44.005299 | 2025-11-18 00:11:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| afe54bcf-71b6-31f9-8e1f-ed2df1db9623 | -9.7172 | -48.8997 | 2025-11-18 00:11:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee5493b0-18c1-357b-836e-9b2f639e6b5c | -4.5078 | -46.029099 | 2025-11-18 00:11:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1aa4ae34-44b5-3a7b-9449-408f7bdbe96e | -3.1538 | -51.485401 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35fb34ff-842f-3894-b1ba-1296457b8912 | -12.8511 | -41.4687 | 2025-11-18 00:11:00 | METOP-B | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ace6fd54-a924-3f67-9685-dfb71237366c | -2.3944 | -45.7094 | 2025-11-18 00:11:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 214ba063-7761-3b81-b044-969d14db4350 | -9.9155 | -47.8536 | 2025-11-18 00:11:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80961e44-a647-3434-9bf0-94b3cf4b58be | -12.8258 | -41.450001 | 2025-11-18 00:11:00 | METOP-B | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1efa2ba1-63e5-3da8-a0f1-d3fa9926fa88 | -12.9822 | -44.1035 | 2025-11-18 00:11:00 | METOP-B | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 62df57c3-188f-39de-bbc3-bf1754e31bf1 | -4.0509 | -47.491798 | 2025-11-18 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 958711e2-c814-30e4-aa13-97d7afdb1f20 | -11.576 | -48.141102 | 2025-11-18 00:11:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11321c98-1f63-3eb0-afa8-6291db6ff147 | -4.6019 | -45.9464 | 2025-11-18 00:11:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38b049d7-5ca5-3f8e-8030-768287c4759e | -4.6395 | -47.946499 | 2025-11-18 00:11:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f72a0c93-a2c9-3b46-9801-8cb911fcbef4 | -11.5615 | -48.447399 | 2025-11-18 00:11:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec9f26e8-7707-32f2-ab20-25549603dcff | -3.1505 | -51.4706 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 632b3bf2-6c6c-3e46-b1b1-5f4010b61012 | -7.6864 | -46.8465 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fa57e62-c910-363a-bbb9-e469d496111c | -6.3067 | -43.765099 | 2025-11-18 00:11:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 283c2ec0-a8f6-3d35-83eb-6ae17ce8325a | -10.7942 | -47.638302 | 2025-11-18 00:11:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7eb7e93a-9e89-3c6d-9264-a78313ae7562 | -4.5254 | -46.4174 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d653a9a0-7659-3c18-966e-68621424e91f | -3.5921 | -43.603401 | 2025-11-18 00:11:00 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9acb2f1d-38f5-331f-8a00-3adaea9a38b6 | -5.3338 | -43.745899 | 2025-11-18 00:11:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0271da6b-eeeb-3dd6-b7f5-9c59803dff70 | -4.9675 | -44.684601 | 2025-11-18 00:11:00 | METOP-B | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d52df61-1145-3685-960f-7b51fb589e18 | -3.1636 | -51.4832 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 396dabff-6782-367b-b137-4d16de96511c | -3.4622 | -50.113201 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0f8f95a-feed-3900-91b5-1f3a0cee882b | -6.4051 | -47.193401 | 2025-11-18 00:11:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f28f705f-6bc6-34f1-a787-a04afea53369 | -12.8385 | -41.4594 | 2025-11-18 00:11:00 | METOP-B | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4bc1926d-4a44-3089-9db1-1a2d79304cea | -8.5717 | -46.480701 | 2025-11-18 00:11:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36b0bcd9-f90e-3a1b-b35e-1e6b26a9ec55 | -8.9683 | -44.640301 | 2025-11-18 00:11:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1763e303-f599-3200-9ad8-1be3b4fe61f1 | -2.8482 | -45.223301 | 2025-11-18 00:11:00 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a21044c9-c4d9-39da-b104-d2d2110e20f9 | -2.5789 | -46.959202 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2822751-8a06-3604-a2d1-5f8a457e58ea | -3.8122 | -47.4842 | 2025-11-18 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0a0ad49-71ee-339d-9a1f-83ff239fc828 | -9.462 | -40.340199 | 2025-11-18 00:11:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 05b6035b-3b06-34d4-8161-8bec6b609a45 | -2.6854 | -49.0499 | 2025-11-18 00:11:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb401dc2-b50f-3767-afb0-921d5db5adfc | -4.7765 | -44.616199 | 2025-11-18 00:11:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 596706cd-55fe-3b32-b29e-e0a257a8be41 | -3.7153 | -45.855202 | 2025-11-18 00:11:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f45105a-fe40-3639-b1ce-c2df906e660d | -10.6614 | -49.355801 | 2025-11-18 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1329c031-26bb-30e9-8ec4-60e0785db52d | -4.7046 | -46.300999 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc7c584c-e9cf-3a83-8779-ea50448bd100 | -7.069 | -46.048 | 2025-11-18 00:11:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18d01999-4c48-3c8a-a2e3-d4c5c920565d | -2.858 | -45.2211 | 2025-11-18 00:11:00 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0dd8957c-d199-39af-b333-10ea1d78ff1e | -10.543 | -47.987701 | 2025-11-18 00:11:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9042e5b1-eb53-3607-8284-9476606fb28f | -4.4152 | -43.386501 | 2025-11-18 00:11:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcde0c48-2c5c-3b68-8ed1-803cfa6cdb94 | -6.6377 | -43.597198 | 2025-11-18 00:11:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebac342b-47cb-3a92-9d00-cc8cf34cb4e4 | -13.207 | -48.306801 | 2025-11-18 00:11:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
