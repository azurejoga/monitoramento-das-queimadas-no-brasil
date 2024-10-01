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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a86b7347-e1e5-3c02-99be-8970d0765634 | -11.44461 | -46.94982 | 2024-10-01 04:14:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82165f62-cd41-36f2-a815-156ce71ee5c9 | -11.44393 | -46.95385 | 2024-10-01 04:14:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7eab4263-915f-355c-b533-e9c85cdf277f | -11.4411 | -46.94907 | 2024-10-01 04:14:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4846a69-5c0b-31d1-aea9-1cc6a7580f21 | -11.44042 | -46.95311 | 2024-10-01 04:14:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02328723-6047-3f5f-b2c1-69c3e6a9e8d0 | -11.4369 | -46.95238 | 2024-10-01 04:14:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7abbbed7-d139-30fe-9d56-c99f633242b9 | -11.43622 | -46.95642 | 2024-10-01 04:14:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68f4ea3c-ac75-3c87-ab27-ade32c46c73f | -11.43554 | -46.96047 | 2024-10-01 04:14:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65095b27-0ebc-3f50-be6b-20a763b0fdfe | -13.53698 | -47.57935 | 2024-10-01 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85a121c1-9d7f-380b-8048-3bf68fa9a216 | -13.53413 | -47.57456 | 2024-10-01 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea7e29b2-75e6-3db2-b70e-b95e808d09b8 | -13.53342 | -47.57875 | 2024-10-01 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3a22082-06ba-3c65-b5d2-c7a8aaecd962 | -13.52773 | -47.56915 | 2024-10-01 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2981620-1e79-3687-b70d-6240758a2a21 | -13.12869 | -46.77021 | 2024-10-01 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a098cc5-0cfe-396e-a827-a175d831b1de | -13.12805 | -46.77408 | 2024-10-01 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49d731ac-9b6c-3a71-a505-4d297b6e330e | -13.1274 | -46.77795 | 2024-10-01 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbfb6266-2ded-3d43-aade-a7f013f525b5 | -13.1246 | -46.77347 | 2024-10-01 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb1134a2-71be-3f6d-a331-d4ac97fa1a7f | -13.12395 | -46.77737 | 2024-10-01 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 013718e5-0949-3314-84cd-cb60bd841117 | -13.12114 | -46.77287 | 2024-10-01 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee1c4e06-8d31-396e-b124-53b93b6520e5 | -12.80882 | -47.44564 | 2024-10-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da68f020-c7f4-3deb-ab4b-592dee599863 | -12.47696 | -47.49913 | 2024-10-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 739221a3-c315-3bef-9e8a-3ec719353a02 | -12.47338 | -47.4985 | 2024-10-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb7b957a-6a0f-3b2b-a720-5d201f477d09 | -12.46754 | -46.43983 | 2024-10-01 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83e2f771-86a1-3188-8c0d-568502425c2c | -14.78053 | -48.07852 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd7cf5ae-5e38-31dd-b4bd-288ae116e101 | -14.77768 | -48.07358 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1fb7a96f-2a1b-33ba-999c-fbe897be8e08 | -14.77693 | -48.07795 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab370d3b-26e1-36eb-bd58-66da892d13d4 | -14.77617 | -48.08244 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9b52fcb-6fb7-3916-9cf7-cb7e1f59223e | -14.77407 | -48.07305 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 076ebb86-d8a5-3332-b7e1-8839a74ba7ac | -14.77332 | -48.07743 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df4234db-e452-31de-9d62-e5b9b41326df | -14.77256 | -48.08191 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbd3216f-59d1-37a4-a531-4a69eddbeed2 | -14.76972 | -48.07692 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f806a3c-e2f4-3850-91d5-1269a5f03b5e | -14.76896 | -48.08135 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c8332ee-8836-38ed-b851-56c63d9eddfe | -14.7682 | -48.08582 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b4f6d2b-af45-3d3e-a8de-f654dd267feb | -14.7646 | -48.08521 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bb4e79f-c12c-3587-924b-c693c7ac29f2 | -14.76235 | -48.36059 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8f746b1-5fca-3f27-acfc-5a41b19cabec | -14.76162 | -48.36489 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1961dbfa-fb0d-3375-81fb-96eaabf4f909 | -14.761 | -48.08463 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7de7b58-96df-394b-ac65-17d88ebce501 | -14.74393 | -47.91294 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72236410-3b0f-32ee-a7df-b8344587be61 | -14.74295 | -47.91124 | 2024-10-01 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba7d35fb-80e3-3c28-a203-835b89e455fb | -13.85696 | -48.05938 | 2024-10-01 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 787efcb4-d745-351b-87ec-1f8f84d62982 | -13.75126 | -48.14975 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d786f31c-bcef-3c7a-b34a-48bd4f564d1b | -13.74696 | -48.15291 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3942ffa0-1113-3c4c-b8ae-bc45d89308a9 | -13.74622 | -48.15719 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f654813b-c2cb-3fef-b4f1-63edd18a2d6d | -13.74253 | -48.15678 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d387858-b6c2-3163-a6a3-4769f8f82236 | -16.51246 | -48.05204 | 2024-10-01 04:14:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e113eb0-0a2d-374e-b7fd-5417020a7139 | -16.51178 | -48.05606 | 2024-10-01 04:14:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 59756ea4-75c2-352a-b91b-e47949b47d1d | -15.83528 | -48.19122 | 2024-10-01 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0663a1ec-4862-3701-a1d2-ff1fa9eb96cd | -15.77524 | -48.49685 | 2024-10-01 04:14:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d9f5cf5-3dd3-31a8-8ef9-9ee7da7ef72e | -15.7745 | -48.50113 | 2024-10-01 04:14:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eed2b2e5-181c-314e-9ccc-00850597f26d | -15.77161 | -48.49625 | 2024-10-01 04:14:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78bf780a-81c8-39d4-9763-ca84c936ce9d | -15.77087 | -48.50051 | 2024-10-01 04:14:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da642c9e-7ec5-309d-8096-6940ebbc46ed | -15.62733 | -48.1123 | 2024-10-01 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae5f7cb9-1325-3d62-9f61-4628a7d80066 | -15.62378 | -48.11164 | 2024-10-01 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cd1ca80-2e70-3fb1-b55f-7fc050177b08 | -15.5693 | -47.85729 | 2024-10-01 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52845be2-f4f4-3a31-8b9e-51c91868c18d | -15.25986 | -47.90607 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 613f1be1-d6f1-3983-a586-8c472fb928a1 | -15.19753 | -47.95041 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5b2793e-be67-38db-9b52-9b368384dcff | -15.19682 | -47.95456 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9de2fe13-b85c-3acb-a938-7845a34da560 | -16.62998 | -47.63115 | 2024-10-01 04:14:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86a7aafe-e73a-3eb9-9e37-c02fa31229c1 | -16.62933 | -47.63505 | 2024-10-01 04:14:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43640b85-7b74-368a-8ffd-1f9c1d8a336e | -16.62177 | -47.63776 | 2024-10-01 04:14:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18b76ef4-7db4-380e-b58f-8e7d79c57071 | -15.76794 | -47.71523 | 2024-10-01 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7723c1dc-9862-33bf-a54c-575940f824ef | -15.76726 | -47.71921 | 2024-10-01 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf4bf948-b633-3d68-a4b1-780f34f8d110 | -15.76445 | -47.71461 | 2024-10-01 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30f742e7-fa33-37db-80c4-233be508f3d6 | -15.76377 | -47.71858 | 2024-10-01 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75254513-69c7-3103-87c2-307496c12e96 | -15.38682 | -47.43703 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 942dc46c-6910-3cdd-b0b8-e93467284c98 | -15.38334 | -47.4365 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10e5f6b3-34f4-3021-8c2f-a9190accda39 | -15.37986 | -47.43596 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2409206c-8810-3777-9d60-acb9a1cc07d4 | -15.377 | -47.43173 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a307f76d-170b-3564-8ca8-5ffe2fb7297b | -15.37353 | -47.43116 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13fd8dca-1b20-331f-aaf1-38165b5e7f81 | -15.37162 | -47.43151 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 498ce8d3-dcc4-316e-b726-3a73c277ab29 | -15.37004 | -47.43063 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74ebb288-3f0d-3e01-9242-86528017f239 | -15.36331 | -47.43869 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1060029c-a675-3e97-8633-853fde8ce8a0 | -15.36264 | -47.44271 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37c3b1dd-0910-356f-9f7e-1a4987ec8eec | -15.36116 | -47.58819 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b76f8801-709c-3e52-ac8f-e14902904ca7 | -15.36048 | -47.59219 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3f58b4b-0364-3957-8f3f-fa24263a0a89 | -15.35768 | -47.58756 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f35e2b01-e5e5-3a0b-9e10-a196225b1b77 | -15.35071 | -47.5863 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8df0ead4-6260-3654-8ea8-15ae7b5c35a5 | -15.34996 | -47.56964 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a574642-3d05-3001-8908-02c35f337fad | -15.33112 | -47.54595 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7d7fdf5-f598-3a7a-bb77-72a84ac1430f | -15.33044 | -47.55003 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e98ea4af-e6b7-3cdc-8212-69134d68dffd | -15.32922 | -47.57893 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d239c81-67d4-3a52-9128-9123922a9cbb | -15.32775 | -47.56622 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 558455eb-c22d-38c8-98fb-c836e4e19bfe | -15.32708 | -47.57023 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b70b72b3-d069-3d8a-bdd1-7e96a33d0197 | -15.32697 | -47.54936 | 2024-10-01 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bb8d2fd-9c02-3f19-97db-9e7cc5c01439 | -15.291 | -47.48614 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8879fad1-7f8e-3105-8c95-e849aa680f54 | -15.29006 | -47.47047 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57973198-5252-3c29-b41a-32bbb1f76a4c | -15.28747 | -47.48584 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f360a7b7-b5e3-31c0-9dd9-febebfbcc6de | -15.28683 | -47.48963 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7594c1f0-9529-371d-a82a-9e90a6fba044 | -15.28461 | -47.48161 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28874561-bbfa-3d1e-9e02-c92f0afa5973 | -15.28417 | -47.50537 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09faa0aa-5d45-3e7b-b1b8-1c27d39e701b | -15.28396 | -47.48544 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c852b21-dcf1-37c8-9375-86dacc524a73 | -15.2835 | -47.50935 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97389343-ade9-3a7d-9d64-b6109d0f4a4a | -15.28331 | -47.4893 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58f1ae6a-ffaa-3ce4-930a-2ba1a83db586 | -15.28265 | -47.49318 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a37c19c1-b903-3195-8946-2d343b10c943 | -15.28198 | -47.49714 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e180708-5a74-3fe6-9352-34ad08d9270f | -15.2813 | -47.50116 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de7b48b2-e6c2-3717-8297-cc0212780422 | -15.28063 | -47.50515 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e955b732-5560-3be3-9f5e-d7b0f3ec50b0 | -17.87059 | -49.1051 | 2024-10-01 04:14:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8040313-4643-323a-a1a3-e7da9029fab0 | -17.86983 | -49.10946 | 2024-10-01 04:14:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68466642-1063-37d3-9c61-e4dd9226bf03 | -17.8664 | -49.08621 | 2024-10-01 04:14:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0b63b85-b317-3e67-a77f-74b102ac93cb | -17.26483 | -48.1534 | 2024-10-01 04:14:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a87011cb-2724-32cc-b3af-7b066dd5603a | -17.26133 | -48.15276 | 2024-10-01 04:14:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README77.md)
