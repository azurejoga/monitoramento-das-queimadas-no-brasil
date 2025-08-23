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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daa19df1-0162-3abe-84fd-a72b36857764 | -8.67672 | -62.87844 | 2025-08-23 05:21:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 011281e2-e2b7-39c2-aa7b-0b2478408571 | -11.61936 | -50.42784 | 2025-08-23 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa32dae0-badb-334e-8a09-282640d888a9 | -14.66067 | -54.85733 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 233592a3-c33f-383e-862a-bcdc3692b1fb | -14.38008 | -52.05612 | 2025-08-23 05:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58904fae-0771-33bd-9e90-fb38b0f09217 | -6.93888 | -59.64151 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 446e196f-b442-3fe4-98a0-cdcee4e41989 | -8.67745 | -62.87406 | 2025-08-23 05:21:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d105295c-af80-326b-b3bd-8fd04df06666 | -7.62503 | -63.48873 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e55ff299-1887-3788-b108-13bfb42452b1 | -12.78747 | -48.71942 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6173823-ff65-3a26-8214-1093130bda01 | -9.44616 | -47.65346 | 2025-08-23 05:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| eca665a0-bf9b-33d3-ab80-d8df3eddc82d | -7.78639 | -61.57728 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92fe51d4-ad12-3d9f-b8e6-050bff9fd74d | -8.85162 | -49.86436 | 2025-08-23 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86ff2b19-1aec-34cb-8286-fc23037af990 | -13.33876 | -54.39431 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e08891cd-e306-32bd-a038-6c20fc20cb10 | -11.18575 | -55.02443 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39afa848-1eb8-3a78-8864-3a8cd253f484 | -7.78224 | -61.58062 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e683826-624a-3169-9394-9026a84db1ef | -13.1398 | -46.91606 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 447a4e84-df2e-3c02-931b-b53bab764ee0 | -11.09334 | -58.94274 | 2025-08-23 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7428a41b-ba9e-3627-ba08-32f0b934a1f1 | -8.88964 | -62.42671 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce2a1a09-58fc-374e-932f-3b818cd7c37a | -13.0372 | -46.32561 | 2025-08-23 05:21:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| affbf3ce-60f4-39e1-85c0-b5217962580c | -9.95221 | -60.17957 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8b672604-6b6f-3d16-8591-cc8908079aab | -8.66035 | -51.27349 | 2025-08-23 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecdca771-5f15-324a-a350-f448dc5b449f | -9.21451 | -59.62916 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83d13ca8-3eb2-3d05-8371-ceae97c4324f | -15.54798 | -51.70456 | 2025-08-23 05:21:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c58128d-d076-3cea-ac8e-17f6b2101ba2 | -15.54872 | -51.6981 | 2025-08-23 05:21:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df963372-ef5b-39af-ac52-92474d9261a3 | -13.42846 | -60.94027 | 2025-08-23 05:21:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ccf792d-55a4-3905-afcb-eff9714d28e3 | -9.17295 | -59.59024 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91d33dc9-dd47-3812-9800-65fc8d77b617 | -14.69272 | -54.90508 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 490f58a7-7ed3-35b4-8bbc-73d20f15dece | -6.89795 | -59.89854 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8485b722-ab2e-381d-aa53-895ead1b4889 | -13.36395 | -54.40232 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7f71351-ae1f-3b70-9ba3-d534ddaf60ae | -9.18792 | -59.64634 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25363eae-6d49-39be-94f7-e68af15ddd52 | -9.20667 | -59.46313 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f569029-30c1-33e1-b151-442ad0c1e2be | -14.30273 | -58.55216 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b041c3f8-d4c4-3374-a8f0-8680cc04f38e | -8.90043 | -62.42852 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df864c47-965e-3ead-84fa-4ed23496a924 | -9.20334 | -59.44111 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d562fcc-7ce5-3085-a959-0426b6c5da2f | -10.4659 | -59.13541 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17a153d3-d280-31c8-8b02-147e5fbacdde | -11.61893 | -50.43143 | 2025-08-23 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bece9cc2-8ba2-31e5-973e-c59b74acd5cc | -9.18127 | -59.62382 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 427634a5-53bd-32db-8e94-f3a11d0a51a6 | -14.28142 | -58.55282 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d4aad69-0687-3043-8f31-e8f8a72cc82a | -8.69959 | -62.87783 | 2025-08-23 05:21:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2fbecfcb-d92f-3d57-817d-088c2319f6d1 | -9.94222 | -60.17795 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ab93cfe-e6af-3bf1-9207-7303c3f43c32 | -7.29665 | -59.6269 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99a2f623-cafb-363d-a005-1663f689d7ea | -13.16594 | -46.91854 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ca76a89-ca89-3687-aafe-72965fa08c67 | -9.19012 | -59.58942 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c82e0399-918f-33a3-900d-b55424030851 | -9.14951 | -59.50785 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5a1b6bfd-334d-31bc-be53-779e1e328878 | -9.18571 | -59.70334 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 207ccc91-c06d-3a61-b67a-e3a83d5282dd | -13.38631 | -46.34521 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38b20187-5cc7-37d0-8514-abc9f5c9dde0 | -10.74542 | -48.25152 | 2025-08-23 05:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94c4b098-b949-3806-af85-6b6db1cc0bdd | -11.19953 | -55.04241 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73163e21-f48e-3580-a5b1-7f290cd1c188 | -9.20731 | -59.63158 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc36d4a2-b93e-351d-9951-5b51995c1938 | -9.526 | -60.52127 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20a4ec5a-1414-3ff8-8fc9-0289012b2495 | -10.46311 | -59.13138 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7568b02d-03f3-318a-8710-62cc1e68c06d | -9.95663 | -60.19473 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 75cbd9a2-36cd-31cc-9105-a9c4c6b6646f | -14.76687 | -56.03161 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bb871c4-b305-3add-a3c5-92135bb5b047 | -9.19568 | -59.64042 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79306cb5-80f3-3cf5-a0e1-8b8bdefdfb5a | -9.52258 | -60.54268 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfca09d2-44ad-3a4e-8034-bc10f4b9547b | -9.52044 | -60.51305 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ad2dcdb-846f-3d6d-b2f6-708a7139dfc4 | -14.32346 | -58.55537 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31fd1a75-a6c3-3e81-92e7-99fae292b1ae | -7.05081 | -59.82536 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c647f00-78a2-3669-b04d-513b2f2eda18 | -14.87918 | -47.95829 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab76b1b6-f9ed-3a70-a526-1f33cc35dea8 | -13.02426 | -56.82833 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 95f786fa-39ef-363d-8c59-ea78cdb96d5d | -12.1566 | -60.76763 | 2025-08-23 05:21:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df26c952-272e-3d72-b41f-43d51f3254df | -7.36293 | -57.63147 | 2025-08-23 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44884bc6-b114-3dba-a5c3-a0ab2c8e4fec | -14.66331 | -54.86988 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb7d31cc-6887-34a9-b367-1aeef78fab50 | -9.21276 | -59.4462 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13a253e6-9e5d-37f7-881c-ac704445d518 | -6.88511 | -59.89287 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 195e803c-5479-34a4-a4aa-dd5d83df21dc | -9.20001 | -59.44057 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e71b3b4e-0dfc-3161-b184-f1e6e689d1ec | -13.3759 | -46.21305 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 917214e6-3bc4-3450-9285-fe55bff13f2e | -14.27796 | -58.55229 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b52855c-6517-3b29-8d7f-69af29c0a8b6 | -9.21425 | -60.7915 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 170d682a-3251-35c6-a736-ee99fdd639f7 | -14.82197 | -47.95243 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0fc76e46-6db6-3d6c-ba4e-2c51ec542abe | -8.85254 | -49.85727 | 2025-08-23 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d3d7869-da69-3635-b1cb-4545442f0d5b | -10.74831 | -48.25117 | 2025-08-23 05:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6d20631-bb91-36e9-8814-b18e76585131 | -12.98527 | -56.90104 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af5ed536-9a8b-32cb-b7d6-04edd42f5e67 | -13.02858 | -56.82444 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f92afa06-9e06-328b-93ab-d428cca94a17 | -9.08505 | -61.43338 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c81c1ff2-9005-3c03-84f6-9ee3d393bc77 | -15.03663 | -54.8946 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d361073e-45b1-3717-9ec1-ad358a7cfe61 | -7.94948 | -63.04301 | 2025-08-23 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e76c3a4-23ee-309e-874b-b8bdcf5b2ad8 | -8.53412 | -48.8637 | 2025-08-23 05:21:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f70a5999-b234-38bd-8fd6-9ca54488fff8 | -9.19844 | -59.623 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 548f33c7-cc88-38df-9dab-8d2b1accba11 | -11.19626 | -55.03668 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b20e9725-ec5a-3abb-b0fc-f252f4b78008 | -9.19836 | -59.45105 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 972cf7fc-094b-367f-9764-b48b0c394cac | -13.41692 | -46.2604 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 051b0a94-7690-3513-acf5-ed7179eef5eb | -9.56332 | -68.57674 | 2025-08-23 05:21:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66e5a251-822f-34a3-94e0-2f7793d53435 | -14.76523 | -55.98392 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bd09a92-18ef-34d4-b83e-ff9ea369af6c | -9.65046 | -59.65266 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dee70ff0-44a2-3946-9f31-49c58966965d | -9.50589 | -60.51798 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f2420a7-e292-36ab-94a9-a34ed41cd724 | -14.68022 | -56.61043 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ecef4f0-8456-3883-83f9-eec1ece8bf93 | -9.47529 | -60.32345 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 731d3763-6bd0-3195-ae63-e958b48f0d9d | -9.16798 | -59.70766 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe26ca3b-2a67-3faa-bde1-a82350fb5d42 | -9.18515 | -59.64233 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08843efa-7141-3218-86b1-15ec91828ce3 | -8.86495 | -62.39697 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23e5f127-8b35-3a12-93bf-bef62284b0ff | -9.22727 | -59.69926 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27af2f56-8421-3d4f-8608-e6942e30513e | -14.87863 | -47.96367 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0528a7db-abda-3541-9bae-cb78997e8927 | -15.01768 | -54.87324 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c9877e2-8d7a-38d6-8e77-cadaec44abea | -13.0267 | -56.83774 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3bb7c1e-5dbf-3be5-bc5b-4f14fdc10e7e | -7.58583 | -63.43712 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8e586be-3c5f-3914-b2e2-dc8a17d7d3a4 | -10.34547 | -58.60584 | 2025-08-23 05:21:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48392f09-73da-3bdf-bf86-74108839e66a | -14.67199 | -56.59301 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efbc2a3b-80da-33fb-89b2-fb93b91ea662 | -14.2871 | -60.38797 | 2025-08-23 05:21:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49bb1ebc-0fe0-3ead-821c-cd78693e61c6 | -11.32495 | -55.21701 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43a73717-4fd6-3f3f-b456-39b44668eba3 | -9.19393 | -59.45751 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README72.md)
