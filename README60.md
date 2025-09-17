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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad787df9-b0d5-31d9-a8ca-f969c4ec6915 | -8.99134 | -46.26101 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| a9b49d1c-062d-3948-8efb-671d9057ba3b | -8.95342 | -45.5318 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 745a682c-4643-3602-9f55-c7e40fecc165 | -9.11671 | -48.10738 | 2025-09-17 12:36:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4ba3211e-b299-3548-81d0-c71ed9a66549 | -12.69998 | -47.9638 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| b76d20b1-af62-3880-81f6-c7f68d748d22 | -7.89395 | -48.16669 | 2025-09-17 12:36:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4d2cc456-0637-3c9f-8f00-8d2a3fd091ef | -6.60917 | -45.57752 | 2025-09-17 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| f0922820-2b06-309e-a420-bed6ca1d963c | -8.64592 | -46.43842 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| f8247ca9-f8d3-36bb-8e80-2c9bac0b0f3f | -11.59546 | -49.8148 | 2025-09-17 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b3f3722d-dfc4-3804-a601-08f17fb969b0 | -7.67217 | -46.63451 | 2025-09-17 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| af49dc72-95c1-3c48-b40d-63cfba69f698 | -8.96296 | -46.29185 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 81e72bd7-f097-35c5-85a6-6b4ab6ae9fb2 | -8.90594 | -47.86507 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b4a2da0d-6888-37bb-b3a3-fcff2b4b97f2 | -6.59952 | -49.49422 | 2025-09-17 12:36:00 | TERRA_M-T | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8da9b5fa-1a11-3b16-baa5-c0d4739dbd3e | -12.07436 | -46.56197 | 2025-09-17 12:36:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 3c70a07a-8aed-3efa-ae24-e664e269f906 | -12.10936 | -54.57431 | 2025-09-17 12:36:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 307c4d9f-e31a-30a5-9a84-48ff8cdb920a | -11.36687 | -47.37768 | 2025-09-17 12:36:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 4e74380b-90d0-3691-9a7d-7b67ae91e5cd | -8.95566 | -45.51755 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 2894baf3-acc5-3e13-bdcd-32578c918726 | -11.11403 | -45.34843 | 2025-09-17 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 9d0b1c41-f4dc-305c-b58f-33506213b341 | -7.54193 | -44.73181 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 39.8 |
| d5328537-5855-3307-8801-40d6727d6341 | -8.18448 | -44.81064 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 905fb2e2-2f3f-3d02-a543-e229f7c0471a | -12.70335 | -44.86528 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 1a06be2c-20fe-3014-94b2-2d4b878ec1e0 | -8.78986 | -47.8039 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 437b500a-c8b8-3ece-837d-e40bcdb701e5 | -8.80114 | -46.02655 | 2025-09-17 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 9bc6e994-50c0-3d8d-b38a-9c6277b8a4ae | -8.63715 | -46.44817 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f5ff2802-6033-360a-9fdd-9f758282211b | -8.92874 | -46.22793 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| f7531d07-fd99-30e1-a5c7-30af91630ede | -11.59356 | -48.27746 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| ae7d79d0-f9e1-3436-9319-2a6dd9905514 | -12.4223 | -47.80435 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f5d9ed5a-0666-345a-b628-6213aff0fbbd | -8.47153 | -45.10964 | 2025-09-17 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 829ab459-cb9e-31e8-9926-3b0c550ea47d | -11.88664 | -48.8396 | 2025-09-17 12:36:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 8f3b17a3-a80e-35ce-a07b-43543926b9af | -8.64894 | -46.44975 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| ab81e1e0-eedb-3271-89e0-0b84de86434f | -8.68768 | -46.39379 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 7ce2b4fb-eed5-3854-a53d-9b5df96ed2c7 | -10.65152 | -42.30098 | 2025-09-17 12:36:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 144.2 |
| 51bde7ba-2051-3c1e-9c37-eb27a01ac04b | -12.6916 | -45.27265 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 3247522c-6a0f-351c-a316-2682f4536d30 | -8.95096 | -46.29015 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 178a5ab1-70bf-3081-a89a-a0102f317787 | -14.18924 | -55.08799 | 2025-09-17 12:38:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| df41237e-dc82-316e-9fe5-34fb5ec3e6a3 | -18.75483 | -49.32575 | 2025-09-17 12:38:00 | TERRA_M-T | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 243bb6c8-d1ed-3943-a9a5-42e4506c388a | -14.74611 | -51.69345 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2ac05c6d-04e6-3de8-a49e-ddc126596e0c | -14.79705 | -60.22522 | 2025-09-17 12:38:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| b378c8c0-5e7b-3615-ac9a-919ac6597d26 | -14.78764 | -51.72873 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 0fce2300-88a5-3dd9-8bd3-ca4decea4b08 | -14.77435 | -45.32285 | 2025-09-17 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| a3b37bea-5c06-34b2-952f-104a20f8ead9 | -17.44161 | -49.02513 | 2025-09-17 12:38:00 | TERRA_M-T | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7be78a7f-a510-3cfe-9886-bd8842de8154 | -15.43228 | -46.147 | 2025-09-17 12:38:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 76585ea6-0549-3778-a521-1060729c1805 | -16.84577 | -45.44693 | 2025-09-17 12:38:00 | TERRA_M-T | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 1fd1db3e-e29e-3bdf-af57-3804ebc6b703 | -14.79938 | -51.71079 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| e261b4cc-59ff-3f61-8ab4-db436645662f | -13.82919 | -54.90394 | 2025-09-17 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 51e6a233-520a-3afd-b326-754e9948bd9c | -14.828 | -51.70503 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 04ad3ddd-4f73-38f4-a8c1-967390a87c08 | -14.82666 | -51.71465 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| c1a1b626-b0a7-3874-bd44-f2c442ad81e9 | -20.36796 | -49.50088 | 2025-09-17 12:38:00 | TERRA_M-T | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 9e73787e-9509-3f18-ab23-fa52e2c33c1d | -13.35124 | -57.23926 | 2025-09-17 12:38:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9d3311a3-d9ee-3f2d-b7f9-c7df46a9693b | -19.27901 | -47.42798 | 2025-09-17 12:38:00 | TERRA_M-T | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 2e21c8ca-89f5-37bb-a46d-23ea01ba2b12 | -16.84844 | -45.41958 | 2025-09-17 12:38:00 | TERRA_M-T | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 28.6 |
| ed886867-ad08-3e04-93c9-e6f27ccd5a26 | -14.80847 | -51.71208 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 540543cd-2eaa-308b-a22d-0397a596e990 | -15.90964 | -47.30927 | 2025-09-17 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 4d080541-bcb4-397e-a51a-6011d9ce8b72 | -14.57032 | -47.36921 | 2025-09-17 12:38:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| eb0e1363-db49-370a-894e-a13b01140d46 | -14.58297 | -47.41487 | 2025-09-17 12:38:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| e32c95b9-ce7e-3b33-aaff-ce6109ef71c9 | -13.78953 | -54.93237 | 2025-09-17 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1cd637f3-5946-3b54-a214-2293b75bf5cf | -15.8438 | -59.48769 | 2025-09-17 12:38:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 60e5a1bd-1c4a-3aeb-aa1f-2d3a515d3ee8 | -14.76168 | -51.71526 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 173.5 |
| a16c03c2-f1c3-3612-875b-470683049981 | -14.78386 | -60.22259 | 2025-09-17 12:38:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 13e13e82-a12e-3e1b-a601-51fbc8d76e08 | -17.20115 | -45.8997 | 2025-09-17 12:38:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| daad780e-7464-3bb0-9df2-86c50bd5178e | -14.5607 | -47.34798 | 2025-09-17 12:38:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ab21e2d6-a518-3bea-a65f-5b42caf1700c | -14.8098 | -51.70246 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0875be03-f4f7-34af-bd29-f1c3ce80c351 | -14.76037 | -51.72487 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 236f9d83-4d2d-3df8-89c2-01b41c687174 | -17.80885 | -43.81175 | 2025-09-17 12:38:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 825a298b-9d3a-3339-9dd0-f01e6cf86101 | -14.79805 | -51.72041 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 425.4 |
| 22457305-4e83-3d24-a848-19896087bcba | -15.84758 | -59.39073 | 2025-09-17 12:38:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 550b24dd-2a60-34bb-8683-9c896a36e7af | -14.77209 | -51.70694 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4362be9a-5fce-3e94-996c-c755c9846861 | -14.8189 | -51.70374 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 444e9850-8110-3afb-836d-1aa4abcd0822 | -14.78896 | -51.71912 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| dab7cc60-eef5-3533-8792-6250797c1075 | -14.17993 | -55.08656 | 2025-09-17 12:38:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8ce10a82-3eab-3872-99da-7c7c9d82c8fe | -13.24149 | -54.21658 | 2025-09-17 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3f11544b-853d-3200-b8e5-d1f4445c8efd | -16.84416 | -45.43991 | 2025-09-17 12:38:00 | TERRA_M-T | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a65f0019-eebe-3db5-8b32-de7db4194f11 | -19.78172 | -48.31505 | 2025-09-17 12:38:00 | TERRA_M-T | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 483934d6-1866-30ee-a8be-f558e9cac872 | -15.83763 | -59.47352 | 2025-09-17 12:38:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 040899cb-d07c-3bb3-86c2-4e1f7f9c4d4e | -14.77077 | -51.71655 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 43d59309-39e5-394d-9e3e-f3eb0c83c386 | -15.89946 | -47.28892 | 2025-09-17 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1ce44fba-68a9-3dba-891f-a6624ad9de95 | -13.24008 | -54.22605 | 2025-09-17 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 71566868-e2fd-32b9-b4d2-316d1bb174bb | -14.55168 | -47.42171 | 2025-09-17 12:38:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 27.7 |
| a9db6fe0-b1cd-3f1e-b8bb-bdbc63a83110 | -14.80714 | -51.72169 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 1796ad44-04a6-37dc-9092-fbb2f4192d85 | -15.44075 | -46.15285 | 2025-09-17 12:38:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ef7c78b1-2567-304d-b06d-a9a631d72157 | -15.79875 | -59.45633 | 2025-09-17 12:38:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 2725011d-d9f7-361f-b338-430dfcaed6a2 | -13.78027 | -54.93081 | 2025-09-17 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 869c6831-7132-3fb0-b8af-8d6191025d91 | -17.8031 | -43.80597 | 2025-09-17 12:38:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 3b3c4fdb-fba4-38f5-b4cc-e8a369a956e1 | -14.56907 | -47.42967 | 2025-09-17 12:38:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 94354845-ba03-32cc-a1e4-63d791bfe8db | -14.7539 | -51.70436 | 2025-09-17 12:38:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 4cf8a38d-fa70-3c7e-8346-5c95b38b8f79 | -20.36971 | -49.48551 | 2025-09-17 12:38:00 | TERRA_M-T | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 81105ffb-bd92-35e1-8144-a868ca40e11a | -15.83433 | -59.49221 | 2025-09-17 12:38:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 76a5a4be-583e-35e7-a684-b949e59ec33b | -8.9917 | -46.2609 | 2025-09-17 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 401.7 |
| df4ba348-cb0b-3209-af0d-3d26dc6710ce | -12.7106 | -47.9649 | 2025-09-17 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 83a4efb7-c926-313f-81e2-be9d57d169b2 | -8.6313 | -46.4329 | 2025-09-17 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e4e8e675-5b6e-3698-9477-19aabcca3b94 | -6.8734 | -43.9636 | 2025-09-17 12:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| a181f17c-44f5-375e-ab88-209733d964c2 | -8.6887 | -46.3599 | 2025-09-17 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 671bea72-957a-3334-b6ed-d722b54b5c3b | -9.1236 | -44.8849 | 2025-09-17 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 0cd255c5-6cb1-34ed-b5b0-40595baa8c3a | -6.6129 | -45.584 | 2025-09-17 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 4f42dea3-03cc-326a-8d2f-12a5268ac4ff | -9.1239 | -44.862 | 2025-09-17 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 05b1de61-3867-346c-afc6-07fbe3512920 | -8.9725 | -46.2854 | 2025-09-17 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 192.8 |
| fe927916-9fdb-3bdc-8fff-ec25c8780bfd | -7.897 | -48.1787 | 2025-09-17 12:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| fe615a1d-6fd6-3177-8ca7-5a9b3999c1b5 | -8.6702 | -46.3394 | 2025-09-17 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| d3c01af7-000c-3a05-9379-5ea31667f05d | -8.5609 | -47.5712 | 2025-09-17 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 68f5d138-5d28-396b-9adf-50afa646417a | -12.0047 | -46.6989 | 2025-09-17 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| ddfab48a-3838-3dbe-ae23-97a4e40de52e | -10.33 | -46.6025 | 2025-09-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |


[Clique aqui para ver as próximas entradas](README61.md)
