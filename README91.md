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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b78d94dc-efe6-3286-837d-027fa4e3223c | -9.6865 | -38.29848 | 2026-09-29 15:46:00 | NPP-375 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a4e65d54-102b-33bd-a671-187d3d748075 | -12.33447 | -40.30549 | 2026-09-29 15:46:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 84550037-119d-3a45-a110-7c1f5e8dd90d | -14.62749 | -40.70605 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 462e4b32-cdeb-3b3d-84ef-6be41c6900d8 | -10.29378 | -40.02115 | 2026-09-29 15:46:00 | NPP-375 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 1f42ae3e-2a90-3ec1-a45d-8d687fe3cc2e | -15.1957 | -41.43524 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 781da812-3f7f-3006-a49a-d14fbcbe0292 | -11.61554 | -43.32348 | 2026-09-29 15:46:00 | NPP-375 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a2a95b2a-0346-302b-be1f-55c486157976 | -15.23594 | -41.74685 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| a0c0d3e0-1ae0-3ca6-968c-8c3e2c2bd6e4 | -7.96369 | -36.07343 | 2026-09-29 15:46:00 | NPP-375 | TAQUARITINGA DO NORTE | PERNAMBUCO | Brasil | 2615003 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2c933631-ed17-3267-a801-befd581efdd4 | -11.09245 | -39.05966 | 2026-09-29 15:46:00 | NPP-375 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c353b75c-eaf3-3d38-88d5-654b60d06455 | -11.82407 | -43.30472 | 2026-09-29 15:46:00 | NPP-375 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6a820d0f-d9e4-3460-a76d-9af5521b39d7 | -12.34965 | -44.27649 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8036f74c-f953-33c9-9b7d-2664cc411945 | -14.43367 | -41.13622 | 2026-09-29 15:46:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c8cb66b3-f852-398b-8210-c2a8594be29d | -13.62182 | -39.28262 | 2026-09-29 15:46:00 | NPP-375 | TAPEROÁ | BAHIA | Brasil | 2931202 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ff61807d-7866-3d8e-a7c1-290fd5a926f9 | -7.82636 | -36.74583 | 2026-09-29 15:46:00 | NPP-375 | CAMALAÚ | PARAÍBA | Brasil | 2503902 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3302f677-90fb-3caf-906f-f90b094a754a | -11.72165 | -43.45802 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| d6718741-c0a0-3814-bf59-d5d8b327e451 | -13.63459 | -42.70603 | 2026-09-29 15:46:00 | NPP-375 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 5060dc21-9d6d-391c-ae6f-3dacf42862c7 | -11.3139 | -43.54935 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4e75cad3-5ca1-3964-91e5-dcc5495c8041 | -11.31407 | -43.55754 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 38876107-4e19-3927-abf4-0eb57467bf9d | -11.66032 | -43.52969 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| d6bb3281-9aca-3ea4-a84c-0bb857a4eaa7 | -11.40679 | -43.45108 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 9a91ab0c-6969-32dc-a163-3983f8a85fd6 | -14.54483 | -40.74214 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f8606def-a0f6-3c92-b74a-55a6da17c3d2 | -11.40675 | -43.44321 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| ab7254c6-0182-32d5-abf5-f11d5d66a062 | -8.69759 | -39.60029 | 2026-09-29 15:46:00 | NPP-375 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| ffed1aca-3c48-3d1a-9c98-9b9ff9cfaddf | -9.61063 | -42.31505 | 2026-09-29 15:46:00 | NPP-375 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| eff70fe3-9880-3af0-9284-213f87cd4d8b | -15.29979 | -42.76579 | 2026-09-29 15:46:00 | NPP-375 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c5fcd8bd-fd38-397d-9fe9-4542fb7a5ce1 | -9.4441 | -41.81581 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 661f4686-e34b-396c-8fa7-d52ee9b6a604 | -14.38717 | -40.94296 | 2026-09-29 15:46:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a2f9141d-ec4c-33f2-b2ed-39bf52f8fd80 | -11.82309 | -43.30624 | 2026-09-29 15:46:00 | NPP-375 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 2c926ff2-b491-3a99-92ed-6b839dfdf4d6 | -11.66424 | -42.60927 | 2026-09-29 15:46:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| fa2061f2-a0ed-377c-9c26-4d84ca91c090 | -10.95281 | -43.88406 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0ea9f277-b0a3-335c-ba7a-e17a5c143877 | -15.22869 | -41.7446 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.5 |
| 5c02ef66-35bc-39e0-80ad-47982bb5a4c0 | -13.33512 | -43.95436 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e6fa67c1-812f-3a45-90ae-ee00d2658426 | -15.82963 | -42.55939 | 2026-09-29 15:46:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 93d6fe0a-4960-3a4e-bb6c-472cb0f09e22 | -12.22079 | -42.02245 | 2026-09-29 15:46:00 | NPP-375 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d580dac0-2941-38e9-9a1f-43682c040357 | -11.43213 | -43.42967 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 65a4351f-7750-34d3-a775-5fd97b136425 | -14.1703 | -40.54521 | 2026-09-29 15:46:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 948f9580-ee98-3cb4-8184-ab89845d6f3c | -15.07283 | -41.94728 | 2026-09-29 15:46:00 | NPP-375 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| aeee4c62-f961-3286-a4da-615e5b09cf92 | -15.53366 | -40.84422 | 2026-09-29 15:46:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| 91c89e0f-72d9-38d0-aeda-0645d73a2f17 | -13.6763 | -41.01311 | 2026-09-29 15:46:00 | NPP-375 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 4e869f52-b30c-359e-9f46-2f263b9739b9 | -11.39853 | -43.43153 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ee2828fc-f718-3204-a111-e23a4ef9e71c | -8.9665 | -39.97625 | 2026-09-29 15:46:00 | NPP-375 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cedafe93-6d7d-35df-85c5-eb7eb62c46f4 | -14.88488 | -40.41335 | 2026-09-29 15:46:00 | NPP-375 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0297d2dd-5ca4-3b47-b8a8-b6c075580619 | -13.37815 | -44.01583 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9826c219-bd3d-3907-bc83-563b6c88bef7 | -11.6228 | -44.1506 | 2026-09-29 15:46:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a8b16a9a-2e66-3fb4-ba75-fcfd36f6ffa1 | -12.06812 | -40.68075 | 2026-09-29 15:46:00 | NPP-375 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| dd9a6004-6834-3c11-97df-5c87ffd1fd7c | -11.6518 | -43.51624 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 5d4aff3e-c6bc-34a4-9090-a84ee32cb706 | -11.65044 | -43.50491 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| dc990945-5052-30f2-9ca1-6a19c569f0fd | -12.66859 | -42.67859 | 2026-09-29 15:46:00 | NPP-375 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 6d6d31bc-af04-39b4-bf91-a8201f071d75 | -14.91717 | -41.03703 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 6793ee6e-182d-3d5a-ad69-cb96fd379845 | -11.71404 | -44.51059 | 2026-09-29 15:46:00 | NPP-375 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa0aaad6-6914-3626-a613-1a1eabb154ce | -15.8365 | -42.55889 | 2026-09-29 15:46:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 6ddfb021-bd30-3ec7-a337-ccae9d5e27ae | -10.27428 | -40.08836 | 2026-09-29 15:46:00 | NPP-375 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0a4040ba-55ee-381f-bc85-70d21411bdbb | -14.0564 | -40.57431 | 2026-09-29 15:46:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5d8d2544-1b11-350e-954c-42fd95679113 | -15.8368 | -42.55959 | 2026-09-29 15:46:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 10dc6731-8c90-3054-a3c1-40e55474d6f2 | -9.43922 | -41.82965 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 18f8d643-d5ec-368d-bd07-d1089e5cae85 | -15.1924 | -41.06762 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e701d24b-6e51-39d5-aa96-72c88a7e0662 | -10.21383 | -40.35662 | 2026-09-29 15:46:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 69623a0d-345e-3ee0-adf5-e10fe86960b8 | -14.72156 | -41.59359 | 2026-09-29 15:46:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 88da40e7-2ace-337f-af2e-335e8dc3e5c7 | -15.22893 | -41.74225 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 205.6 |
| c89aeff5-31cb-38b1-be1e-8d83cc530127 | -11.43565 | -43.45302 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 3cfc65e9-03e0-3895-96c0-00abaa89c641 | -14.60983 | -41.1099 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 38bafde9-b891-3f29-a7fb-caa081c70a11 | -12.44057 | -44.15041 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 233.1 |
| 99e79cc6-ecbd-3b5e-9366-dda10ef4afe0 | -11.44113 | -43.43967 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.2 |
| b573b2d4-7411-3485-9874-8178a2d9a566 | -14.98461 | -41.48521 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 8063f868-ba3e-324f-84be-33e78e9700e7 | -13.07545 | -39.90088 | 2026-09-29 15:46:00 | NPP-375 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| e3b8ae7b-0007-3e49-806b-a318b793648e | -11.36188 | -43.36172 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f67da5d4-06ba-316d-9dca-fbf06805f07c | -10.29881 | -40.01704 | 2026-09-29 15:46:00 | NPP-375 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 40.3 |
| aa646b32-c0e8-37fb-9e71-2cf8315365a6 | -11.81723 | -43.30549 | 2026-09-29 15:46:00 | NPP-375 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| cf751d84-4c4d-36ff-9cbb-9ed2705f2f06 | -11.65802 | -43.50907 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 0a9533cc-7f07-352e-8866-590b72290590 | -11.42599 | -43.43666 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| d95ba8e6-9721-306d-84c5-8d61bc310709 | -10.95469 | -43.87873 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6abde162-1a59-38eb-af5c-14f0832af884 | -15.00039 | -40.48061 | 2026-09-29 15:46:00 | NPP-375 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 56d018ce-e5eb-3cb5-a2fc-6c62688cc0d9 | -14.99597 | -41.07996 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 1f8c3135-5af4-3459-9432-c3dc81cb4507 | -14.75141 | -41.05153 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 2537ca98-3887-3de6-83b2-55746d0141a3 | -13.5131 | -40.83486 | 2026-09-29 15:46:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3082935e-a743-30f0-ab28-71b0da81bbf6 | -14.66234 | -41.33138 | 2026-09-29 15:46:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 838269fb-3554-3826-8451-31a3d97018fb | -8.69801 | -39.60338 | 2026-09-29 15:46:00 | NPP-375 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| be55dda1-ec46-3999-b0e6-663e8d211567 | -11.43973 | -43.4352 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 0a3fa2cc-314f-39c9-910b-e49890e35461 | -12.44247 | -44.15642 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 1cc670c3-21ed-3778-97ba-3c030953730c | -11.31341 | -40.66008 | 2026-09-29 15:46:00 | NPP-375 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| edf8d547-dca2-3aca-bcfa-99346d99a2ca | -15.22924 | -41.74979 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.5 |
| e3307525-4bdc-3269-b875-d66185e7a4d6 | -14.76718 | -41.20244 | 2026-09-29 15:46:00 | NPP-375 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| fdcdbdf3-3d09-3bb0-98ce-e87b1066eb4d | -12.91748 | -40.04081 | 2026-09-29 15:46:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 8656817d-e7a6-3f8c-ae52-a5a2a6f95998 | -15.66978 | -40.48905 | 2026-09-29 15:46:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2b2faf26-d706-37ac-9fa3-9185d343b8ca | -9.06721 | -45.00694 | 2026-09-29 15:46:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 56ff23ac-192f-33a1-b4e3-f4a9647a61a8 | -12.33605 | -40.30342 | 2026-09-29 15:46:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 72ecc4e6-5b52-3c8e-bda4-113fb5616e58 | -14.9786 | -41.53022 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 779d3794-0818-3678-9463-8e292bd896b9 | -15.01029 | -41.78671 | 2026-09-29 15:46:00 | NPP-375 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 444c079a-1901-3dd7-8f80-e7c1f0bc4778 | -15.53412 | -40.8488 | 2026-09-29 15:46:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| bcca9c5e-67e4-39da-ba4c-0f4384a2fe77 | -11.00624 | -41.42641 | 2026-09-29 15:46:00 | NPP-375 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ae7b179f-c550-3ae1-8a95-4c7a81d2840d | -11.63043 | -43.51344 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| e72b1ce8-bafe-3d9c-92c0-b1a92982cbc0 | -10.28804 | -44.62306 | 2026-09-29 15:46:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| d773d515-37f6-37d5-8d6a-5a9d02865a73 | -14.58125 | -40.17376 | 2026-09-29 15:46:00 | NPP-375 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 851cab04-8d61-32e6-ab25-a963c10fbf81 | -13.32671 | -42.69833 | 2026-09-29 15:46:00 | NPP-375 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 173.8 |
| e06e6b79-ca36-3102-a1ac-654b1e9cea9a | -12.2181 | -38.90946 | 2026-09-29 15:46:00 | NPP-375 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e3209de-554b-3c47-bcec-9bd85222f7a2 | -10.79978 | -39.10217 | 2026-09-29 15:46:00 | NPP-375 | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| cb61387b-191c-390c-8d45-e9bd9cb99170 | -15.3099 | -41.77143 | 2026-09-29 15:46:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| f4b7e466-d97d-32e2-837a-acbf844c9b01 | -10.80077 | -39.10217 | 2026-09-29 15:46:00 | NPP-375 | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a4f33c7a-b302-3dab-92da-3a24b0ff93eb | -13.37899 | -44.02375 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| c23a9828-9cc7-3618-b7c3-0838f7a78cf6 | -11.66875 | -43.54188 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |


[Clique aqui para ver as próximas entradas](README92.md)
