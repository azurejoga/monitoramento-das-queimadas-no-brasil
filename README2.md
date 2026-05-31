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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d7798ce-72b6-3d4b-9fe0-6f2c8c582bb6 | -12.32547 | -47.89739 | 2026-05-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 847d5b23-098c-363d-810c-e7f2940052b9 | -10.07839 | -51.66392 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 9d0b2042-77b7-3abb-8573-c368ab147567 | -13.70591 | -52.96365 | 2026-05-31 00:28:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b355358-a53f-34aa-a743-e4339c8b0ce7 | -10.07704 | -51.65448 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3927e69e-e0bb-32cf-bfa2-2ae584b19bae | -10.79461 | -46.91759 | 2026-05-31 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| fab4620f-0e67-395c-8ff4-782b5dad78e8 | -14.0283 | -58.15099 | 2026-05-31 00:28:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2b96f62e-678c-3a57-9be9-7b49e1ae3a2e | -7.99411 | -55.52951 | 2026-05-31 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b1d6a155-4da7-30dd-9ae6-b5bf5f70c370 | -11.62786 | -55.17695 | 2026-05-31 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1a597c4d-7058-3204-a97e-b52144085a39 | -7.50939 | -55.01128 | 2026-05-31 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4c179ed6-a5ce-3dd2-8d4f-8a2bbba547b9 | -10.06798 | -51.65586 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 221.3 |
| 720f9915-7968-3e3b-97b3-8c860ee80ffe | -7.50814 | -55.00206 | 2026-05-31 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6b76f629-c902-3e7c-b34f-9591ac583034 | -12.90834 | -52.52114 | 2026-05-31 00:28:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a3e7284a-7a5a-360a-a5e8-bcd50b15a259 | -9.49286 | -48.65718 | 2026-05-31 00:28:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2aa97dba-8937-3d26-a6a5-4eb170c2b5e8 | -8.72898 | -48.31956 | 2026-05-31 00:28:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 9f63b7aa-6fa7-38d9-89c3-9ac8d9003365 | -12.80749 | -54.86789 | 2026-05-31 00:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b72627c4-cd8c-30b3-a13f-c54432b81666 | -12.90958 | -52.53013 | 2026-05-31 00:28:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 587e7122-0c4f-3843-9c76-c7c1b2f8de1a | -10.06163 | -51.67606 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 98a5378a-6c58-3dfe-8993-f8b17554663a | -10.78946 | -46.90528 | 2026-05-31 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 18f53f88-5200-3b9d-a2a2-7d2377e91482 | -11.78603 | -54.01828 | 2026-05-31 00:28:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4661e570-6864-311d-9c75-84adb3500fe0 | -8.72863 | -48.32931 | 2026-05-31 00:28:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 01e7fcb0-c59c-38b1-971e-2b4725df2ec1 | -9.44859 | -51.83839 | 2026-05-31 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ed9eb2bd-b5e2-350b-822d-4b4d6401be51 | -11.57481 | -54.57861 | 2026-05-31 00:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c611b6f9-8b2f-3f7e-93b8-7a400e257cf3 | -8.72617 | -48.31352 | 2026-05-31 00:28:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 8bf4ceaf-7a55-33ff-9b8b-d9fdb2363bef | -10.07569 | -51.64503 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 23d1724b-5a1d-3223-a12f-7d717f39a46b | -10.07069 | -51.67472 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| d68762cf-b745-37e1-8b50-9dad8daf26d4 | -10.85688 | -53.75218 | 2026-05-31 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d1973458-35c2-3173-b226-f510c286a926 | -11.79502 | -54.01701 | 2026-05-31 00:28:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| abb7bac1-fba6-3307-8b4e-220ae28d2458 | -10.79234 | -46.92369 | 2026-05-31 00:28:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| cb63e87e-6e2c-3211-8048-15a6ad518df7 | -11.63253 | -55.17059 | 2026-05-31 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6504a693-189d-3114-b502-27c0dd62460a | -8.73132 | -48.33537 | 2026-05-31 00:28:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 08abbb0b-a5d3-36f4-8918-d47712de9eb4 | -10.07339 | -51.69358 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f17ada8b-f1fd-3a77-a078-b76828b0b1c6 | -11.74271 | -54.79889 | 2026-05-31 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1d08ae05-ff4b-366f-b724-adb97cd8364f | -10.06298 | -51.68551 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 33ccdaf5-c22d-3a1d-8e9c-44fb01119b0f | -9.4563 | -51.82766 | 2026-05-31 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 15d2a5e6-1e8e-3b03-8034-efcc946c7145 | -10.07204 | -51.68415 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 453b60d0-15a1-3178-aa62-5f5dad3ffbd7 | -14.05253 | -58.14799 | 2026-05-31 00:28:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 06f9818d-1e29-3ab6-a6c5-045655f44fec | -10.06933 | -51.66529 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 353.1 |
| 17ab1e7c-66d4-3095-aa2b-bf57a862a9f7 | -9.44724 | -51.82898 | 2026-05-31 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e5d1bfd0-ae98-35f3-8d19-f8b142ec0bfd | -12.31436 | -47.89925 | 2026-05-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 031f4850-1e44-3d03-87f6-342303244e71 | -12.31663 | -47.91386 | 2026-05-31 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c0172c40-35c7-355d-97d1-1049107e73d6 | -10.06027 | -51.66663 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 221.4 |
| 1933555e-244b-3fad-a3f0-e2b00fd6ffbe | -14.02371 | -58.15713 | 2026-05-31 00:28:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 57cd33c9-1136-3291-8c21-b3e2ad80478d | -7.49914 | -55.00333 | 2026-05-31 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 4f5242e8-c0ce-38e3-bfbc-39fcc2856eea | -7.99927 | -55.51295 | 2026-05-31 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 3eed2c65-0e8b-38a6-93aa-3a47a3629813 | -10.07974 | -51.67335 | 2026-05-31 00:28:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 94366227-adab-3046-b394-3744cc86305a | -13.70715 | -52.97275 | 2026-05-31 00:28:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e65ddc7a-7e46-3bf5-ace6-bab15c65a043 | -8.7399 | -48.3205 | 2026-05-31 00:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| cf827fcf-f2a1-3fb6-aa41-c3be5258da3a | -6.5631 | -51.1126 | 2026-05-31 00:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 5fd6886f-99d9-32c3-a6c2-ccf7d8a42135 | -10.0723 | -51.6769 | 2026-05-31 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 294.8 |
| e7de1e9f-50f6-37ff-80d3-853310a99ddc | -8.7211 | -48.3222 | 2026-05-31 00:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 91617ae7-f4e2-3ff9-8e6d-a0d181cc9d03 | -10.0725 | -51.6559 | 2026-05-31 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 440.1 |
| 652ed7ea-40ab-375b-93dd-400c4d5b8aa4 | -7.9949 | -55.5169 | 2026-05-31 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| fbb05aba-78d0-338a-9f15-10a433a3a40c | -10.0537 | -51.6576 | 2026-05-31 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 159.3 |
| c2d9c237-3e32-3da0-ac79-6b19197d2a47 | -10.0534 | -51.6786 | 2026-05-31 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 81f8ef1c-dc0f-38c4-9fa3-c61c6f00bbbb | -10.0728 | -51.6349 | 2026-05-31 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 9c50352e-286c-3b17-b55d-0c9eedee03a5 | -6.79952 | -59.04232 | 2026-05-31 00:30:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2d3dc205-3a83-3e50-bd25-2a7fb9758d48 | -6.04166 | -47.89602 | 2026-05-31 00:30:00 | TERRA_M-M | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3c3ee7ef-4120-3e8c-adee-4156d1d07675 | -7.0844 | -46.284599 | 2026-05-31 00:36:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d610daf7-31e3-3a10-bca8-834d33cfe56d | -7.9989 | -55.514099 | 2026-05-31 00:36:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bb2e76e-8f85-3a70-92a1-1b568c82b977 | -8.263 | -48.227402 | 2026-05-31 00:36:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f208e281-e1ee-315e-97a3-640d5ca34dfd | -6.8454 | -47.932499 | 2026-05-31 00:36:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b049b6d3-5492-3b74-ae15-de7d6fd7f0fd | -6.8439 | -47.925598 | 2026-05-31 00:36:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21354c67-c9eb-39fb-a245-cebbcc80d66b | -7.4934 | -55.002602 | 2026-05-31 00:36:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8f4499f-5a88-33dd-9f11-b8ff37ca1cac | -6.0513 | -47.8867 | 2026-05-31 00:36:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d195d3c-3564-32d7-9ee1-6a3a5f66fea1 | -7.9923 | -55.5313 | 2026-05-31 00:36:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62c81bc4-d8a9-33e2-b472-a107129deae6 | -7.9892 | -55.516102 | 2026-05-31 00:36:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5edb31c-6f78-3b73-9b44-0bd6cc18d71e | -8.2645 | -48.234299 | 2026-05-31 00:36:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e8f28a8-ae8b-345e-8171-22bb24877e8c | -7.986 | -55.500999 | 2026-05-31 00:36:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 966b6ce3-41cf-35fd-9c9a-d206840b07b0 | -6.0529 | -47.8936 | 2026-05-31 00:36:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e739678f-e07f-37c3-a5b8-10970291009e | -7.9957 | -55.499001 | 2026-05-31 00:36:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b337c93e-bb68-34fb-b9a0-3cbedfc4c13c | -7.5032 | -55.0005 | 2026-05-31 00:36:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c26e321a-f4ba-3035-bd4c-16feb669c8f0 | -10.0537 | -51.6576 | 2026-05-31 00:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 169.9 |
| 05549228-da0a-314d-8c01-49b84abef185 | -10.0728 | -51.6349 | 2026-05-31 00:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| d27cb9de-16c5-3909-882b-08926873c427 | -10.0723 | -51.6769 | 2026-05-31 00:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 269.4 |
| 6dc523a1-b1b6-3445-9e88-930972cbc518 | -8.7211 | -48.3222 | 2026-05-31 00:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 81063535-4744-30a8-9317-c2b4dd507392 | -10.0725 | -51.6559 | 2026-05-31 00:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 382.4 |
| 616a8119-c8b6-3746-9e9a-069a08cd0346 | -10.0534 | -51.6786 | 2026-05-31 00:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 235552b3-bf49-3076-9fcc-fc4c3cee08dc | -8.7399 | -48.3205 | 2026-05-31 00:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 5ad61d90-27fb-376d-8026-2bb8e2b6f4fa | -7.9949 | -55.5169 | 2026-05-31 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| ce4058f9-8e1f-379d-a685-45fc94f4fa5b | -10.0723 | -51.6769 | 2026-05-31 00:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 273.1 |
| 31213806-6580-3900-ab20-960e0c6d73d7 | -10.0725 | -51.6559 | 2026-05-31 00:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 398.4 |
| a09ba173-1c96-3f92-8ab4-2ceffe367d50 | -10.0534 | -51.6786 | 2026-05-31 00:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 70085d73-8346-3420-9caf-05fb58648cfe | -10.0728 | -51.6349 | 2026-05-31 00:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| e11a6602-7295-3984-b485-467a93c68b11 | -10.0537 | -51.6576 | 2026-05-31 00:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 96f5a59b-2b14-3620-bbe7-9483edbe7a44 | -7.9949 | -55.5169 | 2026-05-31 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 8b25488b-f107-3f31-908f-b914ae81c6ed | -10.0723 | -51.6769 | 2026-05-31 01:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 228.1 |
| d4d9e1d5-0eb2-34c6-94c4-b83135784725 | -8.7399 | -48.3205 | 2026-05-31 01:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 673eb8a2-486c-37ea-9455-c41fbadc80fb | -10.0728 | -51.6349 | 2026-05-31 01:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| fc212c00-3154-3e63-a107-c23f580906ca | -10.0537 | -51.6576 | 2026-05-31 01:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 183.6 |
| 9b9967c1-9229-357b-b5d8-40af8e68ca88 | -10.0725 | -51.6559 | 2026-05-31 01:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 337.3 |
| ba363fec-7ba5-3f6d-b955-4e62d153b2bf | -8.7211 | -48.3222 | 2026-05-31 01:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 2cce5de7-313d-3601-b60c-9b22fac0172b | -10.0534 | -51.6786 | 2026-05-31 01:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 3c7c55ce-8c4d-3361-95d8-4731ccaf61f8 | -7.9949 | -55.5169 | 2026-05-31 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 65f4c84d-e5b6-37a3-b6f5-4ff7e6455565 | -8.7399 | -48.3205 | 2026-05-31 01:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 6c3106da-4c1d-396d-b04b-c446b3ad66ce | -10.0725 | -51.6559 | 2026-05-31 01:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 355.6 |
| 135f9573-11aa-368a-810d-ca425f6a7b99 | -10.0537 | -51.6576 | 2026-05-31 01:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 64e7ba3f-43a3-30a6-8dec-2b79a3df8bcf | -10.0723 | -51.6769 | 2026-05-31 01:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 224.6 |
| d275279d-f399-3217-b661-71611e2b72ff | -7.9949 | -55.5169 | 2026-05-31 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 88b8c7a6-0eca-3d13-a720-958ae36b34c7 | -8.7211 | -48.3222 | 2026-05-31 01:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7491520a-8a76-38d4-a8ca-a31b173f382c | -10.0534 | -51.6786 | 2026-05-31 01:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |


[Clique aqui para ver as próximas entradas](README3.md)
