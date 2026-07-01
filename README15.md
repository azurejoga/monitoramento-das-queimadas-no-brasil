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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b11c1a4c-8953-3aa3-b1ca-ffdc8cfb680d | -13.17283 | -46.02436 | 2026-07-01 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6c5d78f-007b-332b-9b00-52e662a4e098 | -12.05153 | -55.45566 | 2026-07-01 04:38:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff57f7c5-1f39-3b28-a2e7-492e03c5689c | -10.79194 | -53.54618 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dfd20b8b-66ab-38be-9f3e-083a9b591ca2 | -12.4105 | -58.40366 | 2026-07-01 04:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 894a0482-495a-3276-b0b3-d69377ff3ac0 | -12.7671 | -44.49462 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| b13dee2f-c59b-3a86-9132-ae5e38bb6a1b | -10.67264 | -54.5346 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 51ace8e7-a6a4-3d65-9e43-14d43816abe3 | -7.47557 | -44.75058 | 2026-07-01 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 443be71c-0747-3419-88ae-fa92674e375d | -8.3447 | -46.81955 | 2026-07-01 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d3a962e-184e-3abf-a90e-d25d36562e1b | -9.20044 | -45.33061 | 2026-07-01 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9e16cb1-df85-3db1-a6f9-51e436faf016 | -12.66926 | -48.22154 | 2026-07-01 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd3c20d0-8487-39ea-936f-fa9eb1541024 | -13.4725 | -47.8768 | 2026-07-01 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e311c048-84ab-3c98-8237-bff82b4179f2 | -9.68525 | -56.10239 | 2026-07-01 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a50a8a0-3311-3e64-8252-7ebf8d577baf | -8.12829 | -47.88114 | 2026-07-01 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84d25bbf-0e3c-37b1-ad64-94c0a5a0ea1d | -8.59526 | -48.00373 | 2026-07-01 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9b5e44b2-367b-317f-9325-dd95bb65d87b | -11.49408 | -49.87439 | 2026-07-01 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c3411df-20f9-3661-9832-d995127a3683 | -11.62922 | -59.02289 | 2026-07-01 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 55018c19-2a9c-391e-9a57-f0dc95574ca7 | -11.4374 | -55.91526 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88b625f5-ee00-3511-90a8-388c3c2f9af5 | -9.59754 | -56.92631 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db0b5f95-6b6d-3bc4-ade7-e8772f99e7fe | -7.74474 | -44.18808 | 2026-07-01 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3b63805-2425-37ce-ae78-ac08af741408 | -10.76865 | -53.54386 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 93de1a34-6a1d-3943-8b2c-1a774467f86c | -11.83868 | -56.9471 | 2026-07-01 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7bee0841-0cb2-36bc-8922-19de6b8dc608 | -10.81018 | -49.33675 | 2026-07-01 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3db1e6b-4842-3dff-9a1b-3e696b892b48 | -10.37845 | -49.5861 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 892c10b3-8f5c-37a7-b78a-61513d08c262 | -13.72901 | -47.87501 | 2026-07-01 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5574f9b9-9605-32fe-b30d-1061ec520b97 | -12.76039 | -44.48915 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e7f5dde6-c6ab-3019-8078-64d2248d96a8 | -11.42602 | -56.05642 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 22d34c59-d7f9-3b16-a8da-82e7fca63d50 | -11.43549 | -56.06138 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8454c672-06a6-30bc-995b-fd25005bcb4f | -11.43798 | -55.91496 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe425c58-60fd-3863-ba10-d7fb4ee85849 | -12.76406 | -44.4897 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 785e91e2-bf1b-3ca1-bcb6-3544111cd7d7 | -12.84243 | -44.35565 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| d09bfb01-6a58-3d03-b13d-60357586f68c | -12.15058 | -57.2215 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9be58c2e-9e54-34dd-96dc-8bff6c57df89 | -10.97544 | -49.67105 | 2026-07-01 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f92f423-5218-351a-bc06-2f77e8c123d1 | -12.83872 | -44.35509 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| b2051c26-9151-3c4c-a962-d384082a3a68 | -9.59822 | -56.92263 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 979ef11b-5d97-34ae-b517-c4d61b1dd800 | -7.74196 | -45.9201 | 2026-07-01 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1a12476-3555-3dde-8fbc-4047c5616bd0 | -10.78515 | -53.55098 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a37fa8df-4d63-3ecd-9a3a-9a4364c218d8 | -12.77206 | -44.48642 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 4b856161-f32a-3958-a7e2-34e72814e37e | -13.72457 | -47.88152 | 2026-07-01 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca1a619c-6f49-3110-b587-32cb5f6608d6 | -10.12445 | -52.1002 | 2026-07-01 04:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8b434f8b-63b8-371e-8fc6-3c37560310c2 | -12.41788 | -58.39658 | 2026-07-01 04:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aeb1e3ba-c260-351c-a9a9-82a205072bf6 | -12.67251 | -54.58455 | 2026-07-01 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1635237c-76b1-30e2-b321-ab732c747a82 | -10.78586 | -53.54686 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04c0814c-b8a6-3293-aa45-07609fba2a83 | -9.60918 | -56.92491 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ed6d4b5-eb6e-36f2-b114-39c3fde479b4 | -10.93058 | -43.05548 | 2026-07-01 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ec3a74f-af59-3828-bf0a-9ff9fd2135cb | -10.12622 | -52.08997 | 2026-07-01 04:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 74f1396d-ead4-30d3-83e7-70802fe7c291 | -8.59803 | -48.00784 | 2026-07-01 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| d8c0b646-0dea-3177-a837-cbbd8c1f4ce6 | -12.76774 | -44.49025 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 28b9a792-0be4-31a4-b596-a82cfadcfda9 | -10.12841 | -52.10089 | 2026-07-01 04:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db55e673-f9f1-3d81-ba76-383c2bdb37ec | -10.6735 | -54.52985 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 6c4b0e25-a775-3d3d-9524-bcfdc566fc11 | -9.08428 | -59.49088 | 2026-07-01 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85ab04ad-11dc-3e69-94c9-969d09da9463 | -12.84 | -44.34617 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| fb06192f-dcb2-3ce4-a568-7f938305f500 | -7.74828 | -44.18856 | 2026-07-01 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72c98004-98c5-36d5-9e65-3af6b28d94e4 | -10.37782 | -49.58994 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c4ad6e9-992c-3ee9-8b1a-6f098dae3062 | -11.90176 | -57.38379 | 2026-07-01 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a0a089d-6225-3fe3-b143-8c2f6dba9749 | -9.69874 | -47.69299 | 2026-07-01 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c453c5b-726f-3d46-9170-7d9d0d980a21 | -10.65796 | -54.53689 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f839f68c-9c51-3ac6-a758-94f298e37efc | -7.47787 | -44.75865 | 2026-07-01 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f4a5993-c850-39b4-a8e7-5c21868cb2ef | -10.38612 | -49.59033 | 2026-07-01 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba8e82b4-c089-3f4d-9238-7b04aeb12062 | -8.12494 | -47.8806 | 2026-07-01 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cceff792-5fee-308f-84ec-3c6ebb127cd7 | -9.02862 | -59.5424 | 2026-07-01 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c31cd24-7073-3b3c-a99a-cb202159a379 | -9.97478 | -48.24512 | 2026-07-01 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90109a46-1af7-39ae-a9a5-1b62b64d1202 | -8.12158 | -47.88006 | 2026-07-01 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3006ae24-4bb5-3429-a8e7-fea2f75f6632 | -9.19417 | -45.32583 | 2026-07-01 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3786cb3-d67b-3092-ae05-65a8918c729c | -11.6232 | -59.02151 | 2026-07-01 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da3641d7-3426-3b67-9dc9-3229502139ab | -11.42431 | -56.06541 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 4311cf07-3073-3cb8-a33e-ba51fdefc7ac | -12.83809 | -44.35954 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c37c568b-8e53-336c-80ce-6e23384f5683 | -10.65882 | -54.53214 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e0d7d10-aa04-3dba-842a-dd8d4d267b04 | -8.64972 | -47.77263 | 2026-07-01 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e793300a-7791-3567-ab32-56784530165b | -13.72845 | -47.87854 | 2026-07-01 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30f4a6ff-ecb8-3124-8ab5-ef9c07459c36 | -8.52149 | -54.77146 | 2026-07-01 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3e5edf8-09fb-3e77-98f6-cb973e7d5d48 | -9.02041 | -59.54071 | 2026-07-01 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b67fb67-d372-3a92-958f-5ade21ef3f8e | -12.83258 | -44.34502 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a7a79a65-df76-3e01-b3c6-9843482df7d9 | -12.84307 | -44.35119 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| fb72ec7a-b1f2-3196-afcc-0e088b095da6 | -10.79268 | -53.54212 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23adffb8-18b4-3a17-b872-91fe787919a3 | -8.59066 | -50.98112 | 2026-07-01 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d043851-0de2-3462-a445-1140dc0e97ef | -11.54308 | -47.45502 | 2026-07-01 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ddf8bcef-8932-33ff-99ba-065d6e881998 | -11.91867 | -43.39222 | 2026-07-01 04:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36382f0d-5ad1-3acc-b97f-8fdbbde0ccba | -10.78945 | -53.55175 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9bdb61b-51d5-39d4-90ed-a6db48b18498 | -8.72665 | -47.83906 | 2026-07-01 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ba31342-ca26-37be-816c-01e2a100385d | -8.59521 | -50.9772 | 2026-07-01 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30bd2c59-6485-3605-81f7-7a4a0ea442fa | -10.79017 | -53.54763 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16bbf560-6c45-34f4-a569-feb115a21100 | -8.52394 | -54.77343 | 2026-07-01 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1703814-630d-3a55-ab12-1e0ccbb8692a | -7.75121 | -44.19304 | 2026-07-01 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52f2463e-6731-373b-acef-5923c8fdba7b | -11.63111 | -59.01347 | 2026-07-01 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 84db5943-fee8-3475-a4e9-a098acecef00 | -9.60234 | -56.93108 | 2026-07-01 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3127f0a8-00c1-3e1e-b140-27d5d9b5c13b | -9.0221 | -59.5411 | 2026-07-01 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bf3452e-c182-30ba-ad06-3b9ae0fe29b6 | -8.63844 | -47.5291 | 2026-07-01 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f74b4f6-ae60-3d12-aa7f-a524ec3e8a46 | -11.91037 | -43.77587 | 2026-07-01 04:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aee9999-809a-350b-98bd-6a593a6a4d8d | -11.53422 | -47.44636 | 2026-07-01 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13d8b670-46a5-3327-a76b-110d5e5ca103 | -8.72722 | -47.83553 | 2026-07-01 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db20cc36-8580-3433-8400-7f828c6fdae4 | -10.84858 | -56.65681 | 2026-07-01 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78d4806d-951d-3a16-810b-dd58fd7e766e | -12.75975 | -44.49353 | 2026-07-01 04:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 957651ff-31be-3a1a-95ee-a2c11d123bb8 | -7.2916 | -46.24897 | 2026-07-01 04:38:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4147a392-dff9-3491-9789-393610ac40ac | -11.84333 | -56.95148 | 2026-07-01 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c801a3a-36ab-3bc8-a39e-da1da97f9a66 | -11.8852 | -55.53042 | 2026-07-01 04:38:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbb96e19-ef22-3641-9a85-195b56098dda | -11.53887 | -49.77525 | 2026-07-01 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efc88b24-ffdb-3449-9d72-e0bf8ddcd717 | -8.13836 | -47.88275 | 2026-07-01 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8c98e9f-f654-3a7b-950c-06c59c8866b2 | -11.62414 | -59.01684 | 2026-07-01 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 311d0303-e131-3e5d-b2ac-6720a0d5c58c | -10.67724 | -54.53544 | 2026-07-01 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| d28de6d2-7ac2-312a-92f1-79da12dc3858 | -8.65029 | -47.7691 | 2026-07-01 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README16.md)
