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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89e607a4-47ca-3565-84ff-78a0d83b3181 | -6.90275 | -40.9119 | 2026-10-08 04:02:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 257e56d1-092a-3fb5-8101-5b26ffcd72e9 | -7.59971 | -42.38068 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c695a716-694a-31a0-9948-3c0ed0d74410 | -4.26648 | -46.40358 | 2026-10-08 04:02:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f05c2fbd-3c0c-3fbe-b571-993d6d7d05b4 | -5.37913 | -44.17709 | 2026-10-08 04:02:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f19d6e9-d5f2-3ab3-a9ee-21f16fbb384d | -6.84318 | -39.54884 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6156d86e-bdde-3e24-a7b1-fe627b539e65 | -5.28992 | -44.79586 | 2026-10-08 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4bd15e6-9875-32dc-ab45-22c60dbd75f6 | -7.21891 | -44.15497 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9df32e4-b58b-30df-9c23-54cb10235536 | -5.34178 | -50.98847 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3245faac-2f07-3b94-a1c7-7c1273a42f6c | -5.96982 | -40.91574 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 088c5edf-a86e-3d47-8094-7ac8002cded4 | -7.8332 | -45.47847 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 07d0b5f1-e429-385a-8483-e7ce0461eec0 | -6.63129 | -43.73638 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| edb078e5-8545-3471-89c6-450f992930f6 | -7.6897 | -40.19845 | 2026-10-08 04:02:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c5d7a956-8da9-3e0e-9b54-da67efbb0b3a | -7.22209 | -44.28426 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a3d9f65-10fb-3068-b33a-5a3a9d86c534 | -4.06849 | -51.03992 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf5fe87f-49e2-3f12-a2d1-721708f75d7c | -10.42295 | -47.26659 | 2026-10-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 52e7cd17-082f-3ffa-9908-3c3106b156b8 | -8.73767 | -45.16112 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 86b8c62d-a650-3c7d-98a9-41fa5c1db5f4 | -8.39072 | -46.30035 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 24aa430f-c15c-3996-bc71-de8e974c1744 | -3.26174 | -50.41448 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb087cf2-a7e8-31e3-937b-96e2a3eda826 | -4.81268 | -46.82784 | 2026-10-08 04:02:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bd675c6-f188-3d6a-b04d-c26f61ff9633 | -8.73191 | -45.16867 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3a07216a-e9f8-3d25-83b1-ebef57df17c8 | -7.64033 | -44.37732 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b942b96b-325f-3ef9-b08f-657c9f2aa6c6 | -6.0668 | -44.1093 | 2026-10-08 04:02:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 15692e97-58ca-3e08-9565-f8e53dc15b84 | -12.30557 | -38.94535 | 2026-10-08 04:02:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d03202b9-9071-35ce-af84-4fae1cf46f32 | -3.17843 | -50.55743 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eab4a29b-97d3-387c-8eb5-2385c9f0f727 | -9.94431 | -43.55997 | 2026-10-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fead9c12-f7f2-39dc-bb8f-f6c1b0f43c36 | -10.77288 | -46.58693 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48275c47-d802-38da-ab6d-0c5a35beb6e5 | -6.62318 | -43.73494 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6d90d237-4e6a-3eac-a370-67f5af85e27e | -6.37936 | -42.53449 | 2026-10-08 04:02:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 39ba7df6-5271-3840-9967-a6cdc486a08f | -3.20271 | -50.55497 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 460395bf-0db6-3713-b726-2882d103dfba | -7.16497 | -41.99551 | 2026-10-08 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a4898703-38a3-310d-9857-d476edea0af9 | -11.63718 | -43.70247 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2c031f24-25b5-332e-b2f8-c4520e3c8dc3 | -8.597 | -44.87181 | 2026-10-08 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e0e0958-2947-3630-a93e-31955e8041c5 | -10.98907 | -45.47389 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71e4165a-d8dc-3ee0-bc62-4d9940530ab6 | -7.87167 | -44.15543 | 2026-10-08 04:02:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a689ffe0-a831-3cfb-830e-5f34a3188f50 | -5.49418 | -42.85649 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 83a23bb1-a70a-31ab-9d66-e9f7a7433917 | -6.83484 | -39.55819 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4e7f1c2-bd01-3c0e-8cc9-6fa769f4973e | -5.83661 | -50.1468 | 2026-10-08 04:02:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36892bd8-da1a-3819-9bc9-74952df53abb | -9.81964 | -44.8404 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b24e9e43-2f38-3515-9db1-a7839174152e | -6.07715 | -46.58281 | 2026-10-08 04:02:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5542e4bc-32a1-36ae-81cd-e0722e59c53b | -9.83344 | -47.47306 | 2026-10-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f49bdace-33ef-3017-a609-d7bcc430fb71 | -7.10893 | -42.53433 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6e13231-1b6f-3a4a-a6af-2aa7ac5e748a | -3.17557 | -50.45399 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e04a6532-3496-318b-8efe-3a8a349dddd4 | -5.83329 | -50.14565 | 2026-10-08 04:02:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da5d9696-0175-3d21-868e-1a2566dbdc91 | -3.18411 | -50.56461 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7401f6e-a425-3706-88b0-bb353b688dc4 | -6.36727 | -42.90488 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c95e0018-1ac9-36ab-89e1-4c2f5a9f6dd4 | -11.21214 | -44.86724 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d74ffc5e-6d49-373b-aa89-3b73f01f07a8 | -4.34961 | -43.79532 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| cdd3d6d8-d1bb-35ab-b7e2-33c14968208a | -4.51737 | -44.04152 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f235449-c3bf-31d1-b3e2-bbfc21a96922 | -8.21316 | -46.32499 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f0cfaac2-0eec-3f11-ba70-b021ab9c413f | -9.83238 | -47.47884 | 2026-10-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80950dcb-9cb3-3eb6-886b-93e6475d3e4c | -4.2635 | -46.39066 | 2026-10-08 04:02:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 166714e7-de67-3e16-abff-5f2bbd4a1274 | -5.33513 | -50.98724 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cc34cf3-5da5-3249-a0fc-e4e269694e15 | -8.59877 | -45.64065 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acbe6a6c-5914-30fc-840f-c8f0b0b5af01 | -7.17873 | -52.62634 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 83071ed8-cfe9-39f5-aa23-5d3a32d8982f | -9.83837 | -47.47404 | 2026-10-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a528ae6-05f8-3990-8110-c27d76c47ff4 | -5.93485 | -42.13044 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1dc9241a-8a54-3c2f-9062-eaed9bab0c6f | -7.22144 | -44.28807 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| efcec413-a92f-3f5c-9997-68e56671ce4f | -8.72762 | -45.16783 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 016723fb-6bc1-32c8-bbd0-ed6d35e6ea81 | -6.15424 | -39.43485 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1bbd9a84-196f-36cb-bc21-38dcff8b4c56 | -11.63264 | -43.7064 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 471e5e92-5e02-3fc2-88e7-6d6b545a9703 | -9.76218 | -44.79138 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52611a90-3714-3ab1-aa3a-33f3af6bd329 | -9.83674 | -44.7923 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11d34557-9e47-317c-b686-1cd1234c9868 | -7.66183 | -44.95417 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d8ff5e8-e5e9-3042-9b61-2858ff67f4ef | -8.99224 | -45.91898 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a81df9d1-73a0-3c0b-bbab-03316f580a7d | -5.97343 | -41.35764 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3f7ab6f0-e72a-3ca5-9def-757e020656b5 | -5.0871 | -49.70117 | 2026-10-08 04:02:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9431404-7299-3329-a3d5-4f24cf1d9fe8 | -11.20808 | -44.86653 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48be4af4-c62e-37f9-a247-7bfe1def66ba | -7.21693 | -44.16634 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea00dfd8-5950-340f-9326-fdbf899954ed | -3.54275 | -50.10424 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a813cde8-7d1c-37f4-bfb3-5e4e1cc113d7 | -8.38603 | -46.29959 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 73fce8a5-0896-35ec-bb3c-a971ecc5696b | -7.30803 | -43.98064 | 2026-10-08 04:02:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0201ad10-54ee-3ca2-909d-0c1aaa28d478 | -11.23575 | -46.249 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a76f9cb-5926-32bf-b11b-d520e07c3f35 | -5.10901 | -47.11653 | 2026-10-08 04:02:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd2e2ff-0928-3b1a-8f25-135d8333b1d9 | -6.35573 | -42.58341 | 2026-10-08 04:02:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7ecf74f4-2ab1-351e-8cfa-2c9cfc1021f8 | -5.68753 | -40.88834 | 2026-10-08 04:02:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 81e13cf9-8e7a-3449-8d8c-dc84d8d7d0c2 | -3.19602 | -50.5538 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 09fee3c4-df5d-31f0-89ef-2b2f7c020c81 | -10.77153 | -46.54209 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e11b4e1-8917-3a22-9846-b2b1bc1d464b | -8.2153 | -46.34043 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9a1b1bb-6341-3c66-8e76-6e4251b0ae2a | -7.02069 | -42.11805 | 2026-10-08 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8f470ed0-6d82-3451-9a73-177c66843b69 | -6.64031 | -41.71746 | 2026-10-08 04:02:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 140f3eac-7c4f-3b7e-9f00-86413f7bfbc9 | -6.15538 | -39.42782 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d0b580a4-5dec-3a4f-830a-6c49834068ce | -5.75753 | -42.07306 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b1dc515b-691f-3f92-950f-5e58702c51a5 | -6.83262 | -39.55069 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 70859cca-ad69-3752-b20f-1614e4e7cb64 | -5.95484 | -46.36345 | 2026-10-08 04:02:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62e8c3f5-64c1-3df4-97c4-f34209878560 | -8.30461 | -40.49451 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 093657fe-4d81-3402-aac0-fffbf355fe75 | -6.9168 | -41.24144 | 2026-10-08 04:02:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 72bd329b-ec1b-3a51-993c-1c8f104654ea | -11.61865 | -43.675 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6f393d3f-6cd7-35e0-839b-430c6a4a292b | -7.60339 | -42.3813 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a23b89f-3e18-3229-a2fd-00a35e40a768 | -7.66256 | -44.94998 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2530dcd4-2b38-3127-8ad0-de8407f05fd1 | -3.18932 | -50.55265 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3b3d487-a779-3f35-b0d7-dc03d378b38d | -5.47911 | -42.87438 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f34b3ef8-2ffa-3eaf-953b-95c4c2551266 | -8.72332 | -45.16701 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f93900ab-5d9c-3e9e-90d4-5c9b22fdcc0b | -8.72397 | -45.18872 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 460f0d4a-75f5-369b-bea5-e297b4714b97 | -6.59899 | -37.89735 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 51dba402-a0a4-3e1b-993e-8fab97b662e3 | -5.71806 | -41.76777 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b3a4055-72e7-3019-b242-0d3820113761 | -8.73265 | -45.16447 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fcb37f60-8a90-318e-ab3b-582b18d297ff | -7.59898 | -42.38508 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 858db983-0327-33db-ac65-dc70b40358ee | -7.60043 | -42.37627 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a3e02ae1-d8f5-39d5-b57b-7d9622033a6e | -5.48146 | -44.59922 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29ad32ca-f04c-3078-ae72-be47872c7e80 | -4.2972 | -50.78598 | 2026-10-08 04:02:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README70.md)
