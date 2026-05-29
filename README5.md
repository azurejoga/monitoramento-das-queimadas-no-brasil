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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37a10b1d-24e8-3546-a0de-aac3e425ce8e | -8.84714 | -46.70926 | 2026-05-29 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28c3b293-f10b-3b86-984c-115d644238cb | -13.17694 | -52.70944 | 2026-05-29 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 812a474a-f168-3989-bdc0-48aefcbca549 | -11.32831 | -46.79415 | 2026-05-29 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d6c9ee8-5365-34e8-aa13-669e428f14cc | -11.59759 | -47.44226 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a1edf5dc-69d6-3c3f-ad0d-3e8b71ce6c93 | -12.3713 | -54.16141 | 2026-05-29 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d8ccd7fc-24df-33fe-908e-8d3ee2430637 | -8.6843 | -48.30322 | 2026-05-29 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 23313200-2f2f-3cbb-8378-32125db9769d | -12.05018 | -45.27283 | 2026-05-29 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93bc849f-488d-30a6-a9bd-9ea3247b6d49 | -14.44036 | -48.90263 | 2026-05-29 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79e92245-7139-37a7-bd74-e5bd8fe269e5 | -10.71494 | -49.03831 | 2026-05-29 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c32d1ad-8980-33e9-ac79-8a002bb3cc9e | -12.00148 | -45.14596 | 2026-05-29 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ae8c8ef6-200f-3e8b-ac91-d72270c7df86 | -11.60037 | -47.44653 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3cc93647-6fb0-3d88-a505-f915f62f55ad | -8.7156 | -47.80132 | 2026-05-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa41271b-c9da-3c22-8238-ef3ea2feeefa | -13.28391 | -48.86264 | 2026-05-29 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60514c5d-2e64-3cb4-8458-de0c065c7a14 | -12.11574 | -43.97099 | 2026-05-29 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 651de32c-59bf-38b1-8f59-107b3e12ab6f | -11.44993 | -55.10886 | 2026-05-29 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3f3c347-ecff-3895-b4b2-4fd4d1ef4e6b | -10.98588 | -45.09653 | 2026-05-29 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74355cb6-b0ad-393b-b63d-86300f61ab07 | -8.58094 | -45.94123 | 2026-05-29 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6cb4708-a376-32ba-8f42-a6d91c2b550e | -8.35838 | -48.14145 | 2026-05-29 04:21:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c8a7dfb-7429-374d-b564-3070f09063e3 | -14.44448 | -48.89933 | 2026-05-29 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c840196a-1c6d-33c7-a223-810df3be370f | -11.59082 | -47.44114 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 88d46aa7-d5e1-3b71-848c-17a924f842a2 | -10.14155 | -52.39924 | 2026-05-29 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbffa29e-9b2a-3585-8425-d153bcbbb554 | -14.44729 | -48.9039 | 2026-05-29 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8274a898-8430-3dc9-ae6b-41b87312f12a | -7.50551 | -55.00606 | 2026-05-29 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ed83f89-eccd-3a0d-b67a-9ff95a119de7 | -11.593 | -47.44907 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 6620c685-647c-3213-8b88-643a7d66c79c | -8.72653 | -48.32615 | 2026-05-29 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38c410ba-5c8e-3f98-82b8-146ee62dbecd | -11.33183 | -51.40092 | 2026-05-29 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7d08ec4-7bc4-38d4-8009-164f9962c23b | -11.8945 | -47.60528 | 2026-05-29 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b47730a2-750b-318f-bd2b-1d402d03dfcb | -11.69298 | -45.38175 | 2026-05-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 419e9371-755f-38ec-98a8-03a9d39e1354 | -17.86413 | -51.78407 | 2026-05-29 04:23:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0c72ff0-a7b1-3cf5-b97b-df0c3ecee68e | -19.68402 | -54.35451 | 2026-05-29 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2289107f-3db4-3503-b176-7e9ed3e7b6d0 | -19.68925 | -54.35094 | 2026-05-29 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24e840c3-7d9e-3dcc-9bbf-2af425c6ffb0 | -21.38323 | -49.26368 | 2026-05-29 04:23:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9604c878-1e4f-371a-9a11-8b05dcc6660a | -18.4607 | -54.7058 | 2026-05-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e34c8e6f-5fa1-36f6-bfc2-6454faa2def8 | -16.17179 | -58.48027 | 2026-05-29 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 43d1d1a1-c8c3-39aa-801a-0cd1cbb23056 | -18.46432 | -54.71157 | 2026-05-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7ea914ed-247a-33c9-b86e-996d164ee976 | -15.79683 | -58.62572 | 2026-05-29 04:23:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 49eaf2ba-7d84-3fc5-8851-15fc23760c76 | -18.45977 | -54.71061 | 2026-05-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 398ad679-64f0-33c0-a424-a462d83dc519 | -18.45923 | -45.05948 | 2026-05-29 04:23:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9cd1fc8-7968-393e-9fae-01b797a59902 | -15.7979 | -58.62067 | 2026-05-29 04:23:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ef4b6dac-d945-3e83-8a6d-d00976879bf9 | -21.14425 | -48.65526 | 2026-05-29 04:23:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cec476bf-ba9e-33d6-8b0e-e4e8e69e1b01 | -19.68837 | -54.35546 | 2026-05-29 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4bca0d0-0dc2-363e-a3c3-853fe10891c5 | -20.19156 | -49.56187 | 2026-05-29 04:23:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a87329e-abb8-361d-a166-998841d05272 | -18.84967 | -44.5527 | 2026-05-29 04:23:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5d914723-bf71-37d9-83fd-ca386a63feee | -19.17441 | -47.35714 | 2026-05-29 04:23:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7409bd76-a0c8-39f7-881f-d60d97045bfc | -19.06203 | -47.4234 | 2026-05-29 04:23:00 | NOAA-21 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76ef1bf8-2a48-328f-b90c-137fdd1035d8 | -20.48816 | -51.49882 | 2026-05-29 04:23:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e7f6e50c-b6f8-3992-8b57-66238c65e47b | -18.46526 | -54.70676 | 2026-05-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f2d8691e-b214-385e-a3af-5cf70694b3f9 | -16.17367 | -58.47836 | 2026-05-29 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 2f95ff6c-775a-396b-9e26-6e9ec0ff5a10 | -19.86522 | -43.87063 | 2026-05-29 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e22ea2e2-4a7a-369b-ad06-09ea335ab098 | -20.90211 | -46.78828 | 2026-05-29 04:23:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 715db31e-eabb-3511-889f-b168d1ec73a0 | -15.90738 | -50.55345 | 2026-05-29 04:23:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d3247ba-9c97-344d-90da-b501c8991155 | -19.06259 | -47.41977 | 2026-05-29 04:23:00 | NOAA-21 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15a27a7b-f933-3a38-b7f2-2ec96601c52f | -16.1728 | -58.4755 | 2026-05-29 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 17bc867b-d2d2-3f3f-ae52-3119d6691a26 | -15.82431 | -58.61668 | 2026-05-29 04:23:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d4820f43-74d0-33e5-9f11-e4b991addd3d | -15.82338 | -58.61942 | 2026-05-29 04:23:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cd50bdc8-84bc-3a0c-a2b1-21e92b10ae40 | -16.17575 | -58.46885 | 2026-05-29 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 7e2f16cf-72b5-3dbe-8b5a-2b32f3b6e316 | -20.72941 | -54.83195 | 2026-05-29 04:23:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 744e6d52-4242-35f2-98ee-68a756c10333 | -19.97738 | -44.85452 | 2026-05-29 04:23:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3cb050b-7a2f-3f56-a220-22613d8cb581 | -21.645 | -45.57928 | 2026-05-29 04:23:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cbac4955-89eb-32da-8ad0-9be4c46fd366 | -16.17472 | -58.47358 | 2026-05-29 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| b3c85359-10ae-36ce-a132-3116faa63f59 | -20.89821 | -46.79149 | 2026-05-29 04:23:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b47e9055-e88c-3bfc-8cee-6db09dfa0740 | -21.39736 | -48.71227 | 2026-05-29 04:23:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc091d48-8ef4-306a-952b-072cca9de257 | -20.19091 | -49.56573 | 2026-05-29 04:23:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 95be03ea-4eb1-3557-9d1f-eaabba8d9344 | -18.12059 | -42.43928 | 2026-05-29 04:23:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 24456c96-f5b4-357f-9524-36f37bfe5457 | -17.17378 | -47.0781 | 2026-05-29 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9b47b4f-6249-379d-948b-c5ffc87b6a87 | -21.40068 | -48.71286 | 2026-05-29 04:23:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7ed2b50-b5fa-35eb-b906-bdbcc1e50011 | -16.16871 | -58.47223 | 2026-05-29 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 3aa8a9c2-398f-35ce-a467-fefa71842b0b | -20.90155 | -46.79205 | 2026-05-29 04:23:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 31d8bcb0-2942-3584-bd0a-ea19b5f9dd8e | -15.80399 | -58.62209 | 2026-05-29 04:23:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 873c51ec-d53d-3ba2-8c1f-fb31c4203a72 | -18.35007 | -41.09538 | 2026-05-29 04:23:00 | NOAA-21 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7db86e27-3f96-35a1-bb08-d1f1aaee2156 | -16.17381 | -58.47072 | 2026-05-29 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 6bd576d5-030a-3908-a359-77e16120d5ae | -16.17879 | -58.47694 | 2026-05-29 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fabc786f-58d0-3ec8-8a4e-a18c98b5ad11 | -16.16679 | -58.47416 | 2026-05-29 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| ee0cb3a0-cad6-32d4-a1e9-083b2ed8e10a | -14.6524 | -54.52449 | 2026-05-29 04:23:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a7578e7-ee62-3c5d-8357-38f59bccfe93 | -15.82446 | -58.61446 | 2026-05-29 04:23:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c9b128e7-2863-3347-8608-ffc8bbf4995e | -17.23132 | -46.90746 | 2026-05-29 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e219673-b90f-3674-a2e5-f428a1b72583 | -20.08846 | -47.44892 | 2026-05-29 04:23:00 | NOAA-21 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50d8fdd2-1cc0-33e4-892e-bb472efa022f | -18.85262 | -44.55745 | 2026-05-29 04:23:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| e0a8c1bf-b80a-3256-9ab3-daf5758b149e | -21.81366 | -53.08671 | 2026-05-29 04:25:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f5cd7e1-b59c-373e-b5f9-f7ed3db8642d | -21.80585 | -49.13478 | 2026-05-29 04:25:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 96af6252-a7b2-3d15-a761-ae800b7bc502 | -22.79157 | -49.3379 | 2026-05-29 04:25:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7b2ea6a-a3f8-34ca-a101-02fa55b20e80 | -21.81462 | -53.08152 | 2026-05-29 04:25:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2126a713-0108-317e-893c-11bf72a372c3 | -23.42413 | -47.54525 | 2026-05-29 04:25:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2548cfb2-60f6-3da0-bae4-1315969e90e1 | -20.7338 | -54.83293 | 2026-05-29 04:25:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 301aab6b-9c15-3daf-ba04-3050801cc77c | -23.50886 | -45.91537 | 2026-05-29 04:25:00 | NOAA-21 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| ca9d940f-9e4f-33d3-b042-6a7599281cf4 | -22.79489 | -49.33854 | 2026-05-29 04:25:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83d12cfa-ae13-33b5-9e0c-04f0a9cedf14 | -22.78113 | -43.04324 | 2026-05-29 04:25:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c9663b9c-a09a-36bb-a23d-b0a948f2b0ab | -21.99135 | -47.62996 | 2026-05-29 04:25:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ff9e48e-0de9-3f84-98a0-9405db1da235 | -23.51296 | -45.9116 | 2026-05-29 04:25:00 | NOAA-21 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 17cdf38c-4684-3979-81ec-cb1e67c56e86 | -23.5598 | -48.57098 | 2026-05-29 04:25:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a1b5caf-a16b-3297-a12e-58e910349cbe | -22.16504 | -47.13104 | 2026-05-29 04:25:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36b42ce4-9249-308b-9e7d-1e824cc5381f | -23.2088 | -49.41117 | 2026-05-29 04:25:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2031b329-41c8-3eb6-b5b0-b1f98c458b9d | -11.591 | -47.4496 | 2026-05-29 04:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 4959cc17-8f00-34fa-8d34-097c6aada286 | -11.591 | -47.4496 | 2026-05-29 04:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 3751306f-ade1-3dbe-b505-266ece6f5d94 | -11.591 | -47.4496 | 2026-05-29 04:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 439e0378-b30d-32f7-82c6-3dbe8072d6d9 | -6.24607 | -48.57961 | 2026-05-29 04:53:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80a5d5f8-e554-36d0-95e4-17783e224dda | -6.76558 | -45.0249 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bc2b1b3-20b4-3f86-a9c7-a9b3a69d1a94 | -6.2431 | -48.57536 | 2026-05-29 04:53:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afe4a28b-8909-3d9a-96e0-8000eb823725 | -5.3222 | -44.6889 | 2026-05-29 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 31d7f42a-4006-333a-97c9-cc5957ad0171 | -7.0103 | -45.00273 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README6.md)
