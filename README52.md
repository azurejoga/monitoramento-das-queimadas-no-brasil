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
| c02cd602-ec62-3ad5-9107-1ffde0dcae8a | -18.73374 | -46.90936 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f046107-d0fb-3082-8750-f9db3aadb557 | -19.83044 | -45.89562 | 2025-08-26 04:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96d705b7-aafc-3f1e-9e34-4aeec5fca509 | -20.02343 | -45.554 | 2025-08-26 04:25:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4631440-b82a-3a73-9d85-2f102af2fae1 | -18.52833 | -46.28881 | 2025-08-26 04:25:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22addeaa-b15e-357e-8caa-eecee55bb4fd | -17.72506 | -50.73398 | 2025-08-26 04:25:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d63cabf-e87c-3775-a217-ef413324e538 | -21.19932 | -48.92878 | 2025-08-26 04:25:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c9678980-567b-3afb-a6f7-cd544fb84c09 | -18.3453 | -44.9584 | 2025-08-26 04:25:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47f94c6b-2991-3114-a5c3-73ce653763b4 | -17.3534 | -47.85589 | 2025-08-26 04:25:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d733071-a208-3224-a060-63d098a89f53 | -18.75388 | -45.36164 | 2025-08-26 04:25:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7f3e593-3889-3aa3-a8f7-35b17e7808fb | -18.37294 | -49.27018 | 2025-08-26 04:25:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc78a723-6969-37b8-bd07-cfe2d1705d58 | -20.38402 | -42.19398 | 2025-08-26 04:25:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 940c985c-1634-38f1-b966-9495145d6564 | -23.60107 | -49.00416 | 2025-08-26 04:25:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3d2ff81-22a0-3c1f-862b-b94d5840824e | -18.80762 | -47.60027 | 2025-08-26 04:25:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58643d9e-1622-3fad-909b-0923909a1df5 | -22.88449 | -46.37774 | 2025-08-26 04:25:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ad415f20-f329-38e2-af75-0c9cf9ecbe63 | -21.43213 | -45.47344 | 2025-08-26 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 66c45f7b-e197-343a-9a5f-4802adaee415 | -21.72508 | -46.8092 | 2025-08-26 04:25:00 | NPP-375D | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 822ddb2d-c9fb-36d9-9292-2282324b19e5 | -21.38648 | -45.49328 | 2025-08-26 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| c86807c6-2daf-329f-ad28-5e5265445c9d | -18.85369 | -47.00805 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94fb4c98-3fdd-3199-85a0-a43231067f00 | -17.68699 | -46.31546 | 2025-08-26 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 04296ead-6317-355e-92d9-5913c00c1214 | -19.92586 | -44.62065 | 2025-08-26 04:25:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d8d5e5de-4481-3ed6-ad23-630286d3dbe3 | -17.78459 | -44.48159 | 2025-08-26 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b58a6c47-6e09-39d5-befe-2d391e9a6592 | -19.18284 | -48.73084 | 2025-08-26 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0dd46d84-7899-3781-a648-bb9bbd633f4a | -20.38674 | -46.72171 | 2025-08-26 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b996ab0c-036d-3465-aa59-aacd829ceacc | -21.12339 | -45.87791 | 2025-08-26 04:25:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5acf89ac-1e31-3569-b3d7-4531f2103839 | -20.38731 | -46.71791 | 2025-08-26 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea98cbfc-bf59-33c0-b288-4c9e062d7724 | -18.85149 | -47.00018 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5aed308f-fb19-3702-8339-2fd4bc5dfb43 | -19.7455 | -45.28653 | 2025-08-26 04:25:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dba5856-1c7d-3e6e-8c34-f1dabaf7d81e | -23.3258 | -47.84454 | 2025-08-26 04:25:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c67be190-9b0a-33cc-98e8-d859811ac1d1 | -18.85313 | -47.01169 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d4cf336-708c-3852-8f90-8337c44bd437 | -21.0388 | -48.62623 | 2025-08-26 04:25:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e55728b6-caac-3550-810a-1b838c5d18c7 | -21.12396 | -45.87396 | 2025-08-26 04:25:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b6bb54da-a741-3994-a625-4608d93650ac | -20.88088 | -49.03385 | 2025-08-26 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 017fa0d1-1af0-31fe-bf5b-e9f240746a94 | -16.81009 | -51.90466 | 2025-08-26 04:25:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87045cfd-a2c6-307d-9257-41faa389ec2f | -22.89594 | -49.0582 | 2025-08-26 04:25:00 | NPP-375D | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 013698cd-1266-3d25-9d2a-ad10c2a88737 | -18.49197 | -46.79357 | 2025-08-26 04:25:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f34d5c91-7e2c-35b3-9611-f16931c00fa4 | -18.24463 | -51.26313 | 2025-08-26 04:25:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 346b00f6-2704-3ad2-820e-7f8d0be87488 | -21.57627 | -46.35981 | 2025-08-26 04:25:00 | NPP-375D | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3f65c860-255f-3bda-9147-0e33837de3c5 | -21.35154 | -43.75137 | 2025-08-26 04:25:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d3015a93-abd2-3e16-8b95-37c9f269bce8 | -21.72565 | -46.80542 | 2025-08-26 04:25:00 | NPP-375D | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a3bda568-b720-3ba4-9fc5-2f35a534da1e | -22.88507 | -46.37368 | 2025-08-26 04:25:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2e848ae1-9bca-30a6-91bc-c6ad1921fca1 | -18.84426 | -47.00269 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d242030b-bd49-3e65-9f20-8930100bdce9 | -18.8754 | -47.00048 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d10d4d1-4dcb-33ae-a37b-7239d4d7617f | -20.87753 | -49.03322 | 2025-08-26 04:25:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| cef3d235-d361-3c93-87fa-371415295505 | -22.54931 | -49.76848 | 2025-08-26 04:25:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d702263-dcff-3d66-abd4-2a790a53282a | -23.39569 | -51.19624 | 2025-08-26 04:25:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 4f536042-bf4b-37a8-ab0b-16f50019cc1e | -23.60168 | -49.00037 | 2025-08-26 04:25:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8975d16-0469-3ad9-b2ce-fbba056a6020 | -19.07815 | -48.15078 | 2025-08-26 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fab5e231-b475-37a4-bec7-b4ed93b50364 | -20.1906 | -44.58265 | 2025-08-26 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4eeb7069-43e0-3fad-ae08-66b505518030 | -21.428 | -45.47718 | 2025-08-26 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ce25b708-e8e4-3598-b1b7-aa0395401877 | -19.94919 | -44.71613 | 2025-08-26 04:25:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c85b6e24-8d13-3a40-b8ea-c91e83f57011 | -23.59834 | -48.99975 | 2025-08-26 04:25:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90d14a0c-1981-3822-a5be-e21b19abc3cb | -20.04634 | -44.47195 | 2025-08-26 04:25:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 737128aa-c244-3031-9b3b-4b13c64f3844 | -19.48748 | -46.12268 | 2025-08-26 04:25:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28ce56cc-fadd-3514-b6ff-c9b82c1666ed | -19.03254 | -46.91757 | 2025-08-26 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47a39d10-9bd5-3073-994b-e15a5585d51e | -17.65575 | -46.97221 | 2025-08-26 04:25:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aac67680-6256-34c6-aff3-21e07add5e8d | -20.98387 | -42.99476 | 2025-08-26 04:25:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 50dcc31e-1ade-360f-8450-4a72e1099763 | -6.2459 | -60.0174 | 2025-08-26 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 04dc0c84-db21-31a4-9390-2540b34e2ca3 | -9.006 | -65.4 | 2025-08-26 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 14d856c5-0df2-3bc8-bd5e-c5ecb0c8482c | -8.8364 | -62.4321 | 2025-08-26 04:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 6308afbf-f6ab-3af1-8c60-50d2c0ffad9d | -9.1904 | -59.5201 | 2025-08-26 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 73f5b52e-066d-3f9d-aab4-25b1cd1f2fec | -11.54 | -52.119 | 2025-08-26 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a320d994-048f-367a-96aa-289b282c9fef | -8.8734 | -62.4495 | 2025-08-26 04:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 4aaec891-baea-3149-a3a1-729cf86e6f8b | -6.8228 | -58.9753 | 2025-08-26 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| e30bb11e-5c73-320a-97d4-ebf93fb69d81 | -11.5207 | -52.142 | 2025-08-26 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 45732351-224f-3e77-b4fd-17d0df26ef3f | -9.153 | -59.5415 | 2025-08-26 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b86e92be-6c23-322c-a089-8e247505c39b | -11.5017 | -52.1439 | 2025-08-26 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 224db49a-2efc-3c06-95e0-f6e658addead | -9.1529 | -59.5609 | 2025-08-26 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| cdd8be1c-87e0-3779-adb8-dfac185bb81b | -7.3854 | -64.3475 | 2025-08-26 04:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d800c480-974e-3dc4-a342-3e0f182bd305 | -8.9874 | -65.4192 | 2025-08-26 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 6616eced-9ee3-3d6a-a1e9-45f347f4243a | -6.246 | -59.9982 | 2025-08-26 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c4a3d05d-7f62-3336-bbf2-e1bdfdc2de0f | -8.8363 | -62.451 | 2025-08-26 04:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f80da219-496e-38ef-8ddf-5230f4da5b5f | -6.8413 | -58.9552 | 2025-08-26 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| cc5ff934-7092-3c96-bc6a-28aa3678dc32 | -9.1717 | -59.5405 | 2025-08-26 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 33ee7320-469b-32b0-a970-d68082187c4e | -11.559 | -52.117 | 2025-08-26 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2867e94a-cd72-39ab-9b3f-7a598ee091f3 | -6.782 | -59.6519 | 2025-08-26 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 6ff5dbbb-b472-3cec-a6eb-c5ab692f2234 | -9.191 | -59.4425 | 2025-08-26 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 1fa41317-7498-3bf8-abb2-4a13be05bcba | -9.1718 | -59.5211 | 2025-08-26 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b74e09b7-c894-3b6d-b232-d1d2f029e5c6 | -11.521 | -52.1209 | 2025-08-26 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 119.6 |
| f52c66d2-b821-355d-b466-70909ffd7b1e | -11.1591 | -44.7395 | 2025-08-26 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 695dbb7c-9ffc-3375-a132-95d2ece3418d | -9.1724 | -59.4436 | 2025-08-26 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 805958a3-a710-372a-a5c0-6fc51f90a173 | -11.502 | -52.1229 | 2025-08-26 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 83313cc8-5eb5-3271-b6e6-f7585c4d5258 | -9.1903 | -59.5395 | 2025-08-26 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 6bc168df-fba0-35f1-ab62-85e2ed28ac42 | -6.7635 | -59.6718 | 2025-08-26 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 3ec39889-00ac-3e0c-8eeb-e33a5f3fdbfb | -8.855 | -62.4313 | 2025-08-26 04:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 354fe596-a672-3077-8c19-116441f9644e | -8.8548 | -62.4503 | 2025-08-26 04:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 14a319bc-b602-335a-8153-89475c17f5dc | -11.3126 | -55.1112 | 2025-08-26 04:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e55559c9-ae52-36a2-8468-01ffc9b5fe2d | -6.2275 | -60.018 | 2025-08-26 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 3a42238f-f165-39a5-880b-5bc877a21ef4 | -6.8043 | -58.9761 | 2025-08-26 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 2921c83b-6c5c-3dda-bdae-e898990c5ddc | -9.0231 | -65.7169 | 2025-08-26 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 155b2db1-a84d-3ecf-abe4-45fbca8a7e75 | -6.8044 | -58.9568 | 2025-08-26 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| b950f551-a8ba-3af6-97b7-afafcbdd8e2e | -6.7819 | -59.6711 | 2025-08-26 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 8d659c70-fd2a-3f26-b0ad-d1d3fae03b00 | -11.1587 | -44.7627 | 2025-08-26 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| d4d0ecfc-a78c-36b3-aca8-f25cb188414b | -6.8229 | -58.956 | 2025-08-26 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 6c0765d1-f5e5-378e-9ddd-2d09d9112c32 | -4.9606 | -55.8028 | 2025-08-26 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 95d9b2ad-3852-30ca-9592-d8676ad13532 | -8.9874 | -65.4192 | 2025-08-26 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| a82dfc24-86a6-3507-8c06-5a8292eea86f | -8.8734 | -62.4495 | 2025-08-26 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1fae9e33-0a49-3318-83b4-45129abaa1e9 | -9.153 | -59.5415 | 2025-08-26 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 78bb9430-8fbf-3d79-8e14-915788a80685 | -9.1724 | -59.4436 | 2025-08-26 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f51e3707-e392-347a-9d7a-3ee72a4799fb | -8.8548 | -62.4503 | 2025-08-26 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 53c8b629-1ab1-3565-8e1b-d607345520fd | -6.8044 | -58.9568 | 2025-08-26 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |


[Clique aqui para ver as próximas entradas](README53.md)
