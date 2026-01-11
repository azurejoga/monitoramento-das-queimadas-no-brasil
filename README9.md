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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85edb63b-f73c-37b3-abc3-036bf9c0a0f0 | -6.08842 | -37.8654 | 2026-01-11 11:34:00 | TERRA_M-M | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 667954b5-18f0-3946-a8e8-aadce27f06c2 | -8.99399 | -35.5906 | 2026-01-11 11:34:00 | TERRA_M-M | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 2d15f0b3-95fd-3a0c-8020-ef7feedbad43 | -2.84001 | -41.98971 | 2026-01-11 11:34:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| db6f0c63-a588-31ca-8651-657f74cc6aed | -8.29139 | -38.71001 | 2026-01-11 11:34:00 | TERRA_M-M | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 7cac2c2c-83b8-3e50-9a3a-5e6af4e88674 | -2.84193 | -41.97674 | 2026-01-11 11:34:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 53ffa7cd-50e1-32f4-849e-dfeb1f0c513a | -3.46467 | -42.27142 | 2026-01-11 11:34:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 657ff9e8-0c70-37ed-a732-bc5f643eceac | -6.75427 | -38.43453 | 2026-01-11 11:34:00 | TERRA_M-M | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 8.9 |
| d03266c7-c362-3892-9e2a-1c9ca8d70f99 | -4.942 | -37.36229 | 2026-01-11 11:34:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c25bb4e7-44e7-32fa-9abe-9638d7fb4e67 | -5.91069 | -38.07381 | 2026-01-11 11:34:00 | TERRA_M-M | TABOLEIRO GRANDE | RIO GRANDE DO NORTE | Brasil | 2413805 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 8709b1c5-fc3a-316a-9fa6-5d6e324a028d | -7.1205 | -35.17616 | 2026-01-11 11:34:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 1fb4a0b8-07ec-3d1c-a3a0-1e10110a3718 | -5.16338 | -39.09734 | 2026-01-11 11:34:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| cc016a79-667b-377b-a48e-d47f3d86f430 | -4.50825 | -38.39679 | 2026-01-11 11:34:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| e8c205cf-b39a-384d-9e21-d182573d6bfc | -5.16209 | -39.10626 | 2026-01-11 11:34:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| e5a77808-932e-3802-b236-a593fab9a537 | -9.30982 | -36.88843 | 2026-01-11 11:36:00 | TERRA_M-M | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 14.6 |
| e243963f-217d-37d8-8fa8-b48d3a67f410 | -10.1253 | -36.97909 | 2026-01-11 11:36:00 | TERRA_M-M | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 2209ca23-7ab1-30a3-9da4-d41815fb9a3f | -9.30032 | -36.88715 | 2026-01-11 11:36:00 | TERRA_M-M | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 35.3 |
| f2e8fcc7-8d1e-3d0d-a6a6-8b63781defb4 | -9.68741 | -37.09996 | 2026-01-11 11:36:00 | TERRA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 49f7f04d-3d3d-3d92-af39-2a881e0b3b5f | -9.98318 | -36.37123 | 2026-01-11 11:36:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 6fe2a516-71e2-3f7c-8670-6d0ca4503916 | -17.7598 | -43.42587 | 2026-01-11 11:38:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bbd03ebf-7e1f-37d6-affa-2d2ded06fbc2 | -20.14661 | -46.83392 | 2026-01-11 11:38:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| afd8d586-86cd-30c7-a994-c4e44811c32d | -20.24026 | -46.48881 | 2026-01-11 11:38:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 84edc3d8-08f7-3736-9b26-e7d48cba1304 | -20.24275 | -46.47411 | 2026-01-11 11:38:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 90e00bad-122f-3947-988e-802fe0510b84 | -20.14386 | -46.8497 | 2026-01-11 11:38:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| df0ba64e-ff00-31f8-96ce-f841fe088d4d | -19.94355 | -43.09368 | 2026-01-11 11:38:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| d10f3737-5db7-3c8c-9b21-eeca574d3fb7 | -18.8119 | -51.6134 | 2026-01-11 12:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e5267afd-c1fc-3e9b-952e-dff5e60f8dd5 | -18.8119 | -51.6134 | 2026-01-11 13:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| bd3857ef-dc4e-38a9-a419-94224f14f9c7 | -18.8119 | -51.6134 | 2026-01-11 13:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f7ee5312-8e3b-36a3-ab4f-037935131c91 | -18.8119 | -51.6134 | 2026-01-11 13:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 37b7f12f-85d8-3d7b-ac98-535f95858be2 | -18.8119 | -51.6134 | 2026-01-11 13:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 2b4a7d97-8acb-3560-821f-8736bddb99ca | -18.832 | -51.6099 | 2026-01-11 13:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| fd4c7972-2398-3053-b135-8914ce68c147 | -18.8119 | -51.6134 | 2026-01-11 13:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e1a1ad45-b77a-35f0-a015-9d4f8e8b2e15 | -18.832 | -51.6099 | 2026-01-11 13:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 8382dbcf-31a3-3fde-849b-76aae6649479 | -18.8119 | -51.6134 | 2026-01-11 14:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 3ada4abb-e68e-30fc-970d-38d8d5b466af | -18.8119 | -51.6134 | 2026-01-11 14:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 23657da1-e489-365d-bd47-e5a47f5ab3fd | -18.832 | -51.6099 | 2026-01-11 14:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |


