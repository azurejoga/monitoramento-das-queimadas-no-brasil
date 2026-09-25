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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d725cebe-3b48-34cc-aae8-cb67c48b3fcb | -12.93223 | -42.49496 | 2026-09-25 03:49:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ca946c5c-8f66-360e-80b2-f8bb0132ca05 | -7.35864 | -42.07106 | 2026-09-25 03:49:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 910882dc-5d6a-362c-8a30-113af2d0cb70 | -12.65557 | -43.15829 | 2026-09-25 03:49:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1150f8bb-8829-38f4-bd7b-bcc97ac888c4 | -5.77996 | -45.09394 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbfe157f-bc15-3d92-aa76-34c199aa47e5 | -11.34639 | -43.39881 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c292eeb0-3570-3cef-b33c-32dca3684125 | -9.47859 | -40.32713 | 2026-09-25 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fa600e9c-ee2a-3d1e-88f2-6668894f3c75 | -9.85133 | -44.18865 | 2026-09-25 03:49:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a68cafa7-99d4-3540-81eb-b9f112761570 | -5.77343 | -45.10208 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad73bd15-0049-3aac-9018-1947f12caa49 | -13.40533 | -40.96477 | 2026-09-25 03:49:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a04dd4a6-8fe3-362b-bef8-40f606e0d5fc | -6.92552 | -41.69439 | 2026-09-25 03:49:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b44f1807-8d4d-31fb-9bea-a844a388c045 | -7.35921 | -42.06764 | 2026-09-25 03:49:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a7c70d3-2bef-3f66-940c-1f66348c0ecb | -0.93521 | -47.55338 | 2026-09-25 03:49:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d6e545cb-e915-3f81-a868-69bd839d3cd2 | -7.42915 | -40.22887 | 2026-09-25 03:49:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fdbd2cfd-cb15-35d0-a221-38a4c7fc9ccc | -10.24837 | -44.62926 | 2026-09-25 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb777d01-3830-3ace-bdf3-bebf4f3e8b2d | -13.02026 | -43.62745 | 2026-09-25 03:49:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22934890-7a17-3c7b-b0d0-b711f1b94480 | -8.32867 | -44.15163 | 2026-09-25 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 628db545-50a1-3fbf-93fb-687cd8f9f87a | -7.24582 | -45.25932 | 2026-09-25 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cf715c4-61f5-3757-8e3c-6fded0024c63 | -5.37778 | -45.99653 | 2026-09-25 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18f5a720-cbeb-3e0d-a6ce-dcfa88536837 | -6.71224 | -45.99326 | 2026-09-25 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6328ddc0-54ca-301d-b3f8-b6a52d6cbce3 | -8.33397 | -44.14771 | 2026-09-25 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 915050eb-2e9e-30fa-bb4c-c2b913025e84 | -8.33847 | -44.14845 | 2026-09-25 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 12bdc53c-4735-3109-995b-7592d8e181ba | -9.98941 | -48.31795 | 2026-09-25 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2de176cb-6d31-35b8-9d2e-e656b1bc3fa2 | -11.64585 | -43.48297 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f336b600-f989-396a-a964-2a3ec0c04336 | -9.63175 | -43.96817 | 2026-09-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2d3fcf70-44f0-3417-bca5-048fc933922d | -12.65466 | -43.16344 | 2026-09-25 03:49:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| c9a2a804-63c0-3c49-b488-9ecaa325d30c | -11.74324 | -50.55822 | 2026-09-25 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 85f46b61-2e1f-3435-927d-38b64bb94a75 | -11.67113 | -43.50644 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c68ac7d-a09a-3908-8036-0f3305099b60 | -10.03896 | -50.16274 | 2026-09-25 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6571d9cf-fa56-372c-8aa5-789e51b6c78a | -8.92364 | -43.87272 | 2026-09-25 03:49:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10fa43d1-b0bc-3953-8d34-0a425c96760f | -7.38929 | -44.77327 | 2026-09-25 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e850191e-b3e8-335f-9232-0d3a8acdaa26 | -7.12619 | -41.72572 | 2026-09-25 03:49:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7af525c4-6fd1-3809-8252-74a2c7f9d866 | -7.9175 | -36.39941 | 2026-09-25 03:49:00 | NOAA-21 | SANTA CRUZ DO CAPIBARIBE | PERNAMBUCO | Brasil | 2612505 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d4693cae-418f-3716-ba4e-8bda6f58081b | -5.77896 | -45.09984 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 144dd462-0167-3c1a-bc5b-cd4b31686acb | -6.89452 | -43.74803 | 2026-09-25 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55d94a3c-2949-3f8f-9872-5d1a719b98d7 | -9.99022 | -48.31361 | 2026-09-25 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67952e27-8ff7-3f2f-8dd4-22b2fcbc5669 | -13.0673 | -43.27618 | 2026-09-25 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| bde26d98-a528-3f83-939f-95f580dcf551 | -7.86331 | -40.01518 | 2026-09-25 03:49:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 19aff5d6-bb23-3024-b6ff-9137fec23e2f | -9.62963 | -43.9547 | 2026-09-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 6a181b0c-f1ee-3a51-9b05-e435557a913f | -5.61995 | -45.2461 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdc2bda1-b01f-352c-8a52-3d07382515dc | -8.32946 | -44.14701 | 2026-09-25 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1a0b4f93-7749-3058-a43e-0305761b7f11 | -11.73683 | -50.55692 | 2026-09-25 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| d24a69ce-1110-32b0-8016-596d14780c73 | -7.12544 | -41.72769 | 2026-09-25 03:49:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 87ef921e-ef61-33d9-8724-f59746979665 | -11.14871 | -43.23655 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b48a0276-431b-3fcb-be38-93b2a4b657f1 | -13.20369 | -40.45992 | 2026-09-25 03:49:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8095ad2f-14e7-3487-a522-82662bf6d40d | -11.66362 | -43.50132 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 109d3342-e376-3760-bf60-6e1da118f7fb | -6.79752 | -39.29046 | 2026-09-25 03:49:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0b3f9493-288d-3c1e-90e6-b409bb1b5954 | -7.45734 | -44.57986 | 2026-09-25 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ac90c8f-42de-3dae-a4dd-4484408bff29 | -7.04505 | -41.50541 | 2026-09-25 03:49:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0332b766-8fa4-376f-81a3-c131ead17c24 | -7.12156 | -41.72688 | 2026-09-25 03:49:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bcad28fd-5783-32f9-a3f4-76c8056a59c7 | -13.07125 | -43.27389 | 2026-09-25 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cb0986a3-5986-3885-87fa-9d523692ac95 | -9.63183 | -43.94212 | 2026-09-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| de19dcb5-c95f-3cc4-bbd4-f17bcd1710c4 | -13.0674 | -40.26351 | 2026-09-25 03:49:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 784af971-2caf-3db0-9221-af3fe997e57e | -10.92554 | -43.85966 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8abe780c-1447-3d7a-bf5f-01ab77194c25 | -9.47091 | -40.32996 | 2026-09-25 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b2dd0944-475c-3669-becd-31c8683f13a1 | -0.50673 | -49.16088 | 2026-09-25 03:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d47ba5bd-5e77-3c4c-930a-5b60ffe2d437 | -8.33318 | -44.15232 | 2026-09-25 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 54.9 |
| ee33a11c-4609-3488-8ac2-677487ca56a1 | -5.77946 | -45.0969 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bd9c8b64-b813-3d92-9c7c-4001e2c14719 | -6.89532 | -43.74345 | 2026-09-25 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d972b6d-b9b1-3ab3-8507-bf46064f664f | -5.47108 | -45.0949 | 2026-09-25 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6a4a80d-ef78-3667-9c37-b27c0c6764f1 | -10.92624 | -43.85576 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d4bae7a-b49e-3136-81f7-e1ee9671b3ac | -11.6576 | -43.51165 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4503c30a-e03e-391d-95e6-67ab11d5fb4c | -10.94801 | -43.88044 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bed26c73-b789-36d5-ab29-2ed6eb8253c6 | -6.79468 | -39.28612 | 2026-09-25 03:49:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 317264f7-d23e-3356-90fc-cef129f9312b | -8.33024 | -44.14242 | 2026-09-25 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 31708431-7863-3481-ac9e-0fbba2ecd49a | -10.95151 | -43.86054 | 2026-09-25 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c59450ea-e3df-3a1a-b892-d5dd975f5d44 | -9.99089 | -48.31298 | 2026-09-25 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3cb784f-3270-39de-ab49-0638a52142bb | -8.34 | -44.1427 | 2026-09-25 03:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| ddff6826-5288-3d41-930a-6743337245b2 | -11.7522 | -50.5494 | 2026-09-25 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 83b97af3-9474-3c1c-8596-c5ae44d26000 | -12.1685 | -50.7147 | 2026-09-25 03:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1c3f49b7-444d-3537-aa50-e195c1ce95bf | -11.7329 | -50.573 | 2026-09-25 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 24987d5e-e311-3e18-bb47-650dbe524445 | -1.1461 | -54.0996 | 2026-09-25 03:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| a4954573-798b-388e-a704-0658cbbc66bf | -5.7754 | -45.1053 | 2026-09-25 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 8742dbec-b17f-3e17-b110-9c3ef92cda22 | -9.1535 | -59.4834 | 2026-09-25 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| fede9346-05e9-3f35-89d3-2af055bb7dea | -11.7332 | -50.5516 | 2026-09-25 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| e1ae82c1-e198-3339-90f8-021253f6067b | -12.19026 | -50.74226 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0f38bdca-7e0e-3ecd-8a63-fdec607e207a | -14.51762 | -48.33784 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d5ca732-0837-3a59-96d5-7f3b3ad0e3ec | -18.42661 | -47.2035 | 2026-09-25 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5abf9798-7a39-3ef1-8138-73b845e07970 | -14.75019 | -45.58167 | 2026-09-25 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c731ae5f-a081-3186-81f9-808decda6c46 | -12.202 | -50.7504 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 465e2679-3064-3f4a-b472-f7ea629933df | -14.2192 | -48.50652 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95945e26-cbac-3161-9220-afa5e91776dc | -14.51833 | -48.33432 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bbdb4e97-2e0b-3945-a59e-285606be14ce | -12.2009 | -50.75585 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 11a6b9b6-fb41-3fdb-b54d-addf888a4b38 | -14.75735 | -48.47543 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2036f35-e3cf-321d-8cf5-1fba5df9f6d3 | -13.42771 | -43.87953 | 2026-09-25 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fb1e71f-8c3e-3852-ba2b-81d64eb0f83f | -12.19247 | -50.73135 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4ce35e78-9cb6-33e0-9d61-feb46ad80480 | -13.42704 | -43.88323 | 2026-09-25 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d84d6d36-8047-3873-878c-243b20b0e127 | -19.91516 | -45.53833 | 2026-09-25 03:51:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| feb4eb8b-1463-3669-94d3-6484c15be5c4 | -12.19157 | -50.77245 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 054eefcc-6402-3185-af7f-0d0688407d53 | -14.40087 | -41.61675 | 2026-09-25 03:51:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc785602-5521-3492-9a53-0dbc1163ff60 | -12.18214 | -50.75342 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3d992032-f6ef-3696-ba53-b21a2a644576 | -15.4982 | -41.55285 | 2026-09-25 03:51:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4ee6a906-dc54-3e66-a2b0-8b4ebf7b9cea | -12.17526 | -50.78628 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ac0c0593-6eed-377d-afa3-9d06589868d5 | -14.72719 | -46.22636 | 2026-09-25 03:51:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aec6872f-22a9-3b58-bb67-ca39bce51776 | -12.17457 | -50.75756 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3e59dac5-b79a-3959-90a3-923fd58c4ffe | -17.10349 | -46.46839 | 2026-09-25 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 762c3da5-412d-31c6-ae01-85034f1e22fe | -12.18252 | -50.78057 | 2026-09-25 03:51:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| f4d3d046-52ab-384a-b06c-500ca1eef4f6 | -14.51466 | -48.33545 | 2026-09-25 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c2457bd-f295-3991-b2f9-61a17fb3a506 | -14.67756 | -48.75925 | 2026-09-25 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1a7bab4-6a89-3f29-bff1-0f983a7f52f4 | -19.37794 | -46.32186 | 2026-09-25 03:51:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 023da369-0d41-30a9-bd39-bc1b5ea5ce73 | -18.60853 | -48.25777 | 2026-09-25 03:51:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README13.md)
