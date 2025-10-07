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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea9f5ab3-60ba-30c4-a576-7b8633d1da1d | -7.69907 | -42.41206 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 68575826-294f-3883-bf70-e85f6ee83175 | -5.7669 | -45.74409 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d82997d-8486-3b83-bbd3-b6c0cf40a6b3 | -10.67279 | -44.14834 | 2025-10-07 04:08:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0bc6e72-f650-3949-9140-c4a063fc22fe | -7.71008 | -42.38528 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5d17b299-d9b3-3c84-b830-0551d039a7b3 | -5.25557 | -46.49218 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c6e50a0-9334-3040-893d-5b18f5ad8753 | -6.07603 | -42.5576 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 57b2329a-565c-3b0c-a501-e915fe3964f9 | -11.12073 | -47.21307 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fa5bdce-de52-3c5f-a4a0-f7bfc989ac39 | -7.72496 | -42.39831 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7a649ff5-3e0b-3c9f-9e84-2f7dacad239a | -7.24969 | -44.12265 | 2025-10-07 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39cd9498-5830-3a02-90d8-3d38a0811b84 | -5.61322 | -43.93979 | 2025-10-07 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b937c2fb-ee19-30e4-adfd-df4667128110 | -10.36099 | -44.98027 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0a0805b1-916d-3c2c-b2b4-46b9a7a97423 | -5.48781 | -43.0816 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7fecb995-7eb5-3bf4-9daf-10b9a62c87b1 | -11.78485 | -45.13182 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9faec416-d5a8-3a4a-a60c-80981db00bd7 | -6.45201 | -44.58765 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3ac369aa-bb97-335d-8d0f-a9295d00ddeb | -5.64266 | -45.96145 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e83a2c92-990d-3646-8a72-f33df0b73bcd | -7.46445 | -42.62499 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7b220190-70f9-3967-997a-cfd4ccdd1f61 | -8.43714 | -48.69559 | 2025-10-07 04:08:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5499a626-2d93-3d66-93f6-1d9a21b136c3 | -10.40831 | -45.37691 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c7b5b1d-4a8b-3cd3-a355-3943c013f190 | -7.69576 | -42.41154 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| be245a74-1606-3172-8449-ffd841f02716 | -8.45354 | -47.2505 | 2025-10-07 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67dba2d1-df2c-3bd2-b4b2-ea437dcd14e4 | -6.65702 | -39.29351 | 2025-10-07 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d7a9457a-cda3-37f6-ad5f-f8d1fcf82f9d | -5.11494 | -43.21194 | 2025-10-07 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee0244a7-ae04-3fa4-9c14-48b24b4e1734 | -8.11434 | -47.00826 | 2025-10-07 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 584cdc50-a964-3c41-a756-9fd624407113 | -10.03835 | -48.2852 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b04a07eb-aa59-396a-9a9a-5542a8d9835b | -7.01976 | -42.29261 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ad349859-4480-377c-ad78-62485a01e94c | -11.81347 | -45.12408 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73fb7878-a58d-3f7c-8c84-a77921abff6f | -10.89911 | -47.11798 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8941350-1724-3c76-b68d-31ff92d1b022 | -5.91946 | -44.97 | 2025-10-07 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f71b98f4-c28f-3b87-a33c-b7db886d7921 | -9.40132 | -49.36795 | 2025-10-07 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86d90c30-2a6c-3701-9fea-e6e2517a3dd5 | -10.4181 | -48.09927 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c2996a8-c3b9-3a54-a7ad-d267ba19e78d | -6.3673 | -41.61886 | 2025-10-07 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8ddb54b8-e3d1-3763-bfc7-a5c697fc3d46 | -6.24778 | -43.9029 | 2025-10-07 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb235bbe-d544-3f92-a002-240d2952e451 | -10.87625 | -51.02703 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 38c654c7-11ca-399f-b9d3-ba9d66364646 | -8.65899 | -46.28101 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f80d8213-23d9-3ae0-ba2d-be6460f73242 | -5.47323 | -43.15049 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f0ebfbe6-0c48-348a-aeee-34910dfeffdf | -6.17443 | -51.16054 | 2025-10-07 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 527354d1-87ac-3bf1-8c1f-81439b12ccb4 | -8.53256 | -46.24979 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| e1fcb030-6e68-3aec-b12c-e44f506df486 | -10.37648 | -48.14183 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1160ac09-68df-3848-95d7-fce0ebd62a8c | -8.68518 | -49.95441 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3993f31c-bb66-30bc-9f35-3d8dd4cc8266 | -10.37253 | -45.35102 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f15cee40-1067-3b7c-9a33-931fda6f04bf | -7.47891 | -43.0252 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f8f0d03e-8b14-377f-aef1-35cbe22a902f | -11.84629 | -45.05454 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85a6f3af-a0bb-3215-9fc7-377a31f87dfc | -10.74032 | -50.49338 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 83ef70ab-3468-3a75-8c20-5504d93009e5 | -8.10941 | -55.07795 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d7fdc87-917a-3a7f-9afe-a5cd3ff9be05 | -8.61773 | -44.93559 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f3f4a2c-f638-3552-9604-64b8d65c4b64 | -7.56998 | -40.50871 | 2025-10-07 04:08:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 92e4051b-b7a1-3c56-b2d4-75a8cf624a60 | -11.94571 | -46.45431 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 041ff26e-7d71-31e4-9472-e208a4841f52 | -10.23084 | -48.18026 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83d412f3-26e8-394c-9662-2f818d9f9aba | -8.60752 | -44.90916 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad5f2218-127b-3b54-810f-785234bebaab | -6.41418 | -43.61371 | 2025-10-07 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d278050-9bda-3a59-b968-3f3738a51ed8 | -8.55082 | -46.25774 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8c85431-b83a-3139-93a0-80e59d496b48 | -6.29383 | -42.94165 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b56d82e7-9692-317b-9a76-4862dd195def | -10.32214 | -51.45469 | 2025-10-07 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3bbcd46-54bd-394d-b6d1-595d428cea36 | -6.31606 | -41.61781 | 2025-10-07 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0228b713-c764-36fd-b884-4edd322b1fc4 | -7.29399 | -41.9818 | 2025-10-07 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 63019c17-e713-3c57-bcf6-b6661065228e | -11.94941 | -46.43258 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0e1bfec-5be5-3c39-a7af-e01f5b5cd00d | -6.69816 | -41.39257 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3b5ca1d8-d3d2-3239-af9a-0622ea45d618 | -6.72605 | -42.8357 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb879238-cc38-363b-a912-7e14733b49d5 | -10.26461 | -44.36378 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4e1ed5e-86b9-3801-a458-bd1415e14795 | -8.17096 | -50.16573 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 167efecc-e62b-3057-8df3-f9b63d0de8f5 | -6.70647 | -42.18566 | 2025-10-07 04:08:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8aa53114-d3b1-3705-82ac-720f140e2ab5 | -6.72271 | -42.83515 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e19f266d-237e-3248-8ab5-ee7c6d76cfba | -6.52977 | -42.48633 | 2025-10-07 04:08:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9cacab62-1d3a-336f-aa3e-298ca917be8d | -7.02507 | -42.75592 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 979fd68a-2823-3ef0-8a50-da5c2e583ec7 | -11.64729 | -46.87932 | 2025-10-07 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efafe2fa-14f0-395e-ab24-f0180e1d354c | -6.69771 | -42.86716 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f40080dd-4b8d-3e6f-aaf2-b5f9e320457d | -8.9693 | -50.80122 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b87822a4-1462-3806-91b0-a6072d0d7488 | -6.08338 | -46.9931 | 2025-10-07 04:08:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 139f8502-b052-3a2d-9079-f72982a46d46 | -7.69466 | -42.3971 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 671f08bd-b960-39b1-8384-c948850fac39 | -9.03504 | -49.765 | 2025-10-07 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 699ea2b1-74de-36f3-93ed-7a460bc201d9 | -7.57384 | -43.96297 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb3cc4ce-9b3c-3274-a4c2-b5cf0a6df1c0 | -12.48639 | -45.55693 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fffe492-22a1-39d9-bdc2-726879ab4140 | -5.78796 | -42.91365 | 2025-10-07 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 9b2bc90c-3c2c-3395-a256-3e1d65ec3030 | -4.91873 | -48.02438 | 2025-10-07 04:08:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac97bcaf-4f49-3926-8d5b-67482addc3ce | -8.48496 | -46.30001 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e887b8d-100b-32ed-b8c9-523a1ef5b11f | -8.50007 | -46.32711 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1f669288-5648-33a4-ba81-cca5b177beb8 | -8.66319 | -46.28396 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e6f9bd7f-4e98-398d-b694-eef701d20f88 | -8.27425 | -43.82508 | 2025-10-07 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a421f491-f541-3234-a99f-eb894c71e6ec | -5.69951 | -44.8218 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f250152c-2cd4-33a4-af7b-204a8a8deaf3 | -9.67999 | -45.66985 | 2025-10-07 04:08:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68d832b0-5cda-32d4-ac42-ed9430b7dbc4 | -7.47219 | -42.61905 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1900947b-88e6-3418-acfa-f0ec557fd47d | -7.17776 | -47.54116 | 2025-10-07 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f2a1963-b9ee-36c4-9966-56828736211e | -8.64112 | -46.27544 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3b7dc1e-b56f-3cde-9e14-1c541271b314 | -6.65645 | -39.29728 | 2025-10-07 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b71121c0-80d9-30ac-b56b-29395aefc55f | -8.52941 | -46.26882 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01d0b8a7-0991-3027-afac-4bd04e97125f | -8.34381 | -49.65949 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 329a6021-5a29-378a-bff9-978031645ab3 | -8.50167 | -46.31753 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e888173-08ee-3af6-8aca-171614d827d7 | -11.50125 | -44.97003 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b47699c-e603-3471-85bf-07c647006999 | -6.71334 | -42.85501 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7c1ad3a8-bf29-38e3-a1c1-e6b67b6910e2 | -10.74713 | -50.48336 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ed1c89e3-6b42-3f34-af3e-a99471fd7d50 | -7.61208 | -45.47592 | 2025-10-07 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 884c5487-c9db-3117-982c-d5f42c8330f4 | -6.75023 | -49.04157 | 2025-10-07 04:08:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 31281e18-e93a-3339-b2eb-e80a6aab35cd | -8.65938 | -46.28336 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cbff52a5-b5cc-39cc-9863-6a571f7f3a40 | -10.39319 | -51.5973 | 2025-10-07 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25700222-53f7-30b0-b5e2-6d1e0c16a977 | -10.42555 | -50.32235 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee1da7fe-a777-370a-8ebc-97f42224c598 | -11.23214 | -47.76786 | 2025-10-07 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb585a62-804b-3947-beea-373507775c0e | -5.49914 | -43.07594 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| fa7e8517-5ce8-3185-9983-6a1785a1e864 | -7.67783 | -50.21119 | 2025-10-07 04:08:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47f1997d-94fc-3ebc-8891-9a48de164b11 | -10.41591 | -48.09822 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d681fab-1097-3eac-a115-e49159e7b235 | -10.91989 | -47.06562 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |


[Clique aqui para ver as próximas entradas](README22.md)
