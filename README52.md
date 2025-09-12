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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d692540f-d373-3f65-bc79-21fd1253fdbc | -17.37239 | -52.92834 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8df91cf2-43f9-3fa5-a3b3-73e615b69c81 | -18.90635 | -46.67077 | 2025-09-12 04:08:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f0d45aa-c9c6-3cf7-a486-c79419b457fb | -19.64436 | -41.58858 | 2025-09-12 04:08:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 396396d9-ae1f-3a81-ba80-e0df952b905c | -18.75498 | -47.62138 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bd080a6-790b-3aa8-8005-7f1b23461cb6 | -22.51885 | -44.70925 | 2025-09-12 04:08:00 | NPP-375D | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e8226ccf-55da-3c0c-ae27-b075faa6e686 | -21.18911 | -47.53537 | 2025-09-12 04:08:00 | NPP-375D | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 427e0fb5-48b4-3d01-916b-20f262117956 | -22.63125 | -53.09232 | 2025-09-12 04:08:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c92ceec0-a39d-3d3c-80a9-0eb8ddf0af06 | -23.1226 | -47.49473 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7624e60b-b637-3336-9bbe-9990879571e5 | -21.65064 | -45.2812 | 2025-09-12 04:08:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 54cf63b9-1717-392d-b265-f67a32c6a9de | -22.18425 | -49.6016 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9f7d8889-8a10-3112-8ccb-fc4dfacf32db | -17.83656 | -52.05686 | 2025-09-12 04:08:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c05ac07e-308f-3c07-8ad0-bf81bf108606 | -22.18587 | -49.59344 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 795d38c1-e925-349c-bb07-c036015df85f | -19.74328 | -45.94944 | 2025-09-12 04:08:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8654403a-d9d5-3dde-bb38-aa93b1fae093 | -18.33333 | -52.06025 | 2025-09-12 04:08:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0f29583a-aee7-3265-a6db-681ba65cf530 | -23.14588 | -47.47114 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ea1c5191-b03f-3387-874d-93385ea7cd87 | -20.65466 | -46.53659 | 2025-09-12 04:08:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc72affb-ed20-3209-82ed-bb8fd6fb385c | -23.14229 | -49.66039 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| f0cb58d3-7e9d-3e8a-ab95-39e8df37d4c7 | -18.76409 | -48.53279 | 2025-09-12 04:08:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c441fdbf-6730-3fef-a68d-d496f92314ee | -23.10829 | -47.49914 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 40d9d318-e0e9-3081-b6dd-b38715fb0149 | -22.18849 | -49.73458 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| babace37-3ed4-35c8-85c1-6664345d59e4 | -22.82231 | -46.42891 | 2025-09-12 04:08:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ba9f1bb2-1bb8-330d-b56d-5aaba2ca409d | -23.42501 | -47.02737 | 2025-09-12 04:08:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3ced3f4f-8275-338f-9f78-bd0bf3e28307 | -20.35756 | -49.96021 | 2025-09-12 04:08:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15d2ea74-145d-30a6-a40e-98f7decb3553 | -18.31196 | -50.41823 | 2025-09-12 04:08:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 26ccbded-3919-3743-a008-5ed8dfa9c1b0 | -21.33561 | -45.03312 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cb2b706e-f6f4-38d6-932a-dc475608f450 | -20.23253 | -49.25977 | 2025-09-12 04:08:00 | NPP-375D | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c544ac84-99a4-38bb-a55a-565307e37869 | -20.01159 | -47.65783 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b5a19dbb-f76b-366d-a6d3-b9afefb02781 | -23.11361 | -47.49061 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 62811d85-6356-328c-b3b6-189882e8e263 | -19.87975 | -41.41392 | 2025-09-12 04:08:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7560fa76-3838-3019-9bab-ccbbca58603e | -20.35395 | -49.9617 | 2025-09-12 04:08:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6af93ade-fd72-3001-8464-60a619b69a9a | -23.37826 | -47.224 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3f94b7b0-859e-3038-bc99-8eb8a2b5579d | -21.1843 | -47.51906 | 2025-09-12 04:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a605fdd4-4cc7-3aa2-a364-d7db167c5522 | -20.27581 | -42.11357 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 79990a58-5c5e-3eee-95fe-a2bfb9426d13 | -22.65616 | -53.1055 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cd49a06f-bdfd-3dec-9838-f1690306fd2b | -18.66337 | -47.66238 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e16fdec-4897-3558-8662-c29c846cee1e | -21.84871 | -46.51198 | 2025-09-12 04:08:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9c5a609f-9a5a-379d-a232-ebfb94f4e8f0 | -20.01444 | -47.6422 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1920229e-6700-3a62-aec0-234633a0037c | -23.1198 | -47.48932 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3a323ce2-9d27-38b2-9a79-a978e93bff76 | -23.11808 | -47.49865 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 03baf075-2ae2-39c4-b655-d5ac26264749 | -19.66908 | -45.85941 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 063ce878-b3cb-3577-8b5e-06ce662c7e2a | -22.79012 | -47.80246 | 2025-09-12 04:08:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28a21fed-fed5-3bf7-8dc3-d258ec9fc087 | -20.56174 | -46.93241 | 2025-09-12 04:08:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4490110-6a87-3782-86af-5c17a21f3002 | -23.14224 | -47.47033 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5b009c68-1236-3e30-98d3-40ac5d640a15 | -23.1448 | -49.6553 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f98e81d6-faac-3368-89cd-a65445ceeb3a | -17.37799 | -52.91667 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef3ab243-5c4f-34a2-a475-3c89190603a6 | -21.1834 | -47.52398 | 2025-09-12 04:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c16e0c2-cd22-322b-89e7-4c199548d56a | -20.80573 | -46.88796 | 2025-09-12 04:08:00 | NPP-375D | PRATÁPOLIS | MINAS GERAIS | Brasil | 3152907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0bca8000-439f-3bac-8dc7-61e1cd04e404 | -20.11699 | -42.35519 | 2025-09-12 04:08:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 863c6e01-dea7-33c8-adc3-8a28add21fcd | -24.1683 | -51.03823 | 2025-09-12 04:08:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 80537faf-b426-3a04-a744-060351b514d0 | -19.98249 | -47.62032 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7756ba62-775e-3e90-83bf-63289e376ab8 | -19.62321 | -46.43829 | 2025-09-12 04:08:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| de53ab11-71b5-3afd-ab83-617142de030a | -18.53866 | -48.41741 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 3fec68b4-c6d5-3e7d-8884-70dc537c88db | -23.28399 | -46.47899 | 2025-09-12 04:08:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1c343198-25ce-3207-9c73-f1c974c9f81a | -21.62605 | -46.80072 | 2025-09-12 04:08:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b2502fe0-325e-3cc5-9561-bd7271922134 | -22.31423 | -43.65446 | 2025-09-12 04:08:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 685deef9-b287-3980-995a-8be280ef4cf5 | -18.53452 | -48.41658 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 82802014-cd18-3597-802f-8e7f6abb48bc | -23.27516 | -46.55096 | 2025-09-12 04:08:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 154a4527-f230-354b-b449-5e113a3ed065 | -19.36882 | -43.64985 | 2025-09-12 04:08:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01d22ceb-d3a6-3dc4-8edc-9bd42176a3b2 | -23.1365 | -47.15163 | 2025-09-12 04:08:00 | NPP-375D | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 95ec880e-0b25-3beb-bf51-86696564845f | -18.44914 | -49.56813 | 2025-09-12 04:08:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 02f5e07f-f4fc-3447-807a-b380f781131f | -18.82202 | -46.88292 | 2025-09-12 04:08:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b04e92ef-a799-38a5-825a-359b103954fb | -19.99323 | -46.92292 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d9064e5-8f10-33e8-b016-6b5f2322c9c9 | -21.1918 | -47.52076 | 2025-09-12 04:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 3a7b56a1-1139-3d3b-859a-5395c02f79e0 | -23.45124 | -46.70276 | 2025-09-12 04:08:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 71a26312-e0d7-351c-9c35-55b768db1481 | -18.76334 | -48.53674 | 2025-09-12 04:08:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f06de0f9-0ae3-3744-ad00-2468528a3b43 | -22.69608 | -46.21848 | 2025-09-12 04:08:00 | NPP-375D | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c54f677f-ed01-3788-948f-36ad9d5a4aff | -17.36763 | -52.92314 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0facb56e-ccbb-3443-bee6-2ce44535f463 | -23.3458 | -47.19575 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 10ec24ec-0d33-3c4b-8b56-c9912a61e598 | -20.23757 | -49.25645 | 2025-09-12 04:08:00 | NPP-375D | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| dfe90f79-8dba-35fb-a406-6c46480dd522 | -22.18923 | -49.59838 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7b604f1f-db6f-37ab-96ec-442ba744c90a | -19.9556 | -49.27075 | 2025-09-12 04:08:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fd4bfcec-6793-3c1b-b7e5-e190dbb30074 | -19.74856 | -46.08813 | 2025-09-12 04:08:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be0da2bb-f7e3-3d9c-a2bc-460eaf758cda | -21.34093 | -45.02222 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7fc3c3b1-ea3b-3170-b881-a6c1a29266dd | -22.18348 | -49.7378 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 943df220-51a8-3459-8198-c3dd6d471325 | -21.64998 | -50.11734 | 2025-09-12 04:08:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 81824ff2-c945-3b31-b0f1-d70fb67a1b99 | -24.79928 | -50.23027 | 2025-09-12 04:08:00 | NPP-375D | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 230c6b04-b08f-3ceb-a620-0e3f32b43d2f | -21.32934 | -45.00774 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bc2045d1-5d8c-3840-a514-67141a656df3 | -18.62387 | -44.26469 | 2025-09-12 04:08:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b5ed900-d169-3c94-8c42-10d9f9441a67 | -17.37755 | -52.95903 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97c153f0-8bb9-3b00-a588-19db6ecd91b0 | -19.23497 | -48.04503 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9df96d87-177f-3b4b-85e8-9aefc7a5e903 | -18.31565 | -50.42445 | 2025-09-12 04:08:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19116e52-98a8-3575-8215-8c64592a54c0 | -19.99707 | -47.6497 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c8348832-704b-3639-86b1-a279150a8a9b | -20.26345 | -42.12689 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 97e8fc20-f5a0-3b71-9565-725bfb6ac8de | -19.93187 | -43.8747 | 2025-09-12 04:08:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 93ce16f1-292e-3acf-b2fe-42eb44718e1c | -21.43225 | -45.47255 | 2025-09-12 04:08:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 13facfd6-1b3b-3194-b7b1-c4999492d30a | -17.37668 | -52.96305 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df5fcaa2-851b-3379-a587-91d332f9e48a | -22.60785 | -47.28074 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2985e794-6685-3940-a126-09892bd9df73 | -20.34955 | -49.96073 | 2025-09-12 04:08:00 | NPP-375D | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7f4fc6a-1269-37a2-a2f0-55ab3d862a91 | -23.16161 | -47.48888 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1053ef5-7922-3a76-ac76-e90d63c97a1d | -21.86589 | -46.49776 | 2025-09-12 04:08:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3d495b33-dc31-3844-b731-08d817c55c60 | -19.96892 | -46.8822 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8ad9505-5c3d-3777-b3f7-06ea6af26135 | -21.32999 | -45.00388 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1020941b-ceae-3205-b08b-e81697190cad | -21.95222 | -47.56583 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06d03eaf-9069-3e15-ab9a-e7e4778bede5 | -19.66179 | -44.90292 | 2025-09-12 04:08:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f5bbaf12-5707-3b1b-8beb-530b17fe728f | -22.18768 | -49.73871 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 0e279dad-0a2d-3829-9ff4-a61d754efdef | -21.70542 | -46.25284 | 2025-09-12 04:08:00 | NPP-375D | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0411d040-2950-3936-bf94-c3582fa8e152 | -23.83807 | -51.07827 | 2025-09-12 04:08:00 | NPP-375D | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| aa795908-a8e3-3432-89fa-a10a8479d74d | -20.1588 | -43.68168 | 2025-09-12 04:08:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 988a04ec-a8df-3940-a44c-e1b5bfb37356 | -17.76188 | -50.95439 | 2025-09-12 04:08:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bb733a5-3449-3007-8a24-c8116c3f1e8b | -18.38309 | -50.55807 | 2025-09-12 04:08:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README53.md)
