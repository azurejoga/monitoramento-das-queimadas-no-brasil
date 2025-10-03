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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87b75af7-7d62-32b4-aeab-e50bd7ec5b5c | -20.11421 | -44.39442 | 2025-10-03 04:14:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 53e89de0-d4a6-3d0a-a6a5-518ffa5cef36 | -17.86356 | -57.61926 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 47df6449-a67f-35bd-bfd8-d82bd309824f | -15.08923 | -49.56668 | 2025-10-03 04:14:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10912af0-2373-3e53-b4e4-fdfc1cf28cf3 | -16.3647 | -47.01569 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29d10573-4c4d-3f07-8c1c-51685add9a8d | -18.68374 | -47.83161 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6d220ad-30f3-34bd-a5e5-7c4cc0ccddda | -19.5873 | -45.89973 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 933f553a-ead5-3b0b-aa71-9039b5d87211 | -17.88 | -57.60888 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 062cd601-398a-3f4c-87b9-353a9b580867 | -19.90012 | -44.50142 | 2025-10-03 04:14:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2af75446-4023-36d9-aad9-7c67c246e0d3 | -19.9023 | -44.50935 | 2025-10-03 04:14:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 800e5629-4431-3807-a7e7-ea54eb6bdfc1 | -20.12874 | -44.01299 | 2025-10-03 04:14:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1650084b-6ad9-3e42-bd5d-6c937e67aa70 | -15.2481 | -50.12108 | 2025-10-03 04:14:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d6753f5-7d0e-3858-9186-b154561cba8b | -14.77151 | -50.09201 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83fb8305-983e-3b30-b340-3e18d60bca86 | -17.32465 | -49.37787 | 2025-10-03 04:14:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a0bec54-6297-32f2-9f30-0835eba85ed3 | -14.89749 | -48.33924 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c5f5a55-7ca3-371d-a69f-a912536d68b9 | -18.79465 | -43.74952 | 2025-10-03 04:14:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f3bdb6d-4deb-3eb8-9d10-99ca36fca2a4 | -17.35187 | -49.07098 | 2025-10-03 04:14:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 688c8a67-e2fc-31cd-a10d-2c373841515f | -18.15768 | -53.33944 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 781fb0dc-bab3-31cc-bfc2-1761aac24e3c | -19.3863 | -47.27674 | 2025-10-03 04:14:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94626bc5-5ca3-365b-9c23-a3d894dae238 | -15.28867 | -49.30655 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34de6929-1209-3176-aafe-76c8c5659559 | -15.28795 | -49.31039 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3827234d-7c4d-34e3-8549-19b83ef4bb1a | -14.94366 | -49.98851 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 719141ef-df3f-3700-b58e-ddce351206cf | -17.27254 | -49.01115 | 2025-10-03 04:14:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a47197db-ae3b-334d-aaa0-aba62ac5d46e | -19.86977 | -43.65216 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7a21f065-4200-35eb-bd55-90009df0444c | -14.91136 | -48.29663 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c42a128-8a3a-3ceb-a020-61010bc4349f | -14.72776 | -48.11918 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c954302e-0afc-30ab-bfc9-b8e5ae668b52 | -17.31993 | -49.38065 | 2025-10-03 04:14:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3f12a8a-3ba5-30a3-9b5f-92916c919867 | -14.94178 | -46.89421 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0c2ce8ef-f364-3cc6-a08d-3cb64400fc41 | -19.86753 | -43.64418 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1be51e34-957b-3469-8538-4e0ec1cdac64 | -14.89903 | -48.34176 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 09baa9e5-2cd1-3f4f-af12-a0a3eacdf64c | -19.72939 | -46.55707 | 2025-10-03 04:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d23eebd-d4af-328b-a093-8f7194d7c9f1 | -14.90146 | -48.33987 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fdda07cd-57df-3ff9-8b1d-932b7101a5bd | -14.90997 | -48.34896 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18f50d20-8705-3187-9704-196d62d24426 | -14.91198 | -48.32641 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 212107fd-d934-3bea-ac7a-6e0285006e03 | -18.11932 | -43.96366 | 2025-10-03 04:14:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 879279ed-59a0-36c6-a29a-12ae83a317cc | -15.57711 | -48.1939 | 2025-10-03 04:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ceea602-ab97-322f-bfe0-c416a97f745f | -15.78134 | -43.69585 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 4dfaa1e1-5a5a-3478-9212-710be8110026 | -18.67978 | -47.82854 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 953572be-a0a6-3764-b605-e4b04c1debb4 | -14.73174 | -48.11946 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70589cfc-a7cb-3422-bb38-000bbb6712ec | -15.11715 | -48.49234 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0893d2e8-c0ce-3236-b147-f48ebc1c6206 | -15.29047 | -46.38944 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5f206f8-3c08-35d4-ac33-5c0e7cf51b70 | -19.59673 | -43.84405 | 2025-10-03 04:14:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dc6635d-ca0b-3bf1-a5cd-627e2b638639 | -15.34239 | -46.25536 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 248cbf73-7396-3b3f-a515-7ac59d40b035 | -14.94601 | -46.89657 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d121e447-9064-3ac4-bf3e-640f78a9fb2a | -15.94453 | -43.34659 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beae2e8e-6f11-3499-adad-fa2909750d95 | -18.17966 | -53.28381 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de6be7ba-0b29-3ba0-9049-b3e5e53c1587 | -20.36768 | -42.20574 | 2025-10-03 04:14:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c751afca-f594-31a9-a63b-6cdaeeeae04d | -14.73667 | -48.11429 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b9fc4478-887d-3ac0-ab99-2ca68658264f | -14.91388 | -48.34995 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1c66d84-583e-32f2-9981-b83ae91565eb | -17.8316 | -44.37333 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 381c7276-4eb3-37b6-a8ee-4401b02991f0 | -14.61981 | -48.2472 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 945a8e47-e613-3304-8dfd-8eb9f2dcbcbe | -14.65927 | -48.25454 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 262964f9-8961-3884-a7ef-556e6ea4614d | -15.22338 | -47.18651 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae0eec78-ef29-3ee2-9e47-245496a2a56c | -14.67076 | -48.07645 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c6415e10-ad0d-3326-a254-c21970065292 | -14.93935 | -46.89161 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c6c15dfd-7658-34a9-9491-c457ace24e23 | -15.3417 | -46.2594 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f22c8b1-fb7e-34e3-b4ac-b655b8eb3e7c | -14.74241 | -48.12228 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5eebac7f-7e7e-314c-829f-cbc761b99c34 | -15.27004 | -47.90855 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e6ef030-a97e-37a2-bf1f-b458974872f2 | -14.98374 | -49.96835 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 093b0ec4-f151-35e4-a88c-3ee849b4d671 | -14.62378 | -48.24783 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60c38915-3e9d-3d90-9e51-a5c1a7ef0dcd | -19.50828 | -41.96198 | 2025-10-03 04:14:00 | NPP-375D | SÃO SEBASTIÃO DO ANTA | MINAS GERAIS | Brasil | 3164472 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 91a600c8-f8bf-3a8a-a016-c734892c987a | -15.29597 | -46.29321 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b8c724c-2c42-3e77-a3ef-a497955808d7 | -20.11536 | -44.38706 | 2025-10-03 04:14:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 67288674-e4a4-3be3-9032-2470b747d1ec | -16.68633 | -53.01317 | 2025-10-03 04:14:00 | NPP-375D | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba34f133-478a-335d-8cc5-2489da52d6c2 | -14.74137 | -48.12805 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 500ec0f3-0ff1-36fd-b7a0-52086865d57d | -14.87777 | -48.33535 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6041f388-0f78-3623-97fc-9b02acb38f52 | -20.96158 | -42.32153 | 2025-10-03 04:14:00 | NPP-375D | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 3896861f-0899-3f30-805a-985727893c66 | -20.13209 | -44.01355 | 2025-10-03 04:14:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 14bcebcb-4182-30b7-85de-6145378d2caf | -14.68172 | -48.08281 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 028531c8-2941-3eb4-8687-806a8515e5b5 | -14.85846 | -48.28362 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41d2252c-304a-33a5-9420-7dcdb91f818d | -14.91359 | -48.3291 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0128d19e-9762-3994-b829-53829a29ffb5 | -15.66321 | -44.50104 | 2025-10-03 04:14:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c247307-0867-30ea-9282-7be8ca3803a8 | -14.73041 | -48.09935 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b6004bd-048b-3841-bcc2-71b67187ec50 | -17.18091 | -47.02653 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f3bd1e8-470d-328f-a508-b4106cff7698 | -15.78694 | -43.68204 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 183ca14d-f2d3-3cac-997d-d5f1048b9501 | -14.87637 | -48.29731 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6323cddc-2d26-3bd8-9135-943b43f9e98c | -17.86656 | -57.62312 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e1166013-141a-32aa-a2d2-73fcd826bd08 | -15.28721 | -49.31434 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cc734b0-11b4-3138-87d7-196853a4f5ba | -19.94774 | -46.81021 | 2025-10-03 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4c10dd2-1762-3426-97a4-b0c9681aec91 | -14.8188 | -51.43024 | 2025-10-03 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d52aab7-4e11-32d1-b0fa-18d9403c13b7 | -15.9173 | -43.34574 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e44522b7-9c3b-3562-8f3b-819a2ed976ff | -15.34246 | -47.068 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 467b3645-0278-3cac-aa53-51a7a55c0c23 | -14.84871 | -48.29258 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa6b2bf9-5d8c-302c-8b27-eb6a082bdd6c | -18.68263 | -47.83368 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46f049d6-8f95-3357-a116-c6c447fa82dd | -16.34986 | -47.10085 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 941f78bb-c35d-3b0e-8a69-cbed3d4a7d9f | -19.95127 | -41.64833 | 2025-10-03 04:14:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 250aa2bb-7377-30e0-a161-a4fd152a8d61 | -15.35055 | -47.06474 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9d93cf0-f192-3ca8-b9af-1f02f10c0ed4 | -14.73645 | -48.11057 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4ac3e22-f1db-365a-8fd4-2e3a9d6df000 | -14.89786 | -48.29092 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d04cafa-7229-33ed-813e-2a2d2495cd0d | -15.34162 | -47.06564 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17bc3d02-3e50-3e19-8e69-4754f9dc9537 | -14.9544 | -50.00383 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbd5eeac-7b56-3a4f-9658-2e184782cc88 | -19.89839 | -44.51244 | 2025-10-03 04:14:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0d5783fc-084d-34a6-8fa5-8e0967283eeb | -15.78467 | -43.69641 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b832ff19-9b6e-3c94-9782-d1c9587ca770 | -15.30519 | -46.3032 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45d4e48b-13b5-31f2-8753-cd8a6106df26 | -14.72747 | -48.11553 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58b48295-4782-3740-94f7-78c3a4b61af1 | -14.66624 | -48.26118 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b9a9cea5-dabc-3de8-9aae-c35fb9f1eff4 | -14.84966 | -48.28729 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29c38bae-3434-3e53-aef6-47cd86f2541a | -16.04774 | -50.91783 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a12533b-db65-3670-8151-e5e88c9d022c | -16.33989 | -43.51888 | 2025-10-03 04:14:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5aea16c-5d15-3a07-ac16-22edc138857b | -15.70936 | -46.26316 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e13f00b-a0a4-3bc9-a780-31d7077e3143 | -16.76661 | -43.9632 | 2025-10-03 04:14:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README78.md)
