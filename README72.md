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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 906ae2b8-4f95-3c8a-aeb8-e8db9b2d0bed | -11.11929 | -47.86794 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| caf31414-c14d-3858-ac75-e8ebbe574655 | -13.96675 | -48.11014 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6b4c5488-d5f2-39bf-ba1e-2d2e627e55aa | -9.92225 | -43.7313 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2815e30a-74c0-38b1-afac-789d7e8954af | -14.01562 | -44.96643 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 110375f9-c1e0-38f8-a067-b7c9d4f87d9a | -13.54935 | -47.30387 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c0c9729-3bac-3212-a871-eeeca4a16734 | -13.48199 | -47.24168 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 806f94bc-734d-332f-a77c-5eb1037e061e | -13.32832 | -47.60752 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ef88427-3467-3b77-8375-c00553072736 | -9.9277 | -43.76217 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ffd729d9-7faf-3ef9-bbb4-8ef524503714 | -11.31222 | -47.84005 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bec3a8bc-29e7-38d4-9ec1-d2be9608b6bc | -12.63174 | -46.96888 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c00c763-33cd-394f-afcf-db1a76ccf096 | -9.9929 | -43.60177 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f99bb96a-de8e-3fa9-8493-101ff7fe0588 | -10.96692 | -51.09509 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ccab0e2-b76d-32ef-872b-b0b70c872839 | -10.90679 | -47.04604 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f88b4ebd-9b3e-3832-a8b1-7095de6ea2c5 | -11.01699 | -46.54962 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb9431f4-429d-36eb-9068-13d4e5321f16 | -11.65112 | -46.86814 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d236b93d-0fd4-3858-bfb4-0bdcc08e9ab1 | -12.68686 | -48.54786 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 441954b3-bdad-396d-9d92-2aa78ef651d0 | -12.62271 | -46.95358 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 897f5d47-e93f-3d24-95a6-6dda245fd486 | -12.92336 | -45.08335 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7caa8b3-ef62-3c72-8006-1edb3fd9e23c | -13.19291 | -47.82891 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 536b0dd4-9ba6-31a1-ac29-b2febd85417f | -13.73871 | -48.01263 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c48c87c-6f23-3d61-8a79-c9e53991c542 | -8.80373 | -46.66697 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e884ff00-13e0-3ebd-b1f1-27afdcbdc4b2 | -11.85577 | -44.96643 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c992922e-850d-3df3-9004-bc3b15baa447 | -12.90022 | -46.93878 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a02501bc-1205-3316-a733-3a17738dc6e8 | -13.26729 | -47.25114 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70744e65-fa26-333b-9de9-23e1368eb261 | -11.74725 | -46.824 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56aebf22-b13b-351a-9866-54b7af42722f | -13.22844 | -48.49612 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4af901f-10f4-3376-a24f-e3c8be750d3d | -13.14158 | -47.8884 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e7556ad-5adc-3f96-bc40-be2666846601 | -11.491 | -45.01381 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7aea4ecf-7ae0-3d16-92eb-7db7dbfa4b61 | -10.89964 | -56.20142 | 2025-10-03 04:12:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fbf256c3-c234-3572-84e7-7d2555b790e2 | -12.61502 | -46.97566 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 704fe9fd-6e37-38d5-bb33-adb8b70c0063 | -14.33107 | -45.86825 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dc4a784-d751-3c7b-9f2e-df4caed0a87a | -13.76518 | -48.06132 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd3ccef0-48d5-3240-8c8f-021c856f33ce | -11.77825 | -46.82533 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4c2d767-28ef-3b89-bae9-6ef571f52782 | -13.73754 | -47.99615 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5e59a95-6fe6-3d3b-9577-c6c5873b041e | -13.22714 | -46.43407 | 2025-10-03 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e5b084b-f641-3168-be67-7a7a6a349e0b | -11.90208 | -46.26836 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c650e1bf-6610-3107-acc6-a80589e6aed5 | -15.36681 | -43.66738 | 2025-10-03 04:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2a37d0c3-f777-305f-82ce-8726b38ab5cd | -13.15156 | -47.83295 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e905d6a-4aad-3d1b-87cd-f41352c3d20a | -13.77263 | -47.54755 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e0ac946-1841-3105-86fd-7e4a09557bcc | -11.07451 | -48.36416 | 2025-10-03 04:12:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 250c909a-b6c7-31be-bc0b-a37bdc2c2402 | -13.2444 | -47.30028 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e9c2ab9-5e78-3b3e-8d58-84c9ad4d0b72 | -9.91666 | -43.72289 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5fed0585-dc9d-3cfc-90c6-6eacd0426b25 | -12.62679 | -46.99791 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ece49805-79eb-37af-af9a-8f3d560a9037 | -12.85215 | -46.85661 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4306597-6ec7-3e9b-a472-d177c96cc7b0 | -14.09988 | -44.30378 | 2025-10-03 04:12:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a95a7435-f445-3225-bf36-416b7a93937d | -11.01619 | -46.55421 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 28f86603-4777-3589-8470-4034c9c42858 | -12.62651 | -46.95408 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aea83d98-9d56-3f85-bbe7-4a5dc16650a0 | -9.58775 | -43.32235 | 2025-10-03 04:12:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0a906297-3bd4-3762-b2af-3c90d53d2339 | -13.68469 | -48.64264 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1b02182-6e37-36e0-a251-70fbc3c32344 | -12.64827 | -46.87215 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6c51965-3b1f-3fcd-99e7-b8c6c1f540d8 | -12.62716 | -46.97293 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4dd84e5-8a8b-3ff7-b275-e1a8cd9ac272 | -12.86139 | -47.00645 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14fa604a-e9bf-3a5f-9124-b19f1208f147 | -12.37154 | -46.52274 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8c1f0ce-15b1-3bf5-85c0-be325841c6d6 | -13.55694 | -47.30527 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae8257a2-e340-3860-98b4-6dead4ee21b7 | -12.37446 | -46.52794 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5043d16-664b-3dd5-af2e-a62ef4dfb343 | -11.61962 | -45.06283 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8d8e9cf-cd19-3e30-bd12-233377fffd8d | -11.62715 | -47.98714 | 2025-10-03 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2380690-ef51-3e9d-9b47-59a0bdad75a1 | -12.63136 | -46.99397 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d37dbc6-4077-30d4-a63f-41dd14932ab2 | -13.64975 | -47.30324 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6eccdcd-ae86-3ae2-acb2-520926153900 | -11.11997 | -47.86414 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2bc376e6-bcdf-3e32-be13-4adfe218098f | -13.77202 | -47.57338 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 129772cb-72ca-3c5a-8572-77c80a8da9d2 | -12.53036 | -47.30533 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a81f4564-1718-310e-a918-0f6f16ce83fd | -9.33554 | -45.73939 | 2025-10-03 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 766cebe4-b50a-38f5-bf91-1cba6125d25a | -14.97248 | -44.43557 | 2025-10-03 04:12:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c309c85a-eb2a-3e57-8965-518f0e6442f3 | -11.63141 | -45.05653 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae237fbc-8eaf-3453-beac-d35d66c1e5da | -12.1211 | -43.44212 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 097d6e35-1d5f-35d1-b23a-7a8760e2c920 | -11.18631 | -47.74821 | 2025-10-03 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c979f03e-6134-329e-a6c9-335c59da1804 | -9.95632 | -48.78117 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 424a83f0-0cc3-3cf1-8c21-3d7eb1581f50 | -8.71695 | -47.13627 | 2025-10-03 04:12:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df91c912-d66a-3fd6-9442-e3ac4e80a650 | -9.98643 | -48.78547 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9d16e15-4661-3620-b6bc-3db078b90a88 | -11.13505 | -43.40884 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b24b6427-8e68-3112-bfeb-c339acdc6ea8 | -12.11888 | -43.4346 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b89cffb1-b1c7-3f27-854b-c5cc252f6a24 | -12.38704 | -46.52109 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76154e46-1ef9-3b70-b6a0-2f49438e51f1 | -12.7526 | -50.55864 | 2025-10-03 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21cb3399-15d6-3c5f-866f-b50789bbe288 | -11.91095 | -46.26673 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b79aa023-4f88-350f-9565-7a8a3a866d0b | -14.46743 | -48.41601 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8978fbd-2f3e-3f74-a252-130e1f6ef751 | -11.35093 | -44.94012 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78424c05-d762-3782-8124-b14e9adc7ede | -14.6932 | -45.18118 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28a5606c-a197-36a6-9f20-a34637e5667c | -9.87213 | -47.81491 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a051275-024c-38a9-9b45-9ad9295d0caf | -14.59913 | -46.71465 | 2025-10-03 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 521e1040-1ef3-3fd2-baa6-b5e676e23def | -13.75537 | -48.07032 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0e9ddf9c-25fc-3ae3-b418-621c29ce9d1e | -13.32053 | -47.19278 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f188467-c039-3ef4-ac10-d7455687ac65 | -9.88518 | -47.81355 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c35ae246-36e1-39cb-8d8e-6925f4499d42 | -14.42981 | -46.35053 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 588b7c00-a51a-3e5a-be51-24cebf97f94a | -11.91591 | -46.27578 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 9982b0ca-3901-34e7-b2bb-f5616ffc631b | -11.83634 | -45.01913 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34a713db-d160-3bee-8531-5fde55fa851f | -14.57036 | -48.32808 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5bd7cb9-bab2-3091-9b5d-4607a1f76185 | -13.20469 | -47.8312 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e59437a9-c02d-390a-b979-3e7880c59f88 | -13.58084 | -47.58579 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 9dd03087-5876-3ea7-be92-c33f50ab333b | -13.30593 | -47.82471 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c36164b8-ea27-3698-95d3-85b2638d4734 | -10.8628 | -47.24945 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0846a3ca-7ddd-36c5-8d60-059442caa201 | -13.76498 | -47.54605 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7743f773-4bbc-3ede-94be-c67badd70332 | -10.76547 | -45.33762 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44a58e61-f91f-3225-b63a-5a124022dbde | -12.61739 | -46.96186 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33cc4d3e-764c-3c78-b010-f7ca1c760ebc | -13.77798 | -47.58455 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0745a97b-580c-3ab7-835f-32ab0d4f0398 | -13.31727 | -47.57978 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34dd40a4-c0b1-3b83-be2a-27af0841be1a | -11.76908 | -46.83327 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 203ff92d-d1a7-3fc6-8cbd-6fb8fbfb76ea | -9.95642 | -48.77516 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 988812de-bcbe-3560-8ee8-41f28b1494aa | -8.52952 | -47.23998 | 2025-10-03 04:12:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf25fdaf-ed41-3b47-b1b7-9e4a907a8173 | -10.20867 | -48.19254 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README73.md)
