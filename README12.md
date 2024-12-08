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
| 8ceebb8a-05fe-3960-89f8-c78baed5f132 | -12.85661 | -58.22343 | 2024-12-08 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25c06dac-7d4f-3b83-8012-8688de3cb063 | -12.85293 | -58.21905 | 2024-12-08 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eeac6039-2388-3cb2-abdb-43652ef8d529 | -10.53187 | -56.24223 | 2024-12-08 05:31:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b98e162b-a349-3dff-a096-6eabcd6f5d53 | -7.97893 | -50.69839 | 2024-12-08 05:31:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 306bf66f-dc73-31c8-ba19-fe9d8da3150e | -12.78912 | -54.22314 | 2024-12-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f32e89d9-9a68-3341-b501-fe03e2e88e30 | -12.8601 | -51.93594 | 2024-12-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ca0ae8d-4b9c-3861-9518-0fc8dc0fd770 | -12.78955 | -54.21957 | 2024-12-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7fb50a91-c92f-3912-8802-feb5aa6ef90e | -11.76005 | -54.72812 | 2024-12-08 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a08b9bb3-24eb-3561-9388-4719fbc6e67a | -12.77824 | -54.2215 | 2024-12-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bac923d6-ca54-3752-a5aa-891a7b8681c3 | -9.37719 | -57.55156 | 2024-12-08 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a890ab3-3e93-326e-b420-999edf1a39be | -11.75004 | -54.72369 | 2024-12-08 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9be79994-2bb9-3c2e-8285-c2f152095760 | -12.85609 | -51.94338 | 2024-12-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d6af4a1-5a97-32de-8a88-d6ccc6bd0794 | -12.86299 | -51.939 | 2024-12-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e9bd0ee-8471-3371-ba91-7a681db5940f | -11.74925 | -54.72997 | 2024-12-08 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e5a5ee28-2ac8-3937-83cb-5eea94ea48f5 | -12.85096 | -51.93221 | 2024-12-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36f7974d-49f1-3b7a-8a65-6c69b028f1f0 | -11.2103 | -53.82278 | 2024-12-08 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb5bb766-4dbf-3962-953d-12da220b775c | -12.85194 | -58.22662 | 2024-12-08 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42502081-8d88-3f89-af95-db19b3528af2 | -7.97264 | -55.05976 | 2024-12-08 05:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 064f9473-2fe2-34c4-8abe-4a2961e0eb1e | -9.2187 | -49.48151 | 2024-12-08 05:31:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b6fa453-84c8-3dbe-a786-16a4eda740b7 | -9.22327 | -50.69249 | 2024-12-08 05:31:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 693f48ee-160a-3b87-9d92-5c7df57da536 | -11.77718 | -61.34892 | 2024-12-08 05:31:00 | NOAA-21 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89f42928-047b-367d-a3cd-26f6794de688 | -12.8624 | -51.94417 | 2024-12-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5bf0664-0ca7-3611-baac-1ff83692fc72 | -11.74964 | -54.72683 | 2024-12-08 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 832a80cd-e199-32d3-82ab-10057a67e886 | -9.11515 | -49.46647 | 2024-12-08 05:31:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 562ad972-ecfe-304a-98cd-3c8dbf2301a4 | -12.84827 | -58.22225 | 2024-12-08 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9d9ddf1-6ff0-3f6d-b822-7609b0dbad24 | -12.85611 | -58.22721 | 2024-12-08 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a3d3985-c23e-371e-aac7-f3aae2ee3402 | -12.85727 | -51.93301 | 2024-12-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e24aafc2-ed59-3fce-aaa1-bb896198d215 | -12.85434 | -51.92989 | 2024-12-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4fcd8739-e931-3550-b456-e4cc20b514e1 | -9.22004 | -49.48107 | 2024-12-08 05:31:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9aa744d7-8120-36aa-abf4-75d43ed34220 | -13.89723 | -54.62738 | 2024-12-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 260d929e-f550-3b31-ba2e-fc5bb1eb08ed | -12.85323 | -51.94034 | 2024-12-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e25e7b2-2b8c-35a8-b4ff-96c1d85fd9c2 | -12.78324 | -54.22591 | 2024-12-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6745772d-1477-30ce-bca3-bea19a40a9f2 | -12.82866 | -59.03976 | 2024-12-08 05:31:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05ca8f18-d1e1-308a-b36e-d3263833ad06 | -11.82716 | -57.82465 | 2024-12-08 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 926bfc59-df03-32c5-8719-da53311ae47d | -12.78825 | -54.23026 | 2024-12-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2da3856f-20b6-3a33-9982-05031fcfd68e | -11.20529 | -53.81822 | 2024-12-08 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 045ab3d6-52e0-3d6f-92df-53f81203c089 | -11.75524 | -54.72435 | 2024-12-08 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 05f071b1-2402-3200-91b2-230fd2d87538 | -12.795 | -54.22031 | 2024-12-08 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5fd5b51-4526-33cb-986e-d1885ca01acf | -9.37664 | -57.55536 | 2024-12-08 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf350ff9-90ad-34ca-96b3-4da9f2faf4d7 | -12.85145 | -58.23041 | 2024-12-08 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 436e1604-88d7-353e-a754-963e38d0454d | -15.1579 | -56.47841 | 2024-12-08 05:33:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a04b0ce6-fd4b-3160-bac4-9050f1a2cce7 | -15.26252 | -53.57011 | 2024-12-08 05:33:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa32b210-d710-3849-b5e3-ad8c43d2081b | -18.94551 | -54.9269 | 2024-12-08 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e95f86af-05c1-3ed8-953e-27ba46372cb0 | -15.36417 | -53.1263 | 2024-12-08 05:33:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8071f8a-aa10-32e3-9d40-4f7ad2dc1abc | -15.3702 | -53.1272 | 2024-12-08 05:33:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| baec4732-bc15-3298-9c81-6f5631016c60 | -15.09149 | -59.63466 | 2024-12-08 05:33:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d64c7ae4-97b6-3297-8dd1-00c56cd6edd2 | -15.36651 | -53.1221 | 2024-12-08 05:33:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf378214-6554-3f89-abf4-5299d76ecebc | -15.25662 | -53.56972 | 2024-12-08 05:33:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 027a2d05-7856-3ca0-9d2f-0011b86524c9 | -15.16341 | -56.47354 | 2024-12-08 05:33:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e45fba72-491d-394c-83d7-e6d3d4ea3009 | -18.9459 | -54.92297 | 2024-12-08 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0025402d-713e-3580-94fa-3b8bdda32ea6 | -15.26205 | -53.57457 | 2024-12-08 05:33:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 10109a7c-8b50-37f9-8840-8b02f391d245 | -15.08756 | -59.63412 | 2024-12-08 05:33:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 220d99d3-df01-39d1-aa1a-fafe786cfbfd | -15.97927 | -57.16926 | 2024-12-08 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86c4b695-b07e-382c-b471-196b5487db3d | -15.37207 | -53.12769 | 2024-12-08 05:33:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa473082-4a84-3266-8a03-0337fa1b584a | -15.09218 | -59.62955 | 2024-12-08 05:33:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f38ac6a2-784a-3ed1-a865-c7709215097f | -15.36969 | -53.13185 | 2024-12-08 05:33:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 302bafb1-8aca-326c-84aa-97e2707a2304 | -14.45371 | -56.82476 | 2024-12-08 05:33:00 | NOAA-21 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aa50859-8d9b-336c-a634-0d431f13eadd | -15.36467 | -53.1217 | 2024-12-08 05:33:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51592b96-94d7-3c50-b673-8e0bdbc1a196 | -15.08825 | -59.62901 | 2024-12-08 05:33:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbc4b738-55dd-3d96-ace3-7f838cfe1340 | -15.16274 | -56.47912 | 2024-12-08 05:33:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 436e2b14-2029-3d19-8b41-d39702c4490f | -15.3716 | -53.13232 | 2024-12-08 05:33:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f608b72e-0244-32b2-9f81-fc8adf09016a | -15.98196 | -57.17043 | 2024-12-08 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa02ec98-891d-3e00-a1f0-3957324d6490 | -15.97729 | -57.1698 | 2024-12-08 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79d34849-e535-3bc4-a58c-48e3df70d000 | -15.36605 | -53.12674 | 2024-12-08 05:33:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6e286ba-94a6-368e-b351-085b5e21b59a | -15.08687 | -59.63922 | 2024-12-08 05:33:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40eb8763-9b1a-3225-a079-3bf80b55aaa6 | -15.3707 | -53.12254 | 2024-12-08 05:33:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2569823f-2f97-365d-a6b3-96b7c41efc6e | -15.36558 | -53.13142 | 2024-12-08 05:33:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c987dfcd-d91f-323b-852d-e049d6ad3a31 | -11.752 | -54.7255 | 2024-12-08 05:50:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| ab1921f6-a267-330a-aa37-1371c49d1e07 | 2.57463 | -60.69678 | 2024-12-08 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7db1c10a-a9ec-3de5-af4e-e689098aea76 | 2.57534 | -60.6965 | 2024-12-08 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 488b7eb7-b6b6-345c-8067-a6fcab521ec3 | 4.36095 | -60.39714 | 2024-12-08 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75be2e46-0d09-3625-a9d3-2580ccdf842e | 4.36113 | -60.39603 | 2024-12-08 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ff26adc-a2a4-38be-9776-aaf71397ae16 | 4.36512 | -60.3962 | 2024-12-08 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23aea592-96ff-3b16-9901-303347fa3b62 | 1.98094 | -60.91937 | 2024-12-08 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebd7f425-4ded-3e2a-9094-0622123da9bb | 4.60146 | -60.59947 | 2024-12-08 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7fdcdd5-9b0f-306a-a3e5-6a694adde598 | 3.68422 | -60.53492 | 2024-12-08 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14d3a819-fc4b-3824-ae3c-a00e3576fbcc | 2.5711 | -60.69719 | 2024-12-08 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ce718bac-519f-35de-ae65-dc40d30cf060 | 3.68844 | -60.53423 | 2024-12-08 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59097059-385f-3446-958d-5bb6b6b18151 | 2.56935 | -63.94214 | 2024-12-08 05:52:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f20abb09-f463-33f1-b635-e829909a6b42 | 4.36529 | -60.39503 | 2024-12-08 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad414631-7432-3c65-bda9-ca759e40e42e | -9.38284 | -57.54921 | 2024-12-08 05:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78d4b3cc-d86a-3e2a-885d-1b6e16f0dc8f | -11.72605 | -57.43774 | 2024-12-08 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5eb95da0-1633-3793-98a5-6fc39be19b81 | -11.7253 | -57.44327 | 2024-12-08 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ae5417f-bd78-3046-8af1-f41a96bc9bfc | -9.37591 | -57.55351 | 2024-12-08 05:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f71a6f12-3008-376b-9a09-5c88d0add796 | -11.7254 | -57.44324 | 2024-12-08 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 488b01bc-bee6-3808-b73b-10f33dc7e1ad | -8.72723 | -63.81671 | 2024-12-08 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa7fcc8f-d530-3f0b-88c0-d25c7610d1f1 | -11.72591 | -57.43777 | 2024-12-08 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c947b1a2-20e0-31c9-bcb0-6b25a27d66cf | 2.57448 | -60.69867 | 2024-12-08 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 72dce220-faf0-3f85-9fad-f2942dbb6034 | 2.57325 | -60.70049 | 2024-12-08 06:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 66f107d7-c192-305b-9cc3-55fd2626da03 | -2.8019 | -52.86 | 2024-12-08 06:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a489f357-9e85-3242-beff-a8950972b011 | -2.8018 | -52.8803 | 2024-12-08 06:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b2d11760-cba9-3284-ad61-a6e4215071c3 | -2.7835 | -52.8604 | 2024-12-08 06:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 986ee91e-caa4-3961-90ad-2cdeb886462e | -2.8019 | -52.86 | 2024-12-08 06:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 097cc1e8-f729-3bfe-a6c5-12bb42c4b28b | 2.57102 | -60.69213 | 2024-12-08 06:44:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8b7eba2c-cc6e-303e-b9ce-3c2a8d30ded7 | -11.77631 | -63.03492 | 2024-12-08 06:48:00 | AQUA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 02b6ff2c-901d-33d9-8475-9e1616cd9871 | -2.7834 | -52.8808 | 2024-12-08 06:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| fb0f12b0-bb4d-30f0-9bbf-ce5dfdd1331b | -2.8018 | -52.8803 | 2024-12-08 06:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| b29eceb0-2e2d-3449-83d2-1c1869f9564a | -2.7835 | -52.8604 | 2024-12-08 06:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 237a3ffc-f86b-311b-ac36-67bcb7aace59 | -2.8019 | -52.86 | 2024-12-08 06:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| bac8e977-aeb8-3460-ae33-100fa225bd71 | -17.4 | -44.93 | 2024-12-08 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)
