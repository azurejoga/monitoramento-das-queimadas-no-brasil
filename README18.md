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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eecb34aa-bd57-3a2d-9024-e12179e61565 | -8.63559 | -45.145 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c215cdb5-0649-3fad-ba2c-9f2b919456dc | -3.59212 | -49.35357 | 2025-10-09 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fc40c6a-1623-3ccd-bcba-ebf7e3d48191 | -10.81916 | -41.95177 | 2025-10-09 03:57:00 | NPP-375D | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5299fbdd-76c5-30c2-a7c9-144bef579bab | -4.50189 | -46.35447 | 2025-10-09 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d328ede-3b8a-35a8-93d3-ca8e07a3b11b | -8.60857 | -45.09458 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eed8c3f5-76a4-30de-9e1e-6f6b8d0d1fd4 | -7.05202 | -37.68999 | 2025-10-09 03:57:00 | NPP-375D | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c3781b2f-f3d2-35d2-b4d1-eaae7f6f08ee | -6.69024 | -46.30839 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 0c730e85-9d49-3317-b292-84e14c6ea1e1 | -5.48444 | -42.89449 | 2025-10-09 03:57:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 78fdb31c-b425-30a0-9393-e08162390e12 | -4.92919 | -40.14078 | 2025-10-09 03:57:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ab87cca6-607e-35cd-8d25-43d877805e08 | -4.01029 | -43.28766 | 2025-10-09 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd3d03f0-9e53-38cb-bf5a-da89863d0199 | -7.48205 | -43.08921 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 551c2124-543e-344f-9f55-6e360a1c8706 | -4.45206 | -43.22922 | 2025-10-09 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef73ba5b-468a-3cec-884f-ef4ab9d489a0 | -7.79789 | -42.61771 | 2025-10-09 03:57:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 000ba713-3be7-39ce-9986-c8dbaec4576a | -9.09077 | -47.95869 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 678595c9-d906-368a-bd8b-23508f916fa8 | -4.25755 | -48.56804 | 2025-10-09 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a42ff312-d0d2-3b3b-a1f8-f5b76b017bb9 | -9.22335 | -47.85016 | 2025-10-09 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 019b6bf9-e963-3fe0-9aba-67f991148899 | -4.68572 | -45.83838 | 2025-10-09 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0addb7ec-3a9f-3722-a22a-367efe86dd5b | -7.99882 | -44.46391 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8bd791d-ae00-330f-989f-4cce2a826dd8 | -6.74541 | -42.8308 | 2025-10-09 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9675cee5-56ae-3c5a-bf10-9d19fa02f627 | -8.54363 | -46.21088 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 9a105ed1-d5c9-39a9-b5a2-8d2f29e0d944 | -8.54103 | -46.218 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 5327133c-9aba-3ee4-80f7-d025438fb9fe | -7.768 | -44.04512 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ed89c698-2abf-3f53-aa54-06a385fa0b30 | -5.15362 | -46.10235 | 2025-10-09 03:57:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7a90d98-89ed-36e9-989f-aaccce79b892 | -7.80062 | -44.20443 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8010046e-99a6-3f55-819e-5f088b31d208 | -6.55359 | -39.98964 | 2025-10-09 03:57:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 217ad70c-699e-3f9e-8acb-149422cd56c0 | -5.3991 | -40.98247 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| be7cb599-7604-369b-a690-b5c0e00133d1 | -5.04827 | -45.63368 | 2025-10-09 03:57:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11791b2d-cc84-318c-9226-798cebe4b204 | -7.78603 | -48.0444 | 2025-10-09 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 976dd028-a17d-3128-9e14-2b3cc4ab949b | -7.79292 | -44.19933 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a087bbbd-e402-3639-be19-3fdfff081ce4 | -7.43056 | -44.55949 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d5fa4d5-924e-3ea1-a0b1-b90fca22f394 | -7.6906 | -42.96724 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3ebe2c5-4e5a-3172-9f88-596b5adf9b76 | -7.77279 | -44.04192 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ca93dbeb-adbc-34bf-a92f-5caa8c97d345 | -7.79472 | -42.40783 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f553ba13-a1a1-3e61-ba19-673b7cbe3382 | -6.50576 | -44.14923 | 2025-10-09 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35465932-e37d-3945-bbe5-7083b3024fc6 | -7.75689 | -44.03575 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 559d259a-9d6a-3eaa-b30f-8cfc83ec634c | -3.6451 | -39.37696 | 2025-10-09 03:57:00 | NPP-375D | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28960331-2878-3d5e-95dd-433a3d77dadf | -7.77649 | -42.39795 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 56ce42a0-8d42-3e5a-b8e9-126cf6bce320 | -8.53063 | -46.22199 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 6bae5439-c63b-37a0-8c16-54830c9166bf | -9.61421 | -40.33201 | 2025-10-09 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c440a441-6c8b-3187-bd3d-de08fc83a862 | -7.56012 | -44.29913 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0e5926c-b5f7-35a5-ae7a-1bfad89af21a | -4.84388 | -42.77218 | 2025-10-09 03:57:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| c2679653-cbf3-3b87-adac-51f6e9048c2a | -7.98901 | -43.89629 | 2025-10-09 03:57:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 712bf8ea-feec-3be6-8e6d-32030a336a9a | -7.99736 | -44.47225 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46689187-15b3-3754-b7ab-9d6611f62f54 | -4.72578 | -43.35396 | 2025-10-09 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c1aec5ea-9474-3c80-ac9a-20d29f6e95e5 | -7.63382 | -45.23346 | 2025-10-09 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b20937e-9de4-3afd-ac93-afa6120df72f | -5.41531 | -41.34319 | 2025-10-09 03:57:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b731b787-7b87-36e0-8dc4-42d9fc42c5f6 | -9.0907 | -47.95605 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c4729373-8046-30f3-8047-da5225894341 | -3.90847 | -44.34529 | 2025-10-09 03:57:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87c73412-208f-3703-8e15-87f102f15d8f | -4.36939 | -46.75717 | 2025-10-09 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59554acd-95ab-335d-be4f-e66ad67a81d8 | -7.6855 | -42.3919 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ef54cdd9-e376-3882-be91-df88a62f19ae | -7.63724 | -47.69412 | 2025-10-09 03:57:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 579d9337-0a92-3ae5-a5da-8b2e3b3ce745 | -7.27677 | -41.98526 | 2025-10-09 03:57:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 007fcc8a-f4ec-347e-845a-5d359fcd8a2e | -5.17234 | -45.47699 | 2025-10-09 03:57:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cf5a563-239e-3554-a753-19a1bcc3c46a | -7.40047 | -42.09807 | 2025-10-09 03:57:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| adfeba1b-5471-3372-b349-a6ade84146da | -3.11227 | -47.79525 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a519029-07e2-371f-bdc2-7e4e77457259 | -9.08606 | -47.95191 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f9ecbd0-b5bd-3545-8f06-0bf13208bc97 | -8.49763 | -46.21634 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4b738e38-7ab5-3443-9f69-4795c419eeb3 | -6.38546 | -43.86484 | 2025-10-09 03:57:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8e576edf-992d-347e-bc24-98906d1e3321 | -7.68398 | -42.40089 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 61f627dc-64b3-31e0-b17f-08141ee1d88a | -5.90637 | -38.48423 | 2025-10-09 03:57:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 16c8b6c4-aceb-34d9-8752-24591352aee4 | -5.59281 | -44.87507 | 2025-10-09 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c802aae0-3862-36d8-ac80-b3cae03b192b | -2.38358 | -47.71289 | 2025-10-09 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fbd7843-5159-3e75-b34d-25f1ad0a6ffe | -8.19977 | -43.34886 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| ee2a3f14-862a-3324-872d-7440e043dcb0 | -4.49679 | -46.35365 | 2025-10-09 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2615cfd-5d42-3079-aba2-f91ae9644686 | -7.78108 | -44.2441 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1ee6366-c17a-3ba1-9cec-8b8fbd5f27c2 | -5.44616 | -44.82927 | 2025-10-09 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a3113f6d-fc40-3ac6-a5f2-127978e5c9f6 | -7.17733 | -39.32335 | 2025-10-09 03:57:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b59663a7-54f7-3809-98c8-3d47e998cf33 | -8.19754 | -43.33831 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 92bfb949-bacc-3ab1-9b14-65db53cd0fbf | -4.61101 | -43.15079 | 2025-10-09 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a227acc-b670-3fcb-883a-fa2ddc31caa9 | -7.83235 | -44.15242 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e207773-1648-3d65-a3db-a7f07f84b422 | -3.44515 | -45.60201 | 2025-10-09 03:57:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d51217e0-61aa-3fab-9369-7421625ed43a | -8.5372 | -46.21209 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 1a9bea88-02cb-3aa9-963a-e4aa4dda9e91 | -7.36567 | -47.04897 | 2025-10-09 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 895dfdd3-9ec1-3131-b2f2-9599ac34c7d0 | -7.76235 | -44.02866 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e34a570-8680-38ad-9a70-e43ed63f8de0 | -6.65517 | -46.4841 | 2025-10-09 03:57:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aae4cb14-98a3-3002-9053-2328fc4e71d6 | -4.68964 | -45.84501 | 2025-10-09 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0398cdd-e608-31ae-a7f3-aec66171347e | -8.60784 | -45.09887 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2de36fa9-b3e7-3597-bdcd-3482801d7ae1 | -4.89995 | -41.52383 | 2025-10-09 03:57:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e70ef386-749e-3048-8c70-3f45970b0bea | -7.5074 | -42.74173 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a42f32f4-8bdf-3879-a150-bb4c2cc182c4 | -4.29424 | -44.51924 | 2025-10-09 03:57:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df540841-9845-3707-83ac-c6b8e0f858fd | -7.78664 | -48.04097 | 2025-10-09 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb2b3486-b164-3c42-a54a-bfc5112a99c0 | -5.48923 | -42.89016 | 2025-10-09 03:57:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6619407b-015e-38c0-b9e3-2cf8f7304fdc | -10.20031 | -44.56378 | 2025-10-09 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddbb7d3e-ec8a-366b-b358-252efca6eba6 | -7.79709 | -44.19997 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a80eb1c1-e2f2-39e4-8e98-3f70da5b1633 | -5.24039 | -45.79984 | 2025-10-09 03:57:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cfb3977-4e88-3481-9699-6d90865f3623 | -8.55033 | -44.62464 | 2025-10-09 03:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 776d87f8-7241-3033-8e5d-5074f36461a4 | -7.62801 | -43.05665 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d4892be-ccbf-3a93-95b9-c492b0eb851b | -8.15049 | -43.33273 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bbd8b6f1-6119-3c39-ab01-eeaab28c26a1 | -7.71461 | -42.37844 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d47521bb-b1e8-3c5f-864b-f62fc1aa2e50 | -7.6383 | -45.23418 | 2025-10-09 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e57007d-7469-3f22-89c0-72fb83fba971 | -8.51805 | -46.18291 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 74250e98-c4b6-31c8-9679-5baca3f4f96e | -7.40264 | -42.09644 | 2025-10-09 03:57:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ba0fbd6-6d72-3ef2-84dd-298a3a772608 | -5.23949 | -45.80516 | 2025-10-09 03:57:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 265dfd46-15cf-3206-8f58-167f27caf0cd | -5.33251 | -45.51467 | 2025-10-09 03:57:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1f35adf2-d8d4-3c90-aee6-3fa5e5384beb | -7.7617 | -44.03242 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9836b4c4-524c-3d0d-aecd-222b6e91d830 | -9.2172 | -47.85428 | 2025-10-09 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f136ee0-a5d1-37d0-b995-dc2da514642e | -7.06838 | -42.76085 | 2025-10-09 03:57:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d74c8138-af49-3f1f-be09-76647b8ccc50 | -5.45819 | -47.44271 | 2025-10-09 03:57:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6e886ea-480d-3130-aa27-8634a3d9869e | -7.54749 | -44.29711 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4139988-5ad6-35ef-ba6d-6b9131758ac1 | -4.14593 | -38.70622 | 2025-10-09 03:57:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README19.md)
