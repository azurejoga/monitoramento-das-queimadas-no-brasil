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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1cdcfd1-8e12-3533-88e5-1c748a80345e | -8.91342 | -45.29679 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 8dade6ca-b9a1-3717-aa12-cdc2c139dbc4 | -14.75073 | -43.61557 | 2025-10-14 12:19:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| d3423a8d-b76a-3847-8b0e-67f9402ccfc6 | -8.97518 | -45.37545 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 75cc9ed5-bc9d-3b7a-b9e9-80f8f264dff2 | -10.60592 | -43.64663 | 2025-10-14 12:19:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 584d6420-1563-3bd7-821f-c9ad210e052c | -13.40295 | -43.16221 | 2025-10-14 12:19:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| e3ddd620-bbcd-3ee7-9c67-06a74f3429c4 | -8.88902 | -45.26136 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 45fe15ad-94d3-3250-9ba2-41e056351c82 | -8.94662 | -45.3714 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 31d10998-3d32-3e09-a101-b4a213691fbe | -11.13391 | -46.06469 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 335ccbcd-dbac-324e-9b86-d405aad28e11 | -10.81959 | -43.94881 | 2025-10-14 12:19:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 38628ccf-d2b7-3317-9173-faa7717b8283 | -8.96282 | -45.39489 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1437.8 |
| c934399f-013a-3f34-ae88-b264d52d1ca5 | -8.89046 | -45.25082 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| c258b209-d7b7-3ec7-85ed-0c01099c27e1 | -11.12896 | -46.05806 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 23431305-c490-3255-8091-a4efe45fb2c3 | -11.33093 | -45.26601 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 55c9a0e8-dbaa-367c-a49d-c893d05c2a4a | -13.50351 | -51.3313 | 2025-10-14 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 76e0ff54-06a6-3887-aa9f-839c9a95a479 | -8.95083 | -45.34024 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 42bed570-7c1a-35bb-bcc5-89c5cce4c0d1 | -14.90384 | -46.03021 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 72393c03-2acf-39a7-b835-a5d417e9fe08 | -10.6078 | -43.63226 | 2025-10-14 12:19:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 2b957050-0e26-34a2-9dda-c20af9013146 | -8.95755 | -45.3624 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 1e48f6da-1a52-39de-8071-5f49696320e1 | -8.90529 | -45.28501 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 0b6ca4db-b016-3763-a1f5-6605bd1dd894 | -8.93596 | -45.30621 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 789.5 |
| 8e9cbec0-58cf-3617-93e5-4b406ca1b827 | -8.89716 | -45.2732 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.8 |
| e436c2a2-1b95-3e15-85b6-c73126d90d27 | -13.50511 | -51.32071 | 2025-10-14 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 62c4ea0d-0a8e-38c1-8c51-20bb7be6514e | -13.93758 | -48.70137 | 2025-10-14 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 39190457-9bf6-3fa5-bfd8-29f04fb2b942 | -10.82687 | -43.97713 | 2025-10-14 12:19:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 2a3b49dd-8ed9-33ae-874b-fdd669799ef2 | -13.50897 | -51.3274 | 2025-10-14 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 2a65c779-889b-35f5-8cfd-d0fb9c633f4f | -12.5964 | -43.38588 | 2025-10-14 12:19:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a43d660b-5f28-3567-b1b5-b61467a58adb | -10.15807 | -46.87584 | 2025-10-14 12:19:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d0c8ba0c-377f-37ed-b61e-6fd9cc96deb7 | -8.94522 | -45.38169 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 35b8f98b-1979-39df-af42-a31c7503f25b | -8.94382 | -45.39209 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 3a54e6fa-2b65-3449-9ad4-45d3f30c5821 | -8.97233 | -45.39626 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 7f437493-c062-3e2b-874f-3e99ac71a0ff | -8.95474 | -45.38306 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 0f2b4421-26ee-340a-8b9e-1123f9c3ea41 | -12.59325 | -42.95533 | 2025-10-14 12:19:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| eaf8d9e8-8e4a-31f1-aecb-63ee6da01e7c | -9.35621 | -48.67691 | 2025-10-14 12:19:00 | TERRA_M-T | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| db7a501e-bc98-3aaa-84c4-b58e991d4d20 | -8.94801 | -45.36111 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 5a396642-b976-39e3-80e2-387217c7ebd0 | -8.95225 | -45.32978 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 7c6219bf-ee6a-3991-95d5-226bc81bfd6d | -13.07697 | -46.946 | 2025-10-14 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 13304cee-392a-36be-9283-7df07f60fe7d | -13.17896 | -41.6377 | 2025-10-14 12:19:00 | TERRA_M-T | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 0643e191-11fe-3937-ad14-231e49bdadc0 | -8.92443 | -45.28762 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 516.2 |
| 2644daf2-7020-394c-a25e-b0523c947f93 | -12.255 | -47.43181 | 2025-10-14 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f0b712f0-6b68-3515-a081-194d730ad3e5 | -8.93455 | -45.31669 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 984.3 |
| 4b709ef7-2e01-323b-8e50-c293e445e577 | -8.96424 | -45.38454 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 0d128731-dde2-33b5-b59c-d75661f67679 | -10.34544 | -46.52042 | 2025-10-14 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a478980d-a89c-3393-831d-d7c7f2da2c12 | -8.96948 | -45.41705 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| b0989794-2f32-346f-8e3a-4540eb4a5a7b | -8.91631 | -45.27583 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 416.2 |
| 6bfc9606-44e2-3091-b35f-a5dafd8cbe6b | -11.13938 | -46.02369 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e01009cb-320b-3f9f-b4a2-69e609fcf351 | -8.64332 | -41.63651 | 2025-10-14 12:19:00 | TERRA_M-T | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 360009a7-0418-3957-a852-232f4ea8c117 | -8.93108 | -45.30986 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1410.2 |
| 752af11d-f2e0-3d55-a1d0-606d28524121 | -8.94411 | -45.318 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1075.4 |
| b8c36fab-a844-3513-af5f-0a748828dddf | -14.76536 | -46.15534 | 2025-10-14 12:19:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 33.6 |
| f3b8e97e-a295-3d03-8a47-5a552955e177 | -8.8986 | -45.26267 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 377.5 |
| 197aa77e-5a9b-3d17-bfbc-212b29326604 | -11.13253 | -46.07499 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 999b894e-fc28-376b-9220-67dbfbe41029 | -13.98032 | -43.27618 | 2025-10-14 12:19:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 3399ff8d-c1e2-3ba6-972d-13d50850cfeb | -8.9427 | -45.32847 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 713.1 |
| f40a54e2-d542-36c1-a96f-f8ff2c6f8c14 | -12.70607 | -45.12854 | 2025-10-14 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c6c77de4-5fbb-3ca8-9a00-32d43d36e031 | -11.13463 | -46.01706 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 60ac6399-1fbc-3158-baa5-18395cbde303 | -11.13801 | -46.03394 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c4bf8748-f3f8-3d22-bd38-36bc342d029f | -15.78618 | -43.86243 | 2025-10-14 12:19:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 20.6 |
| aa37d1b3-eb2f-31ae-a10c-a14ad09a9d7c | -11.33238 | -45.25483 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 87f8135c-310e-34ad-821e-bf3d05037bf0 | -8.93315 | -45.32716 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ae4b744f-a8c6-3c9c-a0fd-6e98fa817d3f | -11.14332 | -46.06593 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1af7aa24-bce6-344b-85b6-0acdbeafe638 | -12.71626 | -45.12975 | 2025-10-14 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 89203ace-5af6-3bee-bab0-ebead4438bee | -11.13559 | -45.86975 | 2025-10-14 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 472679d8-5cfc-339c-bdaf-79c01621cc6b | -8.96322 | -45.32063 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b27e5a16-a764-3e5f-8773-cd5aa2890dd4 | -8.94551 | -45.30754 | 2025-10-14 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| bc87820e-f622-3a6d-8e53-cdf7167a6b8c | -10.1398 | -44.54907 | 2025-10-14 12:19:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9b7aa0be-68b8-3db4-b1f1-a35ec80dcfd1 | -13.34128 | -42.37386 | 2025-10-14 12:19:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 35227e23-039b-3fc1-8c78-2a8780ca6594 | -13.8264 | -43.03033 | 2025-10-14 12:19:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |
| e0da6089-2d29-3062-9e54-87078aa80501 | -12.7238 | -45.1525 | 2025-10-14 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| a0b74ae1-b1cc-31cd-888e-547998e20545 | -10.8285 | -43.9717 | 2025-10-14 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9bc88a7d-8665-31ff-bda6-6b12bd50deaa | -10.8093 | -43.9744 | 2025-10-14 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 59074ffb-a705-3e81-9537-80eea52114b9 | -12.7242 | -45.1293 | 2025-10-14 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 016f5b86-d3af-32b8-9c29-97939cbe7c57 | -10.8097 | -43.951 | 2025-10-14 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 11335f9c-ddec-3c11-9d39-9471aad2d32a | -23.35917 | -47.51402 | 2025-10-14 12:21:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 5d8e8a11-0be2-3e4d-94a8-e248e093a5fa | -23.845 | -46.14754 | 2025-10-14 12:21:00 | TERRA_M-T | BERTIOGA | SÃO PAULO | Brasil | 3506359 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7ea561a4-bfb4-3f5c-aadc-450ac2afd4d9 | -26.07552 | -48.86173 | 2025-10-14 12:21:00 | TERRA_M-T | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 8f47a3bd-c1c6-3074-9ade-a3b9577ab98c | -18.75025 | -48.53713 | 2025-10-14 12:21:00 | TERRA_M-T | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 552c13a4-2237-3b47-988e-87f680c57003 | -31.11102 | -52.88065 | 2025-10-14 12:23:00 | TERRA_M-T | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 26.1 |
| 7b453426-9142-3659-80a9-60e32f804308 | -29.39542 | -51.51217 | 2025-10-14 12:23:00 | TERRA_M-T | BARÃO | RIO GRANDE DO SUL | Brasil | 4301651 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 95d3af4a-92af-3b8c-abb5-24cd036ebf44 | -27.0281 | -50.92331 | 2025-10-14 12:23:00 | TERRA_M-T | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ed1262f1-680c-3eff-a650-2677d03f7246 | -29.39401 | -51.52248 | 2025-10-14 12:23:00 | TERRA_M-T | BARÃO | RIO GRANDE DO SUL | Brasil | 4301651 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 13c2b787-6af2-336a-a625-e271e69e2b3c | 1.8768 | -55.7029 | 2025-10-14 12:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 157.9 |
| 913f9045-4a62-32f1-a966-1b936e4eb247 | -12.7242 | -45.1293 | 2025-10-14 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| cf4e1c44-cc69-3ade-8ffc-2f0d9343244d | -10.8093 | -43.9744 | 2025-10-14 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 6fa457d2-d654-3754-9028-fe06f0380ad5 | -12.7238 | -45.1525 | 2025-10-14 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 33e6c1a0-2f50-3442-bf59-40d4cc985b35 | -10.8097 | -43.951 | 2025-10-14 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| dc76059a-3d2d-3391-b22b-ba86b1282a76 | -10.8285 | -43.9717 | 2025-10-14 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b927ea16-7087-390c-abd5-2ec29253aec5 | -11.4389 | -44.0468 | 2025-10-14 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| c4c34973-fce2-3dcd-840d-b8b18180512b | 1.8951 | -55.7027 | 2025-10-14 12:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 05154f8e-4f6b-3e03-b0c4-b79f292a580d | 1.8951 | -55.7224 | 2025-10-14 12:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| fabf5eb2-ee17-3791-8404-caec3f3df898 | -11.4389 | -44.0468 | 2025-10-14 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 601d198a-596c-308e-a894-582a2cb866d6 | -10.8093 | -43.9744 | 2025-10-14 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 3d5620af-f146-359c-9545-16c2f84f3fdf | -12.7238 | -45.1525 | 2025-10-14 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 9099bb0d-b629-3721-81ea-a055c24c558e | -12.7242 | -45.1293 | 2025-10-14 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 226.2 |
| 15f8b015-2c9f-3002-bb54-19825b77c249 | -10.8097 | -43.951 | 2025-10-14 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 66158401-dbec-3bfe-bba0-62fa511e2039 | -10.8285 | -43.9717 | 2025-10-14 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 44707c56-a668-3d06-b832-b03d67d64719 | 1.8768 | -55.7029 | 2025-10-14 12:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 5f70c109-ad5f-344a-b50a-99e77c790e94 | -10.8093 | -43.9744 | 2025-10-14 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| f866b7d0-16c1-307e-8c0b-3e60e1b6f92e | -11.5255 | -43.4922 | 2025-10-14 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 4c93ae95-f25c-373b-b51c-47f098fd5d88 | -12.7238 | -45.1525 | 2025-10-14 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 41a7321c-c3b9-30bf-83a9-d0ddb9602504 | -11.4389 | -44.0468 | 2025-10-14 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |


[Clique aqui para ver as próximas entradas](README41.md)
