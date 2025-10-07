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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46256f81-6d8a-3ed6-bad8-33bd0bdf3360 | -13.09984 | -47.98438 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fddbc890-20b7-3af6-a5e7-1023611a0e5a | -13.21642 | -47.81561 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3f958df-3252-344b-af8d-1aca3b52b145 | -11.03714 | -50.92334 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.4 |
| eb943c35-d786-39a6-b57c-59b9748eec76 | -14.92114 | -51.40779 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b17ee345-5026-3899-b9e2-28593cac2bdf | -11.04903 | -44.78566 | 2025-10-07 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb85f961-d673-3038-854b-decb849ec22c | -17.56024 | -50.44547 | 2025-10-07 04:38:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9da6d042-f3af-3920-9182-8b2f9027b999 | -14.90989 | -46.86561 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 21e4efe1-45da-36ef-bc82-9f6a9bbfb116 | -13.24446 | -48.06598 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e96cc17a-541a-30c2-a623-0a02a5dc0b58 | -14.73158 | -46.02619 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d620d81-2288-3a5f-9dcb-12fd82767f38 | -10.40235 | -50.30373 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d3ef344d-b6c5-30e0-898e-4d1d57418a7e | -17.7137 | -40.24117 | 2025-10-07 04:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6bd595db-96c4-3397-9268-7e205f98a383 | -14.9673 | -49.9495 | 2025-10-07 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55195cab-e7e3-3b46-92f9-59de5ee329d7 | -12.98246 | -46.78455 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12fa2083-887f-34f6-83da-87e30598dca2 | -15.49864 | -47.92776 | 2025-10-07 04:38:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75b28bde-7f7a-3f84-97ed-60dedf04edc7 | -12.28566 | -51.36333 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1187b4f4-9aa5-3ea9-840e-7882788cc3e7 | -13.23631 | -48.45781 | 2025-10-07 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0d029fd-44eb-319b-9f49-ba2ee683f0fa | -13.10378 | -47.98135 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5368d55f-8326-3acc-81bb-55bc6f54940c | -12.25559 | -47.8496 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3e855d2-72e8-3ab0-be0d-36a877f6b115 | -14.73843 | -46.03181 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 1999ae03-b0a1-3876-8785-4e7efeda5705 | -17.28248 | -46.90929 | 2025-10-07 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c63c6d46-3ee8-38d7-8d24-1bef7e7e9466 | -13.07042 | -47.88063 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 09268ff2-381f-36ee-b32c-214af68dee91 | -13.32609 | -43.72806 | 2025-10-07 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9567907-ae2b-37dc-ad09-01bd06524eef | -11.38908 | -43.49169 | 2025-10-07 04:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a7b3f95-8a73-3b2d-841f-eea933cfe143 | -9.1707 | -59.55665 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 735521ed-0d78-304d-a084-8541152e3df3 | -15.61001 | -52.56248 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cdac1f61-19e1-3cda-b047-ba646b5792c8 | -14.63998 | -52.53244 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79931a29-1b40-34b6-91cf-0d171c4193ad | -10.9215 | -47.06944 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7665209b-26cf-38cb-8516-431171bf838a | -15.59452 | -48.76578 | 2025-10-07 04:38:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41fdfec9-fcda-3f31-90db-0864203d94e2 | -12.40162 | -51.13264 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38a3604b-1d85-38e7-9807-dfc6eeb13803 | -10.40514 | -50.30796 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4e616d3d-506b-3702-af47-719b1a3afcd4 | -14.76752 | -46.06903 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3c8af3ba-6c86-3e48-92b9-72ed8ddde71c | -15.7943 | -49.39669 | 2025-10-07 04:38:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8faf0965-cba5-3c68-beeb-7c61ab1d5e62 | -13.26673 | -47.57618 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 735935cc-6e39-302a-9fc8-6ba336cc43bd | -14.99074 | -49.96841 | 2025-10-07 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5f77b2e-37d9-31af-8dc4-87eea3bb234c | -13.01577 | -51.03009 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 592ca40f-c6ac-3a05-8383-e480c7bfc3c5 | -10.10968 | -58.53176 | 2025-10-07 04:38:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2336a721-6e8e-3d15-a51d-5804541025d5 | -10.45195 | -50.40634 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 29d68614-1ba3-30c2-9429-83a0fbaa5183 | -13.69179 | -47.33741 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61a2083f-eb43-3d60-9ced-b18714de58c6 | -14.5409 | -46.63811 | 2025-10-07 04:38:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 347327ff-d7a2-3395-b84d-ffec152d644f | -13.26132 | -47.18567 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbe1b34b-8611-3771-99f5-7df8f067bcef | -16.01815 | -51.04782 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5064c03f-db5a-39bd-9701-e548546acb50 | -9.25041 | -59.02184 | 2025-10-07 04:38:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae139eea-78f2-3b40-a114-254f382dcb89 | -13.34729 | -47.56976 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9101911-2f30-389d-8870-c65b755528b6 | -10.7453 | -49.71595 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c356c930-8c7b-38a3-ac31-9c19468a48d8 | -10.38878 | -50.30148 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9af18675-042b-3e28-b572-99be12c3a417 | -12.40381 | -51.14079 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36442f66-eb9e-384a-b066-a097e29972af | -10.62539 | -48.7054 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1c83ad0-52f4-3b63-9d55-20e59ffd464c | -13.24179 | -47.24565 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ffe41fb-157f-3ea3-9ed5-0a9951cb0a4a | -15.28311 | -46.33298 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d804d30-a3b6-3c7f-8aed-d6cada6e829f | -12.92809 | -54.72283 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0825ba0-508a-3128-89e4-56b352702111 | -15.26903 | -48.06582 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be49bac1-695b-38f1-9340-3c45af3aa541 | -13.37493 | -48.03385 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e239591-51d0-30b5-b80e-09cc12f9ef51 | -13.2439 | -51.68097 | 2025-10-07 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e05efd8-e58f-3dd2-9f25-d1880dc2f5b9 | -10.40275 | -50.32262 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1237e679-9248-3977-85f5-0618a177d6e7 | -9.60775 | -57.1393 | 2025-10-07 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d6859e8-c8c5-3530-8683-3bbc1dc975e8 | -14.77256 | -46.06048 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 4998d86c-009f-30f9-b53f-7deb89d4425c | -12.61466 | -44.75567 | 2025-10-07 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cb2d2598-1109-3265-8e70-89153d7b8b18 | -13.13506 | -48.00782 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 859664d7-75b8-37b5-b068-f146abf3abde | -14.63728 | -48.32734 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2bb2174-f584-35ec-8ff2-c53cd54bc984 | -16.31854 | -47.90919 | 2025-10-07 04:38:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7264d6ad-6c9d-3782-9d66-33ec626bd8e2 | -18.28825 | -45.45896 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d410a67b-c344-3eb5-88a9-b13147ed0398 | -11.02255 | -50.9139 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f96ece6-ba1d-3e3b-be42-e20b9ca63cd2 | -11.84624 | -45.06682 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c371deb8-29df-3824-9673-6c35dc500b25 | -11.21037 | -54.98737 | 2025-10-07 04:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f1ec4d3-f33e-3ce7-a18a-d916a6524ad2 | -13.27819 | -47.57024 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a8f3181-6c11-3f2d-a8dc-5cdd41872299 | -13.28341 | -48.06098 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7180b02-f432-3c1f-935f-9b7fe418dc36 | -11.95022 | -46.43848 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4120abb0-648c-3f9e-adcb-865d4634ec73 | -14.64914 | -48.34083 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1de7b7f0-8b63-31f6-81d1-b067f4dd7b5f | -12.89758 | -54.75152 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8cf4620e-df36-3dd6-a10a-ac9203c90bf4 | -14.7706 | -46.07421 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5a5c2b0-bc0f-3cee-9a02-c2f1ac74a281 | -13.58753 | -51.82603 | 2025-10-07 04:38:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 726204d6-5844-35fc-9226-f8927b1c7465 | -12.99545 | -46.79004 | 2025-10-07 04:38:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7998517f-5d90-3faa-a5dc-5af4998200a8 | -16.05563 | -50.98675 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c7fb0e4-45df-3f32-b707-3f6ac11118d9 | -10.81438 | -48.59833 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2d9eac7-0908-3c3d-9919-701dfc5889cf | -13.22436 | -47.80931 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ca83f162-e3df-3007-86be-7ac13d8244da | -11.29774 | -48.27265 | 2025-10-07 04:38:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a680810c-1cfd-338a-8235-40ba24fbaf40 | -13.06525 | -47.89179 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e26cda7-84fe-31d4-aa62-1d7c30bfa087 | -10.92379 | -47.07751 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8725479e-ab3d-3ec0-9f69-a9a0d6875e7c | -11.9457 | -51.47363 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51938c67-5295-3a2c-8f92-9b1ff2fecd66 | -14.77142 | -46.04162 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ded0330f-26ec-34b6-9939-abf3a8933809 | -12.4018 | -51.06685 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7dab9196-6c4d-3ce0-ba0a-beda74f4bc61 | -11.04731 | -51.6615 | 2025-10-07 04:38:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2c021ae-8aa8-3818-8d55-41ab01b3d03e | -14.3471 | -42.34903 | 2025-10-07 04:38:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5eb468b2-ac37-32b5-9b4e-65f18a28218e | -16.37816 | -48.99969 | 2025-10-07 04:38:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6d17f28-551f-3748-ac9e-8ddf130c5f17 | -15.22243 | -56.77164 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40b438be-a209-3d6d-9f48-2cb049d5a2c7 | -12.42981 | -54.50265 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8e901a2-d014-33be-94bd-68328ddceb39 | -16.02692 | -55.98646 | 2025-10-07 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f6b739d5-7c23-35f9-a87d-18926e0bee01 | -18.51353 | -43.91048 | 2025-10-07 04:38:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19de382f-dc56-3cdb-aea6-01fd48c69c2d | -13.22395 | -51.69352 | 2025-10-07 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5312c9a-e182-3936-83c5-9b0192c6d03c | -15.35744 | -47.30573 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78f67e16-f1ad-35d1-a6dc-30c4bba25bc2 | -13.2648 | -47.16199 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| debf4ccc-cd14-3668-a3c7-dbc05e9a3dfc | -18.2906 | -45.40945 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64db40ae-a975-347c-9a11-1101c4ca648c | -13.36215 | -47.25602 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62018c99-9b62-3da3-8877-a8128c1f11e4 | -14.91706 | -46.86679 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7d5a7af-70a4-3a5a-ae98-af430ab89214 | -13.35878 | -47.56358 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36dbe593-53c4-3609-a3a4-be4e7e8f1250 | -10.40914 | -50.30486 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a7b18f9f-4523-3543-a98d-f8e69508dc07 | -10.82445 | -48.81625 | 2025-10-07 04:38:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e788b047-3630-3397-ae0b-946452568048 | -13.26646 | -48.05828 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0377989c-c36a-3dc8-89db-de7b1f242d77 | -9.90941 | -60.19646 | 2025-10-07 04:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca615007-66e4-354a-a0f2-682c6a087e00 | -12.18234 | -47.78225 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README70.md)
