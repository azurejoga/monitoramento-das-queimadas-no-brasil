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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b18b7826-27e9-3e96-9f6a-5cd1e37c4e5d | -14.00038 | -47.26891 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d9e0438-0a53-3837-adaf-b434b6725241 | -14.00021 | -47.2702 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0319f7c-3a1b-36ca-a585-c533abfcabe9 | -13.99969 | -47.27293 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50ee0097-d876-3544-868b-3425d639d680 | -13.99954 | -47.27423 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80a44cb2-b450-372e-a113-1e7756779f79 | -13.99901 | -47.27694 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aef82cbb-ffce-3fdf-946a-0c6ce3078d2d | -13.9962 | -47.27223 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3da7a383-44ef-3d72-8de4-a1540d775b77 | -13.99605 | -47.2735 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5398c241-aa10-3cdf-bd1e-e5ad199aeef7 | -13.60321 | -48.12513 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f704e4d4-d772-3355-9c1b-5039c8ba1358 | -13.60249 | -48.12933 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 96bd3401-a46b-3c57-bc59-93d4b2395994 | -15.27132 | -40.32699 | 2024-10-05 04:14:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e22ee0fa-ccad-39e8-9743-fbaca933706f | -15.26901 | -40.32528 | 2024-10-05 04:14:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9596f6bc-1b2a-353c-8602-ab623d07051f | -9.97471 | -46.34937 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 026b5f2d-863b-347a-9857-6538f9fa5f71 | -9.97055 | -46.35266 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf4998b3-9f94-3b3a-be73-869b9038aa99 | -9.9699 | -46.35658 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80407deb-06cb-36d3-9502-0dd53afd5391 | -9.93213 | -47.91922 | 2024-10-05 04:14:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f84a6519-f9a6-3e2b-bed4-df99df0b03c7 | -9.89224 | -47.19991 | 2024-10-05 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19bbb43c-2ebc-31a6-9187-bfc46c943d59 | -9.88932 | -47.19492 | 2024-10-05 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddf4a3fd-6646-3fa3-9435-6a75277b63b5 | -9.85057 | -52.06561 | 2024-10-05 04:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb950e76-b31a-3d4a-b7e2-e9c41119aac0 | -9.8399 | -46.72985 | 2024-10-05 04:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fb7481b-a23b-3f5e-9af5-0690ed478565 | -9.83632 | -46.72923 | 2024-10-05 04:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 080c9012-1af0-3648-b44e-42a04232747b | -9.79019 | -50.07003 | 2024-10-05 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea273883-ee39-354c-9f3b-96600ec74b2f | -9.78394 | -46.062 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf34bc77-a2d9-372c-8765-e707df36429a | -9.78046 | -46.06142 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08b2f0e8-4fa0-3843-9ba9-d1798d69c009 | -9.73376 | -50.65552 | 2024-10-05 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75fc1280-ee04-3cff-9263-6d773ee8744a | -9.73365 | -50.65844 | 2024-10-05 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13fcc4b4-e3fa-39c7-8f9e-456ef967b212 | -9.72909 | -50.6576 | 2024-10-05 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d997157b-89ef-3084-8cdf-1ec9bf2100ac | -9.72835 | -50.65938 | 2024-10-05 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2eba6756-27ce-3e31-8934-189c4c7398ea | -9.72278 | -50.12154 | 2024-10-05 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6eb66093-5583-3131-b501-796cf62e791e | -9.66944 | -54.32267 | 2024-10-05 04:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fcdd318-1d9c-337d-82e3-2cb0e490dc83 | -9.66439 | -54.31751 | 2024-10-05 04:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13b83161-3afe-32f1-b828-afc1d36c88c7 | -9.66365 | -54.32142 | 2024-10-05 04:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f919e26c-a3d9-3b02-b3e4-f52e734949f1 | -9.6629 | -54.32543 | 2024-10-05 04:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10eba96e-7ce5-3996-993e-1942903a8af2 | -9.59955 | -51.44475 | 2024-10-05 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27db2ea2-f408-325f-b83f-683c532642a0 | -9.59669 | -51.44303 | 2024-10-05 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d53698bb-cb24-38f9-8752-7861107e95a9 | -9.59564 | -51.43893 | 2024-10-05 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 952f3bf6-c0d7-3e6d-a2cb-aeddebbfb999 | -9.59474 | -51.44382 | 2024-10-05 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb43c8b7-af10-3275-bd6f-9862ebbd2b0b | -9.58676 | -50.17969 | 2024-10-05 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe41c38a-daa9-3e30-ba2b-5024e8532ce7 | -9.58234 | -50.17889 | 2024-10-05 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60bdf34b-71bf-30b6-be97-f446c9d06600 | -9.54688 | -46.11983 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee687938-f06b-3bf1-a0eb-3f8969e39128 | -9.54624 | -46.12375 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 617e788c-61eb-35ff-8f7f-7ff19c9cd21e | -9.53528 | -46.49677 | 2024-10-05 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f7bf4ef-86d5-36f5-b60c-74ca992d0c1f | -9.36339 | -51.09813 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca1b5871-dfa5-3343-b5be-4902d78d4e2b | -9.3625 | -51.10307 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bbc2e208-bb12-3105-a1aa-8016115de816 | -9.35957 | -51.09227 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7a871a7-b403-342d-8841-944b66f64c28 | -9.35867 | -51.09725 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5f7a92e-a83b-3651-be5f-b5d6a1df19cc | -9.35778 | -51.1022 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f806a234-8db4-3841-903a-f84bacf93ff2 | -9.35395 | -51.09636 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe68ce57-8316-3647-9160-44c9ad86bb14 | -9.35306 | -51.10132 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7212b8eb-d06b-3174-a95e-01547f96fc6c | -9.35215 | -51.10632 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3e76233-670b-3929-a86b-fd88c79f1c90 | -9.34923 | -51.09547 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95ef94e8-d37d-3a5a-8aef-550264ef223d | -9.34833 | -51.10045 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a967c829-a06d-31a8-99f2-a38995ac30e7 | -9.34743 | -51.10544 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51f7feef-8731-32bc-9d9f-ab737a605c54 | -9.3436 | -51.0996 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8ec0284-abc0-3001-b40a-2a0b30ec74ae | -9.3427 | -51.10461 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52e22846-15fc-3343-accb-f29642536385 | -9.34179 | -51.10963 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0287d217-209b-393b-83f2-d559ee373d2f | -9.33887 | -51.09877 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71f13e15-5493-306f-bfc1-9c3ae6b59cc0 | -9.33796 | -51.1038 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec6b2823-f0fb-3123-ac8d-f766f1d1ba51 | -9.33785 | -51.10074 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5347dc01-5a90-3457-ae99-46bed80a9248 | -9.33613 | -51.11385 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3762b7b4-2b05-3f24-ad62-2dd2ced7881e | -9.33521 | -51.11589 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd80366f-0ad0-36f2-bdc4-4fb56d0b39a7 | -9.3314 | -51.11299 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d80a014e-9bef-3a78-9148-db4d125c37f4 | -9.33048 | -51.11504 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0168ea6-cb8b-333b-bcaa-f0a47d9b5de9 | -9.33046 | -51.11814 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6a2bc5e-abfb-3055-b232-5c7c9bdf5912 | -9.32574 | -51.11419 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d28251e-3f9f-3ac9-9688-07344192eed0 | -9.32572 | -51.11731 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| abcdbe0d-76a1-378a-8be6-2d29c2ab34b7 | -9.32484 | -51.11937 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aca9b06e-c96d-3135-a654-6cc93138504f | -9.05894 | -52.97902 | 2024-10-05 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5711856-9e1a-30ce-b62d-9bd3df1f591b | -9.0583 | -52.98251 | 2024-10-05 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 028b1e8b-cb6a-375b-87d4-073f6aa69935 | -9.05293 | -52.9814 | 2024-10-05 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7da40393-e558-3d79-904a-4c38a25688f5 | -9.04453 | -51.52985 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e02159b-9d44-37cc-a8a3-8892b75d8c5e | -9.04283 | -51.52808 | 2024-10-05 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ba47107-56f4-3e49-98a7-5c694f80d8e3 | -9.00589 | -49.81652 | 2024-10-05 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 598253ff-bb65-375e-b3bc-ec3cf1da4fcb | -9.0056 | -49.81837 | 2024-10-05 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3a908cf-fe3f-3b24-8ad5-97641888afe1 | -8.98744 | -49.81941 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a06775a4-e5e4-3d94-9f3c-64f538a60eaa | -8.9838 | -49.81442 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4af728e0-7e42-3960-ab64-608476ca8633 | -8.98307 | -49.81863 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87844d76-54ed-3a8a-b7e7-e49252f8b19e | -8.98234 | -49.82286 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a2db46c-112c-30e9-a4e3-81873150b2ef | -8.97944 | -49.81363 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ce4c4d7-e8da-3838-999f-7bc4c8461c6c | -8.97871 | -49.81785 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c4ac6019-361f-34c4-8099-d823fc2403aa | -8.97798 | -49.82208 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 77c647ef-fee1-3198-89fb-9431d0e5a11f | -8.97435 | -49.81707 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e101243-f0a8-37a5-8ccd-3121094901f2 | -8.96999 | -49.8163 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bfea39c-93d4-30fa-b3f8-d057176277b3 | -8.94184 | -49.74621 | 2024-10-05 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bda272f4-b3e9-33fc-8603-eff4028f9ea8 | -8.91312 | -49.67387 | 2024-10-05 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bac369c4-e38c-3973-af84-6f4b772c1060 | -8.90809 | -49.67726 | 2024-10-05 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f6c4fbd-1d15-37dd-8a3d-568634fc7259 | -8.89075 | -49.64856 | 2024-10-05 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4421842b-87ef-3c79-8baa-e6faea486fd1 | -8.88714 | -49.64365 | 2024-10-05 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a02bb79-8cde-37e8-8394-a966198c418e | -8.88213 | -49.69836 | 2024-10-05 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27ebed29-8b52-3757-b6f1-d8e5ed1236a9 | -8.88141 | -49.70255 | 2024-10-05 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40f03738-fdd8-37e4-934d-bb903f8d590b | -8.87851 | -49.66773 | 2024-10-05 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8cc699e9-b5d7-319b-8dbc-49a451615d3e | -8.87779 | -49.67187 | 2024-10-05 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2dba1df4-f357-3284-b78c-a781c11d5d53 | -8.86812 | -48.32675 | 2024-10-05 04:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f43fb897-72e4-3e5d-9c0d-c231ca676589 | -8.86725 | -48.33186 | 2024-10-05 04:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebe3bb2c-27d6-3fae-b2fc-87fa8abfc568 | -8.86107 | -48.32028 | 2024-10-05 04:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3fa02b91-cbd9-3cfe-b8cb-1edb37c55851 | -8.8483 | -48.32329 | 2024-10-05 04:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1776148c-5ff0-3c68-8b5a-d8ca3040b6d0 | -8.79672 | -49.95465 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3b0490cd-0186-392a-99f4-040ae5f4aac0 | -8.79595 | -49.959 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68b8001c-77cc-3618-95d8-ce2b03883cee | -8.79076 | -49.96254 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a650a33d-14dd-3573-9b59-99c8fd0e1734 | -8.79 | -49.96688 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5019e53-85e1-3cfb-b990-28c7fba90cba | -8.78923 | -49.97123 | 2024-10-05 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README66.md)
