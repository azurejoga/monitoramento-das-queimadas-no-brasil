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
| 04d61bd7-46fe-33ba-9e9d-5f3cd3408cdf | -9.49145 | -45.42002 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c3f3b5d1-1a8e-32f5-89bc-fc7d424438a2 | -6.88892 | -43.74786 | 2026-09-17 03:36:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f88d953c-5cf5-3beb-9721-c7b54e222dee | -7.36704 | -38.98229 | 2026-09-17 03:36:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0d9d5b16-9c60-3483-add8-87d7d35603e8 | -9.96169 | -45.3196 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| abd199a1-d2ca-3021-9873-4c8a1b8fec16 | -6.76578 | -42.77257 | 2026-09-17 03:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7654c2a5-5692-3662-9342-97d753a39764 | -7.08845 | -41.84469 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a6a106ac-657a-3ed0-bac9-2b4a8a71619c | -10.11377 | -45.57755 | 2026-09-17 03:36:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a95f0b15-02ba-3e64-b03c-7d26b2b808ae | -6.03598 | -44.03566 | 2026-09-17 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 61451eae-92fb-3520-8c1a-a801e593c205 | -7.04114 | -42.07039 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5bd3c9f0-3f94-3b34-9f3e-fbeeda0890e5 | -7.10408 | -41.82791 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 40faa45e-8fc1-34aa-a54b-3ba7669dc6fd | -6.94452 | -41.70136 | 2026-09-17 03:36:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bba14471-181f-3cf6-bd15-f947a1fcb23b | -6.04316 | -44.03629 | 2026-09-17 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 22b0b4ab-906f-3f1c-84bd-345869f58c08 | -8.2569 | -42.15995 | 2026-09-17 03:36:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0f100500-2e6b-36a9-9f98-3514e12246d0 | -11.27604 | -43.4728 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25964069-b061-3fd0-8837-642ee15e03a8 | -9.61257 | -45.35378 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a8bd88a5-39d2-3d8f-9fca-b59aed4c021b | -8.94873 | -44.39939 | 2026-09-17 03:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e34b590c-7694-36e0-9c0e-966f415b2d00 | -8.90586 | -43.8907 | 2026-09-17 03:36:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b61a36df-cf7c-37bf-b43b-68eb0536d8df | -8.58447 | -44.5809 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 08bdee21-c3d5-386d-8aa7-8add1eb661a5 | -7.36251 | -38.97849 | 2026-09-17 03:36:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8f377f31-ca70-3678-822e-0c898859c759 | -11.26977 | -43.47149 | 2026-09-17 03:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12096a40-7412-3ec6-afd7-c79917be1eba | -8.26723 | -42.17224 | 2026-09-17 03:36:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1ef723b6-6869-3dfb-aee9-9daf81253240 | -7.12156 | -42.16633 | 2026-09-17 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8e63675c-1d7e-3ee3-b554-5971fbef2978 | -11.36295 | -40.05941 | 2026-09-17 03:36:00 | NPP-375D | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1ee43599-4dfe-3a09-bd0d-3db4807c8350 | -6.03251 | -44.0347 | 2026-09-17 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0a5db02-0218-3dee-beee-5837b7ae66b3 | -7.36198 | -38.98148 | 2026-09-17 03:36:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| af554bde-6422-321c-893c-980279a2fe70 | -7.35652 | -44.48309 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8dcf0e1-5a60-3dd8-8595-7ed43b409725 | -7.02864 | -42.06876 | 2026-09-17 03:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8e6d98ef-8813-3ca3-912e-836200c4dd96 | -7.18932 | -41.80699 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a1dbb090-04ed-3cdd-9ad3-f9c33a158013 | -11.19951 | -42.82221 | 2026-09-17 03:36:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03236508-f2b3-36ed-ba3c-fcf837d59557 | -9.62379 | -45.36552 | 2026-09-17 03:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5cce7a1a-6c17-32df-9cc7-304ae0d54f36 | -7.94616 | -44.84004 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba3d0538-da7b-3ede-8ce9-e6b8231dcd62 | -7.93908 | -44.83823 | 2026-09-17 03:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f37c9d37-664b-3b8b-8f0b-f53d991afd60 | -7.37314 | -38.97715 | 2026-09-17 03:36:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 10ea93e4-8ca2-3ef1-8ae8-f2aa5a90e8df | -8.25508 | -42.16959 | 2026-09-17 03:36:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c99d689f-ad29-310e-b183-623b63a02dc1 | -7.08861 | -41.84085 | 2026-09-17 03:36:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7304f707-5508-3173-a6cd-2927883fa8d5 | -8.58722 | -44.56728 | 2026-09-17 03:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 27144d86-fac1-3f6d-a5ff-a3eaf6b81a70 | -13.43149 | -43.81547 | 2026-09-17 03:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 62c8fdb8-505d-387a-a5d7-a866d6c0bb4a | -11.8876 | -43.82325 | 2026-09-17 03:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b40b3c0-f58d-3723-b8c8-dc0698775a96 | -13.43727 | -43.81106 | 2026-09-17 03:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d781181d-f5e3-3b38-8822-8719e59eeb1b | -13.43767 | -43.81671 | 2026-09-17 03:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f0fe6e51-b770-3ca2-af7e-64485cafa860 | -14.18505 | -45.14347 | 2026-09-17 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d19e8102-4f8c-3c18-bf53-3bc912fe9a27 | -16.99887 | -45.46842 | 2026-09-17 03:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5bee2c9a-2619-3846-b369-1221500e30e1 | -14.55852 | -46.59973 | 2026-09-17 03:38:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5f2be7ca-1002-30bf-92a5-c46b3a24c7ed | -16.99134 | -45.47227 | 2026-09-17 03:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff8e7273-786a-379c-b267-8360818b4759 | -11.35107 | -44.01856 | 2026-09-17 03:38:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ee15eca-9baf-37a2-ac68-9fa2c8d10e07 | -13.58388 | -45.4752 | 2026-09-17 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be5d6480-f480-3297-abaf-940fb2b5c4bc | -11.35524 | -44.03091 | 2026-09-17 03:38:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 029eed28-4259-3edc-b0f2-0d1eab1b7601 | -14.5561 | -39.64569 | 2026-09-17 03:38:00 | NPP-375D | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 98860ca8-515c-3965-a3a5-e3d74189e225 | -17.77331 | -46.47702 | 2026-09-17 03:38:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f76a2f33-683a-35ec-a8bb-1265c26bc592 | -11.35638 | -44.02542 | 2026-09-17 03:38:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54f6fffe-92e5-3c5f-8d83-06165d531ebb | -16.99252 | -45.46689 | 2026-09-17 03:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f523267d-0268-388c-a1cc-355a022f2dce | -16.67126 | -41.84692 | 2026-09-17 03:38:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c003fb8-4355-3977-bbc2-2d8e9769ad16 | -11.88867 | -43.81801 | 2026-09-17 03:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8e9d5c1-ce33-3460-b30d-90f1cb72448c | -16.99267 | -45.47122 | 2026-09-17 03:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff530438-4350-35fc-9925-881838335b03 | -12.19848 | -43.47979 | 2026-09-17 03:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3428a90-7bc1-365a-95a2-d9dce3daef69 | -16.99768 | -45.47383 | 2026-09-17 03:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3be7864-57d5-3d0b-95f8-b0fe2ec106d3 | -13.43623 | -43.81597 | 2026-09-17 03:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 04bdd5e3-5627-3a1e-b49e-2d49153b8879 | -14.13722 | -44.0128 | 2026-09-17 03:38:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b58ebc62-53e0-3f35-ae93-1500bf765de2 | -16.99902 | -45.47277 | 2026-09-17 03:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0eb12b21-1bd2-3fb4-9337-844321d62374 | -14.55315 | -46.6055 | 2026-09-17 03:38:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d8a2f67-c514-37f3-8a8e-2d8e1333b09b | -16.67173 | -41.85104 | 2026-09-17 03:38:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2573e59c-bc78-39a3-90fa-11c2324dcfb3 | -16.6706 | -41.85023 | 2026-09-17 03:38:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5283ad2b-e202-3075-a009-0baf0180a843 | -14.55701 | -39.64092 | 2026-09-17 03:38:00 | NPP-375D | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 51b2463d-8c87-3d6a-affd-7f88659a1849 | -14.13109 | -44.01136 | 2026-09-17 03:38:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65854d01-1fb8-3b3c-89fa-52ff7e1c0ce2 | -11.89286 | -43.82984 | 2026-09-17 03:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c15a1d2d-a499-321a-8d86-e8e3e6fdb0b9 | -14.5602 | -46.60719 | 2026-09-17 03:38:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be32e13b-66fb-3d17-ace9-f24007461513 | -12.84823 | -44.39581 | 2026-09-17 03:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f499dd3-f79d-383f-b482-3cde1a3306a6 | -14.1362 | -44.01767 | 2026-09-17 03:38:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a9fea7ca-106b-382d-9905-15a9b1538ad7 | -13.4325 | -43.81056 | 2026-09-17 03:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3f80f389-fdd5-3e3e-b9c0-c7e00a6bb09c | -13.74249 | -39.01564 | 2026-09-17 03:38:00 | NPP-375D | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 61b31d50-ffdc-3b10-a6a7-d319e2fcf0ca | -16.67242 | -41.84771 | 2026-09-17 03:38:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 80064743-9940-35fe-b38e-61f7cdc7ccd9 | -14.18626 | -45.1379 | 2026-09-17 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24e9b2cc-2d0b-35d4-a323-d44b9ca13075 | -11.89394 | -43.82457 | 2026-09-17 03:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b4983f0-b013-32b3-8111-f7b54dd12007 | -11.48106 | -45.76993 | 2026-09-17 03:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 561c23ae-b1b2-30bb-beeb-3600ab79ebe4 | -14.55479 | -46.59836 | 2026-09-17 03:38:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83e46cc0-d60c-31d8-bec7-2180bcb68631 | -17.00024 | -45.46737 | 2026-09-17 03:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a8d86de-74fa-3148-a0a3-869c5e9e5dc8 | -16.99389 | -45.46585 | 2026-09-17 03:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62526555-ae82-3e8d-a319-8b18a9ea974a | -14.18263 | -45.15464 | 2026-09-17 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1df8018d-04ee-3e41-8406-5e6903affcb4 | -14.18384 | -45.14904 | 2026-09-17 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6dfbf6c9-fa91-3e06-a766-c226329499b5 | -13.15745 | -43.24448 | 2026-09-17 03:38:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 012bbbae-b2f7-3166-a271-c7c8c576efeb | -15.06248 | -40.99268 | 2026-09-17 03:38:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d9f4cd55-25e7-393d-9ea4-943919ad2028 | -14.78887 | -42.68925 | 2026-09-17 03:38:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83e04c99-edf6-303f-b533-448d232bc57f | -16.6764 | -41.84805 | 2026-09-17 03:38:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d1a8663-9f75-33b0-baf3-cb278e08852a | -16.67573 | -41.85143 | 2026-09-17 03:38:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bc01c3c0-8a5b-304d-9ec6-4729a0b5b7b8 | -14.55692 | -46.60691 | 2026-09-17 03:38:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cf77fbc3-d1cf-3d12-aa27-bcaf7a879d9d | -12.84939 | -44.39027 | 2026-09-17 03:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76f773ea-bd3f-3590-bb5c-1115a3fb9447 | -14.55239 | -39.63992 | 2026-09-17 03:38:00 | NPP-375D | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 58814789-ae95-38ff-9e16-09c9774ad0ed | -14.55857 | -46.61432 | 2026-09-17 03:38:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9d9d8d73-e0be-3dfd-b60d-5d1513be0634 | -13.73798 | -39.01475 | 2026-09-17 03:38:00 | NPP-375D | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| b9e96138-990e-3d5e-ae31-564f8183e3e0 | -11.4796 | -45.7768 | 2026-09-17 03:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88ddeb97-c03d-375b-9dd3-f8ceccdb92f1 | -14.79441 | -42.69081 | 2026-09-17 03:38:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 23ae96da-82b7-3a91-afb4-45a7efb1d976 | -11.89501 | -43.81933 | 2026-09-17 03:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c521c2b-e220-3c62-aa51-f26a8aaa241e | -14.17732 | -45.14738 | 2026-09-17 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11e962ae-8c57-3392-ace8-5e3b61c1aab8 | -15.36292 | -42.19432 | 2026-09-17 03:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e035ab54-675e-3eb9-8134-1da730894734 | -14.1761 | -45.15295 | 2026-09-17 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67eedce4-bf60-35f8-95f0-dd407ab1621d | -9.6087 | -45.3772 | 2026-09-17 03:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| f43637e0-eb5e-3d9a-902e-0fb2dc02739b | -9.628 | -45.3521 | 2026-09-17 03:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| c1ca23af-2acc-338c-9c37-14d4ed10dd29 | -8.4796 | -57.6478 | 2026-09-17 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 5b47ffaf-9131-3789-875a-88f22154e0ed | -8.4797 | -57.6282 | 2026-09-17 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| da4472e2-66df-3626-8c64-74af6ea97bad | -9.112 | -45.7294 | 2026-09-17 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 316.7 |


[Clique aqui para ver as próximas entradas](README19.md)
