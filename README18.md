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
| a20e20dd-446a-37a2-ad2c-073c012dea3f | -11.18089 | -54.86386 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28de6494-56b4-30d0-a231-a9b78f3a85b0 | -14.4312 | -45.66755 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 811e8ce1-8a7d-3e97-8d72-1e1f56ce96eb | -9.08654 | -59.48087 | 2026-08-07 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40c5bab4-b710-37e1-b8ec-1eb41639c0f1 | -14.33943 | -54.93511 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 798d812b-aad6-359a-bb14-04b62c73ab0b | -10.6851 | -50.49859 | 2026-08-07 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 935d291a-27f9-3217-8864-76a7b1c9479b | -15.07116 | -53.59166 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 470828e9-0b82-3720-83e8-72f97b5a695a | -12.58757 | -46.90596 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 491f6b8f-c35a-314d-971a-f157ae31baa9 | -14.21216 | -40.98448 | 2026-08-07 04:46:00 | NPP-375D | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 689a9348-b1d1-31cf-bc90-05f074eb3c71 | -14.42807 | -45.66216 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 235d9a4b-b6e3-3964-8785-500b94d1274e | -16.17062 | -47.88736 | 2026-08-07 04:46:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 91eae86c-7077-33e7-b934-d9f31c13e7ba | -13.42386 | -57.02529 | 2026-08-07 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3f9b5f6-6d81-31e3-a80a-5cdcb6f0d364 | -12.57704 | -46.90428 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44dac6a5-43fe-3818-964a-cc41dc5abf06 | -12.33164 | -53.16945 | 2026-08-07 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcb1e93e-abe8-3dcd-958e-d025273c059c | -12.56236 | -46.93056 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f09d1596-c93a-3c33-b201-8798c853869d | -13.62305 | -54.67213 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3bbe92e-5ff4-311f-9aad-25621de4f978 | -14.35186 | -54.91172 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf1e3fa4-78ec-3085-8ce2-652c33c4b9b3 | -12.63262 | -46.89323 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14e1758a-32e9-3d62-ad8a-342ed0fb29c6 | -11.14173 | -44.47878 | 2026-08-07 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 00a12bd2-32cb-3a67-b60f-f240ae58da02 | -11.2059 | -49.80225 | 2026-08-07 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cf42806-025b-32b7-b78e-56c326dd0dd2 | -11.15151 | -44.48708 | 2026-08-07 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09cff68c-e999-3fe5-b43f-8c4457819fbd | -13.77438 | -47.17721 | 2026-08-07 04:46:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6876d41-ee34-341c-b189-2d0223896930 | -15.89625 | -48.00984 | 2026-08-07 04:46:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14595170-6a6c-3544-80e2-14e6bc45f0ea | -11.46365 | -44.56683 | 2026-08-07 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e425318-82f7-39c7-a030-4c5a085e3b00 | -13.00509 | -42.67207 | 2026-08-07 04:46:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a99cdcbb-04c1-3695-9170-e2f8b7cce3c5 | -12.62912 | -46.89258 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68a7ca1c-9631-3031-a434-103ed3112f7c | -11.72738 | -56.84472 | 2026-08-07 04:46:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 462f6f88-bf94-3532-af0a-f146355fae50 | -11.18783 | -54.84913 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4370fcb-a711-3435-91bf-edcd96d76102 | -11.33711 | -45.21945 | 2026-08-07 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4087ca20-3342-3fb2-89db-638df1a45b3f | -11.18646 | -54.85691 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd157b94-d818-3783-9c7b-b46f6a60198a | -12.55703 | -46.94232 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d053686-2ea0-3202-a6b7-9498eef27c2a | -15.89867 | -48.34199 | 2026-08-07 04:46:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e7a04d2-614d-3553-8511-baaff6967866 | -14.44104 | -53.34188 | 2026-08-07 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 278bdeea-19c3-3118-88c6-7df1502b9fe8 | -11.63144 | -59.01121 | 2026-08-07 04:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 677ec7c8-4085-35a1-8c92-84feb9f788d3 | -15.06481 | -53.56301 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2984ead3-ead1-38e6-afdf-06a90e5ac6db | -12.00537 | -49.28498 | 2026-08-07 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcc8e2d1-c3f3-344b-98d6-95f8b1ec1da1 | -13.41829 | -57.02929 | 2026-08-07 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69db9cd8-a753-3eee-96b5-c6263277d408 | -14.15088 | -53.9997 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a42fe9e-2117-331e-9e63-d6742f1c7887 | -11.08827 | -47.80262 | 2026-08-07 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4829a90f-da54-3d65-a511-259b63c93c9d | -16.16604 | -47.99217 | 2026-08-07 04:46:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ebc0159-cfbb-35aa-a683-301c234c0c0f | -13.42852 | -57.02626 | 2026-08-07 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fb7805c-7697-3cc8-8104-9747109a852e | -14.48236 | -47.98158 | 2026-08-07 04:46:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cea03fd9-a041-31fc-9c11-8b2480c8175e | -12.00033 | -45.1306 | 2026-08-07 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 624d11a8-fce0-3380-a2fe-1f54ce520b1d | -10.86056 | -50.34415 | 2026-08-07 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6ba80e1-0b49-37dd-9987-1a5737dfed03 | -14.41905 | -45.67066 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af57aaed-5bff-3f25-b83b-684ffd2ef93d | -13.42112 | -57.04014 | 2026-08-07 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9626a2a-75c2-36f4-a7da-c9103838f388 | -11.1296 | -54.90745 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be0e3f07-d6e1-3019-8c11-d0b07df0ef76 | -12.62563 | -46.89188 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb9e8653-6009-343c-a8b1-919b070d3cab | -14.2694 | -45.2934 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 566ad169-6daf-374e-9d4c-4a43fdfe2d47 | -14.42425 | -45.66161 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ee8093c-3471-364c-ad29-32c66ca4de8c | -14.30476 | -54.73778 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 788b33be-92e1-3a0f-ba4d-00de21c999a8 | -11.13879 | -54.88062 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 680b0ae9-28e1-363b-94ff-59aa88ce40be | -11.0849 | -47.8021 | 2026-08-07 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 127787c9-2adf-3aaa-b000-4deb142adb62 | -21.87288 | -41.62064 | 2026-08-07 04:49:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9cd4356f-2755-3573-a79a-04aba9ca28e2 | -22.45872 | -43.13168 | 2026-08-07 04:49:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 945f1db5-dbee-3fcb-aa67-4d6d487c9f18 | -19.99856 | -43.97154 | 2026-08-07 04:49:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 5fc1688f-94d7-3b0a-9440-9e826e1495d0 | -20.0031 | -43.97264 | 2026-08-07 04:49:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2d9386b6-6a9f-3f54-8564-c1f606ee1362 | -21.60418 | -42.99864 | 2026-08-07 04:49:00 | NPP-375D | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 78d8ef62-84cd-339e-bafb-40ee0baa724c | -19.79958 | -46.38109 | 2026-08-07 04:49:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb912a59-300c-3419-aec6-976f3f86f0a7 | -19.71033 | -48.13317 | 2026-08-07 04:49:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 83335892-374a-378d-a43d-597d02f88416 | -23.54922 | -47.17883 | 2026-08-07 04:49:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2b9c9c4e-a53a-3ba6-b145-24b9a3c2d323 | -19.71747 | -48.13437 | 2026-08-07 04:49:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46e28315-3267-3a75-8c63-2d9bb9ca9f3a | -18.95589 | -50.62868 | 2026-08-07 04:49:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b9df4df-ff18-315c-a29d-41e88f4634d5 | -20.39032 | -49.30991 | 2026-08-07 04:49:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b76168e5-a18b-3a84-92b5-c682301d17e4 | -22.87907 | -43.01041 | 2026-08-07 04:49:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c4eb2a0b-37c4-3da0-ba6f-f0a3d5cec711 | -22.53076 | -43.5606 | 2026-08-07 04:49:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| cc7687af-0420-3298-9430-6b67d0f78407 | -22.92388 | -48.69915 | 2026-08-07 04:49:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d86d6c71-3c1d-330f-98be-06047f86bd2b | -22.53129 | -43.5555 | 2026-08-07 04:49:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2efe996d-f059-3f44-94b7-9bc211100a00 | -22.88416 | -43.011 | 2026-08-07 04:49:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d3f8b92f-6e09-3da8-932c-b684f3a30b89 | -19.99734 | -43.9725 | 2026-08-07 04:49:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ef7ae7c9-8867-3371-9f4c-6a094b7057de | -17.47658 | -53.32265 | 2026-08-07 04:49:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db3f46a6-6d31-398c-b2d9-0a0951ea4aee | -22.4542 | -43.13602 | 2026-08-07 04:49:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8823776f-e5a2-3ced-9311-fce80263fe73 | -20.583 | -42.21109 | 2026-08-07 04:49:00 | NPP-375D | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b874c289-6a80-3bc1-9bc7-07ba4e7c4818 | -20.56656 | -54.57343 | 2026-08-07 04:49:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81339d30-a58c-342a-8a9b-17abff3347da | -19.84586 | -49.0645 | 2026-08-07 04:49:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27fb9c05-fe8a-3096-ad8d-68935d8fb425 | -19.70676 | -48.13253 | 2026-08-07 04:49:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d33c4fa0-fc7a-35a4-9745-04a65e0524cc | -23.54199 | -46.94813 | 2026-08-07 04:49:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 87410c5c-ed72-32f3-a8da-5be7f0321d0f | -19.7139 | -48.13378 | 2026-08-07 04:49:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5fc6642a-de98-319f-ab71-2c6a5101bf2b | -22.89487 | -43.4532 | 2026-08-07 04:49:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| b0c037ce-dcc7-3212-b1de-6b425606259f | -22.91421 | -43.31702 | 2026-08-07 04:49:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3209310a-589e-3f71-be59-a2c538cd4d8e | -21.60516 | -42.99714 | 2026-08-07 04:49:00 | NPP-375D | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bc60de41-caa1-3ada-96c2-5251fca93b50 | -21.87252 | -41.62443 | 2026-08-07 04:49:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6490b01d-a5a0-3ed4-b75f-db065486cd10 | -22.45323 | -43.13567 | 2026-08-07 04:49:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 187c185b-cf95-373a-bd30-8e2ebf02b41a | -21.60019 | -42.99617 | 2026-08-07 04:49:00 | NPP-375D | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 67210864-da93-3175-93fb-ee3116efbd33 | -17.48009 | -53.32336 | 2026-08-07 04:49:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4be7c8ec-5702-395c-86ef-c943285f521d | -17.4836 | -53.32411 | 2026-08-07 04:49:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5337873-3e52-3561-84e0-c16da43b2767 | -20.21234 | -45.62391 | 2026-08-07 04:49:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca2111d8-9284-3018-ab77-996e183738b6 | -23.31346 | -46.19398 | 2026-08-07 04:49:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4700236d-a861-3863-b4d2-8d6959772ffc | -20.70051 | -44.14581 | 2026-08-07 04:49:00 | NPP-375D | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1f269fbd-ebc8-3899-a6d8-f7c1e5e0f352 | -20.00188 | -43.97363 | 2026-08-07 04:49:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a6776493-e8dd-3461-ae8c-236ba1855da7 | -17.47306 | -53.32196 | 2026-08-07 04:49:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06ccb005-192d-38d4-81eb-356ee2cbb237 | -20.80625 | -49.41938 | 2026-08-07 04:49:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 071acb8c-88f3-3977-9597-f161ae32e89b | -22.52589 | -43.55981 | 2026-08-07 04:49:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9bb8aa56-e5ea-3c02-afd2-dbd43380c311 | -22.53609 | -43.55706 | 2026-08-07 04:49:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ac2cf4b8-e9c8-31bb-8e53-0cad40d1836f | -20.58335 | -42.20781 | 2026-08-07 04:49:00 | NPP-375D | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9b58d129-e904-3375-b701-fbd0f4da11c1 | -11.1443 | -44.4865 | 2026-08-07 04:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| deb72189-467f-313e-998c-2b8383738ac6 | -4.91358 | -49.23434 | 2026-08-07 05:01:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80df1974-0d2f-3a57-869c-296038014055 | -5.37133 | -49.17466 | 2026-08-07 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b9abd3f-71fb-35bb-8316-e831b4c3c7ae | -2.48384 | -49.32812 | 2026-08-07 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c32a78ab-2743-3d80-8bd2-4e62566a4c23 | 2.52107 | -60.64513 | 2026-08-07 05:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75a23f8b-cbd7-36c7-8dfb-23270a71da4d | -4.36952 | -47.76863 | 2026-08-07 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README19.md)
