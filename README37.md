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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc74a8b0-36fa-3975-9fbd-8a85ccb30443 | -8.55892 | -47.40939 | 2026-08-19 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba51a775-a2d9-32a6-8fcd-4460a10f7cfd | -4.01118 | -48.90939 | 2026-08-19 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 250be01b-ce8b-367f-b7c1-5e46a3bbf691 | -4.01079 | -48.05933 | 2026-08-19 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a9cfa89-5496-3936-a1e2-c6ca1326cdfe | -6.68054 | -59.07355 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 633e765c-2ab6-3dbf-ac51-0605374ae067 | -4.48355 | -43.90699 | 2026-08-19 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c84672f-3187-331f-b3d3-a29b9e232b49 | -7.55529 | -55.57172 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c806cc5-5ab5-388b-a186-3f0360c01316 | -8.10412 | -51.66021 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fff68c8b-25ed-369f-987d-d602e525ca42 | -6.00162 | -57.85043 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d316adc9-0d25-3c59-86ea-b334e0286b89 | -6.78854 | -59.4578 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7a5e633-5d1f-377b-873e-fe77ee42d3a6 | -6.76096 | -59.15437 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c29e2443-1e8d-3fdb-a1be-0f311fe41448 | -5.43603 | -48.41365 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| cb7ba946-9aa9-3705-bedb-7307eed0b61e | -5.49295 | -60.1423 | 2026-08-19 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93805a59-9c6b-3568-b90f-e0e5724ca228 | -6.63874 | -45.50466 | 2026-08-19 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 946e5867-3aa9-36f4-b67d-bdcc4e0c3d3b | -6.79638 | -59.44936 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f90667c-4786-31fe-82b7-dce694672951 | -6.14556 | -57.89581 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45807a4a-da43-3cbe-9d8a-d1c2bba1da29 | -6.63935 | -45.50072 | 2026-08-19 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee77bea8-5a00-321a-ae41-aa39d046d182 | -6.01773 | -50.19466 | 2026-08-19 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2abbaad-f68e-36b3-bb5f-1cde0365a56d | -7.5369 | -55.59398 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9373cae-555b-31ec-92b7-215d025965bf | -2.76678 | -48.5746 | 2026-08-19 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 838bf604-8d11-38e8-a5c2-04de60102fbd | -5.91795 | -43.63256 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 629c8013-8081-3072-af50-824adfc1e67f | -6.10101 | -57.86398 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cac2d03-507e-3403-b71d-706982572b71 | -6.44843 | -52.73986 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b66650dc-8eed-3f43-8f8b-196943128aac | -3.45709 | -56.80951 | 2026-08-19 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 094335af-5abf-3aef-98e9-81bdbaef981a | -6.12152 | -57.71571 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1390b368-3328-3a72-91ed-205cd8e55267 | -5.92011 | -43.61815 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64e79bae-0f81-3c7e-b704-d0d5f1ae57e8 | -7.05789 | -59.84946 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 696d2369-bcf7-3824-a690-e4442dd1a266 | -3.75988 | -49.09886 | 2026-08-19 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c4eb30a-38ad-3345-9314-31df58981431 | -6.13997 | -57.8713 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfe1233c-fede-35bb-afbb-73d7cad269e3 | -6.65117 | -56.42962 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c52ca94c-e62c-3315-82ba-3c7624a55cb9 | -7.29278 | -44.08208 | 2026-08-19 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0e30888-79c9-3b58-ae0a-a8e54873df17 | -7.54158 | -55.5948 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f18ba2bb-d185-314b-97f0-ece690038824 | -6.13931 | -57.87511 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7327b41-4603-3782-9460-05cd0d510e43 | -6.68132 | -59.06916 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92aba972-c220-3483-9a8d-89bfde0b1c94 | -7.02237 | -45.90115 | 2026-08-19 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 246b3cd4-759e-3c30-b49b-00e2fd8b111a | -8.04305 | -50.09889 | 2026-08-19 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f2156fc-be3c-35b3-88d6-fe9930befb95 | -6.03233 | -57.80634 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3c968b6-6a07-3bf0-9b69-fb8f2957a23c | -7.54509 | -55.575 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51e127f8-6eb8-32db-917f-11b05935d481 | -6.01997 | -50.20279 | 2026-08-19 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6cece12b-2b89-3391-8254-744a1a9ce2b2 | -3.41776 | -43.33814 | 2026-08-19 04:38:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70b72e8f-93ac-3dc7-8e05-77d194542504 | -6.33946 | -54.90203 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ede90817-9cc7-3d86-b709-231ff086d508 | -6.09676 | -57.85551 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ac30770-a40e-3492-be6f-12c6502776c5 | -6.88006 | -56.41623 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d27224fb-90ee-3558-81e2-0ea1c7274798 | -6.03734 | -57.80265 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a092412a-7a19-3d06-97d1-cccec39983b5 | -6.70044 | -58.94698 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c9fe57b5-c2d7-37fc-8ffe-396f467a8def | -6.34694 | -54.91286 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17353dea-798d-31a4-add4-7332947c77b4 | -6.00653 | -57.85521 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a361aae4-ea82-3afb-8711-4f2bacb3182c | -3.09737 | -61.21714 | 2026-08-19 04:38:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ebfcf36-ce95-3d3b-afeb-59aee8fb737e | -7.17291 | -43.10604 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e060473a-297c-3d74-96fa-6ed313f37b8d | -1.82551 | -47.89234 | 2026-08-19 04:38:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 753d8b32-95f1-3c81-ac95-03c6c3c9cc33 | -6.34613 | -54.91749 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 088adeec-c8da-357b-9c7c-aa95168ffc8d | -3.27034 | -49.52751 | 2026-08-19 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ff1edb8-9036-3272-b366-9d0f5826a9e4 | -2.77071 | -48.57156 | 2026-08-19 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c29544bf-a765-3f44-8739-f5057ba08b59 | -8.08758 | -48.31824 | 2026-08-19 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38aea577-13ac-3007-b80d-4e8937804ab0 | -6.90963 | -43.26145 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 23d0fa79-69d1-374d-8066-74682fd4252f | -7.74724 | -45.05542 | 2026-08-19 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4e48145-a5ef-3e81-9a9a-289ba373fd73 | -2.39722 | -49.02205 | 2026-08-19 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 589b803a-9aa8-3ca5-8d98-6335b0292c46 | -6.83242 | -56.45192 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db1064f8-bba7-3f8a-995a-61648f7a9c6d | -5.99831 | -57.86924 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 58eab682-0ba5-3002-8952-9088617b6e02 | -6.27184 | -55.97158 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e98955a-62d9-3ca7-82b1-94220fdf3df2 | -6.34688 | -54.91068 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e8234ce-0414-34cb-95ec-a86444e74dcf | -6.03598 | -57.81013 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec5af438-388f-3109-888e-ddfa1da3a0b0 | -6.83994 | -59.00654 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 977f2a13-ebb4-3d76-bb2d-8aa3cd2c5bd1 | -3.25205 | -52.91979 | 2026-08-19 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39a6676b-21be-34cf-ac38-59743583e354 | -7.30203 | -44.5624 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d70d5794-8cbb-3a36-a257-36512f48133a | -6.89253 | -56.4333 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f97f478d-cf24-35f7-99b1-86f9ba2a9a85 | -6.01472 | -57.84137 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02815f5f-c140-3deb-9673-7879f3e8a13c | -5.82023 | -43.40191 | 2026-08-19 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95d557e7-779e-30fd-afcf-290c3ac94322 | -7.59212 | -43.96265 | 2026-08-19 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89345da4-7842-37ef-a32f-1dc588495c9d | -6.0855 | -57.91897 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 38e5d52d-50c8-33b7-a105-d27f9488e221 | -7.44672 | -45.13882 | 2026-08-19 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49f4a8c7-4477-3407-a05f-402b39191198 | -8.09618 | -51.66323 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fcd55e90-2cf0-3275-9ec7-407278c80ea9 | -6.69832 | -58.93951 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 66f3121c-6e6b-33d2-9767-20c03ba9ccd6 | -6.75265 | -59.16616 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b215f6c-b50a-3b47-9584-287d340c2ae0 | -6.142 | -57.88367 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d8b3d6d-e8b6-34bd-a57b-6653c8c7e38a | -6.14056 | -57.85997 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bfd8d00-dcea-31f2-8b47-8f8311217479 | -6.14474 | -57.86856 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5104b127-679e-3a52-9e5d-ce18aba2e2e6 | -6.34077 | -54.9213 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7a519c5-f293-3ccd-8a70-94f8bb76b2cf | -6.40582 | -54.95219 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec487308-0707-39d4-9f21-29bda8e25b98 | -6.35473 | -54.89505 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 577ef9fe-ac7c-3a46-84f1-710155b1d794 | -6.73918 | -59.03625 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc59c944-1c00-3afd-8e90-29c0f96eea80 | -5.73379 | -44.50646 | 2026-08-19 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfabaeca-cae0-3bb7-9f06-3eb4c01bb553 | -7.53208 | -55.58107 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7284af66-adc1-3ccb-881a-ced64cafba7d | -5.42221 | -48.41503 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26c71288-3b91-30e9-8546-4721cb7fec6f | -3.68483 | -47.65068 | 2026-08-19 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb84f7aa-e163-3f14-8391-7745fc4b66a6 | -6.83308 | -56.45024 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e1a59de-e90e-382c-8b6d-899d2b3434ff | -4.00747 | -48.05883 | 2026-08-19 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33070966-c5da-3384-9343-31753eca8774 | -6.34311 | -54.90523 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edc8d8d5-5316-31a1-ba4d-71fe437bd3e1 | -6.64 | -56.34716 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de59c86f-6186-303a-a408-1e8c169f4f65 | -6.29361 | -43.64492 | 2026-08-19 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dcb3331-0096-3a20-84ae-140393df330f | -3.6649 | -48.96928 | 2026-08-19 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dd7fe5a-85bf-3e4b-9310-49e3a08f22c9 | -3.42845 | -51.51157 | 2026-08-19 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 866f9e10-683e-339f-9092-f911dd4ee2c0 | -6.1319 | -45.17958 | 2026-08-19 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e1a5f0e-d752-3639-bfb1-f649ead7ea65 | -7.44542 | -45.14737 | 2026-08-19 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d4d0a8b-6abf-325d-80bc-7d50ffc956bf | -5.91867 | -43.62778 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39ff1540-ef8a-393f-9bf7-c4e282d6c913 | -7.05731 | -59.84231 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39298829-e0fe-31cd-a784-67749d7206df | -6.01992 | -57.81168 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b68d3a16-0b2a-3260-ac6d-09cb3c2036c6 | -6.09611 | -57.85918 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a335004a-208d-3710-a861-f016fd25d8fe | -6.74575 | -59.17012 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03b07fee-eb18-34ea-81dd-a1d7981e2c09 | -6.80922 | -59.44902 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf7c5d9a-09f0-3a12-8628-fdf4b65dbf53 | -6.40742 | -54.9428 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README38.md)
