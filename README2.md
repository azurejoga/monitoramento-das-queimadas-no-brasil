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
| 73e7402f-4c76-378b-a7d6-6e66b6f5be81 | -7.39247 | -43.21328 | 2026-04-18 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d3ebb593-fc2c-3a7b-9db8-ddca97d81e02 | -10.85059 | -44.53839 | 2026-04-18 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50b99b54-91d7-3bd4-8c46-47a57e5fe683 | -10.40494 | -44.93645 | 2026-04-18 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 17d0addf-0e25-3f0e-90bd-5364d6ca0e1e | -8.09913 | -43.15456 | 2026-04-18 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 31622af2-438b-3381-9afa-aaf28a442a4a | -11.19047 | -43.56144 | 2026-04-18 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 285656f8-7c21-372f-a582-9d26f8d97262 | -7.39302 | -43.2098 | 2026-04-18 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2ceab5de-e38b-35ea-bae1-e08dc5c791da | -10.40551 | -44.9329 | 2026-04-18 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd343712-8499-318d-b3ff-55e8ee50a28d | -11.97616 | -43.83896 | 2026-04-18 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66b03eb1-5c13-370f-8481-9a7d08cf4a6c | -10.14531 | -39.99237 | 2026-04-18 04:21:00 | NPP-375D | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f192e29d-9c7d-3384-a679-1b93bf4f5b57 | -10.4671 | -38.61677 | 2026-04-18 04:21:00 | NPP-375D | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 21c4b0d2-c2f1-3c75-a7f9-6f46889c444b | -11.97561 | -43.84251 | 2026-04-18 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4f16283-b746-34b0-b542-bcaf3fb3af78 | -10.46293 | -38.61616 | 2026-04-18 04:21:00 | NPP-375D | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 83975290-f208-3c8e-bfd0-9ad8bbf3cef6 | -11.18991 | -43.56499 | 2026-04-18 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 394dc8a0-300b-339e-b01f-f8521b229d88 | -17.13748 | -42.78605 | 2026-04-18 04:23:00 | NPP-375D | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 643ce3c7-3ca1-3336-bb87-7311ffcf27c8 | -13.68042 | -44.29144 | 2026-04-18 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ecb363ba-1f96-3a21-b363-290a37ea1967 | -15.9974 | -41.67487 | 2026-04-18 04:23:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e743331e-6608-339d-8f0f-2b99c0888c22 | -16.14239 | -43.55931 | 2026-04-18 04:23:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c0f2ce5-2aa7-3927-bcc4-6e6898252bad | -13.68375 | -44.292 | 2026-04-18 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6b51de9c-4310-31ff-86b3-10edb1fc9764 | -17.5699 | -46.60164 | 2026-04-18 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 642875e5-7ec8-3ff7-bde1-e0b0ff444c0d | -19.35904 | -40.64837 | 2026-04-18 04:23:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 05c75a0f-8608-377f-88e4-6b11aaad63e3 | -17.57264 | -46.60588 | 2026-04-18 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0527b1aa-2f94-3313-9d93-e91223f8504a | -17.57323 | -46.60223 | 2026-04-18 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b375d819-9e42-3cc2-b2da-8325b10fabf0 | -16.14296 | -43.5555 | 2026-04-18 04:23:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7984e7d8-a5ae-3be1-a6d7-c6ad51dda694 | -13.9527 | -42.0743 | 2026-04-18 04:23:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6a2ff832-923c-39d9-9a4e-28b2a9cf46ef | -13.39122 | -46.79314 | 2026-04-18 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 54ebeb8a-8643-3111-a5ad-4f01a28123b6 | -15.91575 | -44.7906 | 2026-04-18 04:23:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79d05641-4482-3357-9c09-8290d979352a | -17.57598 | -46.60648 | 2026-04-18 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4f7c35d-23bb-3f5b-986e-504d033d21f6 | -18.07428 | -46.37372 | 2026-04-18 04:23:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 512998f9-b276-3326-bd63-677042bf6d58 | -17.21875 | -39.68694 | 2026-04-18 04:23:00 | NPP-375D | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ff94b1ed-8c1b-3428-885d-abcaf0933951 | -18.07486 | -46.37008 | 2026-04-18 04:23:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75becbec-d2b8-3b04-840e-32dcbd8159ee | -15.29908 | -46.84792 | 2026-04-18 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2be61766-2730-3519-a358-76fd2d65de9a | -17.2163 | -39.68842 | 2026-04-18 04:23:00 | NPP-375D | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 292775ea-7725-36c4-8c9f-2aee881adc3f | -13.75225 | -42.6041 | 2026-04-18 04:23:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 63baee3a-199c-3cc0-92b6-d0101a6c1060 | -17.5693 | -46.60529 | 2026-04-18 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30cb7d80-6909-372f-81be-6a4ffcbb4fbd | -18.10431 | -40.34379 | 2026-04-18 04:23:00 | NPP-375D | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fd998af2-bede-3dbb-935f-4521dc16977a | -17.56514 | -46.63092 | 2026-04-18 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c8f7d2f-4323-31ac-9727-2403c16eb29a | -23.64753 | -48.00097 | 2026-04-18 04:25:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24622374-f047-328f-8ac6-e84105f10dfc | -20.63177 | -51.69624 | 2026-04-18 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46e41b03-b058-3cbf-846a-96879bd35b1d | -23.64357 | -48.00413 | 2026-04-18 04:25:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 085539f5-b886-3ba4-9069-cb693c655322 | -21.03753 | -48.55284 | 2026-04-18 04:25:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| cd1a8ea1-0ffc-3b96-bddf-b4849152f596 | -21.39836 | -49.00276 | 2026-04-18 04:25:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0df32b24-4ef3-33a2-a1b0-603e9b25ffc3 | -20.62778 | -51.70266 | 2026-04-18 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dfe0a72d-2b15-3f8f-acc6-8c4f7ab475be | -20.10604 | -45.3772 | 2026-04-18 04:25:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0ac8a982-b6eb-31e3-8a04-e52352074036 | -21.69621 | -56.30865 | 2026-04-18 04:25:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ea33cf6-e49e-3812-96c4-0febd02d1d1e | -23.64963 | -48.00921 | 2026-04-18 04:25:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7976720-aa68-3e00-9ef5-ada15c256f19 | -20.62476 | -51.71171 | 2026-04-18 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ead6034a-dcb1-3c39-8b04-2f9adc1b5090 | -21.70136 | -56.31006 | 2026-04-18 04:25:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b6a921b-fa32-3a07-87b6-bf52ad43a227 | -20.63279 | -51.6981 | 2026-04-18 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bfa975f-be8c-331b-a7af-889dbe893c6f | -23.64419 | -48.00033 | 2026-04-18 04:25:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 99a84779-1794-396e-ab0f-2098e9a3b53d | -20.63278 | -51.6908 | 2026-04-18 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b93c887-8416-3f71-8eb8-363f8309541d | -21.19187 | -48.60906 | 2026-04-18 04:25:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4d0acc69-a5bf-3ab6-be69-e371dba674fa | -20.62568 | -51.71356 | 2026-04-18 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 517249a5-6d8b-31b5-a562-f65e439ccd38 | -21.70993 | -48.42705 | 2026-04-18 04:25:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bef3316c-3b2c-35f3-98d3-cc1e49489483 | -20.63384 | -51.69267 | 2026-04-18 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebc871b1-7c7c-3379-a2cb-a15c6a5ad177 | -21.59756 | -48.49058 | 2026-04-18 04:25:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8837fc47-6d2e-3471-afa0-63db640d98d7 | -20.63488 | -51.68725 | 2026-04-18 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf750994-dbe4-3d91-8cff-06f99ce83d8a | -23.64629 | -48.00857 | 2026-04-18 04:25:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bee4efc-23a6-3583-8961-f5291888601f | -21.19255 | -48.60513 | 2026-04-18 04:25:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0ee8c5d8-93c9-3050-8974-5bc6f9004386 | -21.04094 | -48.55353 | 2026-04-18 04:25:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 410bc47c-defe-3a89-b23d-4c7a581058c6 | -22.96753 | -52.69927 | 2026-04-18 04:25:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2a6c014c-852f-3095-89cf-c596a5b67d7f | -21.23405 | -48.79748 | 2026-04-18 04:25:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0d517c72-f629-3ac0-8ff2-fac99fb4c5b2 | -20.1546 | -46.71634 | 2026-04-18 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 804a80ac-24ae-35c4-8cb1-09b2529f2992 | -20.16456 | -46.71814 | 2026-04-18 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cf23513-508c-3011-aac1-5322f7e654f8 | -23.65086 | -48.00161 | 2026-04-18 04:25:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 320d7ab6-4bea-3570-be92-15ad46cd6840 | -23.65358 | -48.00605 | 2026-04-18 04:25:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7063cf0c-c004-30d5-b82e-d6898505a074 | -21.19254 | -48.6101 | 2026-04-18 04:25:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 569d9455-4ef5-34af-a516-a408c2d4bfa4 | -21.18978 | -48.60552 | 2026-04-18 04:25:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f57a5e7b-6293-39de-964c-13ac31201e56 | -20.62974 | -51.70715 | 2026-04-18 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f712c30-4264-3bec-a8f5-8240674d1ab1 | -21.87952 | -47.1441 | 2026-04-18 04:25:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84e970c4-9bad-3a78-9370-e36476657a35 | -22.96348 | -52.69832 | 2026-04-18 04:25:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8e3d53eb-4ed1-3aea-9925-ee31c37c15cf | -23.65025 | -48.00541 | 2026-04-18 04:25:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d70d66a8-1959-3056-97d2-e6b37c31ce02 | -20.15851 | -46.71326 | 2026-04-18 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c90f0207-7e61-3302-b0a4-248c10e94b92 | -23.17629 | -47.52501 | 2026-04-18 04:25:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 88b5ff6f-144e-385a-af8e-16e803b721d0 | -23.27074 | -55.18396 | 2026-04-18 04:25:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eefb26e4-6663-3b08-ab75-fbf7c779f576 | -21.71332 | -48.42773 | 2026-04-18 04:25:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1cb733b-3f3f-35d0-a8fd-5ac3e7281833 | -20.62673 | -51.7081 | 2026-04-18 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eec75561-58d3-32ce-ab67-8094a227fa26 | -21.1932 | -48.60616 | 2026-04-18 04:25:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e40f3582-da0c-3248-80a5-774e5dc36997 | -24.94014 | -49.99555 | 2026-04-18 04:25:00 | NPP-375D | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9069b2d5-fd1d-3163-bc57-6e057b5bd2f5 | -23.26961 | -55.1893 | 2026-04-18 04:25:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 93c5748d-87c5-3c64-a16f-f1d8fac35c05 | -20.16124 | -46.71753 | 2026-04-18 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a23c68e-6b86-3a68-b25d-c0893ba368ba | -20.16397 | -46.72182 | 2026-04-18 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a1da6ee-5636-34f0-8343-c9e1ee0f84be | -21.20036 | -48.80746 | 2026-04-18 04:25:00 | NPP-375D | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 881d3c33-71d0-3396-b0cc-c459b1b1579a | -20.16671 | -46.7261 | 2026-04-18 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3d5088c-a415-368d-9906-b12148319dc0 | -19.9788 | -44.85553 | 2026-04-18 04:25:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fef4916-0088-3c65-bc97-1d9be96042d0 | -19.9754 | -44.85496 | 2026-04-18 04:25:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0164f96f-46ee-3f3b-a210-d9f845a638c1 | -20.15792 | -46.71694 | 2026-04-18 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbec0321-15bb-3ca1-a9bd-bd216dccbc8a | -23.64691 | -48.00477 | 2026-04-18 04:25:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09fee5da-49ee-3dd0-b45a-baae60509def | -20.62577 | -51.70624 | 2026-04-18 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fce5fef-fe45-39f9-8a56-7cba977d2a78 | -28.06256 | -48.67163 | 2026-04-18 04:27:00 | NPP-375D | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4cbb42d9-174e-3fe4-a2f8-73553b2e737a | -25.98737 | -51.70286 | 2026-04-18 04:27:00 | NPP-375D | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7951e522-f68c-324f-a1c7-0261ba626494 | -28.69342 | -50.17085 | 2026-04-18 04:27:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b0b11d39-b1f4-36df-aa7a-c3e142e03b2f | -3.79997 | -54.79591 | 2026-04-18 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78aae6d2-0e24-3c0d-b6ad-e309076596d9 | -12.24026 | -44.20538 | 2026-04-18 04:42:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2037a659-085d-39bd-97da-11cc6667d5a7 | -10.40305 | -44.93277 | 2026-04-18 04:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bb224f6-d6e6-36f0-be86-0b1c30afab48 | -10.40718 | -44.93337 | 2026-04-18 04:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddc663c5-b3e3-3bba-9d84-356424324e88 | -11.19073 | -43.56029 | 2026-04-18 04:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cfeaf14f-ebd0-3271-b244-e6f202a97474 | -12.24085 | -44.20087 | 2026-04-18 04:42:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2f11566-c818-3b4f-8834-25f4e304afe5 | -11.19008 | -43.56506 | 2026-04-18 04:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3126e811-ccbb-3c86-9119-1deb0811ee45 | -20.15956 | -46.71815 | 2026-04-18 04:44:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3885141-d293-38ec-ad89-c056e43c2a1b | -18.07459 | -52.78542 | 2026-04-18 04:44:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README3.md)
