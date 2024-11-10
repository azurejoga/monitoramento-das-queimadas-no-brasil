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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0b5fb76-d457-3a59-b5cd-30ea3933fab7 | -2.2315 | -48.48319 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45634bae-f4cc-3ff6-903a-798b2d7219b5 | -2.20326 | -48.85353 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e83185c2-9357-39ab-bb54-f2c99e3ce109 | -2.18805 | -48.37061 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 191946b3-f500-33a5-8975-a79374dded7c | -2.19094 | -49.12537 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7aa3d65-02c8-385d-b9cc-7f82e2cc28e5 | -1.22807 | -54.17583 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77d71d95-e7f4-33bd-8d42-cf59f52af84a | -2.1995 | -49.28773 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b4e174a-e392-35bc-9ef5-49aa44f17942 | -1.84595 | -46.28841 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a705cfa-f971-3a27-99a3-d179c870597c | -2.08156 | -50.33897 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41978554-dcbf-37bb-8c6a-730af862e697 | -2.1427 | -49.00381 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9adbe033-2a7a-3010-a005-98ebf5e1175c | -2.42213 | -47.83048 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0269d0b3-e86e-371d-b4a2-5fb8dd0310c2 | 1.6161 | -56.05552 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 438ff7ba-894e-3ad6-bdc0-f94b92fcdaf7 | -2.2273 | -46.84603 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0873cac0-150c-3284-b5be-ba6fe289240b | -2.34096 | -48.94633 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecd2139a-9f1f-3c5f-b92d-359b74c27f66 | -1.94953 | -51.10033 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ca3a618c-8c20-385b-9a89-c93929ed51ac | -1.14045 | -47.82614 | 2024-11-10 04:36:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 184b3e69-9f3d-3f83-891b-3cc2d21cc7f8 | -2.5688 | -46.5336 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ea9feda-4250-30b2-8e4f-d8e6ba15ac82 | -2.20023 | -48.37956 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e05d5537-a330-3e62-a71a-9f3b1e8a20c9 | -1.22823 | -51.96404 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c96aa95b-69d6-3f53-b8ea-ee8be4d43c5a | -2.56627 | -47.33705 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0c87f7d-fb23-30b5-b947-315a5a562af7 | -2.18419 | -48.37354 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b3303e0-8fa7-3e4e-8abc-58cc2965ac82 | -1.3852 | -52.18999 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96210714-b2d5-3d2f-a1c6-4cef480e2d5e | -2.05319 | -48.51907 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5aeb79fd-e454-329e-88f2-4fe2b96921bb | -0.89764 | -51.78619 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 227e2995-b1a3-314f-b3f2-be5eee70fbc3 | -1.93172 | -47.84977 | 2024-11-10 04:36:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ff9030c-f9f0-3130-b2c5-6b6bf96d0150 | -1.18361 | -54.20434 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b866d077-a8b0-3589-a510-06e354232134 | -1.20204 | -53.6269 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 495543d5-c14b-368c-aea4-324597b37da6 | -2.20409 | -48.37663 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c01d3008-86ec-342b-a38b-6e80f323eb69 | -1.1339 | -54.20908 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 964bcfd8-9fd0-307a-b733-73c5b8d06f0e | -2.13713 | -46.68694 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e1c62a4-51dc-347c-8213-c371ed35adb2 | -2.04511 | -46.31841 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a9b051b-8409-32cc-bf6b-356104bbd413 | -2.00563 | -48.39154 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca6c7079-acf6-3f29-8c17-c4cc09350bfc | -1.53589 | -52.21646 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 434b4d9a-5a0e-31f1-8dc0-cb4682baacc7 | -2.9067 | -45.14845 | 2024-11-10 04:36:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 622bd282-0bfe-3bfd-8d4c-44af596afb6f | -1.28055 | -54.13281 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a43db93-05e5-3577-aca1-3802cda3f835 | -2.46001 | -46.31911 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb9949a9-3afb-35c8-9095-e19f259810d2 | -2.39829 | -46.80165 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7b12326-c196-3e63-8133-5874c9003b2c | -2.20294 | -48.36234 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6924ccf-9a91-3cb9-a0b0-d3e8dbd1f57f | -1.6813 | -48.04428 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddcf6edc-1226-3d5b-a807-b84b8b006e9e | -2.14396 | -46.7103 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23eaca42-d90d-38a7-8f52-cd87de2ec4e3 | -2.14777 | -48.79876 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc84512c-b00f-3c5f-ab3c-d86b0ca32829 | -2.31202 | -48.55227 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b78d9cde-0c82-3dda-be00-47f61498bce3 | -2.56141 | -46.54057 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd7bf4bf-11ec-37ac-885a-03f3d1f5dbf6 | -2.18696 | -48.37749 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e2e7efe-a409-3aa4-bb27-396c1d15ebaf | -0.04563 | -50.77989 | 2024-11-10 04:36:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5e6e2b5-6657-3b88-a3d5-f9243255e79d | -2.52811 | -46.30176 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2724339f-92e7-3f98-92d1-c57fe2952012 | -2.17166 | -48.43155 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 107bb705-ebff-3ea9-b06f-9d69332d9695 | -1.42674 | -52.27237 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 767d83a1-a23a-3206-8fc4-16fb3d8a9a02 | -2.07418 | -50.34937 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e0a097f-3b6e-3120-a40e-ecca9245c1db | -1.33185 | -54.59564 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2c9133d-6275-3e30-9d9d-7059716187e9 | -0.04438 | -50.78799 | 2024-11-10 04:36:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a70747c8-ab95-334a-a88e-eb56cd42a0d8 | -2.54925 | -47.32691 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edddc311-79f2-35ee-9fc3-107aac81f09c | -2.31751 | -48.53901 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32c7bc6d-64dc-34e1-ac1c-1e7f87b98fd2 | -2.22763 | -46.62226 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d5bf962-7787-38d2-9da6-7b84763c7bdc | -2.31805 | -48.53556 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 573a052f-d5a9-35f9-b798-d542789e75c3 | -1.45812 | -52.33725 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd4bea4b-fd49-372f-b008-36facd417b7a | -2.08334 | -48.82429 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36504403-dccb-305c-a417-74fee560999c | -1.53282 | -52.21126 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2322d13e-2a7c-3253-917e-7773d92afb69 | -2.2171 | -46.82221 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95abd4ad-4109-3a1a-814d-a5435ea0a644 | -2.1783 | -46.42176 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4039dd64-f4f9-36fa-b080-3c087e0c87d8 | -2.21009 | -47.73731 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1e0cd037-b76b-31c0-b390-67b4c5afb9c9 | -1.51123 | -52.15154 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1db4610c-6b6c-3736-bf29-148ba8927b81 | -1.72728 | -51.16249 | 2024-11-10 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 611f2422-031a-3f1b-beef-5c7910e42aa9 | -2.30583 | -48.33254 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 408c2b26-9e6e-3fbd-996c-746c2e94d954 | -1.23083 | -51.75546 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8756f38-4ced-31ba-8906-5446987dba74 | -2.2284 | -46.55079 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 654a38e4-a38a-3d33-a6f7-709b91c33a5d | -1.34645 | -51.40518 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3c9d389-bd08-30b6-8321-e1c299e00247 | -2.30529 | -48.33599 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8891b39-241d-3ce4-a14b-fe4cdbbe72e3 | -2.37395 | -46.73453 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8e51af7-3416-3936-80a9-c45bcf4c3fb0 | -0.84989 | -47.6497 | 2024-11-10 04:36:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cef21378-8291-38e7-bf20-9c473d9de2b8 | -1.52404 | -52.49975 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5924d284-f630-345c-aceb-774360838ee3 | -8.39393 | -44.16315 | 2024-11-10 04:38:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| e97becb3-47e0-3edd-9b47-b612c1627db2 | -8.38364 | -44.12729 | 2024-11-10 04:38:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 449.1 |
| b2a5ff28-0a7b-3e6b-aefb-6fb309efe80d | -11.07607 | -43.34669 | 2024-11-10 04:38:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 82db40bd-ee70-3d3d-a51c-e5edf2b084cd | -8.37729 | -44.13114 | 2024-11-10 04:38:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 234.7 |
| 839e471c-25e2-3b8c-b532-b3d5a052b8f3 | -7.43019 | -39.75757 | 2024-11-10 04:38:00 | AQUA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 21.0 |
| d37620ca-a0b5-38ea-a8ba-6ecc9972b4b7 | -8.37792 | -44.16043 | 2024-11-10 04:38:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| d18f73a0-1db7-3b75-9760-045e6c0237c7 | -11.09483 | -43.32371 | 2024-11-10 04:38:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 8f77843c-1d30-339f-bd0e-1f2b73c5a839 | -8.39963 | -44.12989 | 2024-11-10 04:38:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 328.6 |
| 664af6f3-1eee-3392-90b9-6cc2ae2c17b2 | -9.59814 | -36.02689 | 2024-11-10 04:38:00 | AQUA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| a593b254-9d68-3b60-9b32-d521d1d32aed | -11.08058 | -43.32111 | 2024-11-10 04:38:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 538fcec4-6d63-3d0e-9491-5948ca90c35e | -8.39328 | -44.13377 | 2024-11-10 04:38:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 374.1 |
| a2617cca-f332-362b-b693-7b92a2949d11 | -8.41562 | -44.13248 | 2024-11-10 04:38:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 640cbc0a-5560-339c-bfb3-d0d787c9514a | -8.40928 | -44.13629 | 2024-11-10 04:38:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 60e59eff-f892-3c94-8ca3-da0ee22a55c1 | -8.36767 | -44.12455 | 2024-11-10 04:38:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 4aa886db-442c-3467-ae91-15d47d496733 | -9.59952 | -36.01783 | 2024-11-10 04:38:00 | AQUA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 9b556021-dfa9-37c3-aa59-c718c7622b8b | -4.32137 | -45.64151 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67096faf-074e-3ca9-b668-ad400b833a85 | -3.83323 | -54.59873 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 549e4a8c-4ef0-3684-a67a-f24077cb36fb | -3.02611 | -48.03488 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30c7322c-0237-3b1a-a8db-63b2301682a6 | -2.30914 | -50.67046 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8f25833-fad5-3542-b5c2-592900ecef23 | -2.72601 | -51.73645 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b3e0272c-0fab-33ca-9b17-b73be9eb9731 | -2.44307 | -50.26501 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 754e4824-3543-3667-9e77-c353102949f8 | -4.0329 | -48.28029 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 918a7a20-9659-3775-bc21-1fbad72382f9 | -2.85947 | -49.22316 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ada5083-ab6d-3393-9f49-76bdda97544d | -2.39118 | -54.09731 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5482b09-b2cb-306a-90d1-86948f4e1893 | -4.36033 | -47.22442 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88eb631d-304a-3293-8742-559b5d0ca3d0 | -3.23799 | -50.45173 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 139d0269-fa14-3a03-8271-1c583437fcac | -3.88819 | -49.92329 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e1420d8-49ba-3318-8af2-964b3422fedd | -3.31208 | -51.66625 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9564ea82-d94f-36a8-802d-7fd1344907c6 | -2.58492 | -51.92275 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28afad1a-4ad9-351e-97ca-7c4203611a37 | -2.95328 | -49.57475 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README74.md)
