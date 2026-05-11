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
| 9274c25a-acb9-3671-8a1b-10f031de4f56 | -14.14897 | -45.43019 | 2026-05-11 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8961f18d-c221-3394-a2cd-38ec95a0d6b9 | -11.06146 | -46.52309 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfefb1e9-6f2f-3447-a205-4781ec7f31a5 | -11.61713 | -54.17396 | 2026-05-11 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 298088c9-dd98-3c8a-b60b-4d1233fa2bc8 | -12.79419 | -46.9809 | 2026-05-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15d1f8a3-d9e0-31ea-801d-0d1d270e32ed | -10.55021 | -56.32489 | 2026-05-11 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8c39feb-92a3-3f99-abbf-20e31e0d797c | -11.04309 | -46.52295 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c241c073-15b4-3f0d-87a9-787a5ad83bd4 | -14.15059 | -45.42775 | 2026-05-11 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fcfa582-3bea-3914-9970-55d9e6d6d26d | -11.27919 | -55.30877 | 2026-05-11 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1fc5776-0d52-3686-b56c-c9988044d536 | -11.05489 | -46.53403 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 346cefab-3d64-350a-94e5-11ad23b3d115 | -11.03798 | -46.52217 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3cebd041-520e-35a7-afd3-7dd540bc0b9b | -11.03872 | -46.51648 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7316722e-eae6-3d47-be7b-33c8e60bd506 | -14.13938 | -47.3936 | 2026-05-11 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55c18821-d2c6-33e3-9ec4-4f648074e1de | -11.06075 | -46.52875 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48670f80-42f1-3ff0-936c-20de7c298acf | -12.79355 | -46.98602 | 2026-05-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0718af52-05f3-3f88-a25b-91711323ea7a | -14.13854 | -47.3949 | 2026-05-11 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9affee1-382c-3ff8-9386-dd778d12afc9 | -11.04382 | -46.51736 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d0ff30f-0e9f-339a-8b95-7d5fc2d8f98f | -12.83025 | -49.79705 | 2026-05-11 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c989bcf4-a9d7-3e12-b77d-a600e1ce9ae9 | -11.03836 | -46.51926 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f5cc0af-47cf-3043-a624-179fee921da6 | -11.04068 | -46.5225 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1981014e-ec7f-3845-b2e5-e50b8750bbdf | -10.55634 | -56.32959 | 2026-05-11 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 692cc7a6-1f61-31f8-a838-241f12a391c3 | -14.14528 | -45.42295 | 2026-05-11 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a80309d-7b32-3742-a324-b5d2c4c1768e | -11.03556 | -46.52174 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0b72725-32e7-3435-8495-03b08ab3d147 | -11.47742 | -52.92156 | 2026-05-11 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d104a06c-8668-3516-af99-b6634759c5ab | -14.15678 | -45.4243 | 2026-05-11 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7e15857-bbde-3bcb-8f52-9fb4d02c9aa2 | -10.54627 | -56.32797 | 2026-05-11 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c602956b-80f2-34df-aa95-52e9e75c9624 | -11.05016 | -46.53016 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 201f0497-1ab7-3795-88af-8269b5de9d7d | -11.04269 | -46.52598 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de17d6b9-4358-3043-bc07-cec1fdb43908 | -10.55356 | -56.32544 | 2026-05-11 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1173ee24-0378-362e-b901-13377b91a892 | -11.03628 | -46.51595 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a67df7c4-5602-3829-99a3-7b8883be8bfd | -14.13433 | -47.39306 | 2026-05-11 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90699f99-61e8-3a7a-bad5-16c1385c4d6f | -11.04978 | -46.53325 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19b590aa-27b5-3c94-9bf9-0c49eec6b35f | -14.13891 | -47.3917 | 2026-05-11 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd40cefc-9587-36a7-a144-d109c4465656 | -20.82397 | -45.53345 | 2026-05-11 05:01:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbafd757-bee2-354a-bd6d-697ec2efd27d | -20.82386 | -45.53644 | 2026-05-11 05:01:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12df645f-b42a-3880-937e-fef6f96d2509 | -16.10662 | -49.23139 | 2026-05-11 05:01:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e43fb18-daf8-3e07-824b-a99e9e52d1fe | -18.34731 | -43.30531 | 2026-05-11 05:01:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| db459604-0501-330b-89ba-ef18a854ff4e | -20.82429 | -45.53164 | 2026-05-11 05:01:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5540ecf-8b1e-3cc5-9262-68b518b46762 | -16.98981 | -46.54177 | 2026-05-11 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5294b10-e6c8-32e8-b983-7aabcb46aa7d | -23.70115 | -46.4584 | 2026-05-11 05:04:00 | NOAA-21 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 6a13d9a8-228e-3444-a0a1-f85dcbd20769 | -23.70075 | -46.46315 | 2026-05-11 05:04:00 | NOAA-21 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 83334e7e-e8c9-3da7-b4ff-3c1b96c82371 | -23.70361 | -46.46108 | 2026-05-11 05:04:00 | NOAA-21 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| c27b4604-2c68-388a-9f1f-b8f1dd2cfed2 | -31.63298 | -52.37064 | 2026-05-11 05:06:00 | NOAA-21 | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| a5529003-6fc7-3787-9a35-85bbbe6e99ec | -10.54764 | -56.32818 | 2026-05-11 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4202caa2-b523-3253-9d5e-0a965275c996 | -10.54298 | -56.33126 | 2026-05-11 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1a03873-17e8-3024-88a6-3bfec1bb69b4 | -10.5471 | -56.33189 | 2026-05-11 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b646107-8952-3c0b-9605-2305a3c17f5e | -10.54505 | -56.33052 | 2026-05-11 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83715311-6473-3548-bfb3-ef2b6efdc15d | -10.54968 | -56.32744 | 2026-05-11 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 31e646ca-2874-3adb-9e77-5dacb68cd85d | -2.97483 | -60.10276 | 2026-05-11 05:31:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bcd6293-751b-3a1f-86a2-5df5e4fb5c71 | -10.55381 | -56.32807 | 2026-05-11 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6a3f5860-5e9a-3b74-91c1-1f77d440aa51 | -2.97151 | -60.10224 | 2026-05-11 05:31:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c557751d-e1cf-3790-a145-6b4fb8b6d8d7 | -2.97422 | -60.10489 | 2026-05-11 05:50:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08986387-7dd0-33dc-a53e-303a2ed15b47 | -10.5462 | -56.32943 | 2026-05-11 05:53:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e744ffd-58d2-3596-ac86-883f61cd5899 | -10.55235 | -56.33033 | 2026-05-11 05:53:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ede82e07-0537-3d12-b874-3d2278442c6e | -10.55293 | -56.3256 | 2026-05-11 05:53:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0477915e-9404-336e-902a-66bbc40e1219 | -11.03822 | -46.51544 | 2026-05-11 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fac99f17-e399-32a7-9ef4-cba962db715f | -11.05479 | -46.52778 | 2026-05-11 06:16:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2d167416-52cd-3962-aadc-b33ff499d157 | -20.82174 | -45.53481 | 2026-05-11 06:18:00 | AQUA_M-M | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| cb9ab9a5-0604-3390-b02d-b8a77655dd50 | -20.82316 | -45.52482 | 2026-05-11 06:18:00 | AQUA_M-M | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 228f46c7-9ece-36b5-b554-3b6d495d1bc7 | -14.1682 | -45.4208 | 2026-05-11 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| ae46116c-1e84-3dc5-9746-0199747f5b7b | -11.88119 | -42.58699 | 2026-05-11 11:19:00 | TERRA_M-M | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 8ded689c-0f6c-3648-92b6-72e2991a9570 | -14.21967 | -43.47632 | 2026-05-11 11:19:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fb4df3a4-d22d-3488-bffe-b302cc5b3265 | -11.04383 | -46.53002 | 2026-05-11 11:19:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| c0a2e218-5efb-34fa-8ad5-3257ab9f96e9 | -14.1682 | -45.4208 | 2026-05-11 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 9061e041-7868-3c20-8a96-31d8b400c4ab | -18.88339 | -40.43753 | 2026-05-11 11:21:00 | TERRA_M-M | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 14b0b6ba-f98d-30bc-871c-284c418cc91a | -19.67533 | -41.51074 | 2026-05-11 11:21:00 | TERRA_M-M | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| eda77390-3bb0-3224-a4c7-a9286fa2b83f | -18.88474 | -40.42822 | 2026-05-11 11:21:00 | TERRA_M-M | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 9ee1049e-3cf1-3916-8e03-7893271b4d6d | -14.1682 | -45.4208 | 2026-05-11 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b6bb8cc0-72b3-3694-9880-d5ace58444ff | -14.1682 | -45.4208 | 2026-05-11 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 82b51748-4e0a-3fe7-a23f-1fac68b9d9c5 | -14.1487 | -45.4242 | 2026-05-11 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 4f4bd92f-f148-36dd-8d13-9df706adcb1f | -14.1487 | -45.4242 | 2026-05-11 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 82968f60-8140-3200-8e8f-9800ea5b6418 | -14.1682 | -45.4208 | 2026-05-11 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| dff179b3-dc56-39b3-9cd2-7976990f5907 | -14.1682 | -45.4208 | 2026-05-11 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| b65b63a6-9cb2-39ff-94b3-53582daa1f0b | -14.1487 | -45.4242 | 2026-05-11 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 96432647-62ea-3bd2-86a7-4720c7a04b6f | -14.1682 | -45.4208 | 2026-05-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| caa75edd-7918-367a-a479-b98e20ed0f51 | -14.1487 | -45.4242 | 2026-05-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 06806fa4-4b12-3fe2-83a1-864d1fb8d18d | -14.1682 | -45.4208 | 2026-05-11 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| a85ba1ef-d513-330c-b2b1-66ecd89edaad | -14.1682 | -45.4208 | 2026-05-11 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 735089b8-fad0-387f-99d5-6e48edd2791e | -14.1682 | -45.4208 | 2026-05-11 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| d86e2b6b-aee3-3c1b-815a-3279da1704a4 | -14.1487 | -45.4242 | 2026-05-11 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 60a335d7-fc55-3f17-bf7c-839bf7bf1147 | -14.1682 | -45.4208 | 2026-05-11 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 0d12629c-066c-3b3a-88d8-9a0991a5db3f | -10.68626 | -52.61853 | 2026-05-11 12:57:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| de8c4f33-1a6c-340a-812e-8621b60dc68c | -11.06159 | -52.47634 | 2026-05-11 12:59:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ef62b3f8-78cc-33cb-b5b3-22a9d1e681dd | -14.12552 | -58.22097 | 2026-05-11 12:59:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 536f7de2-ce57-39de-8feb-670d446e02f3 | -12.65845 | -55.18768 | 2026-05-11 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 5b796d6c-81db-3149-bd5e-2d5f8ef6a0cf | -14.12754 | -58.20428 | 2026-05-11 12:59:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 4dca68e5-c6d4-372b-b162-9dcfaf2080f1 | -11.75032 | -54.79176 | 2026-05-11 12:59:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 2fc2b27c-7b29-33a4-b17c-09028c7a5fc4 | -14.1682 | -45.4208 | 2026-05-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 87f4f7bb-4ccd-3ff4-a0a4-93c7c3cd2a43 | -14.1682 | -45.4208 | 2026-05-11 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 5304c737-3d82-395d-8155-178a61d153ba | -14.1682 | -45.4208 | 2026-05-11 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| d24c8a2f-6fc1-30ed-8fc4-3f4c5fc9ab7d | -14.1487 | -45.4242 | 2026-05-11 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 24337c62-ef10-3326-b3b3-2262646daa69 | -14.1492 | -45.4009 | 2026-05-11 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f12a5be7-b30c-3de1-8e75-05c7a29567e9 | -14.1492 | -45.4009 | 2026-05-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ed352ef6-4c9b-30c1-9ea9-b9d917ada88f | -14.1487 | -45.4242 | 2026-05-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| d385f52a-96c6-331b-870b-cd1cf9dc8153 | -9.6449 | -42.9559 | 2026-05-11 13:30:00 | GOES-19 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 97.0 |
| ea4ef492-ad29-3f95-bfab-a4dea5ec0eaa | -14.1682 | -45.4208 | 2026-05-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 2b6558bb-f3b4-3c60-8225-0e0b27be365e | -14.1682 | -45.4208 | 2026-05-11 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 22f9c028-d6b6-3780-b74a-db022e41d077 | -14.1492 | -45.4009 | 2026-05-11 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 453597b4-b2b8-3228-9558-d08cbae2631f | -9.6449 | -42.9559 | 2026-05-11 13:40:00 | GOES-19 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 935cb935-63b0-3149-9dbf-53a45d7f2fd8 | -14.1487 | -45.4242 | 2026-05-11 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 35f7eea4-6ed1-3224-8b18-caf36b8925e3 | -14.1492 | -45.4009 | 2026-05-11 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |


[Clique aqui para ver as próximas entradas](README4.md)
