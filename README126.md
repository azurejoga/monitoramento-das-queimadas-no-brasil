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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96f4011f-deea-30cc-bc0d-f6973b4516f6 | -3.65567 | -60.26299 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 48facec7-bc18-3657-9cbb-3baed2e6c04d | 3.53598 | -51.5078 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bf8c919c-6f0d-3abd-b9a0-cd3fc8a6b262 | 1.84568 | -55.80278 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 04492507-6ab5-3eb6-86ba-d100280d686f | -1.85455 | -50.63716 | 2026-10-05 17:17:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d13a24bb-09ee-38e7-b1aa-d8e632678bfb | -2.95548 | -54.143 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 854a865e-b875-39c9-a2ba-cb47364b1f2f | -4.25568 | -63.64077 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| f3a91b2c-863b-388a-aae5-f9360135294e | 1.97977 | -60.61151 | 2026-10-05 17:17:00 | NPP-375 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 9919dbe7-1069-31ee-9fbd-52a08e34930a | -1.41518 | -55.4141 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 824dea82-d7bc-37e5-b61d-fd58d9c77a30 | 1.87839 | -55.74426 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bb562ae3-62e4-3bee-a9ef-20660a594048 | 0.44285 | -60.54091 | 2026-10-05 17:17:00 | NPP-375 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 8e0ba6ed-7b04-3689-8c01-f3495dabdbf4 | -3.10079 | -57.6584 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 026ae336-5031-3688-b94c-57b73f3d09d3 | -0.39057 | -51.99713 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 63d9f376-2687-327a-9890-cf49cd7004af | -2.57755 | -56.15683 | 2026-10-05 17:17:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fb47c32a-c47d-3e90-b245-cd4044f9f171 | 1.79032 | -55.54749 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e8f57ca-02b4-3e2a-a951-f615130244a6 | 1.29497 | -51.12628 | 2026-10-05 17:17:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1b0633aa-14d1-3e4f-8c38-254a2025efd7 | -1.9495 | -54.04045 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3d999c1f-1d7e-3b96-9987-5b5b6c6ce92b | 0.92525 | -60.40187 | 2026-10-05 17:17:00 | NPP-375 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a78d1b95-de50-3b40-9c16-afd3b21da5af | 2.08749 | -50.90718 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 199acee9-8184-3c00-bcc3-00fe052009a5 | -3.77193 | -61.18311 | 2026-10-05 17:17:00 | NPP-375 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| fc07dd8c-60b1-376d-9d42-70d349a445fa | 2.96433 | -51.42649 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 18c3698b-875a-385a-b427-b1fec9939f6f | -2.96731 | -54.1094 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ba0faf45-ca13-3604-a55f-adb91d257560 | -3.28743 | -57.87764 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 01aec33d-d50d-3528-97a4-a5ccf75357eb | -1.7226 | -55.36335 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e2555fe5-24dc-38f4-91a7-469c1547baf9 | -1.69396 | -55.02339 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a23456e4-da07-317b-8569-89728634f659 | -2.80848 | -54.0857 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 778d6045-b1f0-30f9-895a-938d0ab8ee9d | -2.77075 | -57.66572 | 2026-10-05 17:17:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 422.3 |
| 84271ddf-2e44-31de-97e6-99d2ab9accaa | -2.95879 | -54.1425 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| ab4f8386-7789-3065-a4e8-448816076c77 | -2.94203 | -54.13887 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f5c43a35-adba-3290-9430-25cad9c85b45 | -1.61869 | -55.01785 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f679221b-26c1-3d5d-a033-f30827eaddb7 | -1.38478 | -55.40893 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 90df4f0f-cab2-3157-b708-463cdf4d1792 | -2.94097 | -54.13197 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 47f6d73d-299d-3145-98d2-1f2441ccc010 | 2.40104 | -50.90255 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a9c3ea2a-1007-3e76-b1d9-ee93e9e07b7b | -2.96264 | -54.14544 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 30419e31-171d-31df-9a1d-1ce97c76742e | -1.77479 | -53.7826 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a72fb7f4-b1ee-3c7b-9d60-467896cd30aa | -2.97244 | -65.19225 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2c41a9c2-2a07-30e0-868d-e82b704d09b4 | -2.93433 | -54.13298 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 181a1f77-0e05-37b7-809e-9290428e0a83 | -3.65259 | -60.26472 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9175451b-056b-3457-a6f9-3c8d14865508 | -2.89653 | -54.08578 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2b30d5de-d2ab-3b84-af83-98a8b3871491 | -3.53098 | -59.39635 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| da82a066-27f3-3ed6-ba83-241179b0eb89 | -3.3697 | -58.19038 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| efa50a4e-6f91-385a-a3a4-71bbfa004122 | -2.98378 | -65.18624 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc726f36-455f-39e3-97b0-a6bc48c73e90 | -1.45724 | -55.26582 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 30a70b83-625e-3634-8331-3f28627cd444 | -1.18934 | -49.25127 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c7723bde-f0ae-33a3-9a01-1638431d082f | -0.85896 | -48.6811 | 2026-10-05 17:17:00 | NPP-375 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 613687a9-3214-36e7-90f8-5d1b1e87cdce | -3.17122 | -58.63334 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 82b04d7f-ff7b-3636-9b2f-9adf85c03da9 | 3.40083 | -51.53409 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 25ef6372-96f2-344c-8129-f7ab99986b65 | -0.38698 | -51.99769 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cee41700-4ab2-3c1e-bf46-7a94abf692fc | 1.90178 | -55.72387 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0c2fd375-b5d5-3071-96fa-23c82f7bf489 | -3.15437 | -64.8769 | 2026-10-05 17:17:00 | NPP-375 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eff2295a-d204-3661-a3d0-ed585a405d81 | -3.43364 | -59.62653 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a560bfc0-b90a-3d58-889e-0aa92ec5cf43 | -3.07004 | -58.40297 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d60f4a99-d6bb-3810-8153-9a497b38aff9 | -2.94339 | -54.1307 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee91bd96-3067-38c9-a104-16f942f6b14e | -1.80438 | -55.72631 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55c66bc1-c5e2-3d5a-8192-423ce3b7330d | -3.2862 | -64.80714 | 2026-10-05 17:17:00 | NPP-375 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f3c7bdc0-c251-3fbf-9eaf-e6b117edd7d7 | -3.75584 | -61.01541 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 93ff3716-033c-3de3-8d46-e1afbbe7cafc | -4.29804 | -63.42882 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a756ae5e-577e-3beb-bfe9-acdf32656072 | -3.46521 | -60.66388 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9848b23a-923e-3edd-be79-985d8af99c5b | 0.31758 | -60.43815 | 2026-10-05 17:17:00 | NPP-375 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 28fcefcc-c729-3661-879f-138193606f2c | -2.96399 | -54.10991 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e04182ba-7c49-3727-be90-855c063cb396 | -0.83779 | -49.28938 | 2026-10-05 17:17:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 86946d70-5aac-3fba-a9bc-582e49f49b5f | -1.67612 | -55.75342 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a838c848-7edc-322b-ac43-2be404b998e9 | -2.95163 | -54.14005 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0b1f530-b898-3c72-9e01-84130ad87b4d | 0.05919 | -60.42522 | 2026-10-05 17:17:00 | NPP-375 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 82817f3e-b5b8-3b4d-be32-9039d61d8bf8 | 2.35329 | -50.7603 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cb7a87c1-31cb-33e3-99a0-f0dd848bbfcc | 1.71289 | -53.13326 | 2026-10-05 17:17:00 | NPP-375 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 8c21b0b6-b857-3b59-ab61-b9268528750c | -1.61617 | -55.13482 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 40eab9cc-8531-396c-8976-1f49bfd18f62 | -1.38 | -52.66452 | 2026-10-05 17:17:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f996617d-3fdd-3be0-9384-dcc26f918523 | -3.4258 | -60.55111 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f55e4424-803a-3721-b5c5-a5d15e5aa127 | -2.93328 | -54.12607 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 5287ed58-30b6-3e83-872b-6c12b05a4eb3 | 1.01021 | -51.29334 | 2026-10-05 17:17:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 32a88e56-345c-3c3b-a271-fd6bd03306cf | -1.71999 | -55.01593 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 574bdf48-0ba0-3489-9336-d5333205c366 | -0.85392 | -48.67755 | 2026-10-05 17:17:00 | NPP-375 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25a8f70c-1521-3331-9d54-9657604df074 | -2.94671 | -54.1302 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4aad557b-bddd-321f-9bf6-6f9e816e637b | -1.18455 | -49.24808 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f9eab617-0169-3a99-958b-305346b2b132 | 1.87349 | -55.7541 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5f16842-b449-308d-b115-b11af364764f | -0.40493 | -51.99492 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7d2d86af-5ab6-3fa1-b154-03b985c69030 | 3.4276 | -51.5134 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 29.2 |
| c47be4fb-8e16-330d-99e6-ed13af115b41 | -2.98517 | -65.22068 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ae8df280-9bf5-3338-932e-0b4ff6276d05 | -2.49249 | -56.82294 | 2026-10-05 17:17:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| daccd38a-2d7c-3737-886e-742cb3cc88f7 | -2.78191 | -54.08972 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 0e1aa263-ffac-3e7f-84cb-970d75efae99 | -1.29596 | -55.71557 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b887aa9a-c0d0-3cb7-bbcd-204518e09209 | 2.28015 | -59.78996 | 2026-10-05 17:17:00 | NPP-375 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a1a91db-9db7-3b4a-8151-1d2b610d1618 | 2.29112 | -55.89815 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dc66e279-ed52-38e4-bd8a-90c64b9e3213 | -1.42897 | -55.34809 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a7434310-05c7-33e1-8bc2-a231445f0487 | -4.26161 | -63.64284 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e19356f3-ce5e-3e0b-8c24-6b59354f892b | -3.85097 | -61.34707 | 2026-10-05 17:17:00 | NPP-375 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da974002-d742-3a82-bd2a-faada9c19215 | -3.71908 | -59.68446 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 46b8b2b1-6732-3bc9-bda7-e0a270778eec | 0.80055 | -51.15055 | 2026-10-05 17:17:00 | NPP-375 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2d3b2b5c-2074-37c8-98d1-d791af222a28 | 2.15154 | -55.9714 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 98fcac31-92ce-3879-a68b-530cbd4d384f | 3.51969 | -51.507 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0da1f187-957e-34f2-b60c-da930763b131 | -1.46789 | -53.61769 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 12dad776-a745-3be6-a131-51131f3daf61 | -2.26967 | -57.08937 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 55a98046-cf70-30df-af76-16bb845565e2 | 1.7297 | -55.63335 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d22dc45e-c08d-3ad5-a193-82ed0e5bf9c4 | -2.98829 | -54.11329 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 6a974d7a-ecdb-36cc-ae77-5fe858ab0ad2 | -0.38879 | -52.08053 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 15b1ee7c-f88b-3e80-b072-cfb8b6314d2b | -4.25621 | -63.64439 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| d7974727-94d5-3df5-91f4-1be846dbcc93 | -3.49248 | -59.58009 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e8aaab7-99e5-3fc1-ad2d-6949168dc39c | -1.52584 | -54.82823 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5560184a-304d-35eb-a870-2ac0b18bd328 | -1.3275 | -55.27925 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 2bbaa4f4-7b5a-38f2-a948-5e68c63c8a3d | -2.54275 | -65.87959 | 2026-10-05 17:17:00 | NPP-375 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |


[Clique aqui para ver as próximas entradas](README127.md)
