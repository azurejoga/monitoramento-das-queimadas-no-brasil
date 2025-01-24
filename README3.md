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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5a7efe6-ea3b-38b1-969a-55167c42f971 | -12.75302 | -44.84146 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b34178f4-5324-321c-882b-7184278ade17 | -17.0379 | -50.21013 | 2025-01-24 04:10:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c86f431-8446-373e-a709-0d1504e159ac | -16.42953 | -41.26302 | 2025-01-24 04:10:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1043c462-e0ae-3d9e-bf18-569f137d699a | -16.34992 | -43.69622 | 2025-01-24 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37ec3347-23d8-3f66-a14a-e2eb1ffd557e | -17.67728 | -42.31246 | 2025-01-24 04:10:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5dc9e2a-c7e0-3f18-b245-27feb5627ff3 | -17.68179 | -42.30536 | 2025-01-24 04:10:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f267925-270b-36e9-bf52-700e1f904fdc | -13.47707 | -44.02173 | 2025-01-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5875b8d6-31eb-30d7-b11e-fed452490e93 | -12.76385 | -44.83941 | 2025-01-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1963ffb2-3d5d-37d0-8d18-5f2430b3bc55 | -18.46951 | -51.05532 | 2025-01-24 04:10:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5ccdc32-1fca-3adb-b3f5-3552a41e688e | -17.71665 | -40.14602 | 2025-01-24 04:10:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0d9ec096-dbb1-3b1f-915e-346ab7dabfd8 | -21.18033 | -43.98081 | 2025-01-24 04:12:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c349f102-a621-3dab-aab4-a9b737ad96a7 | -20.88082 | -41.92628 | 2025-01-24 04:12:00 | NOAA-21 | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 36d3010e-8b09-3e6c-a998-8f97d7101b36 | -23.40648 | -46.55632 | 2025-01-24 04:12:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| db759075-028a-3183-a3b6-2b09ee9916ab | -23.33776 | -46.77279 | 2025-01-24 04:12:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e9cf2ef3-ca65-31c9-a813-3050c264a1b1 | -23.63211 | -46.42605 | 2025-01-24 04:12:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0d808788-5547-3d07-841b-236c0555a663 | -22.69784 | -43.34809 | 2025-01-24 04:12:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8bff5067-ffb9-37f1-9ede-3f3418443955 | -20.76302 | -46.77057 | 2025-01-24 04:12:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73db845a-2a86-3e79-9581-c2fe43ff9fae | -9.259 | -60.309 | 2025-01-24 04:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e9b14ff9-398b-3889-b062-e3e61e47cd45 | -9.259 | -60.309 | 2025-01-24 04:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 1d67927f-c647-3c2f-a660-43067f8bc6ac | 0.88588 | -60.151 | 2025-01-24 04:31:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 42485636-d407-3f15-b2c5-6563ea056fc0 | 0.8798 | -60.15921 | 2025-01-24 04:31:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 605d2fe9-bfa3-3dab-8ad9-13741f3538d7 | 0.88428 | -60.15837 | 2025-01-24 04:31:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aa4212dc-b1b0-3e17-bfda-0dca03f3f550 | 0.87869 | -60.15199 | 2025-01-24 04:31:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 18e42930-32f3-3c0e-9413-f507bea70f49 | -1.57671 | -46.68063 | 2025-01-24 04:31:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48dca3d5-b9cb-3d23-ba57-4cc032c32a32 | 0.88697 | -60.15808 | 2025-01-24 04:31:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 037b7367-2e41-3e75-b6d8-fe6469e13b05 | 0.88314 | -60.15126 | 2025-01-24 04:31:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 30cf70af-419c-397a-bf88-3761bc212ada | -6.6389 | -47.35281 | 2025-01-24 04:33:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae78ca4e-5d93-361c-9f87-5eb2abdfd908 | -11.65223 | -58.20673 | 2025-01-24 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d21ecd6-3db9-30a8-bd42-b17945870bf6 | -11.65285 | -58.20354 | 2025-01-24 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05ef0f68-2255-3b89-95bd-a83cb4c83624 | -10.34864 | -47.90784 | 2025-01-24 04:33:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c218a170-9253-3f05-9d10-632b5aa22671 | -11.02513 | -45.0528 | 2025-01-24 04:33:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80e87a40-3799-35cc-923d-d4510cec5ae8 | -11.38967 | -55.12237 | 2025-01-24 04:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58963865-07eb-399d-8ea9-b0062a8f6adf | -10.34919 | -47.90428 | 2025-01-24 04:33:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21e85ef8-1273-37d2-8d67-0fdd6057c884 | -10.34975 | -47.9007 | 2025-01-24 04:33:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7059af5c-57b4-36fc-adbf-f82680296bfa | -12.76674 | -44.83161 | 2025-01-24 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64ff8db7-e248-3d6d-86d6-fa12036091b2 | -7.86263 | -43.08561 | 2025-01-24 04:33:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 763fa0c9-54c5-3c8e-8e6e-2ba05485b652 | -12.74681 | -44.83653 | 2025-01-24 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36547090-31e2-30f9-83e7-63f7d196c43f | -12.74287 | -44.83594 | 2025-01-24 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2490815-6c3f-37b7-ba5e-cfc8da49db5c | -9.99819 | -47.60722 | 2025-01-24 04:33:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee90ca2d-083e-39c5-ad5d-aa3e3f39f5b6 | -6.64224 | -47.35333 | 2025-01-24 04:33:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70168505-c8cd-35e4-bf4f-35aeb3e8aef3 | -12.7628 | -44.83103 | 2025-01-24 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 530ebe77-fc81-3182-a972-21bdce880850 | -11.6489 | -58.1956 | 2025-01-24 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bff682b-a1c2-31f3-9467-96c98d5af25e | -11.02444 | -45.05747 | 2025-01-24 04:33:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e483efb9-c324-3849-831a-418ca7c0304f | -11.64888 | -58.19611 | 2025-01-24 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13d66edd-c95c-3bb3-b3f3-6c24d1fe80b3 | -9.26221 | -60.31363 | 2025-01-24 04:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9512ed4e-a090-30bc-9792-de56b06f908f | -11.6535 | -58.19988 | 2025-01-24 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ff765bf-9b7a-340b-af0c-68b0e27b2321 | -11.27626 | -44.44984 | 2025-01-24 04:33:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 915e9785-d43e-3f71-87a0-6680df4bd27b | -11.65346 | -58.20038 | 2025-01-24 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78ebbf2c-dd36-33cc-8d0f-499b1d1aafe6 | -13.47464 | -44.0216 | 2025-01-24 04:33:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 508416d5-c4e5-33b7-9aa2-f1ef0f579312 | -12.77437 | -44.84062 | 2025-01-24 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 426c5348-462d-32c8-8c6a-89938753618f | -8.80972 | -44.70136 | 2025-01-24 04:33:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34cf993e-1506-3f9a-8a3a-bddf00483844 | -13.47517 | -44.01768 | 2025-01-24 04:33:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fa23996-650d-3595-a5c1-6200d69c91d0 | -12.74359 | -44.83088 | 2025-01-24 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d60b7d85-abc4-3a7b-a49c-7b20b96396f8 | -12.74609 | -44.84161 | 2025-01-24 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0010dc5d-38dc-301c-85f1-b8fa8c1e2ce7 | -11.65292 | -58.20306 | 2025-01-24 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd3b78ac-7b9b-3fff-8f5f-a8b678e860f4 | -11.02783 | -45.05532 | 2025-01-24 04:33:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc046d35-581f-3d5f-a4d3-be26f32ed928 | -11.02402 | -45.05479 | 2025-01-24 04:33:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f376a20f-20cf-3b62-9447-17086f97f6c9 | -9.98693 | -48.08191 | 2025-01-24 04:33:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36002a1a-95bc-3722-b259-67c42ff93c5b | -11.65232 | -58.20626 | 2025-01-24 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6755f8c0-2eb4-3744-a6b0-0ab316d204db | -8.80962 | -44.70401 | 2025-01-24 04:33:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c95c4578-d275-367b-bfbb-c6d8ad410278 | -12.76328 | -44.83381 | 2025-01-24 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2511fd1b-de43-3c09-a52d-d7bcacf7360b | -12.6316 | -49.02711 | 2025-01-24 04:33:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4fbe676-f29b-3f66-a39a-fd1655306056 | -10.31698 | -48.65357 | 2025-01-24 04:33:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29fe4e8a-355c-3e5c-8eec-2b9757f2b7f4 | -9.5168 | -47.78199 | 2025-01-24 04:33:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 32bd4b98-07c4-330c-8fdf-fe3618638669 | -11.03096 | -45.06057 | 2025-01-24 04:33:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1c9ffd9-4efe-3e77-b8d6-335c9c67ae7e | -12.76211 | -44.83613 | 2025-01-24 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd4d622d-f60e-312e-bb3e-c74d8d3de2f2 | -9.26129 | -60.31846 | 2025-01-24 04:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 242f78e6-a3b5-3aa3-b286-e672915d1119 | -12.77043 | -44.84005 | 2025-01-24 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12818bdd-8360-360c-b5ab-b4c9c1fd98eb | -9.25508 | -60.31721 | 2025-01-24 04:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6791fc3e-a8f5-3553-a00f-02e04acb80be | -11.65173 | -58.20947 | 2025-01-24 04:33:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ee13e74-ca47-3d8e-b285-54ca2de17b03 | -15.24018 | -60.22419 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d44f6821-8c99-3aa9-8192-5a958ee1a909 | -15.24312 | -60.22697 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d96d67bf-bb22-3049-99c4-a51089f05c61 | -15.23198 | -60.22475 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91fce5ad-a088-360e-ac26-c3bfe6b373ef | -15.24093 | -60.22047 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d92220a2-6b25-3297-9f7d-3778f4e5c49e | -15.24573 | -60.22537 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b279803-6db0-38c7-ab63-e29c0b4bc7c8 | -15.23943 | -60.22792 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0e4f7cef-eef9-384c-a4e8-dc4c6f4581da | -15.26986 | -51.46597 | 2025-01-24 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5197756d-8768-3a78-a6f7-3a9ce6ab7106 | -15.26925 | -51.46968 | 2025-01-24 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb86498c-1196-318c-854b-1d864e943dd7 | -16.34805 | -43.69669 | 2025-01-24 04:36:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1707249-12e3-3c71-9b3e-86fbd0e9720b | -12.94824 | -61.34324 | 2025-01-24 04:36:00 | NPP-375D | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e3cb585-915c-3126-a29b-186d52f84a6b | -17.03436 | -50.2114 | 2025-01-24 04:36:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba469b15-6ec5-3f88-8865-9f6696352fce | -15.07827 | -48.9455 | 2025-01-24 04:36:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6577cb7b-1d11-3380-bec6-1494776b1263 | -16.68085 | -43.88665 | 2025-01-24 04:36:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecaf283c-aa61-38db-af60-fe4045db1d94 | -15.23833 | -60.2221 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 792d07c8-c102-30c3-847e-4c9e46fd7ba5 | -15.27142 | -51.4777 | 2025-01-24 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f4dcb92-d5d4-3ecb-ac06-a5f5d3d35c88 | -15.27203 | -51.47398 | 2025-01-24 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b797eb4c-0adc-378c-bd0a-4e8a8f7f26cc | -15.23385 | -60.22684 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ef2cee67-abff-3e09-b738-957ef239e38b | -15.23756 | -60.22583 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ae35060-97f5-38cb-b186-6243e4464292 | -15.23118 | -60.22856 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9350bb7-d0f2-3610-989d-15ca96d9ec8c | -15.26804 | -51.47711 | 2025-01-24 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c033b4e9-0db8-3101-ae2e-65555ce9c663 | -17.67997 | -42.30536 | 2025-01-24 04:36:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d656557-acd7-38af-8e3c-c14cf529c97f | -16.68144 | -43.88186 | 2025-01-24 04:36:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa0121ef-608f-3187-a1a9-65c254206bb9 | -15.24389 | -60.22325 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ddac9047-8ffb-3679-9608-9d95206f7815 | -15.23461 | -60.22306 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 187ab228-5d3f-3f28-b4a3-de1e210d6474 | -16.35006 | -43.69492 | 2025-01-24 04:36:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e75fd1f7-2151-3bad-a052-cf881c5222e9 | -15.23677 | -60.22958 | 2025-01-24 04:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e221f8e-010e-330d-8c2e-e46b67a50be9 | -15.20359 | -51.56991 | 2025-01-24 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a89baf4-425a-3d16-b698-e4c2a89f7ed5 | -16.80489 | -42.57329 | 2025-01-24 04:36:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c78b47a6-dd83-38e2-989f-91843e4c0beb | 0.70919 | -59.33419 | 2025-01-24 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7cb529e-71eb-34ca-ad32-20fb8ce08ead | 0.88081 | -60.15688 | 2025-01-24 04:53:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README4.md)
