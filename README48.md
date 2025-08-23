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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0412d28c-9071-3b92-8f91-c0ddfd8f5d64 | -9.65339 | -59.64096 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 992d3292-f2f8-31e8-97dc-c842bd8c90d3 | -9.23579 | -60.47964 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0423e377-9eeb-3711-889c-1fae12846512 | -12.48718 | -53.81291 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75ad0869-11c4-36bd-bab3-aa6c96c47499 | -12.49932 | -53.82209 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a0b6384-fbb3-3b45-836e-d6f32de46e4b | -12.18746 | -47.20928 | 2025-08-23 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a5fc892-b9fc-31f7-8d37-115d2bc70221 | -16.48309 | -49.2324 | 2025-08-23 04:53:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4949b05-747e-3602-8c88-aa54203c81e0 | -14.61623 | -54.85672 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63f38774-bbf0-32c4-973f-0facea230407 | -14.33877 | -58.58822 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb92ebc3-5254-31cd-b796-8023d674a5a7 | -15.0191 | -54.89053 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 789fab36-741d-35ab-8749-c2b511307766 | -11.1999 | -55.02922 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3be9a088-4afe-3b34-b1dd-3a3985742610 | -14.81443 | -59.63324 | 2025-08-23 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f717847-8f51-3be5-b2e7-8a83ba22d756 | -14.80692 | -56.00282 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d23d42d6-614e-3efc-87bc-1d61f0907b97 | -11.19933 | -55.03282 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f600f0e6-2d00-32e5-a614-f2acb3f2c58c | -15.05501 | -56.39114 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4fc7ef23-9186-3993-8ff6-a047a5af4e75 | -14.34251 | -58.58889 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 9eabcc95-8316-3c77-9212-fcb4e6516119 | -14.38103 | -52.05516 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81e48b28-d53f-39da-a528-0bca12c8e9e9 | -8.68827 | -62.86786 | 2025-08-23 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06736ace-c7ad-33c8-a967-4d78dbec08f0 | -11.19875 | -55.03642 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfaf93e4-44db-3a37-8a77-ad987b113544 | -14.43361 | -52.04545 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96f3c0e5-8b88-3980-9112-fb5a06c338b5 | -8.8966 | -62.43323 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60a10172-e9a4-36fb-bbcd-d485ce905cfb | -11.30762 | -55.14336 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c851d67d-0ab6-3180-a7be-e97eafec67aa | -14.66222 | -54.91145 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58042f90-b851-34e5-8ec8-b044e3ece927 | -9.10666 | -61.43153 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 20a3435c-e4b8-3737-ada6-b3e35063c4ac | -14.62009 | -54.8537 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebe4382f-8512-3cc6-8c79-eb57f61949da | -14.2998 | -58.52424 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f219a76-60b7-3fd4-bbd0-d7abbcd5e7be | -14.76584 | -55.98861 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 521c8e54-4534-3b92-9102-de62c150c52d | -13.47133 | -47.03289 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6e6b3475-c945-319c-87fd-9f992e4804da | -8.88024 | -62.43363 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f19bd063-ef6a-398f-95b0-6c8e76399b62 | -14.66408 | -56.59122 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 858505ab-fae4-3854-8828-c532c12fe40f | -16.61574 | -49.40406 | 2025-08-23 04:53:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f083cfc-0d7e-3d71-a65b-b4ff10913145 | -13.34215 | -54.39275 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b867755-7aa3-3cee-b10b-dc429548e944 | -9.51763 | -60.51387 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 859847d8-13fe-3ff1-b22a-16e7784d5d0d | -10.46746 | -59.13067 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04aed114-f713-3def-bbf2-6738ca498d34 | -13.0402 | -46.32491 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 80eba22a-be68-343e-b32a-8ecdadf4f11e | -15.03534 | -56.38387 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a8e9521-8d92-3592-a23c-695ec13525cf | -14.65204 | -54.86628 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61346919-3ed6-3426-acc9-277caf96df66 | -14.36352 | -52.05245 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc0473bf-0d21-341a-8eaf-188fe33122e5 | -11.18479 | -55.03783 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abe3a835-a577-365b-a264-f5f9b3f3af75 | -14.38161 | -52.05117 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4de9877d-6c97-3956-9529-7d9082cfd691 | -10.61115 | -55.41084 | 2025-08-23 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9673f4be-5d9f-36ce-b896-84890121e11a | -14.66432 | -56.61113 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ba25d52-8f6e-328b-81e9-a4dacbc1a392 | -13.16386 | -46.91851 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0cd45c41-f7ab-352c-a0bd-e365810e47e8 | -11.19541 | -55.03586 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 620e6eb8-6141-36fa-8368-0a961f1c168a | -13.37688 | -46.2182 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bb317ef1-969c-3e6a-9778-cf45ff05db49 | -9.21676 | -60.79527 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ddb30f2c-afc1-3af2-83cc-ce0a60de9996 | -9.95513 | -60.19392 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 9256d903-8319-3cdb-ae09-1e4ab629ba30 | -9.84087 | -64.29373 | 2025-08-23 04:53:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a84988a7-aac7-3280-a941-8872636b0bdd | -14.60746 | -54.82613 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51f1ac02-c8ae-3b8e-9b5a-c62701bd8e86 | -13.4214 | -46.26513 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| dce31a29-4d46-3c52-bfb5-882f43c87e94 | -14.81654 | -47.95178 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 03485bb1-4f4e-35c7-82a0-399834f92d53 | -13.36751 | -54.40411 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19d519a6-1991-3e95-bf78-e07d412917d0 | -9.94563 | -60.16954 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eadd2dc9-12ae-3cba-b3c3-916267f56f28 | -14.81535 | -59.62798 | 2025-08-23 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 739df80a-c81d-377f-a3e3-cebecb226501 | -13.37523 | -54.39813 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5626bd2e-5594-3fee-bd04-0224333ec0e7 | -9.24148 | -60.47343 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e9be84d-794b-3530-99f9-eefb139fa9f1 | -13.02683 | -56.86738 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01dd181f-beba-387f-86e1-d77927dfa480 | -17.28196 | -46.77484 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42d888de-7b4b-3045-be97-51354b144ebc | -13.47881 | -46.89949 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ed2588af-d39e-3298-ba19-aeddb8ccae90 | -13.02287 | -56.82587 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7737a69-722b-3c2b-9cfc-d8d592f86080 | -13.17389 | -46.91496 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d95b5ad2-5413-3e92-9f55-dd5d2cebc0f5 | -10.10973 | -57.76745 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34a6cb6e-132f-3304-ae1f-dff03cddd7a2 | -14.67377 | -54.9243 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91335e4a-4ffd-3581-a464-5d09c2441ec5 | -9.9536 | -60.20279 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56894ad4-df5c-36da-92a2-d2e676ad986b | -12.30279 | -50.00113 | 2025-08-23 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c414139-3112-30db-8ece-b1f98472e61e | -15.03233 | -54.8927 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8bb3a855-6b66-32f7-ad42-409fe63a5d5a | -11.44693 | -47.32894 | 2025-08-23 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 871a805b-53bf-3d63-8fa6-83846608295e | -9.52884 | -60.53049 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 78176bb7-b84a-3561-859d-c3ac83d4eb9a | -14.91889 | -47.31726 | 2025-08-23 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb6674d1-55c3-36ea-9d5f-58672759a3c8 | -14.66066 | -56.59072 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ff36281-337e-3a11-b9d8-ef214b33b654 | -14.91824 | -47.32253 | 2025-08-23 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cfa8ce7-bb06-3b7d-b8a6-663ce68d00b6 | -14.35634 | -53.12186 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3e919a5-4dbf-350e-8225-3137b2709943 | -9.94993 | -60.19752 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| e63979fe-fa53-3a9a-ad87-8a446ad6fe70 | -12.77992 | -48.71504 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d89cb44-8976-349e-a3a3-e3818181e132 | -12.71141 | -48.10392 | 2025-08-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34d2d4d1-08ca-3513-90e9-d5ece74ce894 | -13.37192 | -54.39759 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a52647b2-e0a0-3b24-8edb-431f2550274f | -9.50477 | -60.50666 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdf0cc2b-b08d-3b67-ae6e-fdd95caf919f | -8.8914 | -62.42963 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da2203b1-cf20-3a03-a6da-56a01f1333a8 | -17.26782 | -46.76443 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 034e267d-8f90-3490-b480-e6d92ef48950 | -14.47338 | -55.94656 | 2025-08-23 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd632266-af30-3b0b-9f2b-e9d76d99a01a | -14.34377 | -52.99802 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6bb71c8b-01a6-3386-a816-8fe25d652b6b | -14.35886 | -52.05993 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6df1c71c-4bd5-35ef-9b6e-2984d444d6e5 | -9.96381 | -60.18935 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f2082a5-50de-3caf-b98b-524927b337b9 | -14.37868 | -52.04662 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f5884005-db3a-3d70-8ba8-f1284c37be7e | -9.21586 | -60.80023 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 07569353-ddc6-3f8b-bc7a-97a5db363e42 | -15.00093 | -54.87659 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9607c039-0731-3e0e-b61b-3e6063003176 | -14.66715 | -54.9232 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0558e0c6-6adb-3177-a66d-a9f234082f76 | -12.5431 | -45.61709 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bdfc2fa-5884-34e8-95b0-35ee51f7832c | -14.65041 | -54.85508 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60985d3a-c559-3d2d-984f-8a7452f3acdf | -12.50813 | -53.80904 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcbf8d82-c6d6-34a0-b75e-40795edc77a4 | -9.95373 | -60.17556 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7defaee1-58f7-3a01-8f73-6d160c6b82fb | -13.72641 | -44.40097 | 2025-08-23 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5bd391d3-a24b-3d3b-8f6f-66c3747fdee7 | -13.37248 | -54.39406 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51cbbeac-496e-3bd4-8df0-059e4117896b | -13.41577 | -46.27011 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7ee5d30-5167-3c73-ad39-172e94924fb7 | -15.06759 | -48.48244 | 2025-08-23 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7d02ea2-a5a4-38bf-98f8-6fe42556e1ce | -14.65977 | -54.86028 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e5b2b33-35fb-30ce-9303-6cd1f5ce03a1 | -9.94893 | -60.19569 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c919ffb3-31ea-32d8-b727-5bb0c087281c | -14.26604 | -58.53357 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6e521840-2afd-3f41-ae2a-833ec2205e15 | -13.37809 | -47.50397 | 2025-08-23 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 02e0a71d-8902-3992-b58d-544caa99f652 | -12.51089 | -53.8131 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1400619-9672-3e74-9a54-f153d7b6be67 | -15.05134 | -48.47104 | 2025-08-23 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README49.md)
