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
| 613d6ac7-ab66-39ed-bc19-3d14d7162da7 | -2.44522 | -52.2264 | 2025-12-16 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80001174-3370-3ef1-901b-c79be2e51a33 | -3.08249 | -44.88713 | 2025-12-16 04:44:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c99761d8-e211-30b4-9d63-f852120b6371 | -3.43413 | -41.64883 | 2025-12-16 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1eb457db-f00a-3eef-be22-8b3057a70bb5 | -1.61029 | -45.89674 | 2025-12-16 04:44:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb543fab-d9ab-39b2-ae19-534923a4ca6e | -3.43365 | -41.65199 | 2025-12-16 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| b21ecd60-2a8d-369b-8124-4b3f3b0a5270 | -2.79148 | -51.40895 | 2025-12-16 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23523280-cda9-33ee-b2b0-0bbf3fabb29a | -0.85229 | -47.5708 | 2025-12-16 04:44:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| def0d30c-09b7-3e50-9eeb-9cf523434b69 | -2.91291 | -49.08914 | 2025-12-16 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1d43f4b-fee6-391f-9c81-ecbefc86c228 | -1.33556 | -45.82328 | 2025-12-16 04:44:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01434c88-ad2b-385b-beb8-04ea04e9cf1b | -3.15223 | -48.14246 | 2025-12-16 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78e7bed7-6dc1-3ff9-88ca-52f35c4e069e | -1.09191 | -47.4967 | 2025-12-16 04:44:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fbbccb1-8a9d-3dac-910a-81bf1f316c3f | -2.79482 | -51.40948 | 2025-12-16 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4884412-6ede-3f13-a181-4c485b6fa46a | -1.91882 | -46.50011 | 2025-12-16 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff94fee8-6c90-3dc1-a5d3-902cc0bc24b7 | -2.50332 | -48.03438 | 2025-12-16 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aa31031-5a48-36d9-b236-82bca412a325 | -2.47282 | -47.02328 | 2025-12-16 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35b952e6-be1d-3a4e-933e-095aef5d6769 | -2.66779 | -51.64703 | 2025-12-16 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2a31ec2-8198-303c-a44b-e61b648f0a03 | -3.42796 | -41.6548 | 2025-12-16 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 5b51a1d2-7378-33a1-a880-1ba90c7ea2ca | -1.84662 | -46.39139 | 2025-12-16 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 376ab430-6b87-3496-b6f8-4c43e4aa7af5 | -3.42842 | -41.6512 | 2025-12-16 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 6d7db251-8dc5-39fc-83dd-76810f42449e | -2.83638 | -51.81261 | 2025-12-16 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ceaf6d51-9d4a-31ab-8860-0d0fe27f99b8 | -1.16379 | -53.65659 | 2025-12-16 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f181acb2-4368-3c90-a4f0-9b8161720253 | -2.22765 | -51.94048 | 2025-12-16 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9db6d92c-e523-32ec-8f2b-c20c0d644680 | -2.44865 | -52.22694 | 2025-12-16 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b36fde6a-f30d-3b19-b9b1-c2382519d2aa | -1.84845 | -46.38972 | 2025-12-16 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f92da105-6869-3464-92a6-b2b5a08b24ec | -3.14876 | -48.14192 | 2025-12-16 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9635bd54-22c5-351a-b9f6-2a574dce0a8c | -0.84882 | -47.57026 | 2025-12-16 04:44:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 39a5762a-6ad5-3f03-a2f6-f94b5503c76c | -2.44464 | -52.23011 | 2025-12-16 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34758f9e-be8e-3e1e-bc72-345536fad8e8 | -2.39616 | -47.16017 | 2025-12-16 04:44:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c21be395-fb08-3af8-9215-2916abf9c0c1 | -0.85289 | -47.56699 | 2025-12-16 04:44:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cba7c34-dc52-3b13-ac7b-0d4edcb6f1da | -0.84822 | -47.57407 | 2025-12-16 04:44:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8e5a8aff-3ef4-3251-b1cc-fe463c59035c | -1.30267 | -53.3987 | 2025-12-16 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 392e4118-7ebc-34fc-9f14-a1b7ebb8d4f5 | -2.48954 | -49.31606 | 2025-12-16 04:44:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22f03db3-4a4c-3f44-a58b-897837caadd4 | -3.32828 | -44.86086 | 2025-12-16 04:44:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf54f237-0d45-3456-93c6-82648b6fa4bd | -3.42793 | -41.65436 | 2025-12-16 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3294f701-9222-3546-9758-5b761b96d492 | 0.79066 | -51.96771 | 2025-12-16 04:44:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6d58e88-b346-35b3-a612-7c7cc05d62a1 | -2.48566 | -49.31904 | 2025-12-16 04:44:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57efebd2-3caa-3168-a02e-c45286fb58b6 | -1.29317 | -52.82759 | 2025-12-16 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8af9ca56-3d8c-3397-9bb3-d96432944737 | -2.50214 | -48.04198 | 2025-12-16 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b6f3b93-1c1f-3af1-919e-2fe41baec992 | -2.85123 | -46.80575 | 2025-12-16 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cc782b9-d2a1-3366-96fb-ccf04b9325e7 | -0.84535 | -47.56973 | 2025-12-16 04:44:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f7890068-460a-35cb-999c-5c443922c120 | -3.14698 | -48.15336 | 2025-12-16 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4772c7d5-7ce5-3c12-886d-ba25c3448120 | -2.80788 | -49.13076 | 2025-12-16 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd8842a1-87e3-3503-a45a-47e83427b804 | -1.92253 | -46.50068 | 2025-12-16 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 794f5ff0-2f5e-31c1-afc3-3168e224e449 | -0.89824 | -47.55048 | 2025-12-16 04:44:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f50f612e-6aea-35fc-bd6e-67aab6cc1bb7 | -2.8111 | -48.64642 | 2025-12-16 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60574120-0cb4-3e83-9660-992a183b84ee | -1.42836 | -53.47868 | 2025-12-16 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bee80688-8b80-3efd-841f-badbef9456e3 | -1.84777 | -46.39416 | 2025-12-16 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 64397074-42c4-34dd-bee5-fab41da3ebca | -3.14757 | -48.14955 | 2025-12-16 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b89435a-e10b-3538-8a2d-99adc6a4eb2f | -3.42842 | -41.65163 | 2025-12-16 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 033837f4-a29e-37d6-9b55-cc5a7427ed7a | -1.33864 | -45.82861 | 2025-12-16 04:44:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dcac1cb-4baa-3953-8132-67f987827591 | -3.35474 | -46.86024 | 2025-12-16 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bee2a4c5-9241-310b-97a7-64b6646fac8f | -1.66852 | -45.79916 | 2025-12-16 04:44:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4034d781-21d8-378b-ac2f-61646bbe4d49 | -2.81179 | -49.12774 | 2025-12-16 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19f32ed7-0999-3954-9785-68726bdf05a1 | -0.84942 | -47.56645 | 2025-12-16 04:44:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f54e8f9-86e9-3af5-a556-b78b128be0a6 | -1.25777 | -47.18003 | 2025-12-16 04:44:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d903051-b246-3796-b12c-2ed72e5b69d6 | -1.63163 | -55.38372 | 2025-12-16 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 240dad85-8935-3dfb-a1d8-57f0e7b239e0 | -1.60263 | -45.89561 | 2025-12-16 04:44:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffb57a57-041e-3483-929a-4c8b70823efe | -2.48287 | -49.31503 | 2025-12-16 04:44:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ab660c3d-319e-3984-a822-fe238948fe9a | -2.66836 | -51.64347 | 2025-12-16 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b15d8b95-7fa3-3e2b-9fda-fe7364144cd7 | -2.665 | -51.64294 | 2025-12-16 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e41fd0bf-26b4-378a-832b-811337968272 | -3.64888 | -44.25887 | 2025-12-16 04:44:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56124938-a832-3b3d-aa35-f6dee8912681 | -3.56828 | -47.17418 | 2025-12-16 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64c18b08-506e-386f-8f4d-4acf761199d3 | -3.43412 | -41.64926 | 2025-12-16 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 85febcdd-6917-39d8-a364-3c10e775e999 | -3.56397 | -47.17545 | 2025-12-16 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acd9d764-5b9b-3f30-9391-844628d5444d | -3.24839 | -45.35828 | 2025-12-16 04:44:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c7bd5b4-2a19-3752-947d-86d712ad0ec1 | -0.84475 | -47.57354 | 2025-12-16 04:44:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5e6afc21-2d75-31c6-bbd7-586b73354d4f | -2.99296 | -46.92646 | 2025-12-16 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 800f4d18-f01f-3ba5-9ad0-61b22ec0b001 | -2.80844 | -49.12722 | 2025-12-16 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb2da81b-1d86-3495-b8e2-2016099aee7b | -0.85577 | -47.57133 | 2025-12-16 04:44:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a0ca98d-2a36-397b-a882-540450b431e0 | -3.42888 | -41.64846 | 2025-12-16 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c7a8d1bd-9d7a-39b2-aae2-178e466ee3c7 | -0.84595 | -47.56591 | 2025-12-16 04:44:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ec88966-8a53-37e4-b8e2-703774f5358f | -2.66941 | -46.89 | 2025-12-16 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0cd225f-3448-3385-a787-e4aacf6a96d6 | -2.809 | -49.12368 | 2025-12-16 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa5b0d43-1b0c-365b-95b2-7bd8e3500d9a | -1.60706 | -45.89912 | 2025-12-16 04:44:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 99705394-0f2e-3f72-8fe1-b5b8db193924 | -1.84964 | -46.3964 | 2025-12-16 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2a533610-3e1b-359a-a3cc-f0e81bbeb658 | -3.02675 | -49.05567 | 2025-12-16 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 125082bf-08cb-3cb7-98ae-d17dcafae8cb | -2.47644 | -47.02389 | 2025-12-16 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa0dbbb3-ab8f-3e99-87a5-b6240c3aa8b6 | -2.79537 | -51.40597 | 2025-12-16 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba96be41-e4b0-3285-a7d6-ef507dce5a81 | -1.26131 | -47.1806 | 2025-12-16 04:44:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36b32abd-12ee-3c2b-b715-c0bb12b3f14b | -1.67162 | -45.80454 | 2025-12-16 04:44:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fcb60be-02e7-3080-9604-da12efab9fd2 | -2.66508 | -46.89377 | 2025-12-16 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afd8eb68-37dd-362a-bffc-94036b8dfea9 | -1.60323 | -45.89856 | 2025-12-16 04:44:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 635c674f-888f-3265-94a2-6ce433b6ddd2 | -2.76393 | -52.117 | 2025-12-16 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7298f586-bdf4-3281-8d85-e3cdd45f8c73 | -3.56762 | -47.17599 | 2025-12-16 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b9ab7c8-5703-3080-bd13-90a391c7e021 | -2.45592 | -52.22378 | 2025-12-16 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9d4fed1-433c-31cd-8a46-b37e530c1c12 | -2.67115 | -51.64756 | 2025-12-16 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4482d6d4-8016-39fb-bd72-67ab002d1986 | -1.60957 | -45.90143 | 2025-12-16 04:44:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d972878d-a1aa-3c0b-8b66-e970c27b5bdd | -2.1672 | -50.26332 | 2025-12-16 04:44:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afefd364-7452-3b15-9399-cca198f41f59 | -2.48233 | -49.31852 | 2025-12-16 04:44:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8286af2d-0370-363a-92f0-7dfacc51a1d2 | -1.60631 | -45.90379 | 2025-12-16 04:44:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11bae0c0-88b8-3050-b7e8-cce373e9999d | -2.66443 | -51.64649 | 2025-12-16 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adc44150-803b-333b-8130-92c031a67c6c | -1.36216 | -46.99641 | 2025-12-16 04:44:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39a15f80-3d8f-3cab-bba2-a75c8632f0eb | -3.15163 | -48.14627 | 2025-12-16 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22c3bac3-f15e-37f2-a96f-af7a44514605 | -2.66574 | -46.88947 | 2025-12-16 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 386fe3fa-d183-3ee8-8f87-706e45653be9 | 0.08108 | -49.89207 | 2025-12-16 04:44:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 28bd790d-6e9c-3927-93ef-267c15d326df | -2.48342 | -49.31152 | 2025-12-16 04:44:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8893acf9-843c-3e46-beef-252655b511bb | -2.48675 | -49.31204 | 2025-12-16 04:44:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e97a3b1-ead3-3ce1-ab66-be56b92709ca | -2.02393 | -47.14083 | 2025-12-16 04:44:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f623975a-babc-3250-afc7-1eca3a547d8e | -3.00377 | -41.87376 | 2025-12-16 04:44:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 0f8620d1-98e6-3645-b566-11a9c425ae34 | -1.725 | -47.15718 | 2025-12-16 04:44:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
