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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 195e03e0-303c-30aa-97ad-1fa07d58b64a | -14.7006 | -48.75294 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4986eae7-a41e-31db-b0f7-4b7b65557d78 | -14.70051 | -48.7749 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90750d8a-42ac-39b3-ae2e-231886a795f5 | -14.70004 | -48.75647 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0930a96a-8fa7-32fc-88d7-cc495af75ee7 | -14.69897 | -48.74187 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bcfc619-7549-3c2e-bf85-31436a33d824 | -14.69841 | -48.7454 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94a9fa2c-4744-3039-98d1-21a7c05358c1 | -14.69834 | -48.76715 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff1c3d66-9748-30a3-82a1-b299bd6151e2 | -14.69785 | -48.7489 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 376fcd22-a5aa-3fff-b502-ba1c349a9388 | -14.69777 | -48.77075 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67a05099-4e0b-3c97-88b5-b5b89c20679f | -14.69729 | -48.7524 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9d53feff-cfa8-381e-94b0-ad47ac1c01e4 | -14.69673 | -48.75592 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b788b656-b3fb-3cd8-b96a-2ade2cdc2030 | -14.69566 | -48.74132 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5aff0d51-201a-3b79-9053-bce049acd48b | -14.6956 | -48.76302 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ebacf2ba-d4b1-3fd5-bd69-732aa5ad9abd | -14.6951 | -48.74485 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc708403-3b91-374d-a791-37fa0848a62d | -14.69503 | -48.76662 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 18166cb2-1758-36d0-8461-f84b1f9d05bd | -14.69342 | -48.75537 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0713425a-df97-311d-84a9-7be938abe416 | -14.69285 | -48.75893 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7019aafc-4f54-3d5d-bc0e-2d8a033c1684 | -14.69228 | -48.76251 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36a38221-d34d-3733-9a9d-653142dc6f93 | -14.69011 | -48.75482 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cc23c8e-95da-3c8f-9a17-23aa5062575b | -13.96577 | -49.00468 | 2024-10-03 04:27:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 354fe3fa-db44-3c77-b83c-91d66b3cbe24 | -7.12214 | -49.16257 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31ce3f70-eb75-3948-9bd8-89b7ed035420 | -7.73307 | -49.88905 | 2024-10-03 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e10d839-20ee-3cb8-8973-577d0958bb20 | -7.85844 | -49.6548 | 2024-10-03 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12240b18-3988-3351-a4f9-5327e8bd92d9 | -7.77479 | -49.47875 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c22db08-d180-3868-b901-8edf3637b4ef | -7.73601 | -49.89388 | 2024-10-03 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc1dc28e-296d-3e8b-9c16-4ab70139ea97 | -7.73238 | -49.89328 | 2024-10-03 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0aec0a09-c8a8-3464-9c0b-e214001019ed | -7.36629 | -49.60451 | 2024-10-03 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30b0c24c-0dfb-355e-ab25-b38bfa1cc261 | -9.14528 | -48.96688 | 2024-10-03 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1db4400-ee28-36f0-ac1d-f682fd9f6d35 | -8.85113 | -48.93924 | 2024-10-03 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ed7cd4c-1422-335f-b23e-fa72b07616b9 | -9.1013 | -49.78338 | 2024-10-03 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad802c85-64fb-30bf-999f-c0cfa99e1790 | -9.10109 | -49.78222 | 2024-10-03 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7eb8342-cfcf-3f31-b8d5-ee5a512622d1 | -9.04061 | -49.81945 | 2024-10-03 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3793ef2-7680-3070-aa42-4c4c92d4c0ab | -9.03705 | -49.81887 | 2024-10-03 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea3d8f08-9349-3109-ac71-0ca047d4c151 | -9.03061 | -49.81359 | 2024-10-03 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1282b488-f466-3139-bbe5-f48083360d70 | -9.02704 | -49.813 | 2024-10-03 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1907102f-b430-3f18-9752-d6eca4249112 | -8.95042 | -49.75031 | 2024-10-03 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b28ab46-ed14-3f9a-99d5-e781e7e73d04 | -8.9186 | -49.67846 | 2024-10-03 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d631004-aeb7-39ff-af5b-ac92e6310e8d | -8.90933 | -49.66865 | 2024-10-03 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee57edd6-0687-3b80-a0b6-d6c1fbed6e17 | -8.87649 | -49.64767 | 2024-10-03 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 938ed259-7dc0-3ffc-98b5-fd28a8aaef88 | -8.7529 | -49.78254 | 2024-10-03 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 699c70cf-5897-38be-801f-f91b73509a04 | -8.75223 | -49.78664 | 2024-10-03 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2ff47009-bc46-39b7-b98a-e5dfd3a2dfb7 | -8.62454 | -49.47991 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7db46b10-38d2-30c8-af5d-1a616b87276a | -8.6175 | -49.47875 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 143fca2e-c583-3950-b08b-d5898adfe98c | -8.58238 | -49.51456 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e977b19-f6a3-3e56-ab3f-0298489c272c | -8.30103 | -49.23471 | 2024-10-03 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f29bb507-e5f4-3959-b78f-29111435dd19 | -8.25149 | -49.38438 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e90c22d3-c8f2-3947-a841-44fae06a2b74 | -8.24798 | -49.38379 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15fa4445-bb04-3983-b05b-27578df59bd9 | -8.2429 | -49.76497 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26410ffb-29af-3c0e-8722-ed9ec206fd3c | -8.23932 | -49.76437 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17541e45-f899-3b60-8675-364b4ae9af8c | -8.23762 | -49.76111 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18ee87b6-5ca9-3cda-bc3e-f383d428491b | -8.08645 | -49.52731 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6715f2d1-5078-3fbd-ac1c-e556e9e50775 | -8.08579 | -49.53131 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3edaf8c-c5db-35bd-b847-20a4d85749a2 | -8.08556 | -49.51063 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46f08c46-de0f-38eb-a45c-b23eaaff6410 | -8.0849 | -49.51466 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eee4424b-ddd4-3b3d-99d7-cbd775527f99 | -10.77356 | -49.39448 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec21e4b5-393e-3cd9-904f-1f1957490a28 | -10.62359 | -49.38564 | 2024-10-03 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8799016-7871-3e68-978d-03581de18e38 | -10.50012 | -50.26179 | 2024-10-03 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97b621a5-1a9a-32ec-bfe9-e9c8f539e4ce | -9.88876 | -50.13905 | 2024-10-03 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08ae0bc9-80b3-3693-812e-d4d674f46036 | -9.82427 | -49.60633 | 2024-10-03 04:27:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fcee89c-f614-3c2c-9379-3ddf989a580d | -9.78947 | -50.08107 | 2024-10-03 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 453364e8-32f6-3696-ab46-614e00d72752 | -9.7859 | -50.08047 | 2024-10-03 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49c44110-c51e-3553-885e-217ac1f86a41 | -9.59901 | -50.09356 | 2024-10-03 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cc03b9d-5d89-3028-be45-42fb0f83c56b | -9.59834 | -50.09772 | 2024-10-03 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3b75ae0-5a4d-33a8-afb0-cc4bf178f032 | -9.59751 | -50.09292 | 2024-10-03 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90f8a3ca-fb92-3cfb-8355-781eeb992131 | -9.59681 | -50.09707 | 2024-10-03 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9aa8dc9e-dc54-3cbc-8dce-f05bdbadb8d7 | -9.59641 | -50.18706 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50672793-659a-3785-862b-4d1e61505f7b | -9.5957 | -50.19125 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6872278b-0ec3-3300-bc22-1a84efd8942e | -9.59351 | -50.18227 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47622f92-ffe9-3dbb-8c11-fd25466594fc | -9.59281 | -50.18646 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f37fb784-a52c-3559-b736-120641dbb33a | -9.58992 | -50.18166 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a21452a4-799a-3245-874f-97d642055156 | -9.58962 | -50.08345 | 2024-10-03 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0319319-7fbb-3ebf-9d12-d3fae2b4b2a2 | -9.58921 | -50.18585 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89001f52-a150-331b-b2cd-c53351a63c7e | -9.58561 | -50.18525 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| afbfd11c-57bb-30a6-94f5-73d4ebc43a47 | -9.5849 | -50.18944 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a7ebb946-f9ad-3162-959c-1d1f8be2fd96 | -9.57492 | -50.21849 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f70b0a21-668e-316b-9060-d2c7b240d992 | -9.57423 | -50.2227 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 340801d0-baed-30b1-9b51-0d9888a6aeed | -9.572 | -50.22184 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 216a44bf-6779-3e49-8328-e1a881cddf58 | -9.56839 | -50.21307 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d22c0e53-cb10-3d18-a622-af7755e94aae | -9.56478 | -50.21247 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| abd452ab-c007-3a14-8694-ff6d44207bf5 | -9.55687 | -50.21547 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4f51450-868e-3903-b6bf-13ec9023797f | -9.55327 | -50.21487 | 2024-10-03 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcb5d914-7dc2-3ec2-8ac6-1da179ac8923 | -12.21718 | -50.50984 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9500e47a-00c4-3b12-b358-04ce92eff547 | -12.18546 | -50.08788 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a5279cd-f274-3331-99e2-ba6f607055c6 | -12.18021 | -50.05461 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaf91abd-62c1-3b89-96cd-734d0cf333e3 | -12.17797 | -50.46104 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c6ffefb-2f92-3b82-be75-64b7242b00d3 | -12.17673 | -50.05402 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6904c7c-f7ad-30f0-aa7d-dce2dc3b8c38 | -12.17543 | -50.06189 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4c77b18-f074-394d-8e94-ab66eb8dadc6 | -12.17478 | -50.06582 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac4a2f6a-4298-363b-bb25-93baaa33ce3d | -12.17443 | -50.46043 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a3379ba-2c68-30aa-8d2f-4dc07f2d34bd | -12.1726 | -50.05737 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf63dbd9-88f7-3931-ac1f-4da0b5d3038e | -12.17195 | -50.06129 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc20c626-2808-3ece-9fe2-de0c144430bb | -12.1702 | -50.46391 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53c43008-527d-3dac-a1f7-d7e7e28ac2d9 | -12.16847 | -50.0607 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c18a1eef-230e-384c-a433-ed5aab84535f | -12.16564 | -50.05618 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c908c8e9-e639-3ca7-a048-bffa682d1624 | -12.16498 | -50.06011 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10905112-2420-35fb-9802-d352d66474c2 | -12.16216 | -50.05559 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 450eea7c-97e0-3611-8980-1f49a81bf821 | -12.15933 | -50.05107 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b70d1cc6-8538-337f-b74a-55d5dd69b94c | -12.15868 | -50.05499 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 784720ee-3b9e-358a-a9d7-d1681858e36b | -12.1565 | -50.04654 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e92494d-54b0-326f-afe2-21db17afdef5 | -12.15585 | -50.05047 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3d3a43e5-9033-31bb-a015-919afabb1f2b | -12.15303 | -50.04595 | 2024-10-03 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README94.md)
