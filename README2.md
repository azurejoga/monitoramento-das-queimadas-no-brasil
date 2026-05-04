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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a794f52-dccf-32cb-a911-4853d1e7a83c | -11.91678 | -54.82121 | 2026-05-04 04:23:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 52083e5d-2b22-3b69-8540-c70a29fb4dcb | -12.35988 | -50.03448 | 2026-05-04 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0619590b-402a-3dae-9539-c5cddc3e18fb | -12.36054 | -50.03072 | 2026-05-04 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8861ea15-6530-3902-9854-718847d67b76 | -12.38847 | -50.0282 | 2026-05-04 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 246315e6-904c-3996-a1a6-a5d55d12581a | -14.32515 | -57.73853 | 2026-05-04 04:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 371bd065-1557-39e8-8b3e-5ce88b4ed6db | -11.91219 | -54.82489 | 2026-05-04 04:23:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c930af91-5f75-3d4a-8b18-dcc898951014 | -11.92025 | -54.81409 | 2026-05-04 04:23:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a928ea56-32c5-38b2-9630-e5d9baec7c41 | -10.58486 | -44.32745 | 2026-05-04 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea5ed861-56b5-38cc-a197-d6b259f582b1 | -11.79056 | -43.6302 | 2026-05-04 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b8f0f8b7-d358-3180-81b0-8238c0920a9e | -14.30273 | -49.24632 | 2026-05-04 04:23:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9459cbee-22e2-348b-8eb3-4b19d20ea5ea | -13.94797 | -47.25606 | 2026-05-04 04:23:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 782835b9-d42a-38b0-8c42-46675a5c019d | -11.84952 | -55.01565 | 2026-05-04 04:23:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2cc1368-61be-3206-b5bd-e989034ed1cd | -14.06409 | -53.39786 | 2026-05-04 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9adb8f0a-a445-3467-b4f0-529f4ecef2f3 | -13.99143 | -47.23122 | 2026-05-04 04:23:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83afe742-9485-38a5-86f5-c98473e36d80 | -12.35577 | -50.03372 | 2026-05-04 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76af45ef-2d78-38cc-bc58-714b96ea4493 | -11.84378 | -55.01447 | 2026-05-04 04:23:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bfaf238-0473-331e-be4b-4db8d5776737 | -14.06295 | -53.40374 | 2026-05-04 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66764641-d919-37f9-85f1-0f519ef69e94 | -13.95904 | -47.25398 | 2026-05-04 04:23:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac95b8fe-eb6e-3f75-b7e4-1bb7d33f682c | -11.91945 | -54.81807 | 2026-05-04 04:23:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 966897c4-7240-38cf-9ceb-5d8de3d38fc0 | -10.58153 | -44.32691 | 2026-05-04 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c075e1b-0f93-3acd-9d88-dc81321e74cf | -11.85083 | -55.01198 | 2026-05-04 04:23:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22ed95d6-d418-3d11-9615-181b98c76e92 | -11.84298 | -55.01854 | 2026-05-04 04:23:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44dfccd7-d118-3858-bfee-8d861744998f | -10.97689 | -45.09322 | 2026-05-04 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56a0897c-cf08-30d0-b476-a0c827659d52 | -13.95557 | -47.25336 | 2026-05-04 04:23:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af02ef06-2821-31b9-9e01-8ec5d029e48f | -11.913 | -54.82086 | 2026-05-04 04:23:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 222f03d3-e0e5-31eb-933a-21bfcac0eecd | -12.36465 | -50.0315 | 2026-05-04 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa8f0319-3a6f-34df-9a23-1803c7b6ed29 | -14.31874 | -57.73682 | 2026-05-04 04:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecefb5b2-3a5e-3473-b545-a2fb0320fd5a | -12.36589 | -50.03561 | 2026-05-04 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 23689778-c2b6-3d54-9f24-2ccccd3e68bc | -12.36657 | -50.03186 | 2026-05-04 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5126cd3-7eb6-3320-b15b-fa0406acef47 | -10.97966 | -45.09732 | 2026-05-04 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2b7f170-4bee-3627-b6fd-300fa45696a8 | -14.62413 | -43.66817 | 2026-05-04 04:23:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4d5411d-8655-34fa-ae56-1ebb55bfbd03 | -14.31748 | -57.7428 | 2026-05-04 04:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4439d696-869e-3fa4-98a0-948f142eaabc | -13.95145 | -47.25662 | 2026-05-04 04:23:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c753e9c3-a809-3518-9db9-5ebe999c1cce | -12.3681 | -50.03603 | 2026-05-04 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95b07f18-c9f3-3032-9179-6b0219ddea9b | -14.05912 | -53.39684 | 2026-05-04 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f77ba8d-29bb-37f2-a9c7-bd4f27a8882b | -12.364 | -50.03525 | 2026-05-04 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cd257b1b-56d6-3048-9d0b-23385ffce843 | -14.05798 | -53.40269 | 2026-05-04 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba75521d-3d31-34bc-bd07-0e020678c47c | -11.55342 | -48.27254 | 2026-05-04 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94257a1c-4e12-3147-83fc-993b0e158506 | -11.79112 | -43.62663 | 2026-05-04 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 936ae4a4-f253-32aa-91a0-f265d3de555a | -11.91755 | -54.81725 | 2026-05-04 04:23:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2075c133-e754-37f0-8117-e42f52a938d9 | -14.32455 | -57.73728 | 2026-05-04 04:25:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3f3baf4-fadc-30fa-bdd4-0d64e34d36e6 | -17.50257 | -42.35618 | 2026-05-04 04:25:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92ca92c3-bed0-3f4d-9164-3c83bb2f6204 | -17.405 | -42.62312 | 2026-05-04 04:25:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1912e654-f076-35b8-9790-801ba3926380 | -14.31684 | -57.74156 | 2026-05-04 04:25:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27d339cf-3e8f-3d28-8d41-8a7d0317edbb | -21.28916 | -49.19194 | 2026-05-04 04:25:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5eb10847-0fa6-3575-8355-2b0b138e313d | -20.17331 | -46.46515 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03c34c48-d26e-3cda-acf9-76be549b597b | -20.18172 | -46.45528 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b740a75-e907-3fab-8b2c-8414de066993 | -18.00486 | -52.97379 | 2026-05-04 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05f0242d-13c1-3065-a9d8-fce5878d99b1 | -18.00037 | -52.97279 | 2026-05-04 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c81db8e8-3cad-3e94-a617-ebdd781b9e93 | -18.25407 | -51.26237 | 2026-05-04 04:25:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e61dc86-1ffd-351a-82f3-ca20a1eb4f18 | -21.50018 | -51.77302 | 2026-05-04 04:25:00 | NPP-375D | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 95684f59-6edf-3796-8431-671fa3f468f9 | -21.51878 | -49.86225 | 2026-05-04 04:25:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f82dc190-b05b-3933-bb99-eb14ef9af3b2 | -18.04945 | -52.99059 | 2026-05-04 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a28df9f4-06cc-3092-9794-3cc05113b952 | -23.16083 | -48.35999 | 2026-05-04 04:25:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e96e9a7f-218c-3a5e-b270-6b09c17f4d54 | -21.51728 | -49.86327 | 2026-05-04 04:25:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 594f703b-4e91-3d25-b075-23da072d5c5d | -18.00099 | -52.97509 | 2026-05-04 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87fa890b-8ad9-393e-b6aa-572dc79da71d | -20.17156 | -46.47621 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d483836f-8a1b-3923-94c7-faed1a0dc30a | -18.66255 | -46.47845 | 2026-05-04 04:25:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee3761a3-68b5-3a90-ae68-a85f10d60e6e | -21.49963 | -51.76916 | 2026-05-04 04:25:00 | NPP-375D | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e3132f2c-3bc6-364d-9a68-b2e5f76a8a01 | -18.26236 | -47.00937 | 2026-05-04 04:25:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7450f612-c2e2-3418-8d7b-9651ca36dc3d | -19.69553 | -47.98057 | 2026-05-04 04:25:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 449cdcb3-64bd-3e8e-9510-33b6f2fa59a9 | -20.17273 | -46.46883 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f2d66d4-e570-3bfd-aae9-cc326ee48c43 | -20.17214 | -46.47252 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0705e871-1e83-3af8-8b73-f9ed9c181c33 | -20.17781 | -46.45837 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11303984-747d-31fc-beeb-4e5a1105bb28 | -22.36265 | -47.3175 | 2026-05-04 04:25:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 1fe75736-d4af-3e95-baf0-2b51429e61c0 | -17.91967 | -42.89299 | 2026-05-04 04:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2d271635-8dbd-3142-abb8-8f25150e058a | -18.00548 | -52.97607 | 2026-05-04 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d2d47e3-2383-3ccd-aff8-749dab596d8b | -18.08097 | -52.97287 | 2026-05-04 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4a802f5-e75b-33c2-869e-4126dff65f05 | -18.04854 | -52.99527 | 2026-05-04 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 035ce7a2-1c18-3b34-bd2f-1bd68ed9be9e | -18.25005 | -51.26154 | 2026-05-04 04:25:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 110621c4-a1de-393a-ad6c-1caf3bb77571 | -20.18505 | -46.45587 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b4b06bb-74f5-349e-b140-9e5bb7731de6 | -17.50526 | -42.35477 | 2026-05-04 04:25:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72110dd5-adf2-3070-8cd3-c8fad25a8f92 | -19.69893 | -47.98119 | 2026-05-04 04:25:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0752f897-6c61-36ca-96f9-8ff192065853 | -21.49626 | -51.77216 | 2026-05-04 04:25:00 | NPP-375D | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bf13f1d9-2c7e-33f6-8899-1a89b1a79600 | -20.17664 | -46.46574 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecea567c-54fc-3aa5-acb2-46a0362969ac | -22.36598 | -47.31812 | 2026-05-04 04:25:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 93dc5c9e-2dc0-3601-9dfa-18ba99f7ff20 | -20.18563 | -46.45219 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a02bb37-8a2b-3bff-aa5a-ca9d9942dd76 | -18.00396 | -52.97847 | 2026-05-04 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9a1b081-ecbc-3392-a475-d28699b4b128 | -18.07648 | -52.97193 | 2026-05-04 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0aa5ed3f-e1d3-3b70-bbc9-7437319b4ab3 | -21.19541 | -48.81485 | 2026-05-04 04:25:00 | NPP-375D | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cffffdfe-6fd5-3108-8948-8523fc113cfe | -20.17373 | -46.48416 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0de632eb-fb65-3441-9f15-4bbc7ba9cda8 | -20.17314 | -46.48785 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e3d49a1-e883-354b-b783-279ba89c8c31 | -20.17706 | -46.48476 | 2026-05-04 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 972ce076-cea1-3729-8c8c-8dddc40eb644 | -10.98195 | -45.09314 | 2026-05-04 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f34842e1-6788-3192-a542-7af8b7f461f2 | -9.4681 | -47.79664 | 2026-05-04 04:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f048e98-9513-33c1-b546-3b4fdcad1070 | -8.20951 | -43.7145 | 2026-05-04 04:42:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 588a3514-3311-32ab-8e9a-c3cc6e96fe7e | -11.84069 | -43.96756 | 2026-05-04 04:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0a18660-bf5f-3a53-a092-3c5d887cd0c6 | -10.98605 | -45.09377 | 2026-05-04 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3a68dae-daf1-385e-a58a-c2dba3ca5d22 | -11.84518 | -43.96819 | 2026-05-04 04:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 490e8609-049f-3916-91b8-5c7aac185e82 | -10.98553 | -45.09745 | 2026-05-04 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be481682-b224-34d8-ad70-3d35283dde9d | -10.98501 | -45.10111 | 2026-05-04 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b0e098e-35e1-3b12-a8e7-1752d9261f77 | -10.98247 | -45.08942 | 2026-05-04 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45693d78-207b-394f-a7af-7cc0f24f161a | -10.97733 | -45.09621 | 2026-05-04 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 10dc43e1-ebe1-31e0-94de-4a927aa18594 | -11.885 | -43.80592 | 2026-05-04 04:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8bd71921-74fc-3b54-a1fa-0d6801eb41b8 | -10.8601 | -48.90604 | 2026-05-04 04:42:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 658f193a-5323-3e93-b5a7-798f6efc744c | -10.98143 | -45.09684 | 2026-05-04 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| decb4d29-bf72-32e4-add0-451a56e3573d | -10.97785 | -45.0925 | 2026-05-04 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 242d0160-b86e-39a0-80e8-fe25041c0203 | -11.99607 | -47.7743 | 2026-05-04 04:42:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cfd42b13-9163-3f96-b9cb-27131adfde3b | -11.88046 | -43.80529 | 2026-05-04 04:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 583bbd3b-1c28-373c-8eba-73cb8959ddda | -10.98091 | -45.1005 | 2026-05-04 04:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README3.md)
