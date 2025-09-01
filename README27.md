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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54a20b55-dca8-3bc7-a39f-2abbee8d79a0 | -6.32752 | -42.53959 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7606f4bb-6f97-355b-9ef4-ef2ad29d32d5 | -6.57421 | -43.71371 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91d26aa6-ce36-31d1-b0c7-b662c0f1b328 | -6.2873 | -43.28624 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d045403-5cd2-3ba7-90e4-a44950e4f4f9 | -6.81802 | -52.82033 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e5b9eef-91e7-332a-b30d-9c9071f720e8 | -6.1815 | -44.19667 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3a2c002-c933-3cb7-9b3d-ddc03f37947b | -11.89727 | -46.69069 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a04a1a0d-a8f3-3d4e-8fda-62c5aea2d72d | -11.05161 | -46.90984 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9619cfc6-6535-393c-9080-caa8e65c5289 | -6.50431 | -43.56644 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ca09347-759b-3fa1-bcc0-19b78e2b5d05 | -10.72856 | -49.57765 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91cb5441-394a-31e6-b578-f17ae8c0a6da | -11.37811 | -43.62894 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44b99b3b-0670-37eb-bf42-3ef91257a41f | -6.26676 | -42.61072 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d86b113f-ed89-3767-b4bf-1c4592c4e1e3 | -6.49674 | -44.0766 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f755f38-8887-3f5e-adf0-fdd5c83c3a4e | -8.47342 | -45.17129 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 510e1a12-9c6c-325b-bf92-a2a0ff2bdf02 | -7.24007 | -44.05938 | 2025-09-01 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb78f901-8811-30e3-ac8b-e5a68da27e48 | -6.15129 | -43.33374 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 875e0059-c95f-34a5-b9c4-20a90d858f49 | -11.33122 | -43.68411 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 725b3e09-22c6-39e1-af9e-3c9f917d1b9f | -7.14983 | -45.14458 | 2025-09-01 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd166a5d-ee3d-3843-b8e9-a34c85df1325 | -7.71587 | -50.26656 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94e2fe01-3d97-38a5-bd75-4754db1ba751 | -11.89407 | -46.69204 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dbfc8040-d802-3fbd-91bd-fa26fac9fc64 | -6.04812 | -44.2594 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a887a379-b3f6-3224-943a-32f4a767bb9c | -6.74298 | -43.78782 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f007b6e1-881f-3538-b07a-81d18feb1a36 | -6.15233 | -43.34932 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da56ca9b-8f13-3a05-889a-7147f585aa0f | -6.15997 | -43.32365 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67120a3c-3cea-3e2c-bc26-3cd2543da792 | -9.63379 | -47.80061 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03b553b5-f106-38e0-9d2a-5f19ced98ead | -7.07428 | -44.3469 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90363703-4860-3923-9671-c4e1b658735b | -6.09392 | -43.18714 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5087c63f-f47f-3a8c-9b8a-fd131b2a7c07 | -11.02442 | -46.85954 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7a9d579-ef2f-3e91-a836-4c10e7a45a01 | -6.16565 | -43.33228 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32ccd821-000b-3af2-be0c-c00402f17c1c | -11.04837 | -46.97531 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4f1f401-83fa-3476-9c75-0fc2ff7b8b40 | -7.7133 | -50.31002 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a888680-725d-3280-a36e-b23385e89be6 | -7.07942 | -44.36031 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| cb2a5394-ca34-34cb-94f2-87f00b528952 | -5.966 | -42.96369 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 79c08b41-f820-3574-8e77-95f4797ba1bb | -6.30959 | -43.62949 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56652a6f-981b-3897-b1c9-f6639790f1fd | -10.77309 | -48.83627 | 2025-09-01 04:10:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15099811-887f-3f67-88d9-511b7a92aad8 | -6.36138 | -43.55944 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0493461-8d51-37bc-912b-891aac4c80a0 | -8.88127 | -47.20976 | 2025-09-01 04:10:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 213c66f3-024c-3d12-8b37-ad9adf2c7cd7 | -5.49198 | -43.19623 | 2025-09-01 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38ff895b-ced6-3c31-a990-6301cebf2a22 | -6.13124 | -44.13118 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bdfc83ac-ca6e-34bc-bf0f-94ca1a7a7673 | -7.55585 | -45.93857 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f96c2459-7960-39e1-9f36-6160ffac4f5d | -6.18235 | -44.21387 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5686d9b-d9b5-3544-a58e-437097aba4c8 | -9.66572 | -47.0572 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b83a76d-06a6-36a9-aed1-2de5d44b7b7c | -5.99975 | -43.35972 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0a6d4290-ca6d-3be6-8d1b-eafa06e59ae6 | -10.04805 | -48.10323 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c117ab18-e6a1-3c64-bb2e-665e22e43b6f | -6.09048 | -43.18663 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fcc26432-fe9a-3dc9-a647-324fd1700241 | -11.8935 | -46.68995 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fef49f9-ac25-3400-9457-a4af2559a13a | -8.84494 | -47.51394 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ca20a92b-2ffa-37fc-a7ef-3ff6c77d3ee8 | -6.45286 | -43.9495 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fb77eec-9739-3e2c-bcdb-6a9a511a49fb | -10.92864 | -50.85556 | 2025-09-01 04:10:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3c0c9e1-b959-38bf-86e7-0f060e71c110 | -7.57959 | -45.20893 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7ac217f-8b1a-31a2-b6e3-34cf0b1db4b0 | -7.113 | -44.77465 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 705e1f07-37c9-33df-9134-ed4a2b365829 | -8.47272 | -45.17547 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e46078ff-39a8-36ee-9f2e-177cae917937 | -8.19768 | -46.77946 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| ea97ed66-05a3-3e14-92e9-06a976720e0f | -11.47677 | -46.79533 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c32b306c-0d6e-31bd-b8cb-e11025acf6d7 | -7.87885 | -45.17799 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a600637-ef33-35c3-a2cf-4558e590dee1 | -11.88451 | -46.74874 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02cf5d3f-b280-3223-894e-8fabd2fcbefe | -6.45223 | -43.95333 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e34b6443-8854-37db-9d24-ac74b9f90a43 | -6.21401 | -42.74596 | 2025-09-01 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 39892c23-3733-375a-aa60-f77658aa442e | -6.98238 | -43.11669 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2378ae9-2b3a-3bd8-8cc5-cfd09c3fc440 | -6.94675 | -42.01135 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 067d49e2-848c-32b0-829d-85b2c0ed7162 | -6.10077 | -43.18826 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 49e01e24-0013-33a0-beb5-542bd5fa2031 | -11.03199 | -47.02395 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f3d540e4-3069-31be-a369-cb28080fcc3a | -6.83806 | -52.81459 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56f73813-fb02-3399-b473-d1846e595abd | -11.02537 | -46.94608 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8f8e2acd-6527-354a-bcdb-9b668ba8f991 | -10.23771 | -51.10994 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0d4e1ed6-896d-3ac4-9737-d9efe3a9e055 | -10.24055 | -51.12378 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a2f805c8-fc35-3060-bab9-ad88b141337c | -11.42805 | -46.91581 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98c95a8b-3a5d-3c41-8645-5d563d4fdaa6 | -6.98179 | -43.12033 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e030d9d-3290-3b50-a8fe-e17a3b9888a1 | -6.24037 | -43.38581 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2cf532c-9e2b-34bd-8a48-5834ac86b107 | -9.12707 | -45.19495 | 2025-09-01 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 874f32c2-f98a-311f-8dbc-6a87dbd9d271 | -6.94342 | -42.01082 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7be9526-868d-3551-930a-668fe4cc2648 | -6.30448 | -43.61693 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 04c7c4c6-d908-3d1b-a22d-1c58dbe69cf9 | -7.95479 | -46.45134 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72a9ffe0-3855-3960-be46-00a3065a9790 | -6.81717 | -52.8249 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f010c5c-5a69-3efb-b3fe-e9201c108e3c | -6.30267 | -43.30005 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27fb2e54-c20a-3776-81d7-1b2aca486e2f | -6.82585 | -43.32563 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 7bbf73de-eec6-3872-ab5f-4d0a6cfc0b33 | -6.80067 | -45.69062 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8f99db7-0673-36bf-9837-1654452d7024 | -9.24064 | -47.05883 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33b3b042-583e-39e0-a2ea-f7a2b89f79c5 | -7.07718 | -44.35157 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a03702ea-cec5-3a71-9c7e-2b3567ee077e | -5.99854 | -43.3672 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 005ea9c3-0fb3-3ffb-a5d4-80e978cb51f8 | -6.33078 | -53.42658 | 2025-09-01 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8951529-8a72-389e-84fd-f1fd77abac39 | -7.3917 | -47.43908 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a03d6d81-7976-39f6-9742-ad2bac434478 | -10.23253 | -51.10895 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cac99d3-e087-362a-bfb3-08d2915708df | -11.89945 | -46.68318 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4bca308-dce5-36fa-ab32-3d936cf7fd5c | -6.94564 | -42.01833 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 49aab661-7cd6-35da-9245-3b4bfe393d98 | -11.04025 | -45.14163 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 16180fab-c894-3285-aee3-02a663935e0e | -6.1666 | -43.3394 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e03f169c-1a2a-3c68-b99c-22b7e2b743da | -6.81293 | -45.68792 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 193cb7d6-70c2-3ba7-9f32-a2ec9bf2346b | -5.73366 | -45.53032 | 2025-09-01 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85e791a7-e809-3282-9404-04a5b1efd907 | -11.02639 | -47.03305 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9bd01820-a0c7-34e9-afd2-897791cb5f1b | -6.81184 | -52.82153 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05171c06-1e38-31cb-b960-534f3f6f00d3 | -6.33392 | -44.47497 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa4b17c7-a2d5-37af-b1b8-98a8c900ba0d | -7.06848 | -44.33765 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 197919ec-d2d7-33c4-8525-873190b36bc4 | -11.04533 | -46.96967 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdcf62dc-b8b5-3239-b562-e3a2cb080af1 | -9.23695 | -47.07999 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 57cdac62-7323-3e57-9402-87ec2eb78b5a | -7.87273 | -46.95463 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb1b21fc-8931-36a0-b084-0c2aff0dffa8 | -6.23692 | -43.38524 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 662f85f5-d161-36c7-ab56-5ef0d62907d8 | -6.4497 | -43.96895 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cffdf78d-1fc0-308a-a42b-a0775c5e38ad | -6.26701 | -43.54073 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f93c86ef-b8be-332e-b229-97d5751e7502 | -7.41755 | -44.80736 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39a59250-7894-34a8-8f03-049d4113426a | -6.3777 | -43.54652 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README28.md)
